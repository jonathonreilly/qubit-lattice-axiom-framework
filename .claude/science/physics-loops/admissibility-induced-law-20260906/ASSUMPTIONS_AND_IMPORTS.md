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

## Block 23 (2026-09-15) — algebraic decay on the plane
- Dependencies: `minimal_axioms`; the possibility-covariance note (on `main`; the sphere domain and the unsoldered reading); block 01 (on `main`; the static reading). Proposed, unaudited. PRs #8153 and #8154 referenced as evidence addresses for the placement only.
- Named premises: the pure-state sphere as the possibility domain; the unsoldered reading; the static reading on plane windows with exterior records (no records outside) and on tori; the exponential overlap with `β` supplied.
- Scaffolding: the cylindrical coordinates `(ρ cos φ, ρ sin φ, ζ)`; the trigonometric polynomial `(Σ_{m≤4}(c cos φ)^m/m!)e^{iφ}` for the shift lemma; sup-norm shells on `Z²` (`j < 30`) and on tori (`L ≤ 12`); `R ≤ 60` for the shell sum; the two-site instance; a `4×4` window, a `24×24` torus, `R ≤ 40` bond sums and a `10⁵`-point grid in the refuting pass.
- Standard mathematical imports at definition level: the shift lemma for the period integral of an entire `2π`-periodic function; the area-preserving cylindrical projection (`dσ = dζ dφ`).
- References named, not used: McBryan–Spencer; Fröhlich–Spencer; Fröhlich–Pfister; Kosterlitz–Thouless.
- Counterfactual pass: a discrete menu (no angle to rotate; block 17 orders on the plane); `d = 3` (the shell sum grows like `R`, not `log R`, and the bound is useless — consistent with block 19's order); the Born overlap (the shift argument applies to any weight entire in the angles; its constants are not computed); the formation reading (block 12).
