# Finite Record Isometry to Kraus Instrument Algebra

**Date:** 2026-05-20
**Type:** bounded_theorem
**Primary runner:** [`scripts/persistent_record_kraus_instrument_certificate.py`](../scripts/persistent_record_kraus_instrument_certificate.py)

## Scope Repair (2026-05-27)

## Premise-Wiring Correction (2026-07-13)

The unanimous `5/5` judicial-panel handoff was: “The algebraic implication is
exact and the runner genuinely corroborates it, but the packet explicitly
identifies normalized W as an external premise and assumes record-basis
orthogonality. Under the rubric's explicit-premise and normalization rule,
those inputs are not closed by the restricted packet.” This correction leaves
the finite algebra unchanged and repairs that premise bookkeeping. It wires
normalized `W` to two bounded controlled-copy authorities, with their
conditions preserved, and names record-basis orthogonality as the declared
reading `(R_perp)` below rather than attributing an inner-product theorem to
the Record axiom. Outside the two named controlled-copy surfaces, normalized
`W` remains conditional; outside a model that derives orthogonal labels,
`(R_perp)` remains conditional.

## Source Boundary

The finite Kraus/CPTP algebra closes once a normalized linear isometry `W` and
an orthonormal record-label representation are supplied. This note does not
derive either input from the persistent-record overlap-kernel lane. This
revision takes the **split path**:

- **Load-bearing (in scope):** The finite-instrument algebraic certificate — that if a normalized linear isometry `W : H_sys → H_sys ⊗ H_record` is given, then extracting record blocks `K_r` yields (a) resolution of identity `Σ_r K_r†K_r = I`, (b) a CPTP unconditional update, and (c) normalized selective post-record states — all verified by the runner on a concrete `C^4 → C^4 ⊗ C^3` example.
- **Source-wired bounded instantiations (in scope only at their stated
  surfaces):** The W1a controlled-copy classification supplies a normalized
  write under its declared readings and blank-input trace preservation; the
  2026-06-18 controlled-copy theorem supplies one in its explicit finite
  controlled-copy/fresh-fragment model.
- **NON-load-bearing (split off):** Any derivation of a normalized linear
  record-writing isometry `W`, or of pairwise record-state orthogonality, from
  the `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE` overlap-kernel pilot lane. The
  present runner does not construct either input from overlap-kernel dynamics.

No new axiom is introduced. The runner-verified core remains the load-bearing
algebra; the dependencies below supply bounded source instantiations without
turning them into an arbitrary persistent-record-to-isometry bridge.

## Load-Bearing Dependencies and Premise Wiring

