# Route agent R3: the exact-price lens

**Agent:** Claude Opus 5.5, extra-high (xhigh) effort.
**Refresher read (stated):** the full axioms, the primitive registry check, `axiom_premise_nodes.json`.
**Scripts:** `scripts/R3_c1 … c6` with their outputs.
**Labels:** EXACT means a proof given here, not landed. Nothing in this report is refereed.

## The general-lemma question: does any local theory on fixed adjacency have a TT stiffness?

Not "always nonzero". What does hold:
1. **No symmetry protection (EXACT, Schur).** Under O_h the traceless strains split into E_g ⊕ T_2g, so there are two free numbers. A trace-only mechanism moves both equally or not at all. K3a″'s refereed values have opposite signs, so one such term cannot cancel both. This closes ledger row S6, and agrees with R4.
2. **No exact equivalence between shears on a crystal (EXACT).** Suppose a unitary maps H(g) to H(g′) and maps Z³ translations to Z³ translations. Then g′ = M⁻¹gM⁻ᵀ with M ∈ GL(3,Z), a discrete set. So a shear can be pure gauge only if the translation group is continuous. This agrees with R4's Lemma R.
3. **The window part is a surface term (EXACT, CHECKED).** E″ = ½∮_∂D φ′(|p|²)(p·h·p)(p·h·n̂) dS.
   - A ball gives exactly −K₀⁴/(60π²) for the Dirac sea, which extends the supervisor's S0 identity.
   - The cube [−π, π]³ gives −0.4317 (E_g) and −0.3828 (T_2g); bulk, surface and finite-difference values agree to 8 digits.
   - The sign is that of φ′ at the cutoff.
4. **See-or-stiff (EXACT for networks, CHECKED).**
   - Simple-cubic springs: E_g = 0.25, T_2g = 0.
   - A diamond central-force network with a relaxing inner sublattice (a pentamode): all 5 traceless strains are exactly 0.
   - Adding a bond-angle term makes all 5 stiff.
   - So the stiffness vanishes on a fixed graph exactly where the graph cannot see the strain. Spinor frames need angles, so universal coupling makes every channel visible.

## Point-set checks (CHECKED; couplings computed from current proper distances only; E″ per site)

| Substrate | Scalar E_g / T_2g | Frame-sensitive Dirac sea E_g / T_2g |
|---|---|---|
| Z³ crystal | +0.0474 / +0.0140 | −0.688 / +0.235 |
| Jittered Z³ | +0.0232 / +0.0132 | — |
| Hard-core frozen (d₀ = 0.8), a glass | +0.0041(1) / +0.0041(1) | −0.108(1) / −0.108(1) |
| **Pattern-free (Poisson) frozen, mean** | **≤ 1.2e-4** at boxes 8/10/12 | **≤ 1.7e-3**, inside the crystal's own finite-size drift |
| **Pattern-free, random part per site** | **0.035–0.040** | **0.11–0.13** |

- **Why the Poisson mean vanishes (EXACT).** A Poisson set mapped by a volume-preserving map is again Poisson in law. This agrees with R2's Lemma A.
- **Why correlated frozen sets must fail (EXACT).** Every pair term is shear-blind at O(t²) only if the pair density satisfies 4ρ₂′ + rρ₂″ = 0, so ρ₂ = a + b/r³. Local finiteness forces b = 0. **No minimum spacing is allowed**, and a glass fails.
- **The random part is white noise (CHECKED).** Its per-realization spread scales as 1/√N.
- **What it does to gravitons (ARGUED, Born estimate, order of magnitude).** A random mass-type term scatters at a frequency-independent rate. The mean free path is about 0.2–300 l_P at a = l_P. Waves crossing 1 Gpc would need a⁻¹ ≲ 1e7 GeV.
  - **So a frozen Poisson set fails on fluctuations, though its mean is fine.** This corrects R2's Route 1 "Poisson passes".
- **Mobile sites in a liquid (EXACT, given a liquid ground state).** x → g^{1/2}x is an exact unitary intertwiner, so the stiffness is zero **configuration by configuration**.

**Prior art and a correction.** The outside view already has fluid protection, the finite label symmetry, Volovik and the Poisson test. The agent read it only after its own checks.
- **The correction.** The outside view says "adjacency recomputed from geometry makes the vacuum a fluid", and its Poisson–Delaunay pass criterion (a zero mean) is **insufficient**. A pass must also require that the per-configuration σ·√N vanishes.
- **The reason.** Recomputed adjacency on **frozen** sites fails, on the glass mean and on the Poisson random part.

**Price in one sentence (R3): "the sites must be free to flow."**

## Routes

| Route | Family | Premise changed | What you would have to believe | First artifact (pass/fail) | Cost | What it would change |
|---|---|---|---|---|---|---|
| **1. Flowing sites** | E(g); exact x → g^{1/2}x intertwiner plus a liquid vacuum; obligation: a graviton kinetic term plus a conserved stress on this substrate | Lattice point set Z³ → mobile sites with continuous positions; Admissibility's "nearest neighbour" becomes geometric; positions are extra continuous variables beyond M₂(C) | The vacuum is a quantum liquid, not a crystal or glass, and the fluid's sound and vector modes stay off gravitational strength | **Done in a toy:** crystal, glass and frozen pattern-free sets all fail configuration by configuration. **Next:** ground-state E″ of a mobile-site liquid, for example a bosonic He-like variational state, against its crystal phase. **Pass:** the liquid gives 0 within errors and no √N random part, while the crystal gives a nonzero value | It replaces Lattice (owner decision). It loses the exact Z³, K7a's W(B4) staggered structure and G0c's face qubits. **The fluid's rest frame violates Lorentz invariance in the scalar and vector sectors** (COMPARATOR, Dubovsky) | **It prices the stiffness face exactly**, removing K3a″'s and W1's stiffness at every order. The finite-slot partner face (L2) and the kinetic term remain |
| **2. Keep the grid and pay with an identity or tuning** | E(g) on Z³; Schur split; obligation: E constant in E_g and T_2g | Drop S6, or add a Q-exact structure | Either two tuned counterterms, or SUSY unbroken down to Δ ≲ 0.2–1 keV against TeV collider bounds (ARGUED; m_g ~ Δ²/M_P with zero mass supertrace). A frustration-free (RK) vacuum gives E ≡ 0, but gapless frustration-free systems have z ≥ 2 (COMPARATOR) | A boson–fermion Q-exact model on Z³ under strain. **Pass:** E ≡ 0 to machine precision while unbroken, and the modulus ∝ Δ⁴ once softly broken | low | Closes S6. The tuning price is exactly 2 counterterms |
| **3. See-or-stiff on fixed graphs** | networks; invisibility under relaxation | S7 | Matter is blind to the shear | Done: the pentamode is 0, and an angle term restores stiffness | done | Closes the under-coordinated-graph escape |

**Gap test.**
- **Route 1** is target-equivalent for the stiffness face. Sufficiency is EXACT; necessity holds for frozen sites at the two-point level, with the random part CHECKED. It brings a new mechanism, so it is not blocked-equivalent. Its remaining obligations are on a new substrate.
- **Route 2:** tuning is a forbidden weakening, and the identity versions are excluded (ARGUED).
- **Route 3** is blocked-equivalent.

## The exact price (R3)

The stiffness face is equivalent to "**the vacuum has no continuous relabelling symmetry in each configuration**". In ledger terms that is L1's fixed point set together with S4 (a non-liquid vacuum), not adjacency alone. The partner face (L2) is untouched.
