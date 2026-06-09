# kappa_EW is an axiom-boundary admission: the axioms supply no weighting

**Date:** 2026-06-09
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict; effective status is pipeline-derived after
independent audit.
**Primary runner:**
[`scripts/frontier_ew_kappa_axiom_boundary_admission.py`](../scripts/frontier_ew_kappa_axiom_boundary_admission.py)
(`RUNNER STATUS: PASS (PASS=10 FAIL=0)`, zero PDG/experimental inputs).

## Summary

The EW absolute normalization (the `kappa_EW = 0` color projection: `sqrt(9/8)` on
`g_1, g_2` and `sqrt(8/9)` on `y_t`/`m_t`) rides a single coefficient `kappa_EW`,
the weight of the color-singlet channel in the EW current correlator's color
readout `Pi_phys = C + kappa_EW S`. A portfolio of route-specific no-gos has shown
no derivation route fixes it (CMT, OZI, tracelessness, Monte Carlo, color-blindness,
the Route-2 `c_TE = -R_conn` bridge, and the Record register-not-read route). This
note records **why**, from the axiom boundary, and answers the standing question
"is the framework wrong, or do the axioms have an issue?":

- **`kappa_EW` is a weighting.** It is the free inter-sector weight in the color
  readout; the central-sector partition delivers the channel **count** (the
  `(N_c^2-1)/N_c^2 = 8/9` cardinality fraction) but not the weight (runner §A).
- **The axioms explicitly supply no weighting.** The Record axiom
  ([`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md)) states verbatim that
  a record supplies "no readout context, decomposition, ... **weighting**,
  normalization, ...". The Quantum axiom supplies "no ... **physical observable
  bridge**." `kappa_EW` is a weighting in the EW physical-observable bridge —
  doubly axiom-disclaimed (runner §B).
- **Therefore `kappa_EW` is not derivable from {Lattice, Quantum, Record} alone** —
  not only contingently (the route-specific no-gos) but as a direct consequence of
  the axiom boundary. Each route-specific no-go confirms this from a different
  angle: each tries to derive a weighting the axioms supply no rule for (runner §D).

**Answer:** the framework is internally consistent and the axioms are minimal and
clean — there is no axiom *defect*. But `kappa_EW = 0` is an **admitted input** — a
**candidate Tier-A admission** of the same axiom-disclaimed class as the two
*registered* admissions (`AC_phi_lambda` = the sector-generation rule / matter
realization; `theta` = the source/action) — currently **absent** from
`tier_a_admissions.json` (runner §C); its recognition is for the audit lane, which
owns the registry. The framework's EW absolute-normalization precision is
conditional on it; `sin^2(theta_W)` is `kappa_EW`-invariant within the construction
(unconditional with respect to `kappa_EW`) (runner §E).

This note does **not** fabricate `kappa_EW = 0` and does **not** assert
`kappa_EW = 1`. It records that the coefficient is an admission, not a derivable
value.

## The axiom boundary (the load-bearing fact)

[`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md):

- **Record** — "A record supplies no readout context, decomposition, `K`/CPT
  structure, sector-generation rule, **weighting**, normalization, probability,
  measurement/decoherence dynamics, time metric, within-sector data, or occupancy
  rule."
- **Quantum** — "does not supply a dynamics, composition theorem beyond the named
  lattice placement, measurement instrument, Born rule, species identification,
  gauge group, particle content, or **physical observable bridge**."
- **Lattice** — "does not supply a dynamics, boundary condition, metric scale,
  lattice spacing, continuum or infrared limit, ... or physical unit conversion."

`kappa_EW` is a weight in the color readout of the EW physical-observable bridge.
"Weighting" and "physical observable bridge" are *named* axiom exclusions.
Deriving `kappa_EW` from the axioms would require the axioms to supply exactly the
content they enumerate as not-supplied. This is the structural reason every route
fails — and it is independent of which route is tried.

## `kappa_EW` is a weighting, not a count

The color readout splits the `q`-`qbar` matrix `G in End(C^{N_c})` into the trivial
(singlet) and adjoint sectors with weights `S = (1/N_c)|Tr G|^2` and `C`. The
central-sector partition delivers the cardinality **count** `1 : N_c^2-1`
(`-> 8/9`), but the readout `Pi_phys = C + kappa_EW S` requires the inter-sector
**weight** `kappa_EW`: `Pi(0) = C` and `Pi(1) = C + S` are both functions of the
same `{S, C}` (runner §A). A weight is exactly what the partition (and the Record
axiom) does not deliver — the same structure by which registration "constrains the
Koide within-block weight `r` not at all" (plain-text in-flight companion:
`docs/EW_KAPPA_REGISTRATION_REGISTERS_ALL_COLOR_SECTORS_NO_GO_NOTE_2026-06-09.md`).

## Parallel with the registered admissions

`tier_a_admissions.json` registers exactly two genuine admitted inputs; each is a
named axiom-disclaimed category:

| Admission | Axiom-disclaimed category | Registered? |
|---|---|---|
| `AC_phi_lambda` (matter realization) | "sector-generation rule" (Record) | yes |
| `theta` (strong-CP) | "source/action" (MINIMAL_AXIOMS open-gates) | yes |
| **`kappa_EW`** (EW color readout weight) | **"weighting" (Record)** | **no** |

`kappa_EW` is a **candidate** third admission of the same class — content the
axioms explicitly do not supply — currently outside the registry. Recognition is
the audit lane's to make; this note only proposes it, sets no audit status, and
does not edit the registry.

## Why this is not a derivation gap to keep attacking

