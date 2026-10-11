# Campaign C4 / lane RD / probe D1 — independent referee

## VERDICT: CONFIRMED WITH CORRECTIONS

The fixed **FAIL (bounded)** survives, but the report must narrow several
statements.  Lemma K is sound for the concrete uniformly subsonic
rainbow/SCBA models after adding the missing domination and measure hypotheses;
abstract UI is stronger than pointwise finite residue.  The claimed elementary
one-dimensional Fermi-sea proof fails without a kinematic-overlap hypothesis.
The general Herglotz and all-`Z=0` shape claims remain conditional,
and RC B2 is closed only in the regular scalar parametrized subclass, not in
full generality.

## 1. Lemma K

**Core result: confirmed after explicit hypothesis repairs.**  Starting from
the displayed difference quotient, the limit is

\[
 \Sigma'_{\rm os,\pm}=A+B+E'_{\pm}\,\partial_\lambda\Sigma,
 \qquad
 (1-\partial_\lambda\Sigma)E'_{\pm}=\epsilon'_0+A+B.
\]

Thus the two sides agree when the right-hand data have the same trace and
`1 - partial_lambda Sigma` is finite and nonzero.  For a positive Stieltjes
weight independent of `lambda`, `partial_lambda Sigma=-K`, so
`Z=(1+K)^(-1)` and a differentiable local bare band cannot support a dressed
face kink.  No analyticity is used in this argument; Lipschitz regularity,
a.e. differentiability, stability, UI, and a simple finite-residue root are
enough.  This confirms the mechanism at `D1_report.md:68-84` and the
"no analyticity" sentence at `D1_report.md:88`, subject to the corrections
below.

- The hypotheses at `D1_report.md:60-64` do not quite imply the domination
  used at `D1_report.md:79-81`: the second term contains `w_0`, so one must
  assume `|w_0(xi)| <= C W(xi)` (or incorporate `|w_0|` into `W`).
- For a rainbow kernel, the Rademacher step at `D1_report.md:87` is correct if
  `E` is Lipschitz on `k_f-supp(q)` (normally the whole torus) and the
  momentum marginal of `mu` is absolutely continuous with respect to
  Lebesgue measure.  The stated assumption that `E` is Lipschitz only near
  `k_f` is insufficient for `E(k_f-q)` at arbitrary `q`.  With the corrected
  global/support-local condition, translation by `k_f` preserves the null
  nondifferentiability set, so `partial_k Omega=partial E(k_f-q)` exists for
  a.e. `q`.  A singular momentum measure could concentrate on that null set
  and is not covered.
- UI is **not abstractly equivalent** to `Z>0`.  Pointwise `K(k_f)<infinity`
  is equivalent to `Z(k_f)>0` for a positive `lambda`-independent pole
  weight, while UI is a neighborhood condition on an envelope.  In the
  concrete uniformly subsonic power-law class, the additional bounds
  `|D(k,q)| >= kappa|q|` and `W(q) <= C|q|^(2a)` give an integrable uniform
  majorant exactly when `d+2a>2`; necessity also needs two-sided weight and
  denominator scaling on a set of nonzero angular measure.  The one-sided
  upper bound written at `D1_report.md:87` proves sufficiency, not the claimed
  equivalence by itself.
- If `w` depends on `lambda`, `partial_lambda Sigma` also contains
  `integral (partial_lambda w)/D`; then `Z=(1+K)^(-1)` and positivity do not
  follow merely from `w>=0`.  Those identities are correct for the standard
  Stieltjes/Herglotz representation with `lambda`-independent measure, as the
  report partly acknowledges at `D1_report.md:49`.
- The Herglotz extension is acceptably labeled conditional at
  `D1_report.md:20,32,194-196`, but it is not a theorem for an arbitrary
  momentum-dependent Herglotz family.  Herglotz control is in the energy
  variable; a common Lipschitz continuum parametrization in momentum is an
  additional premise.  The zero-transfer Ward identity alone does not supply
  that global parametrization.  Accordingly `D1_report.md:90` must be read as
  closure only for the regular parametrized scalar subclass.

For a kinked bare band, the same calculation works with one-sided derivatives
and yields the jump law `J_E=Z J_epsilon0`; this is a straightforward extension
of the stated lemma, whose literal hypothesis instead makes `epsilon0`
differentiable.

## 2. Numerics

**Confirmed.**  I reran all five worker scripts.  They reproduce their saved
outputs, apart from harmless SciPy warnings caused by requesting tolerances
near machine precision in `d1_kink_1d.py:45-49` and
`d1_inverse_1d.py:67-71`.  I also used an independent midpoint rule in 1D, a
split Gauss--Legendre product rule in 2D, different `k`/`q` grids for the
inverse problem, and a local asymptotic calculation; see
`referee_d1_checks.py:43-147`.

