lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T16:55Z

# bridge-check: check of `library/d2-d4.md`, `library/s4-s6.md`, `library/cone-o6.md`

Queue row 205. Started 2026-11-04T04:55Z, finished 05:15Z. Verdicts: all three notes ADVANCE, first failing step none (Sections 1-3); moved nodes and bookkeeping in Section 4.

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

1. Section 3, last paragraph: "a fixed bump f ≥ 1 on a cube" must also be nonnegative everywhere. Otherwise Σ_p f(x(p)) can cancel. The outline says "a fixed nonnegative bump of nonzero integral" (SA L4189-4190).
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
- **Section 3, (4)-(6), one subsequence and moving tests: ADVANCE.** This is the outline's diagonal extraction principle (SA L479-516). The telescoping bound (4) uses only containers that fit in radius-R balls with mutual distance δ. The Cauchy argument through a fixed approximant is correct, and so is (6) for moving tests.
- **Section 4, (7)-(11), invariance, mirrors, one-point constant, cumulants: ADVANCE.** I checked these steps.
  - The rounding offsets are θ_{c_j}x - θ_c x = 2(c_j - c)e_μ for a coordinate mirror and (c_j - c)(e_μ ± e_λ) for a diagonal mirror. Lattice diagonal mirrors need c_j ∈ a_j Z, as the note says.
  - The plaquettes sampled by F lie in the open half once |c_j - c| + √2 a_j/2 is below the mirror gap.
  - Centering covariance uses the reflection invariance of ν_j at Σ_j (S1g).
  - The concatenated pairs are separated, as in SA L536-544.
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
  - These are the outline's QF orders with α = 5: k_* = A+15 = 20 (SA QF1-QF2, L24939-24956), without the factorial.
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
2. Section 6 applies (18), a bound for unit-radius supports, to the slot functions χ e_v. Their supports are the expanded cubes, of side O(ℓ) with ℓ ≤ 1/1024, so the bound applies. The note does not state the inner side, the expanded side and how they relate to the period 8ℓ. Any choice works in which each expanded cube meets no other period-8ℓ copy of its inner cube (in one coordinate: inner side + expanded side < 16ℓ), for example sides 2ℓ and 4ℓ. With those sides the expanded cubes on supp D_r are at least 56ℓ_r ≥ h_r/2 apart in sup distance. The note should state one choice.

What this does not show: E1 (existence of the first-passage cutoff data) and D1 behind S3. The note says so.

## 3. `library/cone-o6.md` (T0's O6, the spectral cube cone)

**Verdict: ADVANCE as an implication from the Result of `library/s4-s6.md` (O4, O5 and the position-independent bound (2)). First failing step: none.** Checked line by line by Claude against YM3_I Lemma IV-28-17 and Proposition IV-28-21 (Y3 L75480-75566, fetched by URL at the pinned commit).

Per section:

- **Section 2, the diagonal Hilbert space H_u: ADVANCE.** This is Y3 IV-27-22 with normal u = (e_4+e_j)/√2. I checked these steps.
  - Cross distances do not shrink under τ_{tu}: |y - x + 2tu|^2 = |y-x|^2 + 4t u·(y-x) + 4t^2 ≥ |y-x|^2 when u·x < 0 < u·y. So s4-s6 (2) gives a_F(t) ≤ C_F.
  - θ_u τ_{tu} = τ_{-tu} θ_u (θ_u u = -u) gives symmetry. Tangential τ_{sv} preserves q_u, since θ_u v = v and u·v = 0.
  - The halving argument and H_u = -log T^u_1 ≥ 0 are correct, as in s4-s6 Section 5.
- **Section 3, the measure estimate: ADVANCE.** This is Y3 IV-28-17. I checked these steps.
  - |e^{-sw-s'w̄}| = e^{-(s+s')E/√2} ≤ 1, so Fubini holds.
  - In (2), ∫c̄(s')e^{-is'y}ds' = conj(p(-iy)) = p^♯(y), and no commutation is used.
  - The Gamma transform and the hand proof of Γ(α) ≠ 0 are correct: the Beta integral by parts, dominated convergence with (1-s/N)^N ≤ e^{-s}, the convergent harmonic difference, and |log(1+z) - z| ≤ |z|^2 for |z| ≤ 1/2, from the displayed integral identity.
  - The two suprema are η^{-ε} on x ≥ 0 and η^{-ε}e^{|κ|π/2} on iℝ, since |(z+η)^{-α}| = |z+η|^{-ε}e^{κ arg(z+η)}.
  - Fatou in ε, then in η, is correct.
  - μ{arg w ≥ π/4+δ} ≤ Ce^{-2κδ} → 0, and since Re w ≥ 0 the union over δ is exactly {|q| > E}.
