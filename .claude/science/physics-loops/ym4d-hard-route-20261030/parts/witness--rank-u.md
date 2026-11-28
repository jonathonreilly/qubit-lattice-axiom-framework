lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T03:00Z

## State of attack

*Lead check, 2026-11-01 (Opus 5.5, same session as the queue, not an audit).* Read the proof line by line against `parts/witness.md` Text 3.14. Then ran `checks/gate_ranku/check_ranku.py` on the source's own matrices, with criteria written first. At L = 5 and 6, on F = e01 with A_eps as in (S1): the largest singular value of m on NN(t_eps) falls exactly as eps, with slope 643.5 and 2181, against C_L of (S8); at eps = 0 it is 7.9 and 22.4 on the larger kernel; and with a random s in place of the staggered one it stays at 7.2 and 20.9. The registered criterion PASS-S4 (at most 1e-7) failed only at the smallest eps, where the kept singular value of the constraints reaches round-off: 5.5e-7 at L = 5, eps = 3.9e-7, and 4.8e-5 at L = 6, eps = 2e-7. A first run failed through the source's rank tolerance and is kept as `L5_first_run.out`. This is numerical evidence at L = 5, 6 for (S2), not a proof. It reads no Mini or Codex numerics, since the author ran none.

Working on queue item 12 only, at `892504e4c63f195fbd791a1db913f67b4b749459`.
Status: **discharged counterexample to the limit clause of (RANK-U)**.
Finished at an honest stop. No numerical job was run in this session.
For every box side L>=4, unit F=e01 and gauges with ||d_0 t||<=2 in the
axial reference convention, a staggered sequence tends to an axial gauge
while the entire constrained
moment-map norm tends to zero. Every limiting NN-space in that sequence
carries zero m. The spaces are nonempty. In the source's Fock convention the
same actual fields and moments give a finite bound M_L<=L+2. Thus the
fixed-box assertion for every finite gauge bound fails. The proof is saved in
[`rank-u-staggered-limit.md`](../library/rank-u-staggered-limit.md).

This refutes the local input as stated; it does not refute the conclusion
of Theorem 3.19, construct a matching Gaussian covariance, or decide NT2.

- **Discharged:** explicit currents prove nonzero m, nonzero dip and nonzero
  coupling for `A=(x0+C)e1`, uniformly in C and in limits of this family.
- **Discharged:** the leading Maxwell dipole matrix, its exact annihilators,
  and arbitrarily large kernel-matrix rank whenever the scalar kernel is
  actually nonzero.
- **Implication:** the limit-subspace clauses of (RANK-U) are equivalent to
  positive minima of explicit finite matrices on a compact set, at fixed
  box and gauge bound.
- **Discharged:** in the axial convention the moment minimum in (U2) and
  the coupled minimum (U3) are zero at M=2 for every L>=4. They are zero
  at M_L<=L+2 after conversion to the Fock convention.
- **Gap:** pointwise nonvanishing without the limit clause, a replacement
  that survives the counterexample, and the actual level-j rank theorem.

The numerical preflight found 65% memory free but the machine's lock held
by `excess-v6d`. While waiting, the exact counterexample above made a numeric
run unnecessary. No acquire succeeded and no numeric job was started.
The next scientific step, if reopened, is a changed local statement (for
example the proposed two-source variant), not an attempt to prove (U2)/(U3)
as written.

## Scope and source

This is a mathematical working note, not an audit or a proof of Yang--Mills
existence. The definition of non-triviality is NT1 and NT2 in `../GOAL.md`.
No hard-core proof is imported. The requested source is `witness.md`, Text
3.13--3.14, especially Lemmas 3.13--3.15, Theorems 3.16 and 3.19, and Text 7
item 29. The earlier `gates/witness-3b7fd4e57.md` predates (RANK-U).

The task's restricted output and stopping instructions override the generic
campaign and delivery procedures. The repository workflow was read through
`git show HEAD:docs/ai_methodology/SCIENCE_WORKFLOW.md` because it is outside
this sparse checkout. No scientific status is inferred from planning state.

## Target as read

**Discharged counterexample to this target's limit clause.** For nonzero
constant flux F, on a sufficiently large finite box, and for every site
function t with bounded gradient, the limiting spaces
`NN(t) = ker(div) intersect ker(rho_A) intersect PP_h^perp`,
`A = e_F + d_0 t`, must carry a nonzero moment map
`m_J(F') = <J, P[F',F] - tbar e_F'>`. The space `N(t)` without the harmonic
polynomial constraints must carry a nonzero dipole. The row must also be
controlled relative to the error moments. The required quantifiers and norms
will be made explicit below; pointwise nonvanishing is not yet a bound for
the level-j comparison.

