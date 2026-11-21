#!/usr/bin/env python3
"""Lead's numerical check of the staggered counterexample in library/rank-u-staggered-limit.md,
using the source's own matrices (checks/witness_rank_moment.py), not the author's derivation.

Field: A_eps = (x0 + 1) e1 + eps d_0 s, s = (-1)^x1 x0^3, x uncentred, F = e01.
The source code centres its potentials at c, so t_eps := (1 + c0) x1 + eps s gives this same A.

CRITERIA, written before the first run.
 PASS-P: the source's own M0 check, H P = J2 on the interior, relative 1e-10 for F = e01.
 PASS-S4: on NN(t_eps), eps != 0, |<J, x0^3 e_a>| / ||J|| <= 1e-7, a = 2, 3.
 PASS-C2: sigma_max(m on NN) falls with eps: over each factor 10 down in eps it falls by at least 5, while dim NN > 0;
          and sigma_max <= C_L eps with C_L of (S8).
 PASS-CTRL: at eps = 0 exactly, sigma_max(m on NN(t_0)) >= 0.01: the map is not zero before the limit, so the check can see it.
 CONTRAST (report only): the same sequence with s replaced by a random bounded function.
A failure of PASS-S4 or PASS-C2 refutes the counterexample as written. A pass is numerical evidence at L = 5, 6 only.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"; os.environ["OMP_NUM_THREADS"] = "1"; os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, sys.argv[2])
from witness_rank_moment import Moment, check_rss

L = int(sys.argv[1])
mo = Moment(L)
# REVISION after the first run at L = 5, recorded before this rerun: the source's relative rank tolerance 1e-9 misjudged the rank below
# eps ~ 1e-5 (dim NN jumped 740, 747, 764 while S4 failed only at those eps). The rank at eps != 0 is generic, so fix it from eps0 and
# take the d smallest right singular vectors, printing the smallest kept and largest dropped singular values. Criteria are unchanged.
_rank = {"r": None}
def kernel_fixed(A, tol=None):
    b = mo.box
    A = A / max(np.abs(A).max(), 1e-300)
    prod = mo.Zb * A[None, :]
    R = np.zeros((b.V, mo.n))
    for i in range(b.W):
        xa, xb = mo.ends[i]
        R[xa] += 0.5 * prod[:, i]; R[xb] += 0.5 * prod[:, i]
    K = np.vstack([R, mo.mom_h.T])
    U, sv, Vt = np.linalg.svd(K, full_matrices=True)
    rk = _rank["r"] if _rank["r"] is not None else int(np.sum(sv > 1e-9 * sv[0]))
    _rank["last"] = (sv[rk - 1] / sv[0], (sv[rk] / sv[0]) if rk < len(sv) else 0.0)
    return Vt[rk:], rk
mo.kernel = kernel_fixed
b = mo.box
F = np.zeros(6); F[0] = 1.0
coef, worst = mo.particular(F)
print(f"L={L} W={b.W} PASS-P rel={worst:.2e} {'PASS' if worst < 1e-10 else 'FAIL'}")
sites = np.array([list(k) for k, _ in sorted(b.sidx.items(), key=lambda kv: kv[1])])
c0 = mo.c[0]
x0, x1 = sites[:, 0], sites[:, 1]
s = (-1.0) ** x1 * x0.astype(float) ** 3
base = (1 + c0) * x1.astype(float)
ell = L - 1
E = 4 * ell * L**3
CL = np.sqrt(6 * E) * (8 * ell**6 + ell**4)
# test fields of (S4) on links, uncentred
dirs = np.array([l[1] for l in b.links]); lx0 = np.array([l[0][0] for l in b.links], dtype=float)
g2 = (dirs == 2) * lx0**3; g3 = (dirs == 3) * lx0**3

def sig(t):
    mN, dn, rk = mo.m_on_kernel(F, coef, t)
    sv = np.linalg.svd(mN, compute_uv=False) if mN.size else np.zeros(1)
    A = F @ mo.e + b.D0 @ t
    Nz, _ = mo.kernel(A)
    J = Nz @ mo.Zb  # orthonormal rows, currents on links
    s4 = max(np.abs(J @ g2).max(), np.abs(J @ g3).max()) if dn else 0.0
    return sv, dn, s4, np.abs(b.D0 @ (t - base)).max()

sv0, dn0, _, _ = sig(base)
print(f"eps=0: dim NN={dn0} sv={' '.join(f'{v:.3e}' for v in sv0)}  PASS-CTRL {'PASS' if sv0[0] >= 0.01 else 'FAIL'}")
eps0 = 1 / (4 * ell**3)
_rank["r"] = mo.kernel(F @ mo.e + b.D0 @ (base + eps0 * s))[1]
print(f"fixed rank {_rank['r']}")
prev = None; ok_c2 = True; ok_s4 = True
for k in range(0, 5):
    eps = eps0 * 10.0**-k
    sv, dn, s4, _ = sig(base + eps * s)
    fall = (prev / sv[0]) if prev else float("nan")
    ok_s4 &= s4 <= 1e-7; ok_c2 &= dn > 0 and sv[0] <= CL * eps
    if prev and fall < 5: ok_c2 = False
    prev = sv[0]
    print(f"eps={eps:.2e} dim NN={dn} sv_max={sv[0]:.3e} sv_max/eps={sv[0]/eps:.3e} fall={fall:.2f} S4={s4:.1e} kept/dropped sv={_rank['last'][0]:.1e}/{_rank['last'][1]:.1e} all sv: {' '.join(f'{v:.1e}' for v in sv)}")
    check_rss(2.0)
print(f"C_L={CL:.3e} PASS-S4 {'PASS' if ok_s4 else 'FAIL'} PASS-C2 {'PASS' if ok_c2 else 'FAIL'}")
_rank["r"] = None
rng = np.random.default_rng(5)
r = rng.normal(size=s.shape)
for eps in (1e-2, 1e-4):
    sv, dn, _, _ = sig(base + eps * r)
    print(f"CONTRAST random s, eps={eps:.0e}: dim NN={dn} sv: {' '.join(f'{v:.2e}' for v in sv)}")
