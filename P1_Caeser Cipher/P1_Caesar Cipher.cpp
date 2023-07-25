#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg, int key)
{
    string res = "";
    
    for(auto &i:msg)
    {   
        res += (((i-'a'+key)%26)+'a');
    }
    return res;
}

string decrypt(string msg, int key)
{
    string res = "";

    for(auto &i:msg)
    {   
        res += ('a'+((i-'a'-key+26)%26));
    }
    return res;
}

int main()
{
    string msg;
    cout<<"\n\n20BCS018 AYUSH CHAUHAN\n\n";
    cout<<"Enter orginal msg :\t";
    cin>>msg;
    int key1;
    cout<<"Enter Key to Cipher :\t";
    cin>>key1;
    string hidden_msg = encrypt(msg, key1);
    cout<<"Cipher Text :\t"<<hidden_msg<<"\n";

    cout<<"Enter Key to Decipher :\t";
    int key2;
    cin>>key2;
    string clear_msg = decrypt(hidden_msg, key2);
    cout<<"Deciphered Text :\t"<<clear_msg<<"\n";
}