lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 14:17:58 UTC 2026, pinned at commit 49b21cf18. Author only, checked by no one.

# Gap purity, wish (Y4): solve attempt (FINISH row 1696)

## 0. Plan (written first, save protocol)

1. Read the crux card, the RH strategy file (2.3, 2.11, 2.12, Part 4), the strategy mine (section 4), and the cited Lean statements.
2. Phase 1 (closed folder). Look for a one-way inequality in the neutral sector whose proof reads the group. If none, prove an obstruction for a stated class.
3. Phase 2. Open the registry and the crux card section 3 files. Compare each candidate.
4. End with the RESULT line.

(Steps are appended below as they are done.)

## 1. Reading done (Phase 1 sources only)

Read: the crux card in full; `gap-purity-rh-strategy-fable.md` sections 0, 2.3, 2.11, 2.12 and Part 4; `gap-purity-strategy-mine-fable.md` sections 0, 2.0 and 4. Lean: statement-level lines of `Purity.lean` and `Stage0.lean` (see section 2).

Working note after reading (before any proof). Three routes were tried on paper, in this order.
1. Kinetic operator alone (Casimir spectrum of the one-link Wilson kernel). Verdict below: every sign found holds for U(1) with m² in place of j(j+1).
2. Symmetry sectors (centre, charge conjugation, global colour). Verdict below: one exact statement reads the group (Proposition INN). It gives nothing extensive.
3. Comparison models inside SU(2): the closed subgroups that contain −1. This gives the obstruction (Theorem SUB) and a sharper test than "fails for U(1)".

## 2. Setting and notation

Lean statements used (read, not run): `Stage0.lean` L38-L44 (`centreSign`, `centreShift`: a cut in axis ν multiplies by −1 the ν-links whose source has residue 0), L71 (`neutralProj` = mean of the eight centre translations); `Transfer.lean` L508-L552 (`spatialAction`, `gaugeAction`, `temporalAction`, `transferKernel`, `transferKernel_apply`); `Purity.lean` L25-L29 (`purity`).

Notation. Γ is the spatial periodic cube of side n. A slice configuration is u ∈ SU(2)^(3n³). T = T_β is the transfer operator with kernel

    K(u,v) = exp(−β(S(u)+S(v))/2) · ∫ dg Π_e exp(−β(1 − ½tr(g v_e g⁻¹ u_e⁻¹))),

where S is the spatial plaquette action and g runs over vertex gauges. P₀ is `neutralProj`. Z₀(t) = tr(P₀ T^t). purity(u) = Z₀(2u)/Z₀(u)². For k ⊂ {1,2,3}, C_k is the centre translation and Z_k(t) = tr(C_k T^t), so Z₀ = (1/8) Σ_k Z_k. I use the trace formula tr(C_k T^t) = ∫ exp(−β A_(k,t)) over all links of n³ × t, with A_(k,t) the Wilson action in which the temporal plaquettes of one time layer over the cut links carry 1 + ½tr in place of 1 − ½tr. (ARGUED from `transferKernel_apply`; the same assumption as Lemma P7 of row 1688.)

