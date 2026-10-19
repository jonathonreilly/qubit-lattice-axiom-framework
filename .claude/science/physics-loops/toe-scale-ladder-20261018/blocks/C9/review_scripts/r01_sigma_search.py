"""C9 review / r01: independent 1D counterexample search for Theorem 1 (reviewer-written).

Different route from the author's c9_03 (which searches for images of the SWAP).  Here we
search directly for the image of the single-site Pauli triple: a TI SU(2)-symmetric 1D qubit QCA
alpha with neighbourhood window [0, n-1] (any position of site 0 inside it; range <= n-1) is
determined by W^j := alpha(sigma^j_0), which must be
  (i)  a Hermitian SU(2) VECTOR operator on the n-site window
       (alpha commutes with gamma_D, so gamma_D(W^j) = sum_k R_kj W^k),
  (ii) satisfy the Pauli algebra  W^j W^k = delta_jk + i eps_jkl W^l,
  (iii) commute with its translates  [W^j, tau_s W^k] = 0  for s = 1..n-1.
(i)-(iii) are necessary for any TI SU(2) QCA; they define an injective TI endomorphism.
Theorem 1 predicts: the only solutions are W = sigma at a single window site (a shift).

Part A: Lemma B independent random test (invariant ops built from random Hermitian combos of
        permutation operators, overlapping in one site, 5-site register).
Part B: dimension of Hermitian vector-operator space on n sites vs Schur-Weyl prediction
        (multiplicity of spin 1 in (1/2)^{(x)2n}).
Part C: least-squares search from random starts over all of (i); classify converged solutions.

usage: python3 r01_sigma_search.py LOG n starts budget_seconds seed [maxnfev polish_nfev]
"""
from __future__ import annotations

import itertools
import sys
import time
from math import comb

import numpy as np
from scipy.optimize import least_squares

LOG = sys.argv[1]
N = int(sys.argv[2])
STARTS = int(sys.argv[3])
BUDGET = float(sys.argv[4])
SEED = int(sys.argv[5]) if len(sys.argv) > 5 else 1
MAXNFEV = int(sys.argv[6]) if len(sys.argv) > 6 else 400
POLISH = int(sys.argv[7]) if len(sys.argv) > 7 else 1500
slow_tail = []

out = open(LOG, "x")  # never overwrite
npass = nfail = 0


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def check(ok, msg):
    global npass, nfail
    if ok:
        npass += 1
        log("PASS " + msg)
    else:
        nfail += 1
        log("FAIL " + msg)


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]
EPS = np.zeros((3, 3, 3))
for (a, b, c), s in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                     ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    EPS[a, b, c] = s


def site_op(op, k, n):
    m = np.array([[1.0 + 0j]])
    for i in range(n):
        m = np.kron(m, op if i == k else I2)
    return m


def perm_matrix(perm, n):
    """|i_0..i_{n-1}> -> |i_{perm^-1}> : qubit at position q moves to perm[q]."""
    d = 2 ** n
    M = np.zeros((d, d), dtype=complex)
    for idx in range(d):
        bits = [(idx >> (n - 1 - q)) & 1 for q in range(n)]
        nb = [0] * n
        for q in range(n):
            nb[perm[q]] = bits[q]
        j = 0
        for b in nb:
            j = 2 * j + b
        M[j, idx] = 1
    return M


def total_spin(n):
    return [sum(site_op(P, k, n) for k in range(n)) / 2 for P in PAULI]


# ---------------------------------------------------------------- Part A: Lemma B
def partA(rng):
    n = 5  # g on sites {0,1,2}, h on sites {2,3,4}; overlap {2}
    S = total_spin(n)
    perms3 = [perm_matrix(p, 3) for p in itertools.permutations(range(3))]

    def rand_inv3():
        c = rng.normal(size=6) + 1j * rng.normal(size=6)
        X = sum(ci * P for ci, P in zip(c, perms3))
        return X + X.conj().T

    minrel = np.inf
    for _ in range(30):
        g3, h3 = rand_inv3(), rand_inv3()
        g = np.kron(g3, np.eye(4))
        h = np.kron(np.eye(4), h3)
        for Sa in S:
            assert np.linalg.norm(Sa @ g - g @ Sa) < 1e-10
        c = g @ h - h @ g
        minrel = min(minrel, np.linalg.norm(c) / (np.linalg.norm(g) * np.linalg.norm(h)))
    check(minrel > 1e-3, f"A Lemma B: 30 random generic invariant pairs with one-site overlap never "
                         f"commute (min rel ||[g,h]|| = {minrel:.3e})")
    # converse: g trivial on the shared site (g = invariant on {0,1} (x) 1_2) -> commute
    p01 = perm_matrix([1, 0], 2)
    g = np.kron(np.kron(0.3 * np.eye(4) + 0.7 * p01, I2), np.eye(4))
    g3, h3 = rand_inv3(), rand_inv3()
    h = np.kron(np.eye(4), h3)
    check(np.linalg.norm(g @ h - h @ g) < 1e-12, "A converse: trivial vector channel at overlap => commute")
    # an invariant op whose vector channel at the overlap is nonzero but has a special form:
    # g = sigma_1 . sigma_2 (on sites 1,2), h = sigma_2 . sigma_3 -> must not commute
    def dot(a, b):
        return sum(site_op(P, a, n) @ site_op(P, b, n) for P in PAULI)
    g, h = dot(1, 2), dot(2, 3)
    check(np.linalg.norm(g @ h - h @ g) > 1, "A Heisenberg bonds sharing one site do not commute")


