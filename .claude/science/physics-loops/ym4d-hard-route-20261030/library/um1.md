lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T07:13Z

# UM1 for the actual intrinsic action (queue row 178)

Proved by Claude, not yet checked by the other model. Research-stage working state; no status.

Commit read: 9a35fdcba. Work in progress; sections are written as they close.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the UM chapter (SA 14280-14800), the local Gaussian comparison (SA 13893-14090) and the step anatomy (SA 7590-7640). Tadeusz Balaban for the background-field and localisation constructions (CMP 95-122). SA means `YM4_sketch_500.tex` at `31a47c543775`, fetched once to a scratch folder.

## 1. Check of `b4-step.md` Section 5, the Gaussian comparison (7) (Codex)

Provenance: Claude Opus 5.5, effort max, commit 9a35fdcba. One line-by-line reading by the other model. Not an audit.

**Verdict: ADVANCE, as an implication from (6).** Checked line by line by Claude, first failing step none. It agrees with SA (FG1)-(FG12).

The steps, each redone:

- **D_0.** D_0 >= C_0 >= ||C_0^{-1}||^{-1} >= K_G^{-1}, since C_0 Gamma_0 Gamma_0^T C_0 >= 0. Also ||D_0|| <= K_G + K_G^2 K_G^2. Correct.
- **D - D_0.** Telescoping the three factors of C Gamma Gamma^T C gives ||D - D_0|| <= eps_G + 4(K_G + eps_G)^3 eps_G. Bilinear transposes keep operator norms. Correct.
- **Re D^{-1}.** For a complex symmetric S, the entrywise real part is the Hermitian part. If ||D - D_0|| <= 1/(2K_G), then ||D^{-1}|| <= 2K_G and ||D^{-1} - D_0^{-1}|| <= 2K_G^2 ||D - D_0||. So Re D^{-1} >= (K_G + K_G^4)^{-1} - C(K_G) eps_G. Correct.
- **Q_0.** Expanding (b - C_0 Gamma_0 xi)^T C_0^{-1} (b - C_0 Gamma_0 xi) + |xi|^2 gives b^T C_0^{-1} b - 2 b^T Gamma_0 xi + xi^T (I + Gamma_0^T C_0 Gamma_0) xi, the form of Q_0. The shear L_0 and its inverse have norm <= 1 + K_G^2. So Q_0 >= min(1, K_G^{-1}) (1 + K_G^2)^{-2}. Then ||Q - Q_0|| <= C(K_G) eps_G needs ||C^{-1} - C_0^{-1}|| <= 2 K_G^2 eps_G, which is the resolvent identity. No dimension enters. Correct.
- **Marginal.** The Schur complement is C^{-1} - Gamma (I + Gamma^T C Gamma)^{-1} Gamma^T. Woodbury with U = C Gamma, V = Gamma^T C gives D^{-1}. Here I + Gamma^T C Gamma = Q_xixi has positive real part, so it is invertible. det Q = det C^{-1} (eliminate the b block) and det Q = det Q_xixi det D^{-1} (eliminate xi). So det D = det C det(I + Gamma^T C Gamma). Correct.
- **Branch.** The identities hold at real symmetric data by real Gaussian integration. Real symmetric C and real Gamma form a totally real set of full dimension, so one-variable identity theorems extend them. Determinants do not vanish on the convex ball, so the root continues from the positive reference root. Correct.
- **(7).** |J[F]| <= F_* |det D|^{-1/2} det(Re D^{-1} - 2 rho)^{-1/2}. Write D = D_0(I + E_2) and Re D^{-1} - 2 rho = D_0^{-1}(I + E_1). Then ||E_2|| <= C eps_G and ||E_1|| <= C(eps_G + rho). With |tr E^n| <= m ||E||^n, each factor is at most (1 - ||E||)^{-m/2} <= e^{m ||E||} for ||E|| <= 1/2. This gives F_* e^{A_K(eps_G + rho) m}. Only m enters. Correct.
- **Failed cutoffs.** On the failed set, sum over P_0 of |b_beta|^2 >= v b^2. The blocks are disjoint, so |b|^2 is at least that sum. Hence the indicator is at most e^{(gamma/2)(|b|^2 - v b^2)}, and (7) at rho + gamma/2 gives the tail. Correct.

**Scope.** This is (7) given (6). Input (6) is `um-envelope.md` (7) with the adopted inverse-root series (`inv-root.md`, `carrier-adopt.md` Section 1); I did not recheck it. The tilt |b|^2 must be the Euclidean norm in the same orthonormal coordinates as D. The per-bond norm |B(b)|^2 of UM1 must be a sum of squares of those coordinates. I take that as part of the coordinate convention; no defect.
