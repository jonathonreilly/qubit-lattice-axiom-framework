lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T18:45Z

# h-walk-fix: region-trace locality and single-term covariance of statement 5

Queue row 123. Pinned at commit 8fac7b660 on `claude/ym4d-hard-route`. Same-model work (Claude Opus 5.5, max). It has not been gated and has no status.

Status: in progress. Sections are written as they are finished.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session, repository commit 8fac7b660. Same-provider text: it repairs Claude's `h-walk.md` against Codex's `gates/h-walk-gate.md`. Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder (SHA-256 d7f77d4d…4d6f, the same file as rows 103–126) and not copied here; SA nnnn are its line numbers. No numeric job was run, so the numeric lock was not needed. No subagent. Every step is written by hand.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for statement 5 and its clauses (SA 10309–10343), mechanisms (f), (g), (i) (SA 10540–10560), the bond-midpoint convention for the hypercubic tensor (SA 13191–13200), and the consumers listed in §1. Tadeusz Balaban for the cut-down-sequence method (CMP 99 (1985) 389–434, pp. 408–410), used through `h-walk.md`. OpenAI Codex for the counterexample and the visible repairs in `gates/h-walk-gate.md` §§3, 8 that this note completes.

## 1. Who reads W(c)–(d), T(d) and H3 on our chain

The failed clauses (`gates/h-walk-gate.md` §§3, 6, 8, 10 items 1, 4) are:

- **(RT) region-trace locality and canonicity:** W(c)'s "depends on S only through Omega_i ∩ [[omega]]", W(d)'s "same function under a translation carrying the data on the hull", T(d) (which inherits both), and H3's "depends on the regions only through their traces on [[omega]]" and "same function for two sequences, tori or cutoffs related on the hull";
- **(IC) single-term isometry covariance:** H3's "covariant under the lattice isometries that preserve the level-(k+1) M_1-grid, the regions and Omega_{k+1}".

The field-locality and field-holomorphy part of W(c), and the gauge-covariance part of W(d), passed the gate (§6) and are not at issue.

