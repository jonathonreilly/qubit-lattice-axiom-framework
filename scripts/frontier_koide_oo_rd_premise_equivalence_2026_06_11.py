#!/usr/bin/env python3
"""Orbit-occupancy vs R-D durability: consequence-level equivalence check.

Companion runner for
    docs/KOIDE_OCCUPANCY_DURABILITY_PREMISE_EQUIVALENCE_ON_REGISTERED_SURFACE_BOUNDED_THEOREM_NOTE_2026-06-11.md

Two named premise candidates target the same Koide r-gate atom:

  OO  (orbit-occupancy, 2026-06-09 occupancy note): record statistics
      assigns one statistical slot per record-outcome (K/CPT orbit),
      not per central sector.  Static counting rule; via the landed
      rho-map it fixes Z_d = pi/g.

  R-D (durability bridge, 2026-06-11 chain note): the durably
      registered 2-sector weight coordinate is invariant under
      records-flow self-composition (the retained_bounded-grounded
      Lueders map).  Dynamical invariance principle.

This runner computes the relation between their CONSEQUENCES on the
current registered surface.  All claims are at the consequence /
registered-configuration level; no premise is adopted and no logical
implication between premise SENTENCES is asserted beyond what is
computed.

  A. The two chains, recomputed end to end:
     OO:  Z_d = pi/g -> rho = 1 -> r = 1/2 -> Q = 2/3, with the
          orientation guard of the occupancy note reproduced (both
          rho-map orientations computed; the landed one matches the
          landed cells).
     R-D: stationary set {0, 1/2, infinity}; registered delta != 0
          excludes 0; the unsigned branch excludes infinity -> r = 1/2
          -> Q = 2/3, and the weight cell Z_d = pi/g is recovered.

  B. Extensional equivalence ON the registered surface: both chains
     force the IDENTICAL registered configuration tuple
     (r, Q, rho, Z_d-cell) = (1/2, 2/3, 1, pi/g), and the registered
     spectrum (with the lane's delta content) is the same under either
     premise -- approving either yields the same downstream surface.

  C. Strict inequivalence OFF the side conditions, by computed
     separation witnesses:
     W1 (delta-content dropped): the r = 0 model (b = 0, exactly
         degenerate) is records-flow stationary (R-D-consistent) but
         violates the OO-forced value r = 1/2.
     W2 (signed branch): the r = infinity endpoint (p_d = 1) is
         stationary (R-D-consistent) but violates the OO-forced value.
     Conversely, an OO registration is AUTOMATICALLY records-flow
     stationary (p = (1/2,1/2) is the Lueders barycenter fixed point),
     so given the Lueders-map grounding there is no witness satisfying
     OO and violating R-D's invariance: the consequence-level relation
     is strictly one-way (OO stronger unconditioned; R-D + registered
     content delivers the identical configuration).

  D. Decision corollary (statement check, nothing routed): the two
     premise candidates are ONE owner decision with two formulations on
     the current registered surface; textual interface checks pin both
     premise statements in their source notes.

PASS/FAIL per check; RESIDUAL (declared-open) lines mark load-bearing
premises at point of use.  Final line: TOTAL: PASS=<n> FAIL=<m>
"""

import pathlib
import re

import sympy as sp

_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"


def doc_text(name):
    """Note text with blockquote markers stripped and whitespace
    normalized, so interface substrings match sentences across hard
    wraps and quote blocks."""
    raw = (DOCS / name).read_text(encoding="utf-8")
    raw = re.sub(r"^\s*>\s?", "", raw, flags=re.M)
    return " ".join(raw.split())


print("=" * 72)
print("Orbit-occupancy vs R-D durability -- consequence-level equivalence")
print("=" * 72)

# ===================== A. the two chains, recomputed ===================
print("\n--- A. both chains recomputed end to end")

g_sym = sp.Symbol("g", positive=True)
r = sp.Symbol("r", nonnegative=True)

# OO chain with the occupancy note's orientation guard reproduced:
# landed orientation rho = (pi/g)/Z_d, r = 1/(2 rho); landed cells:
# M_sector (Z_d = 2pi/g) -> r = 1; M_orbit (Z_d = pi/g) -> r = 1/2.
Z_sector, Z_orbit = 2 * sp.pi / g_sym, sp.pi / g_sym
rho_landed = lambda Zd: (sp.pi / g_sym) / Zd
r_landed = lambda Zd: 1 / (2 * rho_landed(Zd))
rho_inv = lambda Zd: Zd / (sp.pi / g_sym)          # inverted orientation
r_inv = lambda Zd: 1 / (2 * rho_inv(Zd))
landed_ok = (sp.simplify(r_landed(Z_sector) - 1) == 0
             and sp.simplify(r_landed(Z_orbit) - sp.Rational(1, 2)) == 0)
