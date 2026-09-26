#!/usr/bin/env python3
"""Exact local encoding/moments and Fourier energy controls; finite Gaussian checks."""
from pathlib import Path
from itertools import product,permutations
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parent
I=s.I

def unit(i,j):
 a=s.zeros(4);a[i,j]=1;return a
A=[unit(0,i)+unit(i,0) for i in range(1,4)]
B=[I*(unit(i,0)-unit(0,i)) for i in range(1,4)]
O=A+B
q=s.Rational(1,2);r=s.Rational(1,6);la=s.Rational(1,8);lb=s.Rational(1,16)
rho0=s.diag(q,r,r,r)
J=s.zeros(6);J[:3,3:]=s.eye(3);J[3:,:3]=-s.eye(3)
colors=[]
for i in range(3):
 for sign in (-1,1):
  e=s.zeros(3,1);e[i]=sign;colors.append((tuple(e),tuple([0]*3)))
colors += [(tuple([0]*3),b) for b in product((-1,1),repeat=3)]

def rho(e,b):
 w=la*s.Matrix(e)+I*lb*s.Matrix(b)
 ans=s.diag(q,r,r,r);ans[1:,0]=w;ans[0,1:]=w.conjugate().T;return ans

def rotations():
 out=[]
 for perm in permutations(range(3)):
  for signs in product((-1,1),repeat=3):
   R=s.zeros(3)
   for j in range(3):R[perm[j],j]=signs[j]
   if R.det()==1:out.append(R)
 assert len(out)==24;return out

def local_controls():
 pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
 sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
 T=s.Matrix.hstack(sing,*[s.kronecker_product(x,s.eye(2))*sing for x in pauli])
 assert s.simplify(T.H*T)==s.eye(4)
 S1=[s.kronecker_product(x,s.eye(2)) for x in pauli];S2=[s.kronecker_product(s.eye(2),x) for x in pauli]
 for i in range(3):
  assert s.simplify(T.H*(S1[i]-S2[i])*T/2)==A[i]
  cross=sum((s.LeviCivita(i,j,k)*S1[j]*S2[k] for j in range(3) for k in range(3)),s.zeros(4))
  assert s.simplify(-T.H*cross*T/2)==B[i]
 states={c:rho(*c) for c in colors};state_rows=[]
 for (e,b),state in states.items():
  assert state==state.H and s.trace(state)==1
  w=state[1:,0];schur=s.simplify(q-(w.H*w)[0]/r);assert schur>0
  means=[s.simplify(s.trace(state*x)) for x in O]
  assert means==[2*la*x for x in e]+[2*lb*x for x in b]
  swap=s.diag(-1,1,1,1)
  assert swap*state*swap==states[(tuple(-x for x in e),tuple(-x for x in b))]
  state_rows.append(dict(e=list(map(int,e)),b=list(map(int,b)),schur=str(schur),means=list(map(str,means))))
 count=0
 for R in rotations():
  U=s.diag(1,R)
  for (e,b),state in states.items():
   target=(tuple(R*s.Matrix(e)),tuple(R*s.Matrix(b)))
   assert U*state*U.T==states[target];count+=1
 F=s.Matrix.hstack(*[s.Matrix([*e,*b]) for e,b in colors]);assert F.rank()==6
 tangent=s.Matrix.hstack(*[s.Matrix(16,1,states[c]-states[colors[0]]) for c in colors[1:]])
 assert tangent.rank()==6
 QQ,RR=s.symbols('q r',real=True);base=s.diag(QQ,RR,RR,RR)
 V=s.Matrix(6,6,lambda i,j:s.simplify(s.trace(base*(O[i]*O[j]+O[j]*O[i]))/2))
 Sigma=s.Matrix(6,6,lambda i,j:s.simplify(-I*s.trace(base*(O[i]*O[j]-O[j]*O[i]))))
 assert V==(QQ+RR)*s.eye(6) and Sigma==2*(QQ-RR)*J
 eigs=(V+I*Sigma/2).eigenvals();assert eigs=={2*QQ:3,2*RR:3}
 assert Sigma.subs({QQ:s.Rational(1,4),RR:s.Rational(1,4)})==s.zeros(6)
 return dict(exact_states=state_rows,rotation_state_equalities=count,population_tangent_rank=6,
   exact_covariance=str(V),exact_commutator_form=str(Sigma),quantum_covariance_eigenvalues={str(k):v for k,v in eigs.items()},
   physical_Pauli_identities=6,tracial_commutator_zero=True)