- The 1D `n=2,3` laws give slope/`sK` = 0.999906 and 0.999945 at
  `delta=1e-4` (`referee_d1_checks.out:1-3`), agreeing with
  `d1_kink_1d.out:4-24`.
- The independent 2D value is `K=0.083295`, and slope/`sK` approaches one as
  `delta` falls from 0.02 to 0.005 (`referee_d1_checks.out:6-9`), consistent
  with the grid sequence at `d1_kink_2d.out:4-20`.
- The marginal fit gives `C=0.0691263` against the local coefficient
  `0.0691590` (`referee_d1_checks.out:4-5`); the worker's local-rate sequence
  reaches 0.069159 at `d1_kink_1d.out:26-37`.
- At the gapped quadratic touching, direct quadrature tends to
  `dSigma/sqrt(delta)=0.24404`.  Independently, near `q=pi+y`,
  `w=y^2/2` and `D=-(s delta+y^2)+o(delta+y^2)`, so the singular integral is
  `sqrt(s delta)/4`, with `sqrt(s)/4=0.244040`
  (`referee_d1_checks.out:10-14`; compare
  `d1_gapped_touch_1d.out:18-27`).
- The self-consistent finite-`Z` slope ratio is reproduced at
  `d1_selfconsistent_1d.out:3-9`.  The exact linearized mixed-iteration factor
  is 0.401797 (`referee_d1_checks.out:19-20`), matching the observed approach
  to 0.4010--0.4017 at `d1_selfconsistent_1d.out:11-22`.
- The marginal self-consistent data have successive
  `d(s0/s)/dlog(1/h)=0.05035,0.04891,0.04732,0.04602`
  (`referee_d1_checks.out:19-21`), confirming the reported trend at
  `d1_selfconsistent_1d.out:24-29`.  This is finite-size evidence consistent
  with logarithmic erasure, not by itself an asymptotic proof of the nonlinear
  continuum fixed point.
- The independent inverse-tail ratios 1.35636, 1.36322, 1.36565 approach
  `1+K=1.366775` (`referee_d1_checks.out:15-18`), confirming
  `d1_inverse_1d.out:9-15`.

## 3. Cusp catalogue and Fermi sea

**Partly confirmed; scope corrections are required.**

- The soft `q=0` threshold does not generate a new on-shell
  `k`-nonanalyticity when the band, mediator, and vertex are analytic in the
  relevant variables, the subsonic margin is uniform, and no other denominator
  zero occurs.  The cancellation is structural:
  `E(k)-E(k-q)=q integral_0^1 E'(k-tq)dt`, so the on-shell denominator and its
  `k` derivatives retain the same soft factor.  The exponential Fourier decay
  in the one tested analytic model (`d1_inverse_1d.out:17-20`) is a valid
  check, not proof of the unrestricted phrase "smooth subsonic point, any IR
  power" at `D1_report.md:119`.  A merely Lipschitz/smooth nonanalytic input,
  loss of a uniform subsonic margin, or another finite-`q` threshold is outside
  this conclusion.
- The marginal `+C delta log(1/delta)` sign and the particular gapped-touching
  `+C sqrt(delta)` sign/form are confirmed.  For a regular positive scalar
  soft weight, rescaling `q=delta x` gives the sub-marginal exponent
  `|delta|^(d+2a-1)`; in the 1D local model the coefficient is positive because
  moving inside the face increases every singular denominator's magnitude.
  An independent fractional-power test fits exponent 0.49669 against 0.5 with
  positive coefficient (`referee_d1_checks.out:24-25`).  This supports the
  conditional regular power-law catalogue, although the worker itself labeled
  it **SUGGESTED** at `D1_report.md:122,198-202`, and the synthetic fractional
  weight is not an ordinary finite-range trigonometric vertex.  Self-consistent
  erasure was still not established for every `Z=0` model.  The fixed reading
  does not need that universal claim: `Z=0` already fails its residue clause.
- For a regular `d>=2` Lindhard sea, the claim is correct after stating the
  usual hypotheses.  Small-`q` particle-hole support reaches zero on an open
  set of directions; for any nonzero matter velocity one can choose directions
  with an allowed positive energy transfer.  A nonzero analytic vertex cannot
  vanish on that entire open set.  This is a statement about a regular Fermi
  surface and generic/nonzero coupling, not every possible "Fermi sea."
- The `d=1` assertion at `D1_report.md:126,183` is **not proved by the stated
  elementary/Lindhard argument**.  Low-energy `2k_F` pairs do not ensure energy
  conservation with the matter loss.  For the nonempty lattice sea
  `epsilon_f(p)=2t(1-cos p)`, `t=0.001`, `k_F=0.1`, every particle-hole energy
  at transfer `Q` is at most `min(4t,2t|Q|)`, whereas the SLAC-face loss
  `E(pi)-E(pi-|Q|)` is strictly larger for every `0<|Q|<=pi`.  The direct scan
  has positive minimum margin (`referee_d1_checks.py:150-165`;
  `referee_d1_checks.out:22-23`).  This is a counterexample to the claimed
  universal **single-pair** decay kinematics, not a construction of an exact
  all-orders quasiparticle: a 1D no-band result would instead need an explicit
  overlap hypothesis or a separate multipair/orthogonality-catastrophe proof.

