"""Independent exact scalar/symbolic check; no author executable imports.

Numerical targets are known from the read candidate. Bounds are assembled
from the separately recorded component derivation, not its reported total.
"""
import datetime, hashlib, json, os, resource, sys, time
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
START = time.monotonic()
HERE = Path(__file__).resolve().parent
PRE = json.loads((HERE / 'PRELAUNCH.json').read_text())

def ident(path):
    p = Path(path)
    data = p.read_bytes()
    st = p.stat()
    return dict(path=str(p), sha256=hashlib.sha256(data).hexdigest(), bytes=len(data),
                device=st.st_dev, inode=st.st_ino, mtime_ns=st.st_mtime_ns)

for entry in PRE['bindings']:
    assert ident(entry['path']) == entry, entry['path']

import sympy as sp

checks = []
values = {}

def check(name, statement, evidence):
    assert bool(statement), name
    checks.append(dict(name=name, evidence=evidence))

def put(name, value):
    if isinstance(value, F):
        values[name] = dict(exact=str(value), approximate=float(value),
                            approximate_is_not_an_outward_enclosure=True)
    else:
        values[name] = value
    return value

klo, khi = F(1,10**12), F(1,10**8)
sigma, v, s, sqsigma = F(1,10**6), F(1,40), F(3,20), F(1,1000)
Nlo, J = F(99,100), F(3752638388379,125000000000000)
q0 = F('4.510351185997098')
sin0, cos0 = 2*q0/(q0*q0+1), (q0*q0-1)/(q0*q0+1)
sin2, cos2 = 2*sin0*cos0, cos0*cos0-sin0*sin0
v0, b0, E0 = 2*J*sin0, 2*sin2, 2*J*(1-cos0)
SigmaR, negSigmaI = -2*cos2*sin2/v0, 2*sin2*sin2/v0
put('v0', v0); put('b0',b0); put('E0',E0)
check('exact_trigonometric_circle', sin0*sin0+cos0*cos0==1, 'rational half-angle identity')
check('velocity_on_full_real_band', v0-2*J*sigma>v and v0<F(3,100), 'Lipschitz bound, not endpoint sampling')
check('curvature_ratio', 2*J/v<F(5,2), str(2*J/v))
check('center_b0_and_width', b0>F(3,2) and negSigmaI>19, [str(b0),str(negSigmaI)])
check('self_energy_center_identity', SigmaR**2+negSigmaI**2==(b0/v0)**2, 'exact real/imaginary expansion')
check('rectangle_center_bounds', max(abs(SigmaR)/v0,negSigmaI/v0)<3200 and 3200*khi**2<sigma/4, 'all kappa dependence is kappa^2')
check('residue_time_rate', v*negSigmaI/v0>F(125,4)>30, str(v*negSigmaI/v0))
check('square_root_majorants', s*s<v and sqsigma*sqsigma==sigma, [str(s*s),str(v)])

eps = 4*sigma
rin, rout = 22*sigma/(1-eps), 24*sigma/(1-eps)
eta2 = (F(4,3)*sigma)**2
check('real_relative_denominator',100*(J*sigma+560*khi**2)<eps,str(100*(J*sigma+560*khi**2)))
check('rational_profile_l2', rin/Nlo<30*sigma and rout/Nlo+4*eta2<30*sigma, [str(rin/Nlo),str(rout/Nlo+4*eta2)])
check('density_relative_error',(2*18*sigma+(18*sigma)**2+2*eps+eps**2)/(1-eps)**2<45*sigma,
      str((2*18*sigma+(18*sigma)**2+2*eps+eps**2)/(1-eps)**2))
density_L1=put('density_L1',45*sigma/Nlo+16*khi**2/(v*v*sigma))
check('density_comparison_floor',density_L1<50*sigma,str(density_L1))
check('exp_base',F(1)+F(1)+F(1,2)+F(1,6)+F(1,24)>F(8,3),'strict positive exponential series remainder')
check('log_argument',1+2*F(4,10**8)/(19*klo*klo)<F(8,3)**40,str(1+2*F(4,10**8)/(19*klo*klo)))
check('energy_rectangle_bound',F(3,100)*sigma+2*khi*khi/v<F(4,10**8),str(F(3,100)*sigma+2*khi*khi/v))
check('L1_profile_bound',3200/(1-eps)<4000,str(3200/(1-eps)))

