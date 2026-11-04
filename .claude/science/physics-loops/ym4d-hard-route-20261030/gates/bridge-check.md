lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T16:55Z

# bridge-check: check of `library/d2-d4.md`, `library/s4-s6.md`, `library/cone-o6.md`

Queue row 205. Started 2026-11-04T04:55Z. Work in progress; sections are added as they are written.

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, at branch commit `62242b86b`. One reading by one other model of three Codex notes. This is not an audit and grants no status. Sussman-Alpoge outline read at `31a47c543775` (`YM4_sketch_500.tex`, fetched by URL into a scratch folder, sha1 `107abaef`). Credit: the arguments checked here rebuild Ethan Sussman and Levent Alpoge's outline (with Claude and Codex as authors of their text), Sections all-state-source-transfer (SA L23622-24040, ST1-ST15), graded-rooted-source (SA L24042-24360, GS1-GS13), continuum compactness and the Euclidean-Hilbert bridge, as each section says.

Kind of result (FINISH item 9): a check of Codex's rebuilds of proofs the outline gives in detail. Each step was redone by hand, and each was compared with the outline passage it ports.

## 1. `library/d2-d4.md` (D2, D4, G4; skeleton S2, S3)

**Verdict: ADVANCE as an implication from full D1, S1d (finite-torus link reflection positivity) and S1g. First failing step: none.** Checked line by line by Claude.

Per section:

- **Section 2, (1)-(4), chessboard and domination: ADVANCE.** I checked these steps.
  - Nonnegativity of (1) holds by torus reflection positivity at a pair of opposite link planes.
  - The complex one-direction bound is correct. Reflection Cauchy-Schwarz gives T(σ)^2 ≤ T(σ_+)T(σ_-). The normalisations multiply, N(σ_+)N(σ_-) = N(σ)^2. Both reflected values are nonnegative, so both maximise. Retaining the half that starts at a constant run of length h ≤ q/2 doubles the run, and a run that contains a half reflects to a constant filling. A constant filling has normalised value Z_j/(Z_j+ε) < 1.
  - The four directions compose. Each dissemination is the reflection group's unique map between cells, so the copies agree.
  - The triangle inequality, homogeneity and p(F̄) = p(F) are correct.
  - (3) is correct. The count is C(ℓ/a)^3 boundary plaquettes, with each Wilson factor in [e^{-2β}, 1], for the numerator and the denominator. The source factors are unchanged. Dividing by N = (ℓ/l)^4 gives the stated error.
  - The log(1+tG) step is correct, with limits in ℓ first and then t ↓ 0.
  - The coarse-cell step in (4) is correct. The coarse reflections lie in the fine reflection group, which acts simply transitively on the fine cells. So the coarse dissemination of ∏F_C is the fine product with the copies of F_C on the coarse orbits and 1 elsewhere, and (2) with p(1) = 1 gives (4).
  - This is SA (ST1)-(ST4) and (AM5)-(AM7).
- **Section 3, (5)-(10), normalisers, D4, G4: ADVANCE.** I checked these steps.
  - The stability cost divides to (C_+ + C_-)l^4.
  - The odd-cell terms g(z̄) become the holomorphic conj(g(z̄)) with the same real part, so Re of the retained sum is N Re E_{C,ℓ}. No covariance of the D1 terms is needed, because E is defined as the average over cells.
  - A discarded nonzero term has D^+ meeting a support copy and a face. So diam D^+ ≥ b and m ≥ b/(C a_s) - 1.
  - The fixed-cutoff local bound in ℓ, the Montel selection, and the subsequence that does not depend on the state are correct.
  - The offset count is correct.
  - The Cauchy estimates in (8) and (9) are correct. A point term has a zero mixed derivative. A domain that sees all n supports has diameter ≥ d. The scale sum is at most C max(1, d^{-4}).
  - The log-partition identity in (10) is correct. Ordered j-block partitions weighted by (-1)^{j-1}/j give (-1)^{|π|-1}(|π|-1)!.
  - The partition improvement to C(R+1)^4 is correct.
  - The plaquette consequence is correct. S1g makes Δ the same for all plaquettes, since the lattice isometries act transitively on plaquettes.
  - This is SA (ST5)-(ST15).
