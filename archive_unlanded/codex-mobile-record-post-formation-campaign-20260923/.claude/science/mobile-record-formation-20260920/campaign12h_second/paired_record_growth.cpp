// Supplied classical matching process. Continuous-time null-event sampling.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
struct Model {
 int N,V; vector<int> s; vector<array<int,6>> nb; vector<array<int,8>> cube;
 explicit Model(int n):N(n),V(n*n*n),s(V,-1),nb(V),cube(V){
  if(n<4||n%2)throw runtime_error("side must be even and >=4");
  for(int x=0;x<n;x++)for(int y=0;y<n;y++)for(int z=0;z<n;z++){
   int a=id(x,y,z);array<int,3> q{x,y,z};
   for(int j=0;j<3;j++)for(int sign=0;sign<2;sign++){auto p=q;p[j]+=sign?-1:1;nb[a][2*j+sign]=id(p[0],p[1],p[2]);}
   for(int b=0;b<8;b++)cube[a][b]=id(x+((b>>2)&1),y+((b>>1)&1),z+(b&1));
  }
 }
 int id(int x,int y,int z)const{return (((x%N+N)%N)*N+(y%N+N)%N)*N+(z%N+N)%N;}
 static int bit(int b,int j){return (b>>(2-j))&1;}
 bool siteok(int x)const{int d=s[x];return d<0||(d<6&&s[nb[x][d]]==(d^1));}
 bool valid()const{for(int x=0;x<V;x++)if(!siteok(x))return false;return true;}
 bool birth(int x,int axis,bool apply=true){
  int y=nb[x][2*axis];if(s[x]>=0||s[y]>=0)return false;
  if(apply){s[x]=2*axis;s[y]=2*axis+1;}return true;
 }
 bool translate(int x,int a,bool apply=true){
  if(s[x]<0)return false;
  int y=nb[x][s[x]],u=nb[x][a],v=nb[y][a];
  if((u!=x&&u!=y&&s[u]>=0)||(v!=x&&v!=y&&s[v]>=0))return false;
  if(apply){int dx=s[x],dy=s[y];s[x]=s[y]=-1;s[u]=dx;s[v]=dy;}return true;
 }
 bool parallel(int anchor,int axis,int mask,bool apply=true){
  array<int,8> old;for(int b=0;b<8;b++)old[b]=s[cube[anchor][b]];
  int channel=0;bool changed=false;
  for(int b=0;b<8;b++)if(!bit(b,axis)){
   int c=b|(1<<(2-axis));if(mask&(1<<channel)){changed|=old[b]!=old[c];swap(s[cube[anchor][b]],s[cube[anchor][c]]);}channel++;
  }
  bool accepted=changed;
  if(accepted)for(int b=0;b<8&&accepted;b++){
   int x=cube[anchor][b];if(!siteok(x)){accepted=false;break;}
   for(int d=0;d<6;d++)if(!siteok(nb[x][d])){accepted=false;break;}
  }
  if(!accepted||!apply)for(int b=0;b<8;b++)s[cube[anchor][b]]=old[b];
  return accepted;
 }
 bool fullcube(int anchor,int axis,bool apply=true){
  int p=(axis+1)%3,q=(axis+2)%3;
  auto aligned=[&](int face,int direction){
   for(int b=0;b<8;b++)if(bit(b,axis)==face&&s[cube[anchor][b]]!=2*direction+bit(b,direction))return false;
   return true;
  };
  if(!((aligned(0,p)&&aligned(1,q))||(aligned(0,q)&&aligned(1,p))))return false;
  return parallel(anchor,axis,15,apply);
 }
 void jam(){
  for(int x=0;x<N;x+=2)for(int y=0;y<N;y+=2)for(int z=0;z<N;z+=2){
   assert(birth(id(x+1,y,z),1));assert(birth(id(x,y+1,z),2));assert(birth(id(x,y,z+1),0));
  }
 }
 void read(const string& path){ifstream f(path);if(!f)throw runtime_error("cannot read state");for(auto &v:s)if(!(f>>v)||v< -1||v>5)throw runtime_error("invalid state word");int extra;if(f>>extra)throw runtime_error("extra state words");if(!valid())throw runtime_error("invalid reciprocal matching");}
 void save(const string& path){ofstream f(path);for(int i=0;i<V;i++)f<<s[i]<<(i+1==V?'\n':' ');}
 array<long long,4> enabled(){
  array<long long,4> out{};
  for(int x=0;x<V;x++){
   for(int d=0;d<3;d++)out[0]+=birth(x,d,false);
   for(int d=0;d<6;d++)out[1]+=translate(x,d,false); // Endpoint channels, each rate kappa/2.
   for(int d=0;d<3;d++){out[2]+=fullcube(x,d,false);for(int mask=1;mask<16;mask++)out[3]+=parallel(x,d,mask,false);}
  }return out;
 }
 array<double,5> structure(){
  array<double,5> out{};
  for(int m=1;m<=2;m++)for(int direction=0;direction<3;direction++){
   array<complex<double>,3> F{};
   for(int x=0;x<N;x++)for(int y=0;y<N;y++)for(int z=0;z<N;z++){
    int a=id(x,y,z);array<int,3> point{x,y,z};double sign=((x+y+z)%2)?-1.:1.;
    complex<double> phase=polar(1.,-2.*acos(-1.)*m*point[direction]/N);
    for(int j=0;j<3;j++)F[j]+=phase*sign*((s[a]==2*j?1.:0.)-1./6.);
   }
   double lon=norm(F[direction])/V,tot=0;for(auto f:F)tot+=norm(f)/V;
   out[2*(m-1)]+=(tot-lon)/6.;out[2*(m-1)+1]+=lon/3.;
  }
  array<double,3> zero{};
  for(int x=0;x<N;x++)for(int y=0;y<N;y++)for(int z=0;z<N;z++){
   int a=id(x,y,z);double sign=((x+y+z)%2)?-1.:1.;
   for(int j=0;j<3;j++)zero[j]+=sign*((s[a]==2*j?1.:0.)-1./6.);
  }
  for(auto a:zero)out[4]+=a*a/V;
  return out;
 }
 void enumerate(const string& path){
  ofstream out(path);if(!out)throw runtime_error("cannot open enumeration");auto original=s;
  auto record=[&](const char* family,int x,int a,int mask,bool yes){
   if(yes){if(!valid()||s==original)throw runtime_error("bad transition");out<<family<<' '<<x<<' '<<a<<' '<<mask<<' ';for(int v:s)out<<(v+1);out<<'\n';}s=original;
  };
  for(int x=0;x<V;x++){
   for(int a=0;a<3;a++)record("B",x,a,0,birth(x,a));
   for(int a=0;a<6;a++)record("T",x,a,0,translate(x,a));
   for(int a=0;a<3;a++){
    record("C",x,a,0,fullcube(x,a));
    for(int mask=1;mask<16;mask++)record("P",x,a,mask,parallel(x,a,mask));
   }
  }
 }
};
int main(int argc,char**argv){try{
 if(argc==5&&string(argv[1])=="--enumerate"){Model m(stoi(argv[2]));m.read(argv[3]);m.enumerate(argv[4]);return 0;}
 if(argc!=11)throw runtime_error("usage: binary N seed beta kappa nu mu t_max prefix init(empty|jam) snapshots");
 int N=stoi(argv[1]);uint64_t seed=stoull(argv[2]);double beta=stod(argv[3]),kappa=stod(argv[4]),nu=stod(argv[5]),mu=stod(argv[6]),limit=stod(argv[7]);string prefix=argv[8],init=argv[9];int snapshots=stoi(argv[10]);
 if(min({beta,kappa,nu,mu})<0||limit<=0||snapshots<2)throw runtime_error("invalid simulation parameters");
 Model model(N);if(init=="jam")model.jam();else if(init!="empty")throw runtime_error("unknown initial state");
 vector<int> born(model.V);int occupied=0;for(int x=0;x<model.V;x++)if(model.s[x]>=0){born[x]=1;occupied++;}
 int initial_occupied=occupied;double weight=3*beta+3*kappa+3*nu+45*mu;if(weight<=0)throw runtime_error("zero total attempt rate");
 mt19937_64 rng(seed);auto unit=[&](){return generate_canonical<double,53>(rng);};auto integer=[&](int n){return uniform_int_distribution<int>(0,n-1)(rng);};
 ofstream csv(prefix+".csv");if(!csv)throw runtime_error("cannot open output");csv<<setprecision(17);
 csv<<"time,occupied,vacancies,births,translations,cube_exchanges,parallel_swaps,attempts,reused_sites,max_site_births,nx,ny,nz,ST1,SL1,ST2,SL2,zero_mode_power\n";
 array<uint64_t,4> accepted{};uint64_t attempts=0;double t=0,first_full=-1;
 auto report=[&](double at){
  if(!model.valid())throw runtime_error("snapshot validity failed");
  int count=0,reused=0,maximum=0;array<int,3> orient{};
  for(int x=0;x<model.V;x++){if(model.s[x]>=0){count++;if(model.s[x]%2==0)orient[model.s[x]/2]++;}reused+=born[x]>1;maximum=max(maximum,born[x]);}
  if(count!=occupied||uint64_t(count)!=uint64_t(initial_occupied)+2*accepted[0])throw runtime_error("birth budget failed");
  auto S=model.structure();csv<<at<<','<<count<<','<<model.V-count;
  for(auto a:accepted)csv<<','<<a;csv<<','<<attempts<<','<<reused<<','<<maximum;
  for(auto a:orient)csv<<','<<a;for(auto a:S)csv<<','<<a;csv<<'\n';csv.flush();
 };
 vector<double> times{0};double first=min(0.01,limit/1000.);
 for(int i=0;i<snapshots;i++)times.push_back(first*exp(log(limit/first)*i/(snapshots-1.)));
 times.back()=limit;int next=0;
 while(t<limit){
  double proposed=t-log1p(-unit())/(model.V*weight);
  while(next<(int)times.size()&&times[next]<=proposed){report(times[next]);next++;}
  if(proposed>=limit)break;t=proposed;attempts++;
  double choose=unit()*weight;int x=integer(model.V);bool ok=false;
  if(choose<3*beta){int a=integer(3),y=model.nb[x][2*a];ok=model.birth(x,a);if(ok){occupied+=2;born[x]++;born[y]++;accepted[0]++;if(occupied==model.V&&first_full<0)first_full=t;}}
  else if(choose<3*beta+3*kappa){ok=model.translate(x,integer(6));accepted[1]+=ok;}
  else if(choose<3*beta+3*kappa+3*nu){ok=model.fullcube(x,integer(3));accepted[2]+=ok;}
  else {ok=model.parallel(x,integer(3),1+integer(15));accepted[3]+=ok;}
 }
 while(next<(int)times.size()){report(times[next]);next++;}
 model.save(prefix+".final.txt");auto enabled=model.enabled();
 ofstream meta(prefix+".json");meta<<setprecision(17)<<"{\"side\":"<<N<<",\"seed\":"<<seed<<",\"beta\":"<<beta<<",\"kappa\":"<<kappa<<",\"nu\":"<<nu<<",\"mu\":"<<mu<<",\"horizon\":"<<limit<<",\"initial\":\""<<init<<"\",\"first_full_time\":"<<first_full<<",\"occupied\":"<<occupied<<",\"attempts\":"<<attempts<<",\"accepted\":[";
 for(int i=0;i<4;i++)meta<<(i?",":"")<<accepted[i];meta<<"],\"enabled_channel_counts\":[";
 for(int i=0;i<4;i++)meta<<(i?",":"")<<enabled[i];meta<<"],\"translation_count_convention\":\"endpoint channels of rate kappa/2\"}\n";
 cout<<"N="<<N<<" seed="<<seed<<" init="<<init<<" occupied="<<occupied<<'/'<<model.V<<" first_full="<<first_full<<" attempts="<<attempts<<'\n';return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 1;}}
