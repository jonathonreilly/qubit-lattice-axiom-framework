# A self-consistent source with a box-independent extent exists, and the operator family separates on the binding energy rather than on any decay exponent — on the parent note's own lattice and four-member family, and under a stated isolation condition

**Date:** 2026-07-27
**Status:** bounded support; proposed for independent audit, not an audit verdict
**Claim type:** `bounded_theorem`
**Parent row:** `self_consistency_forces_poisson_note`
**Primary runner:** [`scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py`](../scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py)
**Cached runner output:** [`logs/runner-cache/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.txt`](../logs/runner-cache/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.txt)
**Gates:** [`CYCLE713_VALUE_NO_GO_AND_CLUSTER_CAP_GATES_2026-07-27.md`](CYCLE713_VALUE_NO_GO_AND_CLUSTER_CAP_GATES_2026-07-27.md)

Independent audit is still required before the repo may treat anything here as
retained-grade.

---

## Why this cycle exists

`docs/SELF_CONSISTENCY_FORCES_POISSON_NOTE.md` states its own claim as
"unscreened Poisson is the best-supported member of the audited operator family
and the only one in that sweep that stays near the Newtonian target", reached by
requiring that the field be sourced by the density of the propagator evolving in
that same field. Its ledger row asks, verbatim, to "normalize
alternative-operator source signs consistently", and records that "a
response-kernel bridge is still missing".

Three prior cycles worked that row. PR #5656 showed both of the note's operator
discriminators are empty — the matched point-to-point kernel gives `corr = -0.06`
where the note reports `0.93`, and after consistent sign normalization all four
operators are attractive and monotone. PR #5662 showed the note's `beta`
diagnostic has no far field to extrapolate: the fit window lies inside the
source and the enclosed fraction *rises* with the box. PR #5693 repaired the
protocol for a **prescribed** source and found the note's own diagnostic
inverted, then closed with a named successor:

> any future self-consistency claim in this lane needs a source term that is not
> the normalized propagator density.

This note takes that successor. The question it asks is not whether Poisson
wins, but whether the self-consistent problem the parent note is *about* has any
solution to which a far-field test applies at all.

## Construction

The source is the density of the lowest eigenstate of the field that density
itself sources:

```text
H = -t A + V,      A psi_0 = eps_0 psi_0  (lowest),      rho = abs(psi_0)^2
Op phi = s g rho,  V = phi <= 0
```

`A` is the Dirichlet nearest-neighbour graph Laplacian on the `N^3` interior,
taken from the parent runner itself; `Op` ranges over the parent note's own
family `{poisson, biharmonic, screened, local}`. The sign `s` is fixed once per
operator, from the sign of `sum(phi)` on the first iterate, so that **every**
operator produces an attractive well. The parent runner instead used one fixed
negative source for operators of opposite definiteness, which is exactly the
convention-dependence the ledger row names.

This source is not a propagated, per-layer-normalized amplitude. Its extent is
set by the balance between kinetic spreading and its own self-attraction, so it
is free to be box-independent — which is what makes the question answerable.

## The criterion, and why the second half is the load-bearing one

At fixed coupling with the box growing, call a source **self-bound** when

1. the RMS extent of `rho` converges to a finite limit, **and**
2. the depth of the self-consistent well converges to a finite limit.

Condition 2 is where the content is. A state whose extent stops growing can
still be held by a well that deepens without bound as the box grows — that is
box-squeezing by an operator whose kernel has no decaying far field, not
self-binding.

This is not a hypothetical concern. `docs/FROZEN_STARS_RIGOROUS_NOTE.md` tests
condition 1 only, and rows F1/F2 below run that note's own runner at its own
parameters and measure what it does in 3D.

