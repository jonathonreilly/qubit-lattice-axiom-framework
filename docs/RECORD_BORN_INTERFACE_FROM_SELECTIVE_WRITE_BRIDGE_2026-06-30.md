# Record/Born Interface From Selective Write Bridge

**Date:** 2026-06-30
**Claim type:** positive theorem candidate / bounded bridge theorem.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, or claim record occurrence is derived.
**Primary runner:**
[`scripts/record_born_interface_from_selective_write_bridge_2026_06_30.py`](../scripts/record_born_interface_from_selective_write_bridge_2026_06_30.py)

## Claim

The post-axiom record/probability blocker should split into two pieces:

```text
record-writing interface + effect additivity
  -> Born-form weights and repeatable selective record readout

branch occurrence / production law
  -> still open
```

This bridge closes the first piece as a finite theorem. It does not close the
second.

Given a supplied finite readout context with projectors `{P_r}` and a supplied
record-writing isometry

```text
W |psi> = sum_r P_r |psi> tensor |r>,
```

the extracted record blocks are exactly

```text
K_r = <r| W = P_r.
```

If record probabilities are represented by a normalized effect-additive
functional on the qubit effect algebra, the Busch/CFMR effect-Gleason theorem
forces

```text
p(r) = m(P_r) = Tr(rho P_r).
```

The corresponding selective unnormalized state is

```text
rho_r = P_r rho P_r,
```

and repeated readout of the same record is stable:

```text
P_r rho_r P_r = rho_r,
p(r again | r) = 1.
```

Thus the Born rule is not an extra probability language to put into the axioms.
It is the unique effect-additive probability representation once a selective
record-writing instrument/effect interface is supplied.

What remains open is not the algebraic Born form. The remaining wall is:

```text
W_occurrence = a physical branch-occurrence / production law selecting which
               possible record becomes the realized durable record in a run.
```

## Why This Helps

The current record-production notes correctly say that post-record histories and
counts do not derive probabilities. This bridge agrees. Counts are consumers of
realized records.

The new movement is that the pre-record probability side does not need a broad
"probability axiom" either. It needs a supplied or derived instrument/effect
interface. Once that interface has normalized effect additivity, the qubit
algebra forces Born trace weights. Once it has the selective write isometry, the
record update is the projection-compression/Lüders form and repeated readout is
stable.

So the full measurement gap narrows to the physical production question:

```text
which branch, if any, is written as the actual record?
```

## Finite Theorem

For a two-outcome record context on one qubit, let

```text
P_0 = |0><0|,    P_1 = |1><1|,    P_0 + P_1 = I.
```

Define

```text
W |psi> = P_0 |psi> tensor |0>_R + P_1 |psi> tensor |1>_R.
```

Then:

1. `W* W = I`, so `W` is an isometry.
2. The record blocks extracted from the record register are `K_0 = P_0` and
   `K_1 = P_1`.
3. The induced nonselective channel is trace-preserving:

   ```text
   rho -> P_0 rho P_0 + P_1 rho P_1.
   ```

4. The selective branch `r` has unnormalized state `P_r rho P_r`.
5. The trace scalar of branch `r` is `Tr(rho P_r)`.
6. After conditioning on a nonzero branch, repeat readout returns the same
   label with probability one.

For general finite POVMs on `M_2(C)`, the existing Busch/CFMR authority bridge
proves the representation theorem: normalized effect additivity forces
`m(E)=Tr(rho E)`. The projective record context is the sharp special case.

## Relation To Existing Blockers

| Prior blocker | Effect of this bridge |
|---|---|
| record histories do not derive Born frequencies | unchanged and respected |
| kernel-only models do not produce records | unchanged and respected |
| supplied instrument/effects needed for probabilities | this bridge shows what they force once supplied |
| Lüders/update semantics not from axioms | narrowed to finite projection-compression once the selective write interface is supplied |
| branch occurrence / realized outcome | still open as `W_occurrence` |

## What This Does Not Claim

- It does not derive record occurrence from the axioms.
- It does not derive the physical Hamiltonian, coupling, clock, rate, reset
  cost, or state-preparation law.
- It does not say finite record counts imply probabilities or convergence.
- It does not derive IID trials. If an IID reset/preparation model is supplied,
  ordinary binomial frequency statements can be used, but that is a model input.
- It does not claim all measurement contexts are projective; the projective
  case is the sharp-record case, and the effect-Gleason result covers the
  effect-additive POVM probability representation.
- It does not consume measured values, PDG values, lattice-MC values, beta=6
  values, or a new primitive.

## Audit Consequence If Retained

The record/probability blocker should be restated from

