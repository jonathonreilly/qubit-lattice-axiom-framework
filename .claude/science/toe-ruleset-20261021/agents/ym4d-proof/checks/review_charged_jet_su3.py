"""Actual-path SU(3) product jets versus stated local coefficients."""
import json
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq
from review_charged_jet_independent import Paths

N = 3
rng = np.random.default_rng(209161)
checks = []


def trace(x):
    return float(np.trace(x).real / N)


def dagger(a):
    return np.swapaxes(a.conj(), -2, -1)


def su3(count):
    z = rng.normal(size=(count, N, N)) + 1j*rng.normal(size=(count, N, N))
    z = (z - dagger(z)) * .13
    return z - np.trace(z, axis1=-2, axis2=-1)[:, None, None]*np.eye(N)/N


def pmul(a, b):
    out = np.zeros_like(a)
    for k in range(5):
        for j in range(k+1):
            out[..., k, :, :] += a[..., j, :, :] @ b[..., k-j, :, :]
    return out


def pexp(a):
    out = np.zeros(a.shape[:-2] + (5, N, N), complex)
    out[..., 0, :, :] = np.eye(N)
    for j in range(1, 5):
        out[..., j, :, :] = out[..., j-1, :, :] @ a / j
    return out


def productjet(path, field, output):
    ids, signs = path.idx[output], path.sgn[output]
    result = np.zeros((path.count, 5, N, N), complex)
    result[:, 0] = np.eye(N)
    B = np.zeros((path.count, N, N), complex)
    prefix = np.zeros_like(B)
    for k in range(ids.shape[-1]):
        x = field[ids[:, k]]*signs[:, k, None, None]
        B += (prefix@x-x@prefix)/2
        prefix += x
        result = pmul(result, pexp(x))
    return result.mean(axis=0), B.mean(axis=0)


def direct_phi_jet(M, b):
    X = pmul(dagger(M), M)
    X[0] -= np.eye(N)
    root = np.zeros_like(X)
    root[0] = np.eye(N)
    power = np.zeros_like(X)
    power[0] = np.eye(N)
    for k, c in enumerate([.5, -.125, .0625, -5/128], 1):
        power = pmul(power, X)
        root += c*power
    return np.array([trace(x) for x in root - pmul(pexp(-b), M)])


def cj5(M, b):
    A, M2, M3 = M[1:4]
    r = b-A
    R2 = M2+dagger(M2)-A@A
    return trace(r@M3 + dagger(M2)@M2/2 - b@b@M2/2
                 + b@b@b@A/6-b@b@b@b/24-R2@R2/8)


def eq(name, value, expected):
    err = float(abs(value-expected))
    threshold = 1e-10+1e-9*abs(expected)
    checks.append(dict(name=name, error=err, threshold=threshold, pass_=err<=threshold))


def nonzero(name, value):
    value = float(abs(value))
    checks.append(dict(name=name, witness=value, floor=1e-7, pass_=value>1e-7))


path = Paths((3, 6, 3, 3))
field = su3(path.nfine)
M, B = productjet(path, field, 0)
b = su3(1)[0]
phi = direct_phi_jet(M, b)
A, r = M[1], b-M[1]
eq("M2_commutator_mean", np.linalg.norm((M[2]-dagger(M[2]))/2-B), 0)
eq("quadratic", phi[2], -trace(r@r)/2)
eq("cubic", phi[3], trace(r@B))
eq("CJ5_full_quartic", phi[4], cj5(M, b))
eq("CJ6_zero_residual_square", direct_phi_jet(M, A)[4], -trace(B@B)/2)
nonzero("colour_commutator_deletion", np.linalg.norm(B))
nonzero("trace_normalization", (N-1)*phi[4])
R2 = M[2]+dagger(M[2])-A@A
nonzero("polar_R2_square_omission", trace(R2@R2)/8)
plaq = Paths((3,6,3,3), "plaquette")
P, Bp = productjet(plaq, field, 3)
X = P.copy()
X[0] -= np.eye(N)
log = X.copy()
power = X.copy()
for k in range(2,5):
    power = pmul(power,X)
    log += (-1)**(k+1)*power/k
f, C = log[1], log[3]
eq("CJ4_plaquette_cubic", -trace(P[3]), -trace(f@Bp))
eq("CJ4_plaquette_quartic", -trace(P[4]), -trace(Bp@Bp)/2-trace(f@C)-trace(f@f@f@f)/24)
scales = []
for eps in [.06,.03,.015]:
    e = np.array([expm(eps*x) for x in field])
    ids, signs = path.idx[0], path.sgn[0]
    curr = np.tile(np.eye(N, dtype=complex), (path.count,1,1))
    for k in range(ids.shape[-1]):
        factor = e[ids[:,k]].copy()
        negative = signs[:,k]<0
        factor[negative] = dagger(factor[negative])
        factor[signs[:,k]==0] = np.eye(N)
        curr = curr @ factor
    exactM = curr.mean(axis=0)
    phase = float(np.angle(np.linalg.det(exactM)))
    singular = np.linalg.svd(exactM, compute_uv=False)
    lagrange = brentq(lambda v: np.sum(np.arcsin(v/singular))-phase,
                      -min(singular)/2,min(singular)/2,xtol=1e-17)
    angles = np.arcsin(lagrange/singular)
    correction = float(np.sum(2*singular*np.sin(angles/2)**2)/N)
    eq("SU3_phase_constraint_"+str(eps), np.sum(angles), phase)
    scales.append(dict(epsilon=eps, phase=phase, phase_over_cube=phase/eps**3,
                       maximum_correction=correction, correction_over_sixth=correction/eps**6))
phase6 = [x['correction_over_sixth'] for x in scales]
nonzero("SU3_nonzero_cubic_determinant_phase", scales[-1]['phase_over_cube'])
checks.append(dict(name="SU3_sixth_order_correction_scaling", relative_spread=float(np.ptp(phase6)/max(phase6)),
                   threshold=.05, pass_=bool(np.ptp(phase6)/max(phase6)<.05)))
result = dict(N=N, actual_contours=path.count, phi_coefficients=phi.tolist(),
              zero_residual_square=-trace(B@B)/2, determinant_scaling=scales,
              checks=checks, passed=sum(x['pass_'] for x in checks), total=len(checks))
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(x['pass_'] for x in checks) else 1)
