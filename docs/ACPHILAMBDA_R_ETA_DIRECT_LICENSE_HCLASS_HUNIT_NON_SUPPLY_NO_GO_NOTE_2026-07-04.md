# Record Additivity Does Not Fix the R-eta Unit Calibration

**Date:** 2026-07-04; countermodel repair 2026-07-11
**Type:** no_go
**Claim type:** no_go
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.py`](../scripts/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.txt`](../logs/runner-cache/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.txt)

## Narrow no-go claim

Grant the R-eta h-class hypothesis: the charged-lepton eta readout lies in the
fixed-locus density class represented by a nonzero local scalar `h`. This grants
the class, not its identity calibration. Even with that grant, the
[four axioms](MINIMAL_AXIOMS_2026-06-29.md) do not entail

```text
|delta| = h,
Phi = 3|delta| = 3h.
```

They admit a real one-parameter family of readouts

```text
I_beta(R) = beta h N(R),
```

where `N(R)` is the number of records in a finite pairwise-disjoint record
collection. Every real `beta` satisfies empty-zero, record-content
determination, and finite additivity. The target is `beta=1`; `beta=2` is an
explicit countermodel with the same axiom structure and the same granted `h`.
For a singleton record `x` and a three-record cycle `C`, respectively,

```text
|delta_beta| = I_beta({x}) = beta h,
Phi_beta = I_beta(C) = 3 beta h.
```

Thus the same free coefficient changes the original AC(ii) eta-angle identity
and its additive cycle-holonomy consequence.

This is a no-go for the direct inference from Record additivity to the R-eta
h-unit. It is not a claim against a future same-observable holonomy theorem,
an explicit coordinate convention after a same-observable theorem, or a
stronger physical readout law.

## Countermodel family

Keep the Lattice, Qubit, and Admissibility structures fixed. Let a state carry
finite-support records, each locking one admissible local possibility as the
Record axiom requires. For a finite record collection `R`, define `N(R)` as
its cardinality. Because cardinality depends on record content and not on a
site label, it is invariant under translations, proper cubic rotations, and
permutations of the three cycle positions.

For any real `beta`, set

```text
I_beta(empty) = 0,
I_beta(R disjoint-union S) = I_beta(R)+I_beta(S),
I_beta(R) = beta h N(R).
```

The first two equations follow directly from cardinality. For a singleton
record `x` and a three-record cycle `C`,

```text
I_beta({x}) = beta h,
I_beta(C) = 3 beta h.
```

When `h=2/9` is granted, `beta=1` gives the eta angle `2/9` and cycle
holonomy `2/3`, while `beta=2` gives `4/9` and `4/3`. Both models obey the
stated axiom requirements. Therefore those requirements do not entail
`beta=1` at either the singleton eta-angle resolution or the three-record
cycle resolution.

The countermodel is real and hence even under complex conjugation. Adding a
K/CPT-evenness requirement does not remove the free coefficient.

## Scope

The result grants the h-class association for the sake of the argument. It
therefore proves a narrower and stronger residual statement than a joint
h-class/h-unit discussion: h-unit remains unentailed after h-class has been
supplied.

The result does not derive or refute the physical R-eta identification. It
does not set `h`, `delta`, `r`, or a charged-lepton mass, and it does not force
`r=1/2`. It changes no axiom, approved primitive, premise registry, or audit
verdict.

