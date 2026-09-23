from pathlib import Path
import itertools,math,json
import numpy as np
import sympy as sp
from scipy.linalg import eigh
D=Path(__file__).resolve().parent

def states_P(L):
 n=2*L;out=[]
 for occupied_B in itertools.combinations(range(L),2):
  occupied=sorted(list(range(0,n,2))+[2*j+1 for j in occupied_B])
  for minus in occupied:
   q=[0]*n
   for x in occupied:q[x]=1
   q[minus]=-1;out.append(tuple(q))
 return out

def charge_hops(q):
 n=len(q)
 for x,c in enumerate(q):
  if not c:continue
  for s in (-1,1):
   y=(x+s)%n
   if q[y]:continue
   e=x if s==1 else y
   r=list(q);r[x]=0;r[y]=c
   yield tuple(r),e,-s*c

def fiber(L,theta):
 ps=states_P(L);ix={q:i for i,q in enumerate(ps)}
 H=np.zeros((len(ps),len(ps)),complex)
 for col,q in enumerate(ps):
  for r,e,de in charge_hops(q):
   for s,f,df in charge_hops(r):
    if s not in ix:continue
    shift=(de if e==2*L-1 else 0)+(df if f==2*L-1 else 0)
    H[ix[s],col]-=np.exp(1j*theta*shift)
 assert np.max(abs(H-H.conj().T))<2e-14
 assert np.max(abs(np.diag(H)+2*(L-2)))<2e-14
 return ps,H

def form_q(L,charge):
 q=[1 if x%2==0 else 0 for x in range(2*L)]
 q[-1]=1;q[0]=charge;q[1]=-charge
 return tuple(q)

def factor_modes(L,theta,ps):
 N=L+2;cols=[];energies=[];labels=[]
 for j in range(N):
  phi=(L*theta+2*math.pi*j)/N
  for m,n in itertools.combinations(range(L),2):
   km=(2*math.pi*m+math.pi+phi)/L;kn=(2*math.pi*n+math.pi+phi)/L
   v=[]
   for q in ps:
    C=[i for i in range(L) if q[2*i+1]]
    occupied=[x for x,c in enumerate(q) if c];r=occupied.index(q.index(-1))
    spin=np.exp(1j*r*(phi-theta))/math.sqrt(N)
    slater=(np.exp(1j*(km*C[0]+kn*C[1]))-np.exp(1j*(kn*C[0]+km*C[1])))/L
    v.append(spin*slater)
   cols.append(v);energies.append(-2*(L-2)-2*math.cos(km)-2*math.cos(kn));labels.append((j,m,n,phi))
 return np.array(cols).T,np.array(energies),labels

