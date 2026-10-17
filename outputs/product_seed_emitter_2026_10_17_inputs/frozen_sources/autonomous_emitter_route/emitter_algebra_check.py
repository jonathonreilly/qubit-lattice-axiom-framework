#!/usr/bin/env python3
"""Bounded exact algebra for one exploratory two-contact emitter.

No optimization, grid certificate, dynamics simulation, Markov approximation,
or integrated gate-emitter certificate is performed. Largest matrix: 16x16.
"""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
started = time.monotonic()
import sympy as s

R = s.Rational
i = s.I
J = R('0.030021107107032')
q0 = R('4.510351185997098')
z0 = (q0*q0 - 1 + 2*i*q0)/(q0*q0 + 1)
cos0, sin0 = s.re(z0), s.im(z0)
phase = s.expand(z0*z0)
E0 = 2*J*(1-cos0)
coupling = R(1,10**12)
sigma = R(1,10**6)
speed = R(1,40)
sin2 = 2*sin0*cos0

def ck(name, expr):
    assert bool(expr), name
    return {'check': name, 'passed': True}

checks = []
checks += [ck('z0 is exactly unit modulus', s.expand(z0*s.conjugate(z0)) == 1),
           ck('E0 - 2 coupling is positive', E0 > 2*coupling),
           ck('sin(2 k0) is positive', sin2 > 0),
           ck('speed lower bound on k0 +- sigma', 2*J*(sin0-sigma) > speed)]

# Order is (emitter, clock L, intermediate clock L+1, clock L+2).
I2 = s.eye(2)
ann = s.Matrix([[0,1],[0,0]])
num = ann.H*ann
def at(op, index):
    factors = [op if j == index else I2 for j in range(4)]
    return s.kronecker_product(*factors)
aa = [at(ann,j) for j in range(4)]
nn = [at(num,j) for j in range(4)]
I16 = s.eye(16)
zero16 = s.zeros(16)

# t is the coefficient of a_site^dagger a_emitter.
def edge(site, t):
    hop = t*aa[site].H*aa[0] + s.conjugate(t)*aa[0].H*aa[site]
    return coupling*(nn[0]+nn[site]) + hop, hop
Qa, ha = edge(1, coupling)
Qb, hb = edge(3, -coupling*phase)
for label, Q in [('first edge',Qa),('second edge',Qb)]:
    checks.append(ck(label+' Hermitian', Q == Q.H))
    # The selfadjoint polynomial identity implies spectrum {0,2 coupling}.
    checks.append(ck(label+' positive with norm 2 coupling',
                     (Q*Q-2*coupling*Q).applyfunc(s.expand) == zero16 and Q != zero16))
addition = Qa + Qb + (E0-2*coupling)*nn[0] + coupling*(I16-nn[1]) + coupling*(I16-nn[3])
desired = E0*nn[0] + ha + hb + 2*coupling*I16
checks.append(ck('full 16-dimensional scalar-reserve identity',
                 (addition-desired).applyfunc(s.expand) == zero16))
head_number = nn[0]+nn[1]+nn[2]+nn[3]
checks.append(ck('addition conserves total emitter-plus-clock head number',
                 (addition*head_number-head_number*addition).applyfunc(s.expand) == zero16))

# Infinite-lead form factor with L=0; shifting L only supplies unit phases.
def vplus(z):
    return s.expand(1-phase/z**2)
def vminus(z):
    return s.expand(1-phase*z**2)
vp0 = s.simplify(vplus(z0))
vm0 = s.simplify(vminus(z0))
checks += [ck('return/right-emission central notch', vp0 == 0),
           ck('left-emission central amplitude squared',
              s.simplify(vm0*s.conjugate(vm0)-4*sin2*sin2) == 0)]

