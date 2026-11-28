lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-28T21:15:14Z

# gap-kernel-solve-fable (FINISH row 1674): closed-folder solve from the Lean hypothesis

Started 2026-11-28T09:15:14Z (date -u). Worker: Mac mini Claude worker 1, Claude Fable 5.2, max. Base commit 9a626d7f6. No commit, no push; the relay copies this file.

Status: COMPLETE at 2026-11-28T10:32:33Z (date -u). Outcome: clean negative with exact reductions. The RESULT line is the last line.

## 0. Scope, and one conflict in the instructions

- The row brief says: closed folder. Read only `lean/gapchain/GapChain/Stage0.lean`, `lean/gapchain/GapChain/Final.lean` and `library/gap-mech-direction4-fable.md` sections 1.4 and 1.5. Do not read FINISH.md, GOAL.md, the registries or any other library file.
- The dispatch text says: read FINISH.md and GOAL.md, build on all published work, and grep `library/open-core.md` and the FINISH rows before a statement is called new.
- These two texts conflict. Decision: the row brief wins, because it is the specific text for this item, and because a closed-folder look cannot be repaired after the folder is read.
- What was read before the conflict was seen: GOAL.md (in full, 94 lines; it is about the existence target and has no content on the gap), and FINISH.md row 1674 only (found by grep of the row name). No other FINISH row, no registry and no other library file was read. The header sections of FINISH.md (efficiency rules, Build on published work) were NOT read; the general working rules were applied instead.
- Consequence: no statement in this file is called new. Novelty against `library/open-core.md` and the FINISH rows was NOT checked. The check row can do that comparison.
- The session memory index (one line per earlier row) was loaded by the harness. Its lane files were not opened.
- No numeric job was run (row rule). Labels: PROVED, CITED, ARGUED, GUESSED, as the row asks.

## 1. The statement in plain mathematics (read from Stage0.lean L33-L250 and Final.lean)

Credit. The Wilson transfer operator, the lattice moments, the continuum witnesses and the reconstruction are from the YM4 Lean release of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (release `3932084a9b82`, as cited in Stage0.lean L11-L15). The multi-scale method behind the release is Balaban's. The conditional chain (seed gives gap) is the lane's, in `GapChain`.

Reading assumptions. These names are defined in imported files. The closed folder does not let me open them. I read them as follows, and every PROVED label below is conditional on this reading.
- (RA1) `Γ.side` is the side N of a cubic periodic lattice. `Γ.SliceL2 μ` is L^2 of the Haar product measure on the links of one slice orthogonal to axis μ.
- (RA2) `Γ.transfer μ β` is the Wilson transfer operator T = T_β of the slice. It is bounded and self-adjoint. T^n is trace class for n >= 1. Its trace is the periodic Wilson partition function: Tr T^n = Z_β(N^3 x n) (`Wilson.partition`), with n the length of axis μ.
- (RA3) T has a strictly positive continuous kernel (Wilson weight, integrated over the time links). CITED for the Wilson action: Lüscher, Commun. Math. Phys. 54 (1977) 283; Osterwalder and Seiler, Ann. Phys. 110 (1978) 440.
- (RA4) `HSNormLE A r` means: the Hilbert-Schmidt norm of A is at most r. `ketBra φ` is the rank-one operator |φ><φ|. `SpinHarmonics.tracePW` is the trace.
- (RA5) `betaAt L M K g0` is the Wilson β at cutoff step K. The lattice mesh is a_K = L^(-K) in units of the reference scale. Stage0.lean L306-L309 gives β_K / (K log L) -> 11/(3 π^2).

Objects.
- C_k, for k a subset of the three space axes: the centre translation. It multiplies by -1 each slice link in a direction ν in k that leaves the plane x_ν = 0 (L36-L60). The C_k are 8 commuting unitary involutions. They commute with T (the Wilson weight is invariant; PROVED from RA2-RA3 by the change of variables of L46-L56).
- P_0 = (1/8) Σ_k C_k: the orthogonal projection on the centre-neutral (zero electric flux) subspace (L70-L72).
- Rank-one test at time w (L74-L77): there are a unit vector φ and c > 0 with || c^(-1) P_0 T^w - |φ><φ| ||_HS <= 2/5.
- `NeutralRankOneTest` (L79-L80): the test holds for one w with 1 <= w and 1024 w <= N.
- `NeutralAtCutoff L M g0 ℓ K` (L153-L155): the test holds at β = β_K on every cubic lattice of side N = ℓ L^K.
- `MNeutralAll L M g0 ℓ` (L158-L159): ℓ > 0, 4 divides ℓ, and there is K_0 such that `NeutralAtCutoff` holds for every K >= K_0.
- `ExpClusters L K ν m` (L228-L231): for every positive-time span Z, for infinitely many j, there is C = C(Z, j) such that for every n: U_j(Z, t_n) <= C exp(-m t_n), with t_n = (2n+1) a_(K_j). U_j is the reflected truncated autocorrelation of Z in the infinite-volume lattice state ν_j (L214-L221).

