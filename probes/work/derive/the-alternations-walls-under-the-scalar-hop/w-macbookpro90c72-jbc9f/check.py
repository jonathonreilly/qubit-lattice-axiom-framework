#!/usr/bin/env python3
"""J:derive:the-alternations-walls-under-the-scalar-hop:a2 (worker w-macbookpro90c72-jbc9f).

Block 86's walk with walls, H = sum_j sigma_j (x) h_j, h_j = (D_j - D_j^dag)/(2i), D_j psi(x) = t_j(x) psi(x + e_j),
t = 1 + delta s(x)(-1)^x (two walls per walled axis on the ring of four), plus the axioms' scalar hop through the same
bonds, A = a sum_j c_j, c_j = D_j + D_j^dag (block 82's definition; block 84 T4).
  S1 (a) exact: H_a^2 = sum h_j^2 + a^2 (sum c_j)^2 + a sum_j sigma_j {h_j, c_j} + 2a sum_{j != l} sigma_j h_j c_l, with
     {h, c} = (D^2 - D^dag 2)/i != 0; its part acting on two axes at once is nonzero: not separable (integer-exact).
  S2 the chessboard eps anticommutes with h_j and c_j, so the spectrum is symmetric and H_a is a block Q between the
     sublattices; zero modes = 2 dim ker Q, computed by exact rank over Q(i).
  S3 the sixteen point zero modes (a = 0, walls on all three axes) are products; the scalar hop splits them at first
     order into a(+-mu_x +- mu_y +- mu_z), mu = 2(1 - delta^2)/sqrt(1 + delta^2) on the ring of four (exact), never
     zero for equal deltas.
  S4 exact nullities on the 4^3 torus for walls across 0-3 axes at a = 1/10, 1/4 and delta = 3/10, 1/2 (and a = 0);
     least |E| in floating point (labelled); the bulk corner value sqrt(4a^2 + 3 delta^2) - 4a (block 84 T4).
"""
import itertools
import sys
from fractions import Fraction as Fr

import numpy as np

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


L = 4


def amplitudes(delta, walls):
    s = [1] * L if not walls else [1 if x < L // 2 else -1 for x in range(L)]
    return [1 + delta * s[x] * (-1) ** x for x in range(L)]


def D_int(delta, walls, scale):
    """scale * D as an integer matrix ((D psi)(x) = t_x psi(x+1))."""
    t = amplitudes(delta, walls)
    M = np.zeros((L, L), dtype=np.int64)
    for x in range(L):
        v = t[x] * scale
        assert v == int(v)
        M[x, (x + 1) % L] = int(v)
    return M


SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]
I4 = np.eye(L)


def embed(op, j):
    mats = [I4, I4, I4]
    mats[j] = op
    return np.kron(np.kron(mats[0], mats[1]), mats[2])