- **Section 4, (11)-(14), rooted counts: ADVANCE.** I checked these steps.
  - A grid edge meets a closed cube only at a corner or along a cube edge, so every cube of X contains a tree vertex, and a corner of Q is a tree vertex (also when m = 0).
  - There are 16 corners. The depth-first closed walk gives 8^{2m}. There are at most 16(m+1) candidate cubes, so 2^{16(m+1)} subsets.
  - (12) follows, because X^+ lies within C M a_s of X.
  - The three ranges of (13) are correct.
    - Range a_s ≥ η uses the global count, (η/a_s)^4 summed geometrically. The ball count would give log(1/η) here, which is why the global count is needed.
    - Range δ ≤ a_s < η has a bounded cost per scale, over C(1+log(η/δ)) scales.
    - Range a_s < δ has the forced size m ≥ cδ/a_s - C.
  - So the cell loss is polynomial, Q_0(η/δ)^p. This is SA (GS1)-(GS4).
- **Section 5, (15)-(22), D2: ADVANCE.** I checked these steps.
  - The offset count is n(4δ/a+2) ≤ η/(16a) + η/(512a) = (33/512)η/a, using a ≤ δ/16 = η/(1024n).
  - Distinct tests lie in distinct cells, because a side-η cell has diameter 2η ≤ d̄/8 < d.
  - (17) is a product polydisc, since each chessboard factor carries one univariate source.
  - (18): the derivative ∂_S at 0 of ρ(∏ e^{z_i O(v_i) - E_i(z_i)}) is ρ(∏ X_i), because E_i(0) = 0.
  - Expanding over the 2^n subsets gives 2^n ∏ Q_i t_{v_i}/r. Summing over the piece choices gives (19), with δ^{-1} < 1024 L n/d̄.
  - The coarse-mesh case a > δ/16 is correct.
  - k = ⌈p⌉+5 works, since n^n ≤ e^n n!.
  - The composition count in (21) is correct: Σ_{|π|=m} ∏|D|! = n! C(n-1,m-1)/m!.
  - This is SA (GS5)-(GS13).
- **Section 6 and Result: CORRECT-NO-ADVANCE.** The remarks on d = 4 are right: δ^{-4} from the partition count times δ^{-1} from the norm gives d^{-5n}. So is the ST6-only obstruction, which is the same as the outline's remark at SA L4117.

Defects: none that break a statement. Minor points for the note's owner:

1. Section 3, last paragraph: "a fixed bump f ≥ 1 on a cube" must also be nonnegative everywhere. Otherwise Σ_p f(x(p)) can cancel. The outline says "a fixed nonnegative bump of nonzero integral" (SA L4183).
2. Skeleton bookkeeping (for the lead): node S2 in `library/t0-skeleton.md` lists inputs D1 and S1e. D2 also reads S1g, through the domination (4), whose proof uses the reflection invariance of ρ. The note states this correctly ("Conditional on full D1, S1e and S1g").
3. The chessboard input is S1d, finite-torus reflection positivity at link planes. The note rebuilds S1e from S1d in its complex form, so S1e is not a separate premise.

What this does not show: D1 itself, which the note marks as the open upstream input (first C1/OH1 in `library/d1-floor.md`).

## 2. `library/s4-s6.md` (S4, S6; T0's O1, O2, O4, O5)

**Verdict: ADVANCE as an implication from the supplied cutoff sequence (E1), S3 in its explicit form (`d2-d4.md` (8)-(10)) and S1g. First failing step: none.** Checked line by line by Claude.

Per section:

- **Section 1, (1)-(2): ADVANCE.** This is the moment-cumulant identity with shifted singletons, as in SA (ST15). Complexification costs 2^n, which M_n absorbs.
- **Section 2, (3), volume-first Gibbs states: ADVANCE.** I checked these steps.
  - X is compact metric, and the cylinder functions are dense.
  - C(X) is separable, and Riesz gives the weak limit.
  - The DLR identity passes to the limit. Once the torus is large enough that the projection is injective on supp F ∪ W ∪ N(W), the lifted γ_W F is the torus kernel applied to the torus function. So μ_N(γ_W F) = μ_N(F) holds at every large torus and passes weakly. Properness then gives the conditional form.
  - Invariance under aZ^4 ⋊ W_4 passes from the tori.
  - This is SA (CC1) and following (L24376-24420).
