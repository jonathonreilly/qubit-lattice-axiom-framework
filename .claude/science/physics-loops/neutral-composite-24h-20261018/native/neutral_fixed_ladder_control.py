import numpy as np, math, json
rng=np.random.default_rng(1831);N=6
Phi=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));Phi=(Phi+Phi.T)/2;np.fill_diagonal(Phi,0);Phi/=np.linalg.norm(Phi)
Xi=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));Xi=(Xi+Xi.T)/2;np.fill_diagonal(Xi,0);Xi/=np.linalg.norm(Xi)
def act(state,M,spin=False):
 out={}
 for occ,amp in state.items():
  for i in range(N):
   for j in range(i+1,N):
    if spin and (occ[i] or occ[j]):continue
    n=list(occ);n[i]+=1;n[j]+=1;n=tuple(n)
    out[n]=out.get(n,0j)+amp*np.sqrt(2)*M[i,j]*np.sqrt((occ[i]+1)*(occ[j]+1))
 return out
def dot(a,b):return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())
rho=Phi.conj().T@Phi;z=[1.];dz=[0.];power=np.eye(N,dtype=complex);tr=[0.];mix=[0.]
for k in range(1,5):
 mix.append(np.trace(power@Phi.conj().T@Xi));power=power@rho;tr.append(np.trace(power))
for m in range(1,5):
 z.append(sum(2**(k-1)*tr[k]*z[m-k] for k in range(1,m+1))/m)
 dz.append(sum(2**(k-1)*mix[k]*z[m-k] for k in range(1,m+1)))
bos={(0,)*N:1.};spin=bos.copy();rows=[]
for m in range(1,5):
 Fprev=act(bos,Xi);Sprev=act(spin,Xi,True);bos=act(bos,Phi);spin=act(spin,Phi,True)
 exact=dot(bos,bos);form=math.factorial(m)**2*z[m];mixed=dot(bos,Fprev);mf=math.factorial(m)*math.factorial(m-1)*dz[m]
 hc={k:v for k,v in bos.items() if max(k)<=1};projerr=sum(abs(hc.get(k,0)-spin.get(k,0))**2 for k in hc.keys()|spin.keys())
 assert abs(exact-form)<1e-10 and abs(mixed-mf)<1e-10 and projerr<1e-20
 rows.append(dict(m=m,boson_norm=float(exact.real),spin_norm=float(dot(spin,spin).real),norm_identity_error=float(abs(exact-form)),mixed_identity_error=float(abs(mixed-mf)),hardcore_projection_error=float(projerr)))
# Independent disjoint-pair algebra family, not a native Hamiltonian calculation.
dilute=[]
for pairs in [8,32,128,512]:
 for m in [2,3,4]:
  norm=math.factorial(m)*math.prod(1-j/pairs for j in range(m));vertex=np.sqrt(m*(1-(m-1)/pairs));dilute.append(dict(pairs=pairs,m=m,norm=norm,vertex=float(vertex),relative_vertex= float(vertex/np.sqrt(m))))
print(json.dumps(dict(status='bounded-support',random_pair_controls=rows,disjoint_pair_algebra_only=dilute,scope='Algebra device only; no additional physical site modes or native many-particle numerical spectrum'),indent=2))
