#!/usr/bin/env python3
"""GL(F) record-value dictionary commuting lock — exact finite check.

Class-A finite-dimensional runner. Everything is exact (sympy Rational /
Gaussian rationals / symbolic lam); no floats anywhere.

Objects (all declared here; no external authority consumed):

  * Record-configuration measures: on a finite graph Lambda with edge set E,
    the probability measure on (S^2)^Lambda with density
    D = prod_{(x,y) in E} (1 + lam * v_x . v_y) against the product uniform
    measure (a probability density for -1 <= lam <= 1).
  * Record-value dictionary: psi_x |-> F_x = (v_x^1 + i v_x^2)/2, a
    complex-valued FUNCTION of the site-x record value (the sigma_+ Bloch
    coordinate: F_x = tr(sigma_+ rho(v_x)) for rho(v) = (I + v.sigma)/2).
  * Functional-level GL(F) (annihilation criterion): the induced functional
    W on words in {psi_x, psi_x^dag} passes iff it annihilates EVERY
    word-sandwiched cross-site anticommutator insertion
    W(u {psi_x, psi_y^#} w) = 0, x != y.
  * Graded comparator: Jordan-Wigner family c_x on (C^2)^{otimes N}
    (exact integer matrices).

Checks:
  [A] exact uniform-S^2 monomial moments (self-test against closed forms);
  [B] the commuting lock: for record-value dictionaries the sandwiched
      anticommutator functional equals exactly 2x the sandwiched product
      functional (verified on exact integrals AND as an operator identity
      for the cross-site qubit ladders), so GL(F)-annihilation forces every
      cross-site two-point to vanish;
  [C] nonvanishing witnesses: exact cross-site two-points lam/18 (edge),
      lam^2/54 (distance-2), lam^2-coefficient 1/27 (square diagonal, two
      paths), all nonzero for lam != 0; the lam=0 product point kills every
      two-point AND still fails the sandwiched criterion at exact value 1/18
      unless the dictionary is a.e. trivial;
  [D] cross-route consistency: the classical moment functional equals the
      induced separable qubit state evaluated on the hard-core ladders;
  [E] graded coexistence: exact CAR for the JW family (anticommutator
      insertions vanish as OPERATOR identities, hence in every state) while
      an explicit state carries cross-site two-point exactly 1/2.

Prints one line per check; ends with TOTAL: PASS=N FAIL=0.
"""

from sympy import (Rational, Symbol, I, Matrix, eye, zeros, expand, cancel,
                   factorial2, conjugate, series, simplify)

PASS = 0
FAIL = 0