What the kernel proves (Final.lean L68-L78): at the release witnesses (K, v, ν, S, X_2, X_4), `MNeutralAll L M g0 ℓ` gives `HasMassGap (centredOf S) (gapRate ℓ)` and `HasUniqueVacuum`, with gapRate ℓ = (2/ℓ) log(2^18/5041) (about 7.9/ℓ). `Stage2.massGap_of_expClusters` gives the same from `ExpClusters` for any m > 0.

So the target has two forms.
- (T-A) There are ℓ and K_0 such that the rank-one test holds on side ℓ L^K at β_K for all K >= K_0. The physical side ℓ is fixed. The cutoff goes to zero.
- (T-B) There is m > 0 such that `ExpClusters L K ν m` holds.

Section 1 written at 2026-11-28T10:22:28Z (date -u).

## 2. Exact reductions of (T-A) (each PROVED under RA1-RA5; novelty not checked)

Notation. N is the side. T = T_β. λ_0 = ||T||. Z(n) = Z_β(N^3 x n) = Tr T^n. Z^0(n) = Tr(P_0 T^n) = (1/8) Σ_k Tr(C_k T^n). The eigenvalues of T are λ_i, with joint eigenvectors ψ_i of T and of all C_k (they commute, and T is compact).

**Lemma 2.1 (the vacuum is neutral). PROVED.** λ_0 is a simple eigenvalue. Its eigenvector Ω can be taken strictly positive, and P_0 Ω = Ω.
Proof. By RA3 the kernel of T is strictly positive and continuous on a compact space. So T is positivity improving, λ_0 is simple, and Ω > 0 (Jentzsch). C_k Ω is a positive eigenvector for λ_0, because C_k is a measure-preserving change of variables that commutes with T. So C_k Ω = Ω for all k. QED

**Lemma 2.2 (the test from the trace tail). PROVED.** Let Θ_0(n) = Z^0(n)/λ_0^n - 1 for even n. If Θ_0(2w) <= 4/25, the rank-one test holds at time w, with φ = Ω and c = λ_0^w.
Proof. P_0 T^w = Σ_(i neutral) λ_i^w |ψ_i><ψ_i|. So λ_0^(-w) P_0 T^w - |Ω><Ω| = Σ_(i neutral, i ≠ 0) (λ_i/λ_0)^w |ψ_i><ψ_i|. Its squared Hilbert-Schmidt norm is Σ_(i neutral, i ≠ 0) (λ_i/λ_0)^(2w) = Θ_0(2w) <= 4/25 = (2/5)^2. QED
Remark. The converse loss is small: the lane's Stage 4 statement (Stage0.lean L127-L129) gives Θ_0(2w) <= 4/21 from the test.

**Lemma 2.3 (two-torus bound). PROVED.** For even n: Θ_0(n) <= Z(n)^2 / Z(2n) - 1, and also Θ_0(n) <= Z^0(n)^2 / Z^0(2n) - 1.
Proof. Put y_i = (λ_i/λ_0)^n in [0, 1], y_0 = 1. Then Σ y_i^2 <= Σ y_i, so Σ y_i <= (Σ y_i)^2 / Σ y_i^2 = Z(n)^2/Z(2n). Also 1 + Θ_0(n) = Σ_(i neutral) y_i <= Σ_i y_i. The second bound is the same argument on the neutral eigenvalues only. QED

**Proposition 2.4 (periodic two-torus criterion). PROVED.** Let 1 <= w and 1024 w <= N. If

    (E1)   Z_β(N^3 x 2w)^2  <=  (29/25) Z_β(N^3 x 4w),

then `NeutralRankOneTest` holds on side N at β. The same holds with Z^0 in place of Z. Then RA3 and Lemma 2.1 are not needed: use T >= 0 (CITED, Lüscher 1977), the top neutral eigenvector as φ, and its eigenvalue to the power w as c.
Proof. Lemma 2.3 with n = 2w gives Θ_0(2w) <= 29/25 - 1 = 4/25. Lemma 2.2 gives the test. QED
So (T-A) follows from: there are ℓ > 0 with 4 | ℓ and K_0 such that for every K >= K_0 the inequality (E1) holds at β = β_K, N = ℓ L^K, for one w in [1, N/1024]. This is an inequality between two ordinary periodic Wilson partition functions. It has no operator norm, no eigenvector and no twist.

