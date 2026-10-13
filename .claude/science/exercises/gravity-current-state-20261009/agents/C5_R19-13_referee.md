# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed **NO-LOCAL-ESCAPE** reading is met in the stated free-field,
plane-insertion, completed-law scope.  The lower-bound theorem and monotonicity
are sound, and an independent direct quadrature confirms the massless-scalar
bound by enormous margins.  Three qualifications are material: the reported
`R^-4.87 -> R^-5` curve is the best *found Gaussian isometry* (an upper bound),
not the proved optimum over all channels; the `1.7e23 a` radius is a controlled
continuum-asymptotic extrapolation rather than the proved finite-lattice bound;
and the photon statement remains conditional on the unbuilt two-transverse-
scalar/Gauss-law identification.

## Per-item findings

1. **Lower-bound chain: confirmed, with a fidelity-convention and scope
   correction.**  On a finite transverse torus, let `p0=<g|rho|g>` for the
   new chain ground state and use squared fidelity `F_sq`.  The precise chain
   is

   `Delta E_q >= M_q(1-p0) >= M_q[1-F_sq(rho_T,sigma_T)] >= M_q D(rho_T,sigma_T)^2 >= M_q |Delta<O>|^2/4`.

   The first step is the spectral-gap inequality; the second is monotonicity
   of fidelity under partial trace; the third is Fuchs--van de Graaf; and the
   last follows from `|Tr O(rho-sigma)| <= 2D` for `||O||<=1`.  If `F` denotes
   the unsquared root fidelity, the report's literal `1-F` form must instead
   be `1-F^2`.  The cosine witness is valid: for
   `O=cos(lambda(phi_L-phi_R))`, `||O||<=1`, and the two Gaussian boundary
   marginals give `exp(-lambda^2 a)` and `exp(-lambda^2 b)`, optimized at
   `lambda^2=log(b/a)/(b-a)`.  The worker implements this formula at
   `r1913_analysis.py:79-87`, corresponding to `R19-13_report.md:96-102`.

   The two untouched boundary planes really are fixed for every deterministic
   trace-preserving slab channel: in the Heisenberg picture
   `E_S^dagger(I)=I`, so the complete complement marginal, including the joint
   state of the two planes, is unchanged.  This remains true with locally
   initialized ancillas and arbitrary non-Gaussian channels.  The reason is
   no-signalling/trace preservation, not that the operation “cannot change
   their separation.”  It does not cover postselection, an ancilla already
   entangled with the far region, or anticipatory preparation outside the
   slab.  Those exclusions agree with the disclosed scope at
   `R19-13_report.md:203-217`.

2. **Monotonicity: confirmed for the optimized energy, not automatically for
   every derived product.**  The admissible radius-`R` maps are a subset of
   the radius-`R+1` maps (the larger map can act trivially on the added shell),
   hence the infimum `Delta E_min(R)` is non-increasing.  Therefore a valid
   lower bound at `R_*` above an energy threshold excludes every `R<=R_*`, as
   claimed at `R19-13_report.md:103`.  This does not say that a numerical
   optimizer, an interpolated lower-bound estimate, or
   `Delta E_min(R) tau_ins(R)` must itself be monotone.  The registered
   product needs its own time lower bound (for a nearest-neighbour circuit,
   `tau_ins/a >= depth >= R`) or a direct check of `R LB(R)`.

3. **Independent massless-scalar recomputation: confirmed, with a 0.29%
   numerical correction; scaling claims narrowed.**  I evaluated
   `G(0)-G(d)` and `G(0)-G(d+1)` directly, without importing `r1913_lib` or
   interpolating the worker's mass table (`referee_r1913_check.py:23-82`).  At
   `R=32`, the result converges to
   `LB=1.2785785769e-13`; changing the transverse quadrature from 80 to 100
   points changes it by `1.3e-11` relatively, and doubling the longitudinal
   quadrature changes only the last displayed digits
   (`referee_r1913_check.out:1-7`).  This is 0.290% below the worker's
   `1.2823e-13`, consistent with the fact that its log-mass interpolation and
   midpoint Brillouin-zone sum are not certified lower interpolation rules
   (`r1913_analysis.py:93-100`).  The discrepancy is immaterial: the direct
   value is `3.38e110` times the persistent threshold and `3.98e49` times the
   registered `tau=1` threshold (`referee_r1913_check.out:8-11`).  An extra
   direct run gives `LB(256)=2.2807043e-18`
   (`referee_r1913_check.out:12-14`), independently securing the scalar
   endpoint used below.

   The reported `2.159e-11` at `R=32` and exponent `-4.869` are correctly
   reproduced for the optimized Gaussian construction
   (`r1913_analysis.out:5,9-11`), but that construction is only an upper bound
   on the all-channel optimum (`R19-13_report.md:83-88`).  Thus the defensible
   statement is that the computed Gaussian cost is consistent with `R^-5`
   up to slow factors, while the rigorous witness supplies a much smaller
   lower bound; it is not an exact determination of the “best cost.”  For a
   massive scalar, `kappa=arccosh(1+m^2/2)` is the correct nearest complex-
   momentum decay constant and `exp(-4 kappa R)` is the leading exponential
   expected after squaring a separation-`2R+1` correlation, but polynomial
   prefactors remain.  The `m=1` optimized data hit the numerical floor before
   the ratio approaches `exp(4 kappa)=46.98`
   (`r1913_analysis.out:8,12-13`), so this is an asymptotic mechanism, not a
   numerically established exact law for the global optimum.  “Dirac:
   similar” is likewise numerical/expected, not a proved universal formula.