# This checks signs and normalizations at two exact momenta, not interval
# nonsingularity. The route's interval bound is analytic and independent.
point_reports = []
for label, q in [('central',q0),('off_center_algebra_only',q0+R(1,10))]:
    z = (q*q-1+2*i*q)/(q*q+1)
    sint, cost = s.im(z), s.re(z)
    vg = 2*J*sint
    vp, vm = s.simplify(vplus(z)), s.simplify(vminus(z))
    w = s.Matrix([vp,vm])
    Sigma = s.simplify(-i/vg*(2-(phase+s.conjugate(phase))*z*z))
    D = s.simplify(2*J*(1-cost)-E0-coupling**2*Sigma)
    smat = (s.eye(2)-i*coupling**2/(vg*D)*(w*w.H)).applyfunc(s.simplify)
    checks += [ck(label+' self-energy optical identity',
                  s.simplify(-s.im(Sigma)-(w.H*w)[0]/(2*vg)) == 0),
               ck(label+' exact two-port unitarity',
                  (smat.H*smat-s.eye(2)).applyfunc(s.simplify) == s.zeros(2)),
               ck(label+' equal transmission probabilities',
                  s.simplify(smat[0,0]*s.conjugate(smat[0,0])-smat[1,1]*s.conjugate(smat[1,1])) == 0)]
    if label == 'central':
        checks += [ck('return transmission at center is exactly one', smat[0,0] == 1),
                   ck('both reflection amplitudes at center vanish', smat[0,1] == 0 and smat[1,0] == 0)]
    point_reports.append({'label':label, 'q_exact':str(q),
                          'return_reflection_squared_display':float(s.re(smat[1,0]*s.conjugate(smat[1,0]))),
                          'return_transmission_minus_one_squared_display':float(s.re((smat[0,0]-1)*s.conjugate(smat[0,0]-1)))})

# Analytic band estimates: |v(+k)| <= 2 sigma,
# |v(-k)| >= 2 sin(2 k0)-2 sigma.
ratio = sigma/(sin2-sigma)
return_r = 2*ratio
return_t_error = 2*ratio*ratio
wrong_way_probability_fraction = ratio*ratio
checks += [ck('directional ratio strict ceiling', ratio < R(131,10**8)),
           ck('return reflection amplitude strict ceiling', return_r < R(262,10**8)),
           ck('return transmission error strict ceiling', return_t_error < R(344,10**14)),
           ck('wrong-way in-band probability-fraction strict ceiling', wrong_way_probability_fraction < R(172,10**14))]

# The seed variance is exact also with the installed gate: the seed is at e,
# B u_j=b_j u_j, and only two new hopping terms act away from it.
single_col_spill_sq = 2*coupling**2/(speed*sigma)**2
group_op_spill_sq = 2*single_col_spill_sq  # two old-energy columns per parity
checks += [ck('single-column out-of-band amplitude below 6e-5', single_col_spill_sq < R(6,10**5)**2),
           ck('grouped operator out-of-band amplitude at most 8e-5', group_op_spill_sq == R(8,10**5)**2)]

report = {
    'scope':'exact cell/form-factor/optical algebra and analytic diagnostic constants; no installed-emitter time certificate',
    'parameters_exact':{'J':str(J),'q0':str(q0),'E0':str(E0),'coupling':str(coupling),'sigma':str(sigma),'speed':str(speed)},
    'constants_exact':{'sin_2k0':str(sin2),'directional_ratio':str(ratio),
        'return_reflection_ceiling':str(return_r),'return_transmission_error_ceiling':str(return_t_error),
        'wrong_way_in_band_probability_fraction_ceiling':str(wrong_way_probability_fraction),
        'single_column_out_of_band_norm_squared_ceiling':str(single_col_spill_sq),
        'grouped_out_of_band_operator_norm_squared_ceiling':str(group_op_spill_sq),
        'added_common_scalar':str(2*coupling),
        'emitter_incident_positive_block_norm_sum':str(E0+2*coupling),
        'clock_attachment_added_positive_block_norm_sum':str(3*coupling)},
    'display_only':{'k0':float(2*s.atan(1/q0)), 'E0':float(E0),
                    'sin_2k0':float(sin2),'directional_ratio':float(ratio),
                    'return_reflection_ceiling':float(return_r),
                    'return_transmission_error_ceiling':float(return_t_error),
                    'wrong_way_in_band_probability_fraction_ceiling':float(wrong_way_probability_fraction)},
    'point_algebra':point_reports,
    'checks':checks,
    'resources':{'max_matrix_dimension':16,'onshell_exact_points':2,'interval_grid_points':0,
                 'cpu_cap_seconds':10,'wrapper_wall_cap_seconds':30,'optimizer_iterations':0},
    'runtime':{'python_executable':sys.executable,'python_version':sys.version,
               'platform':platform.platform(),'sympy_version':s.__version__,
               'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'elapsed_seconds':time.monotonic()-started},
    'limitations':['same-model source-exposed author algebra, not independent review',
                   'no finite emission-completion time', 'no augmented old/source matching inverse',
                   'no in-band point-spectrum bound for the installed apparatus',
                   'no complete-output gate theorem for the autonomous seed']}
print(json.dumps(report, indent=2, sort_keys=True))
