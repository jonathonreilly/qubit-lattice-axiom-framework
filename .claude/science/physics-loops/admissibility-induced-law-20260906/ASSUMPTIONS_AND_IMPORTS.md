# Assumptions and imports — admissibility-induced-law-20260906 (block 01)

## Scientific dependencies
- The four axioms, `docs/MINIMAL_AXIOMS_2026-06-29.md` (premise node `minimal_axioms`): the Admissibility sentences (one fixed covariant nearest-neighbor rule; "determined by, and varies with, the nearest-neighbor conditions") and the Record sentences ("Records form."; permanence; one per site; "Only records are readable."; "A site with no record cannot be read.").
- Upstream landed note (unaudited): `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md` — the static half on binary menus. Linked; its mechanism is re-proved here at the six-state scope.

## Named premises (not axiom content; each shown load-bearing)
- **Records-only extension** of a rule to partially recorded neighborhoods: an unrecorded neighbor contributes no factor and is not a condition. Read off "Only records are readable" / "A site with no record cannot be read". The alternative (a covariant absence-dependent factor) is route G(3), computed.
- **Formation order**: the axioms supply no order; every formation-law statement is "for every total order on the window" or for a declared order family.
- **Positivity** of the rule (every menu value has nonzero probability under every condition): needed for the product-form conclusion (T1 ⇒); its necessity is witnessed (family E).
- **Declared menu and windows**: the six Bloch-axis projectors; path3, star4, cycle4, cube8 with open boundary. No claim beyond them.

## Declared mathematical scaffolding (not physics inputs)
- The 24 proper cubic rotations as signed axis permutations; their spinor lifts for two generators (exact).
- Exact rational weight triples `(3,1,2)`, `(5,2,4)`, `(2,2,2)`; sum-rule couplings `1/4`, `-1/8`; the fixed linear congruential generator for the cube configuration sample (seed 20260906).

## External references (reference and re-prove; never authority)
- Brook (1964) ratio lemma; Besag (1974) consistency of conditionals; Hammersley–Clifford (1971, unpublished) / Grimmett (1973) factorization; Moussouris (1974) non-positive Markov field on the four-cycle. Each finite statement used is re-proved in the note at its scope.

## Counterfactual pass (what if an implicit choice is wrong)
- Boundary: open windows (no exterior records). Fixed exterior records would enter as recorded neighbors; the formation identity is unchanged in form (the exterior contributes factors to both numerator and each `Z_k`); not executed — named.
- Menu: a non-transitive menu (e.g. the Q8 atoms with the two central points) would make the one-neighbor normalizer non-constant, so T2(a)'s "at most one recorded neighbor" criterion would shrink; named, not executed.
- Site weight `ψ`: constant by covariance on the transitive menu (executed); on a non-transitive menu it is not.
- Simultaneous formation (several records locking in one step) is not a total order; the formation law of a partial order with simultaneous steps would need a joint conditional the axiom does not state; named in N7.
- Infinite volume: the static specification's DLR existence (compactness on a finite menu) and uniqueness are outside the block.

## Block 08 (2026-09-15) — the three-dimensional monotone formation law

### Scientific dependencies
- `minimal_axioms` (the Admissibility sentences; "no possibility is privileged" through the internal covariance of the rule; Record's records-only reading).
- Block 05's note on main (the rectangle law `μ_P`, P1's recorded-set argument, P4's chains, P7(a)'s 180° identity) and block 02's note on main (E1–E3: the row transfer preserves the chain law; the projective limit on the strip). Both proposed, unaudited; the parts used are restated and re-proved at scope.
- Block 03's note on main (the coupling method for the static law; re-proved here for the formation law with a different structure — monotone paths instead of a random scan).

### Named premises (supplied; not axiom content)
- The records-only extension of the rule; positivity `p, q, r > 0`; the six-axis menu; the monotone class (linear extensions of the product order on a box) as a declared order class with a declared corner; the sweep direction `x_1` (any axis by symmetry).

### Declared mathematical scaffolding
- The one-neighbor sensitivity `c_k := max TV(r(·|A), r(·|A'))` over `k`-tuples differing in one entry; `c := max(c_1, c_2, c_3)`; exact rationals at `(3,1,2), (5,2,4), (7,3,5), (2,1,2), (3,2,2), (5,4,4), (11,10,10), (2,2,2)`.
- Monotone-path counts `N(z, x)` (multinomial) and the generating function `Σ_j C(n+j, n)(2c)^j = (1−2c)^{−n−1}`.
- The internal symmetry group of order 48 and the plane transpose for the orbit reduction of the `2×2` plane transfer.

### External references (reference and re-prove; never authority)
- Unilateral Markov fields / Markov meshes; probabilistic cellular automata and their high-noise uniqueness (Dobrushin–Vasershtein-type coupling); Perron–Frobenius for positive matrices (block 02's F2 on main); Kolmogorov extension; Krylov–Bogolyubov for Feller kernels on compact spaces.

### Counterfactual pass
- Sweep axis: by the axis-permutation symmetry of the box law, the choice of `x_1` is immaterial; removing the first plane in any direction fails the same way.
- Corner: the eight corner classes of `Z^3` give (by the point-reflection argument that fails in 3D) up to eight laws; this block treats one corner and states the covariant family; #8102's cube witness shows reversal moves the law.
- Cross-section boundary: open (no exterior records); a fixed exterior record would enter as a recorded neighbor of the boundary sites, changing `c` to the sensitivities of larger recorded sets (bounded by `c_3`'s analogue with up to four neighbors); not treated.
- Menu: the sensitivities `c_k` are menu-specific; the theorems (A)–(E) hold for any finite menu with a positive symmetric covariant `φ` with the same proofs; only the exact numbers are six-menu.
- Order class: a non-monotone order (snake, random priority) has different recorded sets; the coupling theorem's mechanism (discrepancy along recorded-neighbor paths) applies to any order with the branching number replaced by the maximal out-degree of the recorded-set graph; not executed here.
