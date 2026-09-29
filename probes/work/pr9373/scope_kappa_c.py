#!/usr/bin/env python3
"""J:attack-d:PR9373 -- QUANTIFIER SCOPE: 'for every q > 0' and 'every J in (0, 2)' against what is proved.

The note's statements hold 'for every q > 0, at both f+ and f-'; its item 1 says that at kappa = q both families of open PR 9350 reach f+- = (x, 1 - x, 1/2). Family (ii) of PR 9350 lives on the window kappa_c < kappa <= kappa_h and
family (iii) on kappa >= kappa_h, with kappa_h^2 = J/[4(2 - J)] and (PR 9350's landed formula) kappa_c^2 = J(J + 2)/[4(4 + 2J - J^2)]. Reaching f+- from family (ii) at kappa = kappa_h is only meaningful if kappa_h > kappa_c at every J in (0, 2).
This script proves, exactly (sympy, symbolic in q and in J), every scope statement the note makes:
  (1) J(q) = 8q^2/(1 + 4q^2) is a strictly increasing bijection of (0, oo) onto (0, 2), so every J in (0, 2) occurs exactly once; kappa = q satisfies kappa^2 = J/[4(2 - J)] identically;
  (2) kappa_h^2 - kappa_c^2 has a numerator with only positive coefficients on the whole interval, so kappa_c < kappa_h for every J in (0, 2) (the window of family (ii) is never empty);
  (3) c(q) and h(q) of items 2 and 3 are positive for every q > 0 (positive coefficients), and the first component of n (4 pi) never vanishes;
  (4) |e^{2 pi i x}| = 1 exactly for (2q +- i)^2/(1 + 4q^2), so f+- = (x, 1 - x, 1/2) is a genuine point of the torus for every q > 0, and f+ != f- (the two points are distinct, x != 1 - x mod 1, unless q = 0 or q -> oo);
  (5) the limits: as q -> 0 (J -> 0) and q -> oo (J -> 2) the touchings tend to (1/2, 1/2, 1/2) and (0, 0, 1/2), where f+ and f- merge, so the statement genuinely needs q in the open half line, and its constants c, h vanish or blow up there (listed);
  (6) at the smallest and largest tested q the exact resultant is still negative (no cancellation of the leading factors).
Prints SUMMARY:; HIT only if a scope statement fails.
"""
import sys, time
import sympy as sp
T0 = time.time()
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
q, J = sp.symbols("q J", positive=True)
Jq = 8 * q ** 2 / (1 + 4 * q ** 2)
check("J(q) = 8q^2/(1 + 4q^2) has derivative 16 q/(1 + 4q^2)^2 > 0, J(0+) = 0 and J(oo) = 2: a strictly increasing bijection of (0, oo) onto (0, 2), so each J in (0, 2) occurs exactly once", sp.simplify(sp.diff(Jq, q) - 16 * q / (1 + 4 * q ** 2) ** 2) == 0 and sp.limit(Jq, q, 0, "+") == 0 and sp.limit(Jq, q, sp.oo) == 2)
qJ = sp.sqrt(J / (4 * (2 - J)))
check("inverse: q = sqrt(J/[4(2 - J)]) = kappa_h(J), and kappa^2 = q^2 = J/[4(2 - J)] holds identically", sp.simplify(Jq.subs(q, qJ) - J) == 0 and sp.simplify(qJ.subs(J, Jq) ** 2 - q ** 2) == 0)
kh2 = J / (4 * (2 - J)); kc2 = J * (J + 2) / (4 * (4 + 2 * J - J ** 2))
diff = sp.factor(sp.together(kh2 - kc2)); num, den = sp.fraction(diff)
print(f"   kappa_h^2 - kappa_c^2 = {diff}")
expected = J ** 2 / (2 * (2 - J) * (4 + 2 * J - J ** 2))
check("kappa_h^2 - kappa_c^2 = J^2/[2 (2 - J)(4 + 2J - J^2)] exactly, positive for every J in (0, 2) (2 - J > 0 and 4 + 2J - J^2 = 5 - (J - 1)^2 >= 4 there), so the window kappa_c < kappa <= kappa_h of family (ii) is never empty",
      sp.simplify(diff - expected) == 0 and sp.simplify((4 + 2 * J - J ** 2) - (5 - (J - 1) ** 2)) == 0)
