#!/usr/local/bin/python3
"""Direct exact checks of the conditional closed radiation/vacuum reconstruction.
No numerical observational fit or selection of the supplied scalar action.
"""
from pathlib import Path
import sys,json,hashlib,argparse,tempfile
import sympy as S
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/EXPONENTIAL_SCALAR_CURVATURE_LOOPHOLE_BOUNDED_THEOREM_NOTE_2026-10-14.md',
    'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md',
    'docs/EXPONENTIAL_SCALAR_RADIATION_PAST_BOUND_BOUNDED_THEOREM_NOTE_2026-10-14.md',
]
_ap=argparse.ArgumentParser();_ap.add_argument('--output');_args=_ap.parse_args()
_tmp=tempfile.TemporaryDirectory(prefix='scalar-curvature-') if _args.output is None else None
OUT=Path(_args.output) if _args.output else Path(_tmp.name)/'RESULTS.json'
checks=[]
def check(name,ok,detail=None):
    checks.append(dict(name=name,passed=bool(ok),detail=detail))
def zero(name,expr):
    z=S.simplify(S.expand_trig(expr));check(name,z==0,str(z))
def solution_checks(tag,X,h,K,D2,t):
    H=S.diff(X,t)/(2*X)
    Hdot=S.diff(H,t)
    zero(tag+'_Friedmann',H**2-h**2-D2/X**2+K/X)
    zero(tag+'_Raychaudhuri',Hdot-K/X+2*D2/X**2)
    zero(tag+'_radiation_conservation',S.diff(3*D2/X**2,t)+4*H*(3*D2/X**2))
    zero(tag+'_scale_acceleration',S.diff(X,t,2)-4*h**2*X+2*K)
    A=Hdot+H**2;B=H**2+K/X
    zero(tag+'_Ricci',6*(A+B)-12*h**2)
    zero(tag+'_Kretschmann',12*(A**2+B**2)-24*(h**4+D2**2/X**4))
    return H,Hdot
