# Neutrino channel family, data-map audit and noise-memory boundary

Candidate research, 2026-10-12. Source pin: `7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`.
No framework axiom, audit status, retained claim, or experimental exclusion is changed.

The positive output is an explicit probability/composition construction and an exact
noise-memory identifiability example. The Daya Bay files also give a reproducible
descriptive shape contrast, but do **not** close the likelihood needed to choose
among arbitrary propagation laws. A newly identified normalization problem in the
ancillary matrix makes direct use of its advertised response convention unsafe.

## Contract and source disposition

The target is finite-dimensional flavor propagation at fixed energy `E>0` and
distance `L>=0`, followed by a specified preparation and Born measurement. Hilbert
space, flavor basis, preparation, measurement, distance clock, dispersion law and
noise are supplied physical hypotheses. Complete positivity below establishes an
operationally admissible channel; it does not establish Lorentz compatibility or
identify a native repository carrier with a neutrino.

`origin/ai/execution:AGENTS.md`, current main's `SCIENCE_WORKFLOW.md`, and the campaign
`OBSERVATION_LEDGER.md` were read. Main was checked at the source pin above. Searches
for Daya Bay, neutrino oscillation, Lindblad, dephasing semigroup, wrapped Cauchy and
conditionally negative definite kernels found no matching Daya Bay inference
implementation in the searched main `docs/` and `scripts/` surfaces. This search is
not a global novelty certificate. Closest inspected main sources are:

- `docs/LOCAL_QUANTUM_COLLISIONS_AND_RAPID_MIXING_BOUNDED_THEOREM_NOTE_2026-10-09.md`:
  explicit supplied ancillas, channels and a controlled generator limit; it does
  not supply the neutrino observable dictionary used here.
- `docs/SINGLE_AXIOM_HILBERT_NOTE.md`: explicitly conditional Hilbert/Hamiltonian/
  Born inputs, not a derivation of them.
- `scripts/ca_oscillation_decoherence.py`: phase averaging in a different causal
  graph toy; no Daya Bay detector map or neutrino channel theorem.

No novelty is claimed for Gaussian dephasing, Schur channels or Poisson kernels.
The useful campaign contribution is their explicit constraint and inference scope.

`FROZEN_PROTOCOL.md` fixes input, normalization, development holdout, uncertainty
and decision roles before this worker calculated spectrum comparisons. Published
oscillation results were already known. None of these comparisons is blind.

## A channel family with the required probability and composition laws

For every fixed energy choose real `h_a(E)` and finite real vectors `v_a(E)`, with
`a=1,...,d`. Put

\[
\Gamma_{ab}(E)=\tfrac12\|v_a(E)-v_b(E)\|^2,\qquad
K_{ab}(L,E)=e^{-i(h_a-h_b)L-\Gamma_{ab}L},
\quad \Phi_{L,E}(\rho)=K(L,E)\circ\rho.                 \tag{1}
\]

Let `B(L)` be a vector of independent real Brownian motions with covariance `L I`.
The diagonal unitary

\[
U_B=\operatorname{diag}_a e^{-ih_a L-i v_a\cdot B(L)}
\]

has `E[U_B rho U_B^dagger]=Phi_(L,E)(rho)`, by the Gaussian characteristic
function. Thus (1) is completely positive and trace preserving, preserves
populations in the propagation basis, and satisfies
`Phi_(0,E)=identity` and `Phi_(L+M,E)=Phi_(L,E) Phi_(M,E)`. The last physical
realization uses stationary independent increments; the channel identity alone
does not certify those environmental increments (see below).

Equivalently, with `H=diag h` and `J_mu=diag_a v_(a,mu)`,

\[
\frac{d\rho}{dL}=-i[H,\rho]+\sum_\mu
\left(J_\mu\rho J_\mu-\tfrac12\{J_\mu^2,\rho\}\right).       \tag{2}
\]

All jumps commute with the supplied `H`, so this model preserves its mean energy
and full propagation-basis population law. Energy exchange, source production,
matter effects, wave packets and a microscopic distance clock remain separate.

For any supplied unitary mixing matrix `U`, prepare
`|nu_alpha>=sum_a U_(alpha a)^* |a>` and measure the orthonormal flavor projectors.
Then

\[
P_{\alpha\to\beta}=
\sum_{ab}U_{\beta a}U^*_{\alpha a}U^*_{\beta b}U_{\alpha b}K_{ab}.
                                                               \tag{3}
\]