- **Section 4, two reflections: ADVANCE.** I checked these steps.
  - As point maps, r = θ_u θ sends (x_j, x_4) to (x_4, -x_j). So u·rx = (x_4 - x_j)/√2, and W_j and r(W_j) lie in {u·x > 0}.
  - θ_u(θ_u(θF)) = θF holds for either action convention, since both maps are involutions.
  - Both equalities in (6) are correct. The first uses t = (s+s')/√2 ≥ 0 and x = (s-s')e_j/√2 in s4-s6 (17). The second is the defining form q_u. Every concatenation is separated, because θF̄ lies in {x_4 < -|x_j|} and τ_{su+s'v}F lies in {x_4 > 0} ∩ {u·x > s}.
  - The large-time shift into W_j, the commutation of the spectral projections with T_R, and injectivity of T_R give Π_j = 0.
  - (7) and (8) follow from |p_j| ≤ E almost everywhere for μ_ψ.
- **Section 5 and Result: CORRECT-NO-ADVANCE.** The comparison uses only the (x_4, x_j) plane. In d = 4 there are two spectator coordinates and three generators, and nothing else changes.

Route note (for the lead): the outline's own cube-cone proof (SA HB8-HB15, L25736-25904) reads a lattice carrier sinh(E/2) ≥ |sin(p/2)| "established in the plateau argument", which is node S12. The Y3 continuum route checked here reads only O4 and O5. So O6 does not wait on S12 or `library/cluster-port.md`, as the skeleton line for O6 already says.

Defects: none that break a statement. Minor point:

1. The sign convention of P_j is not fixed in s4-s6 (17) or here. The first equality of (6), with w = (E - ip_j)/√2, needs U_x = e^{ix·P}. With the opposite sign, push forward by (E,p) ↦ (E, -p_j), as Y3 does with ε q_k. The conclusion is symmetric in p_j, so nothing changes.

## 4. What moved, bookkeeping, what stays open

**Moved (FINISH item 0).** Skeleton nodes S2, S3, S4 and S6, and T0's O1, O2, O4, O5 and O6, move from "cited" to "proved by Codex, checked by Claude, first failing step none". Each is an implication from the inputs below. Every proof is a written hand argument. No step rests on a computed value.

| Note | Nodes | Verdict | Premises read |
|---|---|---|---|
| `d2-d4.md` | S2 (D2), S3 (D4, G4) | ADVANCE, first failing step none | full D1 with its rooted GS geometry; S1d at coordinate link planes on cubic tori; S1g |
| `s4-s6.md` | S4, S6; O1, O2, O4, O5 | ADVANCE, first failing step none | E1's cutoff sequence; S3 in the explicit form of `d2-d4.md` (8)-(10); S1g |
| `cone-o6.md` | O6 | ADVANCE, first failing step none | the Result of `s4-s6.md` (O4, O5, bound (2)) |

**Bookkeeping for the lead** (no other file edited here):

1. `t0-skeleton.md` S2: add S1g to the inputs, since (4) uses the reflection invariance of ρ. S1e is rebuilt in `d2-d4.md` Section 2 from S1d.
2. `t0-skeleton.md` S1d says "coordinate case written in upper-chain Lemma 1.1". That lemma is site-plane RP only (`parts/upper-chain.md` L234). The chessboard here, like SA (ST1), cuts at link planes and needs the crossing-plaquette kernel. That case is the "coordinate bond cut" paragraph of `library/am1-port.md` Section 3 (Codex), the gauge-averaged Gram kernel ∫k_S(u, w·u') dw. I read that paragraph and it is correct, but the line-by-line check of `am1-port.md` stays with row 206.
3. `t0-skeleton.md` S4: add S1g (mirrors, invariance) and E1 (the cutoff sequence) to the inputs.
4. `t0-skeleton.md` O2 and O5 are marked "cited". `s4-s6.md` Sections 2-4 prove them as implications from S1g, with this check.
5. All three notes give D1's first open input as "C1/OH1". That pointer is out of date: `library/p2-floor.md` (in progress) records C1 (P1) as proved by Codex and checked by Claude. D1 itself stays open.

**Stays open.** The premises of this chain:

- D1 (rank 10): open. The floor's (P2)-(P3) are in `p2-floor`, and OH4's inputs are in `d1-floor.md` Theorem U.
- E1, the first-passage cutoff data: open.
- S1g and the bond-cut case of S1d: both in `am1-port.md`, proved by Codex and not yet checked (row 206).

Factorial growth (E0', `growth-qf3.md`) is not checked here. It belongs to `gates/cluster-check.md`.

## Result

Kind: a check of Codex's rebuilds of proofs that Sussman-Alpoge give in detail (SA ST1-ST15, GS1-GS13, CC1 and the compactness theorem L24889, HB1-HB7, QF1-QF2; YM3_I IV-27-22, IV-28-17, IV-28-21). Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

`library/d2-d4.md`, `library/s4-s6.md` and `library/cone-o6.md` were checked line by line by Claude. First failing step: none in any of the three. Each holds as an implication from its stated premises. The defects found are wording and bookkeeping only: a nonnegative-bump condition, the sign convention of P_j, and the box geometry in `s4-s6.md` Section 6. None breaks a statement.

Finished 2026-11-04T05:15Z.
