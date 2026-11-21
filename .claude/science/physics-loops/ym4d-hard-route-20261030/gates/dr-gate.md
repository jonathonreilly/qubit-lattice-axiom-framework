First failing step: none

# DR gate: pass-3 referee of library/dr.md (610 lines)

Text read once, line by line: `library/dr.md`. The draft `dr-draft.md` was read only where the text points to it (Lemma 2.4 at draft L130, the NL remark at draft L584, the order row at draft L563). Frozen texts checked at the cited places: st1-r4 §2 (L122–160), Lemma 6 (L345–494), L1467–1471, L1543; nl1-L L80–85 and L159–174; p82 §§1–4 (L60–188, L190–540); cp12 D5, Lemma 5, Lemma 6, Theorem 7 (L174–345), Theorem 2 (L51–62); in1 rows 1–10 and Amendment 1 (L221–236, L666–676); descent L5–7, L52, L275. SA lines read: 5602–5609, 5762–5803, 5880–5887, 9598–9606, 10380–10392, 10560–10578, 12385–12392, 12438–12450, 12753–12758. CA index: `sa-index/ca-4.12-4.19/README.md` L10 and chunk-06 L43–52.

## Steps checked and found correct

- **(4)–(5) against ST1 (40)–(43).** Put H=ℓ, H_1=ℓ_1, M^walk=Σ, â=a_0I, K_0=Q̂. Then h=α−HC(h) is T=L(A′). The derivative of ST1 (41) has exactly the five terms of (4). Two facts are used: Σ is symmetric, and R_F′=N_0. The outer equation is (42): α=ℓ_1B′−𝔊W_1(α). The current (5) is (43), since E_h^T=f(−iη ad h)=f_h. This uses (ad h)^T=−ad h in the bilinear trace pairing.
- **(7) and the bare counterexample, checked by hand.** At U=I, Ω_1=∅, every bond is a bare row. Then Q′=I, R=0 and K_0=ηI, with K_0^T=η^{-3}I (P82 Lemma 3). Also C=0, so H=H_1=η^{-1}I and 𝔊=0: the slice ker Q̂ is {0}, and ℓ_1Q̂G_1=G_1. Hence h=η^{-1}S and F′(0)=0. Since K_0^TH^T=I, j−j^F=(f_h^{-1}−I)J. On span{σ_1,σ_3}, z=−i ad(εσ_2) gives zσ_1=−2εσ_3 and zσ_3=2εσ_1, so z=2εJ_2 with J_2²=−I. Multiplying (ε cot ε−εJ_2)(e^{2εJ_2}−I) gives 2εJ_2, which confirms (8). The σ_3 coefficient is δ_0ε≠0. This agrees with ST1 (35): changing the current by δ changes K by f_H^{-1}δ−δ.
- **drlocp L69.** drlocp L69 does **not** assert that the two currents are equal. Its words are: "There is no supplied reason for (8) to vanish." So the brief's phrase "drlocp L69 is false" is not right. The step that fails is assembly-status item 4 (L185), which asks for "the two-current identification of drlocp L69". dr.md disposition 4 (L587) says exactly this.
- **Which current the frozen consumers read.** ST1 reads (43) (L463–471). NL1-L H-DR (7) bounds n_b(h) with l_+^3|K| (L82, L165), where K is ST1's DR current. TD R (unfrozen) reads n_b(H,K). CP12 L60, "At the reference, λ_0=H^TF′(0)", is on the physical locus, where the two currents agree. It is not an off-locus consumer.
- **Lemma 1.** O1D hypothesis (P) (o1-decoupled L116) and Lemma P's r_1=16L³M_1+4L (L120) are quoted correctly. The torus-lift argument is correct. A set of diameter less than one side meets at most two closed intervals in each coordinate, so at most 2⁴ cubes. The n_b stencil lies in the max-norm 2η-cube. Its diameter 4η is less than Mξ_{i−1} exactly when M>4, which repairs draft Lemma 2.4 (M≥4). A box of cubes is face-connected.
- **Lemma 3.** The margins are drlocp (16)–(17) (drlocp L150–170): 3L²M_1<(4L²−5/2)M_1. Also L(ρ_B+r_g)<(4L²−3/4)M_1, by M_1≥16Lr_g, and (33/8+21L/4)<4L². The Neumann form of d_s′^T is correct. The vanishing, splicing and holomorphic-section arguments are correct under ABS and existence/uniqueness in common balls.
- **Theorem 4 and (9).** Put b=‖S‖ and R=2Bb.
  - Contraction constants: the outer constant is 2C_WB⁴b≤2C_Wc_*≤1/8, and the inner constant is 4C_CB²b≤1/4.
  - Domain: 4Bb≤r_0/B, since b≤c_*B^{-4} and c_*≤r_0/4.
  - (11): 1+1/8 gives 8/7, and 4/3·8/7=32/21<2.
  - Multiplier smallness: 8C_RTBb≤1/4 needs b≤(32C_Rt_0b_0)^{-1}e^{-32κ̄}. Rows needs 4Bb≤r_R, that is b≤r_R/(4b_0)e^{-16κ̄}. Both follow from s_D=ε_De^{-64κ̄}.
  - Constants: B(1+T)²≤b_0(1+t_0)²e^{48κ̄}, so E=e^{48κ̄}, c_D=64, and C_D is free of κ̄ and M.
  - Fit with the consumers: ST1 (16) L141 and its "ε_De^{-c_Dκ̄}" form (L142), and NL1-L (7)'s s_D (L161).
  - The weight w=e^{θd(·,supp S)} has ‖S‖_{Y,w}=b. The choice θ≤τ_L/8 is O1D Theorem B(c)'s rate. θ≤log2/D_R gives the factor 2 at each local weight comparison.
