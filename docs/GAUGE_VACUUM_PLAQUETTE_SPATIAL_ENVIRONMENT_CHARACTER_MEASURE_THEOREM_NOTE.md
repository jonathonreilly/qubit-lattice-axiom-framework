# Gauge-Vacuum Plaquette Actual Spatial-Environment Character Measure

**Date:** 2026-04-17; actual-environment derivation and computation
2026-07-10.
**Type:** bounded_theorem
**Claim scope:** on the finite periodic three-dimensional `L_s=3` `SU(3)`
Wilson lattice, for one marked spatial plaquette and any `beta>0`, the
normalized character coefficients of the actual 80-plaquette unmarked
environment obey an exact marked-factor deletion identity.  At `beta=6`, the
primary runner computes the low-rank coefficients by two independent
finite-volume Markov chains: a full-Wilson deletion estimator and a direct
80-plaquette environment estimator.  Identification of those static boundary
coefficients with the algebraically stripped two-slice source residual remains
an open operator-compression gate.
**Status authority:** independent audit lane only.  The claim type above is a
source-side proposal; this note does not set or predict its audit verdict or
effective status.
**Primary runner:**
`scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py`
**Historical bounded single-link packet runner:**
`scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py`

The exact support theorem is a finite-volume Wilson-integral identity, not a
thermodynamic-limit claim.  The quoted `beta=6` numbers are computed lattice
inputs with block-jackknife errors, not exact arithmetic values.  No canonical
plaquette comparator, fitted selector, generic positive `rho`, or single-link
Wilson coefficient is used to derive or tune them.

## 1. The gap this revision closes

The former runner computed the normalized **single-link** coefficients

`c_(p,q)(6)/(d_(p,q)c_(0,0)(6))`

and inserted them into a finite diagonal packet.  That was a bounded packet,
but it was not the full spatial environment.  In particular,
it did not establish

`R_beta^env = C_(Z_beta^env)`

for the actual unmarked Wilson integral.

This revision starts from that integral.  It derives its Fourier coefficients
without assuming the residual spectrum and evaluates the first channels with
two different probability measures.

## 2. Actual unmarked environment

Let `Lambda=(Z/3Z)^3`.  There are 81 positive-direction spatial links and 81
unoriented elementary spatial plaquettes.  Fix a marked plaquette `m`.  For a
link configuration `U`, write its marked holonomy as `W_m(U)` and define

`w_beta(W) = exp[(beta/3) Re Tr W]`.

With normalized product Haar measure `dU`, the full Wilson partition function
is

`Z_full(beta) = int dU prod_(p in P) w_beta(W_p(U))`.

The unmarked environment boundary density `Z_beta^env(W)` is characterized by
the push-forward identity

`int_SU(3) dW Z_beta^env(W) f(W)`

`= int dU f(W_m(U)) prod_(p != m) w_beta(W_p(U))`                     `(2.1)`

for every continuous class function `f`.  This is the actual 80-active-
plaquette environment around the marked plaquette.  It is not a single-link
integral and it does not tie symmetry-related internal links.

Global simultaneous conjugation of all 81 link variables preserves product
Haar measure and every unmarked Wilson factor while conjugating the marked
holonomy.  Hence `Z_beta^env` is central.  Lattice reflection through the
marked plaquette, followed by link-orientation inversion, is a Haar-measure-
preserving bijection that sends `W` to `W^dagger`; the real Wilson branch gives

`Z_beta^env(W)=Z_beta^env(W^dagger)`.

Define its character coefficients by

`Z_beta^env(W) = sum_lambda d_lambda z_lambda^env(beta) chi_lambda(W)`

in the Peter-Weyl sense, and normalize

`rho_lambda^env(beta)=z_lambda^env(beta)/z_0^env(beta)`.

## 3. Theorem 1: exact marked-factor deletion identity

Let angle brackets with subscript `full` denote expectation under the
normalized full Wilson measure

`dP_full(U)=Z_full(beta)^(-1) prod_p w_beta(W_p(U)) dU`.

