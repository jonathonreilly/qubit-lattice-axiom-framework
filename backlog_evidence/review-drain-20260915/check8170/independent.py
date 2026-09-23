"""Independent bounded controls. Standard library only; no original runner import.
Limits: k<=150 integer convolution, no simulation, no primary/audit execution.
"""
from fractions import Fraction as F
from math import sinh,tanh,sqrt,pi,log,factorial
from collections import defaultdict
import json,pathlib,re,time
start=time.monotonic()
# Exact sign witness: sinh(1)^2 > 1+1/3+2/45 > 4/3, hence A'(1)>1/4.
print('Derivative upper-bound counterexample: exact sinh(1)^2 lower=',F(1)+F(1,3)+F(2,45),'>',F(4,3))
assert F(1)+F(1,3)+F(2,45)>F(4,3)
print('Numerical illustration A_prime(1)=',1-1/sinh(1)**2,'claimed upper=',1/4)
# Replacement proof coefficients for ((x^2+3)sinh x - 3x cosh x).
for n in range(1,21):
 actual=F(1,factorial(2*n-1))+F(3,factorial(2*n+1))-F(3,factorial(2*n))
 assert actual==F(4*n*(n-1),factorial(2*n+1))
print('Langevin replacement series coefficients: 4n(n-1)/(2n+1)!; positive n>=2; finite coefficient check n<=20')
for beta in (F(1,3),3,6,12,24):
 k=float(3*beta); gain=1/tanh(k)-1/k
 print('Common transverse rotation exact conditional mean gain',str(beta),gain,'not 1')
# Independent recurrence of path counts, not multinomial formula used by primary.
counts={(0,0):1}; cum=F(0); harmonic=F(0);c=3*sqrt(3)/(4*pi);worst=0
for k in range(1,151):
 nxt=defaultdict(int)
 for (a,b),v in counts.items():
  for pos in ((a,b),(a-1,b),(a,b-1)):nxt[pos]+=v
 counts=nxt;p=F(sum(v*v for v in counts.values()),9**k);cum+=p;harmonic+=F(1,k)
 deficit=c*float(harmonic)-float(cum);worst=max(worst,deficit)
 assert deficit<.24
print('Independent recurrence k<=150 harmonic deficit maximum (float comparison)=',worst,'final=',deficit,'kP_k=',150*float(p))
print('Upper summation including P0:',1+27*pi*pi/6+98,'<150')
# Explicit exact directed mean map: all three predecessors rotate together by theta.
# mean transverse=A(3beta)sin(theta), derivative A(3beta). Normalized mean direction derivative=1.
root=pathlib.Path('/private/tmp/review-drain-20260915/drain8170-original/source/.claude/science/physics-loops/admissibility-induced-law-20260906/specs')
for name in ('sphere_sim','refuter','sixaxis_sim'):
 text=(root/f'supervisor_control_block26_{name}.out.txt').read_text()
 print('Historical raw output',name,'lines',len(text.splitlines()),'sections',len(re.findall(r'^=====',text,re.M)))
 if name=='sphere_sim':
  pairs=[tuple(map(float,m)) for m in re.findall(r'\|m\|=([0-9.]+)\s+m_z=(-?[0-9.]+)',text)]
  print('Largest reported norm-minus-projection in sphere controls=',max(a-b for a,b in pairs))
print('Fit expected split files present=',len(list(root.glob('sim_b*_L*_T*.txt')))+len(list(root.glob('ref_sphere_b*_L*.txt'))))
print('Wall_seconds',time.monotonic()-start)
