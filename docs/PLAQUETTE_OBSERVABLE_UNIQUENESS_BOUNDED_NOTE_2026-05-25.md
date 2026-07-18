# Plaquette Observable Uniqueness Bounded Note

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/plaquette_observable_uniqueness_runner.py`](../scripts/plaquette_observable_uniqueness_runner.py)

## Claim

Given the existing retained graph-first SU(3) Wilson-plaquette evaluation
surface at `beta = 2 N_c / g_bare^2 = 6` and the finite compact Haar
measure of the cited partition function, the average plaquette is uniquely
determined by the partition-function derivative. With the Wilson action
convention used here,

```text
S_W[U] = (beta / N_c) * sum_p Re Tr[1 - U_p],
```

the relation is the affine identity

```text
<P> = 1 + (1 / N_plaq) * d ln Z / d beta.
```

The proof-walk uses
only:

- finiteness of the Haar product on compact SU(3) over a finite periodic
  L^4 lattice;
- well-definition of `d ln Z / d beta` as differentiation of an
  absolutely convergent integral.

This note isolates the structural-uniqueness half of
[`plaquette_self_consistency_note`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md).
The numeric-value half of the parent (`<P>(beta = 6) ~= 0.5934`) is not
claimed here and remains conditional per the parent's audit verdict.

This is a bounded proof-walk of an existing observable definition. It
does not add a new axiom, a new repo-wide theory class, or a retained
status claim.

## Proof-Walk

| Step | Load-bearing input | Numeric-value input? |
|---|---|---|
| Haar product finiteness on compact SU(3), finite periodic L^4 | retained gauge-source temporal completion authority | no |
| `Z(beta) = integral DU exp(-S_W[U])` finite, well-defined | finite compact Haar product, bounded Wilson action | no |
| Dominated-convergence differentiation `d ln Z / d beta` | bounded integrand `-S_W[U]/N_plaq` on a compact domain | no |
| Affine identity `<P> = 1 + (1/N_plaq) d ln Z / d beta` under the stated Wilson-action sign convention | algebraic differentiation of `exp(-S_W)` | no |
| Observable is single-valued real | sum of the above | no |

The checked proof path does not cite the numeric value `0.5934`, the
analytic `beta = 6` insertion candidate, the tensor-transfer Perron
solve, or any Monte Carlo readout.

## Exact Arithmetic Check

For the finite periodic Wilson surface with `N_plaq` plaquettes and
action

```text
S_W[U] = (beta / N_c) * sum_p Re Tr[1 - U_p],
```

differentiation under the absolutely convergent compact-Haar integral gives

```text
d ln Z / d beta = - <d S_W / d beta>
               = - (1/N_c) * sum_p < Re Tr[1 - U_p] >
               = - (N_plaq / N_c) * (N_c - <Re Tr U_p>),
```

so the standard normalized plaquette `<P> = (1/N_c) <Re Tr U_p>` reduces
to

```text
<P> = 1 + (1 / N_plaq) * d ln Z / d beta.
```

Equivalently, the unique-observable relation

```text
<P>(beta) = 1 + (1 / N_plaq) * d ln Z(beta) / d beta
```

holds at every finite `beta > 0` where `Z(beta)` is absolutely
convergent. At `N_c = 3` and `beta = 6` the right-hand side is a single
real number determined by `Z`. The runner repeats this differentiation
symbolically on a finite-dimensional compact toy Haar measure and
confirms the affine derivative relation is single-valued and real.

## Dependencies

- [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the parent same-surface uniqueness/numeric-value claim that this
  note narrows to the structural half.
- [`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md`](GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md)
  for the retained gauge-source temporal completion authority on the
  accepted 3 spatial + 1 derived-time surface.
- [`GAUGE_VACUUM_PLAQUETTE_SPECTRAL_MEASURE_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_SPECTRAL_MEASURE_THEOREM_NOTE.md)
  for the retained finite-volume Wilson source-surface theorem that the
  average plaquette pushforward of Haar measure is a compact positive
  measure whose Laplace transform generates the finite connected
  plaquette hierarchy.
- [`GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md)
  for the finite-volume source theorem that, for `L >= 2`, the
  one-plaquette inverse defines a unique analytic, strictly increasing
  coordinate `beta_eff,L(beta)`. The resulting plaquette equality is true by
  definition and is not used here as a physical reduction law.
These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This note does not close:

- the numeric value `<P>(beta = 6) ~= 0.5934`;
- the analytic `beta = 6` insertion candidate `P(6) = 0.593530679977098`;
- the tensor-transfer Perron solve at `beta = 6`;
- any Monte Carlo evaluation;
- the parent `plaquette_self_consistency_note` audit verdict;
- any downstream row that requires the numeric value rather than the
  structural-uniqueness premise alone.

Downstream rows that need only the structural-uniqueness premise of
`<P>` as a uniquely defined observable of `Z(beta = 6)` through the
affine derivative relation may cite this note. Downstream rows that need
the numeric value continue to cite the parent.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/plaquette_observable_uniqueness_runner.py
```

Expected:

```text
TOTAL: PASS=... FAIL=0
VERDICT: bounded proof-walk passes; <P> is an affine derivative observable
of the cited finite compact-Haar partition function, with no numeric-value
claim.
```
