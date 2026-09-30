// Independent re-implementation for the kill check on T01.
// Different from attacker's sim.c: splitmix64 RNG, naive O(N) site selection with double rates,
// exponential-clock (next-reaction) style for U (iid priorities) and Gillespie for E/A,
// content draw by explicit cumulative sampling; a1 measured on all 3N edges.
// usage: ./indep CLAUSE p q r L nsamp seed [f0 f1 ... f6]   (custom hazards if clause=='H')
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
static uint64_t st;
static uint64_t sm(void){uint64_t z=(st+=0x9e3779b97f4a7c15ULL);z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
static double ur(void){return (sm()>>11)*(1.0/9007199254740992.0);}
int L,N; double W[6][6]; double haz[7];
int nbr[4096][6]; int val[4096], formed[4096];
int id(int x,int y,int z){x=(x%L+L)%L;y=(y%L+L)%L;z=(z%L+L)%L;return x+L*(y+L*z);}
int main(int c,char**v){
  char cl=v[1][0]; double p=atof(v[2]),q=atof(v[3]),r=atof(v[4]); L=atoi(v[5]); long ns=atol(v[6]); st=strtoull(v[7],0,10);
  N=L*L*L;
  for(int a=0;a<6;a++)for(int b=0;b<6;b++)W[a][b]=(a==b)?p:((a/2==b/2)?q:r);   // opposite = same axis pair (a/2==b/2, a!=b)
  for(int k=0;k<7;k++){ if(cl=='U')haz[k]=1; else if(cl=='E')haz[k]=(1+k)*(1+k); else if(cl=='A')haz[k]=1.0/(1+k); else haz[k]=atof(v[8+k]); }
  int D[6][3]={{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
  for(int z=0;z<L;z++)for(int y=0;y<L;y++)for(int x=0;x<L;x++)for(int d=0;d<6;d++)nbr[id(x,y,z)][d]=id(x+D[d][0],y+D[d][1],z+D[d][2]);
  double sa=0, sa2=0; double sm2=0; long nuc=0; long hist[7]={0};
  static double rate[4096]; static int kk[4096];
  for(long s=0;s<ns;s++){
    for(int i=0;i<N;i++){formed[i]=0;kk[i]=0;}
    for(int step=0;step<N;step++){
      double tot=0; for(int i=0;i<N;i++){ if(!formed[i]){rate[i]=haz[kk[i]];tot+=rate[i];} else rate[i]=0; }
      double u=ur()*tot,acc=0; int x=-1; for(int i=0;i<N;i++){ acc+=rate[i]; if(u<acc){x=i;break;} } if(x<0){for(int i=N-1;i>=0;i--)if(!formed[i]){x=i;break;}}
      double w[6]; for(int a=0;a<6;a++)w[a]=1; int any=0;
      for(int d=0;d<6;d++){int y=nbr[x][d]; if(formed[y]){any=1; for(int a=0;a<6;a++)w[a]*=W[a][val[y]];}}
      if(!any)for(int a=0;a<6;a++)w[a]=1;
      double Z=0;for(int a=0;a<6;a++)Z+=w[a]; double uu=ur()*Z,ac=0; int pick=5; for(int a=0;a<6;a++){ac+=w[a]; if(uu<ac){pick=a;break;}}
      if(kk[x]==0)nuc++; hist[kk[x]]++; val[x]=pick; formed[x]=1; for(int d=0;d<6;d++)kk[nbr[x][d]]++;
    }
    long agree=0; for(int i=0;i<N;i++)for(int d=0;d<6;d+=2)if(val[i]==val[nbr[i][d]])agree++;
    double a1=(double)agree/(3.0*N); sa+=a1; sa2+=a1*a1;
    double m[3]={0,0,0}; for(int i=0;i<N;i++){int a=val[i]; m[a/2]+= (a%2==0)?1:-1;} sm2+=(m[0]*m[0]+m[1]*m[1]+m[2]*m[2])/((double)N*N)*N;
  }
  double mean=sa/ns, var=(sa2/ns-mean*mean)*ns/(ns-1); printf("%c p=%g L=%d n=%ld a1=%.6f se=%.2e chi=%.3f\n",cl,p,L,ns,mean,sqrt(var/ns),sm2/ns);
  printf("nucleation fraction=%.5f  k-at-formation hist:",(double)nuc/((double)ns*N)); for(int k=0;k<7;k++)printf(" %.4f",(double)hist[k]/((double)ns*N)); printf("\n");
  return 0;
}
