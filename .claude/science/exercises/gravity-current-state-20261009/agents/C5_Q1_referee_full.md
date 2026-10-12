# C5/Q1 independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

The exact core is sound: a configuration-diagonal coupling to orthogonal
sprinkling labels produces a random-unitary light channel after the substrate
is traced out, and with the Poisson weights this reproduces the RZ intensity
variance.  The worker's campaign-level label needs narrowing, however.  The
FIXED wording does not restrict the substrate to fixed Poisson magnitudes,
uniform final-state amplitudes, substrate-only later dynamics, or circular
Gaussian one-mode noise (`TESTS.md:2345-2354`).  Structured complex amplitudes
and more general joint coherent dynamics therefore remain inside the stated
class unless it is explicitly narrowed.  Under the FIXED readings the result
is **INCONCLUSIVE, leaning FAIL**; **FAIL (bounded)** is established only for
the subclasses identified below.

## 1. Tracing out the substrate

**Confirmed, with scope corrections.**  In the direct-integral/configuration
basis used by the worker, the controlled evolution

\[
U=\int^{\oplus}d\mu(P)\,|P\rangle\!\langle P|\otimes U_P
\]

gives

\[
\rho_L=\int d\mu(P)\,|\psi(P)|^2U_P\rho_0U_P^\dagger .
\]

This is exact (with the `|P>` understood as a generalized basis on a
non-atomic configuration space), and all phases of `psi` disappear
(`Q1_report.md:65-80`; `q1_A_toy_theorems.out:1-4`).  It is the classical
**Poisson** average, and hence has the particular RZ mean and variance, only
when `|psi(P)|^2=1` relative to the Poisson reference measure.  Arbitrary
magnitudes change the ensemble.  The two-weight counterexample in
`q1_referee_checks.out:1-4` changes the mean and intensity while leaving the
same two branch maps.  Thus “any phases” is correct; “any amplitudes give
RZ's value” is not.

This is a natural reading of “one classical sprinkling per branch,” but it is
not the unique reading of a quantum event substrate.  It excludes
nonorthogonal substrate states, off-diagonal transitions between configuration
labels during propagation, and later joint light-substrate erasure.  Those
possibilities are not excluded by the FIXED Q1 statement itself.

The no-signalling corollary is correct and is actually stronger than stated:
every trace-preserving operation on the substrate alone leaves the light
marginal unchanged (`Q1_report.md:90`; `q1_A_toy_theorems.out:2-4`).  It does
not cover a later **joint** light-substrate unitary.  An explicit controlled
unitary can undo each `U_P` and output the same chosen light state in every
branch; the finite-dimensional check has errors below `4e-16`
(`q1_referee_checks.out:6-9`).  This eraser is highly tuned, but it disproves
the claim that nonunitary projection is logically necessary without the
substrate-only restriction.

The DFS criterion also needs precision.  A random-unitary channel is unitary
on a code subspace only when every `U_P^dagger U_Q` acts as a scalar there; for
one specified input it is enough that all `U_P|chi>` are collinear.  Nonzero
RZ variance rules out the latter for the tested displaced vacuum/source mode.
White, carrier-blind noise is strong evidence against a useful observed-mode
DFS, but it is not by itself a proof excluding every code subspace; that needs
the Weyl-displacement representation or a full covariance-support argument
(`Q1_report.md:92-95`).

With the fixed Poisson weights and the scalar-to-photon/readout bridge, the
identity `E|alpha|^2=|E alpha|^2+Var(alpha)` is exact, so the RZ controlled
bound gives `Gamma_B <= exp(-43986)` for the tested one-second/one-Gpc case
(`Q1_report.md:82-84,97-106`; `q1_C_physical.out:3-8`).  It inherits all of
RZ's stated qualifications (`RZ_referee.md:9-15`).

## 2. Coherent projection and Gaussian noise

**The formulas are confirmed; the necessity and physical transfer claims need
qualification.**  Projection onto the initial normalized substrate state
produces the unnormalised light vector `E[U_P chi]`, and

\[
\|E X\|^2=E\|X\|^2-E\|X-EX\|^2=1-E\|X-EX\|^2
\]

for `X=U_P chi`.  The worker's number reproduces exactly
(`Q1_report.md:114-120`; `q1_A_toy_theorems.out:6-7`), and an independent
finite-dimensional check agrees to displayed precision
(`q1_referee_checks.out:11-13`).  This “variance” is the bounded Hilbert-space
variance of normalized branch states, not the unbounded classical RZ field
variance `V`.

For one mode with proper circular complex Gaussian displacement noise,
`E|delta|^2=V`, the exact normalized output amplitude is indeed
`2 Psi/(2+V)`, with the worker's prefactor as written
(`Q1_report.md:123-148`).  Independent deterministic Gauss-Hermite quadrature,
which does not share the worker's Monte Carlo path, gives relative vector
error `7.4e-6` and the predicted complex amplitude to `3e-10`
(`q1_referee_checks.out:15-18`).  The original seeded checks rerun byte-for-byte
apart from paths (`referee_rerun_A.out:9-14`).

