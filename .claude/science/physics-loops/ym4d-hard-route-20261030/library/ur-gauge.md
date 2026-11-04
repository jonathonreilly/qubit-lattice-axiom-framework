lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T13:53Z

# ur-gauge: check of `ur-ya.md`, the Hessian gauge identity, (UR) and (YA)

Queue row 217. Started 2026-11-04T01:53Z on commit 1face7c7e. Work in progress; sections are written as they close.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; commit 1face7c7e; Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL to a scratch folder (SHA-1 107abaef…2348885), cited as SA nnnn; Balaban CMP 109 read from `~/ym4d-papers/cmp109.txt`. One reading by one model, not an audit. Every step is by hand; no numerics were run, so the numeric lock was not taken (memory free was 43%, below the 50% floor, in any case). No subagent.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for PH1-PH23 (SA 12889-13424), ER1-ER14 (SA 6460-6720), the Landau pair and its covariance (SA 1a.3.6, 1a.3.10, SA 7700-7750) and the soft block axial factor (SA 7178-7186). T. Balaban for the soft gauge fixing (CMP 109 (0.14)-(0.19)) and for the standing assumption that every activity is invariant under all complex gauge maps (CMP 109 (1.19)). Codex for `ur-ya.md`, whose Sections 2, 4 and 5 are used below as checked.

## 1. Check of `ur-ya.md` (Codex), line by line

Verdicts. Each is an implication from the inputs that the note names.

| Item | Verdict | Remark |
|---|---|---|
| §2, ER8u from ER7 | ADVANCE | SA ER9 with ε_0 = C(c + c²)α_j and ε_1 = cα_j. ER7 then gives tower radius CK_T(c + c²)α_j < α_j/2 for small c. Conditional on ER7. |
| §2, (1) | ADVANCE | Circle radii a_j/(4‖v‖), a_j/(4‖w‖) keep ‖sv + tw‖_{1,j;X} ≤ a_j/2. Cauchy gives the factor 16‖v‖‖w‖/a_j². The norm is the one on X, as in SA ER14, because G(X,·,z) reads the pair on X only. |
| §2, (2) | ADVANCE | The weight costs e^{2mC_M(q+1)}; the two site sums cost C(q+1)^8; the rooted count costs C e^{κ_D q}. The series converges when 2mC_M < (κ − κ_D)/2. Only m < δ is needed for the site sums; m < δ/2 is harmless. |
| §2, "ER8u plus (R) proves UR" | ADVANCE | This is SA PH5a. DG(X,(1,0),z) = 0 by constant colour invariance (SA ER3), so (PH4) is the composite Hessian. |
| §3, counterexample (3)-(4) | ADVANCE (correct) | Checked below. (R) is false for the contour response, uniformly in j. |
| §3, "the checked inputs give only the block-constant subgroup" | ADVANCE, with a note | True of the sources that `b2-extract.md` §4 cites (`h-walk.md` test 2.1, `carrier-adopt.md` Lemma L(c), `a2-full.md` §10 item 5). But other notes already use full invariance: `wf-c.md` §6 ("G̃ is gauge invariant ... in its Landau reading"), `wf7-bf.md` §2 ("Gauge invariance removes that gauge"), `d1-floor.md` 4b, `inn-fix.md` §5. The chain is inconsistent here. Section 3 below removes the inconsistency. |
| §4, (6) and (7) | ADVANCE | A_p(W) = 1 − ½ tr W = ½ det(W − 1) on SL(2,ℂ), so abs(A_p) ≤ C abs(W − 1)² ≤ Cα_j²η_j⁴. The tent quadrature η⁴ Σ_p h_z(p) = 1 per orientation is SA PH21 (rechecked in `b2-extract.md` Step 9). This is SA 13570-13577 ("its own tent action obeys abs(A(h_z, U)) ≤ Ca²"). |
| §4, unmultiplied tent kernel | ADVANCE | Each A_p is invariant under every bare gauge map, so its Hessian at 1 kills gradients. The plaquette curl d_η of a response is a combination of first difference quotients, bounded by (5). This is SA 13323-13345. |
| §4, "UR would imply (8)" | ADVANCE | Proved in Section 4 below, as (8). |
| §5, (9) | ADVANCE given (8) | 1 + T² ≤ 2T³ for T ≥ 1. The own tent is filed once, so it adds C g_j once, not per domain. |
| §5, young ages, (10) | ADVANCE given (8) | 1 + n ≤ 2^n; N exists because L ≥ 3 > √2; σ ≥ L^{−N} and ρ ≥ 1 for n < N. |

**The counterexample (3)-(4).** I redid it from `prefactor-loc.md` Sections 2-3.

1. The augmented branch is the saddle of Δ̃_j = d^*d + Σ_{r<j} Q_{0,r}^* τ_r^* τ_r Q_{0,r} under Q_{0,j}a = B. Lemma B (ii) gives Q_r J_r = 1 for the face-crossing insertion J_r.
2. Put v := J_1 ⋯ J_j B for B_1 ≡ T, B_μ ≡ 0 (μ ≠ 1). Then Q_{0,j}v = B. Also Q_{0,r}v = J_{r+1} ⋯ J_j B is a face-crossing field of level-j faces.
3. τ_r averages path sums along R3 contours from a node to a point of the same level-(r+1) cube. With L odd the cubes are nested, so such a contour never crosses a level-j face. Hence τ_r Q_{0,r} v = 0 for r < j.
4. On a plaquette in a (1,μ) plane, both 1-bonds lie at the same x_1, so both cross a face or neither does. Hence dv = 0.
5. So Δ̃_j v = 0, and (v, 0) solves the saddle system with datum B. Lemma B (vii) makes the polynomially bounded solution unique. So R_{0,j}B = v.
6. In the chart U_b = e^{iηA_b}, the physical response is η^{−1}v: abs = η^{−1} on crossing bonds. Its difference quotient across a crossing is η^{−2}.
7. If (R) held, Σ_x e^{−δ dist(x,X)} ≤ C would bound sup_X abs(H_jB) uniformly in j. Truncation of B and Lemma B's decay at fixed j make the sum legitimate.

The gauge function that converts the smooth response (η T on each 1-bond, as a link angle) into v is χ(x) = T n_1(x) − ηT x_1, with n_1(x) the block index in direction 1. It varies inside each final block. So it is not a block-constant direction, as the note says.

What this refutes. It refutes SA ER12 **for the representative fixed by (Id)**. SA writes ER2 for "its configuration-current pair in a fixed gauge near zero" and leaves the gauge open (SA 6487). With the Landau representative, ER12 holds by (5). So this is not a correction of SA's text (FINISH item 6 (3)). It does not refute UR, YA or (19).

**First failing step of `ur-ya.md`:** none. Its first failing input is correctly named: (R) for the contour response, and no Hessian gauge identity to transfer the Landau bound. Sections 2-4 below supply that identity.