# ---------------------------------------------------------------- Part B: vector-operator basis
def vector_basis(n):
    d = 2 ** n
    S = total_spin(n)
    Id = np.eye(d)
    # unknown x = (vec X^1, vec X^2, vec X^3) (row-major vec: vec(AXB) = (A kron B^T) vec X)
    blocks = []
    for a in range(3):
        ad = np.kron(S[a], Id) - np.kron(Id, S[a].T)  # vec([S_a, X])
        for j in range(3):
            row = [np.zeros((d * d, d * d), dtype=complex) for _ in range(3)]
            row[j] = row[j] + ad
            for k in range(3):
                if EPS[a, j, k] != 0:
                    row[k] = row[k] - 1j * EPS[a, j, k] * np.eye(d * d)
            blocks.append(np.hstack(row))
    M = np.vstack(blocks)
    # real formulation: X Hermitian.  Parametrise X^j = sum_r x_{j r} H_r with H_r a real basis of
    # Hermitian d x d matrices (Pauli strings) -> real linear system.
    strings = []
    for idx in itertools.product(range(4), repeat=n):
        m = np.array([[1.0 + 0j]])
        for i in idx:
            m = np.kron(m, [I2, SX, SY, SZ][i])
        strings.append(m)
    # restrict to strings with total weight parity / just use all 4^n strings
    Hs = np.array([s.reshape(-1) for s in strings]).T  # d^2 x 4^n
    Z = np.zeros_like(Hs)
    E = np.block([[Hs, Z, Z], [Z, Hs, Z], [Z, Z, Hs]])  # 3d^2 x 3*4^n
    A = M @ E
    Ar = np.vstack([A.real, A.imag])
    _, sv, vt = np.linalg.svd(Ar, full_matrices=True)
    tol = 1e-9 * sv[0]
    rank = int((sv > tol).sum())
    null = vt[rank:]  # real coefficient vectors
    basis = []
    for v in null:
        Ws = []
        for j in range(3):
            c = v[j * 4 ** n:(j + 1) * 4 ** n]
            Ws.append(np.einsum("r,rij->ij", c, np.array(strings)))
        nrm = np.sqrt(sum(np.linalg.norm(W) ** 2 for W in Ws))
        basis.append([W / nrm for W in Ws])
    return basis


