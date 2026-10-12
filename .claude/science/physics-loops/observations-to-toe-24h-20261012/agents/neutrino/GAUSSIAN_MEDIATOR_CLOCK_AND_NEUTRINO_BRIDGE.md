# Gaussian mediator environment: clock test and neutrino bridge

Follow-up research, 2026-10-12, source pin
`7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`. All field, state, coupling and apparatus
identifications below are supplied conditional hypotheses. This note changes no
axiom or audit standing and claims no feasible neutrino echo experiment.

The derivation independently checks the coordinator's proposed positive scalar
mass measure. It gives three useful constraints: the mass cutoff does not by itself
regularize a point detector; a regular inertial vacuum of this family gives a
dephasing transient with zero asymptotic exponential rate; and longitudinal clock
visibility probes the symmetric covariance, so it cannot establish the vacuum
spectral condition by itself.

## 1. Supplied field and state

Use natural units and a real Gaussian generalized free scalar with positive measure

\[
d\rho(\mu)=C\mu^{s-1}e^{-\ell\mu}d\mu,
\qquad C>0,\quad s>0,\quad\ell>0.                    \tag{1}
\]

Here the measure is over mass, not mass squared. In the usual mass-squared variable
`z=mu^2`, its density is `(C/2) z^(s/2-1) exp(-ell sqrt z)`. Missing this Jacobian
changes the model. The vacuum two-point function is defined by

\[
W^+(t,\mathbf x)=\int_0^\infty d\rho(\mu)
\int\frac{d^3k}{(2\pi)^3\,2\omega_{\mu k}}
e^{-i\omega_{\mu k}t+i\mathbf k\cdot\mathbf x},
\quad \omega_{\mu k}=\sqrt{k^2+\mu^2}.                 \tag{2}
\]

This is a positive-energy Gaussian vacuum by construction, with the free-field
commutator integrated using the same positive measure. Each mass contribution
vanishes at spacelike separation in the commutator, so the weighted distribution
does too. These statements concern the stipulated continuum field; they do not
derive it from the repository's lattice, admissibility or record primitives.

For two static point charges the supplied linear coupling gives

\[
V(r)=-\frac{q_A q_B}{4\pi r}\int_0^\infty e^{-\mu r}d\rho(\mu)
=-\frac{C\Gamma(s)q_Aq_B}{4\pi r(r+\ell)^s}.           \tag{3}
\]

The sign is the attractive scalar exchange convention. This static kernel fixes
the same spectral measure as (2), but does not fix the environmental state.
Thermal and vacuum Gaussian states have the same free commutator/retarded response
and different symmetric noise. Choosing vacuum is therefore an additional physical
state claim, not a consequence of the static force law.

## 2. A normalized source–clock–readout map

Supply a two-level clock with `H_clock=Omega sigma_z/2`, a normalized real spatial
profile `f_a`, and a centered bath initially uncorrelated with the clock. Let

\[
B(t)=\int d^3x f_a(\mathbf x)\phi(t,\mathbf x),\qquad
H_I(t)=\frac\lambda2 y(t)\sigma_z B(t).                 \tag{4}
\]

The source current on the two clock branches is
`J_±(t,x)=±(lambda/2)y(t)f_a(x)`. An ideal clock pi pulse changes the sign of the
longitudinal coupling in its toggling frame. Control work and pulse fidelity are
apparatus inputs. The scalar coupling must actually distinguish the clock's two
states; a coupling proportional to the identity gives no such signal.

For a common real switching profile define `X_y=int y(t)B(t)dt` and
`N_y=〈X_y^2〉=int dt ds y(t)y(s)〈{B(t),B(s)}〉/2`.
The commutator is a c-number. Its time-ordered exponential has an exact second-order
Magnus form

\[
U_q[y]=e^{i q^2\varphi_y}e^{-iq X_y},
\quad
\varphi_y=-\frac12\int_{t>u}dtdu\,y(t)y(u)\Delta(t,u),
\quad[B(t),B(u)]=i\Delta(t,u).                        \tag{5}
\]

The environmental overlap between charges `q_i,q_j` is

\[
F_{ij}[y]=e^{i(q_i^2-q_j^2)\varphi_y}
e^{-(q_i-q_j)^2N_y/2}.                                \tag{6}
\]

It is a unitary-environment Gram kernel, hence its Schur channel is completely
positive and trace preserving. The real damping has the squared-distance form
proved in the first neutrino report, now in the Gaussian test-function covariance
norm. For the symmetric clock charges the commutator phase cancels and