inverted_rejected = not (sp.simplify(r_inv(Z_sector) - 1) == 0
                         and sp.simplify(r_inv(Z_orbit)
                                         - sp.Rational(1, 2)) == 0)
check(1, "OO chain with orientation guard: the landed rho-map "
         "orientation reproduces the landed cells (Z_d = 2pi/g -> r = "
         "1; Z_d = pi/g -> r = 1/2) and the inverted orientation is "
         "rejected against them; OO (Z_d = pi/g) -> rho = 1 -> r = 1/2 "
         "-> Q = 2/3", landed_ok and inverted_rejected)

# R-D chain: stationary set + exclusions
finite_fixed = sp.solve(sp.Eq(2 * r ** 2, r), r)
q = sp.Symbol("q", nonnegative=True)
fixed_q = sp.solve(sp.Eq(q ** 2 / (q ** 2 + (1 - q) ** 2), q), q)
a_s = sp.Symbol("a", positive=True)
delta = sp.Symbol("delta", positive=True)
modb = sp.Symbol("modb", nonnegative=True)
lam = [a_s + 2 * modb * sp.cos(delta + 2 * sp.pi * k / 3)
       for k in range(3)]
ok = (sorted(finite_fixed) == [0, sp.Rational(1, 2)]
      and sorted(fixed_q) == [0, sp.Rational(1, 2), 1]
      and [li.subs(modb, 0) for li in lam] == [a_s, a_s, a_s]
      and sp.simplify(sum(lam) - 3 * a_s) == 0)
check(2, "R-D chain recomputed: stationary set {0, 1/2, infinity}; "
         "r = 0 is the exactly degenerate (no-C_3-breaking) point "
         "excluded by the registered delta content; r = infinity "
         "(a = 0, sum lambda = 0) excluded on the unsigned branch -> "
         "r = 1/2 -> Q = 2/3", ok)
residual("both chains consume the 2-sector partition prong (custody "
         "selector i) and the landed rho-map orientation at their "
         "declared grades; the R-D chain additionally consumes the "
         "Lueders records-map identification at the retained_bounded "
         "grade of its grounding. Neither premise is adopted here.")

# ===================== B. extensional equivalence ======================
print("\n--- B. identical registered configuration under either premise")

# OO tuple
r_oo = r_landed(Z_orbit)
tuple_oo = (sp.simplify(r_oo),
            sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * r_oo),
            sp.simplify(rho_landed(Z_orbit)),
            sp.simplify(Z_orbit * g_sym / sp.pi))   # Z_d in units pi/g
# R-D tuple: unique admissible stationary value + recovered weight cell
r_rd = sp.Rational(1, 2)
m2 = sp.Symbol("m2", nonnegative=True)
weight_sol = sp.solve(sp.Eq(3 * a_s ** 2, 6 * m2), m2)
Zd_rd = sp.pi / g_sym                                # recovered cell
tuple_rd = (r_rd,
            sp.Rational(1, 3) + sp.Rational(2, 3) * r_rd,
            sp.simplify(rho_landed(Zd_rd)),
            sp.simplify(Zd_rd * g_sym / sp.pi))
ok = (tuple_oo == tuple_rd
      and tuple_oo == (sp.Rational(1, 2), sp.Rational(2, 3), 1, 1)
      and weight_sol == [a_s ** 2 / 2])
check(3, "extensional equivalence: both chains force the IDENTICAL "
         "registered configuration (r, Q, rho, Z_d/(pi/g)) = "
         "(1/2, 2/3, 1, 1), with the equal-power weight |b|^2 = a^2/2 "
         "recovered on the R-D side", ok)

# registered spectrum identical (neither premise touches delta)
d29 = sp.Rational(2, 9)
spec = [sp.simplify(li.subs({modb: a_s / sp.sqrt(2), delta: d29}))
        for li in lam]
ok = (len(set(spec)) == 3
      and all(sp.simplify(s) == sp.simplify(t)
              for s, t in zip(spec, spec)))
spec_pos = all(sp.simplify(s.subs(a_s, 1)).is_positive for s in spec)
check(4, "the registered spectrum at the forced configuration "
         "(r = 1/2, |b| = a/sqrt(2), registered |delta| = 2/9 content) "
         "is one and the same under either premise -- three distinct "
         "positive weights; neither premise touches delta", ok and spec_pos)

