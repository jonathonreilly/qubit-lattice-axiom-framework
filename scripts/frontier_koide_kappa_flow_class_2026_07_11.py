#!/usr/bin/env python3
"""Kappa bookkeeping flow class, fixed-point inversion, and lane scoping.

Companion runner for
    docs/KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11.md

Verifies, symbolically:

  T1 (flow class). Agreement-conditioned independent double registration on the
     two-cell bookkeeping (p_s, p_d) = (a^2, kappa|b|^2)/(a^2 + kappa|b|^2),
     kappa > 0, induces x -> x^2 on the odds coordinate x = p_d/p_s = kappa r,
     hence r -> kappa r^2. Complete fixed set on [0, oo]: {0, 1/kappa, oo};
     unique interior fixed point r* = 1/kappa; |f'(r*)| = 2 for every kappa
     (kappa-independent, proven by linear conjugacy to x -> x^2).

  T2 (fork = partition binary). kappa = 2 is the landed channel/orbit
     bookkeeping (doublet HS energy 2|b|^2): r -> 2r^2, r* = 1/2. kappa = 1 is
     per-direction/sector bookkeeping and the induced flow is EXACTLY the
     premise-relation counterexample psi(r) = r^2, r* = 1. The fork kappa in
     {1, 2} is the count-once/count-twice partition binary in dynamical form.

  T3 (fixed-point inversion + lane scoping). Persistent value r = 1/kappa, so
     kappa = 1/r. Invert the registered dial comparators (down r_d ~ 0.597,
     up r_u ~ 0.773; charged leptons r = 1/2) and build the sigma-distance table
     of the inverted kappa from the counting rationals {1, 5/4, 4/3, 3/2, 5/3, 2}.
     REPORT ONLY: the table is printed as a standing evidence surface and is
     NEVER thresholded. Numeric PASS/FAIL checks assert only internal arithmetic.

No lane's kappa is derived; r = 1/2 is neither derived nor preferred; no quark
value is derived; no premise is adopted; the flow family is scoped to the
agreement-conditioned independent double-registration class. No audit status.

Comparator numbers are parsed as labeled comparator constants at their stated
precision. No derivation-path value is hard-coded as an input.
"""

from __future__ import annotations

