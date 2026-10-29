# Approach note: REC-LIB, rebuilding the Osterwalder–Schrader reconstruction in our library

Lead: Claude Opus 5.5, 2026-10-29. This follows the owner's directive of 2026-10-29: "if we need their proofs
or lemmas just rebuild them and put them in the repo / PR / library." Execution is by Codex on the Mac mini.

## Why this item
- The full-proof goal is existence **and** the mass gap. Existence in the Clay sense means a quantum field
  theory satisfying axioms at least as strong as Wightman's, or OS axioms that yield them.
- Everything that turns our Euclidean state into that theory rests on **Theorem REC** (OSLEAF55 §1.4). Its parts
  stand as follows:
  - (a)-(d) are PROVEN-HERE. They cover the Hilbert space, the semigroup and the time-zero structure. The mass-gap
    target's Hamiltonian lives in this part.
  - (e) is **IMPORTED [m-sec]**. It is the step from the linear growth condition E0′ to tempered Wightman
    distributions with the spectral condition, Poincaré covariance and locality.
- ASSEMBLY55 lists the reconstruction theorem as **N9 (REC): MISSING (literature)**, and CODEX_REVIEW_SRCCD
  records that the OS papers were never reached (a security page blocked access).
- OSLEAF55 also notes that the several-field, tensor version of "E0′ ⇒ Wightman" is not written down
  anywhere: OS say the adaptation "should be relatively straightforward". We need exactly that version, because
  our fields are the clover densities e_a and the tests are ^0𝒮, which vanish on coincidence sets.
- CODEX_REVIEW_OSLEAF F6 flags a defect in REC: the translation estimate omits the insertion number.

This is pure mathematics with a known proof strategy, so it is the item most likely to close completely. It is
independent of the soft/hard decision (SOFTHARD lane) and of every RG estimate. It removes a load-bearing citation.

## Target
Theorem REC-LIB. Let {S_n} be Schwinger distributions on ^0𝒮(R^{4n}) ⊗ C^{m^n}, finitely many real
fields, as in OSLEAF55 §1.3, that satisfy:
- (E0′), the linear growth condition: |S_n(F)| ≤ α(n!)^β |F|_{sn};
- (E1), Euclidean covariance;
- (E2), reflection positivity on the ordered positive-half cone that OSLEAF55 actually uses;
- (E3), symmetry.

Then there exist:
- a Hilbert space H;
- a vacuum Ω;
- a continuous unitary representation of the Poincaré group, satisfying the spectral condition;
- tempered operator-valued distributions φ_a, satisfying the Wightman axioms (including locality and cyclicity
  of Ω);

whose Wightman functions are the boundary values of the analytic continuation of {S_n}.

Also state the corollary that the mass-gap target consumes: the Hamiltonian from (a)-(d) is the same operator as
the Wightman generator of time translations, and a gap of its restriction is a Wightman mass gap.

## Proof route
The structure below is recalled from memory and serves only as orientation. Every step must be rebuilt here.
1. **RP gives the Hilbert space.** Build the pre-Hilbert space from the positive-half cone, quotient by the
   null space and complete. Build the contraction semigroup e^{-tH} with H ≥ 0, and the spatial
   translations/rotations. (Re-derive OSLEAF55's (a)-(d), and fix F6's insertion-number omission.)
2. **Analyticity in the time differences.** Show holomorphy in Re t_k > 0 from the semigroup. This step does not
   use E0′.
3. **Inductive continuation to the forward tube.** This is OS II's mechanism, recalled from memory:
   - continue in successively larger domains 𝒞_N;
   - use E0′ to get bounds of the form |S(z)| ≤ C_n (1 + |z|)^{k_n} (dist to the boundary)^{-k_n};
   - these bounds make the boundary values tempered.

   The linear dependence of the seminorm order on n is exactly what E0′ supplies. Locate where it is used, and
   check whether our SRC-κ form C_0^n(n!)^p p(f)^n, with fixed seminorm order p, implies it, using the
   reviewed match s = 11, β = p + 3 from CODEX_REVIEW_OSLEAF item 2.
4. **Lorentz covariance.** Use one of two routes:
   - continue rotations in a time–space plane to boosts;
   - the Klein–Landau / Fröhlich symmetric-local-semigroup route, which may be shorter.

   Choose one, and prove it in full.
5. **Spectral condition** from H ≥ 0 and the positivity of the momentum generators.
6. **Locality** from E3 symmetry, using Jost points and edge-of-the-wedge. If edge-of-the-wedge is load-bearing,
   rebuild it as its own library lemma.
7. **Several fields and tensors.** Carry finitely many real fields and tensor indices through the whole argument,
   with explicit constants.
8. **Coincidence-vanishing tests.** Make sure that working on ^0𝒮 instead of full 𝒮 loses nothing. OS worked on
   ^0𝒮; check this in the proof itself rather than assuming it.

## Acceptance
- Each step is PROVEN, or it is a named library lemma that is itself PROVEN in this lane.
- A step marked [m] or IMPORTED may remain only if the final statement names it explicitly as an open residue.
  Then the result is CONDITIONAL, not PROVEN.
- The theorem's hypotheses match OSLEAF55's E0′-E3 and its test algebra word for word. Any mismatch is recorded
  as a binding fix to OSLEAF55, not glossed over.

## Credit
Osterwalder and Schrader (1973, 1975) for the theorem and the method. Glaser, Zinoviev, Klein–Landau and Fröhlich
where their routes are used. The proof itself is ours.

## Exact checks (optional, finite)
These are algebra sanity checks only. For a free field with a known two-point function, check that:
- the analytically continued Schwinger function equals the Wightman boundary value at sample points;
- the RP Gram matrix on a finite family of ordered positive-half tests is PSD.

Write the criteria first.
