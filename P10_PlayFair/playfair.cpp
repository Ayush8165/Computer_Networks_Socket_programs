#include<bits/stdc++.h>
using namespace std;

vector<vector<char>> genTable(string key)
{
    vector<vector<char>> arr(5, vector<char>(5,'_'));
    vector<int> vis(26,0);
    vis['j'-'a'] = 1;
    for(int i=0;i<key.size();i++)
    {   
        vis[key[i]-'a']=1;
        arr[i/5][i%5] = key[i];
    }

    int itr = key.size();
    char c = 'a';
    while(itr<25)
    {
        if(vis[c-'a']==0)
        {
        arr[itr/5][itr%5] = c;
        itr++;
        }
        c++;
    }

    return arr;
}
string cleanMsg(string msg)
{
    string res;
    vector<int> vis(26,0);
    for(auto i:msg)
    {   
        if(vis[i-'a'])
        continue;
        vis[i-'a']=1;
        res.push_back(i);
    }

    return res;
}



string cipher(string key, string msg)
{
    for(int i=0;i<key.size();i++)if(key[i]=='j')key[i]='i';

    key = cleanMsg(key);

    // generating table

    vector<vector<char>> arr = genTable(key);
    
// pairing now 
    vector<int> vis(26,0);
    vector<string> vs;

    int i = 0;
    int size = msg.size();
    while(i<size)
    {   
        if(i==size-1)
        {   
            string t ;
            t.push_back( msg[i]);
            t+="z";
            vs.push_back(t);
            i++;
        }
        else if(msg[i]==msg[i+1])
        {   
            string t ;
            t.push_back(msg[i]);
            t+="x";
            vs.push_back(t);
            i++;
        }
        else
        {   
            string t ;
            t.push_back(msg[i]);
            t.push_back(msg[i+1]);
            
            
            vs.push_back(t);
            i+=2;
        }

    }

    string res;
    for(auto it:vs){
        char c1 = it[0], c2 = it[1];
        pair<int,int> p1, p2; 
        for(int i=0;i<5;i++)
        {
            for(int j=0;j<5;j++)
            {
                if(arr[i][j]==c1)
                    p1={i,j};
                
                if(arr[i][j]==c2)
                    p2={i,j};
                                
            }
        }

        if(p1.first==p2.first)
        {   
            int x = p1.first;
            int y1 = (p1.second+1)%5, y2 = (p2.second+1)%5;
            res.push_back(arr[x][y1]);
            res.push_back(arr[x][y2]);

        }

        else if(p1.second==p2.second)
        {
            int y = p1.second;
            int x1 = (p1.first+1)%5, x2 = (p1.second+1)%5;
            res.push_back(arr[x1][y]);
            res.push_back(arr[x2][y]);
        }

        else 
        {
            int d = abs(p1.second-p2.second);
            if(p1.second<p2.second)
            {
                res.push_back(arr[p1.first][p1.second+d]);
                res.push_back(arr[p2.first][p2.second-d]);
            }
            else
            {
                res.push_back(arr[p1.first][p1.second-d]);
                res.push_back(arr[p2.first][p2.second+d]);

            }
        }
    }

    return res;

}

string decipher(string key, string msg)
{
    vector<vector<char>> arr = genTable(key);
    
    string res;
    for(int it=0;it<msg.size();it+=2)
    {
        char c1 = msg[it], c2 = msg[it+1];
        pair<int, int> p1, p2;
        for(int i=0;i<5;i++)
        {
            for(int j=0;j<5;j++)
            {
                if(arr[i][j]==c1)
                p1={i,j};
                if(arr[i][j]==c2)
                p2={i,j};
            }
        }

        if(p1.first==p2.first)
        {   
            int x = p1.first;
            int y1 = (p1.second-1+5)%5, y2 = (p2.second-1+5)%5;
            res.push_back(arr[x][y1]);
            res.push_back(arr[x][y2]);

        }

        else if(p1.second==p2.second)
        {
            int y = p1.second;
            int x1 = (p1.first-1+5)%5, x2 = (p1.second-1+5)%5;
            res.push_back(arr[x1][y]);
            res.push_back(arr[x2][y]);
        }

        else 
        {
            int d = abs(p1.second-p2.second);
            if(p1.second<p2.second)
            {
                res.push_back(arr[p1.first][p1.second+d]);
                res.push_back(arr[p2.first][p2.second-d]);
            }
            else
            {
                res.push_back(arr[p1.first][p1.second-d]);
                res.push_back(arr[p2.first][p2.second+d]);

            }
        }
        
    }
    return res;
}

int main()
{   
    string msg,key;
    cout<<"Enter msg :\t";
    cin>>msg;
    cout<<"Enter key :\t";
    cin>>key;
    string cipher_msg;
    cipher_msg = cipher(key, msg);
    cout<<"Encrypted MSG : "<<cipher_msg<<"\n";
    cout<<"Enter key for decryption : ";
    cin>>key;
    cout<<"UnEncrypted MSG : "<<decipher(key, cipher_msg)<<"\n";
}