def check(label, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


lam = Symbol('lam')

# ---------------------------------------------------------------- sites ----
MAXN = 4
V = [[Symbol(f'v{x}_{i}', real=True) for i in range(3)] for x in range(MAXN)]
ALLV = [s for row in V for s in row]


def moment1(exps):
    """Exact uniform-S^2 moment of v1^a v2^b v3^c (normalized measure)."""
    a, b, c = exps
    if a % 2 or b % 2 or c % 2:
        return Rational(0)
    num = factorial2(a - 1) * factorial2(b - 1) * factorial2(c - 1)
    return Rational(num, factorial2(a + b + c + 1))


def integrate_uniform(expr):
    """Integrate a polynomial in the site variables against the product
    uniform S^2 measure, exactly, monomial by monomial."""
    expr = expand(expr)
    total = Rational(0)
    terms = expr.as_ordered_terms() if expr.is_Add else [expr]
    for term in terms:
        coeff, mono = term.as_independent(*ALLV, as_Mul=True)
        powers = mono.as_powers_dict()
        val = coeff
        for x in range(MAXN):
            exps = [int(powers.get(V[x][i], 0)) for i in range(3)]
            val *= moment1(exps)
        total += val
    return total


def dot(x, y):
    return sum(V[x][i] * V[y][i] for i in range(3))


def density(edges):
    d = 1
    for (x, y) in edges:
        d = expand(d * (1 + lam * dot(x, y)))
    return d


def W(expr, edges):
    """Moment functional of the pair-weight measure: normalized."""
    D = density(edges)
    Z = integrate_uniform(D)
    return cancel(integrate_uniform(expand(expr * D)) / Z)


def F(x):
    return (V[x][0] + I * V[x][1]) / 2


def Fb(x):
    return (V[x][0] - I * V[x][1]) / 2


# ------------------------------------------------------- [A] moment tests --
check("A1 moment <1> = 1", moment1((0, 0, 0)) == 1)
check("A2 moment <v3^2> = 1/3", moment1((0, 0, 2)) == Rational(1, 3))
check("A3 moment <v3^4> = 1/5", moment1((0, 0, 4)) == Rational(1, 5))
check("A4 moment <v1^2 v2^2> = 1/15", moment1((2, 2, 0)) == Rational(1, 15))
check("A5 odd moment vanishes", moment1((1, 2, 0)) == 0)

P2 = [(0, 1)]
P3 = [(0, 1), (1, 2)]
C4 = [(0, 1), (1, 2), (2, 3), (3, 0)]

check("A6 Z(P2) = 1", integrate_uniform(density(P2)) == 1)
check("A7 Z(P3) = 1", integrate_uniform(density(P3)) == 1)
ZC4 = integrate_uniform(density(C4))
check("A8 Z(C4)|lam=0 = 1", ZC4.subs(lam, 0) == 1)
print(f"  Z(C4) = {ZC4}")

# ------------------------------------------- [B] the commuting lock (2x) ---
# Functional level: sandwiched anticommutator = 2 * sandwiched product,
# exactly, because record-value dictionaries multiply pointwise.
nz = (1 + V[2][2]) / 2          # F-even sandwich: occupation-like at site 2
sandwiches = [(1, 1), (nz, 1), (Fb(0) * F(1), 1), (1, nz)]
labels = ["u=w=1", "u=n_2", "u=Fb0*F1", "w=n_2"]
for (u, w), lab in zip(sandwiches, labels):
    lhs = W(u * (F(0) * Fb(1) + Fb(1) * F(0)) * w, P3)
    rhs = 2 * W(u * F(0) * Fb(1) * w, P3)
    check(f"B lock {lab}: W(u{{psi0,psi1^dag}}w) = 2 W(u psi0 psi1^dag w)",
          simplify(lhs - rhs) == 0)

# Operator level: cross-site qubit ladders commute, so the anticommutator IS
# twice the product as a matrix identity (and it is NOT the zero operator).
s_p = Matrix([[0, 1], [0, 0]])
s_m = Matrix([[0, 0], [1, 0]])
s3 = Matrix([[1, 0], [0, -1]])
id2 = eye(2)


def kron(*ms):
    out = Matrix([[1]])
    for m in ms:
        out = Matrix([[out[i, j] * m[k, l] for j in range(out.cols)
                       for l in range(m.cols)]
                      for i in range(out.rows) for k in range(m.rows)])
    return out


A0 = kron(s_p, id2)
B1 = kron(id2, s_m)
anti = A0 * B1 + B1 * A0
check("B op: {sp^0, sm^1} = 2 sp^0 sm^1 (matrix identity)",
      anti == 2 * A0 * B1)
check("B op: {sp^0, sm^1} != 0 (nonzero operator)", anti != zeros(4, 4))

# --------------------------------- [C] nonvanishing two-point witnesses ----
tp_edge = W(F(0) * Fb(1), P2)
check("C1 edge two-point = lam/18", simplify(tp_edge - lam / 18) == 0)
check("C2 edge mixed anticommutator = lam/9 != 0 at lam=1/2",
      W(F(0) * Fb(1) + Fb(1) * F(0), P2).subs(lam, Rational(1, 2))
      == Rational(1, 18))
check("C3 same-type anticommutator W({psi0,psi1}) = 0 (U(1) base symmetry)",
      simplify(W(2 * F(0) * F(1), P2)) == 0)
tp_far = W(F(0) * Fb(2), P3)
check("C4 distance-2 two-point = lam^2/54", simplify(tp_far - lam**2 / 54) == 0)
tp_diag = W(F(0) * Fb(2), C4)
c2 = tp_diag.series(lam, 0, 3).removeO().coeff(lam, 2)
check("C5 square-diagonal lam^2 coefficient = 1/27 (two paths add)",
      c2 == Rational(1, 27))
check("C6 square-diagonal two-point != 0 at lam=1/2",
      tp_diag.subs(lam, Rational(1, 2)) != 0)
print(f"  square-diagonal two-point = {simplify(tp_diag)}")

# lam=0 product point: every cross-site two-point dies...
check("C7 lam=0: edge two-point = 0", tp_edge.subs(lam, 0) == 0)
check("C8 lam=0: distance-2 two-point = 0", tp_far.subs(lam, 0) == 0)
# ...but the sandwiched annihilation criterion still fails unless the
# dictionary is a.e. trivial: the witness value is 2*Int(|F0|^2 |F1|^2) > 0.
sand = W(Fb(0) * F(1) * (F(0) * Fb(1) + Fb(1) * F(0)), P2)
check("C9 sandwiched anticommutator = 2|F|^2x|F|^2 = 1/18, ALL lam (P2)",
      simplify(sand - Rational(1, 18)) == 0)
check("C10 sandwiched witness nonzero at lam=0",
      sand.subs(lam, 0) == Rational(1, 18))

# --------------------------- [D] qubit-state cross-route (independent) -----
sig = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), s3]


