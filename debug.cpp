#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <ctime>
#include <unordered_map>
#include <chrono>
#include <algorithm>
#include "debug.h"
#include "ograph.h"


using namespace std;


void fastatodot(const char * name,const char * namout)
{
	ifstream in(name);
	ofstream out(namout);
	string data;
	while(!in.eof())
	{
		getline(in,data);
		transform(data.begin(), data.end(), data.begin(), ::tolower);
		if(data!="")
			out<<data<<";"<<endl;
	}
}



void createinputlm(int64_t lr,int k,const char *name)
{
	ofstream out(name,ios::trunc);
	int r;
	string c;
	string kmer(k,'a');
	for(int b(0);b<k;b++)
	{
		r=rand()%4;
		switch(r)
		{
			case 1:
			{
				kmer[b]='a';
				break;
			}
			case 2:
			{
				kmer[b]='c';
				break;
			}
			case 3:
			{
				kmer[b]='g';
				break;
			}
			case 0:
			{
				kmer[b]='t';
				break;
			}
		}
	}
	for(int64_t b(0);b<lr;b++)
	{
		kmer=kmer.substr(1,k-1);
		r=rand()%4;
		switch(r)
		{
			case 1:
			{
				c='a';
				break;
			}
			case 2:
			{
				c='c';
				break;
			}
			case 3:
			{
				c='g';
				break;
			}
			case 0:
			{
				c='t';
				break;
			}
		}
		kmer+=c;
		out<<kmer<<";"<<endl;
	}
}


bool checkfile(string name1, string name2)
{
	int fail(0);
	ifstream t1(name1), t2(name2);
	string line;
	unordered_map<string,bool> s1,s2;
	while(!t1.eof())
	{
		getline(t1,line);
		if(line.size()>2)
		s1.insert(make_pair(line,false));
	}
	while(!t2.eof())
	{
		getline(t2,line);
		if(line.size()>2)
			s2.insert(make_pair(line,false));
	}
	for(auto it=s1.begin(); it!=s1.end(); it++)
	{
			string str=it->first;
			auto smt=s2.find(str);
			if(smt==s2.end())
				fail++;
			else
				smt->second=true;
	}
	for(auto it=s2.begin(); it!=s2.end(); it++)
		if(!it->second)
		{
			string str=it->first;
			fail++;
		}
	cout<<"Errors:"<<fail<<endl;
	return(fail==0);
}
