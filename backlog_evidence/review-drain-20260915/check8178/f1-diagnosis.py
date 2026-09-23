import sympy as s,json
from fractions import Fraction as F
L=4;sites=[(a,b) for a in range(L) for b in range(L)];U=s.Matrix([[s.I**(-(a*x+b*y))/L for x,y in sites] for a,b in sites]);P=s.zeros(16,16)
for i,(x,y) in enumerate(sites):
 for z in [(x,y),((x-1)%L,y),(x,(y-1)%L)]:P[i,sites.index(z)]+=s.Rational(1,3)
D=s.diag(*[(1+s.I**(-a)+s.I**(-b))/3 for a,b in sites]);E=U*P*U.H;delta=E-D;raw=[(i,j,str(E[i,j]),str(D[i,j]),str(delta[i,j])) for i in range(16) for j in range(16) if E[i,j]!=D[i,j]]
assert E!=D;assert delta.applyfunc(s.expand)==s.zeros(16)
wrong=s.diag(*[(1+s.I**a+s.I**b)/3 for a,b in sites]);wr=(E-wrong).applyfunc(s.expand);assert wr!=s.zeros(16)
# Independent exact Gaussian rational pairs; no symbolic simplification machinery.
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def phase(n):return [(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))][n%4]
def scale(a,c):return(a[0]*c,a[1]*c)
for a,b in sites:
 # Fourier transform of P applied to plane wave exp(+ik.x)
 for c,d in sites:
  val=(F(0),F(0))
  for x,y in sites:
   forward=(F(0),F(0))
   for xx,yy in [(x,y),((x-1)%4,y),(x,(y-1)%4)]:forward=add(forward,scale(phase(a*xx+b*yy),F(1,3)))
   val=add(val,scale(mul(phase(-c*x-d*y),forward),F(1,16)))
  expected=scale(add(add(phase(0),phase(-a)),phase(-b)),F(1,3)) if (a,b)==(c,d) else (F(0),F(0))
  assert val==expected
print(json.dumps(dict(status='RESOLVED structural symbolic equality false negative',sympy_version=s.__version__,raw_mismatch_count=len(raw),raw_mismatches=raw,expanded_residual_all_zero=True,wrong_sign_nonzero_entries=[(i,j,str(wr[i,j])) for i in range(16) for j in range(16) if wr[i,j]!=0],independent_rational_pair_entries_verified=256,production_imports=0,production_baseline_runs=0),indent=2))
