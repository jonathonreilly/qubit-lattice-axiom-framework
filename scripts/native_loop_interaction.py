#!/usr/bin/env python3
"""Exact finite coefficient checks, not a full microscopic potential test."""
from pathlib import Path
import sys,json,itertools,hashlib
from fractions import Fraction as F
from math import comb
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_simple_loop.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rectangle_range.py']
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0,str(PACK))
from neutral_simple_loop import coeff,closed
from neutral_rectangle_range import coefficient

def colored_source(colors,reference):
 n=len(colors);masks=[(1<<j)|(1<<((j+1)%n)) for j in range(n)];states=[0]*(1<<n);dp=[F(0)]*(1<<n);der=[F(0)]*(1<<n);dp[0]=F(1)
 for s in range(1,1<<n):
  bit=s&-s;states[s]=states[s^bit]^masks[bit.bit_length()-1]
 for s in range((1<<n)-1):
  for j,t in enumerate(colors):
   if s>>j&1:continue
   ss=s|(1<<j);amp=(-1)**(((states[s]^reference)&masks[j]).bit_count()) if t else -1
   value=dp[s]*amp;dv=der[s]*amp
   if ss!=(1<<n)-1:
    flips=states[ss].bit_count();den=-4*flips;slope=4*flips
    dv=dv/den-value*slope/den**2;value/=den
   dp[ss]+=value;der[ss]+=dv
 return dp[-1],der[-1]
def run():
 cycle_rows=[]
 for n in [4,6,8]:
  values={}
  for colors in itertools.product([0,1],repeat=n):
   c=sum(colors[j]!=colors[(j+1)%n] for j in range(n));got=coeff(colors);assert got==closed(n,c);values[c]=str(got)
  cycle_rows.append(dict(n=n,color_assignments=2**n,coefficients=values))
 rect=[]
 for r in range(1,8):
  c=coefficient(r);formula=-F(6*comb(4*r-2,2*r-1),4**r*(2*r)*(2*r+1));assert c==formula
  rect.append(dict(width=r,coefficient=str(c),bulk_K=str(-c/4**(2*r+1))))
 reference_checks=0
 for colors in [(0,1,0,1),(0,0,1,0,0,1),(0,0,0,1,0,0,0,1),(0,0,1,0,1,0,0,1)]:
  n=len(colors);corners=[j for j in range(n) if colors[j-1]!=colors[j]];base=closed(n,len(corners))/4**(n-1)
  for ref in range(1<<n):
   val,der=colored_source(colors,ref);parity=(-1)**sum((ref>>j)&1 for j in corners)
   assert val==parity*base and der==(n-1)*val
   reference_checks+=1
 result=dict(status='PASS',cycles=cycle_rows,rectangles=rect,reference_and_source_checks=reference_checks,scope='Distinct-edge formal coefficients and source derivatives only; full-H remainder and empirical identification open')
 out=ROOT/'outputs/native_loop_interaction/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