For every `SU(3)` irrep `lambda`, equation (2.1) with
`f=conj(chi_lambda)` gives

`d_lambda z_lambda^env(beta)`

`= int dU conj(chi_lambda(W_m)) prod_(p != m)w_beta(W_p)`

`= Z_full(beta) <conj(chi_lambda(W_m))/w_beta(W_m)>_full`.          `(3.1)`

For the trivial character,

`z_0^env(beta)=Z_full(beta)<1/w_beta(W_m)>_full`.                   `(3.2)`

Dividing (3.1) by (3.2) proves

`rho_lambda^env(beta)`

`= <conj(chi_lambda(W_m))/w_beta(W_m)>_full`

`  / [d_lambda <1/w_beta(W_m)>_full]`.                             `(3.3)`

This is an exact finite-volume identity.  It turns the boundary-conditioned
80-plaquette integral into a ratio in the positive full Wilson ensemble.  It
contains no supplied environment coefficient.

Translation and cubic-orientation symmetry make the right-hand side the same
for every plaquette.  Therefore averaging its numerator and denominator over
all 81 plaquettes preserves the numerator and denominator expectations and
reduces variance.  Their finite-sample ratio need not itself be unbiased.
This all-plaquette averaging is used by the primary estimator.

## 4. Theorem 2: direct environment estimator

Normalize the 80-plaquette measure obtained by deleting the marked factor:

`dP_env,m(U) = [z_0^env(beta)]^(-1)
                prod_(p != m) w_beta(W_p(U)) dU`.

Equation (2.1) immediately gives a second exact identity,

`rho_lambda^env(beta)
 = (1/d_lambda)<conj(chi_lambda(W_m))>_(env,m)`.                    `(4.1)`

The runner samples (3.3) and (4.1) in independent chains, with distinct seeds,
hot/cold initial states, and four marked plaquettes spanning different
positions/orientations.  Agreement of the two spectra is a discriminating
test of the deletion identity and of the implemented 80-plaquette action.

## 5. Open operator-compression gate and doubled-slice discriminator

The static identities above do not by themselves prove

`R_beta^env=C_(Z_beta^env/z_0^env)`.

The actual one-step Wilson kernel is a two-boundary object.  After the marked
spatial half-weights and four marked mixed-link factors are deleted literally,
it still contains two sets of 80 unmarked spatial half-weights, 77 unmarked
mixed-link weights, and integrations over both slice configurations.
Compression to the marked class sector need not commute with deleting factors
before compression.  In particular, the retained mixed-kernel theorem sends
nonmarked links to the trivial channel only when the function being integrated
is independent of them; the unmarked spatial plaquette weights violate that
hypothesis.

The companion runner
`scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py`
therefore constructs the literal doubled-slice factor-deleted weight rather
than replacing it by (2.1).  Its exact census is:

- 80 incoming and 80 outgoing spatial half-plaquette factors;
- 77 nonmarked mixed-link factors;
- both 81-link slice integrations.

It measures the tracked character-basis matrix without assuming diagonality.
At the production packet, all off-diagonal entries are consistent with zero,
but only at a maximum significance of `1.77` standard errors.  Its normalized
diagonal estimates are

| irrep | literal doubled-slice deletion diagonal | block-jackknife error |
|---|---:|---:|
| `(1,0)` and `(0,1)` | `-0.01237` | `0.01864` |
| `(1,1)` | `-0.00238` | `0.01635` |

Those estimates are too imprecise to establish equality with the static
fundamental coefficient `0.04079 +/- 0.00343`, and literal deletion is not yet
a proof of algebraic stripping after source-sector compression.  The companion
is a discriminator and blocker-localization artifact, not a closure
certificate.

The remaining exact task is to define the marked-class compression map for the
full two-slice Wilson kernel, form

`R_stripped=(D_beta^loc)^(-1) M_(beta/2)^(-1)
             (P_cls T_beta P_cls^*) M_(beta/2)^(-1)`,

and either derive its integral kernel or compute its character matrix with
controlled truncation and covariance.  Only then can its spectrum be compared
to Sections 3--4 without repeating the original identification by naming.