The saved sprinkling comparison is reproducible.  At the four retained times,
the empirical and same-covariance Gaussian recombination probabilities are
`0.1426/0.1400`, `0.0908/0.0773`, `0.0406/0.0359`, and `0.0444/0.0357`
(`q1_B2_surrogate.out:4-23`).  This is reasonable one-mode, accessible-epsilon
support for the surrogate.  The amplitude estimator is much noisier, and the
later rows underflow or have unresolved means (`q1_B2_surrogate.out:24-38`).
It is not an asymptotic Gaussian theorem.

The physical “extinction by `exp(-43985)`” additionally assumes that RZ's
band-integrated scalar variance projects into the same normalized photon mode,
that the many-emitter covariance makes that mode proper circular Gaussian,
and that `V_ph=nbar N_B/S`.  The report itself marks circularity and the
inter-emitter step as argued (`Q1_report.md:150-169,311`).  Total in-band noise
spread among orthogonal frequency/angular modes is not automatically the
single-mode `V` in the theorem.  Thus extinction is exact under the stated
one-mode Gaussian bridge, not for every coherent recombination in Q1.

## 3. Structured complex amplitudes

**The one-mode mathematics is confirmed, with two corrections to its
interpretation.**  Expanding Fock components for all source strengths forces
`g_{-n}(r)=Psi_1^n r^{-n}g_0(r)`; square integrability then forces `g_0=0` for
`r<|Psi_1|` (`Q1_report.md:174-183`).  The explicit factor
`x/(x-Psi_1)` has exactly those angular coefficients
(`q1_referee_checks.out:20-26`).  The supplied quadrature reruns exactly and
finds unit fidelity for the tested strengths with finite norm
(`q1_D_structured_phase.out:1-8`; `referee_rerun_D.out:1-8`).

The magnitude-only impossibility is valid only for the stated nonzero-mean,
circular-Gaussian, `L2`, all-source-strength problem; it is not a theorem for
arbitrary noise laws or zero target mean.  More importantly, an
input-dependent postselection success probability is not itself a violation
of the Born rule: ordinary postselection has exactly such probabilities.  If
the successful final condition is imposed deterministically and every output
is renormalized, the resulting effective evolution is nonlinear and not a
trace-preserving standard quantum channel.  That is the precise price.  The
construction is also source/geometry/target tuned and only one-mode; its
finite-mode extension and field limit are not closed (`Q1_report.md:185-200`).

These structured amplitudes belong inside the broad FIXED class.  Q1 asks for
an “explicit coherent-substrate rule” and does not preregister uniform
amplitudes or ordinary unitary dynamics (`TESTS.md:2345-2353`).  The
construction is not a PASS—it lacks a source-independent multimode field rule
and negligible-decoherence proof—but its unclosed extension prevents a FAIL
for the entire stated class.

## 4. Positive-energy Lorentz-invariant vacuum and Poisson statistics

**A narrower spectral statement is correct; the uniqueness/no-scattering
claim is overbroad.**  For future null photon momenta, the worker's
`q=k-k'` satisfies `q^2=2 omega omega'(1-cos theta)>=0`, so noncollinear
transfer is spacelike (`Q1_report.md:202-205`; `q1_referee_checks.out:28-33`).
If a local substrate operator acts on a translation-invariant vacuum obeying
the spectrum condition, its Wightman spectral measure has future-cone support.
That excludes Born-order absorption of noncollinear spacelike `q`.  A gap (or
an explicit absence of massless null spectral weight) is still needed to
exclude the collinear-null channel; the report includes the gap only in its
all-orders bullet and then states the conclusion too generally
(`Q1_report.md:206-210`).  A static lens also breaks spatial translation, so
the below-gap energy argument must be stated separately.

