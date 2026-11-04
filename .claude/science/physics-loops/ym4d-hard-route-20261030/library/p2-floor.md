lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T15:34Z

# p2-floor: check of `c1-repr.md`, then the floor's (P2) and (P3)

Queue row 179. Pinned at commit f20eba5f1. Work in progress; sections are written as they finish.

**Moves:** D1's floor (`sa-ledger.md` rank 10; `t0-skeleton.md` D1, node "unsourced floor"). Written by Claude (Opus 5.5, max) on the Mac mini worker, fresh session. Research text, not an audit; it grants no status. Proved by Claude, not yet checked by the other model, unless a line says otherwise.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the history representation (SA 1a.2.3, L7463; the two layers, L17499), the average (L7049-7074), Theorem 2.1 (L17259), the never-large label and (ER7)-(ER8) (L6560-6640), B2 (L3937) and Theorem 5(a) (L9746). Their YM3_I Proposition I-3-55 (YM3_I L1971) is the precedent for the Borel average. T. Balaban for CMP 98, 102, 109, 119 and 122, as rebuilt in the notes cited. OpenAI Codex for `library/c1-repr.md`, checked below. Claude for `a3-close.md` Lemma T and `d1-floor.md`.

**Sources.** Outline `YM4_sketch_500.tex` and `YM3/YM3_I.tex` at `31a47c543775`, fetched by URL into a private scratch folder. Memory free was 45 percent, below the 50 percent floor, so no numeric job was run. Every step below is a written argument.

## 1. Check of `c1-repr.md` Sections 2-8 (Codex)

Checked line by line by Claude (Opus 5.5, max), commit f20eba5f1. Not an audit. Verdict per section, then remarks. No remark breaks a statement.

| Section | Statement | Verdict |
|---|---|---|
| 2 | Borel tests: the small-diameter mean is a contraction fixed point; existence and uniqueness sets are countable unions of compact projections; the unique solution is Borel; tests total, value 0 off their domain | ADVANCE, first failing step none |
| 3 | Kernel identity (1): K_h ≥ 0, Σ_h K_h = 1, exact sourced mass, \|τ_h^F\| ≤ ‖F‖_∞ τ_h^1; insertion kept inside deleted-slot integrals | ADVANCE, first failing step none |
| 4 | Average as δ_{M(U)}; soft gauge factor ∫G(U^u)du = 1; tests and storage; strip map a diffeomorphism with positive Jacobian; completed square exact | ADVANCE, first failing step none |
| 5 | Healing as relabelling; restriction and commuting kernels; three fates as measure operations | ADVANCE, first failing step none |
| 6 | R kernel (2)-(3) with recorded drop-out off 0 < D_r < ∞; one frame per summand; tree coordinates (4) with Jacobian 1 | ADVANCE, first failing step none |
| 7 | M_*μ ≪ dV (5); Haar densities ρ_{k,h} ≥ 0 and (6) at every finite depth | ADVANCE, first failing step none |
| 8 | (ER7) from A1 (9.2), (AV), (7.14) and Definition A, via a corrected Lemma T | ADVANCE, first failing step none |

**What was redone.**

