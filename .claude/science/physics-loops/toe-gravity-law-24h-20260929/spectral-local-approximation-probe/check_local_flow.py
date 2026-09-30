#!/usr/bin/env python3
"""Diagnostic of the actual sampled ADM Hamiltonian; no proof by convergence plot.

Transverse reflections make the x-dependent diagonal canonical subspace
invariant. The code compares the original Christoffel Hamiltonian gradient
with a separately integrated-by-parts local variation, then evolves it.
"""
import json
import os
import resource
import signal
import time
from pathlib import Path

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
RUNTIME = Path("/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929")
assert not (RUNTIME / "STOP_REQUESTED.json").exists()
assert time.time() < json.loads((RUNTIME / "DEADLINE.json").read_text())["deadline_epoch"]
signal.alarm(30)
started = time.monotonic()
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

A, B, C = gs = sp.symbols("A B C", positive=True)
pa, pb, pc = ps = sp.symbols("pa pb pc")
qa, qb, qc = qs = sp.symbols("qa qb qc")
ra, rb, rc = rs = sp.symbols("ra rb rc")
S = sp.sqrt(A * B * C)
W = [S / x for x in gs]
u, b, c, v, w = qa / (2*A), qb / (2*B), qc / (2*C), -qb / (2*A), -qc / (2*A)
potential = (-ra*(b+c) + rb*v + rc*w
             - W[0]*(u*(b+c)-b*b-c*c)
             - W[1]*v*(u-b+c) - W[2]*w*(u+b-c))
trace = sum(x*y for x, y in zip(gs, ps))
kinetic = (sum((x*y)**2 for x, y in zip(gs, ps)) - trace**2/2)/S
arguments = (*gs, *ps, *qs, *rs)
exprs = ([sp.diff(kinetic, x) for x in ps]
         + [-sp.diff(kinetic+potential, x) for x in gs]
         + [sp.diff(potential, x) for x in qs]
         + [sp.diff(potential, x) for x in rs]
         + [sp.diff(x, y) for x in W for y in gs])
local = sp.lambdify(arguments, exprs, "numpy", cse=True)


def derivative(n):
    assert n % 2 == 1 and n >= 3
    spacing = 2*np.pi/n
    out = np.zeros((n, n))
    for j in range(n):
        out[j, (j+1) % n] = 1/(2*spacing)
        out[j, (j-1) % n] = -1/(2*spacing)
    assert np.array_equal(out, -out.T)
    return out


def original(g, p, D):
    """Literal scalar curvature with centered derivatives left unexpanded."""
    aa, bb, cc = g
    qa_, qb_, qc_ = g @ D.T
    u_, b_, c_ = qa_/(2*aa), qb_/(2*bb), qc_/(2*cc)
    v_, w_ = -qb_/(2*aa), -qc_/(2*aa)
    rxx = -D @ (b_+c_) + u_*(b_+c_)-b_*b_-c_*c_
    ryy = D @ v_ + v_*(u_-b_+c_)
    rzz = D @ w_ + w_*(u_+b_-c_)
    sqrtg = np.sqrt(aa*bb*cc)
    gp = g*p
    td = (np.sum(gp*gp, axis=0)-np.sum(gp, axis=0)**2/2)/sqrtg
    cd = td - sqrtg*(rxx/aa+ryy/bb+rzz/cc)
    jd = np.sum(p*(g @ D.T), axis=0)-2*(D @ (aa*p[0]))
    return np.mean(cd), cd, jd


def rhs(t, state, D):
    n = D.shape[0]
    g, p = state.reshape(2, 3, n)
    q = g @ D.T
    sqrtg = np.sqrt(np.prod(g, axis=0))
    ww = sqrtg/g
    r = ww @ D.T
    values = local(*g, *p, *q, *r)
    z = np.asarray([np.broadcast_to(x, (n,)) for x in values])
    dg = z[:3]
    dp = z[3:6]+z[6:9] @ D.T
    dw = z[9:12] @ D.T
    wgrad = z[12:].reshape(3, 3, n)
    dp += np.einsum("ijn,in->jn", wgrad, dw)
    return np.stack([dg, dp]).reshape(-1)


