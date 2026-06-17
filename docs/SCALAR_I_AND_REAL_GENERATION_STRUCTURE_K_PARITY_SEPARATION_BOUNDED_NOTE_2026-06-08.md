# Scalar-i and Real J_cs Structure Have Different K-Parity

> **Key terms used in this doc** follow the non-load-bearing glossary index
> `docs/KEY_TERMINOLOGY.md`; the theorem below does not cite that index as a
> mathematical or audit dependency.

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_scalar_i_real_generation_k_parity_separation.py`](../scripts/frontier_scalar_i_real_generation_k_parity_separation.py)
**Cached log:**
[`logs/runner-cache/frontier_scalar_i_real_generation_k_parity_separation.txt`](../logs/runner-cache/frontier_scalar_i_real_generation_k_parity_separation.txt)

## Statement

In a supplied readout context with a supplied entrywise conjugation
`K(X) = conj(X)`, the scalar-`i` sector and the real generation complex
structure `J_cs` have different `K`-parity.

The central scalar `i I_2`, the `K`-odd Pauli generator `sigma_y`, the
`Cl(3,0)` volume product `sigma_x sigma_y sigma_z = i I_2`, the shared tensor
central `i`, and the phase of a Hermitian `C_3` circulant are all reversed by
the supplied conjugation. By contrast, the real generation complex structure
`J_cs = (C - C^2) / sqrt(3)` is fixed by the same conjugation while satisfying
`J_cs^2 = -(I - P_triv)`.

The labeled generation Vandermonde orientation sign from the cited orientation
note is not part of that K-even `J_cs` sector. Under the induced
`delta -> -delta` map it flips sign:
`Delta(+delta) = +0.04674385`, `Delta(-delta) = -0.04674385` in the runner's
sample. The sorted-spectrum discriminant is K-even only after erasing labels,
so it is retained as a multiset control, not as the generation-orientation
object.

Therefore scalar-`i` phase data and the real `J_cs` complex-structure data are
separate `K`-parity sectors. The finite calculation no longer claims the
labeled Vandermonde orientation sign is K-even; it aligns with the
orientation/chirality residual named by the cited generation-orientation note.

## What this establishes

- The `Cl(3,0)` one-site volume product equals the central scalar `i I_2`.
- The same central scalar `i` is shared under the tensor placement
  `(i I_2) tensor I_2 = I_2 tensor (i I_2) = i I_4`.
- Under a supplied entrywise conjugation, the scalar-`i` cluster is `K`-odd.
- A Hermitian `C_3` circulant phase is conjugated by `delta -> -delta` while
  its spectrum is unchanged as an unordered real multiset.
- The real generation complex structure `J_cs` is `K`-even and squares to
  `-(I - P_triv)` on the doublet.
- The labeled generation Vandermonde orientation sign is real but K-odd under
  the induced `delta -> -delta` map.
- The sorted-spectrum discriminant is K-even only as an unordered-multiset
  control, not as the cited orientation object.

## What this does not establish

- It does not derive `r`, a charged-lepton phase value, `theta_gauge`, or any
  empirical number.
- It does not provide a selector, weighting rule, probability rule,
  normalization rule, readout bridge, source/action, or dynamics.
- It does not assert that Record supplies the readout context, the central
  decomposition, or the `K`/CPT conjugation. Those are supplied inputs for this
  bounded calculation.
- It does not add an axiom, primitive, Tier-A admission, or retained status.
- It does not prove that either `K`-parity sector is realized by nature.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the
  one-qubit operator algebra / `Cl(3,0)` one-site carrier and the Record
  boundary: Record does not supply `K`/CPT, a decomposition, readout context,
  weighting, probability, or dynamics.
- [`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md)
  for the Hermitian `C_3` circulant algebra context.
- [`KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md`](KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md)
  for the generation Vandermonde / orientation-sign context.

## Forbidden-imports check

No PDG value, fitted selector, literature comparator, measured parameter, or
Planck-scale input is consumed. The runner uses only finite matrix identities
and a supplied entrywise conjugation.

## Validation

Run:

```bash
python3 scripts/frontier_scalar_i_real_generation_k_parity_separation.py
```

Expected: `TOTAL: PASS=9 FAIL=0`.
