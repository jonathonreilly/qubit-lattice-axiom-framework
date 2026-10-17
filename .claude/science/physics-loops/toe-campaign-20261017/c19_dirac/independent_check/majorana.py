"""N1 route: number-violating (Majorana) masses.  Pairing (1/2) sum Delta_ij c^dag_i c^dag_j + h.c. with
Delta[(n+sh,c2),(n,c1)] = e^{iP.n} d_sh[c2,c1], P in {0, Q}.  Invariance under the TWISTED site rotations
(c -> i^{w1} sigma c) means U Delta U^T = (-1)^{w1} Delta (A2 under the untwisted PSG); under the UNTWISTED
rotations U Delta U^T = Delta.  Node-space pairing block and BdG dispersion near k*."""
import itertools
import numpy as np
from core import *
from bases import get
from invspace import invariant_basis, shifts

rng = np.random.default_rng(9)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4; KM = np.array(fm[1]) * np.pi / 4
Xb = get('X_r1')
def rnd(bs, cplx=False):
    c = rng.normal(size=len(bs)) + (1j * rng.normal(size=len(bs)) if cplx else 0); m = addm(*bs, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
Hb = addm(hop(-1.0, 0.2), rnd(Xb), coeffs=[1, 0.05])
EN = np.linalg.eigvalsh(bloch(Hb, KS))[0]

def pair_basis(S, P, twisted):
    idx, b = invariant_basis(shifts(S), stag=(P == 'Q'), imag=True, chiA2=1 if twisted else 0, with_inv=False)
    out = []
    for v in b:
        m = {}
        for (sh, c2, c1), i in idx.items():
            if v[i]: m.setdefault(sh, np.zeros((12, 12), complex))[c2, c1] += v[i]
        out.append(m)
    return out

def Dk(d, P, k):
    Pv = Q if P == 'Q' else np.zeros(3)
    out = np.zeros((12, 12), complex)
    for sh, M in d.items(): out += M * np.exp(-1j * (Pv - k) @ np.array(sh))
    return out
def bdg(d, P, k, mu=EN, amp=1.0):
    Pv = Q if P == 'Q' else np.zeros(3)
    X = -amp * Dk(d, P, k).T
    A = bloch(Hb, k) - mu * np.eye(12); B = bloch(Hb, Pv - k) - mu * np.eye(12)
    return np.block([[A, X], [X.conj().T, -B.T]])

# ---- real-space L = 4 cross-check of the Bloch BdG
L = 4; SITES = list(itertools.product(range(L), repeat=3)); SI = {n: i for i, n in enumerate(SITES)}; NV = 12 * len(SITES)
def realspace(m, P):
    A = np.zeros((NV, NV), complex)
    for n in SITES:
        ph = (-1) ** (sum(n)) if P == 'Q' else 1
        for sh, Mx in m.items():
            t = tuple((a + b) % L for a, b in zip(n, sh))
            A[SI[t]*12:SI[t]*12+12, SI[n]*12:SI[n]*12+12] += ph * Mx
    return A

print(f"E_N = {EN:.6f}")
for P in ('0', 'Q'):
    for tw in (True, False):
        bs = pair_basis('r1', P, tw)
        d = rnd(bs, cplx=True)
        Dr = realspace(d, P)
        anti = np.allclose(Dr, -Dr.T)
        # real-space BdG vs Bloch BdG on the L = 4 grid
        Hr = realspace(Hb, '0') - EN * np.eye(NV)
        amp = 0.02
        HB = np.block([[Hr, amp * Dr], [amp * Dr.conj().T, -Hr.T]])
        er = np.sort(np.linalg.eigvalsh(HB))
        ks = [np.array(t) * 2 * np.pi / L for t in SITES]
        eb = np.sort(np.concatenate([np.linalg.eigvalsh(bdg(d, P, k, amp=amp)) for k in ks]))
        # node-space pairing block: particles at the 4 node states
        evh, Vh = np.linalg.eigh(Hr); nodeV = Vh[:, np.abs(evh) < 1e-8]
        Dn = nodeV.conj().T @ Dr @ nodeV.conj()
        sv = np.linalg.svd(Dn, compute_uv=False)
        # BdG near k*: min |E| on spheres of radius r around k* (and the node itself)
        mins = []
        for r in (0.0, 0.01, 0.03, 0.1):
            dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
            mins.append(min(np.abs(np.linalg.eigvalsh(bdg(d, P, KS + r * dd, amp=amp))).min() for dd in (dirs if r else dirs[:1])))
        # scan a small box for zero-energy points
        gg = np.linspace(-0.15, 0.15, 13)
        box = min(np.abs(np.linalg.eigvalsh(bdg(d, P, KS + np.array([x, y, z]), amp=amp))).min() for x in gg for y in gg for z in gg)
        print(f"P={P} {'twisted-invariant' if tw else 'untwisted-invariant'} pairing (range<=1): dim {len(bs)}; antisymmetric {anti};"
              f" Bloch BdG = real-space BdG on L=4: {np.allclose(er, eb, atol=1e-9)}")
        print(f"     node-space pairing singular values (per unit amplitude): {np.round(sv, 5)}")
        print(f"     BdG (amp {amp}) min|E| at k* and on spheres r=0.01,0.03,0.1: {np.round(mins, 6)}; min|E| in box |dk|_inf<=0.15: {box:.2e}")
# on-site only
for P in ('0', 'Q'):
    for tw in (True, False):
        bs = pair_basis('onsite', P, tw); print(f"  on-site pairing P={P} {'twisted' if tw else 'untwisted'}-invariant: dim {len(bs)}")