- **SA quotations.** The R9 text is SA 5762–5803. The splitting sentence is at 5795–5797 ("When s vanishes on separating cubes, the equations split..."), so dr.md's correction of NL1-L L170 (which cites 5797–5801) is right. Also confirmed: d_B at 9598–9606, b̂=Ce^{16κ̄} and the Lipschitz constant Cb̂²r at 10383–10389, and 10562–10576 asserts NL. Common lifts, 5602–5609 and 5880–5887, are as read. CP12 (11) is SA BGH5 (12438–12448), as stated at L313. The CA-I 49495ff reading matches chunk-06 L48–52.
- **Lemma 5.** Insert A=v, C=a in ST1 (37). The direct-v terms give E_0a. The endpoint terms give ⟨λ_v,Y_a⟩, with the ½ retained. The Dλ_v term gives Z_a. Here R is symmetric and is the same orthogonal projection onto Δ_U ker Q′ for either top mass (P82 Lemma 2). Hence G′R=S_scR and RG′=RS_sc. The start-point curl (18) was re-derived by expanding the four terms: only Ad(U_μU_ν)−Ad(U_νU_μ) at x+μ+ν survives. In (17), Π Dχ=0 follows from ST1's λ_{Dχ}=χ on ker Q′.
- **Lemma 6.** (21) follows from BGH5 by dyadic shells with ratio 2^{β−1}. The value bound uses the zero-sum kernel and ∫e^{−μ²t}t^{β/2−1}≤Cμ^{−β}. In the Hölder bound, the late part telescopes over about |h|/η steps and integrates to C|h|^β. In (20), the force, flux and commutator terms were checked one by one: [χg]_β≤C(Γ_β+R^{−β}Γ_0), and [Δ,χ]^T=−[Δ,χ]. The off-diagonal kernel orders and the resulting powers of R all match.
- **Lemma 7.**
  - (25): the Green-kernel bound |D^qG|≤C(|x|+η)^{−2−q} comes from q+3 integrations by parts, which leave a |p|^{−5} integrand. The harmonic part is handled by iterated Caccioppoli steps, four-coordinate telescoping and Cauchy–Schwarz.
  - Weighted maximum Φ: the absorption bookkeeping after multiplying by (d/r)² was checked term by term.
  - (22) uses only bounded flux, through CP12 (9). (23) uses [B]_β≤Ca r^{−1−β}, which follows from first-order bounds alone. (24) uses (14) through [C_0]_β and applies (20) to D_ju with the single flux f_0.
  - The proof is non-circular.
- **Theorem 8.**
  - Blocks (28): checked against P82 (21): h=Pg_1+RSg_2, ψ=SRg_1−SRSg_2, Q′SR=0.
  - (29): checked against P82's rows 2–3.
  - Dual bounds (30): checked slot by slot (field energy, ψ, Dψ, h). The amplitudes are m^{−2}, m^{−4}, m^{−3}, m^{−2}, with volume factor (M_Pm)².
  - Pieces: (31) is P82 L452–461. The S1, S3 and flux pieces use (23)/(22), which need only first-order Reg. The S2 and S4 pieces use (24), which needs Reg^{1,β}.
  - Assembly: the weighted assembly with θ≤δ_w/2=θ_0 is P82 (11) and I4. The support radius C_LM_P costs the fixed factor 2^{C_L/D_L}.
