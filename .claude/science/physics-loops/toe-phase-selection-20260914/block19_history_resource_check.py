from pathlib import Path
import itertools,math,json,hashlib
from fractions import Fraction

def count(d,R):return sum(2**j*math.comb(d,j)*math.comb(R,j) for j in range(min(d,R)+1))
def brute(d,R):return sum(sum(abs(x) for x in v)<=R for v in itertools.product(range(-R,R+1),repeat=d))
def run():
 balls=[]
 for R in range(8):
  b3=count(3,R);b4=count(4,R);assert b3==brute(3,R)==(4*R**3+6*R**2+8*R+3)//3;assert b4==brute(4,R)==(2*R**4+4*R**3+10*R**2+8*R+3)//3
  future=sum(count(3,s) for s in range(R+1));assert 2*future==b4+b3
  balls.append(dict(radius=R,three=b3,four=b4,future=future))
 thresholds=[]
 for C,kappa in ((1,1),(2,8),(3,4),(4,8)):
  R=1
  while count(4,R)<=kappa*count(3,C*R):R+=1
  assert count(4,R)>kappa*count(3,C*R)
  thresholds.append(dict(edge_dilation=C,congestion=kappa,first_full_ball_failure=R,required_sites=count(4,R),capacity=kappa*count(3,C*R)))
 layouts=[]
 for L in (2,3,4,8):
  points=list(itertools.product(range(L),repeat=4));f=lambda v:(v[0],v[1],v[2]+L*v[3]);images={f(v) for v in points};assert len(images)==L**4
  largest=0
  for v in points:
   for mu in range(4):
    if v[mu]+1<L:
     u=list(v);u[mu]+=1;dist=sum(abs(a-b) for a,b in zip(f(v),f(u)));assert dist==(L if mu==3 else 1);largest=max(largest,dist)
  assert largest==L;layouts.append(dict(L=L,events=len(points),sites=len(images),largest_neighbor_distance=largest))
 # A finite exact digit interleaver is a bijection, not finite-precision compression.
 outputs={};m=4
 for seed in range(1<<(2*m)):
  a=sum(((seed>>(2*j))&1)<<j for j in range(m));b=sum(((seed>>(2*j+1))&1)<<j for j in range(m));recovered=sum(((a>>j)&1)<<(2*j) for j in range(m))+sum(((b>>j)&1)<<(2*j+1) for j in range(m));assert recovered==seed
  outputs[a,b]=outputs.get((a,b),0)+1
 assert len(outputs)==256 and set(outputs.values())=={1}
 # Covering-volume exponent for a locally Lipschitz decoder, not a simulation of arbitrary maps.
 exponents=[]
 for native_sites,outdim in ((1,9),(8,65),(10,100)):
  m=8*native_sites;n=outdim;assert n>m
  vals=[Fraction(1,2**k)**(n-m) for k in (1,2,4,8)];assert all(a>b for a,b in zip(vals,vals[1:]));exponents.append(dict(native_sites=native_sites,real_input_dimension=m,output_dimension=n,covering_exponent=n-m))
 return dict(exact_balls=balls,resource_thresholds=thresholds,finite_layouts=layouts,digit_interleaver=dict(seed_bits=8,output_bits_each=4,bijective_outputs=len(outputs)),Lipschitz_covering_exponents=exponents,qualification='Finite arithmetic and layout/codec checks only. General graph and measure-dimension statements rely on the written proof; no native axiom obstruction or full formation law is established.')
if __name__=='__main__':
 result=run();Path(__file__).with_name('BLOCK19_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
