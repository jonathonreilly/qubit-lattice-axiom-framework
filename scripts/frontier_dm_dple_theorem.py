"""DPLE conditional math diagnostics; no physical selector or audit promotion.

W minima require p!=0, p'=0 and p''/p>0. Exact regressions check the
former classification errors. Random pencils and supplied decimal basin fixtures
are numerical diagnostics, not a proof of the quantified bound.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

PASS = FAIL = 0


def check(label, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")


def p_at(coeffs, t):
    return np.polynomial.polynomial.polyval(t, coeffs)


def char_poly_coeffs(H0, H1, d):
    """Floating interpolation of degree <=d; not an exact certificate."""
    ts = np.linspace(-1, 1, d+1)
    vals = [np.linalg.det(H0+t*H1).real for t in ts]
    return np.polynomial.polynomial.polyfit(ts, vals, d)


def critical_points(coeffs, interval=(0., 1.), tol=1e-9):
    """Numerical classifier with explicit singular/degenerate rejection.

    Small residuals/curvatures are unresolved, not classified Morse minima.
    Exact fixtures below independently cover signs, poles and degree drops.
    """
    c = np.asarray(coeffs, dtype=float)
    scale = max(1., float(np.max(np.abs(c))))
    c = np.polynomial.polynomial.polytrim(c, tol*scale)
    if len(c) <= 1:
        return []
    dp = np.polynomial.polynomial.polyder(c)
    ddp = np.polynomial.polynomial.polyder(dp)
    result = []
    for z in np.polynomial.polynomial.polyroots(dp):
        if abs(z.imag) > tol or not interval[0]+tol < z.real < interval[1]-tol:
            continue
        t = float(z.real)
        p = float(p_at(c,t))
        if abs(p) <= tol*scale:
            continue
        pdd = float(p_at(ddp,t))
        if abs(pdd) <= tol*scale:
            continue
        result.append((t,p,pdd,pdd/p))
    return sorted(result)


def interior_morse_idx0(coeffs, interval=(0.,1.), tol=1e-9):
    """Minima of log|p|, not minima of p (corrected legacy API)."""
    roots = [t for t,p,pdd,wdd in critical_points(coeffs,interval,tol) if wdd>0]
    return len(roots), roots


def positive_polynomial_minima(coeffs):
    return [t for t,p,pdd,wdd in critical_points(coeffs) if p>0 and pdd>0]


def exact_regressions():
    t = sp.symbols('t', real=True)
    x = t-sp.Rational(1,2)
    B = sp.Matrix([[x,1],[1,-x]])
    p = sp.expand(B.det())
    check('d=2 Hermitian witness determinant', p == -x**2-1 or sp.expand(p+x**2+1)==0)
    check('negative p maximum is W minimum', p.subs(t,sp.Rational(1,2))==-1 and sp.diff(p,t,2)==-2)
    Wdd = sp.diff(p,t,2)/p-(sp.diff(p,t)/p)**2
    check('exact log curvature is +2', Wdd.subs(t,sp.Rational(1,2))==2)
    check('numeric classifier sees nonvacuous d=2 W minimum', interior_morse_idx0([-1.25,1,-1])[0]==1)
    check('p minimum on negative sheet is W maximum', interior_morse_idx0([-.75,-1,1])[0]==0 and len(critical_points([-.75,-1,1]))==1)
    check('singular stationary point excluded', critical_points([.25,-1,1])==[])
    check('constant pencil has no Morse minima', critical_points([1,0,0,0])==[])
    check('quadratic degree drop in cubic container', interior_morse_idx0([-1.25,1,-1,0])[0]==1)
    # Two exact nondegenerate W minima on a positive quartic determinant.
    def block(a):
        return sp.Matrix([[t-a,sp.Rational(1,8)],[sp.Rational(1,8),a-t]])
    H4 = sp.diag(block(sp.Rational(1,4)),block(sp.Rational(3,4)))
    p4 = sp.expand(H4.det())
    check('d=4 determinant factorization', sp.expand(p4-(x**4-sp.Rational(3,32)*x**2+sp.Rational(25,4096)))==0)
    for root in [sp.Rational(1,2)-sp.sqrt(3)/8,sp.Rational(1,2)+sp.sqrt(3)/8]:
        check('d=4 exact W minimum '+str(root), sp.simplify(sp.diff(p4,t).subs(t,root))==0 and sp.simplify(p4.subs(t,root))>0 and sp.simplify(sp.diff(p4,t,2).subs(t,root))>0)
    # Odd-dimensional sign flip preserves all log derivatives.
    Hp = sp.diag(-1,B); pp = sp.expand(Hp.det()); pn=sp.expand((-Hp).det())
    check('opposite determinant pencils have identical logarithmic derivative', sp.simplify(sp.diff(pp,t)/pp-sp.diff(pn,t)/pn)==0 and sp.expand(pp+pn)==0)
    check('same sign is not same inertia', sp.det(sp.eye(3))==sp.det(sp.diag(1,-1,-1)) and sp.eye(3)!=sp.diag(1,-1,-1))
    # Positive local minimum and positive baseline do not certify whole path.
    pc = (sp.Rational(9,10)-t)*((t-sp.Rational(3,10))**2+sp.Rational(1,100))
    root = sp.Rational(1,2)-sp.sqrt(33)/30
    check('positive baseline/minimum can precede a singularity', pc.subs(t,0)>0 and sp.simplify(pc.subs(t,root))>0 and sp.simplify(sp.diff(pc,t).subs(t,root))==0 and sp.simplify(sp.diff(pc,t,2).subs(t,root))>0 and pc.subs(t,sp.Rational(9,10))==0)
    # The plus discriminant branch is a p minimum for either leading sign.
    for sign in [-1,1]:
        poly=sign*(t**3-sp.Rational(3,2)*t**2+sp.Rational(3,5)*t)+2
        c=list(reversed(sp.Poly(poly,t).all_coeffs()))
        D=c[2]**2-3*c[1]*c[3]
        tp=(-c[2]+sp.sqrt(D))/(3*c[3])
        tm=(-c[2]-sp.sqrt(D))/(3*c[3])
        check('cubic plus branch curvature, c3='+str(sign), sp.simplify(sp.diff(poly,t,2).subs(t,tp)-2*sp.sqrt(D))==0 and bool(tp<tm)==(sign<0))


def finite_diagnostics():
    rng=np.random.default_rng(20260419)
    for d in [2,3,4,5]:
        largest=0
        residual=0.
        for _ in range(100):
            A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); H0=(A+A.conj().T)/2
            A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); H1=(A+A.conj().T)/2
            c=char_poly_coeffs(H0,H1,d)
            largest=max(largest,interior_morse_idx0(c)[0])
            for t in [.137,.619]:
                det=np.linalg.det(H0+t*H1).real
                residual=max(residual,abs(p_at(c,t)-det)/(1+abs(det)))
        check(f'finite d={d} W count diagnostic',largest<=d//2,f'max={largest}; not proof')
        check(f'finite d={d} interpolation holdout',residual<1e-8,f'residual={residual:.3e}')


def basin_diagnostics():
    E1=math.sqrt(8/3); E2=math.sqrt(8)/3
    H0=np.array([[0,E1,-E1-.5j],[E1,0,-E2],[-E1+.5j,-E2,0]])
    M=np.array([[1,0,0],[0,0,1],[0,1,0]])
    D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]])
    Q=np.array([[0,1,1],[1,0,1],[1,1,0]])
    basins={'1':(.657061,.933806,.715042),'N':(.501997,.853543,.425916),'P':(1.037883,1.433019,-1.329548),'X':(21.128264,12.680028,2.089235)}
    for name,(m,delta,q) in basins.items():
        H1=m*M+delta*D+q*Q
        c=char_poly_coeffs(H0,H1,3)
        roots=critical_points(c)
        positive=positive_polynomial_minima(c)
        disc=c[2]**2-3*c[1]*c[3]
        formula=False
        if disc>0 and abs(c[3])>1e-9:
            t=(-c[2]+math.sqrt(disc))/(3*c[3])
            formula=0<t<1 and p_at(c,t)>0
        print(f'INFO supplied decimal basin {name}: coefficients={c.tolist()}, (t,p,pdd,Wdd)={roots}, positive-F4={bool(positive)}')
        check('cubic formula agrees with root classifier for basin '+name,formula==bool(positive))
        for t,p,pdd,wdd in roots:
            H=H0+t*H1
            A=np.linalg.solve(H,H1)
            direct=-np.trace(A@A).real
            check('Jacobi matrix curvature independently matches at basin '+name,np.isclose(direct,wdd,rtol=1e-7,atol=1e-7),f'matrix={direct}, polynomial={wdd}')


def main():
    exact_regressions()
    finite_diagnostics()
    basin_diagnostics()
    print('per_element: explicit finite matrix determinants and derivative coefficients were checked.')
    print('per_site: checked and not executed — no physical lattice-site dynamics is defined here.')
    print('per_mode: nonsingular nondegenerate critical points are classified by pdd/p, with exact controls.')
    print('per_block: exact dimensions 2, 3, 4 and sampled dimensions 2 through 5 were exercised.')
    print('lattice_wide: checked and not executed — no volume limit or physical source selection was tested.')
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
    print('Scope: conditional finite-pencil mathematics; no physical dimension, sheet, endpoint or audit status selected.')
    return int(FAIL>0)


if __name__=='__main__':
    raise SystemExit(main())
