"""Exact Pauli controls; infinite-temperature ensemble is an explicit premise."""
import numpy as np,json
from collections import defaultdict

def mul(p,q):return (p[0]^q[0],p[1]^q[1]),(-1 if (p[1]&q[0]).bit_count()%2 else 1)
def comm(A,B):
 out=defaultdict(complex)
 for p,a in A.items():
  for q,b in B.items():
   if ((p[0]&q[1]).bit_count()+(p[1]&q[0]).bit_count())%2:
    r,s=mul(p,q);out[r]+=2*s*a*b
 return {p:a for p,a in out.items() if abs(a)>1e-12}
def inner(A,B):return sum(np.conj(a)*B.get(p,0) for p,a in A.items())
def model(L,J=(1.,1.,1.),q=(0.,0.,0.)):
 H={};Hs=[{} for _ in range(3)];Eq={};C={};V=L**3
 for r in np.ndindex(L,L,L):
  i=np.ravel_multi_index(r,(L,L,L))
  for a in range(3):
   s=list(r);s[a]=(s[a]+1)%L;j=np.ravel_multi_index(tuple(s),(L,L,L));bits=(1<<int(i))|(1<<int(j))
   p=(bits,0) if a==0 else ((bits,bits) if a==1 else (0,bits));v=J[a] if a==1 else -J[a]
   center=np.array(r,dtype=float);center[a]+=.5;H[p]=v;Hs[a][p]=v;Eq[p]=v*np.exp(-1j*np.dot(q,center))/np.sqrt(V)
  s=list(r);s[2]=(s[2]+2)%L;j=np.ravel_multi_index(tuple(s),(L,L,L));C[(0,(1<<int(i))|(1<<int(j)))]=1
 return H,Hs,Eq,C

def run():
 rows=[]
 for L,J,k in [(5,(1,1,1),(1,0,0)),(5,(.7,1.2,1.5),(1,2,1)),(6,(1,1,1),(1,1,0))]:
  q=2*np.pi*np.array(k)/L;H,Hs,E,C=model(L,J,q);K=comm(H,E);m0=float(inner(E,E).real);m2=float(inner(K,K).real);pred=32*sum(J[a]**2*J[b]**2*(1-np.cos(q[a]/2)*np.cos(q[b]/2)) for a in range(3) for b in range(a+1,3))
  assert abs(m0-sum(x*x for x in J))<1e-10 and abs(m2-pred)<1e-9
  Qq=defaultdict(complex)
  for Ha in Hs:
   Haq={p:E[p] for p in Ha}
   for p,v in comm(Ha,comm(H,Haq)).items():Qq[p]+=v
  g=inner(E,Qq).real/m0;gp=-32*sum(J[a]**2*J[b]**2*np.cos(q[a]/2)*np.cos(q[b]/2) for a in range(3) for b in range(a+1,3))/m0
  assert abs(g-gp)<1e-9
  rows.append(dict(L=L,J=J,k=k,m0=m0,m2=m2,predicted_m2=pred,distinct_current_strings=len(K),Qq_overlap=g,predicted_overlap=gp,Qq_norm=float(inner(Qq,Qq).real)))
 H,Hs,E,C=model(5);Q=defaultdict(complex)
 for Ha in Hs:
  for p,v in comm(Ha,comm(H,Ha)).items():Q[p]+=v
 Q={p:v for p,v in Q.items() if abs(v)>1e-12};V=125;overlap=inner(H,Q).real;var=inner(H,H).real;g=overlap/var;qvar=inner(Q,Q).real
 # H^2 overlap with distance-two source, exact Pauli coefficient accumulation.
 ch2=0
 for p,a in H.items():
  for q,b in H.items():
   r,s=mul(p,q);ch2+=C.get(r,0)*s*a*b
 assert abs(g+32)<1e-10 and ch2==2*V and inner(C,H)==0
 return dict(status='PASS',moments=rows,Q_terms=len(Q),Q_variance_per_site=qvar/V,energy_projection=g,conserved_weight_per_site=g*g*var/V,conserved_fraction=g*g*var/qvar,C_H2_per_site=ch2/V,scope='Exact Pauli traces in supplied infinite-temperature state; no retarded susceptibility, ground excitation or empirical identification')
if __name__=='__main__':
 r=run();print(json.dumps(r,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(r,indent=2)+'\n')
