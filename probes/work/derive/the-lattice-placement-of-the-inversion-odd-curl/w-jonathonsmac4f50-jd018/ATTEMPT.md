# The lattice placement of block 158's (1/8) ε·C for the walk's eight species

Worker `w-jonathonsmac4f50-jd018` (Claude Opus 5.5), unit `J:derive:the-lattice-placement-of-the-inversion-odd-curl:a1`.

**Provenance, disclosed.** Blocks 158 and 161 T4 are the supervisor's own derivations on this machine, in the same model family as this worker. This attempt treats their open item, "the term's placement on the lattice and what it does for the other seven species". It is not a referee of either block. It needs a referee from another family.

Sources: blocks 62, 65 and 70 read as landed on main; blocks 158 and 161 read on their pushed branches.

## 1. Statement attempted

**Setting.**
- **Walk and frame.** Block 62's framed walk H[E] = ½Σ_j{E^j·σ, S_j}. Block 158's inversion-odd curl is ε·C = ε_abc E^i_b E^j_c (∂_i e^a_j − ∂_j e^a_i), where e is the co-frame and E = e⁻¹.
- **Species.** The species at the corner A = πn of {0, π}³ has D_d = cos A_d, sense s = D₁D₂D₃ and ρ = sD (block 70, landed).
- **What a species sees.** Through the site-sign map V_n, species A sees any lattice operator P as V_n P V_n acting on its smooth envelope.
- **Placement.** A coin-scalar placement is a site potential plus symmetric hops by displacements m, with real bond weights.

**Claims** (at long wavelength, exact).

- **(i) What each species needs.**
  - By block 70 T2, species A's operator is s·H[ρEρ].
  - Block 158 T1 completes it to the comparator's operator of its own frame by adding s·(1/8)ε·C[ρEρ].
  - This compensator is N_A = (1/8) Σ_d cos(A_d) X_d, where X_d = 2ε_abc E^d_b E^j_c ∂_d e^a_j is the part of ε·C whose derivative is along axis d, and ε·C = X₁ + X₂ + X₃.
  - Equivalently, the species' effective frame ρED weights the derivatives by cos A_d, as the task's hint says.

- **(ii) Which placements serve which corners.** A hop by displacement m reaches species A with the sign Π_d cos(A_d)^{m_d mod 2}. Site potentials reach every species unchanged. So a placement serves every corner if and only if its long-wavelength weight in each displacement-parity class matches the corresponding Walsh coefficient of N_A:
  - nothing on even displacements (site, two-step), on face diagonals or on the body diagonal;
  - a total of X_d/8 on the displacements that are odd along axis d alone.

  This is unique. Within range 2 the only such hops are the nearest-neighbour hops along each axis. So the one serving placement is per-axis hops, axis d carrying the d-derivative part X_d/8 of ε·C, placed like block 65's twist hop. Its range-1 form v_d = ¼ε_abc Ē^d_b Ē^j_c (e^a_j(x + e_d) − e^a_j(x)) reproduces X_d/8 with an error of relative size ℓ⁻² for a frame varying on scale ℓ.

- **(iii) The alternatives.** These hold for independent X₁, X₂, X₃, which the lengths' own frame attains at second order.

  | placement | corners served |
  |---|---|
  | site potential (1/8)ε·C | k = 0 only |
  | face-diagonal hops with weight (1/8)ε·C | k = 0 only |
  | body-diagonal C₁C₂C₃ with weight (1/8)ε·C | k = 0 and (π,π,π) |
  | block 161's links on the bonds | k = 0 and (π,π,π) |

- **(iv) What block 161's links do to the other six species.**
  - At first order in the strain the links carry a per-axis scalar L_j = ½Σ_bc ε_jbc ∂_c η_bj. It is nonzero, although the three sum to zero.
  - So they give species A the coin scalar Σ_d cos A_d L_d = (D₁ − D₃)L₁ + (D₂ − D₃)L₂ at first order. For example, at (π,0,0) it is −(∂₃η₁₂ − ∂₂η₁₃).
  - Every species needs zero at first order, because each X_d vanishes at first order on the lengths' frame. The links therefore add a spurious first-order scalar to the six mixed species.

**HIT.** (i)–(iv): an exact answer for all eight corners. On the task's two priors:
- the site potential serves only k = 0, as the supervisor's prior 0.7 says;
- a per-axis placement serves all eight only with the ∂_d split of ε·C, not with the connection's split.

## 2. Steps

**Step 1 — the exchange rule for every hop. PROVED, CHECKED (A1).**
- U_n multiplies by (−1)^{n·x}. So the entry (p, p + m) of any hop is multiplied by (−1)^{n·(2p+m)} = Π_d D_d^{m_d}, and diagonal entries are unchanged.
- This is block 70 T1(a) extended to every displacement. It is checked on a 4³ torus for all 8 maps and 9 displacements.

