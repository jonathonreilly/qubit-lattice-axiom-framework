# C5 R16-8 report: Wall W7. Is the off-box gravity tail physical?

**Author.** Claude Opus 5.5 probe (the same model family as the supervisor and every C5 worker). **Unrefereed.** Ran 2026-10-12 from 23:05Z to about 23:30Z. No repository file was edited. No downloads and no web lookups; every literature item is RECALLED.

**Scratch.** `S/` = `.../scratchpad/C5/R16-8/`. Scripts and outputs are in `S/scripts/`. Each runs in under 5 s at `OMP_NUM_THREADS=2`.
- `r168_jets.py` / `.out` (script A): where the off-box Killing defect sits, for four matter laws in d = 3; whole-zone v_max; ray tests.
- `r168_kernel.py` / `.out` (script B): the tail kernel in real space, its gauge-invariant curvature, and the TT/Kill independence check.
- `sublum_copy.py`: R14-1's S(b) and G(b) symbols, copied unmodified from `scripts/C5/R14-1/sublum.py`.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS` and `SUMMARY` are files in `P/`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full.
- `vR12-1` = `P/agents/C5_R12-1_referee_verdict.md`. `vR13-4` = `P/agents/C5_R13-4_referee_verdict.md`; the full referee text is `P/agents/C5_R13-4_referee.md`.
- `vR16-5` = `scratchpad/C5/ref_R16-5/REFEREE_VERDICT.md`. It appeared during this run: CONFIRMED WITH CORRECTIONS, OPEN.

**Read.**
- `AX`, in full.
- `TESTS`: the C5 method (`:2302-2320`); R9-9 and its verdict (`:3862-3873`, `:3939-3950`); R12-1 and its verdict (`:4335-4348`, `:4477-4485`); R13-4 and its verdict (`:4644-4664`, `:4771-4777`); R14-1 and its verdict (`:4781-4814`); RFW (`:2263-2300`); R16-8 (`:5339-5358`).
- `P/agents/`: `C5_R12-1_report.md` and its verdict; `C5_R13-4_report.md`, its verdict and the full referee text; `C5_R16-5_report.md`; `C5_S17_synthesis.md` §2.
- `SUMMARY`: §26 (`:677-714`), §17's root obstruction (`:397-413`), §20 (`:520-532`).

**Labels.**
- **proved:** complete under the stated hypotheses; unrefereed.
- **checked:** numerics here.
- **suggested:** argued, not proved.
- **reading:** interpretation.
- **comparator:** literature, RECALLED.

---

## 0. In plain words

1. **What the tail is.** R12-1's off-box tail is a Coulomb field. Its source is the matter's Poincaré defect, i.e. the edge anomaly: the "defect charge" Q_D = Σ_k ε(k)(P′(k) − 1) n_k, carried only by quanta whose momenta lie in the edge (|k_i| > b/a).
   - The tail kernel is exactly the map that solves gravity's Hamiltonian constraint (scalar curvature = source), applied to the local source D = ∇·(defect density).
   - GR uses the same map to turn a point mass into its Newtonian field. Here the source is one derivative higher, so every power drops by one: the kernel falls as 1/r^{d−1} = 1/r² in d = 3.
   - Its gauge-invariant part (curvature) falls as 1/r^{d+1}, and no allowed gauge or TT addition removes it (proved; checked).
