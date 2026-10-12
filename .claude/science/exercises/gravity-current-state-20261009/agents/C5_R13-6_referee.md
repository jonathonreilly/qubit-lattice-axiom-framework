# C5 R13-6 independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

The decisive result is confirmed, but only at the scope actually defined by
E1-H1--H5: the literal, preferred-frame, temporally filtered Newtonian mean
field is excluded for every `ell_s` in the fixed R11-5 family.  This is not a
no-go for all causal CQ dilations, for GR, for R6-4's instantaneous Newtonian
kernel, or for a still-unwritten reciprocal/strong-field completion.  The
zero-first-moment modification evades the leading drag, but changes the
literal R11-5 gain and therefore defines a repaired class whose reading is
OPEN.  Two material corrections are required: the coefficient
`6 (v tau/R)^2` is profile/convention-specific, and the exact finite-start
`J0` output has no pointwise finite `hdot` variance because differentiation
contains a white-noise boundary term.

The fixed task and readings are at `TESTS.md:4682-4692`.  I did not change
`TESTS.md`.

## Reproducibility

- The worker program reruns byte-for-byte against its saved output:
  `python3 scripts/r136_checks.py | diff -u scripts/r136_checks.out -` exits
  zero.  Its script and output SHA-256 hashes agree with those reported by the
  worker.
- I independently re-derived the load-bearing arithmetic in
  `scripts/r136_referee_checks.py:1-134`; the saved result is
  `scripts/r136_referee_checks.out:1-33`.
