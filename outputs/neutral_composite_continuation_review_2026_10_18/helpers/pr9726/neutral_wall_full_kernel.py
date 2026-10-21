from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_rung_model import h
bits=[(b<<1)|(b.bit_count()%2) for b in range(8)];moves=[[(i,int(h[i,j])) for i in range(8) if h[i,j]] for j in range(8)]
N=10;rows=[]
for a in range(8):
 for b in range(8):
  if bits[a]^bits[b] not in [6,9]:continue
  def E(st):return sum(2*(bits[x]^bits[y]).bit_count() for x,y in zip((a,)+st,st+(b,)))
  def V(vec):
   out=defaultdict(F)
   for st,amp in vec.items():
    for j in range(N):
     for new,c in moves[st[j]]:out[st[:j]+(new,)+st[j+1:]]+=c*amp
   return {st:v for st,v in out.items() if v}
  def calc(pos):
   ref=(a,)*pos+(b,)*(N-pos);e0=E(ref);vd=V({ref:F(1)});w={st:v/F(e0-E(st)) for st,v in vd.items() if E(st)!=e0};y=V(w)
   b2={st:v for st,v in y.items() if E(st)==e0};assert b2=={ref:-F(N,2)-1},(a,b,pos,b2)
   return w,y
  w,y=calc(5);kernel={}
  for shift in [-2,-1,0,1,2]:
   wl,yl=calc(5+shift)
   direct=sum(v*yl.get(st,0)/F(4-E(st)) for st,v in y.items() if E(st)!=4)
   fold=(-F(N,2)-1)*sum(v*wl.get(st,0) for st,v in w.items());kernel[str(shift)]=str(direct-fold)
  assert kernel['-2']==kernel['2']=='-3/64' and kernel['-1']==kernel['1']=='0'
  rows.append(dict(a=a,b=b,kernel=kernel))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2));print(rows[0]);print('all16 local wall kernels pass')