\[
\mathcal V_y=e^{-\chi_y},\qquad \chi_y=\lambda^2N_y/2. \tag{7}
\]

Prepare `|+x>`, apply the specified coupling and pulses, and measure sigma_x and
sigma_y using final rotations. Their expectations reconstruct the coherence;
with a compensated known phase, the sigma_x outcome probabilities are
`p_±=(1±V_y)/2`. This supplies an explicit preparation/channel/readout map with
normalized positive probabilities, rather than identifying a bare correlation
function with a count rate.

For strict spatial localization choose a compact smooth `f_a`. The numerical
example instead uses a Gaussian profile, whose tails are an explicit detector
idealization; it makes no claim of compact support or an exact apparatus light
cone. Smearing or smooth temporal switching is required for well-defined pointlike
limits. The initially factorized vacuum and switched coupling also matter:
switching and pulses can supply work and create branch-dependent dressing. This
is not an assertion of energy extraction from a stationary ground state of the
fully coupled clock-plus-field Hamiltonian.

## 3. Spectrum, ultraviolet condition and lack of a vacuum Markov rate

Define the unsymmetrized spectrum with the convention
`S^+(omega)=int dt exp(i omega t)〈B(t)B(0)〉`. For a point at rest,

\[
S^+_0(\omega)=\frac{C\theta(\omega)}{2\pi}
\int_0^\omega d\mu\,\mu^{s-1}e^{-\ell\mu}
\sqrt{\omega^2-\mu^2}.                               \tag{8}
\]

The factor `1/(2 pi)` follows by integrating the radial momentum delta function
`2 pi delta(omega-sqrt(k^2+mu^2))` in (2). A spatial Gaussian
`f_a=(2 pi a^2)^(-3/2) exp(-x^2/(2a^2))` inserts
`exp[-a^2(omega^2-mu^2)]` into the integrand. An arbitrary isotropic profile inserts
`|fhat(sqrt(omega^2-mu^2))|^2`.

At low frequency, any normalized regular spatial profile has

\[
S^+_a(\omega)\sim\frac{C}{4\pi}
B(s/2,3/2)\,\omega^{s+1}.                            \tag{9}
\]

At high frequency the **point** spectrum instead satisfies

\[
S^+_0(\omega)\sim\frac{C\Gamma(s)}{2\pi\ell^s}\omega. \tag{10}
\]

Thus `exp(-ell mu)` suppresses the mass mixture but not large momentum at a fixed
mass. A sharp point-detector Ramsey switch still has a logarithmic ultraviolet
divergence. It is incorrect to treat `ell` alone as a full spacetime detector
cutoff. The Gaussian spatial profile used below makes the needed integrals finite.

For vacuum, `S^+(omega<0)=0` and the symmetric spectrum is
`S_N(omega)=[S^+(omega)+S^+(-omega)]/2`. Therefore

\[
\chi_y=\frac{\lambda^2}{4\pi}\int_0^\infty
d\omega\,S^+_a(\omega)|Y(\omega)|^2,
\qquad Y(\omega)=\int y(t)e^{i\omega t}dt.             \tag{11}
\]

For Ramsey over `[0,T]` and a sign reversal at `T/2`, respectively,

\[
|Y_R|^2=\frac{4\sin^2(\omega T/2)}{\omega^2},\qquad
|Y_E|^2=\frac{16\sin^4(\omega T/4)}{\omega^2}.         \tag{12}
\]

When `S^+_a/omega^2` is integrable, as here for `s>0` with the ultraviolet
regularization, the Riemann–Lebesgue lemma gives

\[
\chi_R(T)\to K=\frac{\lambda^2}{2\pi}\int_0^\infty
\frac{S^+_a(\omega)}{\omega^2}d\omega,\qquad
\chi_E(T)\to3K.                                     \tag{13}
\]

The factor three uses the ideal sign reversal and sharp temporal edges, not an
arbitrary finite-pulse sequence. In particular `chi_R(T)/T -> 0`. A constant
positive asymptotic Markov dephasing rate does not follow from this regular
inertial vacuum. This is an exact pure-dephasing statement under (1)–(4), stronger
than reading a formal weak-coupling zero-frequency rate from `S_N(0)=0`.
It is not a prohibition on vacuum transients, other couplings, acceleration,
initial correlations, baths with different infrared measures, or singular limits.

