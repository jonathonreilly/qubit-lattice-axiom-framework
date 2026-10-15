"""Exact rational domains and error envelopes for the conditional momentum inverse.

Finite real decimal inputs are interpreted as exact supplied decimal numbers.
This does not certify observational input uncertainties, observable denominators, or floating ODE error.
Coefficient envelopes presume already admitted normalized physical inputs.
"""
from itertools import product
import json
from pathlib import Path
import sympy as sp


def rational(value):
    if isinstance(value, bool):
        raise ValueError('boolean is not a physical scalar')
    try:
        z = sp.Rational(str(value))
    except (TypeError, ValueError, ZeroDivisionError):
        raise ValueError('finite real rational input required') from None
    if z.is_finite is not True or z.is_real is not True:
        raise ValueError('finite real rational input required')
    return z


def vector3(values):
    if len(values) != 3:
        raise ValueError('three rows required')
    return sp.Matrix([rational(v) for v in values])


def system(P, r, M):
    P, r, M = vector3(P), vector3(r), vector3(M)
    if any(p == 0 for p in P):
        raise ValueError('normalized chart requires nonzero P')
    L = sp.Matrix([[1, -p/2, -p*t/2] for p, t in zip(P, r)])
    if L.det() == 0:
        raise ValueError('rank deficient momentum rows')
    return L, M


def inverse(P, r, M):
    L, rhs = system(P, r, M)
    R, x, y = L.inv()*rhs
    if R <= 0:
        raise ValueError('positive dust density/F required')
    if y == 0:
        raise ValueError('turning or unidentified ratio: y is zero')
    q = x/y
    if q <= 0:
        raise ValueError('positive canonical coupling q required')
    return dict(R=R, x=x, y=y, q=q)


def norm_inf(mat):
    return max(sum(abs(mat[i, j]) for j in range(mat.cols)) for i in range(mat.rows))


def error_envelope(P, r, M, eP, er, eM):
    L, rhs = system(P, r, M)
    P, r = vector3(P), vector3(r)
    eP, er, eM = vector3(eP), vector3(er), vector3(eM)
    if any(z < 0 for z in list(eP)+list(er)+list(eM)):
        raise ValueError('error envelopes must be nonnegative')
    li = L.inv(); zhat = li*rhs
    d = max((ep+abs(p)*et+abs(t)*ep+ep*et)/2 for p,t,ep,et in zip(P,r,eP,er))
    e = max(eM); n = norm_inf(li); eta = n*d
    out = dict(matrix_delta=d, rhs_delta=e, inverse_norm=n, eta=eta,
               Rhat=zhat[0], xhat=zhat[1], yhat=zhat[2])
    if eta >= 1:
        return dict(out, certified=False, reason='matrix envelope inconclusive')
    eps = n*(e+d*norm_inf(zhat))/(1-eta)
    out['state_error'] = eps
    if abs(zhat[2]) <= eps:
        return dict(out, certified=False, reason='ratio may cross turning domain')
    qhat = zhat[1]/zhat[2]
    qe = eps*(1+abs(qhat))/(abs(zhat[2])-eps)
    out.update(qhat=qhat, q_error=qe)
    ok = zhat[0] > eps and qhat > qe
    return dict(out, certified=bool(ok), reason='positive coefficients certified' if ok else 'positive coefficients inconclusive')