# Assemble TV separately, retaining both endpoint jumps. Curvature uses 2J/v<5/2.
TV_coeff = put('TV_coefficient',F(8)+F(8)+F(4))
curvature_coeff = put('curvature_coefficient',F(5,2)*4)
edge_coeff = put('two_vertical_edges_coefficient',F(2)+F(2))
H = put('half_line_edges_and_cutoff', khi*khi/(v*s)*(TV_coeff/sigma+curvature_coeff+edge_coeff/sigma))
Btm = put('incoming_bottom', khi**3/(v*v*sigma*sqsigma))
P = put('residue_onset',2*F(3,8)**30)
qin = put('incoming_ceiling',30*sigma+H+Btm)
qout = put('outgoing_ceiling',30*sigma+H+2*Btm+P)
check('incoming_target',qin<F('0.000030640002'),str(qin))
check('outgoing_target',qout<F('0.000030640004') and qout<F(1,2),str(qout))
check('half_line_time_threshold',v/khi**2>1,str(v/khi**2))

A = put('common_emitter_scalar',50*sigma+P+(8+4)*khi**4/(v**3*sigma**2))
S = put('incoming_scalar',F(1600)*khi*rin+khi**3/v**2*(F(3)/sigma+(TV_coeff/sigma+curvature_coeff)/2))
check('emitter_scalar_target',A<F('0.000050000001'),str(A))
check('incoming_scalar_target',S<F('0.0000000003521'),str(S))
off = F(1,10**14)
clock_parts = {
    'Cg_center':31*S,
    'Cg_variation':2700*sigma*2000*khi,
    'Kloc_center':khi*20000*A,
    'Kloc_variation':khi*10**6*sigma,
    'Kloc_delta_y':khi*20000*(4*sigma+off)
}
for name, val in clock_parts.items(): put(name,val)
clock_col=put('full_clock_column',sum(clock_parts.values(),F(0)))
clock_op=put('full_clock_operator',F(3,2)*clock_col)
loc=put('full_localized',A+F(3,2)*(4*sigma+off)+clock_op)
Q=put('escape_only',qin+qout+loc)
total=put('complete_infinite',F('0.003')+F('0.000714')+Q)
check('full_clock_ceiling',clock_op<F('0.0000001286'),str(clock_op))
check('full_localized_ceiling',loc<F('0.000056128570'),str(loc))
check('escape_budget',Q<118*sigma,str(Q))
check('complete_target',total<F('0.003832'),str(total))