- **Theorem 9.** S_J=S_q°+diag(Δ′−Δ′_π[J],0).
  - The pieces E_0v, Y_v and Z_v are bounded by γ times S2's quantities.
  - The bounds use S1 for the Y term, then S3, S4 and (17) for the Z term. C_Uχ∈G^β, with norm at most Ca_regγ‖v‖, by (18) and Reg^{1,β}.
  - Then the Neumann series gives (34).
  - The field block on (0,b) is ℓb: Q̂ℓ=I, and the multiplier is (Σ−â)b. This was checked against ST1 (38)–(39).
  - No Hölder bound on J is used. The scope (L494, L513, L596) is exactly the first current-corrected lift H(1), for real Reg^{1,β} references and small independent current.
- **Lemmas 10–11.** The Möbius inversion is correct. The cancellation for mixed and disconnected X uses component additivity with F(∅)=0. The integral formula is repeated one-variable calculus. In WW, (36) gives the X_w bound with σ_x=m_x^{−1}. The single-cube objection to the wall matrix (L536) and the factorial-count remark (L549) are correct.
- **Order.** The order paragraph (L95) matches IN1 rows 2–5 and 9 with Amendment 1:
  - early constants, M_P, M_1, R_1, before κ (rows 2–3);
  - κ in the amended window (row 4);
  - κ̄, then ℓ_P (which needs M after κ̄), then M (row 5);
  - the coupling last (row 9).

  κ̄ enters only B, T, s_D, E_κ̄ and the ℓ_P floors. Theorems 8–9 are free of M and κ̄.

## Findings

1. **L11, L184, L189 — metric in the H-DR conversion.** The step "Since d_−≥d_+, it also gives NL1-L (7)" holds only if d_B is the old (finer) layer metric d_−, or any metric dominating d_+. L11 calls d_B "the ambient layer distance" but does not say which of the two sequences it uses. *Repairable, not fatal.* State at L11 that d_B is the main step's old layer metric, so d_B=d_−≥d_+ (ST1 L1467).

2. **L22, L36, L48, L170–189 — the name clash between ST1 (16) and NL1-L H-DR (7).** The same letters mean different objects in the three texts:
   - The pair response is (H,K) in ST1 (16), h in NL1-L (7), and 𝔥=(h,j) in dr.md.
   - dr.md's H is the linear lift, which ST1 calls ℓ at s=1. dr.md's K_0 and K_h are row derivatives, while ST1's K is the current.
   - dr.md's own equations (7) and (16) share their numbers with NL1-L (7) and ST1 (16).

   Every cross-reference carries its prefix, and Lemma 2's proof gives the correspondence implicitly, so no step is wrong. *Repairable.* Add one dictionary line at L58: "𝔥=(h,j) is ST1's (H,K) and NL1-L's h; H(1)=ℓ, K_0=Q̂." The mathematical difference between the two clauses (H-DR is the full-ball, norm-linear, current-including strengthening, NL1-L L172) is stated correctly at L586.

3. **L210–212, (12) — a factor 2.** O1D Theorem B(c) bounds **each** of its two column sums by C_H. With the weight factor 2 on each sum, the first brace term is at most 4C_RT‖h‖_{X,w}, not 2C_RT‖h‖_{X,w}. So (12) should read 8C_RT(1+Tγ_*). The text's constant holds only if T bounds the sum of both column sums. *Repairable, harmless.* Only C_D changes, inside C_conv. The radius (9) and E_κ̄ do not change.

4. **L481–483, (33) — provenance of the Hessian remainder.** a3-derivative §7.1 (L435) proves ‖Δ′v‖_F≤Cκ‖v‖_X with κ the curvature parameter. Its proof also uses the reference-current bound |J|≤CκL^{−3} (the BCH term). Reg^{1,β} alone does not bound the physical current by a_reg m^{−3}. Theorem 9 assumes (33) explicitly, so the theorem is correct as stated, but the sentence calling (33) "the input of a3-derivative §7.1" overstates the match. *Repairable.* Read (33) with a_reg replaced by max(a_reg,κ_A3). Here κ_A3 includes the real-critical current bound (P82 I6), and the smallness hypothesis becomes a_reg+κ_A3+γ≤c_♯. a3-derivative is not frozen.

5. **L91, L95, L483 — current ceiling against c_♯.** Theorem 9 needs a_reg+γ≤c_♯. For its conclusion to cover the whole §1 current ball ‖J‖_{F,1}≤γ_*, the order must also impose γ_*+a_reg≤c_♯ (both are early). The order paragraph does not say this. *Repairable, no cycle.*

