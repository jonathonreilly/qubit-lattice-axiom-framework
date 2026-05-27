# Finite Record Isometry to Kraus Instrument Algebra

**Date:** 2026-05-20
**Type:** bounded_theorem
**Status:** source-side proposal — independent audit lane owns the verdict
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/persistent_record_kraus_instrument_certificate.py`](../scripts/persistent_record_kraus_instrument_certificate.py)

## Scope Repair (2026-05-27)

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The Kraus/CPTP algebra closes once a normalized linear isometry W is assumed, and the runner verifies that algebra on a finite sampled isometry. The restricted packet does not derive W from the retained persistent-record overlap-kernel pilo"*

with repair: *"missing_bridge_theorem: derive or cite a retained normalized linear record-writing isometry theorem for the persistent-record overlap-kernel lane; then re-audit the finite Kraus/CPTP algebra as a bounded bridge."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The finite-instrument algebraic certificate — that if a normalized linear isometry `W : H_sys → H_sys ⊗ H_record` is given, then extracting record blocks `K_r` yields (a) resolution of identity `Σ_r K_r†K_r = I`, (b) a CPTP unconditional update, and (c) normalized selective post-record states — all verified by the runner on a concrete `C^4 → C^4 ⊗ C^3` example.
- **NON-load-bearing (split off / admitted):** The derivation of a normalized linear record-writing isometry W from the retained `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE` overlap-kernel pilot lane; the packet assumes W as an external input and does not construct it from the overlap-kernel dynamics, so the Kraus bridge is conditional on a retained isometry theorem that is not yet supplied.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Claim

This repair narrows the binding claim to the self-contained bounded
linear-algebra theorem:

> Given a finite-dimensional system Hilbert space `H_sys`, a finite
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
dimension `d`, and let `H_record` have an orthonormal basis
`{|r>}_{r=1}^R`. Let

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
simulation of persistent-record dynamics.

## What This Claims

- Exact bounded finite-isometry-to-Kraus instrument algebra.
- A concrete finite matrix certificate in dimension `d = 4`, record count
  `R = 3`.
- The algebraic target that any future persistent-record bridge must
  supply if it wants a Kraus/CPTP measurement-update structure.

## What This Does Not Claim

- Does not derive the finite isometry `W` from the persistent-record
  overlap-kernel lane.
- Does not claim record labels are orthogonal or POVM-compatible in the
  physical persistent-record process.
- Does not repair or retag the Born-rule derivation.
- Does not depend on Kraus 1971, Choi 1975, or textbook quantum
  operations as load-bearing citations; the finite matrix algebra is
  proved and checked directly here.
- Does not consume `MINIMAL_AXIOMS` or any framework axiom row as a
  dependency.

## Audit Boundary

The 2026-05 audit verdict asked for a retained normalized linear
record-writing isometry theorem before using this row as a persistent
record bridge. This repair does not provide that bridge. It instead
narrows the row to the finite isometry algebra itself. Independent audit
should treat any downstream persistent-record or Born-rule use as a
separate bridge problem.
