#include<bits/stdc++.h>
using namespace std;

map<char, string> mp;
map<string, char> mp2;

void builder()
{
    for(int i=0,l=0;i<26;i++)
    {   
        if(i==9 || i==21)
        {
            mp['a'+i]=mp['a'+i-1];
            
            continue;
        }
        string temp = "";
        int k = 5;
        
        int j = l;
        l++;
        while(k--)
        {
            j&1?temp+="b":temp+="a";
            j = (j>>1);
        }
        reverse(temp.begin(),temp.end());
        mp['a'+i]=temp;
        mp2[temp]=('a'+i);
    }

}

string encrypt(string msg)
{
    string res = "";
    for(auto i:msg)
    {
        if(i!=' ')
        {
            res+=mp[i];
        }
        else
        {
            res+=" ";
        }
    }
    cout<<res<<"\n";
    return res;
}

string decrypt(string msg)
{
    int n = msg.size();
    string res = "";
    
    for(int i=0;i<n;)
    {
        if(msg[i]==' ')
        {
            res+=" ";
            i++;
        }
        else
        {   
            res.push_back(mp2[msg.substr(i,5)]);
            i+=5;
        }
    }
    return res;
}

int main()
{   
    builder();
    cout<<"\n\n20BCS018 AYUSH CHAUHAN\n\n";
    
    string msg;
    cout<<"Enter orginal msg :\t";
    cin>>msg;
    
    string hidden_msg = encrypt(msg);
    cout<<"Cipher Text :\t"<<hidden_msg<<"\n";

    string clear_msg = decrypt(hidden_msg);
    cout<<"Deciphered Text :\t"<<clear_msg<<"\n";
}