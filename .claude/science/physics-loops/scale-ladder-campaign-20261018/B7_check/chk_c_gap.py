#!/usr/bin/env python3
"""(c): own certified even-filling insulator (nu = 2, class G = translations + 24 dressed rotations),
own nu = 1 insulator with a single C2, and the site irreps with/without inversion."""
import itertools, sys
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__file__))
from chk_core import *

T4 = torus_ops(4)
def sym_blocks(idx, r, seed, scale):
    rr = np.random.default_rng(seed)
    h = {d: rr.normal(size=(12, 12)) + 1j*rr.normal(size=(12, 12)) for d in itertools.product(range(-r, r+1), repeat=3)}
    A = T4['from_blocks'](h); A = (A + A.conj().T)/2
    S = sum(T4['G'](g) @ A @ T4['G'](g).T for g in idx) / len(idx)
    hb = T4['to_blocks'](S, r)
    nrm = max(np.linalg.norm(B, 2) for B in hb.values())
    return {d: scale * B / nrm for d, B in hb.items()}

def site_commutant_blocks(idx, seed=0):
    rr = np.random.default_rng(seed)
    X = rr.normal(size=(12, 12)) + 1j*rr.normal(size=(12, 12)); X = X + X.conj().T
    Y = sum(UF[g] @ X @ UF[g].T for g in idx) / len(idx)
    ev, V = np.linalg.eigh(Y)
    return ev, V

def certify(h, nu, N):
    t = 2*np.pi*np.arange(N)/N
    ks = np.array(list(itertools.product(t, t, t)))
    Emax, Emin = -np.inf, np.inf
    for chunk in np.array_split(ks, 64):
        e = np.linalg.eigvalsh(Hk(h, chunk))
        Emax = max(Emax, e[:, nu-1].max()); Emin = min(Emin, e[:, nu].min())
    Lip = sum(np.linalg.norm(B, 2) * np.linalg.norm(d) for d, B in h.items())
    delta = np.sqrt(3) / 2 * 2*np.pi/N
    return Emin - Emax, Emin - Emax - 2*Lip*delta

# site irreps: commutant eigenvalue multiplicities = irrep dims (generic)
for name, idx in (('O (proper)', PROPER), ('O_h', ALL), ('C2x only', [0, find(np.diag([1, -1, -1]))])):
    ev, V = site_commutant_blocks(idx)
    print(f"site one-particle irreps under {name}: dims {mults(ev, 1e-8)}")

# nu = 2 in class G: on-site -P onto a 2-dim irrep + random symmetric range-1 hopping (strength 0.15)
ev, V = site_commutant_blocks(PROPER, 3)
mm = mults(ev, 1e-8); start = 0; P = None
for d_ in mm:
    if d_ == 2: P = V[:, start:start+2] @ V[:, start:start+2].conj().T; break
    start += d_
assert all(np.allclose(UF[g] @ P @ UF[g].T, P) for g in PROPER)
h = sym_blocks(PROPER, 1, 11, 0.02)
h[(0, 0, 0)] = h[(0, 0, 0)] - P
# symmetry check of the Bloch Hamiltonian at random continuous k (incl. affine shift)
ks = np.random.default_rng(5).uniform(-np.pi, np.pi, (10, 3))
okB = all(np.allclose(UF[g] @ Hk(h, k)[0] @ UF[g].T, Hk(h, fibre_image(g, k))[0]) for g in PROPER for k in ks)
print("Bloch symmetry U_g H(k) U_g^T = H(Rk + pi R lam) at random k, all 24:", okB)
for N in (24, 48):
    g_, c_ = certify(h, 2, N)
    print(f"nu=2 class G: grid N={N} indirect gap {g_:.4f}, certified lower bound {c_:.4f}")
print("k* levels of this nu=2 Hamiltonian:", np.round(np.linalg.eigvalsh(Hk(h, np.array([.5, -.5, .5])*np.pi)[0])[:4], 4))

# same Hamiltonian at nu = 1, 3: forced closures at k*
e = np.linalg.eigvalsh(Hk(h, np.array([.5, -.5, .5])*np.pi)[0])
print("E1,E2 at k*:", e[0], e[1], " E3,E4:", e[2], e[3])

# nu = 1 with C2x alone: on-site projector onto one eigenvector of a generic C2x-commuting matrix
c2x = find(np.diag([1, -1, -1])); idx = [0, c2x]
ev, V = site_commutant_blocks(idx, 4)
P1 = np.outer(V[:, 0], V[:, 0].conj())
assert all(np.allclose(UF[g] @ P1 @ UF[g].T, P1) for g in idx)
h1 = sym_blocks(idx, 1, 12, 0.02); h1[(0, 0, 0)] = h1[(0, 0, 0)] - P1
g_, c_ = certify(h1, 1, 48)
print(f"nu=1 with only C2x: grid gap {g_:.4f}, certified {c_:.4f}")
