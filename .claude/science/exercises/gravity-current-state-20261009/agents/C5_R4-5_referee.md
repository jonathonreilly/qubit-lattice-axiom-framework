# Independent referee report — C5 R4-5

## VERDICT: CONFIRMED WITH CORRECTIONS

The worker's overall **INCONCLUSIVE** reading against the fixed criterion is
correct, and the past-cone/magnitude arithmetic, reciprocal-row coefficient,
and Bianchi scale comparison substantially reproduce.  The corrections are
material to the advertised FAIL-type sub-results: the Set-A number is not a
class-wide upper bound and uses today's density throughout the past cone; the
Set-C number is a conditional `F=1` comparator rather than a bound from Record
alone; and the finite LRL experiment does not exclude a small asymptotic
volume-law term.  Lemma V remains a sketch and does not establish its stated
necessity of *spacelike* in-band weight.

Independent arithmetic is in `referee_checks.py` and
`referee_checks.out`.  I also checked the primary papers: [ADGS
astro-ph/0209274](https://arxiv.org/abs/astro-ph/0209274), [Zwane--Afshordi--Sorkin
1703.06265](https://arxiv.org/abs/1703.06265), [Das--Nasiri--Yazdi part
II 2307.13743](https://arxiv.org/abs/2307.13743), [Das--Nasiri--Yazdi part
I 2304.03819](https://arxiv.org/abs/2304.03819), [Barrow
gr-qc/0612128](https://arxiv.org/abs/gr-qc/0612128), and the [DESI DR2
cosmology paper 2503.14738](https://arxiv.org/abs/2503.14738).

## 1. Magnitude arithmetic and past-cone four-volume

**Confirmed, with a scope correction to the quoted range.**  Direct
dimensionless quadrature gives

\[
 {V_{\rm lc}\over(c/H_0)^4}=0.122872508692,
 \qquad
 V_{\mathrm{lc}}=4.360137\times10^{103}\ \mathrm{m}^4
             =6.389407\times10^{242}\ell_P^4.
\]

This independently reproduces the worker's value (`R4-5_report.md:88-100`;
`scripts/r45_numbers.out:7-21`; `referee_checks.out:1-14`).  With
`ell_e=ellbar_P`, `kappa_u=1`, and this actual past cone,
`Delta Lambda/Lambda_obs=1.389023`, so the headline 1.39 is correct.

The phrase “0.24--35, depending only on conventions” is too loose
(`R4-5_report.md:102`).  For the actual past cone, the four combinations
displayed by the report span **0.695--34.91**, not 0.24--35.  The 0.243 endpoint
comes from replacing the past cone by the Hubble four-cube and taking
`kappa_u=1/2` (`referee_checks.out:5-14`).  Region choice is not merely a unit
convention, and choosing ordinary versus reduced Planck *element density*
changes the physical four-density by `(8 pi)^2`.  The calculation establishes
an order-of-magnitude comparator, not a derived coefficient.

## 2. Set A

**The qualitative suppression is confirmed; the claimed numerical upper bound
is not.**  The script sets every particle density equal to its present value
throughout the past cone (`scripts/r45_numbers.py:76-89`).  For conserved
particles with `n(a)=n0 a^-3` and a constant proper-time flash rate, independent
past-cone integration gives

\[
 {\langle n\rangle_{J^-}\over n_0}=51.7978,
 \qquad
 \sqrt{51.7978}=7.197.
\]

Thus the worker's deliberately generous `4.552e-73` becomes about
`3.28e-72 Lambda_obs` under the same forced count-volume recipe
(`referee_checks.out:15-18`).  This correction is scientifically immaterial to
the many-decade mismatch, but it invalidates `5e-73` as the literal bound
(`R4-5_report.md:145-147`).

More importantly, `5.3e-11 s^-1` is a nucleon heat bound
(`TESTS.md:2406-2412`), while applying `1e-9 s^-1` to every photon and neutrino
is an intentionally generous scenario, not a proved ceiling on every allowed
Set-A record carrier (`R4-5_report.md:120,147`).  The supplied axiom leaves the
formation site and rate downstream (`MINIMAL_AXIOMS_2026-06-29.md:173-186`).
Matter-following flashes also have a nonuniform intensity and therefore do not
satisfy H2/H3 as stated (`R4-5_report.md:76-82`).  The defensible statement is:
for the specified Poisson flash census and a forced count-volume bridge,
`Delta Lambda/Lambda_obs` is of order `10^-81` for standard GRW nucleon rates
and at most order `10^-72` for the report's extravagant present carrier/rate
scenario, with an additional factor `kappa_u/sqrt(F)`; this is not a theorem
about all Set-A record laws.