def site_rho(x):
    m = zeros(2, 2)
    for i in range(3):
        m += V[x][i] * sig[i]
    return (id2 + m) / 2


for (edges, n, lab) in [(P2, 2, "P2"), (P3, 3, "P3")]:
    T = kron(*[site_rho(x) for x in range(n)])
    D = density(edges)
    Z = integrate_uniform(D)
    R = T.applyfunc(lambda e: integrate_uniform(expand(e * D))) / Z
    check(f"D {lab}: induced state has exact unit trace",
          simplify(R.trace() - 1) == 0)
    ops = [s_p if k == 0 else (s_m if k == n - 1 else id2) for k in range(n)]
    O = kron(*ops)
    cls = W(F(0) * Fb(n - 1), edges)
    check(f"D {lab}: tr(rho_lam sp^0 sm^{n-1}) = classical two-point",
          simplify((R * O).trace() - cls) == 0)

# ------------------------------------- [E] graded (JW/CAR) coexistence -----
N = 3
c = []
for x in range(N):
    facs = [s3] * x + [s_p] + [id2] * (N - 1 - x)
    c.append(kron(*facs))
cd = [m.conjugate().T for m in c]
ok_car = True
for x in range(N):
    for y in range(N):
        acc1 = c[x] * c[y] + c[y] * c[x]
        acc2 = c[x] * cd[y] + cd[y] * c[x]
        ok_car &= (acc1 == zeros(2**N, 2**N))
        ok_car &= (acc2 == (eye(2**N) if x == y else zeros(2**N, 2**N)))
check("E1 JW family: exact CAR (cross-site anticommutators are the ZERO "
      "operator => every state annihilates every sandwiched insertion)",
      ok_car)
vac = zeros(2**N, 1)
vac[0, 0] = 1
check("E2 vacuum: c_x |0> = 0 for all x", all((m * vac) == zeros(2**N, 1)
                                              for m in c))
chi = (cd[0] + cd[1]) * vac
nrm = (chi.conjugate().T * chi)[0, 0]
val = (chi.conjugate().T * cd[0] * c[1] * chi)[0, 0] / nrm
check("E3 graded cross-site two-point <c0^dag c1> = 1/2 != 0 in state chi",
      val == Rational(1, 2))
check("E4 same state, anticommutator insertion = 0 (operator identity)",
      (chi.conjugate().T * (c[0] * cd[1] + cd[1] * c[0]) * chi)[0, 0] == 0)

print("SUMMARY commuting frame: exchange functional == 2 x propagator "
      "(locked); graded frame: exchange == 0 with propagator 1/2 (free).")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