6. **L34 (ONE), "â=a_0I".** ST1 L389 and L422 make â a "fixed positive diagonal" raw-row mass, not necessarily scalar. ONE requires it to be scalar, which is consistent with P82 I1 ("a^dim=I"). This is an explicit hypothesis, so nothing is wrong. If â is not scalar, the unparameterized term in (4) must be −â. *Repairable (scope note).*

## Imports: frozen and unfrozen

Frozen imports are used only as stated:
- ST1 §1, §2 and Lemma 6 (33)–(43);
- NL1-L H-DR;
- P82 Theorem P and Lemmas 1–7, with I1–I5 and I8 (I6–I7 only for actual references);
- CP12 Lemma 5 (9)–(11) and Theorem 7 with its D5 hypotheses (L243);
- descent (scope remark L221 only);
- IN1's order.

Unfrozen notes, each used only as the text states:
- **o1-decoupled:** Definition D, Theorem B(a)–(d), hypothesis (P), Lemma P, and the saddle characterization. Used in W, ONE (H(1)=ℓ), the column constant T, Lemma 1 and Lemma 2.
- **drlocp:** D, UNQ, the ABS majorants, the Theorem 1 proof, and (16)–(17). Used in Lemma 3.
- **h-walk, h-walk-fix and its gate, loc-3:** used in W.
- **dec-field:** the L171 second-jet premise and the Theorem 4.2 floor. Used in ONE and Lemma 1. Its (3.5) is only "as in" for (25), which is proved by hand.
- **pw-bridge (7.4) and §§6–7:** the 𝔊 assignment in W. The alternative PW route is named, not used.
- **nl-r9 §§3–6, (4.2):** the conditional NL supply. Theorem 4 assumes NL.
- **a3-derivative (9)–(12) and §7.1:** the provenance of Rows/Pair, and (33).
- **td.md:** a consumer only.
- **p81-crit-draft, d3-local, red, loc-4:** §6 provenance and disposition remarks only. They are not proof inputs.

Results that depend on unchecked notes:
- Lemma 1, through O1D (P);
- Lemma 2's lift identity, through O1D;
- Lemma 3, through drlocp and O1D WC;
- Theorem 4, through O1D B(c) and W, and through nl-r9 if NL is supplied that way;
- Theorem 9, through (33) from a3-derivative.

Lemmas 5–8 and 10 rest only on frozen texts plus ST1's own OPS/SLICE hypotheses.

## Verdict

dr.md proves what it claims, under its stated imports. In particular:
- the specification at one is exactly ST1 (42)–(43);
- the two currents differ, by a correct bare counterexample, and every frozen consumer reads ST1's current;
- Theorem 4 gives H-DR (7) and ST1 (16), with E_κ̄=e^{48κ̄}, s_D=ε_De^{−64κ̄} and C_D free of κ̄ and M;
- the locality and DR-locP clauses hold for this response (Lemma 3);
- the mesh-uniform flux estimates and the P82 rerun prove P^div and S1–S4;
- Theorem 9 bounds the first current-corrected lift at s=1, for real Reg^{1,β} references and arbitrary small independent current, with no Hölder bound on the current.

The six findings are all repairable, and none breaks a proof.

**The Outstanding marks are correctly placed:**
- admission (L32);
- PW (L60);
- NL (L68; a named conditional import through nl-r9);
- the uniform complex local input for Rows/Pair (L91);
- full restriction and transport (L166);
- the rest of PW at one, meaning H_1, 𝔊, complex references, and the Reg^{1,β} cell and seam supply (L515);
- WW's premises (L549).

None of these is claimed proved elsewhere in the text.

**What changes for critical-path item 4** (assembly-status L185):
- Drop "Includes the two-current identification of drlocp L69". That identification is false (dr.md Lemma 2) and not needed, because ST1 (43) is the consumed current.
- Record DR as a conditional implication. Proved: the specification, holomorphy, H-DR/(16) with the explicit E_κ̄ and s_D, component splitting, row locality and DR-locP, and the s=1 first-lift bound on the real Reg^{1,β} class.
- Open inputs:
  - PW for H_1, 𝔊, switched s and complex pairs;
  - the NL premises;
  - the complex Rows/Pair estimates;
  - pair-domain admission;
  - ABS, LIFT and S-loc;
  - solvers on every 𝒪_σ;
  - the Reg^{1,β} supply at cells and seams;
  - WW, if the Boolean route is taken.
- The node-table row (L126) may cite dr.md Lemma 3 for DR-locP with ST1's current.

Checked line by line by Claude (fresh session).