**Lemma 2.5 (sandwich and monotonicity). PROVED.** Let R(n) = Z(n)^2/Z(2n) for even n, and Θ(n) = Z(n)/λ_0^n - 1. Then sqrt(R(n)) <= 1 + Θ(n) <= R(n), and R(n) does not increase in n.
Proof. Right side: Lemma 2.3. Left side: λ_0^(2n) <= Tr T^(2n) = Z(2n), so Z(n)/λ_0^n >= Z(n)/Z(2n)^(1/2). Monotonicity: with x_i = |λ_i|/λ_0, p_i ∝ x_i^u and q_i ∝ x_i^(2u), d/du log R = 2 (E_p[log x] - E_q[log x]) <= 0, because q is p tilted by the increasing weight x^u. QED
Use. The best choice is the largest time, w = floor(N/1024). (E1) is equivalent to the full (all flux sectors) tail bound up to a square: Θ(2w) <= 0.077 gives (E1), and (E1) gives Θ(2w) <= 0.16.

**Lemma 2.6 (integral form). PROVED.** Let ā_n(β) be the mean of 1 - (1/2) tr U_p over the 6 N^3 n plaquettes of the periodic torus N^3 x n at coupling β. Then

    log R_β(2w) = 24 N^3 w ∫_0^β [ ā_(4w)(β') - ā_(2w)(β') ] dβ'.

Proof. d/dβ log Z_β(Λ) = - <A_Λ>, where A_Λ is the sum of 1 - (1/2) tr U_p over the plaquettes of Λ (the weight of Stage0.lean L97-L102 without twist). At β = 0 every Z is 1, because the Haar measure is a probability. So log R_β(2w) = ∫_0^β ( <A>_(N^3 x 4w) - 2 <A>_(N^3 x 2w) ) dβ'. The torus N^3 x n has 6 N^3 n plaquettes. QED
Meaning. (E1) is: 24 N^3 w ∫_0^(β_K) [ā_(4w) - ā_(2w)] dβ' <= log(29/25) = 0.1484. The integrand is the change of the mean plaquette when the time period goes from 4w to 2w. The integral runs over all couplings below β_K, on the lattice whose size is fixed by β_K.

