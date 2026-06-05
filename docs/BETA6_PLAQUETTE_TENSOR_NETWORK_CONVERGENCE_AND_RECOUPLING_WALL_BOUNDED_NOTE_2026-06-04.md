# Beta=6 SU(3) Plaquette Tensor-Network Route: Irrep-Truncation Convergence and the Recoupling Wall

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_plaquette_tensor_network_2026_06_04.py`](../scripts/frontier_beta6_plaquette_tensor_network_2026_06_04.py)

## Scope

Characterizes the tensor-network (character-expansion) route to `<P>(beta=6)` --
the route ORTHOGONAL to the strong-coupling series, which truncates by IRREP /
bond dimension rather than by order in `beta`. Two results: (i) the irrep
truncation **converges** at `beta=6` (the series does not: radius `R~5.4<6`); and
(ii) the actual `D>=3` contraction is the SAME treewidth-29 wall, via `6j`
recoupling. Frontier_discovery / scoping increment; NOT a closure of `<P>(6)`.

## (i) The irrep truncation converges at beta=6

The single-link character coefficients
`a_lambda(beta) = int_SU(3) chi_lambda(U)^* exp((beta/3) Re Tr U) dU` were computed
**three independent Haar ways that agree exactly**: (a) the add-a-box
Clebsch-Gordan multiplicity series `a_lambda = sum_{P,Q} (beta/6)^{P+Q}/(P! Q!)
m_lambda(P,Q)`; (b) the Schur-Weyl Bessel determinant; (c) direct Weyl-torus Haar
integration. Cross-checks: the singlet `a_(0,0)(beta)` equals the framework `J(beta)`
recurrence (`a_(0,0)(6) = 3.4414...`); `sum_lambda m_lambda(P,Q) dim_lambda =
3^(P+Q)`; the add-a-box singlet multiplicity equals the exact Haar projector trace.

At `beta=6` the coefficients **decay exponentially in the quadratic Casimir**:

```text
a_lambda(6) ~ exp(2.15) * exp(-0.296 * C2)        (fit, C2 >= 5)
c_lambda = a_lambda/a_(0,0)  drops below 0.1% at C2 ~ 24-26  (~41 irreps)
```

So the **irrep-truncated character sum converges at `beta=6`** -- the key premise
of the TN route, and exactly what the order-in-`beta` series cannot do (its radius
is `~5.4 < 6`, a complex-conjugate pair off the real axis).

## (ii) 2D validation

SU(3) lattice gauge theory factorizes in 2D, so `<P>_2D(6) = a_F/(3 a_(0,0)) =
0.422532`, equal to the framework single-plaquette `P_1plaq(6) = J'(6)/J(6)` (the
certified value, separate note) and to an independent SU(3) Haar Monte-Carlo
`0.4231(8)`. The character machinery is correct.

## (iii) The recoupling wall (honest)

The naive "one irrep per plaquette + delta link constraints" dual contraction is
valid **only in 2D**. In `D>=3`, each link variable sits inside the 4-link product
of *every* plaquette bordering it, so the link integral is a `6j` intertwiner
**recoupling**, not a delta. Contracting that recoupled network IS the treewidth
wall: the campaign's `L_s=3` spatial environment is treewidth-29 (`8^30` exact
contraction infeasible). The naive delta-contraction was checked to converge in
cutoff but **to the wrong value (`0.625`)**, and is therefore NOT reported -- the
recoupling is precisely what raises `<P>` from the `0.4225` single-plaquette value
toward `0.5934`.

So the TN route does **not bypass** the `rho_{p,q}(6)` wall; it **re-expresses** it
as a `6j`-recoupled contraction. The well-posed path through is a **bounded-bond-
dimension TRG / HOTRG** truncation of that recoupled network, with the per-link
irrep cutoff now quantified (`C2 <= 26` for 0.1%). That truncation is not performed
here (`D>=3` non-abelian TRG at scaling coupling is a research-frontier compute);
its cost is the open item.

## Net

The TN route is **viable in principle** (irrep truncation converges at `beta=6`,
established here) but its contraction is the SAME treewidth-29 object that walls
the series and the cluster expansion -- the `beta=6` wall is one object appearing
identically in three formulations (order series, multi-cube cluster expansion,
character TN). A converged, retained `<P>(6)` requires bounded-bond-dimension TRG
of the `6j`-recoupled network; the certified backbone `0.5155...` (separate note)
remains the rigorous lower portion.

## Boundary

- Established (theorems / exact): the three-way-agreeing `a_lambda(6)`, their
  Casimir decay (irrep-truncation convergence), and the 2D plaquette `0.4225`.
- NOT established: any converged `D>=3` / `<P>(6)` value. The `6j`-recoupled
  contraction is the wall; only a bounded-bond TRG (not done) would deliver it.
- Repins nothing.

## Forbidden-import

Clean: all character coefficients are Haar integrals (multiplicity / Bessel /
Weyl-torus routes all equal the same Haar integral); `0.5934` and the Monte-Carlo
numbers are after-the-fact comparators only, never computation inputs.

## Key files

- [`scripts/frontier_beta6_plaquette_tensor_network_2026_06_04.py`](../scripts/frontier_beta6_plaquette_tensor_network_2026_06_04.py) (this note's runner)
- [`BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md) (the certified 0.5155 lower portion; P_1plaq cross-check)
- [`BETA6_PLAQUETTE_D10_COEFFICIENT_AND_DIVERGENCE_VERDICT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_DIVERGENCE_VERDICT_BOUNDED_NOTE_2026-06-04.md) (why the series route diverges at beta=6)
