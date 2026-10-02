I've finished the synthesis (derivation only: nothing run, no files written). It answers the six questions and accounts for both hostile reviews.

**Headline.** The candidate as you framed it is not the best version. Lane B's staggered singlet mass breaks the odd translations, and those are the symmetry that forbids a light-to-mirror Dirac mass. Keeping full translations and gapping all five non-light corners by interactions gives a candidate that is stronger on every count I could check: one tuning instead of two or three, and a higher-order leak into the light modes. Whether the gapped phase exists in 3+1D is still not shown.

# Synthesis: three light chiral generations on the coin carrier (Lane B + Lane C)

**Labels.** EXACT = proof given here; CHECKED = finite hand evaluation; ARGUED = reasoning, unverified; LIT = abstract or search summary fetched this session, never used as a premise; LANDED = on origin/main `0485dc0738`; [S] = supplied piece.

**Sources read.**
- Both lane REPORTs and both REVIEWs.
- On main:
  - the axiom memo ("standard translations, and proper cubic rotations about each site");
  - the 09-22 scalar-hop note;
  - the 09-22 what-can-gap-the-walk note, T1 (corner orbits 1, 1, 3, 3; any translation-invariant symbol is scalar at a corner);
  - the 09-14 Spin(10) atomic-gaps note, §1.
- LIT: Golterman–Shamir arXiv:2603.15985, Wang–Wen arXiv:1809.11171 and García-Etxebarria–Montero arXiv:1808.00009 (abstracts); Wang–Wen–Witten arXiv:1810.00844 (search summary).

## 0. What the reviews change

- **The carrier is supplied.** The coin carrier is a supplied walker, and the Kawamoto-Smit (KS) carrier has no triplet. Everything below uses the coin carrier with 2·N_int modes per site [S].
- **The 3|1 split at a = 0.** At a = 0 the even exchange maps V_v are kinetic symmetries that merge the triplet with the 111 corner. In this synthesis the split is set by the supplied interaction, which breaks every V_v (D5).
- **The eigenmode-mixing error is generic.** Lane C's reviewer found it for one term, but it applies to any quadratic term coupling k to k+Π. It is the main reason to drop the staggered singlet mass (D6 computes the leak in both variants).
- **ε·f is its own supplied term.** It has face-diagonal support. The chessboard note's on-site (c/2)ε gaps the triplets and the singlets equally (Lane B, D5 at β = 0), so it cannot keep the triplet light.

## 1. The problem

**Carrier [S].** Each site carries ψ_{σi}: σ is a spin-½ index and i runs over an internal representation R of an on-site group G, with dim R = N_int.

**Free Hamiltonian.** H₀(k) = [a₀ + 2aΣcos k_j + vΣσ_j sin k_j] ⊗ 1_R, the general zero-flux nearest-neighbour (NN) form (Lane B D1, reviewed).
- Corner πn has chirality χ_n = (−1)^{|n|} and energy E_n = a₀ + 2a(3 − 2|n|).

**Target.** A G-invariant interaction, invariant under translations and the proper rotation group O, with:
- gapped set 𝒢 = {000, 111, ē₁, ē₂, ē₃};
- light set = the three weight-1 corners, each carrying a chiral multiplet R;
- the three copies exactly degenerate.

## 2. Obstructions, with exact scope

**O-A (EXACT): the staggered singlet mass strips the triplet's protection.**
- Translation T_v acts on corner n by (−1)^{n·v}.
- A bilinear between corners n ≠ n′ carries momentum π(n⊕n′), so full translations forbid it. Note e_a ⊕ ē_a = 111.
- Any momentum-Π term ε·g, with g even-displacement and O-invariant, takes two independent corner values: M_s = g(000) = g(111) and M_t = g(e_a) = g(ē_a).
- Keeping the triplets light requires M_t = 0. That is codimension 1 and is not protected by any remaining symmetry (even translations, O, G, Hermiticity).
- Lane C's constant "−3" in f is the same tuning.

**O-B (EXACT): the corner energy cannot be fixed by axiom symmetries.**
- Consider a symmetry built from translations, proper rotations R, the staggered sign, time reversal and particle-hole. It acts as H(k) ↦ ηU H(Lk+κ)^{(*)}U†, with L = ±R and κ ∈ {0, Π}.
- Preserving vΣσ_j sin k_j requires η·s_κ = det O_spin · det L.
- Every such map with proper R has det O_spin · det L = +1, so η·s_κ = +1 and the identity hop 2aΣcos k_j is also preserved.
- So E_light = a₀ + 2a is a symmetry-allowed relevant parameter: one tuning.
- A lattice CP that includes site inversion does forbid a₀ and a (σ_y H(k)* σ_y = −H(k) iff a₀ = a = 0). Inversion is not an axiom symmetry.