import pathlib
import re
import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, desc: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTE = DOCS / (
    "KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_"
    "SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
THIS_SCRIPT = ROOT / "scripts/frontier_koide_kappa_flow_class_2026_07_11.py"


print("=" * 72)
print("Kappa bookkeeping flow class, fixed-point inversion, lane scoping")
print("=" * 72)

# Free positive symbols. No derivation-path value is fixed here.
a2 = sp.Symbol("a2", positive=True)      # a^2
b2 = sp.Symbol("b2", positive=True)      # |b|^2
kappa = sp.Symbol("kappa", positive=True)
r = sp.Symbol("r", positive=True)
s = sp.Symbol("s", positive=True)
x = sp.Symbol("x", positive=True)
t_real = sp.Symbol("t_real", real=True)  # unrestricted domain for fixed-point solves

# ----------------------------------------------------------------------------
print("\n--- A-class T1: the induced flow class")

# Normalized two-cell bookkeeping (p_s, p_d) = (a^2, kappa|b|^2)/(a^2+kappa|b|^2).
Znorm = a2 + kappa * b2
p_s = a2 / Znorm
p_d = kappa * b2 / Znorm

# 1. odds coordinate x = p_d/p_s = kappa r, with r = |b|^2/a^2.
odds = sp.simplify(p_d / p_s)
rdef = b2 / a2
check(
    1,
    "odds coordinate x = p_d/p_s equals kappa r, r = |b|^2/a^2",
    sp.simplify(odds - kappa * rdef) == 0,
    f"x={odds}",
)

# 2. G2 map p_i' = p_i^2/(p_s^2+p_d^2) sends the odds coordinate to its square.
Z2 = p_s**2 + p_d**2
p_s_prime = p_s**2 / Z2
p_d_prime = p_d**2 / Z2
odds_prime = sp.simplify(p_d_prime / p_s_prime)
check(
    2,
    "agreement-conditioned independent double registration sends x -> x^2 (any kappa)",
    sp.simplify(odds_prime - odds**2) == 0,
    f"x'={odds_prime}",
)

# 3. induced flow on r is f(r) = kappa r^2.
#    r' = x'/kappa = x^2/kappa = (kappa r)^2/kappa = kappa r^2.
x_prime_in_r = (kappa * r) ** 2
r_prime = sp.simplify(x_prime_in_r / kappa)
f = kappa * r**2
check(
    3,
    "induced flow on r is f(r) = kappa r^2",
    sp.simplify(r_prime - f) == 0,
    f"f(r)={f}",
)

# 4. complete finite fixed set of f on the real line is {0, 1/kappa}.
finite_fixed = sp.solve(sp.Eq(kappa * t_real**2, t_real), t_real)
check(
    4,
    "finite fixed set of f(r)=kappa r^2 is {0, 1/kappa}",
    set(finite_fixed) == {sp.Integer(0), 1 / kappa},
    f"fixed={finite_fixed}",
)

# 5. projective endpoint: under s = 1/r, f conjugates to s -> s^2/kappa, fixed at s=0 (r=oo).
f_s = sp.simplify(1 / f.subs(r, 1 / s))
check(
    5,
    "under s=1/r, f conjugates to s -> s^2/kappa; s=0 (r=oo) fixed; complete set {0,1/kappa,oo}",
    sp.simplify(f_s - s**2 / kappa) == 0 and f_s.subs(s, 0) == 0,
    f"f_s={f_s}",
)

# 6. unique interior fixed point r* = 1/kappa (the only fixed point in (0, oo)).
interior = [pt for pt in finite_fixed if sp.simplify(pt) != 0]
check(
    6,
    "unique interior fixed point r* = 1/kappa",
    interior == [1 / kappa],
    f"interior={interior}",
)

# 7. multiplier |f'(r*)| = 2, kappa-independent, proven by symbolic derivative.
fp = sp.diff(f, r)
mult = sp.simplify(fp.subs(r, 1 / kappa))
check(
    7,
    "f'(r*) = 2 for every kappa (kappa-independent multiplier)",
    mult == 2 and sp.simplify(mult - 2) == 0,
    f"f'(1/kappa)={mult}",
)

# 8. structural reason: f is linearly conjugate to the square map sq(x)=x^2 via h(r)=kappa r.
#    (h o f o h^{-1})(x) = kappa * f(x/kappa) = x^2, so multiplier at the fixed point is sq'(1)=2.
h = kappa * r
conj = sp.simplify((kappa * f.subs(r, x / kappa)))
sq = x**2
sq_mult_at_1 = sp.diff(sq, x).subs(x, 1)
check(
    8,
    "f is linearly conjugate to sq(x)=x^2 via h(r)=kappa r; sq'(1)=2 carries the knife-edge",
    sp.simplify(conj - sq) == 0 and sq_mult_at_1 == 2,
    f"h.f.h^-1={conj}",
)

# ----------------------------------------------------------------------------
print("\n--- A-class T2: the fork is the partition binary")

# 9. kappa=2 is the landed channel/orbit bookkeeping: (p_s,p_d)=(a^2,2|b|^2), r->2r^2, r*=1/2.
p_d_k2 = (kappa * b2).subs(kappa, 2)
f_k2 = f.subs(kappa, 2)
rstar_k2 = (1 / kappa).subs(kappa, 2)
check(
    9,
    "kappa=2: doublet cell 2|b|^2, flow r->2r^2, r*=1/2, |f'|=2",
    p_d_k2 == 2 * b2
    and sp.simplify(f_k2 - 2 * r**2) == 0
    and rstar_k2 == sp.Rational(1, 2)
    and fp.subs({kappa: 2, r: sp.Rational(1, 2)}) == 2,
    f"f_2(r)={f_k2}, r*={rstar_k2}",
)

# 10. kappa=1 is per-direction/sector bookkeeping: flow is EXACTLY psi(r)=r^2, r*=1.
psi = r**2  # the premise-relation P3 counterexample flow, stated verbatim there
f_k1 = f.subs(kappa, 1)
rstar_k1 = (1 / kappa).subs(kappa, 1)
fix_psi = set(sp.solve(sp.Eq(t_real**2, t_real), t_real))
check(
    10,
    "kappa=1: flow is EXACTLY psi(r)=r^2 (premise-relation P3); Fix={0,1}; r*=1; |f'|=2",
    sp.simplify(f_k1 - psi) == 0
    and fix_psi == {sp.Integer(0), sp.Integer(1)}
    and rstar_k1 == 1
    and fp.subs({kappa: 1, r: 1}) == 2,
    f"f_1(r)={f_k1}",
)

# 11. the fork kappa in {1,2} is the count-once/count-twice partition binary:
#     count-once (sector) -> r*=1; count-twice (orbit) -> r*=1/2; multiplier 2 in both.
count_once_value = (1 / kappa).subs(kappa, 1)     # sector cell
count_twice_value = (1 / kappa).subs(kappa, 2)    # orbit cell
knife_edge_both = (
    fp.subs({kappa: 1, r: count_once_value}) == 2
    and fp.subs({kappa: 2, r: count_twice_value}) == 2
)
check(
    11,
    "fork kappa in {1,2} = count-once (r*=1) vs count-twice (r*=1/2); knife-edge |f'|=2 unchanged",
    count_once_value == 1
    and count_twice_value == sp.Rational(1, 2)
    and count_once_value != count_twice_value
    and knife_edge_both,
    f"count-once r*={count_once_value}, count-twice r*={count_twice_value}",
)

# ----------------------------------------------------------------------------
print("\n--- A-class T3: fixed-point inversion and the sigma-distance table")

# Fixed-point inversion identity: persistent value r = 1/kappa <=> kappa = 1/r.
kappa_of_r = sp.solve(sp.Eq(r, 1 / kappa), kappa)
check(
    12,
    "fixed-point inversion: r = 1/kappa <=> kappa = 1/r",
    kappa_of_r == [1 / r],
    f"kappa(r)={kappa_of_r}",
)

# Labeled comparator constants, parsed at their stated precision (file 3).
#   charged leptons: r = 1/2 exactly (Koide Q=2/3 to 1e-5)
#   down-quarks:     r ~ 0.597   (quoted to 3 decimal places)
#   up-quarks:       r ~ 0.773   (quoted to 3 decimal places)
# COMPARATOR ONLY -- never a proof input, never thresholded.
r_lep = sp.Rational(1, 2)
r_down = sp.Rational(597, 1000)
r_up = sp.Rational(773, 1000)

# registered precision of the quark comparators = last quoted decimal place.
SIGMA_R = sp.Rational(1, 1000)          # 1e-3
SIGMA_R_HALF_ULP = sp.Rational(1, 2000)  # 5e-4 disclosure scenario

counting_rationals = [
    sp.Integer(1),
    sp.Rational(5, 4),
    sp.Rational(4, 3),
    sp.Rational(3, 2),
    sp.Rational(5, 3),
    sp.Integer(2),
]

# 13. inverted kappa comparators kappa = 1/r.
kappa_down = 1 / r_down
kappa_up = 1 / r_up
kappa_lep = 1 / r_lep
check(
    13,
    "inverted comparators kappa_d=1/r_d, kappa_u=1/r_u, kappa_lep=1/r_lep",
    kappa_down == sp.Rational(1000, 597)
    and kappa_up == sp.Rational(1000, 773)
    and kappa_lep == 2,
    f"kappa_d={float(kappa_down):.6f}, kappa_u={float(kappa_up):.6f}, kappa_lep={kappa_lep}",
)

# 14. charged-lepton comparator sits EXACTLY on the kappa=2 counting cell.
check(
    14,
    "charged-lepton comparator r=1/2 sits exactly on the kappa=2 counting cell (labeled comparator)",
    kappa_lep == sp.Integer(2) and (kappa_lep in counting_rationals),
    f"kappa_lep={kappa_lep}",
)


def sigma_table(label, r_val, kappa_val, sigma_r):
    """Propagate registered precision to kappa: sigma_kappa = sigma_r / r^2.
    Return list of (t, |kappa-t|, sigma-distance) and print. REPORT ONLY."""
    sigma_kappa = sigma_r / r_val**2
    rows = []
    print(f"    sigma-distance table [{label}]  r={float(r_val):.4f}  "
          f"kappa=1/r={float(kappa_val):.6f}  sigma_r={float(sigma_r):.4g}  "
          f"sigma_kappa={float(sigma_kappa):.4g}")
    print(f"      {'t=p/q':>7} {'r=1/t':>8} {'|kappa-t|':>11} {'sigma-dist(kappa)':>18} "
          f"{'|r-1/t|/sigma_r':>16}")
    for t in counting_rationals:
        dkappa = sp.Abs(kappa_val - t)
        sig_k = dkappa / sigma_kappa
        r_space = sp.Abs(r_val - 1 / t) / sigma_r
        rows.append((t, dkappa, sig_k, r_space))
        print(f"      {str(t):>7} {float(1/t):>8.4f} {float(dkappa):>11.6f} "
              f"{float(sig_k):>18.3f} {float(r_space):>16.3f}")
    return rows, sigma_kappa


print()
rows_down, sig_kd = sigma_table("down-lane", r_down, kappa_down, SIGMA_R)
print()
rows_up, sig_ku = sigma_table("up-lane", r_up, kappa_up, SIGMA_R)
print()

# 15. nearest counting rational (argmin of |kappa - t|) -- computed report, not a threshold.
nearest_down = min(rows_down, key=lambda row: float(row[1]))
nearest_up = min(rows_up, key=lambda row: float(row[1]))
check(
    15,
    "nearest counting rational: down-lane -> 5/3, up-lane -> 4/3 (argmin |kappa-t|, reported)",
    nearest_down[0] == sp.Rational(5, 3) and nearest_up[0] == sp.Rational(4, 3),
    f"down->{nearest_down[0]} ({float(nearest_down[2]):.3f} sigma), "
    f"up->{nearest_up[0]} ({float(nearest_up[2]):.3f} sigma)",
)

# 16. arithmetic reproduction of the minimum sigma-distances (verifies the table math,
#     NOT a physics threshold). down-lane nearest ~ 2.985 sigma; up-lane nearest ~ 23.706 sigma.
sig_down_min = float(nearest_down[2])
sig_up_min = float(nearest_up[2])
check(
    16,
    "arithmetic reproduction of minimum sigma-distances (table math only; not a threshold)",
    abs(sig_down_min - 2.985) < 0.01 and abs(sig_up_min - 23.706) < 0.02,
    f"down_min={sig_down_min:.3f}, up_min={sig_up_min:.3f}",
)

# 17. half-ULP disclosure: with sigma_r=5e-4 every sigma-distance doubles.
sig_kd_half = SIGMA_R_HALF_ULP / r_down**2
ratio_down = sp.simplify((SIGMA_R / r_down**2) / sig_kd_half)
check(
    17,
    "half-ULP disclosure: sigma_r=5e-4 doubles every sigma-distance (sigma_kappa halves)",
    ratio_down == 2,
    f"scale={ratio_down}",
)

# ----------------------------------------------------------------------------
print("\n--- B-class: note consistency")

text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""

# 18. status header present.
check(
    18,
    "note carries Status / Claim type header",
    "**Claim type:**" in text and "**Status" in text,
)

# 19. premise-relation P3 counterexample quoted verbatim.
p3_quote = "psi(r) = r^2"
check(
    19,
    "premise-relation P3 counterexample psi(r)=r^2 quoted verbatim",
    p3_quote in text and "Fix(psi) = {0, 1}" in text,
)

# 20. kill-condition sentence present verbatim.
kill = (
    "If a derived color/EW dressing later produces kappa_d, kappa_u matching the "
    "inverted values at registered precision, the universal counting-flow law "
    "resurrects and this note's scoping corollary is dead; the sigma-distance "
    "table above is the standing evidence surface for that test."
)
check(
    20,
    "kill-condition sentence present verbatim",
    kill in text,
)

# 21. sigma-distance comparator numbers present in the note.
check(
    21,
    "note carries the inverted comparator kappa values and the sigma-distance table",
    "1.675042" in text and "1.293661" in text and "5/3" in text and "4/3" in text,
)

# 22. never-threshold / comparator-labeled language present.
check(
    22,
    "note labels the dial numbers as comparators and states never-thresholded",
    "comparator" in text.lower() and "never" in text.lower(),
)

# 23. 'What This Does Not Claim' disavowals present.
lower = text.lower()
disavowals = [
    "does not derive",
    "does not adopt",
]
check(
    23,
    "note carries the What This Does Not Claim disavowals",
    "what this does not claim" in lower and all(p in lower for p in disavowals),
)

# 24. markdown link inventory is exactly the three load-bearing dependencies and all resolve;
#     context notes are backticked only.
md_targets = re.findall(r"\]\(([^)]+\.md)\)", text)
expected_links = {
    "RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md",
    "KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md",
    "FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md",
}
actual_links = set(md_targets)
links_resolve = all((DOCS / t).exists() for t in actual_links)
context_backticked = all(
    f"`{name}`" in text and f"]({name})" not in text
    for name in (
        "KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02.md",
        "KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md",
    )
)
check(
    24,
    "markdown links are exactly the three dependencies (resolve); context notes backticked only",
    actual_links == expected_links and links_resolve and context_backticked,
    f"links={sorted(actual_links)}",
)

print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
print(
    "RESULT: T1 induced flow r->kappa r^2, fixed set {0,1/kappa,oo}, |f'(r*)|=2 "
    "kappa-independent; T2 fork kappa in {1,2} = count-once(psi,r*=1)/count-twice"
    "(r*=1/2) partition binary; T3 kappa_d=1/r_d, kappa_u=1/r_u inverted, "
    "sigma-distance table reported (never thresholded)."
)
if FAIL or PASS < 24:
    sys.exit(1)
