// Independent selective harness: compile the unchanged supplied Model by inclusion.
// The reference geometry, channels and state updates below do not call its predicates.
#define main supplied_growth_main
#include "../geometric_partner_growth.cpp"
#undef main

int adjacent(int u,int axis,int sign,int N) {
    int stride=axis==0?N*N:axis==1?N:1;
    int coordinate=(u/stride)%N;
    return u+(((coordinate+sign+N)%N)-coordinate)*stride;
}
void demand(bool yes,const char* what) {if(!yes)throw std::runtime_error(what);}
std::vector<int> reference_births(const Model& m) {
    std::vector<int> ids;
    for(int u=0;u<m.V;u++)for(int axis=0;axis<3;axis++)
        if(m.partner[u]<0 && m.partner[adjacent(u,axis,1,m.N)]<0)ids.push_back(3*u+axis);
    return ids;
}
std::vector<int> reference_slides(const Model& m) {
    std::vector<int> ids;
    for(int u=0;u<m.V;u++)if(m.partner[u]>=0)
        for(int axis=0;axis<3;axis++)for(int sign:{1,-1})
            if(m.partner[adjacent(u,axis,sign,m.N)]<0)ids.push_back(6*u+2*axis+(sign<0));
    return ids;
}
void catalog_check(const Model& m) {
    auto b=m.births.list,s=m.slides.list;
    std::sort(b.begin(),b.end());std::sort(s.begin(),s.end());
    demand(b==reference_births(m),"reference birth catalog disagreement");
    demand(s==reference_slides(m),"reference slide catalog disagreement");
    m.verify();
}
int main(int argc,char**argv)try {
    demand(argc==3,"usage: fixture-list observable-output");
    std::ifstream input(argv[1]);std::ofstream obs(argv[2]);
    std::string name,path;int N;std::uint64_t fixtures=0,births=0,slides=0,turns=0,wraps=0;
    while(input>>name>>N>>path) {
        Model m(N);m.load(path);catalog_check(m);fixtures++;
        for(int id:reference_births(m)) {
            Model actual=m;auto p=m.partner,r=m.record,counts=m.births_at;
            int a=id/3,b=adjacent(a,id%3,1,N);p[a]=b;p[b]=a;
            r[a]=2*m.pairs;r[b]=2*m.pairs+1;counts[a]++;counts[b]++;
            actual.born(id);catalog_check(actual);
            demand(actual.partner==p && actual.record==r && actual.births_at==counts,"reference birth state disagreement");
            demand(actual.pairs==m.pairs+1 && actual.birth_events==m.birth_events+1 && actual.slide_events==m.slide_events,"reference birth budget disagreement");births++;
        }
        for(int id:reference_slides(m)) {
            Model actual=m;auto p=m.partner,r=m.record;
            int b=id/6,axis=(id%6)/2,sign=id%2?-1:1,c=adjacent(b,axis,sign,N),a=p[b];
            p[a]=-1;p[b]=c;p[c]=b;r[b]=m.record[a];r[c]=m.record[b];r[a]=-1;
            actual.slid(id);catalog_check(actual);
            demand(actual.partner==p && actual.record==r && actual.births_at==m.births_at,"reference slide state disagreement");
            demand(actual.pairs==m.pairs && actual.birth_events==m.birth_events && actual.slide_events==m.slide_events+1,"reference slide budget disagreement");
            int reverse=-1;for(int di=0;di<6;di++)if(adjacent(b,di/2,di%2?-1:1,N)==a)reverse=6*b+di;
            demand(reverse>=0 && actual.slides.has(reverse),"missing reciprocal slide");
            Model undone=actual;undone.slid(reverse);catalog_check(undone);
            demand(undone.partner==m.partner && undone.record==m.record,"marked slide is not reversed");
            int oldaxis=-1;for(int q=0;q<3;q++)for(int sg:{-1,1})if(adjacent(b,q,sg,N)==a)oldaxis=q;
            if(oldaxis!=axis)turns++;
            int stride=axis==0?N*N:axis==1?N:1;if(std::abs((b/stride)%N-(c/stride)%N)==N-1)wraps++;
            slides++;
        }
        obs<<std::setprecision(17)<<"{\"fixture\":\""<<name<<"\",\"N\":"<<N<<",\"birth_channels\":"<<m.births.list.size()<<",\"slide_channels\":"<<m.slides.list.size()<<",";
        m.observables(obs);obs<<"}\n";
    }
    std::cout<<"{\"fixtures\":"<<fixtures<<",\"birth_transitions\":"<<births<<",\"slide_transitions_and_exact_inverses\":"<<slides<<",\"turning_slides\":"<<turns<<",\"periodic_crossing_slides\":"<<wraps<<"}\n";
    return 0;
}catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
