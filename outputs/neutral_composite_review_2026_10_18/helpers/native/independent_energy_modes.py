from pathlib import Path
import json
from fractions import Fraction
src=(Path(__file__).parent/'independent_transport.py').read_text();exec(src[:src.index('A={}')])
A={}
for a in range(3):
 for sign in [-1,1]:
  p=[0,0,0];p[a]=sign;A[pauli(((0,0,0),tuple(p)),a)]=1
root=(Path(__file__).parent/'compass_energy_modes.json')
expected=json.loads(root.read_text());rows=[]
for n in range(3):
 values=corr(A);target={tuple(v['r']):v['value']for v in expected['rows'][n]['kernel']};assert values==target
 quadratic=[-sum(Fraction(v*r[a]**2,8)for r,v in values.items()) for a in range(3)]
 rows.append({'n':n,'entries':len(values),'physical_e_kernel_q2_coefficients':[str(v)for v in quadratic]})
 if n<2:A=D(A)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