## 3. Lemma C-count and the axiom text

**The combinatorial cap is real in a fixed-site reading, but the claimed Lambda
bound and “never a 4-volume” conclusion are overstated.**  The axiom fixes the
physical sites to `Z^3` (`MINIMAL_AXIOMS_2026-06-29.md:35-41`) and says both
one record at most per site and permanence (`MINIMAL_AXIOMS_2026-06-29.md:75-83`).
Consequently, “records form” does **not** license reuse or decay.  Four-dimensional
event sites are not the stated sites; they require a change of Lattice.  Record
also supplies no formation rule, time metric, worldline embedding, or site
creation process (`MINIMAL_AXIOMS_2026-06-29.md:114-130,173-190`).

Given the extra reading that the same persistent site labels form a comoving
Planck-spaced grid in the quoted FLRW geometry, the spatial-union count is
indeed

\[
 N_{\rm site}\le {4\pi\over3}(\chi_p/\ell_P)^3
 =8.2392\times10^{184}.
\]

The arithmetic `3.964e-28 Lambda_obs` also reproduces, **after setting**
`kappa_u=1` and `F=1` (`scripts/r45_numbers.py:91-103`;
`referee_checks.out:19-22`).  In general the displayed result is
`3.964e-28 kappa_u/sqrt(F)`.  Record alone supplies neither a positive lower
bound on `F` nor H3, so the site cap by itself does not give a strict upper
bound on `Delta Lambda`: a nearly deterministic occupied-site count has small
variance, and the conjugacy heuristic then moves in the opposite direction.

Site creation is outside the axiom.  If it means monotone refinement into new,
permanent site labels whose present union is still one `Z^3`, the spatial cap
survives.  If it means replaceable four-dimensional event sites, it can evade
the cap but has changed Lattice/Record.  Finally, a bounded one-time-per-site
formation law can track four-volume over a finite interval before saturation,
so “measures a 3-volume, never a 4-volume” (`R4-5_report.md:135`) is too strong.
What is proved is narrower: a fixed persistent `Z^3` cannot supply one new
Planck-density count per Planck four-volume over a Hubble history.

## 4. Crystal frame dependence

**The leading reciprocal-time-row formula is correct.**  For the aligned
diamond, its spatial cross-section is
`A(t)=(4 pi/3) min(t,T-t)^3`, whose derivative has waist jump
`Delta A'=-2 pi T^2`.  At `q_n=2 pi n/s`, two integrations by parts and the
sum over `n != 0` give

\[
 \operatorname{Var}_{\rm row}N
 =\rho^2 {\pi^2T^4s^4\over180},
 \qquad
 {\operatorname{Var}_{\rm row}N\over\rho V}
 ={2\pi\over15}\rho s^4.
\]

The independent coefficients are 0.418879 for the Z4 time row and 7.757748
for L7 (`referee_checks.out:23-25`), agreeing with the reported Monte Carlo
(`scripts/r45_lattice_count.out:2-10,29-37`).

For a boosted timelike reciprocal vector, the waist jump acquires
`sinc(kT/2)` and the leading variance therefore acquires `sinc^2(kT/2)`, with
an additional `q0^-4` factor already present in the worker's executable formula
(`scripts/r45_checks2.py:7-11`).  For 370 km/s and `s=ellbar_P`, the argument is
`6.2416e57`; `2.57e-116` is the **envelope** `x^-2`, not the value of the
oscillatory `sinc^2 x` (`referee_checks.out:26-28`).  It suppresses that one
reciprocal row, not the whole crystal variance; other reciprocal rows explain
the residuals in `scripts/r45_checks2.out:2-11`.  The computations do establish
frame dependence of the translation-averaged crystal count, but the sentence
“for any real observer the row term is gone” should be read asymptotically and
away from Bragg alignments (`R4-5_report.md:157-167`).

## 5. LRL finite-size claim and P-L-prime

**The tabulated finite-size trend is credible; the FAIL-type extrapolation is
not established.**  The code samples the correct hyperbolic radial density
`sinh^2 eta` and uniformly random directions and translations
(`scripts/r45_checks.py:38-56`; `scripts/r45_checks2.py:20-38`).  Its reported
values fall from about `7e-2` to `1.4e-3` in `Var/(rho V)` and fit
`Var ~ T^2.17--T^2.24` over `T=13--108`
(`scripts/r45_checks2.out:12-22`).  Agreement between `eta_max=1.5` and 3 is
useful evidence.

