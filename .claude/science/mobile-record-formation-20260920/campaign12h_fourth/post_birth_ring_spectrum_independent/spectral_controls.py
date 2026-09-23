from pathlib import Path
import ast,hashlib,json,math,itertools
import numpy as np
import sympy as sp
from scipy.linalg import eigh
D=Path(__file__).resolve().parent
p=D/'ring_control.py';assert hashlib.sha256(p.read_bytes()).hexdigest()=='b082190bf88df120577cf9337a4edee200e1306a96bcd05d8bcfedd4978e5bf9'
# Reuse only our already executed function definitions, without rerunning its outputs.
module=ast.parse(p.read_text());ns={'np':np,'sp':sp,'math':math,'itertools':itertools}
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),str(p),'exec'),ns)
fiber=ns['fiber'];form_q=ns['form_q'];factor=ns['factor_modes']
rows=[]
for theta in (0.,.37,.79,1.19):
 ps,H=fiber(4,theta);ev,V=eigh(H)
 a=np.zeros(36);a[ps.index(form_q(4,1))]=1
 b=a.copy();b[ps.index(form_q(4,-1))]=1;b/=math.sqrt(2)
 flat=abs(ev+4)<1e-10;lowest=abs(ev-ev[0])<1e-10
 wa=abs(V.conj().T@a)**2;wb=abs(V.conj().T@b)**2
 rows.append({'theta':theta,'center_eigenvalue_multiplicity':int(sum(flat)),'resolved_center_energy_weight':float(sum(wa[flat])),'coherent_center_energy_weight':float(sum(wb[flat])),'lowest_eigenvalue':float(ev[0]),'lowest_multiplicity':int(sum(lowest)),'resolved_lowest_weight':float(sum(wa[lowest])),'coherent_lowest_weight':float(sum(wb[lowest]))})
 if theta:
  assert sum(flat)==12 and abs(sum(wa[lowest])-sp.Rational(1,48))<2e-13
  assert sum(wb[lowest])<1/24+2e-13
 else:
  assert sum(flat)==14 and abs(sum(wa[flat])-13/24)<2e-13 and abs(sum(wb[flat])-7/12)<2e-13

# Exact full 36-dimensional microscopic characteristic polynomial at theta=0.
ps,H=fiber(4,0.);assert np.max(abs(H.imag))==0 and np.all(H.real==np.rint(H.real))
e=sp.symbols('e');poly=sp.Matrix(H.real.astype(int)).charpoly(e).as_expr();x=e+4
expected=sp.expand(x**12*8192*(sp.chebyshevt(24,x/(2*sp.sqrt(2)))-1))
assert sp.expand(poly-expected)==0
# Complete six-dimensional charge block fourth moment, with a symbolic twist.
z=sp.symbols('z',nonzero=True);pairs=list(itertools.combinations(range(4),2));ix={q:i for i,q in enumerate(pairs)};C=sp.zeros(6)
for j,q in enumerate(pairs):
 for a in q:
  for direction in (-1,1):
   b=(a+direction)%4
   if b in q:continue
   target=tuple(sorted((set(q)-{a})|{b}));amp=z if(a,b)==(0,3)else 1/z if(a,b)==(3,0)else 1
   C[ix[target],j]+=amp
m4=sp.expand((C**4)[ix[(0,3)],ix[(0,3)]])
assert sp.simplify(m4-(12+2*(z+1/z)))==0

# Wrong boundary phase countercontrol: removing fermionic pi changes the full eigenproblem.
L=4;theta=.37;ps,H=fiber(L,theta);N=L+2;wrong=[]
for j in range(N):
 phi=(L*theta+2*math.pi*j)/N
 for m,n in itertools.combinations(range(L),2):
  km=(2*math.pi*m+phi)/L;kn=(2*math.pi*n+phi)/L
  v=[]
  for q in ps:
   occ=[x for x,c in enumerate(q) if c];r=occ.index(q.index(-1));B=[i for i in range(L) if q[2*i+1]]
   v.append(np.exp(1j*r*(phi-theta))/math.sqrt(N)*(np.exp(1j*(km*B[0]+kn*B[1]))-np.exp(1j*(kn*B[0]+km*B[1])))/L)
  energy=-4-2*math.cos(km)-2*math.cos(kn)
  wrong.append(float(np.linalg.norm(H@v-energy*np.array(v))))
assert max(wrong)>1
out={'L4_fiber_energy_and_band_weights':rows,'L4_exact_full_characteristic_polynomial_theta_zero':str(sp.factor(poly)),'L4_exact_charge_centered_fourth_moment':str(m4),'wrong_fermion_boundary_phase_max_eigenvector_residual':max(wrong),'read_boundary':'Only this independent packet functions are reused; no fourth-campaign author source is imported or read.'}
(D/'SPECTRAL_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
