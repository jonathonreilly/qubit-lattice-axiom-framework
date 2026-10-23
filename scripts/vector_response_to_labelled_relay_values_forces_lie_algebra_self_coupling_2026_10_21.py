#!/usr/bin/env python3
"""Finite numerical support for an open vector-response classification target.
In supplied 3+1 Minkowski kinematics, test a six-structure parity-even cubic
ansatz at N=3,4 and K=12 sampled four-point kinematics for three Lie examples
and one random N=5 antisymmetric tensor. Contact fits are independent per label
quadruple, without Bose consistency. These tests do not establish a universal
Ward/Jacobi necessity or sufficiency theorem. Seed and tolerances are in the
paired note. Algebra and stabilizer calculations use explicitly supplied
complex-linear or star-preserving/unitary actions; they derive no charges or
lattice dynamics. The historical filename is a recovery identifier, not status.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

AUDIT_INPUT_PATHS = ('docs/VECTOR_RESPONSE_TO_LABELLED_RELAY_VALUES_FORCES_LIE_ALGEBRA_SELF_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import sys, os, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 300-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0
G = np.diag([1.0, -1.0, -1.0, -1.0])
RNG = np.random.default_rng(7)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def dot(a, b): return a @ G @ b


def null_vec():
    n = RNG.normal(size=3); return RNG.uniform(0.5, 2.0) * np.concatenate([[1.0], n / np.linalg.norm(n)])


def boost(v):
    """Lorentz boost taking the rest frame to four-velocity u = v / sqrt(v.v) (v timelike, v0 > 0)."""
    m = np.sqrt(dot(v, v)); u = v / m; g = u[0]; b = u[1:]
    L = np.eye(4); L[0, 0] = g; L[0, 1:] = b; L[1:, 0] = b
    L[1:, 1:] += np.outer(b, b) / (1 + g)
    return L


def four_null():
    """Four real null momenta, all incoming, summing to zero."""
    p1, p2 = null_vec(), null_vec(); Q = p1 + p2; M = np.sqrt(dot(Q, Q))
    n = RNG.normal(size=3); n /= np.linalg.norm(n)
    q3 = 0.5 * M * np.concatenate([[1.0], n]); q4 = 0.5 * M * np.concatenate([[1.0], -n])
    L = boost(Q)
    return [p1, p2, -(L @ q3), -(L @ q4)]


def pol(p):
    r, n = RNG.normal(size=4), null_vec()
    return r - dot(r, p) / dot(n, p) * n


# ---------- (1) general cubic vertex ----------
def vertex_general(c, k1, k2):
    """c[s,a,b,c]; returns V[a,b,c,mu,nu,rho] with lower indices; k3 = -k1-k2 is implicit."""
    l1, l2 = G @ k1, G @ k2
    S = [np.einsum('mn,r->mnr', G, l1), np.einsum('mn,r->mnr', G, l2),
         np.einsum('nr,m->mnr', G, l1), np.einsum('nr,m->mnr', G, l2),
         np.einsum('rm,n->mnr', G, l1), np.einsum('rm,n->mnr', G, l2)]
    return np.tensordot(c, np.array(S), axes=([0], [0]))


def ym(f, k1, k2, k3):
    l1, l2, l3 = G @ k1, G @ k2, G @ k3
    T = np.einsum('mn,r->mnr', G, l1 - l2) + np.einsum('nr,m->mnr', G, l2 - l3) + np.einsum('rm,n->mnr', G, l3 - l1)
    return np.einsum('abc,mnr->abcmnr', f, T)


def first_order(N):
    nun = 6 * N ** 3; rows = []
    def lin(fun):
        E = np.eye(nun).reshape(nun, 6, N, N, N)
        return np.array([fun(E[i]).ravel() for i in range(nun)]).T
    for _ in range(3):  # Bose symmetry at generic off-shell momenta
        k1, k2 = RNG.normal(size=4), RNG.normal(size=4); k3 = -k1 - k2
        rows.append(lin(lambda c: vertex_general(c, k1, k2) - vertex_general(c, k2, k1).transpose(1, 0, 2, 4, 3, 5)))
        rows.append(lin(lambda c: vertex_general(c, k1, k2) - vertex_general(c, k1, k3).transpose(0, 2, 1, 3, 5, 4)))
    for t in range(8):  # gauge consistency with legs 1, 2 on the free shell (transverse null or pure gauge)
        k1, k2 = null_vec(), null_vec(); k3 = -k1 - k2
        e1 = pol(k1) if t % 4 != 3 else k1 * RNG.normal()
        e2 = pol(k2)
        if t % 4 == 2:  # pure gauge on an off-null momentum: still solves the free equation
            k2 = RNG.normal(size=4); k3 = -k1 - k2; e2 = k2.copy()
        rows.append(lin(lambda c: np.einsum('abcmnr,m,n,r->abc', vertex_general(c, k1, k2), e1, e2, k3)))
    M = sum(r.T @ r for r in rows)  # Gram matrix (nun x nun): same null space, small memory
    w, U = np.linalg.eigh(M); null = int(np.sum(w < 1e-9 * w[-1])); basis = U[:, :null].T
    # compare with the YM span for antisymmetric f
    k1, k2 = RNG.normal(size=4), RNG.normal(size=4); k3 = -k1 - k2
    sols = [vertex_general(b.reshape(6, N, N, N), k1, k2).ravel() for b in basis]
    asym = []
    for (a, b, cc) in itertools.combinations(range(N), 3):
        f = np.zeros((N, N, N))
        for p in itertools.permutations(range(3)):
            f[tuple((a, b, cc)[i] for i in p)] = np.linalg.det(np.eye(3)[list(p)])
        asym.append(ym(f, k1, k2, k3).ravel())
    rk = lambda M: np.linalg.matrix_rank(np.array(M), tol=1e-8) if len(M) else 0
    return null, rk(asym), rk(sols + asym)


# ---------- (2) four-point Ward identity ----------
def ward_residual(f, K=12):
    N = f.shape[0]; exch, struct = [], []
    for _ in range(K):
        p = four_null(); e = [pol(p[i]) for i in range(3)] + [p[3]]  # leg 4 replaced by its momentum
        tot = np.zeros((N,) * 4)
        for (i, j), (k, l) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
            P = p[i] + p[j]
            Va = np.einsum('abxmnl,m,n->abxl', ym(f, p[i], p[j], -P), e[i], e[j])
            Vb = np.einsum('cdxmnl,m,n->cdxl', ym(f, p[k], p[l], P), e[k], e[l])
            amp = np.einsum('abxl,ls,cdxs->abcd', Va, np.linalg.inv(G), Vb) / dot(P, P)
            order = np.argsort([i, j, k, l]); tot += amp.transpose(order)
        exch.append(tot)
        struct.append([dot(e[0], e[1]) * dot(e[2], e[3]), dot(e[0], e[2]) * dot(e[1], e[3]), dot(e[0], e[3]) * dot(e[1], e[2])])
    exch = np.array(exch); S = np.array(struct)  # (K,N,N,N,N), (K,3)
    Q, _ = np.linalg.qr(S); R = exch - np.einsum('ks,js,j...->k...', Q, Q, exch)  # least-squares contact removed
    scale = np.sqrt(np.sum(exch ** 2, 0)) + 1e-300
    return np.sqrt(np.sum(R ** 2, 0)), scale


def jacobi(f):
    return (np.einsum('abe,ecd->abcd', f, f) + np.einsum('bce,ead->abcd', f, f) + np.einsum('cae,ebd->abcd', f, f))


def eps3():
    f = np.zeros((3, 3, 3))
    for p in itertools.permutations(range(3)): f[p] = np.linalg.det(np.eye(3)[list(p)])
    return f


def su3_f():
    l = np.zeros((8, 3, 3), complex)
    l[0][0, 1] = l[0][1, 0] = 1; l[1][0, 1] = -1j; l[1][1, 0] = 1j; l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1; l[4][0, 2] = -1j; l[4][2, 0] = 1j; l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j; l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    T = l / 2
    return np.real(-2j * (np.einsum('aij,bjk,cki->abc', T, T, T) - np.einsum('bij,ajk,cki->abc', T, T, T)))  # f = -2i Tr([Ta,Tb]Tc)


# ---------- (3) compact reductive algebras by dimension ----------
def simple_dims(D):
    d = set()
    for n in range(1, 40):
        d |= {n * (n + 2)} | ({n * (2 * n + 1)} if n >= 2 else set()) | ({n * (2 * n - 1)} if n >= 4 else set())
    d |= {14, 52, 78, 133, 248}
    # multiplicities: B_n and C_n (n >= 3) share a dimension
    mult = {x: 0 for x in d if x <= D}
    for n in range(1, 40):
        for x, ok in [(n * (n + 2), True), (n * (2 * n + 1), n >= 2), (n * (2 * n + 1), n >= 3), (n * (2 * n - 1), n >= 4)]:
            if ok and x <= D: mult[x] += 1
    for x in (14, 52, 78, 133, 248):
        if x <= D: mult[x] += 1
    return mult


def count_reductive(D):
    kinds = [(x, i) for x, m in simple_dims(D).items() for i in range(m)]
    tot = 0
    def rec(idx, rem):
        nonlocal tot
        tot += 1
        for j in range(idx, len(kinds)):
            if kinds[j][0] <= rem: rec(j, rem - kinds[j][0])
    rec(0, D); return tot


def main():
    # (1)
    for N in (3, 4):
        null, r_ym, r_both = first_order(N)
        from math import comb
        check(f'(1) N={N}: sampled six-structure cubic constraint kernel has dimension C(N,3) = {comb(N,3)} and matches the sampled antisymmetric Yang-Mills span',
              null == comb(N, 3) and r_ym == null and r_both == null, f'null space {null}, YM span {r_ym}, joint span {r_both}')
    # (2)
    for name, f in [('su(2)', eps3()), ('su(2)+u(1)', np.pad(eps3(), ((0, 1),) * 3)), ('su(3)', su3_f())]:
        res, sc = ward_residual(f); J = np.max(abs(jacobi(f)))
        check(f'(2) {name}: Jacobi holds ({J:.1e}) and K=12 sampled Ward residuals admit independent per-quadruple contact fits (Bose consistency untested)', J < 1e-12 and np.max(res / np.max(sc)) < 1e-10, f'max relative residual {np.max(res / np.max(sc)):.1e}')
    A = RNG.normal(size=(5, 5, 5)); f = sum(np.sign(np.linalg.det(np.eye(3)[list(p)])) * A.transpose(p) for p in itertools.permutations(range(3)))
    res, sc = ward_residual(f); J = abs(jacobi(f))
    bad = J > 1e-8; rel = res / np.max(sc)
    check('(2) seeded N=5 antisymmetric sample: K=12 least-squares contact residual exceeds threshold on Jacobi-violating quadruples and is below threshold elsewhere',
          bad.any() and np.min(rel[bad]) > 1e-3 and (np.max(rel[~bad]) if (~bad).any() else 0) < 1e-10,
          f'Jacobi-violating quadruples {int(bad.sum())}/625, min residual there {np.min(rel[bad]):.2e}, max elsewhere {(np.max(rel[~bad]) if (~bad).any() else 0):.1e}')
    corr = np.corrcoef(rel[bad].ravel(), J[bad].ravel())[0, 1]
    print(f'    residual vs |Jacobi| correlation on violating quadruples: {corr:.3f}')
    # N=4 zero bracket is abelian, not su(2)+u(1); no RNG consumption.
    zero4 = np.zeros((4, 4, 4), dtype=int)
    check('(2) N=4 v=0: zero bracket has Jacobi zero and commutator-span rank zero (abelian R^4)',
          np.array_equal(jacobi(zero4), np.zeros((4,) * 4)) and np.linalg.matrix_rank(zero4.reshape(16, 4)) == 0)
    # (3)
    n12, n3, n8 = count_reductive(12), count_reductive(3), count_reductive(8)
    check('(3) compact reductive Lie algebras: 8 of dimension 12 (su(3)+su(2)+u(1) among them), 2 of dimension 3, 4 of dimension 8',
          (n12, n3, n8) == (8, 2, 4), f'counts {n12}, {n3}, {n8}')
    # (4)
    E = [np.zeros((2, 2), complex) for _ in range(4)]
    for i, (r, c) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]): E[i][r, c] = 1
    # derivation D: linear map on M_2 (4x4 complex); D(xy) = D(x)y + xD(y) for all basis x, y
    rows = []
    for x in range(4):
        for y in range(4):
            xy = E[x] @ E[y]
            for out in range(4):
                r_, c_ = divmod(out, 2); row = np.zeros(16, complex)
                for k in range(4):  # D(E_k) = sum_out D[out,k] E_out
                    coef = xy.ravel()[k]
                    if coef: row[out * 4 + k] += coef
                for o2 in range(4):  # D(x) y + x D(y)
                    row[o2 * 4 + x] -= (E[o2] @ E[y])[r_, c_]
                    row[o2 * 4 + y] -= (E[x] @ E[o2])[r_, c_]
                rows.append(row)
    nder = 16 - np.linalg.matrix_rank(np.array(rows), tol=1e-10)
    # Impose star preservation as real-linear constraints on the complex D map.
    L = np.array(rows)
    real_L = np.block([[L.real, -L.imag], [L.imag, L.real]])
    star_cols = []
    for j in range(32):
        v = np.zeros(32); v[j] = 1
        D = (v[:16] + 1j * v[16:]).reshape(4, 4)
        defects = []
        for k in range(4):
            kt = (k % 2) * 2 + k // 2
            defects.extend((D[:, kt].reshape(2, 2) - D[:, k].reshape(2, 2).conj().T).ravel())
        z = np.array(defects)
        star_cols.append(np.concatenate([z.real, z.imag]))
    nstar = 32 - np.linalg.matrix_rank(np.vstack([real_L, np.array(star_cols).T]), tol=1e-10)
    H = np.diag([1, -1]); integer_E = [e.real.astype(int) for e in E]
    deriv = lambda x: H @ x - x @ H
    leibniz = all(np.array_equal(deriv(x @ y), deriv(x) @ y + x @ deriv(y)) for x in integer_E for y in integer_E)
    not_star = not np.array_equal(deriv(integer_E[1].T), deriv(integer_E[1]).T)
    check('(4) exact integer negative control: ad_diag(1,-1) obeys Leibniz but fails star preservation', leibniz and not_star)
    check('(4) Der_C(M2(C)) dimension 3 complex / 6 real; star-preserving derivations dimension 3 real',
          nder == 3 and 32 - np.linalg.matrix_rank(real_L, tol=1e-10) == 6 and nstar == 3,
          f'complex dimension {nder}, star real dimension {nstar}')
    sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
    X = [-0.5j * s for s in sig]; fc = np.array([[[np.trace(np.linalg.inv(X[c]) @ (X[a] @ X[b] - X[b] @ X[a])).real / 2 for c in range(3)] for b in range(3)] for a in range(3)])
    kill = np.einsum('acd,bdc->ab', fc, fc)
    stab = [x for x in X if np.allclose(x @ np.diag([1, 0]) - np.diag([1, 0]) @ x, 0)]
    check('(4) supplied anti-Hermitian traceless generators span the real star-derivation algebra su(2); rank-one projector stabilizer inside SU(2) has Lie algebra u(1)',
          nstar == 3 and np.all(np.linalg.eigvalsh(kill) < 0) and np.allclose(fc, eps3()) and len(stab) == 1, f'real star dimension = {nstar}, Killing eigenvalues {np.round(np.linalg.eigvalsh(kill), 3)}')
    Nn = 8; Ps = [np.diag(np.eye(Nn)[i]) for i in range(Nn)]
    basis = []
    for i in range(Nn):
        for j in range(Nn):
            M = np.zeros((Nn, Nn), complex); M[i, j] = 1; basis.append(M)
    A = np.array([np.concatenate([(M @ P - P @ M).ravel() for P in Ps]) for M in basis]).T
    dim_stab = Nn * Nn - np.linalg.matrix_rank(A, tol=1e-10)
    check('(4) complex commutant of eight labelled rank-one projectors has dimension 8; supplied U(8) pointwise stabilizer is U(1)^8 (common phase acts trivially by conjugation)',
          dim_stab == Nn, f'complex commutant dimension {dim_stab}')
    print('per_site: the vector-field ansatz (local, covariant, at most one derivative, positive kinetic metric), the Feynman-gauge tree test and the internal dimension N are supplied choices.')
    print('lattice_wide: no gauge group, coupling, matter assignment, link dynamics on the lattice or empirical identification is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
