#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <complex>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <mutex>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

struct RNG {
  uint64_t state;
  explicit RNG(uint64_t seed):state(seed){}
  uint64_t next(){uint64_t z=(state+=0x9e3779b97f4a7c15ULL);z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
  uint64_t integer(uint64_t bound){ // Rejection removes modulo bias.
    uint64_t cutoff=(-bound)%bound,r;
    do {r=next();} while(r<cutoff);
    return r%bound;
  }
  double uniform(){return (next()>>11)*0x1.0p-53;}
};

struct Job {int L;double z;int init;uint64_t seed;};
std::mutex output_mutex;

void run(Job job,uint64_t burn,uint64_t production,const std::string& output){
 const int L=job.L,V=L*L*L;const double pi=std::acos(-1.0);
 const std::array<std::array<int,3>,4> modes{{{{1,0,0}},{{2,0,0}},{{1,1,0}},{{2,2,0}}}};
 const std::string tag="L"+std::to_string(L)+"_z"+std::to_string(int(job.z*10))+"_init"+std::to_string(job.init);
 std::ofstream stream(output+"/"+tag+".csv");stream<<std::setprecision(17);
 if(!stream)throw std::runtime_error("cannot open output");
 stream<<"sample,attempt,rho,S_x1,S_x2,S_xy1,S_xy2,flux_x,flux_y,flux_z\n";
 std::vector<int8_t> label(V,job.init?1:0);
 std::vector<std::array<int,6>> neighbors(V);
 std::vector<std::array<std::complex<double>,4>> phases(V);
 std::array<std::array<double,3>,4> sine;
 auto index=[L](int x,int y,int z){return (x*L+y)*L+z;};
 for(int x=0;x<L;x++)for(int y=0;y<L;y++)for(int z=0;z<L;z++){
  const int p=index(x,y,z);std::array<int,3> xyz{{x,y,z}};
  for(int a=0;a<3;a++)for(int b=0;b<2;b++){
   auto q=xyz;q[a]=(q[a]+(b?1:L-1))%L;
   neighbors[p][2*a+b]=index(q[0],q[1],q[2]);
  }
  for(int m=0;m<4;m++){
   double angle=-2*pi*(modes[m][0]*x+modes[m][1]*y+modes[m][2]*z)/L;
   phases[p][m]={std::cos(angle),std::sin(angle)};
  }
 }
 for(int m=0;m<4;m++)for(int a=0;a<3;a++)sine[m][a]=std::sin(2*pi*modes[m][a]/L);
 RNG rng(job.seed);int head=0,tail=0;int occupied=job.init?V:0;
 std::array<int,3> flux{{job.init?V:0,0,0}};
 uint64_t accepted=0,creations=0,removals=0,closed=0,samples=0;
 double maximum_longitudinal=0;
 const uint64_t stride=job.z<.5?1024:1;
 const auto began=std::chrono::steady_clock::now();
 auto feature=[&](int p,int a){const int v=label[p];return std::abs(v)==a+1?(v>0?1:-1):0;};
 for(uint64_t step=0;step<burn+production;step++){
  if(head==tail){tail=int(rng.integer(V));head=tail;}
  const int dir=int(rng.integer(6)),axis=dir/2,sign=(dir%2)?1:-1;
  const int slot=neighbors[head][dir],next=neighbors[slot][dir];
  const int old=label[slot];
  bool creating=old==0,removing=old==-sign*(axis+1);
  if(creating||removing){
   double ratio=creating?job.z:1/job.z;
   if(ratio>=1||rng.uniform()<ratio){
    label[slot]=creating?sign*(axis+1):0;occupied+=creating?1:-1;
    flux[axis]+=sign;head=next;accepted++;creations+=creating;removals+=removing;
   }
  }
  if(step<burn||head!=tail)continue;
  closed++;if(closed%stride)continue;
  std::array<std::array<std::complex<double>,3>,4> fourier{};
  int actual_occupied=0;std::array<int,3> actual_flux{};
  for(int p=0;p<V;p++){
   int divergence=0;
   for(int a=0;a<3;a++)divergence+=feature(neighbors[p][2*a+1],a)-feature(neighbors[p][2*a],a);
   if(divergence!=0)throw std::runtime_error("closed-state Gauss failure");
   const int value=label[p];if(!value)continue;
   int a=std::abs(value)-1,sign=value>0?1:-1;actual_occupied++;actual_flux[a]+=sign;
   for(int m=0;m<4;m++)fourier[m][a]+=double(sign)*phases[p][m];
  }
  if(actual_occupied!=occupied||actual_flux!=flux)throw std::runtime_error("content accounting failure");
  std::array<double,4> spectrum{};
  for(int m=0;m<4;m++){
   std::complex<double> longitudinal=0;
   for(int a=0;a<3;a++){spectrum[m]+=std::norm(fourier[m][a])/(2*V);longitudinal+=sine[m][a]*fourier[m][a];}
   maximum_longitudinal=std::max(maximum_longitudinal,std::abs(longitudinal));
   if(std::abs(longitudinal)>1e-8*V)throw std::runtime_error("Fourier Gauss failure");
  }
  stream<<samples<<','<<step-burn+1<<','<<double(occupied)/V;
  for(double x:spectrum)stream<<','<<x;
  for(int x:flux)stream<<','<<x;
  stream<<'\n';samples++;
 }
 stream.close();double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count();
 std::ofstream meta(output+"/"+tag+".json");meta<<std::setprecision(17);
 meta<<"{\n\"L\":"<<L<<",\"z\":"<<job.z<<",\"initialization\":"<<job.init<<",\"seed\":"<<job.seed
     <<",\"burn_attempts\":"<<burn<<",\"production_attempts\":"<<production<<",\"accepted\":"<<accepted
     <<",\"creations\":"<<creations<<",\"removals\":"<<removals<<",\"production_closed_visits\":"<<closed
     <<",\"closed_trace_stride\":"<<stride<<",\"samples\":"<<samples<<",\"final_occupied\":"<<occupied
     <<",\"final_worm_open\":"<<(head!=tail?"true":"false")<<",\"maximum_Fourier_longitudinal_residual\":"<<maximum_longitudinal
     <<",\"wall_seconds\":"<<seconds<<"\n}\n";
 std::lock_guard<std::mutex> guard(output_mutex);
 std::cout<<tag<<" samples="<<samples<<" seconds="<<seconds<<" exact_Gauss=ok"<<std::endl;
}

int main(int argc,char** argv){
 if(argc!=5){std::cerr<<"usage: program output_directory burn_attempts production_attempts threads\n";return 2;}
 const std::string output=argv[1];uint64_t burn=std::stoull(argv[2]),production=std::stoull(argv[3]);
 const int count=std::stoi(argv[4]);if(count<1||count>8)return 2;
 std::vector<Job> jobs;int case_index=0;
 for(int L:{9,13,17})for(double z:{.2,1.,4.}){
  for(int initial:{0,1})jobs.push_back({L,z,initial,uint64_t(20260921300ULL+2*case_index+initial)});
  case_index++;
 }
 std::atomic<size_t> next{0};std::atomic<bool> failed{false};std::vector<std::thread> workers;
 for(int t=0;t<count;t++)workers.emplace_back([&](){
  try{while(true){size_t i=next.fetch_add(1);if(i>=jobs.size())break;run(jobs[i],burn,production,output);}}
  catch(const std::exception& e){failed=true;std::lock_guard<std::mutex> guard(output_mutex);std::cerr<<e.what()<<std::endl;}
 });
 for(auto& worker:workers)worker.join();return failed?1:0;
}
