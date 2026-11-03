lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T01:06Z

# cond-c: condition (C) of the box-first WF7 route (queue row 157)

Pinned at commit 75752c07e (branch claude/ym4d-hard-route). Research-stage working state. Not an audit; no status.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Section 1 checks Codex text (`library/wf7-bf.md`), so it is a cross-provider check. Sections 2-7 are proved by Claude and not yet checked by the other model. No numeric job was run. Every step is a hand argument.

Sources read: `library/wf7-bf.md`; `gates/wf7-extension-gate.md` Section 6; `library/wf7-extension.md` Sections 1-4; `library/old-depth.md` Section 2 (Lemma CR); `library/joint-loc.md` Sections 4, 7; `library/assign-adopt.md` Sections 1-2 (Definition A); `library/geo-5.md` Sections 1-3 and `gates/geo-gate.md` (checked by Claude, first failing step none); `library/wf-room-2.md` Sections 1, 3. Outline: Sussman-Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder, not copied here. SA line numbers refer to it. Read: SA 6012-6125 (frame, label, R21), 6318-6335 (index maps), 9588-9790 (1b setting, Theorems 1, 2, 6), 13426-13560 (PW), 15707-16360 (WF1-WF15), 17300-17450 (step tests, Proposition 2.3, fates), 17528, 20903-20912.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the windows, WF1-WF15, the label, the step formation, the fates, the nests and the frame. Tadeusz Balaban for the restriction mechanism (CMP 109 (3.18)-(3.25), (3.38)) and for the window scale of the local layer (CMP 119 p. 276, as read in `joint-loc.md` Section 7). Codex for `wf7-bf.md`, `wf7-extension.md` and `geo-5.md`.

## 0. Result

(Written last; see the end of this file.)

## 1. Check of `library/wf7-bf.md` (Codex)

Checked line by line by Claude. First failing step: none. Four defects, none breaks a consumer.

| Section | Verdict |
|---|---|
| 1, check of the gate's Section 6 | **CORRECT-NO-ADVANCE.** Items 1-8 are correct clarifications. Item 4 is right: `wf7-extension.md` (4.5) bounds the two-map difference F_R(w)-F_R(v) with beta = w-v, so beta = 0 gives zero. The single-map term is DF_R(v)v', and Section 3 bounds it. |
| 2, identity (2) on contained boxes | **ADVANCE** as an implication from (C), Lemma CR, BG, AX and gauge invariance. Checked: d/dnu exp(i eta (t+nu zeta)H_b) = i eta zeta_b H_b exp(i eta (t+nu zeta)H_b), because zeta_b is a scalar. The chain rule is linear in the direction, and sum zeta = 1 on bonds, so sum_zeta d_nu Phi_zeta = d/dt G(X, F_T(m_T V_t)). At complete physical pairs V_i is regular critical for S^i. It is then also critical for the truncation S^{i,<=j}, which has more constraints, so Pi_j(V_i) = V_i up to residual gauge (BG). Lemma CR with (C) gives F_T(m_T V_i) = V_i on T_0 up to the assigned gauge, with the currents on bonds whose plaquettes lie in T_0. The member is gauge invariant. The sufficient condition R_z in Omega_j^0 cap Omega_j^1 and the aligned case of joint-loc (7.2) follow by nesting. |
| 3, bounds | **ADVANCE** as an implication from T4, AX, AV, MS, PW. Checked: (3); the weighted sum with 2 gamma below the T4 rate and gamma above the MS rate (needs rho >= 32 log L / theta, gate W1); (4) by integration on the complex segment; the node product rule and d(gJg^{-1}) = gJ'g^{-1} + [g'g^{-1}, gJg^{-1}]; the WF8 arithmetic (A E_H / alpha_j^2 <= C rho^2 sigma^{4+alpha_H}, A E_N / alpha_j^2 <= C rho^3 sigma^6 from alpha_j / r_B <= C, A^3 / alpha_j^3 = C rho^3 sigma^6); the tail split (5). |
| 4, heredity and consumers | **ADVANCE.** Checked: the inclusion-exclusion identity f[K\|B] = sum_{A in K} (-1)^{\|K-A\|} f(1_{B cup A}) and the corner coefficient (1-1)^{\|Lambda-B-A\|}; mixed Cauchy with one derivative per parameter; (6) from (4), the Cauchy cost C g_j / alpha_j and the C_M sigma^{-4} count; both WF12 inequalities from e^x >= x^n / n!. The OA7 paragraph claims only the pair estimate and says so. |
| 5, stop at a lower-layer seam | **ADVANCE.** The Cartan example is correct: 4 x 2 x 3^3 = 216 edges, 81 sites, cycle space 216 - 81 + 1 = 136 > 8 rows; d*da = 0 with d*a = 0 forces a = 0 by the flat lattice identity d*d + dd* = componentwise Laplacian and compact support. The first failed inference is named correctly. |

Defects, ranked:

1. **Scope (this note answers it).** Section 5 leaves open whether actual windows satisfy (C). Sections 2-6 below answer that: yes for top-layer base points (Theorem C1), no for the outline's level-k windows at lower-layer base points (Example C3), and yes for every base point under the filing of Section 5 (Theorem C2).
2. **Section 2, stronger than needed.** It requires X and its current stencil inside T_j(R_z). Lemma CR needs only the stencil inside the interior of T_0 = R_z. Harmless.
3. **Section 3, constant.** C_* adds the erosion (rho + L M_frak)/(L-1). The bound D >= bM/sigma - 2 holds without it, since every weight of the box metric is at least xi_j^{-1} and a row carrier has size at most 2 xi_j. Harmless.
4. **Section 3, input name.** "AV and PW give (3)": PW here is the first-order R9 bound of `o1-decoupled.md` Section 5, as `wf7-extension.md` Section 4 defines it, not SA's (PW1)-(PW5). Wording only.
