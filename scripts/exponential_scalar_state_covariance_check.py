#!/usr/local/bin/python3
"""Exact conditional covariance/support and bounded spatial ensemble checks."""
from pathlib import Path
import json,hashlib,argparse,itertools
import sympy as S
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_STATE_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-14.md','docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md']

def check_inverse():
    rows=[]
    def ck(n,b,d=None):rows.append({'name':n,'ok':bool(b),'details':d})
    def zero(n,x):
     v=S.simplify(x);b=v==S.zeros(*v.shape) if isinstance(v,S.MatrixBase) else v==0;ck(n,b,str(v))
    i=S.I
    T=S.Matrix([[1,i,0],[0,1,1]]);B=S.Matrix([[1,2*i],[3-i,1]]);C=B*B.H
    R=T.H*(T*T.H).inv()
    P=R*C*R.H
    zero('general.right_inverse',T*R-S.eye(2));zero('general.reconstructed_covariance',T*P*T.H-C);zero('general.P_hermitian',P-P.H);zero('general.P_factorization',P-(R*B)*(R*B).H)
    z=S.Matrix([-i,1,-1]);zero('general.kernel_vector',T*z);N=z*z.H;zero('general.kernel_family',T*(P+N)*T.H-C)
    Ccross=R*B+z*S.Matrix([[1,i]]);Pc=Ccross*Ccross.H
    zero('general.cross_block_feasible',T*Pc*T.H-C);ck('general.kernel_addition_not_exhaustive',T*(Pc-P)!=S.zeros(2,3))
    # Rank-deficient exact projection. The impossible covariance is PSD but outside transfer support.
    a=2-i;Ts=S.Matrix([1,a]);Rs=Ts.H/(Ts.H*Ts)[0];Pi=Ts*Rs;Cs=3*Ts*Ts.H
    zero('rank.projector',Pi*Pi-Pi);zero('rank.projector_hermitian',Pi-Pi.H);zero('rank.feasible_support',(S.eye(2)-Pi)*Cs);zero('rank.exact_reconstruction',Ts*(Rs*Cs*Rs.H)*Ts.H-Cs)
    bad=S.eye(2);ck('rank.PSD_alone_not_enough',(S.eye(2)-Pi)*bad!=S.zeros(2));zero('rank.ordered_complex_cross',Cs[0,1]-S.conjugate(a)*Cs[0,0]);ck('rank.wrong_conjugation_rejected',Cs[0,1]!=a*Cs[0,0])
    left=S.Matrix([[-a,1]]);zero('rank.left_null',left*Ts);zero('rank.left_covariance',left*Cs);ck('rank.incompatible_left_witness',left*bad!=S.zeros(1,2))
    # Candidate Hamiltonian constraint in the declared origin event with zero field perturbations.
    H,rm,rr,p=S.symbols('H rm rr p',positive=True);W,th,de=S.symbols('W th de',real=True)
    momentum_factor=3
    radiation_factor=4
    T0=S.Matrix([[-rm/p**2,-momentum_factor*H*rm/p**4,-radiation_factor*rr/p**2],[0,1,0],[1,0,0]])
    R0=S.Matrix([[0,0,1],[0,1,0],[-p**2/(4*rr),-3*H*rm/(4*rr*p**2),-rm/(4*rr)]])
    zero('candidate.determinant',T0.det()-4*rr/p**2);zero('candidate.right_inverse',T0*R0-S.eye(3))
    n,theta,mon=S.symbols('n theta mon',real=True);XX=S.Matrix([n,theta,mon]);YY=T0*XX
    zero('candidate.initial_constraint',p*p*YY[0]+rm*n+4*rr*mon+3*H*rm*theta/p**2)
    zero('candidate.physical_density',YY[2]-n);zero('candidate.physical_velocity',YY[1]-theta)
    target=S.Matrix([W,th,de]);initial=R0*target
    zero('candidate.reconstructed_constraint',p*p*W+rm*initial[0]+4*rr*initial[2]+3*H*rm*initial[1]/p**2)
    zero('candidate.monopole_charge',initial[2]+(p*p*W+rm*de+3*H*rm*th/p**2)/(4*rr))
    # Dust forces subsequent motion: the initial origin is not a constant vacuum background.
    k=S.symbols('k',positive=True);ak=(1-k)*(1+3*k)/4;sk=(1+k)/(k*(1-3*k));j0=1+(1-3*ak)*sk;ku=j0/(1+sk)**2;bu=S.sqrt(ak)/(1+sk)
    zero('candidate.origin_coupling',bu*bu/ku-k)
    for kv in [S.Rational(1,10),S.Rational(2,13)]:
     acc=(-rm*bu/ku).subs({k:kv,rm:S.Rational(3,4)})
     ck('candidate.dust_acceleration_nonzero',acc!=0,str(acc))
    # Bounded exact Rademacher populations realize the requested output covariance at two synthetic backgrounds.
    B0=S.Matrix([[1,2,0],[0,1,1],[1,0,3]]);configs=[{H:1,rm:S.Rational(3,4),rr:S.Rational(3,8),p:S.Rational(5,3),'Hv':S.Rational(1,2)},{H:S.Rational(6,5),rm:S.Rational(8,5),rr:S.Rational(1,50),p:S.Rational(7,4),'Hv':S.Rational(3,5)}];data=[]
    for q in configs:
     sub={key:v for key,v in q.items() if key!='Hv'};tm=T0.subs(sub);rc=R0.subs(sub);load=rc*B0
     scales=[sum(abs(x) for x in load.row(0)),sum(abs(x) for x in load.row(1))/q[p],4*sum(abs(x) for x in load.row(2)),sum(abs(x) for x in B0.row(0))];eps=1/(100*max(scales));cov=S.zeros(3);icov=S.zeros(3);worst=S.Integer(0)
     zero('realization.background_constraint',q[H]**2-q['Hv']**2-2*(q[rm]+q[rr])/3)
     for signs in itertools.product([-1,1],repeat=3):
      zz=S.Matrix(signs);yy=eps*B0*zz;xx=rc*yy;actual=tm*xx;cov+=actual*actual.T/8;icov+=xx*xx.T/8
      zero('realization.each_constraint',(p*p*yy[0]+rm*xx[0]+4*rr*xx[2]+3*H*rm*xx[1]/p**2).subs(sub))
      ck('realization.positive_populations',1+xx[0]>0 and 1+4*xx[2]>0)
      worst=max(worst,abs(xx[0]),abs(4*xx[2]),abs(xx[1])/q[p],abs(yy[0]))
     zero('realization.exact_output_covariance',cov-eps**2*B0*B0.T);zero('realization.exact_initial_covariance',icov-rc*(eps**2*B0*B0.T)*rc.T);ck('realization.weak_bounds',worst<=S.Rational(1,100),str(worst));data.append({'background':{str(key):str(v) for key,v in q.items()},'common_amplitude':str(eps),'largest_dimensionless_amplitude':str(worst),'output_covariance':str(cov),'initial_covariance':str(icov)})
    # Small-radiation and high-p obstruction to uniform fixed-amplitude realization.
    monopole=-(p*p*W+rm*de+3*H*rm*th/p**2)/(4*rr)
    zero('limits.inverse_radiation_scaling',S.diff(monopole,rr)+monopole/rr)
    ck('limits.high_p_fixed_W_unbounded',S.limit(monopole.subs({W:1,de:0,th:0,rr:1}),p,S.oo)==-S.oo)
    result={'scope':'Exact algebra and bounded synthetic initial data, no orbit/observational fit or state selector.','passed':sum(r['ok'] for r in rows),'failed':sum(not r['ok'] for r in rows),'checks':rows,'bounded_realizations':data}
    return result

