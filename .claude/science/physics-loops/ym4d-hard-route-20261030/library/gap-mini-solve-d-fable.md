lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T11:54Z

# gap-mini-solve-d-fable: the mass gap of four-dimensional SU(2) Yang-Mills (plain brief, fourth sibling)

Queue row 1193 of `FINISH.md`, pinned at commit 32c14c113. Worker: Claude Fable 5.2 (max), Mac mini worker 1.
Started 2026-11-19T23:54Z (`date -u`). This is research-stage working state. Nothing here is a public claim.

Labels used: PROVED (every step written here), ARGUED (argument written, a step is not fully written),
GUIDE (numeric or heuristic evidence, never a proof step), OPEN.

## Status log

- 23:54Z. File created. Read `GOAL.md`, the rule sections of `FINISH.md`, the row. Next: the sibling rows a, b, c
  (rows 1188-1190) and `parts/gap.md`, so that this row does not repeat them.
- 23:55Z. Read in full the three sibling files (rows 1188-1190: `gap-mini-solve-a-fable.md`, `-b-`, `-c-`). Their attacks: (a) pinned-slice
  Ward route, Lemma PC; (b) the doubly flat corner (route S2), Theorem A8, stops at (Sigma-unif) and at the first unfreezing;
  (c) seventeen candidates all on file, cube identity, chi-square restatement. I do not repeat these. Next: `parts/gap.md`.
- 00:25Z. Read `parts/gap.md` L1-104 and L223-322, the RESULT lines of rows 1178-1187, the digest of the two posted 2D O(N)
  proofs (`library/prior/gap-2don-proofs-read-opus.md` L44-126), statement (A) (`gap-council-op-astra.md` L14-52), the
  corner-twist candidates C1-C8 and their kill table (`gap-invent-selective-max.md` L96-200) with the cross-provider check
  items 11-18 (`gap-invent-selective-check-astra.md` L50-72). Section 1 written.
- 00:33Z. Read the lane's digest of OpenAI's pinned-cell proof for the step from the twist bound to all observables
  (`library/prior/gap-o4-pinned-cell-read-opus.md` L57-80, L181-223), Lemma WN and its corollaries
  (`gap-invent-selective-max.md` L136-168), Theorem D (f) (`gap-crux-restate.md` L99), the RESULT of row 1084. Section 2
  written. The gauge form of every step is on file with a first failing step. Next: Section 3, the one count that
  the record still holds as ARGUED and open (the corner form C1).
- 00:37Z. Section 3 written: Lemma PC-c (corner power count), proved by hand, with a hand check in d = 2. The numeric
  sanity script is ready in a scratch folder under /tmp; memory free was 47, 47, 48, 45 percent at four readings
  between 00:31Z and 00:37Z, below the 50 percent rule, so it has not run yet.
- 00:45Z. Sections 3.5-3.6 and Section 4 written (Remark 3.5, Corollary PC-c2). Every PROVED item re-read once; six
  wording corrections (three classification claims softened, the setting of 3.6 restricted to the torus, two anchors).
  The numeric sanity run still waits for memory.
- 00:48Z. Repo search for the one new statement done (Section 0).
- 00:53Z. The numeric sanity run ran at 00:51:54Z, when memory first read 50 percent free (3.7): no violation. Section 0
  corrected after a second grep (rows 1016, 1031, 1056, 1068, 846 also name the corner terms; none holds the count).
  Finished.
- 00:54Z. A last grep, file by file, found the d = 4 spectrum of the corner Laplacian in the check of row 1013 by Opus
  (row 1015, `gap-invent-selective-check.md` L157-161). Credited in Section 0, in step 1 of the proof, in Section 4 and
  in the RESULT line. The count (PCc2) and Corollary PC-c2 are not in that file.

## 0. Repo search (for Lemma PC-c and Corollary PC-c2, the only statements this row calls new)

- This folder: `grep` for "corner graph", "link-end", "K_(2,2,2,2)", "corner twist", "family inequality" in
  `library/gap-*.md`, `library/prior/`, `parts/gap.md`, `library/open-core.md` and the `FINISH.md` rows. Hits, all read at
  the lines that hold the terms: row 1013 (`gap-invent-selective-max.md`: the corner graph, Lemma WN, C1) with its
  checks (`gap-invent-selective-check-astra.md` item 13; `gap-invent-selective-check.md` L157-161, row 1015, which holds
  the Laplacian spectrum 0, 6 (four times), 8 (three times) of K_(2,2,2,2), so step 1 of Lemma PC-c is on file for
  d = 4); row 1016
  (`gap-global-reform-max.md` L539-545: for conjugation fields, equal at the two ends of a link, the cost form is a
  Dirichlet form on the lattice of links, not scale invariant in d = 4) with its checks (row 1020 and the astra
  check); row 1051 with its two checks (`gap-direction3-max.md` L265, L456: a count on pin space, not on corners;
  `gap-direction3-check-astra.md` L433: "C1 in corner form ... retain their prior open standing"; row 1056); row 1068
  (`gap-ir-first-astra.md` L544, Lemma WN restated); rows 846 and 1031 (the graph K_(2,2,2,2) in another role);
  `parts/gap.md`. `library/open-core.md` has no hit. No file holds the corner count or a corner form of the family
  inequality.
