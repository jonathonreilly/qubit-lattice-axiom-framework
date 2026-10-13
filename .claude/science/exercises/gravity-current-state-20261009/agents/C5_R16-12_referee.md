# VERDICT: CONFIRMED WITH CORRECTIONS

The worker's fixed reading **OPEN** is correct.  The supplied runs reproduce,
and the leading-order weak translation/JJ algebra and the conditional scalar
boost pole are sound.  The material corrections are that weak closure is not
the registered standard undeformed HDA, Theorem B3 is only a narrow
bounded-angular obstruction rather than a physical or presentation-invariant
no-go for option (beta), strict subluminality is sufficient but not necessary,
and the population conclusion is conditional on both the Planck-lattice scale
and a thermal state.

## Per-item findings

1. **Theorem T3 and Lemma J3 — confirmed in their narrow weak,
   leading-|q|, Killing-sector scope; not a degree-3 standard-HDA
   completion.**  Fresh copies of all three worker runners reproduce their
   saved outputs byte-for-byte (`referee_run/SHA256SUMS.txt:1-6`).  In
   particular the sampled S/G weak solves
   retain residuals at or below `1.3e-15`, the W1 helicity-0 identity agrees to
   `3e-17`, and the numerical JJ mismatch is at the finite-difference floor
   (`referee_run/r1612_degree3.out:3-13,44-46`).  A separate implementation
   that does not import the worker solver substitutes the displayed closed
   form directly into the 3x3 tensor equations for 2,000 arbitrary subluminal
   samples: the forbidden weak projections are `6.0e-16` and `3.2e-16`, while
   `q.A=(q.Delta_c)v/2` and the stress identity hold to `4.6e-16` and
   `4.4e-16` (`referee_r1612_independent.py:52-115`;
   `referee_r1612_independent.out:1-6`).  Thus the h-linear term really does
   cancel the displayed R16-8 transport term weakly, and its divergence is the
   JJ repair stated at `R16-12_report.md:191-201`.  But the construction
   explicitly quotients by the linear constraints (`R16-12_report.md:100-104`)
   and represents the leftover coefficients by matter-dependent, `1/r^2`
   structure functions or a nonlocal basis change (`R16-12_report.md:213-217`).
   That is a deformed/weak first-class statement, not the standard undeformed
   algebra fixed at `TESTS.md:5535-5538`.  Non-Killing smearings are not solved
   (`R16-12_report.md:105-113,330-334`), consistently with the earlier
   local-germ warning (`C5_R12-1_referee_verdict.md:3-15`).  “Closure holds
   only weakly” is established for the displayed W1/`tau=0` construction; it
   is not an exhaustive theorem over every additional regular completion.

2. **Theorem B3 — its two-equation pole is correct, but the no-go must be
   demoted to a conditional obstruction.**  Under the report's explicitly
   assumed standard HDA, setting `(N,M)=(x_b,1)` does require
   `{K_b,H}=P_b` at degree 3, and its right side contains the degree-3
   momentum term (`R16-12_report.md:83-87,150-152,234-247`).  Given the forced
   `b_T`, the W1 translation solution, a regular uniform-lapse Hamiltonian and
   the report's linear-bilinear ansatz, the scalar equations do rigidly give
   `Y_qq=b_T` and
   `X_T=2 i b_T/(q.v)=-(q.Delta_b)/(|q|^2(q.v))`.  The worker null space has
   no `X_T` or `Y_qq` freedom (`referee_run/r1612_controls.out:5-7`), and the
   independent substitution closes to `1.1e-16` while the pole grows by one
   decade per decade in `qhat.v` (`referee_r1612_independent.out:7-14`).
   Class C is therefore a legitimate *narrow* symbol class in which this
   particular boost completion is excluded for a generic mode with
   `qhat.Delta_b != 0` on `qhat.v=0`.  It is not the right class for deciding
   whether alpha versus beta is physical: the fixed test did not impose it,
   it excludes shells, auxiliaries, non-Killing completion and the forced
   directional distribution by definition (`R16-12_report.md:100-113,263-275`),
   and it is not invariant under Lemma W's singular canonical relocation.
   Also, the world-line symbol is homogeneous of degree `-2`; what fails is
   boundedness of its angular factor, so “non-homogeneous” at
   `R16-12_report.md:269` is inaccurate.  Since `{P,K}`, `{K,K}`, general
   smearings, and the listed counter-routes are untested
   (`R16-12_report.md:263-275,330-333`), B3 does **not** prove that beta is
   inconsistent as a full degree-3 completion or that physical nonlocality is
   forced.  The strongest defensible label is “bounded-angular scalar-boost
   obstruction in the displayed leading-order ansatz.”