It follows from the channel construction that every probability is in `[0,1]`
and the sum over `beta` is one. For electron survival, writing
`w_a=|U_(ea)|^2`, (3) is `sum_a w_a^2+2 sum_(a<b) w_a w_b Re K_ab`.

Two levels give the ledger's candidate without a probability repair:

\[
P_{ee}=1-\frac A2\{1-e^{-\gamma(E)L}
\cos[2\kappa L(E/E_0)^n]\},\quad
A=4p(1-p)\in[0,1],\quad E_0=4\ {\rm MeV}.              \tag{4}
\]

Take `v_1=0`, `v_2=sqrt(2 gamma)`, and `h_1-h_2=2 kappa(E/E0)^n`.
`gamma>=0` may have a separately supplied energy law. `gamma=0,n=-1` is
the coherent inverse-energy control, provided its mass/phase units and values
are supplied. `n=0,+1` are alternative dispersions. `kappa=0` is a monotonic
dephasing survival law. These are conditional rivals, not equally established
neutrino theories. Complete positivity does not select `n`, a mass scale, mixing
amplitude or a noise rate.

**Exact constraint on extending pairwise damping.** For a real symmetric matrix
`Gamma` with zero diagonal, `exp(-L Gamma)` entrywise is positive semidefinite
for every `L>=0` iff

\[
x^T\Gamma x\le0\quad\hbox{whenever}\quad \sum_a x_a=0.       \tag{5}
\]

Necessity follows by differentiating `x^T exp(-L Gamma) x>=0` at `L=0` on
the zero-sum subspace. For sufficiency choose a reference `d` and form
`B_(ab)=Gamma_(ad)+Gamma_(bd)-Gamma_(ab)` for `a,b<d`. If
`z=(x,-sum x)`, then `x^T B x=-z^T Gamma z>=0`. Real Gram vectors for `B`,
with `v_d=0`, obey `||v_a-v_b||^2=2 Gamma_ab`; the Brownian construction proves
sufficiency. The Schur channel is completely positive iff this kernel is positive
semidefinite: its Choi matrix restricted to the span of `|aa>` is `K/d` and
vanishes on the orthogonal complement.

Nonnegative individual rates are therefore insufficient for three flavors.
`Gamma_12=Gamma_23=1, Gamma_13=9` gives `x^T Gamma x=10` for
`x=(1,-2,1)`. At `L=.1` the kernel's least eigenvalue is
`-0.09239500257726928`. Applied to the equal-superposition density matrix, it
produces a negative eigenvalue divided by three. This is a concrete falsifier of
that pairwise model, not of dephasing generally.

## Baseline mixtures and an exact memory ambiguity

The observed mixture over reactor/detector baselines is an average of probabilities
or channels with their proper flux/exposure weights. It is not the channel at the
mean baseline. For example, coherent equal weights at distances `.5s` and `1.5s`
have coherence `kbar(s)=exp(-is) cos(s/2)`. Thus
`|kbar(2)-kbar(1)^2|=sin(.5)^2=0.22984884706593026`.
The averaged channel remains completely positive but is not a semigroup in `s`.
Fitting that envelope as intrinsic dephasing would confuse source geometry with
environmental noise.

There is a stronger limitation even with exact baselines. Choose a dimensionless
step length and `0<r<1`. The bounded phase distribution

\[
f_r(\theta)=\frac{1-r^2}{2\pi(1-2r\cos\theta+r^2)},
\qquad -\pi\le\theta<\pi                              \tag{6}
\]

has `E exp(-in theta)=r^|n|`; expand its two geometric series to verify this.
Consider a two-level unitary step with relative phase `omega+theta`.

1. Draw `theta` once and hold it fixed for all steps of a run.
2. Draw an independent phase with density (6) at each step.

Both have coherence `exp(-in omega) r^n` for **every integer** `n>=0`, and
therefore exactly the same full one-time channel and flavor survival probabilities.
Their local per-step phase is bounded; an unbounded Cauchy energy distribution is
unnecessary for this discrete-domain example. Their multitime processes differ.
An ideal sign reversal between two `m`-step blocks cancels the static phase exactly,
giving echo coherence one. Independent renewed phases give `r^(2m)`.
For `r=.8,m=4`, these are `1` and `0.16777216`, despite identical unintervened
eight-step coherence `0.16777216`.

