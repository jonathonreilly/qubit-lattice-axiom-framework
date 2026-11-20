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


## Step 4. Continuation by Claude Opus 5.5 max (from 2026-11-20T04:12Z, date -u)

Handover. Steps 0-3 above are the earlier run of this row (Claude Fable 5.2 max, Mac mini worker 2, pinned at 3c181a68c). That run ended at the account's Fable weekly limit (FINISH row 1200, lead note 04:20Z) and wrote no RESULT line. Its text is kept as written. Only the lead and lease lines were replaced, as the row's lead note asks. This continuation is pinned at 3065cacc7 on `claude/ym4d-hard-route`.

Read for this continuation (no proof work before this list was done): `GOAL.md` in full; `FINISH.md` L1-84, L299-351 and row 1200; `parts/gap.md` L1-104 and L311-322 (the exact price); `library/gap-mini-branch-fable.md` L300-361 ((N-phys), Theorem BP); the RESULT lines of rows 1180, 1184, 1188-1202, 1211, 1215, 1217 and the briefs of rows 1203-1225; `library/gap-council-rg-fable.md` L195-232 (the virial attack (VIR)); the CA-full index of Sussman and Alpoge for "mass gap" and "clustering" (two statements, CA-III 103479 and 108223; both are consumers of a gap or of clustering for the O(4) clause, not producers).

Plan of this continuation, one step per response, each appended when done:

- Step 5. Where Step 3 stopped ("I found no neutral analogue"): classify the observables whose asymptotic-freedom sign is an index, and decide whether one of them is centre-neutral. Grep each candidate against the record first.
- Step 6. One rigorous lattice statement that the Step 3 reading needs and does not have (the minimum of the crossed-twist action), proved or corrected by hand.
- Step 7. One attack on the neutral half itself, chosen after Step 5, worked to its first failing step.
- Step 8. Results table and the RESULT line.

## Step 5. Which weights carry an index engine, and is one of them centre-neutral (ARGUED; one new reading)

