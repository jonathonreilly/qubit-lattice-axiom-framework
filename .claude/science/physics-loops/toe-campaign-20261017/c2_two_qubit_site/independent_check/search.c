// Independent search: strings on 7-site star, 2 qubits/site, commuting with all translates of all O-images.
// label bits: b0 spin-x, b1 spin-z, b2 flav-x, b3 flav-z.  mode 0: flavour fixed, mode 1: flavour soldered.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int site[7][3]={{0,0,0},{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
static int idx(int*v){for(int i=0;i<7;i++)if(site[i][0]==v[0]&&site[i][1]==v[1]&&site[i][2]==v[2])return i;return -1;}
// 1-qubit pauli code: (x,z): I=00, X=10, Z=01, Y=11 ; axis index of X=0,Y=1,Z=2
static int p2ax(int p){ // p = x | z<<1
  if(p==1)return 0; if(p==3)return 1; if(p==2)return 2; return -1;}
static int ax2p(int a){return a==0?1:(a==1?3:2);}
static int sym1(int a,int b){return ((a&1)&((b>>1)&1))^(((a>>1)&1)&(b&1));}
static int comm(int a,int b){return sym1(a&3,b&3)^sym1(a>>2,b>>2);}
int main(int argc,char**argv){
  int mode=atoi(argv[1]);
  // build O: signed perm matrices det +1
  int G[24][3][3];int ng=0;
  int perms[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
  for(int p=0;p<6;p++)for(int s=0;s<8;s++){int M[3][3]={{0}};
    for(int i=0;i<3;i++)M[perms[p][i]][i]=(s>>i&1)?-1:1; // M e_i = +-e_{perm(i)}
    int d=M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]);
    if(d==1){memcpy(G[ng],M,sizeof(M));ng++;}}
  if(ng!=24){printf("bad group %d\n",ng);return 1;}
  int sp[24][7]; int lab[24][16];
  for(int g=0;g<24;g++){
    int pi[3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(G[g][j][i])pi[i]=j;
    for(int r=0;r<7;r++){int v[3];for(int j=0;j<3;j++){v[j]=0;for(int k=0;k<3;k++)v[j]+=G[g][j][k]*site[r][k];}sp[g][r]=idx(v);}
    for(int l=0;l<16;l++){int s=l&3,f=l>>2;int s2=s?ax2p(pi[p2ax(s)]):0;int f2=f;if(mode==1)f2=f?ax2p(pi[p2ax(f)]):0;lab[g][l]=s2|(f2<<2);}
  }
  // checks: (g,t) -> list of pairs (a,b): a=idx(g r + t) [S site], b=r [preimage site]
  int nchk=0; int npair[600]; int pa[600][7], pb[600][7], pg[600];
  for(int g=0;g<24;g++)for(int tx=-2;tx<=2;tx++)for(int ty=-2;ty<=2;ty++)for(int tz=-2;tz<=2;tz++){
    if(g==0&&tx==0&&ty==0&&tz==0){} // identity g is G[0]? check below
    int n=0;for(int r=0;r<7;r++){int gr=sp[g][r];int v[3]={site[gr][0]+tx,site[gr][1]+ty,site[gr][2]+tz};int a=idx(v);if(a>=0){pa[nchk][n]=a;pb[nchk][n]=r;n++;}}
    if(n==0)continue;
    int isid=(G[g][0][0]==1&&G[g][1][1]==1&&G[g][2][2]==1&&tx==0&&ty==0&&tz==0);
    if(isid)continue;
    npair[nchk]=n;pg[nchk]=g;nchk++;}
  // sort by npair
  int ord[600];for(int i=0;i<nchk;i++)ord[i]=i;
  for(int i=0;i<nchk;i++)for(int j=i+1;j<nchk;j++)if(npair[ord[j]]<npair[ord[i]]){int t=ord[i];ord[i]=ord[j];ord[j]=t;}
  static unsigned char C[24][16][16];
  for(int g=0;g<24;g++)for(int a=0;a<16;a++)for(int b=0;b<16;b++)C[g][a][b]=comm(a,lab[g][b]);
  fprintf(stderr,"checks %d\n",nchk);
  long cnt=0;
  for(unsigned long n=1;n<(1UL<<28);n++){
    int S[7];for(int r=0;r<7;r++)S[r]=(n>>(4*r))&15;
    int ok=1;
    for(int k=0;k<nchk&&ok;k++){int c=ord[k];int g=pg[c];int x=0;for(int q=0;q<npair[c];q++)x^=C[g][S[pa[c][q]]][S[pb[c][q]]];if(x)ok=0;}
    if(ok){cnt++;printf("%lu\n",n);}
  }
  fprintf(stderr,"count %ld\n",cnt);
  return 0;
}
