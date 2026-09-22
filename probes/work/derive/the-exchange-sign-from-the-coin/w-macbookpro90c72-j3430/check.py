#!/usr/bin/env python3
"""J:derive:the-exchange-sign-from-the-coin:a1 -- exact checks.

One moving record is an amplitude over sites with the qubit as content: V = C^sites (x) C^2 (index 2*site + coin).
Block 54's walk is H = sum_a sigma_a (x) p_a with p_a = -i(T_a - T_a^T)/2 (the symmetric one-step difference); on
rings, block 78's reduced walk H = sigma_3 (x) p.  Two records live in V (x) V.  P is the exchange (swap), HC the
hard-core space (the records on different sites: the Record axiom), K+ / K- its symmetric / antisymmetric parts,
and H2 the free generator H(x)1 + 1(x)H compressed to HC.

Exactness: 2H has Gaussian-integer entries, so every matrix product below has Gaussian-integer entries far below
2^53 in modulus and complex128 carries them exactly; gi() asserts integrality wherever a value is read off.
sympy is used for the one-site algebra (B4).
"""
import sys
from fractions import Fraction as F
from itertools import product
import numpy as np
import scipy.sparse as sp
import sympy as sy

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


def gi(z):
    """read an exactly-integral complex128 value as a Gaussian integer (re, im)"""
    z = complex(z)
    re, im = round(z.real), round(z.imag)
    need(z.real == re and z.imag == im and abs(re) < 2 ** 50, "non-integral value %r" % z)
    return re + 1j * im if im else re


PAULI = {1: np.array([[0, 1], [1, 0]], dtype=complex), 2: np.array([[0, -1j], [1j, 0]]),
         3: np.array([[1, 0], [0, -1]], dtype=complex)}


# ------------------------------------------------------------------ (a) the objects
def walk_2H(d, L, sig):
    """2H on the d-torus of side L: hop +e_a with amplitude +i*sigma_{sig[a]}, -e_a with -i*sigma_{sig[a]}"""
    sites = list(product(range(L), repeat=d))
    ix = {s: i for i, s in enumerate(sites)}
    r, c, v = [], [], []
    for s in sites:
        for a in range(d):
            for sgn, amp in ((1, 1j), (-1, -1j)):
                t = list(s)
                t[a] = (t[a] + sgn) % L
                i, j = ix[s], ix[tuple(t)]
                for c1 in range(2):
                    for c2 in range(2):
                        if PAULI[sig[a]][c2, c1] != 0:
                            r.append(2 * j + c2)
                            c.append(2 * i + c1)
                            v.append(amp * PAULI[sig[a]][c2, c1])
    n = 2 * len(sites)
    return sp.csr_matrix((v, (r, c)), shape=(n, n)), len(sites)


