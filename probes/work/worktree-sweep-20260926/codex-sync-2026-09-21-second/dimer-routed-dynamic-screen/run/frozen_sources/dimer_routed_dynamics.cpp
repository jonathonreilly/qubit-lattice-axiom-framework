#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <complex>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

using U=uint32_t;
using C=std::complex<double>;
struct Rng {
    using result_type=uint64_t;
    std::array<uint64_t,4> s;
    explicit Rng(uint64_t seed) {
        for(auto &v:s) {
            uint64_t z=(seed+=0x9e3779b97f4a7c15ULL);
            z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
            z=(z^(z>>27))*0x94d049bb133111ebULL;v=z^(z>>31);
        }
    }
    static uint64_t rot(uint64_t x,int k) {return (x<<k)|(x>>(64-k));}
    static constexpr result_type min(){return 0;}
    static constexpr result_type max(){return UINT64_MAX;}
    result_type operator()(){
        const uint64_t r=rot(s[1]*5,7)*9,t=s[1]<<17;
        s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rot(s[3],45);
        return r;
    }
    uint64_t bounded(uint64_t n) {
        if(!n)throw std::runtime_error("zero RNG bound");
        const uint64_t threshold=-n%n;
        uint64_t r;do{r=(*this)();}while(r<threshold);return r%n;
    }
};
const int delta[6][3]={{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
int feature[14][6],S2[3][14][14];
void alphabet(){
    for(int a=0;a<6;++a)for(int i=0;i<3;++i)feature[a][i]=delta[a][i];
    for(int a=0;a<8;++a)for(int i=0;i<3;++i)feature[6+a][3+i]=((a>>(2-i))&1)?1:-1;
    for(int i=0;i<3;++i)for(int a=0;a<14;++a)for(int b=0;b<14;++b){
        int j=(i+1)%3,k=(i+2)%3;
        S2[i][a][b]=feature[a][j]*feature[b][3+k]-feature[a][k]*feature[b][3+j]
                    +feature[b][j]*feature[a][3+k]-feature[b][k]*feature[a][3+j];
    }
}
struct Geometry {
    U N,V,K;std::vector<U> partner,black,white,pair_at;
    explicit Geometry(U side):N(side),V(side*side*side),K(V/2),partner(V,UINT32_MAX),pair_at(V,UINT32_MAX) {
        if(N<8||N%2)throw std::runtime_error("even N>=8 required");
    }
    std::array<int,3> coord(U x) const {return {int(x/(N*N)),int((x/N)%N),int(x%N)};}
    U site(int x,int y,int z) const {
        return U((x+int(N))%int(N))*N*N+U((y+int(N))%int(N))*N+U((z+int(N))%int(N));
    }
    U neighbor(U x,int j)const {auto p=coord(x);return site(p[0]+delta[j][0],p[1]+delta[j][1],p[2]+delta[j][2]);}
    void verify(){
        black.clear();white.clear();
        for(U x=0;x<V;++x){
            if(partner[x]>=V||partner[x]==x||partner[partner[x]]!=x)throw std::runtime_error("invalid partner involution");
            bool adjacent=false;for(int j=0;j<6;++j)adjacent|=neighbor(x,j)==partner[x];
            if(!adjacent)throw std::runtime_error("nonlocal partner");
            auto p=coord(x);if((p[0]+p[1]+p[2])%2==0){
                U u=U(black.size());black.push_back(x);white.push_back(partner[x]);pair_at[x]=u;pair_at[partner[x]]=u;
            }
        }
        if(black.size()!=K)throw std::runtime_error("incorrect pair count");
    }
};
void write_geometry(U N,const std::string&kind,uint64_t seed,const std::string&path){
    if(std::filesystem::exists(path))throw std::runtime_error("geometry output exists");
    Geometry g(N);Rng rng(seed);
    for(U x=0;x<g.V;++x){
        auto p=g.coord(x);
        if((p[0]+p[1]+p[2])%2==0){
            int j=kind=="winding"?0:(p[0]%2==0?0:1);U y=g.neighbor(x,j);g.partner[x]=y;g.partner[y]=x;
        }
    }
    if(kind!="winding"&&kind!="irregular")throw std::runtime_error("unknown geometry kind");
    uint64_t accepted=0,proposals=kind=="irregular"?uint64_t(8)*g.V:0;
    for(uint64_t z=0;z<proposals;++z){
        U a=U(rng.bounded(g.V));int i=int(rng.bounded(3)),j=(i+1+int(rng.bounded(2)))%3;
        U b=g.neighbor(a,2*i),d=g.neighbor(a,2*j),c=g.neighbor(b,2*j);
        if(g.partner[a]==b&&g.partner[d]==c){g.partner[a]=d;g.partner[d]=a;g.partner[b]=c;g.partner[c]=b;++accepted;}
        else if(g.partner[a]==d&&g.partner[b]==c){g.partner[a]=b;g.partner[b]=a;g.partner[d]=c;g.partner[c]=d;++accepted;}
    }
    if(proposals&&!accepted)throw std::runtime_error("failed irregular fixture");
    g.verify();std::ofstream o(path,std::ios::binary);o.write("DRPAIR01",8);o.write(reinterpret_cast<char*>(&N),4);
    o.write(reinterpret_cast<const char*>(g.partner.data()),4*g.V);if(!o)throw std::runtime_error("geometry write failed");o.close();
    std::cout<<"{\"N\":"<<N<<",\"kind\":\""<<kind<<"\",\"seed\":"<<seed
             <<",\"proposals\":"<<proposals<<",\"accepted_flips\":"<<accepted<<",\"bytes\":"<<(12+4*uint64_t(g.V))<<"}\n";
}
Geometry read_geometry(const std::string&path){
    std::ifstream in(path,std::ios::binary);char magic[8];U N=0;in.read(magic,8);in.read(reinterpret_cast<char*>(&N),4);
    if(!in||std::string(magic,8)!="DRPAIR01")throw std::runtime_error("bad geometry header");
    Geometry g(N);in.read(reinterpret_cast<char*>(g.partner.data()),4*g.V);
    if(!in||in.peek()!=std::ifstream::traits_type::eof())throw std::runtime_error("bad geometry length");g.verify();return g;
}
struct Channel {U l,u,v,r;uint8_t axis;int8_t sign;};
struct Snapshot {double t;std::array<std::array<C,6>,3> modes;};
Snapshot observe(double t,const Geometry&g,const std::vector<U>&key,const std::vector<uint8_t>&colors){
    Snapshot out{};out.t=t;std::vector<C> phase(g.N);
    for(U x=0;x<g.N;++x)phase[x]=std::polar(1.0,-2*std::acos(-1.0)*x/g.N);
    for(U u=0;u<g.K;++u){auto xyz=g.coord(g.black[u]);int a=colors[key[u]];
        for(int j=0;j<3;++j)for(int f=0;f<6;++f)out.modes[j][f]+=phase[xyz[j]]*double(feature[a][f]);
    }
    for(auto &mode:out.modes)for(auto &v:mode)v/=std::sqrt(double(g.K));return out;
}
void run(const std::string&geom,uint64_t seed,const std::string&output,bool validation){
    if(std::filesystem::exists(output))throw std::runtime_error("simulation output exists");
    auto start=std::chrono::steady_clock::now();Geometry g=read_geometry(geom);Rng rng(seed);alphabet();
    std::array<std::vector<U>,6> q,inv;
    for(int j=0;j<6;++j){q[j].resize(g.K);inv[j].assign(g.K,UINT32_MAX);
        for(U u=0;u<g.K;++u){U v=g.pair_at[g.neighbor(g.black[u],j)];q[j][u]=v;
            if(inv[j][v]!=UINT32_MAX)throw std::runtime_error("routing not injective");inv[j][v]=u;}
    }
    std::vector<Channel> channels;channels.reserve(5*g.K);U minimum_cycle=g.K;
    for(int j=0;j<6;++j){std::vector<bool>seen(g.K,false);
        for(U u=0;u<g.K;++u){if(!seen[u]){U v=u,len=0;do{seen[v]=true;++len;v=q[j][v];}while(v!=u);
                if(len>1){if(len<g.N/2)throw std::runtime_error("short routing cycle");minimum_cycle=std::min(minimum_cycle,len);}}
            U v=q[j][u];if(v==u)continue;U l=inv[j][u],r=q[j][v];
            if(l==u||l==v||l==r||u==r||v==r)throw std::runtime_error("overlapping context");
            channels.push_back({l,u,v,r,uint8_t(j/2),int8_t(j%2?-1:1)});
        }
    }
    if(channels.size()!=5*uint64_t(g.K))throw std::runtime_error("wrong channel multiplicity");
    std::vector<U>key(g.K);std::iota(key.begin(),key.end(),0);std::vector<uint8_t>colors(g.K);std::array<U,14>counts{};
    for(U u=0;u<g.K;++u){colors[u]=uint8_t(rng.bounded(14));++counts[colors[u]];}
    std::vector<Snapshot>snapshots;snapshots.push_back(observe(0,g,key,colors));
    std::array<double,4>times={7./16,7./8,21./16,7./4};if(validation)times={.005,.01,.015,.02};
    uint64_t attempts=0,accepted=0,changed=0;double previous=0;
    for(double t:times){
        double mean=double(channels.size())*42./40*g.N*(t-previous);
        std::poisson_distribution<uint64_t>poisson(mean);uint64_t number=poisson(rng);attempts+=number;
        for(uint64_t z=0;z<number;++z){
            const Channel &c=channels[rng.bounded(channels.size())];
            int l=colors[key[c.l]],a=colors[key[c.u]],b=colors[key[c.v]],r=colors[key[c.r]];
            int h2=c.sign*(S2[c.axis][l][a]+S2[c.axis][a][r]-S2[c.axis][l][b]-S2[c.axis][b][r]);
            int numerator=22+5*h2;if(numerator<2||numerator>42)throw std::runtime_error("rate outside ceiling");
            if(rng.bounded(42)<uint64_t(numerator)){std::swap(key[c.u],key[c.v]);++accepted;changed+=a!=b;}
        }
        snapshots.push_back(observe(t,g,key,colors));previous=t;
    }
    std::vector<bool>seen(g.K,false);std::array<U,14>final_counts{};
    for(U id:key){if(id>=g.K||seen[id])throw std::runtime_error("record key not a permutation");seen[id]=true;++final_counts[colors[id]];}
    if(final_counts!=counts)throw std::runtime_error("immutable color counts changed");
    double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::ofstream o(output);o<<std::setprecision(17);
    o<<"{\"N\":"<<g.N<<",\"pairs\":"<<g.K<<",\"seed\":"<<seed<<",\"geometry\":\""<<geom
     <<"\",\"mode\":\""<<(validation?"validation":"production")<<"\",\"k0\":1.1,\"gamma\":1,\"channels\":"<<channels.size()
     <<",\"minimum_nontrivial_cycle\":"<<minimum_cycle<<",\"attempts\":"<<attempts<<",\"accepted\":"<<accepted
     <<",\"color_changes\":"<<changed<<",\"wall_seconds\":"<<seconds<<",\"key_permutation_verified\":true,\"counts_verified\":true,\"color_counts\":[";
    for(int a=0;a<14;++a){if(a)o<<',';o<<counts[a];}o<<"],\"snapshots\":[";
    for(size_t i=0;i<snapshots.size();++i){if(i)o<<',';o<<"{\"t\":"<<snapshots[i].t<<",\"fields\":[";
        for(int j=0;j<3;++j){if(j)o<<',';o<<'[';
            for(int f=0;f<6;++f){if(f)o<<',';C z=snapshots[i].modes[j][f];o<<'['<<z.real()<<','<<z.imag()<<']';}o<<']';}
        o<<"]}";
    }o<<"],\"final_rng_state\":[";for(int j=0;j<4;++j){if(j)o<<',';o<<rng.s[j];}o<<"]}\n";
    if(!o)throw std::runtime_error("output write failed");
    {
        std::ofstream f(output+".state",std::ios::binary);f.write("DRSTATE1",8);f.write(reinterpret_cast<char*>(&g.N),4);
        f.write(reinterpret_cast<char*>(key.data()),4*g.K);f.write(reinterpret_cast<char*>(colors.data()),g.K);
        if(!f)throw std::runtime_error("final state write failed");
    }
    std::cout<<"{\"N\":"<<g.N<<",\"seed\":"<<seed<<",\"attempts\":"<<attempts<<",\"wall_seconds\":"<<std::setprecision(6)<<seconds<<"}\n";
}
int main(int argc,char**argv){
    try{
        if(argc==6&&std::string(argv[1])=="geometry"){write_geometry(U(std::stoul(argv[2])),argv[3],std::stoull(argv[4]),argv[5]);return 0;}
        if(argc==5&&(std::string(argv[1])=="run"||std::string(argv[1])=="validate")){
            run(argv[2],std::stoull(argv[3]),argv[4],std::string(argv[1])=="validate");return 0;
        }
        throw std::runtime_error("usage: geometry N winding|irregular seed path OR run|validate geometry seed output.json");
    }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}
}
