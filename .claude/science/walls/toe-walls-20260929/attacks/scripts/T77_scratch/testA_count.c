// T77 Test A in C: count +-1 assignments on one sublattice of the torus Z_L^3 with, for every site of the other
// sublattice, the six-neighbour sum in the allowed set A. Usage: ./testA L Amax cap  (A = {-Amax,...,Amax} even values; Amax=0 => A0)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int L, nvar, ncons;
static int (*cons)[6];       // constraint -> 6 vars
static int *v2c[64*64*64];   // not used for large
static int var2cons[4096][6]; static int nv2c[4096];
static int psum[8192], rem_[8192];
static int Amax;
static long long count=0, cap=0, nodes=0;
static int abortf=0;
static int feasible(int s,int r){
  // exists a even-ish value a in {-Amax..Amax} with |a-s|<=r and (a-s-r) even, a has parity of 6 (even) => a even
  for(int a=-Amax;a<=Amax;a+=2){ int d=a-s; if(abs(d)<=r && ((d-r)%2==0)) return 1; }
  return 0;
}
static void rec(int i){
  if(abortf) return;
  if(i==nvar){ count++; if(count>=cap) abortf=1; return; }
  nodes++;
  for(int t=1;t>=-1;t-=2){
    int ok=1;
    for(int k=0;k<nv2c[i];k++){ int c=var2cons[i][k]; psum[c]+=t; rem_[c]--; }
    for(int k=0;k<nv2c[i];k++){ int c=var2cons[i][k]; if(!feasible(psum[c],rem_[c])){ok=0;break;} }
    if(ok) rec(i+1);
    for(int k=0;k<nv2c[i];k++){ int c=var2cons[i][k]; psum[c]-=t; rem_[c]++; }
    if(abortf) return;
  }
}
int main(int argc,char**argv){
  L=atoi(argv[1]); Amax=atoi(argv[2]); cap=atoll(argv[3]);
  int *eid=malloc(sizeof(int)*L*L*L); int *oid=malloc(sizeof(int)*L*L*L);
  nvar=0; ncons=0;
  for(int x=0;x<L;x++)for(int y=0;y<L;y++)for(int z=0;z<L;z++){
    int s=(x*L+y)*L+z; if((x+y+z)%2==0){eid[s]=nvar++; oid[s]=-1;} else {oid[s]=ncons++; eid[s]=-1;} }
  cons=malloc(sizeof(int)*6*ncons);
  memset(nv2c,0,sizeof(nv2c));
  int dx[6]={1,-1,0,0,0,0},dy[6]={0,0,1,-1,0,0},dz[6]={0,0,0,0,1,-1};
  for(int x=0;x<L;x++)for(int y=0;y<L;y++)for(int z=0;z<L;z++){
    int s=(x*L+y)*L+z; if(oid[s]<0) continue; int c=oid[s];
    for(int k=0;k<6;k++){ int X=(x+dx[k]+L)%L,Y=(y+dy[k]+L)%L,Z=(z+dz[k]+L)%L; int t=(X*L+Y)*L+Z; int v=eid[t]; cons[c][k]=v; var2cons[v][nv2c[v]++]=c; }
    psum[c]=0; rem_[c]=6; }
  rec(0);
  printf("L=%d Amax=%d vars=%d count_one_sublattice=%lld%s nodes=%lld\n",L,Amax,nvar,count,abortf?" (CAP HIT)":"",nodes);
  return 0;
}
