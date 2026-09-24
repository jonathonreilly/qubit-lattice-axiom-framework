#!/usr/bin/env python3
"""Exact six-dimensional energy-preserving transfer and star embedding checks.
This constructs a fixed-input output witness, not the full birth channel.
"""
from pathlib import Path
import json,hashlib,importlib.util,sys
sys.dont_write_bytecode=True
import sympy as s
HERE=Path(__file__).resolve().parent
r,Omega=s.symbols('r Omega',positive=True)
p=r/(1+r);lo=1/s.sqrt(1+r);hi=s.sqrt(r)/s.sqrt(1+r)
# Composite order: d0,d1,l0,l1,h0,h1, with system energies 0,0,Omega.
H=s.diag(0,Omega,0,Omega,Omega,2*Omega)
U=s.eye(6)
for a,b in ((0,2),(1,4)):
 U[a,a]=U[b,b]=0;U[a,b]=U[b,a]=1
assert U.T*U==s.eye(6) and U*H==H*U
initial=s.Matrix([lo,hi,0,0,0,0]);out=U*initial
expected=s.Matrix([0,0,lo,0,hi,0]);assert out==expected
assert s.simplify((initial.T*H*initial)[0]-p*Omega)==0
assert s.simplify((out.T*H*out)[0]-p*Omega)==0
rho=out*out.T;reduced=s.zeros(3)
for i in range(3):
 for j in range(3):reduced[i,j]=s.simplify(sum(rho[2*i+b,2*j+b] for b in (0,1)))
phi=s.Matrix([0,lo,hi]);assert reduced==s.simplify(phi*phi.T)
# Dephased fuel has the same energy, but gives the stationary dephased output.
incoherent=s.diag(1-p,p,0,0,0,0);dephased=U*incoherent*U.T
out_dephased=s.zeros(3)
for i in range(3):
 for j in range(3):out_dephased[i,j]=s.simplify(sum(dephased[2*i+b,2*j+b] for b in (0,1)))
assert s.simplify(out_dephased-s.diag(0,1-p,p))==s.zeros(3)
difference=s.simplify(reduced-out_dephased)
X=s.Matrix([[0,0,0],[0,0,1],[0,1,0]])
C=s.simplify(2*lo*hi)
assert s.simplify(s.trace(X*difference)-C)==0
assert s.simplify((difference**2)[1,1]-p*(1-p))==0
# A wrong output that leaves high fuel occupied violates the energy identity.
wrong=s.eye(6);wrong[1,1]=wrong[5,5]=0;wrong[1,5]=wrong[5,1]=1
assert wrong*H-H*wrong!=s.zeros(6)
source=HERE.parent/'microscopic_birth_energy_author/exact_star_energy.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='ce202e534e19254516e7a3437c5c19e8a229334170eda73f65a16ae2f1fa377e'
spec=importlib.util.spec_from_file_location('pinned_root_star_for_fuel',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# Exact physical embedding at several epsilons checks that the abstract
# d,l,h states are distinct normalized eigenvectors of the actual Hamiltonian.
rows=[]
for eps in (s.Rational(1,2),s.Rational(1,5),s.Rational(1,17)):
 hh1=m.h1.subs(m.e,eps)/eps**4;hh3=m.h3.subs(m.e,eps)/eps**4
 Om=(1+3*eps**2)/eps**4
 dressed=m.psi_num.subs(m.e,eps)/s.sqrt(1+3*eps**2)
 assert hh1*dressed==s.zeros(4,1)
 for label,J in [('plus',m.jump(1,1)),('minus',m.jump(1,-1)),('coherent',m.jump(1,1)+m.jump(1,-1))]:
  v=J*m.F1*m.v0;v=v/s.sqrt((v.T*v)[0])
  highpart=s.simplify(hh3*v/Om);lowpart=s.simplify(v-highpart)
  prob=s.simplify((highpart.T*highpart)[0])
  assert s.simplify((lowpart.T*highpart)[0])==0
  assert s.simplify(hh3*lowpart)==s.zeros(12,1)
  assert s.simplify(hh3*highpart-Om*highpart)==s.zeros(12,1)
  c=s.simplify(prob*(1+3*eps**2)/eps**2)
  assert c=={'plus':2,'minus':1,'coherent':s.Rational(3,2)}[label]
  mean=s.simplify(prob*Om);coherence=s.simplify(2*s.sqrt(prob*(1-prob)))
  assert mean==c/eps**2
  rows.append({'epsilon':str(eps),'mark':label,'c':str(c),'p_high':str(prob),'fuel_gap':str(Om),'fuel_energy':str(mean),'minimum_stationary_trace_norm_distance':str(coherence),'physical_embedding_verified':True})
result={'standing':'Personal exact conditional witness; not a full autonomous instrument','abstract_unitary':U.tolist(),'total_free_energy_diagonal':list(H.diagonal()),'fuel_parameterization':'p=r/(1+r), r>0','fuel_mean_energy':str(p*Omega),'fuel_and_output_trace_asymmetry':str(C),'stationary_output_distance_attained':True,'dephased_fuel_same_energy_different_output':True,'wrong_energy_transfer_detected':True,'physical_star_embeddings':rows,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(HERE/'COHERENT_FUEL_RESULTS.json').write_text(json.dumps(result,default=str,indent=2)+'\n')
print(json.dumps({'abstract_energy_conservation':True,'physical_embeddings':len(rows),'fuel_mean':str(p*Omega),'trace_asymmetry':str(C),'scope':result['standing']},indent=2))