## Claim ledger

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| **thesis** | On the parent note's own lattice and its own four-member operator family, with the source sign normalized so no operator is handed a repulsive well, a self-consistent source whose extent is set by the coupling rather than by the box exists; and the family separates on whether the self-consistent binding energy has a box-independent limit, not on any fitted decay exponent | R0, R3-R14 | [supplied] the Dirichlet graph Laplacian and operator family of the parent runner; [supplied] hopping `t = 1` and screening `mu^2 = 0.25`; [supplied] the isolation condition, that an isolated object's binding energy must have a limit independent of the box; [satisfied] the source sign is normalized per operator (R0); [satisfied] every scored fixed point converged (R3-R5, R8-R14) | Shown: a two-way separation over four named operators on finite lattices up to `N = 52` (`N = 96` for the kernel-only rows). Not shown: that no other local operator passes, that the limits exist as proved limits rather than as fits, or that the separation survives a multi-particle source | Exhibit an operator outside `{poisson, screened}` whose self-consistent well depth has a box-independent limit on this construction, or show that Poisson's does not |
| R0 | All four operators are handed an attractive well; none is scored unphysical for a sign convention | runner R0 | [satisfied] the per-operator sign `s` is fixed from the first iterate | Shown: `max(V) <= 0` throughout the interior for all four. Not shown: that this is the only admissible sign rule | Find an operator for which the rule yields `max(V) > 0` |
| F1 | The 3D width in `FROZEN_STARS_RIGOROUS_NOTE` grows monotonically over `L = 6..16` and fits `a + b*L` with `b = 0.311` per unit `L`; it does not saturate | runner F1, executing `scripts/frontier_frozen_stars_rigorous.py` | [supplied] that note's own parameters `G = 0.5`, `n_particles = 8` | Shown: `2.5214 -> 5.6336`, monotone at every step, linear rss `9.43e-03` against bounded rss `4.10e-01`. Not shown: behaviour at `L > 16`, or that the note's 1D result is wrong | Run `L = 20, 24` and exhibit saturation |
| F2 | At those parameters the gravitating state is the box ground state | runner F2 | [satisfied] the `G = 0` control is the same code path with the coupling zeroed | Shown: the gravitating width is 0.866-0.945 of the free box ground state across `L = 6..16`, and the note's stability test `width < 1.5 -> COLLAPSED` is passed by any delocalized state. Not shown: that no coupling in that construction self-binds | Find a coupling at which the ratio departs from 1 and the width saturates |
| R3 | Poisson's extent converges: the relative change per box step falls by more than two orders of magnitude and ends below `1e-3` | runner R3 | [supplied] `t = 1`; [satisfied] convergence at every box | Shown: at `g = 20`, `3.0595 -> 5.7063` over `N = 12..52`; at `g = 50`, `1.9051 -> 1.9376` over `N = 12..48`. Not shown: a proved limit | Extend to `N = 64` and find the extent moving again |
| R4 | Poisson's well depth also has a finite limit | runner R4 | [supplied] `t = 1`; [satisfied] convergence at every box | Shown: the bounded family beats the linear family at both couplings — `g = 20` limit `0.2957` (rss `3.84e-03` vs `8.28e-03`), `g = 50` limit `2.7945` (rss `5.21e-04` vs `2.31e-02`). Not shown: a proved limit | Show the linear family fits better at larger `N` |
| R5 | Biharmonic satisfies condition 1 but not condition 2 | runner R5 | [supplied] `g = 10`, chosen because every box converges there while `g = 100` does not; [satisfied] convergence at every scored box | Shown: extent flat at `2.6725-2.9127` while the depth runs `0.7874 -> 3.7835` and fits `a + b*M` with `b = 0.1507` per interior site (linear rss `1.61e-03` vs bounded rss `6.72e-01`). Not shown: behaviour at couplings where the iteration does not converge | Exhibit a coupling at which the converged biharmonic depth saturates |
| R6 | The split is a property of the kernels, not of the nonlinear fixed point | runner R6 | [satisfied] self-consistency removed entirely; a prescribed unit Gaussian of fixed extent | Shown: with no iteration at all, biharmonic's peak potential runs `0.1079 -> 0.4691` and is fit by the linear family, while poisson (`0.0460 -> 0.0547`), screened (`0.0311 -> 0.0313`) and local (`0.0436 -> 0.0436`) are fit by the bounded family. Not shown: other source profiles | Use a source profile for which biharmonic's peak potential saturates |
| R7 | The biharmonic growth is not an artifact of the Dirichlet wall | runner R7 | [satisfied] boundary-free torus, zero mode removed | Shown: biharmonic `0.1123 -> 0.9544` out to `N = 96`, linear with `b = 0.0105` per unit `N`; poisson `0.0448 -> 0.0564`, bounded with limit `0.0587`. Not shown: other boundary conditions | Find a boundary condition under which biharmonic's peak potential saturates |
| R8 | `local` has no single self-consistent branch to compare | runner R8 | [satisfied] identical `V = 0` start at every box | Shown: at `g = 100` the converged extent jumps `0.0245 -> 7.5743` as the box grows. Not shown: which branch is preferred, or whether a different start selects consistently | Exhibit a start rule under which `local` gives one branch at every box |
| R9 | Screened Poisson satisfies both conditions, so the self-binding gate does not by itself single out unscreened Poisson | runner R9 | [supplied] `mu^2 = 0.25`, the parent runner's own value | Shown: extent constant at `0.1633` (spread `1.1e-05`), depth `20.6868 -> 20.7065` with limit `20.7219`. Not shown: behaviour at other screening masses | Find a screening mass at which the depth diverges |
| R10 | Outside the source, the self-consistent Poisson field is the matched point-source kernel of the same operator to about 1 part in `10^4` — the response-kernel bridge the ledger row records as missing | runner R10 | [satisfied] same operator, same boundary condition, same window on both sides, so no correction is applied and no exponent is fitted; [satisfied] odd interior width, so the state's centroid falls exactly on a lattice site and the comparison point source sits where the mass is | Shown: median ratio `1.00013 -> 1.00006` across `N = 25..49`, tightening monotonically with the box rather than drifting. Not shown: that the agreement is exact, or that it holds at radii inside the source | Exhibit a box at which the median ratio leaves `1e-3` of unity |
| R11 | The residual in the even-width boxes is the placement of the comparison point source, not physics | runner R11 | [satisfied] identical construction at adjacent box sizes, differing only in the parity of the interior width | Shown: moving the centroid from half a spacing off in each axis (offset `0.8660`) to exactly on a site (offset `0`) shrinks the mean absolute deviation by a factor of `203` at `N = 24` vs `25` and `212` at `N = 32` vs `33`, moving the median ratio `1.01389 -> 1.00013` and `1.01228 -> 1.00008` and the scatter `1.29e-01 -> 1.03e-03`. Not shown: a multipole decomposition of what remains | Show a comparable residual at odd width, or no improvement across the parity pair |
| R12 | The matched-kernel comparison tests source localization, which every converged fixed point here satisfies; it is not the operator discriminator | runner R12 | [satisfied] the same comparison run for biharmonic and screened | Reported, not scored. Shown: the other two operators with an extended field also give ratios near unity | — |
| R13 | The extended self-bound branch ends in a collapse to below one lattice spacing | runner R13 | [supplied] fixed box `N = 28` | Shown: the extent shrinks smoothly with the coupling, then drops by more than a factor of three between two adjacent couplings to below one spacing; every box-independence row above is taken on the extended branch. Not shown: the order or universality of that collapse | Show the extent is smooth across the coupling where the jump is measured |
| R14 | What fails for biharmonic is the binding energy, not the local field difference | runner R14 | [satisfied] the same boxes, referenced to a fixed radius instead of to the well bottom | Shown: biharmonic's potential difference across the fixed window runs `1.15613 -> 1.45532` and is fit by the bounded family, while its well depth over the same three boxes runs `2.5637 -> 5.0018` and is not (poisson's difference is `0.44796 -> 0.44803`, screened's `0.18568 -> 0.18543`). Not shown: that the isolation condition is the right one to impose — it is a stated choice | Argue that a box-dependent binding energy is admissible for an isolated object; the separation then does not hold |

