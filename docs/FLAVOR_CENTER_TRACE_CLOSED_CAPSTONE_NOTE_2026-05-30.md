# Flavor - center-trace route reduced-status source packet

> **Packaging / supersession (2026-06-07 repair):** the old closed-capstone
> framing is superseded. This repaired note is a reduced-status source packet:
> it preserves the exact center/full-trace algebra and supplies graph-visible
> authorities, but it does **not** restore the historical "decisive closure" of
> the center-trace route. It is not a ledger retag; independent audit owns any
> future effective-status change.

The old closed-capstone framing is superseded. The pre-record identification
remains retained_bounded; equivalently, pre-record identification remains retained_bounded
on this repair surface.

**Date:** 2026-05-30; repaired 2026-06-07
**Claim type:** bounded_theorem / exact-support repair packet
**Claim boundary:** superseded historical capstone narrowed to exact support for
the algebraic center/full-trace comparison and its dependency surface. The old
center-trace route-closure claim is historical provenance only.
**No new axioms:** no axiom is introduced or restated as a premise.
**Runner:** `scripts/flavor_center_trace_closed_2026_05_30.py`
**Runner output:** `outputs/flavor_center_trace_reduced_status_source_packet_2026_05_30.json`
and `logs/runner-cache/flavor_center_trace_closed_2026_05_30.txt`.

## Repaired status

The earlier note asked whether decoherence / superselection forces the charged
lepton mass functional to read the **center** trace of `R[Z3] = R + C` (equal
central atoms, giving the block-count route) rather than the **full-algebra**
trace (dimension weighting). The exact algebraic answer remains:

```text
{P_X1, P_X2, P_X3} + C3 cycle generate M3(C).
The only coordinate subsets invariant under both D3 and C3 are empty/full.
Tracial I/3 gives singlet/doublet populations (1/3, 2/3).
Singlet/doublet dephasing preserves those populations.
```

That is exact support for the dimension-weighted default on this finite
generation carrier. It is **not** by itself a proof that the physical/gauge
observable algebra has been identified, and it is not a proof that the
center-trace derivation route is closed on the current authority surface.

## Source authorities checked by the runner

| Role | Authority | Current ledger status used here | Boundary |
|---|---|---:|---|
| No proper quotient | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | `retained` | Exact `D3 + C3` algebra-generation/no-proper-quotient theorem; physical-species interpretation remains out of scope. |
| Trace uniqueness source | `powers_uhf_tracial_uniqueness_on_qubit_lattice_narrow_theorem_note_2026-05-20` | `retained` | Unique tracial state on the type-`2^infty` qubit-lattice quasi-local algebra; Powers is provenance, not an admitted import. |
| Pre-record trace-identification boundary | `pre_record_reference_state_tracial_derivation_note_2026-05-20` | `retained_bounded` | Finite-region tracial mathematics is checked, but the pre-record physical identification remains retained_bounded and outside this repair. |

The key repair is dependency honesty. The no-proper-quotient theorem and the
UHF trace theorem can be cited as retained source authorities. The pre-record
identification remains retained_bounded, so this row cannot honestly claim an
unbounded retained tracial-reference closure.

## Exact algebra retained in this packet

Let `P_X1, P_X2, P_X3` be the three translation-character projectors and let
`C3` cyclically permute the three coordinates. The diagonal projector algebra
`D3` plus the cycle generates all matrix units and hence `M3(C)`. Equivalently,
a subspace preserving both the coordinate-projector separation and the C3 cycle
must correspond to a subset of `{X1, X2, X3}` that is closed under the 3-cycle;
only the empty and full subsets qualify.

On the tracial finite carrier `rho = I3/3`, the singlet projector
`P_s = (1/3) 1 1^T` and doublet projector `P_d = I - P_s` have populations:

```text
Tr(P_s rho) = 1/3
Tr(P_d rho) = 2/3
```

The dephasing map `rho -> P_s rho P_s + P_d rho P_d` removes coherence between
the singlet and doublet blocks but does not change those populations. Thus the
dimension-weighted readout is stable under this dephasing operation.

Equal central-atom weighting would instead assign `(1/2, 1/2)` to the two
central idempotents. This packet records that choice as an extra selector, not
as a consequence of the tracial algebra above.

## What this packet can and cannot unlock

This packet can support re-audit of the historical row after narrowing:

```text
retained no-proper-quotient source
+ retained UHF tracial uniqueness source
+ explicit retained_bounded boundary on pre-record identification
+ exact finite center/full-trace algebra
=> reduced-status exact-support packet
```

It cannot support the old statement that the center-trace route is closed by a
retained theorem. To recover that stronger statement, a separate bridge would
still have to derive the physical observable-algebra identification and close
the pre-record trace-identification edge without adding a new axiom or importing
the desired weight as a selector.

## Runner contract

Run:

```bash
PYTHONPATH=scripts python3 scripts/flavor_center_trace_closed_2026_05_30.py
```

The runner checks live ledger statuses for the three source authorities, verifies
the exact `D3 + C3` algebra and tracial population computations, writes the JSON
certificate, and prints a `SCORECARD PASS=... FAIL=0` line when the repaired
packet is internally consistent.
