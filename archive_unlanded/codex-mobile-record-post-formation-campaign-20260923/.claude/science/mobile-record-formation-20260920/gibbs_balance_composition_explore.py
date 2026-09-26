"""Scratch exact search: does a local Gibbs rate factor preserve curl exchange balance?"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,random

N=4
sites=list(product(range(N),repeat=3));index={x:i for i,x in enumerate(sites)}
zero=(0,0,0)
labels=[(zero,zero)]+[(tuple(s if i==a else 0 for i in range(3)),zero) for a in range(3) for s in (-1,1)]+[(zero,b) for b in product((-1,1),repeat=3)]
def shift(x,a,d):
 y=list(x);y[a]=(y[a]+d)%N;return tuple(y)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def S(a,b,i):
 e,v=labels[a];f,w=labels[b]
 return F(cross(e,w)[i]+cross(f,v)[i],2)
def h(eta,x,i):
 l,a,b,r=[eta[index[shift(x,i,d)]] for d in (-1,0,1,2)]
 return S(l,a,i)+S(a,r,i)-S(l,b,i)-S(b,r,i)
bonds=[(index[x],index[shift(x,i,1)]) for x in sites for i in range(3)]
def score(eta):return sum(eta[a]==eta[b] for a,b in bonds)
def rates_and_residual(eta):
 C=score(eta);base=F(0);res=F(0);direct=F(0);channels=[]
 for x in sites:
  for i in range(3):
   a=index[x];b=index[shift(x,i,1)]
   if eta[a]==eta[b]:continue
   nxt=list(eta);nxt[a],nxt[b]=nxt[b],nxt[a]
   hh=h(eta,x,i);hr=h(nxt,x,i);assert hr==-hh
   dc=score(nxt)-C;factor=F(2)**dc
   r=(2+hh/2)*factor;reverse=(2+hr/2)/factor
   assert r>0 and reverse>0
   defect=(F(4)**dc)*reverse-r
   assert defect==-hh*factor
   base-=hh;res-=hh*factor;direct+=defect
   if hh:channels.append({'site':x,'axis':i,'h':str(hh),'delta_equal_bonds':dc,'defect':str(defect)})
 assert base==0 and res==direct
 return res,channels
def main():
 rng=random.Random(2109211359);out=Path(__file__).resolve().parent/'campaign12h_second'/'gibbs_composition_exploration';out.mkdir(exist_ok=True)
 trials=[]
 for m in range(2,13):
  for repetition in range(100):
   eta=[0]*len(sites)
   for u in rng.sample(range(len(sites)),m):eta[u]=rng.randrange(1,15)
   residual,channels=rates_and_residual(eta)
   trials.append({'occupied':m,'repetition':repetition,'residual':str(residual)})
   if residual:
    result={'scope':'one exact finite configuration refutes this specified symmetric Gibbs multiplier, not all Gibbs-compatible curl generators','N':N,'occupied':m,'seed':2109211359,'repetition':repetition,'configuration':[[*sites[u],a] for u,a in enumerate(eta) if a],'equal_bond_score':score(eta),'stationarity_residual_divided_by_target_weight':str(residual),'nonzero_bias_channels':channels,'all_trials':trials,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out/'WITNESS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['N','occupied','repetition','configuration','stationarity_residual_divided_by_target_weight']}));return
 raise RuntimeError('No witness found in declared finite search; no theorem follows')
if __name__=='__main__':main()