**O-C (EXACT): adjacency limits the suppression.**
- Each light corner e_a has three neighbours (000, ē_b, ē_c), and all three are gapped.
- Restrict a composite's form factor with reach R per axis to the edge from πe_a to a gapped neighbour. It is a degree-R trigonometric polynomial that is nonzero at the far end, so it has at most 2R zeros. Hence it vanishes at e_a to order at most 2R.
- One-sided cube stencils (exponents 0, 1) give order at most 1.
- Lane C's light node also has three gapped neighbours, so the triplet choice is not geometrically worse.

**O-D (LIT + ARGUED): dynamics.**
- Golterman–Shamir's abstract: if mirror zeros are "kinematical" and their conditions hold, "the massless fermion spectrum must be vector-like".
- Golterman–Petcher–Rivas, as cited by Lane C.
- Neither is resolved here.

**O-E (EXACT): the overall fermion-number U(1)_F must be broken.** 𝒢 has four corners with χ = +1 and one with χ = −1. The U(1)_F³ coefficient is therefore proportional to 3N_int ≠ 0.

## 3. Routes, ranked

| Rank | Route | What it supplies | What it shows | Tunings | Leak into light modes |
|---|---|---|---|---|---|
| R1 (top) | Variant T: keep all translations; symmetric mass generation (SMG) of all five 𝒢 corners | N_int = 16 per corner (Spin(10) 16 = one SM generation with ν_R); corner-indicator composites of reach R; the landed Ω quartic | Symmetry protection against every bilinear except one energy; exact degeneracy; per-corner anomaly freedom | 1 (E_light) | O(q^{2R}) |
| R2 | Variant E: Lane B's ε·f_B^p with M_t = 0, then SMG of the mirror triplet | Same, plus the face-diagonal mass | Same structure, fewer interacting corners | 2 (E_light, M_t), plus a = 0 for the Lorentz-scalar mass reading | O(m\|q\|^{2p−1}) |
| R3 | R1 with U(1) content (1, 5, −7, −8, 9) per corner (10 modes/site) | Lane C's four monomials on corner composites | Perturbative anomalies vanish per corner; global ARGUED | 1 | O(q^{2R}) |
| Rejected (EXACT) | Canonical 2×2×2 "taste" blocking | — | Translations drop to 2Z³, all corner characters become trivial, inter-corner masses become allowed, and the triplet splits as E_{1/2} ⊕ G_{3/2} | — | — |

## 4. Derivation for R1 (answers Q1–Q4)

**D1 (EXACT): composites (Q1).**
- Definitions: σ_j = sin²(k_j/2) and γ_j = cos²(k_j/2). The corner indicator is I_n(k) = Π_j [n_jσ_j + (1−n_j)γ_j].
- Properties: I_n(πn′) = δ_{nn′} and Σ_n I_n = 1.
- Stencil: β_n(y) = 2^{−3−|y|₀}(−1)^{n·y} on y ∈ {−1,0,1}³, where |y|₀ counts nonzero entries. The composite is Φ^{[n]}_x = Σ_y β_n(y)ψ_{x+y}: a smeared field demodulated by the corner character.
- The weight-2 indicator Σ_m I_{ē_m} = (3 − Σc − Σcc + 3c₁c₂c₃)/8 is 1 on the three mirror corners and 0 on the other five (CHECKED at all four weights).
- Orders at πe_a + q (CHECKED):
  - I₀₀₀ ≈ q_a²/4;
  - I_{ē_b} ≈ q_c²/4 (c is the third axis);
  - I_{ē_a} ≈ (q_aq_bq_c)²/64;
  - I₁₁₁ ≈ (q_bq_c)²/16.
- These saturate O-C at R = 1. Using I_n^R saturates it at reach R.
- Your proposed b(k) = Σ s_js_l has two defects: sin(k/2) is not 2π-periodic, and as a bond modulus b leaks linearly at e_a and equals 3 at 111.
- The cube option: on a unit cube the Walsh weights 0/1/2/3 carry the O representations A₁/T₁/T₂/A₂ (EXACT). The T₂ triplet Σ_y(−1)^{y_j+y_l}ψ_{c+y} isolates one mirror corner exactly, but it leaks linearly, at about 4|q_l|.
- Symmetry checks:
  - I_n is real and even, so the stencil is real and inversion-symmetric.
  - Rotations about the site permute I_n within a weight and rotate the spin.
  - H_int = Σ_x Σ_{n∈𝒢} V(Φ^{[n]}_x) is invariant under all of Z³, and Hermitian if V is.
