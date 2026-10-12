# C5 R12-7 independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading is **OPEN**.  The scalar numerics, the damped-wave Green
function, the narrow classical Lamb-string identity, and most quoted
observational arithmetic survive.  The report nevertheless overstates its
meter as an explicit CQ dilation, its kinetic-fluid estimate as a general
hydrodynamic impossibility, its string as a gravitating/Bianchi-compatible
sink, and the Lu et al. number as an observational margin.  These corrections
reinforce rather than change OPEN: `VIABLE` requires an explicit stationary
E2 model passing every listed test, and that object has not been constructed
(`TESTS.md:4529-4542`).

## 1. Meter bank and causal kernel

**Kernel confirmed; meter only partially confirmed.**  I reran
`scripts/r127_checks.py` with the supplied hash-matching source.  It reproduced
the stored output, including the pole locations, cone support, static integral,
bank excess $1\le X\le2.467$, the $+1/-1$ spectral slopes, and finite
fixed-$\gamma$ integrals growing logarithmically
(`scripts/r127_checks.out:1-9,48-58`).  The stated retarded kernel is the correct
fundamental solution of the telegraph equation: after
$h=e^{-\gamma t/2}u$, the interior is the tachyonic Klein--Gordon $I_1$
tail, while the principal part retains the light cone
(`R12-7_report.md:112-115`).  The boosted-frame sampling can also be upgraded
to an exact pole bound: the discriminant identity in
`scripts/r127_referee_checks.out:24-26` proves that both boosted frequencies
have non-positive imaginary part.

What the code actually constructs is a finite scalar spectral recipe.  It
postulates each element's quantum-limited QND spectra and zero reverse gain,
then classically filters and sums them (`scripts/r127_checks.py:147-187`).  The
two-tone check verifies stationarity of one classical OU record covariance,
not the signal/backaction cross spectra or a quantum instrument
(`scripts/r127_checks.py:189-205`).  No Hamiltonian/Kraus dilation, spatially
local spin-2 realization, tensor constraints, or combined bank-plus-
$\omega^{-8}$ UV chain is supplied; the worker itself records the last two
omissions (`R12-7_report.md:91-93`).  Consequently CP under retarded feedback
is correct **conditional on** legitimate QND elements, but “an explicit
stationary non-demolition E2 model” is not established
(`R12-7_report.md:78-89`).

## 2. Sink, string, and second-order Bianchi claim

**The classical string identity is confirmed, but the claimed sink completion
is not.**  For an outgoing semi-infinite string,
$y(x,t)=q(t-x/c)$ gives $T y_x(0,t)=-Z\dot q$ and outward flux
$Z\dot q^2$, exactly reproducing local Ohmic friction and energy loss
(`scripts/r127_referee_checks.out:28-30`).  The discretized experiment agrees
at the quoted $10^{-4}$-$10^{-3}$ level
(`scripts/r127_checks.out:64-66`).  This proves a noiseless **classical
oscillator-bath boundary model**, not a field-level gravitating sink: “one
string per frame point” is asserted without an action, a stress tensor, an FRW
evolution law, or coupling to all constrained metric components
(`R12-7_report.md:98-108`).  In particular, the dust equation
$\dot\rho_s+3H\rho_s=\gamma\rho_{GW}$ is not derived from the Lamb strings;
an infinite string stores ever more total energy even when the endpoint state
is stationary.

The Bianchi core is narrower than the report says.  If one demands a
diffeomorphism-compatible Einstein completion, the contracted Bianchi identity
does require a compensating sector carrying the four-momentum lost by the GW,
and that sector appears in the total gravitational source.  But E-H5 states
only that the classical near-cone GW content gravitates
(`R12-7_report.md:66-72`); it does not derive a stress tensor for the fixed
frame or string bath.  The phenomenological friction equation explicitly
breaks the usual gauge symmetry and no second-order completion is given
(`R12-7_report.md:104-108,117-118`).  Thus “a consistent Einstein completion
must account gravitationally for the exchanged stress-energy” is sound;
“this string sink has been shown to gravitate” is not.

