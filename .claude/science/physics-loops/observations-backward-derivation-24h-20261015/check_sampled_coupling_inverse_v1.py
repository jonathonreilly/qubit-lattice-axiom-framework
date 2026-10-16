#!/usr/bin/env python3
"""Exact algebra and synthetic controls for the sampled clamped-pulse inverse."""
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
CHECKS = []
DELTA = 0.35
TAU = 1.7


def check(name, passed, **details):
    CHECKS.append(dict(name=name, passed=bool(passed), **details))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def symbolic():
    s, p, z = sp.symbols('s p z', nonzero=True)
    F0, F1, F2 = sp.symbols('F0 F1 F2')
    F3 = (1+s)*F2-(s+p)*F1+p*F0
    check('affine characteristic polynomial yields recurrence',
          sp.expand((z-1)*(z*z-s*z+p)) == z**3-(1+s)*z*z+(s+p)*z-p)
    check('differences obey homogeneous second-order recurrence',
          sp.expand((F3-F2)-s*(F2-F1)+p*(F1-F0)) == 0)
    d0, d1 = sp.symbols('d0 d1')
    d2, d3 = s*d1-p*d0, s*(s*d1-p*d0)-p*d1
    H = d0*d2-d1*d1
    check('Cramer inverse recovers both recurrence coefficients',
          sp.factor((d0*d3-d1*d2)/H-s) == 0 and
          sp.factor((d1*d3-d2*d2)/H-p) == 0)
    fm2, fm1, f0, f2, f3, f4 = sp.symbols('fm2 fm1 f0 f2 f3 f4')
    D = (f4-(1+s)*f3+(s+p)*f2)/p-((1+s)*f0-(s+p)*fm1+p*fm2)
    check('coefficient sensitivity formulas are exact',
          sp.simplify(sp.diff(D,s)-((f2-f3)/p-f0+fm1)) == 0 and
          sp.simplify(sp.diff(D,p)-(-(f4-(1+s)*f3)/p**2+fm1-fm2)) == 0)
    t, gamma, om2 = sp.symbols('t gamma om2', positive=True)
    Z = sp.Function('Z')(t)
    energy_rate = sp.diff((sp.diff(Z,t)**2+om2*Z**2)/2,t)
    check('passive step-response energy has nonpositive derivative',
          sp.simplify(energy_rate.subs(sp.diff(Z,t,2),-gamma*sp.diff(Z,t)-om2*Z))
          == -gamma*sp.diff(Z,t)**2)


def afun(x):
    return 1.5*(1+x*x)


def bfun(x):
    return x+x**3/3


def ufun(x):
    return x+0.2*x**3


def advance(state, dt, q, om2, gamma):
    M = np.array([[0.,1.,0.],[-om2,-gamma,-bfun(q)/TAU],[0.,0.,0.]])
    return (expm(M*dt)@np.array([*state,1.]))[:2]


def force(state, x):
    return ufun(x)+afun(x)*state[0]


def exact_sp(om2, gamma, dt=DELTA):
    T = expm(np.array([[0.,1.],[-om2,-gamma]])*dt)
    return np.array([np.trace(T), np.exp(-gamma*dt)])


def calibration(om2, gamma, start, x=0.3, count=9):
    return np.array([force(advance(start,n*DELTA,x,om2,gamma),x)
                     for n in range(count)])


def infer(samples):
    d = np.diff(samples[:5])
    X = np.array([[d[1],-d[0]],[d[2],-d[1]]])
    y = d[2:4]
    return np.linalg.solve(X,y), X, y


def weights(s,p):
    return np.array([-p,s+p,-(1+s),(s+p)/p,-(1+s)/p,1/p])


def pulse(x,y,start,om2,gamma):
    before = [advance(start,n*DELTA,x,om2,gamma) for n in range(3)]
    end = advance(before[-1],DELTA,y,om2,gamma)
    after = [advance(end,n*DELTA,x,om2,gamma) for n in (1,2,3)]
    samples = np.array([force(st,x) for st in before+after])
    reference = advance(before[-1],DELTA,x,om2,gamma)
    direct = force(end,x)-force(reference,x)
    return samples, direct


def green(t,om2,gamma):
    # Normalized impulse, independently integrated for the pulse identity.
    return expm(np.array([[0.,1.],[-om2,-gamma]])*t)[0,1]


def jend(om2,gamma):
    return quad(lambda t:green(t,om2,gamma),0,DELTA,epsabs=1e-12)[0]