## 6. Independent `beta=6` computation

The primary runner uses four full-Wilson chains and four direct-environment
chains.  Each chain has 900 thermalization sweeps followed by 2400 measurement
sweeps sampled every four sweeps.  Two chains in each family start cold and
two start hot.  Uncertainties come from 12 consecutive blocks per chain,
combined in a delete-one-block jackknife for the coefficient ratios.

The full-Wilson deletion estimator gives:

| irrep | `rho_lambda^env(6)` | block-jackknife error | old single-link packet |
|---|---:|---:|---:|
| `(0,0)` | `1.000000` | normalization | `1.000000` |
| `(1,0)` and `(0,1)` | `0.040787` | `0.003432` | `0.422532` |
| `(1,1)` | `-0.000658` | `0.001230` | `0.162260` |
| `(2,0)` and `(0,2)` | `0.001458` | `0.001444` | `0.135962` |

The exact coefficients are real and conjugation-symmetric.  The raw complex
estimators retain their imaginary fluctuation as a diagnostic; it is
consistent with zero within the reported errors.  The `(1,1)` and `(2,0)`
channels are also statistically consistent with zero, so this computation
does not claim their strict sign.

The independent direct 80-plaquette estimator gives:

| irrep | direct `rho_lambda^env(6)` | block-jackknife error |
|---|---:|---:|
| `(1,0)` and `(0,1)` | `0.047235` | `0.01165` |
| `(1,1)` | `0.002020` | `0.003283` |
| `(2,0)` and `(0,2)` | `0.000899` | `0.004197` |

Across the five nontrivial displayed channels, the maximum difference between
the two estimators is `0.76` combined standard errors.  The deletion estimate
differs from the former single-link packet by `111` standard errors in the
fundamental channel and `132` standard errors in the adjoint channel.  The old
packet is therefore a useful control but is not the physical environment.

## 7. Runner checks

Command:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py
```

Expected summary:

```text
SUMMARY: PASS=21 FAIL=0
```

The checks include:

- exact `SU(3)` character dimensions at the identity;
- a deterministic Weyl-Haar `beta=0`/marked-only control in which every
  tracked nontrivial character moment vanishes;
- the 81-link/81-plaquette census and four incidences per link;
- equality of the local Metropolis action change and a full Wilson-action
  recomputation;
- unitarity and unit determinant of every proposal type;
- normalization, reality, and conjugation symmetry of the coefficient packet;
- hot/cold full-chain and direct-environment marked-face agreement,
  nondegenerate acceptance, direct-spectrum reality/conjugation checks, and
  per-chain block lengths above ten estimated autocorrelation times;
- enforcement of the fixed four-chain minimum production protocol so reduced
  exploratory runs cannot emit the audit certificate;
- statistical separation from the single-link packet;
- agreement of the full-Wilson deletion and direct 80-plaquette spectra.

Companion discriminator command:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py
```

Expected summary on the bounded production packet:

```text
SUMMARY: PASS=6 FAIL=0
```

## 8. Dependencies

- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the retained linkwise temporal-gauge factorization used to construct
  the doubled-slice discriminator; it does not supply residual identification.
- [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
  defines the bounded source-sector operator-stripping target.  This note does
  not import that row as a proof of the missing compression identity.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the retained finite character/convolution convention for the
  tracked discriminator packet.

The former finite single-link coefficient note is a non-load-bearing control,
not a dependency of the derivation.

## 9. What this closes and what remains

This note closes, on the stated finite periodic Wilson surface:

- the derivation of the actual unmarked environment coefficient estimator;
- the independent low-rank `beta=6` computation from the 80-plaquette action.

It does not claim:

- exact-arithmetic values for the displayed statistical coefficients;
- equality of the static environment coefficients with the algebraically
  stripped two-slice source residual spectrum;
- all-weight numerical evaluation or a convergence rate in irrep weight;
- a thermodynamic/infinite-spatial-volume limit;
- the `beta` derivative of the environment coefficients;
- a completed Perron solve or an analytic canonical plaquette value;
- repo-wide repinning of the plaquette value or any audit-status change.