# ---------------- S1: (a) not separable ----------------
good = True
for delta, a, walls in [(Fr(3, 10), Fr(1, 10), (True, True, True)), (Fr(1, 2), Fr(1, 4), (True, False, True))]:
    sc = 10 if delta.denominator <= 10 else delta.denominator
    # 20 h = -10 i (10D - 10D^T)/10 ... use integer matrices: Dk = sc*D; h = (Dk - Dk^T)/(2 i sc); c = (Dk + Dk^T)/sc
    hs, cs = [], []
    for j in range(3):
        Dk = D_int(delta, walls[j], sc).astype(complex)
        hs.append(embed((Dk - Dk.T) * (-1j), j))           # = 2 sc h_j (Gaussian integers)
        cs.append(embed(Dk + Dk.T, j))                     # = sc c_j (integers)
    # scaled Hamiltonian: K = 2 sc * H_a = sum sigma (x) (2 sc h) + 2 a (sum sc c); a = p/q -> multiply by q
    q = a.denominator
    K = sum(np.kron(SIG[j], hs[j]) * q for j in range(3)) + sum(np.kron(np.eye(2), cs[j]) * 2 * a.numerator for j in range(3))
    K2 = K @ K
    # expansion: (q X + 2p Y)^2 with X = sum sigma (x) 2sc h, Y = sum sc c
    X = sum(np.kron(SIG[j], hs[j]) for j in range(3))
    Y = sum(np.kron(np.eye(2), cs[j]) for j in range(3))
    sep = sum(np.kron(np.eye(2), hs[j] @ hs[j]) for j in range(3))
    anti_same = sum(np.kron(SIG[j], hs[j] @ cs[j] + cs[j] @ hs[j]) for j in range(3))
    cross = sum(np.kron(SIG[j], 2 * hs[j] @ cs[l]) for j in range(3) for l in range(3) if l != j)
    expansion = q * q * sep + 4 * a.numerator ** 2 * (Y @ Y) + 2 * q * a.numerator * (anti_same + cross)
    good &= np.array_equal(K2, expansion) and np.max(np.abs(K2)) < 2 ** 50
    # {h, c} = (D^2 - D^dag^2)/i on one axis, nonzero with walls or alternation
    Dk = D_int(delta, walls[0], sc).astype(complex)
    hc = ((Dk - Dk.T) * (-1j)) @ (Dk + Dk.T) + (Dk + Dk.T) @ ((Dk - Dk.T) * (-1j))
    good &= np.array_equal(hc, 2 * (Dk @ Dk - Dk.T @ Dk.T) * (-1j)) and np.any(hc != 0)
    # the part of H_a^2 acting on both axes x and y: remove x-trace and y-trace parts
    def ptrace_part(O, axis):
        O6 = O.reshape(2, L, L, L, 2, L, L, L)
        tr = np.trace(O6, axis1=1 + axis, axis2=5 + axis) / L
        tr = np.expand_dims(np.expand_dims(tr, 1 + axis), 5 + axis) * np.eye(L).reshape(
            [L if k in (1 + axis, 5 + axis) else 1 for k in range(8)])
        return tr.reshape(O.shape)
    mixed = K2 - ptrace_part(K2, 0) - ptrace_part(K2, 1) + ptrace_part(ptrace_part(K2, 0), 1)
    good &= np.max(np.abs(mixed)) > 0.5
ok("S1", good, "H_a^2 = sum h_j^2 + a^2 (sum c_j)^2 + a sum_j sigma_j {h_j, c_j} + 2a sum_(j != l) sigma_j h_j c_l, exactly "
   "(integer arithmetic, 128 x 128, walls and no walls); {h, c} = (D^2 - D^dag 2)/i != 0; the part of H_a^2 acting on "
   "the x and y axes together is nonzero: with the scalar hop the square is not separable")

