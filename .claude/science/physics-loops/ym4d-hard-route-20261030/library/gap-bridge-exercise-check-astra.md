## Repo search

Writer: OpenAI Codex, gpt-6-astra, xhigh (the dispatched model and effort).
Research check of row 1072 at `5113576a341dd34420cf5c07e46e15deb82a65df`;
not an audit, no status granted, no mass gap claimed. This file does not
attempt a new bridge, run numerical proof steps, or check the full literature
inventory in row 1072. The requested statement check is complete.

The target-specific prior digest is absent. The handoff reports a lead search
of main and PRs 10114, 10133, 10134 and 10141, without target-specific paths.
The available November 8 digest concerns other RG obligations. I read it
whole and checked its nearby hits at their source:

- PR 10114, `f76f6c649cff7dffbab664d8976e680e8f287fe9`,
  `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`
  L1–18, L106–178: an existing positive one-step plaquette witness. Its
  conclusion is an upper bound on the spectral threshold, not a positive
  lower gap or a coupling comparison. It does not supply LIN-perp.
- Main, `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`,
  `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
  L1–12, L79–94: finite-clock Villain, with both stated parameters at least
  2000. Different action/group/range; no window-only Wilson counterexample.
- Within this lane, S2 supplies MON-T's coefficient; row 878 F5 supplies
  the affine-Hamiltonian comparison; K3'/Lemma SLAB already supplies the
  slab obstruction. These are credited below, not presented as new work.

I did not repeat the lead's broad PR search or check unrelated RG hits.
Row 1073, read whole, is a literature reading, not a proof check.
The open registry has no match for
`gap-bridge-exercise`, `CA-FAIL`, `FACE-SG`, `MON-L` or `LIN-path`.
The present task is the requested check, not a new attack on those suppliers.

## Checkpoint

- Sources: pinned checkout above; Sussman–Alpoge outline and CA-I at
  `31a47c543775`, fetched once each into the new empty directory
  `/tmp/sa-gap-bridge-exercise-check-astra.arVNuY`.
- Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
  of their text. Row 1072 is by Claude Opus 5.5 high; row 1073 by gpt-6-luna high.
- Complete: MON-T's Schur and analytic-zero steps, the FSS threshold and D2
  overlap, every requested statement, and the kill table.
- Open scientific inputs: FACE-SG, endpoint MON-L, a sector-matched path
  estimate and its start bound. No new bridge attack was started.
- Failed arguments: MON-L's derivative-sign identification, LIN-perp's
  spectral inference, and BR-6/BR-7's strength claims, detailed below.
- Next decision: the lead can use CA-FAIL only with its corrected strong-
  mixing scope; no conclusion of this check supplies the remaining bridge.
- Local delivery: only this file changed, on branch
  `codex/gap-bridge-exercise-check-astra-5113576a3`; uncommitted and unpushed.

## 1. MON-T and NO-MON: HOLDS on each fixed finite free box

Checked row 1072 L121–130 against Claim S2 in `gap-aniso-trajectory.md`
L174–203. First failing line: none for MON-T or the two assertions of NO-MON.

Here is a direct check of the coefficient. Write the transverse plaquette
as the quaternion inner product of products of its first two and last two
sheet variables. Two distinct plaquettes have an unused sheet occurring
once; its central sign change kills that term. A repeated plaquette not
containing both observed sheets has a disconnected cumulant. First-order
terms also have an unused odd sheet. Thus only two copies of the common
plaquette contribute. Integrating its two unobserved sheets gives
`G(u,u')^2/4` times the quaternion inner product on the observed sheets.
The Taylor factor is `1/2`; the inner product is half the matrix trace.
This recovers S2's coefficient `1/16`, without a numerical check.

For MON-T's real bond-energy observable, the centered matrix expectation
`A` is a quaternion and satisfies `h^{-1} A h=A` for every unit quaternion.
Writing `A=a0+a1 i+a2 j+a3 k`, commuting with `i` kills `a2,a3`, and
commuting with `j` kills `a1`. Therefore `A=kappa I`. Left invariance does
the same for `B`; identical sheet laws give `B=kappa I`. Consequently
`tr(AB)=2 kappa^2` and

    c2 = (1/8) sum_{u,u'} G(u,u')^2 kappa(u,u')^2.

The `(a,b)` term has `kappa=Var(e_ab)>0`: the finite-volume density is
strictly positive on the compact configuration space and `e_ab` is
nonconstant. The partition function and numerator defining `G(a,b)` are
real analytic at each real coupling, with positive denominator. At zero
coupling, all bond terms other than `(a,b)` have a Haar variable occurring
once and integrate to zero. Four equal quaternion-coordinate variances sum
to one, so `G(a,b)=beta_M/4+O(beta_M^2)`. It is not identically zero.
The real-analytic identity theorem makes its zeros isolated in `(0,infinity)`.
This exceptional set is for the fixed box; no common exceptional set or
box-uniform Taylor remainder is asserted.

Off that set, covariance starts at zero and is positive for sufficiently
small positive `beta_T`. Its absolute value cannot be nonincreasing.
Separately, `beta_T<=epsilon/X^2<=epsilon<2.3` prevents a point of
`R_epsilon` from dominating a window point coordinatewise. These facts do
not rule out rate-only comparisons, restricted observable classes, or
comparisons that change the directions of different couplings separately.

## 2. FSS threshold and CA-FAIL: HOLDS AFTER CORRECTION

Read the open original by J. Fröhlich, B. Simon and T. Spencer,
[Infrared Bounds, Phase Transitions and Continuous Symmetry Breaking](https://math.caltech.edu/SimonPapers/65.pdf),
printed pp. 80–81 and 85–86, Theorem 3.1 and equations (3.1)–(3.5).
The Hamiltonian on p. 81 counts each unordered nearest-neighbour pair once.
Thus its `J` is exactly this note's `beta` in `exp(beta sum s_x.s_y)`.
For unit O(4) spins its conclusion is

    lim_{|x|->infinity} E[s_0.s_x] >= 1 - 2 I3/beta,
    I3 = (2 pi)^(-3) integral_{[-pi,pi]^3}
                             1 / sum_i(1-cos k_i) dk.

The sufficient threshold is `2 I3`, not an identified critical coupling.
The printed decimal for `I3` explains the author's recalled `1.01`.
No decimal evaluation is needed for the requested comparison. Since
`1-cos x>=2x^2/pi^2` on `[-pi,pi]`, let `Q=[-pi,pi]^3` and let the
ball `B_R` have the same volume, so `R^3=6 pi^2`. Then

    I3 <= (1/(16 pi)) integral_Q |k|^(-2) dk
       <= (1/(16 pi)) integral_{B_R} |k|^(-2) dk = R/4 < 1.

The middle inequality is elementary: `Q\B_R` and `B_R\Q` have equal
volume, while the integrand on the former is at most `R^(-2)` and on the
latter at least `R^(-2)`. The radial integral is `4 pi R`.
Finally `pi<22/7` gives `6 pi^2<64`, hence `R<4`.
Therefore `2 I3<2<23/10`. Every window coupling satisfies FSS's strict
sufficient inequality. This is a hand bound; FSS itself remains a named
published input, not a theorem rebuilt or formalized here.

**Replacement for L337–340 and the precision at L368.** For every
`beta>2 I3`, uniform strong mixing of the full link specification, over all
finite subsets of links and all exterior configurations, is false. Here
the bound measures distance to the *changed* exterior links, with constants
independent of the conditional volume and the unchanged pinned links. Take
the free links in one temporal layer over a finite spatial box. Fix all
spatial links in its two bounding slices to the identity and fix the other
temporal links as exterior data. The resulting specification is precisely
the 3D nearest-neighbour O(4) specification at coupling `beta`.
That boundary-influence bound would force its local expectations to be
independent of the exterior in the infinite-volume limit. It also forces
clustering: condition on the exterior of a radius-r box about one spin,
use the boundary-uniform bound for that spin, and multiply by a bounded
spin component supported outside the box. The covariance tends to zero.
The periodic-limit state is O(4)-invariant, so each spin component has zero
mean. FSS gives a strictly positive limiting sum of these covariances,
a contradiction. This avoids claiming that extremality alone implies
translation mixing without its Gibbs tail argument.

The precision's last inference at L368 needs this correction: ordinary
weak mixing measured by distance to the *whole* boundary gives no such
contradiction. Every free link in the thin slab is near a pinned spatial
link, even far from its spatial rim. Nonuniqueness of the induced 3D
specification does not refute that ambient weak-mixing bound.

This refutes any continuous-spin analogue of complete analyticity whose
definition entails the stated strong-mixing property. The
Dobrushin–Shlosman theorem read in row 1073 has finite-spin hypotheses;
it is not directly a theorem about SU(2) links. This obstruction says
nothing by itself against mixing restricted to gauge-invariant observables,
cubes with a restricted boundary class, or typical boundary data. The
spin components used above are observables of the pinned specification.

**Prior work, not a new slab construction.** `gap-tiltproof-max.md`
L175–256 (D1 and D2) has two-dimensional sheets and a finite-size infrared
sum. Its side-4 threshold `103/96` does not prove three-dimensional
long-range order or failure of uniform mixing. The closer prior is
`gap-invent-selective-max.md` row K3' (L57) and Lemma SLAB (L220–228),
which already state the 3D slab and the mixing obstruction at large beta.
CA-FAIL applies that prior device to a specified mixing claim.
No new attack on the slab is needed.

## 3. RP-ANI: HOLDS AFTER CORRECTION to its consequence

The plaquette argument at L119 holds for nonnegative finite couplings,
reflection-compatible finite volumes, and their reflection-positive limits.
Reflection normal to a coordinate axis preserves each plaquette type.
For a crossing kernel, expand `exp(beta_p s(g).s(h))` in tensor powers:
all coefficients `beta_p^n/n!` are nonnegative. Products keep positivity;
the half-space weights are conjugate factors. Gauge averaging is an
orthogonal compression and preserves positivity. Site cuts instead give
conditional products across the fixed cut. Nothing uses equality of the
three couplings. This also explains why negative couplings are excluded.
This is the positive-Gram construction already in Sussman–Alpoge's
outline, AM2 and AM4, L2773–2795 and L2834–2860, with a separate
nonnegative coefficient at each crossing plaquette.

First overreach: L119's last consequence, "inverse spectral gaps ... at
every point of every path." Positivity alone does not identify an
infinite-volume local-observable correlation length with a gap on a
finite spatial torus, including its other sectors. Also the written domain
`[0,infinity)^3` omits the face used later. At a zero coupling the transfer
operator can have a kernel; it need not have a densely defined logarithm
on the unreduced space.

**Replacement.** The anisotropic model has positive transfer operators in
each coordinate direction in the reflection-compatible construction.
Reflection positivity passes to any specified face limit by convergence of
each finite quadratic form. In a specified translation-invariant,
reflection-positive state, exponential bounds with one common rate for
all local vectors in its cyclic gauge-invariant sector exclude spectral
weight below that rate above the vacuum. Conversely a gap gives these
bounds in that sector. A positive bound, vacuum uniqueness, the face limit,
and transfer to finite-torus sectors are additional statements.

## 4. CONT, C4 and C5

**Lemma CONT: HOLDS.** At L134, a nonempty clopen subset of the connected
interval `[0,1]` is the interval. The argument needs no regularity of `P`.

**C4–C5: HOLDS AFTER CORRECTION as a method statement, not a universal
theorem.** First failing inference: L136, "Every path argument has this
form," which is not a consequence of connectedness. Both openness and
closedness can require separate estimates. For fixed constants, weak
limits pass bounds for continuous local observables; compactness and the
DLR property identify the limit if the limiting Gibbs state is unique.
This statement requires continuity of the specification, so the infinite
coupling endpoint needs its separately constructed face limit. Passing
arbitrary bounded measurable observables requires approximation in addition
to weak convergence. Existence of some constants at every parameter is not
by itself a uniform bound on those constants.

**Replacement.** An open-and-closed continuation proof needs both properties
for its explicitly chosen `Q`. A quantitative continuation proof may
instead supply a uniform positive lower bound, an integrable differential
bound, or finitely many justified comparison steps. Any such theorem must
have hypotheses that fail in each countermodel within its actual domain.
This can happen through its start data or a verified path hypothesis; the
formula need not mention the group or dimension explicitly. The
five-dimensional example remains a belief-grade test. The U(1) test has
the action and range qualifications in section 5 below.

In particular, L492's later claim of equivalence to a bounded linear
log-gap law is false. Even analytic finite-dimensional families can have a
uniform positive gap without a volume-independent derivative bound. For
example, with integer `n>=1`, `x=t-1/2`, put

    m_n(t)=2-x/(2 sqrt(n^(-2)+x^2)),  H_n(t)=diag(0,m_n(t)).

Then `3/2<m_n<5/2` for every `n,t`, whereas
`-d(log m_n)/dt` at `t=1/2` equals `n/4`. This is a hand-checkable
counterexample to the asserted functional implication, not a Wilson
counterexample or a proposed bridge.

## 5. U(1) range and step 6d, row 10

**U(1) correction: HOLDS AFTER CORRECTION to its quantifiers.** The exact
input on file (`parts/gap.md` L223) is a recalled Villain result at
`beta>=2^14`; it does not refute a theorem whose conclusion is restricted
to the Wilson window. A same-action bridge whose hypotheses hold for
U(1) and whose conclusion includes such a large-beta Villain point is
refuted by that input. Merely drawing a path through that point is
insufficient. Conversely an endpoint restriction alone does not evade
the test if the theorem also asserts clustering at every point of a path
containing that point. The absence of a supplied theorem below `2^14`
is not a theorem that no sharper published result exists. The claimed
window counterexample remains belief-grade in the evidence read here;
no Wilson/Villain identification is imported.

**Step 6d row 10: HOLDS.** The frozen 2+2 anchor has 2D O(4) sheets;
a start requiring 3D mixing belongs to the different 1+3 construction.
Replacing the start does not prove continuation. Near the anchor, the
required seed is the corrected whole-sheet mixing input plus the still
open expansion `(S)`; the posted spin two-point bound alone does not
supply either. This is a change of hypotheses, not an improvement in
the standing of method 27.

## 6. MON-L-cov and the MON-L class argument

**MON-L-cov FALSE: HOLDS.** At L412–413 take `F=H=x_p` on an
L-plaquette. Its face variance is zero. At finite couplings choose one
link of `p` and condition on the others. Write its conditional density as
`exp(f(U))/Z`, with `|f|<=B`, where `B` is the sum of the finitely many
incident plaquette couplings (`B<=2 beta_L+4 beta` for the chosen
longitudinal link). The density relative to Haar is at least
`delta=exp(-2B)`. For every real `a`,

    E[(x_p-a)^2 | exterior] >= delta integral (x_p(U)-a)^2 dU
                            >= delta/4.

The last integral has Haar mean zero and variance `1/4`, irrespective of
the fixed other three links. Infimize over `a`, then use total variance.
This proves a strictly positive, volume-independent lower bound, also
for any finite-coupling Gibbs limit. The bound depends on `beta_L` as
well as the other couplings; it need not survive `beta_L->infinity`.
It refutes the asserted covariance domination, which includes coincident
observables. It refutes no inequality solely about large-distance rates.

**MON-L class argument: FAILS as a refutation of the stated MON-L.**
First failing line: L416, "(MON-L) is a sign of d m/d beta_L."
The written MON-L at L414 is only
`m(beta_L,beta,beta)>=m(infinity,beta,beta)`.
An endpoint lower bound does not imply monotonicity between finite
couplings. Nor does nonmonotonicity along an isotropic 3D Z2 path refute
this fixed-`beta_M,beta_T` inequality. The recalled duality also needs an
observable/sector identification: critical Ising spin correlations are
not automatically the local gauge transfer gap. That identification is
not supplied in L416; the recalled Ising papers were not checked further
after the earlier logical failure.

**Replacement.** No covariance domination of the stated kind holds.
The SU(2) endpoint rate inequality MON-L remains open. A derivative-sign
law would be a stronger sufficient input. Generic coupling-monotonicity
warnings do not refute MON-L without a counterexample in its stated
one-coupling family. The five-dimensional warning is conditional both on
a gapped face and on the believed gapless endpoint.

## 7. LIN-perp: FAILS at L428

First failing inference: "So on finite boxes the transverse decay per
unit transverse step is of order log(1/t)." PERP bounds each fixed-distance
Taylor series, with constants allowed to depend on distance and box.
MON-T gives one nonzero adjacent-sheet covariance. Neither statement
provides the large-distance asymptotic or a transfer eigenvalue estimate.
Moreover MON-T's two adjacent boundary links have different transverse
orientations; this is not the autocorrelation sequence of one vector
under powers of a transverse transfer operator.

Even a two-sided comparison `m(t) asymp log(1/t)` would not alone justify
differentiating that asymptotic. A derivative bound can instead be ruled
out by integrating it, provided divergence of `m(t)` at zero is proved:
if `-(log m)'<=C` on `(0,t0]`, then
`log m(t)<=log m(t0)+C(t0-t)`, contradicting divergence.
The missing premise is the divergence of the specified spectral rate,
not this elementary integration.

**Replacement.** PERP and MON-T concern finite-volume covariances only.
They do not establish LIN-perp, its infinite-volume analogue, or that
`min(m_parallel,m_perp)=m_parallel` near the anchor. A longitudinal
LIN-path remains a legitimate sufficient hypothesis. It has not been
shown necessary, and a transverse version has not been refuted by these
two lemmas. No new spectral attack is made here.

## 8. Kill table 7.2 and the two surviving labels

The verdicts here concern the stated implications and retirement reasons.
They do not certify every historical result cited in that table.

| Row | Verdict | Exact scope or correction |
|---|---|---|
| BR-0, L395 | HOLDS | Given a true seed, the endpoint-only implication is equivalent to its endpoint conclusion. This does not rule out proving a quantitative bridge. |
| BR-1, L396 | HOLDS AFTER CORRECTION | Retire the two universal covariance comparisons tested by NO-MON. No retirement of every coordinatewise rate comparison follows. |
| BR-2, L397 | HOLDS AFTER CORRECTION | “Wounded” means covariance domination fails; FACE-SG and the endpoint rate inequality MON-L remain open. The class argument does not refute MON-L. |
| BR-3, L398 | HOLDS AFTER CORRECTION | “Blocked-stronger” is appropriate for the sufficient uniform path hypothesis below. It is not a necessary or equivalent form of every bridge. |
| BR-4, L399 | HOLDS AFTER CORRECTION | The full-specification strong-mixing carrier fails, given FSS. This does not retire all finite-size criteria or ambient weak mixing. |
| BR-5, L400 | HOLDS AFTER CORRECTION | A convergent expansion with uniform spatial decay along the whole path is a sufficient extra input. No such input is supplied. A known convergence-radius limit is not an impossibility theorem for every expansion; the numerical factor 5.4 was not rechecked. |
| BR-6, L401 | FAILS | First failing implication: membership of a blocked marginal in R_epsilon is said to give a bound on the original model's correlation length. Observable recovery is missing. |
| BR-7, L402 | FAILS | First failing claim: a size-uniform cylinder gap is “the infinite-volume gap by another name.” The forward implication needs matching local limits; its converse is not supplied. |
| BR-8, L403 | HOLDS | This is the previously stated flux-only tool, with its named inputs retained. No proof of TB is added or inferred. |
| BR-9, L404 | HOLDS AFTER CORRECTION | “Dead for now” means no supplied start estimate, not a refutation. The point with finite beta_L and beta_T=0 is not the flat-plane anchor. |

**BR-3's sufficient statement, corrected.** Let `m_L(t)>0` be the gap of
one specified transfer operator on a spatial torus, in one specified
sector. Assume `log m_L` is absolutely continuous on `[0,1]`, the start
bound `m_L(0)>=m_*>0` is uniform in `L`, and
`-(log m_L)'<=a(t)` almost everywhere, with `a>=0` integrable and
independent of `L`. Then integration gives

    m_L(t) >= m_* exp(-integral_0^t a(s) ds).

For the constant `a=C`, this is exactly L426's elementary conclusion.
At eigenvalue crossings, an almost-everywhere or suitable one-sided
form replaces an everywhere derivative. To infer the intended local
infinite-volume conclusion, specify converging states and the dense
observable sector whose spectral bounds pass to the limit.

First missing input at L426: `(S-q)` was defined for infinite-volume local
clustering (`gap-aniso-trajectory.md` L76–84), not as a uniform gap for
every finite spatial torus and flux sector. RP-ANI does not supply that
upgrade. This distinction was already made in `gap-aniso-check-astra.md`
L176–196; it must be retained. Alternatively formulate the whole path in
the one infinite-volume cyclic sector and prove the required regularity
there. Neither formulation is established here.

L430 correctly cites F5 for *affine* families `H(t)=A-tB`. It does not
show that the actual anisotropic transfer generator `-log T(P(t))` has
that form. Thus “the path changes the start, not that law” needs a
separate identification or a bound on the nonlinear remainder.
The sign of each proposed leg is only a belief; one must control every
leg on which a decrease has not been excluded. The anchor supplies the
initial lower bound even when the later differential inequality has a
different starting point.

**BR-6 correction.** A coarse marginal can discard a slowly varying
independent component entirely. Clustering of that marginal bounds only
the observables it retains. To compare lengths of the original model,
supply a local observable-recovery identity and bounds on its conditional
remainder, as well as an exact identification of the generated action.
The bare three-coordinate estimate does none of these. Replace the
claimed strength classification by “blocked; exact map and observable
transfer not supplied.” This is a missing implication, not a refutation
of a completed blocking theorem.

**BR-7 correction.** A common cylinder gap, together with suitable
local thermodynamic limits and uniform observable bounds, is sufficient
for a local infinite-volume gap. Infinite-volume local clustering alone
need not control finite-torus sectors. Replace “target-equivalent” by
“a sufficient family of estimates, converse not established.” On the
face this is a possible formulation of FACE-SG only after the same
sector and limit qualifications.

For BR-8 I checked `gap-cr-tomboulis-max.md` L320–347, L385–398 and
L806–819. Its DEC conclusion is T_flux at one coupling; FAC factorizes
the map and a twist in one group factor. Together with its named
massless-product input it cannot control the other factor's gap. This
supports the scope statement, not the missing TB inequality.

## 9. Source coverage

The entire 506-line row-1072 note and 71-line row-1073 reading were read.
The assigned S2 and gap-part ranges were read at the pinned checkout.
Source proofs were left unchanged. No registry, FINISH, status, audit or
other author's file was edited. Only this report is a repository output.

The Sussman–Alpoge index was used for each account object examined:

- Outline index chunk 01, neighbouring rows at L59–73 and L83–88,
  and obligations L14–30: outline L588–599 and L766–779 distinguish
  polynomial clustering and a block-constrained scalar gap from a physical
  spectral gap. These are explicit scope statements, not gap suppliers.
- Chunk 03, rows at L17–28 and L124–131, with obligations L90–105:
  outline L2773–2807, L2811–2818 and L2834–2860 supply the finite-torus
  positive-Gram/reflection construction used in section 3. L3712–3720
  explicitly leaves a gap above the invariant subspace unproved.
- The CA-I 4.12–4.19 README and targeted chunk search have no matching
  MON-T, MON-L, CA-FAIL or gap-transport entry. The nearby operation/small-
  coupling hit is chunk 05 L49–67. Its cited CA-I L48132–48147 and
  L48173–48188 concern a conditional operator theorem and operation scales,
  not coupling-path gap transport. No claim of exhaustive absence in the
  166711-line account is inferred from that search.

The main workflow map and its current rules/check procedure were read
through git because this checkout does not contain them. The user's
specified research output and verdict vocabulary govern this report;
no machine-readable standing record or audit workflow was run.

No numerical experiment, symbolic certificate, or Lean run was used.
All new calculations above are displayed hand arguments. FSS's theorem,
the face/anchor construction, and the previously named seed remain
explicit inputs at the scopes stated. The full FSS proof, the posted
2D O(4) proofs, the recalled Ising/duality literature, the historical
expansion-radius survey and Balaban's papers were not rechecked.
`pdftotext` was unavailable; PyMuPDF extracted the open FSS copy and
rendered its formula pages for visual checking. Those tools supplied
no mathematical proof step.

RESULT: MON-T, NO-MON, CONT and MON-L-cov FALSE HOLD; RP-ANI's consequence, C4–C5, CA-FAIL, the U(1) filter and the route table need the corrections above; the MON-L class refutation, LIN-perp and BR-6/BR-7 strength claims FAIL at their stated first lines. FSS's sufficient threshold is below 2 by a hand bound, and K3'/SLAB is prior work. BR-2 remains wounded and BR-3 blocked-stronger as corrected; no mass gap or status is claimed.