def hard_core(H):
    """basis of HC (ordered pairs of one-record basis states on different sites), H2 = H(x)1+1(x)H compressed
    to HC, and the exchange P on HC"""
    d = H.shape[0]
    Hc = H.tocsc()
    col = [(Hc.indices[Hc.indptr[i]:Hc.indptr[i + 1]], Hc.data[Hc.indptr[i]:Hc.indptr[i + 1]]) for i in range(d)]
    basis = [(i, j) for i in range(d) for j in range(d) if i // 2 != j // 2]
    ix = {b: k for k, b in enumerate(basis)}
    r, c, v, pr = [], [], [], []
    for k, (i, j) in enumerate(basis):
        pr.append(ix[(j, i)])
        for i2, a in zip(*col[i]):
            if i2 // 2 != j // 2:
                r.append(ix[(i2, j)])
                c.append(k)
                v.append(a)
        for j2, a in zip(*col[j]):
            if j2 // 2 != i // 2:
                r.append(ix[(i, j2)])
                c.append(k)
                v.append(a)
    n = len(basis)
    H2 = sp.csr_matrix((v, (r, c)), shape=(n, n))
    P = sp.csr_matrix((np.ones(n), (pr, range(n))), shape=(n, n))
    return basis, H2, P


def same(A, B):
    return (A - B).count_nonzero() == 0 if sp.issparse(A) else np.array_equal(A, B)


# ring of 4 (block 78's reduced walk) and the 3-torus of side 5 (block 54's walk)
H1r, _ = walk_2H(1, 4, (3,))
br, H2r, Pr = hard_core(H1r)
H3, n3 = walk_2H(3, 5, (1, 2, 3))
b3, H23, P3 = hard_core(H3)
ok = True
for (H, H2, P, nsite) in ((H1r, H2r, Pr, 4), (H3, H23, P3, n3)):
    ok &= same(H, H.conj().T) and same(H2, H2.conj().T) and same(P @ P, sp.identity(P.shape[0]))
    ok &= same(P @ H2, H2 @ P) and H2.shape[0] == 4 * nsite * (nsite - 1)
need(ok, "A: HC is exchange-invariant and the compressed generator commutes with P")
rec("ok A objects: one record = amplitude in V = C^sites (x) C^2; two records in V(x)V; the Record axiom confines "
    "them to HC = {different sites} (dim 4n(n-1)), P^2=1 and [P,H2]=0 on HC for the ring of 4 and the 3-torus of "
    "side 5, so K+ = HC^{P=+1} and K- = HC^{P=-1} are each closed under the dynamics (dims %d+%d on the 3-torus)"
    % (H23.shape[0] // 2, H23.shape[0] // 2))


# ------------------------------------------- (b) routes to a sign from the axioms' sentences
# B2 the discrete exchange rotation: g = (translation e1) o (rotation by pi about e2 at site 0) swaps 0 and e1
L3 = 5
sites3 = list(product(range(L3), repeat=3))
ix3 = {s: i for i, s in enumerate(sites3)}
Dpi = -1j * PAULI[2]                                      # exp(-i pi sigma2 / 2), the coin's lift of R_pi
perm = [ix3[((-s[0] + 1) % L3, s[1], (-s[2]) % L3)] for s in sites3]
Wg = sp.kron(sp.csr_matrix((np.ones(len(sites3)), (perm, range(len(sites3))))), sp.csr_matrix(Dpi)).tocsr()
ok = same(Wg @ H3 @ Wg.conj().T, H3) and same(Wg @ Wg, -sp.identity(Wg.shape[0]))
ok &= perm[ix3[(0, 0, 0)]] == ix3[(1, 0, 0)] and perm[ix3[(1, 0, 0)]] == ix3[(0, 0, 0)]
need(ok, "B2 exchange rotation")
rec("ok B2 the lattice symmetry g = (shift e1)o(pi about e2) swaps sites 0 and e1, commutes with the walk, and on "
    "one record g^2 = -1 (the coin's spinor sign); on two records (W(x)W)^2 = (-1)(-1) = +1 on K+ and on K- alike, "
    "and W(x)W commutes with P: the discrete rotation-exchange carries no sign (the continuous "
    "Finkelstein-Rubinstein homotopy is not supplied)")

# B4 the Clifford grading of Cl(3,0) = M2(C)
a0, a1, a2, a3, b0, b1, b2, b3 = sy.symbols("a0 a1 a2 a3 b0 b1 b2 b3", real=True)
s1, s2, s3 = sy.Matrix([[0, 1], [1, 0]]), sy.Matrix([[0, -sy.I], [sy.I, 0]]), sy.Matrix([[1, 0], [0, -1]])
sg = (s1, s2, s3)


def alpha(x):                                              # the Clifford grading automorphism, antilinear
    return s2 * x.conjugate() * s2


ok = alpha(sy.eye(2)) == sy.eye(2) and alpha(sy.I * sy.eye(2)) == -sy.I * sy.eye(2)
ok &= all(alpha(s) == -s and alpha(sy.I * s) == sy.I * s for s in sg)
ok &= all(alpha(x * y) == alpha(x) * alpha(y) for x in sg + (sy.I * sy.eye(2),) for y in sg)
u1, u2, u3 = sy.symbols("u1 u2 u3", real=True)
proj = (sy.eye(2) + u1 * s1 + u2 * s2 + u3 * s3) / 2      # a pure record state: even part 1/2, odd part u.s/2
ok &= sy.expand((proj + alpha(proj)) / 2) == sy.eye(2) / 2
need(ok, "B4 the grading alpha")
Gam = sy.Matrix([[a0 + sy.I * b0, a1 + sy.I * b1], [a2 + sy.I * b2, a3 + sy.I * b3]])
eqs = []
for s in sg:                                               # complex-linear Gamma with Gamma s = - s Gamma
    eqs += [sy.re(e) for e in (Gam * s + s * Gam)] + [sy.im(e) for e in (Gam * s + s * Gam)]
lin = sy.solve(eqs, [a0, a1, a2, a3, b0, b1, b2, b3], dict=True)
eqs = []
for s in sg:                                               # antilinear Gamma = M K:  M conj(s) = - s M
    E = Gam * s.conjugate() + s * Gam
    eqs += [sy.re(e) for e in E] + [sy.im(e) for e in E]
anti = sy.solve(eqs, [a0, a1, a2, a3, b0, b1, b2, b3], dict=True)
Ms = Gam.subs(anti[0]) if anti else None
ok = lin == [{a0: 0, a1: 0, a2: 0, a3: 0, b0: 0, b1: 0, b2: 0, b3: 0}] and Ms is not None
if Ms is not None:
    free = sorted(Ms.free_symbols, key=str)
    ok &= len(free) == 2 and sy.expand(Ms - (Ms[0, 1] / (-sy.I)) * s2) == sy.zeros(2)
    cc = Ms[0, 1] / (-sy.I)                               # M = cc * s2
    sq = sy.expand(Ms * Ms.conjugate())                   # (MK)^2 = M conj(M)
    ok &= sy.expand(sq + cc * sy.conjugate(cc) * sy.eye(2)) == sy.zeros(2)
need(ok, "B4 no grading on C^2")
# the minimal graded module is C^4: Gamma = 1 (x) s3, generators s_a (x) s1
I2 = sy.eye(2)
ea = [sy.kronecker_product(s, s1) for s in sg]
Gm = sy.kronecker_product(I2, s3)
ok = all(ea[i] * ea[j] + ea[j] * ea[i] == (2 * sy.eye(4) if i == j else sy.zeros(4))
         for i in range(3) for j in range(3))
ok &= all(Gm * e + e * Gm == sy.zeros(4) for e in ea) and Gm * Gm == sy.eye(4)
need(ok, "B4 graded module C^4")
# the graded composite of two Cl(3,0) presentations: Cl(6,0) from three-qubit Majoranas
X, Y, Zm, Id = PAULI[1], PAULI[2], PAULI[3], np.eye(2)


def k3(A, B, C):
    return np.kron(np.kron(A, B), C)


e6 = [k3(X, Id, Id), k3(Y, Id, Id), k3(Zm, X, Id), k3(Zm, Y, Id), k3(Zm, Zm, X), k3(Zm, Zm, Y)]
ok = all(np.array_equal(e6[i] @ e6[j] + e6[j] @ e6[i], (2 * np.eye(8) if i == j else 0 * np.eye(8)))
         for i in range(6) for j in range(6))
wx, wy = e6[0] @ e6[1] @ e6[2], e6[3] @ e6[4] @ e6[5]
ok &= np.array_equal(wx @ wx, -np.eye(8)) and np.array_equal(wx @ wy, -wy @ wx)
ok &= all(np.array_equal(wx @ e, e @ wx) for e in e6[:3]) and all(np.array_equal(wy @ e, e @ wy) for e in e6[3:])
mono = []
for mask in range(64):
    Mm = np.eye(8, dtype=complex)
    for i in range(6):
        if mask >> i & 1:
            Mm = Mm @ e6[i]
    mono.append(np.concatenate([Mm.real.ravel(), Mm.imag.ravel()]))
rank64 = sy.Matrix(np.array(mono).round().astype(int)).rank()
sub = [np.concatenate([Mm.real.ravel(), Mm.imag.ravel()]) for Mm in
       [np.eye(8)] + [e6[i] for i in range(3)] + [e6[i] @ e6[j] for i in range(3) for j in range(i + 1, 3)] + [wx]]
rank8 = sy.Matrix(np.array(sub).round().astype(int)).rank()
ok &= rank64 == 64 and rank8 == 8
need(ok, "B4 Cl(6,0) composite")
rec("ok B4 Clifford route: the grading of Cl(3,0)=M2(C) is the antilinear a+b.s -> conj(a)-conj(b).s; on a record's "
    "content C^2 no involution makes s1,s2,s3 odd (linear solutions: 0; antilinear: M = c*s2 only, and "
    "(MK)^2 = -|c|^2), so a single record has no Clifford parity; the smallest graded module is C^4 (Gamma = 1(x)s3, "
    "e_a = s_a(x)s1), i.e. the parked M4(C); and the graded composite of two presentations is Cl(6,0) (real rank %d; "
    "each site's span rank %d with central w^2=-1) in which the two sites' complex units anticommute, against "
    "M2(C)(x)M2(C) = M4(C) (real dim 32) with one shared i: the one-site sentences fix neither composite"
    % (rank64, rank8))


# -------------------------------------- (d) at which order, and in what observable, the sign shows
def exch_traces(H2, P, kmax):
    """tr(P (2H2)^k), k=1..kmax, as exact Gaussian integers (for k = 3, 4 via elementwise products with H2^2,
    so that no fourth power is ever formed)"""
    if kmax <= 4:
        M2 = (H2 @ H2).tocsr()
        PM2 = (P @ M2).tocsr()
        out = [gi((P @ H2).diagonal().sum()), gi(PM2.diagonal().sum())]
        if kmax >= 3:
            out.append(gi(PM2.multiply(H2.T).sum()))
        if kmax >= 4:
            out.append(gi(PM2.multiply(M2.T).sum()))
        return out[:kmax]
    out, M = [], sp.identity(H2.shape[0], dtype=complex, format="csr")
    for _ in range(kmax):
        M = (M @ H2).tocsr()
        out.append(gi((P @ M).diagonal().sum()))
    return out


# rings (block 78's reduced walk): even N first at order N, odd N never (explicit unitary)
ring = {}
for N in range(4, 9):
    H, _ = walk_2H(1, N, (3,))
    bN, H2N, PN = hard_core(H)
    ring[N] = (bN, H2N, PN, exch_traces(H2N, PN, N))
ok = all(all(t == 0 for t in ring[N][3][:N - 1]) for N in ring)
ok &= all(ring[N][3][N - 1] != 0 for N in (4, 6, 8)) and all(ring[N][3][N - 1] == 0 for N in (5, 7))
# block 78's normalisation: hard-core tr H^2/dim = (N-2)/(N-1) in either sector; at N=4 the fourth traces 5/6, 7/6
b4, H24, P4 = ring[4][0], ring[4][1], ring[4][2]
t2 = gi((H24 @ H24).diagonal().sum())
t4 = gi((H24 @ H24 @ H24 @ H24).diagonal().sum())
dimK = H24.shape[0] // 2
ok &= F(t2, 4 * 2 * dimK) == F(2, 3) and F(t4 - ring[4][3][3], 16 * 2 * dimK) == F(5, 6)
ok &= F(t4 + ring[4][3][3], 16 * 2 * dimK) == F(7, 6)
need(ok, "D ring orders")
odd_ok = True
for N in (5, 7):
    bN, H2N, PN, _ = ring[N]
    n = len(bN)
    J = sp.diags([1.0 if i // 2 < j // 2 else -1.0 for (i, j) in bN])
    G = sp.diags([(-1.0) ** (i // 2 + j // 2) for (i, j) in bN])
    ixN = {b: k for k, b in enumerate(bN)}
    C = sp.csr_matrix((np.ones(n), ([ixN[(i ^ 1, j ^ 1)] for (i, j) in bN], range(n))), shape=(n, n))
    U = (C @ G @ J).tocsr()
    odd_ok &= same(U @ H2N @ U.conj().T, H2N) and same(U @ PN @ U.conj().T, -PN)
    odd_ok &= same(U @ U.conj().T, sp.identity(n))
need(odd_ok, "D odd rings equivalent")
rec("ok D rings (H = s3 p; block 78's values reproduced: hard-core trH^2/dim = 2/3, fourth traces 5/6 and 7/6 at "
    "N=4): tr(P H2^k) = 0 for k < N on N = 4..8; at k = N it is %s, %s, %s (x 2^-N) on N = 4, 6, 8; on N = 5, 7 "
    "the unitary U = (s1(x)s1)(G(x)G)J (J = sign of the order, G = (-1)^x) gives U H2 U* = H2 and U P U* = -P "
    "exactly, so K+ and K- are isospectral: on odd rings the sign is invisible to all orders"
    % (ring[4][3][3], ring[6][3][5], ring[8][3][7]))


def local_exch(d, sig, k):
    """infinite lattice: sum over r != 0 and coins of <Ps|(2H2)^k|s>, s = (record at 0, record at r);
    returns (total, {r: value}) -- the per-site exchange trace"""
    hops = []
    for a in range(d):
        for sgn, amp in ((1, 1j), (-1, -1j)):
            e = tuple(sgn if i == a else 0 for i in range(d))
            for c1 in range(2):
                for c2 in range(2):
                    if PAULI[sig[a]][c2, c1] != 0:
                        hops.append((e, c1, c2, complex(amp * PAULI[sig[a]][c2, c1])))
    z = (0,) * d
    tot, per = 0, {}
    for r in product(range(-k, k + 1), repeat=d):
        if r == z or 2 * sum(abs(t) for t in r) > k:
            continue
        acc = 0
        for ca in range(2):
            for cb in range(2):
                vec = {(z, ca, r, cb): 1}
                for _ in range(k):
                    nv = {}
                    for (x, c1_, y, c2_), am in vec.items():
                        for (e, c1, c2, v) in hops:
                            if c1 == c1_:
                                x2 = tuple(p + q for p, q in zip(x, e))
                                if x2 != y:
                                    nv[(x2, c2, y, c2_)] = nv.get((x2, c2, y, c2_), 0) + am * v
                            if c1 == c2_:
                                y2 = tuple(p + q for p, q in zip(y, e))
                                if y2 != x:
                                    nv[(x, c1_, y2, c2)] = nv.get((x, c1_, y2, c2), 0) + am * v
                    vec = {q: w for q, w in nv.items() if w != 0}
                acc += vec.get((r, cb, z, ca), 0)
        per[r] = gi(acc)
        tot += acc
    return gi(tot), per


H2d, n2 = walk_2H(2, 5, (1, 2))
b2d, H22, P2 = hard_core(H2d)
tr2d = exch_traces(H22, P2, 4)
tr3d = exch_traces(H23, P3, 4)
loc2 = [local_exch(2, (1, 2), k)[0] for k in (2, 3, 4)]
loc3 = [local_exch(3, (1, 2, 3), k)[0] for k in (2, 3)]
t34, per3 = local_exch(3, (1, 2, 3), 4)
ok = tr2d[1] == tr2d[2] == tr3d[1] == tr3d[2] == 0 and loc2[:2] == [0, 0] and loc3 == [0, 0]
ok &= tr2d[3] == n2 * loc2[2] == 25 * (-128) and tr3d[3] == n3 * t34 == 125 * (-384)
nb = [per3[r] for r in per3 if sum(abs(t) for t in r) == 1]
dg = [per3[r] for r in per3 if sum(abs(t) for t in r) == 2 and max(abs(t) for t in r) == 1]
ln = [per3[r] for r in per3 if max(abs(t) for t in r) == 2]
ok &= nb == [-32] * 6 and dg == [-16] * 12 and ln == [0] * 6
need(ok, "D fourth order on Z^2, Z^3")
rec("ok D Z^2 and Z^3 (block 54's walk): tr(P H2^2) = tr(P H2^3) = 0 (no exchange path of 2 hops under exclusion; "
    "odd orders vanish on a bipartite lattice); tr(P H2^4) per site = %s on Z^2 and %s on Z^3 (= -8 per plaquette), "
    "exact on the tori of side 5 (%s, %s) and by local enumeration; per pair (coin-summed <Ps|H2^4|s>): -2 for "
    "neighbours, -1 for face diagonals, 0 at distance 2 on a line"
    % (F(loc2[2], 16), F(t34, 16), F(tr2d[3], 16), F(tr3d[3], 16)))

# (c) the two composition rules differ observably: the sector fourth moments on the 3-torus
M23 = (H23 @ H23).tocsr()
t4all = gi(M23.multiply(M23.T).sum())                      # tr H2^4 = sum_ij (H2^2)_ij (H2^2)_ji
dim3 = H23.shape[0] // 2
m4p, m4m = F(t4all + tr3d[3], 2 * 16 * dim3), F(t4all - tr3d[3], 2 * 16 * dim3)
need(m4p != m4m and F(t4all, 16) > 0, "C sectors differ")
rec("ok C both rules K+ and K- satisfy each axiom sentence (table in ATTEMPT.md: hard-core by construction, "
    "dynamics-closed, covariant, content unchanged) and are different theories: on the 3-torus of side 5, "
    "tr H2^4/dim = %s on K+ against %s on K-" % (m4p, m4m))

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "COUNTEREXAMPLE the exchange sign does not follow from the axioms as stated: the hard-core symmetric and "
      "antisymmetric two-record sectors are both closed, covariant and one-record-per-site; the Cl(3,0) grading "
      "cannot act on a record's content C^2 (its smallest graded module is C^4, the parked M4(C)); the sign first "
      "shows at fourth order on Z^2 and Z^3 (plaquette exchange, -8 per plaquette), at order N on even rings, "
      "never on odd rings."))
if not FAIL:
    print("HIT: two consistent composition rules for two records (hard-core symmetric K+ and hard-core "
          "antisymmetric K-) satisfy every axiom sentence, so the exchange sign is not derivable from Record, "
          "the Qubit axiom's Cl(3,0) presentation or 'no possibility is privileged': no involution of C^2 makes "
          "s1,s2,s3 odd (antilinear candidate c*s2*K squares to -|c|^2), so the grading gives a record no parity.")
    print("HIT: under exclusion the sign is invisible at orders 2 and 3 on Z^2 and Z^3 and first shows at order 4: "
          "tr_{K+}H2^4 - tr_{K-}H2^4 = -8 per plaquette (coin-summed pair exchange -2 for neighbours, -1 for face "
          "diagonals); on rings it is zero below order N, nonzero at N for even N, and K+, K- are unitarily "
          "equivalent (U = (s1(x)s1)(G(x)G)J) for odd N.")
sys.exit(1 if FAIL else 0)
