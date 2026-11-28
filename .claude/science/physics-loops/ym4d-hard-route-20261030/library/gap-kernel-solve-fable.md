lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-28T21:15:14Z

# gap-kernel-solve-fable (FINISH row 1674): closed-folder solve from the Lean hypothesis

Started 2026-11-28T09:15:14Z (date -u). Worker: Mac mini Claude worker 1, Claude Fable 5.2, max. Base commit 9a626d7f6. No commit, no push; the relay copies this file.

Status: IN PROGRESS. Each section is written when its step is finished. The last section in the file is the current state.

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

then `NeutralRankOneTest` holds on side N at β. The same holds with Z^0 in place of Z (then RA3 and Lemma 2.1 are not needed: use the top neutral eigenvector and its eigenvalue).
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
