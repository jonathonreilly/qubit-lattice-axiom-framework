# Hostile review of the gauge report (c7/hard/gauge/REPORT.md)

Most of the report's mathematics holds up. Three of its headlines claim more than the arguments show, and one claim is probably already answered in the literature: the report treats SU(2) Wilson infinite divisibility as open, but Kent 1977 very likely already covers it. I worked by hand only. I ran no code, wrote no files and made no git writes. I read the notes on origin/main at `0485dc0738`.

## Verdicts

**O1 (site-frame redundancies are locally SU(2)^a×U(1)^b): HOLDS WITH NARROWED SCOPE.**
- **The proof is right (EXACT).** The site map π is injective, and on a finite C it is a bijection. Skolem–Noether then gives α = Ad(⊗u_x)∘π. Permutations are discrete, so a connected group lands in ∏PU(2). Simplicity then forces the semisimple part to be su(2)^a.
- **The definition fits "site frame" but not "gauge redundancy."** The report's own §1(i) lets each Γ_v(g) act on several sites near v. O1 says nothing about that case.
- **The landed note shows the gap.** `DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_…_2026-09-24` builds V = diag(Ω_L, Ω_R) on C^N_L ⊕ C^N_R and encodes SU(3) in three qubits. Even its two-qubit SU(2) link breaks the site-factor premise. Write V = P₀⊗Ω_L + P₁⊗Ω_R. Then V(σ_x⊗1)V† = |0⟩⟨1|⊗Ω_LΩ_R† + h.c., which is not a site factor unless Ω_LΩ_R† is a scalar (EXACT).
- **"Frame change of a composite" is ambiguous.** The composite algebra M_8 has automorphism group PU(8), which contains SU(3). The word "site" is load-bearing.
- **The "electroweak shape" remark is not EXACT.** The U(1) in U(2) acts trivially on the site algebra, whose automorphism group is PU(2) ≅ SO(3). That remark should be labelled ARGUED.
- **Correct headline:** SU(3) never acts by on-site (factor-preserving) frame changes; any SU(3) acting on qubits must entangle the qubits inside a carrier of at least 3 qubits. This agrees with O4 and R3.

**O2 (fixed-basis records allow only abelian redundancies): HOLDS as a conditional.**
- It needs record projectors to commute with Γ as operators. A weaker reading, unchanged statistics on gauge-invariant states, is satisfied by any G and makes O2 vacuous.
- The fixed product basis is a supplied input, not axiom content. The Qubit axiom says "No possibility is privileged". The landed triality note says the axioms "do not supply … a preferred measured basis."

**O3 (graph-first SU(3) is a commutant that moves record-visible content): HOLDS WITH NARROWED SCOPE, and partly misaimed.**
- **What the notes claim.** The integration note claims algebra only: "the joint commutant is `gl(3) \oplus gl(1)`, with compact semisimple part `su(3)`", and that this "closes the structural `SU(3)` hole." It says nothing about records.
- **Where the redundancy claim lives.** It is in the fibre-frame bridge. That note is scoped to "the registered weak/Record-sector data currently present in the cited authorities". It cites `MINIMAL_AXIOMS_2026-06-05` and disclaims any "theorem saying future colour-readout contexts cannot register additional fibre data." So O3 is a re-reading under the 2026-06-29 axioms, not a refutation within the notes' own scope.
- **X_μ is mislabelled.** The corner shift belongs to the weak su(2), not to su(3). The su(3) generators do still move content between base corners, for example by mixing the |00⟩ and |11⟩ base points.
- **Wrong carrier size.** The bridge puts V_x = C²_weak ⊗ C³_fibre (6 states) at each site, not C^8.
- **"Fails (b)" is overstated.** It holds only if those carrier sites carry records. The report's own R3 escape uses carriers that are never recorded.
- **Labels should split.** The algebra is EXACT; the identification of corners with record-bearing sites is ARGUED.
- **The selector point holds (EXACT).** I re-derived Tr H⁴ = 8(|φ|⁴ + 4Σφ_i²φ_j²), so V_sel = 32Σφ_i²φ_j². It is ≥ 0 and zero on the axes. Choosing the axes requires the supplied sign "minimise"; maximising gives the S₃-symmetric point.

