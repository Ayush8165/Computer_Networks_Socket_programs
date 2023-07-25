#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg, string key)
{
    int c = key.size();
    int r = (msg.size()/c) + (msg.size()%c?1:0) ;
    
    vector<vector<char>> mat(r, vector<char> (c,' '));
    int i=0;
    for(auto &k:msg)
    {
        mat[i/c][i%c] = k;
        i++;
    }

    string res = "";
    for(int j=0;j<mat[0].size();j++)
    {
        for(int i=0;i<mat.size();i++)
        res+=mat[i][j];
    }
    return res;

}

string decrypt(string msg, string key)
{
    int r = key.size();
    int c = (msg.size()/r) + (msg.size()%r?1:0) ;
    
    vector<vector<char>> mat(r, vector<char> (c,'_'));
    int i=0;
    for(auto &k:msg)
    {
        mat[i/c][i%c] = k;
        i++;
    }

    string res = "";
    for(int j=0;j<mat[0].size();j++)
    {
        for(int i=0;i<mat.size();i++)
        res+=mat[i][j];
    }
    return res;
}

int main()
{
    string msg;
    cout<<"\n\n20BCS018 AYUSH CHAUHAN\n\n";
    cout<<"Enter orginal msg :\t";
    cin>>msg;
    string key1;
    cout<<"Enter Key to Cipher :\t";
    cin>>key1;
    string hidden_msg = encrypt(msg, key1);
    cout<<"Cipher Text :\t"<<hidden_msg<<"\n";

    cout<<"Enter Key to Decipher :\t";
    string key2;
    cin>>key2;
    string clear_msg = decrypt(hidden_msg, key2);
    cout<<"Deciphered Text :\t"<<clear_msg<<"\n";
}