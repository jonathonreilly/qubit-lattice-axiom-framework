from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
from math import factorial
import json,time
start=time.monotonic();base=Path(__file__).parent/'8056/original/.claude/science/physics-loops/native-uniform-cubic-flux-defect-stiffness-20260908/RAW_CANDIDATES';cube=json.loads((base/'CUBE_INPUTS.json').read_text());trig=json.loads((base/'TRIG_INPUTS.json').read_text());rows=cube['rows'];lookup={tuple(x['face_signs']):x['id'] for x in rows};assert len(lookup)==32
classes={}
for row in rows:
 s=row['face_signs'];orb=set()
 for p in permutations(range(3)):
  for flips in product((0,1),repeat=3):orb.add(tuple(s[2*p[j]+(k^flips[j])] for j in range(3) for k in range(2)))
 rep=min(lookup[x] for x in orb);assert rep==row['symmetry_representative'];classes.setdefault(rep,set()).add(row['id'])
assert sorted(classes)==[0,1,3,5,10,15]
def atan(inv):
 terms=[F((-1)**k,(2*k+1)*inv**(2*k+1)) for k in range(57)];s=sum(terms[:-1]);return min(s,s+terms[-1]),max(s,s+terms[-1])
a,b=atan(5);c,d=atan(239);lo=16*a-4*d;hi=16*b-4*c;assert F(trig['pi_lower_numerator'],trig['pi_denominator'])<=lo<=hi<=F(trig['pi_upper_numerator'],trig['pi_denominator'])
for row in trig['rows']:
 j=row['j'];x=(lo+hi)*F(2*j+1,128);rad=(hi-lo)*F(2*j+1,128);s=sum(F((-1)**k,factorial(2*k+1))*x**(2*k+1) for k in range(50));err=abs(x)**101/factorial(101)+rad
 assert F(row['lower_numerator'],row['denominator'])<=2*(s-err)<=2*(s+err)<=F(row['upper_numerator'],row['denominator'])
out={'scope':'Independent exact signed-face orbit census and higher-order rational Machin/sine enclosures; no canonical generator import or physical grid run','classes':{k:sorted(v) for k,v in classes.items()},'trig_intervals_verified':32,'pi_verified':True,'seconds':time.monotonic()-start};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
