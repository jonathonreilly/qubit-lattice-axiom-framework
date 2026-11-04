lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T02:48Z

# Check of `library/r-inv.md` (row 242)

Status: in progress. Sections are written as the check proceeds.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, branch `claude/ym4d-hard-route` at `a6369e61b`. Checks `library/r-inv.md` (Codex) line by line. One reading by one other model; not an audit. Sussman–Alpoge `YM4_sketch_500.tex` at `31a47c543775` (SA below), fetched by URL to a scratch folder (sha1 `107abaef1a08…`, 32992 lines). Balaban CMP 119 read from `~/ym4d-papers/cmp119.txt`. No numerics were run; every step below is by hand.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the operation **R**, the frame sum, the healing formula, the hard-core gas and the insertion age. T. Balaban (CMP 119, (2.32)–(2.33); CMP 122) for the partition-preserving covariance of R-terms and the frame-averaged trees. Codex for `r-inv.md`.

Kind of result (FINISH item 9): check of our own new text. The outline requires the invariance and does not prove it (SA 7581: "Both symmetries are part of the definition of 'renormalised'"; SA 20646: "The actual domain and naturality hypotheses remain part of closure"). Balaban states the covariance and defers its proof (CMP 119 p. 260: "will follow immediately from the construction of the R-terms given in the next paper").

## Verdicts, §§1–3

| Step of `r-inv.md` | Verdict |
|---|---|
| §1 (1): T_{D_H} = T_H − \|G\|^{-1} Σ_g T_H(g^{-1}P) | ADVANCE. Sum (INS) over X and reindex X ↦ gX. Invariant totals give zero. |
| §1 sources: SA 7581, SA 16057–16067 (WF10), CMP 119 (2.32)–(2.33) | CORRECT. Quotes match. Balaban's covariance is for "Euclidean transformations r, which leave the partition of the lattice ... in MR_j-cubes invariant", the same restriction as (R-inv). |
| §2: (N), (T), (F) are natural with grids and frames carried | ADVANCE. (N): the least box with faces in the carried F_i containing D_{i-1}+[−m_i,m_i]^4 is unique and maps to its image. (T): ⟨Ox+t, Ore_i⟩ = ⟨x, re_i⟩ + ⟨t, Ore_i⟩, so the frame-lexicographic order is carried. (F): equal weights on a carried set of minimal unions. |
| §2 (2): s \| L^{m+1−j} for every formation grid side | ADVANCE, via `ti-2.md` Lemma 3, which I redid. Ř_i is the least L-power ≥ (log min_{u≤i} x_u)^r (SA 17334). M is an L-power. The test-cube side M_2Ř_t has M_2 an L-power with L²M_2 ≤ M (SA 17334). Lemma 3(a) gives Ř_i ≤ L^{j−i}Ř_j. So in level-i units every side is an L-power at most MŘ_i ≤ L^{j−i}·MŘ_j ≤ L^{m+1−i}, which also covers sides finer than one level-j unit. Signed permutations about the origin fix centred partitions of odd side. Precision: SA says the test cube has side "of order" M_2Ř_t. Lemma 3 reads it as exactly M_2Ř_t on a centred grid. That is a formation choice; it is natural. |
| §3 (3): T_{H̄,L̄}(ι W) = T_{H,L}(W)^{-1} | ADVANCE. With q = q(W), θ(ιW) = θ(W) because ιW is conjugate to W^{-1}. So q̄(ιW) = L^{-1}q^{-1}L, and ιW·q̄(ιW)·L̄ = L^{-1}q^{-1}W^{-1} = (WqL)^{-1}. Also H̄ = −Ad(L^{-1})H is the principal log of B̄L̄^{-1} = L^{-1}(BL^{-1})^{-1}L, valid for small H. |
| §3: ι preserves Haar measure; ι_{H̄,L̄}∘ι_{H,L} = id | ADVANCE. In W = cos u + i sin u n·σ, ι is (u, n) ↦ (u, −R_{g(u)}n) with g(u) = (q(u)L)^{-1} and R_g ∈ SO(3). For fixed u this is orthogonal on S², so Fubini keeps sin²u du dΩ. I redid the double application; it returns W. |
| §3 (4): J_{H̄,L̄}(ιW) = J_{H,L}(W) | ADVANCE. I also checked it on the explicit Jacobian of `s210.md` (7), J = 1 − X_Hθ. With W' = ιW, θ(W'e^{isH̄}) = θ(e^{isH}q^{-1}Wq) = θ(We^{isH}). So X_{H̄}θ(ιW) = X_Hθ(W). |
| §3: θ = 0 and θ = 1 give the unshifted and fully shifted charts | CORRECT. At θ = 0, ιW = B^{-1}W^{-1}B. That is the (F2) reversal Ā = −Ad(B^{-1})A. At θ = 1, T(W) = WL. |
