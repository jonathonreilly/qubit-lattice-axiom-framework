from pathlib import Path
import json,itertools
import numpy as np
import sympy as sp
from scipy.linalg import null_space,expm
x=sp.symbols('x:3');pairs=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
def symmetric(v):
 M=sp.zeros(3)
 for a,(i,j) in zip(v,pairs):M[i,j]=M[j,i]=a
 return M

def polynomial_space(degree,kind):
 mon=[sp.prod(x[j]**a[j] for j in range(3)) for a in itertools.product(range(degree+1),repeat=3) if sum(a)==degree]
 coef=sp.symbols('a:'+str(6*len(mon)));M=symmetric([sum(coef[i*len(mon)+l]*v for l,v in enumerate(mon)) for i in range(6)])
 k=sp.Matrix(x)
 polys=list(M*k) if kind in ['vector','vector_trace'] else [(k.dot(k)*sp.trace(M)-(k.T*M*k)[0])]
 if kind=='vector_trace':polys.append(sp.trace(M))
 equations=[]
 for p in polys:equations+=sp.Poly(p,*x).coeffs()
 A=sp.linear_eq_to_matrix(equations,coef)[0];N=A.nullspace()
 return {'degree':degree,'kind':kind,'variables':len(coef),'rank':A.rank(),'nullity':len(N)}

def basis6():
 out=[]
 for i,j in pairs:
  b=np.zeros((3,3));b[i,j]=b[j,i]=1 if i==j else 1/np.sqrt(2);out.append(b)
 return np.array(out)
B=basis6()
def cross(k):
 a,b,c=k;return np.array([[0,-c,b],[c,0,-a],[-b,a,0.]])
def operators(k):
 k=np.asarray(k,dtype=float);Q=cross(k)
 # Two spatial derivatives: R=-Q h Q^T. Positive k^2 on TT.
 R=np.array([[np.sum(a*(-Q@b@Q.T)) for b in B] for a in B])
 G=np.array([b@k for b in B]).T
 tr=np.trace(B,axis1=1,axis2=2)
 S=tr@R
 C=np.stack([Q@(b-np.eye(3)*np.trace(b)/2) for b in B],axis=-1).reshape(9,6)
 K0=np.eye(6)-np.outer(tr,tr)/2
 return R,G,S,C,K0

def mode_checks():
 rows=[]
 for k in [np.array([0.,0.,.7]),np.array([.2,.7,-1.1]),np.array([1.,2.,3.])]:
  R,G,S,C,K0=operators(k);q2=k@k
  assert np.max(abs(G@R))<1e-13 and np.max(abs(G@S))<1e-13
  assert np.max(abs(C@S))<1e-13
  TT=null_space(np.vstack([G,S]))
  assert TT.shape==(6,2)
  assert np.max(abs(TT.T@R@TT-q2*np.eye(2)))<1e-12
  assert np.max(abs(TT.T@C.T@C@TT-q2*np.eye(2)))<1e-12
  J=.7;g=1.3
  spectra=[]
  for name,K,V,power in [('L',J*C.T@C,g*R.T@R,3),('N',J*K0,g*R,1)]:
   KT=TT.T@K@TT;VT=TT.T@V@TT
   F=np.block([[np.zeros((2,2)),KT],[-VT,np.zeros((2,2))]])
   w=np.sort(abs(np.linalg.eigvals(F).imag));expected=np.sqrt(J*g)*q2**(power/2)
   assert np.max(abs(w-expected))<2e-12
   spectra.append({'model':name,'frequencies':w.tolist(),'expected':float(expected)})
  rows.append({'k':k.tolist(),'physical_pairs':TT.shape[1],'spectra':spectra})
 return rows

def scalar_exact():
 J,g,U,V,k=sp.symbols('J g U V k',positive=True)
 K=sp.Matrix([[0,-J/sp.sqrt(2)],[-J/sp.sqrt(2),J/2+U*k*k]])
 b=-g*k*k+2*V*k**4;B=sp.diag(b,0);Z=sp.zeros(2)
 F=Z.row_join(K).col_join((-B).row_join(Z))
 assert sp.simplify(K.det()+J**2/2)==0
 assert sp.simplify(F**4)==sp.zeros(4)
 assert sp.simplify(F**3)!=sp.zeros(4)
 vals={J:sp.Rational(7,10),g:sp.Rational(13,10),U:3,V:5,k:sp.Rational(1,5)}
 A=np.array(F.subs(vals),dtype=float)
 t=1.3;poly=np.eye(4)+t*A+t*t*A@A/2+t**3*A@A@A/6
 assert np.max(abs(expm(t*A)-poly))<1e-14
 return {'kinetic_determinant':str(sp.factor(K.det())),'fourth_power_zero':True,'third_power_generic_nonzero':True,'scalar_characteristic_polynomial':str(F.charpoly().as_expr()),'matrix_exponential_vs_cubic_error':float(np.max(abs(expm(t*A)-poly)))}