| Premise face | Authority | Consumed content and exact boundary |
|---|---|---|
| Normalized `W`: admissible one-step write class | [`RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md`](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md) | **Conditional on that note's four declared finite-surface readings (C1–C4) and blank-input trace preservation**, its minimal `C^2 tensor C^2` blank-input restriction has `A_a = c_a V`, with the stated common Kraus normalization `sum_a |c_a|^2 = 1`, orthonormal conditional record vectors, and `V^dagger V = I_S`. The operator readings remain declared there: its runner proves their implication and does not prove that the English Record clauses require them. No grain-wide write class or arbitrary persistent dynamics is consumed here. |
| Normalized `W`: explicit controlled-copy source | [`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md) | In its explicit finite pointer-record model only, the `theta = pi/4` controlled-copy kick on a fresh blank fragment supplies orthogonal vectors `|eta_0>`, `|eta_1>` and, after fixed record-register calibration, the projective record-write isometry `W|psi> = P_0|psi> tensor |0> + P_1|psi> tensor |1>`. This consumes its exact model-specific isometry result, not an arbitrary persistent-dynamics-to-`W` theorem and not a derivation of its record reading from the minimal axioms. |
| Record-basis orthogonality / semantic Record surface | [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Verbatim: “When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.” Verbatim: “Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.” Verbatim: “A state is a configuration of records.” These clauses supply the record-content/configuration and disjoint-additivity surface; they do **not** define `H_record`, an inner product, or pairwise orthogonality of record states. |

The Record clauses therefore do not prove `<r|s> = delta_rs`: “pairwise
disjoint” is a relation among records in a finite collection, not a supplied
Hilbert-space inner-product relation. Record-basis orthogonality is a declared
reading of the Record surface. For the generic finite theorem in this note,
the required physical-to-Hilbert identification is the following named
conditional, deliberately mirroring W1a's declared readings:

> **Record-basis orthogonality reading `(R_perp)`.** On the finite record
> surface being represented, distinct record configurations used as record
> labels are read as distinct classical data and are represented by mutually
> orthogonal vectors `{|r>}` in `H_record`, so `<r|s> = delta_rs`.

The phrase “distinct record configurations are distinct classical data” is a
declared reading here, not a verbatim Minimal-Axioms theorem. W1a discharges
`(R_perp)` on its narrow surface only through its declared C1 orthogonal-support
reading; its C4 additivity reading expressly imposes no additional
Hilbert-space relation among the blank and written vectors. The 2026-06-18
controlled-copy theorem instead derives
`<eta_0|eta_1> = 0` inside its explicit finite model. Thus either bounded
controlled-copy authority supplies both normalization and orthogonal labels on
its own stated surface; neither promotes `(R_perp)` to a consequence of the
bare Record axiom.

## Claim

This repair narrows the binding claim to the self-contained bounded
linear-algebra theorem:

> Given a finite-dimensional system Hilbert space `H_sys`, a finite record
> surface represented under the declared reading `(R_perp)` by the
> orthonormal record basis `{|r>}`, and a normalized isometry
> `W : H_sys -> H_sys ⊗ H_record` decomposed as
> `W = sum_r K_r ⊗ |r>`, the extracted blocks `{K_r}` form a Kraus
> instrument: `sum_r K_r† K_r = I`, the unconditional map
> `rho -> sum_r K_r rho K_r†` is CPTP, and nonzero selective branches
> normalize to positive density matrices.

Explicitly out of scope:

- deriving `W` from persistent-record dynamics;
- deriving record labels or record orthogonality from the overlap kernel;
- repairing the downstream Born-rule row;
- asserting asymptotic record-formation closure.

The result is still useful: it gives the exact algebra any future
persistent-record-to-isometry bridge must satisfy.

## Theorem

Let `H_sys` be a finite-dimensional complex Hilbert space with
dimension `d`, and represent the finite record labels under `(R_perp)` by
`H_record` with orthonormal basis `{|r>}_{r=1}^R`. Let

```text
W : H_sys -> H_sys ⊗ H_record
```

be a linear isometry, `W† W = I_sys`, with block decomposition

```text
W |psi> = sum_r (K_r |psi>) ⊗ |r>.
```

Then:

1. **Kraus resolution.**
   ```text
   sum_r K_r† K_r = I_sys.
   ```

2. **Unconditional CPTP map.** The map
   ```text
   E(rho) = sum_r K_r rho K_r†
   ```
   is completely positive and trace preserving.

3. **Selective updates.** For any density matrix `rho` and any record
   branch with
   ```text
   p_r = Tr(K_r rho K_r†) > 0,
   ```
   the selective state
   ```text
   rho_r = K_r rho K_r† / p_r
   ```
   is normalized and positive.

## Proof

Expand the isometry in the record basis:

```text
W = sum_r K_r ⊗ |r>.
```

Because the record basis is orthonormal,

```text
W† W = sum_{r,s} (K_r† K_s) <r|s>
     = sum_r K_r† K_r.
```

The isometry condition `W† W = I_sys` therefore gives the Kraus
resolution.

Complete positivity of `E` follows directly from the Kraus form: each
term `rho -> K_r rho K_r†` is completely positive and finite sums of
completely positive maps are completely positive. Trace preservation
follows from cyclicity of trace and the resolution of identity:

```text
Tr(E(rho)) = sum_r Tr(K_r rho K_r†)
           = sum_r Tr(K_r† K_r rho)
           = Tr(rho).
```

For a selective branch with `p_r > 0`, positivity of `K_r rho K_r†`
follows from positivity of `rho`, and division by `p_r` gives trace one.

## Runner Certificate

The runner constructs a seeded finite isometry
`W : C^4 -> C^4 ⊗ C^3`, extracts three blocks `{K_r}`, and verifies:

- `W† W = I`;
- `sum_r K_r† K_r = I`;
- the Choi matrix of `rho -> sum_r K_r rho K_r†` is positive;
- sampled arbitrary density matrices remain trace-one and positive under
  the unconditional channel;
- every nonzero selective branch is trace-one and positive.

This is a matrix-algebra certificate for the theorem above. It is not a
simulation of persistent-record dynamics. It does not validate the declared
reading `(R_perp)` or re-check the two source authorities' bounded write
theorems; those inputs are traced in the dependency table rather than
re-derived by this runner.

## What This Claims

- Exact bounded finite-isometry-to-Kraus instrument algebra.
- A concrete finite matrix certificate in dimension `d = 4`, record count
  `R = 3`.
- Bounded source wiring: the W1a class and the 2026-06-18 explicit model meet
  the normalization and orthogonal-label premises only on their respective
  stated surfaces.
- The algebraic target that any future persistent-record bridge must
  supply if it wants a Kraus/CPTP measurement-update structure.

## What This Does Not Claim

- Does not derive the finite isometry `W` from the persistent-record
  overlap-kernel lane.
- Does not claim record labels are orthogonal or POVM-compatible in the
  physical persistent-record process, and does not claim that the bare Record
  axiom entails `(R_perp)`.
- Does not repair or reclassify the Born-rule derivation.
- Does not depend on Kraus 1971, Choi 1975, or textbook quantum
  operations as load-bearing citations; the finite matrix algebra is
  proved and checked directly here.
- Consumes the quoted `MINIMAL_AXIOMS` Record clauses only as the semantic
  surface for the explicitly declared `(R_perp)` reading; it imports no
  Hilbert-space orthogonality theorem from that memo.

## Downstream Boundary

Any downstream persistent-record or Born-rule use outside the two named
controlled-copy surfaces still needs a separate derivation of the normalized
linear record-writing isometry and either a derivation or an explicit declared
reading of record-label orthogonality. This note supplies the finite isometry
algebra once those premises are present; it does not widen the source
authorities beyond their bounded claims.
