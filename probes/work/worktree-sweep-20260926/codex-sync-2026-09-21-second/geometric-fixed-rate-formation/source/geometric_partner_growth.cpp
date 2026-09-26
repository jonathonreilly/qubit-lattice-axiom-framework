// Exact Gillespie geometry for antipodal partner records, nu=0.
// Integer IDs track immutable partners; this does not sample Bloch marks.
#include <algorithm>
#include <array>
#include <cmath>
#include <complex>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

struct Active {
    std::vector<int> list, position;
    explicit Active(int capacity):position(capacity,-1) {}
    void set(int id,bool enabled) {
        int p=position.at(id);
        if(enabled && p<0) {position[id]=static_cast<int>(list.size());list.push_back(id);}
        if(!enabled && p>=0) {
            int last=list.back();list[p]=last;position[last]=p;list.pop_back();position[id]=-1;
        }
    }
    bool has(int id) const {return position.at(id)>=0;}
};

struct Model {
    int N,V;
    std::vector<std::array<int,3>> xyz;
    std::vector<std::array<int,6>> neighbors;
    std::vector<int> partner,record,births_at;
    Active births,slides;
    int pairs=0,max_births=0,reuses=0;
    std::uint64_t birth_events=0,slide_events=0;
    explicit Model(int side):N(side),V(side*side*side),xyz(V),neighbors(V),partner(V,-1),record(V,-1),births_at(V),births(3*V),slides(6*V) {
        if(N<4 || N%2) throw std::runtime_error("even N>=4 required");
        for(int x=0;x<N;x++) for(int y=0;y<N;y++) for(int z=0;z<N;z++) {
            int u=(x*N+y)*N+z;xyz[u]={x,y,z};
            for(int a=0;a<3;a++) for(int sign=0;sign<2;sign++) {
                auto p=xyz[u];p[a]=(p[a]+(sign?-1:1)+N)%N;neighbors[u][2*a+sign]=(p[0]*N+p[1])*N+p[2];
            }
        }
        rebuild();
    }
    bool birth_enabled(int id) const {int x=id/3,i=id%3;return partner[x]<0 && partner[neighbors[x][2*i]]<0;}
    bool slide_enabled(int id) const {int x=id/6,d=id%6;return partner[x]>=0 && partner[neighbors[x][d]]<0;}
    void rebuild() {
        for(int id=0;id<3*V;id++) births.set(id,birth_enabled(id));
        for(int id=0;id<6*V;id++) slides.set(id,slide_enabled(id));
    }
    void refresh(int x) {
        for(int i=0;i<3;i++) {
            int a=3*x+i,b=3*neighbors[x][2*i+1]+i;births.set(a,birth_enabled(a));births.set(b,birth_enabled(b));
        }
        for(int d=0;d<6;d++) {
            int a=6*x+d,y=neighbors[x][d],b=6*y+(d^1);slides.set(a,slide_enabled(a));slides.set(b,slide_enabled(b));
        }
    }
    void born(int id) {
        if(!birth_enabled(id)) throw std::runtime_error("disabled birth selected");
        int a=id/3,b=neighbors[a][2*(id%3)];partner[a]=b;partner[b]=a;
        record[a]=2*pairs;record[b]=2*pairs+1;pairs++;birth_events++;
        for(int u:{a,b}) {if(births_at[u]>0) reuses++;births_at[u]++;max_births=std::max(max_births,births_at[u]);}
        refresh(a);refresh(b);
    }
    void slid(int id) {
        if(!slide_enabled(id)) throw std::runtime_error("disabled slide selected");
        int b=id/6,c=neighbors[b][id%6],a=partner[b];
        int ra=record[a],rb=record[b];partner[a]=-1;record[a]=-1;partner[b]=c;partner[c]=b;record[b]=ra;record[c]=rb;
        slide_events++;refresh(a);refresh(c);
    }
    void verify(bool catalog=true) const {
        int occupied=0;std::vector<int> identities(2*pairs);int total_births=0;
        for(int u=0;u<V;u++) {
            total_births+=births_at[u];int v=partner[u];
            if(v<0) {if(record[u]!=-1) throw std::runtime_error("vacancy has identity");continue;}
            occupied++;
            if(v>=V || partner[v]!=u || record[u]<0 || record[u]>=2*pairs) throw std::runtime_error("bad partner or identity");
            if(std::find(neighbors[u].begin(),neighbors[u].end(),v)==neighbors[u].end()) throw std::runtime_error("nonlocal pair");
            if(record[u]/2!=record[v]/2 || (record[u]^record[v])!=1) throw std::runtime_error("immutable partnership changed");
            identities[record[u]]++;
        }
        if(occupied!=2*pairs || total_births!=2*static_cast<int>(birth_events) || std::any_of(identities.begin(),identities.end(),[](int n){return n!=1;})) throw std::runtime_error("birth budget or identities failed");
        if(catalog) {
            for(int id=0;id<3*V;id++) if(births.has(id)!=birth_enabled(id)) throw std::runtime_error("birth catalog drift");
            for(int id=0;id<6*V;id++) if(slides.has(id)!=slide_enabled(id)) throw std::runtime_error("slide catalog drift");
            for(std::size_t j=0;j<births.list.size();j++) if(births.position[births.list[j]]!=static_cast<int>(j)) throw std::runtime_error("birth back index drift");
            for(std::size_t j=0;j<slides.list.size();j++) if(slides.position[slides.list[j]]!=static_cast<int>(j)) throw std::runtime_error("slide back index drift");
        }
        for(int u=0;u<V;u++) {
            int sigma=((xyz[u][0]+xyz[u][1]+xyz[u][2])%2)?-1:1,div6=0;
            for(int i=0;i<3;i++) {
                int v=neighbors[u][2*i+1];
                div6+=sigma*(6*(partner[u]==neighbors[u][2*i])-1)+sigma*(6*(partner[v]==u)-1);
            }
            if(div6!=-6*sigma*(partner[u]<0)) throw std::runtime_error("integer Gauss identity failed");
        }
    }
    void save(const std::string& path) const {
        std::ofstream f(path);if(!f) throw std::runtime_error("cannot open state output");f<<"N "<<N<<"\nsite partner identity births_at_site\n";
        for(int u=0;u<V;u++) f<<u<<' '<<partner[u]<<' '<<record[u]<<' '<<births_at[u]<<'\n';
    }
    void load(const std::string& path) {
        std::ifstream f(path);std::string line;int side;
        if(!(f>>line>>side) || side!=N) throw std::runtime_error("bad input N");std::getline(f,line);std::getline(f,line);
        pairs=0;birth_events=0;slide_events=0;max_births=0;reuses=0;
        for(int u=0;u<V;u++) {int index;if(!(f>>index>>partner[u]>>record[u]>>births_at[u]) || index!=u) throw std::runtime_error("bad state row");if(record[u]>=0)pairs=std::max(pairs,record[u]/2+1);max_births=std::max(max_births,births_at[u]);reuses+=std::max(0,births_at[u]-1);}
        birth_events=pairs;rebuild();verify();
    }
    void catalog(const std::string& path) const {
        std::ofstream f(path);if(!f) throw std::runtime_error("cannot open catalog output");
        for(int id=0;id<3*V;id++) if(birth_enabled(id)) f<<"B "<<id/3<<' '<<neighbors[id/3][2*(id%3)]<<'\n';
        for(int id=0;id<6*V;id++) if(slide_enabled(id)) {int b=id/6;f<<"S "<<partner[b]<<' '<<b<<' '<<neighbors[b][id%6]<<'\n';}
    }
    void observables(std::ostream& f) const {
        std::array<int,3> counts{},wind{};bool full=2*pairs==V;
        for(int i=0;i<3;i++) {
            std::vector<int> planes(N);
            for(int u=0;u<V;u++) if(partner[u]==neighbors[u][2*i]) {counts[i]++;int sigma=((xyz[u][0]+xyz[u][1]+xyz[u][2])%2)?-1:1;planes[xyz[u][i]]+=sigma;}
            wind[i]=planes[0];if(full && std::any_of(planes.begin(),planes.end(),[&](int value){return value!=wind[i];})) throw std::runtime_error("winding plane disagreement");
        }
        f<<"\"orientation_counts\":["<<counts[0]<<','<<counts[1]<<','<<counts[2]<<"],\n\"winding\":["<<wind[0]<<','<<wind[1]<<','<<wind[2]<<"],\n\"winding_valid\":"<<(full?"true":"false")<<",\n\"modes\":[";
        std::set<std::array<int,3>> modes;
        for(auto base:std::vector<std::array<int,3>>{{1,0,0},{2,0,0},{1,1,0},{1,1,1}}) {
            std::sort(base.begin(),base.end());
            do {for(int mask=0;mask<8;mask++){auto k=base;for(int i=0;i<3;i++)if(mask>>i&1)k[i]*=-1;int sign=0;for(int value:k)if(value){sign=value>0?1:-1;break;}if(sign>0)modes.insert(k);}}while(std::next_permutation(base.begin(),base.end()));
        }
        const double pi=std::acos(-1.0);bool first=true;
        for(auto k:modes) {
            std::array<std::complex<double>,3> field{},d{};std::complex<double> charge{};
            for(int u=0;u<V;u++) {
                double angle=-2*pi*(k[0]*xyz[u][0]+k[1]*xyz[u][1]+k[2]*xyz[u][2])/N;std::complex<double> phase=std::polar(1.0,angle)/std::sqrt(static_cast<double>(V));int sigma=((xyz[u][0]+xyz[u][1]+xyz[u][2])%2)?-1:1;
                for(int i=0;i<3;i++)field[i]+=phase*static_cast<double>(sigma)*(static_cast<double>(partner[u]==neighbors[u][2*i])-1.0/6);
                if(partner[u]<0)charge-=static_cast<double>(sigma)*phase;
            }
            double power=0,dnorm=0;std::complex<double> div{};
            for(int i=0;i<3;i++){d[i]=1.0-std::polar(1.0,-2*pi*k[i]/N);dnorm+=std::norm(d[i]);power+=std::norm(field[i]);div+=d[i]*field[i];}
            double longitudinal=std::norm(div)/dnorm,residual=std::abs(div-charge);if(residual>1e-8)throw std::runtime_error("Fourier Gauss residual");
            if(!first)f<<',';first=false;
            f<<"{\"ell\":["<<k[0]<<','<<k[1]<<','<<k[2]<<"],\"power\":"<<power<<",\"transverse_per_polarization\":"<<(power-longitudinal)/2<<",\"longitudinal\":"<<longitudinal<<",\"gauss_residual\":"<<residual<<'}';
        }
        f<<']';
    }
};