- **Section 3, (4)-(6), one subsequence and moving tests: ADVANCE.** This is the outline's diagonal extraction principle (SA L479-520). The telescoping bound (4) uses only containers that fit in radius-R balls with mutual distance δ. The Cauchy argument through a fixed approximant is correct, and so is (6) for moving tests.
- **Section 4, (7)-(11), invariance, mirrors, one-point constant, cumulants: ADVANCE.** I checked these steps.
  - The rounding offsets are θ_{c_j}x - θ_c x = 2(c_j - c)e_μ for a coordinate mirror and (c_j - c)(e_μ ± e_λ) for a diagonal mirror. Lattice diagonal mirrors need c_j ∈ a_j Z, as the note says.
  - The plaquettes sampled by F lie in the open half once |c_j - c| + √2 a_j/2 is below the mirror gap.
  - Centering covariance uses the reflection invariance of ν_j at Σ_j (S1g).
  - The concatenated pairs are separated, as in SA L527-532.
  - (9) is exact: m_{j,1}(f) = δ_j Σ_p f(x_p).
  - The Riemann-sum error is C(R+1)^4 a_j ||∇f||_∞, since a side-a_j cube has diameter 2a_j.
  - In (10), c_j → σ_1(f_*), and then σ_1(f) = c∫f for every f.
  - (11) is correct.
- **Section 5, (12)-(17), compact Hilbert bridge: ADVANCE.** This is SA (HB1)-(HB7) step for step. I checked these steps.
  - The bound a(s) ≤ C_F, uniform in s ≥ 0, comes from the position independence in (2), with separation min(d, 2ε).
  - The iteration a(t) ≤ a(0)^{1-2^{-r}} C_F^{2^{-r}} is correct.
  - Self-adjointness and positivity hold, since T_t = T_{t/2}^2.
  - Strong continuity follows from (4) and (7).
  - ker T_1 = 0 by halving. So H = -log T_1 ≥ 0, and T_t = e^{-tH} holds by uniqueness of positive square roots at dyadic t and then by continuity.
  - Separability is correct.
- **Section 6, (18)-(23), per-order diagonal-flat extension: ADVANCE.** I checked these steps.
  - The separation loss in `d2-d4.md` (10) is only D_n's max(1, δ^{-4}). Q depends on n and R, not on δ. So (18) holds.
  - The Fourier bound with (1-π^{-2}Δ)^4 in each slot is correct. The per-slot sum Σ_v (1+|v|^2)^{-4}(1+|v|) converges in Z^4.
  - (19) is correct: (h/2)^{-5n} from (18) times ℓ^{-n} = (64/h)^n from the C^1 norms gives h^{-6n}.
  - The Taylor order is correct: 10n+2 on top of ≤ 8n gives 18n+2 ≤ 20n.
  - The position sum is correct: (1+Σ|x_i|^2)^{-10n} ≤ ∏(1+|x_i|^2)^{-10} gives B_n h_r^{-4n}.
  - So (21) carries h_r^2, and the layer sum converges.
  - These are the outline's QF orders with α = 5: k_* = A+15 = 20 (SA QF1-QF2, L24970-25000), without the factorial.
  - Density of the separated tensors, uniqueness and (23) are correct.
  - The well-definedness on overlapping product boxes is sketched in one sentence. The step holds if one reads it as follows. For u compactly supported in the open box B ∩ B', take a smaller frame B'' whose expanded cubes lie in B ∩ B'. Its Fourier tensors are evaluated by both T_B and T_{B'} as σ_n, and (19) passes the equality to u. Independence of the partition then follows from the products χ_k χ'_m.
- **Section 7, (24)-(25), H2 on positive-time sequences: ADVANCE.** I checked these steps.
  - The cross-diagonal flatness argument in three cases (time > 0, < 0, = 0) is correct.
  - p_s(f⊗g) ≤ p_s(f)p_s(g) is correct.
  - Approximation by tensors strictly above time zero gives Q ≥ 0 from (8).
  - The unitary identification with (12) uses common mollification, which keeps the gaps, and (4).
  - Translations intertwine through the dense subspace, so no uniform bound on translated seminorms is needed.
- **Section 8 and Result: CORRECT-NO-ADVANCE.** The remark about porting the three-dimensional Fourier order 4n+1 is correct: the majorant |v|^{-(3n+1)} has shell sum Σ r^{4n-1-3n-1} = Σ r^{n-2}, which diverges. Eight derivatives per slot repair it.

Defects: none that break a statement. Minor points:

1. Skeleton bookkeeping (for the lead): node S4 lists input S3 only. Its mirror and invariance clauses also read S1g (Section 4), and its existence reads E1's cutoff sequence. The note says both.
2. Section 6 calls (18) a bound for "unit-radius supports", but the slot functions χ e_v are supported in expanded cubes of side up to 8ℓ ≤ 1/128. That is inside radius one, so the bound applies. The inner side, expanded side and period (8ℓ) are not all stated. Any choice with inner side + expanded side ≤ 8ℓ and expanded cubes h/2 apart works. The note should state one.

What this does not show: E1 (existence of the first-passage cutoff data) and D1 behind S3. The note says so.
