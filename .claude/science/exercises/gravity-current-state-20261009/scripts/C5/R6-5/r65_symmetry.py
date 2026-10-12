"""R6-5 (a)/(d): symmetry bookkeeping for the explicit Wilson-Dirac law with an on-site b*gamma5 term.

Law (Z^3 x R, continuous time, one 4-component fermion per site, NN hopping + on-site):
    h(k) = sum_j alpha_j sin k_j + beta*(m + r*sum_j(1-cos k_j)) + b*gamma5
Checks (numerically, at random k):
  1. covariance under all 24 proper cubic rotations (spinor double cover), for b != 0;
  2. behaviour of each term under inversion P (unitary), time reversal T (antiunitary),
     particle-hole C (antiunitary single-particle map) and the composite CPT;
     the unitaries are FOUND by solving the intertwining equations on the b=0 law,
     not assumed;
  3. the same for the qubit-per-site (2-component) naive Weyl law
        h2(k) = sigma.sin k + t3*cos k1 cos k2 cos k3
     and its taste-singlet node-energy offset.
"""
import itertools
import numpy as np

rng = np.random.default_rng(1)
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
sig = [sx, sy, sz]
Z2 = np.zeros((2, 2))
beta = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in sig]
g5 = np.block([[Z2, s0], [s0, Z2]]).astype(complex)
Sig = [np.block([[s, Z2], [Z2, s]]) for s in sig]


def h4(k, m=0.3, r=1.0, b=0.0):
    k = np.asarray(k)
    H = sum(alpha[j] * np.sin(k[j]) for j in range(3))
    H = H + beta * (m + r * np.sum(1 - np.cos(k))) + b * g5
    return H


def h2(k, t3=0.0):
    k = np.asarray(k)
    return sum(sig[j] * np.sin(k[j]) for j in range(3)) + t3 * np.prod(np.cos(k)) * s0


# --- proper cubic rotations: signed permutation matrices with det +1
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)
assert len(rots) == 24


def spin_lift(R, gens):
    """spinor rep exp(-i theta n.S/2) for rotation R, with generators gens (list of 3 matrices)."""
    from scipy.linalg import expm, logm
    # axis-angle from R
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(th, 0):
        return np.eye(gens[0].shape[0], dtype=complex)
    if np.isclose(th, np.pi):
        # axis = eigenvector with eigenvalue 1
        w, v = np.linalg.eig(R)
        n = np.real(v[:, np.argmin(abs(w - 1))]); n = n / np.linalg.norm(n)
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    G = sum(n[i] * gens[i] for i in range(3))
    return expm(-1j * th * G / 2)


def max_cov_err(hfun, gens, nk=20, **kw):
    err = 0.0
    for R in rots:
        S = spin_lift(R, gens)
        for _ in range(nk):
            k = rng.uniform(-np.pi, np.pi, 3)
            err = max(err, np.abs(S @ hfun(k, **kw) @ S.conj().T - hfun(R @ k, **kw)).max())
    return err


print("1. proper-cubic covariance (24 rotations, spinor lift):")
print("   Wilson-Dirac b=0.4 : max |S h(k) S^+ - h(Rk)| = %.2e" % max_cov_err(h4, Sig, b=0.4))
print("   naive Weyl t3=0.3  : max |S h(k) S^+ - h(Rk)| = %.2e" % max_cov_err(h2, sig, t3=0.3))


# --- find intertwiners for the b=0 law: unitary U with U X(k) U^+ = s * Y(k) for all k
def solve_intertwiner(Xs, Ys, s, dim):
    """solve U X = s Y U for all pairs (linear in U); return null-space basis."""
    rows = []
    I = np.eye(dim)
    for X, Y in zip(Xs, Ys):
        # vec(U X) = (X^T kron I) vec U ; vec(Y U) = (I kron Y) vec U   (column-major vec)
        rows.append(np.kron(X.T, I) - s * np.kron(I, Y))
    A = np.vstack(rows)
    u, sv, vh = np.linalg.svd(A)
    null = vh[np.abs(sv) < 1e-9] if len(sv) == vh.shape[0] else vh[len(sv[sv > 1e-9]):]
    return [v.reshape(dim, dim, order='F') for v in null.conj()]


ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]