It is not enough to identify the Haar probability measure on the compact
quotient or an asymptotic exponent.  No fundamental domain, mixing-rate bound,
or truncation error is supplied (`R4-5_report.md:169-180`), and only causal
diamonds—not the actual FLRW past-cone family—were tested
(`R4-5_report.md:312-315`).  More decisively, the same four data points admit
`Var/(rho V)=F+A/T^2` fits with `F` between roughly `1e-4` and `2e-3`, depending
on cutoff and fit range (`referee_checks.out:29-31`).  These fits do not prove a
volume term, but show that `T<=108` cannot exclude one beneath the boundary
term.  The finite result should therefore be stated only as “no order-one
volume-law plateau is visible over the sampled sizes and truncated-ball
averages,” not “H3 fails asymptotically.”

There is no contradiction with P-L-prime.  That theorem guarantees some
spacelike Bartlett weight but explicitly does not put it in any prescribed
band (`R2-2_referee.md:56-85,191-216`; `TESTS.md:2710-2718`).  LRL has such
weight on Bragg mass shells while maintaining the invariant gap
`0<|q^2|<(2 pi)^2/7` (`R2-2_referee.md:124-147`).

## 6. Lemma V

**Suggested is the strongest permissible label, and even the suggested
conclusion needs narrowing.**  The sketch leaves the needed form-factor decay
unproved (`R4-5_report.md:195-202`).  It also needs uniform control of the
weights and growth of all invariant-mass shells; a per-orbit decay does not by
itself control their sum.

The two displayed directions support at most this conditional statement: if
the full spectral measure has a two-sided nonzero invariant-mass gap, has no
separate null/zero contribution, and satisfies the required decay and
summability bounds, then the diamond variance is sub-volume.  Conversely, a
near-zero invariant-mass density can yield a volume law.  Nothing in the sketch
shows that the required near-zero weight must be **spacelike** rather than
timelike or null, and nothing upgrades nonzero weight to “Poisson-size” weight
(`R4-5_report.md:197-206`).  P-L-prime supplies spacelike weight somewhere,
not near zero.  Thus the steering/lensing conclusion in lines 204--207 is an
interesting programmatic conjecture, not a lemma.

## 7. Bianchi estimate

**The scale estimate is correct, with an interpretation caveat.**  Converting
the observed geometric Lambda to energy density gives

\[
 u_\Lambda={c^4\Lambda\over8\pi G}\simeq5.3\times10^{-10}
 \ \mathrm{J\,m^{-3}},
\]

so an order-one stochastic change per Hubble time requires an exchange of that
cumulative magnitude, or power density about `1.2e-27 W m^-3`.  The quoted GRW
heating `5.4e-27 J m^-3` per Hubble time is lower by `9.8e16`, i.e. about 17
decades (`R4-5_report.md:209-217`).  This is a scale comparison between a
signed compensating exchange and positive dissipative heating, not proof that
the exchange must appear as heat.

The report's “whether DNY part I addresses this is unverified” is now resolved
(`R4-5_report.md:219`).  DNY part I, sec. 4.1 and Appendix B, explicitly says
that varying Lambda departs from classical GR, that Model 1 evolves only the
first Friedmann equation, and that the energy-conserving fluid completions have
zero-crossing or numerical-instability problems; it leaves a consistent
modified dynamics open.  ADGS sec. IV likewise identifies the contracted
Bianchi obstruction and possible compensating matter exchange.  These sources
confirm the conceptual tension but do not derive a record-sourced energy
channel of the required magnitude.

## 8. Literature and data summary

**Substantially accurate, with important model/procedure qualifications.**

- ADGS finds the useful phenomenological amplitude range about 0.01--0.02,
  but calls the parameter `alpha`; ZAS later calls the Model-1 parameter
  `beta`.  This is a simulation amplitude, not independently a measured causal
  element spacing (`R4-5_report.md:106-110,239-249`).
- ZAS's selected Model-2 history has `alpha=0.8824`, `mu=0.9804`, and
  `chi^2=11335.2` versus 11334.6 for LambdaCDM.  It also reports relief of the
  then-H0 and Lyman-alpha BAO tensions and no significant solution of the
  ultramassive-black-hole or lithium problems.  The numbers in the report are
  correct.  But Model 2 is phenomenological and its CMB fit uses an explicitly
  ad hoc quintessence-like perturbation prescription; it is not a test of the
  count dynamics.
