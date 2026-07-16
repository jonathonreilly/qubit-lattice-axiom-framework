# UV Gauge-to-Yukawa Coefficient Comparison: Plaquette-Series Radius Evidence Does Not Select an Expansion at beta=6

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

This is a **subordinate support** note for the bounded bridge
[UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md](UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md)
(`uv_gauge_to_yukawa_bridge_sc_vs_pert_note`). It consumes only the bridge's
finite coefficient packet:

```text
    C_pert   = 1/(2 N_c) = 1/6
    C_strong = 1/N_c^2   = 1/9
```

The bridge proves that these are distinct finite coefficient calculations and
preserves the public `C_strong = 1/N_c^2` convention. It does not select either
coefficient as physically governing, identify either square root with a
Yukawa/gauge readout, or supply a convergence theorem.

The plaquette-series exercise below remains useful only as finite-order
domain evidence for that plaquette series. It cannot promote the coefficient
comparison into a selector: a finite d-log Padé estimate is not a convergence
proof; a common partition-function denominator does not prevent
observable-specific numerator cancellation; and a small displayed coupling
does not prove convergence of the perturbative expansion.

---

## (A) The two leading coefficients are reproven here (the fork is exact)

- **`C_pert`** from the retained SU(N_c) Fierz identity
  ([YT_EW_COLOR_PROJECTION_THEOREM.md](YT_EW_COLOR_PROJECTION_THEOREM.md)),
  `sum_A (T^A)_ab (T^A)_cd = 1/2 (d_ad d_bc - (1/N_c) d_ab d_cd)`, verified in the
  runner on explicit SU(3) generators (residual `5.6e-17`); the color-singlet
  coefficient magnitude is `C_pert = 1/(2 N_c)`.
- **`C_strong`** from the one-link Haar integral
  `int dU U_ab (Udag)_cd = (1/N_c) d_ad d_bc`, with normalized singlet-projector
  coefficient `1/N_c` and unnormalized `delta_ab delta_cd` tensor coefficient
  `C_strong = 1/N_c^2`; the runner retains a Haar-sampled cross-check.

## (B) Plaquette-series d-log Padé evidence: R_est ~ 5.39

The connected single-plaquette series
`Delta(beta) = <P> - P_1plaq = sum_{n>=5} d_n beta^n` has exact coefficients
(derived from SU(3)-Haar primitives + the reproven Picard-Fuchs `J` recurrence in
the on-main campaign runners and **reused here**):

```text
    d_5 = 1/472392     d_6 = 7/5668704      d_7 = 5/17006112      d_8 = 5/272097792
    d_9 = -2035/264479053824     d_10 = -10483/5289581076480     d_11 = -13/3967185807360
```

The runner forms a finite-order **d-log Padé** estimate from these coefficients.
The `d_9 < 0` sign change with `d_8 > 0` is consistent with complex-pair
behavior, and the balanced `[2/2]` approximant gives

```text
    beta_c ~ 1.781 +/- 5.083 i ,   |beta_c| = R_SC ~ 5.386 ,   arg ~ +/-70.7 deg
```

consistent with the on-main radius evidence
[BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md).
**Teeth (controls that fire):** the `[1/1]` real-pole ansatz returns a *spurious*
real pole `~3.375` (invalid for a complex pair), and a naive early-coefficient
ratio `sqrt(|d_6/d_8|) ~ 8.2 > 6` *over-estimates* the radius (the real-pole
intuition mis-applied to a complex pair). Only the complex-pair-aware estimators
give estimates near `5.3-5.4`, consistent with the literature Fisher-zero
`|beta_c| ~ 5.7` (Li-Meurice, arXiv:0710.5771; **comparator only, never an
input**). This finite packet does not certify the exact convergence radius.

## (C) Why the plaquette estimate is not a four-fermion selector

At finite volume every lattice observable is a ratio
`<O> = N_O(beta) / Z(beta)` of **entire** functions of `beta` (finite sums of
`exp(-beta S)`). Common Fisher zeros are possible singularities, but a numerator
can cancel a zero of `Z`; the nearest uncancelled singularity and therefore the
Taylor radius need not be identical for every observable. The runner now
includes both sharing and cancellation controls on a minimal toy denominator.
Consequently the plaquette d-log Padé estimate cannot by itself be assigned to
the four-fermion coefficient.

## (D) Open selector and transport conditions

No governing-expansion conclusion follows from this packet. A selector would
still have to connect an expansion-domain theorem for the relevant
four-fermion observable to the stated action and surface. Separately, any
physical Yukawa/gauge readout still needs the canonical-surface, `g_bare`,
staggered-Dirac, and transport inputs named by the parent bridge.

---

## Scope and honest residual

This note does not close a strong-coupling-exclusion or perturbative-selection
leg for `uv_gauge_to_yukawa_bridge_sc_vs_pert_note`. It preserves only the exact
coefficient comparison plus the plaquette-series diagnostic. The open
conditions include:

1. a convergence/domain theorem for the relevant four-fermion observable,
   rather than a plaquette-only finite-order estimator;
2. a physical selector connecting that domain result to `C_pert` or
   `C_strong`;
3. the separate plaquette/`u_0`, `g_bare`, staggered-Dirac, and shared
   tadpole-transport inputs required by any absolute readout.

The radius estimate is **evidence** from finite coefficients and comparators,
not a closed-form proof of convergence or divergence.

## Reprove-and-cite ledger

- **Reproven here** (runner): the SU(N_c) Fierz identity on explicit generators;
  `C_pert = 1/(2 N_c)` and the public unnormalized-tensor convention
  `C_strong = 1/N_c^2`; the one-link Haar identity (Haar-sampled); the finite
  d-log Padé estimate from `d_5..d_11`; and a toy cancellation control showing
  why common Fisher-zero denominators do not supply an observable-independent
  radius theorem.
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