| Consumer | Position on our chain | What it reads | Failed clause read |
|---|---|---|---|
| `a2-full.md` Theorem VI, in the collared form of `gates/h-walk-gate.md` §9 | M (A2 item 3) | (H1), (H2) with root support, the field carrier, field holomorphy on a fixed region sequence | none (the gate's §9 says so; checked) |
| `o1-decoupled.md` Theorem B (a), (d) | N (WF room, rank 4) | field part of W(c), gauge part of W(d) | none |
| `o1-decoupled.md` Theorem C, through its Lemma C1 | N (removed-map comparison) | the term identity for walks of two **different** sequences (S and the box sequence) that agree on G^♯ | **(RT)** for W, in an instance, proved in place |
| `o1-decoupled.md` §3 (H-field), "the same walk-term argument" for H_1(s), 𝔊(s) | N | the same identity for the tree walks of Theorem T | **(RT)** for T(d), in an instance, not proved there |
| `wf-room-2.md` (WF7) removed fields | N | Theorems C, D of `o1-decoupled.md` | **(RT)**, through the row above |
| Package C, SA 17548–17556: terms with domain X ⊂ Λ_{j+1} "are built from walks and fields inside X, so the regions do not affect them … the same for every label"; SA 19523 (e): "a carried term is literally unchanged" | H (Package C, carried) | walk terms of the fluctuation form whose hull lies where two labels agree are the same function | **(RT)** for H3 |
| (3b), SA 7837: "A term localised in X is assembled from walks, potentials and tests within X … depends on neither the torus nor the cutoff"; its users: the infinite-lattice companion of a pointed member (SA 32651–32652), the torus comparison (ET9)–(ET10) (SA 26918–26930) | R (D1 producer), E | identity of terms on all tori with room | **(RT)** for H3 and W(d) |
| R9's transport, SA 10404–10405 and 10567: "transports the solution whenever the assigned walk data are transported" | N | translation transport of the specified walk data (`o1-decoupled.md` Definition D uses Theorem W at j = 0) | **(RT)** for W(d) |
| Requirement B2, SA 3937–3950: "the individual member's pointed totals are covariant under unit translations and the full hypercubic group"; SA 7581: pointed totals covariant under all isometries, "part of the definition of renormalised" | E (marginal coefficient, merged into P1), N | covariance of each localisation domain's activity, hence of the walk terms assigned to it | **(IC)** |

`sa-2.13-2.md` (line 128) and `wf-room-2.md` (line 413) mention `h-walk.md` without reading any of its clauses.

**Conclusion of the listing.** Consumers exist. Inside our library, only `o1-decoupled.md` reads (RT), and it reads an instance that its Lemma C1 proves. The outline positions that our route carries (H, N, R, and E through P1) read (RT) and (IC) in full. So the item is not stopped, and §§2–4 do the repair.

**Mechanism (i)'s symmetrisation does not replace (IC).** Its Haar mean is over real **gauge** transformations, and its mean over translations, push-forward and Montel limit (SA 10560) give one assignment for all tori. None of these averages over coordinate reflections or permutations. So the outline's own construction has to supply single-term isometry covariance, and the outline itself moves to bond midpoints for this reason when it reaches the hypercubic tensor (SA 13191: "Under reflections, lower bond starts undergo a direction-dependent integer displacement … move first to bond-midpoint coordinates").

## 2. Region-trace locality: the read set of a normalised cutoff (repaired (C5))

**Setting.** As in `h-walk.md` §3: L odd and large, M_1 and R_1 powers of L, rho = R_1 M_1, level-k units with xi_j = L^{j-k} and eta = xi_0. A sequence is *separated* in the outline's sense: each Omega_j is a union of level-j M_1-cubes and dist_∞(Omega_j^c, Omega_{j+1}) > R_1 M_1 xi_j (SA 10115-10117). Layers are L_j = closure(Omega_j \ Omega_{j+1}), with Omega_{k+1} := ∅ for the depth-k sequence when it is used alone. The level-j M_1-grids are fixed, closed and nested: each level-(j+1) M_1-cube is a union of L^4 level-j M_1-cubes. The M'-grids refine them. K_j is the set of level-j M_1 grid cubes contained in L_j, and K is the union of the K_j. The profiles p, q and the cutoffs phi_κ, θ_κ, h~_κ are those of `h-walk.md` §3, with one added choice of the even profile p, fixed once:

    p >= 1/2 on [-5/8, 5/8].                                                  (2.0)

This is compatible with p = 1 on [-1/2, 1/2] and p = 0 off [-3/4, 3/4]. It is used only in §4.

**Added gap hypothesis.** It replaces R_1 >= 64L in (G0) of `h-walk.md` and is the one `o1-decoupled.md` already assumes:

    (G0')  R_1 >= 8 L^3.

R_1 is a power of L chosen after L, so this costs nothing in the order of constants.

**Enlargements.** For a level-i M_1 grid cube κ (in K or not), with centre c_κ:

- κ^♭ is the closed concentric cube of side 4L M_1 xi_κ;
- κ^♯ is the closed concentric cube of side 8L^2 M_1 xi_κ (`o1-decoupled.md` Definition D).

For L >= 3 these satisfy κ^(4) ⊂ int κ^♭ and κ^♭ ⊂ κ^♯.

**Candidates.** Cand(κ) is the set of level-i' M_1 grid cubes λ with i' ∈ {i-1, i, i+1} ∩ [0, k] and λ^(1/4) ∩ κ^(1/4) ≠ ∅. This set is defined from κ and the fixed grids alone, so it is the same for every sequence. That covers a cube that is present in one sequence and absent in another.

**Agreement.** Two separated sequences S = (Omega_j) and S' = (Omega'_j) on the same torus, with the same grids, *agree on* a set G if Omega_j ∩ G = Omega'_j ∩ G for every j. §3 extends this to different tori.

**Lemma N0 (membership is a trace test).** A level-j M_1 grid cube λ is in K_j iff λ ⊂ Omega_j and λ ⊄ Omega_{j+1}. So membership depends only on Omega_j ∩ λ and Omega_{j+1} ∩ λ.

*Proof.* Omega_j is a union of level-j grid cubes, and two distinct cubes of one grid have disjoint interiors. So either λ ⊂ Omega_j or int λ ∩ Omega_j = ∅. Omega_{j+1} is a union of level-(j+1) cubes, each of which is a union of level-j grid cubes. So either λ ⊂ Omega_{j+1} or int λ ∩ Omega_{j+1} = ∅. If λ ⊂ Omega_j and int λ ∩ Omega_{j+1} = ∅, then int λ ⊂ Omega_j \ Omega_{j+1}, so λ = closure(int λ) ⊂ L_j. Conversely, let λ ⊂ L_j. Then λ ⊂ Omega_j, since L_j ⊂ Omega_j and Omega_j is closed. If also λ ⊂ Omega_{j+1}, every point of int λ has a neighbourhood inside Omega_{j+1}, which misses Omega_j \ Omega_{j+1}. Then that point is not in L_j, a contradiction. ∎

**Lemma N1 (level window).** Let κ ∈ K_i and κ' ∈ K_{i'} with |i - i'| >= 2, and put m = max(i, i'). Then dist_∞(κ, κ') >= R_1 M_1 xi_{m-1} = (R_1/L) M_1 xi_m.

*Proof.* Say i' >= i + 2. Then κ' ⊂ Omega_{i'}. By Lemma N0, int κ misses Omega_{i+1}, so int κ ⊂ Omega_{i+1}^c ⊂ Omega_{i'-1}^c, because i' - 1 >= i + 1 and the Omega's decrease. Separation gives dist_∞(Omega_{i'-1}^c, Omega_{i'}) > R_1 M_1 xi_{i'-1}. Pass to the closure of int κ. The case i >= i' + 2 is the same with the roles exchanged. ∎

**Lemma N (repaired (C5)).** Assume (G0') and L >= 3. Let κ be a level-i M_1 grid cube, and let S, S' be separated sequences that agree on κ^♭.

- (a) κ ∈ K_i(S) iff κ ∈ K_i(S').
- (b) Let κ ∈ K_i. The cubes of K(S) whose cutoff phi meets κ^(1/4) = supp phi_κ all lie in Cand(κ), and they are exactly the cubes of K(S') with this property. Hence θ_κ^S = θ_κ^{S'} as functions on the torus. h~_κ depends on κ alone.
- (c) The cut-down sequence of `h-walk.md` Lemma C is the same for S and S'. So is every object listed in (C2) at points of κ^(7/2): layers, tops, pillars, rows, omitted inward bonds and inner plaquettes.
- (d) Size. κ^♯ meets at most the layers L_{i-1}, L_i, L_{i+1} (and, when i = 0, the outside of Omega_0). On κ^♯ the density of d_B is at most L/xi_κ, and the d_B-diameter of κ^♯ is at most 16 L^3 M_1.

*Proof.* (a) Lemma N0, since κ ⊂ κ^♭.

(b) Let κ' ∈ K(S) with phi_{κ'} ≠ 0 somewhere on κ^(1/4). Then κ'^(1/4) ∩ κ^(1/4) ≠ ∅, so dist_∞(κ, κ') <= (M_1/4)(xi_κ + xi_{κ'}) <= (M_1/2) xi_m, with m the larger of the two levels. If the levels differed by 2 or more, Lemma N1 would give dist_∞(κ, κ') >= (R_1/L) M_1 xi_m >= 8L^2 M_1 xi_m. So the levels differ by at most 1, and κ' ∈ Cand(κ).

Every λ ∈ Cand(κ) lies in κ^♭. For λ of level i + 1, the condition λ^(1/4) ∩ κ^(1/4) ≠ ∅ gives |c_λ - c_κ|_∞ <= (3/4)(L + 1) M_1 xi_i. So λ lies in the concentric cube of half-side ((5L + 3)/4) M_1 xi_i <= 2L M_1 xi_i. Levels i and i - 1 give less.

By Lemma N0, membership of λ in K(S) is decided by Omega_{i'} ∩ λ and Omega_{i'+1} ∩ λ, which S and S' share. The first paragraph applies to S' as well, by (a). So both sequences have the same contributing cubes, namely Cand(κ) ∩ K(S) = Cand(κ) ∩ K(S'). On κ^(1/4) the denominator of θ_κ is the sum of phi_λ over these cubes, so it is the same function for both. Off κ^(1/4), θ_κ = 0 for both. h~_κ is a fixed profile centred at c_κ.

(c) Whether a point x lies in L_j depends only on the traces of Omega_j and Omega_{j+1} on a neighbourhood of x. int κ^♭ is an open neighbourhood of κ^(4), so the layers of S and S' agree on κ^(4). The indices i_0, i_1 of Lemma C, the boxes C_i (built from κ, κ^(7/2) and the M'-grids), and Omega^κ_i = Omega_i ∩ C_i with C_i ⊂ C_0 ⊂ κ^(4) are therefore the same for both. The objects of (C2) at x are decided within one pillar or row carrier of x, which is d_B-distance <= 4L. That is physical distance <= 4L^2 xi_κ < M_1 xi_κ / 2, so it stays inside κ^(4) when x ∈ κ^(7/2).

(d) κ^♯ extends κ by (4L^2 - 1/2) M_1 xi_κ. Since κ ⊂ Omega_i and dist_∞(Omega_i, Omega_{i-1}^c) > R_1 M_1 xi_{i-1} >= 8L^2 M_1 xi_κ by (G0'), κ^♯ misses Omega_{i-1}^c when i >= 1. Since int κ ⊂ Omega_{i+1}^c and dist_∞(Omega_{i+1}^c, Omega_{i+2}) > R_1 M_1 xi_{i+1} >= 8L^4 M_1 xi_κ, κ^♯ misses Omega_{i+2}. By the definition of |Γ|_B (SA 10123: density xi_j^{-1} on L_j for j >= 1, and xi_0^{-1} outside Omega_1), the density on κ^♯ is at most xi_{i-1}^{-1} = L/xi_κ, or xi_0^{-1} = 1/xi_κ when i = 0. A straight segment in κ^♯ has Euclidean length at most 2 · 8L^2 M_1 xi_κ, hence d_B-length at most 16 L^3 M_1. ∎

**Remark (the gate's counterexample against Lemma N).** In `gates/h-walk-gate.md` §3, κ has first-coordinate interval [-7s, -6s] with s = M_1 xi_j. The coarse cube λ = [0, Ls] × (tangential) has φ_λ(c_κ) > 0 for large odd L (the gate's L > 26). For L >= 23, λ^(1/4) meets κ^(1/4), so λ ∈ Cand(κ) ⊂ κ^♭. The two sequences of the counterexample differ on λ, so they do not agree on κ^♭, and Lemma N claims nothing about them. The counterexample also shows that a read set inside κ^(4) cannot work. A candidate of level i + 1 can reach (3/4)(L + 1) M_1 xi_κ from c_κ, beyond κ^(4) once L >= 6.

**Lemma N2 (the read set of a stage-2 coefficient).** Assume (G0') and L >= 3. Let κ ∈ K_i, and let c be a row whose location lies in κ^(7/2) (§4: its midpoint; for the base-point convention, its initial point). Every κ'' ∈ K whose cutoff θ_{κ''} is nonzero at the location of c has level within 1 of i. Moreover κ''^♭ lies in the concentric cube of κ of half-side 3L^2 M_1 xi_κ, which is inside κ^♯.

*Proof.* The location lies in κ''^(1/4) and in κ^(7/2), so dist_∞(κ, κ'') <= 4 M_1 xi_κ + (1/4) M_1 xi_{κ''} <= 5 M_1 xi_m. Lemma N1 and (G0') exclude a level difference of 2 or more, so xi_{κ''} <= L xi_κ. Then |c_{κ''} - c_κ|_∞ <= 4 M_1 xi_κ + (3/4) L M_1 xi_κ. Adding the half-side 2L M_1 xi_{κ''} <= 2L^2 M_1 xi_κ of κ''^♭ gives (2L^2 + 3L/4 + 4) M_1 xi_κ <= 3L^2 M_1 xi_κ for L >= 3. ∎

**What Lemma N changes in `h-walk.md`.** (C5) is replaced by Lemma N(b)-(c): the geometric read set of κ is κ^♭, not κ^(4). Everything in (C1)-(C4) is unchanged, and so are the local matrices, which do depend only on κ^(4), as the gate notes. The only object that reads further is the normalising denominator of θ_κ. Lemma N2 bounds what a stage-2 local model reads through the coefficient j^(0).

## 3. The repaired clauses W(c)–(d), T(d) and H3

**Geometric hull.** For a walk ω = (κ_0, ..., κ_n) of Theorem W, and for a tree walk of Theorem T (all its trunk and branch cubes), put

    [[ω]]^♯ := union of κ^♯ over the cubes κ of ω.

By Lemma N(d), [[ω]]^♯ lies within d_B-distance 16 L^3 M_1 of the cells X_κ ⊂ κ^♯ of ω. This is `o1-decoupled.md`'s set [[ω]]^+, which its Definition D already uses for the parameter monomial. The *field hull* is `h-walk.md`'s [[ω]] = union of κ^(4), enlarged by the read range of the coefficient, as in W(c). Its field part passed the gate (§6) and is not changed here.

**♭-local coefficients.** A row function j is *♭-local* if two things hold. First, for every κ ∈ K and every row c located in κ^(7/2), the value j(c) is the same for any two sequences that agree on κ^♯. Second, j(c) depends on the data within a fixed number of boxes of c, as in `h-walk.md` §6. The coefficient j = 0 is ♭-local. So is j^(0) of §7. At a row c it is the sum of j_{(κ'')}(c) = xi_c^{-4} <[h~_{κ''} S^G_{κ''} θ_{κ''}]_{Aν} e_c, J>_f over the κ'' ∈ K with θ_{κ''} ≠ 0 at c. Let S, S' agree on κ^♯. By Lemma N2 (for S and for S'), every such κ'' has κ''^♭ ⊂ κ^♯. So by Lemma N(a)-(c) the two sequences have the same such κ'', the same θ_{κ''}, and the same local inverse S^G_{κ''}, which reads κ''^(4).

**Grid translations between tori.** Let T, T' be tori in level-k units whose sides are multiples of the level-(k+1) M_1-grid, and U ⊂ T open. A *grid translation of U into T'* is an injective map ι: U → T' of the form π' ∘ τ ∘ (π|_Ũ)^{-1}. Here π, π' are the covering maps from R^4, Ũ is an open set that π maps injectively onto U, and τ is a translation by a vector of M_1 xi_k Z^4 (for Theorem H: of M_1 xi_{k+1} Z^4). Such a τ maps every grid of level <= k (resp. k + 1), every M'-grid, every lattice T^(j) and the fine lattice onto themselves, because these grids are nested inside the top one. ι *relates* two systems on U if ι(Omega_j ∩ U) = Omega'_j ∩ ι(U) for every j, and if the pair, the current, Y and the coefficient data correspond under ι on U. When T = T', a global translation is the special case. "Two tori with room" means that the U below has such a ι.

**Input (I4-tr), translation covariance of the building blocks.** The matrix entries of K[S, P, j], and of C_V, G^(2)_V, a and E^(2)[ψ], at a pair of unknowns are given by one local formula. The formula reads the sequence and the data within their finite stencils (range <= r_0, `h-walk.md` §4), and it is the same at points related by a grid translation. This is the translation case of the outline's covariance of its operators (SA 10340; Proposition 1a.1.11, SA 7380-7392), and it holds by construction for translation-covariant averages. It is not re-derived here. §4 states the isometry case (I4) separately, because it is weaker.

**Theorem W' (replaces W(c)–(d)).** Assume the hypotheses of Theorem W, (G0') and L >= 3, and let j be ♭-local. Let ω be a walk.

- (c') T_ω depends on the regions only through their traces on [[ω]]^♯. It depends on (P, J) and on the data entering j only through their values on the field hull. It is holomorphic on the local class there and real at real data (the gate-kept part of W(c)).
- (d') Let U ⊃ [[ω]]^♯ ∪ (field hull) be open, and let a grid translation ι of U into T' relate (S, P, j) on T to (S', P', j') on T'. Then ιω is a walk of S', and T'_{ιω} = ι_* T_ω. Here ι_* acts on unknowns by relabelling, and translations reverse no bond, so there is no twist. Gauge covariance as in W(d) is unchanged (gate §6).

*Proof.* (c') The factors of T_ω are h~_{κ_0}, S_{κ_0} = K_{κ_0}^{-1}, θ_{κ_0}, and R_{κ_l} = -[K_{κ_l}, h~_{κ_l}] S_{κ_l} θ_{κ_l} for l = 1, ..., n. Here [K, h~_κ] = [K_κ, h~_κ] because K and K_κ agree within r_0 of supp ∇h~_κ, which is the identity proof of Theorem W(a). Fix a cube κ of ω and two sequences S, S' that agree on [[ω]]^♯ ⊃ κ^♯.

- θ_κ: the same, by Lemma N(b).
- h~_κ: depends on κ alone.
- K_κ = K[S^κ, P^κ, j^κ]. The cut-down S^κ is the same by Lemma N(c). The coefficient j^κ is j on the rows of S^κ that are rows of S inside κ^(7/2), and 0 on the others. Those rows are the same by Lemma N(c), and the values of j on them are the same because j is ♭-local. The remaining entries of K_κ read the regions within O(1) stencils inside κ^(4). So K_κ is the same matrix, and so is S_κ.

Every factor is the same, hence so is T_ω.

(d') The same argument, read through ι. τ preserves every grid, so ι maps each cube, its enlargements κ^(t), κ^♭, κ^♯, Cand(κ), the profiles phi_κ and h~_κ, and the boxes C_i of the cut-down (built by rounding to an M'-grid) to the corresponding objects at ικ. Lemma N0 makes membership in K a trace test on the candidate itself, and the candidates lie in U. So ι maps Cand(κ) ∩ K(S) onto Cand(ικ) ∩ K(S'), and θ'_{ικ} ∘ ι = θ_κ on κ^(1/4). By (I4-tr), K'_{ικ} = ι_* K_κ entrywise, since both are finite matrices given by the same local formulas at corresponding points. The commutator factors follow in the same way. Since ι is injective on U, walks go to walks: X_{κ_{l-1}} ∩ X_{κ_l} ≠ ∅ is preserved. ∎

**Theorem T' (replaces T(d)).** Under the hypotheses of Theorem T and (G0'), every tree-walk term T^(1)_ω has properties (c') and (d') of Theorem W', with [[ω]]^♯ the union of κ^♯ over all trunk and branch cubes. So does every term of Corollary T: [T^(1)_ω]_{Aν}, [T^(1)_ω]_{νν}, and j^(1)_ω.

*Proof.* The trunk factors are those of Theorem W' at the ♭-local coefficient j^(0). Their region reads lie in κ_l^♯ for the trunk cubes κ_l, by the proof of (c') with Lemma N2. A vertex factor is -V_{β} h~_{κ_l} S^(0)_{κ_l} θ_{κ_l}. Its last three factors are trunk-type. V_β = K[S, P, j_β] - K[S, P, 0] is the j_β-linear part of K, a finite stencil operator around the rows of supp j_β ⊂ supp θ_{κ'_m}. Its coefficient j_β(c) = xi_c^{-4} <[T^G_β]_{Aν} e_c, J>_f reads the regions on [[β]]^♯, by Theorem W'(c') at j = 0. The stencil lies in κ'_m^♯. So every factor reads the regions inside [[ω]]^♯, and corresponds under ι by Theorem W'(d') and (I4-tr). For j^(1)_ω, the pairing <·, J>_f is local and translation invariant. ∎

**Theorem H' (replaces the region and canonicity clauses of H3).** Under the hypotheses of Theorem H and (G0'):

- Each A_ω ∈ {A^loc_κ, A^G_ω, A^E_ω} depends on the regions (Omega_j)_{j<=k+1} only through their traces on [[ω]]^♯. For A^loc_κ this is κ^♯.
- [[ω]]^♯ lies within d_B-distance 16 L^3 M_1 + C_L of the cells. In the outline's words, the hull enlarges the cells by O(M_1) local units, with the constant now 16 L^3 + O(1).
- A_ω is the same function, transported by ι, for any two systems (sequences, tori, pairs, Y) that a grid translation in M_1 xi_{k+1} Z^4 relates on an open U ⊃ [[ω]]^♯ ∪ (field hull). Such a ι carries Omega_{k+1} and Y on U.
- Holomorphy on the local class on [ω], reality at real pairs and the gauge clause are as in `h-walk.md` H3 with the gate's wording repair, namely: "the construction is covariant under" the block-constant subgroup, in place of "A itself is covariant exactly under". The isometry clause is §4.

*Proof.* A^loc_κ = θ_κ C_V^T (G^(2)_V - a) C_V for κ ∈ K_k. θ_κ reads κ^♭. The level-k maps read V = M^k U and the mask (bonds of T^(k) touching Omega_{k+1}) within O(1) stencils (I3), which lie in κ^(4) ⊂ κ^♯ near supp θ_κ. A^G_ω = -C_V^T [T^(1)_ω]_{νν,act} C_V and A^E_ω = -C_V^T E^(2)[j^(1)_ω] C_V. Here Theorem T' applies, the active rows (level k, touching Omega_{k+1}) are read locally, and the stencils of C_V and E^(2) at the rows of supp θ_{κ_n} lie in κ_n^♯. For the comparison, ι preserves the level-(k+1) grid, hence every finer one. Theorems W', T' and (I4-tr) give the rest. The size bound is Lemma N(d) plus the O(1) stencils. The d_B of the depth-k sequence dominates that of the longer one (`h-walk.md` (H2)). ∎

**Consequence for `h-walk.md` §2.8.** With [[ω]]^♯ in place of [[ω]], the claim of §2.8 holds as proved here. The terms are canonical: two systems that a grid translation relates on [[ω]]^♯ ∪ (field hull) have the same terms, on one torus or on two tori with room. So the translation mean, push-forward and Montel limit of mechanism (i) (SA 10560) are not needed for (RT). They are not needed for (IC) either, because they do not average over coordinate isometries (§1). §4 supplies (IC) directly.

## 4. Single-term isometry covariance: cutoffs at midpoints

**The defect** (`gates/h-walk-gate.md` §8). `h-walk.md` §3 applies a cutoff f to an unknown at its *base point*: the initial point of a bond or row, the site, or the top. Let a reflection r reverse a bond b = (x, x + eta e_1). The stored image bond starts at rx - eta e_1, but conjugating multiplication by f through r evaluates f at rx. So r M_f r^{-1} ≠ M_{f∘r^{-1}} wherever f varies, and the H3 claim that the isometries carry the cutoffs to themselves fails. Rows fail in the same way, with their length xi_c.

**Convention (M), orientation-free locations.** Every scalar cutoff (θ_κ, h~_κ) multiplies an unknown v at its *location* ℓ(v):

- for a fine bond, a row (a bond of T^(j)), or a level-k bond of T^(k) (the coordinates of A in Theorem H), ℓ(v) is the midpoint;
- for a site or a top, ℓ(v) is the point itself.

This is the outline's own device for the hypercubic tensor (SA 13191: "move first to bond-midpoint coordinates"). The pillar partition χ_x of `h-walk.md` §5 enters only the local norms, never a term, and is left as it is.

**Lemma M (the construction survives the change).** Assume (2.0) and M_1 >= 4, and replace the declared range r_0 <= 8L by r_0 := 8L + 1 in (c3) and in M_C(L) of (G0).

- (m1) At the location of every unknown of K[S, P, j], and of every coordinate of A, Σ_{κ'} phi_{κ'} >= 2^{-4}. Hence Σ_κ θ_κ = 1 at every location.
- (m2) (c1)-(c4) of `h-walk.md` §3 hold with locations in place of base points. The constant C_p becomes C_p' = C(p, nu_0(L)).
- (m3) Lemma K, the identity and the bounds of Theorem W(a)-(b), Lemmas J and 8.1, Theorem T(a)-(c), Corollary T and (H1), (H2), (H4) of Theorem H hold with the same proofs. Their constants change by factors depending on L only. Lemmas N, N2 and Theorems W', T', H' do not refer to locations and hold as written.

*Proof.* (m1) Each location lies within ℓ∞-distance xi_{κ'}/2 of a point z of a cube κ' ∈ K. An unknown on a bond of Omega_0 has an endpoint in Omega_0, and the midpoint is eta/2 <= xi_{κ'}/2 from it. A row is a bond of T^(j) with an endpoint in L_j, which K_j tiles, and its midpoint is xi_j/2 = xi_{κ'}/2 from that endpoint. A level-k bond touching Omega_{k+1} has an endpoint in Omega_k, which K_k tiles (L_k = Omega_k for the depth-k sequence). Sites and tops of Omega_0 lie in some κ'. Then every coordinate of (ℓ - c_{κ'})/(M_1 xi_{κ'}) has modulus at most (1 + 1/M_1)/2 <= 5/8, and (2.0) gives phi_{κ'}(ℓ) >= 2^{-4}.

(m2) Supports, the identity h~_κ = 1 on κ^(1) ⊃ κ^(1/4) ⊃ supp θ_κ, and Σ_κ θ_κ = 1 are statements about functions of points, so they hold at every location. For the difference bounds, write θ_κ = phi_κ / D. On the set where D >= 2^{-4}, the quotient rule gives |Δθ_κ| <= (2^4 + 2^8 nu_0) C_p |Δx|_∞ / (M_1 xi_κ), and similarly for second differences. At most nu_0 cubes contribute to D at a point. (c3): a location is within d_B-distance 1/2 of its base point, so the r_0-neighbourhoods of (c3) grow by at most 1. This is absorbed by r_0 := 8L + 1, with M_1 >= 16L(rho' + 4M' + 16L r_0). (c4) does not involve locations.

(m3) The proofs use only (c1)-(c4), the algebraic identity K(h~ Φ) = h~ K Φ + [K, h~] Φ (valid for any diagonal multiplication), and supports up to O(1) in d_B. In Lemma K the shift between the locations of two unknowns joined by one stencil entry is at most C xi of the local scale, as it was for base points. The supports in Theorem W(b) ("the output lies in supp h~_{κ_0}; the input is read on supp θ_{κ_n}") become "located in", and every set they feed into ((c3), the pillar sums) is enlarged by at most d_B-distance 1. ∎

**The group.** Let 𝒢 be the group of lattice isometries g of the torus that preserve every lattice T^(j) (j <= k+1) and map the level-(k+1) M_1-grid onto itself. Every finer grid nests inside that grid, so it contains the grid's vertices. Hence g, an affine map with linear part P ∈ W_4 that maps the top vertex set onto itself, maps every level-j M_1-grid (j <= k+1) and every M'-grid onto itself. Indeed, put the origin at a top vertex. Then g(x) = Px + t with t in the top vertex lattice, which lies inside every finer vertex lattice s Z^4, and P maps s Z^4 onto itself. 𝒢 contains the translations by M_1 xi_{k+1} Z^4 and every element of W_4 fixing a top vertex that preserves the T^(j). Let 𝒢_ax ⊂ 𝒢 be the subgroup that also maps the axial trees of the level-(k+1) blocks onto themselves.

**Input (I4), isometry covariance of the building blocks.** Cited from the outline and unchecked here: Proposition 1a.1.11 (SA 7380-7392) and statement 5's closing paragraph (SA 10340-10343). For g ∈ 𝒢, write g_U for the twisted action: relabelling, with -Ad U(b)^{-1} on a reversed bond (SA 7118-7120), and the corresponding twist on a reversed row. The input is:

- (I4a) For every separated sequence S (cut-downs included), every pair P and every coefficient j: K[gS, g_U P, g_U j] = g_U K[S, P, j] g_U^{-1}.
- (I4b) For g ∈ 𝒢_ax, the same identity holds for C_V, G^(2)_V, a and E^(2)[ψ].

The outline makes its averages W_4-covariant by a mean over comb orders (SA 7416). The tower-axial gauge objects are covariant only under 𝒢_ax (SA 10343: "in the strict axial gauge the isometry must also preserve the axial trees"). (I4a) contains (I4-tr) of §3.

**Theorem IC (replaces the isometry clause of H3).** Assume the hypotheses of Theorem H', convention (M), and (I4). Let g ∈ 𝒢.

- (a) For every walk ω of Theorem W at a ♭-local coefficient j: T^{gS}_{gω}[g_U P, g_U j] = g_U T^S_ω[P, j] g_U^{-1}. The same holds for the tree walks of Theorem T and the terms of Corollary T, j^(1)_ω included.
- (b) If g ∈ 𝒢_ax and g also carries Omega_{k+1} and Y, then A_{gω}[gS, g_U P] = g_U A_ω[S, P] g_U^{-1} for each A_ω ∈ {A^loc_κ, A^G_ω, A^E_ω}.
- (c) When g preserves the regions (and Omega_{k+1}, Y), (a) and (b) say that single terms are covariant. For W- and T-terms this holds under every such g ∈ 𝒢. For A-terms it holds under every such g ∈ 𝒢_ax. This is the outline's clause in statement 5, with its axial-tree proviso.
- (d) For decoupled terms s^ω T_ω with P(ω) defined from [[ω]]^♯ (`o1-decoupled.md` Definition D), (a)-(c) hold with s replaced by s ∘ g^{-1}, for every g that also maps the parameter partition onto itself.

*Proof.* (a) Take the objects in order.

- *Cubes and walks.* g preserves the level-j grids, and membership in K_j is the geometric test of Lemma N0. So g maps K_j(S) onto K_j(gS), cells X_κ onto X_{gκ}, and walks onto walks.
- *Profiles.* With c_{gκ} = g c_κ and xi_{gκ} = xi_κ, g^{-1}x - c_κ = P^{-1}(x - c_{gκ}). The coordinates of P^{-1}w are a signed permutation of those of w, and phi_κ is a product of the even profile p over the coordinates. So phi_κ ∘ g^{-1} = phi_{gκ}, and likewise h~_κ ∘ g^{-1} = h~_{gκ}. Summing over K(S), the denominators correspond, so θ^S_κ ∘ g^{-1} = θ^{gS}_{gκ}.
- *Locations.* ℓ(gv) = g ℓ(v) for every unknown v, because an isometry maps the midpoint of a segment to the midpoint of its image, however the image bond or row is stored. The twist of g_U acts in the fibre of each unknown as a linear map, which commutes with multiplication by a scalar. Hence g_U M_f g_U^{-1} = M_{f ∘ g^{-1}} for every scalar cutoff f. This is the step that fails for base points.
- *Cut-downs.* C_{i_1}(κ) is the smallest union of level-i_1 M'-cubes containing κ^(7/2). g preserves the M'-grid and maps κ^(7/2) onto (gκ)^(7/2), so g C_{i_1}(κ) = C_{i_1}(gκ). Each later C_{i-1} moves every face outward by a fixed amount and rounds outward to a g-invariant grid, which commutes with g. The indices i_0, i_1 are defined by intersections with layers, which g carries. So S^{gκ}_{gS} = g S^κ_S, and j^{gκ} = g_U j^κ.
- *Local models.* K_{gκ} = K[g S^κ, g_U P^κ, g_U j^κ] = g_U K_κ g_U^{-1} by (I4a). So S_{gκ} = g_U S_κ g_U^{-1}, and the commutator factors correspond as well.

The product formula (6.1) then gives (a) for W.

For T, first note that j_β(c) = xi_c^{-4} <[T^G_β]_{Aν} e_c, J>_f is carried to j_{gβ}. The unit row vector e_c goes to g_U e_c, which is the twisted unit vector at gc. J goes to g_U J. The bilinear pairing is g_U-invariant, because Ad of a complex group element preserves the bilinear form tr(XY), and the signs of the twist square to 1. So j_{gβ} = g_U j_β, and j^(0) is carried to its own image. V_{gβ} = g_U V_β g_U^{-1} by (I4a), since V_β is linear in j_β. Tree walks (trunk, vertex set, branches) are carried to tree walks. Corollary T's blocks and j^(1)_ω follow in the same way.

(b) A^loc_κ = θ_κ C_V^T (G^(2)_V - a) C_V uses (I4b) and the location rule. A^G_ω and A^E_ω use (a) and (I4b) for C_V and E^(2). The active rows and the mask are carried because g carries Omega_{k+1}.

(c) Restate (a), (b) with gS = S.

(d) g maps [[ω]]^♯ onto [[gω]]^♯ and the partition onto itself, so P(gω) = gP(ω). ∎

**What is narrowed.** `h-walk.md` H3 claimed covariance of single terms under every lattice isometry preserving the level-(k+1) M_1-grid, the regions and Omega_{k+1}. What holds is:

- W- and T-terms: covariant under 𝒢, given (I4a);
- A-terms: covariant under 𝒢_ax, given (I4b).

The restriction to 𝒢_ax is the outline's own scope (SA 10343), not a defect of the walk construction. (I4b) gives covariance of A only under 𝒢_ax, because G^(2)_V and C_V are tower-axial objects. Whether A is covariant under some g in 𝒢 but not in 𝒢_ax is not settled here. If it is not, then no expansion of A has g-covariant terms, because a sum of g-covariant terms is g-covariant (the argument of test 2.1, applied to isometries). Under the base-point convention, covariance failed even under 𝒢_ax. Convention (M) removes that failure.

## 5. The consumers of §1 against the repaired clauses

1. **`o1-decoupled.md`, Definition D and Theorem B.** Its set [[ω]]^+ is exactly [[ω]]^♯, and its Lemma P already uses the d_B-radius 16 L^3 M_1 + 4L of Lemma N(d). Both rest on the same gap (G0'). Convention (M) changes Theorem W's constants by L-dependent factors (Lemma M), which Theorem B's C_L, B_L absorb. No statement changes.
2. **`o1-decoupled.md` Lemma C1 (Theorem C).** (H-seq) has the regions agree on G^♯ = ∪{κ^♯ : κ^(4) ⊂ G}. A walk with every κ_i^(4) ⊂ G has [[ω]]^♯ ⊂ G^♯. So Lemma C1 is the case U = int G^♯, ι = identity of Theorem W'(c'), with the pair change handled by its Cauchy estimate as before. Its own proof uses the same candidate argument as Lemma N. Lemma C1 is now also a corollary of a stated theorem, and the "general repair of (C5), with candidates absent in one sequence" that `o1-decoupled.md` §5 item 2 lists as open (row 123) is Lemma N.
3. **`o1-decoupled.md` §3 (H-field).** It needs the term identity for the tree walks of H_1(s). Theorem T' supplies it for walks with every cube's κ^(4) ⊂ G. 𝔊(s) is not built by `h-walk.md`, so its expansion has to be specified separately, as `o1-decoupled.md` already says.
4. **`a2-full.md` Theorem VI, collared form of `gates/h-walk-gate.md` §9.** It works on one region sequence and reads no clause repaired here, so it is unchanged. One recommendation for its downstream use, not an edit: build the decoupling monomial from the cubes that meet [[ω]]^♯ ∪ (field carrier). Then each decoupled term's region dependence lies inside its polymer, which Package C and (3b) need (items 5-6). The gate's §9 estimates use only that the hull lies within R_h of an admitted tree. With R_h := 16 L^3 M_1 + C_L (Lemma N(d)), which is the gate's R_h = C_L M_1, and ℓ_P >= 8 C_geom R_h, they hold verbatim.
5. **Package C (SA 17548-17556, 19523).** By Theorem H', a term of A whose [[ω]]^♯ lies where two labels' regions agree is the same function for both. So the outline's "built from walks and fields inside X, so the regions do not affect them" holds once the term's domain X contains [[ω]]^♯ (item 4). The consumer's margin ("X one cell inside Λ_{j+1}") must exceed 16 L^3 M_1 + C_L local units. This is a constant for the consumer, compatible with the outline's order: M is a multiple of M_1 chosen after it (SA 10582). The same paragraph also reads walk terms of C^(j)(Λ_{j+1}). Statement 5 for C^(k)(Y) is not in `h-walk.md`, and it stays open. If it is built from A's terms by the parametrix of mechanism (h), its terms inherit the read sets [[ω]]^♯ by the factorwise argument of Theorem T'.
6. **(3b), SA 7837, and its users (SA 32651-32652, 26918-26930).** Theorem W'(d') and Theorem H' give the same term on all tori with room, for grid-translated configurations, provided the term's domain contains [[ω]]^♯ ∪ (field hull) (item 4).
7. **R9 transport (SA 10404-10405, 10567).** The specified walk data of Definition D are transported by grid translations (Theorem W'(d')) and by 𝒢 given (I4a) (Theorem IC(a), (d)). So "transport follows from uniqueness" has the data covariance it needs.
8. **Requirement B2 (SA 3937-3950), SA 7581 and (R14) (SA 5893-5898).** These ask that the pointed totals of a member be covariant under every lattice isometry, *including unit translations*. Theorem IC gives covariance of single terms under 𝒢 (W- and T-terms, given (I4a)) and under 𝒢_ax (A-terms, given (I4b)). Two gaps remain between that and B2, and neither is in the walk construction:
   - **(i) Unit translations.** Single walk terms on a fixed M_1-grid are covariant only under translations that preserve that grid. Statement 5 claims no more (SA 10337). Covariance of pointed totals under unit translations needs a mean over grid offsets. Mechanism (i)'s first step is "a mean over translations", but applied to terms on region sequences, whose regions are unions of grid cubes, such a mean is not defined as written. So `h-walk.md` §2.8's "mechanism (i) is not needed" is true for statement 5's own clauses and false for (R14) and B2.
   - **(ii) Isometries outside 𝒢_ax.** For these, (I4b) is not available. Unless the axial trees are invariant under the whole hypercubic group, B2's covariance of A-built activities needs an argument outside the walk expansion, for example from gauge invariance of the localised activities.

   Both gaps belong to the B2 / (R14) consumer (the E position, through P1). They are recorded here, not attacked.

**Order of constants.** First L; then (2.0)'s profile p and its constant C_p'(L), r_0 = 8L + 1, and the constants of `h-walk.md` and Lemma M as functions of L; then R_1 >= 8L^3 and M_1 >= M_h(L) with M_C(L) recomputed for the new r_0; then κ-bar, ℓ_P and M as in the consumers. Nothing is circular. Lemma N and Theorems W', T', H' add no constant to any bound. Theorem IC adds none either; it reads (I4).
