# Charged-Lepton Brannen-BAE Delta Conditional Algebra Note

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_charged_lepton_brannen_bae_delta_tier_a_bounded_verifier.py`](../scripts/frontier_charged_lepton_brannen_bae_delta_tier_a_bounded_verifier.py)

**Current authority (2026-07-11):** the filename and older taxonomy below are
historical provenance only. This note supplies no premise and cannot satisfy a
dependency. Its algebra is conditional on `delta=2/9` and `sqrt(2)`; deriving
those charged-lepton readout inputs remains an `open_gate`.

## 1. Why this note exists

A previously landed open-gate row,
`LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md`
(`effective_status=open_gate` on origin/main), records the conditional
Brannen-BAE mass-ratio chain at `delta = 2/9` as a named conditional
value to be derived or rejected by later source science.

Historically, the framework's former admitted-input index
`docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`
(meta on origin/main) and its machine sibling
[`docs/audit/data/premise_decision_history.json`](audit/data/premise_decision_history.json)
recorded the generation mass-pattern phase — "the C_3-breaking phase
delta (which collapses into the same delta tracked as the Koide
phase)" — under the former `AC_phi_lambda` decision.

These two source rows are consistent at the structural level but use
incompatible upstream framings. The open-gate row treats `delta = 2/9`
as an open derivation target; the historical index once recorded the
generation-pattern phase (= the Koide phase = `delta`) as accepted bounded
input. That historical treatment has no current authority.

The audit rubric (see
[`docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md`](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md))
states explicitly:

> "Tier-A admitted derivation targets are different: they are accepted
> non-axiom premises only at the bounded tier. A clean row depending on
> a Tier-A admitted derivation target may become `retained_bounded`
> after the pipeline computes effective status, but it is not eligible
> for full unbounded `retained` until that admission is retired by a
> retained derivation."

This note isolates the Brannen-BAE algebraic chain at `delta = 2/9` as
**conditional algebra under an explicit hypothesis**. It does not derive `delta`, does not derive the
amplitude-equipartition coefficient `sqrt(2)`, and does not derive the
overall scale `a`. It states only what the Brannen-BAE algebraic form
gives once those upstream Tier-A admissions are accepted, plus the
empirical comparator against PDG charged-lepton masses.

The note does not promote the Tier-A admission to retained, does not
modify the radian-bridge retained no-go, and does not change any
existing audit row's status.

## 2. Claim scope

### S1 — Algebraic structure (pure trigonometric identity)

Let the Brannen-BAE mass-ratio ansatz be

```text
x_k / a  =  1 + sqrt(2) * cos(delta + 2 * pi * k / 3)   for k = 0, 1, 2,    (B)
```

with `a > 0` the framework's overall charged-lepton scale and `delta`
the C_3-breaking phase. This is a fixed mathematical form; (B) is
algebra, not a derivation.

### S2 — explicit conditional hypothesis

For the conditional calculation, this note assumes the Brannen phase value

```text
delta  =  2 / 9    (radians)                                          (TA)
```

as a hypothesis. This note does not derive (TA). The related no-go portfolio
includes:

- [`koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md) (retained_no_go)
- [`koide_delta_lattice_wilson_selected_eigenline_no_go_note_2026-04-24`](KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md) (retained_no_go)
- [`koide_delta_marked_relative_cobordism_no_go_note_2026-04-24`](KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md) (retained_no_go)

These no-gos establish that the listed retained periodic phase
sources and finite-Wilson constructions cannot supply the literal
`2/9`-radian value. Thus (TA) remains open rather than premise content.

### S3 — Sorted positive-ratio values

Under (B) and (TA), the three values `x_0/a, x_1/a, x_2/a` are
positive real numbers and admit a unique sorted form. Direct
computation gives:

```text
x_sorted / a  ∈  { 0.040349908..., 0.580211920..., 2.379438172... }    (R)
```

with `x_0/a = 2.379438172...`, `x_1/a = 0.040349908...`, and
`x_2/a = 0.580211920...` before sorting. At this admitted phase all
three Brannen-BAE values are positive; the sorted positive ratios are
therefore just the increasing-order chamber presentation of the same
three algebraic outputs.

