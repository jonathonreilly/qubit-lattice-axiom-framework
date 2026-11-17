// Guarded successor, NOT used for the recorded grid. su2.cpp is the frozen production source.
// GUIDE only. Wilson SU(2), quaternion convention e_i e_j=-delta_ij+eps_ijk e_k.
// Creutz heat bath; Kennedy-Pendleton gamma rejection for alpha>=1.
// Microcanonical over-relaxation is reflection about the weighted staple.
#include <array>
#include <vector>
#include <random>
#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <string>
#include <stdexcept>
#include <sys/resource.h>
using Q=std::array<double,4>;
Q add(Q a,Q b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}
Q scale(Q a,double s){for(double &x:a)x*=s;return a;}
double dot(Q a,Q b){double z=0;for(int i=0;i<4;i++)z+=a[i]*b[i];return z;}
Q dag(Q a){for(int i=1;i<4;i++)a[i]=-a[i];return a;}
Q mul(Q a,Q b){return {a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],a[0]*b[2]+a[2]*b[0]+a[3]*b[1]-a[1]*b[3],a[0]*b[3]+a[3]*b[0]+a[1]*b[2]-a[2]*b[1]};}
Q unit(Q a){double n=sqrt(dot(a,a));if(n<1e-100) return {1,0,0,0}; return scale(a,1/n);}
struct Lattice {
 int L,V; bool face; double B[4][4]{};
 std::vector<Q> U; std::vector<std::array<int,4>> up,dn,coord;
 std::mt19937_64 rng; std::uniform_real_distribution<double> ur{0,1};
 double rnd(){return std::max(ur(rng),1e-300);}
 Q haar(){std::normal_distribution<double> n(0,1);return unit({n(rng),n(rng),n(rng),n(rng)});}
 Lattice(int l,double bl,double bm,double bt,bool f,uint64_t seed,bool hot):L(l),V(l*l*l*l),face(f),U(4*V),up(V),dn(V),coord(V),rng(seed){
  int st[4]={1,L,L*L,L*L*L};
  for(int mu=0;mu<4;mu++)for(int nu=mu+1;nu<4;nu++)B[mu][nu]=B[nu][mu]=(mu==0&&nu==1)?bl:(mu==2&&nu==3)?bt:bm;
  for(int x=0;x<V;x++){for(int d=0;d<4;d++){int c=(x/st[d])%L;coord[x][d]=c;up[x][d]=x+(c==L-1?-(L-1):1)*st[d];dn[x][d]=x+(c==0?L-1:-1)*st[d];U[4*x+d]=(hot&&(!face||d>=2))?haar():Q{1,0,0,0};}}
 }
 Q staple(const std::vector<Q>& A,int x,int mu,int excluded=-1,bool weighted=true){
  Q h{};int xm=up[x][mu];
  for(int nu=0;nu<4;nu++)if(nu!=mu&&nu!=excluded){
   int y=dn[x][nu];
   Q a=mul(mul(A[4*x+nu],A[4*up[x][nu]+mu]),dag(A[4*xm+nu]));
   Q b=mul(mul(dag(A[4*y+nu]),A[4*y+mu]),A[4*up[y][mu]+nu]);
   h=add(h,scale(add(a,b),weighted?B[mu][nu]:1.));
  }return h;
 }
 Q hb(double a){
  if(a<1e-10)return haar();
  double r0;
  if(a>=1){double x;
   // Rejection uses a single squared uniform, not a product of uniforms.
   for(;;){double c=cos(6.283185307179586*rnd());x=-(log(rnd())+c*c*log(rnd()))/a;double r=rnd();if(x<=2&&r*r<=1-x/2)break;}
   r0=1-x;
  }else{for(;;){r0=1+log(exp(-2*a)+(1-exp(-2*a))*rnd())/a;double r=rnd();if(r*r<=1-r0*r0)break;}}
  double z=2*rnd()-1,phi=6.283185307179586*rnd(),r=sqrt(std::max(0.,1-r0*r0)),s=sqrt(1-z*z);
  return {r0,r*s*cos(phi),r*s*sin(phi),r*z};
 }
 void sweep(bool over){
  for(int mu=face?2:0;mu<4;mu++)for(int x=0;x<V;x++){
   Q h=staple(U,x,mu);double a=sqrt(dot(h,h));
   if(a<1e-14){if(!over)U[4*x+mu]=haar();continue;}h=scale(h,1/a);
   U[4*x+mu]=over?unit(add(scale(h,2*dot(U[4*x+mu],h)),scale(U[4*x+mu],-1))):mul(hb(a),h);
  }
 }
 void cycle(int ors){sweep(false);for(int i=0;i<ors;i++)sweep(true);}
 Q loop(const std::vector<Q>& A,int x,int mu,int nu,int r=1,int s=1){
  Q q{1,0,0,0};int y=x;
  for(int k=0;k<r;k++){q=mul(q,A[4*y+mu]);y=up[y][mu];}
  for(int k=0;k<s;k++){q=mul(q,A[4*y+nu]);y=up[y][nu];}
  for(int k=0;k<r;k++){y=dn[y][mu];q=mul(q,dag(A[4*y+mu]));}
  for(int k=0;k<s;k++){y=dn[y][nu];q=mul(q,dag(A[4*y+nu]));}return q;
 }
 double action(){double a=0;for(int x=0;x<V;x++)for(int m=0;m<4;m++)for(int n=m+1;n<4;n++)a+=B[m][n]*loop(U,x,m,n)[0];return a;}
 void smear(std::vector<Q>& A,int axis){auto out=A;for(int mu=0;mu<4;mu++)if(mu!=axis&&(!face||mu>=2))for(int x=0;x<V;x++)out[4*x+mu]=unit(add(scale(A[4*x+mu],.5),scale(staple(A,x,mu,axis,false),.125)));A.swap(out);}
 std::vector<float> measure(){
  // layout: axis(0,2), smearing(0,8), plane(01,02,03,12,13,23), shape(P,R), slice
  std::vector<float> out;out.reserve(48*L+24);
  for(int axis:{0,2}){auto A=U;for(int sm=0;sm<2;sm++){
   if(sm)for(int step=0;step<8;step++)smear(A,axis);
   for(int mu=0;mu<4;mu++)for(int nu=mu+1;nu<4;nu++){
    std::vector<double> p(L),r(L);
    for(int x=0;x<V;x++) {int t=coord[x][axis];p[t]+=loop(A,x,mu,nu)[0];
     if(mu==axis)r[t]+=loop(A,x,mu,nu,1,2)[0];
     else if(nu==axis)r[t]+=loop(A,x,mu,nu,2,1)[0];
     else r[t]+=.5*(loop(A,x,mu,nu,1,2)[0]+loop(A,x,mu,nu,2,1)[0]);}
    for(auto &v:{p,r})for(double z:v)out.push_back(float(z/(V/L)));
   }
  }}
  // Unsmoothed loop means for Creutz ratios; six planes, 11,12,21,22.
  for(int m=0;m<4;m++)for(int n=m+1;n<4;n++)for(auto rs:{std::pair<int,int>{1,1},{1,2},{2,1},{2,2}}){double z=0;for(int x=0;x<V;x++)z+=loop(U,x,m,n,rs.first,rs.second)[0];out.push_back(float(z/V));}
  // Winding loops: axis(0,2), winding direction !=axis, slice. Eight spatial APE steps.
  for(int axis:{0,2}){auto A=U;for(int step=0;step<8;step++)smear(A,axis);for(int mu=0;mu<4;mu++)if(mu!=axis){std::vector<double> p(L);for(int x=0;x<V;x++)if(coord[x][mu]==0){Q q{1,0,0,0};int y=x;for(int k=0;k<L;k++){q=mul(q,A[4*y+mu]);y=up[y][mu];}p[coord[x][axis]]+=q[0];}for(double z:p)out.push_back(float(z/(L*L)));}}
  return out;
 }
 std::vector<float> anchor_corr(){ // spin two-point function, averaged over all sheets and both longitudinal directions
  std::vector<float> o;for(int r=0;r<=L/2;r++){double z=0;for(int x=0;x<V;x++)for(int mu=2;mu<4;mu++)for(int a=0;a<2;a++){int y=x;for(int k=0;k<r;k++)y=up[y][a];z+=dot(U[4*x+mu],U[4*y+mu]);}o.push_back(float(z/(4*V)));}return o;
 }
};
void memory_gate(){rusage r{};getrusage(RUSAGE_SELF,&r);
#ifdef __APPLE__
 double bytes=r.ru_maxrss;
#else
 double bytes=1024.*r.ru_maxrss;
#endif
 if(bytes>2.e9)throw std::runtime_error("2 GB RSS stop");}
