# Lüders Rule from Compositional Bayesian Consistency

**Date:** 2026-05-20 (parent-boundary repair 2026-06-07: align this
row with the narrower finite PEP bridge, which supplies compression
algebra but not measurement probability semantics; audit-target split
2026-06-08: separate the exact finite projective/instrument support from
the still-open measurement probability bridge).
**Type:** conditional-support assembly over exact finite subclaims
**Status:** source-side conditional proposal — independent audit lane owns
the verdict
**Actual current-surface status:** conditional-support. This parent row is
not a retained, unbounded, or framework-native Lüders/Born theorem. It is
an assembly note whose exact source-side support is limited to the finite
projective/instrument algebra listed in the 2026-06-08 split below; the
measurement probability semantics remain a separate open bridge.
**Supplies (proposed):** a conditional bounded replacement for one of
the admitted inputs in
`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — the
Lüders rule import for record-conditioning state updates — only after the
measurement-side trace/effect probability interpretation and the standard
(U1)–(U4) update-consistency requirements are accepted for the row. The
Born note is a downstream consumer, not an upstream authority for this
row. The current source packet includes a native finite-operator bridge
for the `P E P` compression and trace-cyclicity algebra used in Step 1:
[`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
with runner
[`scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py`](../scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py)
and cache
[`logs/runner-cache/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.txt`](../logs/runner-cache/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.txt).
It does not by itself supply the Born rule, trace/effect probability
interpretation, measurement instruments, or the physical meaning of a
record-conditioning update.

## Claim

Given the measurement-side trace/effect probability interpretation and the
standard update-consistency requirements below, on the qubit-lattice
operator algebra defined by
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) (A1+A2,
giving per-site `M_2(ℂ)` operator algebra and `Z^3` substrate), the
**unique** state-update rule for record conditioning that satisfies
the four standard consistency requirements

- **(U1)** Positivity preservation: `σ ≥ 0 ⇒ σ' ≥ 0`
- **(U2)** Normalization preservation: `Tr(σ) = 1 ⇒ Tr(σ') = 1`
- **(U3)** Probability consistency: for any subsequent measurement
  effect `E`, the joint probability decomposes as `p(P then E) =
  p(P) · p(E | P)` (Bayes rule on sequential measurements)
- **(U4)** Compositional consistency: recording `P_1` then `P_2` gives
  the same posterior state as recording `P_2 · P_1` once

is the **Lüders rule**: for a projection-valued record `P`,

> `σ → σ|_P = (P σ P) / Tr(P σ P)`

and more generally, for a Kraus operator `K`,

> `σ → σ|_K = (K σ K†) / Tr(K σ K†)`

The conditional-update domain is explicit: the projection formula is
claimed only when `Tr(P σ P) > 0`, and the Kraus formula only when
`Tr(K σ K†) > 0`. Zero-probability conditioning events are excluded
from this theorem.

If independently retained under those measurement-side premises, this
supplies a conditional replacement for the Lüders-rule input to the Born-rule
support / repair route under Gleason–Busch on the pre-record reference. It
does not retag or promote the Born row by itself.

## Setup

By A1+A2, the per-site operator algebra is `M_2(ℂ)` (equivalently
`Cl(3,0)` as a real algebra), composing over `Z^3` by standard
C*-tensor product. For a finite region `Λ ⊂ Z^3`, the local
operator algebra is `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` acting on
`H_Λ = ⊗_{x ∈ Λ} ℂ²`.

A **state** on `A_Λ` is represented by a density matrix `σ`
(`σ ≥ 0`, `Tr(σ) = 1`). The interpretation of `Tr(σE)` as a
measurement probability is a measurement-side premise of this row, not a
consequence of the finite PEP bridge. A **record** corresponds to a
measurement outcome — formally, a positive operator `P` (typically a
projection, more generally a Kraus operator) representing which outcome
was obtained once that measurement semantics is supplied.

The **state-update problem**: given a pre-record state `σ` and a
record outcome `P`, what is the post-record state `σ|_P`?

## Step 1 — Lüders rule from (U3) Bayes consistency

Apply (U3) Bayes rule to two sequential measurements. Let the first
measurement record outcome `P` (rank-1 projection for clarity;
generalizes to higher rank). Let the second measurement be POVM
`{E_i}` with `Σ_i E_i = I`. By Bayes:

```text
p(P then E_i)  =  p(P) · p(E_i | P)                                      (1)
```

Using the admitted measurement-side state/effect trace-probability
pairing on the operator algebra:

```text
p(P then E_i)  =  Tr(σ · M_{P, E_i})                                     (2)
```

for some effect `M_{P, E_i}` representing the joint "P then E_i"
outcome. The finite PEP bridge supplies the algebraic compression
fact used here: `M_{P, E_i}=P E_i P` is a valid finite-matrix effect,
has the required boundaries `M_{P,I}=P` and `M_{I,E_i}=E_i`, satisfies
the trace identity `Tr(σPEP)=Tr(PσPE)`, composes by nested compression,
and is separated from a boundary-satisfying Jordan alternative by the
runner's positivity/trace-scalar guards. The bridge does not derive the
physical probability interpretation of this effect.

So

```text
p(P then E_i)  =  Tr(σ · P E_i P)  =  Tr(P σ P · E_i)                    (3)
```

(using the cyclicity of trace). Substituting in (1):

```text
Tr(P σ P · E_i)  =  p(P) · p(E_i | P)  =  Tr(σ · P) · Tr(σ|_P · E_i)     (4)
```

For (4) to hold for **every** effect `E_i`, we must have

```text
Tr(σ|_P · E_i)  =  Tr( P σ P · E_i ) / Tr(σ · P)    ∀ E_i                (5)
```

Since `{E_i}` ranges over all POVM effects on `A_Λ` (the trace dual
of which is the full operator space), equality of these linear
functionals forces

```text
σ|_P  =  (P σ P) / Tr(P σ P)                                             (6)
```

This is the Lüders rule. Given the trace-probability premise and (U3)
Bayes consistency, combined with the bridged finite-operator compression
`M_{P,E}=PEP`, (6) is forced on the positive-probability conditioning
domain.

## Step 2 — (U1), (U2) are corollaries

The Lüders rule (6) automatically satisfies:

- **(U1) Positivity:** `σ ≥ 0 ⇒ P σ P ≥ 0` (sandwich preserves
  positivity), so `σ|_P ≥ 0` after normalization.
- **(U2) Normalization:** `Tr(σ|_P) = Tr(P σ P) / Tr(P σ P) = 1` by
  construction.

These are immediate from the form of (6); they are properties of the
Lüders rule, not independent constraints.

## Step 3 — (U4) compositional consistency

Apply Lüders twice for sequential records `P_1` then `P_2`:

```text
(σ|_{P_1})|_{P_2}  =  (P_2 (σ|_{P_1}) P_2) / Tr((σ|_{P_1}) · P_2)         (7)
```

Substituting (6):

```text
                    =  (P_2 (P_1 σ P_1) P_2 / Tr(P_1 σ P_1)) /
                       Tr((P_1 σ P_1) · P_2 / Tr(P_1 σ P_1))
                    =  (P_2 P_1 σ P_1 P_2) / Tr(P_2 P_1 σ P_1 P_2)
                    =  ((P_2 P_1) σ (P_2 P_1)†) / Tr((P_2 P_1) σ (P_2 P_1)†)
                                                                          (8)
```

This is exactly Lüders applied once to the composite operator
`P_2 · P_1`. Compositional consistency (U4) is therefore automatically
satisfied by the Lüders form derived from (U3).

## Step 4 — Uniqueness

Any state-update rule `σ → f(σ, P)` satisfying (U1)–(U4) must reproduce
(6) by the argument in Step 1, since (U3) alone forces (6) up to the
ambiguity in `M_{P, E}`. The bridge
[`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
discharges that ambiguity for the finite operator-algebra setting used
here at the algebraic level: it shows `P E P` is a valid effect,
proves the finite trace-compression identity, composes as
`(QP)†F(QP)`, and separates a boundary-satisfying Jordan alternative.
Therefore Lüders is the unique update rule satisfying (U1)–(U4) on the
standard finite operator-algebra structure of `M_2(C)`-based
qubit-lattice regions, within the stated positive-probability domain,
conditional on the measurement-side probability semantics stated above.

## What this can close after audit

- **A narrowed Lüders-import replacement candidate** in the Born derivation note
  (`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
  Step 3 admitted Lüders 1951 / Cassinelli-Lahti 1995 as the standard
  measurement-update rule). This note derives the conditional update
  formula from (U1)–(U4) and the admitted trace/effect probability
  interpretation, with the finite `M_{P,E}=PEP` compression algebra now
  supplied by the native bridge. Full closure of the Born row remains
  conditional on independent audit and any later dependency-chain update.

