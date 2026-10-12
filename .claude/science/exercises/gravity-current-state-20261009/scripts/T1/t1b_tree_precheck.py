"""T1 part (b) PRE-CHECK (tree level only; the one-loop part was not run, see report).
3D Poisson points (density 1) in a periodic box, periodic Delaunay complex, circumcentric (Voronoi-dual) weights
w_e = A_e/l_e (A_e = signed Voronoi face area), Voronoi volumes V_i = sum_{e ni i} A_e l_e / 6.
Periodic-Delaunay and circumcentric-area code follow R1's scripts R1_B_liquid_glass_crystal.py and
R1_D_3d_circumcentric.py (copied logic, not imported).

Checks:
  I1  sum_i V_i = box volume                                (exact identity)
  I2  sum_j w_ij e_ij = 0 at every site                    (closed Voronoi cell: sum_f A_f n_f = 0)
  I3  sum_e w_e e_e e_e^T = V_tot * Identity                (divergence theorem, summed over cells)
  I4  per-site tensor tau_i = 1/2 sum_j w_ij e e^T - V_i I  (NOT zero; the per-site defect)
  S   scalar  L_p u = w^2 V u : lowest Bloch band w(p)/|p| -> 1 per configuration (since L(k.x) = 0 exactly)
  F   fermion H_p = sum_e (-i/2) w_e alpha.e e^{ip.e} + h.c. + beta (r/2) L_p  (Hermitian, nearest neighbour,
      Wilson r = 1): lowest positive Bloch levels E(p)/|p| per configuration and direction.
"""
import numpy as np, sys, time
from scipy.spatial import Delaunay
from itertools import product

def periodic_delaunay(Y, A):
    N, d = Y.shape
    shifts = np.array(list(product((-1, 0, 1), repeat=d)))
    P = np.concatenate([Y + s @ A for s in shifts])
    idx = np.tile(np.arange(N), len(shifts)); off = np.repeat(shifts, N, axis=0)
    tri = Delaunay(P, qhull_options="Qbb Qc Qz Q12").simplices
    frac = P[tri].mean(axis=1) @ np.linalg.inv(A)
    keep = np.all((frac >= 0) & (frac < 1), axis=1)
    return idx[tri[keep]], off[tri[keep]]

EVEN = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 2, 0), (2, 3, 0, 1)]

def tri_cc(a, b, c):
    u, v = b - a, c - a; w = np.cross(u, v)
    return a + (np.einsum("ti,ti->t", u, u)[:, None] * np.cross(v, w) + np.einsum("ti,ti->t", v, v)[:, None] * np.cross(w, u)) / (2 * np.einsum("ti,ti->t", w, w)[:, None])

def tet_cc(p):
    a = p[:, 0]; B = p[:, 1:] - a[:, None, :]
    rhs = 0.5 * np.einsum("tki,tki->tk", B, B)
    return a + np.linalg.solve(B, rhs[..., None])[..., 0]

def edges_circumcentric(X, A, vid, voff):
    """Return dict (i, j, offset_j - offset_i) -> signed dual area A_e (i<j canonical), plus edge vectors."""
    pos = X[vid] + np.einsum("tvk,kl->tvl", voff, A)
    D = pos[:, 1:] - pos[:, :1]
    flip = np.linalg.det(D) < 0
    vid = vid.copy(); pos = pos.copy(); voff = voff.copy()
    for arr in (vid, pos, voff):
        tmp = arr[flip, 0].copy(); arr[flip, 0] = arr[flip, 1]; arr[flip, 1] = tmp
    cT = tet_cc(pos)
    acc = {}
    for (i, j, k, l) in EVEN:
        xi, xj, xk, xl = pos[:, i], pos[:, j], pos[:, k], pos[:, l]
        e = xj - xi; le = np.linalg.norm(e, axis=1); n = e / le[:, None]; mpt = 0.5 * (xi + xj)
        P = [mpt, tri_cc(xi, xj, xk), cT, tri_cc(xi, xj, xl)]
        area = sum(0.5 * np.einsum("ti,ti->t", n, np.cross(P[a] - mpt, P[(a + 1) % 4] - mpt)) for a in range(4))
        for t in range(len(area)):
            a_, b_ = vid[t, i], vid[t, j]; o = tuple(voff[t, j] - voff[t, i])
            if (a_, b_) > (b_, a_) or (a_ == b_ and o < tuple(-np.array(o))):
                a_, b_, o = b_, a_, tuple(-np.array(o))
            key = (a_, b_, o); acc[key] = acc.get(key, 0.0) + area[t]
    I = np.array([k[0] for k in acc]); J = np.array([k[1] for k in acc]); O = np.array([k[2] for k in acc], float)
    Ae = np.array(list(acc.values()))
    E = X[J] + O @ A - X[I]
    return I, J, E, Ae

alpha = None
def dirac_mats():
    s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    Z = np.zeros((2, 2)); I2 = np.eye(2)
    al = [np.block([[Z, x], [x, Z]]) for x in s]
    be = np.block([[I2, Z], [Z, -I2]]).astype(complex)
    return al, be

