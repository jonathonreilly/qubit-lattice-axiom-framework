#!/usr/bin/env python3
"""Independent SU(2) conditional reflection and Haar-kernel diagnostics.

Full 4D side-6 plaquette/cell densities, random noncommuting link data,
conditional boundary rank-one forms, and two independent Haar normalizers.
No author code is imported; non-interval diagnostics do not prove the theorem.
"""
import itertools as it
import json
import math
import time
from fractions import Fraction as F
import numpy as np
import mpmath as mp

start = time.time()
mp.mp.dps = 65
checks, controls = {}, {}


def mul(a, b):
    return np.concatenate(((a[..., 0]*b[..., 0]-np.sum(a[..., 1:]*b[..., 1:], axis=-1))[..., None],
                           a[..., 0, None]*b[..., 1:]+b[..., 0, None]*a[..., 1:]+np.cross(a[..., 1:], b[..., 1:])), axis=-1)


def conj(a):
    return a*np.array([1, -1, -1, -1])


rng = np.random.default_rng(10292026)
n = 6
shape = (n,)*4+(4, 3)
samples = []
for j in range(3):
    xyz = rng.normal(0, .14, size=shape)
    angle = np.linalg.norm(xyz, axis=-1)
    samples.append(np.concatenate((np.cos(angle)[..., None], xyz*np.sinc(angle/np.pi)[..., None]), axis=-1))
boundary = samples[0]


def combine(i, j):
    out = samples[i].copy()
    for x in range(n):
        for d in range(4):
            if d == 0 and x >= n//2:
                out[x, ..., d, :] = conj(samples[j][(-x-1) % n, ..., d, :])
            elif d != 0 and x > n//2:
                out[x, ..., d, :] = samples[j][(-x) % n, ..., d, :]
            elif d != 0 and x in (0, n//2):
                out[x, ..., d, :] = boundary[x, ..., d, :]
    return out


def density_parts(U, delta):
    energy, G = 0., np.zeros((n,)*4, dtype=bool)
    for a, b in it.combinations(range(4), 2):
        Ua, Ub = U[..., a, :], U[..., b, :]
        p = mul(mul(mul(Ua, np.roll(Ub, -1, axis=a)), conj(np.roll(Ua, -1, axis=b))), conj(Ub))
        energy += float(np.sum(1-p[..., 0]))
        badp = np.sqrt(np.maximum(0, 2*(1-p[..., 0]))) >= delta
        transverse = [d for d in range(4) if d not in (a, b)]
        for shifts in it.product(range(2), repeat=2):
            bf = badp
            for d, shift in zip(transverse, shifts):
                bf = np.roll(bf, -shift, axis=d)
            G |= bf
    return energy, int(np.sum(G))


energies = np.zeros((3, 3))
badcounts = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        energies[i, j], badcounts[i, j] = density_parts(combine(i, j), .95)
forms = []
for h in [0., .7, 3.1]:
    logform = -.4*energies-h*badcounts
    defect = logform-(np.diag(logform)[:, None]+np.diag(logform)[None, :])/2
    assert np.max(np.abs(defect)) < 1e-11
    M = np.exp(logform-logform.max())
    eig = np.linalg.eigvalsh(M)
    assert eig.min() > -1e-12
    z = np.array([1+2j, -.3+.4j, .8-1j])
    assert np.vdot(z, M@z).real >= -1e-12
    forms.append({'h': h, 'max_log_factorization_error': float(abs(defect).max()), 'smallest_eigenvalue': float(eig.min())})
assert len(set(badcounts.ravel())) > 1
checks['noncommuting_4D_tilted_site_reflection_conditional_form'] = True
controls['penalty_was_not_constant_fixture'] = len(set(badcounts.ravel())) > 1

# Wrong reflection leaves the direction-normal link uninverted. It must break
# the density factorization for these genuinely noncommuting fields.
badE = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        U = combine(i, j)
        U[n//2:, ..., 0, :] = conj(U[n//2:, ..., 0, :])
        badE[i, j], _ = density_parts(U, .95)
reflection_mutation = float(abs(badE-(np.diag(badE)[:, None]+np.diag(badE)[None, :])/2).max())
controls['normal_link_reflection_inversion_omission_rejected'] = reflection_mutation > .01

# SU(2) arithmetic mean of noncommuting contours. Quaternion means need not
# be unitary: replacing their radius by one changes the actual normalizer.
qs = np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [.5, .5, .5, .5]])
m = np.mean(qs, axis=0)
r = mp.sqrt(sum(mp.mpf(str(float(x)))**2 for x in m))
assert 0 < r < 1
kernel_runs = []
for t in map(mp.mpf, ['.2', '2', '7']):
    x = t*r
    # Haar even moments: E[v0^(2k)] = (2k)!/[4^k k!(k+1)!].
    term, Hseries = mp.mpf(1), mp.mpf(1)
    for k in range(1, 180):
        term *= x*x/(4*k*(k+1))
        Hseries += term
    Hquad = 2/mp.pi*mp.quad(lambda th: mp.sin(th)**2*mp.exp(x*mp.cos(th)), [0, mp.pi/2, mp.pi])
    assert abs(Hseries-Hquad) < mp.mpf('1e-60')
    assert abs(mp.exp(-t)*Hquad/(mp.exp(-t)*Hseries)-1) < mp.mpf('1e-60')
    Hpolar = 2*mp.besseli(1, t)/t
    kernel_runs.append({'t': str(t), 'mean_radius': str(r), 'normalizer_relative_error': str(abs(Hseries/Hquad-1)),
                        'polar_normalizer_integral': str(Hquad/Hpolar),
                        'unnormalized_numerator_integral': str(mp.exp(-t)*Hquad)})
