// Kill-check T01: rule-derived hazards (function of the rule's own conditional p(.|N)) -- parameter-free, covariant, single-site.
// clause 'H': hazard = exp(entropy of p(.|recorded nbrs))  ; 'M': hazard = max_s p(s|recorded nbrs); 'Z': hazard = 1/max_s p
// usage: ./rulehaz CLAUSE p q r L nsamp seed
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
static uint64_t st;
static uint64_t sm(void){uint64_t z=(st+=0x9e3779b97f4a7c15ULL);z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
static double ur(void){return (sm()>>11)*(1.0/9007199254740992.0);}
int L,N; double W[6][6]; int nbr[8192][6]; int val[8192], formed[8192]; double rate[8192]; char cl;
int id(int x,int y,int z){x=(x%L+L)%L;y=(y%L+L)%L;z=(z%L+L)%L;return x+L*(y+L*z);}
void cond(int x,double*pr){double w[6];int any=0;for(int a=0;a<6;a++)w[a]=1;for(int d=0;d<6;d++){int y=nbr[x][d];if(formed[y]){any=1;for(int a=0;a<6;a++)w[a]*=W[a][val[y]];}}
  double Z=0;for(int a=0;a<6;a++)Z+=w[a];for(int a=0;a<6;a++)pr[a]=w[a]/Z;(void)any;}
double haz(int x){double pr[6];cond(x,pr);double mx=0,H=0;for(int a=0;a<6;a++){if(pr[a]>mx)mx=pr[a];H-=pr[a]*log(pr[a]);}
  if(cl=='H')return exp(H); if(cl=='M')return mx; return 1.0/mx;}
int main(int c,char**v){cl=v[1][0];double p=atof(v[2]),q=atof(v[3]),r=atof(v[4]);L=atoi(v[5]);long ns=atol(v[6]);st=strtoull(v[7],0,10);N=L*L*L;
  for(int a=0;a<6;a++)for(int b=0;b<6;b++)W[a][b]=(a==b)?p:((a/2==b/2)?q:r);
  int D[6][3]={{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
  for(int z=0;z<L;z++)for(int y=0;y<L;y++)for(int x=0;x<L;x++)for(int d=0;d<6;d++)nbr[id(x,y,z)][d]=id(x+D[d][0],y+D[d][1],z+D[d][2]);
  double sa=0,sa2=0,sc=0,smax=0;
  for(long s=0;s<ns;s++){for(int i=0;i<N;i++){formed[i]=0;} for(int i=0;i<N;i++)rate[i]=haz(i);
    for(int step=0;step<N;step++){double tot=0;for(int i=0;i<N;i++)if(!formed[i])tot+=rate[i];
      double u=ur()*tot,acc=0;int x=-1;for(int i=0;i<N;i++){if(formed[i])continue;acc+=rate[i];if(u<acc){x=i;break;}} if(x<0)for(int i=N-1;i>=0;i--)if(!formed[i]){x=i;break;}
      double pr[6];cond(x,pr);double uu=ur(),ac=0;int pick=5;for(int a=0;a<6;a++){ac+=pr[a];if(uu<ac){pick=a;break;}}
      val[x]=pick;formed[x]=1;rate[x]=0;for(int d=0;d<6;d++){int y=nbr[x][d];if(!formed[y])rate[y]=haz(y);}}
    long ag=0;for(int i=0;i<N;i++)for(int d=0;d<6;d+=2)if(val[i]==val[nbr[i][d]])ag++;double a1=(double)ag/(3.0*N);sa+=a1;sa2+=a1*a1;
    double m[3]={0,0,0};for(int i=0;i<N;i++){int a=val[i];m[a/2]+=(a%2==0)?1:-1;}sc+=(m[0]*m[0]+m[1]*m[1]+m[2]*m[2])/N;}
  double mean=sa/ns,var=(sa2/ns-mean*mean)*ns/(ns-1);printf("%c p=%g L=%d n=%ld a1=%.6f se=%.1e chi=%.3f\n",cl,p,L,ns,mean,sqrt(var/ns),sc/ns);return 0;}