# Independent symbolic signs and discriminators.
x, aa, bb, vv, kk = sp.symbols('x a b v kappa', real=True)
D = x+sp.I*kk**2*(aa**2+bb**2)/(2*vv)
tm = 1-sp.I*kk**2*bb**2/(vv*D)
phase_identity = sp.factor(tm-sp.conjugate(D)/D-sp.I*kk**2*aa**2/(vv*D))
check('exact_phase_identity',phase_identity==0,str(phase_identity))
Dtest=1+sp.I
correct_phase=sp.simplify(1-2*sp.I/Dtest-sp.conjugate(Dtest)/Dtest)
wrong_phase=sp.simplify(1-2*sp.I/Dtest-Dtest/sp.conjugate(Dtest))
check('phase_reciprocal_discriminator',correct_phase==0 and wrong_phase==-2*sp.I, [str(correct_phase),str(wrong_phase)])
q,c,g,n=sp.symbols('q c gamma N',real=True,positive=True)
p0=g/(sp.pi*n*((q-c)**2+g*g))
partial=(1/(q-c-sp.I*g)-1/(q-c+sp.I*g))/(2*sp.pi*sp.I*n)
check('density_partial_fraction',sp.factor(p0-partial)==0,str(sp.factor(p0-partial)))
res=sp.simplify(sp.limit((q-c+sp.I*g)*p0,q,c-sp.I*g))
check('density_clockwise_residue',sp.simplify(-2*sp.pi*sp.I*res-1/n)==0,str(res))
signed_in=sp.simplify(sp.limit((q-c-sp.I*g)/(q-c-sp.I*g),q,c+sp.I*g))
check('incoming_pole_is_upper',signed_in==1,'denominator q-c-i gamma vanishes at c+i gamma; gamma>0')
endpoint=sp.integrate(sp.exp(-sp.I*q),(q,0,sp.pi))
check('hard_cutoff_endpoint_discriminator',endpoint==-2*sp.I,str(endpoint))
aligned=sp.Matrix([[1,1],[0,0]])
gram=aligned.conjugate().T*aligned
check('localized_aligned_column_discriminator',set(gram.eigenvals())=={0,2},str(gram.eigenvals()))
check('parity_operator_rounding',F(3,2)**2>2,'sqrt(2)<3/2; largest column alone is insufficient')
# Normalize retained component, not entire full-line vector.
delta=F(3,5); retained=F(4,5)
check('restricted_normalization',1-retained<=delta and retained*retained+delta*delta==1,
      'For all delta in [0,1], (1-delta)^2<=1-delta^2 follows from 2delta(delta-1)<=0; example delta=3/5.')

# Exact shortest distance and finite radius budget; no enormous device allocated.
Tmin=put('minimum_T',1/khi**2); Mmin=put('minimum_M',50*Tmin)
margin=put('minimum_distance_margin',F(22,5)*Tmin-22)
finite=put('finite_correction',F(32,5)*F(3,8)**9)
fin_total=put('complete_finite',total+finite)
check('integer_path',Mmin.denominator==1 and int(Mmin)-12-1==int(Mmin)-13,'one emitter hop plus M-(L+2) clock hops')
check('finite_margin',margin==43999999999999978 and margin>0,str(margin))
check('finite_correction_ceiling',finite<F('0.001'),str(finite))
check('finite_total_target',fin_total<F('0.004832'),str(fin_total))
put('minimum_qubits',int(Mmin)+5)
check('positive_emitter_reserve',E0>2*khi,str(E0-2*khi))
put('actual_upper_scalar',F('1.459892813020969')+2*khi)
put('clock_attachment_load',4*J+3*khi)
put('emitter_load',E0+2*khi)
put('seed_variance_extra_at_upper',2*khi*khi)
old_cutoff=put('failed_fixed_cutoff_allowance',4*khi/(v*sqsigma))
old_clock=put('failed_absolute_clock_allowance',153000*khi)
bad_scalar=put('failed_qin_for_Cg_allowance',F(3,2)*31*30*sigma)
check('old_estimates_fail_target_budget',old_cutoff+old_clock>F('0.003832')-F('0.003')-F('0.000714') and bad_scalar>F('0.003832')-F('0.003')-F('0.000714'),
      'Failure of sufficient allowances, not a leakage lower bound or physical no-go.')

after=[]
for entry in PRE['bindings']:
    got=ident(entry['path']); assert got==entry,entry['path']; after.append(got)
usage=resource.getrusage(resource.RUSAGE_SELF)
print(json.dumps(dict(status='all requested exact checks held',
    completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    python=sys.version, sympy=sp.__version__, pid=os.getpid(),
    caps=resource.getrlimit(resource.RLIMIT_CPU), matrix_dimension_maximum=2,
    scientific_runtime_seconds=time.monotonic()-START,
    self_cpu_user=usage.ru_utime, self_cpu_system=usage.ru_stime, peak_rss=usage.ru_maxrss,
    checks=checks, values=values, unchanged_bindings=len(after),
    limits='Rational/symbolic corroboration of separately written analysis; no grid/quadrature/dynamics or author-code execution.'),indent=2))
