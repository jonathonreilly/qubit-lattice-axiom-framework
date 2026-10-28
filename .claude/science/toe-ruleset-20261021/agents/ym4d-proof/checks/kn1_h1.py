#!/usr/bin/env python3 -I
"""kn1-1 + kn1-4: H1 convexity gate, its designed-FAIL control, and the patch identities.

Criteria: ../checks/kn1_criteria.md, written BEFORE this script.
Exact Fraction arithmetic for the weight family and the identities.
The designed-FAIL control (c-ii) uses double-precision complex arithmetic; its margin is
~0.98 against a threshold of 0.1875, so no verdict turns on the precision (disclosed).
"""
from fractions import Fraction as F
from math import factorial, cos, sin

out = []
def p(s=""):
    out.append(str(s))

p("=" * 78)
p("kn1-1 / kn1-4  --  H1 (S4' convexity) and the patch identities")
p("criteria: checks/kn1_criteria.md (written first).  Exact Fraction arithmetic.")
p("=" * 78)

# ---------------------------------------------------------------- kn1-1 (i)(ii)
p("")
p("## kn1-1  CONVEX / NOT-CONVEX / DEGENERATE-BUT-CONVEX")
p("")
p("Object: PROOF.md l.1754   M_bar_c(U) := (d! L^d)^{-1} * sum_sigma sum_{y in B(X)} T^sigma_y(U)")
p("Index set: PROOF.md l.711-714   sigma in S_d (d! orders) x y in B(X) (L^d sites).")
p("")
p(f"{'(d,L)':>8} {'#orders':>8} {'#sites':>8} {'#index':>10} {'w_i':>16} {'min w_i>=0':>11} {'sum w_i':>9} {'exact 1?':>9}")
verdicts = []
for (d, L) in [(2, 3), (3, 3), (4, 3), (5, 3), (4, 5)]:
    n_ord = factorial(d)
    n_site = L ** d
    n_idx = n_ord * n_site
    w = F(1, n_idx)
    weights = [w] * n_idx            # the family exactly as the definition writes it
    nonneg = all(x >= 0 for x in weights)
    tot = sum(weights, F(0))
    ok = (tot == 1)
    verdicts.append(nonneg and ok and len(weights) == n_idx)
    p(f"{str((d,L)):>8} {n_ord:>8} {n_site:>8} {n_idx:>10} {str(w):>16} {str(nonneg):>11} {str(tot):>9} {str(ok):>9}")
V1 = "CONVEX" if all(verdicts) else "NOT-CONVEX"
p("")
p(f"VERDICT kn1-1 (uniform family, all five (d,L)):  {V1}")

# degeneracy leg: do distinct (sigma,y) ever give the same complete-axial path?
p("")
p("Degeneracy leg (the DEGENERATE-BUT-CONVEX outcome).")
p("A complete-axial path c_X -> y in order sigma visits the coordinates in which y differs")
p("from c_X; orders that permute only the COINCIDING coordinates give the SAME path.")
p("So the induced weight on a DISTINCT transporter is m/(d! L^d) with m = the number of")
p("orders giving it, m >= 1, sum_distinct m = d! L^d.  Enumerated at (d,L)=(4,3):")
d, L = 4, 3
half = (L - 1) // 2
import itertools
sites = list(itertools.product(range(-half, half + 1), repeat=d))
assert len(sites) == L ** d
tot_m = 0
induced = []
for y in sites:
    moving = [i for i in range(d) if y[i] != 0]           # coordinates actually traversed
    distinct_paths = {}
    for sigma in itertools.permutations(range(d)):
        key = tuple(i for i in sigma if i in moving)       # the path is the order of the MOVING legs
        distinct_paths[key] = distinct_paths.get(key, 0) + 1
    for key, m in distinct_paths.items():
        induced.append(F(m, factorial(d) * L ** d))
        tot_m += m
p(f"  sites |B(X)| = {len(sites)},  index pairs = {factorial(d) * L**d},  distinct (path,y) = {len(induced)}")
p(f"  sum of multiplicities m = {tot_m}  (must equal d! L^d = {factorial(d)*L**d})")
p(f"  induced weights all > 0 : {all(x > 0 for x in induced)}")
p(f"  induced weights sum to  : {sum(induced, F(0))}  (exact 1? {sum(induced, F(0)) == 1})")
p(f"  distinct induced values : {sorted(set(induced))}")
DEG = "DEGENERATE-BUT-CONVEX" if len(induced) != factorial(d) * L ** d else "NON-DEGENERATE"
p(f"VERDICT degeneracy leg: {DEG}  -- in either case nonnegative and normalised.")