- Other branches: a bare blob-less fetch of `main` and of PR #10114 into a scratch folder under /tmp, then `git grep`
  for the same terms on the 72 ym4d and mass-gap `.md` files of `main` and on the 5 files `MASS_GAP*.md`, `RTARGET.md`,
  `PROOF.md` of the `ym4d-proof` folder of PR #10114. No hit. The other PR branches were not searched.

## 1. How best to attack it

### 1.1 The target as the record holds it (cited, not re-proved)

- The Jaffe-Witten gap clause is reduced to the continuum datum of the T0 chain (OPEN, `FINISH.md` L11) plus one lattice
  estimate, the one-cube physical neutral bound (N-phys) (row 1161, `gap-solve9-astra62.md` L146-148; consumer Theorem BP
  of row 1179; checks 1162, 1183). (N-phys) is a lattice gap for centre-neutral states at arbitrarily weak coupling with
  a rate of asymptotic-scaling type (rows 1180, 1184; check 1187).
- In one sentence (`parts/gap.md` L32-34, L311-322): one selective inequality is missing at every scale between first
  passage and the seed size; selective means false for a massless factor.
- The three sibling rows (1188, 1189, 1190; files as of this pin, rows 1189 and 1190 had no RESULT line yet) found this
  map again. Their own attacks: the pinned-slice Ward route (dead
  in d = 4 by Lemma PC of row 1188), the doubly flat corner (stops at (Sigma-unif) and does not descend, row 1189), a
  candidate screening (row 1190). I do not repeat them.

### 1.2 My screening (GUIDE; every line was checked against the record by grep before any work)

I asked from scratch what a proof needs, and searched `library/gap-*.md`, `library/prior/` and `parts/gap.md` for each
tool. Each has a match; the number is the count of lane files that name it.

| Candidate from first principles | Where it stops | On file |
|---|---|---|
| Zero-point closing of flat valleys (Simon's x^2 y^2, Luscher's toron Hamiltonian) as a volume-uniform operator inequality | it bounds H below, not E_1 - E_0; in a background field the spin term reverses the sign (the paramagnetic term that gives asymptotic freedom) | toron 40, quartic 29, `gap-skeleton-max.md` L76, `gap-paths-fable.md` L105 |
| Orbit-space geometry (Feynman, Singer, Karabali-Kim-Nair) | no consumer above beta about 1/8 | method 31; `gap-measured-vectors-max.md` L219 |
| Thin twisted torus, semiclassical gap, then continuity in the torus size | (AC') is the crux again | Route T, rows 678-695, 842 |
| The neutral premise as "no Casimir energy at aspect ratio K" (thermal form) | Proposition Delta: log(1 + s(a; n^3)) <= (n/a)^3 Delta(a^4); the seed again | `gap-ladder-max.md` L197; Casimir 115 |
| Concavity of a stiffness or of Delta in the logarithm of the size, as a carrier of asymptotic freedom | Delta >= 0 forces a change of convexity before the seed; no exact convexity known | (CVX), (CAS), (MONO-Delta); `parts/gap.md` L76-78 |
| Triangular (field-dependent, Haar-preserving) moves; frames read from the field | frames decohere; pointwise frustration by non-commuting plaquettes | C8 of row 1013; rows 1141, 1177, 1181 |
| Staple rotations (exact field-dependent symmetries special to SU(2)) | they preserve the action, so their Ward identities carry no coupling: void | Lemma MC, row 1016 |
| Loop equations with positivity | numerical; Theorem O | rows 754-767 |
| A corner-twist background with an exact non-abelian link-field invariance (my derivation of W(G^F) = W(G)) | found again: it is C1 of row 1013 | `gap-invent-selective-max.md` L101 |
| Commutator extraction (A) | a Doeblin factorization in Moser coordinates; no mechanism | rows 1132-1138 |

Verdict (GUIDE): a fourth screening finds no route off the map. I stop screening here.

### 1.3 What I take to be the exact obstruction (ARGUED; my wording of statements that are on file)

1. Power counting. A p-form transformation has a scale-invariant quadratic cost in dimension 2p + 2. Gauge functions
   (p = 0) are marginal on two-dimensional objects only: the 2D spin models, a 2D pinned plane (Lemma EMB of row 1011),
   the base of the corner model (row 1189). One-forms (p = 1) are marginal in d = 4, and the exact one-form
   symmetry of Wilson SU(2) on file is the centre, which is discrete (I claim no classification).
2. Every continuous move of the links has a pointwise mean cost that is a mass form, because no colour direction is
   covariantly constant on a field whose plaquettes do not commute (Proposition J and Lemma 5.1a of row 1181, Lemma FR
   of row 1011, row 1141 (2)). The physical stiffness is the difference of two such terms. A bound that drops the
   variance cannot see it.
3. Transitivity. In an O(N) spin model every boundary condition is a site-dependent symmetry twist of every other one.
   So a twist-stiffness bound controls every observable, the rotation-invariant ones included. In a gauge theory the
   boundary data modulo the gauge group is the gauge orbit of the boundary field, and no exact symmetry on file moves
   it (rows 1013, 1016: Lemma CEN+, Lemma MC; I claim no classification).
   Every Haar-preserving change of variables gives a Schwinger-Dyson identity: the function exp(S o tau - S) - 1 has
   conditional mean zero given the links that tau does not move. Such identities exist in abundance and say nothing
   about the conditional law given gauge-invariant boundary data. This is the "neutral half".

Item 3 decides my choice. (N-phys) is a statement about the neutral half. The 2D proofs cross their band and, per the
record, also deliver mixing for all observables and a doubling criterion for partition functions. So the step to read
is not their twist bound (ported four times, each port dead) but **how they pass from the twist bound to the
rotation-invariant observables**. Section 2 reads that step in the lane's digest and asks for its gauge analogue.

## 2. The step that reaches rotation-invariant observables in two dimensions, and its gauge form

Reading only. Every statement about the 2D proof is OpenAI's, taken from the lane's digest of row 1009
(`library/prior/gap-o4-pinned-cell-read-opus.md`); I did not read the paper and I check none of its proofs.

### 2.1 The 2D chain after the twist bound

- (i) Small stiffness on a pinned square. This part "allows arbitrary signed couplings and fixed right twists"
  (digest L78-79, quoting p. 13). The gain is the bracket term.
- (ii) Small stiffness, then coarse orientations, then a disagreement coupling, then decay of charged observables
  (digest L72, L78-80).
- (iii) The decomposition q = (cos(alpha) z, sin(alpha) w) with z, w on the circle. Given alpha, the two circle sectors
  are independent XY models with couplings b_e cos(alpha_x) cos(alpha_y) and b_e sin(alpha_x) sin(alpha_y), and the law of
  alpha is associated. With charged decay this gives (3.67): covariance decay for all local Lipschitz observables,
  uniform on unpinned tori and free subgraphs, for every set of couplings 0 <= b_e <= b (digest L183-186). "Only this
  last part requires nonnegative untwisted couplings" (digest L80).
- (iv) (3.69): the mean bond energies of the tori n and 2n are compared by cutting the bonds of a free square; no pins
  occur. (3.70): d/dt Delta_t(n) = 8 n^2 [e_t(n) - e_t(2n)] and Delta_0(n) = 0; integrate over t in [0, b]. The mixing
  length must be the same for every t <= b (digest L187-197).

So the twist bound gives the charged half only. The rotation-invariant half comes from positivity: the model is a
mixture of abelian ferromagnets with an associated mixing law. OpenAI's first O(n) paper says the same from the other
side: "A full transfer gap would additionally control covariances of all local observables, including
rotation-invariant bond energies, and requires a separate argument" (`library/prior/gap-2don-proofs-read-opus.md`
L124, B(1)).

