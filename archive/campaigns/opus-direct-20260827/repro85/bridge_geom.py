"""bridge_geom.py -- reduced (x0-only) geometry: Vol, S_Regge and their exact
gradients w.r.t. the reduced variables S[c,x0] (= squared length of every edge of
class c whose base vertex sits at x0-coordinate x0).  Valid whenever the
configuration is invariant under translations in directions 1,2,3."""
import numpy as np, itertools
from bridge_core import *

# ---- triangle (hinge) classes ------------------------------------------------
TRIP = [t for t in itertools.combinations(range(NC), 3)]          # 10 corner triples
_keys, TKEY = {}, []
TC   = np.zeros((24, 10), dtype=np.int64)      # (type p, triple index) -> triangle class
TCX  = np.zeros((24, 10), dtype=np.int64)      # x0 offset of the triangle base inside the simplex
TCEX = np.zeros((24, 10, 2), dtype=np.int64)   # excluded corner pair (for the dihedral angle)
for p in range(24):
    for m, (i, j, k) in enumerate(TRIP):
        a = CORN[p]
        key = (tuple(a[j]-a[i]), tuple(a[k]-a[i]))   # GLOBAL class: base x0 is tracked separately
        if key not in _keys:
            _keys[key] = len(TKEY); TKEY.append(key)
        TC[p, m]  = _keys[key]
        TCX[p, m] = a[i][0]
        TCEX[p, m] = [x for x in range(NC) if x not in (i, j, k)]
NT = len(TKEY)
# per triangle class: the 3 edge (class, x0-offset) pairs, in order (ij, ik, jk)
TEC = np.zeros((NT, 3), dtype=np.int64); TEX = np.zeros((NT, 3), dtype=np.int64)
for t, (u, w) in enumerate(TKEY):
    u = np.array(u); w = np.array(w)
    TEC[t] = [ECIDX[tuple(u)], ECIDX[tuple(w)], ECIDX[tuple(w-u)]]
    TEX[t] = [0, 0, int(u[0])]                # base of edge jk is at +u0 from the triangle base

def geometry(S, L):
    """S[15,L] -> dict with V, loc, dV, dloc, Mv, areas, deficits and the reduced
    gradients dVol[c,x0], dReg[c,x0]."""
    SS = simplex_s(S, L)                                    # (24,L,10)
    V, loc, dV, dloc = element(SS)
    # lumped mass per vertex, by x0
    Mv = np.zeros(L)
    x0b = np.arange(L)
    for p in range(24):
        for i in range(NC):
            np.add.at(Mv, (x0b + CORN[p][i][0]) % L, V[p]/5.0)
    # --- volume gradient
    dVol = np.zeros((NE, L))
    for p in range(24):
        for k in range(10):
            np.add.at(dVol, (SEC[p, k], (x0b + SEX[p, k]) % L), dV[p, :, k])
    # --- triangle areas and their gradients
    TS = S[TEC[:, None, :], (x0b[None, :, None] + TEX[:, None, :]) % L]   # (NT,L,3)
    sab, sac, sbc = TS[..., 0], TS[..., 1], TS[..., 2]
    A = heron(sab, sac, sbc)
    dA = np.stack([(sac + sbc - sab), (sab + sbc - sac), (sab + sac - sbc)], -1) / (16.0*A[..., None])
    # --- deficits
    theta = np.zeros((NT, L))
    for p in range(24):
        for m in range(10):
            r, s = TCEX[p, m]
            c = -loc[p, :, r, s] / np.sqrt(loc[p, :, r, r]*loc[p, :, s, s])
            np.add.at(theta, (TC[p, m], (x0b + TCX[p, m]) % L), np.arccos(np.clip(c, -1, 1)))
    dfc = 2.0*np.pi - theta
    # --- Regge gradient
    dReg = np.zeros((NE, L))
    for t in range(NT):
        for e in range(3):
            np.add.at(dReg, (TEC[t, e], (x0b + TEX[t, e]) % L), dfc[t]*dA[t, :, e])
    return dict(V=V, loc=loc, dV=dV, dloc=dloc, Mv=Mv, A=A, dfc=dfc,
                dVol=dVol, dReg=dReg,
                Vol=float(V.sum())*L**3, Reg=float((A*dfc).sum())*L**3, SS=SS)
