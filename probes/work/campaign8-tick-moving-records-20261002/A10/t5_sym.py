"""t5: one-excitation symmetry of the cycles, Bloch form.
Rotation R about the cube centre c=(1/2,1/2,1/2) maps cell n -> R n and in-cell p -> R(p-c)+c.
Symmetry test: P_R U(K) P_R^T == Lam U_r(RK) Lam, with Lam a diagonal sign pattern (gauge dressing)
and U_r a cyclic shift of the layer list (schedule relabelling)."""
import numpy as np, itertools
from vcyc import layers_U, plain6, strang9

pi = np.pi
rng = np.random.default_rng(6)

# the 24 proper rotations as signed permutation matrices
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i in range(3):
            M[perm[i], i] = sg[i]
        if np.isclose(np.linalg.det(M), 1):
            rots.append(M)
assert len(rots) == 24

def axis_perm_parity(M):
    perm = [int(np.nonzero(M[:, i])[0][0]) for i in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
    return inv % 2

def P_of(M):
    P = np.zeros((8, 8))
    c = np.array([0.5, 0.5, 0.5])
    for p in itertools.product((0, 1), repeat=3):
        p = np.array(p)                           # (px,py,pz)
        q = np.rint(M @ (p - c) + c).astype(int)
        P[q[0] + 2 * q[1] + 4 * q[2], p[0] + 2 * p[1] + 4 * p[2]] = 1
    return P

lams = [np.diag(np.array([1] + list(s))) for s in itertools.product((1, -1), repeat=7)]

def test(lay, signed, nK=4):
    Ks = rng.uniform(-pi, pi, (nK, 3))
    shifts = [lay[r:] + lay[:r] for r in range(len(lay))]
    res = {}
    for M in rots:
        P = P_of(M)
        A = np.einsum("ij,njk,lk->nil", P, layers_U(Ks, lay, signed), P)
        RK = Ks @ M.T
        best = (np.inf, None, None)
        for r, sl in enumerate(shifts):
            B = layers_U(RK, sl, signed)
            for li, L in enumerate(lams):
                e = np.abs(A - L @ B @ L).max()
                if e < best[0]:
                    best = (e, r, li)
                if e < 1e-10:
                    break
            if best[0] < 1e-10:
                break
        res[tuple(M.flatten())] = (best, axis_perm_parity(M))
    return res

for name, lay, signed in [("plain-6", plain6(0.6), False), ("signed strang-9", strang9(0.6), True),
                          ("signed plain-6", plain6(0.6), True)]:
    res = test(lay, signed)
    ok_even = sum(1 for (b, par) in res.values() if par == 0 and b[0] < 1e-10)
    ok_odd = sum(1 for (b, par) in res.values() if par == 1 and b[0] < 1e-10)
    exact = sum(1 for (b, par) in res.values() if b[0] < 1e-10 and b[1] == 0 and b[2] == 0)
    worst_odd = min(b[0] for (b, par) in res.values() if par == 1)
    print(f"{name}: rotations symmetric (dressing+shift allowed): even-axis-perm {ok_even}/12, odd {ok_odd}/12; "
          f"exact (no dressing, no shift): {exact}/24; best residual among odd ones {worst_odd:.2e}")

# spectra: invariant under all 24 rotations and K -> -K?  (odd rotations map the cycle to its reverse)
lay = strang9(0.6)
Ks = rng.uniform(-pi, pi, (50, 3))
ph0 = np.sort(np.angle(np.linalg.eigvals(layers_U(Ks, lay, True))), axis=1)
dev = 0.0
for M in rots:
    ph = np.sort(np.angle(np.linalg.eigvals(layers_U(Ks @ M.T, lay, True))), axis=1)
    dev = max(dev, np.abs(ph - ph0).max())
print(f"signed strang-9: spectrum at RK vs K, max dev over 24 rotations, 50 K: {dev:.1e}")

# unit translation T_x in Bloch form (maps x-even <-> x-odd partner layers)
def Tx(K):
    T = np.zeros((8, 8), complex)
    for p in itertools.product((0, 1), repeat=3):
        i = p[0] + 2 * p[1] + 4 * p[2]
        if p[0] == 1:
            T[i, i - 1] = 1.0                      # (T psi)(s) = psi(s - e_x), same cell
        else:
            T[i, i + 1] = np.exp(-1j * K[0])       # from the p_x=1 site of the cell to the left
    return T
for name, lay, signed in [("plain-6", plain6(0.6), False), ("signed strang-9", strang9(0.6), True)]:
    best = np.inf
    for K in rng.uniform(-pi, pi, (3, 3)):
        T = Tx(K)
        A = T @ layers_U(K[None], lay, signed)[0] @ T.conj().T
        b = np.inf
        for r in range(len(lay)):
            sl = lay[r:] + lay[:r]
            for L in lams:
                b = min(b, np.abs(A - L @ layers_U(K[None], sl, signed)[0] @ L).max())
        worst = b if best == np.inf else max(best, b)
        best = worst
    print(f"{name}: unit translation e_x as (dressing + schedule shift) symmetry: worst residual {best:.2e}")
