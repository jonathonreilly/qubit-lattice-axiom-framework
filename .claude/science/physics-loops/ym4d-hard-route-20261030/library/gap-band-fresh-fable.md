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
    r := (Z_0 - Z_{e_4}) / (Z_0 + Z_{e_4}) = (2x + x^2 - y) / (2 + 2x + x^2 + y), and x/(1+x) <= r <= x.
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
