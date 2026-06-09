# Scalar-i and Real Generation Structure Have Different K-Parity

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

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
`K(X) = conj(X)`, the scalar-`i` sector and the real generation-orientation
sector have different `K`-parity.

The central scalar `i I_2`, the `K`-odd Pauli generator `sigma_y`, the
`Cl(3,0)` volume product `sigma_x sigma_y sigma_z = i I_2`, the shared tensor
central `i`, and the phase of a Hermitian `C_3` circulant are all reversed by
the supplied conjugation. By contrast, the real generation complex structure
`J_cs = (C - C^2) / sqrt(3)` is fixed by the same conjugation while satisfying
`J_cs^2 = -(I - P_triv)`, and the Vandermonde orientation sign is real and
therefore fixed.

Therefore scalar-`i` phase data and real generation-orientation data are
separate `K`-parity sectors. The finite calculation blocks only the strong
identification that one scalar-`i` phase object is also the real
generation-orientation lever.

## What this establishes

- The `Cl(3,0)` one-site volume product equals the central scalar `i I_2`.
- The same central scalar `i` is shared under the tensor placement
  `(i I_2) tensor I_2 = I_2 tensor (i I_2) = i I_4`.
- Under a supplied entrywise conjugation, the scalar-`i` cluster is `K`-odd.
- A Hermitian `C_3` circulant phase is conjugated by `delta -> -delta` while
  its spectrum is unchanged as an unordered real multiset.
- The real generation complex structure `J_cs` is `K`-even and squares to
  `-(I - P_triv)` on the doublet.
- The Vandermonde orientation sign is a real `Z_2` datum and is `K`-even.

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

Expected: `TOTAL: PASS=8 FAIL=0`.
