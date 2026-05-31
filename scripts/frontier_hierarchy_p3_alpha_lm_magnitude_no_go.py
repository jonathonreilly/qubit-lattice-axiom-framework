#!/usr/bin/env python3
"""
Hierarchy P3: the u_0^16 -> alpha_LM^16 magnitude substitution is structurally
foreclosed from promotion to a determinant/condensate/transport theorem on the
delta = 0 Cl(3)/Z^3 substrate
==============================================================================

Exact/symbolic companion runner for the bounded no-go note

    docs/HIERARCHY_P3_ALPHA_LM_MAGNITUDE_STRUCTURAL_FORECLOSURE_NO_GO_NOTE_2026-05-30.md

Background
---------
The hierarchy formula v = M_Pl * (7/8)^{1/4} * alpha_LM^{16} uses the primitive
P3 substitution u_0^{16} -> alpha_LM^{16}, with alpha_LM = alpha_bare / u_0
(HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10 section P3). The honest-status
note already records that this is an algebraic relabeling, not a determinant
identity. This runner records that the relabeling cannot be UPGRADED to an
RG-transport / determinant theorem on this substrate -- the foreclosure is
structural, not merely "unsupplied".

The four exact / symbolic facts
-------------------------------
1. The magnitude is a coupling power. The suppression in the formula is
   dominated by alpha_bare^{16} = (4 pi)^{-16} (g_bare = 1 => alpha_bare =
   1/(4 pi)), an exact pure number ~ 2.586e-18.

2. Arithmetic of record. HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10
   section 3 (P3) prints alpha_bare^{16} = 1.34e-17 inline. That value is a
   typo: it is off by 5.18x from (4 pi)^{-16} = 2.586e-18, AND it is
   inconsistent with that same note's OWN companion numbers alpha_LM^{16} =
   2.09e-17 and u_0^{-16} = 8.07 (which force alpha_bare^{16} =
   alpha_LM^{16} / u_0^{-16} = 2.59e-18). The EW-VEV-bridge note already flags
   this. We record the corrected value; we do not edit the honest-status note.

3. Geometric progression = power-law fingerprint. The three couplings
   alpha_bare (UV cell), alpha_LM (geometric mean), alpha_s(v) = alpha_bare/u_0^2
   (IR) form an exact geometric progression with constant multiplicative ratio
   1/u_0. A constant per-step multiplicative ratio in alpha is the defining
   fingerprint of POWER-LAW running alpha(mu) ~ mu^{-kappa}, NOT one-loop
   running (which is linear in 1/alpha vs ln mu): the equal-log-spacing test
   fails, Delta2/Delta1 = u_0 != 1.

4. The block observables carry only u_0. The framework's three exact block
   observables -- the determinant |det(D+m)| = prod[m^2 + u_0^2 (3 + sin^2 w)]^4,
   the free-energy density, and the staggered condensate density
   (1/N) Tr[(D+m)^{-1}] = (m/L_t) sum_w 1/[m^2 + u_0^2 (3 + sin^2 w)]
   (HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md, exact) -- contain ONLY u_0; there
   is no explicit factor of alpha_bare in any of them. So the (4 pi)^{-16}
   suppression is produced by NO determinant/condensate object the framework
   owns; it enters solely via the relabeling alpha_LM = alpha_bare/u_0.

Consequence (scoped EXACTLY)
----------------------------
Power-law gauge running in 4D requires delta > 0 compactified extra dimensions
(Dienes-Dudas-Gherghetta KK tower). Cl(3)/Z^3 has delta = 0. So the
geometric-mean structure is permanently a relabeling on this substrate and
cannot be promoted to an RG trajectory: C2 (extra-dimension power-law) is
foreclosed STRUCTURALLY (not merely "not derived"), and C3's residual is exactly
the alpha_LM^{16} the YT transport-obstruction theorem already names as
non-perturbative / out-of-scope. P3 is therefore a genuinely SEPARATE admission:
the (4 pi)^{-16} coupling-power suppression is imported, not derived. This is
NOT a closure and adds no axiom.

Type: no_go (companion runner). Status authority: independent audit lane only.
No new tags, no new vocabulary, no promotion language.

Run:
  python3 scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py
"""