The current target is the zero-weight `open_gate` in
[`AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md).
Historical decision text identifies provenance only and is not used as proof.

## No-Go Discipline Gate

### N1 — alternative route enumeration

| Route tested against the countermodel | Marker | Result and authority/check |
|---|---|---|
| Full Record readout route | ATTEMPTED | Empty-zero, record-content determination, and finite disjoint additivity all hold for every real `beta`; Record clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Parts A--C. |
| Lattice and cycle symmetry | ATTEMPTED | `N(R)` is invariant under translations, proper cubic rotations, and cycle-position permutations; Lattice clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Part B. |
| K/CPT-even real readout | ATTEMPTED | Real `beta` and real `h` make `I_beta` unchanged by complex conjugation; this is an extra grant checked in runner Part B, not axiom content. |
| Pointwise realized-state evaluation | ATTEMPTED | Evaluating the same realized record state leaves the law-level coefficient `beta` free; [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) boundary plus runner Parts A--C. |
| Dimensionful scale reference | ATTEMPTED | The [scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) supplies units conversion and no dimensionless phase, selector, or readout bridge; `beta` is dimensionless, runner Part D. |
| Kinetic-form isotropy | ATTEMPTED | The [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) supplies `c_t=c_s` and no phase, selector, or readout bridge; the family is unchanged, runner Part D. |
| Exact fixed-locus value | ATTEMPTED | Granting the nonzero value `h=2/9` leaves both `beta=1` and `beta=2`; runner Part A checks the singleton and cycle values separately. |

The runner checks all seven routes. Their authority boundary is the current
minimal axiom memo, the approved primitive boundary notes, and the explicit
family above; no prior negative row is used as a witness.

### N2 — wall independence

The scoped claim carries one wall: `W_unit`, the coefficient `beta=1` in
`|delta|=beta h`. The h-class face of AC(ii) is an explicit hypothesis, not a
second unresolved wall in this theorem. The three-record relation
`Phi=3|delta|` is an additive consequence of the same coefficient, not an
independent normalization wall. No pairwise wall table is needed after this
collapse.

### N3 — hidden-wall scan

The proof text was scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| granted h-class and `h` | explicit hypothesis that strengthens the countermodel |
| historical-target language in the AC(ii) boundary discussion | non-load-bearing provenance for the current open obligation |
| `registered` in the mass-coordinate path | non-load-bearing description of a partial route |
| scan terms appearing in this checklist sentence | audit metadata, not proof steps |

No other scan hit is used in the proof.

### N4 — residual matching

No prior no-go row is cited as evidence. The target is matched directly against
`AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`, which requires the
physical readout to be the fixed-locus density class `h`, identity-read in
h-units as the eta angle, with no intervening normalization factor.

| Target or prior negative witness | Residual there | Current residual | Match/disposition |
|---|---|---|---|
| current R-eta open obligation | h-class plus identity h-unit for the eta angle | h-class granted; identity h-unit `|delta|=h` tested | exact match to the h-unit face |
| prior negative witness: none | n/a | the same h-unit face, with `Phi=3|delta|` kept as a consequence | direct countermodel; no witness citation to drop |

### N5 — rhetoric and resolution audit

The countermodel is checked for the empty collection, a singleton eta-angle
readout, finite disjoint collections, a three-record cycle holonomy, and
arbitrary finite cardinality. It supports the statement that the named
finite-record axioms do not entail `beta=1` at those resolutions. It makes no
per-mode, per-action-block, continuum, or lattice-wide dynamical claim, and no
claim against a future same-observable theorem.

### N6 — partial-closure paths

| Candidate path | Current status | What it would address |
|---|---|---|
| current zero-weight R-eta obligation | open derivation target, not a premise | records both walls without supplying either one |
| convention-only coordinate ratification | not adopted as a separate convention | could dispose of h-unit only after the physical fixed-locus scalar and eta angle are shown to be the same observable |
| same-observable determinant-line/holonomy theorem | no retained theorem on the current ledger surface | h-class and h-unit by physical derivation |
| `ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md` | unaudited source context | registered value face; does not identify the physical fixed-locus observable |

These paths remain compatible with the result. The derivational and
convention-only paths are not supplied by the four axioms or approved
primitives. This note does not classify them as impossible and does not propose
a new primitive.

### N7 — steelman

The strongest objection is that radians make the identity coefficient a
coordinate statement rather than new physics. That objection succeeds if the
fixed-locus scalar and the physical eta angle are first proved to be the same
observable in the same coordinate. The current axioms name neither object and
contain no such identity. Thus the objection identifies a same-observable path
while leaving the present derivational non-entailment intact.

### N8 — cross-cycle echo

| Similar mechanism | Was its wall retired? | Applicability here |
|---|---|---|
| historical AC(ii) governance adoption and withdrawal | now provenance only; no premise content remains | the current target is the zero-weight R-eta obligation |
| theta mass-side split | occupancy and quark-determinant readout are independent obligations; no theta theorem is used here | the analogous mechanism here is a retained same-observable/readout theorem that closes exactly this obligation |
| scale-reference primitive | calibration made explicit by owner approval | an analogous h-unit primitive would relocate the premise, not derive `beta=1` |
| registered mass-coordinate reconstruction | reconstructs phase after state data are supplied; current source row is unaudited | does not establish the h-unit identity for the physical fixed-locus observable |
| identity-unit/radian-convention source routes | current relevant source rows are unaudited, so they are not used as authority here | they motivate convention tests but do not refute this direct countermodel |

All listed mechanisms have been considered and do not refute the narrow
current-surface claim.

**Gate result: PASS.** N1–N8 support the finite-record, current-surface
non-entailment statement above.

## Verification

Run:

```bash
python3 scripts/acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_2026_07_04.py
```

Expected result: `PASS=40`, `FAIL=0`.