For the verifier, the values computed directly from (B)+(TA) without
any sign or ordering convention are reported. The verifier checks
that the three sorted positive values exactly match the independent
target set in (R) above (algebraic exactness, not numerical
comparator).

### S4 — Phase-independent Koide guardrail (retained crosscheck)

Independent of the value of `delta`, the Brannen-BAE ansatz with
coefficient `sqrt(2)` satisfies the Koide identity `Q = 2/3` exactly,
where

```text
Q  :=  sum(x_k^2) / (sum(x_k))^2.                                     (Q)
```

This is a retained pure-trigonometric identity, established in
[`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
(positive_theorem) and
[`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md).
The verifier checks `Q = 2/3` exactly on the values in (R).

**This is NOT evidence for `delta = 2/9` specifically.** The Koide
identity holds for every `delta` once the `sqrt(2)` coefficient is
assumed. (Q) is a crosscheck on the ansatz's mathematical
consistency with the retained Koide structure, not a derivation of
(TA).

### S5 — Empirical comparator (sidecar, not load-bearing)

Using PDG 2024 charged-lepton masses

```text
m_e   = 0.5109989461 MeV
m_mu  = 105.6583755 MeV
m_tau = 1776.86 MeV
```

and the empirical scale extraction

```text
a_PDG  :=  (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau)) / 3,
```

the PDG-extracted sorted positive ratios match the values in (R) to
relative deviation < 5e-5 per slot (max observed ~2.9e-5). Equivalently
the PDG-extracted phase on the same Brannen-BAE chamber is

```text
delta_PDG  =  0.222270... rad,
delta_PDG - 2/9  =  4.7e-5 rad.
```

This is a sidecar empirical comparator, not a derivation input. PDG
values are not consumed by S1-S4. The empirical match is recorded for
falsifiability tracking only.

## 3. What this bounded theorem does NOT claim

- Does **not** derive `delta = 2/9` from the framework baseline plus retained content. (TA)
  is an explicit conditional hypothesis; the radian-bridge no-go
  portfolio establishes that the listed native-unit constructions
  cannot supply it.
- Does **not** derive the amplitude-equipartition coefficient
  `sqrt(2)` (BAE). It is another explicit conditional input.
- Does **not** derive the overall charged-lepton scale `a`; the absolute scale
  is outside this dimensionless conditional calculation.
- Does **not** make any neutrino-sector claim.
- Does **not** derive `m_e`, `m_mu`, `m_tau` in MeV. Only the
  dimensionless sorted ratios are computed, plus the empirical
  sidecar match.
- Does **not** modify or promote the Tier-A admitted-input registry.
- Does **not** retire or weaken any retained no-go (the three
  radian-bridge no-gos remain authoritative).
- Does **not** propose a new axiom, new theory-language extension, or
  new admission.
- Does **not** predict any audit verdict on this note or any
  downstream row.

## 4. Setup (retained / conditional / no-go content cited honestly)

