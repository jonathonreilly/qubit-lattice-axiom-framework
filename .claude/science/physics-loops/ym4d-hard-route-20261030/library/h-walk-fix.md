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
