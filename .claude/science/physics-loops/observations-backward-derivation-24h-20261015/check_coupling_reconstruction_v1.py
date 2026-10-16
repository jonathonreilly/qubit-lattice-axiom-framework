#!/usr/bin/env python3
"""Exact identities and synthetic, separately implemented clamped-pulse controls."""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sys

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
import sympy as sp


HERE = Path(__file__).resolve().parent
CHECKS: list[dict] = []


def check(name, passed, **evidence):
    CHECKS.append(dict(name=name, passed=bool(passed), **evidence))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def symbolic_controls():
    q, w = sp.symbols('q w', real=True)
    tau, C, gamma, lam = sp.symbols('tau C gamma lam', positive=True)
    u, a, b = [sp.Function(n)(q) for n in ('u', 'a', 'b')]
    wp, wpp = sp.symbols('wp wpp')
    F = u + a*w
    residual = a*wpp + gamma/tau*a*wp + C/tau*F
    residual = sp.expand(residual.subs(wpp, (-gamma*wp-C*w-b)/tau))
    check('constant-clamp force obeys affine oscillator equation',
          sp.simplify(residual-(C*u-a*b)/tau) == 0)

    ax, ar, bx, by, bz, d, J = sp.symbols('ax ar bx by bz d J', nonzero=True)
    Dxy = -J*ax*(by-bx)/tau
    Dxz = -J*ax*(bz-bx)/tau
    E = sp.factor(Dxy-Dxz)
    check('column subtraction removes row-specific forcing offset',
          sp.simplify(E+J*ax*(by-bz)/tau) == 0)
    aa, ab, bc, bd = sp.symbols('aa ab bc bd')
    mat = sp.Matrix([[aa*bc, aa*bd], [ab*bc, ab*bd]])
    check('centered pulse response has exact rank-one minors', mat.det() == 0)
    kap = ar/(lam*d)
    E0 = -J*ar*d/tau
    check('interaction multiplier sign follows measured anchor and shape',
          sp.simplify(E0*kap+J*ar**2/(tau*lam)) == 0)

    U = sp.Function('U')(q)
    V = U+lam*C*w*w/2+lam*b*w
    check('potential completion has both prescribed cross forces',
          sp.diff(V,q) == sp.diff(U,q)+lam*sp.diff(b,q)*w and
          sp.diff(V,w) == lam*C*w+lam*b)
    check('mixed derivatives require reciprocity rather than rank one',
          sp.simplify(sp.diff(u+a*w,w)-sp.diff(lam*C*w+lam*b,q))
          == a-lam*sp.diff(b,q))

    bbad = q+q**3/3
    abad = 1+q
    ratio_derivative = sp.factor(sp.diff(abad/sp.diff(bbad,q),q))
    check('explicit rank-one nonreciprocal control has nonconstant ratio',
          ratio_derivative != 0 and ratio_derivative.subs(q,0) == 1,
          ratio_derivative=str(ratio_derivative))

    Ap = 1+q*q
    Bp = (q+q**3/3)/sp.Rational(4,3)
    kappa = sp.Rational(3,4)
    check('integral shape law fixes constant from normalized anchor',
          sp.simplify(sp.diff(Bp,q)-kappa*Ap) == 0 and
          sp.simplify(kappa*sp.integrate(Ap,(q,0,1))) == 1)

    # Two response directions can yield a rank-two centered surface.
    M = sp.Matrix([[1,2],[2,5]])
    check('two-channel control violates rank-one signature', M.det() == 1,
          determinant=str(M.det()))


TAU = 1.7
OMEGA2 = 4.0
GAMMA = 0.4
C = TAU*OMEGA2
LAMBDA = 1.5
H = 0.12
PRE = np.array([-0.5,-0.25,0.0])
POST = 0.45
T = np.array([[0.,1.,0.],[-OMEGA2,-GAMMA,1.],[0.,0.,0.]])
EH = np.array([1.,0.,0.])
O = np.vstack([EH@expm(T*t) for t in PRE])
OI = np.linalg.inv(O)


def bfun(q):
    return q+q**3/3


def afun(q):
    return LAMBDA*(1+q*q)


def ufun(q):
    # Selected stable synthetic potential; not fitted observational physics.
    return q+0.3*q**3+LAMBDA/C*bfun(q)*(1+q*q)


def advance(state, dt, drive, omega2=OMEGA2, gamma=GAMMA):
    # Forward simulation of the hidden state, not equation (5).
    M = np.array([[0.,1.,0.],[-omega2,-gamma,-drive/TAU],[0.,0.,0.]])
    return (expm(M*dt)@np.array([*state,1.]))[:2]