The mean-free-path calculation correctly rules out a dilute kinetic fluid of
cosmological density as the source of $\gamma\sim H_0$
(`scripts/r127_checks.out:68-70`), but it is not a theorem against every
hydrodynamic or strongly coupled sink.  The quantum-FDT budget is likewise
conditional on the asserted noise transfer, mode normalization, and
unrenormalized gravitational role of the half-quantum.  Indeed, the code's
displayed integral is $1.0000$ while the prose assigns a $1/2$ normalization
(`scripts/r127_checks.out:88-94`), so its absolute $\rho$ coefficient is not
independently closed.

## 3. TT-only acausality

**Confirmed for the E2-TT law as defined, with a scope qualification.**  The
standard spatial TT projector contains inverse Laplacians and sends a compact
tensor to nonzero instantaneous spatial tails; the supplied FFT example
reproduces this at radii 2, 3, and 5 outside unit support
(`scripts/r127_checks.out:81-86`).  In ordinary linearized GR, nonlocal pieces
of the scalar, vector, and tensor split cancel in gauge-invariant curvature.
Changing only the TT retarded response leaves
$\Lambda^{TT}(G_\gamma-G_0)*T$ uncancelled, and since
$G_\gamma-G_0=O(\gamma)$, generic curvature acquires spacelike support at
that order (`R12-7_report.md:119-121`).  This excludes the naive
preferred-slicing, instantaneous-projector E2-TT prescription; it is not a
no-go against every local tensor/aether completion that reduces to tensor
damping on shell.  E2-h's constant-coefficient linear equation is hyperbolic
and causal, but its scalar/vector positivity and nonlinear completion remain
unchecked (`R12-7_report.md:117-118`).

## 4. Observational numbers and Lu et al.

**Most arithmetic is confirmed; the status of the siren and PPN tests needs
correction.**

