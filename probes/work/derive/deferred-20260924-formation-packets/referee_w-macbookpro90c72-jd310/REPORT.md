# Referee: deferred-20260924-formation-packets a1

Worker `w-macbookpro90c72-jd310` (`grok-4.6`). Author `w-macbookpro9927a-jb986` (`claude-opus-5-5`). Independent check; the attempt's script is not imported.

## Verdict

Confirmed. The scoped statement holds: on each of the nine boxes, once the uniform vector is cyclic for the transposed plaquette jumps, the normalized RK projector is the unique stationary state for every positive rate vector and every Hermitian Hamiltonian that kills it. That cyclicity holds on every flip component with at least two states.

The general implication "a separating function implies cyclicity" is still open, as the attempt says. The frozen numerical transients and Poisson rewards were not rebuilt.

## What was checked

- **Sources.** `origin/main` is `0e6ad8285096`. The frozen helper, its README, and the landed `scripts/local_gauge_record_cooling_check.py` match the unit-12 manifest hashes. The landed file keeps `geometry` and `gauss` only. The README says the unused cooling routines are not claims of that unit.
- **Local algebra.** On a flip pair plus a spectator, `L = |+⟩⟨−|` is a partial isometry with `L² = 0`, the pair channels compose, and half the derivative at rate 1 is the dissipator. On one pair, `mᵀ v = 2 κ P⁻ v` with `κ = (1+t)/(1−t)`.
- **Separating function.** `F₂ = Σⱼ 3ʲ sⱼ`, `sⱼ = ±1`, is injective because the leading power strictly dominates. Any signed sum of distinct powers of 3 is nonzero, so each plaquette's four distinct links have a nonzero displacement. Both were checked as exact integer inequalities, and then on every component: `F₂` is injective and the displacement is constant on that plaquette's pairs.
- **Census.** 82,872 components, maximum dimension 30: open `2×2` 1 (max 2), `3×2` 14 (max 3), `2×2×2` 778 (max 9), `3×3` 702 (max 7), `4×2` 150 (max 5), `4×3` 27,078 (max 17); periodic `2×2` 35 (max 6), `3×2` 710 (max 12), `3×3` 53,404 (max 30). No face was degenerate.
- **Cyclicity and connectivity.** The pair graph of every component is connected, so the common kernel of the jumps is the constants. The cyclic span of the all-ones vector under the transposed jumps has dimension equal to the component, certified by rank modulo `1000003` (with `1000033` as a retry). A two-state component is cyclic for a one-line reason: one flip sends the uniform vector to a nonzero sum-zero vector. The four-state alternating cycle, which is not a lattice component, has cyclic dimension 2 under the same routine.
- **Divergence.** Every retained plaquette flip changes the lattice divergence by zero. The four signs on a raising flip are known, so this is one identity per face (41 faces), and every component therefore lies in a single Gauss sector.
- **Frozen control.** On the largest components of the open `2×2`, `3×2`, and `2×2×2` boxes (`d = 2, 3, 9`), at `γ_p = p+1` and `h_p = (−1)^p (p+2)` in frozen face order, `8G` has rank `d² − 1` modulo 65537 and annihilates `vec(uuᵀ)` over the integers, so the nullity is one. The same nullity holds for every rate equal to 1 with `H = 0`, and for `H = vvᵀ` with `v` orthogonal to the uniform vector. Numbering only nonempty plaquettes does not change those three rate vectors.
- **Two-level kernel.** For a single pair the leading 3×3 minor of `8G` is `−64 g (g² + 4 h²)`. For real `g ≠ 0` and real `h` the minor is nonzero, and the all-ones vector is a kernel vector, so the nullity is one. At `g = 0`, `h = 1` the rank drops.
- **Counterexample.** The alternating cycle is connected and its only common dark vector is the uniform one, but the cyclic span is two-dimensional. `(vvᵀ + wwᵀ)/2` is a second stationary state, including for `H = P₁⁻ + P₂⁻`. A displacement that is constant on each matching forces `F(0) = F(2)` and `F(1) = F(3)`.

## Kernel argument

The attempt's support argument is the general step. A stationary density is orthogonal to every `L_pᵀ u` because the population of the uniform vector only grows through those jumps. Its support is invariant under the jumps and meets `u^⊥` in an invariant subspace; cyclicity kills that subspace. The support is then one-dimensional and lies in the common kernel, which connectivity reduces to `span{u}`. Square-zero of each jump, which holds because each plaquette's pairs are a matching, kills any other eigenvalue on that line. So the only stationary density is the normalized RK projector.

Contractivity of the semigroup makes the zero eigenvalue semisimple. The Cesàro projection is completely positive and trace-preserving, sends every state to that projector, and the pure-state projectors span the Hermitian matrices, so the kernel itself is `span{|u⟩⟨u|}`. The rank certificates above are the finite witness of that one-dimensional kernel, not a substitute for the parameter-free step.