## What this does and does not do to the parent row

It supplies the response-kernel bridge the row records as missing (R10), and it
supplies the consistent source-sign normalization the row asks for (R0). It
replaces a discriminator the row calls convention-dependent with one that has no
sign convention in it.

It does **not** retire the row. The row's headline is that self-consistency
*forces* Poisson; what is shown is a separation over the parent's own
four-member family, which is not an exhaustiveness result over local operators.
And the second gate — that among the survivors only unscreened Poisson gives the
Newtonian far-field exponent, screened rising `1.68 -> 9.74` — is PR #5693's
result on a prescribed source, which is neither merged nor audited. Rows R0-R14
stand without it; the composed selection sentence does not.

## The condition, stated plainly

The separation rests on requiring that an isolated object's binding energy have
a limit independent of the box it is measured in. That is a condition, not a
neutral measurement, and row R14 shows what it costs: biharmonic's *local field
differences* across a fixed window are perfectly box-independent, so under a
reference-to-fixed-radius choice biharmonic is not excluded at all. The
hostile reading — that requiring a box-independent binding energy is requiring
an asymptotically free kernel, which is a Newtonian property smuggled into the
test — is recorded in full in the gates document's N7 steelman, and this note is
demoted in response: what is claimed is a bounded theorem under a named
condition, not an unconditional no-go against biharmonic.

## Verification

```bash
python3 scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py
```

The runner verifies that both parent modules it imports match their committed
blobs (row P0) before measuring anything.
