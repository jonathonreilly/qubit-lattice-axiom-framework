lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T06:48Z

# Gate: `library/a2-curved.md` Sections 4, 5, 6, 8, 9, 10, 11, 12 (row 93, `a2-curved-gate`)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; repository
commit a5188ee27 (branch claude/ym4d-hard-route); gating `library/a2-curved.md` (OpenAI Codex, written at
d7043777d) for its reader `library/a2-layers.md` (Claude). The outline `YM4_sketch_500.tex` at
31a47c543775 (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text) was fetched by URL
into a scratch folder and not committed; outline line numbers below refer to it. Gate by hand, one reader, not an
audit, grants no status. No numerical job was run.

Status: in progress, written section by section.

## 4. Exact transfer between the two gauge projections: ADVANCE

I redid the proof. Take the minimiser of ||v - Dz|| over Z. The normal equation gives P D^* v_0 = 0, and
C v_0 = 0 because CDZ = 0. The cross term in beta vanishes (null identity with v_0 in ker C), and so does
beta(Dz, Dz) (null identity with Dz in ker C). The bound ||Dz|| <= p ||D^* D z|| and the identity
D^* D z = R D^* v - R D^* v_0, with ||R D^* v_0|| <= ||D^* v_0||, give (4.3) with the constants stated.
(4.2) applied to v_0 also gives beta(v_0, v_0) >= 0, so nothing is assumed there.

I checked the identification of R against the outline (L10142): R = 1 - G'Q'^T (Q'G'^2Q'^T)^{-1} Q'G' is the
orthogonal projection onto ker(Q'G') = G'^{-1} ker Q' = Delta_U ker Q' = D^* D Z, as §3 and §4 say. The warning
about the null identity is right: it holds for the stationary Lagrangian Hessian, and it is false for the Wilson
Hessian alone at nonzero current. **For the reader:** `a2-layers` does not use §4 on layers (its §5, L439, says
it replaces §4 there). §4 is an input only to a2-curved's own uniform-torus line.

## 5. Curved one-step statement, node-free, depth zero: ADVANCE

I checked every step against the outline's definitions: the block map (QC1)-(QC4), L7931-8010; the pivot
(QC15)-(QC20), L8165-8240; the chart (QC22)-(QC24); and the soft gauge (CF2)-(CF3) with its normalisation
A(e^{ita}) = t^2||da||^2/2 + ... . All of them agree.

- **(5.2), local flat injectivity.** I redid it. Zero curl inside a block makes the internal field a gradient
  (the cube is simply connected), and the contour means then equal phi(x) - phi(y). With zero contour sums, every
  internal bond vanishes. Face plaquettes then equate neighbouring crossing values, and the transverse grid of
  L^3 crossing bonds is connected, so all crossing values on a face equal one value b_c. By (QC15), the row is
  L^{-4} sum_x a([x,x']) = L^{-3} * L^3 b_c = b_c, so zero rows kill the crossings. Compactness gives m_L > 0.
  Each bond starts in exactly one block, so the sum over blocks recovers ||B||^2. (nu_L <= 81, independent of L.)
- **Block-constant frame.** The contour mean (QC1) is covariant, av(g T_j h^{-1}) = g av(T_j) h^{-1}, so
  V^s(y,x) = s(y)s(x)^{-1}. The block-constant replacement keeps every link at 1 + O_L(eps) and keeps axiality.
  d_V, G_V and K_V transform by Ad, which is orthogonal (q_{V^g}(Ad_g a) = Ad_{g(y)} q_V(a)). This step is correct.
- **(5.3).** Correct, given the two estimates above.
- **(5.4).** It is (QC22)-(QC23). The pivot b_0(c) is the only pivot in the support of q_{V,c}, so the fixed
  point decouples row by row (outline L8283-8285). D Psi(0) = I, and D^2 Psi(0) = -h_V D^2 q_V(0).
- **(5.5)-(5.6).** The chart Hessian is F'' + DA(V)[D^2 Psi], with DGF(V) = 0 at an axial V. The Wilson second
  variation is ||d_V B||^2 + O(eps)||B||^2. The gauge Hessian is exactly ||G_V B||^2, because X(0) = 0 for the
  contour logarithm. ||J(V)|| <= C eps, because the inserted generator is traceless. Finally
  ||B|| = ||C_V u|| >= ||u||.
- **(5.7).** The Schur row-and-column test is applied to a finite-stencil analytic difference. Re<u, E_W u>_H
  >= <u, E_V u>_H - ||E_W - E_V|| ||u||^2 holds because E_V is real symmetric. One point is not stated: at
  non-axial W, the term DGF(W)[D^2 Psi_W] is either dropped or included in E_W. Either way it is O(rho) on the
  same stencil, so nothing breaks.

**For the reader:** `a2-layers` Lemma N reads exactly this mechanism, with injectivity redone per boundary pattern.

## 6. An explicit regular curved family: CORRECT-NO-ADVANCE (the identity a2-layers reads is correct)

- **(6.1).** I checked the plaquettes: theta away from the seam; -theta N n_2 + theta N(n_2+1) - theta(N-1) =
  theta on the seam; -theta(N^2-1), equal to theta modulo 2 pi Z, at the double wrap. No other plaquette is
  affected. J = 0 exactly: the two incident 12-plaquettes give sin(theta) and -sin(theta) on Z, and the
  off-diagonal generators have zero trace against Cartan elements. The local potential A_2 = f(x_1 - x_{1,0}) Z and
  the regular-pair clauses hold at C M_1 L^2 f < alpha_0.
- **Neutral sector.** (6.2)-(6.3) are correct. The one-step decomposition P_L = S_L - d sigma and P_L df = d(r_L f)
  are (QC15) on gradients. S_L o S_L = S_{L^2} by the block digits. For the row and column weights of T_n
  (n^2 and n^{-2}), I redid the count: each fine plaquette lies in n^2 start/square pairs, each of weight n^{-4}.
  So ||T_n F|| <= ||F||. The S_n / P^{[k]} exchange by a fine gradient, and (6.5), are correct. Q = S_n is the
  right per-length row on the neutral sector, because the outline (L7108) has Q^sharp = Q^st at U = 1, and the
  neutral linearisations are the flat ones.
- **What a2-layers reads (Lemma F).** For K = F + Q^T a Q > 0 and Q onto,
  min_{Qh=b} F[h] = <b, (Q K^{-1} Q^T)^{-1} b> - <b, a b>. This is elementary and correct.

Section 6 is a test family and a neutral-sector proof. The charged colours are not treated there, so A2 does not
move on §6 itself.
