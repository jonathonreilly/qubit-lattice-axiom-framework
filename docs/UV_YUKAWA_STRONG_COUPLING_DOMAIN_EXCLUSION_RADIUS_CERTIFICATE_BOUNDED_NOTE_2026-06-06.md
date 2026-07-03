# UV Gauge-to-Yukawa Coefficient Selection: Strong-Coupling Domain Exclusion at beta=6

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. It writes no audit verdict and supplies no direct
effective-status change.
**Primary runner:**
[`scripts/frontier_uv_yukawa_sc_exclusion_certificate_2026_06_06.py`](../scripts/frontier_uv_yukawa_sc_exclusion_certificate_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_uv_yukawa_sc_exclusion_certificate_2026_06_06.txt`](../logs/runner-cache/frontier_uv_yukawa_sc_exclusion_certificate_2026_06_06.txt)

---

## Role

This is a **subordinate support** note for the audited_conditional bridge
[UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md](UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md)
(`uv_gauge_to_yukawa_bridge_sc_vs_pert_note`). That bridge selects the
**perturbative** leading 4-fermion coefficient

```text
    C_pert  = 1/(2 N_c) = 1/6      ->   y_t/g_s = sqrt(C_pert)  = 1/sqrt(6) = 0.40825
```

over the **strong-coupling** leading coefficient

```text
    C_strong = 1/N_c^2  = 1/9      ->   y_t/g_s = sqrt(C_strong) = 1/N_c    = 0.33333
```

on the framework's tadpole-improved canonical surface. The bridge argues the
selection **heuristically** ("the character-coefficient ratio `c_1/c_0 ~ O(0.4)`
at `beta=6` is not small, so the strong-coupling expansion does not converge
rapidly"). This note **replaces that heuristic** with a domain-exclusion
certificate built from the framework's own certified `beta=6` connected-plaquette
campaign, hardening the **strong-coupling-exclusion leg** of the selection.

**Why the selection (not the plaquette value) is the load-bearing piece for the
ratio.** In the `y_t/g_s` ratio the mean-link tadpole factor
`u_0 = <P>^(1/4)` cancels (bridge Step 4: `1/sqrt(u_0)` cancels in `y_t/g_s`).
So the *value* `<P> = 0.5934` is **not load-bearing for the ratio**; the
**choice** between `C_pert` and `C_strong` is exactly what fixes the ratio at
`1/sqrt(6)` versus `1/N_c`. The two forks are numerically distinct
(`0.40825` vs `0.33333`), so the selection is non-vacuous.

---

## (A) The two leading coefficients are reproven here (the fork is exact)

- **`C_pert`** from the retained SU(N_c) Fierz identity
  ([YT_EW_COLOR_PROJECTION_THEOREM.md](YT_EW_COLOR_PROJECTION_THEOREM.md)),
  `sum_A (T^A)_ab (T^A)_cd = 1/2 (d_ad d_bc - (1/N_c) d_ab d_cd)`, verified in the
  runner on explicit SU(3) generators (residual `5.6e-17`); the color-singlet
  projection of one-gluon exchange gives `C_pert = 1/(2 N_c)`, hence
  `y_t/g_s = 1/sqrt(6)`.
- **`C_strong`** from the one-link Haar integral
  `int dU U_ab (Udag)_cd = (1/N_c) d_ad d_bc` (bridge B.1), Haar-sampled
  cross-check (max deviation `0.0018 -> 0`); two link bilinears + the same Fierz
  give `C_strong = 1/N_c^2`, hence `y_t/g_s = 1/N_c`.

## (B) The strong-coupling radius is certified: R_SC ~ 5.39 < 6

The connected single-plaquette series
`Delta(beta) = <P> - P_1plaq = sum_{n>=5} d_n beta^n` has exact coefficients
(derived from SU(3)-Haar primitives + the reproven Picard-Fuchs `J` recurrence in
the on-main campaign runners and **reused here**):

```text
    d_5 = 1/472392     d_6 = 7/5668704      d_7 = 5/17006112      d_8 = 5/272097792
    d_9 = -2035/264479053824     d_10 = -10483/5289581076480     d_11 = -13/3967185807360
```

The runner reproves the radius from these by **d-log Pade**. The `d_9 < 0` sign
change (with `d_8 > 0`) forces a **complex-conjugate** dominant singularity (a
real pole is ruled out). The `d_10`-activated balanced `[2/2]` d-log Pade gives

```text
    beta_c ~ 1.781 +/- 5.083 i ,   |beta_c| = R_SC ~ 5.386 ,   arg ~ +/-70.7 deg
```

independently reproducing the on-main radius result
[BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md).
**Teeth (controls that fire):** the `[1/1]` real-pole ansatz returns a *spurious*
real pole `~3.375` (invalid for a complex pair), and a naive early-coefficient
ratio `sqrt(|d_6/d_8|) ~ 8.2 > 6` *over-estimates* the radius (the real-pole
intuition mis-applied to a complex pair). Only the complex-pair-aware estimators
give `R_SC ~ 5.3-5.4`, consistent with the literature Fisher-zero
`|beta_c| ~ 5.7` (Li-Meurice, arXiv:0710.5771; **comparator only, never an
input**).

## (C) The radius is observable-independent (Fisher-zero lemma)

At finite volume every lattice observable is a ratio
`<O> = N_O(beta) / Z(beta)` of **entire** functions of `beta` (finite sums of
`exp(-beta S)`). Its only finite-`beta` singularities are therefore **zeros of
the common partition function `Z`** (Fisher zeros), which are
**observable-independent**. The 4-fermion coefficient is a local observable, so
its strong-coupling radius equals the same `R_SC` that the plaquette series
measures. The runner illustrates this on a minimal toy `Z = b^2 - 4b + 5`
(zeros `2 +/- i`): two distinct observable numerators both yield radius
`|b_c| = sqrt(5)`. Physical statement: Yang-Lee / Fisher; Itzykson-Drouffe,
*Statistical Field Theory* (comparators).

## (D) The exclusion, and the complementary perturbative leg

Because `beta = 6 > R_SC ~ 5.39`, the leading **strong-coupling** coefficient
`C_strong` lies **beyond its domain of convergence** at `beta = 6`: the
strong-coupling fork (ratio `1/N_c`) is **excluded**. The complementary
**perturbative** leg is *in* its domain: `alpha_LM = alpha_bare/u_0 = 0.0907 << 1`
(optimal asymptotic truncation `~ pi/alpha_LM ~ 35` loops, re-verified). Hence
`C_pert` is the leading term of the **only convergent expansion** at `beta = 6`,
and the selection `y_t/g_s = 1/sqrt(6)` is forced on this leg.

---

## Scope and honest residual

This certificate closes the **strong-coupling-exclusion leg** of the bridge's
selection (the conceptually load-bearing `1/sqrt(6)`-vs-`1/N_c` fork for the
ratio). It does **not** by itself lift `uv_gauge_to_yukawa_bridge_sc_vs_pert_note`
to retained. The bridge remains conditional on:

1. an **absolute** derivation of `<P>(6) = 0.5934` — this cancels in the ratio,
   but its absolute value is the **deferred `beta=6` wall** (the open
   `rho_{p,q}(6)` / treewidth-29 object) for any absolute `g_s` use;
2. the **`g_bare` / staggered-Dirac trace-normalization** gates (a separate
   matter-sector lane);
3. **shared tadpole transport**.

The radius `R_SC` is **evidence** (three concurring complex-pair estimators
trending `4.81 -> 5.39` with order + the literature Fisher-zero comparator), not
a closed-form proof of divergence; "exclusion" here means precisely "`beta = 6`
lies beyond the certified/cross-checked strong-coupling radius."

## Reprove-and-cite ledger

- **Reproven here** (runner): the SU(N_c) Fierz identity on explicit generators;
  `C_pert = 1/(2 N_c)`, `C_strong = 1/N_c^2`, and their `y_t/g_s` forks; the
  one-link Haar identity (Haar-sampled); the `R_SC` d-log Pade from `d_5..d_11`;
  the observable-independence toy lemma; `alpha_LM = 0.0907 < 1`.
- **Cited** (derivation lives elsewhere, reused, not re-derived): the exact
  `d_5..d_11` connected coefficients from the on-main campaign runners
  `frontier_beta6_d9/d10/d11_coefficient_2026_06_04.py` and the certified-backbone
  note; the literature Fisher-zero `|beta_c| ~ 5.7` (Li-Meurice, arXiv:0710.5771;
  hep-lat/0507034) as a **comparator** for the radius evidence.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote this note or change any
audited claim scope.

- [UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md](UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md)
- [BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md)
- [BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md)
- [BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md)
