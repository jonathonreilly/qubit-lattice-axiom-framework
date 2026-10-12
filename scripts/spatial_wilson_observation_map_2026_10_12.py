#!/usr/bin/env python3
"""Finite controls for the explicitly supplied spatial Wilson observation map.

All controls are synthetic. Analytic source arguments carry global quantifiers;
this runner supplies no nature data, detector likelihood, or formal audit.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/SPATIAL_WILSON_OBSERVATION_MAP_AND_MASS_MATCHING_BOUNDED_THEOREM_NOTE_2026-10-12.md',
    'data/spatial_wilson_observation_map_2026_10_12/observations.json',
)
if not __debug__:
    raise RuntimeError("Scientific controls require assertions; optimized Python is unsupported")

import argparse
from pathlib import Path
import itertools
import math
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / 'outputs/spatial_wilson_observation_map_2026_10_12/results.json'
MUTATION = ''



# Canonical link vertex and displaced-shell coarea
from pathlib import Path
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq, root
from scipy.integrate import quad
em_sx = np.array([[0, 1], [1, 0]], complex)
em_sy = np.array([[0, -1j], [1j, 0]])
em_sz = np.diag([1, -1])
em_i2 = np.eye(2)
em_G = [np.kron(em_sx, s) for s in [em_sx, em_sy, em_sz]] + [np.kron(em_sz, em_i2)]

def em_dvec(p, mu):
    p = np.asarray(p)
    return np.r_[np.sqrt(1 - mu) * np.sin(p), mu + 2 * np.sum(np.sin(p / 2) ** 2)]

def em_energy(p, mu):
    return np.linalg.norm(em_dvec(p, mu))

def em_eg(p, mu):
    v = 2 * np.sin(p / 2) ** 2
    return np.sin(p) * (1 + v.sum() + (mu - 1) * v) / em_energy(p, mu)

def em_omega(k):
    return 2 * np.linalg.norm(np.sin(k / 2))

def em_og(k):
    return np.sin(k) / em_omega(k)

def em_op(v):
    return sum((x * g for x, g in zip(v, em_G)))

def em_basis(v):
    v = v / np.linalg.norm(v)
    ref = np.eye(3)[np.argmin(abs(v))]
    u = np.cross(v, ref)
    u /= np.linalg.norm(u)
    return np.array([u, np.cross(v, u)])

def em_vertex(p, k, mu, eps):
    z = p - k / 2
    return np.r_[np.sqrt(1 - mu) * eps * np.cos(z), np.dot(eps, np.sin(z))]

def em_strength(p, k, mu):
    q = p - k
    npv = em_dvec(p, mu) / em_energy(p, mu)
    nq = em_dvec(q, mu) / em_energy(q, mu)
    out = 0.0
    for eps in em_basis(2 * np.sin(k / 2)):
        v = em_vertex(p, k, mu, eps)
        out += np.dot(v, v) * (0.5 * np.dot(npv - nq, npv - nq)) + 2 * np.dot(npv, v) * np.dot(nq, v)
    return out

def em_matrix_checks():
    rng = np.random.default_rng(16041)
    errors = []
    for j in range(160):
        p = rng.uniform(-np.pi, np.pi, 3)
        k = rng.uniform(-np.pi, np.pi, 3)
        mu = rng.uniform(0.03, 0.9)
        q = p - k
        hp = em_op(em_dvec(p, mu))
        hq = em_op(em_dvec(q, mu))
        ward = sum((2 * np.sin(k[z] / 2) * em_op(em_vertex(p, k, mu, np.eye(3)[z])) for z in range(3)))
        assert np.max(abs(ward - hp + hq)) < 4e-15
        xp, up = np.linalg.eigh(hp)
        xq, uq = np.linalg.eigh(hq)
        sp = 0.0
        for eps in em_basis(2 * np.sin(k / 2)):
            V = em_op(em_vertex(p, k, mu, eps))
            sp += np.linalg.norm(uq[:, 2:].conj().T @ V @ up[:, 2:]) ** 2
        err = abs(em_strength(p, k, mu) - sp)
        errors.append(err)
        assert err < 2e-14
    return {'cases': len(errors), 'max_eigenspinor_error': max(errors)}

def em_F(A, y):
    return y * (1 - A + (1 - 2 * A) * y + (1 - A) * y * y) / 4

def em_maxima(A):
    vals = [(1.0, em_F(A, 1.0))]
    if A > np.sqrt(3) - 1:
        y = (1 - A) / (2 * A - 1 + np.sqrt(A * A + 2 * A - 2))
        vals.append((y, em_F(A, y)))
    return max(vals, key=lambda v: v[1])

def em_primitive_intervals(A, b):
    B = 1 - A
    roots = np.roots([B / 4, (1 - 2 * A) / 4, B / 4, -b * b])
    ends = [0.0, 1.0] + [float(z.real) for z in roots if abs(z.imag) < 1e-09 and 0 < z.real < 1]
    ends = sorted(ends)
    return [(l, u) for l, u in zip(ends, ends[1:]) if em_F(A, (l + u) / 2) > b * b]

def em_leading(A, b):

    def integrand(y):
        D = em_F(A, y) - b * b
        return (1 - y) ** 2 * D / y + (1 - y) ** 2 * (b - y / 2) ** 2 / y + 2 * D
    return 0.5 * sum((quad(integrand, l, u, epsabs=1e-13)[0] for l, u in em_primitive_intervals(A, b)))

def em_exact_shell(A, b, r, ny=40, nt=24):
    t = (1 + np.sqrt(6 * A - 2)) / 3
    n = np.array([np.sqrt(t), np.sqrt((1 - t) / 2), np.sqrt((1 - t) / 2)])
    U = em_basis(n)
    p = r * n
    mu = b * r * r
    ep = em_energy(p, mu)
    cache = {}
    resids = []

    def center(y):
        if y in cache:
            return cache[y]

        def g(z):
            q = r * y * n + r * r * (z @ U)
            k = p - q
            return U @ (em_eg(q, mu) - em_og(k)) / r
        rr = root(g, [0.0, 0.0], tol=1e-09)
        z = rr.x
        q = r * y * n + r * r * (z @ U)
        gap = ep - em_energy(q, mu) - em_omega(p - q)
        resid = float(np.linalg.norm(g(z)))
        resids.append(resid)
        assert resid < 2e-08
        cache[y] = (z, gap)
        return (z, gap)
    ys = np.linspace(1e-05, 1 - 1e-05, 500)
    positive = [center(y)[1] > 0 for y in ys]
    bounds = []
    for i in range(len(ys) - 1):
        if positive[i] != positive[i + 1]:
            bounds.append(brentq(lambda y: center(y)[1], ys[i], ys[i + 1], xtol=1e-12))
    ends = [1e-05] + bounds + [1 - 1e-05]
    intervals = [(l, u) for l, u in zip(ends, ends[1:]) if center((l + u) / 2)[1] > 0]
    nodes, weights = leggauss(ny)
    total = 0.0
    shell_res = []
    for l, u in intervals:
        for y, wy in zip((l + u) / 2 + (u - l) * nodes / 2, (u - l) * weights / 2):
            zc, _ = center(y)
            q0 = r * y * n + r * r * (zc @ U)
            theta_sum = 0.0
            for angle in 2 * np.pi * (np.arange(nt) + 0.5) / nt:
                direction = np.cos(angle) * U[0] + np.sin(angle) * U[1]

                def gap(rho):
                    q = q0 + rho * direction
                    return ep - em_energy(q, mu) - em_omega(p - q)
                hi = r * r
                while gap(hi) > 0:
                    hi *= 2
                rho = brentq(gap, 0, hi, xtol=1e-15, rtol=1e-13)
                q = q0 + rho * direction
                k = p - q
                der = abs(np.dot(-em_eg(q, mu) + em_og(k), direction))
                shell_res.append(abs(gap(rho)))
                theta_sum += rho * em_strength(p, k, mu) / (em_omega(k) * der)
            total += wy * theta_sum * 2 * np.pi / nt
    val = r * total / (4 * np.pi)
    return {'A': A, 'b': b, 'r': r, 'ny': ny, 'nt': nt, 'intervals': intervals, 'gamma_over_alpha': val, 'leading_over_alpha': r ** 3 * em_leading(A, b), 'ratio': val / (r ** 3 * em_leading(A, b)), 'max_shell_residual': max(shell_res, default=0), 'max_center_gradient': max(resids), 'longitudinal_cutoff': 1e-05}


# Open-boundary real-space magnetic Hamiltonian
import numpy as np
from scipy.sparse import diags, bmat
from scipy.sparse.linalg import eigsh
import math, json
from pathlib import Path

def field_evaluate(mu, a2, w, B, extent=12):
    N = int(math.ceil(extent / math.sqrt(B))) | 1
    x = np.arange(N) - (N - 1) / 2
    T = diags(np.ones(N - 1), 1, shape=(N, N), dtype=complex)
    D = (T - T.T.conjugate()) / 2j
    C = (T + T.T.conjugate()) / 2
    sy = diags(np.sin(-B * x))
    M = diags(mu + w * (2 - np.cos(B * x))) - w * C
    vals = []
    resids = []
    for sign in [1, -1]:
        off = math.sqrt(a2) * (D - sign * 1j * sy)
        H = bmat([[M, off], [off.T.conjugate(), -M]], format='csc')
        ev, vec = eigsh(H, k=5, sigma=mu, which='LM', tol=2e-12, v0=np.ones(2 * N, dtype=complex))
        order = np.argsort(ev)
        ev = ev[order]
        vec = vec[:, order]
        assert ev[0] > 0
        vals.append(ev)
        resids.append(max((np.linalg.norm(H @ vec[:, i] - ev[i] * vec[:, i]) for i in range(5))))
    plus, minus = vals
    spin = minus[0] - plus[0]
    cycl = plus[1] - plus[0]
    expected = a2 / (a2 + mu * w)
    return dict(mu=mu, a2=a2, w=w, B=B, N=N, extent=extent, spin_gap=spin, cyclotron_gap=cycl, ratio=spin / cycl, target=expected, anomaly_over_B=(spin - cycl) / B, plus=plus.tolist(), minus=minus.tolist(), max_residual=max(resids))


# Scalar exchange, contact and gauge controls
from pathlib import Path
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
mass_sx = np.array([[0, 1], [1, 0]], complex)
mass_sy = np.array([[0, -1j], [1j, 0]])
mass_sz = np.diag([1.0, -1.0])
mass_i2 = np.eye(2)
mass_I = np.eye(4)
mass_gam = [np.kron(mass_sz, mass_i2)] + [np.kron(mass_sx, s) for s in [mass_sx, mass_sy, mass_sz]]

def mass_symbols(k):
    W = 2 * np.sum(np.sin(k / 2) ** 2, axis=-1)
    om = np.sqrt(2 * W)
    E = np.sqrt(np.sum(np.sin(k) ** 2, axis=-1) + W * W)
    return (W, om, E)

def mass_densities(k):
    W, om, E = mass_symbols(k)
    tad = 3 / (4 * om)
    exc = (4 * W - E * E) / (2 * E * om * (E + om))
    pos = (E * E + 3 * E * om + 8 * W) / (4 * E * om * (E + om))
    return np.stack([tad, exc, pos], axis=-1)

def mass_integrate_duffy(n):
    z, w = leggauss(n)
    u = (z + 1) / 2
    v = u.copy()
    ww = np.outer(w / 2, w / 2)
    U, V = np.meshgrid(u, v, indexing='ij')
    total = np.zeros(3)
    for t, wt in zip(np.pi * (z + 1) / 2, np.pi * w / 2):
        k = np.stack([np.full_like(U, t), t * U, t * V], axis=-1)
        total += wt * t * t * np.sum(ww[:, :, None] * mass_densities(k), axis=(0, 1))
    return 3 * total / np.pi ** 3

def mass_integrate_cube(n):
    z, w = leggauss(n)
    x = np.pi * (z + 1) / 2
    ww = np.outer(w, w) / 4
    X, Y = np.meshgrid(x, x, indexing='ij')
    total = np.zeros(3)
    for v, wv in zip(x, w / 2):
        k = np.stack([np.full_like(X, v), X, Y], axis=-1)
        total += wv * np.sum(ww[:, :, None] * mass_densities(k), axis=(0, 1))
    return total

def mass_matrix_controls():
    rng = np.random.default_rng(912740)
    errs = []
    gauges = []
    freq = []
    naive = []
    for j in range(120):
        k = rng.uniform(-np.pi, np.pi, 3)
        k0 = rng.normal() * 3
        W, om, E = mass_symbols(k)
        K = np.r_[k0, 2 * np.sin(k / 2)]
        K2 = K @ K
        D = -1j * (k0 * mass_gam[0] + sum((np.sin(k[i]) * mass_gam[i + 1] for i in range(3)))) + W * mass_I
        S = np.linalg.inv(D)
        vs = [1j * mass_gam[0]] + [1j * np.cos(k[i] / 2) * mass_gam[i + 1] - np.sin(k[i] / 2) * mass_I for i in range(3)]
        ward = sum((K[i] * vs[i] for i in range(4)))
        assert np.max(abs(ward + D)) < 3e-15
        scalar = -sum((np.trace(v @ S @ v).real / 4 for v in vs)) / K2
        pred = (4 * W - E * E) / ((k0 * k0 + E * E) * K2)
        errs.append(abs(scalar - pred))
        assert errs[-1] < 2e-14
        longitudinal = -np.trace(ward @ S @ ward).real / (4 * K2 * K2) + om * om / (2 * K2 * K2)
        gauges.append(abs(longitudinal))
        assert gauges[-1] < 1e-14
        Dnaive = D - W * mass_I
        Snaive = np.linalg.inv(Dnaive)
        nv = [vs[0]] + [1j * np.cos(k[i] / 2) * mass_gam[i + 1] for i in range(3)]
        trace0 = -sum((np.trace(v @ Snaive @ v).real / 4 for v in nv)) / K2
        naive.append(abs(trace0))
        assert naive[-1] < 2e-14
        if j < 20:
            val, err = quad(lambda u: (4 * W - E * E) / ((u * u + E * E) * (u * u + om * om)) / np.pi, 0, np.inf, epsabs=1e-12, epsrel=1e-12)
            expected = (4 * W - E * E) / (2 * E * om * (E + om))
            freq.append(abs(val - expected))
            assert freq[-1] < 3e-13
    return dict(matrix_cases=120, max_scalar_error=max(errs), max_gauge_cancellation_error=max(gauges), max_naive_scalar=max(naive), frequency_cases=20, max_frequency_error=max(freq))


# Fixed-regulator kinetic derivatives and exact static response
from pathlib import Path
import numpy as np, json
from numpy.polynomial.legendre import leggauss

def kin_fields(k, m):
    s = np.sin(k)
    c = np.cos(k)
    W = 2 * np.sum(np.sin(k / 2) ** 2, axis=-1)
    M = m + W
    E = np.sqrt(np.sum(s * s, axis=-1) + M * M)
    om = np.sqrt(2 * W)
    g = s * (c + M[..., None]) / E[..., None]
    return (s, c, W, M, E, om, g)

def kin_densities(k, m):
    s, c, W, M, E, o, g = kin_fields(k, m)
    E2 = E * E
    I1 = 1 / (2 * E * o * (E + o))
    I2 = (2 * E + o) / (4 * E ** 3 * o * (E + o) ** 2)
    A = 1 - 2 * c * c + 3 * c - 2 * M[..., None] * c
    B = 2 * s * s * (M[..., None] - 3 + c) * (M[..., None] + c)
    zt = -2 * I1 + 4 * E2 * I2
    zs = np.mean(A, axis=-1) * I1 + np.mean(B, axis=-1) * I2 - 1 / (4 * o)
    ze = (1 - np.mean(g * g, axis=-1)) / (2 * E ** 3)
    ibp = np.zeros_like(E)
    orig = np.zeros_like(E)
    for x in range(3):
        for y in range(3):
            if x == y:
                continue
            gx = g[..., x]
            u = g[..., y]
            h = s[..., x] * s[..., y]
            ibp += (1 - 2 * h * h + 6 * h * gx * u - 5 * gx * gx * u * u) / (2 * E ** 3) / 6
            epp = (c[..., x] ** 2 + M * c[..., x] - gx * gx) / E
            np2 = (1 - gx * gx) / E2
            up = (h - gx * u) / E
            upp = c[..., x] * s[..., y] / E - 2 * gx * h / E2 - u * epp / E + 2 * u * gx * gx / E2
            orig += ((np2 + u * upp - up * up) / (2 * E) + (1 - u * u) * epp / (4 * E2)) / 6
    return np.stack([zs - zt, ze, ibp, orig, ibp - ze], axis=-1)

def kin_cubature(fun, m, n):
    z, w = leggauss(n)
    u = (z + 1) / 2
    U, V = np.meshgrid(u, u, indexing='ij')
    ww = np.outer(w / 2, w / 2)
    breaks = [0.0, min(m, np.pi)]
    while breaks[-1] < np.pi:
        breaks.append(min(np.pi, 4 * breaks[-1]))
    total = None
    for lo, hi in zip(breaks, breaks[1:]):
        for t, wt in zip((lo + hi) / 2 + (hi - lo) * z / 2, (hi - lo) * w / 2):
            k = np.stack([np.full_like(U, t), t * U, t * V], axis=-1)
            arr = fun(k, m)
            part = wt * t * t * np.sum(ww[:, :, None] * arr, axis=(0, 1))
            if total is None:
                total = np.zeros_like(part)
            total += part
    return 3 * total / np.pi ** 3

def kin_static_difference(k, m, ext):
    s, c, W, M, E, o, g = kin_fields(k, m)
    d = np.concatenate([s, M[..., None]], axis=-1)
    out = np.zeros_like(E)
    for x in range(3):
        kp = k.copy()
        km = k.copy()
        kp[..., x] += ext / 2
        km[..., x] -= ext / 2
        sp, cp, wp, mp, ep, op, gp = kin_fields(kp, m)
        sm, cm, wm, mm, em, om, gm = kin_fields(km, m)
        npv = np.concatenate([sp, mp[..., None]], axis=-1) / ep[..., None]
        nmv = np.concatenate([sm, mm[..., None]], axis=-1) / em[..., None]
        for y in range(3):
            if x == y:
                continue
            v = np.zeros_like(d)
            v[..., y] = c[..., y]
            v[..., 3] = s[..., y]
            strength = 1 + np.sum(npv * nmv, axis=-1) - 2 * np.sum(npv * v, axis=-1) * np.sum(nmv * v, axis=-1)
            zero = (1 - g[..., y] ** 2) / E
            out += -2 * (strength / (ep + em) - zero) / (ext * ext) / 6
    return out[..., None]


# Original matrix kinetic derivatives
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import quad
mat_S = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.diag([1.0, -1.0])]
mat_G = [np.diag([1.0, 1.0, -1.0, -1.0])] + [np.block([[np.zeros((2, 2)), -1j * s], [1j * s, np.zeros((2, 2))]]) for s in mat_S]
mat_I = np.eye(4, dtype=complex)
mat_C = [1j * mat_G[0] @ g for g in mat_G[1:]] + [mat_G[0]]

def mat_dirac(p, m):
    return 1j * mat_G[0] * p[0] + sum((1j * g * np.sin(x) for g, x in zip(mat_G[1:], p[1:]))) + (m + sum(1 - np.cos(p[1:]))) * mat_I

def mat_vertices(p, k):
    a = p[1:] - k[1:] / 2
    return [1j * mat_G[0]] + [1j * g * np.cos(x) + mat_I * np.sin(x) for g, x in zip(mat_G[1:], a)]

def mat_matrix_derivative(k, m, j):
    p = np.zeros(4)
    q = p - k
    prop = np.linalg.inv(mat_dirac(q, m))
    vs = mat_vertices(p, k)
    kh = np.r_[k[0], 2 * np.sin(k[1:] / 2)]
    K2 = kh @ kh
    dp = 1j * mat_G[j] if j == 0 else 1j * mat_G[j] * np.cos(q[j]) + mat_I * np.sin(q[j])
    sp = -prop @ dp @ prop
    out = np.zeros((4, 4), complex)
    for a, v in enumerate(vs):
        vp = np.zeros((4, 4), complex)
        if a == j and j > 0:
            vp = -1j * mat_G[j] * np.sin(-k[j] / 2) + mat_I * np.cos(-k[j] / 2)
        out -= vp @ prop @ v + v @ sp @ v + v @ prop @ vp
    if j > 0:
        out -= 0.5j * mat_G[j]
    out /= K2
    return float((np.trace(mat_G[j] @ out) / 4j).real)

def mat_reduced(k, m, j):
    nu = k[0]
    s = np.sin(k[1:])
    c = np.cos(k[1:])
    W = 2 * np.sum(np.sin(k[1:] / 2) ** 2)
    M = m + W
    E2 = s @ s + M * M
    R = nu * nu + E2
    K2 = nu * nu + 2 * W
    if j == 0:
        return (2 / R - 4 * nu * nu / (R * R)) / K2
    a = j - 1
    A = 1 - 2 * c[a] ** 2 + 3 * c[a] - 2 * M * c[a]
    B = 2 * s[a] ** 2 * (M - 3 + c[a]) * (M + c[a])
    return (A / R + B / (R * R) - 0.5) / K2

def mat_integrated_closed(k, m):
    s = np.sin(k)
    c = np.cos(k)
    W = 2 * np.sum(np.sin(k / 2) ** 2)
    M = m + W
    E = math.sqrt(s @ s + M * M)
    o = math.sqrt(2 * W)
    I1 = 1 / (2 * E * o * (E + o))
    I2 = (2 * E + o) / (4 * E ** 3 * o * (E + o) ** 2)
    A = 1 - 2 * c * c + 3 * c - 2 * M * c
    B = 2 * s * s * (M - 3 + c) * (M + c)
    return np.r_[-2 * I1 + 4 * E * E * I2, A * I1 + B * I2 - 1 / (4 * o)]

def mat_band(k, m):
    d = np.r_[np.sin(k), m + np.sum(1 - np.cos(k))]
    E = np.linalg.norm(d)
    H = sum((x * g for x, g in zip(d, mat_C)))
    return (d / E, (mat_I + H / E) / 2, (mat_I - H / E) / 2)


def spectrum_controls():
    rng=np.random.default_rng(93401);identity=[];pair=[];axis=[]
    for _ in range(400):
        p=rng.uniform(-math.pi,math.pi,3);k=rng.uniform(-math.pi,math.pi,3)
        mu=rng.uniform(.01,.95);x=1-np.cos(p);W=x.sum()
        rhs=mu*mu+2*W+2*sum(x[i]*x[j] for i in range(3) for j in range(i))+mu*(x@x)
        if MUTATION=='spectrum_mass':rhs+=mu*mu
        identity.append(abs(em_energy(p,mu)**2-rhs));assert identity[-1]<6e-14
        lower=math.sqrt(4*mu*mu+em_omega(k)**2)
        pair.append(em_energy(p,mu)+em_energy(k-p,mu)-lower);assert pair[-1]>=-1e-13
        P=rng.uniform(-math.pi,math.pi);q=rng.uniform(-math.pi,math.pi,3)
        gap=em_energy([P,0,0],mu)-em_energy(q,mu)-em_omega(np.array([P,0,0])-q)
        axis.append(float(gap));assert gap<1e-13
    corners=[]
    for c in itertools.product([0,1],repeat=3):
        p=np.array(c)*math.pi;gap=em_energy(p,.1);assert abs(gap-(.1+2*sum(c)))<1e-14
        corners.append({'corner':c,'gap':gap})
    return {'sample_count':400,'max_identity_error':max(identity),'minimum_pair_slack':min(pair),
            'largest_sample_axis_excess':max(axis),'corners':corners,
            'scope':'Finite controls of full-torus inequalities proved in the note.'}


def magnetic_controls():
    rows=[field_evaluate(.3,.7,1,B) for B in [.001,.00025,.0000625]]
    target=.7 if MUTATION!='magnetic_wilson' else 1.
    errors=[abs(x['ratio']-target) for x in rows]
    assert errors[-1]<.001 and errors[-1]<errors[0]/8
    repeat=field_evaluate(.3,.7,1,.00025,14)
    assert abs(repeat['ratio']-rows[1]['ratio'])<2e-8
    assert max(x['max_residual'] for x in rows+[repeat])<1e-9
    # Separate finite two-by-two Landau blocks, also a non-unit Wilson check.
    landau=[]
    for mu,a2,w in [(.2,.8,1),(.2,1.,1),(.3,.82,.6)]:
        B=1e-7;n=1
        mat=np.array([[mu+w*B*(n+.5),math.sqrt(2*a2*B*n)],
                      [math.sqrt(2*a2*B*n),-mu-w*B*(n-.5)]])
        val=np.linalg.eigvalsh(mat)[1]
        formula=w*B/2+math.sqrt((mu+w*B*n)**2+2*a2*B*n)
        assert abs(val-formula)<2e-15
        landau.append({'mu':mu,'a2':a2,'w':w,'positive_eigenvalue':val,'operational_ratio':a2/(a2+mu*w)})
    return {'open_boundary_rows':rows,'extent_repeat':repeat,'landau_blocks':landau,
            'scope':'Synthetic literal-link hopping; finite B, extent and eigenvector residuals retained.'}


def cherenkov_controls():
    rows=[]
    for A in [1/3,.5,.739,.75,.8,.9,.99]:
        y,M=em_maxima(A)
        candidates=[0.,1.]+[float(t.real) for t in np.roots([3*(1-A),2*(1-2*A),1-A])
                            if abs(t.imag)<1e-12 and 0<t.real<1]
        actual=max(em_F(A,t) for t in candidates)
        chosen=em_F(A,1.) if MUTATION=='cherenkov_soft_only' else M
        assert abs(chosen-actual)<1e-13
        n1=(1+math.sqrt(6*A-2))/3
        n=np.array([math.sqrt(n1),math.sqrt((1-n1)/2),math.sqrt((1-n1)/2)])
        yy=min(y,.8);b=.7*math.sqrt(em_F(A,yy))
        errors=[]
        expected=(1-yy)*(em_F(A,yy)-b*b)/(2*yy)
        for r in [.04,.02,.01]:
            mu=b*r*r;gap=em_energy(r*n,mu)-em_energy(yy*r*n,mu)-em_omega((1-yy)*r*n)
            errors.append(abs(gap/r**3-expected))
        assert errors[-1]<2e-5 and errors[-1]<errors[0]/8+2e-10
        rows.append({'A':A,'maximizer':y,'maximum':M,'expansion_errors':errors})
    Ac=(8-2*math.sqrt(2))/7
    assert abs(em_F(Ac,1)-em_F(Ac,math.sqrt(2)-1))<1e-16
    assert abs(em_maxima(.75)[1]-1/108)<1e-16
    return {'rows':rows,'crossover':Ac,'scope':'Leading polynomial and fixed-fraction small-r controls, not a finite-r global search.'}


def vertex_controls():
    rng=np.random.default_rng(12801);errors=[]
    for _ in range(80):
        p=rng.uniform(-math.pi,math.pi,3);k=rng.uniform(-math.pi,math.pi,3);mu=.3
        vv=[]
        for i in range(3):
            v=em_vertex(p,k,mu,np.eye(3)[i])
            if MUTATION=='vertex_wilson':v[3]=0
            vv.append(em_op(v))
        err=np.max(abs(sum(2*np.sin(k[i]/2)*vv[i] for i in range(3))-
                       em_op(em_dvec(p,mu))+em_op(em_dvec(p-k,mu))))
        errors.append(float(err));assert err<2e-14
    return {'ward_cases':80,'max_ward_error':max(errors),'eigenspinor':em_matrix_checks()}


def rate_controls():
    rows=[]
    for A in [.5,.8,.9]:
        b=.8*math.sqrt(em_maxima(A)[1]);pair=[]
        for r in [.04,.02]:
            row=em_exact_shell(A,b,r,ny=24,nt=16)
            tested=row['ratio']/(2 if MUTATION=='rate_normalization' else 1)
            assert abs(tested-1)<.02
            assert row['max_shell_residual']<5e-13
            rows.append(row);pair.append(abs(tested-1))
        assert pair[-1]<pair[0]*.7+.0002
    A=.8;b=.8*math.sqrt(em_maxima(A)[1])
    refined=em_exact_shell(A,b,.04,ny=48,nt=32)
    change=abs(refined['gamma_over_alpha']/rows[2]['gamma_over_alpha']-1)
    assert change<2e-7
    return {'rows':rows,'refinement':refined,'refinement_relative_change':change,
            'scope':'Detected near-central shells; y endpoints cut at1e-5. Not the whole finite-momentum torus rate.'}


def mass_controls():
    matrix=mass_matrix_controls();rows=[]
    for n in [16,32,48]:
        v=mass_integrate_duffy(n);total=(0 if MUTATION=='mass_seagull' else v[0])+v[1]
        assert abs(total-v[2])<2e-13
        rows.append({'n':n,'seagull':float(v[0]),'exchange':float(v[1]),'positive_total':float(v[2])})
    assert abs(rows[-1]['positive_total']-rows[-2]['positive_total'])<2e-12
    direct=mass_integrate_cube(64)
    assert abs(direct[2]-rows[-1]['positive_total'])<3e-8
    return {'matrix':matrix,'duffy':rows,'untransformed_cube_n64':direct.tolist(),
            'scope':'Finite order-e2 inverse-propagator scalar; convergence estimates, not interval proof.'}


def kinetic_subtracted(n):
    z,w=leggauss(n);u=(z+1)/2;U,V=np.meshgrid(u,u,indexing='ij');ww=np.outer(w/2,w/2)
    R=np.sqrt(1+U*U+V*V);A=(1+U**4+V**4)/R**4;h=(5*A-3)/(12*R**3);out=np.zeros(3)
    for t,wt in zip(math.pi*(z+1)/2,math.pi*w/2):
        k=np.stack([np.full_like(U,t),t*U,t*V],axis=-1);d=kin_densities(k,0.)
        out[0]+=wt*np.sum(ww*t*t*d[...,0]);out[1]+=wt*np.sum(ww*(t*t*d[...,4]-h/t))
    out[1]+=np.sum(ww*h*np.log(R));out[2]=np.sum(ww*h);out*=3/math.pi**3
    contacts=np.array([1/(24*math.pi**2),1/(60*math.pi**2)])
    if MUTATION=='kinetic_contacts':contacts*=0
    return {'n':n,'massless_fermion':float(out[0]),'spherical_massless_photon':float(out[1]),
            'angular_zero_residual':float(out[2]),'contacts':contacts.tolist(),
            'matched_differences':(out[:2]+contacts).tolist()}


def kinetic_controls():
    rng=np.random.default_rng(441902);matrix_errors=[];frequency_errors=[]
    for _ in range(100):
        k=np.r_[rng.normal()*2,rng.uniform(-math.pi,math.pi,3)];m=rng.uniform(.001,.5)
        matrix_errors.extend(abs(mat_matrix_derivative(k,m,j)-mat_reduced(k,m,j)) for j in range(4))
    assert max(matrix_errors)<2e-12
    for _ in range(4):
        k=rng.uniform(-1.5,1.5,3);m=.2;o=em_omega(k);closed=mat_integrated_closed(k,m)
        for j in range(4):
            val,_=quad(lambda th:mat_matrix_derivative(np.r_[o*np.tan(th),k],m,j)*o/
                       (np.cos(th)**2)/(2*math.pi),-math.pi/2,math.pi/2,epsabs=2e-10)
            frequency_errors.append(abs(val-closed[j]))
    assert max(frequency_errors)<3e-9
    rows=[kinetic_subtracted(n) for n in [24,40]]
    assert np.max(abs(np.array(rows[0]['matched_differences'])-rows[1]['matched_differences']))<3e-11
    fixed=[]
    for m in [.01,.0001,.000001]:
        v=kin_cubature(kin_densities,m,24)
        assert abs(v[2]-v[3])<2e-11
        fixed.append({'m':m,'fermion':float(v[0]),'electric':float(v[1]),'magnetic':float(v[2]),
                      'photon_difference':float(v[4]),'ibp_error':float(v[2]-v[3])})
    limiting=np.array(rows[-1]['matched_differences'])
    assert np.max(abs(limiting-[fixed[-1]['fermion'],fixed[-1]['photon_difference']]))<5e-7
    full=kin_cubature(kin_densities,.2,24);static=[]
    for q in [.04,.02,.01]:
        val=float(kin_cubature(lambda k,m:kin_static_difference(k,m,q),.2,24)[0])
        static.append({'q':q,'value':val,'error':abs(val-full[2])})
    assert static[-1]['error']<5e-6 and static[-1]['error']<static[0]['error']/12
    return {'matrix_derivative_cases':400,'matrix_derivative_max_error':max(matrix_errors),
            'matrix_frequency_cases':16,'matrix_frequency_max_error':max(frequency_errors),
            'subtracted':rows,'positive_regulators':fixed,'finite_static_control':static,
            'scope':'Fixed-positive-m Euclidean derivative limits and finite local matching; no physical pole-speed identification.'}


def observation_controls():
    data=json.loads((ROOT/AUDIT_INPUT_PATHS[1]).read_text());ds={x['id']:x for x in data['data']}
    m=ds['electron_rest_energy']['value']*(1000 if MUTATION=='data_unit' else 1)
    assert abs(1000*m-.51099895069)<1e-15
    eqg=ds['timing_EQG2_subluminal']['value'];sigma=ds['fan_g_over_2']['standard_uncertainty']
    bound=6*m/eqg;assert abs(bound-4.443469136434782e-15)<1e-28
    assert ds['hess_candidate_endpoint']['interpretation']=='not an identified electron-survival energy'
    assert data['selection_and_complexity']['fit_count']==0
    assert data['selection_and_complexity']['blind_validation_count']==0
    for datum in data['data']:
        assert datum['role'] in ['discovery','fit','calibration','nuisance','comparator']
        assert datum['source'] in data['sources']
    return {'tree_deficit_envelope':bound,'fraction_of_fan_standard_uncertainty':bound/sigma,
            'mass_calibration_relative_standard_uncertainty':ds['electron_rest_energy']['standard_uncertainty']/m,
            'fit_count':0,'blind_validation_count':0,'empirical_exclusion_count':0,
            'scope':'Conditional tree parameter comparison; no combined confidence interpretation.'}


def main():
    global MUTATION
    families={'spectrum':spectrum_controls,'magnetic':magnetic_controls,'cherenkov':cherenkov_controls,
              'vertex':vertex_controls,'rate':rate_controls,'mass':mass_controls,
              'kinetic':kinetic_controls,'observations':observation_controls}
    mutations={'spectrum_mass':'spectrum','magnetic_wilson':'magnetic','cherenkov_soft_only':'cherenkov',
               'vertex_wilson':'vertex','rate_normalization':'rate','mass_seagull':'mass',
               'kinetic_contacts':'kinetic','data_unit':'observations'}
    p=argparse.ArgumentParser();p.add_argument('--mutation',choices=list(mutations));args=p.parse_args()
    MUTATION=args.mutation or '';selected=[mutations[MUTATION]] if MUTATION else list(families)
    result={'scope':'Author finite controls for a supplied Wilson law; no empirical fit, audit or physical exclusion.'}
    for name in selected:
        result[name]=families[name]();print(name+': PASS',flush=True)
    if MUTATION:
        print('MUTATION SURVIVED: '+MUTATION);return
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('per_element: checked original 4x4 traces, link Ward identities and matrix derivatives.')
    print('per_site: checked finite open-boundary synthetic magnetic hopping with extent control.')
    print('per_mode: checked free spectra, declared emission shells and continuous-frequency integrals.')
    print('per_block: checked quadrature refinement, regulator limits and one-loop local coefficients.')
    print('lattice_wide: checked and not executed numerically — no full interacting-lattice simulation; full-torus and limiting quantifiers rest on the stated proofs.')
    print('TOTAL: PASS=8 FAIL=0')


if __name__=='__main__':
    main()
