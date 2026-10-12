#!/usr/bin/env python3
"""Tilted Cauchy quadrature versus scalar transport and independent source duality."""
import argparse
import json
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss

MASS = .83
SPEED = 1.37
SIGMA = .72
CENTER = .23
KAPPA = 1.17
SX = np.array([[0.,1.],[1.,0.]])
SY = np.array([[0.,-1j],[1j,0.]])
SQRT2PI = np.sqrt(2*np.pi)
WAVE_TOL = 2e-8
NORM_TOL = 2e-9

def energy(q):
    return np.sqrt(MASS*MASS+SPEED*SPEED*np.asarray(q)**2)

def matrix(q):
    q = np.asarray(q)
    return -SPEED*q[...,None,None]*SX-MASS*SY

def quadrature(n, radius):
    nodes, weights = leggauss(n)
    return radius*nodes, radius*weights

def packet_x(x):
    y = np.asarray(x)-CENTER
    envelope = np.exp(-y*y/(2*SIGMA*SIGMA))
    return envelope[:,None]*np.stack([np.cos(KAPPA*y), .61*np.sin(1.4*KAPPA*y)+.28*np.cos(.63*KAPPA*y)],axis=-1)

def packet_hat(q):
    q = np.asarray(q)
    def shifted(k):
        return SIGMA*np.exp(-.5*SIGMA*SIGMA*(q-k)**2)
    first = .5*(shifted(KAPPA)+shifted(-KAPPA))
    second = .61*(shifted(1.4*KAPPA)-shifted(-1.4*KAPPA))/(2j)+.14*(shifted(.63*KAPPA)+shifted(-.63*KAPPA))
    return np.exp(-1j*q*CENTER)[:,None]*np.stack([first,second],axis=-1)

def spin(eta):
    return np.cosh(eta/2)*np.eye(2)-np.sinh(eta/2)*SX

def flow(q, eta):
    return np.asarray(q)*np.cosh(eta)+energy(q)*np.sinh(eta)/SPEED

def gauge(q, kind, band):
    q = np.asarray(q)
    if kind == 'parallel':
        return np.zeros_like(q)
    if kind == 'constant':
        return np.full_like(q, .37*band)
    # The negative phase is -chi_plus(-q), preserving real conjugation.
    return band*np.pi/2+np.arctan(SPEED*q/MASS)/2

def frame(q, kind, band):
    q = np.asarray(q)
    theta = np.arctan(SPEED*q/MASS)
    u = np.stack([np.exp(.5j*theta), -1j*band*np.exp(-.5j*theta)],axis=-1)/np.sqrt(2)
    return u*np.exp(1j*gauge(q,kind,band))[:,None]

def band_boost_hat(q, eta, initial_hat, kind='parallel', berry=True, reverse=False):
    answer = np.zeros((len(q),2),dtype=complex)
    for band in [1,-1]:
        k = flow(q, (1 if reverse else -1)*band*eta)
        u0 = frame(k,kind,band)
        coefficient = np.einsum('ij,ij->i',u0.conj(),initial_hat(k))
        phase = np.exp(1j*(gauge(k,kind,band)-gauge(q,kind,band))) if berry else np.ones_like(k)
        answer += frame(q,kind,band)*(np.sqrt(energy(k)/energy(q))*coefficient*phase)[:,None]
    return answer

def integrate_inverse(hat, q, weights, x):
    return np.exp(1j*x[:,None]*q[None,:])@(weights[:,None]*hat)/SQRT2PI

def direct_tilted(q, weights, x, eta, wrong_spin=False):
    # Hermitian eigendecomposition supplies this path's projectors; no analytic frame is used.
    values, vectors = np.linalg.eigh(matrix(q))
    fhat = packet_hat(q)
    xp = x*np.cosh(eta)
    tp = x*np.sinh(eta)/SPEED
    phi = np.zeros((len(x),2),dtype=complex)
    for column in range(2):
        eigenvector = vectors[:,:,column]
        coeff = np.einsum('ij,ij->i',eigenvector.conj(),fhat)
        phase = np.exp(1j*(xp[:,None]*q[None,:]+tp[:,None]*values[:,column][None,:]))
        phi += phase@(weights[:,None]*coeff[:,None]*eigenvector)/SQRT2PI
    boosted = phi@spin(-eta if wrong_spin else eta).T
    return boosted, phi

def norm2(array, weights):
    return float(np.sum(weights[:,None]*np.abs(array)**2))

def relative_error(left, right, weights):
    return np.sqrt(norm2(left-right,weights)/max(norm2(right,weights),1e-300))

def source_time_hat(omega):
    return np.exp(-.5*.31**2*np.asarray(omega)**2-1j*(-.17)*np.asarray(omega))