int main(int argc,char**argv){try{
 if(argc!=12){std::cerr<<"L beta_L beta_M beta_T face seed hot burn n stride outprefix\n";return 2;}
 int L=std::stoi(argv[1]),face=std::stoi(argv[5]),burn=std::stoi(argv[8]),N=std::stoi(argv[9]),stride=std::stoi(argv[10]);
 Lattice lat(L,std::stod(argv[2]),std::stod(argv[3]),std::stod(argv[4]),face,std::stoull(argv[6]),std::stoi(argv[7]));
 std::string path=argv[11];std::ofstream raw(path+".f32",std::ios::binary),therm(path+".therm.csv");if(!raw||!therm)throw std::runtime_error("output open failed");
 bool save_spin=face&&std::stod(argv[4])==0;
 std::ofstream spin;if(save_spin){spin.open(path+".spin.f32",std::ios::binary);if(!spin)throw std::runtime_error("spin output open failed");}
 auto start=std::chrono::steady_clock::now();therm<<"cycle,action_per_site\n";
 for(int i=0;i<burn;i++){lat.cycle(1);if(i%32==0){memory_gate();therm<<i<<","<<std::setprecision(16)<<lat.action()/lat.V<<"\n";}}
 for(int i=0;i<N;i++){for(int j=0;j<stride;j++)lat.cycle(1);auto o=lat.measure();raw.write(reinterpret_cast<char*>(o.data()),o.size()*sizeof(float));if(!raw)throw std::runtime_error("raw output write failed");if(save_spin){auto s=lat.anchor_corr();spin.write(reinterpret_cast<char*>(s.data()),s.size()*sizeof(float));if(!spin)throw std::runtime_error("spin output write failed");}if(i%32==0){raw.flush();memory_gate();}if((i+1)%128==0)std::cout<<"sample "<<i+1<<" elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n"<<std::flush;}
 raw.flush();therm.flush();if(save_spin)spin.flush();
 if(!raw.good()||!therm.good()||(save_spin&&!spin.good()))throw std::runtime_error("record output flush failed");
 std::ofstream cfg(path+".cfg",std::ios::binary);if(!cfg)throw std::runtime_error("configuration open failed");cfg.write(reinterpret_cast<char*>(lat.U.data()),lat.U.size()*sizeof(Q));cfg.flush();if(!cfg)throw std::runtime_error("configuration write failed");
 std::cout<<"done elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
 return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
