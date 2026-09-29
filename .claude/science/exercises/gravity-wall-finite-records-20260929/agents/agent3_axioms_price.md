# Agent 3: the axioms' own structure and the exact price

**Read:** `MINIMAL_AXIOMS_2026-06-29.md` (full), `PRIMITIVE_REGISTRY_CHECK.md`, `axiom_premise_nodes.json` (skim), neutral brief, `WALL.md`, `ASSUMPTIONS.md`, CCR note (05-02), comparator (09-24), tensor parent (09-14), probes 10, 17, 20, 21 in full, probe 11's scope. All premises treated as fallible.

## 1. What the wall is equivalent to

C24 works because two terms are invariant only *weakly*: DeWitt (O(1) in E, invariant on GE = 0) and h·R(h) (O(k²) on TT, invariant under h → h + Gᵀξ after summation by parts, GR = 0). Both are polynomials in a variable the constraint translates by a c-number.

**Lemma P (compact variables: weak = strict).** Let each h_s live on a circle or finite cyclic group and H = Σ_s f_s(h) be periodic. If Σ_s[f_s(h+Gᵀξ) − f_s(h)] = 0 for all h, ξ, every character e^{im·h} in H has Gm = 0. *Proof.* Fourier-expand; the coefficient of e^{im·h} is C_m(e^{im·Gᵀξ} − 1), zero for all ξ only if Gm = 0. ∎ With the landed moment lemma, TT stiffness is O(k⁴). Same for E under S.

**Corollary (the "compact-character class" is vacuous on finite slots).** M_N(C) is spanned by Weyl words XᵃZᵇ; a local term restricted to the stabilizer sector is its projection onto the commutant, a sum of words with Gb ≡ 0, Sa ≡ 0 (mod N). No third kind of term exists. The 09-14 bound's real hypotheses are lifting (±½ spectra lift automatically, probe 10) and the harmonic expansion.

Trichotomy for the vector rule: (S) stabilizer ⇒ Lemma P ⇒ ω_TT = O(k²) [21(i)]; (∅) absent ⇒ ±1 partners [20, 21(ii)]; (W) c-number generator, H weakly invariant ⇒ Einstein [C24], needing a variable with spectrum R (probe 17 A).

**The CCR step is not load-bearing.** Fluctuation operators F_q(A) = N^{-1/2}Σe^{iq·x}(A_x − ⟨A⟩) of qubits in any clustering state form an exact CCR algebra in the limit (Goderis–Verbeure–Vets quantum CLT; defect ~ L^{-3/2}). Collective canonical pairs are free. What survives coarse-graining is the moment lemma in state-independent form, probe 10 T3: m₁(F_q(E)) ≤ C_H q⁴ in every eigenstate, every N, every block.

> **Price.** Einstein's TT mode needs a local term with nonzero TT first moment that the vector rule leaves invariant. On a finite-dimensional local algebra with the rule exact none exists (Lemma P), in any state. A linear mode can then only sit in a channel with χ_TT = O(q²), S ≤ O(q³) (T4): an incompressible TT-electric pattern. If E–E correlations cluster exponentially, S is analytic and even, and the T4 chain forces S, χ = O(q⁴): the mode's momentum is not the stored E.

Theorem-strength test: inside the harmonic class the trichotomy equals the target iff non-additive realizations are exhausted; probes 14/15 put the tested ones in (S) by the f-sum. Outside it the gap is exactly (E): a rule holding only on a low-energy subspace.

## 2. Routes

| Route | Family | Premise dropped/changed | Must believe | First artifact | Cost | Changes |
|---|---|---|---|---|---|---|
| **1. Price as lemma** | Lemma P + corollary; obligation: the scalar-rule analogue of T3, so both Hessian orders are state-independent | None dropped; S2 becomes exact ("finite slots" = "both conjugates compact"); A2 relieved of the CCR blame | The harmonic expansion around the chosen state is honest | The proofs above. Falsifier: a sector-preserving local finite-slot term with nonzero TT first moment | A note | Wall premises shrink to {rule exact as stabilizer, harmonic}; ledger row CCR no longer load-bearing |
| **2. Collective / incompressible** | Fluctuation algebra; mechanism: emergent 1/q² TT-electric interaction; obligation: a gapless state with χ_TT ~ q², S ~ q³ | S4, S11 | A finite-slot model has a gapless phase with an insulator's TT-electric response, and the mediator of the long-range interaction does not propagate (photon mediators bring ±1 partners: probes 11, 16) | Falsifier lemma above: clustering E–E ⇒ graviton decouples from E at O(q⁴); so route 2 needs power-law E–E tails (~r⁻⁶, non-analytic angular part). Test: E–E tails by ED/DMRG in the 20-slot exact-rule qubit family | Many-body numerics | No tails in any low-energy state closes the E-stored route beyond harmonic order |
| **3. Reading: gravity is not a mode** | Admissibility as a Markov random field; gravity as an equation of state (Jacobson); obligation: a local energy/boost structure | S1, S8's "mode" form; all four axioms kept | TT waves at 10⁻¹⁵ speed with Gpc damping lengths can be hydrodynamic modes of the record process (not harmonic lattice modes, so probes 10–21 do not apply) | **Lemma MI.** For any NN rule read as an MRF, I(A : Aᶜ) ≤ H(∂A) ≤ \|∂A\| ln 2 (given ∂A, inside and outside are independent). Jacobson's area law; probe 19's volume law is entropy, not MI. The missing half, δQ = T dS, needs a Hamiltonian, boost and time metric, which AX:114–123 exclude | Target becomes an equation of state; damping must be computed | The graviton wall becomes the time-metric wall of the source-link lane (blocks 53–62, 112) |

Rejected readings: lapse-only/frozen star is scalar, GW polarization is tensor; the Z⁴ block reading meets Lemma P in Euclidean form (curvature-squared action, 1/k⁴ propagator).

**(2), precisely.** Transfers to collective variables: T3 (any state, any block; block size only rescales C_H) and probes 20/21 (symbols of local quadratic forms: any harmonic effective theory local in block units). Does not transfer: the CCR no-go and Lemma P (the fluctuation algebra is non-compact). The collective wall is the sum rule, not "error vs block size"; it is escaped only by a non-linear, non-local, or non-E momentum (T5's list).