def numerical():
    rng = np.random.default_rng(26101617)
    cases = [(4.,0.),(4.,0.7),(4.,4.),(4.,5.)]
    for om2,gamma in cases:
        tag = f'omega2={om2},gamma={gamma}'
        cal = calibration(om2,gamma,np.array([1.3,-0.8]))
        est,X,_ = infer(cal)
        actual = exact_sp(om2,gamma)
        residuals = [cal[n+3]-(1+est[0])*cal[n+2]+sum(est)*cal[n+1]-est[1]*cal[n]
                     for n in range(len(cal)-3)]
        check('calibration and reserved recurrence '+tag,
              np.max(abs(est-actual))<1e-10 and max(abs(np.array(residuals)))<1e-11,
              inferred=est.tolist(),actual=actual.tolist(),condition=float(np.linalg.cond(X)),
              held_sequence_max_error=float(max(abs(np.array(residuals)))))
        j = jend(om2,gamma)
        errors=[]; law_errors=[]
        grid = np.array([0.,0.25,0.5,0.75,1.])
        D=np.empty((len(grid),len(grid)))
        for i,x in enumerate(grid):
            for k,y in enumerate(grid):
                samples,direct = pulse(x,y,rng.normal(size=2)*3,om2,gamma)
                inferred = float(weights(*est)@samples)
                D[i,k]=inferred
                errors.append(abs(inferred-direct))
                law_errors.append(abs(inferred+afun(x)*(bfun(y)-bfun(x))*j/TAU))
        check('six settled samples recover pulse end '+tag,
              max(errors)<1e-10 and max(law_errors)<1e-10,
              max_extrapolation_error=float(max(errors)),max_green_error=float(max(law_errors)),
              unrelated_preparations=25)
        E=D-D[:,[0]]; e0=E[0,-1]
        A=E[:,-1]/e0; B=E[0,:]/e0
        check('relative shapes and positive interaction sign '+tag,
              max(abs(A-(1+grid**2)))<1e-9 and
              max(abs(B-(grid+grid**3/3)/(4/3)))<1e-9 and j>0 and e0*0.75<0,
              anchor=float(e0),step_integral=j)
        # Additional pairs were not in the grid; known synthetic shapes are used,
        # not a claim that finite grid values determine a continuum function.
        reserved_errors=[]
        for x,y in [(-.2,.9),(.1,1.2),(.37,.82),(.83,-.1)]:
            samples,_=pulse(x,y,rng.normal(size=2)*5,om2,gamma)
            predicted=e0*(1+x*x)*(bfun(y)-bfun(x))/(4/3)
            reserved_errors.append(abs(float(weights(*est)@samples)-predicted))
        check('reserved synthetic pairs '+tag,max(reserved_errors)<1e-9,
              maximum=float(max(reserved_errors)),independent_empirical_test=False)

    # Coefficients can be inferred from rows in different histories.
    records=[calibration(4.,.7,np.array(st)) for st in ([1.,0.],[-.4,1.7])]
    ds=[np.diff(f) for f in records]
    X=np.array([[d[1],-d[0]] for d in ds]); y=np.array([d[2] for d in ds])
    check('pooled unrelated calibration histories identify common recurrence',
          np.max(abs(np.linalg.solve(X,y)-exact_sp(4.,.7)))<1e-11,
          determinant=float(np.linalg.det(X)))
    steady=np.ones(5)*.2; d=np.diff(steady)
    X0=np.array([[d[1],-d[0]],[d[2],-d[1]]])
    check('steady calibration is explicitly inconclusive',np.linalg.matrix_rank(X0)==0,
          scientific_outcome='not identifiable; no model falsification')

    # Aliased continuous underdamped modes have identical sampled maps' traces
    # and determinants, but different hidden frequencies and step magnitudes.
    gamma=.7; wd=2.; wd_alias=wd+2*np.pi/DELTA
    aliases=[wd*wd+gamma*gamma/4,wd_alias*wd_alias+gamma*gamma/4]
    coefs=[exact_sp(o,gamma) for o in aliases]
    check('continuous frequency aliases share discrete recurrence',
          np.max(abs(coefs[0]-coefs[1]))<1e-12 and aliases[1]/aliases[0]>50,
          omega2=aliases,coefficients=[v.tolist() for v in coefs])
    normalized=[]; js=[]
    for om2 in aliases:
        j=jend(om2,gamma); js.append(j)
        values=[]
        for x,y in [(0.,0.),(0.,1.),(.6,0.),(.6,1.)]:
            samples,_=pulse(x,y,rng.normal(size=2),om2,gamma)
            values.append(float(weights(*coefs[0])@samples))
        anchor=values[1]-values[0]
        normalized.append((values[3]-values[2])/anchor)
    check('aliased dynamics retain normalized coupling and pulse-end sign',
          max(abs(np.array(normalized)-1.36))<1e-8 and min(js)>0 and
          abs(js[0]-js[1])>.01,normalized=normalized,step_integrals=js)
    zero_om2=(2*np.pi/DELTA)**2
    check('full undamped period gives no nonzero response anchor',
          abs(jend(zero_om2,0.))<1e-12)
    late=quad(lambda u:green(2.-u,4.,0.),0,DELTA)[0]
    check('late response sign cannot replace extrapolated pulse-end sign',
          late<0 and jend(4.,0.)>0,late_integral=late)
    active_j=jend(zero_om2+.25,-1.)
    check('negative damping can break pulse-end positivity',active_j<0,
          excluded_active_integral=active_j)

    # Exact read-noise bound: align signs to saturate the six linear weights.
    s,p=exact_sp(4.,.7); samples,_=pulse(.3,.8,np.array([.4,-.9]),4.,.7)
    W=weights(s,p); eps=2e-7
    error=abs(W@(samples+eps*np.sign(W))-W@samples)
    bound=eps*np.sum(abs(W))
    check('six-sample error norm is sharp',abs(error-bound)<1e-13,
          error=float(error),bound=float(bound))
    smallp=np.exp(-40*DELTA)
    check('strong damping makes backward extrapolation ill-conditioned',
          1/smallp>1e6,p=float(smallp),minimum_post_gain=float(1/smallp))

    # Deterministic errors, all 32 force-error corners; no iid assumption.
    cal=calibration(4.,.7,np.array([1.3,-.8])); theta,X,y=infer(cal)
    ecal=1e-8; max_ratio=0.; max_theta=0.; max_bound=0.
    for signs in itertools.product([-1,1],repeat=5):
        noisy=cal[:5]+ecal*np.array(signs)
        that,Xhat,_=infer(noisy)
        norm=float(np.linalg.norm(np.linalg.inv(Xhat),np.inf)); eta=norm*4*ecal
        bnd=norm/(1-eta)*(2*ecal+4*ecal*np.linalg.norm(that,np.inf))
        err=float(np.linalg.norm(theta-that,np.inf))
        max_ratio=max(max_ratio,err/bnd);max_theta=max(max_theta,err);max_bound=max(max_bound,bnd)
    check('calibration perturbation bound covers all correlated sample corners',
          max_ratio<=1+1e-12,max_error=max_theta,max_bound=max_bound,max_fraction=max_ratio)
    e_theta=2e-4; max_fraction=0.
    for signs in itertools.product([-1,1],repeat=2):
        estimate=theta+e_theta*np.array(signs)
        pmin=min(theta[1],estimate[1]); S=max(abs(theta[0]),abs(estimate[0]))
        M=max(abs(samples)); bnd=M*e_theta*(2/pmin+4+(2+S)/pmin**2)
        err=abs(weights(*estimate)@samples-weights(*theta)@samples)
        max_fraction=max(max_fraction,err/bnd)
    check('coefficient propagation bound covers all perturbation corners',
          max_fraction<=1+1e-12,max_fraction=float(max_fraction))
    # A genuine second independent mode generally violates the learned recurrence.
    mixture=cal+.15*np.exp(-.11*np.arange(len(cal))*DELTA)*np.sin(3.1*np.arange(len(cal))*DELTA)
    fitted,_,_=infer(mixture)
    res=[mixture[n+3]-(1+fitted[0])*mixture[n+2]+sum(fitted)*mixture[n+1]-fitted[1]*mixture[n]
         for n in range(2,len(mixture)-3)]
    check('unmodeled second mode is exposed by reserved recurrence samples',
          max(abs(np.array(res)))>1e-4,reserved_residual=float(max(abs(np.array(res)))))


def main():
    symbolic(); numerical()
    out=dict(status='conditional-support',claim_type='bounded_theorem',
             evidence='exact identities and synthetic controls; no empirical validation',
             source_hashes={n:sha(HERE/n) for n in
                 ['SAMPLED_COUPLING_INVERSE_v1.md',Path(__file__).name,
                  'COUPLING_RECONSTRUCTION_v2.md']},
             versions=dict(python=sys.version.split()[0],numpy=np.__version__,
                           scipy=scipy.__version__,sympy=sp.__version__),
             checks=CHECKS,total=dict(passed=sum(r['passed'] for r in CHECKS),
                                     failed=sum(not r['passed'] for r in CHECKS)),
             unresolved=['physical source/coordinate bridge','single hidden passive response class',
                         'measurement and pulse-model error budgets','continuous coupling coverage',
                         'absolute scale and moving-coordinate kinetic action'])
    print(json.dumps(out,indent=2))
    return int(out['total']['failed']>0)


if __name__ == '__main__':
    raise SystemExit(main())
