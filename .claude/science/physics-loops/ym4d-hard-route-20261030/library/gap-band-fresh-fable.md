lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-23T04:47Z

# gap-band-fresh-fable (queue row 1402): a new band direction from first principles

Status: research-stage working state, nothing here is a public claim. Worker file of queue row 1402, pinned at
commit 4f7004035, branch claude/ym4d-hard-route. Started 2026-11-22T16:47Z (date -u). Written section by section; the last
section present is the point the run reached.

## 0. Plan (written before any reading beyond GOAL.md and row 1402)

- Phase 1 (first principles). Read only: GOAL.md, the rule sections of FINISH.md, row 1402, row 1367, published
  work (Balaban; the Sussman-Alpoge account). From the target (M-neutral), derive how a proof of a gap at one
  fixed physical side could cross couplings of order one. Write the route and its first exact lemma in Section 2
  BEFORE reading rows 1128 to 1401.
- Phase 2 (comparison). Read the RESULT parts of rows 1379 to 1401, the filter (t1) to (t5) and Remark PAIR of
  row 1386 (its 4.5), and requirement (b) (its 4.3). Say whether the route is on file and what that row found.
- Phase 3. For the route kept: show it is not equivalent to the seed or to (M-neutral); run the filter; attack
  its first lemma. A quantified negative for a named class is a valid result.
- End: the next two rows with decisive outcomes, then the RESULT line.

Step log (each time from a fresh date -u):

- 2026-11-22T16:47Z file created with this plan.
- 17:30Z Phase 1 written (Sections 1 and 2) before any reading of rows 1128 to 1401 or of lane files. Read so far:
  GOAL.md, FINISH.md lines 1-84 and 299-362, rows 1402 and 1367, and my own navigation notes (which name some
  on-file items; I mark those below as "expected on file").

## 1. Phase 1: what the target asks, from first principles

All of Section 1 is ARGUED (physics-level derivation, written blind), not PROVED, unless marked.

**1.1 The target as one number.** Let T be the transfer matrix of the n^3 spatial torus at bare coupling beta,
with eigenvalues lambda_0 > lambda_1 >= ... in the neutral sector. (M-neutral) reads
s(t) := sum_{i>=1} (lambda_i/lambda_0)^t <= 4/21 at t = 2 floor(n/1024). Two exact rewritings:

- (thermal form) 1 + s(t) = Tr_neutral T^t / lambda_0^t. With the box read in the crossed channel (lattice
  rotation by 90 degrees) this is a Casimir statement: the free energy of the slab of thickness t = L/512
  differs from the bulk value by at most log(25/21)/(L^3 t), about 1.3e-9 / t^4. Free gluons give about
  0.66 / t^4. So (M-neutral) says: at temperature 512/L the pressure is nine orders below Stefan-Boltzmann.
  With a glueball gas this needs m t >= about 22, so m L >= about 10^4.
- (replica form) (1 + s(t))^2 / (1 + s(2t)) = Z(t)^2 / Z(2t), and s(2t) <= s(t)^2. So the seed is the statement
  that the doubled torus weighs the same as two copies of the single torus (Section 2).

**1.2 What the trajectory fixes.** On the trajectory beta_j = 8 b_0 log n_j - C + o(1) with 8 b_0 = 11/(3 pi^2)
= 0.3715 (1/(8 b_0) = 2.69), and the physical side L enters only through C. So (M-neutral) at one L is:
there are C and c_0 with m(beta) >= c_0 exp(-beta/(8 b_0)) for the lattice gap at all large beta. Two facts follow.

- (F1, sharp rate below the band, bounded loss inside it.) The exponent 2.69 must be exact, so every scale
  where the running coupling is small must be crossed with the exact one-loop rate: only the Balaban control
  can do that. Between the scale xi_0 where the running coupling reaches the fixed value gamma_0 and the seed
  scale, the ratio of scales is a fixed number R(gamma_0). So in the band only cutoff-uniform positivity of
  constants matters; no sharp rate is needed there. The band is "a bounded number of non-perturbative block
  steps with any bounded loss".
- (F2, one object.) If the effective theory at scale xi_0 converges as the cutoff is removed, (M-neutral) at
  late cutoffs is one strict inequality about one object (the continuum effective theory at scale xi_0 in a
  box of R^4 blocks), not a family. It has no parameter to vary except the scale itself.

**1.3 Three tests any crossing must pass (necessary inputs).**