## What this does not close

- **General uniqueness of sequential products on arbitrary effect
  algebras.** The native bridge proves the finite operator-algebra
  facts used here and rules out a concrete boundary-satisfying Jordan
  alternative; it does not reprove the full Gudder-Greechie
  sequential-product uniqueness theory.
- **Measurement-side semantics for this row itself:** the Born/trace
  probability interpretation, the physical instrument/readout meaning of
  record conditioning, and the acceptance of (U1)–(U4) as the governing
  update constraints are not derived by the finite PEP bridge.
- **The remaining inputs of the broader Born derivation chain**:
  Gleason 1957, Busch 2003 POVM extension, no-extra-structure
  pre-record identification, and persistent-record → Kraus operator
  identification. Each is separate. This note addresses only the
  Lüders update row.

## Source dependencies and inputs

1. **Measurement-side premises for this parent row:** the trace/effect
   probability interpretation `p(E|σ)=Tr(σE)`, the meaning of sequential
   record conditioning, and (U1)–(U4) as the standard consistency
   requirements on
   measurement update rules — these are mainstream-textbook
   foundational conditions (Cassinelli-Lahti 1995, Busch et al. 1995
   *Operational QM*, Heinosaari-Ziman 2012).
2. **Finite operator-algebra bridge for `M_{P,E}=PEP` compression and
   trace-cyclicity algebra** —
   [`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
   with runner/cache linked above.
3. **Positive-probability conditioning domain** — `Tr(PσP)>0` for
   projection conditioning and `Tr(KσK†)>0` for Kraus conditioning.

## Risk classification

This is a conditional `bounded_theorem` candidate. Steps 1–4 are
textbook operator-algebraic derivations (Cassinelli-Lahti 1995 Ch.3
covers essentially the same content), but the current framework-native
input supplied by this packet is only the finite `PEP` compression and
trace identity. The trace probability interpretation and (U1)–(U4)
measurement-update requirements remain measurement-side premises for
this parent row.

## 2026-06-07 Parent-Boundary Repair

This repair aligns the parent row with the narrower PEP bridge. The bridge
is useful and runner-certified, but it is a finite matrix theorem: it proves
compression positivity, `0 <= PEP <= P`, trace cyclicity, and nested
compression. It explicitly does **not** derive the Lüders update, Born rule,
trace/effect probability interpretation, or a measurement instrument from
the framework axioms.

The parent row therefore remains a conditional Lüders-update theorem:
given trace/effect probability semantics, (U1)–(U4), and the finite PEP
compression bridge, the normalized compression formula follows. That is
valuable support for replacing a bare textbook Lüders import, but it does
not by itself retire every measurement-side premise in the Born chain.

Boundary guard:

```bash
python3 scripts/luders_parent_boundary_guard_2026_06_07.py
```

Expected:

```text
SUMMARY: PASS=12 FAIL=0
```

## 2026-06-08 Audit-Target Split

The current source packet should be audited as a split target, not as a
single framework-native Lüders theorem.

**Exact finite support already present in source:**

1. The finite `PEP` compression theorem:
   [`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
   proves `0 <= PEP <= P`, trace cyclicity, nested compression, and the
   relevant boundary cases in finite matrix algebra. It does not assign
   physical probability meaning to the trace scalar.
2. The canonical projective Kraus selection:
   [`LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md`](LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md)
   proves `K_r = P_r` for the canonical finite projective readout frame,
   and proves why general apparatus label-mixing is outside that scope.
3. The finite pointer-record write bridge:
   [`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`](RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md)
   proves that supplied stable pointer projectors plus a supplied ideal
   pointer-label write give a normalized isometry `W`, projective Kraus
   blocks `K_r=P_r`, a CPTP pointer-dephasing channel, and repeat-readable
   selective branches inside that finite pointer model.
4. The typed record-instrument kernel interface
   `RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md`
   proves that, once a finite instrument and trace/effect pairing are
   supplied, `mu_r = Tr(K_r rho K_r^dag)` is a normalized kernel over
   possible record atoms and that realized post-record atoms remain distinct
   from predictive probabilities. (That note is a **later companion**
   (2026-06-05); this Lüders-rule derivation (2026-05-20) predates it and does
   not load-bear on it — rendered as a plain (non-link) reference to avoid a
   spurious audit-graph cycle, the genuine direction being companion → this note.)

**Residual open bridge for this parent:**

The missing theorem is not another `PEP` algebra check. It is the physical
measurement-semantics bridge from the approved `{Lattice, Quantum, Record}`
surface to:

```text
pre-record density state + physical instrument/readout context
  -> trace/effect probability law
  -> sequential record probabilities
  -> selective conditioning update as a physical record update.
```

The 2026-06-05 Record axiom explicitly supplies durable realized-outcome
registration and finite scalar additivity only after a readout context is
given; it supplies no probability, normalization, measurement/decoherence
dynamics, or instrument generation. Therefore the parent row remains
conditional-support unless a separate retained measurement-side bridge is
accepted. The exact subclaims above can be independently useful audit targets
and can retire bare textbook *algebra* imports, but they do not by themselves
retire the Born/measurement probability premise.

Audit split guard:

```bash
python3 scripts/luders_measurement_semantics_audit_split_guard_2026_06_08.py
```

Expected:

```text
SUMMARY: PASS=23 FAIL=0
```

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra and `Z^3` substrate)
- [`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) — finite operator-algebra bridge for `M_{P,E}=PEP`, valid-effect bounds, trace-cyclicity algebra, nested compression, and the Jordan-product guard
- [`LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md`](LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md) — canonical finite projective Kraus selection `K_r=P_r` under restricted readout-frame scope
- [`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md`](RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md) — finite pointer-record write to projective Kraus isometry bridge under supplied pointer-model premises
- `RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md` (later companion, plain reference — see note above) — typed finite kernel interface under supplied instrument and trace/effect pairing

**Runner/cache evidence** (load-bearing for the native bridge):

- [`scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py`](../scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py)
- [`logs/runner-cache/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.txt`](../logs/runner-cache/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.txt)
- [`scripts/luders_parent_boundary_guard_2026_06_07.py`](../scripts/luders_parent_boundary_guard_2026_06_07.py)
- [`logs/runner-cache/luders_parent_boundary_guard_2026_06_07.txt`](../logs/runner-cache/luders_parent_boundary_guard_2026_06_07.txt)
- [`scripts/luders_measurement_semantics_audit_split_guard_2026_06_08.py`](../scripts/luders_measurement_semantics_audit_split_guard_2026_06_08.py)
- [`logs/runner-cache/luders_measurement_semantics_audit_split_guard_2026_06_08.txt`](../logs/runner-cache/luders_measurement_semantics_audit_split_guard_2026_06_08.txt)

**Parallel standard-math comparators** (not the only source route):

- Cassinelli-Lahti 1995 *Found. Phys.* 25, 1395 — Lüders rule from (U1)–(U4)
- Busch-Lahti-Mittelstaedt 1995 *Operational Quantum Physics* — effect-algebra consistency conditions
- Heinosaari-Ziman 2012 *The Mathematical Language of Quantum Theory* — modern textbook treatment of measurement update
- Standard operator-algebraic sequential-effect composition `M_{P, E} = P E P`

**Plain-text pointer references** (NOT load-bearing deps; deliberately not markdown links to avoid polluting the audit dependency graph):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer that may cite this row after independent audit / dependency-chain update
- `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` — relevant for the persistent-record → Kraus operator identification (separate admitted input handled in the companion `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`)
- Marlow / Wright "minimal disturbance" rule literature — alternative measurement-update rules; not adopted here

## What this file is not

- Not a derivation of Gleason–Busch from A1+A2.
- Not a derivation of the Born/trace probability interpretation, physical
  measurement instruments, or record-conditioning semantics from A1+A2.
- Not a general uniqueness theorem for all sequential products on all
  effect algebras; the finite operator-algebra `PEP` bridge used here
  is supplied separately and linked above.
- Not a numerical-prediction change.
- Not a unilateral retagging of the Born note. The bounded-theorem
  candidacy depends on independent audit acceptance of the (U1)–(U4)
  framing and the linked sequential-effect/trace bridge.