## 4. Which clock observables distinguish which hypotheses

For static real Gaussian noise with covariance `N(t,u)=sigma^2`,
`chi_R=lambda^2 sigma^2 T^2/2` and `chi_E=0`.
For white noise `N(t,u)=D delta(t-u)`, both are `lambda^2 D T/2`.
The two-point switch thus distinguishes these **fixed** kernel families. The
earlier bounded static phase model also gives perfect echo, while its refreshed
phase rival does not. No neutrino flavor reversal apparatus is asserted.

However, every centered real Gaussian classical process with covariance equal to
the quantum bath's symmetric `N` gives exactly (7) for all these longitudinal
clock controls. Even a complete Ramsey/echo filter scan cannot establish the
vacuum's unsymmetrized spectral support with this symmetric clock alone.

A separate allowed transverse matrix element provides a different witness.
Supply a weak interaction `g_perp sigma_x B` and independently prepare the clock
ground and excited states. In the stationary, long-interaction, weak-coupling
limit, transition probabilities per unit time are

\[
\Gamma_{\uparrow}=g_\perp^2 S^+(-\Omega),\qquad
\Gamma_{\downarrow}=g_\perp^2 S^+(+\Omega).            \tag{14}
\]

These signs follow directly by combining the clock's `exp(±i Omega t)` matrix
elements with the bath two-point function. Consequently:

- Vacuum: upward rate zero and downward rate positive when the spectrum overlaps.
- A free thermal KMS state: `Gamma_up/Gamma_down=exp(-beta Omega)`.
- Stationary real classical Gaussian noise alone: equal upward/downward rates,
  because its spectrum is even.

At finite switching time there can be vacuum excitation from the control's energy
input, so a measured finite-time count is not literally the first limiting rate.
One must model the switching response and other backgrounds. A purely diagonal
scalar coupling does not supply `g_perp`; if that matrix element is forbidden,
(14) is unavailable. This proposed apparatus is therefore a conditional clock
spectrometer, not an asserted property of a particular existing clock or neutrino.
The stated comparison also does not exclude every possible classical model with
additional dissipative dynamics.