- Non-canonical: {Φ_x, Φ_x†} = (3/8)³. A translation-covariant composite family is canonical iff |β̃| ≡ 1, which cannot vanish at the light corners (EXACT). So there is no product-state strong-coupling limit.

**D2: the interaction.**
- V = g(Ω + Ω†) + λC₂, built on the composites. Here Ω = Σ_A B_A B_A, B_A is the Spin(10) 10-channel spin-singlet pair, and C₂ is the Spin(10) Casimir.
- LANDED §1: Ω is nonzero, Spin(10)- and spin-singlet, and carries fermion number 4. It reduces number rotations to the Spin(10) centre Z₄, and C₂ removes SU(16). This meets O-E.
- The landed exact gap relies on a 32-body projector ΔQ. With non-canonical composites none of that exactness transfers (ARGUED).

**D3 (EXACT): exact corner zero modes.**
- {ψ_k, Φ^{[n]†}_x} = I_n(k) × phase, so [ψ_k, H] = H₀(k)ψ_k + Σ_n I_n(k)𝒥_{n,k}.
- At k = πe_a this gives [ψ_{πe_a}, H] = (a₀ + 2a)ψ_{πe_a}, for every coupling and on every even torus.
- So the E_light tuning is stable within this model class, but not against generic local terms.
- Every interaction-generated self-energy factorises as I(k)†Σ̃I(k), to all orders in perturbation theory.

**D4 (EXACT): bilinear protection.**
- Translations forbid all inter-corner bilinears.
- Spin(10) forbids intra-corner pairing in either spin channel, because 16⊗16 = 10_s ⊕ 126_s ⊕ 120_a contains no singlet (LANDED).
- What remains is the corner energy (scalar at a corner, LANDED T1) and marginal velocity terms. So E_light is the light triplet's one symmetric relevant bilinear deformation.
- T₁₁₁ acts on corners as (−1)^{|n|} = χ_n. That one exact lattice translation already forbids every light-to-gapped Dirac bilinear.