This is a mathematical intervention witness, not a proposed feasible neutrino
echo apparatus. It shows exactly why one-time propagation data cannot identify
environmental memory in this family. Continuous-baseline equality is not claimed
for the bounded static model. At arbitrary real distances its characteristic
function is not `r^L`.

For a supplied finite causal circuit, placing such random local phase unitaries
on its registers gives trace-preserving, completely positive noise. Local gates
and nearest-neighbor transport preserve the circuit's causal cone. A Gaussian
phase correlation kernel is a Gram kernel
`K_ab=E exp[-i(phi_a-phi_b)]`; this transfers the positivity construction to
an existing carrier. It does not normalize an arbitrary endpoint sum of path
amplitudes: that endpoint map must itself be a channel or an instrument.

## What the Daya Bay inputs establish

Primary input version is [arXiv:2211.14988v1](https://arxiv.org/abs/2211.14988v1),
submitted 2022-11-28. Eight ancillary inputs were acquired on 2026-10-12, and
their SHA-256 identities are frozen in the runner. Full acquisition metadata and
the paper PDF are in the runtime input directory. All comparisons parse only
`Emin,Emax,Ec,Nobs_6AD,Nobs_8AD,Nobs_7AD`. `Npred` is neither parsed nor used.
The published oscillation chi-square grids are not used for rival laws.

The [spectra](https://arxiv.org/src/2211.14988v1/anc/DayaBay_IBDPromptSpectrum_EH1_3158days.txt)
describe energy after nonlinearity correction. The total observed candidates across
all three halls and periods are `5,546,118.00`, consistent with the paper's rounded
5.55 million. Nominal total backgrounds are subtracted per hall/period/bin.
Periods are never pooled into a single detector exposure.

The [response file](https://arxiv.org/src/2211.14988v1/anc/DayaBay_DetectorModel_Etrue_to_Eprompt.txt)
has hash `92a2c1399d0d768eae59ed9aec965dee18942357a5dbedb6a01231b4571e23c8`.
The following are direct arithmetic facts, independently repeated with decimal
arithmetic:

- Shape: `240 x 240`, 50 keV bin convention, nonnegative entries.
- Sum of **all** entries: `0.999999893121`.
- Only 172 columns are nonzero; maximum column sum `0.015555734370`.
- Maximum row sum `0.015443081239`; transposition does not make it stochastic.
- The nominal 3.025 MeV column sums to `0.01525666358`; after dividing that column
  by its sum its mean row energy is `2.9812029348359013` MeV.

The header advertises multiplication of an arbitrary true spectrum by a conditional
response. The supplied matrix does not have that normalization in either orientation.
A jointly normalized simulated migration histogram is a plausible **inference**,
not verified metadata. If that interpretation is correct, its marginal must first
be removed by conditionalization; using the raw matrix multiplies the input spectrum
by that marginal. Zero columns cannot be conditioned. We do not make this repair
silently or fit a law through it.

The same header initially defines true energy as positron kinetic energy plus
1.022 MeV, then later calls the column variable kinetic energy alone. Its support
and near-diagonal structure are compatible with the former convention, but do not
replace a metadata clarification. Moreover, the hall spectra already include a
nonlinearity correction. The correct forward map is the raw response followed by
that correction, with its covariance, rather than blindly applying a response twice.

The [supplement](https://arxiv.org/src/2211.14988v1/anc/supplemental.tex) uses
546 detector/period/bin observations, `(6+8+7)*26`, before fitting 29 free parameters
and nuisance pulls. Hall aggregation supplies only 234 values. The referenced
detector-level arrays `b_i`, four `f_li`, `g_i`, reactor fractions `omega_rd`,
reactor spectral correction shapes and all background/response nuisance covariances
are not supplied by these hall files. A flux-averaged baseline near 500 or 1650 m
does not replace the actual six-reactor/detector mixtures. Thus the collaborator's
fit cannot be reconstituted by treating these corrected hall numbers as independent
Poisson data.

## A limited response-independent shape witness

Under a supplied energy-independent propagation law, a common source spectrum
`f_p(E)` for the reactor components within period `p`, a common response `R_p`,
and energy-independent relative exposures, the signal factorizes:

\[
S_{hpi}=c_{hp}(R_p f_p)_i,
\quad c_{hp}=\sum_{d\in h,r}w_{drp}P(L_{dr}).              \tag{7}
\]

The weights include geometry and exposures. Arbitrary baseline mixtures change
`c_hp` only. The hall-by-energy matrix has rank one and every normalized hall ratio
is constant. This null includes `n=0` **only when gamma is also energy-independent**.
It does not include energy-dependent dephasing with a constant phase.

The frozen whole-bin rule gives an actual normalization window 2.05–7.30 MeV,
low window 2.05–3.80 and high window 6.05–7.30, containing 21, 7 and 5 bins.
The originally named round-number windows cannot be reconstructed exactly from
the published bins; no fractional-bin interpolation is used.
For background-subtracted far counts `F`, near counts `N`, and normalization `W`,

\[
R_B=\frac{F_B/F_W}{N_B/N_W},\quad
D=R_H-R_L,\qquad Q=\frac{F_H/F_L}{N_H/N_L}.             \tag{8}
\]

The pooled-near central results are:

| Period | `D`, percentage points | diagonal-count proxy error | `Q` |
|---|---:|---:|---:|
| 6AD | 3.417811 | 3.201721 | 1.03458092 |
| 8AD | 3.552062 | 1.029589 | 1.03585278 |
| 7AD | 2.776540 | 1.130821 | 1.02795980 |

These are descriptive conditional mismatches, not exclusions or sigma levels.
The proxy uses `Var Nobs=Nobs`, zero cross-bin covariance and fixed background.
It propagates the shared normalization dependence: for example,
`dR_B/dF_i=R_B(1_(i in B)/F_B-1_(i in W)/F_W)`.
The covariance of genuinely corrected histograms instead requires their correction
operator, e.g. `C diag(mu_raw) C^T`, plus background/response uncertainties and
cross terms. The diagonal proxy is neither a proven lower bound nor conservative.

The high/low central ratios would require at least symmetric effective far/near
transfer modulations `|Q-1|/(Q+1)` of 1.70%, 1.76%, and 1.38%, respectively, if
one insisted on matching these central values by two such factors. That is an
algebraic description, not a nuisance bound; statistical fluctuations can also
contribute. Near-hall controls have their own central high-minus-low contrasts
1.67%, 1.13%, and 2.30%, showing why exact common-spectrum cancellation must not
be promoted to a precision assumption. Different reactor fuel mixtures, baseline
oscillations and response residuals are unresolved in this reduced test.

No value of `n`, `gamma`, `A` or `kappa` is selected by this calculation. An
unconstrained energy-dependent transfer can match any positive candidate signal;
therefore a nuisance bound or full likelihood is essential for an exclusion.

## Reproduction, checks and next decisive work

From the campaign checkout:

```bash
python3 .claude/science/physics-loops/observations-to-toe-24h-20261012/agents/neutrino/neutrino_channel_shape_check.py --download
python3 .claude/science/physics-loops/observations-to-toe-24h-20261012/agents/neutrino/independent_ingestion_check.py
```

The first script permits alternate `--inputs` and `--output` paths, checks all input
hashes, and uses one numerical thread. Runtime defaults are under
`/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/neutrino/`.
The captured execution used Python 3.12, NumPy 2.4.1, SciPy 1.17.0 and completed
in under one second. `results.json`, `check.log` and `independent.log` retain the
full numerical output. No detached process was launched.

Explicit matrix exponentiation versus the elementwise channel had zero displayed
error; the semigroup and Kraus-survival discrepancies were at most `2.24e-16` and
`5.56e-16`. Sampled normalized Choi eigenvalues were nonnegative to `1.19e-16`
roundoff. The bounded-phase Fourier check differed by at most `8.89e-16`.
A separate standard-library implementation used decimal ingestion, grouped ratios,
finite-difference derivatives and a closed-form bad-kernel eigenvalue. Its largest
central-statistic discrepancy was `3.13e-16` and its relative proxy-error discrepancy
`1.96e-11`. These finite checks support, but do not replace, the proofs above or
independent review. No interval arithmetic or Lean proof was run.

The initial Python HTTPS download failed because its local certificate bundle was
missing a trusted issuer. System `/usr/bin/curl` succeeded with normal certificate
verification. No input identity was weakened.

The next empirical action is to establish the conditional response normalization,
energy convention and corrected-spectrum transformation, then obtain detector-level
observations/mixtures and nuisance arrays or a collaboration-supported likelihood.
Only then compare the frozen propagation families using a specified covariance and
parameter/nuisance ranges. For the causal-noise connection, the next mathematical
action is to derive this channel from a supplied physical environmental two-point
function and identify a real preparation/intervention/readout that distinguishes
memory. The second task is developed separately in this assigned directory.
