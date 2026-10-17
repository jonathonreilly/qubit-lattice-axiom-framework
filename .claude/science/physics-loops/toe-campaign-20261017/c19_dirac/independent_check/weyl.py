"""Items 1-3 (Bloch level): covariance, fixed momenta, irreps at +-k*, Weyl pair for generic X,
selection rule for all ranges, A2 mass, Dirac dispersion fit."""
import itertools, sys
import numpy as np
from core import *
from bases import get

rng = np.random.default_rng(11)
print("gauge solved:", U is not None)
fm = fixed_momenta(); print("O-fixed momenta (units pi/4):", fm)
KS = np.array(fm[0]) * np.pi / 4; KM = np.array(fm[1]) * np.pi / 4
print("k* (mine) =", KS / (np.pi / 2), " -k* =", KM / (np.pi / 2), " k*+Q = -k* mod 2pi:",
      np.allclose(np.exp(1j * (KS + Q - KM)), 1), " -k* = -(k*) mod 2pi:", np.allclose(np.exp(1j * (KS + KM)), 1))

h0 = hop(-1.0, 0.2)
Xb = get('X_r1'); print("dim X space (range<=1, O x I x transl, conj-odd):", len(Xb))
def rndX():
    c = rng.normal(size=len(Xb)); m = addm(*Xb, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}

# covariance h(Rk + pi R s) = W h(k) W^T, inversion likewise
X0 = rndX(); H = addm(h0, X0, coeffs=[1, 0.05])
res = 0
for _ in range(5):
    k = rng.uniform(-np.pi, np.pi, 3)
    for R, (e, s), W in zip(ROTS, PSG, WR):
        res = max(res, np.abs(bloch(H, R @ k + np.pi * (R @ s)) - W @ bloch(H, k) @ W.T).max())
    eI, sI = PSGI
    res = max(res, np.abs(bloch(H, -k + np.pi * (INV @ sI)) - WI @ bloch(H, k) @ WI.T).max())
print(f"covariance residual (24 rotations + inversion, random k): {res:.1e}")
print("X conj-odd & Hermitian:", all(np.allclose(X0[sh], -X0[sh].conj()) for sh in X0),
      np.allclose(bloch(X0, [0.3, 0.1, -0.7]), bloch(X0, [0.3, 0.1, -0.7]).conj().T))
eI, sI = PSGI
print("inversion momentum shift pi*I s_I =", (INV @ sI) % 2, "(0 => I maps k -> -k)")

# ---- irreps of the 12-dim internal space at k* (twisted D = i^w1 W); both lifts
D = [(1j ** w) * W for w, W in zip(W1, WR)]
Ls = lift(D); print("number of 2O lifts found:", len(Ls))
for li, Lf in enumerate(Ls):
    chi = np.array([np.trace(Lf[g]) for g in range(48)])
    print(f"  lift {li}: 12-dim shell = {decomp(chi)}")
def doublet_label(V, Lf):
    chi = np.array([np.trace(V.conj().T @ Lf[g] @ V) for g in range(48)]); return decomp(chi)
def d2_comm(V):
    """commutator sign of the axis C2x, C2y about the site on subspace V (U(1)-gauge invariant)"""
    ix = rid(np.diag([1, -1, -1])); iy = rid(np.diag([-1, 1, -1]))
    a = V.conj().T @ D[ix] @ V; b = V.conj().T @ D[iy] @ V
    c = a @ b @ np.linalg.inv(a) @ np.linalg.inv(b)
    return np.round(c, 8)

def nodes(H):
    out = []
    for k in (KS, KM):
        e, V = np.linalg.eigh(bloch(H, k)); out.append((e, V))
    return out

