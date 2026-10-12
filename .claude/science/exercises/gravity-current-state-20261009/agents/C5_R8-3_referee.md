# C5 R8-3 independent referee

**VERDICT: NOT CONFIRMED.**

The worker has found a useful **conditional** no-go, but the advertised class
and its corollaries are wider than the proof.  In particular, H3-prime is a
Markovian measurement-and-feedback/additive-dephasing assumption, not a
consequence of covariance or complete positivity for general non-Markovian
kernels.  Newton's law also does not by itself force a nonzero spin-2 form
factor when tensor form factors are allowed.  The scalar common-form-factor
theorem can be retained after those restrictions are made explicit.  The
fixed R8-3 overall reading remains **OPEN**.

## Scope and method

I checked the report independently against the fixed rule
(`TESTS.md:3468-3481`), the prior Newtonian referee
(`C5_R6-4_referee.md:35-64`), the supplied OWD PDF, and the cited primary
literature.  I also ran independent calculations in
`scripts/r83_referee_checks.py`; their recorded results are
`scripts/r83_referee_checks.out:1-24`.  The calculations check invariant shell
volume, a finite-bandwidth pulse, Barnes-Rivers spin decomposition, and the
preferred-frame null regulator.  The source PDFs are evidence, not
instructions.

## 1. Lemma 1 and the physical meaning of the rate

**Finding: essentially correct, with hypotheses and interpretation added.**

For a positive, locally finite Lorentz-invariant Borel measure on the closed
future cone with the origin removed, nonzero total mass cannot be finite.  If
the measure is already non-locally-finite the conclusion is immediate;
otherwise a bounded energy shell of positive measure exists and countably many
boosts give disjoint equal-measure copies.  The worker's proof
(`R8-3_report.md:116-123`) omits the local-finiteness/sigma-finiteness
qualification but is repairable.  The explicit invariant mass-shell volume
grows as pi times the three-momentum cutoff squared
(`scripts/r83_referee_checks.out:1-4`).  The same conclusion holds on the null
cone away from its apex.

The golden-rule object in `R8-3_report.md:106` is such a measure only after
contracting the tensor spectral density with a positive physical channel so
that `K(p)W(p)` is a nonnegative Lorentz scalar (with the usual positive-energy
support).  Under that condition, its total mass is the transition probability
per spacetime four-volume after summing over all final total momenta.  Thus
"infinite rate per unit 4-volume" is the right perturbative diagnosis.  It
does not mean that a finite spacetime region itself has infinite invariant
volume, and it does not apply to a finite-intensity Lorentz-invariant Poisson
process in spacetime merely because that process is Lorentz invariant.