## 4. Inverse problem and non-locality

**Confirmed in the finite-residue class.**  Taking the jump of the corrected
slope identity gives

\[
 J_{\epsilon_0}=(1-\partial_\lambda\Sigma)J_E=J_E/Z.
\]

For a `lambda`-independent positive pole weight this is
`J_epsilon0=(1+K)J_E`.  A continuous periodic function with the SLAC endpoint
derivative jump consequently has
`t_r ~ (-1)^r s(1+K)/(pi r^2)`, so it cannot be nearest-neighbor, finite-range,
or exponentially local.  The independent tail calculation confirms the
coefficient (`referee_d1_checks.out:15-18`).  This validates
`D1_report.md:143-149` for finite `Z`.

Two qualifications: the literal Lemma K must be extended to one-sided bare
derivatives before applying it to a kinked `epsilon0`, and the formula
`J_epsilon0=J_E/Z` is not meaningful at `Z=0`.  In the checked marginal and
gapped-touching `Z=0` examples, the inverse bare dispersion must cancel a
stronger logarithmic or square-root nonanalyticity and is again non-local, but
`D1_report.md:143-155` has not proved the same detailed conclusion for every
possible mediator or non-UI parametrization.

## 5. Scope

**RC B2 is only partly closed.**  B2 left threshold contact and gapless
momentum nonanalyticity open (`RC_C1_report.md:168-184` and
`RC_C1_referee_full.md:15`).  Corrected Lemma K closes the scalar,
finite-residue, regularly parametrized rainbow/SCBA subclass, both for a
uniformly subsonic gapless threshold and for a regular gapped continuum that
touches at the face.  If the positive pole integral diverges, the residue is
zero and the fixed PASS criterion is already missed; the supplied models also
show the wrong cusp forms.  This does **not** close an arbitrary
momentum-dependent Herglotz family, a singular continuum parametrization, a
sonic/non-Lipschitz vertex, or every possible `Z=0` touching theory.

Leaving the dressed symmetry-protected two-band face crossing open is correct
(`D1_report.md:157-164,204`).  Such a crossing is a multiple matrix root; the
scalar simple-root transfer argument does not exclude it, and the interaction
selection-rule/partner-band issue was already open at
`RC_C1_report.md:186,196-202`.

## 6. Fixed verdict

The fixed criterion is `TESTS.md:1324-1327`.  The corrected finite-residue
theorem proves that a local differentiable scalar bare band in the stated
uniformly subsonic rainbow/SCBA class cannot acquire an exact SLAC face cusp.
The marginal and gapped-touching checks instead have `Z=0` and the displayed
non-SLAC singularities.  That is enough for **FAIL (bounded)** even after
removing the unsupported universal 1D Fermi-sea proof and all-`Z=0` claims.  The
proper referee verdict is therefore **CONFIRMED WITH CORRECTIONS**, not
unqualified confirmation.

## Strongest correct statement

For a single scalar band with a differentiable periodic finite-range bare dispersion and a stable rainbow/SCBA self-energy whose momentum measure is absolutely continuous, whose dressed intermediate band and vertex admit the stated a.e.-differentiable Lipschitz bounds, and whose soft denominator is uniformly subsonic with the required UI, the face-slope jump obeys `J_E=Z J_epsilon0`; hence a local bare band has no dressed face cusp at finite nonzero residue.  In the concrete power-law models, `d+2a>2` supplies this UI under two-sided regular scaling, while the marginal gapless model and the tested quadratic gapped touching have `Z=0` and respectively `+C delta log(1/delta)` and `+C sqrt(delta)` behavior, not the SLAC cusp.  Conversely, imposing an exact SLAC target at finite residue forces a bare `1/r^2` hopping tail amplified by `1/Z`.  The same conclusion extends only conditionally to Herglotz families with a common Lipschitz momentum parametrization; generic regular `d>=2` Lindhard seas damp a moving band, but the stated elementary `d=1` Lindhard argument does not establish the all-orders no-band claim.  Singular/non-UI or sonic vertices, arbitrary momentum-dependent Herglotz measures, universal sub-marginal and `Z=0` shape claims, the general 1D Fermi-sea problem, and dressed symmetry-protected two-band crossings remain open.  Under the fixed reading, this establishes **FAIL bounded to the corrected scalar rainbow/SCBA and parametrized finite-residue classes**.
