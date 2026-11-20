lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:12Z

# gap-mini-solve-j-fable (queue row 1200)

Research-stage working state. Nothing here is a public claim, and nothing here grants status.

Item: FINISH.md queue row 1200, `gap-mini-solve-j-fable`. The problem as the row states it: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Pinned commit: 3c181a68c on `claude/ym4d-hard-route`. Start time (date -u): 2026-11-20T03:11Z.

Labels used below: PROVED (every step written here or in a cited checked file), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## Step 0. Save protocol

This file was created before any proof work. Each step below was appended when it ended.

## Step 1. What was read before choosing an attack

Read at the pin, in this order (no proof work yet):

- `GOAL.md` in full; `FINISH.md` L1-84 (state, method), L299-360 (joining, efficiency, rules), the row of this item (L1281).
- `parts/gap.md` L1-104 (formulation, the wall (W), methods 19-36, lead rules) and L223-322 (route registry, test table, the exact price).
- The RESULT lines of the plain-brief rows 1188-1190, 1193-1195, 1197, 1199, 1201 (Claude Fable 5.2), rows 1205-1208 (Gemini Argon and its checks), rows 1209-1211, 1214, 1216-1218.
- `library/gap-mini-branch-fable.md` Sections 5-6: (N-phys) and Theorem BP (the gap clause given the one-cube neutral bound and the continuum datum).
- `library/prior/gap-o4-pinned-cell-read-opus.md` L57-200: the reading of OpenAI's pinned-cell stiffness iteration for the 2D O(4) model (credit: OpenAI, posted and unrefereed).
- The RESULT lines of rows 1007, 1009-1011, 1013, 1016 (the readings of the 2D proofs and the three gauge ports).

What this reading fixes for the present row (all on file, nothing new):

1. The lane's reduction ends at (N-phys): one bound s_+(u; n^3) <= 1/2 on the centre-neutral excited trace of one cube of fixed physical side, with u <= n/K, at every cutoff. With the continuum datum it gives the gap clause (Theorem BP, row 1179). (N-phys) is an infrared statement of the same strength as the gap.
2. Eight plain-brief rows screened about 100 route candidates and found each one on the lane's map. This row does not screen again.
3. The one mechanism that crosses the band in a comparable model is the 2D pinned-cell stiffness iteration. Its gauge ports stop at the same place each time: a link translation has no cost form that is a curl form in a rough non-abelian field (rows 1011, 1013, 1016, 1188, 1193, 1197).

## Step 2. Candidates derived in this row and their matches on file (GUIDE; no new route)

Each line is: the idea as I derived it, then the place where the lane already holds it. Every match was found by `grep -n` in `library/gap-*.md`, `parts/gap.md` or the FINISH rows before the idea was worked. Nothing in this step is new.