int main(int argc,char**argv) try {
    if(argc==5 && std::string(argv[1])=="--catalog") {Model m(std::stoi(argv[2]));m.load(argv[3]);m.catalog(argv[4]);return 0;}
    if(argc<7 || argc>8) {std::cerr<<"usage: N seed beta kappa event_cap prefix [check_every]\n";return 2;}
    int N=std::stoi(argv[1]);std::uint64_t seed=std::stoull(argv[2]),cap=std::stoull(argv[5]),check_every=argc==8?std::stoull(argv[7]):0;double beta=std::stod(argv[3]),kappa=std::stod(argv[4]);std::string prefix=argv[6];
    if(!(beta>0 && kappa>0))throw std::runtime_error("positive beta,kappa required");
    Model m(N);std::mt19937_64 rng(seed);std::uniform_real_distribution<double> uniform(0,1);double t=0;std::uint64_t events=0;
    std::ofstream trajectory(prefix+".csv");if(!trajectory)throw std::runtime_error("cannot open trajectory");trajectory<<std::setprecision(17)<<"time,occupied,vacancies,birth_channels,slide_channels,birth_events,slide_events,site_reuses,max_site_births\n";
    auto snapshot=[&](){m.verify();trajectory<<t<<','<<2*m.pairs<<','<<m.V-2*m.pairs<<','<<m.births.list.size()<<','<<m.slides.list.size()<<','<<m.birth_events<<','<<m.slide_events<<','<<m.reuses<<','<<m.max_births<<'\n';};snapshot();int stride=std::max(1,m.V/200);
    while(2*m.pairs<m.V && events<cap) {
        double rb=beta*m.births.list.size(),rs=kappa*m.slides.list.size(),rate=rb+rs;if(!(rate>0))throw std::runtime_error("nonfull state has no active event");
        double u;do{u=uniform(rng);}while(u<=0);t+=-std::log(u)/rate;bool birth=uniform(rng)*rate<rb;
        if(birth) {std::uniform_int_distribution<std::size_t> pick(0,m.births.list.size()-1);m.born(m.births.list[pick(rng)]);} else {std::uniform_int_distribution<std::size_t> pick(0,m.slides.list.size()-1);m.slid(m.slides.list[pick(rng)]);}
        events++;if(check_every && events%check_every==0)m.verify();
        if(birth && (m.pairs%stride==0 || m.V-2*m.pairs<=32))snapshot();
    }
    m.verify();m.save(prefix+".state.txt");if(2*m.pairs<m.V)snapshot();
    std::ofstream result(prefix+".json");if(!result)throw std::runtime_error("cannot open result");result<<std::setprecision(17);
    result<<"{\n\"scope\":\"geometric projection, nu=0; integer identity bookkeeping only\",\n\"N\":"<<N<<",\"seed\":"<<seed<<",\"beta\":"<<beta<<",\"kappa\":"<<kappa<<",\"nu\":0,\n\"full\":"<<(2*m.pairs==m.V?"true":"false")<<",\"time\":"<<t<<",\"event_cap\":"<<cap<<",\"events\":"<<events<<",\"birth_events\":"<<m.birth_events<<",\"slide_events\":"<<m.slide_events<<",\"site_reuses\":"<<m.reuses<<",\"max_site_births\":"<<m.max_births<<",\n";
    m.observables(result);result<<"\n}\n";
    std::cout<<"N="<<N<<" beta="<<beta<<" seed="<<seed<<" full="<<(2*m.pairs==m.V)<<" time="<<std::setprecision(9)<<t<<" events="<<events<<"\n";return 0;
} catch(const std::exception&e) {std::cerr<<e.what()<<'\n';return 1;}
