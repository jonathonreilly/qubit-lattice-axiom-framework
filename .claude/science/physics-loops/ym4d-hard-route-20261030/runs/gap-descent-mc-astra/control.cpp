#define main sampler_main
#include "su2.cpp"
#undef main
int main(){
 std::cout<<std::setprecision(16);
 Lattice l(4,3.7,2.4,.8,false,1234,true);
 for(double a:{0.,.1,.9,1.,2.,10.,100.}){double s=0,s2=0;int n=200000;for(int i=0;i<n;i++){auto q=l.hb(a);s+=q[0];s2+=q[0]*q[0];}std::cout<<"hb "<<a<<" "<<s/n<<" "<<sqrt((s2/n-s*s/n/n)/n)<<"\n";}
 double e0=l.action();l.sweep(true);std::cout<<"or_action_error "<<l.action()-e0<<"\n";
 int x=17,mu=2;Q old=l.U[4*x+mu],fresh=l.haar(),h=l.staple(l.U,x,mu);double a=l.action();l.U[4*x+mu]=fresh;
 std::cout<<"local_action_error "<<l.action()-a-dot(fresh,h)+dot(old,h)<<"\n";
 std::vector<Q> g(l.V);for(auto &q:g)q=l.haar();a=l.action();
 auto before=l.measure();for(int y=0;y<l.V;y++)for(int d=0;d<4;d++)l.U[4*y+d]=mul(mul(g[y],l.U[4*y+d]),dag(g[l.up[y][d]]));
 auto after=l.measure();double err=0;for(size_t i=0;i<before.size();i++)err=std::max(err,std::abs(double(before[i])-after[i]));
 std::cout<<"gauge_action_error "<<l.action()-a<<"\ngauge_smeared_measurement_error "<<err<<"\n";
 Lattice f(4,0,2.4,.8,true,555,true);double direct=0;
 for(int y=0;y<f.V;y++){for(int m=2;m<4;m++)for(int d=0;d<2;d++)direct+=2.4*dot(f.U[4*y+m],f.U[4*f.up[y][d]+m]);direct+=.8*f.loop(f.U,y,2,3)[0];}
 std::cout<<"face_reduction_error "<<f.action()-direct<<"\n";
 double normerr=0;for(int i=0;i<4;i++)f.cycle(1);for(auto q:f.U)normerr=std::max(normerr,std::abs(dot(q,q)-1));
 std::cout<<"unitarity_error "<<normerr<<"\n";
 memory_gate();
}