def pulse(x, y, start, post=POST, a=afun, b=bfun):
    pre_states = [advance(start,t-PRE[0],b(x)) for t in PRE]
    pre_f = np.array([ufun(x)+a(x)*s[0] for s in pre_states])
    during = advance(pre_states[-1],H,b(y))
    after = advance(during,post-H,b(x))
    force = ufun(x)+a(x)*after[0]
    weights = EH@expm(T*post)@OI
    prediction = weights@pre_f
    return float(force-prediction), pre_f, float(force), weights


def green(t):
    omega = np.sqrt(OMEGA2-GAMMA**2/4)
    return np.exp(-GAMMA*t/2)*np.sin(omega*t)/omega


def pulse_j(t):
    return quad(lambda s: green(t-s),0,H,epsabs=1e-13,epsrel=1e-13)[0]


def sampled_matrix(grid, rng, a=afun, post=POST):
    out = np.empty((len(grid),len(grid)))
    for i,x in enumerate(grid):
        for j,y in enumerate(grid):
            out[i,j] = pulse(x,y,rng.normal(size=2)*3,post=post,a=a)[0]
    return out


def numerical_controls():
    rng = np.random.default_rng(261016)
    grid = np.linspace(0.,1.,5)
    j = pulse_j(POST)
    D = sampled_matrix(grid,rng)
    oracle = np.array([[-afun(x)*(bfun(y)-bfun(x))*j/TAU for y in grid]
                       for x in grid])
    err = float(np.max(np.abs(D-oracle)))
    check('forward hidden dynamics and same-run baseline recover pulse law',
          err < 1e-11, max_error=err, distinct_preparations=25)
    check('null pulses cancel with unrelated run preparations',
          np.max(np.abs(np.diag(D))) < 1e-11)
    check('baseline sampling is observable and conditioned',
          np.linalg.matrix_rank(O) == 3 and np.linalg.cond(O) < 1000,
          condition=float(np.linalg.cond(O)))

    E = D-D[:,[0]]
    e0 = E[0,-1]
    A = E[:,-1]/e0
    B = E[0,:]/e0
    ferror = float(np.max(np.abs(E-e0*np.outer(A,B))))
    check('observed centered factorization reconstructs both relative shapes',
          ferror < 1e-11 and np.max(abs(A-(1+grid**2))) < 1e-10 and
          np.max(abs(B-(grid+grid**3/3)/(4/3))) < 1e-10,
          factorization_error=ferror, anchor=float(e0))
    check('early-lag kernel is positive and reciprocal energy sign is positive',
          j > 0 and e0*0.75 < 0, pulse_integral=j)

    # This polynomial-degree restriction is chosen for a synthetic demonstration.
    # It is not a derivation of the continuum coupling from finite samples.
    ap = np.polynomial.Polynomial.fit(grid,A,2).convert()
    bp = np.polynomial.Polynomial.fit(grid,B,3).convert()
    kappa = 1/(ap.integ()(1)-ap.integ()(0))
    residual = np.max(abs(bp.deriv()(grid)-kappa*ap(grid)))
    check('selected synthetic polynomial reconstruction satisfies integral law',
          residual < 1e-9, kappa=float(kappa), derivative_residual=float(residual),
          selected_degrees=dict(A=2,B=3))

    held = [(-0.2,0.9),(0.1,1.2),(0.37,0.82),(0.83,-0.1)]
    errors=[]
    for x,y in held:
        actual = pulse(x,y,rng.normal(size=2)*9)[0]
        predicted = e0*ap(x)*(bp(y)-bp(x))
        errors.append(float(abs(actual-predicted)))
    check('frozen synthetic shape predicts additional histories and preparations',
          max(errors) < 1e-10, held_out_synthetic_errors=errors,
          empirical_independent_test=False)

    at_later = sampled_matrix(grid,rng,post=0.7)
    collapse = float(np.max(abs(at_later/pulse_j(0.7)-D/j)))
    check('independently prepared later windows obey same temporal collapse',
          collapse < 1e-9, max_error=collapse)

    _, pre, force, weights = pulse(0.4,0.8,np.array([1.3,-0.8]))
    eps=2e-6
    noisy = (force+eps)-weights@(pre-eps*np.sign(weights))
    exact = force-weights@pre
    bound = eps*(1+np.linalg.norm(weights,1))
    actual_error=float(abs(noisy-exact))
    check('force-error amplification bound is attained by aligned errors',
          abs(actual_error-bound)<1e-13, actual_error=actual_error,bound=float(bound))

    # Aliasing is excluded by the observation contract, not cured by inversion.
    T0=np.array([[0.,1.,0.],[-4.,0.,1.],[0.,0.,0.]])
    O0=np.vstack([EH@expm(T0*t) for t in [-np.pi,-np.pi/2,0.]])
    check('aliased undamped sample times are not observable',
          np.linalg.matrix_rank(O0,tol=1e-12)<3)

    Dbad=sampled_matrix(grid,rng,a=lambda x:1+x)
    Ebad=Dbad-Dbad[:,[0]]
    A_bad=Ebad[:,-1]/Ebad[0,-1]
    B_bad=Ebad[0,:]/Ebad[0,-1]
    ab=np.polynomial.Polynomial.fit(grid,A_bad,2).convert()
    bb=np.polynomial.Polynomial.fit(grid,B_bad,3).convert()
    kb=1/(ab.integ()(1)-ab.integ()(0))
    bad_res=float(np.max(abs(bb.deriv()(grid)-kb*ab(grid))))
    check('nonreciprocal force passes rank one but fails common-potential shape',
          np.max(abs(Ebad-Ebad[0,-1]*np.outer(A_bad,B_bad)))<1e-11 and
          bad_res>0.05, shape_residual=bad_res)

    Dneg=sampled_matrix(grid,rng,a=lambda x:-afun(x))
    Eneg=Dneg-Dneg[:,[0]]
    check('negative interaction multiplier fails positive-energy sign',
          Eneg[0,-1]*0.75 > 0)

    # Common gain cancels; row-dependent gains are a live measurement import.
    gained=7.3*E
    check('common positive force gain cancels from both reconstructed shapes',
          np.max(abs(gained[:,-1]/gained[0,-1]-A))<1e-13 and
          np.max(abs(gained[0,:]/gained[0,-1]-B))<1e-13)
    row_gain=(1+0.4*grid)[:,None]*E
    changed_A=row_gain[:,-1]/row_gain[0,-1]
    check('setting-dependent gain changes inferred feedback shape',
          np.max(abs(changed_A-A))>0.3)

    ratios_ok=True
    max_ratio_error=0.0
    for dn,de in itertools.product([-0.03,0.03],[-0.02,0.02]):
        nh,eh=0.7,-0.4
        rh=nh/eh
        true=(nh-dn)/(eh-de)
        rb=(0.03+abs(rh)*0.02)/(abs(eh)-0.02)
        ratios_ok &= abs(true-rh)<=rb+1e-14
        max_ratio_error=max(max_ratio_error,abs(true-rh))
    check('ratio error bound covers all error corners',ratios_ok,
          max_error=max_ratio_error)

    x,y,edge=0.2,0.9,0.02
    def actual_q(s):
        if s<edge:return x+(y-x)*(1-np.cos(np.pi*s/edge))/2
        if s>H-edge:return x+(y-x)*(1-np.cos(np.pi*(H-s)/edge))/2
        return y
    force_error=abs(afun(x)/TAU*quad(
        lambda s:green(POST-s)*(bfun(actual_q(s))-bfun(y)),0,H,
        points=[edge,H-edge],epsabs=1e-13)[0])
    Lb=1+max(x*x,y*y)
    edge_bound=abs(afun(x))/TAU*POST*Lb*abs(y-x)*2*edge
    check('rounded pulse respects stated transition error bound',
          force_error <= edge_bound, force_error=float(force_error),bound=float(edge_bound))


def main():
    symbolic_controls()
    numerical_controls()
    result=dict(
        status='conditional-support',claim_type='bounded_theorem',
        evidence='exact identities and synthetic controls; no measured dataset',
        source_hashes={
            'COUPLING_RECONSTRUCTION_v1.md':sha(HERE/'COUPLING_RECONSTRUCTION_v1.md'),
            Path(__file__).name:sha(Path(__file__))},
        versions=dict(python=sys.version.split()[0],numpy=np.__version__,
                      scipy=scipy.__version__,sympy=sp.__version__),
        checks=CHECKS,
        total=dict(passed=sum(x['passed'] for x in CHECKS),
                   failed=sum(not x['passed'] for x in CHECKS)),
        open_conditions=['physical calibrated coordinate/source/time',
                         'shared hidden linear response and coefficients',
                         'pole uncertainty, drift and pulse error bounds',
                         'continuum coupling inference beyond finite samples',
                         'moving-coordinate inertia and global stability'])
    print(json.dumps(result,indent=2))
    return int(result['total']['failed'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
