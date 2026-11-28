// Supplemental beta_T=0 single-sheet controls, including published 128^2 size.
// Separate spin geometry, shared SU(2) radial sampler: limited independence.
#define main sampler_main
#include "su2.cpp"
#undef main
int main(int argc,char**argv){try{
 if(argc!=8){std::cerr<<"L beta seed hot burn samples output\n";return 2;}
 int L=std::stoi(argv[1]),V=L*L,burn=std::stoi(argv[5]),N=std::stoi(argv[6]);double beta=std::stod(argv[2]);
 Lattice gen(3,0,0,0,false,std::stoull(argv[3]),false);bool hot=std::stoi(argv[4]);
 std::vector<Q> u(V);std::vector<std::array<int,4>> near(V);
 for(int y=0;y<L;y++)for(int x=0;x<L;x++){int i=x+L*y;u[i]=hot?gen.haar():Q{1,0,0,0};near[i]={(x+1)%L+L*y,(x+L-1)%L+L*y,x+L*((y+1)%L),x+L*((y+L-1)%L)};}
 std::vector<double> co(L),si(L);for(int x=0;x<L;x++){co[x]=cos(6.283185307179586*x/L);si[x]=sin(6.283185307179586*x/L);}
 auto cycle=[&](){for(int over=0;over<5;over++)for(int i=0;i<V;i++){Q h{};for(int j:near[i])h=add(h,u[j]);double norm=sqrt(dot(h,h));if(norm<1e-14){if(!over)u[i]=gen.haar();continue;}h=scale(h,1/norm);u[i]=over?unit(add(scale(h,2*dot(u[i],h)),scale(u[i],-1))):mul(gen.hb(beta*norm),h);}};
 std::ofstream out(argv[7]);if(!out)throw std::runtime_error("output open");out<<std::setprecision(16)<<"energy,chi0,chi1";for(int t=0;t<=L/2;t++)out<<",wall"<<t;if(L<=12)for(int t=0;t<=L/2;t++)out<<",point"<<t;out<<"\n";
 auto start=std::chrono::steady_clock::now();
 for(int i=0;i<burn;i++){cycle();if(i%64==0)memory_gate();}
 for(int k=0;k<N;k++){
  cycle();cycle();std::vector<Q> wx(L),wy(L);Q total{},cx{},sx{},cy{},sy{};double en=0;
  for(int y=0;y<L;y++)for(int x=0;x<L;x++){int i=x+L*y;auto q=u[i];total=add(total,q);wx[x]=add(wx[x],q);wy[y]=add(wy[y],q);cx=add(cx,scale(q,co[x]));sx=add(sx,scale(q,si[x]));cy=add(cy,scale(q,co[y]));sy=add(sy,scale(q,si[y]));en+=dot(q,u[near[i][0]])+dot(q,u[near[i][2]]);}
  out<<en/(2*V)<<","<<dot(total,total)/V<<","<<(dot(cx,cx)+dot(sx,sx)+dot(cy,cy)+dot(sy,sy))/(2*V);
  for(int t=0;t<=L/2;t++){double g=0;for(int r=0;r<L;r++){g+=dot(wx[r],wx[(r+t)%L])+dot(wy[r],wy[(r+t)%L]);}out<<","<<g/(2*L*L*L);}
  if(L<=12)for(int t=0;t<=L/2;t++){double g=0;for(int y=0;y<L;y++)for(int x=0;x<L;x++){g+=dot(u[x+L*y],u[(x+t)%L+L*y])+dot(u[x+L*y],u[x+L*((y+t)%L)]);}out<<","<<g/(2*V);}
  out<<"\n";if(k%128==0){out.flush();memory_gate();}
 }
 if(!out.good())throw std::runtime_error("output write");
 std::cout<<"elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