- DNY part II finds only about 0.015% of scanned Model-1 seeds beat LambdaCDM
  on the supernova sample.  In its CMB treatment, unsuppressed Model 1 is worse
  by more than 150 in chi-square; artificial last-scattering suppression
  reduces the gap to about 20, and preferred generic variations are smaller
  than typical everpresent-Lambda fluctuations.  Its treatment differs from
  ZAS (notably in perturbations and allowed sign/range), so the papers test
  different phenomenological completions rather than directly contradicting
  one another.
- Barrow's `alpha less than about 1e-5` conclusion is correctly reported for
  his assumption of horizon-scale spatial stochasticity.  ZAS explicitly
  objects that this was not derived from a covariant quantum model.  It is not
  a class-wide exclusion.
- The exact phrase about a “yet-unknown solution to the old cosmological
  constant problem” is from ZAS, although DNY part I independently and
  explicitly also treats zero mean as an unsupported assumption
  (`R4-5_report.md:223-228`).
- DESI DR2 reports a data-combination-dependent preference for a `w0-wa`
  evolving-dark-energy fit, not a test of everpresent Lambda.  The worker's
  statement that no DR2 everpresent-Lambda fit was identified is fair, but a
  press-summary hint cannot count toward the fixed PASS criterion
  (`R4-5_report.md:250-251`).

The safe observational conclusion is therefore the worker's narrower one:
current count-derived Model 1 is CMB-disfavoured in the DNY implementation,
while selected phenomenological stochastic histories are not excluded as a
class.  No literal set in R4-5 has both a derived count bridge and a current
CMB/BAO fit.

## 9. Fixed reading, FAIL-type scope, and prior-art relation

**INCONCLUSIVE is confirmed.**  PASS is not established because A+, B-prime+,
and the causal-set comparator add the very count, density, randomness, and
source rules that the literal sets do not supply (`R4-5_report.md:114-127,292-300`).
FAIL is also not established: Set B lacks the Lorentzian observable bridge,
the LRL asymptotic is unresolved, and the data exclude implementations rather
than every allowed stochastic history.  This matches the fixed trichotomy
(`TESTS.md:2840-2849`).

The sub-results should be recorded as follows.  Set A has a many-decade
suppression only for the specified matter-following Poisson flash models, not a
`5e-73` class bound.  Set C has an exact fixed-site event-count cap, but the
`4e-28` Lambda number is conditional on the FRW embedding, forced H1/H2, and
`F=1`; it is not a Record-only theorem.  LRL has a finite-size sub-volume-like
trend, not a proved absence of an asymptotic volume law.

The prior `Lambda=3/R^2` note is explicitly bounded/conditional and lacks the
cosmological radius/FRW bridge (`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:4-8,48-56`).
There is therefore no present repository contradiction.  If both proposals
were adopted as exclusive identifications of the total observed dark energy,
then they would conflict: the spectral-gap route fixes `w=-1`, and an
everpresent stochastic total Lambda triggers that note's stated falsifier
(`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:88-107`).  A separately specified
fixed-plus-stochastic decomposition is logically possible but is not derived
here.

## Strongest correct statement

Under the unimodular conjugacy and count-volume heuristics, an approximately
Poisson, Lorentzian four-dimensional count near Planck density gives the right
present order of magnitude: for the stated flat-LambdaCDM background the
past-cone volume is `6.3894e242 l_P^4` and one standard convention gives
`Delta Lambda=1.389 Lambda_obs`; neither the coefficient nor zero mean is
derived.  Literal matter-following GRW-like flashes are many tens of decades
too sparse in the specified models, and a fixed persistent `Z^3` with one
permanent record per site has at most `8.239e184` distinct record events in the
stated comoving Planck-grid embedding, far below a Planck four-volume count,
but the published numerical Lambda bounds require extra Fano-factor, carrier,
rate, and embedding assumptions.  Crystal translation-averaged count variance
is frame dependent with the verified leading reciprocal-row coefficient
`(2 pi/15) rho s^4`; the solar-motion `10^-116` figure is only that row's sinc
envelope.  The LRL data through `T=108` show a robust sub-volume-like finite-size
trend consistent with its invariant Bragg gap and fully consistent with
P-L-prime, but do not exclude a smaller asymptotic volume term; Lemma V and the
claim that volume-law variance specifically forces low-band spacelike weight
remain open.  Existing phenomenological implementations face a real Bianchi
completion problem and current CMB tension, while neither observations nor
this probe exclude every everpresent-Lambda history; hence the fixed campaign
reading is **INCONCLUSIVE**.
