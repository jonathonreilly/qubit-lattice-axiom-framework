# B19 check

Provenance: a fresh-context checker of the same model family. Its code is new and imports nothing from B14, B16 or B19. Saved by the supervisor from the hand-back.

**Method.** sympy Function fields with `euler_equations`; vanishing tested through Fourier kernels on the momentum-conservation surface; an independent second-order √gR; fully general ansätze (no isotropy, no parity); lattice tested by exact rational rank plus least squares optimised over ζ.

**Result: 19 PASS, 0 FAIL.** The first gravity run had the checker's own bugs and is kept.

## Verdicts

1. **{G, G}: confirmed.**
   - λ G_m closes iff λ ∈ {0, ν}.
   - λ1 G1 + λ2 G2 closes iff λ2 = ν, with λ1 free. λ1 is the background scale r.
2. **Confirmed, more generally than B19 tested.**
   - With a general 3×3 structure matrix, {C, C} forces K1/(4αλ1)·I and v_s² = λ_s K1/(4αλ1).
   - {G, C} at matter² gives s1 = −λ_s, using general 120/126-coefficient couplings, an 18-coefficient lapse rule, G_s[BNξ] terms and Gauss multipliers.
   - Shear coupling = (λ_s/λ1) × metric stress.
   - λ_A = λ_m, because G1 produces only ∂ξ.
3. **A genuine derivation; nothing smuggled in.**
   - With a fully general 648-coefficient one-derivative G2, the h-linear {C_g, λ1G1 + G2} forces N′ = −(λ1K2/K1)ξ·∂N. G2 has a 144-dimensional null space. G2 = 0 has no solution.
   - Solved as one chain: λ_m = λ_A = λ1K2/K1, so v² = K2/(4α), the TT graviton speed².
   - Block 62's R1 and R2 are exactly the first- and second-order parts of √gR, so K1 = K2.

   **Corrections:**
   - (a) **s2 = 0 is a lapse/density-weight convention.** Under N → N(1 + t tr h), s2 = 2λ1t. Only s1 enters the cone.
   - (b) **K1 = K2 needs a premise.** Block 101's quadratic Hamiltonian must be read as C(N = 1) of a lapse-smeared constraint, with R2 inside C.
   - (c) **Further premises:**
     - one total C and G;
     - a field-independent, local, first-order lapse rule;
     - G2 local, P-linear and one-derivative;
     - the Fierz–Pauli form of R2.
   - (d) **Open:** degree-2 brackets might force K1 = K2 on their own.
4. **Confirmed, with scope.** λ_s is invariant only under sector-preserving canonical maps at a fixed ξ normalisation. Only ratios are meaningful.
5. **Lattice: confirmed.**
   - Exact non-closure at L = 3, 4.
   - Optimised over ζ, the defect slopes are −2.3 (scalar) and −0.89 (Maxwell G_L).
   - B19's β_s values are diagnostics.

**Novelty.** The physics is known: Teitelboim; HKT; Barbour–Foster–Ó Murchadha 2002; Anderson–Barbour 2002 (their geometric Lie-derivative transport hides the λ's); Deser; Weinberg 1964. New and internal are:
- the normalisation bookkeeping;
- that B14 and B16 omitted gravity's own h-linear {G, C};
- that the B16 check's {G, G} argument leaves λ1 free.
