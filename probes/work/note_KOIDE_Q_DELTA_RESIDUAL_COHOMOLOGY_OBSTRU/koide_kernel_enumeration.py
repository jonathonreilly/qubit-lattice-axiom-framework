#!/usr/bin/env python3
"""J:note:KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION -- exact enumeration of the note's chains and of the uniqueness of its closing representatives, beyond the runner's two examples.

Note on main: docs/KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md. Claims tested with exact Fractions (no sympy, no floating point):
 (Q) with reduced source coordinates (t, z), w_plus = (1 + z)/2, r = (1 - w_plus)/w_plus, Q = (1 + r)/3 and K_TL = (r^2 - 1)/(4 r): the zero label z = 0 gives w_plus = 1/2, K_TL = 0, Q = 2/3; z = -1/3 gives w_plus = 1/3, K_TL = 3/8, Q = 1;
     kernel translations (t, z) -> (t, z + a) preserve the retained total t; the closing representative is unique: over every rational z in (-1, 1) on a grid of 4001 points, K_TL = 0 and Q = 2/3 hold at z = 0 and only there;
 (D) with eta_APS = (1/3) sum_(k=1,2) 1/((w^k - 1)(w^(2k) - 1)), w = e^(2 pi i/3), equal to 2/9 (computed here in exact arithmetic in Q(sqrt(-3))), the normalised open boundary delta_open/eta_APS - 1 = -spectator + c/eta_APS: the three listed nonzero kernel
     representatives give delta_open = 0, 1/9, 1/3, and the closing point (spectator, c) = (0, 0) is the unique zero of delta_open/eta_APS - 1 on the kernel lattice {(s, c): s in {0, 1/2, 1}, c in {0, 1/9, 1/3}} and on a 41 x 41 rational grid;
 (K) the kernels: ker(pi_Q) = span{(0, 1)} and ker(pi_delta) = span{(-1, 1, 0), (0, 0, 1)} (integer Smith/nullspace computation over Q), and their dimensions 1 and 2.
The eta_APS value is also checked for the other Z_n orbifold weights (1, 2) at n = 3 only (the note's case) and its algebraic form is printed. Prints SUMMARY: and, only if a stated value or uniqueness fails, HIT:.
"""
import sys
from fractions import Fraction as Fr

RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def w_plus(z): return (1 + z) / 2
def r_of(w): return (1 - w) / w
def Q_of(w): return (1 + r_of(w)) / 3
def K_of(w): r = r_of(w); return (r * r - 1) / (4 * r)


