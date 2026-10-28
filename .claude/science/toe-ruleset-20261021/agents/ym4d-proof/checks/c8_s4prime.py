#!/usr/bin/env python3
"""Check for S4' (PROOF.md, session 3): order-averaged log-averaging of SU(N) links, L = 3, d = 4, fine torus side 6 (even).
  T^s_y = P^s(c_X -> y) S_y P^s(c_Y -> y + L e_mu)^dag, s = one of the 24 coordinate orders; T_c := S_{c_X} (order-free)
  U'(X, X+e_mu) = S_{c_X} exp( (1/24) sum_s L^-4 sum_y log(S_{c_X}^-1 T^s_y) )
Checks (exact identities, finite instances): (a) gauge covariance, (b) SU(N), (c) pure gauge, (d) AXIS-PERMUTATION
covariance V[pi U] = pi V[U] (fails for the fixed-order S4: printed as a control), (e) reflection covariance through a
block-boundary plane, both directions; (f) U(1) exact linearisation: log U' = Q_str A - (d h)(X, mu) with
h(X) = avg_s avg_y int_{P^s(c_X -> y)} A (the [S3] decomposition), for both S4' and the fixed-order S4.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(3); d = 4; Lb = 3; Tc = 2; S = Lb * Tc
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
def logu(Z):
    w, V = np.linalg.eig(Z); return V @ np.diag(np.log(w)) @ np.linalg.inv(V)
def expa(X):  # exp of anti-hermitian
    w, V = np.linalg.eigh(-1j * X); return V @ np.diag(np.exp(1j * w)) @ dag(V)
def gens(N):
    G = []
    for i in range(N):
        for j in range(i + 1, N):
            A = np.zeros((N, N), complex); A[i, j] = A[j, i] = .5; G.append(A)
            B = np.zeros((N, N), complex); B[i, j] = -.5j; B[j, i] = .5j; G.append(B)
    for k in range(1, N):
        D = np.zeros((N, N), complex); D[:k, :k] = np.eye(k); D[k, k] = -k; G.append(D / np.sqrt(2 * k * (k + 1)))
    return np.array(G)
E = np.eye(d, dtype=int); ORD = list(it.permutations(range(d)))
idx = lambda x: tuple(np.asarray(x) % S)
def step(U, x, m, sg):
    return U[m][idx(x)] if sg > 0 else dag(U[m][idx(np.asarray(x) - E[m])])
def path(U, a, b, order):
    P = np.eye(U.shape[-1], dtype=complex); cur = np.array(a)
    for m in order:
        while cur[m] != b[m]:
            sg = 1 if b[m] > cur[m] else -1; P = P @ step(U, cur, m, sg); cur[m] += sg
    return P
def straight(U, y, m):
    P = np.eye(U.shape[-1], dtype=complex); cur = np.array(y)
    for _ in range(Lb): P = P @ step(U, cur, m, 1); cur[m] += 1
    return P
def avg(U, X, m, orders):
    cX = np.array(X) * Lb + 1; cY = cX + Lb * E[m]; Sc = straight(U, cX, m); acc = 0
    for o in orders:
        for off in it.product(range(Lb), repeat=d):
            y = np.array(X) * Lb + np.array(off)
            T = path(U, cX, y, o) @ straight(U, y, m) @ dag(path(U, cY, y + Lb * E[m], o)); acc = acc + logu(dag(Sc) @ T)
    Xb = acc / (len(orders) * Lb ** d); Xb = (Xb - dag(Xb)) / 2
    return Sc @ expa(Xb)
def field(N, amp, seed):
    r = np.random.default_rng(seed); G = gens(N); a = amp * r.normal(size=(d, S, S, S, S, len(G)))
    H = np.einsum("...a,aij->...ij", a, G); w, V = np.linalg.eigh(H); return V @ (np.exp(1j * w)[..., None] * dag(V))
for N in (2, 3):
    U = field(N, 0.12, 1); X = (0, 1, 1, 0); m = 1; Up = avg(U, X, m, ORD)
    g = field(N, 1.0, 2)[0]
    Ug = np.array([np.einsum("abcdij,abcdjk,abcdlk->abcdil", g, U[k], np.conj(np.roll(g, -1, axis=k))) for k in range(d)])
    cX = idx(np.array(X) * Lb + 1); cY = idx(np.array(X) * Lb + 1 + Lb * E[m])
    e = np.linalg.norm(avg(Ug, X, m, ORD) - g[cX] @ Up @ dag(g[cY]))
    check(f"a SU({N}) S4' gauge covariance", e < 1e-10, f"err {e:.1e}")
    check(f"b SU({N}) S4' U' in SU(N)", np.linalg.norm(Up @ dag(Up) - np.eye(N)) < 1e-10 and abs(np.linalg.det(Up) - 1) < 1e-10)
    Upure = np.array([np.einsum("abcdij,abcdkj->abcdik", g, np.conj(np.roll(g, -1, axis=k))) for k in range(d)])
    e = np.linalg.norm(avg(Upure, X, m, ORD) - g[cX] @ dag(g[cY])); check(f"c SU({N}) S4' pure gauge -> pure gauge", e < 1e-10, f"err {e:.1e}")
    # (d) axis permutation pi: (pi U)_{pi(k)}(pi x) = U_k(x); V[pi U](pi X, pi m) should equal V[U](X, m)
    pi = (2, 0, 3, 1); inv = np.argsort(pi)
    Upi = np.empty_like(U)
    for k in range(d):
        Upi[pi[k]] = np.transpose(U[k], axes=tuple(inv) + (4, 5))  # array index: new axis pi[k] <- old axis k
    piX = tuple(np.array(X)[inv]); e1 = np.linalg.norm(avg(Upi, piX, pi[m], ORD) - Up)
    e0 = np.linalg.norm(avg(Upi, piX, pi[m], ORD[:1]) - avg(U, X, m, ORD[:1]))
    check(f"d SU({N}) S4' axis-permutation covariance V[piU](piX, pi mu) = V[U](X, mu)", e1 < 1e-10,
          f"err {e1:.1e}; fixed-order S4 control err {e0:.1e} (nonzero expected)")
    # (e) reflection x0 -> S-1-x0 (block-boundary plane between fine 5 and 0 / 2 and 3)
    th = lambda A: A[::-1]
    Ur = np.array([dag(np.roll(th(U[0]), -1, axis=0))] + [th(U[k]) for k in range(1, d)])
    X0 = (0, 1, 1, 0); w1 = avg(U, (Tc - 1 - X0[0],) + X0[1:], 1, ORD); v1 = avg(Ur, X0, 1, ORD)
    w0 = avg(U, ((Tc - 2 - X0[0]) % Tc,) + X0[1:], 0, ORD); v0 = avg(Ur, X0, 0, ORD)
    e = max(np.linalg.norm(v1 - w1), np.linalg.norm(v0 - dag(w0)))
    check(f"e SU({N}) S4' reflection covariance (unreflected and reflected direction)", e < 1e-10, f"err {e:.1e}")
# (f) U(1): A real, U = exp(iA) small; compare -i log U' with Q_str A - dh
r = np.random.default_rng(7); A = 0.02 * r.normal(size=(d, S, S, S, S)); U1 = np.exp(1j * A)[..., None, None]
def lineint(a, b, order):
    return float(np.real(-1j * np.log(path(U1, a, b, order)[0, 0])))
def h(X, orders):
    c = np.array(X) * Lb + 1
    return np.mean([lineint(c, np.array(X) * Lb + np.array(off), o) for o in orders for off in it.product(range(Lb), repeat=d)])
for name, orders in (("S4'", ORD), ("S4 fixed order", ORD[:1])):
    errs = []
    for X, m in (((0, 1, 1, 0), 1), ((1, 0, 1, 1), 3), ((1, 1, 0, 0), 0)):
        lhs = float(np.real(-1j * np.log(avg(U1, X, m, orders)[0, 0])))
        qstr = np.mean([float(np.real(-1j * np.log(straight(U1, np.array(X) * Lb + np.array(off), m)[0, 0]))) for off in it.product(range(Lb), repeat=d)])
        Y = tuple((np.array(X) + E[m]) % Tc); errs.append(abs(lhs - (qstr - (h(Y, orders) - h(X, orders)))))
    check(f"f U(1) {name}: log U' = Q_str A - (dh)(X, mu) exactly (3 links)", max(errs) < 1e-12, f"max err {max(errs):.1e}")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