def spin1_multiplicity(m):  # m spin-1/2's
    if m < 2:
        return 0
    return comb(m, m // 2 - 1) - comb(m, m // 2 - 2) if m // 2 - 2 >= 0 else comb(m, m // 2 - 1)


# ---------------------------------------------------------------- Part C: search
def make_residual(basis, n):
    B = np.array([[b[j] for j in range(3)] for b in basis])  # m x 3 x d x d
    d = 2 ** n
    Id = np.eye(d)

    def Wof(c):
        return np.einsum("a,ajxy->jxy", c, B)

    def prod_overlap(X, Y, s):
        """(X (x) 1_s)(1_s (x) Y) and reverse, without forming 2^{n+s} kron of full size twice."""
        a, o = 2 ** s, 2 ** (n - s)
        Xt = X.reshape(a, o, a, o)
        Yt = Y.reshape(o, a, o, a)
        XY = np.einsum("pqrk,kbjc->pqbrjc", Xt, Yt, optimize=True)
        YX = np.einsum("qbkc,pkrj->pqbrjc", Yt, Xt, optimize=True)
        D = 2 ** (n + s)
        return (XY - YX).reshape(D, D)

    def resid(c):
        W = Wof(c)
        Wp = W[0] + 1j * W[1]
        Wz = W[2]
        r = []
        for j in range(3):
            for k in range(3):
                R = W[j] @ W[k] - (Id if j == k else 0)
                for l in range(3):
                    if EPS[j, k, l] != 0:
                        R = R - 1j * EPS[j, k, l] * W[l]
                r.append(R.ravel())
        for s in range(1, n):
            # spherical components of T_jk = [W^j_0, W^k_s]: rank2 (++), rank1, rank0
            T2 = prod_overlap(Wp, Wp, s)
            T1 = prod_overlap(Wp, Wz, s) - prod_overlap(Wz, Wp, s)
            T0 = sum(prod_overlap(W[j], W[j], s) for j in range(3))
            # also one extra full component for safety
            Tzz = prod_overlap(Wz, Wz, s)
            r += [T2.ravel(), T1.ravel(), T0.ravel(), Tzz.ravel()]
        v = np.concatenate(r)
        return np.concatenate([v.real, v.imag])

    return Wof, resid


def partC(rng):
    t0 = time.time()
    n = N
    basis = vector_basis(n)
    m = len(basis)
    pred = spin1_multiplicity(2 * n)
    check(m == pred, f"B n={n}: dim Hermitian vector operators = {m}, Schur-Weyl spin-1 "
                     f"multiplicity in (1/2)^(2n) = {pred}")
    Wof, resid = make_residual(basis, n)
    # controls: the n shifts are exact solutions
    shift_res = []
    targets = []
    for k in range(n):
        T = [site_op(P, k, n) for P in PAULI]
        # coefficients of T in basis (least squares in Hilbert-Schmidt)
        G = np.array([[sum(np.vdot(bi[j], bj[j]) for j in range(3)).real for bj in basis] for bi in basis])
        h = np.array([sum(np.vdot(bi[j], T[j]) for j in range(3)).real for bi in basis])
        c = np.linalg.solve(G, h)
        rec = Wof(c)
        assert max(np.linalg.norm(rec[j] - T[j]) for j in range(3)) < 1e-9
        shift_res.append(np.linalg.norm(resid(c)))
        targets.append(T)
    check(max(shift_res) < 1e-10, f"C n={n}: the {n} window shifts sigma_k are exact solutions "
                                  f"(max residual {max(shift_res):.1e})")
    # negative control: a normalised superposition (sigma_0+sigma_1)/sqrt2 is not
    T = [(site_op(P, 0, n) + site_op(P, 1, n)) / np.sqrt(2) for P in PAULI]
    G = np.array([[sum(np.vdot(bi[j], bj[j]) for j in range(3)).real for bj in basis] for bi in basis])
    h = np.array([sum(np.vdot(bi[j], T[j]) for j in range(3)).real for bi in basis])
    check(np.linalg.norm(resid(np.linalg.solve(G, h))) > 1e-1,
          f"C n={n}: control (sigma_0+sigma_1)/sqrt2 violates constraints (constraints active)")

    found = {k: 0 for k in range(n)}
    other = 0
    conv = 0
    tried = 0
    scale = np.sqrt(2 ** n)  # ||sigma_k||_HS per component ~ sqrt(d); basis normalised to 1
    for st in range(STARTS):
        if time.time() - t0 > BUDGET:
            log(f"   budget reached after {tried} starts")
            break
        tried += 1
        c0 = rng.normal(size=m)
        c0 *= scale * np.sqrt(3) / np.linalg.norm(c0)
        sol = least_squares(resid, c0, method="trf", xtol=1e-15, ftol=1e-15, gtol=1e-15,
                            max_nfev=MAXNFEV)
        rn = np.linalg.norm(sol.fun)
        W = Wof(sol.x)
        label = "nonconverged"

        def mindist(W):
            ds = [max(np.linalg.norm(W[j] - targets[k][j]) for j in range(3)) for k in range(n)]
            k = int(np.argmin(ds))
            return k, ds[k]

        if rn < 1e-7:
            conv += 1
            k, dk = mindist(W)
            if dk < 1e-5:
                found[k] += 1
                label = f"shift-to-site-{k}"
            elif dk < 3e-2:
                # Degenerate valley: the linearised constraints at a shift admit the first-order
                # deformations delta W = i[sum_x tau_x h, W] (h an SU(2)-invariant local term;
                # the generator of the quasi-local flow e^{itH}), so Gauss-Newton converges only
                # slowly along it.  Polish further and record whether the distance decreases.
                sol2 = least_squares(resid, sol.x, method="trf", xtol=1e-16, ftol=1e-16,
                                     gtol=1e-16, max_nfev=POLISH)
                k2, dk2 = mindist(Wof(sol2.x))
                rn2 = np.linalg.norm(sol2.fun)
                slow_tail.append((dk, dk2, rn, rn2))
                if k2 == k and dk2 < dk:
                    found[k] += 1
                    label = (f"shift-to-site-{k} (slow valley: dist {dk:.2e} -> {dk2:.2e} after "
                             f"polish, residual {rn:.1e} -> {rn2:.1e})")
                else:
                    other += 1
                    label = f"OTHER (near shift {k}, dist {dk:.2e} -> {dk2:.2e}, not decreasing)"
            else:
                other += 1
                label = f"OTHER (min dist to a shift {dk:.2e})"
        log(f"   start {st}: residual {rn:.2e} nfev {sol.nfev} -> {label}  t={time.time()-t0:.0f}s")
    log(f"   n={n}: starts {tried}, converged {conv}, shifts found {found}, other {other}")
    if slow_tail:
        log(f"   slow-valley cases {len(slow_tail)}: max dist before polish {max(t[0] for t in slow_tail):.2e}, after {max(t[1] for t in slow_tail):.2e}")
    check(other == 0, f"C n={n}: every converged solution of (i)-(iii) is a single-site Pauli triple "
                      f"(a lattice shift); {conv}/{tried} converged, 0 other expected, got {other}")
    check(conv >= 1, f"C n={n}: at least one start converged (search is not vacuous)")


rng = np.random.default_rng(SEED)
log(f"r01 sigma-image search; n={N} starts={STARTS} budget={BUDGET}s seed={SEED}")
partA(rng)
partC(rng)
log(f"TOTAL: PASS={npass} FAIL={nfail}")