- The GW170817 speed interval and the (1.53\times10^{-42}) correction at
  (100\) Hz are correct (`scripts/r127_referee_checks.out:1-5`; [GW170817 and
  GRB 170817A](https://arxiv.org/abs/1710.05834)).  The front speed remains
  (c).
- The Hubble-rate ratios (\gamma/\Omega=4.9\times10^{-15}) and
  (1.5\times10^{-15}) are correct, and are negligible relative to the
  published Double Pulsar (1.3\times10^{-4}) quadrupolar test
  (`scripts/r127_checks.out:17-29`; [Double Pulsar](https://arxiv.org/abs/2112.06795)).
  The script's (\le\gamma/\Omega) statement is a conservative scaling for
  its smooth source examples, not a proved source-independent theorem.
- Lu et al. do use (e^{-\beta D/2}), quote
  (\beta<6.75\times10^{-4}\,\mathrm{Mpc}^{-1}), and therefore give the
  numerical conversion (\beta=\gamma/c\) and (2.9809H_0)
  (`text/lu1803.txt:145-166,349-364`;
  `scripts/r127_referee_checks.out:1-4`; [Lu et al.](https://arxiv.org/html/1803.11397v1)).
  However, their limit freezes every true distance at its (\beta=0)
  best fit (`text/lu1803.txt:277-290`).  If (D_i) is profiled, every
  (\beta\ge0) can be absorbed exactly into
  (D_{\rm eff}=D_i e^{\beta D_i/2}), as explicitly checked in
  `scripts/r127_referee_checks.out:7-10`.  The (2.98H_0) figure is therefore
  a fixed-distance benchmark, not a robust BBH-only limit.  GW170817's EM
  distance breaks this degeneracy, but only at the much weaker scale of about
  (14.08\times10^{-3}\,\mathrm{Mpc}^{-1}\simeq62H_0)
  (`text/lu1803.txt:393-433`).
- The constant-cosmic-time friction calculation gives ratios 1.197 at
  (z=0.5), 1.316 at (z=1), and a high-redshift limit 1.612
  (`scripts/r127_referee_checks.out:12-16`).  The cited GWTC-3 result
  (\Xi_0=1.2^{+0.7}_{-0.7}) is correct for a flat prior at 68% HDI
  ([Mancarella et al.](https://arxiv.org/abs/2203.09238)), so (\gamma=H_0)
  is compatible at this coarse one-parameter level.  It is not a fit of E2,
  because the (\Xi(z)) shape and population/cosmology nuisance parameters
  were not refit.
- (G_\gamma(0,k)=1/k^2) and the negligible far-off-cone lab correction are
  confirmed (`scripts/r127_checks.out:38-46,81-83`).  But the fixed PPN task is
  not completed: E2-h is not supplied as a nonlinear conservative metric
  theory from which (\alpha_1,\alpha_2) can be read, and the worker expressly
  leaves noise-fed second order open (`R12-7_report.md:140-145`).  Smallness of
  one linear moving-source dipole is useful evidence, not a derivation that
  both PPN parameters “pass.”  The quoted slow drag is therefore a tentative
  linear-model effect, not yet a controlled prediction of a complete theory.

## 5. Energy budget and the reason for OPEN

**The arithmetic is reproduced, but the word “forces” must remain
conditional.**  At (\gamma=H_0), inserting the R11-5 form
(\rho_{GW}=\epsilon L\hbar c/(\pi^3\ell^4)), E-H5, and the assumed dustlike
sink factor (1+\gamma/(3H)=4/3) gives exactly
(\epsilon<4.89\times10^{-17},8.13\times10^{-12},5.19\times10^{-9},
3.32\times10^{-6}) (`scripts/r127_referee_checks.out:18-22`).  Optimizing over
(0<\gamma\le H_0) places the least burden near
(\gamma\simeq0.037)-(0.040H_0) and relaxes the endpoints only to
(6.18\times10^{-17})-(4.18\times10^{-6}), so the qualitative suppression
problem remains.

Those values are not model-independent consequences of E2.  They inherit the
unfixed R11-5 normalization/tensor weights, the Isaacson-gravitation premise,
and a sink dilution law that the string model does not derive
(`R12-7_report.md:36-39,103-108`).  They correctly show that E2 has not removed
R11-5's open coefficient and near-cone trade-off; they do not by themselves
exclude or fully specify E2.  Independently, the missing tensor CQ dilation,
gravitating sink completion, and PPN calculation already prevent `VIABLE`.

## 6. Reading

**OPEN is confirmed.**  `EXCLUDED` does not follow because the local E2-h
linear propagator is a causal stationary spectral escape and no stated bound
is violated for every (\gamma).  `VIABLE` does not follow because the fixed
rule demands an explicit stationary model passing every item, whereas the
submission has only a scalar ideal-meter bank, a non-gravitating toy bath, no
Bianchi-compatible field completion, and no derivation of the PPN parameters
(`TESTS.md:4531-4542`; `R12-7_report.md:91-108,140-145`).

## Strongest correct statement

For each fixed preferred-frame scalar mode, the supplied positive finite bank
has bounded H-T excess and realizes the desired regulated near-cone spectral
slopes, while the retarded telegraph propagator is hyperbolic, light-cone
causal, boost-stable, and exactly Newtonian at zero frequency; a classical
outgoing Lamb string can realize the corresponding noiseless Ohmic boundary
friction for a toy mode, and the naive spatial-TT-only modification is
generically acausal at (O(\gamma)).  At (\gamma\lesssim H_0), GW speed,
binary-pulsar scaling, static/laboratory response, and current coarse siren
comparators pose no demonstrated conflict, but Lu et al.'s (2.98H_0) number
is only a fixed-distance benchmark and the PPN test is not closed.  Conditional
on R11-5's spectral normalization, gravitating Isaacson content, and a
dustlike gravitating sink, the dark-energy budget again demands extreme
near-cone suppression; because the full spin-2 CQ dilation, conserved
gravitating bath, and nonlinear preferred-frame completion are absent, E2 is
a strengthened stationary spectral construction, not yet a viable theory, and
the fixed reading remains **OPEN**.
