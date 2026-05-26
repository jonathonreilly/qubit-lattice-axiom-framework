# Bekenstein-Hawking Entropy Bounded Lattice Companion

**Status**: bounded companion / finite-packet evidence only. The note records
finite-lattice free-fermion entanglement computations and their numerical
comparison to the `S_BH = A / (4 l_P^2)` coefficient. It does **not** derive
the Bekenstein-Hawking coefficient and does **not** retain an all-`L` or
OBC-lattice Widom asymptotic theorem.
**Claim type:** bounded_theorem
**Dependency:** [`BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md`](BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md),
which currently supplies retained-bounded finite-`L <= 64` evidence and the
exact 2D diamond Widom coefficient evaluation, while explicitly deferring the
all-`L` carrier-Widom bridge.

## 2026-05-26 finite-packet rescope

The previous version of this note overstated the boundary by saying that the
free-fermion carrier's asymptotic RT ratio is retained as `c_Widom = 1/6` and
by importing the extended `L <= 96` probe into the binding story. The current
audit ledger correctly blocks that stronger reading: the dependency retained
only a finite-`L <= 64` numerical-fit packet plus the exact 2D Widom integral,
not a full OBC-lattice all-`L` asymptotic theorem.

This rescope keeps only the source-side bounded packet:

- finite 2D/3D OBC tight-binding Hamiltonians built by
  `scripts/frontier_bh_entropy_derived.py`;
- finite half-space correlation-matrix entropies on the reviewed sizes;
- transfer-layer SVD rank readouts `chi_eff`;
- the finite-L RT comparison values reported by the runner;
- gravity-modulation and species-cancellation checks on the finite runner
  surface;
- the upstream finite-`L <= 64` Widom no-go packet as retained-bounded context,
  not as an all-`L` asymptotic theorem.

Excluded from this row's binding scope:

- a derivation of `S_BH = A / (4 l_P^2)`;
- a retained statement that `lim_L r(L) = 1/6` on the OBC carrier;
- any `L <= 96` cache/probe value;
- any claim that the finite-L values near `1/4` select the physical black-hole
  entropy coefficient.

## Result (bounded)

On the finite free-fermion half-filled nearest-neighbor tight-binding carrier,
the runner computes:

1. **Area-law-like finite fits.** Half-space entanglement entropy on the
   reviewed finite 2D and 3D lattices fits a boundary-size linear model with
   `R^2 > 0.998`. This is finite numerical behavior, not a continuum theorem.

2. **Transfer-layer rank scale.** The adjacent-layer correlator SVD gives a
   finite `chi_eff` readout used in the comparison denominator
   `S_max = |dA| * log(chi_eff)`.

3. **Finite-L RT ratios.** On the reviewed small 2D surface the mean ratio
   `S_ent / (|dA| * log(chi_eff))` is about `0.2364`; individual values for
   `L = 8, 10, 12, 16, 20, 24, 32` are approximately
   `0.241, 0.247, 0.245, 0.236, 0.236, 0.231, 0.220`. On the reviewed 3D
   sizes `L = 4, 6, 8, 10`, the mean is about `0.1222`.

4. **BH comparison boundary.** The finite 2D mean is numerically close to
   `1/4`, but that is only a bounded comparison number. It is not a retained
   derivation of the physical entropy coefficient.

5. **Species cancellation.** For independent species, both entropy and the
   log-bond denominator scale linearly in the species count, so the ratio is
   species-independent. The runner verifies spread below `1e-12`.

6. **Finite-size trend diagnostics.** The runner reports finite tail-fit
   diagnostics for the reviewed sizes. Those diagnostics are observations only;
   they do not prove an asymptote.

## What The Widom Dependency Supplies

The linked Widom note is retained-bounded for:

- direct evaluation of the 2D diamond Widom coefficient `c_Widom = 1/6`;
- finite-`L <= 64` numerical-fit evidence on the stated OBC free-fermion
  packet;
- the explicit statement that the all-`L` OBC carrier-Widom bridge and
  threshold-rank proof remain open.

Therefore this note may use the Widom row only as bounded context explaining
why the finite-L comparison is not a closed BH derivation. It may not import a
retained all-`L` no-go theorem.

## Checks

The repaired runner reports pass/fail only for finite claims it recomputes
directly:

| Check | Threshold | Status |
|-------|-----------|--------|
| Area law 2D | `R^2 > 0.998` | PASS |
| Area law 3D | `R^2 > 0.998` | PASS |
| Gravity modulation | monotone for `g >= 0.5` | PASS |
| Species universality | ratio spread `< 1e-12` | PASS |

Observations reported outside pass/fail:

| Observation | Scope |
|---|---|
| 2D finite-L RT ratio near `1/4` | finite comparison only |
| 3D finite-L RT ratio far from `1/4` | finite comparison only |
| Frozen-star scaling table | identity after manually setting RT ratio to `1/4` |
| Tail-fit intercepts | diagnostic only, no asymptotic theorem |

## Chain Summary

```text
finite OBC free-fermion Hamiltonian
  -> finite half-space correlation-matrix entropy
  -> finite transfer-layer SVD rank chi_eff
  -> finite-L comparison S_ent / (|dA| log chi_eff)
  -> bounded companion values, not S_BH derivation
```

The strongest honest status is finite-packet bounded support pending
independent audit.