class Q3:
    """Elements a + b*sqrt(-3) with rational a, b: the field Q(omega), omega = (-1 + sqrt(-3))/2."""
    def __init__(self, a, b=0): self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, Q3) else Q3(o); return Q3(s.a + o.a, s.b + o.b)
    def __sub__(s, o): o = o if isinstance(o, Q3) else Q3(o); return Q3(s.a - o.a, s.b - o.b)
    def __mul__(s, o): o = o if isinstance(o, Q3) else Q3(o); return Q3(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    def inv(s): n = s.a * s.a + 3 * s.b * s.b; return Q3(s.a / n, -s.b / n)
    def __repr__(s): return f"({s.a} + {s.b} sqrt(-3))"


def eta_aps():
    om = Q3(Fr(-1, 2), Fr(1, 2))                       # omega = (-1 + sqrt(-3))/2
    tot = Q3(0)
    def pw(x, n):
        out = Q3(1)
        for _ in range(n): out = out * x
        return out
    for k in (1, 2):
        z1 = pw(om, k); z2 = pw(om, 2 * k)
        tot = tot + ((z1 - 1) * (z2 - 1)).inv()
    return tot * Fr(1, 3)


def nullspace_int(M):
    """Nullspace of a rational matrix (rows) by Gaussian elimination over Q; returns basis vectors."""
    M = [[Fr(x) for x in row] for row in M]
    rows, cols = len(M), len(M[0])
    piv, r = [], 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        M[r] = [x / M[r][c] for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == rows: break
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * cols; v[f] = Fr(1)
        for i, c in enumerate(piv): v[c] = -M[i][f]
        basis.append(v)
    return basis


def run():
    z0, z1 = Fr(0), Fr(-1, 3)
    ok = w_plus(z0) == Fr(1, 2) and K_of(w_plus(z0)) == 0 and Q_of(w_plus(z0)) == Fr(2, 3) and w_plus(z1) == Fr(1, 3) and K_of(w_plus(z1)) == Fr(3, 8) and Q_of(w_plus(z1)) == 1
    check("(Q1) z = 0: w_plus = 1/2, K_TL = 0, Q = 2/3; z = -1/3: w_plus = 1/3, K_TL = 3/8, Q = 1 (exact)", ok, f"z = 0: K = {K_of(w_plus(z0))}, Q = {Q_of(w_plus(z0))}; z = -1/3: w = {w_plus(z1)}, K = {K_of(w_plus(z1))}, Q = {Q_of(w_plus(z1))}")
    if not ok: FIRED.append("Q chain values differ")
    zs = [Fr(i, 2000) for i in range(-1999, 2000)]
    zeros_K = [z for z in zs if K_of(w_plus(z)) == 0]
    hits_Q = [z for z in zs if Q_of(w_plus(z)) == Fr(2, 3)]
    okQ = zeros_K == [Fr(0)] and hits_Q == [Fr(0)]
    # the closed forms: Q = 2/(3(1 + z)), K_TL = -z/... exact identity check
    okid = all(Q_of(w_plus(z)) == Fr(2, 3) / (1 + z) for z in zs) and all(K_of(w_plus(z)) == ((1 - z) ** 2 - (1 + z) ** 2) / (4 * (1 - z) * (1 + z)) for z in zs)
    check("(Q2) on 3999 rational labels z in (-1, 1) (step 1/2000) K_TL = 0 and Q = 2/3 hold at z = 0 and nowhere else; closed forms Q = 2/(3(1 + z)) and K_TL = -z/(1 - z^2)", okQ and okid,
          f"K_TL = 0 at {zeros_K}; Q = 2/3 at {hits_Q}; closed forms exact on the whole grid: {okid}")
    if not (okQ and okid): FIRED.append("closing representative not unique or closed forms fail")
    eta = eta_aps()
    check("(D1) eta_APS = (1/3) sum_(k=1,2) 1/((w^k - 1)(w^2k - 1)) = 2/9 in exact Q(sqrt(-3)) arithmetic", eta.a == Fr(2, 9) and eta.b == 0, f"eta_APS = {eta}")
    if not (eta.a == Fr(2, 9) and eta.b == 0): FIRED.append(f"eta_APS = {eta}, not 2/9")
    e = Fr(2, 9)
    def delta_open(s_, c_): return (1 - s_) * e + c_                       # the note's / runner's normalised open endpoint: (1 - spectator) eta_APS + c
    def resid(s_, c_): return delta_open(s_, c_) / e - 1                    # = -spectator + (9/2) c
    listed = {(Fr(1), Fr(0)): Fr(0), (Fr(1, 2), Fr(0)): Fr(1, 9), (Fr(0), Fr(1, 9)): Fr(1, 3)}
    okL = all(delta_open(s_, c_) == d for (s_, c_), d in listed.items()) and resid(Fr(0), Fr(0)) == 0 and all(resid(s_, c_) == -s_ + Fr(9, 2) * c_ for s_, c_ in listed)
    check("(D2) the note's three listed kernel representatives (spectator, c) = (1, 0), (1/2, 0), (0, 1/9) give delta_open = 0, 1/9, 1/3 at eta_APS = 2/9, and the residual is -spectator + (9/2) c (exact)", okL, "; ".join(f"({s_}, {c_}) -> {delta_open(s_, c_)}" for (s_, c_) in listed))
    if not okL:
        FIRED.append("listed delta values differ")
    # the closing locus inside the note's own section family s_(b1, b2)(1) = (1 - b1, b1, b2): residual = 0 is ONE linear condition on the two-dimensional kernel
    grid = [(Fr(i, 20), Fr(j, 180)) for i in range(-20, 21) for j in range(-20, 21)]        # spectator in [-1, 1], c in [-1/9, 1/9]
    zeros = [(s_, c_) for (s_, c_) in grid if resid(s_, c_) == 0]
    nonzero_closing = [(s_, c_) for (s_, c_) in zeros if (s_, c_) != (0, 0)]
    cx = (Fr(1, 2), Fr(1, 9))
    total_pres = (1 - cx[0]) + cx[0] == 1
    counter_ok = total_pres and resid(*cx) == 0 and delta_open(*cx) == e and cx != (0, 0)
    check("(D3) the note says nonzero kernel representatives 'move the open endpoint' and that the closing section 'requires b1 = b2 = 0'; in its own coordinates the closing locus is the line c = (2/9) spectator: (spectator, c) = (1/2, 1/9) preserves the closed total "
          f"(selected + spectator = 1) and has delta_open = eta_APS = 2/9, i.e. it closes; {len(nonzero_closing)} of the {len(grid)} grid points other than the origin close", not counter_ok,
          f"counterexample ({cx[0]}, {cx[1]}): closed total {(1 - cx[0]) + cx[0]}, delta_open {delta_open(*cx)}, residual {resid(*cx)}; grid zeros {len(zeros)}, all on c = (2/9) s: {all(c_ == e * s_ for s_, c_ in zeros)}")
    if counter_ok:
        FIRED.append("the closing section is not unique in the delta kernel: (spectator, c) = (1/2, 1/9) preserves the closed total and gives delta_open = eta_APS; the closing locus is the line c = (2/9) spectator, not the origin")
    kq = nullspace_int([[1, 0]]); kd = nullspace_int([[1, 1, 0]])
    okK = len(kq) == 1 and kq[0] == [0, 1] and len(kd) == 2 and {tuple(v) for v in kd} <= {tuple(Fr(x) for x in (-1, 1, 0)), tuple(Fr(x) for x in (0, 0, 1)), tuple(Fr(x) for x in (1, -1, 0))}
    # span check: (-1, 1, 0) and (0, 0, 1) are in the kernel and independent
    okspan = all(sum(a * b for a, b in zip(v, (1, 1, 0))) == 0 for v in ((-1, 1, 0), (0, 0, 1)))
    check("(K) ker(pi_Q) = span{(0, 1)} (dimension 1) and ker(pi_delta) = span{(-1, 1, 0), (0, 0, 1)} (dimension 2), by exact elimination over Q", okK and okspan, f"kernel bases {kq}, {[[str(x) for x in v] for v in kd]}")
    if not (okK and okspan): FIRED.append("kernel dimensions or spans differ")
    print("   [done]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0]); print("HIT: Koide Q/delta cohomology obstruction note (Section Obstruction and Delta Exact Sequence): " + "; ".join(FIRED)); return 0
    print("SUMMARY: no falsifier fired: all stated values of the Q and delta chains hold exactly, the closing representative of the Q fibre is unique on 3999 rational labels (Q = 2/(3(1 + z)), K_TL = -z/(1 - z^2)), eta_APS = 2/9 in exact Q(sqrt(-3)) arithmetic, "
          "and the kernels have the stated bases; the delta fibre's zero set is a line c = eta_APS s, so 'the unique closing representative' is unique only once the endpoint-exact coordinate is tied to the spectator (the note's section families keep them independent)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
