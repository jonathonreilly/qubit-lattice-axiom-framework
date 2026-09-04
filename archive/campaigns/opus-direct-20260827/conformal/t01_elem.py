"""T01 - element sanity: flat config must give V=1/24, lumped mass 1/vertex,
and the assembled stencil must be the NN hypercubic Laplacian (+8, -1 x8).
Also validate analytic dV, dloc against complex-step differentiation."""
import numpy as np, itertools, sys
sys.path.insert(0, ".")
from bridge_core import *

L = 6
S = edge_s(L, 0.0, 1, [0,0,0,0])
SS = simplex_s(S, L)                    # (24,L,10)
V, loc, dV, dloc = element(SS)
print("T01 flat:  V per simplex =", np.unique(np.round(V, 14)), " (exact 1/24 =", 1/24, ")")

# lumped mass at a vertex: sum over all incident simplices of V/5
Mv = np.zeros(L)
for p in range(24):
    for i in range(NC):
        np.add.at(Mv, (np.arange(L) + CORN[p][i][0]) % L, V[p]/5.0)
print("T01 flat:  lumped mass per vertex =", np.unique(np.round(Mv, 13)))

# stencil: K_{x, x+delta} for offsets delta
sten = {}
for p in range(24):
    for i in range(NC):
        for j in range(NC):
            dlt = tuple(CORN[p][j] - CORN[p][i])
            sten[dlt] = sten.get(dlt, 0.0) + loc[p, 0, i, j]   # x0b arbitrary (flat)
print("T01 flat stencil (nonzero offsets):")
for o in sorted(sten, key=lambda o: (sum(abs(x) for x in o), o)):
    if abs(sten[o]) > 1e-12:
        print(f"      {str(o):>16} : {sten[o]:+.12f}")

# --- complex-step validation of dV, dloc on a RANDOM (curved) element
rng = np.random.default_rng(0)
ss0 = np.array([2.0,3.0,4.0,1.0, 2.0,3.0,1.0, 2.0,1.0, 1.0])   # a generic Kuhn-like set
ss0 = simplex_s(edge_s(L, 0.07, 1, [0.3,1.0,-1.0,0.5]), L)[7, 3]
V0, loc0, dV0, dloc0 = element(ss0[None])
h = 1e-20
errV, errL = 0.0, 0.0
for k in range(10):
    ssc = ss0.astype(complex).copy(); ssc[k] += 1j*h
    G = gram(ssc[None]); Gi = np.linalg.inv(G); det = np.linalg.det(G)
    Vc = np.sqrt(det)/24.0
    lc = np.zeros((1,NC,NC), dtype=complex)
    lc[:,1:,1:] = Vc[...,None,None]*Gi
    lc[:,0,1:] = -lc[:,1:,1:].sum(axis=-2); lc[:,1:,0] = lc[:,0,1:]
    lc[:,0,0] = -lc[:,0,1:].sum(axis=-1)
    errV = max(errV, abs(Vc.imag[0]/h - dV0[0,k])/abs(dV0[0,k]))
    den = np.abs(dloc0[0,k]).max()
    errL = max(errL, np.abs(lc.imag[0]/h - dloc0[0,k]).max()/den)
print(f"T01 complex-step check:  max rel err dV = {errV:.3e},  dloc = {errL:.3e}")
print(f"T01 row sums of dloc (must vanish): {np.abs(dloc0.sum(axis=-1)).max():.3e}")
