#!/usr/bin/env python3
"""Focused algebra/resource checks; reads only the provisional checked polynomial.

The battery fixture is a separate 12-dimensional exact algebra control,
not a surrogate computation of PR9345's unbounded reservoir dynamics.
"""
from pathlib import Path
from fractions import Fraction
import json, math
import sympy as s

OUT=Path(__file__).resolve().parent
polys=json.loads((OUT.parent/'independent-birth-energy-check/coefficients.json').read_text())
z=[ [[-2,0,0],[-2,-1,0],-1], [[-2,0,0],[-1,0,0],1],
    [[-1,-1,0],[-2,-1,0],1], [[-1,-1,0],[-1,0,0],-1] ]
witness={}
for mark,terms in polys.items():
    p={json.dumps(w):Fraction(c) for w,c in terms}
    c=p[json.dumps(z)]
    assert c==Fraction(2,5)
    witness[mark]={'offdiagonal_compression_over_delta':str(c),
        'psi_plus_minus_expectation_difference_over_delta':str(2*c)}

# Exact positive finite ladder, input H=0, output H=diag(0,1).
# C|n>=(|0,n>+|1,n-1>)/sqrt(2), with the second term absent at n=0.
# This is the energy lift of |0> -> (|0>+|1>)/sqrt(2).
M=4
C=s.zeros(2*M,M)
for n in range(M):
    C[n,n]=1/s.sqrt(2)
    if n: C[M+n-1,n]=1/s.sqrt(2)
K_in=s.diag(*range(M));K_out=s.diag(*(list(range(M))+list(range(1,M+1))))
assert K_out*C==C*K_in
D_in=s.diag(1/s.sqrt(2),0,0,0)
D_out=s.eye(2*M)
for n in range(M):
    cn=C[:,n];norm2=(cn.T*cn)[0]
    D_out -= (1-s.sqrt(1-norm2))/norm2*(cn*cn.T)
assert s.simplify(D_out*D_out-(s.eye(2*M)-C*C.T))==s.zeros(2*M)
U=D_in.row_join(-C.T).col_join(C.row_join(D_out))
K=s.diag(K_in,K_out)
assert s.simplify(U.T*U)==s.eye(3*M)
assert s.simplify(K*U-U*K)==s.zeros(3*M)
# Two-state time-independent program. At T=2*pi, g=1/4, exp(-iKT)=I;
# g(I+Q)>=0 and exact evolution sends |0>psi to -|1>U psi.
Q=s.zeros(3*M).row_join(U.T).col_join(U.row_join(s.zeros(3*M)))
Kclock=s.diag(K,K)
assert s.simplify(Q*Q)==s.eye(6*M)
assert s.simplify(Q*Kclock-Kclock*Q)==s.zeros(6*M)
# Lower boundary has a real refusal probability 1/2; no wrapped shift.
assert (D_in[:,0].T*D_in[:,0])[0]==s.Rational(1,2)

# Normalized sine on battery levels 1,2: no refusal, actual mark coherence.
beta=s.Matrix([0,1/s.sqrt(2),1/s.sqrt(2),0])
v=C*beta;rho=s.zeros(2)
for i in range(2):
    for j in range(2): rho[i,j]=s.simplify(sum(v[i*M+n]*v[j*M+n] for n in range(M)))
assert rho==s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,2)]])
initial_E=(beta.T*K_in*beta)[0]
out_system_E=rho[1,1]
out_battery_E=s.simplify(sum(v[i*M+n]**2*n for i in range(2) for n in range(M)))
assert initial_E==out_system_E+out_battery_E

rows=[]
for width in (2,3,7,15,31):
    overlap=math.cos(math.pi/(width+1))
    rows.append({'sine_levels':width,'exact_overlap_formula':'cos(pi/(L+1))',
      'overlap_numeric':overlap,'output_trace_norm_error':1-overlap,
      'initial_mean_battery_energy':(width+1)/2,
      'system_energy_gain':0.5,'battery_energy_change':-0.5})

# Conservative actual rotor first-event resource constants, not optimized.
N=24**3//2;delta=K_e=1.;epsilon=.01
bound_C=delta*(95040+48*N+2*math.sqrt(48*N))+2*K_e
bound_J=delta*math.sqrt((1974*N)**2+48*N)
width=4*math.pi*bound_C/epsilon
bottom=8*(bound_C+bound_J)/epsilon
headroom=8*bound_J/epsilon
p=(bound_C+bound_J)**2/bottom**2+bound_J**2/headroom**2
err=2*math.pi*bound_C/width+2*math.sqrt(p)+p
assert err<epsilon
energy_scaling=[]
for lam in (100,10000,1000000):
    phase=2*math.pi/lam
    refusal=2/lam**6
    accepted_error=phase+2*math.sqrt(refusal)
    energy_error=2*math.sqrt(2*accepted_error)+2/lam**3+math.sqrt(2)*(1+lam)/lam**3
    energy_scaling.append({'lambda':lam,'trace_norm_bound':accepted_error+refusal,
        'absolute_energy_error_over_C_plus_J':energy_error,
        'battery_energy_cap_over_C_plus_J':2*lam**3+lam})
assert all(x['absolute_energy_error_over_C_plus_J']>y['absolute_energy_error_over_C_plus_J']
           for x,y in zip(energy_scaling,energy_scaling[1:]))
r={'actual_PR9345_covariance_witness':witness,'word':z,
  'exact_Julia_fixture':{'joint_dimension':3*M,'unitarity':True,'additive_energy_commutation':True,
    'two_state_clock_joint_dimension':6*M,'clock_involution_and_energy_commutation':True,
    'exact_clock_arrival_time':'2*pi','clock_coupling':'1/4',
    'ground_battery_refusal_probability':'1/2','accepted_system_density':str(rho),
    'initial_battery_mean':str(initial_E),'final_battery_mean':str(out_battery_E),
    'system_energy_gain':str(out_system_E)},
  'finite_sine_controls':rows,
  'normalizable_positive_battery_energy_convergence':energy_scaling,
  'actual_rotor_sufficient_resource_example':{'L':24,'N':N,'K':K_e,'delta':delta,
    'desired_trace_norm_error':epsilon,'C_bound':bound_C,'J_bound':bound_J,
    'sine_energy_width':width,'initial_energy_bottom':bottom,'upper_headroom':headroom,
    'battery_energy_cap':bottom+width+headroom,'initial_battery_mean':bottom+width/2,
    'refusal_probability_upper':p,'total_error_upper':err},
  'scope':'Exact small matrix control and explicit conservative resource arithmetic; no full rotor propagation.'}
(OUT/'results.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
