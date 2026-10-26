# Conditional de Sitter / S³ Spectral Consistency Identity

**Date:** 2026-04-18 (audit-prep cite-chain rigorize 2026-05-10)
**Status:** structural identity theorem; current ledger `effective_status:
audited_conditional` (see "Audit-driven dependency-edge rigorization (2026-05-10)"
below). Separates the exact identity `Lambda = lambda_1(S^3_R)` from the
still-bounded numerical value of `R` / `Lambda`.
**Script:** `scripts/frontier_cosmological_constant_spectral_gap_identity.py`
**Claim type:** positive_theorem
**Claim scope:** the exact function identity `Lambda_vac = lambda_1(S^3_R) =
3 / R^2` for every `R > 0`, on a comparison sphere explicitly assigned the de Sitter curvature radius
(the minimum-radius global slice), conditional
on the upstream-authority statuses recorded below; the numerical values of
`R` / `R_Lambda` / `Lambda` remain in the existing bounded cosmology rows.
**Upstream authorities (current ledger statuses, not assertions of
retainedness):**
[`UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md`](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md)
(unaudited),
[`UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md`](UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md)
(unaudited),
[`UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md`](UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md)
(unaudited),
[`S3_GENERAL_R_DERIVATION_NOTE.md`](S3_GENERAL_R_DERIVATION_NOTE.md)
(unaudited),
[`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)
(audited_conditional).

## Audit-driven dependency-edge rigorization (2026-05-10)

The 2026-04-30 leaf-resweep audit verdict on this row was `audited_conditional`
(load-bearing 19.996, direct-in-degree 23) with rationale: "The local step
cannot be promoted because direct upstream authorities remain unaudited,
support/open/unknown, or terminal non-clean." The named repair target was:
"dependency_not_retained: ratify or repair the listed upstream theorem/bridge
rows and rerun the local runner so it computes the disputed bridge rather
than only checking consequences."

The earlier framing of this note — "**proposed_retained structural identity
theorem** on `main`" with "Upstream authorities (all already retained on
`main`)" — predates the audit lane's later classification of those upstream
rows as `unaudited` or `audited_conditional`. This rigorize pass corrects the
header to track the live ledger so the audit graph routes to the correct
upstream statuses. It does not derive any of the upstream objects within this
packet, does not promote any sibling claim, and does not change this row's
`audited_conditional` status. Audit verdict and effective status are set by
the independent audit lane only; nothing in this rigorization edit promotes
status.

**Cited authorities and current ledger statuses (one-hop deps):**

| Cited authority | Role in this note | Current ledger status |
|---|---|---|
| [`UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md`](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md) | direct-universal discrete `3+1` GR closure on `PL S^3 x R` (theorem condition 1) | unaudited |
| [`UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md`](UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md) | smooth global weak gravitational stationary/Gaussian solution class (theorem condition 2) | unaudited |
| [`UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md`](UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md) | canonical textbook Einstein-Hilbert action family with cosmological-constant sector (theorem condition 3, used in Leg A) | unaudited |
| [`S3_GENERAL_R_DERIVATION_NOTE.md`](S3_GENERAL_R_DERIVATION_NOTE.md) | round `S^3` of radius `R` for any `R > 0` (theorem condition 4 part i) | unaudited |
| [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md) | `S^3` cap uniqueness (theorem condition 4 part ii) | audited_conditional |
| `COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` (backticked to break cycle-0043/0044 length-3 cycles; the load-bearing citation direction is *result_2026-04-12 → spectral-gap-identity* via the result note's own dependency chain, not the other way: Leg B Obata equality below is proved directly from Lichnerowicz-Obata, not from the result note) | "exact on the retained internal surface" point 2 — Leg B Obata equality attribution back-reference | unaudited |
| `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` (back-reference, not load-bearing — cosmology_scale_identification names this identity theorem as an *upstream* authority for its derivation chain, so the load-bearing citation direction is *cosmology_scale_identification → this identity*, not vice versa. Backticked to break length-2 cycle `cycle-0007` in `docs/audit/data/cycle_inventory.json`.) | "Fixed-gap vacuum scale" section — Leg A Einstein-side reference | audited_conditional |
| `DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md` (back-reference, not load-bearing — the EOS corollary is a downstream consumer that cites this identity theorem as upstream authority. Backticked to break the residual length-3 cycle in `docs/audit/data/cycle_inventory.json`; citation graph direction is *EOS corollary → this identity*.) | downstream EOS corollary that consumes this identity | unaudited |

**What the cite-chain does NOT close.** Five of the eight cited authorities
remain `unaudited`; two remain `audited_conditional`; none currently carry a
retained-grade ledger status. The `dependency_not_retained` repair target is
therefore not satisfied by this rigorize pass; the chain remains conditional
on those parent audits being upgraded. The runner's PASS=22/0 verifies the
two-leg algebraic identity (Leg A: vacuum Einstein trace contraction in
`D = 4` plus de Sitter throat Ricci giving `Lambda = 3/R^2` for `R` in
`{0.5, 1.0, 2.0, pi, 1e6, 1e26}`; Leg B: Lichnerowicz–Obata equality on
round `S^3` giving `lambda_1 = 3/R^2` for the same `R` sweep; closure:
both legs match to `0.0` residual at every `R`, with log-log slope `-2`
and intercept `log 3`); this is the bounded scope on which the row
stands.

**What this rigorize pass NEVER claims.** It does not derive the GR closure,
the smooth gravitational global solution class, the canonical textbook
continuum GR closure, or the round-`S^3` topology / cap-uniqueness from
the accepted axiom within this packet. It does not promote
`cosmological_constant_spectral_gap_identity_theorem_note` to retained or
remove the conditional perimeter on the upstream authorities listed above.

## Audit-aware repair path

Per `audit_ledger.json`, `notes_for_re_audit_if_any` for
`cosmological_constant_spectral_gap_identity_theorem_note`: the cheapest
path to a stronger audit verdict is to ratify or repair the eight
upstream theorem/bridge rows listed above and rerun the local runner so
it computes the disputed bridge rather than only checking consequences.
Either path makes the structural identity self-contained from retained-grade
upstream surfaces; the current note is conditional on those upstream rows
being upgraded.

## Scientific correction (2026-10-21)

The two radii must be distinguished. Write `ell` for the four-dimensional
de Sitter curvature radius and `a(t)` for the radius of a global spatial
S³ slice. In units c=1,

```text
ds² = -dt² + ell² cosh²(t/ell) dOmega_3²,
a(t) = ell cosh(t/ell),
Lambda = 3/ell²,
lambda_1(S³_a(t)) = 3/a(t)² = Lambda sech²(t/ell).
```

Thus equality with the spatial spectral gap holds at the minimum-radius
slice t=0, or on an auxiliary sphere whose radius is explicitly chosen to
be ell; it is not an identity on every spatial slice. A static product
`-dt²+R²dOmega_3²` has `R_00=0` and `R_ij=2g_ij/R²`, so no single positive
Lambda satisfies its vacuum Einstein equations. The previous constant-spatial-
radius de Sitter argument is withdrawn. See [Spradlin, Strominger and
Volovich, §2.1](https://arxiv.org/html/hep-th/0110007).

The local consistency identity below is conditional on identifying the
sphere's radius with ell. The Einstein equation already contains Lambda;
this computation does not determine it, derive it from topology, or solve
the vacuum-energy problem. Prior audit-history text above is preserved as
history, not a new status decision.

## Role

The purpose of this note is to split the existing spectral-gap
cosmological-constant companion into two strictly separated pieces:

1. an **exact structural identity** `Lambda_vac = lambda_1(S^3_R) = 3 / R^2`
   on the retained direct-universal GR de Sitter stationary vacuum sector,
   valid for any `R`, and
2. the **numerical value** of `R` / `Lambda`, which remains the
   cosmology-scale identification blocker and stays bounded.

The identity is already called "exact on the retained internal surface" in
`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` (backticked to break cycle-0043/0044;
attribution back-reference only, this note's Leg A/Leg B proof stands without that note)
(section "Exact on the retained internal surface", point 2), and the GR-side
derivation is already written out in
`COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md`
(section "Fixed-gap vacuum scale"; backticked here to break length-2 cycle `cycle-0007` in `docs/audit/data/cycle_inventory.json` — cosmology_scale_identification cites this identity theorem as an upstream authority for its own derivation chain, so the load-bearing citation direction is *cosmology_scale_identification → this identity theorem*, not vice versa). This note does not add new science —
it records a conditional consistency identity so downstream corollaries (including
`DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`, backticked here as a
downstream consumer rather than a load-bearing input) must carry the same radius-identification premise.

## Theorem

Let the retained surface carry:

1. the retained direct-universal discrete 3+1 GR closure on `PL S^3 x R`
   with an exact global Einstein/Regge stationary action family (authority:
   [`UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md`](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md));
2. the retained smooth global weak gravitational stationary/Gaussian
   solution class on the chosen smooth realization of `PL S^3 x R`
   (authority:
   [`UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md`](UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md));
3. the retained canonical textbook Einstein-Hilbert-style weak/stationary
   action family on the chosen realization, carrying a well-defined
   cosmological-constant sector (authority:
   [`UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md`](UNIVERSAL_QG_CANONICAL_TEXTBOOK_CONTINUUM_GR_CLOSURE_NOTE.md));
4. retained `S^3` spatial topology on `PL S^3 x R` with round spatial metric
   of radius `R`, for any `R > 0` (authority:
   [`S3_GENERAL_R_DERIVATION_NOTE.md`](S3_GENERAL_R_DERIVATION_NOTE.md),
   [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)).

**Theorem (spectral-gap cosmological-constant identity).** On the
stationary de Sitter vacuum sector of conditions (1)–(3), with the comparison sphere in condition (4) explicitly chosen at
`R=ell` (the minimum-radius global slice or an auxiliary sphere), the cosmological-constant scale `Lambda_vac`
and the first nonzero scalar-Laplacian eigenvalue `lambda_1(S^3_R)` are
equal as a structural identity:

  `Lambda_vac = lambda_1(S^3_R) = 3 / R^2`,

for every `R > 0`. The identity is an exact function identity in `R`; it
does **not** fix a numerical value of either `R` or `Lambda_vac`.

**Proof.** The proof compares two standard formulas after the supplied identification
`R=ell`; numerical agreement is not an independent derivation of that premise.

*Leg A (Einstein side, vacuum equations).* On the canonical textbook
Einstein-Hilbert-style continuum GR closure (condition 3), the action on
`PL S^3 x R` is

  `S = (1 / (16 pi G)) integral (R_4d - 2 Lambda) sqrt(-g) d^4 x`,

where `R_4d` is the 4D Ricci scalar and `Lambda` is the cosmological-constant
parameter of the action. The vacuum Einstein equations from this action are

  `R_{mu nu} - (1/2) g_{mu nu} R_4d + Lambda g_{mu nu} = 0`.

Trace-contraction with `g^{mu nu}` in `D = 4` gives

  `R_4d - 2 R_4d + 4 Lambda = 0  ==>  R_4d = 4 Lambda`,

and substituting back:

  `R_{mu nu} = Lambda g_{mu nu}`.

The de Sitter vacuum has `R_{mu nu}=(3/ell²)g_{mu nu}`, where ell
is its spacetime curvature radius, giving `Lambda_vac=3/ell²`.
For the comparison sphere in condition (4), additionally choose `R=ell`.
This radius identification is a premise, not a consequence of S³ topology.

This is the content of the "Fixed-gap vacuum scale" section of
`COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` (backticked, not a
markdown link, to break length-2 cycle `cycle-0007` in
`docs/audit/data/cycle_inventory.json`; see the demotion explanation in
the citation-table footnote above).

*Leg B (spectral side, Lichnerowicz–Obata).* On the round S^3 of radius `R`
(condition 4), the scalar Laplacian has exact spectrum `lambda_n =
n (n + 2) / R^2`, with first nonzero eigenvalue

  `lambda_1(S^3_R) = 3 / R^2`.

This is the Obata equality for spheres (Lichnerowicz–Obata 1962/1968):
for an n-dimensional round sphere of radius `R`, `lambda_1 = n / R^2`, and
for `n = 3` this gives `3 / R^2`. This is the content of the
"exact on the retained internal surface" point 2 of
`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` (backticked to break
cycle-0043/0044; attribution back-reference only).

*Closing.* Legs A and B give the same function `3 / R^2` of the same
retained radius `R`, so as an identity on the retained de Sitter stationary
vacuum sector,

  `Lambda_vac = lambda_1(S^3_R)`.

This holds for every `R=ell > 0` on the comparison sphere; it does not
establish equality for the evolving global spatial sphere. □

## Algebraic content under the radius-identification condition

- the coefficient `3` on both sides (Einstein: `R_{mu nu} = (3/R^2) g_{mu nu}`;
  Laplacian: Obata equality on S^3);
- the `1 / R^2` scaling on both sides;
- the **function identity** `Lambda_vac = lambda_1(S^3_R)` as a statement
  that holds for every `R > 0`, with no free parameter on the right-hand
  side that is not also on the left-hand side;
- the specialization of this identity to the retained de Sitter stationary
  vacuum sector of the direct-universal GR + smooth GR closure.

## What the identity does not establish

- the numerical value of `R` / `R_Lambda`: the cosmology-scale identification
  remains the honest remaining gap, as recorded in
  `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md`
  (backticked to break `cycle-0007`; see citation-table demotion footnote above),
  "Honest Remaining Gap";
- the numerical value of `Lambda`: remains the bounded companion
  result of
  `COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` (backticked to break
  cycle-0043/0044; see-also pointer only);
- the present-day `Omega_Lambda` value: remains gated on the matter-content
  bridge, unchanged;
- the full FRW / expansion-history derivation: still conditional.

This theorem is deliberately narrower than the full cosmology-companion
portfolio. Its point is to isolate the single exact structural claim — the
`R`-free identity between `Lambda_vac` and `lambda_1(S^3_R)` — so that
downstream corollaries that depend only on the identity (not on its
numerical evaluation) must retain the comparison-sphere premise.

## Downstream boundary

This correction supplies no publication-matrix or audit-status change.
The old packaging claim that an arbitrary fixed spatial S³ radius discharges
the downstream EOS premise is withdrawn. A constant cosmological parameter
fixes ell, while the global spatial radius a(t) still evolves. Downstream
uses must distinguish those radii and carry the radius-identification premise.
The numerical value of ell, matter fraction, physical spectral interpretation,
and framework-to-continuum bridge remain separate obligations.

## Commands Run

```bash
python3 scripts/frontier_cosmological_constant_spectral_gap_identity.py
```

## Boundaries

This note does not close:

- the numerical value of `R` / `R_Lambda`: cosmology-scale identification
  remains the honest remaining gap, recorded in
  `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md`
  (backticked to break `cycle-0007`; see citation-table demotion footnote above),
  "Honest Remaining Gap";
- the numerical value of `Lambda`: bounded companion result of
  `COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` (backticked to break
  cycle-0043/0044; see-also pointer only);
- the present-day `Omega_Lambda` value: gated on the matter-content bridge;
- the full FRW / expansion-history derivation: still conditional;
- any retained-grade promotion of the eight upstream authorities listed in
  the audit-driven dependency-edge rigorization section above;
- any chain closure beyond the two-leg algebraic identity reported by the
  runner.