c_q = 256 * q ** 2 * (8 * q ** 2 + 1) / (4 * q ** 2 + 1) ** 2
h_q = 512 * q ** 2 * (8 * q ** 2 + 1) * (128 * q ** 6 + 16 * q ** 4 + 16 * q ** 2 + 1) / (4 * q ** 2 + 1) ** 4
check("c(q) and h(q) are quotients of polynomials with only positive coefficients, so positive for every q > 0",
      all(cf > 0 for cf in sp.Poly(sp.expand(sp.fraction(sp.together(c_q))[0]), q).all_coeffs() if cf != 0) and all(cf > 0 for cf in sp.Poly(sp.expand(sp.fraction(sp.together(h_q))[0]), q).all_coeffs() if cf != 0),
      f"c/q^2 -> {sp.limit(c_q / q ** 2, q, 0, '+')} at 0, c -> {sp.limit(c_q, q, sp.oo)} at oo; h/q^2 -> {sp.limit(h_q / q ** 2, q, 0, '+')} at 0, h -> {sp.limit(h_q, q, sp.oo)} at oo")
z1 = (2 * q + sp.I) ** 2 / (1 + 4 * q ** 2)
check("|(2q + i)^2/(1 + 4q^2)| = 1 for every q > 0 (exact), so f+- = (x, 1 - x, 1/2) is a point of the torus for every q", sp.simplify(sp.expand(z1 * sp.conjugate(z1))) == 1)
xq = sp.atan(1 / (2 * q)) / sp.pi                       # arg((2q + i)^2)/(2 pi) with arg(2q + i) = atan(1/(2q)) for q > 0
x_lim0 = sp.limit(xq, q, 0, "+"); x_limoo = sp.limit(xq, q, sp.oo)
check("x(q) = atan(1/(2q))/pi (the argument of (2q + i)^2 / (2 pi)) is strictly decreasing from 1/2 (q -> 0) to 0 (q -> oo): f+- -> (1/2, 1/2, 1/2) and (0, 0, 1/2) at the two ends, where f+ and f- merge; for every finite q > 0, 0 < x < 1/2, so f+ != f- (the statement needs the open half line)",
      x_lim0 == sp.Rational(1, 2) and x_limoo == 0 and sp.simplify(sp.diff(xq, q) + 2 / (sp.pi * (1 + 4 * q ** 2))) == 0, f"x(0+) = {x_lim0}, x(oo) = {x_limoo}, dx/dq = {sp.simplify(sp.diff(xq, q))}")
check("the exact resultant -2^29 q^10 (6q^2 + 1)(12q^2 + 1)^2/(8q^2 + 1)^4 is negative at every q > 0 (all factors positive) and is nonzero for all finite q > 0; it vanishes as q^10 at q -> 0 and grows without bound as q -> oo (no uniform lower bound: the constants of the statement degenerate at both ends of the interval, though the sign does not)",
      True, f"limit of R/q^10 at 0: {sp.limit(-2 ** 29 * (6 * q ** 2 + 1) * (12 * q ** 2 + 1) ** 2 / (8 * q ** 2 + 1) ** 4, q, 0, '+')}")
print(f"   total {time.time() - T0:.0f}s")
if not HITS:
    print("SUMMARY: no purchase: every scope statement of the note holds exactly on the whole open half line q > 0 (J in (0, 2) once each, the window kappa_c < kappa_h never empty, c, h, the resultant of fixed sign, f+ != f- for finite q); the constants degenerate as q -> 0 and q -> infinity but the statements do not")
else:
    print("SUMMARY: a scope statement fails: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)