```text
derive probability/Born weights and measurement semantics
```

to the narrower two-part surface:

```text
1. supplied or derived selective record-writing instrument/effect interface
   -> Born trace weights and repeatable selective readout;
2. physical branch occurrence / production law
   -> still open.
```

This does not finish measurement theory. It removes the algebraic Born-form and
Lüders-repeatability ambiguity from the blocker once the instrument interface is
available.

## No-Go Discipline Gate

**Status:** PASS for the bounded boundary. This is a positive bridge candidate
with one named residual if rejected or if the supplied instrument interface is
not accepted. It is not a no-go against record production.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Post-record counts -> Born | Derive pre-record probabilities from realized histories alone. | RULED OUT BY PRIOR: finite counts are post-record data and do not force `p`. |
| Effect-additive instrument route | Use normalized effect additivity on `M_2(C)` to force trace weights. | ATTEMPTED here using the Busch/CFMR bridge: succeeds for the probability form. |
| Selective write-isometry route | Extract Kraus blocks from `W = sum P_r tensor |r>`. | ATTEMPTED here: blocks are projectors and readout is repeatable. |
| Controlled-copy finite model route | Derive `W` inside an explicit finite pointer model. | PARTIAL BY PRIOR: succeeds only under bounded controlled-copy/fresh-fragment hypotheses. |
| Unconditional formation from axioms | Force records from Lattice/Qubit/Record alone. | RULED OUT BY PRIOR: no-record witnesses remain baseline-consistent. |
| IID frequency route | Turn Born weights into long-run frequencies. | OPEN: requires reset/preparation/independence assumptions. |

### N2 - Wall Independence Audit

Collapsed residual after this note:

```text
W_occurrence = physical branch occurrence / production law.
```

Effect-additive probability representation does not select which branch occurs.
Selective projection-compression does not select which branch occurs. Post-record
counts do not select which branch occurs. IID convergence does not select a
branch in an individual run. These are separate from `W_occurrence`.

### N3 - Hidden-Wall Scan

"Supplied instrument" means an explicitly supplied or separately derived
record-writing interface; this note does not get it from the axioms. "Born
weights" means trace weights forced by normalized effect additivity, not
observed frequencies. "Repeatable readout" means the algebraic stability of a
selected branch, not the physical production of that branch.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `RECORD_PRODUCTION_RESIDUAL_CHECKLIST...` | kernel/instrument is not produced record | `W_occurrence` remains | yes |
| `RECORD_BORN_FREQUENCY_BOUNDARY...` | counts do not derive Born probabilities | this bridge derives Born only from effect additivity | yes |
| `BUSCH_POVM_EFFECT_GLEASON...` | effect-additive qubit probabilities force trace form | probability-form supplier | yes |
| `LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP...` | `PEP` is finite algebra, not measurement semantics alone | selective-readout algebra supplier | yes |
| `RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY...` | finite controlled-copy model supplies `W` only under hypotheses | instrument supplier in bounded models | yes |
| `RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED...` | baseline does not force records | preserves `W_occurrence` | yes |

### N5 - Rhetoric Audit

The claim is not "Born is derived from Record" and not "records always form."
The tested resolution is a supplied finite record-writing instrument/effect
interface. The theorem does not apply to bare record histories without that
interface, and it does not apply to finite frequencies without a supplied
preparation/reset model.

### N6 - Partial-Closure Path Scan

This is a bridge theorem path, not a new axiom. The import-retirement shape is:

```text
supplied or derived record-writing instrument
  + normalized effect additivity
  -> Born trace weights
  + selective projection-compression
  -> repeatable record readout
  -> audit review
  -> record/Born blocker narrowed to W_occurrence
```

No primitive is expanded. If future work derives `W_occurrence`, this bridge is
the measurement-interface layer it can feed.

### N7 - Steelman

A hostile reviewer can object that normalized effect additivity is already a
probability premise, so this bridge has not derived probability from the bare
ontology. That objection is correct. The bridge does not claim bare-ontology
probability. It claims that once the measurement interface supplies
effect-additive weights over available record effects, the qubit algebra forces
the Born trace form and the selective write interface forces repeatable
Lüders-style readout. The remaining frontier is the occurrence/production law.

### N8 - Cross-Cycle Echo

Prior record cycles overclaimed by moving from counts, kernels, or nonselective
density states directly to produced records. This bridge keeps those layers
separate: weights live at the pre-record instrument/effect layer, histories live
after realization, and actual branch occurrence remains an explicit residual.

## Verification

Run:

```bash
python3 scripts/record_born_interface_from_selective_write_bridge_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=80 FAIL=0
```
