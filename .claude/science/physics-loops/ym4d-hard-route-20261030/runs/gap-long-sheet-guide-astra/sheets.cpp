// GUIDE only. Reuses row 1101's guarded quaternion heat bath and RSS guard.
// New geometry: GH2_2, P4, and a periodic reduced face with trivial holonomy.
#define main old_sampler_main
#include "../gap-descent-mc-astra/su2_guarded.cpp"
#undef main
#include <unistd.h>
#include <algorithm>

struct Sheets {
 int L,V,n,T; std::string mode; double b,k; bool gauge;
 Lattice gen;
 std::vector<Q> p,a;
 std::vector<std::array<int,2>> up,dn;
 std::vector<std::array<int,4>> loops;
 std::vector<std::vector<std::pair<int,int>>> incidence;
 Sheets(std::string m,int l,int t,double B,double K,uint64_t seed,bool hot):
  L(l),V(l*l),n(m=="face"?2*t*t:m=="p4"?4:2),T(t),mode(m),b(B),k(K),
  gauge(m=="gh"&&K>=0),gen(3,0,0,0,false,seed,false),p(n*V),a(gauge?2*V:0),up(V),dn(V),incidence(n) {
  if(L<4||L%2||n<2||b<0||!std::isfinite(b)||!std::isfinite(k))throw std::runtime_error("bad geometry/coupling");
  if(mode=="face"&&T<3)throw std::runtime_error("face T must be >=3");
  if(mode!="face"&&mode!="p4"&&mode!="gh")throw std::runtime_error("bad model");
  for(int y=0;y<L;y++)for(int x=0;x<L;x++){int i=x+L*y;up[i]={(x+1)%L+L*y,x+L*((y+1)%L)};dn[i]={(x+L-1)%L+L*y,x+L*((y+L-1)%L)};}
  for(Q &q:p)q=hot?gen.haar():Q{1,0,0,0};
  for(Q &q:a)q=hot?gen.haar():Q{1,0,0,0};
  if(mode=="p4")loops.push_back({0,1,2,3});
  if(mode=="face")for(int y=0;y<T;y++)for(int x=0;x<T;x++){
   int s=x+T*y,s0=(x+1)%T+T*y,s1=x+T*((y+1)%T);
   loops.push_back({2*s,2*s0+1,2*s1,2*s+1});
  }
  for(int j=0;j<(int)loops.size();j++)for(int h=0;h<4;h++)incidence[loops[j][h]].push_back({j,h});
  memory_gate();
 }
 Q factor(int j,int h,int i)const {Q q=p[loops[j][h]*V+i];return h<2?q:dag(q);}
 double plaq(int j,int i)const {return mul(mul(mul(factor(j,0,i),factor(j,1,i)),factor(j,2,i)),factor(j,3,i))[0];}
 Q local(int f,int i)const {
  Q h{};
  for(int d=0;d<2;d++){
   Q v=p[f*V+up[i][d]],w=p[f*V+dn[i][d]];
   if(gauge){v=mul(a[d*V+i],v);w=mul(dag(a[d*V+dn[i][d]]),w);}
   h=add(h,add(v,w));
  }
  h=scale(h,b);
  if(mode!="gh"&&k!=0)for(auto [j,pos]:incidence[f]){
   Q r{1,0,0,0};for(int z=1;z<4;z++)r=mul(r,factor(j,(pos+z)%4,i));
   h=add(h,scale(pos<2?dag(r):r,k));
  }
  return h;
 }
 Q glocal(int d,int i)const {
  int e=1-d,im=up[i][d],y=dn[i][e];
  Q s=mul(mul(a[e*V+i],a[d*V+up[i][e]]),dag(a[e*V+im]));
  Q t=mul(mul(dag(a[e*V+y]),a[d*V+y]),a[e*V+up[y][d]]);
  Q h=scale(add(s,t),k);
  for(int f=0;f<n;f++)h=add(h,scale(mul(p[f*V+i],dag(p[f*V+im])),b));
  return h;
 }
 void update(Q &q,Q h,bool over){double z=sqrt(dot(h,h));if(z<1e-14){if(!over)q=gen.haar();return;}h=scale(h,1/z);q=over?unit(add(scale(h,2*dot(q,h)),scale(q,-1))):mul(gen.hb(z),h);}
 void sweep(bool over){
  for(int f=0;f<n;f++)for(int i=0;i<V;i++)update(p[f*V+i],local(f,i),over);
  if(gauge)for(int d=0;d<2;d++)for(int i=0;i<V;i++)update(a[d*V+i],glocal(d,i),over);
 }
 void cycle(){sweep(false);for(int j=0;j<4;j++)sweep(true);}
 double gp(int i)const {return mul(mul(mul(a[i],a[V+up[i][0]]),dag(a[up[i][1]])),dag(a[V+i]))[0];}
 double action()const {
  double s=0;for(int f=0;f<n;f++)for(int i=0;i<V;i++)for(int d=0;d<2;d++){
   Q v=p[f*V+up[i][d]];if(gauge)v=mul(a[d*V+i],v);s+=b*dot(p[f*V+i],v);
  }
  if(gauge)for(int i=0;i<V;i++)s+=k*gp(i);
  if(mode!="gh")for(int j=0;j<(int)loops.size();j++)for(int i=0;i<V;i++)s+=k*plaq(j,i);
  return s;
 }
 // Slice channels E1,E4,E8,E16,plaquette; two longitudinal axes.
 // An Er joins sites r apart perpendicular to the measured separation.
 std::vector<float> measure(){
  std::vector<double> w(10*L);int lens[4]={1,4,8,16};
  for(int axis=0;axis<2;axis++){
   int d=1-axis;
   for(int f=0;f<n;f++)for(int i=0;i<V;i++){
    int t=axis==0?i%L:i/L;Q q=p[f*V+i];
    if(!gauge){for(int c=0;c<4;c++){
     int r=lens[c],j=d==0?(i/L)*L+(i%L+r)%L:i%L+L*((i/L+r)%L);
     w[(axis*5+c)*L+t]+=dot(q,p[f*V+j])/(n*L);
    }}else{
     Q u{1,0,0,0};int j=i,c=0;
     for(int r=1;r<=16;r++){u=mul(u,a[d*V+j]);j=up[j][d];if(r==lens[c]){w[(axis*5+c)*L+t]+=dot(q,mul(u,p[f*V+j]))/(n*L);if(++c==4)break;}}
    }
   }
   for(int i=0;i<V;i++){int t=axis==0?i%L:i/L;
    if(gauge)w[(axis*5+4)*L+t]+=gp(i)/L;
    else if(mode=="gh")w[(axis*5+4)*L+t]+=1./L;
    else for(int j=0;j<(int)loops.size();j++)w[(axis*5+4)*L+t]+=plaq(j,i)/(loops.size()*L);
   }
  }
  return std::vector<float>(w.begin(),w.end());
 }
 std::array<double,3> spin_stats()const {
  double en=0,c0=0,c1=0;std::vector<double> co(L),si(L);
  for(int i=0;i<L;i++){co[i]=cos(6.283185307179586*i/L);si[i]=sin(6.283185307179586*i/L);}
  for(int f=0;f<n;f++){
   Q s{},cx{},sx{},cy{},sy{};
   for(int i=0;i<V;i++){int x=i%L,y=i/L;Q q=p[f*V+i];s=add(s,q);cx=add(cx,scale(q,co[x]));sx=add(sx,scale(q,si[x]));cy=add(cy,scale(q,co[y]));sy=add(sy,scale(q,si[y]));
    for(int d=0;d<2;d++){Q v=p[f*V+up[i][d]];if(gauge)v=mul(a[d*V+i],v);en+=dot(q,v);}
   }
   c0+=dot(s,s)/V;c1+=(dot(cx,cx)+dot(sx,sx)+dot(cy,cy)+dot(sy,sy))/(2*V);
  }
  return {en/(2*n*V),c0/n,c1/n};
 }
};