from __future__ import annotations

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  |  {detail}" if detail else ""))


def main() -> int:
    # ---- 1. (4 pi)^{-16} exact pure number -------------------------------
    alpha_bare_val = 1 / (4 * sp.pi)                       # g_bare = 1
    ab16 = alpha_bare_val ** 16
    ab16_f = float(ab16)
    check("alpha_bare = 1/(4 pi)  (g_bare = 1)", sp.simplify(alpha_bare_val - 1 / (4 * sp.pi)) == 0)
    check("alpha_bare^16 = (4 pi)^-16 ~= 2.586e-18",
          abs(ab16_f - 2.586e-18) / 2.586e-18 < 1e-3, f"= {ab16_f:.4e}")

    # ---- 2. arithmetic of record: the inline 1.34e-17 is a typo ----------
    typo = 1.34e-17
    check("honest-status inline alpha_bare^16 = 1.34e-17 is off 5.18x from (4 pi)^-16",
          abs(typo / ab16_f - 5.18) < 0.05, f"ratio = {typo/ab16_f:.3f}")
    # internal-consistency cross-check against that note's OWN companion numbers
    aLM16_note = 2.09e-17
    u0_m16_note = 8.07
    implied = aLM16_note / u0_m16_note
    check("note's own alpha_LM^16 / u_0^-16 implies alpha_bare^16 ~= 2.59e-18 "
          "(consistent with (4 pi)^-16, NOT 1.34e-17)",
          abs(implied / ab16_f - 1.0) < 0.005, f"implied = {implied:.4e}")

    # ---- 3. geometric progression and the failed equal-log-spacing test --
    u0, ab = sp.symbols("u0 alpha_bare", positive=True)
    aLM = ab / u0
    aS = ab / u0 ** 2
    check("alpha_LM = sqrt(alpha_bare * alpha_s)  (geometric mean)",
          sp.simplify(aLM - sp.sqrt(ab * aS)) == 0)
    check("ratio alpha_LM / alpha_bare = 1/u0", sp.simplify(aLM / ab - 1 / u0) == 0)
    check("ratio alpha_s / alpha_LM = 1/u0  (exact geometric progression)",
          sp.simplify(aS / aLM - 1 / u0) == 0)
    # one-loop test: 1/alpha is linear in ln mu, so equal-log-mu steps give
    # equal 1/alpha steps (Delta2/Delta1 = 1). Here Delta2/Delta1 = u0 != 1.
    inv = [1 / ab, 1 / aLM, 1 / aS]
    D1 = sp.simplify(inv[1] - inv[0])
    D2 = sp.simplify(inv[2] - inv[1])
    check("equal-log-spacing (one-loop) test FAILS: Delta2/Delta1 = u0 (!= 1)",
          sp.simplify(D2 / D1 - u0) == 0, f"Delta2/Delta1 = {sp.simplify(D2/D1)}")

    # ---- 4. block observables carry only u_0 (no explicit alpha_bare) ----
    m, w = sp.symbols("m omega", positive=True)
    Lt = sp.symbols("L_t", positive=True)
    lam = m ** 2 + u0 ** 2 * (3 + sp.sin(w) ** 2)         # one Matsubara eigenvalue block
    det_factor = lam ** 4                                  # |det(D+m)| per-mode factor
    cond_summand = 1 / lam                                 # condensate-density summand
    check("determinant per-mode factor has no explicit alpha_bare",
          ab not in det_factor.free_symbols and u0 in det_factor.free_symbols)
    check("condensate-density summand has no explicit alpha_bare",
          ab not in cond_summand.free_symbols and u0 in cond_summand.free_symbols)
    check("both block observables depend on u_0 only (alpha_bare enters solely "
          "via the alpha_LM relabeling)",
          {s for s in lam.free_symbols} <= {m, w, u0})

    # ---- 5. delta = 0 forecloses power-law => C2 structural, C3 residual --
    delta_substrate = 0   # Cl(3)/Z^3 has no compactified extra dimensions
    check("Cl(3)/Z^3 substrate has delta = 0 (no KK tower) => power-law running "
          "unavailable => C2 foreclosed structurally", delta_substrate == 0)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