Grep before work: "topological susceptib", "theta-depend", "theta vacu", "instanton number", "Braam", "per doubling" in `library/gap-*.md` and `parts/gap.md`. Matches: the measured value L14 of `gap-measured-assumptions-opus.md` L126 (a number, no engine); the rule for way II of `gap-skeleton-max.md` L165 ((RGI): a non-perturbative coupling q with q(2l) >= q(l) + c q(l)^2, and "q = exp(-f_m/2) is proportional to g(l)^2 at small l and is constant for U(1)"); (MON) and (MON') of row 859 (`gap-brainstorm-max.md` L613, L655). No file uses the instanton-number sectors as an engine. Nothing below is a proof step.

### 5.1 The mechanism of Step 3.1 in general form (RECALLED)

Credit: 't Hooft (1976); Brown, Carlitz and Lee (1977); Nielsen (1981); Hughes (1981); Atiyah, Hitchin and Singer (1978) for the moduli dimension. Let A be a self-dual SU(2) connection of topological charge Q > 0. Then:

- The non-zero spectrum of the gauge fluctuation operator with ghosts is that of two adjoint covariant scalar Laplacians (orbital part, a determinant of scalar type).
- The zero modes number 8Q = 4NQ with N = 2 (the moduli dimension). Each gives one factor L/a (spin part, an index).
- The weight of the sector relative to Q = 0 at scale L is exp(-8 pi^2 Q/g_0^2) (L/a)^(8Q) (L/a)^(-2Q/3) x (finite) = exp(-8 pi^2 Q/g^2(L)) x (finite), with 8 pi^2/g^2(L) = 8 pi^2/g_0^2 - (22/3) log(L/a).

The spin part is a finite count only when the minimum of the sector is self-dual and Q is not zero. For a covariantly constant field that is not self-dual the spin part is an infinite sum over Landau levels, of the same kind as the orbital part. At Q = 0 the minima are flat. Their zero modes (the torons) have index 0 and occur also for U(1). This is Step 3.5 in general form.

### 5.2 The two families of index weights

A weight has an index engine when it is the weight of a topological sector whose minimum is self-dual. On the lattice torus there are two families.

(a) The 't Hooft twist sectors Z^(n). The twist fixes Q modulo 1; the crossed twist (1,1) gives Q in Z + 1/2 and the margin of Step 3.3. Each twist ratio is a signed sum of electric flux traces (Step 3.3, row 859). This is the flux half.

(b) The integer-charge sectors of the periodic torus, Z_Q/Z_0, or the theta function Z(theta)/Z(0) = sum over Q of e^(i theta Q) Z_Q/Z_0. The topological density q(x) is a gauge-invariant local function of the plaquettes near x. A centre transformation of the links that cross a hyperplane leaves every plaquette unchanged, so Q is centre-neutral. So family (b) is a centre-neutral weight with an index engine. On the symmetric torus the first self-dual sector is Q = 2 (Braam and van Baal, 1989: no charge-one instanton on T^4); its moduli have dimension 16 and its weight runs like exp(-16 pi^2/g^2(L)), a factor 2^(44/3) per doubling at one loop. Step 3.5 said "I found no neutral analogue". That is corrected here: (b) is one.

Lattice caveat. For the Wilson action Q is not defined on every configuration. Luscher's geometric charge (1982) is an integer on admissible fields (every plaquette near 1). Exact sectors need an action that excludes the other fields. So (b) is a statement about such an action, or about a non-canonical lattice charge.

### 5.3 Why (b) does not reach (N-phys)

1. One channel. The weights of (b) read the law of Q only, that is, the zero-momentum part of the pseudoscalar density. (N-phys) bounds the trace of all centre-neutral levels.
2. Products bind it. Take SU(2) times a free photon with no topology. Its weights Z_Q/Z_0 are those of the SU(2) factor, and its neutral excited trace is unbounded (row 929, Theorem A1: log(1 + S_ev(a; (24a)^3)) > 31 for the free photon at every a). So no statement about the weights of (b) alone implies (N-phys). This is Lemma PT and Proposition NP of the lane (rows 998, 1003).
3. The exit. A route through (b) still needs, at the end of the flow, a one-scale criterion "dense topology at scale L gives the neutral bound at scale K L". That is a (K-one) statement. It is false for the product of item 2, and it has to separate the Wilson trajectory from K7 if Q is defined there.

### 5.4 What 5.1-5.3 say about the neutral half (ARGUED)

At weak coupling a weight with no index engine changes by a relative amount of order g^2(L) per doubling. Examples: the small-box gap 4.1167 g^(2/3)/L of Luscher and van Baal (row 998 I33), whose relative change per doubling is (2/3) b_0 g^2 log 2 to leading order; the excess free energy, of order log(1/g^2(L)). An index weight changes by a fixed factor per doubling. So:

- An engine for the twist ratio may lose up to a factor 2^(11/3) per doubling and still carry (X) (Step 3.3).
- An engine for any centre-neutral quantity other than the weights of (b) must lose less than c g^2(L) per doubling at every scale from first passage on. This is the rule (RGI) of `gap-skeleton-max.md` L165, now with the reason: the neutral half has no index weight except (b), and (b) is one channel.

So the classification gives two engines with a robust margin. One is the flux half. The other is the theta channel, which products bind. The neutral half has no engine with a margin; a proof must be sharp at order g^2, or must start at the exit of the band. This sharpens Step 3.5. It does not move (N-phys).

## Step 6. The minimum of the crossed-twist action (Lemma M, PROVED by hand; one correction to Step 3.2)

Setting of Step 3.2: torus (Z/L)^4, L >= 1, A(U) = sum over plaquettes of (1 - eps_p x_p), x_p = (1/2) tr U_p, eps_p = -1 on the L^2 plaquettes (x; 1, 2) with x_1 = x_2 = L - 1 and on the L^2 plaquettes (x; 3, 4) with x_3 = x_4 = L - 1, eps_p = +1 elsewhere. A_perp(L) = 2 L^4 (1 - cos(pi/L^2)) is the action of the family of Lemma V.

**Lemma M.** (a) For every L >= 1 the field U_1(x) = i sigma_1 if x_1 = L - 1 and 1 otherwise, U_2(x) = i sigma_2 if x_2 = L - 1 and 1 otherwise, U_3 = U_4 = 1, has A = 2 L^2. For L = 1 and L = 2 this is below A_perp(L) (2 < 4, and 8 < 32 (1 - cos(pi/4)) = 9.37...). So for L <= 2 the family of Lemma V is not the minimum set of sector (1,1).

(b) For every L >= 1 and every field with values in one maximal torus, A >= A_perp(L), with equality on the family of Lemma V.

(c) No field in sector (1,1) has eps_p U_p = 1 on every plaquette outside a set S of plaquettes whose base points miss, in each direction rho, at least one value of the coordinate x_rho. In particular S cannot lie in a box of side L - 1.

Proof. (a) Mixed planes: U_1 depends on x_1 only, U_2 on x_2 only, and U_3 = U_4 = 1, so every plaquette (mu, nu) with mu in {1, 2}, nu in {3, 4} is U_mu(x) U_mu(x + e_nu)^(-1) = 1. Plane (3, 4): every plaquette is 1, so each of the L^2 flipped ones costs 1 - (-1)(1) = 2 and the others cost 0. Plane (1, 2): at x_1 = x_2 = L - 1 the plaquette is (i sigma_1)(i sigma_2)(i sigma_1)^(-1)(i sigma_2)^(-1) = -1, so the flipped weight is 1 - (-1)(-1) = 0. At x_1 = L - 1, x_2 != L - 1 it is (i sigma_1) 1 (i sigma_1)^(-1) 1 = 1; at x_2 = L - 1, x_1 != L - 1 it is 1 (i sigma_2) 1 (i sigma_2)^(-1) = 1; elsewhere 1. Total 2 L^2.

(b) Conjugate the field into exp(i theta sigma_3), theta_mu(x) real. Then x_p = cos theta_p with theta_p the signed sum of the four link angles. Fix a (1, 2)-slice (x_3, x_4 fixed). Each link angle of the slice enters two of its plaquettes with opposite signs, so the L^2 angles theta_p of the slice sum to 0 exactly. Put phi_p = theta_p + pi on the one flipped plaquette of the slice and phi_p = theta_p on the others. Then 1 - eps_p x_p = 1 - cos phi_p on every plaquette of the slice and the phi_p sum to pi. Claim: if m >= 1 reals phi_i sum to pi, then sum (1 - cos phi_i) >= m (1 - cos(pi/m)). Given the claim, each of the L^2 (1, 2)-slices and each of the L^2 (3, 4)-slices contributes at least L^2 (1 - cos(pi/L^2)), the mixed plaquettes contribute at least 0, and the sum is A_perp(L). Lemma V (a) gives equality.

Proof of the claim. Write f(t) = 1 - cos t. Reduce each phi_i modulo 2 pi into (-pi, pi]; f is unchanged and the sum becomes an odd multiple of pi, so the t_i = |phi_i| lie in [0, pi] with sum at least pi. Since f is non-decreasing on [0, pi], lowering some t_i makes the sum exactly pi and does not raise sum f(t_i). With sum t_i = pi at most one t_i exceeds pi/2. If none does, f is convex on [0, pi/2] and Jensen gives sum f(t_i) >= m f(pi/m). If t_1 > pi/2, put r = pi - t_1 < pi/2, so f(t_1) = 1 + cos r and the others sum to r. For m = 1 the claim is f(pi) = 2. For m = 2, f(t) + f(pi - t) = 2 = 2 f(pi/2). For m >= 5, f(t_1) >= 1 > pi^2/(2m) >= m f(pi/m). For m = 3, Jensen on the other two gives at least 1 + cos r + 2 (1 - cos(r/2)) = 2c^2 - 2c + 2 with c = cos(r/2) in (2^(-1/2), 1]; this is increasing in c, so it exceeds 2 (1/2) - 2^(1/2) + 2 = 1.585... > 3/2 = 3 f(pi/3). For m = 4, Jensen on the other three gives at least F(r) = 4 + cos r - 3 cos(r/3); F'(r) = sin(r/3) - sin r < 0 on (0, pi/2), so F(r) > F(pi/2) = 4 - 3 cos(pi/6) = 1.401... > 4 (1 - cos(pi/4)) = 1.171.... QED (claim).

(c) By hypothesis pick, for each rho, a value a_rho that no base point of S has as its rho-coordinate, and put x_0 = (a_1, ..., a_4). A plaquette of the 2-torus T_(mu nu)(x_0) = {x_0 + s e_mu + t e_nu} has a base point whose coordinates in the two directions transverse to (mu, nu) are those of x_0, so it is not in S. So every plaquette p of the six 2-tori through x_0 has U_p = eps_p, a central element. On a 2-torus the ordered product of its plaquettes, each transported to x_0, equals the group commutator of the two holonomies through x_0. Central factors need no transport, so the commutator equals the product of the eps_p over the 2-torus. T_(12)(x_0) and T_(34)(x_0) each contain exactly one flipped plaquette, the four mixed tori contain none. So the holonomies Omega_mu at x_0 satisfy Omega_1 Omega_2 = - Omega_2 Omega_1, Omega_3 Omega_4 = - Omega_4 Omega_3, and Omega_i Omega_j = Omega_j Omega_i for i in {1, 2}, j in {3, 4}. Two anticommuting elements of SU(2) are of the form i n.sigma and i m.sigma with n orthogonal to m, up to sign, and the only elements commuting with both are +1 and -1. So Omega_3 and Omega_4 are +-1 and commute. Contradiction. QED

The commutator step in (c) is the standard lattice form of "the product of the plaquettes of a closed surface is a commutator"; for a 2-torus of L x L plaquettes it is checked by ordering the plaquettes row by row (each interior link cancels against its reverse). I wrote it in words, not in symbols.

**What Lemma M changes in Step 3 (ARGUED).**

1. The semiclassical reading of Step 3.2 needs L >= 3 at least. For L >= 3, whether min A = A_perp(L) over all fields is OPEN; (a) gives 2 L^2 > pi^2 > A_perp(L) there and settles nothing.
2. By (c) a field of sector (1,1) with small action cannot put its defect in a small box: the defect has to meet a 2-torus through every point. So lattice lumps of the kind that spoil the charge-1 sector of the Wilson action (the dislocations) have no localized analogue here. This is a qualitative statement only; (c) bounds the support of the defect, not its action.
3. Threshold. If some field of sector (1,1), not near the family of Lemma V, had A below (12/11) pi^2 = 10.77..., then at the scaling point (L/a)^(11/3) e^(-pi^2 beta) of order 1 its weight would be larger than that of the fractional instanton by e^(beta ((12/11) pi^2 - A)), and the twist ratio R(L) of Step 3.3 would read a lattice artifact, not the running coupling. The arithmetic: lump weight e^(-beta A) (L/a)^4, physical weight e^(-pi^2 beta) (L/a)^(11/3), and (L/a) = e^((3/11) pi^2 beta) there. The same number (12/11) pi^2 is the known dislocation threshold of the charge-1 sector (6/11 of 2 pi^2; Luscher; Pugh and Teper, RECALLED). So any proof of (X) must exclude such fields, and (a) shows they exist at L <= 2.

Consumer: none on the gap path. This step only repairs the reading of Step 3.

## Step 7. Attack on the neutral half: the flow of each neutral level along the trajectory (ARGUED; first failing step named)

Why this attack. After Step 5 the neutral half has no index engine. The one kind of (K-flow) left for it moves each neutral level by a relative amount of order g^2 per doubling at weak coupling. Its exact form is the Feynman-Hellmann identity in the coupling at a fixed lattice, read along the trajectory (in the continuum, the trace anomaly). On file: attack 3 of row 1128 (`gap-council-rg-fable.md` L202-232: (MONO), (VIR), ranked last because "(VIR) only bounds gaps at strong coupling below by gaps at weak coupling, which are small"); Proposition VIR of `gap-afield-a` (a virial identity in log b for D, checked HOLDS in `gap-afield-a-check-opus.md` L141-143). What this step adds is the size of the constant that crossing the band needs.

### 7.1 Identity (PROVED, standard)

For the Hamiltonian form H_beta = (2/beta) K + (beta/2) V on one spatial lattice (row 1128 L205-208), with E_i(beta) a simple level, Feynman-Hellmann gives beta d(E_i - E_0)/d beta = [(beta/2) <V>_i - (2/beta) <K>_i] - [(beta/2) <V>_0 - (2/beta) <K>_0]. Put kappa_i(beta; n) = - beta d log(E_i - E_0)/d beta. Then for beta_1 < beta_2,

  (E_i - E_0)(beta_1) = (E_i - E_0)(beta_2) exp( integral from beta_1 to beta_2 of kappa_i d beta/beta ).

### 7.2 The value of kappa in three regimes (RECALLED or from files; GUIDE)

- Small periodic box (Luscher; van Baal; row 998 I33): E_1 - E_0 is proportional to g^(2/3)/n, so kappa_1 tends to 1/3.
- Small twisted box: E_1 tends to the free value 4 arsinh sin(pi/(2n)) (row 1215, unchecked), which does not depend on beta, so kappa_1 tends to 0 as beta grows at fixed n.
- A level of mass m in a box much larger than 1/m, in the scaling regime: E_1 - E_0 = m a(beta), so kappa_1 = beta |d log a/d beta| = (3 pi^2/11) beta (1 + O(1/beta)) for SU(2) with the Wilson action (one loop: a Lambda proportional to exp(- beta/(8 b_0)), b_0 = 11/(24 pi^2)). At beta = 2.5 this is about 6.7.

### 7.3 What crossing the band needs (ARGUED)

(N-phys) forces n m_ev >= K log 2, about 355 for K = 512 (Lemma N2 (a) of row 1184). At the small-box end of the flow n m_ev is at most about 2 pi (twisted box; the free massless value of row 1184's reading) or 4.12 g^(2/3) (periodic box). So the flow at fixed n must multiply n m_ev by at least 355/(2 pi), about 56. Let the box grow by a factor 100 in physical units between the two ends. At fixed n the bare coupling then changes by (11/(3 pi^2)) log 100, about 1.71, so beta_entry/beta_exit is about 1.74 for beta_exit = 2.3. By 7.1 the mean of kappa_1 against d beta/beta on that range must be at least log 56/log 1.74, about 7.3.

That is the value of a massive level in a large box (7.2, third case), not the small-box values 1/3 and 0. A uniform (VIR) with kappa = 1/3 gives the factor 1.74^(1/3), about 1.2.

**First failing step.** A lower bound on kappa_1(beta; n) of about 7 (in the mean against d beta/beta) on the band, at fixed large n. By 7.2 it holds when level 1 is massive on the scale of the box. So the bound restates the gap; I found no other way to supply it.

Two side facts (ARGUED). (i) (VIR) for every box and every beta >= beta_0 with one kappa > 0 is false at weak coupling in the twisted box, where kappa_1 tends to 0 (7.2, second case); so the council's restriction to the band is needed. (ii) The controls behave as the council's file says: kappa = 0 for the free photon and on the levels of a massless factor, kappa tends to 0 at the critical point K7, and for frozen groups the vortex levels have E proportional to beta (kappa = -1) while their gap is true. So (VIR) is selective, but it is not necessary for a gap.

### 7.4 Check of Step 3's Lemma V (Claude Opus 5.5, line by line; a model other than its author)

(a) The (1, 2)-plaquette angle is phi for x_2 < L - 1 (the a_2 terms vanish, a_1 changes by phi), phi for x_2 = L - 1 and x_1 < L - 1 (- phi (L - 1) + phi L (x_1 + 1) - phi L x_1), and phi - pi at x_1 = x_2 = L - 1 (- phi (L - 1) - phi L (L - 1) = phi - phi L^2), whose flipped weight is 1 + cos(phi - pi) = 1 - cos phi. The (3, 4) case is the same. Mixed angles vanish because a_1 depends on x_2 only, a_2 on x_1, x_2, a_3 on x_4, a_4 on x_3, x_4. The bounds follow from 2u^2/pi^2 <= 1 - cos u <= u^2/2 on [0, pi]. (b) The Polyakov line of direction 1 at height x_2 is the product of L factors exp(a (c_1 - phi x_2)), with trace 2 cos(L c_1 - pi x_2/L). (c) is (a) with one plane. Verdict: HOLDS. Lemma M (a) above corrects only the Reading under it (the minimum set at L <= 2), not Lemma V.

### 7.5 What Steps 5-7 say together (ARGUED)

Any proof of (N-phys) contains one of two inputs.

1. A one-scale input at order-one coupling that separates the Wilson trajectory from K7. This is (K-one) at the exit of the band (row 998 6b; `parts/gap.md` L41-50).
2. A neutral level flow whose rate on the band has the size that a massive level has (7.3). This restates the gap.

The index engines of Step 5 do not supply either. They carry the twist ratio (the flux half) and the theta channel (one neutral channel, bound by products). So the reason a (K-flow) for the neutral half has no margin is now explicit: the asymptotic-freedom sign is a zero-mode count only on self-dual sector weights, and every other neutral quantity is slaved to the running coupling at order g^2 per doubling.
