lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T06:48Z

# Gate: `library/a2-curved.md` Sections 4, 5, 6, 8, 9, 10, 11, 12 (row 93, `a2-curved-gate`)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; repository
commit a5188ee27 (branch claude/ym4d-hard-route); gating `library/a2-curved.md` (OpenAI Codex, written at
d7043777d) for its reader `library/a2-layers.md` (Claude). The outline `YM4_sketch_500.tex` at
31a47c543775 (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text) was fetched by URL
into a scratch folder and not committed; outline line numbers below refer to it. Gate by hand, one reader, not an
audit, grants no status. No numerical job was run.

Status: complete (all eight sections gated; summary at the end).

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

## 8. Second jet of the straightened constraint, no depth factor: ADVANCE

- **(8.1).** This is the outline's straightened one-step map (L7092-7100): block factor u, then
  e^{iQ^1} M(W_0) = u(c_-)^{-1} M(W) u(c_+), iterated along W_s = M^s W_0, with a_0 = eta A. q_c = xi^{-1} a_j is
  the per-length row (L10139).
- **(8.4)-(8.5).** I redid the normalised recursion. With z_s = v_s/t_s + p_s/t_s^2 and t_s = L^{s-j}, dividing
  (8.4) gives z_{s+1} <= z_s + C t_s (z_s + z_s^2), using t_s <= 1. The sum of t_s is (1 - L^{-j})/(L - 1), so
  z_s <= z_0 e^{2C/(L-1)} until a first exit, and a small a excludes an exit. The linear plaquette rate L^2 is
  the row sum of T_L (as in (6.4)). The factor (1 + C v_s) is needed only for complex, non-unitary comb gauges.
  p_0 = O((a + a^2) t_0^2) holds because the linear insertions telescope to a first difference.
- **(8.6).** I checked that DF_1(0) = S_L: the u-terms cancel the sigma-terms of (QC15). Its row sum is L. Its
  column sum is L^{-3}: a bond lies on L segments in total, each of weight L^{-4}. The perturbation is
  entrywise, on finitely many entries per row and per column, so the column bound is proved directly and not
  inferred from the row bound.
- **(8.7)-(8.9).** Row and column norms are submultiplicative, and exp(C sum v_s) <= 2. The chain rule (8.8) is
  the second derivative of a composition at a_s = 0, with F_W(0) = 0. I redid the sum: entry of P_{j,s+1} <= its
  column bound 2L^{-3(j-s-1)}; column of P_{s,0} 2L^{-3s}; sup_i sum_{c,h}|D^2F| <= C_L; row of P_{s,0} 2L^s. The
  total is C_L L^{-3j+3} sum_{s<j} L^s <= C'_L L^{-2j}. Units: eta^2 xi^{-1} L^{-2j} = eta^4/xi^3 = xi(eta/xi)^4.