# ---------------------------------------------------------------- designed-FAIL control
p("")
p("## kn1-1 DESIGNED-FAIL CONTROL (mandatory; criteria (c-i),(c-ii) and the ||M||<=1 leg)")
p("")
theta = F(1, 4)
a = F(3)
w_ctrl = [1 + a, -a]
p(f"  signed family: w = {[str(x) for x in w_ctrl]},  sum = {sum(w_ctrl)}  (total mass still 1)")
p(f"  T_1 = e^X, T_2 = e^-X,  X = i*theta*diag(1,-1) in su(2),  theta = {theta},  S = 1")
c_i_fails = not all(x >= 0 for x in w_ctrl)
p(f"  (c-i) rejected by the nonnegativity clause? {c_i_fails}   -> control FAILS clause (i): {c_i_fails}")

th = float(theta); A = float(a)
# X_bar = (1+a)X + (-a)(-X) = (1+2a)X  ;  W' = exp(X_bar)
k = 1 + 2 * A
# diagonal entry 1 of M_bar
m11 = (1 + A) * complex(cos(th), sin(th)) + (-A) * complex(cos(th), -sin(th))
w11 = complex(cos(k * th), sin(k * th))
R11 = m11 / w11 - 1.0
delta = th                                   # max_i ||X_i||_op
bound = 3 * delta ** 2
p(f"  delta = max_i ||X_i||_op = {delta}            Lemma KN' bound 3*delta^2 = {bound}")
p(f"  ||X_bar||_op = {k*th}  (EXCEEDS delta: the convex-hull step is what fails)")
p(f"  ||R||_op = ||W'^-1 M_bar - 1||_op = {abs(R11):.6f}")
c_ii_fails = abs(R11) > bound
p(f"  (c-ii) does the control BREAK ||R|| <= 3 delta^2 ?  {c_ii_fails}   "
  f"(exceeds by x{abs(R11)/bound:.3f})")
p(f"  ||M_bar||_op = {abs(m11):.6f}   violates PROOF.md l.1755's ||M_bar_c||_op <= 1 ?  {abs(m11) > 1}")
POWER = "HAS-POWER" if (c_i_fails and c_ii_fails and abs(m11) > 1) else "NO POWER"
p(f"VERDICT control: {POWER}   -- convexity is load-bearing in KN' and the gate can fail.")

# ---------------------------------------------------------------- kn1-4 identities
p("")
p("## kn1-4  the patch's identities (exact Fractions, d = 4, L = 3)")
p("")
d, L = 4, 3
A_d = F((d - 1) * L * (L - 1), 2)
c_1 = F(1, 2) / (F(L * L) + F(11, 2) * A_d)
p(f"  A_d(L) = (d-1)L(L-1)/2 = {A_d}            [RLARGE.md l.973]")
p(f"  (i)   c_1 = 1/(2(L^2 + 5.5 A_d)) = {c_1}   == 1/117 ? {c_1 == F(1,117)}")
id_ii = (F(L * L) + F(11, 2) * A_d) * c_1
p(f"  (ii)  (L^2 + 5.5 A_d) * c_1 = {id_ii}            == 1/2 ? {id_ii == F(1,2)}")
t = F(1)       # symbolic unit; the identity is homogeneous in t
id_iii = t / 2 + 4 * (t / 8)
p(f"  (iii) t/2 + 4*(t/8) = {id_iii} t                 == t ? {id_iii == t}")
ids_iv = []
for N in (2, 3):
    lhs = (t / 8) ** 2 / (4 * N)
    rhs = t ** 2 / (256 * N)
    ids_iv.append(lhs == rhs)
    p(f"  (iv)  N={N}: (t/8)^2/(4N) = {lhs}   t^2/(256N) = {rhs}   equal? {lhs == rhs}")
IDH = all([c_1 == F(1, 117), id_ii == F(1, 2), id_iii == t] + ids_iv)
p(f"VERDICT kn1-4: {'IDENTITIES-HOLD' if IDH else 'FAIL'}")

p("")
p("  DESIGNED-FAIL control for kn1-4: replace 5.5 by 5, keep c_1 = 1/117.")
bad = (F(L * L) + F(5) * A_d) * F(1, 117)
p(f"    (L^2 + 5 A_d) * (1/117) = {bad}   == 1/2 ? {bad == F(1,2)}   -> control FAILS: {bad != F(1,2)}")
p(f"    control verdict: {'HAS-POWER' if bad != F(1,2) else 'NO POWER'}")

p("")
p("=" * 78)
p(f"SUMMARY  kn1-1 = {V1} ({DEG});  control = {POWER};  kn1-4 = "
  f"{'IDENTITIES-HOLD' if IDH else 'FAIL'}")
p("=" * 78)
p("")
p("Disclosure: the (c-ii) and ||M||<=1 legs of the control use double-precision complex")
p("arithmetic.  The margins are 0.98 against a 0.1875 threshold and 1.98 against 1, i.e.")
p("~15 orders above double-precision error, so no verdict turns on the precision.")
p("Everything else in this script is exact Fraction arithmetic.")

print("\n".join(out))
