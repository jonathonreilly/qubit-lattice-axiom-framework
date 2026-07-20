---
claim_id: microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Unaudited bounded Lieb-Robinson estimate for a supplied finite-volume tensor or even-CAR Hamiltonian whose arbitrary finite interaction supports have a common positive site-weighted exponential activity kappa; family-uniform use requires common kappa, mu, observable norms, and finite support data. The estimate is mathematical support only: it selects no dynamics, physical propagation speed, framework fermion carrier, or retained-grade result."
upstream_dependencies:
  - minimal_axioms
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09
  - exp_decay_lieb_robinson_quasilocal_bridge_theorem_note_2026-06-11
  - free_bilinear_quasilocal_lr_bridge_theorem_note_2026-06-10
runner: scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py
---

# Microcausality: a weighted quasilocal-class walk bound

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit authority:** the independent audit lane only; this note assigns no
audit verdict.
**Primitive status:** no primitive is approved, registered, or enlarged here.

Primary runner:
[`scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py).
Its cache is
[`logs/runner-cache/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.txt).

## Supplied setting

Let `Λ` be a finite subset of `Z^3`, equipped with the ambient `l1` graph
metric.  For every nonempty finite `S ⊆ Λ`, let `h_S` be Hermitian and write

> `H = Σ_S h_S`,
> `diam(S) = max_{x,y∈S} d(x,y)`.

Terms with the same support are summed before their norm is taken.  The
interaction family, the finite region, and a number `μ > 0` are supplied.  The
load-bearing activity assumption is

> `0 < κ := sup_x Σ_{S∋x} ||h_S|| |S| exp(μ diam(S)) < ∞`.          (1)

No connectedness assumption is imposed on `S`.  For a family of growing
regions, “volume uniform” below means that one common finite `κ` is supplied;
it is not inferred separately in each volume.

The tensor version permits arbitrary finite on-site dimensions.  The CAR
version assumes that every interaction term is even.  Observables `A` and `B`
have finite disjoint supports `X` and `Y`, with `d := d(X,Y) ≥ 1`.  In the CAR
version the ordinary commutator estimate retains `||[A,B]||`; that zeroth term
need not vanish for odd--odd observables.  It vanishes for tensor-local
observables and in the even CAR sector.

The finite-matrix Heisenberg convention is `τ_t(A)=exp(iHt)Aexp(-iHt)`.  The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
memo does not choose `H`, `μ`, `κ`, `A`, or `B`.

## Incidence-chain estimate

Put

> `w(S) := ||h_S|| exp(μ diam(S))`,
> `w*(S) := |S| w(S)`,
> `n_X^w := Σ_{S∩X≠∅} w*(S) ≤ |X|κ`.                              (2)

For a chain `(S_1,...,S_k)` satisfying
`S_1∩X≠∅`, `S_{j+1}∩S_j≠∅`, and `S_k∩Y≠∅`, choose an overlap point at every
step.  The triangle inequality and the definition of ambient diameter give

> `Σ_j diam(S_j) ≥ d`.                                             (3)

This remains true for disconnected supports.  Consequently

> `Π_j ||h_{S_j}|| ≤ exp(-μd) Π_j w(S_j)`.                         (4)

For fixed `S`, the union bound over its contact sites gives

> `Σ_{S': S'∩S≠∅} w*(S')`
> `≤ Σ_{x∈S} Σ_{S'∋x} w*(S') ≤ |S|κ`.                             (5)

Peel a chain from the final support back toward `X`.  At each step the
`|S_j|` supplied by (5) combines with `w(S_j)` to reconstruct `w*(S_j)`.
Thus

> `Σ_chains Π_j w(S_j) ≤ n_X^w κ^(k-1)`,                          (6)

where dropping the final requirement `S_k∩Y≠∅` only enlarges the sum.  The
runner checks (3), the `|S|` reconstruction, the exponent `k-1`, and exact
finite-family instances independently.