def checks():
    rows=[]
    def check(name, passed, **evidence):
        rows.append(dict(name=name, passed=bool(passed), **evidence))
    def refused(name, fn):
        try:
            fn()
        except (ValueError, TypeError):
            check(name, True)
        else:
            check(name, False)
    R,x,y=sp.Rational(4,5),sp.Rational(3,50),sp.Rational(2,5)
    P=list(map(sp.Rational,[1,2,4]));r=[sp.Rational(1,10),sp.Rational(1,3),sp.Rational(-1,5)]
    M=[R-p*x/2-p*t*y/2 for p,t in zip(P,r)]
    got=inverse(P,r,M)
    check('exact_known_state',got==dict(R=R,x=x,y=y,q=sp.Rational(3,20)))
    for value in [float('nan'),float('inf'),-float('inf'),1j,True,'z']:
        refused('nonfinite_or_nonreal_'+repr(value), lambda value=value: inverse([value,2,4],r,M))
    refused('wrong_row_count',lambda: inverse(P[:2],r,M))
    refused('zero_P_chart',lambda: inverse([0,2,4],r,M))
    refused('rank_deficiency',lambda: inverse([1,1,1],[1,1,1],M))
    refused('turning_point',lambda: inverse(P,r,[R]*3))
    for label,z in [('negative_R',(-R,x,y)),('zero_R',(0,x,y)),('negative_q',(R,-x,y)),('zero_q',(R,0,y))]:
        mm=[z[0]-p*z[1]/2-p*t*z[2]/2 for p,t in zip(P,r)]
        refused(label,lambda mm=mm: inverse(P,r,mm))
    eP=[sp.Rational(1,10**7)]*3;er=[sp.Rational(2,10**7)]*3;eM=[sp.Rational(3,10**7)]*3
    env=error_envelope(P,r,M,eP,er,eM)
    check('positive_error_certificate',env['certified'],epsilon=str(env['state_error']),q_error=str(env['q_error']))
    maximum=sp.S.Zero;maximumq=sp.S.Zero;allok=True
    for signs in product([-1,1], repeat=9):
        pp=[p+signs[i]*eP[i] for i,p in enumerate(P)]
        rr=[t+signs[i+3]*er[i] for i,t in enumerate(r)]
        mm=[m+signs[i+6]*eM[i] for i,m in enumerate(M)]
        actual=inverse(pp,rr,mm)
        dz=max(abs(actual[key]-got[key]) for key in ['R','x','y'])
        dq=abs(actual['q']-got['q']);maximum=max(maximum,dz);maximumq=max(maximumq,dq)
        allok=allok and dz<=env['state_error'] and dq<=env['q_error']
    check('all_512_rational_error_corners',allok,corners=512,max_state_error=str(maximum),max_q_error=str(maximumq))
    exact=error_envelope(P,r,M,[0]*3,[0]*3,[0]*3)
    check('zero_error_exact',exact['certified'] and exact['state_error']==0 and exact['q_error']==0)
    broad=error_envelope(P,r,M,[1]*3,[1]*3,[1]*3)
    check('large_matrix_error_inconclusive',not broad['certified'] and broad['reason']=='matrix envelope inconclusive')
    turn=error_envelope(P,r,[R]*3,[0]*3,[0]*3,[0]*3)
    check('turning_envelope_inconclusive',not turn['certified'] and turn['reason']=='ratio may cross turning domain')
    negm=[R-p*(-x)/2-p*t*y/2 for p,t in zip(P,r)]
    negative=error_envelope(P,r,negm,[0]*3,[0]*3,[0]*3)
    check('negative_coupling_inconclusive',not negative['certified'])
    refused('negative_error_refused',lambda: error_envelope(P,r,M,[-1]*3,[0]*3,[0]*3))
    refused('nonfinite_error_refused',lambda: error_envelope(P,r,M,[0]*3,[float('nan')]*3,[0]*3))
    smallP=[sp.Rational(1,10**6),sp.Integer(1),sp.Integer(2)]
    sr=[sp.Integer(0),sp.Integer(1),sp.Integer(-1)]
    sm=[1-p/sp.Integer(20)-p*t/sp.Integer(10) for p,t in zip(smallP,sr)]
    witness=error_envelope(smallP,sr,sm,[sp.Rational(1,500000),0,0],[0]*3,[0]*3)
    check('coefficient_label_not_observable_chart',witness['certified'] and witness['reason']=='positive coefficients certified' and smallP[0]-sp.Rational(1,500000)<0)
    # Sharp matrix-error witness: Lhat^-1=[[2,-1,0],[1,-1,0],[-1,2,-1]].
    # Delta L has only column3=(d,-d,d), so delta y=4d/(1-4d).
    pp=[sp.Integer(2),sp.Integer(4),sp.Integer(6)];rr=[0,0,sp.Rational(1,3)]
    zz=[sp.Rational(9,10),sp.Rational(1,2),sp.Integer(1)]
    mm=[zz[0]-p*zz[1]/2-p*r*zz[2]/2 for p,r in zip(pp,rr)]
    dd=sp.Rational(1,100);ee=[2*dd/p for p in pp]
    bound=error_envelope(pp,rr,mm,[0]*3,ee,[0]*3)
    actual=inverse(pp,[r+sg*e for r,sg,e in zip(rr,[-1,1,-1],ee)],mm)
    actual_error=max(abs(actual[k]-v) for k,v in zip(['R','x','y'],zz))
    check('sharp_matrix_inverse_error',actual_error==sp.Rational(1,24) and actual_error==bound['state_error'])
    # Sharp ratio witness: inverse rows (1/3,1/3,1/3), (1,-2,1), (-1/2,2,-3/2).
    # Delta M=e(1,-1,1) gives delta x=4e and delta y=-4e exactly.
    pp=[sp.Rational(-7,3),sp.Rational(2,3),sp.Rational(5,3)];rr=[sp.Rational(6,7),0,sp.Rational(6,5)]
    zz=[sp.Integer(1),sp.Rational(1,2),sp.Integer(1)]
    mm=[zz[0]-p*zz[1]/2-p*r*zz[2]/2 for p,r in zip(pp,rr)]
    bound=error_envelope(pp,rr,mm,[0]*3,[0]*3,[dd]*3)
    actual=inverse(pp,rr,[m+sg*dd for m,sg in zip(mm,[1,-1,1])])
    actual_error=abs(actual['q']-sp.Rational(1,2))
    check('sharp_ratio_error',actual_error==sp.Rational(1,16) and actual_error==bound['q_error'])
    return rows