h,K,e,t=S.symbols('h K e t',positive=True)
D2=(K**2-e**2)/(4*h**2)
Xp=(K+e)/(2*h**2);Xm=(K-e)/(2*h**2)
X=(K+e*S.cosh(2*h*t))/(2*h**2)
H,Hdot=solution_checks('large',X,h,K,D2,t)
zero('root_sum',Xp+Xm-K/h**2);zero('root_product',Xp*Xm-D2/h**2)
zero('bounce_radius',X.subs(t,0)-Xp);zero('bounce_H',H.subs(t,0))
zero('bounce_Hdot',Hdot.subs(t,0)-e/Xp)
zero('large_radiation_vacuum_max',D2/(h**2*Xp**2)-(K-e)/(K+e))
Xs=(K-e*S.cosh(2*h*t))/(2*h**2)
solution_checks('small',Xs,h,K,D2,t)
# This small branch exists only between its two zeros for K>e.
zero('small_boundary_at_finite_time',Xs.subs(t,S.acosh(K/e)/(2*h)))
B=S.symbols('B',positive=True);Xcrit=K/(2*h**2)
Xc=Xcrit+B*S.exp(2*h*t)
Hc,Hdc=solution_checks('critical_upper',Xc,h,K,K**2/(4*h**2),t)
zero('critical_static_Friedmann',h**2+K**2/(4*h**2*Xcrit**2)-K/Xcrit)
zero('critical_static_acceleration',K/Xcrit-2*K**2/(4*h**2*Xcrit**2))
zero('critical_past_limit',S.limit(Xc,t,-S.oo)-Xcrit)
check('critical_positive_H',S.simplify(Hc).is_positive,str(S.simplify(Hc)))
zero('critical_unstable_scale_operator',S.diff(B*S.exp(2*h*t),t,2)-4*h**2*B*S.exp(2*h*t))
# Negative discriminant: exact monotonic sinh solution and finite singular endpoint.
Xn=(K+e*S.sinh(2*h*t))/(2*h**2)
solution_checks('negative_discriminant',Xn,h,K,(K**2+e**2)/(4*h**2),t)
tstart=-S.asinh(K/e)/(2*h)
zero('negative_discriminant_finite_start',Xn.subs(t,tstart))
zero('excluded_zero_radiation_deSitter',X.subs(e,K)-K*S.cosh(h*t)**2/h**2)
# Fractions at a finite expanding event. Correct root branch is essential.
d,r=S.symbols('d r',positive=True);L=1+d-r
zero('dimensionless_discriminant',d**2-4*L*r-(4*r**2-4*(1+d)*r+d**2))
f=(1+d-S.sqrt(1+2*d))/2
zero('fraction_boundary',d**2-4*(1+d-f)*f)
zero('fraction_stable_evaluation',f-d**2/(2*(1+d+S.sqrt(1+2*d))))
zero('fraction_small_curvature',S.limit(f/d**2,d,0)-S.Rational(1,4))
check('fraction_monotone',S.diff(f,d).subs(d,S.Rational(3,1000))>0)
fnum=S.N(f.subs(d,S.Rational(3,1000)),24)
check('illustrative_bound_value',abs(float(fnum)-2.243275204e-6)<1e-13,str(fnum))
# Exact synthetic branches, not observed cosmologies.
examples=[]
for hv,kc,dd in [(S.Rational(1),S.Rational(3),S.Rational(1)),(S.Rational(2),S.Rational(7),S.Rational(1)),(S.Rational(1,2),S.Rational(2),S.Rational(1))]:
    delta=kc**2-4*hv**2*dd**2;xp=(kc+S.sqrt(delta))/(2*hv**2)
    check('sample_strict_discriminant_'+str(kc),delta>0)
    check('sample_regular_branch_not_radiation_dominated_'+str(kc),dd**2/(hv**2*xp**2)<1)
    # Affine/proper completeness follows from a global strictly positive lower bound,
    # not finite-time sample integration. Validate the coefficient used in that proof.
    P=S.Rational(5,3);amin=S.sqrt(xp)
    timelike_lower=1/S.sqrt(1+P**2/amin**2);null_lower=amin/P
    check('sample_positive_completeness_bounds_'+str(kc),timelike_lower>0 and null_lower>0)
    for tv in [S.Rational(0),S.Rational(1,2),S.Rational(2)]:
        xx=(kc+S.sqrt(delta)*S.cosh(2*hv*tv))/(2*hv**2)
        hh=S.sqrt(delta)*S.sinh(2*hv*tv)/(2*hv*xx)
        check('sample_radius_lower_'+str((kc,tv)),xx>=xp)
        if tv>0:
            lv=hv**2/hh**2;rv=dd**2/(xx**2*hh**2);dv=kc/(xx*hh**2)
            check('sample_fraction_branch_'+str((kc,tv)),bool(S.N(lv-rv)>0))
            check('sample_fraction_bound_'+str((kc,tv)),bool(S.N(((1+dv-S.sqrt(1+2*dv))/2)-rv)>0))
    examples.append({'h':str(hv),'Kc':str(kc),'D':str(dd),'Delta':str(delta),'minimum_a_squared':str(xp),'max_radiation_vacuum_ratio':str(dd**2/(hv**2*xp**2))})
# Candidate scalar state: demonstrate zero gradients and C=1, rather than assuming it.
k,nu=S.symbols('k nu',positive=True);u,x,y=S.symbols('u x y',real=True)
a=(1-k)*(1+3*k)/4;alpha=S.sqrt(a);s=(1+k)/(k*(1-3*k));E=S.exp(2*alpha*u);F=1+s*E
C=(1+s)*E/F
U=S.Rational(3,2)+S.Rational(3,2)*s*(E-1)**2/F**2+k*x**2*S.exp(-(1-k)*u/alpha)/2+k*y**2*S.exp(-(1+k)*u/alpha)/3+nu*(1+s)*u**2/(2*F**2)
origin={u:0,x:0,y:0}
zero('action_origin_C',C.subs(origin)-1);zero('action_origin_U',U.subs(origin)-S.Rational(3,2))
for q in [u,x,y]:zero('action_origin_dU_'+str(q),S.diff(U,q).subs(origin))
zero('massless_trace',1-3*S.Rational(1,3))
# Distinguish the H>0 branch throughout from the bounce extension.
check('critical_event_fractions_exist',bool(Hc.subs({K:2,h:1,B:1,t:0})>0))
result={'scope':'Conditional exact classical FLRW reconstruction; synthetic algebra only, no observational likelihood or selected geometry/state.','checks':checks,'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'illustrative_d_limit':'0.003','illustrative_r_limit':str(fnum),'synthetic_examples':examples,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limits':['Completeness proof relies on complete spatial S3, all-real cosmic time and positive global radius bound.','Perturbative, nonlinear, quantum and matter stability not established.','Only radiation plus constant-origin vacuum; observed dust omitted.','Planck curvature posterior not transferred.']}
OUT.parent.mkdir(parents=True,exist_ok=True)
assert not OUT.exists(),str(OUT)
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
for c in checks:
    if not c['passed']:print('FAILED',c)
raise SystemExit(1 if result['failed'] else 0)
