"""Conditional lensing/velocity inverse and synthetic controls. No empirical fit.

Core derivations are root-authored. The background source_model differentiates
the same supplied action as the previously checked cosmological inverse; copied
explicitly here so this scientific helper has no unmerged-code dependency.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import math
import json
import numpy as np
import sympy as s
import sympy as sp
import mpmath as mp
from scipy.integrate import solve_ivp


def pole_inverse(x1, r1, x2, r2):
    x1, r1, x2, r2 = [real_number(x) for x in [x1, r1, x2, r2]]
    if min(x1, r1, x2, r2) <= 0 or x1 == x2:
        raise ValueError('distinct positive scales and responses required')
    intercept = (x1/r1-x2/r2)/(x1-x2)
    slope = x1*(1/r1-intercept)
    if intercept <= 0 or slope < 0:
        raise ValueError('positive coupling and nonnegative pole mass required')
    return s.simplify(1/intercept), s.simplify(slope/intercept)


def response_controls():
    checks=[]
    def zero(name,expr):
        value=s.factor(s.cancel(expr))
        checks.append({'name':name,'passed':value==0,'detail':str(value)})
    F,x,dr,df,q,mu=s.symbols('F x dr df q mu',positive=True)
    Phi,Psi=s.symbols('Phi Psi')
    potentials=s.solve([-2*F*x*Phi-dr+x*df,-2*F*x*Psi-dr-x*df],(Phi,Psi))
    zero('Weyl_from_two_metric_equations',-x*(potentials[Phi]+potentials[Psi])-dr/F)
    zero('metric_slip_sign',potentials[Phi]-potentials[Psi]-df/F)
    ratio=((potentials[Psi]-potentials[Phi])/(potentials[Psi]+potentials[Phi])).subs(df,q*dr/(x+mu))
    zero('single_pole_from_scalar_response',ratio-q*x/(x+mu))
    P,Y,a,h,P3=s.symbols('P Y a h P3',positive=True)
    force=3*P*(1+q)/(2*a**3*Y)
    zero('observable_quotient_normalization',2*Y*a**3*force/(3*P)-1-q)
    zero('factor_two_wrong_convention_witness',2*Y*a**3*force/(6*P)-1-(q-1)/2)
    for mass in [s.Integer(0),s.Rational(1,7),s.Integer(9)]:
        qa=s.Rational(2,9);x1=s.Integer(3);x2=s.Integer(11)
        got=pole_inverse(x1,qa*x1/(x1+mass),x2,qa*x2/(x2+mass))
        checks.append({'name':'positive_pole_inverse_'+str(mass),'passed':got==(qa,mass),'detail':str(got)})
    try:
        pole_inverse(2,s.Rational(2,7),5,s.Rational(5,24));refused=False
    except ValueError:refused=True
    checks.append({'name':'negative_mass_refused','passed':refused})
    beta=s.symbols('beta',positive=True);Z=coupling_shape(beta,q)
    zero('candidate_chart_inverse',beta*(Z-1)/(Z-3*beta)-q)
    zero('candidate_chart_derivative',s.diff(Z,q)-beta*(1-3*beta)/(beta-q)**2)
    t,O,A,S=s.symbols('t O A S',positive=True)
    field=S/O**2+A*s.cos(O*t)
    zero('unexcluded_homogeneous_mode',s.diff(field,t,2)+O**2*field-S)
    zero('quasistatic_discrepancy',field-S/O**2-A*s.cos(O*t))
    lam,rho,delta,H0=s.symbols('lam rho delta H0',positive=True)
    zero('absolute_normalization_freedom',lam*rho*delta/(3*H0**2*lam*F)-rho*delta/(3*H0**2*F))
    # Reconstruct the potential in the SAME normalized mode from the Weyl sum.
    What,r=s.symbols('What r',real=True)
    phi=-3*H0**2*a**-3*P*What*(1-r)/(2*x)
    weyl=-3*H0**2*a**-3*P*What/x
    zero('potential_from_slip_and_Weyl',2*phi-(1-r)*weyl)
    return checks


def run(protocol):
    exact=extended_controls()
    forward=forward_controls(protocol)
    checks=response_controls()+exact['checks']+forward['checks']
    return {'status':'conditional-support','checks':checks,
            'passed':sum(bool(c['passed']) for c in checks),
            'failed':sum(not c['passed'] for c in checks),
            'exceptional_pairs':exact['exceptional_pairs'],
            'background_failures':exact['background_failures'],
            'histories':forward['histories'],
            'independent_empirical_tests':0,
            'full_action_perturbations_solved':False,
            'scope':protocol['scope']}


def real_number(value):
    value = s.sympify(value)
    if value.is_real is not True or value.is_finite is not True:
        raise ValueError("finite real inputs required")
    return value

def positive_q(value):
    value = real_number(value)
    if not 0 < value < s.Rational(1, 3):
        raise ValueError("positive candidate coupling below one third required")
    return value

def coupling_shape(beta, q):
    return beta * (1 - 3*q) / (beta-q)


def candidate_domain(rows, candidate):
    """Only the listed sampled rows are checked, never an unsampled interval."""
    try:
        beta,B,C=[real_number(candidate[k]) for k in ('beta','B','C')]
        values=[(real_number(row['q']),real_number(row['J'])) for row in rows]
    except (ValueError,TypeError,KeyError):
        return False
    return bool(values) and bool(s.Rational(1,4)<beta<s.Rational(1,3) and B>0 and all(
        0<q<beta and J+C>0 for q,J in values))


def assess_candidate(rows,candidate,indices,tolerance):
    """Gate finite sampled inputs before poles and refuse nonfinite arithmetic."""
    rejected={'candidate':candidate,'relative_residuals':[],
              'sampled_domain_passed':False,'within_fixed_threshold':False}
    if not candidate_domain(rows,candidate):
        return rejected
    try:
        if real_number(tolerance)<=0:
            return rejected
        for row in rows:
            if real_number(row['P'])<=0 or real_number(row['What'])<=0:
                return rejected
    except (ValueError,TypeError,KeyError):
        return rejected
    beta,B,C=[candidate[key] for key in ('beta','B','C')]
    residuals=[]
    for i in indices:
        row=rows[i];Z=coupling_shape(beta,row['q'])
        lhs=Z*row['P']*row['What'];rhs=B*(row['J']+C)
        residual=(lhs-rhs)/max(abs(lhs),abs(rhs),1e-30)
        try:
            real_number(residual)
        except (ValueError,TypeError):
            return {**rejected,'sampled_domain_passed':True,
                    'arithmetic_failure':'nonfinite residual'}
        residuals.append(residual)
    return {'candidate':candidate,'relative_residuals':residuals,
            'sampled_domain_passed':True,
            'within_fixed_threshold':bool(residuals) and max(map(abs,residuals))<tolerance}

def validate_rows(rows):
    converted = []
    for row in rows:
        out = {k: real_number(row[k]) for k in ('P', 'W', 'J')}
        out['q'] = positive_q(row['q'])
        if out['P'] <= 0 or out['W'] <= 0:
            raise ValueError("positive lensing/velocity branch required")
        converted.append(out)
    return converted

def integrated_inverse(rows):
    if len(rows) != 3:
        raise ValueError("three calibration epochs required")
    rows = validate_rows(rows)
    q = [v['q'] for v in rows]
    J = [v['J']-rows[0]['J'] for v in rows]
    if J[1] == 0 or J[2] == 0 or J[1] == J[2]:
        raise ValueError("three distinct density-primitive values required")
    t = [v['P']*v['W']*(1-3*v['q']) for v in rows]
    C = [t[0]*(J[2]-J[1]), -t[1]*J[2], t[2]*J[1]]
    beta = s.Symbol('beta', real=True)
    poly = s.Poly(s.expand(sum(C[i]*s.prod(beta-q[j] for j in range(3) if j != i)
                              for i in range(3))), beta)
    if poly.is_zero:
        return {'polynomial': poly, 'rank_failure': True, 'candidates': []}
    candidates = []
    for root in s.real_roots(poly):
        if root in [x['beta'] for x in candidates]:
            continue
        if not max(s.Rational(1, 4), *q) < root < s.Rational(1, 3):
            continue
        Z = [coupling_shape(root, v) for v in q]
        B = s.simplify((Z[1]*rows[1]['P']*rows[1]['W']-
                        Z[0]*rows[0]['P']*rows[0]['W'])/J[1])
        if B > 0:
            offset = s.simplify(Z[0]*rows[0]['P']*rows[0]['W']/B-rows[0]['J'])
            candidates.append({'beta': root, 'B': B, 'C': offset})
    return {'polynomial': poly, 'rank_failure': False, 'candidates': candidates}

def lift_inverse(rows):
    rows = validate_rows(rows)
    if len(rows) < 4:
        raise ValueError("at least four rows required for full-rank lift")
    M = s.Matrix([[1, -r['J']*r['q'], -r['q'],
                   -r['P']*r['W']*(1-3*r['q'])] for r in rows])
    rhs = s.Matrix([-r['J'] for r in rows])
    rank = M.rank()
    if M.row_join(rhs).rank() > rank:
        return {'rank': rank, 'status': 'inconsistent', 'candidate': None}
    if rank < 4:
        return {'rank': rank, 'status': 'rank_failure', 'candidate': None}
    C, u, w, v = M.gauss_jordan_solve(rhs)[0]
    compatibility = s.factor(w-u*C)
    if compatibility != 0:
        return {'rank': rank, 'status': 'nonlinear_incompatibility',
                'compatibility': compatibility, 'candidate': None}
    if not 3 < u < 4 or v <= 0 or any(r['q'] >= 1/u for r in rows):
        return {'rank': rank, 'status': 'outside_chart', 'candidate': None}
    return {'rank': rank, 'status': 'admitted',
            'candidate': {'beta': s.simplify(1/u), 'B': s.simplify(1/v), 'C': C}}

def tensor_inverse(qi, qj, F_ratio):
    qi, qj = positive_q(qi), positive_q(qj)
    F_ratio = real_number(F_ratio)
    if F_ratio <= 0:
        raise ValueError("positive physical F ratio required")
    if qi == qj:
        raise ValueError("equal-coupling endpoints do not identify beta")
    U = F_ratio*(1-3*qi)/(1-3*qj)
    if U == 1:
        raise ValueError("no finite shape at this tensor/coupling ratio")
    beta = s.simplify((U*qj-qi)/(U-1))
    if not max(s.Rational(1, 4), qi, qj) < beta < s.Rational(1, 3):
        raise ValueError("candidate chart failed")
    return beta

def background_residual(N, Z, q, B, Y):
    """Undivided flat-dust second metric identity in H0,Fc units."""
    omega = (1/q-3)/2
    return s.factor((2*Z+s.diff(Z, N))*s.diff(Y, N)/2 +
                    (s.diff(Z, N, 2)-s.diff(Z, N)+omega*s.diff(Z, N)**2/Z)*Y +
                    3*B*s.exp(-3*N))

def relative_potential(N, Z, B, Y):
    """V/(Fc H0^2), before any supplied potential-basis fit."""
    return (Z*(3*Y+s.diff(Y, N)/2)-3*B*s.exp(-3*N)/2+
            Y*s.diff(Z, N, 2)/2+s.diff(Y, N)*s.diff(Z, N)/4+
            5*Y*s.diff(Z, N)/2)

def source_model():
    """Differentiate the supplied Einstein action, before constructing readouts."""
    u, k, nu = sp.symbols("u k nu", real=True)
    ac = (1-k)*(1+3*k)/4
    alpha = sp.sqrt(ac)
    s = (1+k)/(k*(1-3*k))
    E = sp.exp(2*alpha*u)
    W = 1+s*E
    J = 1+(1-3*ac)*s*E
    K = J/W**2
    A = sp.sqrt((1+s)*E/W)
    b = alpha/W
    U = sp.Rational(3,2)+3*s*(E-1)**2/(2*W**2)+nu*(1+s)*u**2/(2*W**2)
    return sp.lambdify((u,k,nu), (K,sp.diff(K,u),A,b,sp.diff(b,u),U,sp.diff(U,u)), "numpy", cse=True)

def inverse_rows(rows):
    """Only synthesized observables q,P,What,J enter; no source parameters."""
    vals=[{k:mp.mpf(str(v[k])) for k in ['q','P','What','J']} for v in rows]
    if len(vals)!=3 or any(not all(mp.isfinite(v) for v in x.values()) or
                          not (0<x['q']<mp.mpf(1)/3 and x['P']>0 and x['What']>0) for x in vals):
        raise ValueError('outside positive candidate inputs')
    q=[x['q'] for x in vals];J=[x['J']-vals[0]['J'] for x in vals]
    if J[1]==0 or J[2]==0 or J[1]==J[2]:raise ValueError('primitive rank failure')
    t=[x['P']*x['What']*(1-3*x['q']) for x in vals]
    C=[t[0]*(J[2]-J[1]),-t[1]*J[2],t[2]*J[1]]
    a=sum(C);b=-sum(C[i]*sum(q[j] for j in range(3) if j!=i) for i in range(3))
    c=sum(C[i]*mp.fprod(q[j] for j in range(3) if j!=i) for i in range(3))
    roots=[]
    if a==0:
        if b==0:raise ValueError('zero polynomial or inconsistent constant')
        roots=[-c/b]
    else:
        disc=b*b-4*a*c
        if disc>=0:roots=[(-b-mp.sqrt(disc))/(2*a),(-b+mp.sqrt(disc))/(2*a)]
    candidates=[]
    for beta in roots:
        if not max(mp.mpf(1)/4,*q)<beta<mp.mpf(1)/3:continue
        Z=lambda qi: beta*(1-3*qi)/(beta-qi)
        B=(Z(q[1])*vals[1]['P']*vals[1]['What']-Z(q[0])*vals[0]['P']*vals[0]['What'])/J[1]
        if B<=0:continue
        offset=Z(q[0])*vals[0]['P']*vals[0]['What']/B-vals[0]['J']
        candidates.append({'beta':float(beta),'B':float(B),'C':float(offset)})
    return {'candidates':candidates,'coefficients':[mp.nstr(x,65) for x in [a,b,c]],
            'q_range':float(max(q)-min(q))}

def extended_controls():
    checks = []
    def check(name, passed, detail=None):
        checks.append({'name':name,'passed':bool(passed),'detail':detail})
    def zero(name, expr):
        expr = s.factor(s.cancel(expr))
        check(name, expr == 0, str(expr))
    def refusal(name, call):
        try:
            call()
            check(name, False, 'invalid inputs accepted')
        except ValueError as error:
            check(name, True, str(error))

    N = s.Symbol('N', real=True)
    beta, B, C = s.Rational(29,100), s.Rational(1,5), s.Integer(2)
    epochs = [0,s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Integer(1)]
    # q is non-Mobius in J=N, giving a genuinely full-rank comparison.
    q = s.Rational(2,25)+N/30+N**2/100
    P = B*(N+C)/coupling_shape(beta,q)
    rows = [{'q':q.subs(N,n),'P':P.subs(N,n),'W':1,'J':n} for n in epochs]
    inverse = integrated_inverse(rows[:3]); lift = lift_inverse(rows[:4])
    check('quadratic_includes_generating_tuple', {'beta':beta,'B':B,'C':C} in inverse['candidates'])
    check('independent_lift_rank_four', lift['rank']==4, lift)
    check('lift_exact_recovery', lift['candidate']=={'beta':beta,'B':B,'C':C})
    check('fifth_row_consistency', lift_inverse(rows)['status']=='admitted')
    check('later_chart_escape_refused',not candidate_domain(
        [rows[0],{**rows[-1],'q':s.Rational(3,10)}],{'beta':beta,'B':B,'C':C}))
    check('later_negative_density_refused',not candidate_domain(
        [rows[0],{**rows[-1],'J':-3}],{'beta':beta,'B':B,'C':C}))
    check('exact_upper_boundary_neighborhood',candidate_domain(
        rows,{'beta':s.Rational(1,3)-s.Rational(1,10**20),'B':B,'C':C}))
    check('nonfinite_density_normalization_refused',not candidate_domain(
        rows,{'beta':beta,'B':s.oo,'C':C}))
    check('nonfinite_density_offset_refused',not candidate_domain(
        rows,{'beta':beta,'B':B,'C':s.oo}))
    pole_row={'q':beta,'J':1,'P':1,'What':1}
    pole_assessment=assess_candidate([pole_row],{'beta':beta,'B':B,'C':C},[0],1e-9)
    check('later_pole_preserved_without_division',
          not pole_assessment['sampled_domain_passed'] and pole_assessment['relative_residuals']==[],pole_assessment)
    assessment_rows=[{**row,'What':row['W']} for row in rows]
    for field in ['P','What']:
        invalid_rows=[dict(row) for row in assessment_rows]
        invalid_rows[-1][field]=float('inf')
        result=assess_candidate(invalid_rows,{'beta':beta,'B':B,'C':C},[0,4],1e-9)
        check('nonfinite_later_'+field+'_refused',not result['within_fixed_threshold'] and
              not result['sampled_domain_passed'],result)
    overflow_rows=[{'q':0.1,'J':0.0,'P':1e308,'What':1e308}]
    overflow=assess_candidate(overflow_rows,{'beta':0.29,'B':0.2,'C':2.0},[0],1e-9)
    check('nonfinite_arithmetic_refused',not overflow['within_fixed_threshold'] and
          overflow.get('arithmetic_failure')=='nonfinite residual',overflow)
    for field in ['q','P','What','J']:
        invalid_rows=[dict(row) for row in assessment_rows[:3]]
        invalid_rows[1][field]=float('inf')
        refusal('nonfinite_calibration_'+field,lambda invalid_rows=invalid_rows:inverse_rows(invalid_rows))
    altered = [dict(x) for x in rows[:4]]; altered[3]['P'] *= s.Rational(101,100)
    check('linear_fit_requires_nonlinear_compatibility',
          lift_inverse(altered)['status']=='nonlinear_incompatibility', lift_inverse(altered))
    # The algebra permits a decreasing primitive as well as increasing one.
    decreasing = [{**x,'J':-x['J']} for x in rows[:3]]
    check('negative_density_slope_not_accepted',integrated_inverse(decreasing)['candidates']==[])
    shifted = [{**x,'J':x['J']+7} for x in rows[:3]]
    check('primitive_origin_does_not_select_state',
          {'beta':beta,'B':B,'C':C-7} in integrated_inverse(shifted)['candidates'])
    # Independent reviewer witness: accepted by v1, refused by v2.
    bad = [{'q':s.Rational(-1,10),'P':s.Rational(27,26),'W':1,'J':0},
           {'q':s.Rational(-39,400),'P':s.Rational(5365,4136),'W':1,'J':s.Rational(1,4)},
           {'q':s.Rational(-19,200),'P':s.Rational(1599,1028),'W':1,'J':s.Rational(1,2)}]
    refusal('negative_q_reported_witness',lambda:integrated_inverse(bad))
    for value in [s.Integer(0),s.Rational(-1,10),s.Rational(1,3),s.oo,s.nan,s.I]:
        changed = [{**x,'q':value} for x in rows[:3]]
        refusal('invalid_q_quadratic_'+str(value),lambda changed=changed:integrated_inverse(changed))
        refusal('invalid_q_tensor_'+str(value),lambda value=value:tensor_inverse(value,s.Rational(1,10),2))
    refusal('tensor_nonpositive_ratio',lambda:tensor_inverse(s.Rational(1,10),s.Rational(1,9),0))
    refusal('equal_q_tensor_rank',lambda:tensor_inverse(s.Rational(1,10),s.Rational(1,10),1))
    refusal('repeated_primitive',lambda:integrated_inverse([rows[0],rows[0],rows[2]]))
    # Exact Möbius second solution, including a nonzero denominator slope.
    x,u,v,w,z,bb,Bb,Cc=s.symbols('x u v w z bb Bb Cc')
    qr=(u*x+v)/(w*x+z)
    b2=(v-u*Cc)/(z-w*Cc)
    C2=(bb*z-v)/(bb*w-u)
    B2=Bb*b2/bb*(bb*w-u)/(b2*w-u)
    flux=Bb*(x+Cc)/coupling_shape(bb,qr)
    zero('general_second_tuple_sufficiency',coupling_shape(b2,qr)*flux-B2*(x+C2))
    a1,a2,b1,b2s,c1,c2=s.symbols('a1 a2 b1 b2 c1 c2')
    qnecessary=(a1*b1*(x+c1)-a2*b2s*(x+c2))/(a1*(x+c1)-a2*(x+c2))
    zero('mobius_necessity_cross_multiply',a1*(b1-qnecessary)*(x+c1)-a2*(b2s-qnecessary)*(x+c2))
    exceptional=[]
    for btrue in [s.Rational(29,100),s.Rational(8,25)]:
        qr=s.Rational(9,50)-N/25
        pp=B*(N+C)/coupling_shape(btrue,qr)
        other=s.Rational(13,50); otherB=B*other/btrue
        otherC=25*(btrue-s.Rational(9,50))
        zero('interval_ambiguity_'+str(btrue),coupling_shape(other,qr)*pp-otherB*(N+otherC))
        rr=[{'q':qr.subs(N,n),'P':pp.subs(N,n),'W':1,'J':n} for n in epochs]
        got=integrated_inverse(rr[:3])
        check('two_exact_roots_'+str(btrue),len(got['candidates'])==2,got['candidates'])
        check('ambiguous_lift_has_rank_loss_'+str(btrue),lift_inverse(rr)['status']=='rank_failure')
        qi,qj=qr.subs(N,0),qr.subs(N,1)
        ratios=[s.factor(coupling_shape(b, qj)/coupling_shape(b,qi)) for b in [btrue,other]]
        check('tensor_ratios_differ_'+str(btrue),ratios[0]!=ratios[1],ratios)
        check('tensor_recovers_both_when_ratio_supplied_'+str(btrue),
              [tensor_inverse(qi,qj,T) for T in ratios]==[btrue,other])
        exceptional.append({'beta1':btrue,'beta2':other,'B2':otherB,'C2':otherC,'tensor_ratios':ratios})
    constant=[{'q':s.Rational(1,10),'P':1+n,'W':1,'J':n} for n in epochs[:3]]
    check('constant_q_continuum_branch',integrated_inverse(constant)['rank_failure'])
    # Exact linear-dust kinematic identity; isolated, not a full gravity solution.
    W=1+N/4; Phi=N/100; J=N+N**2/8+3*Phi; density=J+C
    zero('continuity_with_metric_term',s.diff(density,N)-W-3*s.diff(Phi,N))
    coupling=s.Rational(1,10)+N/50
    P=B*density/(coupling_shape(beta,coupling)*W)
    zero('corrected_integrated_density_identity',s.diff(coupling_shape(beta,coupling)*P*W,N)-B*s.diff(J,N))
    omitted=s.factor(s.diff(coupling_shape(beta,coupling)*P*W,N)-B*W)
    check('omitted_metric_term_is_detectable',omitted!=0,str(omitted))
    # A physical W!=0 need not make J monotone or nonconstant.
    zero('velocity_nonzero_but_density_constant',s.diff(N+3*(-N/3),N))
    # Independent symbolic change from Jordan-time metric equations.
    ZZ,Zp,Zpp,Y,Yp,Fc,H0,BB,Qq=s.symbols('ZZ Zp Zpp Y Yp Fc H0 BB Qq',positive=True)
    H=H0*s.sqrt(Y); Hd=H0**2*Yp/2
    F=Fc*ZZ; Fd=Fc*H*Zp; Fdd=Fc*H0**2*(Y*Zpp+Yp*Zp/2)
    omega=(1/Qq-3)/2; rho=3*H0**2*Fc*BB*s.exp(-3*N)
    raw=-2*F*Hd-rho-Fdd+H*Fd-omega*Fd**2/F
    expected=(2*ZZ+Zp)*Yp/2+(Zpp-Zp+omega*Zp**2/ZZ)*Y+3*BB*s.exp(-3*N)
    zero('background_kinetic_conversion',-raw/(Fc*H0**2)-expected)
    rawV=F*(3*H**2+Hd)-rho/2+Fdd/2+s.Rational(5,2)*H*Fd
    expectedV=ZZ*(3*Y+Yp/2)-3*BB*s.exp(-3*N)/2+Y*Zpp/2+Yp*Zp/4+s.Rational(5,2)*Y*Zp
    zero('background_potential_conversion',rawV/(Fc*H0**2)-expectedV)
    zz=2+N*N;yy=s.exp(-3*N)*(1+N)
    expected_function=rawV.subs({ZZ:zz,Zp:s.diff(zz,N),Zpp:s.diff(zz,N,2),
                                Y:yy,Yp:s.diff(yy,N),BB:s.Rational(1,5)})/(Fc*H0**2)
    zero('implemented_relative_potential',relative_potential(N,zz,s.Rational(1,5),yy)-expected_function)
    # Neither arbitrary reduced-history branch passes the FULL interval
    # kinetic plus Euler consistency. No observational model exclusion follows.
    q=s.Rational(9,50)-N/25; p=s.Rational(1,5)*(N+2)/coupling_shape(s.Rational(29,100),q)
    failures=[]
    for br,Br in [(s.Rational(29,100),s.Rational(1,5)),(s.Rational(13,50),s.Rational(26,145))]:
        Z=coupling_shape(br,q); om=(1/q-3)/2
        L1=2*Z+s.diff(Z,N); L0=s.diff(Z,N,2)-s.diff(Z,N)+om*s.diff(Z,N)**2/Z
        # Y=e^-3N f is necessary after eliminating Y' with Euler, P3=0.
        f=s.factor(-(s.Rational(3,2)*L1*p*(1+q)+3*Br)/(L0-2*L1))
        euler=s.factor((s.diff(f,N)+f)/2-s.Rational(3,2)*p*(1+q))
        value=s.factor(euler.subs(N,0))
        check('background_rejects_manufactured_history_'+str(br),value!=0,str(value))
        check('necessary_expansion_positive_at_origin_'+str(br),f.subs(N,0)>0,str(f.subs(N,0)))
        # The failure is Euler compatibility of the algebraic Y, not the
        # identity used to derive that algebraic Y.
        kinetic=background_residual(N,Z,q,Br,s.exp(-3*N)*f)
        zero('eliminated_system_residual_relation_'+str(br),s.exp(3*N)*kinetic-L1*euler)
        failures.append({'beta':br,'B':Br,'necessary_Y0':f.subs(N,0),'Euler_residual_at_0':value,
                         'meaning':'Manufactured reduced identity is not a full background solution.'})
    return {'checks':checks,'exceptional_pairs':exceptional,'background_failures':failures}


def forward_controls(protocol):
    evaluate=source_model()
    checks=[];histories=[]
    def check(name,passed,detail=None):checks.append({'name':name,'passed':bool(passed),'detail':detail})
    for caseid,case in enumerate(protocol['cases']):
        k,nu,Q0,Hv=[case[n] for n in ['k','nu','Q0','Hv']]
        Q=Q0*(1+k);beta=(1-k)*(1+3*k)/4;alpha=math.sqrt(beta)
        sc=(1+k)/(k*(1-3*k));Fc=Q*sc/(1+sc)
        def background(y):
            u,v,rhoE,aE=y[:4]
            K,Ku,A,b,bu,U,Uu=[float(x) for x in evaluate(u,k,nu)]
            HE=math.sqrt((K*v*v+2*Hv*Hv*U+rhoE/Q)/3)
            vd=-Ku*v*v/(2*K)-3*HE*v-Hv*Hv*Uu/K-b*rhoE/(2*Q*K)
            HEd=-K*v*v-rhoE/(2*Q)
            ndot=HE+b*v;H=ndot/A
            Hd=(HEd+b*vd+(bu-b*b)*v*v-HE*b*v)/(A*A)
            F=Q/(A*A);Fp=-2*F*b*v/ndot
            Fdd=-2*F/(A*A)*(b*vd+(bu-3*b*b)*v*v)
            Fpp=(Fdd-Hd*Fp)/(H*H)
            q=b*b/K;qu=2*b*bu/K-b*b*Ku/(K*K);qp=qu*v/ndot
            return {'K':K,'A':A,'HE':HE,'vd':vd,'ndot':ndot,'H':H,'Hd':Hd,
                    'F':F,'Fp':Fp,'Fpp':Fpp,'rho':rhoE/A**4,'q':q,'qp':qp,
                    'Z':F/Fc,'Zp':Fp/Fc,'Zpp':Fpp/Fc,'U':U,'b':b}
        initial_background=[case['u0'],case['v0_over_Hv']*Hv,
                            case['rhoE_over_QHv2']*Q*Hv*Hv,1.0]
        init=background(initial_background);A0=init['A'];H0=init['H'];B=init['rho']/(3*H0*H0*Fc)
        end=protocol['duration_over_inverse_Hv']/Hv
        for modeid,(K0,dv) in enumerate(zip(protocol['mode_K0_over_H0'],protocol['initial_density_and_velocity'])):
            delta0,W0=dv
            def perturb_read(y):
                bg=background(y);N=math.log(bg['A']*y[3]/A0);aa=math.exp(N)
                K2=(K0*H0/aa)**2
                cphi=bg['rho']*(1-bg['q'])/(2*bg['F']*K2)
                cphip=cphi*(-1-bg['qp']/(1-bg['q'])-bg['Fp']/bg['F'])
                delta,W=y[4:6]
                dp=(W-3*cphip*delta)/(1+3*cphi)
                Wp=bg['rho']*delta*(1+bg['q'])/(2*bg['F']*bg['H']**2)-(2+bg['Hd']/bg['H']**2)*W
                Phi=-cphi*delta
                return bg,N,dp,Wp,Phi
            def ode(t,y):
                bg,N,dp,Wp,Phi=perturb_read(y)
                u,v,rhoE,aE,delta,W,I=y
                return [v,bg['vd'],(-3*bg['HE']+bg['b']*v)*rhoE,bg['HE']*aE,
                        dp*bg['ndot'],Wp*bg['ndot'],W*bg['ndot']]
            y0=initial_background+[delta0,W0,0.0]
            Phi0=perturb_read(y0)[4]
            solution=solve_ivp(ode,[0,end],y0,method=protocol['method'],rtol=protocol['rtol'],
                               atol=protocol['atol'],max_step=end/protocol['max_step_divisor'],dense_output=True)
            check(f'case{caseid}_mode{modeid}_solver',solution.success,solution.message)
            if not solution.success:
                histories.append({'caseid':caseid,'modeid':modeid,'failure':solution.message});continue
            rows=[]
            for frac in protocol['sample_time_fractions']:
                time=frac*end;y=solution.sol(time);bg,N,dp,Wp,Phi=perturb_read(y)
                u,v,rhoE,aE,delta,W,I=map(float,y);aa=math.exp(N)
                Y=(bg['H']/H0)**2;Yp=2*bg['Hd']/H0**2;h=bg['Hd']/bg['H']**2
                # The inverse sees ratios and common-mode integrals, not delta0 or Fc.
                L=aa**3*bg['rho']*delta/(3*H0**2*bg['F']);P=L/W;P3=Wp/W
                qobs=2*Y*aa**3*(P3+2+h)/(3*P)-1
                What=W/W0;J=(I+3*(Phi-Phi0))/W0
                Z,Zp,Zpp=[bg[key] for key in ['Z','Zp','Zpp']]
                omega=(1/bg['q']-3)/2
                kres=-2*Z*h-3*B*aa**-3/Y-Zpp+(1-h)*Zp-omega*Zp*Zp/Z
                vread=Z*(3*Y+Yp/2)-1.5*B*aa**-3+Y*Zpp/2+Yp*Zp/4+2.5*Y*Zp
                vsource=2*Q*Hv*Hv*bg['U']/(bg['A']**4*Fc*H0**2)
                rows.append({'timeE':time,'N':N,'q':qobs,'P':P,'P3':P3,'What':What,'J':J,
                             'E2':Y,'h':h,'Phihat':Phi/W0,'integral_What':I/W0,
                             'source_q':bg['q'],'source_Z':Z,'source_Zp':Zp,'source_Zpp':Zpp,
                             'source_delta_hat':delta/W0,'kinetic_residual':kres,
                             'potential_relative_residual':(vread-vsource)/vsource,
                             'kinematic_error':delta/W0-(J+delta0/W0),
                             'q_readout_error':qobs-bg['q']})
            prefix=f'case{caseid}_mode{modeid}'
            check(prefix+'_positive_chart',all(x['P']>0 and x['What']>0 and 0<x['q']<beta for x in rows))
            check(prefix+'_readout_slip',max(abs(x['q_readout_error']) for x in rows)<protocol['slip_absolute_tolerance'])
            check(prefix+'_exact_dust_continuity',max(abs(x['kinematic_error']) for x in rows)<protocol['integrated_identity_relative_tolerance'])
            check(prefix+'_background_potential',max(abs(x['potential_relative_residual']) for x in rows)<protocol['metric_potential_relative_tolerance'])
            # This residual is dimensionless and its scale is explicitly recorded.
            kscale=max(max(abs(x['source_Z']),abs(3*B*math.exp(-3*x['N'])/x['E2'])) for x in rows)
            check(prefix+'_background_kinetic',max(abs(x['kinetic_residual']) for x in rows)/kscale<protocol['metric_potential_relative_tolerance'])
            with mp.workdps(protocol['inverse_arithmetic_digits']):
                inverse=inverse_rows([rows[i] for i in protocol['calibration_indices']])
            # Truth is used ONLY for recovery diagnostics, never to construct roots.
            candidates=inverse['candidates']
            match=min(candidates,key=lambda x:abs(x['beta']/beta-1)) if candidates else None
            be=abs(match['beta']/beta-1) if match else float('inf')
            Be=abs(match['B']/B-1) if match else float('inf')
            Ce=abs(match['C']/(delta0/W0)-1) if match else float('inf')
            check(prefix+'_shape_in_returned_set',be<protocol['shape_relative_tolerance'],be)
            check(prefix+'_density_ratio_recovery',Be<protocol['B_relative_tolerance'],Be)
            check(prefix+'_initial_density_inferred_not_supplied',Ce<protocol['initial_density_recovery_relative_tolerance'],Ce)
            later=[]
            for candidate in candidates:
                later.append(assess_candidate(rows,candidate,protocol['synthetic_test_indices'],
                                              protocol['integrated_identity_relative_tolerance']))
            check(prefix+'_candidate_chart_at_all_sampled_epochs',
                  bool(later) and all(x['sampled_domain_passed'] for x in later))
            check(prefix+'_later_epoch_admits_candidate',any(x['within_fixed_threshold'] for x in later),later)
            histories.append({'caseid':caseid,'modeid':modeid,'case':case,'K0_over_H0':K0,
                              'source_truth':{'beta':beta,'B':B,'C':delta0/W0,'Fc':Fc,'H0':H0},
                              'rows':rows,'inverse':inverse,'later_tests':later,'nfev':solution.nfev})
    return {'checks':checks,'histories':histories}