controls['polar_projected_kernel_normalizer_rejected'] = abs(Hquad/Hpolar-1) > mp.mpf('.01')
controls['uncompensated_kernel_normalizer_rejected'] = abs(mp.exp(-t)*Hquad-1) > mp.mpf('.01')
checks['actual_SU2_arithmetic_mean_Haar_kernel_normalizer'] = True

# Exact rational accounting for the raw-source cost; no RG input is assumed.
source_runs = []
for N, L in it.product([2, 3], [3, 5]):
    delta, eta, kmin = F(1, 1000), F(1, 2), F(1, 2)
    nA, nC = 192+6144*L**4, 48*L**4
    a, b = delta**2/(8*N), kmin*eta**2/(4*N)
    rho = min(F(1, 10**15), a/(4*nA), b/(4*nC))
    assert a-2*rho*nA >= a/2 and b-2*rho*nC >= b/2
    wrong_rho = a/nA
    assert a-2*wrong_rho*nA < 0
    # Wilson u=2N/g_std^2 and dg/dlog(mu)=-11N*g^3/(48*pi^2)
    # implies du/dlog(mu)=4N*11N/(48*pi^2).
    numerator = F(4*N)*F(11*N, 48)
    assert numerator == F(11*N*N, 12)
    actual_rate_at_delta_one = 11*N/(96*math.pi**2)
    assert actual_rate_at_delta_one < 4
    source_runs.append({'N': N, 'L': L, 'rho': str(rho), 'a_remaining': str(a-2*rho*nA),
                        'b_remaining': str(b-2*rho*nC), 'AF_volume_exponent_delta_one': 4-actual_rate_at_delta_one})
checks['source_radius_and_conditional_AF_convention'] = True
controls['excess_source_radius_rejected'] = a-2*wrong_rho*nA < 0
controls['standard_coupling_slope_substitution_rejected'] = F(11*N, 48) != numerator
assert all(checks.values()) and all(controls.values())
print(json.dumps({'checks': checks, 'negative_controls': controls,
                  'RP': {'torus_side': n, 'plaquettes': 6*n**4, 'cells': n**4,
                         'bad_cell_counts': badcounts.tolist(), 'forms': forms, 'wrong_reflection_defect': reflection_mutation},
                  'kernel': kernel_runs, 'source_budget': source_runs,
                  'scope': 'non-interval SU(2) diagnostics and exact rational budgets; no general-N or continuum proof',
                  'seconds': time.time()-start}, indent=2))