| Authority | Current standing on origin/main | Role in this note |
|---|---|---|
| one-qubit local algebra (`M_2(C) = Cl(3,0)` per site) | axiom premise | foundations; Brannen ansatz lives on this algebra |
| `Z^3` spatial substrate locality | axiom premise | foundations |
| [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | retained positive_theorem | S4 guardrail (`Q = 2/3` for any delta with `sqrt(2)` ansatz) |
| [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) | retained positive_theorem | S4 supporting equivalence |
| [`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) | retained positive_theorem | S1 algebraic ansatz foundation |
| `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` | historical meta only | provenance for the former treatment of (TA); no premise authority |
| [`docs/audit/data/premise_decision_history.json`](audit/data/premise_decision_history.json) | non-authoritative history | provenance only; the pipeline does not read this for status propagation |
| [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md) | retained_no_go | S2 no-go portfolio member; establishes (TA)'s irreducibility from A1-route content |
| [`KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25`](KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md) | retained_bounded | sharpens (TA) boundary: pins what a radian-bridge postulate would have to supply |
| `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26` | open_gate | current non-load-bearing open-derivation framing |
| Particle Data Group 2024 (m_e, m_mu, m_tau) | external observation | S5 empirical sidecar comparator only; not derivation input to S1-S4 |

## 5. Significance

S1-S4 are usable only as conditional algebra. They cannot propagate retained
status until retained derivations supply every open load-bearing hypothesis.

Concretely, the Brannen-BAE algebraic chain on the charged-lepton
sector then has a bounded source row that:

- exhibits the exact algebraic sorted positive ratios `{0.04035...,
  0.58021..., 2.37944...}` from (B)+(TA),
- crosschecks them against the retained `Q = 2/3` Koide identity,
- records the empirical PDG sidecar match at < 5e-5 per slot (sidecar; not load-bearing),
- explicitly leaves `delta = 2/9` as an open derivation target.

This conditional framing preserves the algebra and the radian-bridge no-go
portfolio without treating any governance decision as scientific supply.

## 6. Conditional structure

This bounded theorem is conditional on:

- (H_local_algebra) one-qubit local algebra — `M_2(C) = Cl(3,0)` per site.
- (H_substrate) `Z^3` spatial substrate locality.
- (H_Koide_Q) Retained Koide `Q = 2/3` algebraic narrow theorem.
- (H_circulant) Retained circulant-character bridge narrow theorem.
- (H_delta) `delta=2/9` is supplied only as an explicit conditional hypothesis.
- (H_no_go) The three radian-bridge no-gos retain their current
  `retained_no_go` status (this note relies on them only as boundary
  acknowledgments, not as positive content).

If any retained Koide row degrades, S1+S4 require re-examination. If
the Tier-A registry reclassifies AC_phi_lambda, S2's framing requires
re-examination.

## 7. Audit-lane handoff

Audit should check only the source claim:

- S1 algebraic Brannen-BAE ansatz form (pure algebra).
- S2 conditional use of the Brannen phase datum, acknowledged but not derived.
- S3 exact algebraic sorted positive ratios computed from S1+S2.
- S4 phase-independent `Q=2/3` Koide guardrail crosscheck.
- S5 sidecar empirical PDG match at <5e-5 per slot, not load-bearing for S1-S4.

The note predicts no verdict, does not promote `AC_phi_lambda`, does not touch an existing row, does not introduce an axiom, and does not weaken any no-go.

## 8. Relation to the prior open-gate row

This note is the historical-admission-era companion to
`LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26`.
The two notes carry the same algebraic content. They differ in
upstream framing:

| Row | Upstream framing | Use |
|---|---|---|
| `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26` | delta=2/9 as open derivation target | open-derivation framing |
| This note | delta=2/9 as an explicit conditional hypothesis | conditional algebra |

The open-gate row remains valid as a record of the open-derivation
view. This note does not retire it. The two coexist as
complementary historical source rows; downstream consumers must treat
`delta=2/9` as open unless a retained derivation supplies it.

## 9. Verification

Run:

```bash
python3 scripts/frontier_charged_lepton_brannen_bae_delta_tier_a_bounded_verifier.py
```

Expected: `PASS=N FAIL=0` with N ≥ 12.

The runner checks:
- S1 algebraic ansatz form is correctly computed
- S2 Tier-A registry files present on origin/main
- S3 sorted positive ratios match independent target values exactly
- S4 Q=2/3 holds exactly on the computed ratios
- S5 PDG sidecar match within stated tolerance (NOT load-bearing)
- Hostile-audit checks: no new derivation of delta, no Tier-A promotion,
  no no_go weakening, no PDG load-bearing in S1-S4

## 10. Sidecar references

- Brannen, C. (2005). Spectator equation for Yukawa coupling
  matrices.
- Koide, Y. (1981). Fermion-boson two-body model of quarks and
  leptons.
- Particle Data Group 2024.
- Buckingham, E. (1914). On Physically Similar Systems.

All sidecar context only. No load-bearing import.

## Current Dependency Routing (2026-07-11)

Historical decision records have zero premise weight. The unresolved content
used by this note is routed through the following current foundation or
zero-weight open obligation:

- [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
- [`AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md)