def incidence(L):
 sites=list(itertools.product(range(L),repeat=3));ids={x:i for i,x in enumerate(sites)};n=len(sites)
 def sid(x):return ids[tuple(int(a)%L for a in x)]
 def col(x,a):return 6*sid(x)+a
 G=np.zeros((3*n,6*n),dtype=int);S=np.zeros((n,6*n),dtype=int);T=np.zeros_like(S)
 unit=np.eye(3,dtype=int)
 for s,site in enumerate(sites):
  v=np.array(site)
  for j in range(3):
   row=3*s+j;G[row,col(v+unit[j],j)]+=1;G[row,col(v,j)]-=1
   T[s,col(v,j)]=1
   for i in range(3):
    if i==j:continue
    a=pairs.index(tuple(sorted((i,j))));G[row,col(v,a)]+=1;G[row,col(v-unit[i],a)]-=1
    S[s,col(v+unit[i],j)]+=1;S[s,col(v-unit[i],j)]+=1;S[s,col(v,j)]-=2
  for a,(i,j) in enumerate(pairs[3:],3):
   S[s,col(v,a)]-=1;S[s,col(v-unit[i],a)]+=1;S[s,col(v-unit[j],a)]+=1;S[s,col(v-unit[i]-unit[j],a)]-=1
 assert np.max(abs(G@S.T))==0
 return G,S,T,sites

def static_check():
 rows=[]
 for L in [3,5]:
  G,S,T,sites=incidence(L);n=len(sites);A=np.vstack([G,T])
  w=np.tile([1.,1.,1.,2.,2.,2.],n);wi=1/w
  rho=np.zeros(n);rho[0]=1;rho[1]=-1
  b=np.r_[np.zeros(3*n),rho]
  gram=(A*wi)@A.T
  dual=np.linalg.lstsq(gram,b,rcond=1e-12)[0];field=wi*(A.T@dual)
  residual=np.max(abs(A@field-b));assert residual<2e-12
  energy=np.dot(w*field,field)/2
  assert abs(energy-np.dot(rho,rho)/4)<2e-12
  # A second disjoint neutral source; direct bilinear energy tests contact support.
  rho2=np.zeros(n);rho2[-1]=1;rho2[-2]=-1
  b2=np.r_[np.zeros(3*n),rho2]
  dual2=np.linalg.lstsq(gram,b2,rcond=1e-12)[0];field2=wi*(A.T@dual2)
  assert np.max(abs(A@field2-b2))<2e-12
  crossenergy=np.dot(w*field,field2);assert abs(crossenergy)<2e-12
  assert np.max(abs(field))>0
  # Exact commuting clock stabilizers, for every N, follows from integer zero.
  rows.append({'L':L,'sites':n,'integer_G_S_transpose_zero':bool(np.max(abs(G@S.T))==0),'scalar_source_sum':float(rho.sum()),'minimum_energy_over_g':float(energy),'independent_contact_prediction':float(np.dot(rho,rho)/4),'constraint_residual':float(residual),'disjoint_neutral_cross_energy_over_g':float(crossenergy),'constraint_ranks':[int(np.linalg.matrix_rank(G)),int(np.linalg.matrix_rank(S))]})
 return rows

if __name__=='__main__':
 spaces=[polynomial_space(d,t) for t,d in [('vector',0),('vector',1),('vector',2),('scalar',0),('scalar',1),('vector_trace',2),('vector_trace',3)]]
 assert [s['nullity'] for s in spaces]==[0,0,6,0,8,0,5]
 result={'polynomial_spaces':spaces,'mode_spectra':mode_checks(),'finite_penalty_scalar_block':scalar_exact(),'independent_real_space_source_minimization':static_check()}
 p=Path(__file__).with_name('BLOCK5_TENSOR_CHECK.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
