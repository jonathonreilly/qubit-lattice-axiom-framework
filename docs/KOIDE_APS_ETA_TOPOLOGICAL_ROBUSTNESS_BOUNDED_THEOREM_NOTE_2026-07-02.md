# Local `Z_3` Normal-Plane Density `2/9` — Partial Narrowing

**Date:** 2026-07-02; narrowed 2026-07-31
**Type:** bounded_theorem
**Audit authority:** independent audit lane only.
**Primary runner:**
[`scripts/frontier_koide_aps_topological_robustness.py`](../scripts/frontier_koide_aps_topological_robustness.py),
with cache
[`logs/runner-cache/frontier_koide_aps_topological_robustness.txt`](../logs/runner-cache/frontier_koide_aps_topological_robustness.txt).

The historical filename is kept to preserve the stable claim identifier. This
revision narrows the scientific content to the finite local statement that the
runner actually proves. It does not set or predict an audit outcome.

## Bounded claim

Let `R` be the real two-dimensional rotation through `2π/3`, acting on one
normal plane. Let `ζ = exp(2πi/3)`, and define the finite inverse-normal-
determinant average

```text
L(a,b) = (1/3) Σ_{k=1,2} 1 / [(ζ^(ka) - 1)(ζ^(kb) - 1)].
```

For the conjugate characters `(a,b)=(1,2)` of this one real rotation plane,

```text
det_R(I - R) = (1 - ζ)(1 - ζ²) = 3,
L(1,2) = (1/3)(1/3 + 1/3) = 2/9.
```

Moreover, every symmetric bilinear form `G` on this one real plane satisfying
`Rᵀ G R = G` is a scalar multiple of the identity. Thus the runner proves a
one-dimensional invariant-metric commutant for this local two-real-dimensional
representation. It does not prove that all equivariant metrics on a
four-dimensional tangent representation or on a global manifold are scalar.

## Executable checks

The runner reports 41 finite algebra and representation checks:

- five exact evaluations of the defined average and its dependence on
  characters modulo three;
- eleven checks of the `2×2` real normal-plane commutant and integer lifts;
- five determinant checks;
- four independently evaluated character-weighted averages;
- six elementary integer-shift checks;
- six coprimality and odd-order parity checks, labeled only as arithmetic;
- two cross-formula checks; and
- two representation-sensitivity checks.

The character-weighted values `(2/9,-1/9,-1/9)` are computed from the finite
sum in the runner rather than installed as theorem premises. The integer-shift,
coprimality, and parity checks are elementary arithmetic only; they are not
tests of an APS variation theorem, a spin-lift theorem, or PL smoothability.

## One-hop local support

[`KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md`](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md)
contains the longer block-by-block calculation and explicitly keeps global
PL/ABSS applicability outside its direct claim. The present note consumes it
only as local finite-algebra support. Its complete text is transported to the
independent audit packet so that this boundary is visible rather than clipped.

## Open obligations and exclusions

This note and runner do not establish any of the following:

- an operator-specific equivariant APS or eta localization formula;
- a four-real-dimensional isolated-fixed-point tangent theorem;
- reconciliation of isolated fixed points with fixed axes or timelike
  fixed submanifolds;
- a global `PL S³ × R` compactification or a PL-to-smooth APS bridge;
- existence or uniqueness of an equivariant spin lift;
- metric independence of a global operator invariant;
- selection of a physical tangent class; or
- the R-eta/Brannen-phase carrier, unit, or readout map.

Those obligations require separate direct authorities with a specified
operator, fixed-set geometry, normalization, and boundary convention. The
current physical readout target remains the open derivation obligation at
`docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`. Historical
admission decisions have provenance value only and no premise weight here.

In particular, a pair of complex tangent weights at an isolated point would
describe a real four-dimensional tangent representation. Its invariant metric
commutant is not the `2×2` commutant computed here. No global “no metric dial”
conclusion is drawn from the local normal-plane calculation.

## Verification

```bash
python3 scripts/frontier_koide_aps_topological_robustness.py
```

Expected: `Summary: PASS=41, FAIL=0`.

## Restricted-packet transport record (2026-07-31)

The packet builder preserves the complete identity-verified cached stdout for
the primary runner and the complete one-hop block-by-block support note. The
scoped regression is
`docs/audit/scripts/tests/test_koide_aps_eta_packet_repair.py`.

This is evidence transport, not audit ratification. Full evidence may confirm,
demote, or reject a claim; the independent audit lane decides. No audit
verdict, effective status, or generated audit output is authored here.