**unchecked.** The source's WKB sketch and its earlier numerical tables have
not been reproduced. They are not premises here.

## Attacks made first

1. **Discharged, initial algebraic attack on a degenerate flux.** Take F=e01 and a
   shifted axial gauge. The attempt to kill m fails by an explicit witness:
   if y is an interior 02 plaquette, J=H y belongs to NN and has m_J=2e12;
   K=y belongs to N and has dip(K)=e02. Both survive every C. The same
   family exposes a real degeneracy: for C>0 its dipole image has dimension
   three, not the rank five observed in the source's listed runs.
2. **Discharged, limiting-space attack.** The small matrix example in the
   finite-cell lemma shows why pointwise nonvanishing cannot replace the
   limit-subspace clause. It is not a counterexample in the lattice model.
3. **Discharged, kernel attack.** Differentiate `1/(4 pi^2 |z|^2)` twice.
   The answer is `Q(z)=(pi^2 |z|^4)^(-1) Lambda^2(I-2nn^T)`, n=z/|z|.
   For u=e01 and d=e23, `u.Q(z)d=0` for every z!=0 although both vectors
   are nonzero and Q(z) is invertible. Entire same-duality three-spaces
   also pair to zero. The full algebra is in the companion lemma.
4. **Discharged, decisive bounded staggered attack.** Perturb the axial
   gauge by `epsilon (-1)^x1 x0^3`. The density tests with site functions
   `(-1)^x1 x2` and `(-1)^x1 x3` impose two exact constraints for every
   epsilon!=0. Those constraints annihilate the two particular polynomials
   carrying the axial moment. The other terms tend to zero by an explicit
   estimate. This is a model counterexample to the limit clause; see below.

**Unchecked, unrun proposals.** Self-dual/anti-self-dual finite-box SVDs and
staggered gauges were registered in `../checks/rank-u/CRITERIA.md`, but have
not been run. No numerical evidence is claimed from them. No general
rough/smooth or WKB argument was established.

## Exact partial results and their scope

The initial derivations are saved in
[`rank-u-finite-cell.md`](../library/rank-u-finite-cell.md) and
[`rank-u-dipole-kernel.md`](../library/rank-u-dipole-kernel.md).
They are new author derivations in this session, without an independent
reader or formal audit. No hard-core input is used in them.

## The decisive counterexample

**Discharged.** Fix any L>=4, put ell=L-1, and take

    F=e01,       e_F=x0 e1,
    t_epsilon=x1+epsilon (-1)^x1 x0^3,
    0<epsilon<=1/(4 ell^3).

The link-gradient bound in this axial convention is at most 3/2. For any J
in N(t_epsilon), testing the zero site densities with
`lambda_a=(-1)^x1 x_a`, a=2,3, gives

    <J,x0^3 e2>=<J,x0^3 e3>=0.                                (C1)

The endpoint averages of lambda_a vanish on 1-links; all terms of the
unperturbed field therefore disappear from the test. The remaining
identity follows by subtracting the gradient of x0^3 x_a and using
conservation. These constraints disappear at epsilon=0.

For this F, valid particular solutions are
`P_12=-(x0^3/3)e2`, `P_13=-(x0^3/3)e3`, and P_k=0 for the other four
planes. Thus (C1) kills the particular-polynomial contribution to m exactly.
The density equation along each 1-chain, including its endpoint, gives

    ||J_1||_1 <= 4 epsilon ell^4 ||J||_1.

The unperturbed tbar e_k terms either are harmonic polynomials or reduce
by conservation to pairings with J_1. The perturbed terms have coefficients
bounded by epsilon ell^4. Consequently, with E=4(L-1)L^3,

    ||m_epsilon(J)||_2
       <= sqrt(6E) (8 ell^6+ell^4) epsilon ||J||_2
       for every J in NN(t_epsilon).                          (C2)

Also `dim NN(t_epsilon)>=(2L-4)L^3-139>0`. Along
epsilon_n=1/(4 ell^3 n), take any convergent subsequence of the orthogonal
kernel projections, with limit S. The moment matrices converge to T_0 and
(C2) gives `T_0 S=0`, while rank S>0. This is exactly the forbidden limit
in (RANK-U). All identities, estimates, signs and boundary conventions are
derived in the [counterexample proof](../library/rank-u-staggered-limit.md).