# A generic aliased fixture challenges the exact finite Hamiltonian variation.
n = 7
x = np.arange(n)*2*np.pi/n
D = derivative(n)
g = np.array([1+.04*np.cos(x)+.01*np.sin(2*x),
              1+.03*np.sin(x), 1-.02*np.cos(2*x)])
p = np.array([.08+.03*np.sin(x), .04+.02*np.cos(x), -.03+.01*np.sin(2*x)])
state = np.stack([g, p]).reshape(-1)
velocity = rhs(0, state, D).reshape(2, 3, n)
complex_gradient = np.empty((2, 3, n))
epsilon = 1e-24
for block in range(2):
    for i in range(3):
        for j in range(n):
            trial = np.stack([g, p]).astype(complex)
            trial[block, i, j] += 1j*epsilon
            complex_gradient[block, i, j] = n*original(*trial, D)[0].imag/epsilon
expected = np.stack([complex_gradient[1], -complex_gradient[0]])
gradient_error = float(np.max(np.abs(velocity-expected)))
assert gradient_error < 1e-11, gradient_error

# Pull back the exact Kasner solution by X=x+eta sin(x), at continuum time1.
eta = 1/20
sigma0 = 1/20
metric_initial_norm_2sigma0 = 2*eta*np.exp(2*sigma0)+eta**2/2*(1+np.exp(4*sigma0))
assert metric_initial_norm_2sigma0 < 1/8
exponents = np.array([-1/3, 2/3, 2/3])
duration = .01
rows = []
for n in (17, 33, 65, 129, 257):
    x = np.arange(n)*2*np.pi/n
    D = derivative(n)
    f = 1+eta*np.cos(x)

    def kasner(t):
        scale = t**(2*exponents)
        metric = np.array([scale[0]*f*f, scale[1]+0*f, scale[2]+0*f])
        momenta = np.array([(exponents[0]-1)/scale[0]/f,
                            (exponents[1]-1)/scale[1]*f,
                            (exponents[2]-1)/scale[2]*f])
        return np.stack([metric, momenta])

    initial = kasner(1)
    initial_energy, c0, j0 = original(*initial, D)
    exact_end = kasner(1+duration)
    solution = solve_ivp(lambda t, y: rhs(t, y, D), (0, duration), initial.reshape(-1),
                         method="DOP853", rtol=2e-12, atol=2e-14)
    assert solution.success, solution.message
    final = solution.y[:, -1].reshape(2, 3, n)
    energy, cfinal, jfinal = original(*final, D)
    rows.append({"n": n, "J": (n-1)//2, "spacing": float(2*np.pi/n), "function_evaluations": solution.nfev,
                 "initial_C_sup": float(np.max(np.abs(c0))),
                 "initial_J_sup": float(np.max(np.abs(j0))),
                 "state_error_sup": float(np.max(np.abs(final-exact_end))),
                 "final_C_sup": float(np.max(np.abs(cfinal))),
                 "final_J_sup": float(np.max(np.abs(jfinal))),
                 "energy_drift": float(abs(energy-initial_energy))})

result = {"couplings": {"a": 1, "K": 1}, "full_gradient_fixture_n": 7,
          "gradient_complex_step_error": gradient_error,
          "eta": eta, "sigma0": sigma0,
          "initial_metric_norm_at_2sigma0": metric_initial_norm_2sigma0,
          "duration": duration, "rows": rows,
          "seconds": time.monotonic()-started,
          "max_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          "derivative": "Local centered difference; same author engine adapted, not independent",
          "scope": "Floating deterministic diagnostic; no interval certification, no uniform theorem from samples, duration not certified by majorant bound."}
Path(__file__).with_name("local_flow.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