def check_ensemble():
    rows=[]
    def zero(n,e):
     v=S.simplify(S.trigsimp(e));rows.append({'name':n,'ok':bool(v==0),'residual':str(v)})
    def ck(n,b):rows.append({'name':n,'ok':bool(b)})
    f,a,b=S.symbols('f a b',real=True)
    zero('phase.zero_mean',S.integrate(S.cos(a+f),(f,0,2*S.pi)))
    zero('phase.cross_covariance',S.integrate(2*S.cos(a+f)*S.cos(b+f),(f,0,2*S.pi))/(2*S.pi)-S.cos(a-b))
    u=S.symbols('u',real=True);z=S.symbols('z',positive=True);sphere=S.integrate(S.cos(z*u),(u,-1,1))/2
    zero('sphere.isotropic_kernel',sphere-S.sin(z)/z);zero('sphere.equal_point_limit',S.limit(sphere,z,0)-1)
    zero('phase.translation_invariance',S.cos((a+f)-(b+f))-S.cos(a-b));zero('sphere.parity_invariance',S.cos(z*u)-S.cos(-z*u))
    x,y,w=S.symbols('x y w',real=True);p,A=S.symbols('p A',positive=True);n=S.Matrix([S.Rational(2,3),S.Rational(-1,3),S.Rational(2,3)]);pos=S.Matrix([x,y,w]);phase=p*n.dot(pos)+f;vel=A*n*S.sin(phase)/p
    zero('velocity.physical_divergence',sum(S.diff(vel[j],pos[j]) for j in range(3))-A*S.cos(phase));zero('spatial.mode_eigenvalue',sum(S.diff(S.cos(phase),t,2) for t in pos)+p*p*S.cos(phase));zero('velocity.unit_direction',n.dot(n)-1)
    B=S.Matrix([[1,2,0],[0,1,1],[1,0,3]]);H=S.Rational(1);rm=S.Rational(3,4);rr=S.Rational(3,8);pv=S.Rational(5,3);R=S.Matrix([[0,0,1],[0,1,0],[-pv**2/(4*rr),-3*H*rm/(4*rr*pv**2),-rm/(4*rr)]]);load=R*B;scales=[sum(abs(q) for q in load.row(0)),sum(abs(q) for q in load.row(1))/pv,4*sum(abs(q) for q in load.row(2)),sum(abs(q) for q in B.row(0))];eps=1/(100*S.sqrt(2)*max(scales));G=S.zeros(3)
    for sign in itertools.product([-1,1],repeat=3):
     Z=S.Matrix(sign);am=S.sqrt(2)*eps*B*Z;initial=R*am;G+=am*am.T/16
     ck('bounded.every_sign',max(abs(initial[0]),4*abs(initial[2]),abs(initial[1])/pv,abs(am[0]))<=S.Rational(1,100))
     zero('constraint.every_sign',pv*pv*am[0]+rm*initial[0]+4*rr*initial[2]+3*H*rm*initial[1]/pv**2)
    for j in range(3):
     for k in range(3):zero('covariance.phase_signs_'+str(j)+str(k),(G-eps**2*B*B.T)[j,k])
    r={'scope':'Exact phase/sphere integration and bounded local initial-data realization. No actual survey, ergodicity, evolution or state-selection inference.','passed':sum(x['ok'] for x in rows),'failed':sum(not x['ok'] for x in rows),'checks':rows,'epsilon':str(eps),'S0':str(B*B.T)}
    return r

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--output');args=a.parse_args()
    checks=[];units={};outputs={}
    for name,fn in [('inverse',check_inverse),('ensemble',check_ensemble)]:
        r=fn();rows=[]
        for old in r['checks']:
            row=dict(old);row['passed']=row.pop('ok');row['name']=name+'::'+row['name'];rows.append(row)
        checks.extend(rows);units[name]={'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows)}
        outputs[name]={k:v for k,v in r.items() if k not in ['checks','passed','failed']}
    result={'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'checks':checks,'units':units,'substantive_outputs':outputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Conditional initial-covariance feasibility and bounded homogeneous isotropic witness; no observed fit or selected state.'}
    if args.output:
        out=Path(args.output);assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(bool(result['failed']))
