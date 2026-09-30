"""Test C: discrete-time (unitary, one tick) version. Full soldering; translation-invariant; NOT required to be
Hermitian. Is there a non-trivial covariant U(k) = C + sum_v A_v e^{ik.v} that is unitary for every k,
for nearest-neighbour support (6 hops) and for range |v|_inf <= 1 (26 hops)?"""
import numpy as np
from scipy.optimize import least_squares
from common import O, rho, su2_of_rotation, SIG, I2
from test_B_covariant import hop_set, hop_set_nn

rng = np.random.default_rng(7)
kind = "full"


def build_complex(V):
    keyv = lambda v: tuple(int(x) for x in v)
    nparam = 8 + 8 * len(V)

    def unpack(x):
        def m(y):
            return np.array([[y[0] + 1j * y[1], y[2] + 1j * y[3]], [y[4] + 1j * y[5], y[6] + 1j * y[7]]])
        C = m(x[:8]); A = {}
        for j, v in enumerate(V):
            A[keyv(v)] = m(x[8 + 8 * j: 16 + 8 * j])
        return C, A

    Us = [su2_of_rotation(rho(kind, g)) for g in O]

    def cons(x):
        C, A = unpack(x); res = []
        for i, g in enumerate(O):
            U = Us[i]
            D = C - U @ C @ U.conj().T; res += [D.real.flatten(), D.imag.flatten()]
            for v in V:
                D = A[keyv(g @ v)] - U @ A[keyv(v)] @ U.conj().T; res += [D.real.flatten(), D.imag.flatten()]
        return np.concatenate(res)

    M = np.array([cons(np.eye(nparam)[j]) for j in range(nparam)]).T
    u, sv, vt = np.linalg.svd(M)
    rank = int((sv > 1e-9).sum())
    null = vt[rank:]
    return null, unpack



def tables(null, unpack, ks):
    """M[j, n] = 2x2 matrix of null vector j at k_n ; dM[j] = d/dk_x at Gamma."""
    V_keys = None
    Ms = []; dMs = []
    for row in null:
        C, A = unpack(row)
        M = np.zeros((len(ks), 2, 2), complex) + C
        dM = np.zeros((2, 2), complex)
        for v, Mv in A.items():
            ph = np.exp(1j * ks @ np.array(v, float))
            M = M + ph[:, None, None] * Mv
            dM = dM + 1j * v[0] * Mv
        Ms.append(M); dMs.append(dM)
    return np.array(Ms), np.array(dMs)


for label, V in (("NN (6 hops)", hop_set_nn()), ("range 1 (26 hops)", hop_set(1))):
    null, unpack = build_complex(V)
    print(f"\n{label}: covariant (not necessarily Hermitian) space, real dimension {len(null)}")
    ks = rng.uniform(-np.pi, np.pi, size=(150, 3))
    Ms, dMs = tables(null, unpack, ks)
    def defect(w):
        U = np.einsum('j,jnab->nab', w, Ms)
        D = np.einsum('nba,nbc->nac', U.conj(), U) - np.eye(2)
        return np.concatenate([D.real.flatten(), D.imag.flatten()])
    def spd(w):
        return np.linalg.norm(np.einsum('j,jab->ab', w, dMs))
    for target in (0.05, 0.15, 0.3, 0.6):
        best = 1e9
        for trial in range(60):
            w0 = rng.normal(size=len(null)) * 0.3
            fun = lambda w: np.concatenate([defect(w), [10 * (spd(w) - target)]])
            r = least_squares(fun, w0, method="trf", xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=600)
            d = np.linalg.norm(defect(r.x))
            if d < best and abs(spd(r.x) - target) < 1e-3:
                best = d
        print(f"   required tick-velocity |dU/dk_x| at Gamma = {target:4.2f}: best unitarity defect (2-norm over 150 k) = {best:.3e}")
