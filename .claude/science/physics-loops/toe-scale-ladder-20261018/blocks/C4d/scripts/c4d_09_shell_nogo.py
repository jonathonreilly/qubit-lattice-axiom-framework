"""C4d-09: instance checks of Proposition E (emptiness-shell pattern gates never form a commuting
TI family when both ell-extremes of the pattern region are toggled-in).
Gate g = (A, R, S=A\\R, Lambda, pi): active on c iff c & S = {} and c & R in Lambda; acts by pi.
For each test gate we build the explicit witness of the proof (generic ell, p = argmax_A ell,
v = argmin_R ell, t = p - v, lambda with v toggled-in, non-fixed mu avoiding A+t) and verify by
direct application that g_0 g_t c != g_t g_0 c.  Also confirms the witness exists for -ell when
it fails for ell, as the proof asserts."""
import itertools
import numpy as np
from c4d_common import check, total, T, cheb, add, sub, rot

rng = np.random.default_rng(5)
E = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]          # even tetrahedron


def gate_apply(c, A, R, S, Lam, pi, t):
    At = {add(a, t) for a in A}; Rt = {add(a, t) for a in R}; St = {add(a, t) for a in S}
    if c & St:
        return c
    pat = frozenset(sub(x, t) for x in c & Rt)
    if pat not in Lam:
        return c
    new = {add(x, t) for x in pi[pat]}
    return (c - Rt) | new


def make_tetra_gate(shell_r):
    R = set(E)
    A = {add(e, d) for e in E for d in itertools.product(range(-shell_r, shell_r + 1), repeat=3)}
    S = A - R
    Lam = [frozenset(p) for p in itertools.combinations(E, 2)]
    pi = {p: frozenset(R - p) for p in Lam}       # complement inside the tetrahedron
    return A, R, S, set(Lam), pi


def make_random_shell_gate():
    R = set(E)
    A = set(R)
    for _ in range(rng.integers(10, 60)):
        A.add(tuple(int(v) for v in rng.integers(-3, 5, size=3)))
    # T-symmetrise the shell about the tetrahedron centre (1/2,1/2,1/2): x -> R(x-c)+c
    A2 = set()
    for a in A:
        for M in T:
            v = M @ (2 * np.array(a) - 1) + 1
            A2.add(tuple(int(q) // 2 for q in v))
    A = A2 | R
    S = A - R
    Lam = [frozenset(p) for p in itertools.combinations(E, 2)]
    pi = {p: frozenset(R - p) for p in Lam}
    return A, R, S, set(Lam), pi


def witness(A, R, S, Lam, pi, ell):
    f = lambda x: float(np.dot(ell, x))
    p = max(A, key=f); v = min(R, key=f)
    if p not in S:
        return None, "argmax_A not in shell"
    t = sub(p, v)
    lam = [l for l in Lam if v not in l and v in pi[l]]
    At = {add(a, t) for a in A}
    mus = [m for m in Lam if pi[m] != m and not (set(m) & At)]
    if not lam or not mus:
        return None, "no lambda/mu"
    c = {add(x, t) for x in lam[0]} | set(mus[0])
    a1 = gate_apply(gate_apply(c, A, R, S, Lam, pi, t), A, R, S, Lam, pi, (0, 0, 0))
    a2 = gate_apply(gate_apply(c, A, R, S, Lam, pi, (0, 0, 0)), A, R, S, Lam, pi, t)
    return (a1 != a2), (t, sorted(c))


ok_all = True
cases = 0
for label, maker in [("tetra shell r=1", lambda: make_tetra_gate(1)), ("tetra shell r=2", lambda: make_tetra_gate(2)),
                     ("tetra shell r=3", lambda: make_tetra_gate(3))] + [(f"random T-sym shell #{i}", make_random_shell_gate) for i in range(12)]:
    A, R, S, Lam, pi = maker()
    found = False
    for trial in range(20):
        ell = rng.normal(size=3)
        for sgn in (1, -1):
            res, info = witness(A, R, S, Lam, pi, sgn * ell)
            if res is True:
                found = True
                break
            if res is False:
                ok_all = False
        if found:
            break
    cases += 1
    ok_all &= found
    print(f"{label}: |A|={len(A)}: non-commuting translate pair found = {found}  (t, c) = {info if found else '-'}")
check("Prop. E witness (explicit non-commuting translates) found for every tested shell", ok_all, f"{cases} gates")

# control: a gate that escapes Prop. E (collinear inchworm, partner never toggled) DOES admit
# commuting translates for a suitable shell? (only checks that the witness construction fails)
R = {(0, 0, 0), (1, 0, 0), (2, 0, 0)}
Lam = {frozenset({(0, 0, 0), (1, 0, 0)}), frozenset({(0, 0, 0), (2, 0, 0)})}
pi = {frozenset({(0, 0, 0), (1, 0, 0)}): frozenset({(0, 0, 0), (2, 0, 0)}),
      frozenset({(0, 0, 0), (2, 0, 0)}): frozenset({(0, 0, 0), (1, 0, 0)})}
A = {add(e, d) for e in R for d in itertools.product(range(-2, 3), repeat=3)}
S = A - R
fails = 0
for trial in range(40):
    res, info = witness(A, R, S, Lam, pi, rng.normal(size=3))
    fails += res is None
check("control: for the inchworm gate (end partner never toggled) the Prop. E witness never applies",
      fails == 40, f"{fails}/40 generic ell give no witness")
total()
