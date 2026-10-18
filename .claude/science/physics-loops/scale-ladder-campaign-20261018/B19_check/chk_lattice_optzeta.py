#!/usr/bin/env python3
"""B19 check L4 (float, NOT gating): does the O(a^2) scalar / O(a) Maxwell defect survive OPTIMISING zeta?
B19 measured {G,G} - G[zeta_lat] against one 'natural' second-order zeta_lat, on one smooth test field.
Here: min over ALL bond fields zeta of ||([X_xi,X_eta] - X_zeta) Pi||_F / ||[X_xi,X_eta] Pi||_F, Pi = the 7 lowest
plane waves (k = 0, +-e_j) of the field space; X = D (scalar G_m) or the pure-translation Maxwell G_L
(= G_A - Gauss[theta], no Gauss projection needed). Sparse LSQR. Also prints the same with B19-style zeta_nat
(continuum Lie bracket of the smooth xi, eta sampled at bond midpoints) for comparison.
"""
import sys, time
from itertools import product
import numpy as np, scipy.sparse as sps
from scipy.sparse.linalg import lsqr
from chk_lattice import idx_site, idx_link, sh, D_scalar, M_maxwell

def grad_op(L):
    r, c, v = [], [], []
    for x in product(range(L), repeat=3):
        for j in range(3):
            r += [idx_link(L, x, j)] * 2; c += [idx_site(L, sh(x, j)), idx_site(L, x)]; v += [1, -1]
    return sps.csr_matrix((v, (r, c)), shape=(3 * L ** 3, L ** 3))

def theta_op(L, xi):
    """theta_w = sum_i xi_(w-i,i) A_(w-i,i)  as (sites x links)."""
    r, c, v = [], [], []
    for w in product(range(L), repeat=3):
        for i in range(3):
            l = idx_link(L, sh(w, i, -1), i)
            r.append(idx_site(L, w)); c.append(l); v.append(xi[l])
    return sps.csr_matrix((v, (r, c)), shape=(L ** 3, 3 * L ** 3))

def ML(L, xi, G):
    # G_L = G_A - Gauss[theta]; Gauss[theta] = sum_w theta_w (div E)_w = -E^T grad theta -> delta A gets + grad theta
    return M_maxwell(L, xi) + G @ theta_op(L, xi)

# continuum fields
rng = np.random.default_rng(5)
KX = [[(rng.integers(-1, 2, 3), rng.uniform(0.5, 1), rng.uniform(0, 6.3)) for _ in range(2)] for _ in range(3)]
KE = [[(rng.integers(-1, 2, 3), rng.uniform(0.5, 1), rng.uniform(0, 6.3)) for _ in range(2)] for _ in range(3)]
def fval(spec, pos):
    return sum(a * np.cos(2 * np.pi * pos @ k + ph) for k, a, ph in spec)
def fgrad(spec, pos):
    return sum(-a * np.sin(2 * np.pi * pos @ k + ph)[:, None] * (2 * np.pi * k)[None, :] for k, a, ph in spec)
def bond_field(L, S, a_scale):
    grid = np.array(list(product(range(L), repeat=3)), float) / L
    out = np.zeros(3 * L ** 3)
    for j in range(3):
        pos = grid.copy(); pos[:, j] += 0.5 / L
        out[j::3] = fval(S[j], pos) * a_scale   # lattice components = a * continuum vector
    return out
def nat_zeta(L):
    grid = np.array(list(product(range(L), repeat=3)), float) / L
    out = np.zeros(3 * L ** 3); a = 1.0 / L
    for j in range(3):
        pos = grid.copy(); pos[:, j] += 0.5 / L
        xv = np.stack([fval(KX[k], pos) for k in range(3)], 1); ev = np.stack([fval(KE[k], pos) for k in range(3)], 1)
        gx = fgrad(KX[j], pos); ge = fgrad(KE[j], pos)
        out[j::3] = ((xv * ge).sum(1) - (ev * gx).sum(1)) * a * a   # [xi,eta] lattice comps: a * (a-scaled vector field)
    return out

def modes(L, ncomp):
    grid = np.array(list(product(range(L), repeat=3)), float)
    ks = [np.zeros(3)] + [s * np.eye(3)[j] for j in range(3) for s in (1, -1)]
    cols = []
    for k in ks:
        ph = np.exp(2j * np.pi * grid @ k / L)
        for c in range(ncomp):
            v = np.zeros(ncomp * L ** 3, complex); v[c::ncomp] = ph; cols.append(v)
    return np.array(cols).T

def run(L, kind):
    a = 1.0 / L
    xi, et = bond_field(L, KX, a), bond_field(L, KE, a)
    nb = 3 * L ** 3
    if kind == "scalar":
        G = None; op = lambda z: D_scalar(L, z); Pi = modes(L, 1)
    else:
        G = grad_op(L); op = lambda z: ML(L, z, G); Pi = modes(L, 3)
    T = (op(xi) @ (op(et) @ Pi) - op(et) @ (op(xi) @ Pi))
    # sparse design: column b = vec(op(e_b) Pi)
    rows, cols, vals = [], [], []
    m = Pi.shape[1]
    for b in range(nb):
        e = np.zeros(nb); e[b] = 1
        Y = sps.csr_matrix(op(e)) @ Pi
        nz = np.nonzero(np.abs(Y) > 0)
        rows += list(nz[0] * m + nz[1]); cols += [b] * len(nz[0]); vals += list(Y[nz])
    A = sps.csr_matrix((vals, (rows, cols)), shape=(T.size, nb))
    Ar = sps.vstack([A.real, A.imag]).tocsr(); tr = np.concatenate([T.ravel().real, T.ravel().imag])
    sol = lsqr(Ar, tr, atol=1e-12, btol=1e-12, iter_lim=20000)
    z = sol[0]
    ropt = np.linalg.norm(Ar @ z - tr) / np.linalg.norm(tr)
    zn = nat_zeta(L)
    # sign: find best scalar multiple s of zeta_nat (convention-free), report residual
    v = Ar @ zn; s = (v @ tr) / (v @ v)
    rnat = np.linalg.norm(s * v - tr) / np.linalg.norm(tr)
    return ropt, rnat, s

if __name__ == "__main__":
    Ls = [int(x) for x in sys.argv[1:]] or [8, 12, 16, 24]
    out = {"scalar": [], "maxwellL": []}
    for L in Ls:
        for kind in out:
            t0 = time.time()
            ro, rn, s = run(L, kind)
            out[kind].append((L, ro, rn, s))
            print(f"   L={L:3d} {kind:8s}: optimal-zeta defect {ro:.3e} | best multiple of continuum-sampled zeta: defect {rn:.3e} (multiple {s:+.4f}) ({time.time()-t0:.0f}s)", flush=True)
    for kind, rws in out.items():
        Lv = np.array([r[0] for r in rws], float)
        so = np.polyfit(np.log(Lv[-3:]), np.log([r[1] for r in rws][-3:]), 1)[0]
        sn = np.polyfit(np.log(Lv[-3:]), np.log([r[2] for r in rws][-3:]), 1)[0]
        print(f"   {kind}: slope (last 3 L) optimal-zeta {so:.2f}, sampled-zeta {sn:.2f}   [diagnostic, not gated]")
