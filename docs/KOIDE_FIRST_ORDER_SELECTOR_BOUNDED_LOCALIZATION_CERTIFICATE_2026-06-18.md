# Koide First-Order Selector Bounded Localization Certificate

**Date:** 2026-06-18
**Claim type:** bounded_theorem / no-go demarcation
**Status:** source-side bounded-localization certificate; independent audit required.
**Status authority:** independent audit lane. This source certificate does not
set, predict, promote, or demote any audit outcome and does not edit
audit-owned registry, ledger, queue, or publication-status surfaces.
**Primary runner:** `scripts/koide_first_order_selector_bounded_localization_certificate_2026_06_18.py`
**Runner cache:** `logs/runner-cache/koide_first_order_selector_bounded_localization_certificate_2026_06_18.txt`

## Purpose

This certificate repairs the audit boundary for
`KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md`.
It does not supply the physical `AC_phi_lambda -> M(b) tensor sigma_+`
action bridge and does not derive the physical Koide `r=1/2` selector.

Instead, it isolates the exact finite theorem surface that can be re-audited
without that bridge.

## The Bounded Theorem Surface

Let `C` be the three-cycle on the native generation factor `R^3`, and let

```text
Gamma_chi = (2/3)(I + C + C^2) - I.
```

The bounded surface is exactly:

1. The circulant Koide quotient `Q = sum(lambda_k^2)/(sum lambda_k)^2`
   equals `(1+2r)/3` and is independent of the phase of `b`.
2. The `C3` clock grading has multiplicities `(1,1,1)`, so the formal
   `(singlet,doublet)=(1,1)` block-balance algebra is available while
   respecting `C^3=I`.
3. Within the native circulant generation algebra `span{I,C,C^2}`,
   the only operator that anticommutes with `Gamma_chi` is zero.
4. A separate tensor factor can carry a nonzero anticommuting shape:
   `I_3 tensor sigma_x` commutes with `C tensor I_2` and anticommutes with
   `I_3 tensor sigma_z`.
5. The native circulant mass has `b`-independent Fourier eigenvectors, so it
   remains the Berry-flat/commuting side of the finite comparison.

These five statements are the load-bearing payload. They are finite algebraic
claims checked by the runner.

## What Remains Open

This certificate leaves open:

- the physical `AC_phi_lambda -> M(b) tensor sigma_+` action term;
- the physical first-order/readout weighting rule;
- the derivation of `r=1/2` as a framework-selected charged-lepton branch.

The phrase "L-R coupling gate" is therefore a localization of the remaining
science target, not a claim that the framework already supplies that gate.

## Re-Audit Boundary

The row should be consumed only as bounded algebraic localization and
route-pruning:

```text
native R^3 / C3 / U(1)_b routes do not supply the physical first-order selector;
the explicit escape isolated here requires a separate chiral L-R coupling plus readout.
```

It should not be consumed as a retained physical selector theorem, a retained
Koide `r=1/2` derivation, or a retained `AC_phi_lambda` action/readout bridge.

## No-Go Discipline Gate

**Status: PASS.** The negative boundary is narrow: the tested native
`R^3`/`C3`/`U(1)_b` routes do not supply the physical first-order selector.
The certificate does not claim a global impossibility theorem.

**N1 alternative routes.**

| route | attempt | disposition |
| --- | --- | --- |
| continuous `U(1)_b` | Select `r=1/2` through the phase of `b`. | ATTEMPTED: `Q=(1+2r)/3` is delta-independent on the current finite surface. |
| discrete `C3` clock index | Use `(1,1)` block balance as the physical selector. | ATTEMPTED: the algebra is available, but no physical readout weighting is supplied. |
| native circulant anticommuting operator | Find a nonzero selector inside `span{I,C,C^2}`. | ATTEMPTED: `comm(C) cap anticomm(Gamma_chi)={0}`, matching `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`. |
| static grading or complex structure | Let chirality grading alone supply the first-order branch. | ATTEMPTED: the grading is context only; it does not supply the coupling action term. |
| separate chiral factor | Carry the anticommuting shape on `R^3 tensor C^2`. | ATTEMPTED: the algebraic shape exists, but physical `AC_phi_lambda -> M(b) tensor sigma_+` and readout remain open. |

**N2 wall independence.** The remaining open gates are the physical
chiral-coupling/action bridge and the physical first-order/readout weighting.
Closing either one does not automatically close the other, so they are kept
separate.

**N3 hidden-wall scan.** "Native" means the finite circulant generation
surface checked here. "Physical" marks the open target, not a proof input.
"Supplies" and "framework" appear only in non-claim firewalls. No hidden
admission is used to convert the algebraic escape into a physical selector.

**N4 residual matching.** The cited `KOIDE_Z3...` no-go residual is exactly
the native `R^3` anticommuting-selector residual. The Berry-flat note is used
only for the commuting/native-mass side. The staggered-Dirac gate is cited as
the still-open action bridge, not as closure.

**N5 rhetoric audit.** The certificate avoids global route exhaustion. The
tested resolution is only the finite native generation family plus the
explicit separate-factor escape witness.

**N6 partial-closure path scan.** No new axiom or primitive is demanded.
Future closure may come from a retained chiral-coupling theorem, a retained
readout theorem, or an explicit supplied import later retired by audit.
Approved primitives are not treated as bounded walls.

**N7 steelman.** A future first-order `AC_phi_lambda -> M(b) tensor sigma_+`
bridge could make the anti-Hermitian/CPT-fused count physical and then support
the `r=1/2` selector. That would not contradict this certificate, because it
would add exactly the coupling/readout source this bounded surface leaves
open.

**N8 cross-cycle echo.** Prior Koide selector packets overreached when they
treated available algebra as a retained physical selector. This certificate
keeps the route-pruning value while preserving the open physical bridge and
readout gates.

## Dependencies

- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/koide_first_order_selector_bounded_localization_certificate_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=55 FAIL=0
VERDICT: bounded localization certificate passes; physical L-R coupling/readout remains open.
```
