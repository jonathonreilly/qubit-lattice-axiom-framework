import numpy as np,itertools,math,json
from collections import defaultdict
L=3;N=L**3
idx=lambda x,y,z:((x%L)*L+y%L)*L+z%L
bonds=[(1<<idx(x,y,z))|(1<<idx(x+(a==0),y+(a==1),z+(a==2))) for a in range(3) for x in range(L) for y in range(L) for z in range(L)]
bs=[bonds[a*N:(a+1)*N] for a in range(3)]
vec=[]
for k in range(5):
 out=defaultdict(int)
 for occ in itertools.combinations(range(N),k):
  s=sum(1<<j for j in occ);out[s]+=N-sum((-1)**((s&m).bit_count()) for m in bs[2])
  for m in bs[0]:out[s^m]-=1
  for m in bs[1]:out[s^m]+=(-1)**((s&m).bit_count())
 vec.append({s:v/math.sqrt(math.comb(N,k)) for s,v in out.items() if v})
S=N/2;dim=N+1;Sp=np.zeros((dim,dim),complex)
# k is down-spin count, raising reduces k
for k in range(1,dim):Sp[k-1,k]=math.sqrt(k*(N-k+1))
Sm=Sp.T;Sx=(Sp+Sm)/2;Sy=(Sp-Sm)/(2j);Sz=np.diag([S-k for k in range(dim)])
A0=(6*N**3-5*N**2+2*N)/16;D4=N*(N-1)*(N-2)*(N-3)/16
op=N*(np.eye(dim)+(sum(np.linalg.matrix_power(s,4) for s in [Sx,Sy,Sz])-A0*np.eye(dim))/D4)
errs=[]
for k in range(5):
 for l in range(5):
  direct=sum(v*vec[l].get(s,0) for s,v in vec[k].items());errs.append(abs(direct-op[k,l]))
assert max(errs)<1e-10
lower=4*N*(N-1)*(N-6)/(3*(N-2)*(N-3));mineig=float(np.linalg.eigvalsh(op)[0]);assert mineig>=lower-1e-10
# direct local-basis coherent pair amplitudes and single-flip cancellation
rng=np.random.default_rng(10618);cerr=[]
for _ in range(12):
 n=rng.normal(size=3);n/=np.linalg.norm(n)
 z=np.array([[1,0],[0,-1]],complex);x=np.array([[0,1],[1,0]],complex);y=np.array([[0,-1j],[1j,0]],complex)
 vals,U=np.linalg.eigh(n[0]*x+n[1]*y+n[2]*z);up=U[:,1];dn=U[:,0];a=np.array([dn.conj()@p@up for p in [x,y,z]])
 one=-2*np.sum(n*a);assert abs(one)<1e-12
 variance=N*np.sum(abs(a)**4);target=N*(1+sum(n**4));cerr.append(float(abs(variance-target)))
assert max(cerr)<1e-10
print(json.dumps(dict(physical_qubits=N,dicke_matrix_entries=25,max_matrix_error=float(max(errs)),minimum_symmetric_leakage_squared=mineig,analytic_lower=lower,coherent_cases=12,max_coherent_error=max(cerr),scope='Exact native H action on low-excitation Dicke vectors and collective spin matrix; not full 27-qubit ED'),indent=2))
# Native dimer product expectation: explicit two-qubit Pauli matrix elements.
x=np.array([[0,1],[1,0]],complex);y=np.array([[0,-1j],[1j,0]],complex);z=np.diag([1,-1]);I=np.eye(2)
theta=.5*np.arcsin(.25);pair=np.array([np.cos(theta),0,0,np.sin(theta)])
xx=float(np.vdot(pair,np.kron(x,x)@pair).real);mz=float(np.vdot(pair,np.kron(z,I)@pair).real)
e=-mz*mz-xx/2;assert abs(e+17/16)<1e-14
# Highest-weight test of exact pair residual at z.
raised=defaultdict(float)
for s,v in vec[0].items():
 for j in range(N):
  if (s>>j)&1:raised[s^(1<<j)]+=v
assert max(abs(v) for v in raised.values())<1e-12
print(json.dumps(dict(dimer_energy_per_site=e,highest_weight_residual=max(abs(v) for v in raised.values()),scope='Variational energy and exact first spin channel, not a ground-state phase solution')))
