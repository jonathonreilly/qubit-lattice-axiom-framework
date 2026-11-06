lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T13:39Z

# b102-gate-b: check of library/b102.md, H15-H25 and the Result

Status: in progress (started 2026-11-06T01:39Z). Sections are added as the check proceeds.

## Scope and provenance

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, pinned at commit 242d44119 on `claude/ym4d-hard-route`. Text by Codex (round 3 of `library/b102.md`, lines 1992-3630). One line-by-line reading by the other model. Not an audit; grants no status. I did not write the text.

Read: `library/b102.md` §1 target (T1)-(T7) (lines 36-160), H2-H8 statements (321-897) as the inputs H15-H25 read, Lemma O (906-937), H9 (1247-1345), and all of §8 and the Result (1992-3630). Balaban's text read on the printed pages of `~/ym4d-papers/balaban_cmp102_277.pdf`, rendered locally (nothing copied into the repository). Credit: T. Balaban for every operator, equation number and estimate compared here; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account arguments ported in H16, H17 and H24.

## Running notes (replaced by the verdict table at the end)

- H15: in progress. Adjoint and unit conversions (H15.6) re-derived: B^dagger = Q^* l^-3, Gamma_0 = l J_0 l^-3, H_0 = G_0 Q^* J_0^-1 l^-1. |B^dagger e_c| <= C l_c^-3 re-derived from (H9.2) (pillar multiplicity up to n). Gram upper bound from B: E -> l^2 and K_U >= c J_E.
- H16: ADVANCE. Cauchy on one kernel entry, transpose (H16.3), weighted bound (H16.4) and the four-term telescoping for D_3 re-derived. D''(0) = C''(0) checked (T'(0) = I, R(0) = 0). Import (H16.1) is `a1-balaban.md` §3.5 (kernel bound C_3 r s^{1-d}, gate a1-balaban-gate.md: ADVANCE).
- H17: ADVANCE. Scaling of all four members re-derived; matches CMP 99b (3.42)-(3.45) (printed p. 397-398: value, gradient, G nabla^*, covariant Laplacian; Hoelder for beta < 1 with B_0(beta) -> infinity as beta -> 1; mixed member on Hoelder data). Import (H17.3) is flat-port (4.1) as stated (scalar equation with divergence source, r >= 16 eta); H17 applies it per component in a small local gauge, which is legitimate. (H17.5) differs from printed (3.49) only by a scale ratio absorbed in the exponential.
- H18: ADVANCE for (H18.1)-(H18.8), (H18.10) and positivity; GAP at the Y -> X_beta claim for the two-constraint inverse (H18.9) (see finding F1). Re-derived: second-order gauge invariance gives Delta D lambda = k_J(lambda), D^* Delta D = -m_J, so E_pi = -Theta'_J and G_pi = G^J_pi of CA-I 13680-13979. RD^*S = 0, G_i DR = DG'R, RD^*H_i = 0, both constraints of (H18.9) vanish, (H18.10) = printed CMP 102 (137).