def source_cauchy_hat(q):
    values, vectors = np.linalg.eigh(matrix(q))
    hhat = packet_hat(q)
    result = np.zeros_like(hhat)
    for column in range(2):
        u = vectors[:,:,column]
        coefficient = np.einsum('ij,ij->i',u.conj(),hhat)*source_time_hat(values[:,column])
        result += u*coefficient[:,None]
    return result

def transformed_source_hat(q, eta, wrong_spin=False):
    values, vectors = np.linalg.eigh(matrix(q))
    result = np.zeros((len(q),2),dtype=complex)
    # Full Fourier covectors transform by Lambda^T after changing spacetime variables.
    lam = np.array([[np.cosh(eta),np.sinh(eta)/SPEED],
                    [SPEED*np.sinh(eta),np.cosh(eta)]])
    source_spin = spin(-eta if wrong_spin else eta)
    for column in range(2):
        covectors = np.stack([values[:,column],q],axis=-1)@lam
        transformed = packet_hat(covectors[:,1])*source_time_hat(covectors[:,0])[:,None]
        transformed = transformed@source_spin.T
        u = vectors[:,:,column]
        result += u*np.einsum('ij,ij->i',u.conj(),transformed)[:,None]
    return result

def run_level(n, eta, variant):
    q, wq = quadrature(n,24.)
    x, wx = quadrature(n,10.)
    kind = 'rational' if variant in ['missing_berry','rational_correct'] else ('constant' if variant=='constant_phase' else 'parallel')
    berry = variant != 'missing_berry'
    reverse = variant == 'reverse_scalar'
    direct, phi = direct_tilted(q,wq,x,eta,variant=='wrong_spin')
    scalar_hat = band_boost_hat(q,eta,packet_hat,kind,berry,reverse)
    scalar = integrate_inverse(scalar_hat,q,wq,x)
    initial_norm = norm2(packet_x(x),wx)
    flux_density = np.cosh(eta)*np.sum(np.abs(phi)**2,axis=1)-np.sinh(eta)*np.einsum('ij,ij->i',phi.conj(),phi@SX.T).real
    flux = float(np.dot(wx,flux_density))
    source_left = transformed_source_hat(q,eta,variant=='wrong_source_spin')
    source_right = band_boost_hat(q,-eta,source_cauchy_hat,kind,berry,reverse)
    measurements = {
        'cauchy_full_wave_relative_error':relative_error(direct,scalar,wx),
        'cauchy_norm_relative_error':abs(norm2(direct,wx)-initial_norm)/initial_norm,
        'cauchy_realness_relative_error':np.sqrt(norm2(direct.imag,wx)/initial_norm),
        'scalar_norm_relative_error':abs(norm2(scalar,wx)-initial_norm)/initial_norm,
        'tilted_flux_relative_error':abs(flux-initial_norm)/initial_norm,
        'source_full_vector_relative_error':relative_error(source_left,source_right,wq),
        'scalar_realness_relative_error':np.sqrt(norm2(scalar.imag,wx)/initial_norm),
        'source_real_structure_relative_error':relative_error(source_left,source_left[::-1].conj(),wq),
    }
    gates = []
    for name, value in measurements.items():
        limit = WAVE_TOL if name in ['cauchy_full_wave_relative_error','source_full_vector_relative_error'] else NORM_TOL
        gates.append({'name':name,'value':value,'limit':limit,'pass':bool(value<=limit)})
    return {'nodes':n,'eta':eta,'initial_norm_squared':initial_norm,
            'cauchy_norm_squared':norm2(direct,wx),'scalar_norm_squared':norm2(scalar,wx),'tilted_flux':flux,
            'source_norm_squared':norm2(source_left,wq),'source_reference_norm_squared':norm2(source_right,wq),
            'checks':gates}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--variant', choices=['baseline','wrong_spin','reverse_scalar','missing_berry','wrong_source_spin','rational_correct','constant_phase'], default='baseline')
    ap.add_argument('--nodes', default='180,360')
    args = ap.parse_args()
    levels = [int(x) for x in args.nodes.split(',')]
    rows = [run_level(n,eta,args.variant) for n in levels for eta in [.47,-.38]]
    passed = all(check['pass'] for row in rows for check in row['checks'])
    result = {'variant':args.variant,'python':platform.python_version(),'numpy':np.__version__,
              'fixture':{'m':MASS,'v':SPEED,'sigma':SIGMA,'center':CENTER,'kappa':KAPPA},
              'scope':'Ordinary floating quadrature on Schwartz fixtures; no compact-support, domain or infinite-dimensional local-net certificate.',
              'thresholds':{'wave':WAVE_TOL,'norm_and_realness':NORM_TOL},'rows':rows,
              'all_checks_passed':passed}
    print(json.dumps(result,indent=2))
    return 0 if passed else 1

if __name__ == '__main__':
    raise SystemExit(main())