void controls(){
 double worst=0,overerr=0,normerr=0;
 for(std::string mode:{"gh","p4","face"}){
  Sheets s(mode,6,4,2.4,1.2,4817,true);
  for(int rep=0;rep<30;rep++){
   int f=rep%s.n,i=(rep*11)%s.V;Q old=s.p[f*s.V+i],fresh=s.gen.haar(),h=s.local(f,i);
   double before=s.action();s.p[f*s.V+i]=fresh;
   worst=std::max(worst,std::abs((s.action()-before)-dot(add(fresh,scale(old,-1)),h)));
   if(s.gauge){int d=rep%2;old=s.a[d*s.V+i];fresh=s.gen.haar();h=s.glocal(d,i);before=s.action();s.a[d*s.V+i]=fresh;worst=std::max(worst,std::abs((s.action()-before)-dot(add(fresh,scale(old,-1)),h)));}
  }
  double before=s.action();s.sweep(true);overerr=std::max(overerr,std::abs(s.action()-before));
  for(auto q:s.p)normerr=std::max(normerr,std::abs(dot(q,q)-1));
 }
 std::cout<<std::setprecision(17)<<"local_action_error "<<worst<<" overrelax_action_error "<<overerr<<" norm_error "<<normerr<<"\n";
 if(worst>1e-8||overerr>1e-8||normerr>1e-12)throw std::runtime_error("implementation control FAILS");
}
int main(int argc,char**argv){try{
 if(argc==2&&std::string(argv[1])=="control"){controls();return 0;}
 if(argc!=12){std::cerr<<"model L T beta coupling(-1=gh_infinity) seed hot burn samples stride outprefix\n";return 2;}
 int L=std::stoi(argv[2]),T=std::stoi(argv[3]),burn=std::stoi(argv[8]),N=std::stoi(argv[9]),stride=std::stoi(argv[10]);
 if(burn<0||N<1||stride<1)throw std::runtime_error("bad counts");
 Sheets s(argv[1],L,T,std::stod(argv[4]),std::stod(argv[5]),std::stoull(argv[6]),std::stoi(argv[7]));
 std::string path=argv[11];std::ofstream raw(path+".f32",std::ios::binary),stats(path+".csv"),therm(path+".therm.csv");
 if(!raw||!stats||!therm)throw std::runtime_error("record open");
 stats<<std::setprecision(17)<<"energy,chi0,chi1\n";therm<<std::setprecision(17)<<"cycle,energy,chi0,chi1\n";
 auto start=std::chrono::steady_clock::now();std::cout<<"pid "<<getpid()<<" nice "<<getpriority(PRIO_PROCESS,0)<<" spins "<<s.p.size()<<"\n"<<std::flush;
 for(int j=0;j<burn;j++){s.cycle();if(j%32==0){memory_gate();auto st=s.spin_stats();therm<<j<<","<<st[0]<<","<<st[1]<<","<<st[2]<<"\n";therm.flush();}}
 for(int j=0;j<N;j++){
  for(int z=0;z<stride;z++)s.cycle();auto w=s.measure();auto st=s.spin_stats();raw.write(reinterpret_cast<char*>(w.data()),w.size()*sizeof(float));stats<<st[0]<<","<<st[1]<<","<<st[2]<<"\n";
  if(!raw||!stats)throw std::runtime_error("record write");
  if(j%32==0){memory_gate();raw.flush();stats.flush();}
  if((j+1)%128==0)std::cout<<"sample "<<j+1<<" elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n"<<std::flush;
 }
 raw.flush();stats.flush();therm.flush();if(!raw||!stats||!therm)throw std::runtime_error("record flush");
 std::ofstream cfg(path+".cfg",std::ios::binary);if(!cfg)throw std::runtime_error("configuration open");cfg.write(reinterpret_cast<char*>(s.p.data()),s.p.size()*sizeof(Q));cfg.write(reinterpret_cast<char*>(s.a.data()),s.a.size()*sizeof(Q));cfg.flush();if(!cfg)throw std::runtime_error("configuration write");
 memory_gate();rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<"done elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<" peak_rss "<<usage.ru_maxrss<<"\n";
 return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