### 2.2 The gauge form of each step, and where the record holds it

| 2D step | Gauge form | State on file |
|---|---|---|
| (iv) torus comparison and coupling integral | Phi(n; beta) = 96 n^4 times the integral over s in [0, beta] of (abar_2n(s) - abar_n(s)) | PROVED: Theorem D (f), `gap-crux-restate.md` L99; "(SEED) is a bound on the finite-size shift of one number", L61. The consumer exists. |
| (iii) abelian conditional ferromagnets, association | a conditional abelian structure of the links with positive couplings, or association of plaquette functions | FAILS three ways: row 1084, `gap-checkerboard-singlet-astra.md` L763 (P4-SING-PORT; check row 1086). The Hopf form of one plaquette has a sign pattern that no shift removes: Lemma HF of row 1188, 2.1 of row 1190. Griffiths II for plaquettes is false, also in the even state: Theorem EP-NO, row 754 (`gap-loop-eq-opus.md` L251), check 756. |
| (ii) charged decay from small stiffness | the only charged objects of a gauge theory are centre-charged (flux); everything else charged has mean zero | flux half only: `gap-council-synthesis.md` L54 (2c); rows 731, 1018 |
| (i) small stiffness from the bracket | four ports | class of all pins: FAILS, rows 1011, 1016 (Propositions B, B', Theorem BH). Pinned slice: Lemma PC of row 1188. Corner model: row 1189. Corner graph: C1 of row 1013, verdict ARGUED and reopened by the checks of rows 1013 and 1051; Section 3 below. |

### 2.3 Reading (ARGUED)

(N-phys) is a statement about the rotation-invariant half. In two dimensions that half is not reached by a twist. It
is reached by step (iii), and the gauge form of step (iii) fails at its first line, for the exact reason that
distinguishes the plaquette from the bond: the trace of a product of four elements has terms of both signs in every
abelian coordinate system tried, and non-orientable surfaces carry the sign of the half-integer representations. A
proof of (N-phys) with this architecture needs a positivity structure of Wilson SU(2) that I do not have and that the
record does not have. The supplier for step (iv) is therefore open, with no mechanism:

**(FS) (OPEN; the crux in the form of Theorem D (f)).** There is one n with
96 n^4 times the integral over s in [0, beta] of (abar_2n(s) - abar_n(s)) at most 1.9e-4.

I state it only to fix what Section 4 reports as open. It is (SEED) of row 697.

## 3. The corner form of the family inequality: the power count as a proved inequality

Why this item. The one mechanism known to cross a band is the family inequality of the 2D proof (its Proposition 2.2,
as restated in `library/prior/gap-2don-proofs-read-opus.md` L132, B(2) item 4: the stiffness on Q = sum_i S(f_i, f_i-bar) is at
most K ||T||_HS^2 plus a second term, T the Gram matrix of the gradients). Its ports to pins, to a pinned slice and to
the corner model are settled. Its port to link-end translations, C1 of row 1013 (`gap-invent-selective-max.md` L101),
has the verdict "the family inequality is a one-site statement" as ARGUED (L191), and two cross-provider checks keep
it open because the count was never written (`gap-invent-selective-check-astra.md` item 13;
`gap-direction3-check-astra.md` L433). I write the count. It is the corner analogue of Lemma PC of row 1188. Credit:
the corner graph and Lemma WN are row 1013's (Claude Fable 5.2 max); the family inequality is OpenAI's.

### 3.1 Setting (row 1013, Lemma WN; restated)

Lattice Z^d or a torus with all sides at least 3, d >= 2. A **link-end** is a pair (l, x) with x an end of the link l;
a site has 2d link-ends, two on each axis. Each plaquette p, with its fixed orientation, and each site x of p give a
**corner**: p arrives at x along one link and leaves along another. I write the corner as a -> b, with a the link-end
of arrival and b the link-end of departure. The two link-ends of a corner lie on different axes. Conversely two
link-ends at x on different axes lie on exactly one plaquette. So the corners at x are the edges of the complete
multipartite graph K_(d x 2) on the 2d link-ends (d parts of size 2), each edge with one orientation; a site has
2 d (d - 1) corners (24 for d = 4, the graph K_(2,2,2,2) of row 1013).

For a real or complex link-end field f put (delta f)(a -> b) = f(b) - f(a). For corner fields,
<theta, theta'> = sum over corners of theta theta'-bar and |theta|^2 = <theta, theta>. A real corner field theta is
**co-closed** if <theta, delta phi> = 0 for every real link-end field phi. Every real corner field is uniquely
theta = theta_perp + delta psi with theta_perp co-closed. For a complex link-end field f put

  S(f)(a -> b) = (1/2) Im( f(a) f(b)-bar ).

This is the one-axis part of the pure-gauge corner field at second order: for F = u a' + v b' with [a', b'] = c and
f = u + i v, e^(-F(a)) e^(F(b)) = exp( (delta F) - (1/2)[F(a), F(b)] + O(F^3) ) and -(1/2)[F(a), F(b)] =
S(f)(a -> b) c. (C1 (c) writes it as (1/2)[F_(l,x), F_(l',x)]. A change of the sign convention, or of f to f-bar,
changes nothing below.)

### 3.2 Lemma PC-c (PROVED by hand; checked by no one)

Let theta be a real co-closed corner field, lambda real, phi a real link-end field, and (f_i) a finite family of
complex link-end fields with

  sum_i S(f_i) = lambda theta + delta phi on every corner.   (PCc1)

Let T_ij = <delta f_i, delta f_j> and ||T||_HS^2 = sum_(i,j) |T_ij|^2. Then

  ||T||_HS^2 >= 8 (2d - 2)^2 lambda^2 |theta|^2,  which is 288 lambda^2 |theta|^2 for d = 4.   (PCc2)

If theta is not co-closed, (PCc1) holds with theta_perp in place of theta (move delta psi into delta phi), so (PCc2)
holds with |theta_perp|^2.

Proof. Work on the space V of complex link-end fields with (f, g) = sum_a f(a) g(a)-bar.

1. The Laplacian. (f, Lap g) = <delta f, delta g> defines Lap, and (Lap g)(a) = sum over the corner-neighbours b of a of
   (g(a) - g(b)). Lap is a direct sum over sites of the Laplacian of K_(d x 2). On one site, with J the all-ones matrix
   and M the matching that exchanges the two link-ends of each axis, the adjacency matrix is J - 1 - M and the degree is
   2d - 2, so Lap = (2d - 1) + M - J. Constants: eigenvalue 0. Fields with M v = -v (then J v = 0): eigenvalue 2d - 2,
   multiplicity d. Fields with M v = v and J v = 0: eigenvalue 2d, multiplicity d - 1. That is all 2d dimensions. Let P
   be the projection on the fields with sum zero at every site. On the range of P, Lap >= 2d - 2. (For d = 4 this
   spectrum, 0, 6 four times, 8 three times, is in the check of row 1013 by Claude Opus 5.5, row 1015,
   `gap-invent-selective-check.md` L157-161. The step here is the same computation for every d.)
2. The pairing. Let rho = sum_i f_i f_i^*, a non-negative matrix with entries rho_ab = sum_i f_i(a) f_i(b)-bar. Define
   the matrix H by H_ba = theta(a -> b)/(2i) and H_ab = -theta(a -> b)/(2i) for each corner a -> b, and 0 otherwise. H is
   Hermitian. tr(rho H) = sum over corners of (theta/(2i)) (rho_ab - rho_ba) = sum over corners of theta Im(rho_ab) =
   2 <theta, sum_i S(f_i)> = 2 lambda |theta|^2. The last step uses (PCc1) and that theta is co-closed.
3. H kills the site constants. For the indicator 1_x of the link-ends at x, (H 1_x)(b) = (1/(2i)) [ sum over corners
   a -> b of theta - sum over corners b -> a of theta ] = (1/(2i)) (delta^* theta)(b) = 0, since <theta, delta phi> =
   sum_b phi(b) (delta^* theta)(b) for all phi. H is Hermitian and couples link-ends of one site only, so H = P H P.
4. Cauchy-Schwarz. Write Lap^(-1/2) for the inverse square root on the range of P. Then tr(rho H) = tr(P rho P H) =
   tr( Lap^(1/2) rho Lap^(1/2) . Lap^(-1/2) H Lap^(-1/2) ), so
   |tr(rho H)|^2 <= || Lap^(1/2) rho Lap^(1/2) ||_HS^2 || Lap^(-1/2) H Lap^(-1/2) ||_HS^2.
   The first factor is tr(rho Lap rho Lap) = sum_(i,j) |(f_i, Lap f_j)|^2 = ||T||_HS^2. The second is at most
   (2d - 2)^(-2) tr(H^2), by step 1, and tr(H^2) = sum_(a,b) |H_ab|^2 = (1/2) |theta|^2.
5. So 4 lambda^2 |theta|^4 <= ||T||_HS^2 |theta|^2 / (2 (2d - 2)^2). If theta = 0 there is nothing to prove. QED

### 3.3 What it settles, and what it does not

- **The count C1 (d) asked for.** For every family, (signal)^2 / (cost) = lambda^2 |theta|^4 / ||T||_HS^2 is at most
  |theta|^2 / (8 (2d - 2)^2). There is no sum over modes and no dependence on the size of the support, in any
  dimension. So an inequality of OpenAI's form R(lambda theta, lambda theta) <= K ||T||_HS^2 (plus non-negative terms),
  used with any family that satisfies (PCc1), returns at best R(theta, theta) <= 8 (2d - 2)^2 K |theta_perp|^2. This is
  a multiple of the corner-square norm, the form of the exact second-order response at zero twist (Corollary WN2 of
  row 1013: -W''(0) = beta rho(beta) |theta|^2 for corners at distinct free sites).
- **Normalization, and the size of K.** The 2D proposition is written with Q = sum_i S(f_i, f_i-bar) and
  S(f, f-bar)_e = i Im(f_x f_y-bar), so its lambda is twice mine and 8 (2d - 2)^2 becomes 2 (2d - 2)^2, that is 72 for
  d = 4. Its constant is K_rot(beta) = 6 beta^2 + 4 beta^(3/2) + beta, and its second term is non-negative (digest of
  row 1007, `library/prior/gap-2don-proofs-read-opus.md` L132). So if the corner form holds with the same constant, it
  returns at best 72 K_rot(beta) |theta|^2 for a co-closed theta. The exact value at zero twist is at most
  beta xbar |theta|^2 (Remark 3.5: the subtracted term is the mean of a square). Since 72 K_rot(beta) > beta for every
  beta > 0, the corner form with that constant is weaker than the trivial bound at every coupling. Corollary PC-c2
  (3.6) shows that a corner form does hold, with the smaller constant beta/18, and that it returns the bound with
  no bracket.
- **The sheet of C2.** Let theta = t on one corner at each of A distinct sites and 0 elsewhere. The exact part of one
  edge indicator of K_(d x 2) has squared norm equal to the effective resistance of the edge, which is
  1/(2d - 2) + 1/(2d) = (2d - 1)/(2 d (d - 1)), that is 7/24 for d = 4 (split e_a - e_b into its part with M v = -v and
  its part with M v = v; each has squared norm 1). So |theta_perp|^2 = (17/24) t^2 A and the family inequality
  returns at best 204 K t^2 A for d = 4 (51 K_rot t^2 A in the normalization of the 2D proposition): the order of
  the area, at every t. It cannot give the bound
  Z'' >= -delta_A Z with delta_A = o(A) that the integration along the non-central path needs.
- **Scope.** This is PROVED for inequalities whose cost side is K ||T||_HS^2 with T the corner Gram matrix, plus
  non-negative terms. A corner form of the inequality is proved in 3.6, as a corollary of the bound with no
  bracket. Whether the proof of Proposition 2.2 itself ports to corners is not examined (ARGUED in row 1013); by
  3.6 nothing depends on it. The lemma does not exclude a fourth-order identity of another form (item 13 of the
  check of row 1013 stands for those). It concerns the flux half only: the corner twists of C1 and C2 aim at the
  centre twist, and (N-phys) is not a twist response. The constant in (PCc2) depends on the normalization of S;
  the form of (PCc2) does not. At a site of a free boundary the corner graph is smaller and the constant changes.
  The lemma holds for every family in the full space of link-end fields, so also for families in a subspace, such
  as the conjugation fields of row 1016 (`gap-global-reform-max.md` L539-545), whose own cost form couples the sites.
- **Verdict on C1 as a band crossing.** FAILS in the form in which it was proposed, by Lemma PC-c: the cost form has
  a spectral gap 2d - 2 above the gauge directions, so every family pays for its bracket at the site where it makes it.
  In the spin model the same graph is the lattice and the gap is 0; that is where the logarithm comes from.

### 3.4 Hand check in d = 2 (not a proof step)

For d = 2 a site has four link-ends, a_1, a_2, a_1', a_2' (a_k' opposite to a_k), and four corners. Take them oriented
around the 4-cycle: a_1 -> a_2 -> a_1' -> a_2' -> a_1. The Laplacian of the 4-cycle has eigenvalues 0, 2, 2, 4, as step
1 says (2d - 2 = 2 twice, 2d = 4 once). The co-closed fields are the multiples of theta = 1 on the four corners, and
|theta|^2 = 4. Take one field, f = (1, i, -1, -i) on (a_1, a_2, a_1', a_2'). Then S(f) = (1/2) Im(f(a) f(b)-bar) = -1/2 on
each corner, so (PCc1) holds with lambda = -1/2 and phi = 0. The cost is T = sum over corners of |f(b) - f(a)|^2 =
4 x 2 = 8, so ||T||_HS^2 = 64. The bound (PCc2) is 8 x 4 x (1/4) x 4 = 32. So the lemma holds here with a factor 2 to
spare. The factor is the one that row 1188 found for Lemma PC: H has the eigenvalues 0, 1, 0, -1 on this cycle and
rho >= 0 can use only one sign, which Cauchy-Schwarz does not see.

A second hand check, in d = 4. Take three link-ends a_1, a_2, a_3 of one site on three different axes and let theta
be the circulation of the triangle a_1 -> a_2 -> a_3 -> a_1: theta = 1 on these three corners (-1 on a corner whose
orientation is the opposite one) and 0 on the other 21. It is co-closed and |theta|^2 = 3. Take f = (1, w, w^2) on
(a_1, a_2, a_3) with w = e^(2 pi i/3), and f = 0 on the other five link-ends. On each corner of the triangle
S(f) = (1/2) Im(w^(-1)) = -sqrt(3)/4, and S(f) = 0 on every other corner, so lambda = -sqrt(3)/4 and phi = 0. The cost:
three corners with |w - 1|^2 = 3, and for each a_k its four other corners with |f|^2 = 1, so T = 9 + 12 = 21 and
||T||_HS^2 = 441. The bound (PCc2) is 288 x (3/16) x 3 = 162.

### 3.5 Remark: the exact response at zero twist is a site-local form (PROVED; a small extension of Corollary WN2)

Corollary WN2 of row 1013 takes corners at pairwise distinct sites. The same proof gives the general case. Let all
sites be free, the strength beta constant, theta any real corner field, W(t) = E exp(beta sum_p [x_p(t theta) - x_p])
in the notation of Lemma WN (c = i sigma_3, U = x + i y.sigma, U_(p,x) the holonomy of p based at x). Then W'(0) = 0 and

  -W''(0) = sum over sites x of [ beta xbar |theta_x|^2 - (beta^2/3) sum over corners (p, x), (p', x) of theta_(p,x) theta_(p',x) E( y(U_(p,x)) . y(U_(p',x)) ) ],

with theta_x the restriction of theta to the 2 d (d - 1) corners at x and xbar = E x_p.
Proof. W''(0) = E[D] + E[X^2] with D the second derivative of sum_p beta x_p(t theta) and X = -beta sum over corners of
theta_(p,x) y_3(U_(p,x)). By Lemma WN (i) and the argument of its part (iii), E[D] = -beta xbar |theta|^2: the formula of
(i) holds for every corner field, and each cross term of D joins two corners of one plaquette at two different free
sites. In E[X^2] two corners at different sites give 0, by the independent gauge averages at the two sites. Two
corners at the same site belong to two plaquettes through that site, and the gauge average at the site rotates both
vectors together, so E[y_3 y_3'] = (1/3) E[y . y']. QED

By Lemma WN (iii) the form vanishes on exact fields. So at zero twist nothing is left to bound: the response is a
sum over sites of one quadratic form on the 17-dimensional space of co-closed corner fields of a site (d = 4), with
coefficients xbar and the local numbers E(y . y') of pairs of plaquettes through one site. The long-distance content
of the corner formalism is only in the response at non-zero twist, where the gauge average at a twisted site is
broken to the rotations about c, so corners at different sites are no longer uncorrelated by symmetry. Lemma PC-c
says that the family inequality does not see that content either: its cost side is site-local in every measure.

### 3.6 Corollary PC-c2: the corner form of the family inequality is true, and it is the trivial bound (PROVED)

Setting: the torus of Lemma PC-c (all sides at least 3, every plaquette counted), any set of pinned links, strengths
0 <= beta_p <= beta (a deleted plaquette has strength 0), the notation of Lemma WN with c = i sigma_3, and
x_p(theta) = (1/2) tr(prod_(i=1..4) e^(theta_i c) V_i) the trace of p with the corner twist theta. For real corner
fields theta', theta put Z(theta) = integral over the free links of exp(sum_p beta_p x_p(theta)) and

  R_(theta')(theta, theta) = -(d^2/dt^2) log Z(theta' + t theta) at t = 0,

the response to theta in the measure twisted by theta'.

(a) R_(theta')(theta, theta) <= 4 beta |theta|^2, for all theta', all pins, all strengths up to beta.
(b) Let theta be co-closed and let (f_i) be complex link-end fields with sum_i Im( f_i(a) f_i(b)-bar ) = lambda theta +
delta phi on every corner a -> b. Then lambda^2 R_(theta')(theta, theta) <= (2 beta/(2d - 2)^2) ||T||_HS^2, which is
(beta/18) ||T||_HS^2 for d = 4.

Proof. (a) -(d^2/dt^2) log Z = -E[D] - Var(X) <= -E[D], with E the twisted measure, X and D the first and second
t-derivatives of sum_p beta_p x_p(theta' + t theta). The second derivative of x_p is a sum over pairs (i, j) of corners
of p of theta_i theta_j times (1/2) tr of a product of elements of SU(2) (the factors V, the twists, and two factors
c). Each such trace is at most 1 in absolute value. So |D| <= sum_p beta_p (sum_i |theta_i|)^2 <= 4 beta |theta|^2.
(b) Lemma PC-c with lambda/2 and phi/2 (its S carries the factor 1/2) gives ||T||_HS^2 >= 2 (2d - 2)^2 lambda^2
|theta|^2. Combine with (a). QED

Reading. With a' = i sigma_1, b' = i sigma_2, [a', b'] = -2c, the pure-gauge corner field of F = u a' + v b' is
e^(-F(a)) e^(F(b)) = exp(delta F - Im(f(a) f(b)-bar) c + O(F^3)), f = u + i v. So the hypothesis of (b) is the bracket
hypothesis of the family inequality in the units of Lemma WN, and (b) is an inequality of exactly the family form,
in every twisted measure of the class, with the constant 2 beta/(2d - 2)^2. This constant is linear in beta, below
the K_rot of the 2D proposition. So the port C1 asked for exists and holds, and it is a corollary of the bound with
no bracket: the family form adds nothing on the corner graph. For the sheet of C2 it gives
R_(theta')(theta, theta) <= 4 beta t^2 A, the area order, and Lemma PC-c shows that no family improves on that order
through this form. This closes C1 in the form in which row 1013 proposed it. It does not close "every fourth-order
identity" (item 13 of the check of row 1013).

### 3.7 Numeric sanity run (GUIDE; not a proof step)

Run once, 2026-11-20T00:51:54Z to 00:51:57Z (`date -u` in the log), under the numeric lock (holder
`solve-d-fable-1193`, status "acquired" confirmed in the log, released after the run), plain numpy, one thread. Memory
free read 35 to 49 percent from 00:31Z to 00:51Z, so the job waited; it started at the first reading of 50 percent.
Script and log are in a scratch folder under /tmp (`solve-d-fable-1193/check_pcc.py`, `check_pcc.log`). The corner
orientations are drawn at random; the lemma holds for every orientation. A run can only refute a formula. A search
that finds no violation proves nothing.

| d | link-ends, corners | spectrum of the corner Laplacian | resistance of a corner | (2d - 1)/(2 d (d - 1)) | smallest ||T||_HS^2 / (lambda^2 abs(theta)^2) in 20,000 random families | bound 8 (2d - 2)^2 |
|---|---|---|---|---|---|---|
| 2 | 4, 4 | 0, 2 (twice), 4 | 0.750000 | 3/4 | 65.23 | 32 |
| 3 | 6, 12 | 0, 4 (3 times), 6 (twice) | 0.416667 | 5/12 | 267.66 | 128 |
| 4 | 8, 24 | 0, 6 (4 times), 8 (3 times) | 0.291667 | 7/24 | 634.44 | 288 |
| 5 | 10, 40 | 0, 8 (5 times), 10 (4 times) | 0.225000 | 9/40 | 1095.02 | 512 |

What the run was to test, fixed before it ran (the script prints each quantity next to its predicted value): the
spectrum is 0, 2d - 2 (d times), 2d (d - 1 times); the resistance equals (n - 1)/m, n link-ends and m corners; no
family falls below the bound. All three hold. The smallest ratios sit a
little above twice the bound, as the hand check 3.4 suggests (64 against 32 in d = 2). The true constant is not
determined here.

## 4. State at the end of this row

**PROVED here (by hand; checked by no one).**
- Lemma PC-c (3.2). For every family of two-axis link-end translations whose bracket is lambda times a co-closed
  one-axis corner twist theta, modulo exact twists, the cost ||T||_HS^2 is at least 8 (2d - 2)^2 lambda^2 |theta|^2.
  With it: the corner Laplacian of a site has the eigenvalues 0, 2d - 2 (d times), 2d (d - 1 times) (on file for
  d = 4, row 1015); a corner has
  effective resistance (2d - 1)/(2 d (d - 1)); the corner form of the family inequality returns at best a site-local
  bound, weaker than the trivial one at every coupling if its constant is the K_rot of the 2D proposition, and of
  the order of the area (at best 51 K_rot t^2 A in d = 4) on the non-central sheet path of C2.
- Remark 3.5: the exact second-order response to an arbitrary corner twist at zero twist, a sum over sites.
- Corollary PC-c2 (3.6): in every corner-twisted measure, with any pins and strengths up to beta, the response to a
  co-closed one-axis corner twist obeys an inequality of the family form with the constant 2 beta/(2d - 2)^2
  (beta/18 in d = 4). It follows from the bound with no bracket, R <= 4 beta |theta|^2. So the port that C1 asked
  for holds and carries no gain.

**ARGUED here.** 1.3 (the power count for p-forms; transitivity as the property that the gauge theory lacks); 2.3 (in
two dimensions the rotation-invariant half comes from positivity, not from the twist; the gauge form of that step
fails at its first line). Both restate, in my words, what the record holds.

**GUIDE.** The screening of 1.2; the hand checks 3.4; the numeric sanity run 3.7.

**Not new, by my own grep.** Everything in Sections 1 and 2. Lemma PC-c is the proved form of row 1013's ARGUED
verdict on C1 (`gap-invent-selective-max.md` L166, L191), which two cross-provider checks had left open for want of
the written count. It is the corner analogue of Lemma PC of row 1188. The spectrum of the corner Laplacian for d = 4
is row 1015's (`gap-invent-selective-check.md` L157-161).

**OPEN, unchanged.** (FS), which is (SEED); (N-phys); the continuum datum of the T0 chain; (BS); (W); the
Jaffe-Witten gap. This row gives no proof and no disproof of the mass gap.

**For the lead (ARGUED; one paragraph).** This is the fourth plain-brief row by this model family in one evening, and
it ends at the same map. In the 2D proof the bracket gives the charged half and a positivity structure gives the
rotation-invariant half. For Wilson SU(2) every port of the bracket step now has a written first failing step: the
class of all pins (rows 1011, 1016), the pinned slice (Lemma PC, row 1188), the corner model (row 1189), and the
corner graph in the form of the family inequality (Lemma PC-c and Corollary PC-c2 here). The port of the positivity step failed three
ways in row 1084. (N-phys) lives in the half that needs the positivity step. So the next useful row is not a fifth
screening. It is either a row that looks for a positivity or monotonicity structure of plaquette functions under
Wilson SU(2) that survives Lemma HF and Theorem EP-NO, or a row on neutral mixing in the smallest model with a
non-transitive non-abelian symmetry. That model is on file: (P4) of row 1084 (`gap-checkerboard-singlet-astra.md` L402-423,
four O(4) sheets on a 2D base with an on-site plaquette term), with P4-MIX OPEN for kappa > 0 (its L590-607), inside
(SING) of rows 1053, 1076 and 1115. Its two ends are of the 2D type (kappa = 0: four O(4) models; kappa = infinity: the
corner model of row 1189 with a one-plaquette fibre, a transitive symmetry). I have no mechanism for either row and
do not recommend one.

Finished 2026-11-20T00:54Z (`date -u`); wall clock from 2026-11-19T23:54Z. One numeric run of about 3 s (GUIDE). No
subagent. Files written: this file only (scratch under /tmp aside).

RESULT: no proof and no disproof of the 4D SU(2) mass gap; (FS) = (SEED), (N-phys), the continuum datum, (BS), (W) and the Jaffe-Witten gap stay OPEN. Claude Fable 5.2 max, Mac mini worker 1; author only, checked by no one. A fourth plain-brief screening (ten candidates, each grepped) found no route off the lane's map. Reading (ARGUED; on file in parts, rows 1009, 1076-1086): in the posted 2D O(4) proof the bracket gives only the charged half, and the rotation-invariant half comes from a positivity structure (abelian conditional ferromagnets with association) followed by the coupling integral; the gauge form of the coupling integral is Theorem D (f), the gauge port of the positivity step failed three ways in row 1084, and (N-phys) lives in that half. PROVED by hand: Lemma PC-c (for every family of link-end translations whose bracket is lambda times a co-closed one-axis corner twist theta, the Gram cost ||T||_HS^2 is at least 8 (2d - 2)^2 lambda^2 |theta|^2, because the corner Laplacian of a site, the graph K_(d x 2), has a gap 2d - 2 above the gauge directions; its spectrum for d = 4 is on file, row 1015); Remark 3.5 (the exact second-order response to any corner twist at zero twist is a sum of one-site forms); Corollary PC-c2 (in every corner-twisted measure, any pins, strengths up to beta, an inequality of the 2D family form holds with the constant 2 beta/(2d - 2)^2 and is a corollary of the bound with no bracket, R <= 4 beta |theta|^2; on the sheet of C2 it is of the order of the area). So candidate C1 of row 1013, left open by the checks of rows 1013 and 1051 because its count was never written, FAILS as a band crossing in the form proposed; this is the flux half only, and other fourth-order identities are not excluded. GUIDE: one numeric sanity run (d = 2 to 5, 20,000 random families each), no violation. Output library/gap-mini-solve-d-fable.md.
