#!/usr/local/bin/python3
"""Original-author development controls; no observations, fits, or audit verdicts."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spherical_jn
from numpy.polynomial.legendre import leggauss

HERE = Path(__file__).resolve().parent
CHECKS = []


def check(name, condition, **evidence):
    CHECKS.append({"name": name, "passed": bool(condition), **evidence})
    if not condition:
        raise AssertionError(name + ": " + repr(evidence))


def low_bound(k, mu, C, W, T, beta):
    omega = np.hypot(k, mu)
    delta = mu * mu / (omega + k)
    dv = delta / omega
    theta = np.minimum(2.0, T * delta)
    return C * (dv / k + theta / omega) + W * (dv + (1 + beta) * theta)


def closed_low(mu, K, C, W, T, beta):
    assert K >= mu > 0
    Z = C * T + W * (1 + (1 + beta) * mu * T)
    A, D, J = C / 2, (C * T + W) / 2, W * (1 + beta) * T / 2
    lo = C*C*mu + C*Z*mu*mu + Z*Z*mu**3/3
    hi = (A*A*(mu - mu**4/K**3)/3
          + A*D*(mu**2 - mu**4/K**2)
          + (D*D+2*A*J)*(mu**3 - mu**4/K)
          + 2*D*J*mu**4*math.log(K/mu)
          + J*J*mu**4*(K-mu))
    return lo + hi


def epsilon(mu, C, W, T, beta, V):
    if mu == 0:
        return 0.0, None
    J = W * (1 + beta) * T / 2
    K = max(mu, 2*V/(mu*mu*J)) if J > 0 else max(mu, 1/mu)
    return math.sqrt((closed_low(mu, K, C, W, T, beta)+4*V*V/K)/(2*np.pi**2)), K


def variation_supplier(beta, accel, jerk, C, W, W1, Tc, T1):
    d = 1-beta
    Q0, Q1 = 1+beta, 1+2*beta*(1+beta)
    B0 = Q0/d
    B1 = Q1*accel/d+Q0*accel/d**2
    B2 = ((2+6*beta)*accel**2+Q1*jerk)/d
    B2 += (2*Q1*accel**2+Q0*jerk)/d**2+2*Q0*accel**2/d**3
    V = (Tc+B2*W+2*B1*W1+B0*T1)/d
    V += accel*(C+B1*W+B0*W1)/d**2
    return V, (B0, B1, B2)


def smooth_response(k, mu, z, beta=.18, shifted=False):
    """Original plane response and independent first-IBP representation."""
    nodes, wg = leggauss(192)
    s = (nodes+1)/2
    wg = wg/2
    u = beta*np.sin(np.pi*s)**2
    accel = beta*np.pi*np.sin(2*np.pi*s)
    x = beta*(s/2-np.sin(2*np.pi*s)/(4*np.pi))
    w = np.sin(np.pi*s)**2
    wp = np.pi*np.sin(2*np.pi*s)
    c = .3*np.sin(np.pi*s)**2
    if shifted:
        x = x+.7
        s = s+.3
    omega = math.hypot(k, mu)
    v = k/omega
    d = 1-v*z*u
    q = (1-u*u)*(v*z-u)
    qp = -2*u*accel*(v*z-u)-(1-u*u)*accel
    dp = -v*z*accel
    b = q/d
    bp = qp/d-q*dp/d**2
    phase = np.exp(1j*(omega*s-k*z*x))
    original = np.sum(wg*(c/omega+1j*q*w)*phase)
    ibp = np.sum(wg*(c-bp*w-b*wp)*phase)/omega
    return original, ibp


L = .6
ENDPOINTS = np.array([1.4, 2.4, 3.4])
BETAS = np.array([1., -2., 1.])


def coherent_original(k, mu, z):
    om = math.hypot(k, mu)
    v = k/om
    endpoint = np.sum(BETAS*np.exp(1j*om*ENDPOINTS))
    bracket = ((1+v*z)*np.exp(-2j*om*L)+(v*z-1)
               -2*v*z*np.exp(-1j*(om*L+k*L*z)))
    return -1j*endpoint*bracket/om**2


def coherent_weights(k, mu, z):
    """Integrate the count-derived piecewise weights, not the endpoint formula."""
    om = math.hypot(k, mu)
    v = k/om
    breaks = sorted(set(float(t-a) for a in [0., L, 2*L] for t in ENDPOINTS))
    gn, gw = leggauss(24)
    result = 0j
    for left, right in zip(breaks[:-1], breaks[1:]):
        s = left+(right-left)*(gn+1)/2
        wq = gw*(right-left)/2
        F = lambda a: np.sum(BETAS[:, None]*np.maximum(ENDPOINTS[:, None]-a-s, 0), axis=0)
        Fp = lambda a: -np.sum(BETAS[:, None]*(ENDPOINTS[:, None]-a-s > 0), axis=0)
        ws, wb = F(2*L)+F(0), -2*F(L)
        cs = -Fp(2*L)+Fp(0)
        result += np.sum(wq*((cs/om+1j*v*z*ws)*np.exp(1j*om*s)
                             +1j*v*z*wb*np.exp(1j*(om*s-k*z*L))))
    return result


def angular_expression(k, mu):
    k = np.asarray(k)
    om = np.hypot(k, mu)
    v = k/om
    a, b = om*L, k*L
    j0, j1 = spherical_jn(0, b), spherical_jn(1, b)
    j1_over_b = np.divide(j1, b, out=np.full_like(b, 1/3), where=b != 0)
    I1, I2 = 2*j1, 2*(j0-2*j1_over_b)
    return (8*np.sin(a)**2+8/3*v*v*(np.cos(a)**2+1)
            -8*v*v*np.cos(a)*I2-8*v*np.sin(a)*I1)


def massive_gram(mu, K=2000, order=24):
    nodes, weights = leggauss(order)
    cells = np.arange(K, dtype=float)[:, None]
    k = cells+(nodes+1)/2
    om = np.hypot(k, mu)
    radial = (k*k/om**4 * 16*np.sin(om/2)**4
              * angular_expression(k, mu)/(4*np.pi**2))
    g0 = np.sum(radial*weights[None, :]/2)
    g1 = np.sum(radial*np.cos(om)*weights[None, :]/2)
    return np.array([[g0, g1], [g1, g0]])


def run():
    rng = np.random.default_rng(20261015)
    # Fourier energy normalization: direct periodic real fields at one epoch.
    n = 64
    x = 2*np.pi*np.arange(n)/n
    modes = np.array([-5, -3, -1, 1, 3, 5])
    a = rng.normal(size=len(modes))+1j*rng.normal(size=len(modes))
    energy_errors = []
    for mu in [0, .4, 3]:
        om = np.hypot(modes, mu)
        phase = np.exp(-1j*modes[:, None]*x)
        h = 2*np.real(np.sum(a[:, None]*phase, axis=0))
        hdot = 2*np.real(np.sum((1j*om*a)[:, None]*phase, axis=0))
        hx = 2*np.real(np.sum((-1j*modes*a)[:, None]*phase, axis=0))
        direct = np.mean(hdot**2+hx**2+mu**2*h**2)
        expected = 4*np.sum(om**2*abs(a)**2)
        energy_errors.append(float(abs(direct-expected)/expected))
    check('real_energy_isometry', max(energy_errors) < 3e-14, relative_errors=energy_errors)

    # Quotient derivatives assembled independently from q,d and their derivatives.
    worst = np.zeros(3)
    for _ in range(1000):
        beta, accelmax, jerkmax = .7, 1.2, 2.1
        u = rng.normal(size=3); u *= rng.uniform(0,beta)/np.linalg.norm(u)
        acc = rng.normal(size=3); acc *= rng.uniform(0,accelmax)/np.linalg.norm(acc)
        jer = rng.normal(size=3); jer *= rng.uniform(0,jerkmax)/np.linalg.norm(jer)
        direction = rng.normal(size=3); direction /= np.linalg.norm(direction)
        v = rng.uniform(0,1)
        q = (1-u@u)*(v*direction-u)
        qp = -2*(u@acc)*(v*direction-u)-(1-u@u)*acc
        qpp = -2*(acc@acc+u@jer)*(v*direction-u)+4*(u@acc)*acc-(1-u@u)*jer
        d, dp, dpp = 1-v*(direction@u), -v*(direction@acc), -v*(direction@jer)
        b = q/d
        bp = qp/d-q*dp/d**2
        bpp = qpp/d-2*qp*dp/d**2-q*dpp/d**2+2*q*dp**2/d**3
        _, bounds = variation_supplier(beta,accelmax,jerkmax,1,1,1,1,1)
        worst = np.maximum(worst,[np.linalg.norm(y)/z for y,z in zip([b,bp,bpp],bounds)])
    check('quotient_derivative_supplier', bool(np.max(worst) <= 1), sampled_max_ratios=worst.tolist(), sampled_cases=1000)

    beta=.18
    V, _ = variation_supplier(beta,beta*np.pi,2*beta*np.pi**2,.15,.5,2,.6,4*np.pi)
    ibp_err, difference_ratio, high_ratio = 0., 0., 0.
    for mu in [0., .001, .2, 2.]:
        for k in [.01, .2, 1., 4., 12., 40.]:
            for z in [-1., -.3, .2, 1.]:
                vals = [smooth_response(k,mu,z,shifted=a) for a in [False,True]]
                fm = sum(x[0] for x in vals)
                ip = sum(x[1] for x in vals)
                f0 = sum(smooth_response(k,0,z,shifted=a)[0] for a in [False,True])
                ibp_err = max(ibp_err,abs(fm-ip))
                high_ratio = max(high_ratio,abs(fm)*math.hypot(k,mu)**2/(2*V))
                if mu:
                    bound = low_bound(k,mu,.3,1.,1.3,beta)
                    difference_ratio = max(difference_ratio,abs(fm-f0)/bound)
    check('accelerated_original_vs_ibp', ibp_err < 2e-12, maximum_error=float(ibp_err))
    check('accelerated_mass_difference_bound', difference_ratio <= 1+1e-8, maximum_ratio=float(difference_ratio))
    check('accelerated_high_frequency_bound', high_ratio <= 1, maximum_ratio=float(high_ratio), analytic_V=float(2*V))

    low_ratios=[]
    for mu in [.0001,.02,.4,3.]:
        for C,W,T,beta in [(4.,4.,2.1,0.),(.3,1.,1.3,.18),(0.,1.,2.,.6),(1.,0.,3.,0.)]:
            K=max(mu*1.001,100/mu)
            low = quad(lambda y: mu**3*y*y*low_bound(mu*y,mu,C,W,T,beta)**2,0,1,epsabs=1e-11)[0]
            high = quad(lambda y: (mu*np.exp(y))**3*low_bound(mu*np.exp(y),mu,C,W,T,beta)**2,
                        0,np.log(K/mu),epsabs=1e-10,epsrel=1e-10)[0]
            analytic=closed_low(mu,K,C,W,T,beta)
            low_ratios.append(float((low+high)/analytic))
    check('elementary_low_integral_enclosure', max(low_ratios) <= 1+1e-10, maximum_ratio=max(low_ratios))

    count_error=0.
    for mu in [0.,.02,.4,2.]:
        for k in [.02,.3,2.,7.]:
            for z in [-1.,-.3,.4,1.]:
                count_error=max(count_error,abs(coherent_original(k,mu,z)-coherent_weights(k,mu,z)))
    check('massive_coherent_original_vs_weights',count_error < 3e-12,maximum_error=float(count_error))

    zn, zw=leggauss(96)
    angular_error=0.
    for mu in [0.,.1,1.,5.]:
        for k in [.001,.1,1.,3.,10.]:
            om=math.hypot(k,mu); v=k/om
            B=(1+v*zn)*np.exp(-2j*om*L)+(v*zn-1)-2*v*zn*np.exp(-1j*(om*L+k*L*zn))
            direct=np.sum(zw*abs(B)**2)
            angular_error=max(angular_error,abs(direct-angular_expression(k,mu)))
    check('coherent_angular_reduction',angular_error < 2e-12,maximum_error=float(angular_error))

    target=np.array([[3064.,-1871.],[-1871.,3064.]])/(1620*np.pi)
    K=2000
    tail=128/(np.pi**2*K)
    grams=[]
    for mu in [0.,.001,.05,.5,2.,8.]:
        g24=massive_gram(mu,K,24)
        g32=massive_gram(mu,K,32)
        convergence=float(np.max(abs(g24-g32)))
        eigen=np.linalg.eigvalsh(g32)
        check('coherent_gram_quadrature_mu_'+str(mu),convergence < 3e-11 and min(eigen)>0,
              resolution_difference=convergence,eigenvalues=eigen.tolist(),tail_bound=float(tail))
        if mu == 0:
            check('massless_exact_gram_recovered_with_tail',np.max(abs(g32-target)) <= tail,
                  maximum_error=float(np.max(abs(g32-target))),tail_bound=float(tail))
        grams.append({'mu':mu,'finite_integral_gram':g32.tolist(),'cutoff':K,'entrywise_tail_bound':float(tail),
                      'quadrature_status':'floating convergence diagnostic; only tail is analytically certified'})
    eps_sequence=[]
    for mu in [.01,.0001,.000001,.00000001]:
        eps,Kopt=epsilon(mu,4.,4.,2.1,0.,24.)
        eps_sequence.append({'mu':mu,'epsilon_upper':eps,'K':Kopt})
    check('explicit_mass_continuity_enclosures',all(a['epsilon_upper']>b['epsilon_upper'] for a,b in zip(eps_sequence[:-1],eps_sequence[1:])),sequence=eps_sequence)

    # Feasible fields in a finite-dimensional common energy subspace.
    b0=np.array([[1.,.2,-.1],[.3,.5,.8]])
    bm=b0+np.array([[.01,-.02,.03],[-.04,.02,.01]])
    ep=np.linalg.norm(bm-b0,2)
    gram_error=np.linalg.norm(bm@bm.T-b0@b0.T,2)
    gram_bound=2*np.linalg.norm(b0,2)*ep+ep**2
    check('finite_hilbert_gram_perturbation',gram_error <= gram_bound,actual=float(gram_error),bound=float(gram_bound))
    state=np.array([.4,-1.,.7]); contrast=np.array([1.,-.3]); residual=bm@state
    response_bound=np.linalg.norm(b0.T@contrast)+ep*np.linalg.norm(contrast)
    energy_lower=(contrast@residual)**2/(2*response_bound**2)
    check('conditional_energy_lower_bound',energy_lower <= .5*state@state,lower=float(energy_lower),actual=.5*float(state@state))
    result={'status':'mathematical development controls; not empirical validation',
            'checks':CHECKS,'checks_passed':len(CHECKS),'observations_opened':0,'fitted_values':0,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'working_note_sha256':hashlib.sha256((HERE/'MASSIVE_RESPONSE_WORKING_v1.md').read_bytes()).hexdigest(),
            'massive_grams':grams,'mass_continuity_enclosures':eps_sequence,
            'limits':['No physical mass, energy/error upper budget or state selected.','Flat-background KG only; no dynamical curved-spacetime correction.','Finite quadrature error is not interval-certified.']}
    (HERE/'MASSIVE_RESPONSE_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checks_passed':len(CHECKS),'source_sha256':result['source_sha256'],'mass_continuity_enclosures':eps_sequence}))


if __name__ == '__main__':
    run()