**D10 (structure group (SU(3)×SU(2)×U(1))/Z₆): HOLDS.**
- **Kernel.** Suppose A⊗X = 1. Then A = μ·1 and X = μ⁻¹·1, with μ = ±1. From z⁻³ = μ⁻¹ we get z³ = μ. From B₀ = μ⁻¹z⁻¹·1₃ we get B₀ = z⁻⁴·1₃ = z²·1₃ once z⁶ = 1. Then det B₀ = z⁶ = 1. The converse also checks, so the kernel is Z₆ (EXACT).
- **Dimension.** The group of all A⊗(B⊕c) is 13-dimensional; requiring det = 1 leaves 12. The image of SU(2)×SU(3)×U(1) has finite kernel and dimension 8+3+1 = 12, so it is the identity component.
- **The full group has a second component.** 1⊗diag(1,1,1,−1) has det = 1 but is not in the image (it would need both z³ = μ and z³ = −μ). The label det(A)²·det(B)·c = ±1 separates the two components. The brief and summary line 4 drop "identity component"; D10 keeps it.
- **What the U(1) is.** Tracelessness fixes it uniquely, with ratio −3. That makes it B−L (+1/3 on 6 states, −1 on 2), which equals 2Y on left-handed doublets only. The group is isomorphic to the SM global form as an abstract group; it does not give the hypercharge assignment.

