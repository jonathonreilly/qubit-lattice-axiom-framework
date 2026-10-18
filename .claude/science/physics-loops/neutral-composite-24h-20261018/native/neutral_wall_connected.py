"""Exact fourth-order connected local diagonal contributions at a diagonal-color wall."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import sys,json,itertools
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_rung_model import h
bits=[(b<<1)|(b.bit_count()%2) for b in range(8)]
moves=[[(i,int(h[i,j])) for i in range(8) if h[i,j]] for j in range(8)]
N=10

def coeff(ref,active,left,right):
 def E(st):
  chain=[left]+list(st)+[right]
  return sum(2*(bits[a]^bits[b]).bit_count() for a,b in zip(chain,chain[1:]))
 e0=E(ref)
 def V(vec):
  out=defaultdict(F)
  for st,amp in vec.items():
   for j in active:
    for new,c in moves[st[j]]:
     dest=st[:j]+(new,)+st[j+1:];out[dest]+=c*amp
  return {st:a for st,a in out.items() if a}
 v=V({ref:F(1)});w={st:a/F(e0-E(st)) for st,a in v.items() if E(st)!=e0};y=V(w)
 e2=y.get(ref,F(0));n2=sum(a*a for a in w.values())
 e4=sum(a*a/F(e0-E(st)) for st,a in y.items() if E(st)!=e0)-e2*n2
 return e2,e4
rows=[]
for name,ref,left,right in [('vac',(0,)*N,0,0),('wall',(0,)*5+(3,)*5,0,3),('domain2',(0,)*4+(3,)*2+(0,)*4,0,0),('domain3',(0,)*3+(3,)*3+(0,)*4,0,0)]:
 singles=[coeff(ref,[j],left,right) for j in range(N)]
 pairs={}
 for i in range(N):
  for j in range(i+1,N):
   c=coeff(ref,[i,j],left,right)[1]-singles[i][1]-singles[j][1]
   if j>i+1:assert c==0,(name,i,j,c)
   else:pairs[str(i)+','+str(j)]=str(c)
 total=sum(x[1] for x in singles)+sum(F(v) for v in pairs.values())
 row=dict(name=name,second=list(map(lambda x:str(x[0]),singles)),single_fourth=list(map(lambda x:str(x[1]),singles)),connected_adjacent=pairs,total=str(total));rows.append(row);print(row,flush=True)
vac=F(rows[0]['total'])
for row in rows[1:]:row['excess_vs_vac']=str(F(row['total'])-vac)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