The distinction between symmetric and asymmetric Gaussian noise spectra is
established context in [Paz-Silva, Norris and Viola, arXiv:1609.01792v2](https://arxiv.org/abs/1609.01792v2).
Only its abstract was inspected here; no theorem is imported to close a missing
condition in the derivation above. [Clerk et al., arXiv:0810.4729v2](https://arxiv.org/abs/0810.4729v2)
was likewise checked as context for quantum noise spectroscopy. No novelty for
the general spectroscopy method is claimed.

## 5. A small reproducible synthetic calculation

Before execution the runner fixes `C=s=ell=lambda=1`, Gaussian spatial width
`a=.25`, and times `.25,.5,1,2,4,8,16`. Units are illustrative natural units;
these are not measured scalar parameters. Static-Gaussian and white rivals are
matched to the vacuum Ramsey exponent at `T=1` only. The fixed `T=4` comparison
is a synthetic diagnostic, not a blind physical prediction.

| Model | Ramsey exponent at `T=1` | Ramsey exponent at `T=4` | Echo exponent at `T=4` |
|---|---:|---:|---:|
| Supplied scalar vacuum | 0.030865865706 | 0.038123936563 | 0.108329831933 |
| Matched static Gaussian | 0.030865865706 | 0.493853851292 | 0 |
| Matched white Gaussian | 0.030865865706 | 0.123463462823 | 0.123463462823 |

The vacuum visibilities at `T=4` are `0.962593632952` (Ramsey) and
`0.897331579006` (echo). The asymptotic exponents are `K=0.0386461108380`
and `3K=0.115938332514`. Echo need not improve coherence in a high-frequency
vacuum spectrum: its extra sign switch changes the filter and injects control work.

`gaussian_clock_check.py` calculates (11) using frequency/mass coordinates and
independently repeats selected integrals directly in mass/momentum coordinates:

\[
\chi_y=\frac{\lambda^2}{8\pi^2}\int d\rho(\mu)
\int_0^\infty dk\,\frac{k^2|\widehat f_a(k)|^2}{\omega_{\mu k}}
|Y(\omega_{\mu k})|^2.                               \tag{15}
\]

Their largest difference is `1.59e-13`; doubling the primary angular quadrature
order changes results by at most `4.24e-15`. The adaptive integration's largest
reported error is `2.26e-11`. These are numerical checks, not interval-certified
bounds. The independent integral uses `mu<=40,k<=24`. For the displayed parameters,
`|Y|<=T`, `omega>=mu,k`, and Gaussian/exponential tails bound the omitted positive
contribution for `T<=16` below `7e-15`. The primary `omega<=60` tail is smaller
using the union `mu>40` or `k>sqrt(2000)`.

At `omega=1000`, the unsmeared spectrum divided by the linear asymptotic (10) is
`0.999998999978`, directly checking that the mass exponential is not a full UV
cutoff. The static mass integral is also independently compared with (3).

Reproduce with:

```bash
python3 .claude/science/physics-loops/observations-to-toe-24h-20261012/agents/neutrino/gaussian_clock_check.py
```

Runtime output is `neutrino/gaussian_clock_results.json` and
`neutrino/gaussian_clock_check.log` in the campaign runtime directory. The script
checks stop markers/deadline and uses one numerical thread; the captured run took
less than one second. No external data are fitted by this runner.

## 6. Moving neutrinos require a separate bridge

If the physical hypothesis is **mass** scaling
`m_i(phi)=m_i[1+a_nu phi/M_*+O(phi^2)]`, the common-fixed-momentum dispersion gives

\[
E_i(\phi)=\sqrt{p^2+m_i(\phi)^2},\qquad
q_i=\left.\frac{\partial E_i}{\partial\phi}\right|_0
=\frac{a_\nu m_i^2}{E_i M_*},\qquad
q_i-q_j\simeq\frac{a_\nu\Delta m^2_{ij}}{E M_*}.       \tag{16}
\]

This verifies the coordinator's proposed leading coefficient under its WKB,
slow-background, ultrarelativistic and common-momentum assumptions. Scaling
`m_i^2` by `1+a_nu phi/M_*` instead gives a factor one-half; the physical coupling
definition must be fixed. Common-energy and common-momentum descriptions agree at
the displayed leading ultrarelativistic phase order after their path conventions
are matched, not by silently substituting either into an exact formula.

An inertial moving path samples

\[
S^+_{\mathbf v}(\Omega)=2\pi\int d\rho(\mu)
\int\frac{d^3k}{(2\pi)^3 2\omega_{\mu k}}
|\widehat f(\mathbf k)|^2
\delta[\Omega-(\omega_{\mu k}-\mathbf k\cdot\mathbf v)]. \tag{17}
\]

For `|v|<1`, the argument frequency is positive except the zero-measure origin
of the massless boundary. With this regular infrared measure the zero-frequency
noise vanishes. For the formal pointlike scalar pulled back to a timelike path,
Lorentz invariance gives `S_v^+(Omega)=gamma_v S_0^+(gamma_v Omega)` in lab time.
Spatial smearing tied to the lab can modify that simple rescaling. The limit
`|v|->1` need not commute with `Omega->0` or a UV cutoff: collinear large-momentum
modes require a separate analysis. A static clock spectrum must not be transplanted
as a neutrino propagation rate.

For real flavor branches use their actual currents
`J_i(t,x)=q_i chi(t)f_i(x-x_i(t))`, production wave packets and detector measurement.
Common paths allow the simpler charge-difference kernel (6). Different mass paths
instead give the covariance norm of `J_i-J_j` and additional commutator phases;
the full unitary-environment overlap is still a positive Gram kernel. Actual
source/detector amplitudes, recoil, packet separation and energy resolution remain
open. No Daya Bay value of `gamma` is predicted or bounded by this note.

If an additional universal mass-charge hypothesis sets every material
`q_A=a m_A/M_*`, the static-force amplitude fixes the combination
`C a^2/M_*^2`. A rest clock with internal mass difference `Omega` then has noise
normalization `(C a^2/M_*^2) Omega^2`; the WKB neutrino normalization is
`(C a^2/M_*^2)(Delta m^2/E)^2`. This is a conditional cross-observable relation,
not a derivation of universality. If `a_nu/a` is free, static gravity data do not
fix neutrino noise. Environmental temperature and the apparatus profile also
remain independently necessary inputs.

The next decisive action is to choose a real clock/probe with an independently
calibrated scalar matrix element and spatial/control response, then use static
source response and held-out visibility or rate asymmetry under a fixed state
hypothesis. Until such a map and uncertainty model exist, the result is a checked
conditional mechanism and a precise measurement design, not an empirical scalar
or neutrino discovery.