rows=[]
for L in (3,4,5,6,7):
 for theta in (0.,.37,1.19):
  ps,H=fiber(L,theta);V,E,labels=factor_modes(L,theta,ps)
  orth=float(np.max(abs(V.conj().T@V-np.eye(len(ps)))))
  err=float(np.max(abs(H@V-V*E)))
  assert orth<2e-13 and err<2e-13,(L,theta,orth,err)
  resolved=np.zeros(len(ps));resolved[ps.index(form_q(L,1))]=1
  coherent=resolved.copy();coherent[ps.index(form_q(L,-1))]=1;coherent/=math.sqrt(2)
  wr=abs(V.conj().T@resolved)**2;wc=abs(V.conj().T@coherent)**2
  pr=[];pc=[]
  for j,m,n,phi in labels:
   w=4/L**2*math.sin(math.pi*(m-n)/L)**2
   pr.append(w/(L+2));pc.append(w*(1+math.cos(phi-theta))/(L+2))
  assert np.max(abs(wr-pr))<2e-14 and np.max(abs(wc-pc))<2e-14
  flat=[a for a,(_,m,n,_) in enumerate(labels) if L%2==0 and abs(m-n)==L//2]
  flatwr=float(np.sum(wr[flat]));flatwc=float(np.sum(wc[flat]))
  assert abs(flatwr-(2/L if L%2==0 else 0))<2e-14
  assert abs(flatwc-(2/L if L%2==0 else 0))<2e-14
  C=H+2*(L-2)*np.eye(len(ps))
  for v in (resolved,coherent):
   assert abs(np.vdot(v,C@v))<1e-13 and abs(np.vdot(v,C@C@v)-2)<1e-13
  rows.append({'L':L,'theta':theta,'P_dimension':len(ps),'mode_orthogonality_error':orth,'full_eigenvector_residual':err,'resolved_weight_error':float(np.max(abs(wr-pr))),'coherent_weight_error':float(np.max(abs(wc-pc))),'resolved_flat_weight':flatwr,'coherent_flat_weight':flatwc,'spectrum_min':float(min(E)),'spectrum_max':float(max(E))})

# Exact six-dimensional two-hard-core-particle charge block for L=4.
z,x=sp.symbols('z x',nonzero=True);pairs=list(itertools.combinations(range(4),2));ix={p:i for i,p in enumerate(pairs)}
C=sp.zeros(6)
for col,p in enumerate(pairs):
 for a in p:
  for step in (-1,1):
   b=(a+step)%4
   if b in p:continue
   amp=z if (a,b)==(0,3) else 1/z if (a,b)==(3,0) else 1
   q=tuple(sorted((set(p)-{a})|{b}));C[ix[q],col]+=amp
char=sp.factor(C.charpoly(x).as_expr())
assert sp.simplify(char-x*x*(x**4-8*x*x+8-4*(z+1/z)))==0

# Direct physical-field moments without a field cutoff or fiber matrices.
def valid(q,E):
 return all(E[e]-E[(e-1)%len(q)]+(e%2==0)==q[e] for e in range(len(q)))
def physical_hops(s):
 q,E=s
 for r,e,de in charge_hops(q):
  F=list(E);F[e]+=de;z=(r,tuple(F));assert valid(*z);yield z

def centered_action(L,v):
 out={}
 for s,a in v.items():
  for t in physical_hops(s):
   for z in physical_hops(t):
    if any(z[0][e]==0 for e in range(0,2*L,2)):continue
    out[z]=out.get(z,0)-a
  out[s]=out.get(s,0)+2*(L-2)*a
 return {s:sp.simplify(a) for s,a in out.items() if a!=0}
def make_form(L,field,coherent):
 out={};q0=tuple(1 if x%2==0 else 0 for x in range(2*L))
 for f,coef in field.items():
  s=(q0,(f,)*(2*L))
  for t in physical_hops(s):
   if t[0][0] or t[0][1]:continue
   for c in ((1,-1) if coherent else (1,)):
    q=list(t[0]);q[0]=c;q[1]=-c;E=list(t[1]);E[0]+=c
    z=(tuple(q),tuple(E));assert valid(*z)
    out[z]=out.get(z,0)+coef/(sp.sqrt(2) if coherent else 1)
 assert sp.simplify(sum(sp.conjugate(a)*a for a in out.values()))==1
 return out
mom=[]
for L in (3,4,5,6):
 for label,field in [('one_flux',{0:sp.Integer(1)}),('plus_neighbor_flux',{0:1/sp.sqrt(2),1:1/sp.sqrt(2)}),('minus_neighbor_flux',{0:1/sp.sqrt(2),1:-1/sp.sqrt(2)})]:
  for coh in (False,True):
   v=make_form(L,field,coh);w=v;ms=[]
   for k in range(7):
    val=sp.simplify(sum(sp.conjugate(a)*w.get(s,0) for s,a in v.items()));ms.append(str(val))
    if k<6:w=centered_action(L,w)
   assert ms[1]=='0' and ms[2]=='2'
   mom.append({'L':L,'field':label,'coherent':coh,'centered_moments_0_to_6':ms})

out={'fiber_factorization_and_weights':rows,'L4_exact_charge_characteristic_polynomial':str(char),'physical_formation_moments':mom,'scope':'Independent legal-hop reconstruction, explicit spin/Slater eigenvectors, and exact untruncated physical-field moments. No fourth-campaign author source read.'}
(D/'RING_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