- *Mean (2).* For Φ(H;T) = H + n^{-1}Σ log(T_i e^{-H}), D_HΦ = I − I = 0 at (T,H) = (1,0). So ‖D_HΦ‖ < 1/2 on a small ball, and |Φ(H;T)| ≤ |n^{-1}Σ log T_i| + r/2 < r for T near 1. Banach's theorem gives the unique, continuous, analytic mean. Right covariance moves any small family to one near 1.
- *Tests (2).* With the chart C σ-compact and the defining map F continuous, {V : ∃U ∈ C, F(V,U) = 0} = ∪_n π(F^{-1}(0) ∩ (X_m × K_n)) is F_σ. Two solutions at distance ≥ 1/n give another F_σ set. For open O, s^{-1}(O) is F_σ by the same argument with C ∩ O. So the unique solution is Borel.
- *Gauge factor (4).* C_{yx}(U^u) = u(y)C_{yx}(U)u(x)^{-1}, since the mean is bi-covariant. With u(y) = 1, each factor reads only u(x), and Haar invariance gives z for each. The draw keeps M(U) fixed. It equals multiplication by G only for a gauge-invariant measure, as SA L17499 says.
- *Average, regular rule (7).* Write P for the transport from x to the crossing edge along [x,x'], and Q for the same along U[c]. Under left multiplication of every crossing edge by e^{itH} (comb gauge of the double block),
  W_x(t) = (U(c_-,x)P) e^{itH} (U(c_-,x)P)^{-1} W_x Q e^{-itH} Q^{-1},
  so (1/i)Ẇ_x W_x^{-1} = Ad(U(c_-,x)P)H − Ad(W_xQ)H = O(c_M)\|H\|, because each transport is within CL²ϖ_c ≤ Cc_M of 1 (SA L7213). The factor U[c] gives Ad(e^{Y}Q)H = H + O(c_M)H. This is (1/i)Ṁ M^{-1} = H + E_cH, ‖E_c‖ ≤ Cc_M. Crossing edges of c are read by no other coarse bond, so the Jacobian has a block-diagonal full-rank minor.
- *Average, second rule (7).* A loop Y with transverse coordinate zero is identically 1; every other Y contains one non-central crossing edge once, so Y is a submersion and {Y = −1} has codimension 3. The determinant d_c is analytic on the connected set D_c, and d_c(1) = 1. Its zero set is covered by countably many regular hypersurfaces of lower-order derivatives. So M is a submersion off a Haar-null set, and (5) follows by Fubini in local coordinates.
- *Raw-datum correction (8).* At the flat field M has derivative Q^{pl}a = σ(c_-) + Q^s a − σ(c_+) (SA L7080, L7084); on one-colour fields M(e^{ifT}) = e^{i(Q^{pl}f)T} exactly (SA L7227), and Codex's field has one colour. In Codex's field, ā(c_-,x) = Σ_{ν≠μ}\|x_ν\|H, so σ(c_±) = ±3(L²−1)/(4L)·H, and Q^s a = LH. The raw coefficient is L + 3(L²−1)/(2L), which exceeds 2L for L ≥ 2. So `a3-close.md` Lemma T Step 3, "\|B(w)(c)\| ≤ 2ξ'_q sup\|w\|", is false for the raw increment. The bootstrap it cites (`a1-balaban.md` 3.5) bounds the *straightened* angle, with the endpoint factors removed. Codex's repair is right: (7.14) writes M^q(e^{iη_p w}U) = (e^{i𝔞_q}M^qU)^{v_q}; each new factor is within C t_{q+1}‖w‖_∞ of 1 (`a1-balaban.md` 7.6: ‖u − 1‖ ≤ C_L r_* t_r); so \|v_q − 1\| ≤ exp(C‖w‖_∞ Σ_{r<q} t_{r+1}) − 1 ≤ C' t_q‖w‖_∞ when λ‖w‖_∞ is small. Unitarity of M^qU then gives \|B(w)(c)\| ≤ C_A t_q‖w‖_∞. With R = c_T/λ and C_A c_T < r_B, the datum stays in the ball of (9.2). The rest is Lemma T Steps 1, 2 and 4: (7) S = C_0λ^{-2}; Cauchy on z ↦ f(zw) gives \|Q(w)\| ≤ 2S(‖w‖/R)²; the identity f(a+ib) = f(a) + if(b) − if(0) + Q(a+ib) − Q(a) − iQ(b) holds; λ^{-2} cancels against R^{-2}. So (8) holds with K_T = 3C_1 + 6C_0c_T^{-2}. The change of unit gives the factor L^{-2(j−p)}, stronger than (ER7) needs.

**Remarks (none breaks a statement).**

1. *Minimisers.* Section 2 makes tests Borel when their objects are critical points of continuous equations. SA L17346 says "localised minimal orbit", and Proposition 2.4 (L17636) uses the minima in a class. On the domain the run reads, A1 (8.2) and `ref-chart.md` Theorem 2.4 identify the minimum with the unique regular critical orbit, so Section 2 applies. Off that domain the test value is 0 by totality. If a later note defines a test by a minimum over a class without that identification, the existence set is a projection of a Borel set. It is then analytic, hence universally measurable, and integration against the history measures still holds.
2. *Gauge-restored densities.* (6) uses the restored Haar coordinates (4). The floor integrates ρ_{K,S_0} over B_s, which is not gauge invariant. (P2)'s right side is gauge invariant, so (P2) can hold almost everywhere only for a gauge-invariant representative. So the floor must read the restored densities, and (P2) must assert their invariance. With the slice measures, ∫_{B_s} ρ_{K,S_0} depends on the slice. This is a reading instruction for `d1-floor.md` Theorem F, not a defect.
3. *Section 8 versus `d1-floor.md` 4c.* 4c showed only that (9.2) applied to the raw increment at the near-zero radius gives a depth-dependent radius. Section 8 avoids this with the large ball R = c_T/λ and three real values. So 4c's "(ER7) is not in the library" is superseded: (ER7) is now an implication from A1 (9.2), `a1-balaban.md` 3.5 and 7.6, and Definition A, by Codex, checked here.

**State after this check.** C1 (P1) is proved by Codex and checked by Claude, first failing step none: exact sourced mass and non-negative label densities at every finite depth. (ER7) is proved by Codex from Claude's Lemma T with the raw-datum correction, checked by Claude, first failing step none. These remain implications from A1 (conditional on F0) and the adopted tower geometry.