**Step 2 — what a species sees at long wavelength. PROVED.**
- For a smooth envelope φ, ψ = V_nφ is species A.
- ⟨ψ, Pψ⟩ = ⟨φ, V_nPV_nφ⟩. A symmetric hop by m with bond weight w acts on smooth φ as w(x)φ(x) at leading order.
- So species A receives Σ_m Π_d D_d^{m_d} w_m + W from a placement with site part W.

**Step 3 — (i). PROVED, CHECKED (B1–B3).**
- **Species A's operator.** By block 70 T2, V_nH[E]V_n = s·H[ρEρ].
- **Its comparator completion.** Block 158 T1 is an algebraic identity valid for any invertible frame; it is checked for proper frames, and E → −E flips both sides. It completes s·H_f[ρEρ] to s·(H_f + (1/8)ε·C)[ρEρ].
- **Index computation.** Write E′ = ρEρ and e′ = ρeρ.
  - The first term of ε·C[E′] carries ρ_aρ_bρ_c ρ_i ρ_j² = ρ_i on the derivative index i (det ρ = 1).
  - The second term carries ρ_j in the same way.
  - So ε·C[ρEρ] = Σ_d ρ_d X_d, and s·ε·C[ρEρ] = Σ_d D_d X_d.
- **The split itself.** X_d = 2ε_abc E^d_b E^j_c ∂_d e^a_j collects the ∂_d terms, using the antisymmetry of ε in (b, c).
- **Checked.** B1–B3 hold exactly for four random rational frames with generic symbolic derivatives (27 symbols) at all eight corners.

**Step 4 — (ii). PROVED, CHECKED (C1, C2).**
- The eight sign patterns Π_d D_d^{c_d}, c ∈ {0,1}³, are the Walsh characters of {±1}³, and they are linearly independent.
- N_A has components only on the three characters D_d, with coefficients X_d/8.
- So p_A = N_A at all eight corners if and only if the class weights are (0, X_d/8, 0, 0) by class degree.
- The corners each alternative serves follow by expanding p_A − N_A in X₁, X₂, X₃.

**Step 5 — the X_d are independent on the lengths' frame. CHECKED (C3, C4).**
- On e = 1 + η, every X_d vanishes at first order, and ΣX_d = 2ε_abc η_ad ∂_b η_cd at second. This is block 158 T1(b).
- Three rational second-order jets give X values with determinant −480 ≠ 0.

**Step 6 — (iv). CHECKED (D1–D3).**
- The comparator's connection is ω_jab = e^a_k(∂_j E^k_b + Γ^k_jl E^l_b). The link along j has a^a_j = ½ε_abc ω_jbc (block 161 T4). Its scalar per bond direction is L_j = ¼E^j_a ε_abc ω_jbc.
- **D1.** ΣL_j = (1/8)ε·C through second order (block 161 T4(b)).
- **D2.** At first order ω_jbc = ∂_c η_bj − ∂_b η_jc, so L_j = ½Σ ε_jbc ∂_c η_bj.
- **D3.** The jets ∂₃η₁₂ = 1 and ∂₁η₂₃ = 1 give L = (½, −½, 0) and (0, ½, −½). Only D = ±(1,1,1) has zero error for both.

**Step 7 — range-1 realisation. FLOATING POINT (E1).**
- For a smooth random frame of scale ℓ = 10, 20, 40, the bond weight v_d matches X_d/8 at the bond midpoint with relative error 1.4 × 10⁻², 3.8 × 10⁻³ and 9.6 × 10⁻⁴.
- The error falls as ℓ⁻²: a central difference with midpoint frames.

## 3. Scope, and where it stops

- **Long wavelength only.** Species A is treated on smooth envelopes. The placement is characterised by its total weight per displacement-parity class; how the weight is spread over the bonds matters only at higher order in the spacing.
- **What "needs" means here.** "Needs" means the comparator completion of each species' own effective frame (block 158 T1 applied through block 70's map). It is not a claim that relabellings are kept for the six mixed species. For those species, block 62's frame coupling already differs from the relabellings' coupling at first order: landed block 68, "the relabellings coupling shows them different lengths". That question is separate.
- **Coin-vector and derivative couplings** (S-type hops) are not placements of a coin scalar and are not classified.

## 4. What would finish or extend it

- A lattice rule, at range 1, that builds the links from the lengths and splits by derivative direction rather than by the connection. Block 161's connection split fails the six mixed species at first order.
- Relabelling consistency for the six mixed species with the two-step (reach-three) coupling, which serves all eight at first order (landed block 69). One would ask whether the same per-axis split then keeps them at second order.
- Order beyond long wavelength: how the weight is spread over the bonds.

## Prior art

- Block 70 (landed): the exchange table. Its twist row, ϑ → sH[ρϑ], is exactly why block 65's per-axis twist hop serves every species. This attempt extends that to ε·C and to every displacement.
- Blocks 158 and 161 (the supervisor's, unrefereed) supply the zero-corner term and the links.
- No probes attempt on this problem existed; the claim listed none.

## Check

`python3 check.py` runs in about 15 s. Sections A–D are exact (integers, sympy); section E is floating point and labelled as such. It prints `SUMMARY: PROVED …` and `HIT: …`.