The route-specific no-gos on `main` —
[`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)
(CMT/packet),
[`EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27`](EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md)
(OZI size-class),
[`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)
(tracelessness),
[`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) (MC-not-a-derivation), and
[`EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08`](EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md)
(MC-undecidable / scheme weight) — each closes one route. This note unifies them:
they fail because the target is a weighting and the axioms supply no weighting.
Closing `kappa_EW` therefore requires **additional non-axiom content** — a new
admitted input or new structure — the same status as `AC_phi_lambda` and `theta`;
it is not derivable from `{Lattice, Quantum, Record}` alone.

The `sin^2(theta_W)` robustness (the framework applies `sqrt(K_EW)` equally to
`g_1, g_2`, so it cancels — runner §E) is itself a feature of the *admitted*
observable-bridge placement of `kappa_EW`: a different admissible placement (e.g.
a fermion-weighted quark-loop placement) would not cancel. The `kappa`-invariance
of `sin^2(theta_W)` is therefore part of the admission, not an axiom consequence —
but it does hold for the framework's construction, so `sin^2(theta_W)` carries no
`kappa_EW` conditionality.

## No-Go Discipline (N1-N8)

**N1 — Alternative routes (>=5).** (1) derive the weight from the Fierz count —
ruled out: count != weight (runner §A). (2) derive it from Record registration —
ruled out: Record supplies no weighting (the register-not-read no-go). (3) derive
it from CMT/OZI/tracelessness/MC — ruled out (the four `main` no-gos). (4) fix it
by the lattice coupling extraction — that extraction is part of the physical
observable bridge the Quantum axiom does not supply. (5) admit a new structure
(a non-axiom lattice-current selector) — open, and that is precisely the
"new admitted input" status this note assigns. (6) ATTEMPTED-OPEN: a `sin^2(theta_W)`
fermion-weighted placement makes `kappa` observable — but the placement itself is
admitted (not axiom-fixed), so this relocates the admission, it does not remove it.

**N2 — Wall independence.** Two objects: (a) `kappa_EW` is a weighting (algebra,
runner §A); (b) the axioms supply no weighting (axiom text, runner §B). (a) names
the target's type; (b) is the boundary. Neither follows from the other.

**N3 — Hidden-wall scan.** The load-bearing facts are the weight/count distinction
(exact algebra) and the verbatim axiom-exclusion list (faithful parse of
`MINIMAL_AXIOMS_2026-06-05`, runner §B). No "standard QFT / by construction" step
and no PDG value is load-bearing.

**N4 — Residual matching.** The residual ("`kappa_EW` is an admitted input") matches
the matching-rule no-go's "extra premise, not a consequence of the retained
primitives," now grounded at the axiom (not packet) level.

**N5 — Rhetoric audit.** The note does not say the framework is wrong or the axioms
are defective; it says `kappa_EW` is an admission the axioms' own boundary
foreclosed from derivation, and is currently unregistered.

**N6 — Partial-closure scan.** No convention/relabeling closes it: closing requires
a new admitted input or new structure (same as `AC_phi_lambda`, `theta`).

**N7 — Steelman.** *"A weighting could be forced by a finer/different readout
context the axioms permit."* Reply: the readout context is itself named as
not-supplied by Record; choosing one to force `kappa_EW` is supplying admitted
content, i.e. an admission — which is the conclusion, not a refutation.

**N8 — Cross-cycle echo.** `AC_phi_lambda` and `theta` remain the registered
admissions; this note proposes `kappa_EW` as a candidate third of the same
axiom-disclaimed class (recognition is the audit lane's).

## Does Not Claim

- Does **not** claim `kappa_EW = 0` (it does not fabricate the data-preferred value)
  or `kappa_EW = 1` (it does not assert the full-trace value).
- Does **not** claim the framework is internally wrong or the axioms are defective.
- Does **not** edit `tier_a_admissions.json` or set any audit status; it proposes the
  recognition for the audit lane.
- Does **not** add an axiom, primitive, or new vocabulary; "weighting", "readout
  context", and "physical observable bridge" are the axiom note's own terms.

## Verification

```bash
python3 scripts/frontier_ew_kappa_axiom_boundary_admission.py
```

Verifies (zero PDG inputs): (A) `kappa_EW` is a free inter-sector weight while the
partition delivers the `8/9` count; (B) the verbatim Record ("weighting") and
Quantum ("physical observable bridge") axiom exclusions in `MINIMAL_AXIOMS_2026-06-05`;
(C) the registry has two admissions and `kappa_EW` is absent, with the
axiom-disclaimed parallel for all three; (D) the route-specific no-go portfolio is
present (each confirming the target is a weighting from a different angle);
(E) `sin^2(theta_W)` `kappa`-invariance.
Expected: `RUNNER STATUS: PASS (PASS=10 FAIL=0)`.

## Safe wording

**Can claim:**
- "`kappa_EW` is a weighting, and the Record axiom explicitly supplies no weighting;
  so `kappa_EW` is an axiom-boundary admission, not a value derivable from the axioms
  alone."
- "`kappa_EW` is a candidate third admitted input of the same class as
  `AC_phi_lambda` and `theta`, currently unregistered (recognition is the audit
  lane's)."
- "The EW absolute normalization is conditional on this admission; `sin^2(theta_W)`
  is unconditional with respect to `kappa_EW` within the existing construction."

**Cannot claim:**
- bare `retained` / `promoted`.
- "`kappa_EW = 0`/`= 1` is forced."
- "The framework is wrong" or "the axioms are defective." (Neither — the axioms are
  minimal and explicit; `kappa_EW` is an admission *by* the axiom boundary.)
- editing the Tier-A registry or setting an audit verdict (the note only proposes
  the recognition).