**Gap, distinct question.** This does not show that m_epsilon is zero on
NN(t_epsilon) at any fixed epsilon>0. Pointwise nonvanishing may survive.
The stated target explicitly includes limits, and that clause is false.
For a Fock reference replace t_epsilon by t_epsilon+x0 x1/2, and adjust
the polynomial particular solution by the same endpoint-averaged gauge
term. The moment map and actual fields are identical; the uncentered
gradient bound becomes (L-1)/2+3/2. Section 6 of the counterexample proves
this conversion, including its Ward identity. A newly quantified theorem
requiring L(M) much larger than a fixed Fock-coordinate M is not ruled out
by this construction. Neither is a newly defined rescaled limiting moment.

**Discharged (upper rank bound).** If a bilinear form B vanishes on S x S,
where S has codimension c, its matrix in S plus a complementary space has
blocks `[[0,A],[D,E]]`. The first block row has rank at most c, as does the
second block row, so rank B<=2c. This proves the linear-algebra step of
(3.9) for any cubic form whose contraction has the asserted isotropy. It
does not prove that a level-j matching produces the requisite finite
isotropic graph. In the many-cell formulation, a rank-six far term gives
the corresponding rank-six upper bound, conditional on the exact elimination.

**Unchecked at level j.** The Wilson lower bound in Lemma 3.14 uses a largest
shift of a finite-range matrix. It has not been extended to an exponentially
decaying cubic form here. Theorem 3.16 was read together with Lemmas
3.13--3.15 and their Ward-identity input; its Wilson proof is not treated as
a proof at level j or independently certified by this note.

**Discharged (special case of the requested local statement).** In the axial
family above, L>=4 suffices and `||H y||_2<=64`, `||y||_2=2`. After unit
normalization the moment norm is at least 1/32 and the moment-dipole
coupling in direction `(e0+e1)/sqrt(2)` at least 1/64, independent of C.
The same fixed witnesses belong to all limiting subspaces in this family.
This proves its local limit clause, not the quantifier over arbitrary t.

## What this does to the proposed level-j route

**Discharged failure of the local uniform inequality.** Use the matrices of the
finite-cell lemma: C=[div; rho_A; harmonic moments], C_0=[div; rho_A],
T=m and Delta=dip. Fix a box, |F|=1, t(x_*)=0 and ||d_0 t||_infinity<=M.
Let Gamma be the closure of their two kernel projections, denoted S and P.
The proposed inequalities are

    inf_Gamma ||T S||_op > 0,
    inf_Gamma ||Delta P||_op > 0.                               (RU)

The first infimum equals zero at F=e01, M=2 in axial coordinates for every
L>=4 by (C2), or at the converted finite Fock bound M_L. Thus increasing
a fixed box does not make it valid for every finite M. The second inequality
alone remains open for arbitrary gauges. The compactness argument is valid but
cannot produce positivity. A normalization w(J)>=||J||_2, including finitely
many higher moments with this norm term, still gives a ratio bounded by
C_L epsilon in this sequence. Normalizations without a norm term would
need a new statement; they do not change the zero map on the limiting space.

**Discharged failure of the uniform version; separate auxiliary defect.** The condition
actually used when selecting a nonzero scalar kernel is

    inf_Gamma max_(n in D_10)
       ||S T^T Qhat(n) Delta P||_op > 0,                        (RU-pair)

where D_10 consists of the four coordinate directions and their six
normalized pairwise sums. The companion lemma proves these ten directions
detect every nonzero scalar kernel. (RU) by itself does not give (RU-pair)
for arbitrary pairs of images. Moreover (C2) makes (RU-pair) zero in the
actual lattice model in this bounded sequence. Pointwise compatibility
remains open. Rank(dip)>=4 would suffice pointwise, but the axial
example proves that particular uniform repair false; a non-duality
three-dimensional image can suffice and does in that example.

