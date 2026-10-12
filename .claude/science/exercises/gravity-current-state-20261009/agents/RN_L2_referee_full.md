# Lane RN probe L2 — independent referee report

## VERDICT: NOT CONFIRMED

The worker's central scalar collision obstruction is substantially correct in a
narrower class, and the displayed finite-basis and vacuum-Hessian numbers
reproduce.  The registered bounded **FAIL**, however, does not follow.  The
collision condition is a necessary asymptotic condition, not an equivalence;
the report overextends it to degenerate matrix charges.  More decisively, it
does not complete the Dirac algorithm, its five-degree-of-freedom count is
incompatible with the supplied `H_N` constraint chain, and its own off-shell
dressing caveat leaves the purported untuned vacuum mass unforced.  L3 was not
run.  Under the FIXED reading at `TESTS.md:819-824`, L2 is therefore
**INCONCLUSIVE**.

### Checks performed

- Read the FIXED setting and reading (`TESTS.md:790-824`), the full worker
  report, all three supplied runners/outputs, the K3a/K3a'/K3a2 referee reports,
  the 09-14 `H_N` note, `R2_referee.md`, and the axiom memo.
- Recompiled and fully reran `l2_collision_invariants.py`,
  `l2_sunset_mu.py 1.0`, and `l2_xxz_passer.py`; the supplied outputs reproduce.
- Ran fresh-seed finite-basis SVDs, an exact exceptional-branch collision
  check, the free scalar constraint-chain check, and a larger-volume sunset
  check in `l2_referee_checks.py:18-85`; results are in
  `l2_referee_checks.out:1-17`.