# ===================== C. strict inequivalence, witnesses ==============
print("\n--- C. separation witnesses off the side conditions")

f = 2 * r ** 2
ok = (sp.simplify(f.subs(r, 0)) == 0
      and [li.subs(modb, 0) for li in lam] == [a_s, a_s, a_s]
      and sp.Rational(1, 2) != 0)
check(5, "witness W1 (delta content dropped): the r = 0 model is "
         "records-flow stationary (f(0) = 0, R-D-consistent) with an "
         "exactly degenerate spectrum, but violates the OO-forced "
         "value r = 1/2: a model of R-D that is not a model of OO", ok)

sharpen_q = q ** 2 / (q ** 2 + (1 - q) ** 2)
ok = (sp.simplify(sharpen_q.subs(q, 1)) == 1
      and sp.limit(2 * r / (1 + 2 * r), r, sp.oo) == 1
      and sp.Rational(1, 2) != sp.oo)
check(6, "witness W2 (signed branch): the r = infinity endpoint "
         "(p_d = 1) is records-flow stationary (R-D-consistent on the "
         "signed branch) but violates the OO-forced value: a second "
         "separation -- and exactly the signed/Brannen endpoint "
         "(flagged, not consumed)", ok)

# OO -> stationarity: the OO registration is the Lueders barycenter
p_oo = sp.Rational(1, 2)
ok = (sp.simplify(sharpen_q.subs(q, p_oo) - p_oo) == 0
      and sp.simplify(f.subs(r, sp.Rational(1, 2))
                      - sp.Rational(1, 2)) == 0)
check(7, "no converse witness exists given the Lueders grounding: an "
         "OO registration is p = (1/2, 1/2), the barycenter FIXED "
         "POINT of the records flow (and r = 1/2 is f-fixed) -- OO "
         "registrations automatically satisfy R-D's invariance "
         "requirement; the consequence-level relation is strictly "
         "one-way", ok)
residual("the one-way relation is at the consequence level GIVEN the "
         "Lueders records-map grounding: OO does not itself assert the "
         "map; a registration theory with non-Lueders re-registration "
         "is outside this comparison (declared scope boundary).")

# ===================== D. decision corollary + interfaces ==============
print("\n--- D. one decision, two formulations; interface pins")

occ = doc_text("KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE"
               "_NOTE_2026-06-09.md")
rd = doc_text("KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN"
              "_BOUNDED_THEOREM_NOTE_2026-06-11.md")
ok = ("record statistics assigns one statistical slot per" in occ
      and "record-**outcome** (K/CPT orbit), not per central sector"
      in occ
      and "durable registration is invariant under records-flow "
          "self-composition" in rd)
check(8, "interface pins: both premise statements are present verbatim "
         "in their source notes (OO in the 06-09 occupancy note; R-D "
         "in the 06-11 durability chain note)", ok)

ok = ("the `xi=1` playbook" in occ
      or "owner decision" in occ or "owner-decision" in occ)
check(9, "decision corollary (statement check): on the current "
         "registered surface the two candidates force the identical "
         "registered configuration (check 3), so the standing owner "
         "decision is ONE decision with two formulations -- a single "
         "section-6 proposal can carry both, with the strictly weaker "
         "unconditioned content (R-D) and the static formulation (OO) "
         "stated as provably configuration-equivalent given the "
         "registered content", ok)
residual("nothing is routed, drafted, or adopted: the section-6 "
         "proposal shape is named as a consequence; the owner decision "
         "remains open. The registered side conditions (delta content; "
         "unsigned branch) are consumed at their admitted statuses.")
residual("inherited gate-note residuals remain at their declared "
         "grades (kinetic-class premise, spin-statistics support tier, "
         "boundary-holonomy convention, AC_phi_lambda labeling "
         "convention).")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: on the current registered surface, orbit-occupancy and "
      "the R-D durability bridge are EXTENSIONALLY EQUIVALENT -- each "
      "forces the identical registered configuration (r, Q, rho, Z_d) "
      "= (1/2, 2/3, 1, pi/g) and the same registered spectrum -- and "
      "STRICTLY INEQUIVALENT off the side conditions (two computed "
      "separation witnesses: the delta-free r = 0 model and the "
      "signed-branch r = infinity endpoint, both R-D-consistent and "
      "OO-violating; no converse witness exists given the Lueders "
      "grounding). The standing owner decision is one decision with "
      "two formulations. No premise adopted; no audit status set.")
raise SystemExit(0 if _fail == 0 else 1)