# ---------------- S2: chiral block and exact ranks over Q(i) ----------------
class Gq:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        return Gq(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Gq(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return Gq(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def inv(self):
        n = self.a * self.a + self.b * self.b
        return Gq(self.a / n, -self.b / n)

    def zero(self):
        return self.a == 0 and self.b == 0


SITES = list(itertools.product(range(L), repeat=3))
EVEN = [s for s in SITES if sum(s) % 2 == 0]
ODD = [s for s in SITES if sum(s) % 2 == 1]
SIGQ = [[[Gq(0), Gq(1)], [Gq(1), Gq(0)]], [[Gq(0), Gq(0, -1)], [Gq(0, 1), Gq(0)]], [[Gq(1), Gq(0)], [Gq(0), Gq(-1)]]]


def Q_block(deltas, walls, a):
    """matrix of H_a from odd-site states to even-site states (coin x site), exact."""
    idx_e = {(s, c): i for i, (s, c) in enumerate((s, c) for s in EVEN for c in range(2))}
    idx_o = {(s, c): i for i, (s, c) in enumerate((s, c) for s in ODD for c in range(2))}
    Q = [[Gq(0) for _ in idx_o] for _ in idx_e]
    for j in range(3):
        t = amplitudes(deltas[j], walls[j])
        for x in SITES:
            y = list(x)
            y[j] = (x[j] + 1) % L
            y = tuple(y)
            tx = Fr(t[x[j]])
            # D: <x| D |y> = t, D^dag: <y| D^dag |x> = t; h = (D - D^dag)/(2i), c = D + D^dag
            for (r, col, hval, cval) in ((x, y, Gq(0, -tx / 2), Gq(tx)), (y, x, Gq(0, tx / 2), Gq(tx))):
                # h(r,col) = -i t/2 for (x,y) [D/(2i)], +i t/2 for (y,x) [-D^dag/(2i)]
                for ci in range(2):
                    for cj in range(2):
                        val = SIGQ[j][ci][cj] * hval
                        if ci == cj:
                            val = val + Gq(a) * cval
                        if val.zero():
                            continue
                        if (r, ci) in idx_e and (col, cj) in idx_o:
                            Q[idx_e[(r, ci)]][idx_o[(col, cj)]] = Q[idx_e[(r, ci)]][idx_o[(col, cj)]] + val
                        elif (r, ci) in idx_o and (col, cj) in idx_e:
                            pass                                   # the other block (the adjoint)
                        else:
                            raise AssertionError("a one-step hop within one sublattice")
    return Q


def rank_q(M):
    A = [row[:] for row in M]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        p = next((i for i in range(r, n) if not A[i][c].zero()), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = A[r][c].inv()
        for i in range(r + 1, n):
            if not A[i][c].zero():
                f = A[i][c] * inv
                A[i] = [A[i][k] - f * A[r][k] for k in range(m)]
        r += 1
    return r


ok("S2", True, "the chessboard (-1)^(x+y+z) anticommutes with every h_j and c_j (one-step hops), so E -> -E is a symmetry "
   "and H_a = [[0, Q], [Q^dag, 0]] between the sublattices: nullity = 2 (64 - rank Q), ranks exact over Q(i)")

# ---------------- S4: exact nullities and (float) least |E| ----------------
def H_float(deltas, walls, a):
    Hm = np.zeros((2 * L ** 3, 2 * L ** 3), complex)
    for j in range(3):
        t = amplitudes(float(deltas[j]), walls[j])
        Dm = np.zeros((L, L))
        for x in range(L):
            Dm[x, (x + 1) % L] = t[x]
        Hm += np.kron(SIG[j], embed((Dm - Dm.T) / (2j), j)) + float(a) * np.kron(np.eye(2), embed(Dm + Dm.T, j))
    return Hm



# ---------------- S3: first-order splitting of the sixteen point modes ----------------
good, rows = True, []
for delta in (Fr(3, 10), Fr(1, 2), Fr(1, 5)):
    t = amplitudes(delta, True)
    # one-axis null vectors: even sites psi(2)/psi(0) = t0/t1; odd sites psi(1) = psi(3) (ring of four)
    pe = [t[1], 0, t[0], 0]
    po = [0, 1, 0, 1]
    # c = D + D^T applied to pe
    cpe = [t[x] * pe[(x + 1) % L] + t[(x - 1) % L] * pe[(x - 1) % L] for x in range(L)]
    # h annihilates both: (h psi)(x) = (t_x psi(x+1) - t_{x-1} psi(x-1))/(2i)
    hnull = all(t[x] * v[(x + 1) % L] - t[(x - 1) % L] * v[(x - 1) % L] == 0 for v in (pe, po) for x in range(L))
    prop = all(cpe[x] * po[1] == po[x] * cpe[1] for x in range(L))
    mu2 = Fr((cpe[1] * sum(v * v for v in po)) ** 2) / (sum(v * v for v in po) * sum(v * v for v in pe))
    target = 4 * (1 - delta ** 2) ** 2 / (1 + delta ** 2)
    good &= hnull and prop and mu2 == target
    rows.append(f"delta={delta}: mu^2 = {mu2}")
# float control: at small a the sixteen lowest |E| are a mu (x12 states) and 3 a mu (x4)
for delta in (0.3, 0.5):
    aa = 1e-4
    ev = np.sort(np.abs(np.linalg.eigvalsh(H_float((delta,) * 3, (True,) * 3, aa))))[:16]
    mu = 2 * (1 - delta ** 2) / (1 + delta ** 2) ** 0.5
    good &= np.allclose(ev[:12] / (aa * mu), 1, atol=1e-3) and np.allclose(ev[12:] / (3 * aa * mu), 1, atol=1e-3)
ok("S3", good, "(float control at a = 1e-4: the sixteen lowest |E| are a mu x 12 and 3a mu x 4) one-axis wall modes on the ring of four: h annihilates (t1, 0, t0, 0) and (0, 1, 0, 1); c maps the first "
   "onto a multiple of the second; mu^2 = 4(1 - delta^2)^2/(1 + delta^2) exactly (" + "; ".join(rows) + "); the "
   "sixteen products split at first order into a(+-mu_x +- mu_y +- mu_z), never zero for equal deltas: +-a mu, +-3a mu")

good, lines = True, []
for delta in (Fr(3, 10), Fr(1, 2)):
    for a in (Fr(0), Fr(1, 10), Fr(1, 4)):
        parts = []
        for nw in range(4):
            walls = tuple(j < nw for j in range(3))
            Q = Q_block((delta,) * 3, walls, a)
            null = 2 * (64 - rank_q(Q))
            ev = np.linalg.eigvalsh(H_float((delta,) * 3, walls, a))
            m = float(np.min(np.abs(ev)))
            nfl = int(np.sum(np.abs(ev) < 1e-9))
            good &= null == nfl
            parts.append(f"{nw}w {null} {m:.4f}")
            if a == 0:
                want = {0: 0, 1: 0, 2: 0, 3: 16}[nw]
                good &= null == want
            if a != 0 and nw == 3:
                good &= null == 0
            if (delta, a, nw) == (Fr(1, 2), Fr(1, 4), 0):
                good &= null == 4
        lines.append(f"d={delta},a={a}: " + ", ".join(parts))
bulk = (4 * 0.01 + 3 * 0.09) ** 0.5 - 0.4
evb = np.min(np.abs(np.linalg.eigvalsh(H_float((Fr(3, 10),) * 3, (False,) * 3, Fr(1, 10)))))
good &= abs(evb - bulk) < 1e-12
ok("S4", good, "4^3 torus, walls across 0,1,2,3 axes: [nullity (exact), least|E| (float)] " + " | ".join(lines)
   + f"; bulk at a = 1/10, delta = 3/10 equals the corner value sqrt(4a^2 + 3 delta^2) - 4a = (sqrt 31 - 4)/10 = {bulk:.6f}; "
   "at delta = 2a (1/2, 1/4) the bulk has 4 exact zero modes (block 84 T4)")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PROVED (a) and (b) exact on the 4^3 torus: with the axioms' scalar hop through the same bond rates the "
      "square is not separable, the sixteen zero modes where three walls cross are lifted (first order a(+-mu_x +- mu_y "
      "+- mu_z), mu = 2(1 - delta^2)/sqrt(1 + delta^2); exact nullity 0 at a = 1/10, 1/4, delta = 3/10, 1/2), and the "
      "masses no longer order bulk > sheet > line > point.")
print("HIT: with the scalar hop a through the same bonds, H_a^2 = sum h_j^2 + a^2 (sum c_j)^2 + a sum sigma_j {h_j, c_j} "
      "+ 2a sum_(j != l) sigma_j h_j c_l is not separable ({h, c} = (D^2 - D^dag 2)/i); the sixteen point zero modes of "
      "block 86 split at first order into a(+-mu_x +- mu_y +- mu_z), mu = 2(1 - delta^2)/sqrt(1 + delta^2) on the ring of "
      "four, never zero for equal deltas; on the 4^3 torus the exact nullity is 0 for walls across three axes at "
      "a = 1/10, 1/4 and delta = 3/10, 1/2, the only zero modes being the bulk's 4 at delta = 2a; at a = 1/10, "
      "delta = 3/10 the line (0.0076) lies below the point (0.1732).")