**Lemma 1 (a Gauss-conserving electric factor is central): HOLDS for single-link operators.**
- The proof (Peter–Weyl plus Schur) and the condition T_ν R_h = R_h T_ν ⇔ ν Ad-invariant are both correct.
- It fails for multi-link electric terms. A term E_l^a E_{l'}^a on two links that share a vertex respects the Gauss law but is not central link by link. "Configuration-independent" has to mean "a product of single-link factors."
- The re-reading of the landed drifted step as covariant but not invariant is a correct sharpening, not a contradiction of that note.

**Lemma 2 (the half-turn makes τ real): HOLDS under S4.** The map (x,y,z) ↦ (1−x, −y, z) reverses the bond. W = U⁻¹ turns a right step into a left step with law ι_*ν. Centrality then gives ν = ι_*ν, so τ is real.

**D5 (Hunt's theorem): HOLDS, conditional on unstated premises.**
- **The theorem is applied correctly.** The formula ψ = Σc_i C₂^(i) + q(λ_Z) + ∫(1 − Re χ_λ/d_λ) dΠ is right for symmetric central semigroups. Π = 0 is equivalent to continuous paths and to HK.
- **S3 must also state:**
  - every w_s is a probability density for all real s ≥ 0, i.e. infinite divisibility plus embedding in a continuous semigroup;
  - ν_s → δ_e as s → 0.
- **Why it matters.** Composition over integers (time steps, plaquette counts) puts no constraint on w at all. The positive-maximum-principle step that excludes C₂² generators uses that positivity.
- **Summary line 7** ("under composition closure …") leaves both premises out.
- **Notation.** "Poisson jumps" should read "Lévy jump part (possibly infinitely many small jumps)", and ⊗ should be ∗ (convolution).

**D6 (U(1) Wilson is pure jump with c = 0): HOLDS for U(1). The SU(2) part is mis-scoped.**
- **The general argument holds (EXACT).** c = lim ψ/C₂ follows from the bound 1 − Re χ/d ≤ C₂|X|²/(2 dim g) plus dominated convergence.
- **U(1).** ψ ~ n log n, so c = 0. Kent supplies infinite divisibility. Embedding on the circle is standard (ARGUED). So U(1) Wilson is pure jump.
- **SU(2) is probably not open.**
  - Kent 1977 proves infinite divisibility of von Mises–Fisher laws "for all values of the parameter in all dimensions". A secondary source says the proof uses ultraspherical expansions and Bingham's (1972) convolution on [−1,1], which comes from rotationally symmetric random walks on spheres.
  - On S³ ≅ SU(2), that zonal convolution is exactly central convolution on SU(2). The proof: lift a class function to f(g₁g₂⁻¹) on SU(2)×SU(2), then substitute a = h₁h₂⁻¹ (EXACT). The spherical functions C_n^(1)(cos θ)/(n+1) are the normalized SU(2) characters χ_{n/2}/d (EXACT).
  - The von Mises–Fisher law on S³ with κ = β is the SU(2) Wilson weight exp((β/2) tr U), relative to Haar measure (EXACT).
  - So SU(2) Wilson is very likely infinitely divisible for every β, which would make it pure jump with c = 0. This is LIT, unverified: I could not read Kent's text or his exact dimension range.
- **SU(3)** remains open; SU(3) is not a sphere.
- **The headline overreaches.** "At finite β the action-form question is jump against diffusion" (summary line 8) is stated for all groups. It should be scoped as below.
- **"They agree at t = 2/β" is asymptotic.** From the Hankel expansion, log(I_{2j+1}/I₁) = −C₂(2/β + 1/β²) + O(β⁻³) (ARGUED). Departures from Casimir-linearity start at β⁻³.

**Constituent expansion: HOLDS.**
- I recomputed τ = m_j/((2j+1)m₀) with m_j = (2j+1)/(n+j+1)·C(2n, n−j). This reproduces the report's closed form. Spot checks: τ(1) = 1/3 at n = 1; τ(1) = 1/2 and τ(2) = 1/10 at n = 2.
- Taylor expansion term by term gives:
  - the endpoint terms: −jx + (j²+2j)x²/2 − (j³+3j²+3j)x³/3;
  - the product: −j²x + j²x²/2 − (j⁴+j²)x³/6.
- Summed: log τ = −C₂/n + C₂/n² − (C₂ + C₂²/6)/n³ + O(n⁻⁴). The first two terms are confirmed, and so is the third (EXACT).
- The series equals −C₂/(n+1) − C₂²/(6n³), i.e. HK at t = 2/(K+2) to this order.

## Required corrections
1. Restate O1 for on-site (factor-preserving) frames. Add that SU(3) needs entangling action on composite carriers of at least 3 qubits, and cite the landed SU(N) link note. Relabel "electroweak shape" as ARGUED.
2. In O2, mark the fixed record basis as a supplied input and state the operator-level readout condition.
3. In O3:
   - quote the notes' actual claimed scope;
   - fix the X_μ attribution;
   - correct C^8 to C²⊗C³ per site;
   - make "fails (b)" conditional on recorded carriers;
   - split the labels (EXACT algebra, ARGUED identification).
4. In summary line 4, say "identity component", and note the second component.
5. Restrict Lemma 1 to single-link factors.
6. Add positivity, embedding and continuity at s = 0 to S3 and to summary line 7.
7. Scope the jump-against-diffusion dichotomy: it holds for U(1); for SU(2), very likely holds via Kent's 3-sphere case (pending a read of Kent); for SU(3), it depends on the outcome of the follow-up test C1. Before running C1's SU(2) arm, check Kent's 3-sphere case. If it is confirmed, the SU(2) arm becomes a control and the only open target is SU(3).

## Bottom line
The calculations hold: D10, both lemmas, Hunt's formula, the c-limit, and the constituent series (re-derived to third order). The problems are scope:
- O1's "SU(3) never arises" holds only for on-site frames, and both the report's own definition and the landed note include composite carriers;
- O3 re-reads the earlier notes under the new axioms rather than refuting their stated claims;
- the Lévy–Khintchine reduction leaves out its positivity premise;
- the "SU(2)/SU(3) open" framing is likely half wrong: SU(2) is very probably settled by Kent 1977 through the 3-sphere, and only SU(3) is genuinely open.

Sources:
- [Kent 1977, Proc. LMS s3-35](https://academic.oup.com/plms/article/s3-35/2/359/1579223)
- [Baringhaus–Grübel, arXiv 2301.03870](https://arxiv.org/html/2301.03870)
- [Bingham 1972, Random walk on spheres](https://link.springer.com/article/10.1007/BF00536088)