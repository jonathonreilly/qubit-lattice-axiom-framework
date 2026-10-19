"""Exact local canonical short-domain matrix, including bright folded terms."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_rung_model import h
bits=[(b<<1)|(b.bit_count()%2) for b in range(8)];moves=[[(i,int(h[i,j])) for i in range(8) if h[i,j]] for j in range(8)]
N=10;rows=[]
for a in range(8):
 bs=[b for b in range(8) if bits[a]^bits[b] in [6,9]]
 def E(st):return sum(2*(bits[x]^bits[y]).bit_count() for x,y in zip((a,)+st,st+(a,)))
 def V(vec):
  out=defaultdict(F)
  for st,amp in vec.items():
   for j in range(N):
    for new,c in moves[st[j]]:out[st[:j]+(new,)+st[j+1:]]+=c*amp
  return {st:v for st,v in out.items() if v}
 def R(vec,e,k=1):return {st:v/F(e-E(st))**k for st,v in vec.items() if E(st)!=e}
 def data(pos,b):
  ref=(a,)*pos+(b,)*2+(a,)*(N-pos-2);w=R(V({ref:F(1)}),8);y=V(w);b2={st:v for st,v in y.items() if E(st)==8};wb=R(V(b2),8);return w,y,wb
 g=(a,)*N;wg=R(V({g:F(1)}),0);yg=V(wg);e2=yg[g];eg4=sum(v*v/F(-E(st)) for st,v in yg.items() if E(st)!=0)-e2*sum(v*v for v in wg.values())
 data0=[data(4,b) for b in bs];mat=[]
 for left in range(2):
  row=[]
  wl,yl,wbl=data0[left]
  for right in range(2):
   w,y,wb=data0[right]
   direct=sum(v*yl.get(st,0)/F(8-E(st)) for st,v in y.items() if E(st)!=8)
   fold=sum(v*wbl.get(st,0) for st,v in w.items())+sum(v*wl.get(st,0) for st,v in wb.items())
   row.append(direct-fold/2-(eg4 if left==right else 0))
  mat.append(row)
 sym=sum(sum(row) for row in mat)/2
 assert sym==F(-73,192),(a,mat,sym)
 rows.append(dict(background=a,diagonal_colors=bs,ground_fourth=str(eg4),canonical_boundary_matrix=[[str(x) for x in row] for row in mat],symmetric_coefficient=str(sym)))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2));print(rows[0]);print('all8 backgrounds pass')