- (N1, dimension) Five-dimensional SU(2) has a bulk transition at beta about 1.64 and a Coulomb phase above it.
  So a first lemma that holds on every cell complex, or in every dimension, is false or useless. Dimension
  can enter only through a comparison of two scales (classical weight lambda^(d-4) of the coupling), through
  duality, or through topology.
- (N2, group) Four-dimensional compact U(1) has a Coulomb phase. The lemma must use the non-abelian structure
  (curvature of the group, the O'Neill term of the gauge quotient, or the sign of b_0).
- (N3, action) The fundamental-adjoint SU(2) action has a first-order line ending at a critical endpoint
  (near beta_F 1.5, beta_A 0.9), where the scalar glueball mass vanishes in lattice units while the string
  tension stays positive. So (a) flux and twist quantities cannot control the neutral sector, and (b) a
  single-coupling lemma that holds for a class of reflection-positive actions containing that endpoint is
  false. A valid lemma is either a statement on the renormalized trajectory (late cutoffs), or uses a
  property that the Wilson weight has and the endpoint weight lacks. (My notes say the lane has this as K7.)

**1.4 Classes of crossing and where each stops (blind assessment).**

| Class | Mechanism | Stops at |
|---|---|---|
| C1 finite-size criterion at each beta | box at least xi(beta) at every beta | infinite cost at late cutoffs unless a UV carry exists (my notes: Theorem T, row 1332, expected on file) |
| C2 transport along beta | Feynman-Hellmann: d(m^2)/d(beta) = minus the forward form factor of the plaquette in the lightest state; needs it to be at most C m^2 | a matrix-element bound in the band (my notes: (VIR_K), row 708, on file) |
| C3 exact two-scale inequality | coupling(2L) <= lambda^(d-4) coupling(L) - delta(group) | no exact definition of the coupling with both halves as inequalities (Migdal-Kadanoff, Tomboulis: row 1025, on file) |
| C4 structural zero-freeness (Lee-Yang in the plaquette couplings) | half-plane property of Z in per-plaquette beta_p | false as a complex-independent theorem by N1 (5D zeros pinch the real axis) |
| C5 sharpness (decay or order) | positive association and a Russo-type formula | no positive representation for SU(2) (signed surface sums) |
| C6 certificates in infinite volume | SU(2) loop equations are linear and closed on single loops (Kazakov-Zheng bootstrap); SDP dual certificates are exact | bounds reach loops of length about 20; a gap needs all states, so a truncated relaxation gives no lower bound on m |
| C7 curvature class along the block map | Bakry-Emery class is closed under Riemannian submersions (Lott) and gauge quotients; O'Neill term gains per scale | the class is entered only below beta about 0.25 (Hess S has directions of size sqrt(beta)) |
| C8 other axes (Higgs coupling, thin twisted torus, temperature) | Fradkin-Shenker region, semiclassical twisted torus | each relocates the band to v about Lambda or L about 1/Lambda |

Verdict of the blind pass: every class meets the same one-parameter non-perturbative interval. I found no
mechanism that crosses it. Two items in the table are, to my knowledge at this point, possibly not on file
and exact: the replica form (Section 2) and the submersion-stable curvature class C7. I keep the replica form
as the route because its first lemma is an exact identity with new sectors, and C7 as the alternate.

## 2. Phase 1: the route kept from the blind pass, and its first exact lemma

Written 17:31Z (date -u), before reading rows 1128 to 1401.

**2.1 Route COVER (neutral seed = disorder of the replica swap; sectors = covering tori).**
For a rank-4 period lattice Lambda in Z^4 write Z(Lambda) for the Wilson partition function on Z^4/Lambda.
For a nonzero k in Z_2^4 and Lambda = n Z^4 put Lambda_k = { n v : v in Z^4, k.v even } (index 2), and
Z_k := Z(Lambda_k), Z_0 := Z(Lambda)^2.

**Lemma COV (to prove in Phase 3; exact, no smallness).**
(a) Z_k is the partition function of two replicas on Z^4/Lambda with the replica swap as the transition
    function in each direction mu with k_mu = 1. For k = e_mu it is the torus with side mu doubled. For
    |supp k| >= 2 it is a sheared torus; for k = (1,1,1,1) the period lattice is n D_4.
(b) (order) Z_k <= Z_{k - e_mu} for mu in supp k (with Z_0 for the empty support). Proof idea: in the transfer
    picture along mu, Z_k = Tr(T^n tau) and Z_{k-e_mu} = Tr(T^n) with T >= 0 and tau a commuting involution.
(c) (seed form) with x = s(t), y = s(2t) for the time transfer matrix,
    r := (Z_0 - Z_{e_4}) / (Z_0 + Z_{e_4}) = (2x + x^2 - y) / (2 + 2x + x^2 + y), and x/(1+x+x^2) <= r <= x
    (corrected in 4.2; the blind text had x/(1+x), which is false when y = x^2).
    So the seed is "the swap-odd electric sector has weight at most about 0.16", the exact analogue, for a
    0-form Z_2, of an electric flux sector weight.
(d) (truncated correlations) for the product measure, < (f - f')(g - g') > = 2 <f ; g>. So the neutral
    connected correlations are the two-point functions of swap-odd fields of the SU(2) x SU(2) theory.
(e) (scale step, d = 4) with A = [[1,1],[1,-1]] + [[1,1],[1,-1]], A^T A = 2, the lattice A(n Z^4) =
    Lambda_(1,1,0,0) intersected with Lambda_(0,0,1,1) is a cubic torus of side sqrt(2) n, rotated. So two
    sheared double covers make one similarity step. The finite part F(L) = log Z(L) + f L^4 obeys
    0 <= F and F(cover) <= index . F(base).

**2.2 What the route would need next (blind statement of its wall).** A crossing needs a gain
F(sqrt(2) L) <= theta F(L) with theta < 1 where F is of order one. Lemma COV gives only the trivial side.
The route has no dimension input beyond (e) and no group input. By N1 and N2 of Section 1.3 it cannot cross
the band alone. I expect the filter of row 1386 to say the same. It is kept only if the swap sectors give
an inequality that the centre-flux sectors do not.

**2.3 Alternate (C7).** Lott's theorem: a Riemannian submersion with compact fibres pushes a measure with
Ric + Hess V >= rho forward to one with the same bound; an isometric quotient does too, and adds the O'Neill
term. This is a parameter-free class that is closed under block maps that are submersions. Entry fails for
the Wilson measure above beta about 0.25 in the product metric. First lemma would be: find a block map and
metrics for which one step is a submersion up to constants c(d) with c(4) = 1.

**2.4 Blind verdict.** No route found that crosses the band. Findings to compare in Phase 2: (F1), (F2),
N3(a) (flux quantities cannot see the neutral sector), Lemma COV, class C6 (bootstrap certificates), C7.

## 3. Phase 2: comparison with the file

Written 17:38Z (date -u). Read for this section: the RESULT parts of rows 1379 to 1401 (row 1400 has none yet),
rows 1332 and 1335 (RESULT parts, for Theorem T), `library/gap-mech-direction2-fable.md` Sections 4.1 to 4.5
(Remark PAIR, requirements (a) to (i), the filter (t1) to (t5)), and grep hits in `library/gap-*.md`.
`library/open-core.md` has no hit for replica, swap, covering, bootstrap, Lott or submersion.

**3.1 Verdict: every item of the blind pass is on file. No route is kept from Phase 1.**

| Blind item (Section 1 or 2) | On file | What that row found |
|---|---|---|
| N1 (five dimensions), N2 (U(1)), N3 (mixed-action endpoint) | filter (t2), (t1) and requirement (c) of row 1386 (4.3, 4.5); K7 in `parts/gap.md` L28-30; rows 1380, 1382, 1384 | the selectivity tests; row 1382 with check 1384: one survivor of the 5D test (row 1143 toron integral), struck by Lemma GRP |
| C3, the pair "group gain times dimension carry" | Remark PAIR (row 1386 4.2, credited there to row 1128) | "the missing object is the carry, not the gain"; no inequality passes a local gain through an exact carry at order-one coupling |
| (F1) bounded loss in a renormalized variable; (F2) one object | Proposition CH and (SEED-FP) of row 1332 (check 1335); Corollary S3 of row 1391 ("bounded loss is the seed itself"); kinds K-I, K-II of row 1386 4.4 | first failing step: one block step at an effective coupling of order one |
| C1 with a UV carry | Theorem T of row 1332: (KER) at a window coupling plus (A1), (A2), (A3) | (A1) rows 1391 to 1400, open; (A2) is the band |
| C2 transport along beta | (VIR_K), Theorem TR, row 708 (`gap-mid-max.md` Section 4) | a matrix-element bound, open in the band |
| Thermal and Casimir form (1.1); the beta-integral of the plaquette shift | `gap-loop-eq-opus.md` (Lemma 3.1; delta = 48 a^4 times the integrated shift); Remark RAD of row 1390; row 1283 (7) | identities; no bound at order-one coupling |
| Route COVER, Lemma COV (a), (b): swap sectors are covering tori, with the order | row 1131 (`gap-council-prob-astra.md` L26, L68: two sheets, Z_tau = Z(B'), Z_0 = Z(B)^2); sheared tori and Lemma SHIFT (row 962, `gap-constraints-max.md` L185-198, 7.4); Lemma FR and I9 of row 1066 (`gap-outside-box-max.md` L113-120, L190) | row 1131: odd winding has probability tending to 1 on the fine trajectory, its bound carries no information; row 1066: "the same operators T_B, read on sectors"; "changes a constant, not the crux" |
| COV (e), the spacetime group of the box as a source of sectors | `gap-mini-solve-k-fable.md` L52, L72 (row 1190 item 3) | identities on file; "does the bracket of this group give a gain" left unanswered. See 3.2 |
| C4 Lee-Yang in plaquette or centre-breaking fields | I17 of row 1066, B9 of row 669 ((LY), (M6)), `gap-brainstorm2-max.md` items 7, 40 | not selective; fails |
| C6 loop equations and bootstrap certificates | `gap-loop-eq-opus.md`: SU(2) loop equations in Ward form; Proposition VB (volume blindness) | local loop equations with reflection positivity cannot bound the finite-size shifts |
| C7 Bakry-Emery under submersions, O'Neill, Singer | F1 of `gap-afield-a-max.md` L336, L377 (Lott, math/0211065); idea 18 of `gap-brainstorm2-max.md` L223; row 957 | a ceiling; curvature fails at typical fields at beta 2.3; requirement (f) of row 1386 forbids a worst case |
| C8 thin twisted torus, Higgs axis | `gap-ac-lat.md`; example under (t2) of row 1386; I17 (fundamental Higgs) | the twisted gap is kinematic; the continuation in the width is the band |

**3.2 The one question the file left open that the blind route touches** (row 1190 item 3: does the
non-abelian symmetry group of the box give a gain?). Answer by the filter, ARGUED: no. Every inequality of
Lemma COV, and every inequality among partition functions of flat tori glued by a lattice symmetry or a
replica permutation that follows from positivity of the transfer matrices, holds for every
reflection-positive hypercubic law, compact U(1) at weak coupling included. So it fails (t1) at its first
line: it has no line where the group enters. It also fails requirement (b): its only dimension input is the
index 2^(d/2) of a similarity step. I do not keep it.

**3.3 Requirement (b) and Remark PAIR against the blind pass.** My blind table agrees with Remark PAIR: C3
is the only class with both inputs, and it stops where row 1386 says, at a carry with a sign. The blind pass
adds no carry. It agrees with row 1386's judgement that no first lemma for the band is on hand.

**3.4 Further matches found after 3.1 was written** (17:41Z, by grep and by reading the cited lines).

| Blind item | On file | What that row found |
|---|---|---|
| The 2D loop-soup proof of Ding, Huang and Yang read as a gauge split (an abelian part in a random environment made by the other components) | row 1197 (`gap-mini-solve-g-fable.md`, Lemmas G1, G2, (GC)); M-F of row 1380 (`gap-mech-direction-fable.md` L271-277) | fails at the free collective coordinate: an O(3) block has an orientation with a scale-free law, a ball of gauge field has none, so a decoupling event at scale L has probability of order exp(-c/g^2(L)) |
| Monotones of the flow (a-theorem of Komargodski and Schwimmer; the entropic form of Casini, Teste and Torroba) as an exact carry with a sign in d = 4 | row 1002 (`prior/gap-kflow-read-opus.md` L95-111, as quoted in `gap-compact-rigidity-max.md` L35, L111); `gap-compress-check-astra.md` L254 | every published monotone is group-blind, needs the relativistic continuum, and allows a massless end (a_UV = 3 a_V) |
| Diamagnetic and paramagnetic signs of the one-loop step | `gap-council-conf-fable.md`, `gap-council-rg-fable.md`, `gap-brainstorm2-max.md` (not re-read; file names from grep only) | not read in this row |

## 4. Phase 3: no route is kept; the filter on the blind route; one elementary remark

Written 17:41Z (date -u).

**4.1 Decision.** The row keeps a route only if it is not on file or the row that holds it left it open.
Route COVER is on file (row 1131, row 962, row 1066). The alternate C7 is on file (row 957; idea 18 of
`gap-brainstorm2-max.md` L223; F1 of `gap-afield-a-max.md` L336). So there is no route to attack, and I do not open one by renaming.

**4.2 The filter of row 1386 on route COVER (for the record).**

- (t5) Equivalence. Lemma COV (c) is an identity: r = (2x + x^2 - y)/(2 + 2x + x^2 + y) with x = s(t),
  y = s(2t). PROVED (elementary): since 0 <= y <= x^2, the numerator is at least 2x and the denominator at
  most 2 + 2x + 2x^2, so r >= x/(1 + x + x^2); and r <= (2x + x^2)/(2 + 2x + x^2) <= x. The bound r >= x/(1+x)
  of the blind text is equivalent to x^2 >= y(1 + 2x) and fails when y = x^2 (one excited level).
  So the swap-odd weight is the seed quantity up to these explicit factors. Route COVER is a rewriting of the
  seed. By the rule "Equivalent is not progress" it is no progress.
- (t1) Compact U(1): the route has no line where the group enters. Fails.
- (t2) Five dimensions: its only dimension input is the index of a similarity step. Fails.
- Requirement (b): no carry. Fails.

Correction recorded: Section 2.1 (c) first printed "x/(1+x) <= r". That bound is wrong; 2.1 (c) now carries
the corrected bound. Nothing else used it.

**4.3 Remark TORNEG (elementary; PROVED here, unchecked). An answer to the question left open at row 1190
item 3 (`gap-mini-solve-k-fable.md` L52: does the symmetry group of the box give a gain?).**
Let H be these properties of a lattice law on Z^4: invariance under the hypercubic group and translations,
reflection positivity for every site and link reflection, and a positive self-adjoint transfer matrix on
every slice. Every inequality among partition functions of quotient tori, glued by any lattice symmetry or
replica permutation, that is derived from H alone holds for every law with H. The Gaussian scalar field
with nearest-neighbour action and mass mu > 0 has H. Its one-particle energy at zero momentum is
omega_0 = 2 arcsinh(mu/2) <= mu, so its even excited sum obeys s_even(t) >= exp(-2 omega_0 t). At mu = 1/n and
t = 2 floor(n/1024) <= n/512 this is at least exp(-1/256) > 0.99 > 4/21. So for every n there is a law with H on
the box of side n whose sector inequalities all hold and whose seed fails at that size. Hence the sector
inequalities of the box group contain no gain: a gain needs an input that this scalar does not have.
Limits: this is a statement about derivations from H alone. It says nothing about a derivation that adds a
Wilson-specific input. It does not use the gauge group and is of the same kind as Lemma FR of row 1066.

**4.4 What Phase 1 to 3 establish together.** A fourth blind direction pass (after rows 1380, 1386, 1390)
derived nine classes of crossing from the target alone. Each is on file with a first failing step. The
blind pass and Remark PAIR agree on the one missing object: an exact carry with a sign at a coupling of
order one. I have no candidate for it. Nothing here moves (M-neutral).

## 5. The next two rows and their decisive outcomes

**Row 1. `gap-band-fresh-check-astra62` (cross-provider check of this file; short).**
Check, in order: (i) each line of the tables in 3.1 and 3.4: is the blind item really the cited on-file
item, and is the finding quoted right; (ii) Remark TORNEG (4.3), including whether row 1190 item 3 asked a
different question; (iii) the corrected bound in 4.2; (iv) the claims (F1), (F2) of 1.2 against Proposition CH
and Corollary S3.
Decisive outcomes: if one blind item is not on file, that item is the candidate, and it goes through the
filter (t1) to (t5) before any proof row. If all lines hold, four blind passes (rows 1380, 1386, 1390, 1402)
agree, and a fifth blind direction row has no expected yield.

**Row 2. No attack row on the band. The Fable slot goes to the ultraviolet carry: `gap-univk-rar`, as
proposed by rows 1395 and 1398, after the check of row 1400.**
Reason: (A1) is the one open hypothesis of Theorem T on the side where the account's tools work, and it is
needed whatever crosses the band.
Decisive outcomes: a quantitative rarity bound for the whole discarded set with r_K(a_0) of order
e_w^(1/2) (then the conditional carry of check 1397 has its second input), or a counterexample on the
account's printed bounds (then (A1) needs a new statement).

**Reopen condition for the band (unchanged from row 1386, 4.4):** an input of kind K-I (an exact carry with
a sign for a typical-field stiffness) or K-II (a block step at an effective coupling of order one), from
outside the lane's present generating set: a new publication (the standing literature row), or an idea of
the owner. A candidate names the line where compact U(1) has zero gain and the exact classical factor it
carries.

## 6. Report

- **Verdict.** No new band direction. The first-principles pass produced nine classes of crossing and one
  route with an exact first lemma (COVER). All are on file, each with its first failing step. Route COVER is a
  rewriting of the seed and fails the filter. (M-neutral) is not moved; nothing on file is disproved.
- **PROVED here (elementary, unchecked):** the bound x/(1+x+x^2) <= r <= x of 4.2; Remark TORNEG (4.3).
- **ARGUED:** all of Section 1; 3.2; 3.3.
- **Error of mine, corrected in place:** the first lower bound in Lemma COV (c).
- **Read:** GOAL.md; FINISH.md lines 1-84, 299-362; rows 1402 and 1367 in full; RESULT parts of rows 1379 to
  1399 and 1401, of rows 1332, 1335, 1197; `gap-mech-direction2-fable.md` L267-370;
  `gap-mech-direction-fable.md` L271-294; grep hits quoted in Section 3.
- **Not read:** Balaban's papers and the account (no step here uses them); rows 1128 to 1378 except through
  the grep hits and RESULT parts named above; the full text of the on-file matches (I read the matching
  lines, not the proofs). The matches in 3.1 and 3.4 rest on those lines only.
- **No computation run.** The numeric lock was not taken. No subagents. No file edited except this one.
- **Phase discipline.** Sections 1 and 2 were written before rows 1128 to 1401 were read. My own navigation
  notes, read at the start, name some on-file items (Theorem T, (VIR_K), row 1025); Section 1.4 marks them.
- **Credits.** Tadeusz Balaban, and Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of
  their text), for the ultraviolet control that Section 1.2 presupposes. Rows of this lane as cited:
  1128 (Remark PAIR's reading), 1131, 962, 1066, 1190, 1197, 1002, 1332, 1380 to 1401. Jian Ding, Huang and
  Yang (arXiv:2611.04908) and OpenAI's O(n) papers, through rows 1379 and 1197 only. John Lott
  (math/0211065), recalled, not re-read. Vladimir Kazakov and Zechuan Zheng (the SU(2) loop-equation
  bootstrap), recalled, not re-read. The Tomboulis-Yaffe inequality and the critical endpoint of the mixed
  action are recalled physics, belief grade.

Step log, continued:

- 17:31Z Sections 1, 2 on disk (blind). 17:38Z Section 3 (comparison). 17:41Z Section 4.
- 17:41Z Sections 5, 6 and the RESULT line written.

RESULT: Row 1402 (Claude Fable 5.2 high, Mac mini worker 1, 16:47Z to 17:41Z by date -u; author only, checked by no one; no numeric run, no subagents). No new band direction: (M-neutral) is not moved and nothing is disproved. Phase 1 (blind): the target read as a thermal and a replica statement; three necessary tests (five dimensions, compact U(1), the mixed-action endpoint); nine classes of crossing; one route with an exact first lemma (COVER: the neutral seed as disorder of the replica swap, its sectors being covering tori). Phase 2: every blind item is on file with a first failing step (tables 3.1, 3.4: Remark PAIR and the filter of row 1386, Theorem T and Proposition CH of row 1332, rows 1131, 962, 1066 for the covering tori, row 1197 for the Ding-Huang-Yang port, row 1002 for the flow monotones, gap-loop-eq-opus for loop-equation certificates, row 957 and F1 of gap-afield-a-max for the curvature class). Phase 3: no route kept; route COVER is a rewriting of the seed (PROVED, elementary: x/(1+x+x^2) <= r <= x) and fails (t1), (t2) and requirement (b); Remark TORNEG (PROVED, elementary) answers the question left open at row 1190 item 3: sector inequalities of the box group hold for a free scalar of mass 1/n, whose seed fails, so they contain no gain. One error of mine corrected in place (first lower bound of Lemma COV (c)). OPEN: an exact carry with a sign at a coupling of order one (K-I) or a block step there (K-II); (A1), (A2); the seed; the mass gap. Next rows: a cross-provider check of this file; no band attack row, the Fable slot to gap-univk-rar on (A1).