- **(8.10).** Multiplying by xi_c^4|omega_c| gives C gamma eta^4 xi_c^{-2}. Normalising by the masses gives
  C gamma sigma_b sigma_{b'}/xi_c^2. In the separated whole-block geometry a fine bond lies in carriers at
  adjacent levels only, and in boundedly many rows at each. The Schur test closes it.
  <A, Delta^(2)[omega] A> = 2(C^(2)(A), omega) (L10180) is the same pairing.

The regular-pair clause on cubes in L_j ∪ L_{j+1}, measured at xi_j (L10137), gives (8.2) on the dependence cube
of a level-j row with a = O(L^2 alpha_0 + L^2 alpha_1); outward rows reach into L_{j-1}. "Adjacent-scale factor
included in a" is the right reading. **For the reader:** a2-layers also reads |V_p - 1| <= C_L alpha_0 at level k
from (8.4)-(8.5), i.e. p_k <= z_k t_k^2 with t_k = 1. That reading is correct.

## 9. On-shell multiplier: ADVANCE

- **(9.3).** I redid the arithmetic. The outgoing and incoming start counts are i + m + 1 = n/2 + x_i and
  m - i = n/2 - x_i. sum x_i = 0 and sum x_i^2 = n(n-1)(n-2)/12. Then l_+(phi_+) = n^{-2}[n^2/2 + n^2/2] = 1 and
  l_-(phi_+) = 0, and symmetrically for phi_-. |phi| <= 4n/(n-1) <= 6 (n = 3 gives the values -3 and 6).
- **Leakage geometry.** Each Omega_j is a union of whole level-j blocks, so a level-j seed pillar lies in
  Omega_j minus Omega_{j+1}. Lower-level carriers lie outside Omega_j: inward bonds carry no row, and outward
  carriers point outward. Carriers two or more levels up lie in Omega_{j+1}, including the outer blocks of
  outward rows, because of separation. So only the outward rows of level j+1 can receive leakage. At a flat
  reference the full-grid same-level response is exactly psi extended by zero (orthogonality of phi_+ and phi_-),
  so the leakage is the restriction of the per-length L^{-1} S_L. Its column sum is L^{-4}, and its norm in
  ||.||_{1,xi} is L^{-3}.
- **Curved case.** Telescoping the products of (8.7) gives column error C_L a n^{-4} per unit length, times
  about n^4 seed bonds, so the total error is C_L a (this is why the column power matters). The connection between
  two local gauges moves by C_L a over a carrier. Hence (9.5), and E = E^0(1 + T)^{-1}.
- **(9.2).** The duality <omega, psi> = <J, E psi> with a one-row psi is correct.
- **J = Q^T omega on shell.** I checked RD^T S = 0 and QS = Q. The one-step linearisation of (8.1) at a gauge
  variation is Q'lambda(y) - Ad(M W(c)) Q'lambda(y'), so Q D Z_s = 0. At an outward end the full-pillar mean is the
  transported mean of leaf means, which are all zero. The inner-plaquette action is exactly invariant, so
  <J, Dz> = 0. Criticality on the slice gives <J, Sv> = 0. Duality, with Q onto, gives omega = H^T J for every
  right inverse H. The step reads "physical critical" as criticality for the straightened row constraints in the
  fixed slice. That is the outline's system of (1b) (L10208), and a2-layers reads it the same way.
- **(9.6).** It follows from the §5 plaquette insertions, with |dU_p - 1| <= alpha_0 eta^2 sigma^{-2}, together
  with (8.10) and (9.2).

## 10. Fine Landau form on a uniform torus: ADVANCE

- **(10.2), flat.** I redid the Fourier proof.
  - Constants and identities. Alias sum of |r^|^2 = 1 by DFT Parseval. |b_mu(p)| >= 2/pi from
    sin x >= 2x/pi, which gives c_1 = (2/pi)^10. For q an alias of p in the fine zone, |q| >= |p|, which
    gives c_2 = (pi/2)^2. r_0 g = c because r_0 (-Delta)^{-1} r_0^* = B(p). D'^* zeta = B^{-1} c. D_0^* e = 0
    uses Q_0 D_0 = D' r_0.
  - Bounds. ||g|| <= g_0 ||c|| and ||(-Delta)^{-1} de|| <= b_0 ||c||, with exactly the constants stated.
  - The pairing step is the one that needs checking. With phi = r_0^* c + P_0 phi, which uses r_0 r_0^* = 1:
    ||c||^2 = <h, e> - <P_0 phi, g> = <dh, (-Delta)^{-1} de> - <P_0 phi, g>. So
    ||c|| <= b_0 ||dh|| + g_0 ||P_0 phi||, as claimed.
  - Hodge, the row variance bound and p = 0 are handled correctly. Row densities are <= eta^4 per bond with
    total weight 1. c(0) = 0, and h has no constant mode once Q_0 h = 0.
- **Inhomogeneous version.** For the tents I checked: the moments of p[1 - a(t-a)/v] and p[1 + (1-a)(t-a)/v]
  against (1 - t, t) are (1, 0) and (0, 1); the mass of each interval is 3/32 >= 1/128; and v >= 2^{-18} by the
  pair variance with separation 1/4. The tents vanish near the pillar faces, so the physical gradient is O(1).
  The (9.3) profiles cover 3 <= n < 128, and the identity covers n = 1. On one level there is no leakage, so
  Q_0 E_0 = 1 exactly.
- **(10.3)-(10.4).**
  - (10.3). The Schur bound for Q - Q_0 uses row error C a and column error C a n^{-4}, where
    n^{-4} = eta^4 matches the physical bond weight. rr^* = 1 for unitary transports.
  - Globalisation. The bound sum_i ||[P, chi_i] f||^2 <= C R^{-2} ||f||^2 is right. R is fixed before
    alpha_0, and c_g M_1 >= R is needed for the local gauges.
- **(10.5), null identity.** This is correct. The exact covariance of the straightened map is
  e^{iF(a')} M(W) = (e^{iF(a)} M(W))^{r_1} with r_1 = u(a')^{-1} g u(a) at the coarse sites (outline L7339), so
  the variation under lambda is a coarse gauge variation with parameter r~(A) lambda, and r~(0) = Q'.
  lambda_z(A) lies in ker r~(A). F and q are both null on X_z(A), and D L(0) = 0 then gives beta(D_U z, .) = 0.
- **Poincare and §4.** ||z|| <= p_L ||D_U z|| on ker Q' holds pillar by pillar. The application of §4 with
  C = 0 and P = 1 - r^*r is legitimate. Finally S^T beta S = beta follows from (10.5) and S = 1 - D G' R D^T,
  so K_phys = G_1^{-1} at physical pairs (with H^T J = omega from §9 and (A, Delta^(2)[j] A) = D^2 q[j][A, A]).

**For the reader:** the reads of a2-layers are correct as stated: (10.2), its inhomogeneous version, the tent
and (9.3) lifts, and (10.4) as the template for its Theorem 2.

## 11. Real A2 on the uniform node-free torus: ADVANCE

- **(11.2).** In one local frame: d_V Q h = T_n d_U h + [T_n (d_0 - d_U) + (d_V - d_0) Q + d_0 (Q - Q_0)] h.
  Each bracketed term is C_L alpha_0 ||h||. ||T_n|| <= 1 in physical norms, because
  ||d_0 h||_phys^2 equals the raw curl energy of w = eta h. The scalar majorant of T_n is frame-independent,
  so the global Schur sum holds.
- **(11.3)-(11.4).**
  - The slice P D_U^* h = 0 is a valid gauge slice: z -> P D^* D z is positive on ker Q', by Poincare.
  - Differentiating F'(A) = Dq^T omega gives beta h_b = Q^T omega_dot, so beta(h_b, v) = 0 for all v in ker Q.
    f'' = <omega_dot, b> = beta[h_b, h_b], and the minimum follows from beta >= 0 on ker Q via (10.5) and the
    slice.
  - The plain/straightened identification is right: the node factor is restored by a fine gauge, and the
    converse uses a right inverse of Q' on {lambda = 0 at nodes}, for n >= 3.
  - (11.4) follows by shifting the Landau term away with D_U Z_s, at no cost in beta or Q.
- **(11.5) and the end.** I substituted each step and they check. The chart term is f'(0)[D^2 Psi_V] =
  -<omega, h_V D^2 q_V(0)[b, b]>. Its bound C_L gamma_0 ||b||^2 uses |omega| <= C_L gamma_0 from (9.2),
  ||h_V|| <= 2L^3 and the finite stencil. The gauge Hessian is exactly ||G_V b||^2 at an axial V. (5.3) applies
  because p_k <= C_L alpha_0.

One identification is not re-derived here: this chart term equals the outline's C_V^T E^(2)[H_1^T J] C_V.
`a2-layers` §8.2(c) correctly lists it as a consumer statement. **For the reader:** only the bound on this term
is used ("§11, last step"), and the bound holds whichever identification is used.

## 12. Complex half-gap at nearby physical critical pairs: ADVANCE (for the subcase (12.1))

- **(12.3)-(12.5).** In (12.3), the commutator of two translated covariant differences is the adjoint
  plaquette holonomy, of size alpha_0 eta^2 sigma^{-2}; divided by eta^2, it costs C alpha_0 at sigma = 1. (12.4)
  uses d_U D_U z = curvature times z and ||D z||^2 <= ||z|| ||Delta z||. For (12.5), the lower bound goes through
  h = h_0 + D z: ||h_0||_1^2 <= C beta~ by (10.4) and (9.6), and ||Delta z|| <= ||R D^* h|| + ||D^* h_0||.
- **Cauchy step, (12.6)-(12.9).** (8.4)-(8.7) hold on the whole complex disc, by (8.2) with complex E.
  E_W = E^0 (Q_W E^0)^{-1} has Neumann series in both l^2 and l^1. omega_W = E_W^T J_W follows from the
  holomorphic duality. The l^1 -> L^1 bound gives (12.8).
- **Site Gram.** I checked <G'_U r_U^T b, M_U E_s b> = <r^T b, E_s b> = ||b||^2, so B_U >= C^{-2}. The lift E_s
  (C^2 bump with mean one, centre-supported for n < 128) has ||M_U E_s b|| <= C_L ||b||. In the complex case
  r_W r_W^T = 1 holds for the bilinear transpose, because Ad(g) preserves tr(XY) for g in SL(2,C).
  r_W G'_W R_W = 0, so S_W h = h - D_W z with z in ker r_W, and S_W^T beta_W S_W = beta_W follows from the
  holomorphic (10.5).
- **(12.10)-(12.12).** I checked Q_W T = Q_U for T = 1 + E_W(Q_U - Q_W), and the bound S_{1,U} <= C by testing
  with E_U b.
- **§7, read here and by a2-layers.** I redid (7.1). Z^T Z = I, ||D|| <= e/(1-e), and S = S_0^{1/2}(I+D)^{-1}S_0^{1/2}
  give e/(1-2e). For e <= 1/4 the Hermitian real part is at least half.

**Not load-bearing.** §10 (last paragraph) and §12 identify G_1^{-1} = K exactly. For this they use the outline's
gauge identity Delta^W - Delta'_pi[J(U)] = S^T Delta^W S (L10187; a2-layers lists it with PX94-95 as unchecked),
which I did not re-derive. The gap does not need it. Without it, G_1^{-1} - K = -Delta'_pi[J] + D^2q[omega]
- S^T D^2q[omega] S. That is O(gamma_0) in the H^1 form: the explicit formula (L10180) is bilinear in
lambda = G'R D^T(.) and D lambda, both bounded in L^2 by ||.||_1, times |J|; (8.10) and (12.10) bound the rest.
§7 then absorbs it.

**For the reader:** a2-layers Theorem B (7.6(a)) reads (8.4)-(8.7) on a complex disc and §5's analytic local maps.
Its 7.2(ii) reads E_s. Both reads are as proved here.

## Verdicts

| Section | Verdict | Read by `a2-layers` |
|---|---|---|
| 4 transfer between projections | ADVANCE | no (replaced on layers) |
| 5 one-step chart, (5.2)-(5.7) | ADVANCE | Lemma N; Theorem B(a) |
| 6 explicit family, neutral gap | CORRECT-NO-ADVANCE | completion of the square only (correct) |
| 8 second jet (8.3)-(8.10) | ADVANCE | yes |
| 9 on-shell multiplier (9.1)-(9.2), (9.6) | ADVANCE | Theorem 4 only |
| 10 uniform-torus Landau form, (10.1)-(10.5) | ADVANCE | (10.2), inhomogeneous lift, (10.4) as template |
| 11 real A2 on the uniform torus, (11.1)-(11.5) | ADVANCE | (11.2), last step |
| 12 complex half-gap at nearby physical pairs | ADVANCE (subcase (12.1)) | E_s, (12.5), (12.6) mechanism |

Outside the list but also read: (2.1) is correct (zero extension). (7.1) is correct.

**First failing step: none.** No defect breaks a statement that `a2-layers` reads. Non-breaking remarks:
1. (5.7) does not say whether the term DGF(W)[D^2 Psi_W] at non-axial complex W is in E_W. It is O(rho) either way.
2. The exact G_1^{-1} = K in §§10 and 12 rests on the unchecked outline gauge identity. It is not needed for the
   gap (see §12 above).
3. In §11, the chart term = C_V^T E^(2)[omega] C_V is the outline's consumer identification (a2-layers §8.2(c)).
   Only its bound is read.

## What this gate does and does not move

It moves `sa-ledger.md` #2 (A2) on one half of row 90's gate requirement: the a2-curved inputs that a2-layers
reads are confirmed by one other-provider read (Claude on a Codex text; one reader, not an audit).

It leaves open:
- the gate of a2-layers' own Sections 3-7 (row 92);
- the outline identities a2-layers §8.1 uses unchecked (PX4, PX31-38, PX43-47, PX94-95, PX99-100, PX113,
  PX114-119), including the gauge identity above;
- the identification of A with the next-step effective Hessian (PX97-104, consumer side).

a2-curved itself proves A2 only on the uniform node-free torus (real, at physical critical pairs; complex,
for nearby physical pairs). The layered, off-shell and full-complex cases are a2-layers' claims and are not
gated here.

Status: complete. Only this file was written. No numerical job, no subagent.