## Bounded theorem

The finite-volume Duhamel recursion contributes the order-`k` majorant
`2^(k+1)||A||||B||` times the plain interaction-chain sum and
`|t|^k/k!`.  Combining (4) and (6), then summing from `k=1`, yields

> `||[τ_t(A),B]||`
> `≤ ||[A,B]||`
> `  + 2||A||||B|| (n_X^w/κ) exp(-μd) (exp(2κ|t|)-1)`              (7)
> `≤ ||[A,B]||`
> `  + 2||A||||B|| |X| exp(-μd) (exp(2κ|t|)-1)`.

This holds for all real `t` in every supplied finite region.  Its constants
depend on the family only through the declared inputs.  The slope `2κ/μ`
obtained by rewriting the exponential as `exp[-μ(d-(2κ/μ)|t|)]` is only a
mathematical Lieb--Robinson cone slope for this supplied majorant.  It is not a
selected, measured, pole, group, wavefront, or framework propagation speed and
is not claimed sharp.

## Exact consistency checks

For nearest-neighbour bonds with `||h_b||≤J`, at most six bonds meet a site and
`|b|=2`, so

> `κ ≤ 12 J exp(μ)`.                                               (8)

The bound is attained by a saturated bulk star.  At that envelope (7) has
rate `24J exp(μ)`, while the linked direct finite-range bound has rate
`20J exp(μ)`: the envelope ratio is `6/5`.  This is a deliberately weaker
class-level comparison, not an improvement.  The incidence union bound counts
`12`, the distinct bonds meeting a fixed bond number `11`, and removing the
bond itself leaves `10`.

For pair supports with
`||h_{x,y}||=J_0 λ^{d(x,y)}` and `ρ:=λ exp(μ)<1`, the `l1` sphere count
`N_3(r)=4r^2+2` gives

> `κ_3D = 4J_0 ρ(3+ρ^2)/(1-ρ)^3`,
> `κ_1D = 4J_0 ρ/(1-ρ)`.                                         (9)

In particular, `κ_3D/J_0` is `14` at `ρ=1/3` and `684` at `ρ=3/4`, while
`κ_1D/J_0=4` at `ρ=1/2`.  The runner reconstructs the sphere sums and rejects
the missing-`|S|` half-values.

## Relationship to the linked bounded notes

The five science dependencies in the front matter are unaudited bounded
parents or comparators, not correctness oracles for this runner:

- the
  [`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
  supplies the finite-volume Duhamel convention;
- the
  [`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
  supplies the parity/locality convention;
- the
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  is the narrower interaction comparator;
- the
  [`EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md`](EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md)
  records that a pure exponential has no uniform reproducing-convolution
  constant;
- the
  [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
  is a pair-interaction comparator, with this note's `κ=2W_μ` because of the
  explicit `|S|=2` factor.

The reproducing-convolution obstruction does not prove or disprove (7): the
derivation above extracts `exp(-μd)` on each chain before applying one-center
incidence row sums, so it never assumes a finite two-point reproducing ratio.
That is a method distinction, not a new no-go verdict.

## Boundaries

- This note does not derive or select the supplied Hamiltonian or activity.
- It does not identify a gauged kernel, transfer/log generator, or
  `U`-integrated measure.
- It does not establish an infinite-volume dynamics; it supplies constants
  uniform over a family only when the stated inputs are uniform.
- It does not claim sharp constants or a physical propagation speed.
- It does not alter the narrower finite-range results.
- It does not assign an audit result or retained-grade status.

## Verification

The runner is source-contained: it reads no Markdown or other mutable science
input.  Its descriptive gate manifest covers ambient-diameter reach,
site-weighted activity, the peeling power, Duhamel resummation, wrong-sign and
wrong-factor rejectors, bond incidence, the closed-form pair activities, and
explicit tensor/CAR matrices.  It prints one `PASS` or `FAIL` line per gate and
a final total.  The committed cache is generated from that runner alone.