**Gap (the exact level-j error comparison).** For seven selected row and
column currents let

    B_ij = m_(J_i)( Q(z_i-z'_j) dip(K_j) ),
    exact eliminated matrix = B + E.

The rank-six contradiction requires an admissible geometry for which

    ||E||_op < s_7(B),                                         (ERR-7)

uniformly over the bounded covariances and the levels under consideration.
Here E must include nonuniformity of the far flux, every multipole and bulk
remainder, the replacement of the level-j polynomial response, and any
finite-volume error if a torus is used. This exact inequality has not been
proved in the source or here. Given (ERR-7), for every vector v,
`||(B+E)v|| >= (s_7(B)-||E||)||v||>0`, so B+E has rank seven and cannot
equal minus a rank-six far term. This last implication is **discharged**.

Even a future repair restoring positive local minima would leave a
quantifier problem that fixed-M compactness does not resolve. The draft
allows M of order kappa_hat_0^(1/2) R^4, because the
far plaquette flux has size R^-4 while the covariance only bounds its
potential by a constant. At fixed M, positive minima need have no specified
decay rate as M increases. In the draft's simplified scaling with R of
order D, an error `|F|D^(-(d+6))` compared with a row scale
`|F| alpha(M(D))D^-4` would require

    D^(-(d+2)) / alpha(M(D)) -> 0.                             (RATE)

This is an **implication under those schematic error sizes**, not an error
estimate derived here. Positivity alpha(M)>0 does not imply (RATE): the
positive function exp(-M) is an elementary logical counterexample. It is
not asserted to be the actual matrix minimum. The claimed 1/M row scaling,
the geometry chosen by the finite-color argument, and nonuniformity of F
all need quantitative estimates within (ERR-7). Text 7 item 29 explicitly
says its estimate is not proved.

## Inputs a level-j completion would have to supply

**Gap (named hypotheses, no import from either hard-core proof).** To use
the conditional rank contradiction one needs the following exact statements:

1. **ELIM-j:** for all the chosen finite currents and every matching
   covariance, the triple equations reduce to `B+E=-Far_b` on the constrained
   current spaces, with `rank Far_b<=6`.
2. **POLY-j:** on degree <=3 polynomial link fields, H_j=H after the stated
   normalization, and the particular cubic response differs from the Wilson
   P by a member of PP_h, with a verified Ward identity. The broader source
   symbol statements are not checked against a producer here.
3. **FAR-j/ERR-7:** the field of each compact current has leading flux
   Q(z)dip(J), and the combined remainders in the actual seven-by-seven
   eliminated matrix satisfy (ERR-7) in the same geometry and with the same
   gauge bounds. A pointwise O-term or fixed-M nonvanishing is insufficient.

These are requests stated mathematically, not claims that a hard-core
attempt has delivered them. Theorem 3.10 and Lemma 5.4 were read for their
stated small-momentum, locality and far-field assumptions only. Neither is
used as an unproved fact in the three new library entries.

**Gap (finite grid selection).** The source invokes the Gallai--Witt
finite-color theorem without rebuilding it here. The pole argument in the
dipole lemma removes the need for the separate finite-rank-kernel theorem
once a scalar kernel is nonzero. It does not supply the finite-color result
or its use with a geometry-dependent M. No literature theorem is silently
counted as discharged.

## Verification and reading boundary

**Discharged (author checks, not independent review).** The limit conclusion
was derived twice: by the operator-norm bound (S2), and directly by passing
the density constraints to the limit, forcing J_1=0 and using (S4). The
plaquette signs, polynomial particular solutions, finite-box endpoint
recurrence, dimension count, and reference-gauge conversion are written out
in the library entries. No recalled theorem is needed for the counterexample.

**Unchecked (unrun computations).** No numerical or symbolic-code check was
run. The preflight and numeric-lock status are recorded in
[`checks/rank-u/execution.md`](../checks/rank-u/execution.md). The existing
`witness_rank_moment.py` matrix construction and the `Box` class in
`witness_rank_box.py` were read for definitions; neither was executed.
No floating-point rank threshold or previous run is evidence for (C2).

Read: GOAL and FINISH first; the witness statement hits and the requested
3.13--3.16 chain; Text 3.14, Theorem 3.19 and Text 7 items 21--30;
notation and Proposition 2.2's Ward proof; the nearby tree-coefficient
statement; Lemma 3.3; the stated inputs and arguments of Theorem 3.10 and
Lemma 5.4; the earlier witness gate's verdict table and opening NT2 defect.
An initial gate search also returned unrelated gate snippets, none used.
No full hard-core attempt file, external proof account or paper was read or
used. The restriction to this item and its permitted output paths was kept.

## At this stop

- **Proved / discharged:** the bounded staggered counterexample to the
  ordinary limit-subspace clause of (RANK-U), with explicit estimate (C2)
  and nonempty limiting spaces; the Fock-reference conversion with its
  changed bound; the restricted axial-family positive result; and the
  separate auxiliary failure of the nonzero-scalar-kernel inference.
- **Conditional / implication:** rank-seven contradicts ELIM-j precisely
  when a seven-by-seven leading matrix and its actual remainder satisfy
  (ERR-7). The dipole interpretation at level j still requires FAR-j, and
  identification of its polynomial response requires POLY-j. None is
  claimed supplied by a hard-core attempt.
- **Still open / gap:** pointwise arbitrary-gauge nonvanishing, the source's
  two-far-source replacement, any newly quantified Fock-coordinate L(M)
  theorem outside this counterexample, and the actual level-j separation
  theorem. NT1 and NT2 are not established here. The false limit clause
  cannot be retained as the missing input to this route.

No file outside the permitted outputs was edited; no commit, push, PR, audit, external post or
subagent was made. Work stops with this counterexample.
