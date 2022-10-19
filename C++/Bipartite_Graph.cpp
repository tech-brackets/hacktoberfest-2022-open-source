#include<bits/stdc++.h>
using namespace std;

bool bft(vector<vector<int>> g,int n)
{
    int v[n];
    for(int i=0;i<n;i++){v[i]=-1;}
    queue<int> q;
    q.push(0);
    v[0]=1;
    while(!q.empty())
    {
        int k=q.front();
        q.pop();
        if(g[k][k]==1){return false;}
        for(int i=0;i<n;i++)
        {
            if(g[k][i] && v[i]==-1)
            {
                v[i]=1-v[k];
                q.push(i);
            }
            else if(g[k][i] && v[k]==v[i])
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    int n;
    cin>>n;
    int e;
    cin>>e;

    vector<vector<int>> g(n);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            g[i].push_back(0);
        }
    }
    int u,v;
    for(int i=0;i<e;i++)
    {
        cin>>u>>v;
        g[u][v]=1;
        g[v][u]=1;
    }
  cout<<bft(g,n)<<endl;
}