The spectrum condition does **not** forbid literal on-shell
`gamma gamma -> gamma gamma`; that process exists in positive-energy,
Poincare-invariant QED and has been observed by
[ATLAS](https://arxiv.org/abs/1904.03536).  The defensible statement here
is instead about one photon transferring momentum to a substrate excitation
from its vacuum.  Nor does the spectrum condition alone prove that every
noise-free substrate is a vacuum: transparent sectors, symmetry-forbidden
couplings, spectral holes on only the relevant transfer shell, quantum-error
correction/joint erasure, and nonorthogonal event representations remain
unexcluded.

The no-white-vacuum two-point statement is correct under its bridge.  A local
density operator's connected Wightman transform is supported in the future
cone, and its symmetrized transform in the union of future and past cones,
whereas exact Poisson density covariance `rho delta^4(x)` has constant Fourier
transform and hence spacelike support (`Q1_report.md:212-214`).  This rules out
identifying an exact Poisson random measure with that local operator's
symmetrized vacuum covariance.  It does not by itself rule out Poisson
**measurement outcomes/POVM events**, nor does a two-point argument establish
all higher point-process statistics.  The statement that every normal
translation-invariant state is a mixture of vacua is also not established in
the packet (`Q1_report.md:214`).

Accordingly, the N1/N3/N7 no-go checks fail: fewer than five genuinely closed
alternative mechanisms are supplied; locality, a density-operator bridge,
translation invariance, and a gap/no-null-weight condition are hidden
hypotheses; and the tuned joint-unitary eraser is a concrete counter-route.
P-Q1 is a sufficient candidate price, not “the only noise-free quantum
substrate.”

## 5. Matter decoherence, regional sensitivity, and the side finding

**The arithmetic and toy sensitivity are reproducible; the matter-decoherence
conclusion is not proved.**  The ages, needle dimensions, and particle counts
are arithmetically consistent (`q1_C_physical.out:16-26`).  But the decisive
premise—that massive matter has the same RL4 scalar variance rate at the
shared `ell_k`—is explicitly only suggested (`Q1_report.md:230-236,314`).
Field variance is not yet a theorem for environmental-state distinguishability,
the `10^68` CMB photons are not shown to interact independently with the
relevant microstructure, and no record-production channel is constructed.
Hence this estimate cannot establish decoherence at RZ's level.

The region-resampling statistic is correctly implemented as
`s_R=E|phi_P-phi_P'|^2/(2 Var phi)` (`q1_E_region_sensitivity.py:1-9,54-70`).
The saved runs give near-source `s_R=0.18-0.37` at `epsilon=1/2` and
`0.14-0.25` at `epsilon=1/4`, while an off-axis ball is at most `0.001`
(`q1_E_eps05.out:4-7`; `q1_E_eps025.out:4-7`).  An independent 120-realization
rerun gives the same directional result, near-source `0.19-0.47` versus
off-axis at most `0.001` (`referee_rerun_E_eps05_n120.out:4-7`).  This shows
that the toy scalar readout is sensitive to resampling roughly one event in an
early near-source region.  It does not show that matter records that event,
and the region is centered at `t=1` with radius `0.5`, whereas the source is
turned on at `t=0`; “at the turn-on edge” is not literal
(`q1_E_region_sensitivity.py:15-18,54-55`).  The provided copy is also not
self-contained: `rl2_core.py` requires an omitted `RL1` data file.

The side finding is directionally correct and reproducible
(`q1_B_realizations.out:3-26`; `referee_rerun_B.out:3-26`).  The typical and
variance growth slopes agree to at worst about `3.4%`, not strictly `3%`
(`0.770` versus `0.796` at `epsilon=1/8`).  The normalized fourth moment falls
`103 -> 7.8 -> 3.4 -> 2.4`, toward the proper circular-Gaussian value `2`, but
the accessible data do not prove the physical-`epsilon` limit and the
`epsilon=1` variance level is still strongly tail dominated.

## 6. Verdict under the FIXED readings

The FIXED **FAIL** condition is met exactly, conditional on RZ's controlled
physical bridge, for the orthogonal configuration-diagonal model with fixed
Poisson branch weights when the substrate is traced out, and for any later
trace-preserving substrate-only dynamics.  Uniform initial/final amplitudes
with proper circular Gaussian noise also fail by exact one-mode extinction,
conditional on the same-mode photon bridge.  The condition is **not** met for
the full stated coherent-substrate class: arbitrary magnitudes do not retain
the Poisson ensemble, joint unitary erasure is possible in principle,
structured one-mode amplitudes have an explicit exact construction, their
multimode field extension is open, and matter-induced decoherence at RZ's
level is only conjectural.  Since no supplied construction satisfies all PASS
requirements either, the correct overall FIXED result is **INCONCLUSIVE,
leaning FAIL**.

## Strongest correct statement

For a quantum substrate represented by orthogonal sprinkling labels, coupled configuration-diagonally so that branch `P` applies `U_P`, and populated with the fixed Poisson Born weights, tracing out the substrate—or applying any later trace-preserving operation to the substrate alone—gives exactly the Poisson random-unitary channel, so the light intensity contains `|Psi|^2+V` and inherits RZ's controlled `ln(N_B/S)>=43986` exclusion in RZ's bounded source/readout/bridge scope; projecting back onto the initial substrate instead has success probability `1` minus the Hilbert-space branch variance, and for a single proper circular-Gaussian displacement mode yields the exact normalized amplitude `2 Psi/(2+V)`, hence extinction when that mode inherits RZ's variance.  These results prove FAIL for those subclasses, but not for the whole FIXED Q1 class: structured complex amplitudes and tuned joint-unitary erasure remain admissible counter-routes, the positive-energy argument only excludes spacelike absorption for a local translation-invariant vacuum (with a gap/no-null-weight condition for complete silence), and the matter-decoherence estimate is not a theorem.  The strongest campaign-wide verdict is therefore **INCONCLUSIVE, leaning FAIL**.
