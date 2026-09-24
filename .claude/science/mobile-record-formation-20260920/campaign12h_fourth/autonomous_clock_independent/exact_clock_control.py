#!/usr/bin/env python3
"""Independent exact finite program, including physical free evolution.
No campaign builder is imported. A synthetic non-phase-covariant qubit jump
L=sqrt(gamma)|+><0| tests the general construction with a positive battery.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s
HERE=Path(__file__).resolve().parent
N=2;L=2;B=L+2;T=s.Integer(2);nu=s.pi/T;omega=nu
# Two exact unit steps: gamma=1/4, sqrt(gamma*tau)=1/2.
c=s.sqrt(3)/2;v=s.Rational(1,2)
z=s.zeros(4,1);z[0]=1
w=s.zeros(4,1);w[1]=w[3]=1/s.sqrt(2)
R=s.eye(4)+(c-1)*(z*z.T+w*w.T)+v*(w*z.T-z*w.T)
U=s.diag(1,1,-s.I,-s.I)*R
simplify=lambda A:A.applyfunc(s.simplify)
assert simplify(U.conjugate().T*U)==s.eye(4)
words=tuple(product(range(2),range(B),range(2**N)));index={q:i for i,q in enumerate(words)};D=len(words)
labels=[system+n for system,n,flags in words]
Q=s.diag(*labels)
def finite_gate(bit):
 out=s.zeros(D)
 for col,(system,n,flags) in enumerate(words):
  m=system+n
  if not 1<=m<=L+1:out[col,col]=1;continue
  inp=2*system+((flags>>bit)&1)
  for dest in range(4):
   amp=U[dest,inp]
   if amp==0:continue
   system_out,flag_out=divmod(dest,2)
   nn=m-system_out;ff=(flags&~(1<<bit))|(flag_out<<bit)
   out[index[system_out,nn,ff],col]+=amp
 return out
VS=[finite_gate(j) for j in range(N)]
for V in VS:
 assert simplify(V.conjugate().T*V)==s.eye(D)
 assert Q*V==V*Q
phase=s.diag(*[s.I**m for m in labels])
Ws=[phase*V for V in VS]
prefix=[s.eye(D)]
for W in Ws:prefix.append(simplify(W*prefix[-1]))
control=s.diag(*prefix)
assert simplify(control.conjugate().T*control)==s.eye((N+1)*D)
hc=s.eye(N+1)*s.Rational(N,2)
for j in range(1,N+1):hc[j,j-1]=hc[j-1,j]=s.sqrt(j*(N+1-j))/2
assert hc.eigenvals()=={s.Integer(0):1,s.Integer(1):1,s.Integer(2):1}
program=s.eye((N+1)*D)*s.Rational(N,2)
for j,Wj in enumerate(Ws,1):
 coupling=s.sqrt(j*(N+1-j))/2
 program[j*D:(j+1)*D,(j-1)*D:j*D]=coupling*Wj
 program[(j-1)*D:j*D,j*D:(j+1)*D]=coupling*Wj.conjugate().T
bare=s.kronecker_product(hc,s.eye(D))
qfull=s.kronecker_product(s.eye(N+1),Q)
assert simplify(program-control*bare*control.conjugate().T)==s.zeros((N+1)*D)
assert simplify(program-program.conjugate().T)==s.zeros((N+1)*D)
assert simplify(program*qfull-qfull*program)==s.zeros((N+1)*D)
interaction=program-bare
initial=s.zeros((N+1)*D,2)
for system in (0,1):
 for n in (1,2):initial[index[system,n,0],system]=1/s.sqrt(2)
assert initial.conjugate().T*initial==s.eye(2)
assert simplify(initial.conjugate().T*interaction*initial)==s.zeros(2)
assert simplify(initial.conjugate().T*bare*initial)==s.eye(2)*N/2
assert simplify(initial.conjugate().T*bare*bare*initial-(s.eye(2)*N/2)**2)==s.eye(2)*N/4
# At time T=2, the endpoint clock amplitude is +1 and the physical free
# evolution cancels the explicit counterphase exactly on the entire work space.
free_endpoint=s.diag(*[(-1)**m for m in labels])
assert simplify(free_endpoint*prefix[-1]-VS[-1]*VS[0])==s.zeros(D)
# An uncorrected program would leave an extra physical free evolution.
wrong=free_endpoint*VS[-1]*VS[0]
assert simplify(wrong-VS[-1]*VS[0])!=s.zeros(D)
result={'construction':'Independent exact full finite conserving clock with coherent qubit jump, not a campaign import','clock_positions':N+1,'collision_flags':N,'each_flag_dimension':2,'battery_dimension':B,'work_dimension':D,'full_dimension':(N+1)*D,'duration_T':str(T),'omega_and_clock_spacing_nu':str(nu),'collision_gamma':str(s.Rational(1,4)),'jump_shape':'|+><0|; not an eigenoperator of H','identities':{'full_gate_unitarity':True,'full_gate_free_energy_commutation':True,'program_gauge_conjugation':True,'total_H_free_energy_commutation':True,'positive_program_by_exact_clock_spectrum':True,'initial_interaction_mean_zero_for_every_system_input':True,'endpoint_free_counterphase_cancellation':True,'uncorrected_endpoint_not_equal':True},'clock_spectrum':[str(nu*j) for j in range(N+1)],'clock_initial_mean':str(nu*N/2),'clock_initial_variance':str(nu**2*N/4),'interaction_norm_upper_bound':str(nu*N),'prepared_battery_mean':str(omega*(L+1)/2),'interpretation':'Exact finite-space operator identities. General convergence and resource hypotheses are proved in PRE_RECONSTRUCTION.md.'}
(HERE/'EXACT_CLOCK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