| Idea derived here | Where it stops | On file |
|---|---|---|
| Stiffness of a pinned 4D cell to an abelian boundary twist as the monotone of a 2D-type iteration | no curl-form cost in a rough field; pin supremum forgets colour coherence | rows 1011 (Propositions B, B'), 1013 (Lemma WN), 1016 (Theorem BH) |
| Two-sided torus action on each link, with corner defects | the corner defects of a constant-curl twist grow with the box | row 1013 C1, row 1193 Lemma PC-c |
| The start ("blind") bound is itself the sign of asymptotic freedom; a charged scalar gives the opposite sign | no mechanism for a size-uniform upper bound of a twist response | row 1051 (`gap-direction3-max.md` 5.3: (BDD-Delta), (BL), (BL-c), (L1); L554-560 names the diamagnetic inequality of Brydges, Frohlich and Seiler) |
| The exact variational form of the response with field-dependent extensions (score of a non-constant field, Bochner term) | needs a field-built frame whose Jacobian cancels the frame defect | row 1128 (NL-gen), row 1034 (STAR, PRIV), row 1141 (OPEN item) |
| Adapted (time-ordered) frames have unit Jacobian | frames decohere with depth; bound of order beta^(2/3) L | row 1051 (Lemma RM, RM-TREE; attempt 2 of 5.3) |
| Heat-kernel Hessian bounds in the time direction (Hamilton's matrix Harnack inequality on a compact group) as a pin-uniform blind bound for the electric part | it is the ambient convexity of the one-step kernel; the magnetic Hessian in lab directions is not a curl form | row 941 (exponential family, Hess Lambda), rows 944, 950 ((SC) and its guide-level failure) |
| Araki-Lieb-Thirring comparison of Tr T^L with a classical (dimensionally reduced) partition function | loses the vacuum normalization; extensive | rows 913, 1180 (Lemma R4), `gap-constraints-max.md` B6 |
| The non-central family Z(K), K a commutator of two constant colour twists, as a path from the periodic to the centre-twisted torus | the response at K = 1 is of area order | row 1013 C2, row 1051 Lemma K4 |
| (BDD-Delta) from monotonicity of the excess free energy in each side | only the volume-order bound e(2L) <= 16 e(L) follows | Lemma E of row 1217; Lemma ADD of row 1018 |
| Charged-to-neutral conversion in a twisted 2D O(4) sheet | frustrated abelian examples keep neutral order with charged decay | rows 1115, 1139, 1194 ((SING), method 36) |

Reading of the table (ARGUED, same as rows 1051 and 1197): in the 2D engine the start bound is free and each mode lowers the stiffness. In 4D the response to a background field has two one-loop parts of opposite sign (orbital and spin; Nielsen 1981, Hughes 1981). So an induction that carries only upper bounds on cell stiffness has no sign for the orbital part. This is the reason the direct ports stop, and it is on file.

## Step 3. One reading not found on file in this form: the spin part of the one-loop coefficient as a count of flat directions

Kind of result: a reading of published physics in the lane's variables, with one elementary lattice lemma. It is not a proof step. Labels are per paragraph.

### 3.1 The split 11/3 = 4 - 1/3 in a self-dual background (RECALLED, not re-read in this run)

Credit: 't Hooft (1976, the one-instanton determinant; 1979 and 1981, twisted tori and solutions of constant field strength); Nielsen (1981) and Hughes (1981) for the orbital and spin reading; Gonzalez-Arroyo and Montero (1998) for fractional instantons on twisted tori. The lane holds the split as a recalled number (row 1011, `gap-pinned-cell-gauge-max.md` L496) and the fractional instanton as the carrier of the crossed twist (row 858, `gap-crux-exercise-r858-max.md` L324).

- In a self-dual background of topological charge Q, the non-zero modes of the gauge fluctuation operator pair with those of the covariant scalar Laplacian. So the non-zero-mode part of the one-loop weight is that of charged scalars. Its scale dependence is the orbital (diamagnetic) part, a factor (L/a)^(-NQ/3) for SU(N).
- The gauge operator has 4NQ zero modes. Each zero mode gives one factor L/a. This is the whole spin (paramagnetic) part.
- For SU(2) and Q = 1/2 (the crossed pair of centre twists, n_12 = n_34 = 1): four zero modes. The weight of the twisted sector is e^(-4 pi^2/g_0^2) (L/a)^4 (L/a)^(-1/3) = e^(-4 pi^2/g^2(L)), with 4 - 1/3 = 11/3. In lattice normalization 4 pi^2/g_0^2 = pi^2 beta.

So in this channel the term that gives asymptotic freedom is an index. It counts flat directions of the minimum set of the twisted sector. The term with the other sign is a determinant of scalar type. The diamagnetic inequality of Brydges, Frohlich and Seiler fixes the sign of that part and gives no upper bound for it.

### 3.2 The flat directions on the lattice (Lemma V, PROVED, elementary)

Setting. Torus (Z/L)^4, L >= 2, action A(U) = sum over plaquettes of (1 - x_p), x_p = (1/2) tr U_p. Sector (1,1): the sign of x_p is flipped on the L^2 plaquettes (x; 1, 2) with x_1 = x_2 = L - 1 and on the L^2 plaquettes (x; 3, 4) with x_3 = x_4 = L - 1. Sector (1,0): only the first flip. Put phi = pi/L^2 and a = i sigma_3.

**Lemma V.** (a) For every c in R^4 the abelian field U_mu(x) = exp(a (a_mu(x) + c_mu)), with a_1 = - phi x_2, a_2 = phi L x_1 on the layer x_2 = L - 1 and 0 elsewhere, a_3 = - phi x_4, a_4 = phi L x_3 on the layer x_4 = L - 1 and 0 elsewhere (coordinates taken in 0, ..., L - 1), has in sector (1,1) the action

  A_perp(L) = 2 L^4 (1 - cos(pi/L^2)), and 4 <= A_perp(L) <= pi^2 for every L.

(b) The action does not depend on c. The Polyakov line of direction 1 at height x_2 has trace 2 cos(L c_1 - pi x_2/L), so the family has four parameters that gauge maps do not remove.
(c) The same field with a_3 = a_4 = 0 has action L^4 (1 - cos(pi/L^2)) >= 2 in sector (1,0). Sector (1,0) also holds a field of action 0 (Lemma K4 of row 1051: the constant twist eaters).

Proof. (a) A (1,2)-plaquette at x has angle a_1(x) + a_2(x + e_1) - a_1(x + e_2) - a_2(x). For x_2 < L - 1 this is - phi x_2 + phi (x_2 + 1) = phi. For x_2 = L - 1 and x_1 < L - 1 it is - phi (L - 1) + phi L = phi. At x_1 = x_2 = L - 1 it is - phi (L - 1) - phi L (L - 1) = phi - phi L^2 = phi - pi, and the flipped weight of this plaquette is - cos(phi - pi) = cos(phi). So every (1,2)-plaquette contributes 1 - cos(phi). The (3,4)-plaquettes are the same. A mixed plaquette (mu, nu) with mu in {1, 2} and nu in {3, 4} has angle 0, because a_mu does not depend on x_nu and a_nu does not depend on x_mu. There are L^4 plaquettes in each plane. The bounds follow from 2 u^2/pi^2 <= 1 - cos u <= u^2/2 on [0, pi]. (b) A constant added to a_mu cancels in every plaquette angle. The Polyakov line is the product of L links exp(a (c_1 - phi x_2)). (c) is the same computation with one plane. QED

Reading (ARGUED). In the link metric a constant shift of the L^4 links of one direction by an angle delta has norm delta L^2, and delta runs over an interval of length of order 1/L. So each flat direction has length of order L in lattice units. A stiff direction of curvature beta lambda contributes a width (2 pi/(beta lambda))^(1/2). Four flat directions in place of four stiff ones give the factor (L/a)^4 of 3.1, up to powers of beta. Sector (1,0) has an isolated minimum (row 858 item 3) and no such factor. I did not prove that the family of Lemma V is the minimum set of sector (1,1) on the lattice.

### 3.3 The selective inequality this reading suggests, and where it stops

Let R(L) = Z^(1,1)(L^4)/Z^(1,0)(L^4). By row 859 Stage 1a (`gap-brainstorm-max.md` 4d), 0 < R <= 1 and 1 - R is twice the weight of odd electric flux in the box with magnetic twist.

(X) There are kappa > 1 and r_0 > 0 with R(2L) >= min(kappa R(L), r_0) for all L in the band, at one bare coupling.

Semiclassical value (RECALLED arithmetic of 3.1): kappa = 2^(11/3), about 12.7. It is the product of 16 from the four flat directions and 2^(-1/3) from the scalar-type determinant. So a proof of (X) could lose a factor up to 16 per doubling in the determinant part. The true loss there is 2^(1/3). This margin is the only new information in this step. In the 2D engine the corresponding margin is zero: the sharp constant was needed.

(X) is the symmetric-torus form of (MON') of row 859 (`gap-brainstorm-max.md` L655), which is on file as OPEN. I tried three ways. Each stops at a step that is on file.

1. Doubling the time side. With a, b the even and odd flux traces at time t, R(t) = (a - b)/(a + b) and R(2t) = (a^2 p_e - b^2 p_o)/(a^2 p_e + b^2 p_o), p the purities of the two sector states (Lemma 4 of `gap-skeleton-max.md` Part E in other letters). If p_e >= p_o then R(2t) >= 2 R(t)/(1 + R(t)^2). The purity order is not known. First failing step: p_e >= p_o.
2. Doubling a space side. The tunnelling splitting of the two twisted vacua must grow with the volume of the slice. A comparison of the slice of side 2L with two slices of side L needs reflection positivity across the background twist. That fails (row 859 Stage 2). First failing step: no positive form across the twisted column.
3. Disjoint placements. A translation-equivariant position of the lump gives P(position = v) = L^(-4) exactly, with no content. The content is the weight of the pinned lump against sector (1,0), at two sizes. That comparison is a block renormalization step, and its sign is asymptotic freedom again. First failing step: a bound for the pinned weight at size 2L by the one at size L with loss below 16.

### 3.4 Controls (ARGUED)

- Compact U(1): the crossed twist has integer fluxes with action of order beta and a field that is constant up to gauge. There are no flat directions beyond the holonomies that the untwisted sector also has, so the count gives no factor, and R(L) is constant in L at weak coupling. (X) fails with kappa = 1, as it must.
- Frozen Q_8 and binary tetrahedral group: no continuous directions. The vortex action is of order beta L^2. (X) fails.
- Five dimensions: the action of the lump grows like the size. The entropy of flat directions is logarithmic and loses. (X) fails at weak coupling, as it must.
- Product with a massless factor: (X) reads the centre of the SU(2) factor only. It can hold there and gives no neutral bound.

### 3.5 Why this does not move the row's target

(X) is a twist-only statement. By the council synthesis 2c (row 1134), a twist-only tool reaches at most the flux half, and the lane's present target (N-phys) is the neutral half. For the neutral half the flat directions of the periodic sector are the abelian holonomies, and the one-loop effect on them is of scalar type (a flat background has no spin term). So the index reading gives no gain there. I found no neutral analogue.