4. **Threshold: the fixed probe registers `Delta E tau_ins`, while the
   excitation-left-behind threshold is a distinct conditional reading.**
   `TESTS.md:7721-7723` explicitly asks whether
   `3H Delta E(R) tau_ins/a^3 < rho_Lambda`, so the threshold governing the
   fixed R19-13 reading is
   `Delta E tau_ins < 3.209e-63`.  For a causal nearest-neighbour realization,
   the minimal scaling is `tau_ins >= R` in lattice units.  The report's
   separate persistent-deposit comparison is
   `Delta E < rho_Lambda/3 = 3.779e-124`
   (`R19-13_report.md:110-117`).

   R19-10's referee correctly warns that these are different observables:
   completed-law storage `A_fix` is not net excitation after insertion and is
   not excitation above the instantaneous `H(t)` ground state
   (`C5_R19-10_referee_verdict.md:15-32`).  The axioms choose neither a
   Hamiltonian nor insertion dynamics (`MINIMAL_AXIOMS_2026-06-29.md:114-130`),
   so neither accounting is an axiom-level physical identification.  R17-7
   does not fix that choice: its energy subtraction is explicitly conditional
   on using the same supplied Hamiltonian for `V` and `e0`, and its referee
   calls the map from a preferred-time lattice `H` to `e0` stipulated rather
   than locally derived (`C5_R17-7_referee_verdict.md:7-12,52-58`).  Under the
   persistent reading, the continuum-asymptotic scalar result is
   `R>1.66e23 a`; under the registered reading it is `R>1.43e11 a` for the
   artificial `tau=1` choice and `R>7.91e13 a` for the causal `tau=R` choice
   (`r1913_analysis.out:40-44`).  All three are asymptotic evaluations, not
   the finite-lattice theorem.  Under either accounting the theorem-backed
   finite-radius bound already excludes `R<=10` by scores of orders of
   magnitude.

5. **Fixed reading: met, but only as the scoped model theorem.**
   `TESTS.md:7739-7743` requires a refereed demonstration that the necessary
   radius exceeds a stated bound; the example `1e30 a` is illustrative, not
   a required target.  The analytic part that is proved is the all-CPTP
   lower-bound inequality plus monotonicity.  With direct lattice evaluation,
   the massless scalar has `LB(256)=2.2807043e-18`, above both thresholds even
   at `tau=1`; therefore **`R>256 a` is the confirmed theorem-backed numerical
   bound for the massless scalar**.  This is enough to exclude the fixed
   `R<=10 a` escape.  The worker's analogous evaluated bounds `R>512 a` for
   massless Wilson--Dirac, `R>12 a` for the massive scalar, and `R>16 a` for
   massive Wilson--Dirac are consistent with its stored calculations
   (`r1913_dirac_summary.out:17-19`; `r1913_lb_m1.out:1-10`), but were not needed
   for the reading and were not independently recomputed here.  The
   `R>1.7e23 a` scalar figure is a checked continuum asymptotic, not the bound
   proved by the finite computation (`R19-13_report.md:220-223`).

   The no-go does not extend to every notion of site creation.  The proof does
   close non-Gaussian slab channels, local ancillas, transverse-mode mixing,
   and tuning of the birth isometry.  It does not close at least five distinct
   alternatives: anticipatory correlations prepared outside the slab,
   instantaneous-law rather than completed-law energy, interacting or
   commuting-projector laws, point/ball defect geometry, and a genuine gauge-
   constrained photon insertion.  The report itself lists these boundaries at
   `R19-13_report.md:201-217`; in particular the photon is only a suggested
   two-scalar identification (`R19-13_report.md:162`).  Also, the scalar
   oscillator is not the axiom's one-site `M_2(C)` system
   (`MINIMAL_AXIOMS_2026-06-29.md:43-53`).  Thus “NO-LOCAL-ESCAPE” is confirmed
   as the fixed probe label in its stated model class, not as an axiom-derived
   universal no-go for photons, gravitons, interacting matter, or arbitrary
   growth laws.

## Strongest correct statement

For the nearest-neighbour free scalar under plane insertion, with the old lattice initially in its ground state and energy measured against the completed new Hamiltonian, every deterministic CPTP operation supported on a radius-`R` slab—including arbitrary locally initialized ancillas and non-Gaussian operations—leaves the two exterior boundary planes' joint marginal unchanged and therefore obeys the spectral-gap/fidelity/trace-distance/cosine-witness lower bound; the optimal excess energy is non-increasing with `R`.  Independent direct quadrature gives `Delta E_min(32) >= 1.2785785769e-13` and `Delta E_min(256) >= 2.2807043e-18`, so the required scalar radius is greater than `256a` under either the persistent-deposit threshold or the registered completed-law-storage threshold, decisively excluding the fixed `R<=10a` ENTANGLED-ESCAPE.  The optimized Gaussian construction has cost `2.159e-11` at `R=32` and is consistent with an `R^-5` power up to slow factors, but it is an upper bound rather than the proved global optimum; the quoted `1.7e23a` persistent radius is a well-supported continuum-asymptotic evaluation, not the proved finite-lattice bound.  No corresponding universal conclusion follows for a gauge-complete photon, point insertion, interacting laws, anticipatory preparation, or instantaneous-law accounting.