**The H-model.** Let 𝔖 be the set of closed subgroups H of SU(2) with −1 ∈ H. For H ∈ 𝔖 define T_H, P₀, Z₀^H and purity_H by the same formulas, with the Haar probability of H in place of that of SU(2), on L²(H^(3n³)). The function ½tr, the centre element −1, the gauge action and the centre shift all restrict to H. The members of 𝔖 are, up to conjugacy (CITED, classical: Klein's list of finite subgroups of SU(2), and the closed subgroups of positive dimension): the cyclic groups Z_2m, the torus U(1), the binary dihedral groups D*_m (Q_8 = D*_2), Pin(2) = U(1) ∪ iσ₁U(1) (the normaliser of the torus), the binary tetrahedral, octahedral and icosahedral groups 2T, 2O, 2I, and SU(2).

**The U(1) comparator.** For H = U(1), `neutralProj` projects on even flux. I call this the Z_2-neutral U(1) model. The fully neutral U(1) model projects on flux zero. Section 4 treats both.

## 3. Phase 1, result A: the one statement found that reads the group (Proposition INN)

**Proposition INN (charge conjugation is inner). PROVED.** Let ε = iσ₂ and (Cψ)(u) = ψ(ū), with ū the entrywise complex conjugate. For SU(2), at every β ≥ 0, every Γ and every t ≥ 1:

    C T = T C = T,   so   tr(P₀ C T^t) = tr(P₀ T^t).

In particular Λ_C: tr(P₀ C T^u) ≥ ½ tr(P₀ T^u) holds, with the value 1 in place of ½. The C-odd subspace lies in the kernel of T.

Proof. For U = (a, b; −b̄, ā) one computes ε U ε⁻¹ = (ā, b̄; −b, a) = Ū. So ū = gaugeAction(u, g) for the constant gauge g ≡ ε, and C = R_ε, where (R_hψ)(u) = ψ(gaugeAction(u,h)). The kernel satisfies K(u, gaugeAction(v,h)) = K(u,v) for every gauge h: S is gauge invariant, and the gauge Haar measure is invariant under g ↦ gh (`gauge_mul`, L539). The slice Haar measure is invariant under gaugeAction(·,h). So (T R_h ψ)(u) = ∫K(u,v)ψ(v^h)dv = ∫K(u,v^(h⁻¹))ψ(v)dv = (Tψ)(u). K is symmetric, so R_h T = T as well. C commutes with every C_k (−1 is real). ∎

This is the only step in this file where the proof reads SU(2): it uses that the automorphism U ↦ Ū of SU(2) is inner (the defining representation is quaternionic). The Lie algebra form of the same fact: −T_a^T = ε T_a ε⁻¹.

**How Λ_C fails for U(1). PROVED at fixed lattice and weak coupling (Theorem SUB (c), section 4); ARGUED on a box of fixed physical size.** For U(1), C is θ ↦ −θ and is not a gauge transformation. Free photons in the flux-zero sector give tr(C T^u)/tr(T^u) = Π_modes tanh(ω u/2), each mode being an oscillator with tr(C q^N)/tr(q^N) = (1−q)/(1+q). With ω u ≥ 2π/512 and about (n/u)³ thermal modes, the ratio is exp(−c·512³). So Λ_C fails for weak 4D compact U(1) by an extensive margin, and it holds for SU(2) exactly, and its proof reads the group.

**What INN gives toward (PUR-io): nothing extensive. PROVED (Lemma HALF).** Let S be a unitary involution that commutes with P₀T and is induced by a measure-preserving involution of the slice space. Then tr(P₀ S T^t) ≥ 0, so the S-even part of the trace is at least half of the trace: tr(½(1+S)P₀T^t) ≥ ½ tr(P₀T^t).
Proof. tr(P₀ S T^t) = (1/8)Σ_k ∫K_t(s c_k x, x)dx ≥ 0, because the kernel of T^t is positive. ∎
So the removal of all S-odd states lowers log tr by at most log 2. The target needs log D(u) ≤ 0.31 against a thermal log D of order (n/u)³ = 512³. INN removes the one-photon tower and every other C-odd state. It leaves the C-even states (two photons, two gluons in a colour singlet), and their thermal weight is extensive. INN meets the letter of (Y4). It does not meet its purpose. Section 4 explains why in a way that also judges later candidates: INN holds for Pin(2) and for the binary icosahedral group, and those models fail the purity test.

**Other things tried in Phase 1, with verdicts (ARGUED unless marked).**
- Casimir spectrum of the one-link Wilson kernel. Its eigenvalue on spin j is c_j = I_(2j+1)(β)/I_1(β). If c_j is a Laplace transform in 4j(j+1) (Lemma HW-SU2 of row 1682, CITED there as UNVERIFIED), then log-convexity gives c_1 ≥ c_(1/2)^(8/3) (GUESSED on that condition). The U(1) form is c_2 ≥ c_1⁴. The exponent reads the Casimir values 2 and 3/4, but the direction and the form are the same for both groups. No sign differs.
- Global colour. A gauge-invariant state is a singlet under the constant gauges, which act by a non-trivial SO(3) for SU(2) and trivially for U(1). In a free gas the singlet projection lowers the trace by a power of the number of modes, not by an exponential. Not extensive.
- Twist eaters. Z_k > 0 for both groups. For SU(2) the pair iσ₁, iσ₂ anticommutes, so the twisted action A_(k,t) has zeros, and a tube estimate gives Z_k(t) ≥ c(Γ,t) β^(−9n³t/2) for β ≥ 1 (ARGUED; the tube estimate is Lemma TUBE of 4.5). For U(1) the twisted action has a positive minimum a (about 256π² at the aspect n/u = 512, ARGUED), so Z_k ≤ exp(−aβ). This reads the group and the centre. It concerns the sectors with centre flux, not the neutral sector, and it is Candidate T of row 1688 at small volume. It holds for Q_8.
- Sectors. Lemma SEC (section 4): a symmetry that splits the neutral space bounds the purity from ABOVE. SU(2) has no such symmetry left in the neutral sector (its centre is finite and INN removes C). So the finite centre and the inner C remove two upper bounds for the purity. Neither gives a lower bound.
- Integrality analogues: dim of a non-trivial representation ≥ 2; Casimir ≥ 3/4; centre flux in {0,1}; eight sectors. Each is true. I found no inequality for the neutral trace that uses one of them and fails for the models of section 4.

## 4. Phase 1, result B: the obstruction (Theorem SUB)

### 4.1 Three lemmas

**Lemma SEC (a splitting bounds the purity from above). PROVED.** Let the neutral space be an orthogonal sum of closed subspaces H_s, each invariant under T, with projections P_s. Put Z_s(t) = tr(P_s P₀ T^t) ≥ 0 and p_s = Z_s(u)/Z₀(u). Then purity(u) = Σ_s Z_s(2u)/Z₀(u)² ≤ Σ_s p_s² ≤ max_s p_s.
Proof. In each sector Z_s(2u) = Σ λ^(2u) ≤ (Σ λ^u)² = Z_s(u)². ∎

**Lemma FLAT (finite groups at β = ∞). PROVED.** Let H ∈ 𝔖 be finite. Put ε = |H|^(−3n³), and let N₀(H) be the number of orbits of the set of commuting triples (h₁,h₂,h₃) ∈ H³ under simultaneous conjugation by H and the eight sign changes h_i ↦ ±h_i. Let δ_H = 1 − max{|½tr h| : h ∈ H, h ≠ ±1} (and δ_H = 2 if H = {±1}). Then for all Γ, all t ≥ 1 and all β ≥ 0:

    ε^t N₀(H) ≤ Z₀^H(t; β) ≤ ε^t N₀(H) + exp(−β δ_H).

Proof. Z₀^H(t;β) = (1/8)Σ_k E[exp(−βA_(k,t))], with E the uniform probability on H^(links of n³×t). Each plaquette term is 1 ∓ ½tr h with h ∈ H, so it is 0 or at least δ_H. Hence 1{A=0} ≤ exp(−βA) ≤ 1{A=0} + exp(−βδ_H). It remains to show (1/8)Σ_k P(A_(k,t) = 0) = ε^t N₀. At β = ∞ the kernel is K_∞(u,v) = 1{u flat}·1{v flat}·P_g(v^g = u), so T_∞ = ε·Π, where Π is the orthogonal projection on the gauge-invariant functions supported on flat slices (the factor ε is the mass of one point of H^(3n³)). So tr(P₀T_∞^t) = ε^t·rank(P₀Π). The rank is the number of orbits of flat slices under gauges and centre shifts. A flat connection on the periodic cube is fixed, up to gauge, by its three holonomies up to simultaneous conjugation (the plaquettes generate the relations of π₁ = Z³), and the centre shift along axis i multiplies the i-th holonomy by −1 (a closed line along axis i crosses the cut once). So the rank is N₀(H). ∎

Facts about N₀. (PROVED) N₀({±1}) = 1. If H has an element h ≠ ±1, then N₀(H) ≥ 2, because (h,1,1) is not in the orbit {(±1,±1,±1)} of (1,1,1). (PROVED, by hand and by enumeration) N₀(Q_8) = 22: two elements of Q_8 commute if and only if their images in Q_8/{±1} = Z_2² are linearly dependent, conjugation acts on Q_8 by signs, so the orbits are the triples in Z_2² of rank at most 1: 1 + 3·7 = 22.

Exact check, as a guide (python3 -I, fractions; script kept outside the repository, not a proof step): for H = Q_8 on the one-vertex slice (3 links, 512 configurations), enumeration gives 176 flat slices, 92 gauge orbits, N₀ = 22; and with exp(−β) = 10⁻⁶ the exact rational purity at u = 1 is 0.045454545455…, against 1/22 = 0.045454545454…, inside the bound of Lemma FLAT. At exp(−β) = 10⁻² it is 0.045522.

**Lemma CONC (U(1): the twist measure concentrates). PROVED.** Let H = U(1), with link angles θ. For α ∈ (R/2πZ)³ let C_α multiply by e^(iα_i) the i-links at the cut. C_α is unitary and commutes with T (each spatial plaquette holds two cut links with opposite orientations, or none; each temporal term holds the same link at two times; the group is abelian), and Z(α) := tr(C_αT^u) = ∫ exp(−βA_α(θ))dθ > 0, where A_α is the Wilson action with α_i added to the angle of one temporal plaquette on each (i,4) two-torus. Let ρ_β be the probability measure on (R/2πZ)³ with density proportional to Z(α). Then ρ_β → δ₀ weakly as β → ∞ (Γ and u fixed).
Proof. (1) a(α) := min_θ A_α(θ) is continuous, and a(α) = 0 only for α = 0: if every plaquette term vanishes, every plaquette angle is in 2πZ; the sum of the plaquette angles dθ_p over a closed (i,4) two-torus is 0; so α_i ∈ 2πZ. Hence a_r := min{a(α) : dist(α,0) ≥ r} > 0 for each r > 0, and Z(α) ≤ exp(−βa_r) there. (2) Lower bound for the mass: if |θ_l| ≤ s for all D = 4n³u links and |α_i| ≤ s, each plaquette angle is at most 5s in size, so A_α ≤ 6n³u·25s²/2. With s = β^(−1/2), β ≥ 1: ∫Z(α)dα/(2π)³ ≥ (π²β)^(−(D+3)/2)·exp(−75n³u). (3) So ρ_β(dist ≥ r) ≤ exp(−βa_r)·(π²β)^((D+3)/2)·exp(75n³u) → 0. ∎

### 4.2 The theorem

**Definition (blind proofs).** Let ℱ ⊂ 𝔖. A statement Φ about the SU(2) transfer is *ℱ-natural* if it is the member H = SU(2) of a family Φ_H(Γ,β,u), H ∈ ℱ ∪ {SU(2)}, written in the terms of section 2 (the operators T_H, P₀, C_k, the traces Z_k^H, the kernel, the measure). A proof of Φ is *ℱ-blind* if it proves Φ_H for every H ∈ ℱ. A proof *reads the group against ℱ* if it is not ℱ-blind.
What an ℱ-blind proof may use, for ℱ = {Q_8, 2T, 2O, 2I} (each fact PROVED or classical): H is a compact group with a Haar probability; H is non-abelian; its centre is exactly {±1}; the defining two-dimensional representation is irreducible and quaternionic, so every non-trivial representation in its tensor powers has dimension at least 2; ε ∈ H up to conjugacy, so Proposition INN holds; Q_8 ⊂ H, so twist eaters exist; 2I is perfect, [H,H] = H, as SU(2) is; reflection positivity, positivity of the kernel, gauge invariance, locality, the lattice symmetries, the dimension of the lattice; every lemma of rows 1682 and 1688 (P1 to P7, E1 to E8, REP, ENT).
What it may not use: that H is a manifold of dimension 3; the Lie algebra su(2); C_A = 2; the Casimir spectrum j(j+1); Ric > 0; the coefficient b₀.

**Theorem SUB.**
(a) PROVED. Let H ∈ 𝔖 be finite, H ≠ {±1}. For every Γ, every u ≥ 1 and every β ≥ β_H(Γ,u) := (6n³u·log|H| + log 5)/δ_H:

    purity_H(Γ,β,u) ≤ 1/N₀(H) + 1/5 ≤ 7/10 < 457/625,

and purity_H → 1/N₀(H) as β → ∞. For Q_8 the limit is 1/22. For H = {±1} the limit is 1.
(b) PROVED. For the Z_2-neutral U(1) model, and for the full trace of U(1): purity → 0 as β → ∞, for every fixed Γ and u.
(c) PROVED. For U(1), Λ_C fails at weak coupling on every fixed lattice: tr(P₀CT^u)/tr(P₀T^u) → 0 as β → ∞.
(d) Consequence (PROVED, it is logic). Let c > 7/10. No {H}-blind proof, H finite and ≠ {±1}, proves purity ≥ c at a point (Γ,β,u) with β ≥ β_H(Γ,u). No {U(1)}-blind proof proves purity ≥ c on a set of points that contains, for one Γ and u, arbitrarily large β.

Proof. (a) By Lemma FLAT, purity_H = Z₀(2u)/Z₀(u)² ≤ (ε^(2u)N₀ + e^(−βδ))/(ε^u N₀)² = 1/N₀ + e^(−βδ)/(ε^(2u)N₀²). For β ≥ β_H: e^(−βδ) ≤ ε^(2u)/5, since ε^(2u) = exp(−6n³u log|H|). N₀ ≥ 2. The limit follows from the two-sided bound.
(b) The flux projections P_e = ∫e^(−ie·α)C_α dα/(2π)³, e ∈ Z³, split the space, commute with T, and P₀ = Σ_(e even)P_e. Z_e := tr(P_eT^u) = ∫e^(−ie·α)Z(α)dα/(2π)³ ≥ 0, and Z_e ≤ Z_(e=0) because Z(α) > 0. By Lemma SEC, purity ≤ max_(e even) p_e = Z_(e=0)/Σ_(e even)Z_e = 1/Σ_(e even) ρ̂_β(e), where ρ̂_β(e) = Z_e/Z_(e=0) ≥ 0 is the Fourier coefficient of ρ_β. By Lemma CONC, ρ̂_β(e) → 1 for each e. So for each N the sum is at least N/2 for β large. The full trace is the same with all e.
(c) C P_e = P_(−e) C. So tr(P_eCT^u) = tr(P_e C T^u P_e) = tr(P_eP_(−e)CT^u) = 0 for e ≠ 0. Hence tr(P₀CT^u) = tr(P_(e=0)CT^u) ≤ Z_(e=0), and the ratio is at most p_(e=0) → 0 by (b).
(d) An ℱ-blind proof proves the statement for H, where it is false. ∎

Remark on the trajectory (the limit of what (a) proves). β_H grows like n⁴ and β_K grows like K. With the crux card's figures (β_K > 2^2800 for K ≥ 70, CITED from the card, not checked by me), part (a) applies at the calibrated β_K to every cutoff whose side satisfies 6n³u·log 120 + 2 ≤ 0.19·2^2800, that is n below about 2^700. This is a finite set of cutoffs. (PUR-io) needs an infinite set. So on the trajectory the obstruction for finite H is PROVED for finitely many cutoffs and ARGUED for the rest (next item).

**Statement SUB-arg (ARGUED, not proved here).**
(e) 2I and Q_8 at all large lattices. A finite gauge group at β above its freezing point is in the deconfined (topological) phase: defects have activity of order |H|exp(−6δ_Hβ) per link, uniformly in the volume, and the N₀ holonomy classes are degenerate up to exp(−cβn²). Then purity_H ≤ 1/N₀ + o(1) for all n at fixed large β. The proof would be a Peierls expansion. The freezing point of 2I is near β = 6 (CITED from memory, UNVERIFIED: Petcher and Weingarten 1980; Rebbi 1980).
(f) Pin(2) at weak coupling in four dimensions. Pin(2) is non-abelian, compact, of positive dimension, with centre exactly {±1} and with INN (ε ∈ Pin(2) up to conjugacy). Its Lie algebra is u(1), so C_A = 0 and b₀ = 0. At weak coupling it is U(1) with charge conjugation gauged. The photon pairs stay massless, and by Lemma HALF the trace falls by at most a factor 2 per involution. So its thermal weight is extensive and its purity is exp(−c·512³).
(g) SU(2) itself on a fixed lattice. The upper bound purity ≤ Cβ^(−3/2) is PROVED in 4.5 (Theorem SV), written after this item. What stays ARGUED here is the exact order, β^(−3/2) up to a power of log β. Count: near the flat connections, Z_t(β) is of order β^(−codim/2). The flat connections of SU(2) on n³×t have dimension 3·sites + 3 (gauges modulo a one-dimensional stabiliser, plus four commuting holonomies), so codim = 9n³t − 3, and Z(2u)/Z(u)² has the power β^(−(18n³u−3)/2 + (18n³u−6)/2) = β^(−3/2). The lower bound Z_t ≥ cβ^(−(9n³t−3)/2) is a tube estimate as in Lemma CONC. The upper bound needs the Laplace asymptotics at the singular flat connections (holonomies ±1), which I did not prove. There the six extra zero modes have stiffness β|a|² and the orbit volume is |a|², so the local density is |a|²·|a|^(−6)d⁴a: a logarithm, in exactly four dimensions (GUESSED; it matches the known convergence threshold of SU(2) Yang-Mills matrix integrals, CITED from memory, UNVERIFIED: Krauth and Staudacher 1998).

### 4.3 What the theorem says about (Y4)

1. **"Fails for weak U(1)" is too weak a test.** Proposition INN passes it: the statement is exact for SU(2), false for U(1) (Theorem SUB (c)), and its proof reads the group. But INN holds for Q_8, 2I and Pin(2), whose purity fails (PROVED for the finite groups in the range of (a); ARGUED for Pin(2)). So a proof that reads the group only as INN does cannot reach the purity.
2. **The finite centre cannot be the source. Non-commutativity of the group cannot be the source.** 2I has both, and every other property in the list of 4.2, and purity_2I ≤ 7/10 (range of (a)). What 2I lacks is the Lie algebra. Pin(2) has a Lie algebra, a finite centre and a non-abelian group law; it lacks C_A > 0 (ARGUED failure). So (Y4) must read C_A > 0 itself: the curvature of the group manifold, or the coefficient b₀. In SU(2) the "finite centre" is a consequence of this (a connected compact group has finite centre exactly when it is semisimple), not a second source.
3. **A sharper gate, for every later candidate of this campaign.** Replace test 2 of the crux card ("false or void for weak 4D compact U(1)") by four tests. The estimate must be false or void for each of:
   (T1) weak 4D compact U(1) (fully neutral and Z_2-neutral);
   (T2) the Pin(2) model at weak coupling;
   (T3) the binary icosahedral model 2I (and Q_8) at large β;
   (T4) SU(2) itself on a fixed lattice as β → ∞ (small physical volume).
   T3 is PROVED as a test in the range of Theorem SUB (a). T1 is PROVED on fixed lattices (SUB (b)) and ARGUED at fixed physical size. T4 is PROVED (Theorem SV, 4.5). T2 is PROVED on fixed lattices (Theorem SV) and ARGUED at fixed physical size. Phase 2 found all four tests on file as kill tests (section 5).
4. **The scale must be read with a size.** By T4 (PROVED, Theorem SV) and Lemma P5 of row 1688 (purity = 1 at β = 0, PROVED there), the passing set {β : purity(Γ,β,u) ≥ 457/625} of a fixed lattice contains a neighbourhood of 0 and is bounded. A proof of (PUR-io) must show that β_K lies in it for infinitely many K. So the missing inequality has the form "purity ≥ c for β ≤ β*(n)", with an explicit threshold β*(n) that grows at least as fast as β_K, that is with slope at least 11/(3π²) in log n (`PurIo.lean` L172, L348, as quoted in row 1682). The number 11/(3π²) is 11·C_A/(6π²) at C_A = 2 (ARGUED). This is the "size" of (Y4): C_A must enter as the slope of a threshold in log n. For U(1), Pin(2) and 2I no threshold of this form exists.

### 4.4 Table: every one-way statement on file in the three Phase 1 files, against the tests

| Statement | U(1) (T1) | Pin(2) (T2) | 2I, Q_8 (T3) | Verdict |
|---|---|---|---|---|
| P1 deficit, P2, P3, P6, ENT, REP | holds | holds | holds | blind |
| P4 sandwich (factor 8 = size of the centre cube) | holds for the Z_2 form | holds | holds | blind |
| E1 to E8 (excess, convexity, channel identity) | holds | holds | holds (finite sums) | blind |
| P7 (zeros in the coupling plane) | holds | holds | holds (Z is an exponential polynomial) | blind |
| HW-SU2 operator order | holds (Bessel order 0) | not checked | void (no Laplacian) | blind by T1 |
| Lemma SEC (upper bound for purity) | has infinitely many sectors | none found | none | wrong direction |
| INN (this file) | false | holds | holds | fails T2, T3 |
| Twist-eater lower bound for Z_k | false | holds (Q_8 ⊂ Pin(2)) | holds | fails T2, T3; not neutral |
| Ric > 0, Bakry-Émery (Candidate B of row 1688) | void | void | void | passes T1 to T3; dies at the tilt by the ground state, and it is scale-blind (T4) |
| Running coupling, b₀ > 0 | void | void | void | passes T1 to T3; it is a statement at the cutoff scale, not about the neutral trace at fixed physical size |

So, in the three files read, the statements that read the group against {U(1), Pin(2), 2I} are exactly the two that use the Lie algebra with the sign of C_A. Neither is an inequality for the neutral trace at the physical scale.

### 4.5 Theorem SV: every member of 𝔖 of positive dimension fails on a fixed lattice, SU(2) included

Written after 4.2 to 4.4. It replaces the ARGUED items (g) and, on fixed lattices, (f).

For H ∈ 𝔖 put κ_H(β) = ∫_H exp(−β(1 − ½tr h))dh, and Z_H(t) = tr(T_H^t), the untwisted partition function of n³ × t.

**Lemma SCH (an upper bound for the purity at every coupling). PROVED.** For every H ∈ 𝔖, every Γ, β ≥ 0 and u ≥ 1:

    ‖T_H‖ ≤ κ_H(β)^(3n³),   and   purity_H(Γ,β,u) ≤ 8·κ_H(β)^(3n³u) / Z_H(u).

Proof. The kernel is symmetric and non-negative, so ‖T‖ ≤ sup_u ∫K(u,v)dv (Schur's test). Drop the two spatial factors, which are at most 1: ∫K(u,v)dv ≤ ∫dg∫dv Π_e exp(−β(1 − ½tr(g v_e g⁻¹ u_e⁻¹))) = κ^(3n³), by the invariance of the Haar measure in each v_e. Next, with λ_i the neutral eigenvalues, purity = Σλ_i^(2u)/(Σλ_i^u)² ≤ max_i λ_i^u / Σλ_i^u ≤ ‖T‖^u / Z₀(u). Last, Z₀(u) ≥ Z(u)/8, because every Z_k is non-negative (Lemma P4 of row 1688). ∎

**Lemma TUBE (lower bound near a flat family). PROVED from standard calculus.** Let M be a compact Riemannian manifold of dimension m with its normalised volume, A ≥ 0 a C² function on M, and Φ a C¹ map from an open set of R^d to M with A∘Φ = 0 and with injective differential at one point. Then there is c > 0 with ∫exp(−βA) ≥ c·β^(−(m−d)/2) for all β ≥ 1.
Proof. Near that point Φ is a bi-Lipschitz embedding of a ball. Let F′ be its image. A has a minimum on F′, so ∇A = 0 there, and A(p) ≤ C·dist(p,q)² for q ∈ F′. For r = r₀β^(−1/2), F′ holds at least c·r^(−d) points with mutual distances at least 2r. The balls of radius r about them are disjoint, each has volume at least c·r^m, and A ≤ Cr₀²/β on them. ∎

**Theorem SV. PROVED.** Let H ∈ 𝔖 have positive dimension (H = U(1), Pin(2) or SU(2), up to conjugacy). For every Γ and u ≥ 1 there is C = C(H,Γ,u) with

    purity_H(Γ,β,u) ≤ C·β^(−3/2)   for all β ≥ 1.

Proof. Let h = dim H and S = n³u, the number of sites of n³ × u. (1) κ_H(β) ≤ C_Hβ^(−h/2) for β ≥ 1. For SU(2): κ = (2/π)∫₀^π exp(−β(1−cos θ)) sin²θ dθ ≤ (2/π)∫₀^∞ θ² exp(−2βθ²/π²)dθ = (π^(5/2)/2^(5/2))·β^(−3/2), from 1 − cos θ ≥ 2θ²/π² and sin θ ≤ θ. For U(1) the same bound without sin² gives β^(−1/2). For Pin(2) the second component has ½tr = 0 and adds e^(−β)/2. (2) Z_H(u) ≥ c·β^(−(3hS−3)/2). Apply Lemma TUBE on M = H₀^(4S) (H₀ the identity component; its link space has Haar mass 1 or 2^(−4S)), with A the Wilson action and the flat family

    Φ(ξ,a)_(x,μ) = exp(ξ_x)·exp(i a_μ σ₃/n_μ)·exp(−ξ_(x+μ)),

where ξ runs over a complement of the constants t·iσ₃ in Lie(H)^S, a ∈ R⁴ is near a point a⁰, and n_μ is the side in direction μ. All plaquettes of Φ(ξ,a) equal 1. The domain has dimension d = hS − 1 + 4. The differential at (0,a⁰) is injective: if ξ_x − Ad(e^(iθ_μσ₃))ξ_(x+μ) + i(δa_μ/n_μ)σ₃ = 0 for all (x,μ), with θ_μ = a⁰_μ/n_μ, then the σ₃ components give δa_μ = 0 (sum around the circle in direction μ) and ξ³ constant, hence 0 in the complement; the other components (absent for h = 1) satisfy ξ⁺_x = e^(2iθ_μ)ξ⁺_(x+μ), so ξ⁺ = e^(2ia⁰_μ)ξ⁺, hence ξ⁺ = 0 when some a⁰_μ is not in πZ. So m − d = 4hS − hS − 3 = 3hS − 3. (3) Lemma SCH: purity ≤ 8·C_H^(3S)β^(−3hS/2) / (c·β^(−(3hS−3)/2)) = C·β^(−3/2). ∎

The exponent 3/2 is half the number of spatial holonomy moduli (three directions, rank one): the count of toron states below the temperature 1/u.

**Theorem TRI (trichotomy of 𝔖 on a fixed lattice). PROVED (Theorem SUB (a) and Theorem SV).** For H ∈ 𝔖, every Γ and every u ≥ 1, as β → ∞:

    purity_H → 1           if H = {±1};
    purity_H → 1/N₀(H) ≤ ½   if H is finite and H ≠ {±1};
    purity_H → 0, at least as fast as β^(−3/2),   if dim H ≥ 1, in particular for H = SU(2).

**Corollary (the class, and why none of its members reads the group in the neutral sector). PROVED.** Call a lower bound for the neutral purity *scale-blind* if it is asserted, for one Γ and u, on a set of couplings that is unbounded above. Call it *subgroup-blind* if its proof is {H}-blind for some H ∈ 𝔖 other than {±1} and SU(2), and it is asserted at a point in the failure range of H (β ≥ β_H(Γ,u) for finite H; β above a constant of (H,Γ,u) for U(1) and Pin(2)). Then:
(i) no scale-blind bound purity ≥ c > 0 is true for SU(2);
(ii) no subgroup-blind bound purity ≥ c > 7/10 is true for H, so no such proof exists;
(iii) for c > 1/2, the only member of 𝔖 for which a scale-blind bound purity ≥ c holds is the centre {±1} itself.
So at the level of 𝔖 the neutral purity at weak coupling depends on the group through two numbers only, dim H and N₀(H), and SU(2) lies on the failing side for both readings (dim 3 > 0). Whatever makes SU(2) pass at β_K must be a relation between β and n. It is not a property that the group has at a fixed lattice.

Lemma SCH as an inequality for the Wilson law. It is one-way, exact, valid at every β and Γ, and it is in the neutral sector. Its direction is the wrong one (an upper bound for the purity). It is void where κ^(3n³u) ≥ Z(u)/8, which I expect on the calibrated trajectory (ARGUED: the spatial plaquettes cost an extensive factor).

## 5. Phase 2: each item against the record

Method. Keyword search with bounded context over `library/open-registry.md` and `library/*.md`; I read the quoted lines and their neighbours only. The registry (synced at row 391) has no line with any of: icosahedral, Q_8, Pin(2), finite subgroup, charge conjugation, toron, small volume, commuting triple, SMALL-BOX, Schur test. So the nearest record for every item is an attack file, not a registry row.

| # | Item of this file | Nearest record, quoted in a phrase | What differs | Status |
|---|---|---|---|---|
| 1 | Proposition INN (C T = T) | Row 876 idea 24, `gap-brainstorm2-max.md` L229: "for SU(2) complex conjugation is conjugation by i sigma_2, so C-periodic conditions equal periodic ones exactly" | Nothing in the identity. Here it is put in the (Y4) format, shown false for U(1) (SUB (c)), and judged by Lemma HALF. | ON FILE |
| 2 | Lemma HALF (an involution costs at most log 2) | `gap-band-flux-tail-neon-check-opus.md` L74: "a general identity for any positive kernel with an involution commuting with T. It reads no property of 4D SU(2)" | That file concerns the centre involution. HALF is the one-line bound tr(STᵗ) ≥ 0 for any point involution. | variant, not found as stated |
| 3 | Lemma FLAT, Theorem SUB (a) (finite H) | Check 884, `gap-crux-exercise2-check-astra.md` L233-L240: "(1,1,1) and (i,1,1) lie in distinct orbits even after the three central flips"; "‖T−P_flat‖ ≤ η"; and L231: "Z2 does not have these additional holonomies" | On file for Q_8 and 2T as rank at least 2. Here: every finite H, the exact limit 1/N₀(H), N₀(Q_8) = 22, and the explicit range β_H for the purity test. | ON FILE in substance; variant |
| 4 | Theorem SV (purity ≤ Cβ^(−3/2) on a fixed lattice) | `gap-solve-astra62.md` L102-L106 (checked, `gap-solve-check-opus.md` L76-L78): "At fixed n, the doubling defect is 45/2 log β + 15 log log β + O_n(1)"; "the one-plane twist costs 3/2 log β + log log β + O(V)"; `gap-mech-k2-solve-fable.md` L30: "the beta^(-3/2) toron count are ON FILE" | The file's result is sharper (it has the log log term; this confirms the logarithm that item (g) guessed). SV is a ten-line proof of the upper bound for the neutral purity, for U(1), Pin(2) and SU(2) at once, by Schur's test and a tube. | ON FILE and sharper; variant proof |
| 5 | Lemma SCH (purity ≤ 8κ^(3n³u)/Z(u), all β) | `gap-crux-skeleton-check-astra.md` L138: "c(beta) <= C exp(beta) beta^(-3/2)" (the same one-link integral) | I did not find the Schur bound for ‖T‖ joined to the purity. | not found as stated (bounded search) |
| 6 | Lemma SEC, Lemma CONC, SUB (b),(c) (U(1) on a fixed lattice) | `gap-rotgeom-opus.md` L196: "The projection divides the toron count by 8 x 48" (GUIDE arithmetic) | Here it is a proof for the Wilson U(1) law, by flux sectors and the concentration of the twist measure. | variant |
| 7 | Tests T1 to T4 of 4.3 | `gap-bridge-vectors-max.md` L159: "T1: compact U(1) … T2: frozen Q_8 and 2T … T3: Pin(2), GUIDE. T4: five dimensions"; `gap-direction2-max.md` L247: "SMALL-BOX"; `gap-finishline-opus.md` L197: "group-blind for the binary icosahedral group (row 827)"; `gap-assume-opus.md` L351: "The binary icosahedral test does not bind at order one; Q_8 and 2T do" | The tests are on file. The crux card (clause 2 of section 3) names only U(1). Row 1688's Proposition OBS uses abstract operators, not these models. This file shows by example (INN) that the U(1) clause alone admits a statement with no content for the purity. | ON FILE |
| 8 | Theorem TRI and its corollary | Pieces 3, 4 and 7 above | The three limits were not found in one statement. It is a packaging. | packaging of on-file facts |
| 9 | 4.3 item 4 (C_A as the slope of a threshold in log n) | Crux card section 2: "a deep-infrared statement at every late cutoff"; `PurIo.lean` L172, L348 as quoted in row 1682 | A restatement of dimensional transmutation. | ON FILE |

Correction from Phase 2. Idea 1 of `gap-assume-opus.md` (L351; I did not look up its row number) records that the 2I test "does not bind at order one". My test T3 is a large-β test. It binds where Theorem SUB (a) applies and, by item (e), above the freezing point of 2I. It says nothing about order-one coupling.

## 6. Answer to the brief

**I did not find (Y4).** I found no one-way inequality for the neutral sector, with a sign and a size, in the direction that (PUR-io) needs, whose proof reads the Lie algebra of SU(2).

What exists, exactly:
1. One exact statement in the neutral sector whose proof reads the group and which is false for weak U(1): Proposition INN. It is on file (row 876, idea 24). It gives at most log 2 (Lemma HALF), against an extensive need.
2. One exact one-way inequality for the purity of the Wilson law at every coupling: Lemma SCH. Its direction is the wrong one.
3. The obstruction, Theorem TRI with its corollary: on a fixed lattice the weak-coupling purity of every closed subgroup H ∋ −1 of SU(2) depends on H only through dim H and N₀(H); it tends to 1 for the centre alone, to 1/N₀(H) ≤ ½ for the other finite groups, and to 0 for U(1), Pin(2) and SU(2). So two classes of lower bounds are empty or blind: the scale-blind bounds (false for SU(2) itself) and the subgroup-blind bounds (false for the subgroup). A proof that reads only the finite centre, or only that the group is non-abelian, is subgroup-blind for 2I. Its pieces are on file; the packaging and the exact limits are the new part.

What this gives toward (PUR-io): a narrower statement of what is missing. The missing inequality must (a) fail for 2I and Q_8, so it reads the Lie algebra; (b) fail for Pin(2), so it reads C_A > 0; (c) fail for SU(2) at fixed lattice and large β, so it contains a threshold β*(n) and C_A enters as the slope of β* in log n. In the three Phase 1 files only two statements meet (a) and (b): Ric > 0 on the group and b₀ > 0. Neither is about the neutral trace at fixed physical size. I have no candidate that joins them.

## 7. Labels and limits

- PROVED here (by hand, one author, checked by no one): Proposition INN; Lemma HALF; Lemma SEC; Lemma FLAT; N₀(Q_8) = 22; Lemma CONC; Theorem SUB (a) to (d); Lemma SCH; Lemma TUBE (from the inverse function theorem and Taylor's formula); Theorem SV; Theorem TRI and its corollary. Each uses the trace formula of section 2 (ARGUED from `transferKernel_apply`; not checked in Lean) and, for the H-models, the remark that the construction of T is the same for a closed subgroup.
- CITED: the Lean lines of section 2; the classification of closed subgroups of SU(2) (classical, no page given); row numbers and file lines of section 5, read in bounded context only.
- ARGUED: the free-photon value of tr(CT^u)/tr(T^u); items (e), (f) and the order in (g); the twist-eater tube bound; that Lemma SCH is void on the trajectory; 4.3 items 2 and 4 where they use (e) or (f).
- GUESSED: the Casimir inequality c_1 ≥ c_(1/2)^(8/3) (conditional on an unverified lemma); the logarithm in (g), which Phase 2 found on file in a sharper, checked form.
- UNVERIFIED references (from memory, no paper opened): Petcher and Weingarten 1980; Rebbi 1980; Krauth and Staudacher 1998.
- Computation: one exact enumeration for Q_8 on the one-vertex slice (python3 -I, fractions), as a guide; the script is in the session scratchpad, outside the repository. No Lean run. No floating-point step in any proof. By the lane's rule on written proofs, nothing here may land as a proof note in this state.
- Not done: a proof of (e) (Peierls expansion for finite H at large β on all lattices); a proof of (f) at fixed physical size; explicit constants in Theorem SV; a full read of any Phase 2 file.

RESULT: Row 1696 (Claude Fable 5.2, laptop; author only, checked by no one). (Y4) not found. Obstruction proved: on any fixed lattice, as β grows, the neutral purity of a closed subgroup H ∋ −1 of SU(2) tends to 1 only for the centre, to 1/N₀(H) ≤ 1/2 for other finite H (1/22 for Q_8), and to 0 like β^(−3/2) for U(1), Pin(2) and SU(2) itself (Schur test plus tube). So scale-blind and subgroup-blind lower bounds cannot exist; (Y4) must read C_A > 0 as the slope of a threshold β*(n). Pieces are on file (rows 876, 884, gap-solve-astra62); the packaging, exact limits and Lemma SCH are variants.
