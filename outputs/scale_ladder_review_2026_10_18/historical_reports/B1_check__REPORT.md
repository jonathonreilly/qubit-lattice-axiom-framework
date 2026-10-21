# B1 check: item 6 of the scale-ladder note

Saved by the supervisor on 2026-10-18 from the checker's hand-back, recovered from the session transcript. It was not saved at the time. The text is verbatim apart from removing the harness indentation. Its corrections were applied to the note at the time; later campaign work superseded some numbers, e.g. the runner is now PASS=20.

**B1 independent check of item 6 (scale-ladder corner-fermion note).** Verdict: (a) CONFIRMED WITH CORRECTIONS. (b) CONFIRMED. (c) CONFIRMED WITH CORRECTIONS, for both the original and the generalized constant-spectrum versions.

**Provenance.** Fresh-context Claude Opus 5.5 subagent, the same model family as the author, so this is not an independent model family. I did not change branches or commit. The runner reproduces PASS=17, FAIL=0 (about 2.7 min).

My own code builds a cell gauge (my own GF(2) solve over squares, triangles, all 24 link plaquettes and tubes) and infinite-volume Bloch matrices. It imports only the PSG module's combinatorics. Scripts and log are in `/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_check/`: `check_item6.py`, `check_item6.log`, `dp_vmax.py`, `necessity_probe.py`.

**(a) Minimal Weyl automaton**
- **Formula.** I built U(k) = d − i n·σ from the D'Ariano–Perinotti (DP) / Bisio et al. form. It is unitary (4e-16), and an 8-neighbour BCC fit with h = (±1,±1,±1)/√3 leaves a residual of 1e-14, each transfer matrix having rank 1. Its eigenphases are ±arccos(c_x c_y c_z − s_x s_y s_z).
- **Sign.** The minus sign is one of DP's two Weyl automata, the mirror pair ω⁺(k) = ω⁻(−k). Papers label it differently: it is d⁻ in arXiv:1407.6928 and ω⁺ in arXiv:1601.04832. Both automata are legitimate.
- **Units.** Speeds are in nearest-neighbour distances (|h| = 1) per step.
- **Speed and symmetry.** The speed is 1/√3 and the anisotropy is linear (spread halves with |k|). The dispersion is invariant under 24 of the 48 signed permutations, which is T_d. Its proper part is T (12 elements), and inversion is not included. So it is T-type, not O.
- **Correction 1.** The largest group speed is exactly 1/√2 = 0.70711, reached at k/√3 = (3π/4, −π/4, 5π/4) with v = (1,1,−1)/√6. The runner's 0.705 is an undersampled value from 3000 points.
- **Correction 2.** The real causal cone of one BCC step is the cube |x_i| ≤ 1/√3, and max|v_i| reaches it (0.5773). The runner's test |v| < 1 is therefore weak.
- **Correction 3.** The "collinear pairs" check just restates the phase speed at k/2, so it is not an independent test.

**(b) Corner step**
- **Proof that H_link(k)² = 2.** Each corner {a,b} at site v has exactly two link neighbours: {−a,b} at v+a and {a,−b} at v+b. The diagonal of H_link² is therefore 2. The only off-diagonal two-step endpoint is {−a,−b} at v+a+b, and it is reached by exactly two paths. Those two paths make up a link plaquette of flux π, so they cancel. This holds for any gauge with π link-plaquette flux, in infinite volume. Numerically the error is 4e-16 over 500 random k.
- **Symmetry.** H_link has trace 0, so its +1 space has dimension 6, and the reflection's +1 space has dimension 8. These meet in at least 2 dimensions, and generic k gives exactly 2: the flat pair. W commutes with all 24 PSG rotations and the translations (real space on the L = 4 torus, my own gauge). At k* the commutant has dimension 6, which forces E1/2 + E5/2 + 2G3/2.
- **Speed is exactly 1/√3.** The first-order matrix M(q) on the 6-dimensional node is a rational Gaussian matrix with no √2. With sympy, exactly: M³ = (|q|²/3)M, tr M = 0 and tr M² = 4|q|²/3. So the first-order eigenvalues are 0, 0 and ±|q|/√3, each 2-fold. The commutant splits the node 2 + 4, consistent with G3/2 + E1/2. Corrections to the speed scale as q².

**(c) No-go lemma**
- **Step 1.** It holds because E1/2 and E5/2 each have multiplicity 1, and that decomposition is forced.
- **Step 2.** P_D commutes with every F_j(k*), so the "transport" by the other factors is just scalars. The projected ∂W·W⁻¹ is exactly the sum of the projected ∂F_j·F_j⁻¹.
- **Step 3 (generalized version) is correct.** A cleaner proof: with a constant spectrum, write F = Σλ_i P_i(k). Since P_j ∂P_i P_j = 0 for all i, j, the projection P_E ∂F P_E vanishes onto the full eigenspace E. D lies inside E, so the projection onto D vanishes too.
  - Small fix to the wording: the eigenvalues of P ∂F F⁻¹ P are −i times the eigenphase shifts.
  - The argument needs E to be F_j's whole eigenspace at k*; D alone is not enough.
- **Required correction: the lemma needs isolated doublets.** It holds only for a spin-½ level of W at k* that is exactly 2-fold. In the corner step's 6-fold node, P_D T P_D = 4e-16 but P_D T P_G ≈ 0.46: the E1/2 doublet mixes into the cones. The current text says "every spin-½ doublet", which is false for multifold nodes.
- **Inconsistency introduced by the generalization.** "What escapes it" asks for a factor "with nonzero doublet velocity and a k-independent spectrum". The generalized lemma proves no such factor exists. The escape routes are instead:
  - a symmetric factor with a k-dependent spectrum, outside the algebra generated by constant-spectrum symmetric factors;
  - non-symmetric factors whose product is symmetric (the proof fails there);
  - multifold nodes;
  - giving up O.
- **Strengthening.** The doublet velocity G ↦ P_D ∂G P_D is a derivation: on D the generators act as scalars at k*. It vanishes on the whole algebra generated by such factors, sums included, so Hamiltonians are covered as well as steps. Numerically, H0(t1, t2) plus five symmetric polynomials in H_link and H_on all give doublet velocity exactly 0. This explains why the runner needed its separate X term (v ≈ 0.11).
- **Counterexamples.** I found none within the stated hypotheses. Mixed products of reflections, exp(iθR), conjugated on-site unitaries R·U·R and random symmetric on-site unitaries gave 24 isolated doublets, with max half-splitting/q = 8.9e-9.
- **Hypothesis wording.** "Function of A with A² constant" makes F = α + βA. If β ≠ 0, F symmetric implies A symmetric, so that part of the hypothesis is stated consistently.

Sources:
- [arXiv:1306.1934 (D'Ariano–Perinotti 2014)](https://pdf.arxiv.org/pdf/1306.1934)
- [arXiv:1601.04832](https://arxiv.org/pdf/1601.04832)
- [arXiv:1407.6928](https://arxiv.org/pdf/1407.6928)
- [arXiv:1601.04842](https://arxiv.org/pdf/1601.04842)