- Compared the collision-invariant claim with [Spohn's scalar theorem](https://arxiv.org/html/math-ph/0605069v1),
  [Lukkarinen's phonon-kinetic review](https://arxiv.org/abs/1509.06036), and the
  [matrix-valued Hubbard-chain analysis](https://arxiv.org/abs/1207.6926).

## Findings

### 1. Reduction to collision invariants — necessary, not equivalent

**Finding: confirmed as a necessary obstruction, with major scope corrections.**

For a number-conserving short-range law, a conserved translation-invariant
charge whose connected dressing clusters at large particle separation acts on
two asymptotic particles by the sum of its one-particle symbols.  Conservation
then makes this asymptotic action commute with the two-body S-matrix, yielding

\[
f_A(k_1)+f_B(k_2)=f_A(k_3)+f_B(k_4)
\]

where the on-shell scattering amplitude is nonzero.  Thus the argument at
`L2_report.md:28-37` is a valid **necessary** test, exact in finite nonzero
`U` on regular contact-scattering shells.  It is not equivalent to
`[H,P]=0`: a collision invariant need not lift to a local charge, satisfy the
higher-particle equations, or admit the symmetric local current required by
the gravity coupling.

The range and body order of a regular connected dressing cannot repair a
failed asymptotic one-particle condition: two-body dressing vanishes at large
relative separation and body order at least three vanishes in the two-particle
sector (`L2_report.md:30-32`).  That makes them irrelevant to this necessary
obstruction, not to existence of arbitrary conserved operators.  In
particular, a charge with zero one-particle action is not excluded; it simply
cannot be the required momentum acting on a single particle.  The report needs
this nonzero IR one-particle normalization as a stated hypothesis.

The scalar equation does not close the matrix loophole claimed at
`L2_report.md:21-24,43`.  In a degenerate band/taste space the condition is an
intertwining equation involving the full matrix S-matrix, not one scalar `f`
per preassigned band.  This is exactly material for staggered tastes, which the
report later admits were not checked (`L2_report.md:160,181`).

Non-number-diagonal additions are not a rescue for the ordinary Hubbard/contact
models if the desired momentum has a neutral one-particle action: averaging a
conserved local `P` over the exact U(1) symmetry preserves locality and
conservation and retains that neutral one-particle component.  But this is a
scope reduction, not proof about every charged or spectrum-degenerate conserved
operator.  The claim that the contact `T` is nonzero on *every* shell
(`L2_report.md:37`) must also exclude `U=0`, thresholds, divergent resolvents,
and collapsed relative bands; an almost-everywhere regular-shell statement is
sufficient in `d>=2`.

For onsite phi-four, the O(lambda) projection is sound for a regular family
analytic in lambda.  Between resonant free two-particle states,
`[H2,P4]` is the energy difference times the bounded dressing kernel and
vanishes, while the nonzero Born vertex in `[H4,P2]` forces the same scalar
collision identity (`L2_report.md:38-42`).  It does not cover singular
resonance-supported kernels, nonanalytic-in-lambda charges, or nonperturbative
phi-four.

### 2. Lemma L2-A and the kinetic literature

**Finding: the scalar conclusion is correct for the named massive nearest-neighbor bands; the supplied C1 proof is incomplete and the operator-level wording is too broad.**

[Spohn's proposition](https://arxiv.org/html/math-ph/0605069v1) is stronger for
a single scalar band: in `d>=2`, under C2 regularity away from allowed singular
sets and generic Hessian nondegeneracy, every periodic integrable pair-collision
invariant is `a omega + c`.  Massive nearest-neighbor lattice KG satisfies the
condition (its analytic Hessian determinant is nonzero at `k=0`), and shifted
nearest-neighbor tight binding has Hessian determinant proportional to the
product of the cosines.  Both therefore have no odd scalar invariant.  The
intermediate affine `b dot k` term is killed by periodicity.  Consequently the
literature supplies **constants and energy only**, not a real additive
crystal-momentum-like invariant.  Crystal momentum modulo a reciprocal vector
is group-valued; its sawtooth lift is not a collision invariant once umklapp is
included.  Lukkarinen's review emphasizes that special one-dimensional
collision geometries require separate treatment rather than contradicting
this `d>=2` result.

The sketch at `L2_report.md:56-61` nevertheless differentiates the C1 function
a second time and differentiates the shell quotient without proving the needed
regularity (`L2_report.md:59-60`).  A weak-derivative/local-coordinate argument
can repair it, and the connected-level/nonconstant-gradient hypotheses must be
verified rather than inferred merely from dependence on `sum cos(k_i)`
(`L2_report.md:50-52`).  The conclusion is credible for the stated scalar KG/TB
bands, including the unequal-mass scalar pair after that repair; it is not a
theorem about unrestricted operator- or matrix-valued charges.

If the one-particle kernel obeys
`sum_r (1+|r|)|p_r| < infinity`, its Fourier series can be differentiated
uniformly and is C1.  This covers finite range and exponential quasi-locality,
as claimed at `L2_report.md:54`, provided the many-body quasi-local norm
actually implies that weighted bound (including support-size factors).  Bare
ell-one decay alone gives continuity, not necessarily C1.  Also, “small total
momentum” at `L2_report.md:64` does not mean that both particles are low energy;
the proof uses relative momenta throughout the Brillouin zone.

### 3. Null-space numerics

**Finding: the d>=2 finite-basis result is robust; the 1D control and the word “exact” are wrong.**

The complete worker run reproduces.  In the supplied maximal-range cases the
smallest/largest odd singular-value ratios are order one, at least 0.492
(`l2_collision_invariants.out:20-61`).  With a fresh seed and matrices divided
by `sqrt(N)`, I obtain smallest singular values 0.982 (2D TB, R=8), 0.897 (3D
KG, R=4), and 0.539 (3D unequal-mass KG, R=4), versus largest values 1.41-1.81
(`l2_referee_checks.out:9-11`).  These gaps are nowhere near any plausible
roundoff threshold.  Valid sampled rows are sufficient to exclude an exact
null vector in each tested Fourier space, even though the collision sampling
measure is not uniform.

The nullity implementation uses only `sv < 1e-9*sv[0]`
(`l2_collision_invariants.py:77-79`).  For the 1D TB control the whole design
matrix is roundoff, so this relative-only rule reports nullity zero.  At R=8
the singular values are only `1.01e-14` to `2.53e-13`: an absolute `1e-10`
floor gives nullity eight (`l2_referee_checks.out:5-8`).  The displayed defects
near `1e-15` already reveal the problem (`l2_collision_invariants.out:11-17`).

More importantly, `L2_report.md:69-70,85` is false as collision geometry.  For
the 1D cosine band and total momentum `K=pi`,

\[
\epsilon(k)+\epsilon(\pi-k)=0
\]

for every `k`, so `(k,pi-k)->(q,pi-q)` is a non-permutation resonant branch.
`sin(k)` fails it while `sin(2k)` passes; the explicit residuals are in
`l2_referee_checks.out:1-4`.  The continuous random sampler chooses `K` at
`l2_collision_invariants.py:34-41` and misses the codimension-one value
`K=pi` almost surely.  The exact-U T-matrix on this collapsed relative band is
singular and needs separate analysis, so this correction does not by itself
disprove the integrable 1D Hubbard charge.  It does disprove “only trivial
resonances/every f.”  The Hubbard-chain kinetic literature instead finds
infinitely many special additional invariants, not arbitrary `f`.

The TB even-energy control is right because its energy is in the cosine basis
(`L2_report.md:86`).  KG energy is not a finite trigonometric polynomial, so
its absence from a finite-R exact null space would not be a failed control.
Overall these are well-conditioned **sampled numerical finite-basis** null
spaces, not “exact linear algebra” over all collisions or all smooth symbols.

### 4. Quasi-local decay

**Finding: “not extrapolable” is correct, with two further corrections.**

The tables contain no coefficient-tail bound, uniform collision norm, held-out
sample, infinite-R compactness result, or model selecting an asymptotic form.
They prove neither a positive defect floor nor convergence to an exact
quasi-local charge, so `L2_report.md:97` is the right reading.

The purported condition `f=k` on the low-energy ball is actually a weighted
least-squares penalty of weight 1000 (`l2_collision_invariants.py:99-109`), with
nonzero IR residuals around `1e-3` (`l2_collision_invariants.out:20-61`).  Exact
agreement with `k` on an open ball would itself be incompatible with a globally
analytic periodic symbol by analytic continuation.  It should be described as
a controlled approximation.  The claimed initial 2D local exponent “about
1.5” (`L2_report.md:95`) is also not obtained from the listed data: consecutive
KG exponents are approximately 0.95, 0.52, 0.69, and 0.48.

### 5. Constraint class and degree-of-freedom count

**Finding: failure of the proposed first-class closure is supported; “becomes second class,” overconstraint, and five degrees of freedom are not established.**

A nonzero local Ward defect shows that the proposed shift constraint is not
preserved as the claimed first-class generator (`L2_report.md:109`).  The full
Dirac consistency equation, however, contains both the Hamiltonian defect and
the constraint-bracket matrix.  Depending on its rank it can create further
constraints, determine multipliers, expose an inconsistency, or finish in a
mixed first-/second-class set.  No bracket matrix or rank calculation is given
at `L2_report.md:109-113`.  Therefore `R_i approximately 0`, “no interacting
matter,” and “second class” do not follow as a completed classification merely
from nonconservation.  The standard algorithm explicitly distinguishes these
possibilities; see [Brown's worked Dirac-Bergmann analysis](https://arxiv.org/abs/2201.06558).
Exact local energy continuity at `L2_report.md:103-105` is likewise necessary
but not by itself a proof of the full lapse/shift constraint algebra.

The five-DOF subtraction at `L2_report.md:111-113` assumes the scalar constraint
remains a lone first-class constraint after the vector constraints are deleted.
But the supplied `H_N` note states that its momentum term is scalar-gauge
invariant only on `G=0`
(`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:72-76`).
For `k` along z, its scalar kinetic block has
`dot(h_t)=-J E_z/sqrt(2)` (same note, `:262-266`), so preservation of
`S proportional to h_t=0` generates `E_z=0` even in the free theory.  The
independent spot check is `l2_referee_checks.out:12-14`.  Thus `(12-2)/2=5` is
not a completed Dirac count.  Moreover vector-longitudinal momenta still enter
the DeWitt kinetic form, so “their dynamics come only from the matter defect”
is unsupported.  The report admits that no extra-mode dispersion was computed
(`L2_report.md:179-183`).

### 6. O(lambda^2) TT Hessians

**Finding: the stated tadpole-subtracted numbers and signs are confirmed for the chosen design; a forced untuned graviton mass is not.**

The Wick factors in `l2_sunset_mu.py:97-100` are correct.  Four propagators
joining the vertices give 24 contractions and `-lambda^2 I4/24`; the
two-joining-line/tadpole graph gives `-lambda^2 G^2 I2/8`.  The FFT normalization
and time integral are consistent (`l2_sunset_mu.py:73-85`), and the symmetric
Richardson Hessian is implemented at `:87-95`.  “Basketball vacuum graph” is a
less ambiguous name than “sunset,” which commonly names the associated
self-energy graph.

At `m=1`, an independent `L=48`, `epsilon=0.04` run gives

- `mu_E/lambda^2 = -1.0093124995e-6`,
- `mu_T2/lambda^2 = +1.6108165587e-8`,

for the retained I4 term (`l2_referee_checks.out:15-17`).  This confirms
`L2_report.md:131-140`, including the opposite signs.  The original low-mass
`L<=32` sequence is less converged (`l2_sunset_mu_m0.3.out:2-7`), but larger
volumes recover the quoted approximate `-3.06e-6` and `+6.9e-8` values.

These are not the full bare onsite-phi-four Hessians.  At `m=1` the omitted I2
piece changes the E-channel result to `-8.46297e-5 lambda^2`, while the T2 I2
piece vanishes in the infinite-volume limit (`l2_sunset_mu_m1.out:2-7` and
`l2_referee_checks.out:16-17`).  Dropping it is consistent only after explicitly
adopting the tadpole-subtracted/renormalized-mass design at
`L2_report.md:128-129`.

The free contribution vanishes **exactly within the chosen nonlinear
completion** because `H2(h)=U_h H2 U_h dagger` is isospectral
(`L2_report.md:118-122`).  That completion supplies all quadratic and higher
seagulls; it is additional design data beyond the explicitly linear
`h_ij T_ij/2` coupling registered at `TESTS.md:792`.  An exact free stress alone
does not uniquely select it.

The quoted `mu` is a per-cell Hessian along two strain matrices of equal norm
squared two (`L2_report.md:127`), not yet a canonically normalized graviton
mass squared.  A graviton kinetic normalization and a justified identification
of this Hessian with its zero-momentum inverse propagator are needed for
“tachyonic” and the `10^98` comparison (`L2_report.md:145-147`).  The approved
scale-reference primitive can supply the units conversion `a^-1=M_Pl`, but it
does not supply this dynamical identification or prove the lattice/Planck
self-consistency.  The arithmetic benchmark
`1/[24(16 pi^2)^2]=1.67e-6` is correct, but its designation as a universal
natural three-loop coefficient is heuristic and regulator/convention dependent.

The dressing caveat at `L2_report.md:149` is real and load-bearing.  In the
massive vacuum `0<->4` sector, `sum omega >= 4m`, so the denominator has no
on-shell zero and an analytic, exponentially local O(lambda) kernel can cancel
that off-shell defect without cancelling the obstructed resonant `2->2`
matrix elements.  The report does not construct and verify the full dressed
coupling, so cancellation is not established; but the open route is enough to
prevent the computed vacuum Hessian from being called forced or untuned.

### 7. XXZ control

**Finding: the conserved local charge is confirmed, with normalization and scope corrections.**

The full ED rerun reproduces `l2_xxz_passer.out:1-5`.  For nearest-neighbor XXZ,
the sum of adjacent bond commutators commutes with `H`, and its one-magnon
symbol divided by `i` is `-16 Delta sin(k)+8 sin(2k)`, with slope
`16(1-Delta)`.  This is consistent with the known conserved energy current in
[Zotos, Naef, and Prelovsek](https://arxiv.org/abs/cond-mat/9611007).  As coded,
`Q3` is anti-Hermitian because it is a commutator of Hermitian bonds
(`l2_xxz_passer.py:15-19`); the physical Hermitian charge is `-i Q3`.  It has
the desired nonzero slope only for `Delta != 1` (`L2_report.md:153-154`).

Adding next-nearest-neighbor ZZ gives the reproduced relative commutator 0.849,
which destroys **this** charge, not every possible odd local charge
(`l2_xxz_passer.out:3`).  The result is a useful 1D integrability control, not
an RN PASS: it does not establish a 3D exact constraint algebra, two-species
universality of `G`, vanishing TT Hessians, or `gamma=1`, all required at
`TESTS.md:814-818`.  Nor does scalar KG/TB Lemma L2-A by dimensionality alone
exclude all possible higher-dimensional integrable/matrix constructions, as
claimed at `L2_report.md:156`.

### 8. Fixed-reading verdict and remaining loopholes

**Finding: the registered result is INCONCLUSIVE, not a bounded FAIL.**

The FIXED FAIL is conjunctive: no stress in the stated class **and** either the
specified second-class consequence with a natural-size untuned TT mass/extra
mode, or an L3 escape failing an observational bar (`TESTS.md:819-824`).  The
report's strongest no-stress result is the normalized scalar one-particle
contact-scattering obstruction described above.  But the completed constraint
class/rank and extra spectrum are not computed, the vacuum mass is coupling-
and-dressing-dependent by the report's own caveat (`L2_report.md:149`), and L3
is explicitly not done (`L2_report.md:179-184`).  The second conjunct is absent.

The surviving routes must remain explicit:

- staggered/taste-degenerate matrix `f` and full matrix scattering;
- gauge-mediated interactions, whose massless asymptotics, soft sectors and
  matrix/polarization structure are not the scalar rank-one contact problem;
- nonperturbative or nonanalytic-in-lambda phi-four charges/couplings;
- interactions with zero two-body or zero low-energy scattering on the shells
  needed by the lemma, including higher-body-leading laws;
- strongly correlated/integrable constructions outside scalar KG/TB bands;
- alternative completions of the gravitational matter coupling, including the
  explicit off-shell dressing route;
- the smooth momentum-space-cutoff construction at `L2_report.md:161-164`.
  Its super-algebraic but non-exponential real-space tails put it outside the
  registered local/exponentially quasi-local PASS and conflict with the fixed
  nearest-neighbor Admissibility rule (`MINIMAL_AXIOMS_2026-06-29.md:55-61`),
  but it prevents any broader claim about arbitrary summably nonlocal laws.

## No-go scope stress test

- **N1:** scalar contact, higher-body dressing, non-number-diagonal additions,
  matrix/taste charges, gauge mediation, nonperturbative phi-four, vanishing
  scattering, nonanalytic cutoff interactions, and integrable charges were
  separated.  The first three are narrowed as above; the latter six are not
  all ruled out.
- **N2:** the no-stress lemma and the TT-mass/extra-mode consequence are not
  independent completed walls; the latter is a required downstream leg and is
  open.
- **N3:** hidden assumptions are asymptotic completeness/clustering, nonzero
  scalar IR one-particle action, regular shells, analytic perturbation in
  lambda, a selected nonlinear metric completion, and tadpole subtraction.
- **N4:** K3a's finite-class obstruction matches the scalar collision residual,
  while K3a2's fixed-coupling shear response does not prove a universal mass;
  their referee boundaries (`K_K3a_referee.md:11-18` and
  `K_K3a2_referee.md:15-20`) agree with this narrowing.
- **N5:** finite Fourier spaces, scalar one-particle symbols, asymptotic
  two-particle states, and vacuum Hessians were tested; unrestricted matrix,
  many-particle, finite-density, and full constraint resolutions were not.
- **N6:** the momentum-cutoff model is a genuine partial closure outside the
  registered locality class; the off-shell dressing is an in-class candidate
  closure of the vacuum-mass leg, not a new axiom.
- **N7:** the strongest case for FAIL is Spohn's scalar theorem plus the exact-U
  contact reduction and the reproduced O(lambda^2) Hessian.  It still does not
  complete the fixed consequence leg because the Hessian is design-dependent
  and the Dirac count is unfinished.
- **N8:** the prior K3a and R2 referees already left matrix/quasi-local,
  nonlinear-coupling, and exact weak-N-type matter bridges open
  (`K_K3a_referee.md:11-18`; `R2_referee.md:40-46`).  L2 closes the scalar
  contact subset, not those echoed routes.

## Strongest correct statement

For `d>=2`, massive nearest-neighbor lattice Klein-Gordon and nearest-neighbor scalar tight-binding bands have no nonzero odd periodic C1 scalar invariant of their full regular, nonvanishing-contact `2<->2` collision relation; hence a local or exponentially quasi-local conserved charge with a regular, nonzero scalar one-particle momentum action cannot be rescued by arbitrary-range connected higher-body dressing, exactly in finite nonzero contact `U` on regular shells and at O(lambda) for an analytic onsite-phi-four family.  The sampled finite Fourier null spaces robustly support this obstruction, the selected tadpole-subtracted free-level coupling has reproducible opposite-sign Hessians `mu_E/lambda^2=-1.0093e-6` and `mu_T2/lambda^2=+1.6108e-8`, and nearest-neighbor 1D XXZ supplies a conserved odd local control.  These results do not cover degenerate matrix charges, all gauge-mediated or nonperturbative laws, interactions without the required scattering, or all gravitational coupling completions; nor do they establish a completed second-class Dirac system, a natural-size untuned physical TT mass, or an extra propagating mode.  Therefore the strongest supported reading under the unchanged FIXED criteria is **INCONCLUSIVE**, not bounded FAIL.