- Kramer et al. report the 2.45-hour Double Pulsar and agreement of the
  quadrupolar-radiation prediction at `1.3e-4` (95% confidence):
  [arXiv:2112.06795](https://arxiv.org/abs/2112.06795),
  [Phys. Rev. X 11, 041050](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.11.041050).
  Treating that entire residual as new drag is conservative.

## 1. Lemma D

### Finding: confirmed within the stated E1 Newtonian mean-field model

The model assumptions are unusually important here.  E1-H1 makes matter feel
the record-fed field in a fixed CMB frame, E1-H4 supplies the literal causal
gain, and E1-H5 explicitly restricts the drag calculation to Newtonian mean
field (`R13-6_report.md:144-157`).  R11-5 likewise gives
`E[J] = F_u <T>` and causal record-conditioned feedback
(`C5_R11-5_report.md:131-145`), with the literal
`F_u = exp(-k^2 ell^2/2)(1-i omega tau)^-n`
(`C5_R11-5_report.md:154-159`).

For a rigid density `rho(x-vt)`, Fourier support imposes `omega=k.v`.  Inserting
the filtered potential in `-int rho grad Phi` leaves only the odd imaginary
part and gives

`F_i = -4 pi G int d^3k/(2pi)^3 k_i Im F(k.v,k) |rho_tilde|^2/k^2`.

If `Im F_t(omega)=delta omega+O(omega^3)`, spherical averaging and Parseval
give

`F_self = -(4 pi G/3) delta (int rho^2) v + O(v^3)`.

Thus the sign and coefficient in `R13-6_report.md:352-368` are correct.  For
`(1-i omega tau)^-n`, `delta=n tau>0`: the force is drag.  Translation
invariance does not forbid it because the fixed-frame meter/record sector can
take momentum.

There is one harmless bookkeeping omission.  The displayed force drops the
spatial vertex factors even though E1-H1 says matter feels `g*T`
(`R13-6_report.md:146`) and the source gain also contains `g`
(`R13-6_report.md:154-156`).  Depending on the precise source convention, the
integrand should contain at least one `g_tilde`, and naturally
`|g_tilde|^2`.  This replaces `int rho^2` by its spatially smeared analogue.
For `ell <= 5 micrometres` and a `12 km` neutron star the relative correction
is negligible, so it cannot affect an eleven-decade exclusion.

For an `n=1` polytrope,

`int rho^2/M = pi M/(8R^3)` and
`(4 pi G/3) int rho^2/M = pi^2 GM/(6R^3) = 1.6424e8 s^-2`.

The uniform-sphere comparison is `GM/R^3 = 9.9845e7 s^-2`.  These reproduce
the worker's neutron-star estimate (`R13-6_report.md:374-380`) independently;
see `scripts/r136_referee_checks.out:1-7`.

For a common linear drag coefficient `Gamma` on the two stars, the internal
power is `-2 Gamma K`.  The orbit-averaged Kepler virial relation `K=-E` holds
also for an eccentric orbit, so
`Pdot_b/P_b = -3 Gamma`; circularity is not needed.  The centre-of-mass cross
term cancels.  If the stars have different coefficients, the replacement is
`Gamma_eff=(Gamma_A m_B+Gamma_B m_A)/(m_A+m_B)`; the worker's exact CM
cancellation statement at `R13-6_report.md:376-378` silently assumes a common
coefficient.  The similar Double-Pulsar stars make this an order-unity, not an
orders-of-magnitude, correction.

Using `P_b=8834.535 s`, `|Pdot_GR|=1.252e-12`, and the conservative `1.3e-4`
fractional allowance gives
`Gamma < 6.14e-21 s^-1`, hence
`delta < 3.74e-29 s` for the polytrope (`6.15e-29 s` uniform) and, for `n=3`,
`ell < 3.74e-21 m`.  The independent values are at
`scripts/r136_referee_checks.out:2-7`.  Against the fixed range beginning at
`4e-10 m`, every literal `ell_s` is excluded by about `1e11` to `1e15`, as
claimed at `R13-6_report.md:374-383`.

### Does GR-like self-consistency cancel it?

Not inside the displayed model.  Ordinary relativistic gravity avoids
aberrational self-drag through Lorentz-covariant velocity-dependent fields and
conservation laws; equivalently, a retarded Lorentz-invariant response is real
on a uniformly moving body's spacelike support.  The worker explicitly notes
that escape at `R13-6_report.md:382-386`.  Here the extra absorptive phase is a
preferred-frame source filter, and neither the zero reverse gain
`chi_FF=0` nor zero-mean backaction noise supplies an opposite deterministic
force (`C5_R11-5_report.md:137-145`).  A reciprocal action, dressed-body
construction, dynamical frame, or full nonlinear strong-field theory could
add a cancellation, but none is part of E1 and none is constructed.  The
result is therefore a valid no-go for the explicit model, not a theorem about
all GR-like CQ completions.  Applying its Newtonian density formula directly
to a relativistically compact neutron star is also an uncontrolled
strong-field extrapolation, although ordinary structure-factor changes
cannot plausibly erase the `>=1e11` margin; only a structural cancellation
could.

### R6-4

Lemma D does **not** apply to R6-4's Newtonian Markovian kernel.  R6-4 specifies
an instantaneous back-reaction drift and homogeneous Markovian kernels
(`C5_R6-4_report.md:49-60`) and explicitly puts non-Markovian/coloured models
outside its scope (`C5_R6-4_report.md:62-68`).  It has no temporal mean-field
factor `F_t`, hence `delta=0` and no Lemma-D drag.  R13 may inherit R6-4's
spatial `ell_s` window, but not export the temporal no-go back to R6-4.

## 2. Repair P-r13b and its residual

### Finding: leading repair confirmed; quoted universal suppression corrected

For

`F_c(x)=(1-i n x)(1-i x)^-n`,

the coefficient of `Im F_c` at order `x` vanishes.  At `n=4`,
`Im F_c=20x^3-84x^5+...`; the independent fit is at
`scripts/r136_referee_checks.out:9-11`.  It is causal, stable, proper, and
retains sufficient high-frequency falloff.  This confirms the construction
in `R13-6_report.md:389-396` and its named signed/extrapolating price at
`R13-6_report.md:429-434`.

For the cubic term the spherical result is

`Gamma_res=(4 pi G/M)(20 tau^3 v^2/5) int |grad rho|^2`.

For the stated smooth `n=1` polytrope,
`int |grad rho|^2/M=4.0264e10 kg m^-5`, giving
`Gamma_res=5.64e-29 s^-1` at `ell=5 micrometres`, well below the pulsar bound
(`scripts/r136_referee_checks.out:12-14`).  The strict repaired family therefore
passes this drag test comfortably.

The sentence “reduces the drag by `6(v tau/a)^2`”
(`R13-6_report.md:370-372`) is not a body-independent result.  It is the
worker's Gaussian profile and width convention.  Relative to the `n=3`
literal term, the `n=1` polytrope gives
`4 pi^2 (v tau/R)^2 = 39.4784 (v tau/R)^2`
(`scripts/r136_referee_checks.out:15-16`).  The absolute polytrope result used
for the pass is nevertheless correct.

The quoted `tau_c < 7.9e-12 s` is a useful smooth-polytrope, weak-field estimate,
not a hard model-independent window.  It depends on the assumed CMB speed,
surface profile, and the orbit average of a cubic velocity force.  At the
strict value `tau=ell/c`, the margin is so large that these qualifications do
not matter.

Finally, P-r13b is a changed dynamical law, not literally the R11-5 gain that
defines `K_epsilon` at `C5_R11-5_report.md:154-159`.  It is legitimate as a
named repair, but the fixed literal class remains EXCLUDED and the repaired
class is a separate OPEN candidate.

## 3. Lemma S and the R11-5 measure correction

### Finding: confirmed with the worker's stated scope

The Laplace identity
`int_0^infinity exp(-pt) J0(Omega t) dt=(p^2+Omega^2)^-1/2`
confirms
`Hhat=(Omega^2-(omega+i0)^2)^-1/2`, `Hhat^2=G_R`, and the causal kernel
`theta(t)J0(Omega t)`.  `Hhat` and its inverse are analytic in the upper half
plane; the inverse is a causal distribution of order one.  The relevant
claim and construction are at `R13-6_report.md:170-197`.

For R11-5's displayed `s0=0` baseband profile
`f(x)=x^-1/2 (x+epsilon)/(x+epsilon^2)`, the Stieltjes cut density is

`rho(t)=(epsilon-t)/(pi sqrt(t)(epsilon^2-t))`.

It is negative for `epsilon^2<t<epsilon`, reproduced at
`scripts/r136_referee_checks.out:18-22`.  Hence that profile cannot be a
positive mixture of cone-centred **Lorentzian** lines, correcting the claim at
`C5_R11-5_report.md:168-175`.  This does not rule out non-Lorentzian line
shapes, a finite `s0`, or R13's single-port outer-factor realization; the
worker states the same limitation at `R13-6_report.md:216-229`.

## 4. Finite-start covariance and complete positivity

### Finding: finite `h` covariance confirmed; `hdot` and exact-limit CP overstated

For white input of spectral density `1/2`, the finite-start output has

`C_h(t,t')=(1/2) int_t0^min(t,t') J0(Omega(t-s))J0(Omega(t'-s)) ds`,

as in `R13-6_report.md:247-255`.  In particular,
`Var h=(1/2)int_0^T J0(Omega s)^2 ds` is finite at every finite age and grows as
`[ln(8 Omega T)+gamma_E]/(2 pi Omega)`.  Independent quadrature agrees through
`T=10000/Omega` (`scripts/r136_referee_checks.out:24-28`).

However,

`d/dt int_t0^t J0(Omega(t-s)) xi(s) ds
 = xi(t)-Omega int_t0^t J1(Omega(t-s)) xi(s) ds`.

The worker's `Var hdot` calculation integrates only the `J1` term
(`scripts/r136_checks.py:141-154`) and omits the white-noise boundary term.
Thus the exact `J0` output is Brownian-like/non-differentiable: pointwise
`Var hdot` and a naive derivative energy are not finite.  The assertion
`h=hdot=0` and the “both quadratures finite” claim at
`R13-6_report.md:247-260` require bandwidth regularization or a distributional
interpretation.  This does not invalidate finite `h` covariance or Lemma D,
but it means the exact finite-start metric state is less regular than stated.

CP is established for each finite rational Gaussian network: unitary
matter-meter evolution, homodyne instruments, and causal record-conditioned
feedback compose to a CP map (`R13-6_report.md:270-290`; compare the finite
R11-5 argument at `C5_R11-5_report.md:137-144`).  For the exact irrational
`s0=0` factor, the worker itself says that the quantum initial-state treatment
is only suggested (`R13-6_report.md:236-245`).  A limit of CP maps is CP only
after specifying a convergence topology and proving convergence of the maps;
the report supplies covariance convergence on finite intervals, not a full
proof for unbounded stress couplings.  Therefore: finite rational
approximants are CP; exact-limit CP is conditional, not fully proved.

## 5. E2-h drag

### Finding: order-of-magnitude claim confirmed, but only as a weak-field estimate

Expanding the E2-h frictional propagator for a slowly moving density yields

`F_drag=-(2 gamma |U|/(3c^2)) v`,
`Gamma_E2=2 gamma |U|/(3 M c^2)`.

This independently confirms the formula reported at
`C5_R12-7_report.md:140-145`.  For a uniform `1.3 M_sun`, `12 km` star,
`|U|/(Mc^2)=0.09598`, so `Gamma_E2/gamma=0.06399`; the same pulsar residual
gives `gamma < 0.0436 H0` (`scripts/r136_referee_checks.out:30-33`).  An `n=1`
polytrope or more compact binding estimate moves this to about `0.03-0.04 H0`.
Thus `gamma lesssim 0.03 H0` is a reasonable suggested estimate, not a precise
bound.

Calling it “common-mode” for a binary is incorrect.  A force proportional to
each star's absolute frame velocity damps both CM and relative velocity; for
equal coefficients the internal orbit obeys the same `-3 Gamma` period
mapping.  For unequal coefficients use the mass-weighted `Gamma_eff` above.
The earlier R12-7 referee already correctly warned that E2-h is not a nonlinear
conservative metric theory and its neutron-star drag is only a tentative
linear-model prediction (`C5_R12-7_referee.md:138-145`).

Independently of this regulator drag, E2-h carries the unrepaired R11-5 gain
(`C5_R12-7_report.md:66-70,140-145`), so the literal E2-h construction also
inherits Lemma D.  After P-r13b, its own frictional drag remains and suggests
the additional `gamma/H0` restriction.

## 6. Reading

### Finding: worker reading confirmed after scope corrections

The fixed setting explicitly names R11-5's regulated family, a finite start,
the CMB frame, and `n>=3` (`TESTS.md:4682-4687`); EXCLUDED requires a refereed
violation for every `ell_s` in that class (`TESTS.md:4688-4691`).  Lemma D now
meets that standard for the literal `F_u`: it is independent of epsilon and of
the start-time regulator, and its smallest violation is about eleven orders of
magnitude.  The strongest attempted escapes either remove the temporal delay
(R6-4), restore Lorentz-covariant/comoving dynamics, add an unconstructed
reciprocal strong-field cancellation, or change the gain's first moment.  All
leave the literal class.

The repaired model is OPEN, not VIABLE.  It has a safe strict-family drag
margin and a viable finite rational scalar CP construction, but its gain is a
new law; the exact irrational state has the differentiability/CP-limit caveats
above; and the spin-2 conserved-noise assembly and record-energy coefficients
remain unbuilt (`R13-6_report.md:462-479`).

## Strongest correct statement

Within the explicitly stipulated linearized, preferred-CMB-frame E1 model in
which the Newtonian mean field is sourced through R11-5's literal causal gain
`exp(-k^2 ell^2/2)(1-i omega ell/c)^-n`, `n>=3`, a compact body necessarily
experiences a leading self-drag
`-(4 pi G/3)(n ell/c)(int rho^2)v` up to negligible spatial-smearing and
order-unity stellar-structure corrections; the Double Pulsar then requires
`ell < about 4e-21 m`, excluding every `ell_s` in the fixed
`4e-10--5e-6 m` class by at least about eleven orders of magnitude.  This
conclusion does not apply to R6-4's instantaneous kernel or to arbitrary
Lorentz-covariant/reciprocal CQ completions.  A signed causal gain with zero
first moment removes the linear drag and passes the strict `tau=ell/c` test,
but it is a changed, still-OPEN model rather than a rescue of the literal
class, and its exact irrational finite-start CP/derivative regularity and full
spin-2 completion remain unresolved.