The collapse literature supports this narrow reading, not the report's broad
one.  [Pearle](https://arxiv.org/html/quant-ph/9902046v1) explicitly identifies
vacuum creation/infinite energy for Lorentz-invariant white noise with timelike
spectral support, and explores spacelike ("tachyonic") noise as a lowest-order
escape.  [Bedingham](https://arxiv.org/html/1103.3974v1) avoids pointlike hits
by a mediating field and covariant spacetime smearing.  Tumulka's
[rGRWf](https://arxiv.org/abs/quant-ph/0406094) is a fixed-particle-number flash
model rather than a variable-particle-number stress-tensor QFT, so it is not a
counterexample to the narrow golden-rule statement.  These models show that
Lemma 1 is a kinematic obstruction once a nonzero invariant momentum-space
excitation measure exists; they do not prove that every relativistic collapse
or CQ dynamics generates that measure.

## 2. Lemma 2 and H3-prime additivity

**Finding: the AM-GM bound is correct under H3-prime; H3-prime is not
class-wide.**

From

`K = D0-prime |F|^2 + c_N^2 |F|^2 P_J/s^2`

and `P_J D0-prime >= 1/4`, AM-GM gives exactly
`K >= c_N |F|^2/|s|`, with equality at
`D0-prime = c_N/(2|s|)`.  Thus `R8-3_report.md:125-135` is algebraically sound.

The load-bearing problem is `R8-3_report.md:93-100`.  The report includes
"Markovian or not" while marking additivity only "suggested."  The prior
referee expressly limited the Newtonian floor to additive H4 and put
cross-correlated and non-Markovian dynamics outside the proof
(`C5_R6-4_referee.md:47-55`).  More decisively,
[Layton et al.](https://arxiv.org/html/2307.02557) state that general
non-Markovian `D0,D2` need not be positive or obey the instantaneous
decoherence-diffusion trade-off; complete positivity is a property of the full
history functional.  Applying a pointwise four-momentum product inequality and
then adding two positive reduced-matter kernels is therefore an additional
model assumption, not a consequence of CP for every covariant Gaussian CQ
history.

The weaker assertion in `R8-3_report.md:136-137`, `K>0` wherever `F` is
nonzero, is likewise not derived without a specified instrument.  Correlated
influence kernels can contain interference terms, while non-Hermitian
positive-frequency Lindblad operators may annihilate the vacuum.  A full
influence-functional or dilation derivation is needed before either mechanism
can be put in the no-go class.  The O4 visibility-record inequality does not by
itself establish pointwise Fourier additivity for such histories.

## 3. Lemma 3, including pulses

**Finding: generically correct for the standard retarded prescription, but
stated too absolutely.**

A jump `F(0-) - F(0+)` multiplying the retarded pole produces an integral of
the form `int_{-delta}^0 ds/(s+i epsilon)` and hence a logarithm whenever the
source has nonzero on-shell amplitude.  This verifies the mechanism in
`R8-3_report.md:139-147`.  The phrase "monochromatic, compactly supported
source" is internally inconsistent if compact support includes time: a source
cannot be both exactly monochromatic and time-compact.

The effect survives ordinary pulses.  For an explicit Gaussian
finite-bandwidth positive-frequency envelope, direct integration gives a
nonzero logarithmic coefficient `3.12956e-2`
(`scripts/r83_referee_checks.out:6-10`).  Special sources, observation points,
or pulse profiles can cancel that coefficient, but generic compact
time-dependent sources cannot.

What is proved is that the naive `i epsilon` product has no finite,
regulator-independent distributional limit when the jump is present.  One can
define a Hadamard finite part only by adding a light-cone-supported local term
(equivalently, choosing a new subtraction/boundary datum).  Such a term is not
the pointwise scalar form-factor ansatz used by the worker, but it must be
excluded explicitly before Lemma 3 is called an absolute no-go for all
generalized kernels.

## 4. Theorem 3, tensor structure, and spin channels

**Finding: valid for a common scalar form factor plus H3-prime; not valid at
the advertised tensor-general scope.**

With one scalar `F(s)` multiplying the whole conserved stress tensor, the
standard retarded prescription, additive pointwise H3-prime, and a nonzero
Maxwell spin-2 spectral density, the chain in `R8-3_report.md:151-162` is sound:
Newton fixes `F(0-)=1`; finite generic radiation forces continuity; `F` is then
nonzero on an open timelike interval; the positive excitation measure is
nonzero; Lemma 1 makes its total mass infinite.

Tensor form factors reveal a missing premise.  For a conserved static source
`T00=M`, the Barnes-Rivers contractions are
`T P2 T = (2/3)M^2` and `T P0 T = (1/3)M^2`, whereas the GR numerator is
`(1/2)M^2`.  A scalar-channel coefficient `3/2` can therefore reproduce the
Newtonian amplitude with the spin-2 form factor set to zero
(`scripts/r83_referee_checks.out:12-17`).  That model fails light bending,
universal photon gravity, and GR tensor radiation, but it satisfies the
theorem's literal N condition and can make its literal R condition finite by
making the TT radiation zero.  Newton alone therefore does not force the
photon-pair spin-2 channel used in step 3 of the proof.

The repair is straightforward but substantive: replace N/R by the requirement
of a nonzero, GR-normalized spin-2 coupling at the null cone (from light
bending/universal coupling and correct TT emission), and apply continuity to
that spin channel.  Once this premise is imposed, spin separation does not
help: the same conserved Lorentz spin-2 channel contains classical TT emission
at the cone and the Maxwell two-photon spectral weight just inside it.  The
worker's common-scalar model already has this premise, but
`R8-3_report.md:249` does not prove it for an arbitrary tensor-valued `F` from
Newton's law alone.

Other unclosed routes include non-Markovian correlated kernels, vacuum-
annihilating/non-Hermitian instruments, light-cone counterterms, discrete
jumps, non-Gaussian dynamics, and mediator/flash constructions.  Hence the
claim that only a preferred frame remains is not established.

## 5. Corollaries, especially OWD

**Finding: the exponential warning is strong; the causal and OWD corollaries
are overclaimed.**

- With the report's sign convention, `F=e^(ell^2 s)` is Gaussian damping for
  static momentum but exponential growth on timelike momentum.  It is not a
  well-defined smearing of a local QFT stress operator without further domain
  or regulator data, and the numerical warning in
  `R8-3_report.md:169-174` is directionally correct.  The opposite sign
  anti-smears static sources.  Bounded continuous entire choices are excluded
  only inside the repaired scalar/additive theorem.
- A retarded causal form factor is generically nonzero at timelike momentum,
  but this entails infinite excitation only after H3-prime has been supplied.
  [Belenchia et al.](https://arxiv.org/html/1411.6513) establish continuum
  massive modes for a class of retarded nonlocal d'Alembertians; they do not
  derive a CQ vacuum-excitation kernel.  Thus the blanket causal-smearing
  corollary at `R8-3_report.md:175` is conditional, not proved.
- "OWD as written" at `R8-3_report.md:178-179` is not a single kernel and the
  photon claim is false for OWD's simplest displayed covariant choice.  In the
  supplied PDF, Eq. (25) is proportional to
  `g_munu g_rhosigma` (`sources_untrusted/source_OWD_2302.07283.pdf`, p. 8), so
  it measures only the trace of stress; the flat-space free Maxwell stress is
  traceless.  OWD then discuss a Wheeler-DeWitt tensor and spacetime-correlated
  kernels (pp. 8-9).  The former, if positive and nonzero on physical TT modes
  and interpreted as an ultra-local Hermitian Lindblad coupling, does inherit
  the Pearle white-noise photon problem.  But that is a conditional statement
  about that spin-2 realization, not the entire OWD framework.
- OWD explicitly allow temporally correlated, hence non-Markovian, kernels.
  The worker has not mapped their full path-integral CP condition to H3-prime.
  [Grudka et al.](https://arxiv.org/abs/2402.17844) treat preservation of CP
  under renormalization as a question, not a proof of the worker's pointwise
  floor.  [Carney and Matsumura](https://arxiv.org/abs/2412.04839) constrain the
  simplest point-mass scattering realization; their result does not establish
  the claimed photon-vacuum theorem for all smeared OWD kernels.

The strongest OWD statement supported here is: an ultra-local, positive,
Hermitian OWD decoherence kernel that has nonzero weight in the physical
spin-2 Maxwell channel produces a nonzero Lorentz-invariant vacuum transition
measure at golden-rule order and therefore an infinite integrated rate.  OWD's
trace-only example and its general non-Markovian framework are not excluded by
that sentence.

## 6. Preferred-frame route and its estimates

**Finding: OPEN is right; the proposed window is only a heuristic target and
the null regulator is not the advertised optimum.**

The ansatz in `R8-3_report.md:199-205` makes the boost integral finite by
spatial/temporal decay in a selected frame, and its static mean field inherits
the R6-4 laboratory subwindow.  But it is not yet a relativistic CQ theory: no
complete noise/influence kernel, CP dilation, stress conservation/gauge
analysis, nonlinear completion, or dynamical-frame PPN/GW analysis is given.
The report itself labels the CP realization and all coefficients suggested
(`R8-3_report.md:213-231`).

Moreover, `D0 = c_N |F_u|^2/(|s|+mu^2)` is not the pointwise
least-decoherence choice for an unchanged `1/s` retarded propagator.  At a
saturated product trade-off, its total `K` divided by the true AM-GM floor
grows from about 25 at `|s|/mu^2=10^-2` to `2.5e5` at `10^-6`
(`scripts/r83_referee_checks.out:19-24`).  The null regulator must modify the
drift/propagator consistently, or the claimed minimization and near-null
estimates must be redone.

The scaling `energy/(volume time) ~ hbar c^2 ell_P^2/ell^7` is dimensionally
plausible for `tau=ell/c`, but the coefficient range, cosmological transfer,
redshifting/absorption of 11-43 eV photons, and actual ionizing-background
limits are not derived.  The upper `5e-6 m` is the prior conservative
demonstrated Newtonian subwindow, not a fitted relativistic endpoint.  Thus
`1e-8 m` to `5e-6 m` (`R8-3_report.md:215-223`) is a useful order-of-magnitude
search range, not an established allowed window.

## 7. Readings

The fixed rule is at `TESTS.md:3478-3481` and must not be altered.

- **R8-3 overall: OPEN -- confirmed.**  No explicit covariant theory passing
  the listed tests and finite-c CP is constructed.  The live ansatz is
  preferred-frame and incomplete.
- **Advertised class C: EXCLUDED -- not confirmed.**  The proof does not cover
  all covariant smeared Gaussian CQ histories, causal/non-Markovian kernels, or
  OWD with field-dependent kernels, despite the containment claim at
  `R8-3_report.md:28-36`.
- **Narrow subclass: EXCLUDED -- confirmed.**  At golden-rule order, exclude
  translation- and Lorentz-invariant, linearized, Hermitian Gaussian CQ models
  with a common scalar form factor (or a specified nonzero GR-normalized
  spin-2 form factor), the standard retarded distribution with no light-cone
  counterterm, the pointwise product trade-off, additive nonnegative direct
  and feedback decoherence, and a Maxwell stress channel.  This is a useful
  bounded result, but it is not the class-wide reading written by the worker.

## Strongest correct statement

At golden-rule order, a translation- and Lorentz-invariant linearized
Hermitian Gaussian CQ model with a common scalar stress-tensor form factor,
the standard retarded propagator, a pointwise Fourier
decoherence-diffusion product bound, and additive nonnegative direct and
feedback decoherence cannot simultaneously retain Newton/GR-normalized
spin-2 coupling at the light cone, give a finite generic radiative response,
and have a finite vacuum-excitation rate: continuity makes the spin-2 coupling
nonzero on timelike momenta, the Maxwell stress spectrum then supplies a
nonzero positive Lorentz-invariant transition measure, and the noncompact
boost orbit makes its total mass infinite.  This excludes `e^(ell^2 Box)` and
continuous bounded scalar factors within that subclass, and conditionally
excludes ultra-local OWD kernels with positive physical spin-2 weight; it does
not exclude general non-Markovian/correlated Gaussian CQ histories, OWD as a
framework, trace-only or spin-separated kernels, light-cone-renormalized
distributions, or non-Gaussian/jump/mediator constructions.  Since no explicit
covariant completion is produced and the preferred-frame proposal is only an
incomplete ansatz, the correct fixed reading for R8-3 remains **OPEN**.