def weyl_data(H, k, lev, ndir=20):
    """velocity of the 2-fold level starting at index lev, along random directions"""
    dirs = rng.normal(size=(ndir, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    vs = []
    for d in dirs:
        e1 = np.linalg.eigvalsh(bloch(H, k + 1e-5 * d)); vs.append((e1[lev + 1] - e1[lev]) / 2e-5)
    return np.array(vs)

def berry(H, k0, band, r=0.02, n=24):
    th = np.linspace(0, np.pi, n + 1); ph = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False)
    Uv = [[np.linalg.eigh(bloch(H, k0 + r * np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])))[1][:, band]
           for p in ph] for t in th]
    tot = 0
    for i in range(n):
        for j in range(2 * n):
            a, b, c, d = Uv[i][j], Uv[i+1][j], Uv[i+1][(j+1) % (2*n)], Uv[i][(j+1) % (2*n)]
            tot += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
    return tot / (2 * np.pi)

print("\n== Weyl pair: runner-like parameters (t1=-1, t2=0.2, delta=0.05) with several random X in the 9-dim space")
for trial in range(4):
    X = rndX(); H = addm(h0, X, coeffs=[1, 0.05]); (eK, VK), (eM, VM) = nodes(H)
    deg = (abs(eK[0] - eK[1]) < 1e-10, abs(eK[1] - eK[2]) > 1e-6, abs(eM[0] - eM[1]) < 1e-10, abs(eK[0] - eM[0]) < 1e-10)
    vK = weyl_data(H, KS, 0); vM = weyl_data(H, KM, 0)
    bK, bM = berry(H, KS, 0), berry(H, KM, 0)
    labs = [doublet_label(VK[:, :2], Ls[0]), doublet_label(VM[:, :2], Ls[0])]
    print(f"  X#{trial}: lowest at k*,-k* doublets/equal: {deg}; E_N={eK[0]:.6f}, next level +{eK[2]-eK[0]:.4f};"
          f" v(k*) = {vK.mean():.5f} spread {np.ptp(vK):.1e}; v(-k*) = {vM.mean():.5f}; Berry {bK:+.4f}, {bM:+.4f};"
          f" lift0 labels {labs}; D2 comm k*: {d2_comm(VK[:, :2])[0,0]:+.0f}")

print("\n== generic elements and strengths: t2 in [-0.6,0.6], delta in [0.01, 1.0], t1 = -1 and +1")
stat = {'lowest_doublet': 0, 'lowest_quartet': 0, 'n': 0, 'flux_ok': 0, 'iso_ok': 0, 'doublets_at_E1/2_E5/2': 0}
for trial in range(40):
    t1 = rng.choice([-1.0, 1.0]); t2 = rng.uniform(-0.6, 0.6); dl = 10 ** rng.uniform(-2, 0)
    X = rndX(); H = addm(hop(t1, t2), X, coeffs=[1, dl]); (eK, VK), (eM, VM) = nodes(H)
    stat['n'] += 1
    m0 = int(np.sum(np.abs(eK - eK[0]) < 1e-8))
    # find the two doublets at k* (E1/2 and E5/2 subspaces) wherever they are
    lv = []; i = 0
    while i < 12:
        j = i
        while j + 1 < 12 and abs(eK[j+1] - eK[i]) < 1e-8: j += 1
        lv.append((i, j - i + 1)); i = j + 1
    dbl = [l for l in lv if l[1] == 2]
    if len(dbl) == 2: stat['doublets_at_E1/2_E5/2'] += 1
    if m0 == 2: stat['lowest_doublet'] += 1
    elif m0 == 4: stat['lowest_quartet'] += 1
    ok_f = True; ok_i = True
    for (lev, _) in dbl:
        bk = berry(H, KS, lev, n=16); bm = berry(H, KM, lev, n=16)
        ok_f &= abs(abs(bk) - 1) < 1e-3 and abs(bk + bm) < 1e-3
        vv = weyl_data(H, KS, lev, 8); ok_i &= np.ptp(vv) < 1e-4 * max(abs(vv.mean()), 1e-12) or vv.mean() < 1e-8
    stat['flux_ok'] += ok_f; stat['iso_ok'] += ok_i
    if trial < 12:
        print(f"  t1={t1:+.0f} t2={t2:+.3f} delta={dl:.3f}: lowest level at k* is {m0}-fold; doublets at levels {[l[0] for l in dbl]};"
              f" Berry +-1 opposite at both doublets: {ok_f}; isotropic: {ok_i}")
print("  summary:", stat)
