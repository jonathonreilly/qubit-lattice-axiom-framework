# Hierarchy on the scale ladder: summary (2026-10-18)

**Request.** Jon: "work hierarchy derivation on the scale ladder approach in the recent PR (#9702) as a 12 hour goal (stop if you get it earlier)". He asked for both hierarchies: the scale hierarchy and the fermion mass hierarchy.

**Provenance.** Each test was run by one Opus 5.5 agent at xhigh. Each was refereed by a separate Opus 5.5 subagent, the same model family as the workers, so the referees are not independent. Codex was unavailable. All readings were pre-registered in TESTS.md.

**Bottom line: neither hierarchy is derived from the ladder.** Every built route is excluded or open, and each open route trades the hierarchy for a number the framework does not fix.

| Test | Fixed reading (after referee) | What is established |
|---|---|---|
| HIER-1, scale hierarchy | HIER-NO-GO, within a narrowed class | (a) The exponent 16 in main's formula v = M_Pl(7/8)^{1/4}α_LM^16: the coupling α is not transported across rungs (v/μ = cα^16 at every rung would force d ln α/d ln μ = −1/16), so gate B4 cannot be closed by transport. On the staggered carrier, 16 is a protected free-fermion multiplicity that depends on the regulator; it is not an interacting invariant. (b) The built content has no asymptotically free coupling. With a supplied SU(N) at g² = 1 there is no 15-decade transmutation. (c) Stacking rungs telescopes and gives ξ/a ≤ C·(1/δ)^{1/y}. The ladder's tools cannot fix a nonzero, parametrically small relevant coupling. |
| HIER-3, colour coupling at the first coloured rung | G-OUTSIDE | Getting v from colour needs g²(M_cut) ∈ [0.17, 0.36], two-loop. The framework's only non-circular value is the β = 6 lattice, g² ≥ 1. With a = l_Pl (open gate B2), it confines at about 0.1–0.2 M_Pl. COL-1 cells fix no coupling. Dropping g_bare = 1 needs a supplied non-QCD confining sector at g² ≈ 0.285 and a supplied link to v. |
| HIER-2, fermion mass hierarchy | OPEN (the referee did not confirm MASS-NO) | Proved: the exponents are blind to sector (u, d, e), and free-integer fits carry no evidence. Checked numerically on a comparator node space: one symmetry-fixed period-2 breaking gives Dirac gaps only at orders {1, 3}. So a single lattice breaking cannot make three generations. |

**Open routes.** Each trades the hierarchy for an unfixed number.
- A supplied confining sector at g² ≈ 0.285, plus a link to v.
- An integer extent: clockwork chains, slab or domain-wall depth, or D-theory extent. Exponential localisation turns an integer of about 30 into a factor of 1e-16.
- Two independent breaking amplitudes; dilute or longer-period breaking (ε = ε₀(a/L)³, with the rung assignment supplied).
- Near-conformal or walking dynamics.
- Interaction-driven masses.

**Defects found on main (not edited; for a fix task).**
- One β = 6 colour coupling is placed at the Planck scale and at the QCD scale in different notes, 18.8 decades apart.
- `GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md:73-76` misidentifies 0.019, which is observed α_s at M_Pl, as the β = 6 coupling in the MS-bar scheme.
- Main carries two different values of r0/a at β = 6: 5.006 and 5.37.
- The regulator dependence of 16 is a retained no-go on main; HIER-1 should have credited it.

**Against my advance predictions.** I predicted REDUCED for the scale hierarchy; the result is a sharper NO-GO plus G-OUTSIDE. I predicted PARTIAL or OPEN for the masses; the reading is OPEN.
