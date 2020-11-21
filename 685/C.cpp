#include <iostream>
#include<map>
using namespace std;

int main()
{
   int t;
   cin>>t;
   while(t--)
   {
       int n,k;
       cin>>n>>k;
       string a,b;
       cin>>a;
       cin>>b;
       map<char,int> m1;
       map<char,int> m2;
       for (auto i:a) m1[i]+=1;
       for (auto i:b) m2[i]+=1;
       int ans = 0;
       for (char i='a' ;i<'z';i++)
       {
           if (m1[i]>m2[i])
           {
               int diff = m1[i]-m2[i];
               if (diff%k==0){
                   
               
                    m1[i+1]+=m1[i]-m2[i];
                    m1[i]=m2[i];
               }
                else
                    ans = 1;
           }
       }
       if (m1['z']>m2['z']) ans = 1;
    if (ans==0)
        cout<<"YES";
    else
        cout<<"NO";
   cout<<endl;
   }
   
   return 0;
}
