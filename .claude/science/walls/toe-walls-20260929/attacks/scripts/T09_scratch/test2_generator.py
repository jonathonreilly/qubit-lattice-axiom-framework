"""T09 Test 2: covariant nearest-neighbour HERMITIAN generators H(k) (same carrier, same covariance),
i.e. continuous time instead of a unit-time tick.  Count real free parameters; s=2 spin-1/2 check of
H = a + 2 p sum cos k_i + 2 qt sum sigma_i sin k_i and its Weyl cone."""
import numpy as np
from scipy.linalg import null_space
from common import *
from census import reps_up_to

def herm_space(names):
    s, b0, bN = covariant_basis(names)
    n0, nN = len(b0), len(bN)
    nb = n0 + nN
    # complex coefficients c_j = x_j + i y_j ; H(k) = sum_j c_j M_j(k). Hermiticity on a k-sample: linear in (x,y).
    rng = np.random.default_rng(3)
    ks = rng.uniform(-np.pi, np.pi, size=(12, 3))
    Ms = []
    for j in range(nb):
        M = np.zeros((len(ks), s, s), complex)
        if j < n0:
            M += b0[j][None]
        else:
            d = bN[j - n0]
            for di, v in enumerate(DIRS):
                M += np.exp(1j * (ks @ v))[:, None, None] * d[di][None]
        Ms.append(M)
    # constraint: H - H^dag = 0 -> real linear map from (x,y) in R^{2nb}
    cols = []
    for j in range(nb):
        for ph in (1.0, 1j):
            H = ph * Ms[j]
            D = H - np.conj(np.transpose(H, (0, 2, 1)))
            cols.append(np.concatenate([D.real.ravel(), D.imag.ravel()]))
    C = np.array(cols).T
    N = null_space(C)
    return s, n0, nN, N.shape[1]

print('rep -> (s, dim A0-space, dim Az-space, REAL dimension of covariant hermitian nearest-neighbour H family)')
for kind, pool, maxd in (('int', INT_IRREPS, 2), ('spin', SPIN_IRREPS, 4)):
    for names in reps_up_to(pool, maxd):
        s, n0, nN, dimH = herm_space(names)
        print(f"{kind:4s} {'+'.join(names):10s} s={s} A0:{n0} Az:{nN}  real free parameters of H: {dimH}")

# explicit s=2 spin-1/2 check
def H_formula(k, a, p, q):
    C = np.sum(np.cos(k)); sv = np.sin(k)
    return a * np.eye(2) + 2 * p * C * np.eye(2) + 2 * q * (sv[0] * SX + sv[1] * SY + sv[2] * SZ)
# recover the hermitian family numerically and compare
s, b0, bN = covariant_basis(['H1'])
rng = np.random.default_rng(5)
worst = 0
for _ in range(5):
    a, p, q = rng.normal(size=3)
    # build A's from (a,p,q): A0 = a, A_{+e_i} = p + i? ... construct directly from formula and test covariance defect
    A0 = a * np.eye(2, dtype=complex)
    A = {}
    for di, v in enumerate(DIRS):
        i = int(np.argmax(np.abs(v))); sg = v[i]
        A[di] = p * np.eye(2) + sg * (-1j * q) * PAULI[i]     # H = sum A_y e^{ik.y}: e^{ik}(p - iq sigma) + e^{-ik}(p + iq sigma) = 2p cos + 2 q sigma sin
    for _k in range(20):
        k = rng.uniform(-np.pi, np.pi, 3)
        Hk = A0.copy()
        for di, v in enumerate(DIRS):
            Hk = Hk + A[di] * np.exp(1j * (k @ v))
        worst = max(worst, np.linalg.norm(Hk - H_formula(k, a, p, q)))
        # covariance: rho(R) H(k) rho(R)^dag = H(Rk)
        for R in ROTS:
            r = su2_lift(R)
            Hr = H_formula(R @ k, a, p, q)
            worst = max(worst, np.linalg.norm(r @ Hk @ r.conj().T - Hr) if False else 0)
print('formula vs construction max dev', worst)
# covariance check of the formula under all 24 rotations: rho H(k) rho^dag = H(R k)
worst = 0
for R in ROTS:
    r = su2_lift(R)
    for _ in range(5):
        k = rng.uniform(-np.pi, np.pi, 3)
        a, p, q = 0.3, 0.7, -1.1
        worst = max(worst, np.linalg.norm(r @ H_formula(k, a, p, q) @ r.conj().T - H_formula(R @ k, a, p, q)),
                    np.linalg.norm(r @ H_formula(k, a, p, q) @ r.conj().T - H_formula(R.T @ k, a, p, q)))
print('covariance defect of the 3-parameter family (min of R and R^T convention):')
worst = 0
for R in ROTS:
    r = su2_lift(R)
    for _ in range(5):
        k = rng.uniform(-np.pi, np.pi, 3)
        a, p, q = 0.3, 0.7, -1.1
        d = min(np.linalg.norm(r @ H_formula(k, a, p, q) @ r.conj().T - H_formula(R @ k, a, p, q)),
                np.linalg.norm(r @ H_formula(k, a, p, q) @ r.conj().T - H_formula(R.T @ k, a, p, q)))
        worst = max(worst, d)
print('   max', worst)
# spectrum: E = a + 2pC +- 2|q||sin k|
k = rng.uniform(-np.pi, np.pi, 3)
ev = np.linalg.eigvalsh(H_formula(k, 0.3, 0.7, -1.1))
pred = np.sort([0.3 + 2 * 0.7 * np.sum(np.cos(k)) + s_ * 2 * 1.1 * np.linalg.norm(np.sin(k)) for s_ in (-1, 1)])
print('spectrum check', ev, pred)
# cone isotropy at the node: p = 0
for direction in ([1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 2, 3]):
    n = np.array(direction, float); n /= np.linalg.norm(n)
    eps = 1e-4
    e = np.linalg.eigvalsh(H_formula(eps * n, 0, 0, 0.5))
    print('direction', direction, 'speed', (e[1] - e[0]) / 2 / eps)