**D5 (EXACT): degeneracy, and what fixes the split (Q2).**
- The symmetry is (Z³ ⋊ O*) × Spin(10). V₆ ⊗ 16 is irreducible (Lane B's Mackey argument, reviewed, tensored with an irreducible of the other factor). So the three copies are exactly degenerate and each is pinned to its corner.
- The composite interaction respects all translation characters.
- If Lane B's ε-term is added, the even translations still separate the copies.
- If translations dropped to 2Z³, the copies would split as E_{1/2} ⊕ G_{3/2} under O*.
- The exchange maps V_v send I_n to I_{n⊕v} (for example 111 → e₁), so H_int breaks them. The 3|1 split comes from the supplied form factor, not from kinematics.

**D6 (EXACT): the leak, answering the review.**
- **Variant T.** The eigenmode at k is a spinor of ψ_k alone, because no quadratic term connects k to any other momentum. The interaction reaches it with amplitude I_n(k) = O(q^{2R}). The self-energy is O(q^{4R}), so the velocity is not renormalised at linear order.
- **Variant T, mean-field control.** Condensing B₁₀ gives the pairing P(k) = Σ_n Δ_n I_n(k)².
  - The spectrum is E = ±√(v²|s|² + P²), because στ_z and τ_x anticommute.
  - It is gapless exactly at the three light corners.
  - The light quasiparticle's admixture is O(Δ|q|^{4R−1}).
- **Variant E.** The block at (πe_a+q, πē_a+q) is [[h_L, M], [M, −h_L]]. Light helicity + couples to the same spinor sitting at −v|q|, so θ ≈ M/(2v|q|).
  - With f_B = 4(I₀₀₀ + I₁₁₁) ≈ q_a² + q_b²q_c²/4, θ = O(m|q|), and Φ^{[ē_a]} sees that admixture at full strength.
  - With f_B^p it is O(m|q|^{2p−1}).
- At equal reach, T leaks O(q^{2R}) and E leaks O(m q^{2R−1}).

**D7: anomalies (Q3). EXACT arithmetic; classification LIT.**

*Perturbative.* The gapped set's anomaly is minus the light set's: the singlets cancel and the mirror equals −light. Spin(10) has no cubic anomaly for any representation and no U(1).

*Z₁₆ (Spin-Z₄, with Z₄ acting by i, for example the Spin(10) centre), twisted by T_v.* Corner n has charge 1 or 3 according to (−1)^{n·v}, and ν(S, v) = −N Σ_{n∈S} χ_n(−1)^{n·v}.

| Twist v | ν(gapped set 𝒢) | ν(light set) |
|---|---|---|
| 000 | −3N | 3N |
| weight 1 | −N | N |
| weight 2 | N | −N |
| 111 | −5N | −3N |

- Over all eight corners: −8N at v = 111 and 0 otherwise.
- Requirement: N ≡ 0 mod 16.
- 3 is a unit mod 16, so three generations do not relax the per-generation condition.
- With 16 per corner, every corner is separately anomaly-free.

*Mod-2 (ARGUED).* A translation Z₂ acting on a whole 16 is harmless: the minimal Spin(10) instanton gives 4 zero modes and K3 gives 32, both even.

*LIT.* Wang–Wen–Witten: Spin(10) with spinor fermions and tensor bosons is completely anomaly-free.

*Content verdict.*
- 16 of Spin(10) per corner: passes everything.
- SM without ν_R (15 per corner) with Z₄ kept: fails.
- (1, 5, −7, −8, 9): perturbative pass. There is no Spin-Z₄ because −8 is even. Spin × U(1) globals are ARGUED. Mod-2 parities pass: Σq² = 220 and the K3 count is 10.

**D8: residual symmetry (Q4).**
- Exact lattice symmetries: Spin(10) (centre Z₄ ⊃ fermion parity), Z³ and O*.
- U(1)_F is broken to Z₄, and SU(16) is broken to Spin(10).
- On the copy index the symmetry is the order-48 group Z₂³ ⋊ S₃, with no continuous flavour group.
- Candidate symmetries that would protect the mirror, and their status:
  - U(1)_F: anomalous, and broken.
  - V_v and the sublattice-particle-hole map C·S: both swap light and gapped corners, and both are broken by H_int (EXACT).
  - The emergent per-corner Spin(10)_n: anomaly-free (LIT).
- Time reversal and lattice CP: open.

## 5. Supplied pieces, exhaustive (Q5)

1. **[S1] Carrier:** 32 complex CAR modes per site. This conflicts with Block 02 if read as the fermion field. The landed note says it does not supply a one-qubit compiler.
2. **[S2] Internal content:** Spin(10) and the 16, or the U(1) charges.
3. **[S3] H₀:** the zero-flux coin (a₀, a, v). The form is forced given S1 and zero flux; the values are supplied.
4. **[S4] Tuning:** E_light = 0, or a supplied improper CP.
5. **[S5] Composites:** I_n^R, which reach beyond NN (a 27-site block at R = 1).
6. **[S6] Interaction:** V with strong couplings, or the landed 32-body atom.
7. **[S7] Gapped-set choice:** this fixes the light count at 3. The allowed single-handedness counts are 1, 3 or 4.
8. **[S8] Dynamics:** continuous-time dynamics and a ground-state vacuum. With U(1)_F broken, "half filling" is undefined.
9. **[S9] Variant E only:** ε·f_B^p with M_t = 0, and a = 0.

Record is not used.

**What the axioms supply.**
- Z³ with its translations and proper rotations.
- Hence the corner orbits 1, 1, 3, 3 (LANDED T1), the orbit size 3 = d, and the translation characters that keep the copies distinct.
- M₂(C) per site, which does not hold S1.

## 6. Cheapest decisive computations (spec only, not run)

**C1. Exact symbolic checks (seconds).**
- I_n tables and Taylor orders.
- On an L = 4 torus with N_int = 1 and a generic quartic in Φ, check [ψ_k, H] = H₀(k)ψ_k + Σ I_n𝒥 in rational arithmetic (tests D3).
- The commutant of symmetric bilinears of reach ≤ 3 at the light corners: expected to be the scalar energy alone.
- Variant-E mixing orders: m|q| for f_B and m|q|³ for f_B².
- Any failure means D1, D3 or D6 is wrong.

**C2. Free Bogoliubov-de Gennes control (< 50 MB).**
- E = ±√(v²|s|² + P²) on a 64³ grid.
- Expected: zeros at exactly the three light corners, each with χ = −1, and gap |Δ_n| at each 𝒢 corner.
- This tests isolation at mean-field level; it is not SMG.

**C3. Integer anomaly table.** Compute ν(S, v) for all 8 twists and N ∈ {5, 15, 16}, plus Σq, Σq³ and the mod-2 parities. Expected: N = 16 clean; N = 15 fails at every twist.

**C4. 1+1D DMRG mechanism control (not decisive for 3+1D).**
- Setup: Lane C's 3450 chain with no staggered quadratic term (the T analogue).
- Gapping composites with form factors sin^{2R}(k/2) for R = ½ (bond), 1 and 2.
- An E analogue: add a quadratic mass at momentum π.
- Measure the central charge c, the gaps at 0 and π, the light velocity, exact k = 0 degeneracy (a D3 check) and the light–composite correlator.

| Outcome | Meaning |
|---|---|
| c = 2, π gapped, light velocity intact | The mechanism survives adjacency at that R |
| Works at R ≥ 1 but not R = ½ | Use R ≥ 1 in 3D |
| c < 2, or symmetry breaking, at every R | The adjacency / GPR failure is inherited |
| E analogue worse than T at equal R | Confirms D6 |

**C5. Decisive 3+1D test (not cheap).** First check whether the Yukawa-to-10-scalar version is free of the QMC sign problem (unknown). 32 modes per site at L ≥ 8 exceeds the current numeric slot.

**Ruthless risks, ranked.**
1. No demonstrated 3+1D SMG phase with overlapping composites, and Golterman–Shamir is unresolved.
2. Spontaneous translation breaking. A density wave at odd-weight momentum restores light-to-gapped Dirac masses; one at πe_b splits the copies.
3. The one energy tuning is not axiom-protected.
4. The carrier size and the stencils beyond NN are both supplied.
5. The count 3 is selected by S7, not forced.

## 7. Ten-line summary

1. **[EXACT]** Lane B's staggered singlet mass breaks the odd translations that forbid a light–mirror Dirac mass. Keeping the triplet light is then a codimension-1 tuning M_t = 0, and Lane C's "−3" is the same tuning.
2. **[EXACT]** Keeping all translations (R1) forbids every inter-corner bilinear, and Spin(10) forbids pairing (16⊗16 has no singlet). T₁₁₁ acts as chirality. The light triplet has one relevant symmetric bilinear, its energy a₀ + 2a.
3. **[EXACT]** No symmetry built from translations, proper rotations, the staggered sign, time reversal and particle-hole forbids that energy. An improper CP would; the axioms give proper rotations alone. So there is one tuning, and it is radiatively stable within the composite class.
4. **[EXACT]** The corner indicators I_n = Π[n_jσ_j + (1−n_j)γ_j], on a 27-site stencil 2^{−3−|y|₀}(−1)^{n·y}, are O-covariant, fully translation-invariant and real. Each isolates one corner, and the light corners are left as exact zero modes of the full H.
5. **[EXACT]** Each light corner has three gapped neighbours, so any reach-R composite leaks at most to order q^{2R} (order q¹ for cube stencils). The brief's b and the cube T₂ composites leak linearly.
6. **[EXACT]** Reviewer's point resolved: variant T has no light–mirror quadratic term, so the leak is O(q^{2R}) and the mean-field admixture O(Δq^{4R−1}). Variant E leaks O(m|q|^{2p−1}), which is O(m|q|) for f_B.
7. **[EXACT]** Mackey under (Z³ ⋊ O*) × Spin(10) keeps the three copies degenerate and pinned. The 3|1 split comes from the supplied form factor, which breaks the a = 0 exchange maps.
8. **[EXACT arithmetic, LIT classification]** Mirror and gapped-set anomalies are minus the light set's. Twisted Z₁₆ gives ν ∈ {−3N, −N, N, −5N}, so N ≡ 0 mod 16, and the 3 generations do not help. A 16 of Spin(10) (an SM generation with ν_R) passes per corner; 15 fails with Z₄ kept.
9. **[LANDED + EXACT]** The Ω quartic breaks U(1)_F to the centre Z₄ (required, since the gapped set is U(1)_F-anomalous). The residual symmetry is Spin(10) × Z³ × O*, with Z₂³ ⋊ S₃ on the copy index and no protecting symmetry left.
10. **[ARGUED / SPEC]** Still open: 3+1D SMG with non-canonical composites (Golterman–Shamir, GPR), spontaneous translation breaking, and the supplied carrier, stencils and orbit choice. Next runs: C1–C3 (exact, cheap), then C4 (1+1D DMRG with a form-factor order sweep, T versus E).

**Sources:**
- [Golterman–Shamir, arXiv:2603.15985](https://arxiv.org/abs/2603.15985)
- [Wang–Wen, arXiv:1809.11171](https://arxiv.org/abs/1809.11171)
- [García-Etxebarria–Montero, arXiv:1808.00009](https://arxiv.org/abs/1808.00009)
- [Wang–Wen–Witten, arXiv:1810.00844](https://arxiv.org/pdf/1810.00844)
- [Wen, arXiv:1305.1045](https://arxiv.org/abs/1305.1045)