2. **Where the tail can sit.**
   - Take the momentum generator to be the current, P = ∇(ε²/2) (R8-2/R9-9's forward value).
   - Then every off-box defect lies in brackets that contain the momentum (spatial-diffeomorphism) constraint. The singular completion can be confined there, and the Hamiltonian constraint keeps only regular completions (proved, at the Killing-jet level).
   - With zero shift, time evolution is then quasi-local. The tail acts only through which states are physical and which observables are gauge invariant.
3. **On the box the tail does nothing.**
   - With a sector-respecting placement, the defect density annihilates box states and commutes with box-sector observables. On R12-1's own physical domain (box states) the tail is inert (proved).
   - It acts only when an edge quantum is present, i.e. a quantum with lattice-scale momentum.
4. **Off the box, the decisive question is how the tail follows moving defects.**
   - Edge quanta move: the defect current is v·Δ ≠ 0 (checked).
   - Keeping the momentum constraint true under time evolution produces a new term, κ³∫ξE·(B∗Ȯ_D), with the non-local kernel.
   - Only two things can cancel it:
     - (α) a non-local term in the Hamiltonian constraint. Then the dynamics itself acts at a distance: physically non-local.
     - (β) a second singular term inside the momentum constraint. Then the dynamics stays quasi-local and the tail stays confined to the gauge generator.
   - I could not decide between (α) and (β). That needs the degree-3 algebra, which no one has built.
5. **No local "extended" formulation in the natural class.** A non-dynamical auxiliary potential with a local Gauss-type constraint can reproduce the tail only for static defects (proved). Moving edge quanta rule this out. A dynamical auxiliary field would make the constraints local, but it adds physical massless modes, i.e. it changes the physical content (suggested; the analogue of R12-6's σ for the BF photon).
6. **Relation to R16-5's P-pf1: the same root, but not the same object, and not the same price.**
   - Both come from the zone-mean anomaly −1. P-pf1 puts the anomaly into the matter's momentum symbol (a sawtooth: an axis 1/r hopping tail and a delta on the zone face). W7 puts it into the gravity generator (an isotropic 1/r² kernel).
   - Paying P-pf1 removes W7's defect for every momentum off the face (checked). Paying P50 does not repair T_pf: T_pf is a statement about the matter generator symbol, and the referee places singular generators outside its class (`vR16-5:5,25`).
   - "One anomaly, two placements" is a reading.
7. **Reading: OPEN.**
   - LOCAL-EQUIVALENT would need a constructed completion whose tail acts on no bounded gauge-invariant observable outside the light cone. That holds only on the box domain, where the tail is inert.
   - PHYSICALLY NON-LOCAL would need a refereed demonstration. No bounded gauge-invariant observable responding through the tail was constructed, because the order at which it would respond (degree 3) is unbuilt.

---

## 1. Hypotheses and classes (stated before any title)

- **H-grade (R12-1, `C5_R12-1_report.md:47-54`).**
  - Gravity fields (h, E) have degree 1 and matter bilinears degree 2.
  - The constraints are C = C₁ + C₂ + C₃ + ….
  - The registered "linear order in κ" (`TESTS:5345`) is read as **first order in the completion**: one insertion of the tail, at R12-1's degree 3. Statements at degree 3 that go beyond one insertion are labelled suggested.
- **H-grav.** R9-9's N-type CCR graviton at linear order (`TESTS:3939-3944`). This is the supplied comparator, price P-N1.
  - Gauge actions: E → E + SᵀN with gate s_ij(q) = d_i d̄_j − |d|²δ_ij; h → h + Kill(ξ).
  - Structure functions are the undeformed flat HDA, i.e. the **standard** Ward/HDA identities (H-SF, `C5_R12-1_report.md:75`). No deformed identity is used anywhere below.
  - Whole-zone v_max of the gravity symbol:
    - R9-9's d(q) = ρq + (1−ρ)2 sin(q/2): 1.0000, reached in the box only (`C5_R13-4_report.md:184`, the R8-5 symbol of the same form).
    - Script B's kernel symbol d_c = e^{iq_c} − 1 (forward difference with the midpoint phase): |∂ω| = |cos(q/2)| ≤ 1.
- **H-mat.** Free, number-conserving, one-band matter in d = 3, with m = 0.3 and ε² = m² + Σ_i u(k_i). Whole-zone v_max (script A (1), 96³ grid plus fine axis and diagonal lines):

| law | source | u | v_max (d = 3) |
|---|---|---|---|
| L-box(2.0) | R7-1/R12-1 literal box, b = 2.0, b₂ = 3.1 | s², s = ρk + (1−ρ) sin k | **4.121** (superluminal edge) |
| S(1.4) | R13-4/R14-1 odd subluminal | s² | **0.9927** |
| G(1.4) | R14-1 even gapped subluminal | g = h² | **0.9939** |
| SLAC | R16-5's P-pf1: sawtooth s = k on (−π, π) | k² | **0.9985**; the band is discontinuous across the face |

- **H-P (the momentum generator).** Two choices:
  - the hopping symbol P = s (R12-1's choice for L-box);
  - the current-aligned symbol P = u′/2 = ∂(ε²/2) (R8-2/R9-9/R16-5's forward value, `C5_R16-5_report.md:141`).
- **H-comp.** R12-1's four degree-3 completions T₀₀^{(1,E)}, T₀₀^{(1,h)}, P^{(1,E)} and P^{(1,h)} (`C5_R12-1_report.md:70-73`). "Regular" means C^∞ symbols; "singular" means anything else.
- **Excluded, and not covered below:**
  - nonlinear gravity beyond one completion insertion;
  - pair-creating matter, including pairing (as registered);
  - interacting matter;
  - qubit gravity;
  - Λ;
  - the JJ rotation-sector completion's explicit kernel (only its location is used).

## 2. Prior art (each counted once)

- **R12-1 and its verdict.**
  - Theorem K: necessity is proved. Sufficiency holds only as a local-germ statement (`vR12-1:5`).
  - Within the fixed ansatz, an off-box O(q) Killing defect needs a 1/|q| singularity, i.e. a 1/r^{d−1} tail (`vR12-1:15`).
  - The gravity gate, the JS/JJ kernels, the midpoint phases, the invariant domain and the physical sector are unbuilt (`vR12-1:5,13`).
  - P12-2 (`C5_R12-1_report.md:272`).
- **R13-4(ii) and its verdict.**
  - The tail is not a constraint basis change.
  - It makes the gauge generator non-local, conditionally on realizing the completion.
  - "No local observable is gauge invariant" is too broad.
  - Reading: OPEN (`vR13-4:18`; full referee text `C5_R13-4_referee.md:187-205`).
  - Also: §3.2(c), dressings plus regular matter redefinitions cannot remove the non-regularity (`C5_R13-4_report.md:162-166`, suggested there). And P50 (`C5_R13-4_report.md:223`; `C5_S14_synthesis.md:181`).
- **R13-4(i):** the BF photon tail is PHYSICALLY NON-LOCAL in class 𝓔. R12-6 localizes it only by adding physical modes (`vR13-4:20,22`). This is the template for §3.5.
- **R16-5 and its verdict.**
  - T_pf is confirmed for scalar single-band matter.
  - The finite-band extension is overclaimed: a six-band signed-axis counter-route exists (`vR16-5:13-17`).
  - Singular or non-local generators are outside its class (`vR16-5:5,25`).
  - The sawtooth 1/n tail and the smooth-cut failures are correct (`vR16-5:21`).
  - P-pf1 is defined at `C5_R16-5_report.md:234-238`.
- **R14-1:** the subluminal S(1.4) and G(1.4) laws; A ≤ 0 on the S/G families (`TESTS:4808-4813`).
- **R9-9:** the tree-level box graviton is exact, with an exact Ward coupling to number-conserving stress (`TESTS:3939-3944`).
- **SUMMARY §17:** the root obstruction, zone mean −β (`:397-413`). **RFW F2:** the first-jet obstruction for completions that are C¹ at q = 0. Singular and non-local completions are open there (`TESTS:2268-2280`).
- **Comparators (RECALLED):**
  - Coulomb-gauge QED as the reduction of temporal-gauge QED;
  - the Newtonian constraint solution in linearized ADM;
  - ADM charges as boundary terms;
  - Donnelly–Giddings gravitational dressings (power-law spacelike commutators of dressed operators at O(κ));
  - "hidden momentum" in field cross terms (∫E×B of a charge in a field);
  - Lieb–Robinson bounds.

---

## 3. Results

### 3.1 (a) Where the singular completion must sit (Lemma P). Proved; checked

**Statement.** Take smooth separable bands with the current-aligned generator P = ∂(ε²/2). Then:
- every SS (Hamiltonian–Hamiltonian) Killing jet vanishes identically, on the whole zone;
- every off-box Killing defect is a multiple of ε(∂_a P_c − δ_ac) = ε(Hess(ε²/2) − I)_ac;
- that defect sits only in brackets containing the momentum constraint (JS, JJ).

So the singular completions can be confined to C_j: P^{(1,E)} for JS and P^{(1,h)} for JJ. C_s's completions T₀₀^{(1,E)} and T₀₀^{(1,h)} need only be regular.

**Proof.**
1. **The SS jets vanish.**
   - [H, K_b] has symbol iε∂_bε = i∂_b(ε²/2) = iP_b. So {H, K} = P holds exactly.
   - [K_a, K_b] = x_aP_b − x_bP_a holds with the same P, so {K, K} = J holds once J is defined as x × P.
   - {H, H} = 0.
   - These are R12-1's SS jets (00, 10, 01, 11), the ones listed at `C5_R12-1_report.md:115`.
2. **The JS translation–boost jet.** [P_c, K_b] = iε∂_bP_c, so the defect is ε(∂_bP_c − δ_bc).
3. **Placement on the JS slice.** On the slice p_ξ = 0, Kill(p_ξ) = 0, so only s(p_N)·B can act (R12-1 step 1, `C5_R12-1_report.md:125`). The singular piece is therefore forced into P^{(1,E)}. The same holds for the antisymmetric p_ξ-order-1 (rotation) jets, because Kill annihilates rotations.
4. **The JJ jets** are absorbed by Kill(p)·A − Kill(p′)·A′, i.e. by P^{(1,h)}, which is in C_j.
5. **The regular T₀₀ completions** come from Theorem K's Hadamard construction for jets that vanish. This is a local-germ statement only (`vR12-1:5`). ∎

**Checked** (script A (2), (3)):

| law, P choice | ⟨P′ − 1⟩, raw 2¹⁶-point average | zone fraction with a JS defect (3D) | SS (j − P) defect fraction |
|---|---|---|---|
| L-box, P = s | −1.000000 | 0.721 | 0.347 |
| L-box, P = u′/2 | −1.000000 | 0.727 | **0** |
| S(1.4), P = s | −1.000000 | 0.907 | 0.548 |
| S(1.4), P = u′/2 | −1.000000 | **0.269** (only the transition strips 1.4 < \|k_i\| < π − 1.4) | **0** |
| G(1.4), P = u′/2 | −1.000000 | 0.895 (\|k_i\| > 1.4) | **0** |
| SLAC | 0 almost everywhere; the −1 sits in a face delta (jump 2π) | 0 | 0 |

- **Ray test** on R12-1's JS slice, max|D_JS(0, tu; k)|/|s(tu)| at t = 10⁻¹, 10⁻², 10⁻³, current-aligned P:
  - G(1.4) edge (2.6, −0.2, 0.1): 42, 420, 4225, i.e. ∝ 1/t, a singular completion;
  - G(1.4) in the box: roundoff, scaling 1/t² from a 10⁻¹⁶ numerator;
  - S(1.4) in its mirror box (s′ = −1): also roundoff. With P = u′/2, S(1.4)'s corner valleys carry no defect.
- **Whole-zone mean ⟨P′ − 1⟩ = −1 for every continuous periodic P** (proved: ∮P′ = 0). So **no continuous P removes W7.** The choice of P only moves where the defect sits.

### 3.2 (a) What the tail is: the gravity constraint's solution map applied to the defect's divergence (Lemma B). Proved; checked

**Statement.** Take a defect density with symbol Δ_cb. On the JS slice R12-1's minimal completion is

  **B_ij,c(q) = s_ij(q) D_c(q)/|s(q)|²,   D_c(q) = i q_b Δ_cb (local),   |s|² = (d−1)|q|⁴.**

1. s·B = D. So B is the minimal-norm solution of the linearized Hamiltonian constraint (scalar curvature = source) with the local source D = ∂_bΔ_cb.
   - This is the map that, in linearized GR, takes a point mass T₀₀ = δ to its Newtonian h (comparator).
   - Real-space continuum form: B_ij,c = ½[∂_c∂_i∂_j r/(8π) − δ_ij ∂_c(1/(4πr))], i.e. 1/r^{d−1}.
2. **Gauge freedom of the completion.** One may set B → B + Kill(ζ) + T with T transverse-traceless; these keep s·B fixed.
   - The linearized spatial Ricci tensor R[B] changes only by the TT tensor −½q²T, because R[Kill] = 0.
   - The contracted Bianchi identity fixes the non-TT part of R from its trace D: R^{nonTT}_ij = (D/4)(q̂_iq̂_j + δ_ij) in d = 3.
   - Its traceless part is non-analytic for every Δ ≠ 0. In real space it is a 1/r^{d+1} tidal field: −(1/16π)∂_c∂_i∂_j(1/r) for a unit defect.
   - So **the gauge-invariant content of the tail cannot be removed by any choice in the completion's freedom.** Its r^{−(d−1)} part is gauge-dependent; its curvature falls as r^{−(d+1)}.

**Checked** (script B, 128³ torus, midpoint-phase forward differences; nothing is subtracted except the q = 0 mode, which D does not have):
- r²|B| on the x-axis at r = 4, 8, 16, 24:

| component | r = 4 | 8 | 16 | 24 | continuum |
|---|---|---|---|---|---|
| xx,x | 0.0354 | 0.0361 | 0.0372 | 0.0366 | 1/(8π) = 0.0398 |
| yy,x | 0.0158 | 0.0177 | 0.0186 | 0.0187 | 1/(16π) = 0.0199 |
| xy,y | 0.0177 | 0.0181 | 0.0186 | 0.0183 | 1/(16π) |

  The residual few-per-cent deficit is consistent with torus images (it grows toward r = L/4).
- r⁴|R_xx,x| = 0.101, 0.108, 0.110 at r = 8, 16, 24 (continuum 6/(16π) = 0.119), and r⁴|R_yy,x| = 0.051, 0.054, 0.055 (continuum 3/(16π) = 0.0597).
- The trace of R vanishes off the source to 5e-17 (tr R = D is local).
- Continuum check, 2000 random q, with and without a random TT addition T: |Λ^TT R[B]| ≤ 3.3e-16, and the non-TT part of R[B + T] equals (D/4)(q̂q̂ + δ) to 8.9e-15.
- **GR control** (the point mass through the same map): r³|R_xx| = 0.0416, 0.0408, 0.0409 at r = 8, 12, 16 (continuum 1/(8π) = 0.0398).

**Reading.** The tail is a "defect-Coulomb" (Newton-type) field. What distinguishes it from GR's Newtonian field is not its shape but where it enters: GR's map acts on the *solution* h, while W7's acts on the *generator* (the kernel multiplying E inside C_j). That is R13-4(ii)'s point, now with the exact kernel.

### 3.3 (a) The Killing action of the tail lives at spatial infinity (Lemma F). Proved

- Smear the JS bracket with a constant shift e_c and a decaying lapse N_R = x_b w(|x|/R), with w = 1 for |x| < R/2.
- The singular completion contributes κ²∫(sᵀN_R)·(B_c∗Ô_c) = κ²∫N_R(D_c∗Ô_c) = −κ²Q_D,cb for every R (summation by parts; N_R has compact support).
- For |x| < R/2, sᵀN_R = sᵀx_b = 0 (second differences of a linear function). So the whole −κ²Q_D comes from the cutoff shell R/2 < |x| < R. There the integrand scales as R·R⁻²·R^{−(d−1)}·R^d = O(1), which is exactly the scaling a 1/r^{d−1} tail allows.
- **Consequence.** The completion cancels the matter's Poincaré defect, {P_c, K_b} − δ_bc H = Δ_cb, by a term supported at infinity.
- Equivalently, the total (ADM-type) momentum C_j[e_c] + boundary contains the cross term **κ²∫E·(B_c∗Ô_c)**: the gravity momentum E times the defect-Coulomb field.
- Reading (comparator): this is the analogue of the field-momentum cross term ∫E×B of a charge sitting in a field ("hidden momentum"). It is physical but carried by fields. Here the "field" B∗Ô_c is not an independent degree of freedom, which is the whole issue.

### 3.4 (a) The physical domain. Proved on the box; off the box, characterized

- **Placement (Lemma S, proved within Theorem K's local germ).**
  - Only the forward value Δ(k) of the defect density is fixed by the Killing jets. The off-diagonal values are non-Killing and absorbable by regular completions.
  - So one may choose a sector-respecting density, F(k, k′) = −√(ε(k)|A(k)| ε(k′)|A(k′)|) per component, with A = Hess(ε²/2) − I ≤ 0 on the S/G families (`TESTS:4812`). Then F vanishes unless both momenta carry a defect.
  - Then Ô_D annihilates every state whose quanta all lie where A = 0. That is the plateau for G(1.4), and the plateau plus the mirror boxes for S(1.4) with P = u′/2.
  - Ô_D commutes with every observable built from those modes.
  - **On R12-1's box domain the tail is inert:** {C_j[ξ], O_box} has no tail term, and neither does the gauge variation of the linear curvature on box states.
  - Smoothness caveat: √(flat Gevrey function) is smooth for the exp(−1/x) steps used, but not for every flat function. This is stated for the R14-1 steps only.
- **Off the box (checked, script A (4)).**
  - Each edge quantum carries defect charge Δ_cc = ε(P′ − 1). Examples:
    - G(1.4): −4.71 at k = (2.0, 0.3, 0.2); −6.91 at (2.6, 0.1, −0.4); −0.085 at (1.6, 1.6, 0);
    - S(1.4), P = u′/2: −39.2 at (1.6, 1.6, 0) in the strip; 0 in the mirror box.
  - The quanta move at the group velocity (|v| = 0.23–0.99), so the defect current J_D = vΔ ≠ 0.
  - Such quanta have some |k_i| > 1.4/a, i.e. ≳ 1.7e19 GeV at a = ℓ_P (reading).

### 3.5 (a) A local extended formulation without new physical modes does not exist for moving defects (Lemma A). Proved in class 𝒜

**Class 𝒜.** Extensions by an auxiliary potential φ_c (any finite number of components per site) with:
- a local Gauss-type constraint Γ_c = (d−1)Δ²φ_c − ∂_bÔ_cb ≈ 0;
- the tail replaced by the local term E·sᵀφ_c (on Γ = 0, sᵀφ_c = B_c∗Ô_c exactly, since s·sᵀ = (d−1)Δ²);
- no physical degrees of freedom in (φ, π): π is pure gauge or absent;
- a quasi-local extended Hamiltonian.

**Statement.** In 𝒜, Γ is preserved by the evolution iff ∂_bȮ_cb = (d−1)Δ²V_c for some quasi-local V_c, with V_c the φ-velocity. That fails whenever the defect moves.

**Proof.**
1. Γ̇_c = (d−1)Δ²φ̇_c − ∂_bȮ_cb.
2. φ̇ = ∂H_ext/∂π. A quasi-local H_ext gives a quasi-local φ̇ = V.
3. The equation therefore needs ∂_bȮ_cb = −∂_b∂_aJ_{a,cb} ∈ Δ²(quasi-local). The required V = −Δ^{−2}∂∂J/(d−1) has a degree −2 symbol, i.e. a 1/r^{d−2} kernel, unless ∂∂J vanishes to fourth order at q = 0 for every state.
4. For one moving edge quantum, J(q) → vΔ ≠ 0 at q → 0 (checked, §3.4). So V is non-local.
5. A Γ-multiplier cannot help: Γ contains no π, so ∫μΓ does not move φ. ∎

**Outside 𝒜 (suggested).**
- Giving φ a conjugate and a local kinetic term, i.e. a second tensor field (b, e) with s·b = D and ∂·e = (defect current), the way GR's (h, E) pair transports T₀₀ by ∂·E = P, would make every constraint local.
- But b and e then carry TT components: new massless physical modes coupled to Q_D.
- This is the same fork as R13-4(i), where BF is non-local and R12-6 is local only with new σ, η modes.

### 3.6 (a) The degree-3 transport condition (Lemma D). Suggested (bookkeeping at one completion insertion; not a closed computation)

- Use Lemma P's placement, zero shift, and H = C_s[1] + boundary. The HDA gives {C_j[ξ], C_s[1]} = C_s[ξ·∂1] = 0, so C_j must be preserved weakly.
- The bracket {−κ²∫ξ_cE·(B_c∗Ô_c), −κH_m} produces the E-linear, matter-bilinear term **κ³∫ξ_c E_ij (B_ij,c∗Ȯ_c)**, with Ȯ_c = −∂·J_D. Its kernel B∂ has degree 0 and is non-analytic (a 1/r^d kernel).
- The other degree-3 contributions are:
  - {S(h)[1], ·}: zero, because sᵀ(1) = 0;
  - brackets with the regular C_s completions: local;
  - {gravity quadratic, E·B∗Ô}: h-linear, not E-linear;
  - {½E², P^{(1,h)}}: E-linear;
  - {G(E)[ξ], C₄_s}: E-linear if C₄_s ∋ h·E·matter.
- So the non-local E-linear term can be cancelled only by:
  - **(α)** a non-local h·E·matter completion at degree 4 in C_s. Then H = C_s[1] is non-local and the tail acts dynamically. A bounded observable would then respond instantaneously; the expected size (reading) is κ²|E||Q_D|/(8πr²) per edge quantum. Or by:
  - **(β)** a singular h-linear completion P^{(1,h)} ∋ κ²∫ξ_c h·(B_c∗Ȯ_c) in C_j. Its bracket with ½E² gives the cancelling E-linear term. H stays quasi-local and the tail stays inside the spatial-diffeomorphism generator, transported "covariantly" with the defect current.
- Whether (β) is compatible with the JJ Killing jets, which also need a singular P^{(1,h)}, and with the remaining degree-3 brackets is **not determined**. That is the unbuilt sector named in `vR12-1:5,15` and `vR13-4:18`.

### 3.7 (b) The R13-4 criterion

- **Box-sector observables (proved, under Lemma S's placement).** They commute with Ô_D and with Ȯ_D. They do not respond through the tail at all, at any distance.
- **Gravity observables.** Candidates:
  - the smeared momentum-constraint left side ∂·E[f_x] (invariant under both linear gauge actions, since ∂·sᵀN = 0 and E does not move under Kill);
  - the linear curvature R^{(1)}(h)[f_x].
- At the tail's order:
  - R^{(1)}(h)(x) has the gauge variation κ²R[ξ·(B∗Ô)](x). It is non-zero when an edge quantum is present, so the observable is not gauge invariant there.
  - On physical states, ∂·E(x) = κP(x) + κ²E·(B∗Ô)(x). Its value depends on a distant edge quantum at size κ²|E(x)||Q_D|/(8πr²). This is kinematic, constraint-type dependence, like a field cross term.
  - Its gauge invariance at that order depends on the singular P^{(1,h)}, which shifts E. That is again the unbuilt sector.
- **Instantaneous dynamical response** occurs in (α) and not in (β) (§3.6).
- So the registered test (a *bounded gauge-invariant* observable responding *instantaneously* at ∝ r^{−(d−1)}) cannot be decided at the order built.
- **Size, if (α) holds (reading).** At a = ℓ_P and r = 1 m (6.2e34 ℓ_P), with |Q_D| ≲ 40/ℓ_P per edge quantum, the kernel factor |Q_D|/(8πr²) is ≲ 4e-70 in Planck units, times κ²|E|.
  - The source exists only for lattice-momentum quanta.
  - With number-conserving matter there is no vacuum population. Pair-creating loops (excluded here) would run over the edge, as in R9-9's Theorem T.

### 3.8 (c) Relation to R16-5: T_pf, the sawtooth symbol and P-pf1

- **The same root (proved).** Both are the zone mean ∮(P′ − 1)dk/2π = −1 (`SUMMARY:397-413`). Script A (2) gives −1.000000 for every continuous periodic P and 0 almost everywhere plus a 2π face jump for the sawtooth.
- **Not the same object (proved, by form).**

| | P-pf1 (R16-5) | W7's tail (P50) |
|---|---|---|
| where | the matter's one-body generator (hopping) | the gravity gauge generator C_j: the kernel multiplying E |
| real-space form | 1/r along each lattice axis, Fourier coefficients exactly 1/n (`C5_R16-5_report.md:178`), raw | isotropic 1/r^{d−1} = 1/r² (d = 3), coefficients 1/(8π), 1/(16π) (§3.2), zero mode removed |
| gauge-invariant part | the matter law itself (non-local hopping) | curvature 1/r^{d+1}, fixed by Bianchi (§3.2) |
| extra conditions | vertices never straddle the face (no umklapp); dilation/shear moments fail at the cutoff (suggested there) | degree-3 transport, (α) or (β) (§3.6) |
| whole-zone v_max | SLAC 0.9985 (d = 3, m = 0.3) | the matter law's own: S(1.4) 0.9927, G(1.4) 0.9939; graviton 1 |

- **Alternative payments, not the same payment.**
  - **P-pf1 pays W7 at degree 2 (checked).** With SLAC matter every Killing jet vanishes off the face, so R12-1's ray test is at roundoff (≤ 7.3e-10) at all four sampled k, including k₁ = 3.1, for t ≤ 10⁻². It is 1.4e3 only when the step crosses the face (t = 10⁻¹ at k₁ = 3.1). So regular completions suffice on states supported off the face. The face delta remains, and the no-umklapp condition carries over.
  - **P50 does not pay T_pf.** T_pf is an identity on the number-conserving matter generator at the zeroth moment; W7's completion is E-linear (degree 3). The referee places singular and non-local generators outside T_pf's class (`vR16-5:5,25`). So whether a W7-type generator evades T_pf is OPEN. That it does not is suggested, for the grading reason just given.
- **Reading.** "One anomaly, two placements":
  - In the covariant HDA setting, P50 leaves the matter law local and moves the anomaly into a gauge-generator tail.
  - In the preferred-frame setting, only P-pf1 is on record.
  - They are not the same price. P-pf1 buys both walls at degree 2, but at the cost of a non-local matter law. P50 buys only W7, and only if (β) holds is it harmless to the dynamics.

### 3.9 (d) Prices (named, not adopted)

| price | content | axiom touched | buys |
|---|---|---|---|
| **P50 (refined)** | Singular completions confined to the spatial-diffeomorphism generator (Lemma P, with current-aligned P). Kernel = the constraint solution map of ∇·(defect), 1/r^{d−1}, with gauge-invariant curvature 1/r^{d+1}. Inert on box states (Lemma S). Harmless to the dynamics only under (β) | Admissibility `AX:57-58` (range of the rule) | degree-2 closure off the box |
| **P-W7α** | The non-local Hamiltonian-constraint completion of (α): instantaneous dynamics at 1/r^{d−1} through edge quanta | `AX:57-58`; dynamics is downstream (`AX:116-123`), so this is also a P-dyn price | degree-3 preservation of C_j |
| **P-W7aux** | A dynamical auxiliary tensor field transporting the defect locally. New massless modes coupled to Q_D change the physical content | Qubit `AX:47` (extra fields), plus new particle content | local constraints |
| **P-pf1 (alternative payment)** | Sawtooth/SLAC matter momentum. Removes W7's defect off the face. Face delta and no-umklapp | `AX:57-58`, `AX:187` | W7 at degree 2 and T_pf |

---

## 4. Against the FIXED readings (`TESTS:5354-5357`)

- **LOCAL-EQUIVALENT: not met.**
  - A completion whose tail acts on no bounded gauge-invariant observable is shown only on the box domain, where the tail is inert (Lemma S).
  - Off the box, no completion is constructed beyond the degree-2 local germ.
  - In class 𝒜 a local extension is excluded for moving defects (Lemma A).
- **PHYSICALLY NON-LOCAL: not met.**
  - No refereed demonstration exists, and none is claimed.
  - The worker found no bounded gauge-invariant observable responding through the tail at the order built. The response exists in option (α) and is absent in option (β), and the degree-3 sector that decides between them is unbuilt.
- **Worker reading: OPEN.**
  - New bounded results: Lemmas P, B, F, S and A (proved), Lemma D (suggested), and the location, shape and size of the tail (checked).
- **Against the expectation** ("OPEN or PHYSICALLY NON-LOCAL, with the same price as P-pf1", `TESTS:5358`):
  - OPEN: as expected.
  - "The same price": **not so.** It is the same root, an alternative payment, and a different object (§3.8).

## 5. Strong-word check

- **"Proved":**
  - Lemma P (Killing-jet location; the regular T₀₀ completions only as a local germ);
  - Lemma B (solution map; Bianchi-fixed curvature; TT/Kill independence);
  - Lemma F (summation by parts);
  - Lemma S (within Theorem K's placement freedom; smoothness stated for the R14-1 steps);
  - Lemma A (class 𝒜 only);
  - ∮P′ = 0 for continuous periodic P.
- **"Checked":** every number in §1, §3.1, §3.2 and §3.4, and the SLAC ray test.
- **"Suggested":**
  - Lemma D and its (α)/(β) dichotomy;
  - the auxiliary-tensor route outside 𝒜;
  - "P50 does not pay T_pf".
- **"Reading":** "defect-Coulomb field"; the hidden-momentum analogy; "one anomaly, two placements"; the sizes at a = ℓ_P.
- **"Exactly":** used only for s·B = D, the SS jets under current-aligned P, and the 1/n sawtooth coefficients (quoted from R16-5).
- **Tails and subtractions:**
  - script B removes only the q = 0 mode, which D does not have;
  - script A uses raw symbols and raw 2¹⁶-point averages;
  - R16-5's 1/n is raw.
- **v_max:** stated for every law (§1).
- **Ward/HDA:** the standard (undeformed c-number) HDA throughout. No deformed identity is used.
- **Not claimed:** anything at degree ≥ 4; interacting or pair-creating matter; qubit gravity; the JJ completion's explicit kernel; a finite-band T_pf statement.

## 6. For the referee

1. **Lemma P.** Is current-aligned P = ∂(ε²/2) an admissible momentum generator in R12-1's ansatz? Is the forced placement on the p_ξ = 0 slice (only s(p_N)·B acts) correct for every JS Killing jet, including the rotation–boost ones?
2. **Lemma B.** Check the minimal B and the Bianchi decomposition R^{nonTT} = (D/4)(q̂q̂ + δ) in d = 3, and rerun `r168_kernel.py`.
3. **Lemma F.** Is a decaying-lapse regularization the right reading of R12-1's Killing jet, and is the shell-support argument complete?
4. **Lemma A.** Is class 𝒜 a fair reading of "local extended formulation" (R13-4's definition, `TESTS:4652`) for (ii)? Is the multiplier remark (Γ contains no π) sufficient?
5. **Lemma D.** Is the degree-3 bookkeeping complete at one completion insertion? In particular, can (β) be ruled in or out against the JJ Killing jets?
6. **Lemma S.** Is the sector-respecting placement smooth and cubic-covariant for the R14-1 S/G families?

## 7. Files

All in `S/scripts/`:
- `r168_jets.py` / `.out`:
  - (1) whole-zone v_max;
  - (2) zone means and defect fractions for both P choices;
  - (3) R12-1-style ray tests at four k per law;
  - (4) edge defect charges and velocities.
- `r168_kernel.py` / `.out`:
  - (1) r²B on the axes and the diagonal;
  - (2) r⁴ Ricci and its trace;
  - (3) TT/Bianchi independence (continuum, 2000 random q);
  - (4) the GR point-mass control.
- `sublum_copy.py`: R14-1's symbols, unmodified.