def fluctuation_controls():
 base=np.array(rho0,dtype=complex);ops=[np.array(x,dtype=complex) for x in O]
 sig=np.array(2*(q-r)*J,dtype=float);var=float(q+r)*np.eye(6)
 sequences=[
  [[.7,0,0,0,0,0]],
  [[.7,0,0,0,0,0],[0,0,0,.6,0,0]],
  [[0,0,0,.6,0,0],[.7,0,0,0,0,0]],
  [[.2,-.4,.3,.1,.5,-.2],[.5,.1,-.3,-.2,.4,.1]],
  [[.3,0,.2,.1,0,-.4],[.2,.3,-.1,0,.2,.5],[-.1,0,.2,.3,-.2,.1]],
 ]
 rows=[]
 for index,sequence in enumerate(sequences):
  zs=np.array(sequence,dtype=float);total=zs.sum(axis=0)
  phase=sum(float(zs[i]@sig@zs[j]) for i in range(len(zs)) for j in range(i+1,len(zs)))
  target=np.exp(-.5*total@var@total-.5j*phase)
  ns=[]
  for K in [16,64,256,1024,4096]:
   one=np.eye(4,dtype=complex)
   for z in zs:one=one@expm(1j*sum((z[i]*ops[i] for i in range(6)),np.zeros((4,4),complex))/math.sqrt(K))
   actual=np.trace(base@one)**K;err=abs(actual-target)
   ns.append(dict(K=K,real=float(actual.real),imag=float(actual.imag),absolute_error=float(err)))
  assert ns[-1]['absolute_error']<2e-4
  rows.append(dict(sequence=index,z=sequence,target_real=float(target.real),target_imag=float(target.imag),rows=ns))
 assert rows[1]['target_imag']<0 and rows[2]['target_imag']>0
 assert abs(rows[1]['target_real']-rows[2]['target_real'])<1e-15
 return dict(finite_product_Weyl_rows=rows,scope='Numerical finite-block corroboration of the separate exact product Taylor proof; no microscopic time evolution.')

def cross(v):
 x,y,z=v;return s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])

def hamiltonian_controls():
 x,y,z=s.symbols('x y z',real=True);v=s.Matrix([x,y,z]);C=I*cross(v)
 assert C==C.H and s.simplify(C*C)==(v.dot(v))*s.eye(3)-v*v.T
 assert (v.T*C)==s.zeros(1,3)
 speed=s.Rational(2,7);sigma0=2*(q-r)
 L=s.zeros(6);L[:3,3:]=speed*C;L[3:,:3]=-speed*C
 Sigma=sigma0*J;H=Sigma.inv()*L
 assert H==speed/sigma0*s.diag(C,C) and H==H.H
 assert s.simplify(L*Sigma+Sigma*L.H)==s.zeros(6)
 assert s.simplify(L+L.H)==s.zeros(6)
 assert Sigma*s.eye(6)!=L
 # Alternative canonical potential/momentum state z=(Qpot,P), observables (-P,C Qpot).
 transform=s.zeros(6);transform[:3,3:]=-s.eye(3);transform[3:,:3]=C
 derivative=transform*J*transform.H
 expected=s.zeros(6);expected[:3,3:]=C;expected[3:,:3]=-C
 assert derivative==expected
 Hplus=s.diag(C*C,s.eye(3));Lplus=J*Hplus
 assert s.simplify(transform*Lplus-derivative*transform)==s.zeros(6)
 rows=[]
 for vv in [(1,0,0),(1,2,0),(2,-1,2),(-3,4,0)]:
  cf=C.subs(dict(zip((x,y,z),vv)));hf=H.subs(dict(zip((x,y,z),vv)))
  eigen=hf.eigenvals();positive=sum(m for a,m in eigen.items() if a>0);negative=sum(m for a,m in eigen.items() if a<0);zero=eigen.get(0,0)
  assert (positive,negative,zero)==(2,2,2)
  dj=derivative.subs(dict(zip((x,y,z),vv)));assert dj.rank()==4
  hp=Hplus.subs(dict(zip((x,y,z),vv)));assert all(a>=0 for a in hp.eigenvals())
  rows.append(dict(Q=vv,onsite_generator_energy_eigenvalues={str(a):m for a,m in eigen.items()},derivative_bracket_rank=4,positive_potential_energy_eigenvalues={str(a):m for a,m in hp.eigenvals().items()}))
 aa=s.Rational(1,7);bb=s.Rational(4,7)
 assert la/lb*aa==lb/la*bb==speed
 return dict(symbolic_Curl_square_and_divergence=True,symbolic_generator_Hessian_identity=True,
   symmetric_covariance_and_CCR_preserved=True,positive_energy_derivative_bracket_identity=True,normalization_c=speed.__str__(),exact_Fourier_rows=rows,
   scope='Indefinite Hessian only for the specified onsite CCR and exact full-helicity curl drift. The canonical potential escape changes the observable bracket; neither construction is a microscopic record generator.')

def main():
 out=ROOT/'dimer_covariant_quantum_encoding_checks';out.mkdir(exist_ok=True)
 target=out/'RESULTS.json';assert not target.exists(),'Preserve original results before any repeat.'
 groups={}
 for name,fn in [('local_encoding_and_moments',local_controls),('finite_quantum_fluctuations',fluctuation_controls),('Hamiltonian_and_derivative_escape',hamiltonian_controls)]:
  groups[name]=fn();(out/(name+'.json')).write_text(json.dumps(groups[name],indent=2)+'\n');print(name+' PASS',flush=True)
 sources={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['DIMER_COVARIANT_QUANTUM_FLUCTUATION_ENCODING.md',Path(__file__).name]}
 target.write_text(json.dumps(dict(sources_sha256=sources,groups=groups),indent=2)+'\n')
if __name__=='__main__':main()