3. **Lemma W — confirmed only at first order in the constructed translation
   sector, and it makes the alpha/beta label nonphysical by itself.**  The
   rerun gives `Phi_c/delta_c` independent of `c` to `7.2e-15` and hence the
   displayed first-order generator `W` (`referee_run/r1612_controls.out:16-21`).
   Algebraically, this moves the same singular term between the momentum
   generator and the Hamiltonian under a nonlocal canonical change
   (`R16-12_report.md:219-228`).  Therefore “which constraint contains the
   tail” is presentation-dependent unless the admissible local observable
   algebra and allowed canonical maps are fixed.  Lemma W does not yet prove a
   canonical equivalence of the full constraints: extension beyond
   translations, leading order, and Killing smearings is expressly open
   (`R16-12_report.md:330-342`).  Physical locality must instead be tested on
   completed Dirac observables; none is constructed (`R16-12_report.md:278-281`).

4. **Lemma C — S/G pass and the active superluminal L-box mode fails, but
   strict subluminality is not necessary.**  The rerun confirms positive
   denominators for every sampled S/G mode and a Cherenkov pole for the
   `|v|=3.62` L-box mode, with `|q|^2|B|` growing by about ten per decade toward
   the cone (`referee_run/r1612_degree3.out:17-34`).  For generic `|v|>1`, a
   cone on which both `delta_c` and `sigma_TT` are active is indeed an
   obstruction unless a singular Hamiltonian term is admitted.  The report's
   stronger “every defect-carrying mode must satisfy |v|<1” statement
   (`R16-12_report.md:203-210`) is false at the boundary: for `|v|=1`,
   `sigma_TT` vanishes quadratically with `1-(qhat.v)^2`, and the ratio remains
   bounded.  An explicit independent limit tends to `0.49497475`, not a pole
   (`referee_r1612_independent.py:150-167`;
   `referee_r1612_independent.out:15-17`).  The correct condition is absence of
   an *active* Cherenkov zero; `|v|<1` is a clean sufficient condition, while a
   generic superluminal defect mode fails.  The finite-q figures are only a
   random scan at one momentum per law, as the worker itself records
   (`R16-12_report.md:211`; `scripts/r1612_degree3.py:194-204`).

5. **Fixed readings — neither terminal reading is met; OPEN is correct.**
   QUASI-LOCAL requires a constructed degree-3 completion checked through
   `kappa^3`, while this packet has only a leading-order Killing-sector weak
   solution, nonlocal/deformed structure functions, no general smearings and
   no completed boost algebra (`TESTS.md:5545-5548`;
   `R16-12_report.md:301-306,330-334`).  NON-LOCAL also fails: even the narrow
   B3 obstruction neither constructs alpha nor supplies a bounded
   gauge-invariant instantaneous responder or its actual distant response;
   Lemma W further makes the generator-level fork presentation-dependent
   (`TESTS.md:5541-5548`; `R16-12_report.md:265-281,307-310`).  This agrees with
   the R16-8 referee's prior finding that the fork was not exhaustive and no
   Dirac observable had been built (`C5_R16-8_referee.md:95-119`).

6. **Population — the order-of-magnitude energy bound survives, but the
   inference to negligible occupation is conditional.**  The worker runner
   reproduces, but its “minimum defect energy” is selected with the numerical
   cutoff `|defect|>1e-9` (`scripts/r1612_population.py:15-20`) and is therefore
   not the mathematical infimum.  Because the Gevrey defect turns on
   arbitrarily close above `b=1.4`, the infimum is
   `sqrt(0.3^2+1.4^2)=1.431782/a`, or `1.748e19 GeV` when `a=l_P`; at `m=0` it
   is `1.400/a=1.709e19 GeV` (`referee_r1612_independent.out:18-19`).  Thus the
   rounded `>=1.7e19 GeV` statement is correct **conditional on** `a=l_P`, an
   identification the axioms leave open (`MINIMAL_AXIOMS_2026-06-29.md:173-190`).
   Boltzmann suppression is correspondingly enormous only for an assumed
   low-temperature thermal ensemble.  Number-conserving matter can retain an
   arbitrary initial edge population, as the report itself notes
   (`R16-12_report.md:282-290`), so negligible occupation is not a theorem of
   the construction.

## Strongest correct statement

At leading order in smearing momentum, for free number-conserving current-aligned S/G matter, the displayed h-linear singular momentum-constraint term solves the weak constant-translation equations with the W1 forward stress, its helicity-0 condition is an identity, and its divergence is exactly the required JJ repair; the S/G bands avoid the generic helicity-2 Cherenkov pole, whereas an active superluminal L-box mode does not.  Under the assumed standard HDA the affine-lapse bracket does require `{K_b,H}=P_b`, and within the worker's linear-bilinear, bounded-angular ansatz its scalar equations rigidly force the angular pole `X_T=-(q.Delta_b)/(|q|^2(q.v))`.  This is only a presentation-dependent bounded-angular obstruction: the translation closure is weak/deformed rather than a completed standard HDA, the full degree-3/non-Killing and remaining boost brackets are unbuilt, strict subluminality is not necessary at the luminal boundary, and no bounded Dirac observable with an instantaneous distant response exists.  Consequently neither fixed terminal reading is met and R16-12 remains **OPEN**.