def bloch_L(N, I, J, E, w, p):
    Lp = np.zeros((N, N), complex)
    ph = np.exp(1j * E @ p)
    np.add.at(Lp, (I, I), w); np.add.at(Lp, (J, J), w)
    np.add.at(Lp, (I, J), -w * ph); np.add.at(Lp, (J, I), -w * np.conj(ph))
    return Lp

def bloch_H(N, I, J, E, w, p, r=1.0):
    al, be = dirac_mats()
    H = np.zeros((N, 4, N, 4), complex)
    ph = np.exp(1j * E @ p)
    for e in range(len(w)):
        blk = (-0.5j) * w[e] * sum(E[e, a] * al[a] for a in range(3)) * ph[e]
        H[I[e], :, J[e], :] += blk; H[J[e], :, I[e], :] += blk.conj().T
    Lp = bloch_L(N, I, J, E, w, p)
    H += 0.5 * r * Lp[:, None, :, None] * be[None, :, None, :]
    return H.reshape(4 * N, 4 * N)

if __name__ == "__main__":
    N = int(sys.argv[1]); R = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    rng = np.random.default_rng(seed); Lb = N ** (1 / 3); A = Lb * np.eye(3)
    allS, allF = [], []
    for rep in range(R):
        t0 = time.time()
        X = rng.uniform(0, Lb, (N, 3)); vid, voff = periodic_delaunay(X, A)
        I, J, E, Ae = edges_circumcentric(X, A, vid, voff)
        le = np.linalg.norm(E, axis=1); w = Ae / le
        V = np.zeros(N); np.add.at(V, I, Ae * le / 6); np.add.at(V, J, Ae * le / 6)
        F = np.zeros((N, 3)); np.add.at(F, I, w[:, None] * E); np.add.at(F, J, -w[:, None] * E)
        T = np.einsum("e,ea,eb->ab", w, E, E)
        Ts = np.zeros((N, 3, 3)); np.add.at(Ts, I, 0.5 * w[:, None, None] * np.einsum("ea,eb->eab", E, E))
        np.add.at(Ts, J, 0.5 * w[:, None, None] * np.einsum("ea,eb->eab", E, E))
        tau = Ts - V[:, None, None] * np.eye(3)
        Vm = 1 / np.sqrt(V)
        rowS, rowF = [], []
        for d in range(3):
            for pm in (0.01, 0.02):
                p = np.zeros(3); p[d] = pm
                Lp = bloch_L(N, I, J, E, w, p)
                om2 = np.linalg.eigvalsh(Vm[:, None] * Lp * Vm[None, :])[0]
                Hp = bloch_H(N, I, J, E, w, p)
                Vm4 = np.repeat(Vm, 4)
                ev = np.linalg.eigvalsh(Vm4[:, None] * Hp * Vm4[None, :])
                pos = np.sort(ev[ev > 0])[:2]
                rowS.append(np.sqrt(om2) / pm); rowF.append(pos / pm)
        # spurious low modes of the fermion at p = 0
        H0 = bloch_H(N, I, J, E, w, np.zeros(3)); Vm4 = np.repeat(Vm, 4)
        ev0 = np.abs(np.linalg.eigvalsh(Vm4[:, None] * H0 * Vm4[None, :]))
        nlow = int((ev0 < 0.3).sum())
        rowS = np.array(rowS).reshape(3, 2); rowF = np.array(rowF).reshape(3, 2, 2)
        allS.append(rowS); allF.append(rowF)
        print(f"cfg {rep}: N={N} edges={len(w)} neg-weights={int((w<0).sum())} | I1 sumV/L^3-1={V.sum()/Lb**3-1:+.1e}"
              f" I2 max|sum w e|={np.abs(F).max():.1e} I3 max|T/V-I|={np.abs(T/V.sum()-np.eye(3)).max():.1e}"
              f" I4 rms|tau_i|/V={np.sqrt((tau**2).sum((1,2))/V**2).mean():.3f}", flush=True)
        print(f"   scalar w/|p| (x,y,z; p=.01,.02): {np.round(rowS,6).tolist()}")
        print(f"   fermion E/|p| two lowest (x,y,z; p=.01): {np.round(rowF[:,0,:],7).tolist()}  (p=.02): {np.round(rowF[:,1,:],7).tolist()}"
              f"  | #|E0|<0.3 at p=0: {nlow} (4 exact zero modes expected)  [{time.time()-t0:.0f}s]", flush=True)
    S = np.array(allS); Fm = np.array(allF)
    cF = Fm[:, :, 0, :].mean(-1)   # p = 0.01, average of the two lowest levels, per config x direction
    print(f"SUMMARY N={N} R={R}: scalar c_tree mean {S[:,:,0].mean():.6f} max|c-1| {np.abs(S[:,:,0]-1).max():.1e}")
    print(f"  fermion c_tree: law mean {cF.mean():.7f}; per-config (direction-avg) sd {cF.mean(1).std(ddof=1):.1e};"
          f" within-config direction spread (rms) {np.sqrt(((cF - cF.mean(1, keepdims=True))**2).mean()):.1e};"
          f" level splitting (p=.01) mean {np.abs(Fm[:,:,0,1]-Fm[:,:,0,0]).mean():.1e}")