**Lemma 2.7 ((T-B) is a spectral statement; the constant C gives no slack). PROVED given that the one-step time shift of ν_j is a positive self-adjoint contraction (CITED for the Wilson action in finite volume: Lüscher 1977; ARGUED for the infinite-volume limit state).** Fix Z and j. Let ψ be the vector of Z in the reconstruction space of ν_j, let S be the one-step shift, and let ρ be the spectral measure of ψ for S minus |<Ω, ψ>|^2 times the point mass at 1. Then U_j(Z, t_n) = ∫ λ^(2n+1) dρ(λ). The bound of `ExpClusters` holds at j for some C if and only if ρ((r, 1]) = 0 with r = exp(-m a_j), and then C = ρ([0, r]) <= ||ψ||^2 works.
Proof. If ρ((r', 1]) > 0 for some r' > r, then ∫ λ^(2n+1) dρ >= ρ((r', 1]) r'^(2n+1), which is larger than C r^(2n+1) for large n. The converse is direct. QED
Meaning. (T-B) says: for every Z, for infinitely many j, the lattice theory at β_(K_j) has no spectrum between exp(-m a_j) and 1 on the vector of Z. By RA5, a_j = L^(-K_j) = exp(-(3 π^2/11) β_j (1 + o(1))). So (T-B) is the infinite-volume lattice mass gap at weak coupling with the asymptotic-freedom rate. No published proof exists for any large β (as of my knowledge). The freedom in C and the word "frequently" give no formal short cut.
Remark (interface, ARGUED). (T-B) is stronger than a gap of the limit. Weak convergence of spectral measures allows lattice mass below m that goes to zero with j. A weaker input, "for every Z and ε: for infinitely many j and all n, U_j(Z, t_n) <= C exp(-m t_n) + ε", also gives the limit gap by the same log-convexity step.

Section 2 written at 2026-11-28T10:23:29Z (date -u).

## 3. Two more exact forms of (E1), and what the seed says physically

**Proposition 3.1 (overlap form). PROVED under RA1-RA3.** Let τ(ω, η) be the kernel of T^w and ρ(ω, ω') = ∫ τ(ω, η) τ(η, ω') dη the kernel of T^(2w). ρ(ω, ω') is the partition function of the slab of height 2w with the bottom slice fixed to ω and the top slice fixed to ω'. Let π_1(ω) = ρ(ω, ω)/Z(2w); this is the law of one slice of the periodic torus N^3 x 2w. Let

    κ(ω, ω') = ρ(ω, ω')^2 / ( ρ(ω, ω) ρ(ω', ω') ).

Then 0 < κ <= 1, κ is the squared cosine of the angle between the vectors τ(ω, .) and τ(ω', .) in L^2, and

    1 / R(2w) = Z(4w) / Z(2w)^2 = E[ κ(ω, ω') ],   ω and ω' independent with law π_1.

Proof. Z(2w) = ∫ ρ(ω, ω) dω and Z(4w) = ∫∫ ρ(ω, ω')^2 dω dω'. Divide. κ <= 1 is the Cauchy-Schwarz inequality for ρ(ω, ω') = <τ(ω, .), τ(ω', .)>. QED
So (E1) is: E[1 - κ] <= 4/29. In words: take two independent typical slices of the 2w-periodic system. Use them as the two walls of a slab of height 2w. The free-energy cost of unequal walls against equal walls, -log κ = 2 F(ω, ω') - F(ω, ω) - F(ω', ω'), must be small for the whole N^3 wall, in the mean. The boundary data are typical, not worst-case.

**Lemma 3.2 (crossed channel). PROVED under RA2 for each axis.** Z(N^3 x n) is symmetric in the four sides. So Z(N^3 x n) = Tr (T'_n)^N, where T'_n is the transfer operator of the slice N x N x n along a long axis. Let E'(n) = -log ||T'_n|| and Θ'_n = Tr (T'_n)^N / ||T'_n||^N - 1 >= 0 (N is even). Then

    log R(2w) = N [ E'(4w) - 2 E'(2w) ] + 2 log(1 + Θ'_(2w)) - log(1 + Θ'_(4w)).

Proof. Write log Z(N^3 x n) = -N E'(n) + log(1 + Θ'_n) for n = 2w and n = 4w. QED
Meaning (ARGUED). When the slab tails Θ' are small, (E1) says: the ground energy of the periodic slab of thickness 4w is larger than two times the ground energy of the slab of thickness 2w by at most 0.148/N. This is a bound on the Casimir energy of the periodic slab: at most about 1.4 x 10^(-10) / w^3 per unit area (N = 1024 w).

**Size of the seed (ARGUED, ideal-gas estimate, guide only).** Let t = 2w a be the physical time and ℓ = N a >= 512 t the physical side.
- Free massless field with two polarizations: log(1 + Θ) is about (π^2/45) (ℓ/t)^3 >= 2.9 x 10^7. The seed fails by seven orders of magnitude in the exponent.
- One scalar particle of mass m: Θ is about ℓ^3 m^2 K_2(m t) / (2 π^2 t) = 512^3 (m t)^2 K_2(m t)/(2 π^2). This is below 0.16 only for m t >= 22.5. So ℓ >= 512 x 22.5 / m, about 1.15 x 10^4 / m.
- Small physical volume (Lüscher, Nucl. Phys. B219 (1983) 233): the neutral gap is of order g(ℓ)^(2/3)/ℓ. Then (gap) x t is of order g^(2/3)/512. The seed fails.
So (T-A) can hold only at a physical side of about 10^4 correlation lengths. It is a statement about the deep infrared, at a fixed physical size, uniform in the cutoff. The factor 10^4 comes from the constants 512 and 1024 of the consumer, not from physics.

**Thermal reading (ARGUED).** Θ(n) + 1 = Tr T^n / λ_0^n is the thermal partition function at temperature 1/(n a) with the vacuum energy removed. (E1) says that the Rényi-2 entropy of the thermal state, log R = -log Tr ρ_th^2, is at most 0.148 in a box with (ℓ T)^3 >= 512^3. So the seed is a bound on the entropy density: s_2(T) <= 1.1 x 10^(-9) T^3. A massless phase has s_2 of order T^3.

Section 3 written at 2026-11-28T10:26:20Z (date -u).

## 4. Candidates, and the six tests (g1)-(g6) of gap-mech-direction4-fable.md 1.5

Rule used: a candidate is called an attack only if it passes all six tests. References in this file are recalled from memory. Four were checked on the public web at 2026-11-28T10:34:32Z (date -u), for the bibliographic data only: Shen, Zhu and Zhu (Commun. Math. Phys. 400 (2023) 805-851); Ito and Seiler (arXiv:0711.4930); Olivieri (J. Stat. Phys. 50 (1988) 1179-1200); Dobrushin and Shlosman (1985, two chapters in the same volume). The other references were not re-read.

Remark 4.0 (a second consumer for (T-B); CITED plus ARGUED). The Wilson theory is a Gibbs field on Z^4 with the compact spin space SU(2)^4 at each site and a finite-range interaction. The constructive criterion of Dobrushin and Shlosman ("Constructive criterion for the uniqueness of Gibbs field", and the companion chapter "Completely analytical Gibbs fields", both in Statistical Physics and Dynamical Systems, eds. Fritz, Jaffe and Szász, Birkhäuser 1985) is stated for such spin spaces with the Wasserstein distance. If its condition holds on one cube of side B, the Gibbs state is unique and covariances of local functions decay at a rate of order 1/B. `ExpClusters` lets the constant C depend on Z and on j. So (T-B) follows from: (DS) there is C_0 such that for infinitely many j the Dobrushin-Shlosman condition holds for the Wilson specification at β_(K_j) on a cube of side B_j <= C_0 L^(K_j). ARGUED, not PROVED: I did not match the exact form of their decay statement to `latticeU`. (DS) needs no torus, no aspect ratio 512 and no twist. Its natural scale is a few correlation lengths, not 10^4. Its cost: the boundary data are worst-case.

### 4.1 The candidates

- **C1, the thermal forms.** F = (E1), or its integral form (Lemma 2.6), its overlap form (Proposition 3.1), its Casimir form (Lemma 3.2).
- **C2, continuation in β.** F = "on the seed lattice, d log(E_1 - E_0)/dβ >= -c with c = 3 π^2/11 + (integrable error)". By the Hellmann-Feynman formula d(E_1 - E_0)/dβ is the excess of the action per time step in the first excited state. This is the lattice action sum rule (Michael, Nucl. Phys. B280 (1987) 13). Start at strong coupling and integrate.
- **C3, comparison of each partition function with a coarser lattice.** Migdal-Kadanoff bond moving, chessboard bounds, Jensen bounds on Z(2w) and Z(4w) one by one (the method of Tomboulis, arXiv:0707.2179).
- **C4, contraction at one block scale.** F = (DS) of Remark 4.0, to be reached by a renormalization group carry from β_K to an effective action at order-one coupling, and a convergent block expansion there (in the manner of Olivieri, J. Stat. Phys. 50 (1988) 1179).
- **C5, curvature.** F = a Bakry-Emery lower bound for the lattice action or for the ground-state measure (Shen, Zhu and Zhu, Commun. Math. Phys. 400 (2023) 805, prove the gap this way at strong coupling).
- **C6, start in a small box.** F = the Lüscher spectrum of the small torus (neutral levels of order g(ℓ)^(2/3)/ℓ, a non-abelian effect of the constant modes), carried to large ℓ by a step-scaling inequality "ℓ (E_1 - E_0) grows with ℓ".
- **C7, change the model.** Centre-stabilized compactification (Ünsal and Yaffe, Phys. Rev. D 78 (2008) 065035): a small circle with a double-trace term, abelianization, a dilute gas of monopole-instantons, and the methods of Göpfert and Mack (Commun. Math. Phys. 82 (1982) 545) for the three-dimensional Coulomb gas.
- **C8, kinematics.** Symmetry, anomaly matching, the a-theorem (Komargodski and Schwimmer, JHEP 12 (2011) 099), flux duality ('t Hooft, Nucl. Phys. B153 (1979) 141).

### 4.2 Verdicts

| | (g1) 4D U(1), large β | (g2) 5D SU(2), large β | (g3) gapped twins | (g4) massless factor | (g5) scale | (g6) consumer, carry, method |
|---|---|---|---|---|---|---|
| C1 | pass: F is false (photon gas, R is of order exp(10^7)) | pass on BELIEF | pass: F is true in each gapped twin at large size, no line fires | pass: PROVED, R of a product is the product of the R's | pass: N(β) is about 10^4 ξ(β); at a fixed lattice R grows like a power of β (ARGUED, Laplace asymptotics) | FAIL: equivalent to the seed up to a square (Lemma 2.5); no method |
| C2 | pass: the bound fails at the transition near β = 1 | pass on BELIEF (bulk transition) | pass: the rate is bounded in 3D U(1) (Göpfert-Mack) | FAIL as written: reads one level; must be stated for the whole trace | pass | FAIL: the bound is the scaling law itself; equivalent |
| C3 | FAIL: the 4D recursion also runs to strong coupling for U(1), so the method proves a false statement. Ito and Seiler, arXiv:0711.4930, Section 4: "the Migdal-Kadanoff RG recursion formulas cannot distinguish non-abelian groups from abelian ones"; the gap they name is an inequality that is not proved at large β | not needed | not needed | not needed | pass | FAIL: Proposition 4.3 below |
| C4 | pass: (DS) is false (line: the photon propagator is not summable over a cube of any size) | pass on BELIEF (same line, gluon propagator) | pass: the line does not fire with a Debye mass (3D U(1)) or at small β | pass: (DS) is a property of the whole field; a massless factor breaks it | pass: B(β) is of order ξ(β); at a fixed cube (DS) fails for large β (ARGUED: the single-link coefficient is 18/6 = 3 > 1) | FAIL in part: the consumer exists (Remark 4.0), and (DS) is not the seed. The carry and the method at order-one coupling do not exist |
| C5 | FAIL the pair (g1)+(g3): the convexity line fails at large β in every dimension and for every group, also in 3D U(1), which has a gap | same | FAIL | not needed | FAIL: no N(β) | FAIL |
| C6 | pass: for U(1) the constant modes are free and ℓ (E_1 - E_0) does not grow | pass: in 5D the coupling at scale ℓ decreases | pass | pass if stated for all low levels | pass | FAIL: no consumer. The step from the small box to the seed size is the whole infrared problem |
| C7 | pass | pass | pass | pass | pass | FAIL: it is a different measure. No carry to the Wilson action at β_K (it needs continuity in the circle size and in the deformation) |
| C8 | pass by form | pass by form | pass | FAIL: the product with a massless factor has the same symmetries (Lemma ALG), and the a-theorem allows a massless infrared end (a free photon has a smaller a than the ultraviolet end) | FAIL: no N(β) | FAIL |

No candidate passes the six tests. No candidate is an attack.

**Proposition 4.3 (bulk precision). PROVED.** Let a method give numbers a_n <= log Z(N^3 x n) <= b_n for n = 2w and n = 4w. It proves (E1) only if 2 (b_(2w) - log Z(2w)) + (log Z(4w) - a_(4w)) <= 0.1484. So each bound must be correct to an absolute error of 0.15, on a quantity of order β N^3 w.
Proof. (E1) is 2 log Z(2w) - log Z(4w) <= log(29/25). The method can only conclude it from 2 b_(2w) - a_(4w) <= log(29/25). Subtract the true value, which is >= 0 by Lemma 2.3. QED
Use. A method with an error of η per site in log Z fails as soon as 8 N^3 w η > 0.15 (two tori of 2 N^3 w sites and one of 4 N^3 w sites). Every bound that moves or drops bonds has η > 0. The only methods that pass are those that give the same local expansion on both tori, so that the bulk term cancels exactly.

Section 4 written at 2026-11-28T10:29:04Z (date -u).

## 5. The negative result, for explicitly quantified families

I found no proof of (T-A) or (T-B), and no attack that passes the six tests. This section states what is excluded, family by family. "Consumer" means any theorem that gives the gap for every model of the class K of Lemma ALG (reflection positivity, the centre, the exchange of the axes), such as the lane's chain.

- **(N1) Group-blind arguments. PROVED from CITED results.** Family: every argument for the seed in which each step is true for all compact gauge groups with a Z_2 in the centre, at all β. Obstruction: the argument then proves the seed for U(1) in four dimensions at large β. The consumer then gives a gap. This contradicts the massless phase (Guth, Phys. Rev. D 21 (1980) 2291; Fröhlich and Spencer, Commun. Math. Phys. 83 (1982) 411; for the Villain action). The Migdal-Kadanoff recursion is in this family.
- **(N2) Dimension-blind arguments. BELIEF only.** Family: every argument true for SU(2) in all dimensions d >= 4 at large β. Obstruction: no gap is expected in d = 5 at large β. I know no theorem.
- **(N3) Sector-blind hypotheses. PROVED (this is Lemma ALG; on file).** Family: every hypothesis that reads only the SU(2) factor of a product. Proposition for the forms of this file: R, 1 + Θ and E[κ] are multiplicative under products, and a massless factor has R = +∞ or R of order exp(c (ℓ/t)^3). So the hypothesis must be a statement about the whole trace.
- **(N4) Bulk-lossy methods. PROVED (Proposition 4.3).** Family: every method that bounds Z(N^3 x 2w) from above and Z(N^3 x 4w) from below with an error η > 0 per site. Obstruction: it needs 8 N^3 w η <= 0.15, and N >= 1024 w.
- **(N5) One-level hypotheses. PROVED.** Family: every hypothesis of the form "E_1 - E_0 >= γ on side N" with no bound on the number of levels. Obstruction: Θ_0(2w) is a sum over all neutral levels. The bound Θ_0(2w) <= 4/25 needs, for every s > 0, that the number of neutral levels with E_i - E_0 <= s is at most (4/25) exp(2 w s). A gap alone gives only a factor times the trace tail at an earlier time w' < w: Θ_0(2w) <= exp(-2 (w - w') γ) Θ_0(2w'), where exp(-γ) is the largest ratio |λ_i|/λ_0 over neutral i ≠ 0. So a gap bound must come with a trace bound at one earlier time.
  Proof of the last inequality. For neutral i ≠ 0, (λ_i/λ_0)^(2w) = (λ_i/λ_0)^(2w') (λ_i/λ_0)^(2(w - w')) <= (λ_i/λ_0)^(2w') exp(-2 (w - w') γ). Sum over i. QED
- **(N6) Perturbative-range hypotheses. ARGUED.** Family: every hypothesis whose truth at coupling β is decided by the lattice measure on boxes of side r(β) with r(β) a(β) -> 0 (for example r <= β^k). Obstruction: on such boxes the renormalized coupling is small, the levels are those of the small-volume expansion, and the tail is of the size of a massless gas (Section 3). The hypothesis cannot see the scale 1/a(β) where the seed can first hold. I have no proof, because no rigorous small-volume expansion is at hand.
- **(N7) Symmetry and anomaly arguments. PROVED from Lemma ALG plus BELIEF.** Family: every argument that uses only the global symmetries, their anomalies and monotone quantities of the a-theorem type. Obstruction: the product with a massless factor has the same symmetries (PROVED), and the adjoint-Higgs Coulomb phase has them too (BELIEF).

What is left after (N1)-(N7) (ARGUED). A proof needs an input with these four properties together. (i) It is a statement about the whole field, with multiplicities. (ii) It lives at the scale of the correlation length, which is exp((3 π^2/11) β (1 + o(1))) lattice units. (iii) It is uniform in the cutoff. (iv) It is false for a free massless field. The known source of such an input is an expansion with a small parameter at that scale: strong coupling (Osterwalder and Seiler, Ann. Phys. 110 (1978) 440), a dilute gas of defects (Göpfert and Mack, for 3D U(1)), large N (Kopper, Magnen and Rivasseau, Commun. Math. Phys. 169 (1995) 121, for Gross-Neveu), or a hierarchical structure (Gawedzki and Kupiainen, Commun. Math. Phys. 106 (1986) 533). For the 4D SU(2) Wilson action at the scale of its correlation length I know no small parameter. This is the obstruction in one sentence.

Section 5 written at 2026-11-28T10:31:44Z (date -u).

## 6. The first open estimate, and its first step

**The estimate (exact form).** For one ℓ > 0 with 4 | ℓ and one K_0, for all K >= K_0, with N = ℓ L^K, w = floor(N/1024) and β = β_K:

    (E1)   Z_β(N^3 x 2w)^2  <=  (29/25) Z_β(N^3 x 4w).

By Proposition 2.4 this gives `MNeutralAll L M g0 ℓ`, and the kernel gives the gap. By Lemma 2.5 it is equivalent to the seed up to a square in the constant. So it is a cleaner statement of the same open problem, not progress on it.

**First step (written out).**
1. Algebra: Lemmas 2.1-2.3 and Proposition 2.4 (PROVED above).
2. Bulk cancellation. **Proposition 6.1 (PROVED).** Suppose that at coupling β there are numbers f, A and κ > 0 with | log Z_β(N^3 x n) - N^3 n f | <= A N^3 n exp(-κ n) for n = 2w and n = 4w. Then log R(2w) <= 8 A N^3 w exp(-2 κ w). So (E1) holds when 8 A N^3 w exp(-2 κ w) <= 0.1484.
   Proof. log R = 2 log Z(2w) - log Z(4w). The terms N^3 n f cancel: 2 (2w) - 4w = 0. The remainders are at most 2 A N^3 (2w) exp(-2 κ w) + A N^3 (4w) exp(-4 κ w). QED
   With N = 1024 w this needs 2 κ w >= log(8 A 1024^3 w^4 / 0.1484), that is 2 κ w >= 24.8 + log A + 4 log w.
3. Strong-coupling part of the integral of Lemma 2.6 (CITED, constants not computed: Osterwalder and Seiler 1978; Seiler, Lecture Notes in Physics 159 (1982)). For β' <= β_sc the polymer expansion gives the hypothesis of Proposition 6.1 with κ of order log(1/β'), because a cluster that sees the period n has at least n plaquettes and all other clusters give the same amount per site on every torus. So the part of the integral over [0, β_sc] is negligible for large w, and (E1) is the bound

        24 N^3 w ∫_(β_sc)^(β_K) [ ā_(4w)(β') - ā_(2w)(β') ] dβ'  <=  0.1484 - (negligible).

4. Where it stops. For β' above β_sc no expansion is known. The integrand at β' is small only if the theory at β' has finite-size corrections of the form of Proposition 6.1 on the lattice fixed by β_K. That is the gap at β' again. I see no induction on β: the integrand at β' lives on the lattice of β_K, not on the lattice of β'.

**The same estimate in local form (not equivalent to the seed; stronger).** (DS) of Remark 4.0, or the hypothesis of Proposition 6.1 with κ >= κ_0 / L^K for all K >= K_0. Both say: at the scale of the correlation length the theory has a contraction, uniformly in the cutoff. Their first step would be a renormalization group representation of both tori by one local effective action, so that the bulk cancels as in Proposition 6.1. Stability bounds of the form exp(-E_- |T|) <= Z <= exp(E_+ |T|) are not enough, by Proposition 4.3.

**For the lead (I edited no other file).**
- (E1) has no norm, no eigenvector and no twist. If it is not on file, Proposition 2.4 is a short Lean lemma on top of the trace facts of Stage 4, and the seed could then be stated with `Wilson.partition` only. Proposition 3.1 gives the same statement as a mean over two independent typical slices.
- Remark 4.0: `ExpClusters` accepts any mixing criterion at one cutoff, because C can depend on j. A criterion at a few correlation lengths is enough for (T-B). The seed of (T-A) sits at about 10^4 correlation lengths because of the constants 512 and 1024.
- Lemma 2.7, remark: `ExpClusters` is stronger than a gap of the limit. A weaker input with an additive ε is enough. This matters only if a later method gives the limit gap without the lattice gap.
- Guide only, not a proof step: the integrand ā_(4w) - ā_(2w) of Lemma 2.6 is a difference of mean plaquettes on two tori. It can be measured.
- Not done: no Lean was written or compiled; no numeric job was run; no paper was read in full (four references were checked on the web for their data, the others are recalled); the reading assumptions RA1-RA5 were not checked against the imported Lean files (closed folder); novelty was not checked (closed folder).

## 7. Labels

- PROVED (under RA1-RA5): Lemmas 2.1, 2.2, 2.3, 2.5, 2.6; Propositions 2.4, 3.1, 4.3, 6.1; Lemma 3.2; items (N4), (N5); the product rule in (N3).
- PROVED from CITED results: Lemma 2.7 in finite volume; (N1).
- CITED: transfer operator and positivity (Lüscher 1977; Osterwalder and Seiler 1978); massless 4D U(1) (Guth 1980; Fröhlich and Spencer 1982); strong-coupling expansion; Dobrushin and Shlosman 1985; Lüscher 1983 (small volume).
- ARGUED: the size 1.15 x 10^4 / m of the seed; the thermal and Casimir readings; Remark 4.0 as a consumer; (N6); the fixed-lattice growth of R; the infinite-volume form of Lemma 2.7.
- BELIEF: 5D SU(2) at large β; the adjoint-Higgs Coulomb phase.
- GUESSED: nothing is used as a step.

RESULT: no proof of MNeutralAll or ExpClusters and no attack found (clean negative). PROVED, under the stated reading of the imported Lean names: the seed follows from one inequality between two periodic Wilson partition functions, (E1) Z(N^3 x 2w)^2 <= (29/25) Z(N^3 x 4w) with N = ℓ L^K, w = floor(N/1024), β = β_K (Proposition 2.4), with exact integral, overlap and crossed-channel forms (Lemmas 2.6, 3.2, Proposition 3.1), and ExpClusters is exactly a lattice spectral-support statement with no slack in C (Lemma 2.7). First open estimate: (E1) for all K >= K_0 at one ℓ; it is equivalent to the seed up to a square (Lemma 2.5), its first step (bulk cancellation, Proposition 6.1, and the strong-coupling part of the integral) is written, and it stops at every coupling above the strong-coupling radius. Obstruction, quantified in (N1)-(N7): group-blind, dimension-blind, sector-blind, bulk-lossy, one-level, perturbative-range and symmetry-only arguments cannot give the seed; no small parameter is known at the scale of the correlation length. Tests for the best candidate C4 (contraction at one block scale): (g1) pass, (g2) pass on belief, (g3) pass, (g4) pass, (g5) pass, (g6) fail (consumer exists, no carry, no method at order-one coupling); for C1 (thermal forms): (g1)-(g5) pass, (g6) fail (equivalent to the seed). Open: everything on the seed itself; novelty against the lane files was not checked (closed folder).