def report_ops(hfun, dim, term, name, **kw0):
    out = {}
    # P: U h(-k) U^+ = h(k)    (unitary, k -> -k)
    # T: U h(-k)* U^+ = h(k)   (antiunitary)
    # C: U h(-k)* U^+ = -h(k)  (antiunitary particle-hole map on one-particle h)
    for op, (conj, sgn) in {'P': (False, 1), 'T': (True, 1), 'C': (True, -1)}.items():
        Xs = [(hfun(-k, **kw0).conj() if conj else hfun(-k, **kw0)) for k in ks]
        Ys = [hfun(k, **kw0) for k in ks]
        basis = solve_intertwiner(Xs, Ys, sgn, dim)
        if not basis:
            out[op] = None
            continue
        U = basis[0]
        U = U / np.sqrt(abs(np.trace(U @ U.conj().T)) / dim)
        M = term.conj() if conj else term
        img = sgn * U @ M @ U.conj().T  # image of the term under the map
        if np.allclose(img, term, atol=1e-8):
            out[op] = '+1 (even)'
        elif np.allclose(img, -term, atol=1e-8):
            out[op] = '-1 (odd)'
        else:
            out[op] = 'mixed'
        out[op] += ' [solution-space dim %d]' % len(basis)
    print("   %s:" % name, out)
    return out


print("2. discrete maps found as intertwiners of the b=0 law; parity of the added term:")
o4 = report_ops(h4, 4, g5, "Wilson-Dirac, term gamma5 (b0)", m=0.3, r=1.0, b=0.0)
print("   CPT parity of b-term = product of P,T,C parities")
o2 = report_ops(h2, 2, np.eye(2, dtype=complex), "naive Weyl, scalar term (t3 cos.cos.cos multiplies 1)", t3=0.0)
print("   note: for the naive Weyl law the scalar function multiplying 1 matters, see 3.")

# --- 3. node energies of the qubit-per-site naive Weyl law
print("3. naive Weyl h2 = sigma.sin k + t3 c1c2c3, t3=0.3: Weyl nodes at the 8 BZ corners")
tot = 0.0
for n in itertools.product([0, 1], repeat=3):
    K = np.pi * np.array(n)
    chi = int(np.sign(np.prod(np.cos(K))))  # chirality = sign det(dv/dk) = prod cos K_j
    E = 0.3 * np.prod(np.cos(K))
    tot += chi * E
    print("   corner", n, "chirality %+d  node energy %+.3f" % (chi, E))
print("   taste-singlet offset (1/8) sum_A chi_A E_A = %.4f  (= t3: all R nodes at +t3, all L at -t3)" % (tot / 8))
for name, f in [("t1*sum cos", lambda K: 0.3 * np.sum(np.cos(K))), ("t2*sum_{i<j} cos cos", lambda K: 0.3 * (np.cos(K[0]) * np.cos(K[1]) + np.cos(K[1]) * np.cos(K[2]) + np.cos(K[0]) * np.cos(K[2])))]:
    s = sum(int(np.sign(np.prod(np.cos(np.pi * np.array(n))))) * f(np.pi * np.array(n)) for n in itertools.product([0, 1], repeat=3))
    print("   control %-22s: (1/8) sum chi E = %.4f" % (name, s / 8))

# --- 4. direct one-particle CPT map: unitary U with U h(-k + Q) U^+ = -h(k)  (P,T,C each flip k; two conjugations cancel)
print("4. one-particle CPT as a unitary U h(-k+Q) U^+ = -h(k), found on the term-free law; image of the added term")
def cpt_check(hfun, dim, term, termfun, name, Q=np.zeros(3), **kw0):
    Xs = [hfun(-k + Q, **kw0) for k in ks]; Ys = [hfun(k, **kw0) for k in ks]
    basis = solve_intertwiner(Xs, Ys, -1, dim)
    if not basis:
        print("   %-40s Q=%s : no CPT intertwiner" % (name, Q)); return
    U = basis[0]; U = U / np.sqrt(abs(np.trace(U @ U.conj().T)) / dim)
    # term enters as termfun(k)*term ; image at k: -U termfun(-k+Q) term U^+ ; compare with +termfun(k) term
    k = rng.uniform(-np.pi, np.pi, 3)
    img = -termfun(-k + Q) * (U @ term @ U.conj().T); orig = termfun(k) * term
    par = '+1 (allowed)' if np.allclose(img, orig) else ('-1 (CPT-odd, forbidden)' if np.allclose(img, -orig) else 'mixed')
    print("   %-40s Q=%s : CPT parity of term %s [dim %d]" % (name, Q, par, len(basis)))
cpt_check(h4, 4, g5, lambda k: 1.0, "Wilson-Dirac, b*gamma5", m=0.3, r=1.0, b=0.0)
cpt_check(h2, 2, np.eye(2, dtype=complex), lambda k: np.prod(np.cos(k)), "naive Weyl, t3 c1c2c3", t3=0.0)
cpt_check(h2, 2, np.eye(2, dtype=complex), lambda k: np.prod(np.cos(k)), "naive Weyl, t3 c1c2c3", Q=np.pi*np.ones(3), t3=0.0)
cpt_check(h2, 2, np.eye(2, dtype=complex), lambda k: np.sum(np.cos(k)), "naive Weyl, t1 sum cos", t3=0.0)
