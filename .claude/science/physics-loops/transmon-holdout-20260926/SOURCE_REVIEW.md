# Independent source and protocol review

Status: calibration-only implementation is worthwhile as a reproducible, bounded test of the standard dressed transmon model. The general failure direction is already published and known; this is neither blinded discovery nor evidence establishing a new underlying theory. No held-out values are disclosed in this report. Repository was not modified.

## Source identities

Repository main supplied by supervisor: `e37967e326c2bdb429bd3106d34158bd5420e9c0` (not independently inspected here). Data-source Git pin: `d97280c61c54ca8d54ccf0a8706713130778eb63`. SHA-256 identities for every reviewed local source are in `SOURCE_HASHES.json`.

Primary references:
- Willsch et al., *Observation of Josephson harmonics in tunnel junctions*, Nature Physics (2024), https://doi.org/10.1038/s41567-024-02400-8 . Reviewed supplied full article text and downloaded supplementary information.
- SI: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41567-024-02400-8/MediaObjects/41567_2024_2400_MOESM1_ESM.pdf . Relevant sections II.B, II.C, III.A, III.C and Table S6.
- Data DOI https://doi.org/10.26165/JUELICH-DATA/LGRHUH and pinned CSV https://jugit.fz-juelich.de/qip/josephson-harmonics/-/raw/d97280c61c54ca8d54ccf0a8706713130778eb63/results/Experiment.csv . DOI package points onward to author repository; exact bytes are locally hashed.
- Supplied pinned demonstration notebook source establishes computational units, column ordering and endpoint-mean implementation.

## Necessary corrections and schema

1. CSV row `KIT` corresponds to KIT cooldown 1. It contains `f01` through `f05`, plus `fres1`, `fres2`; higher transitions and additional resonator entries are missing. Predict all three available held-out quantities `f03`, `f04`, `f05`.
2. CSV `f0j` means the total ground-to-j transition frequency in GHz. Table S6 instead tabulates measured j-photon drive frequencies `f0j/j` in GHz. Do not divide CSV f02 before comparing with model total energies. A ±1 MHz variation of the f02/2 drive means ±2 MHz in CSV f02.
3. CSV resonator indexing starts at one: `fres1` is physical f_res,0; `fres2` is physical f_res,1. Calibration cell comparison against Table S6 independently confirms this mapping. The four fit targets are exactly `[f01,f02,fres1,fres2]`.
4. Notebook parameter numerics are frequency units (EC/h, EJ/h, Omega/2π, G/2π in GHz). A Hamiltonian assembled directly from those numbers returns GHz energy differences without a further 2π divisor. The article uses hbar=1 and angular energies, then divides by 2π; do not mix conventions.
5. Material source caveat: SI III.A cooldown-1 description says it uses the dispersive shift measured in cooldown 2 for the model fit. Thus the second CD1 resonator datum embeds a transfer across cooldowns. This is an explicit calibration assumption, not four independently measured contemporaneous CD1 inputs. Record it prominently; do not characterize the input set otherwise.

## Model convention and experimental meaning

Use H/h = 4 EC(n-ng)^2 - EJ cos(phi) + Omega a†a + G n(a+a†) in frequency-valued units, with the complete n matrix in the bare-transmon eigenbasis. Preserve counter-rotating terms and do not substitute nearest-neighbour ladder matrix elements or an RWA. Compute dressed `(k,j)` energies at ng=0 and ng=1/2 and average the corresponding transition differences, as Methods and notebook explicitly do.

The endpoint mean is a published model convention, not a demonstrated measurement protocol for KIT CD1. SI III.C documents extraction of mean frequencies from two controlled charge-parity branches for Köln; it also warns uncontrolled charge drift and unresolved dispersion can cause systematic errors. KIT III.A describes two-tone multiphoton spectroscopy and local line measurements, without equivalent controlled parity averaging. Report both endpoint predictions/dispersion and, if needed, a charge-offset grid sensitivity. A midpoint residual alone must not be portrayed as independent of unknown charge offset. Do not call endpoint values rigorous extrema of the dressed spectrum without checking the intervening ng range.

## Uncertainty and calibration leakage

CSV provides neither uncertainty columns nor a covariance matrix. SI II.B says measured drive frequencies f0j/j have roughly comparable accuracy, of order 1 MHz, and describes ±1 MHz drive-frequency sensitivity tests. This is not a declaration of independent Gaussian 1-sigma errors. No z scores, p-values, chi-square probabilities, or discovery significance are warranted.

A defensible predetermined sensitivity test uses the four corners of ±1 MHz for f01 and f02/2 while maintaining the cavity targets, reports the resulting held-out prediction envelope, and labels it a bounded sensitivity exercise. It is not complete propagation of cavity, charge drift, line-fitting, and cross-cooldown systematics. Report raw residuals in total-frequency MHz and optionally divide by j to compare with drive-frequency accuracy. Distinguish numerical error from experimental error.

Do not load parameters from EJ.csv, EJ2.csv, EJ4.csv, dsigma.csv or ab.csv as independent calibration evidence. They are fitted model outputs. Author standard-model parameters may include weighted use of the full spectrum (SI II.B), so reproducing them is not the requested holdout test. Initialize with broad physically motivated starts using only the four input cells; choose roots using declared physical constraints, calibration agreement and stability, never higher-level residuals. Freeze model, target selection, bounds, truncation tolerances and scoring before opening held-out values. General published failure direction remains prior knowledge regardless of software withholding.

## Level assignments and verification gates

Ascending eigenvalue order does not equal transmon state order because cavity excitations interleave. Use bare product-state overlap for the specific labels (0,0)...(0,5), (1,0), (1,1). The notebook's independent row-wise argmax can assign the same dressed state to different bare labels; check uniqueness, squared overlaps and runner-up margins. Prefer a coupling continuation check from G=0 to fitted G, or an independently implemented one-to-one assignment check. SI II.C explicitly discusses this ambiguity; Fig. S15 shows no avoided crossings for its chosen standard KIT fit, but that does not automatically establish the property for newly calibrated fits.

Increase charge, transmon and photon cutoffs independently enough to show errors below the stated prediction precision. The notebook baseline N=14, M=12, K=9 and its larger N=50, M=20, K=20 comparison are a reproducible reference, not a substitute for checking this fit. Verify all four calibration residuals, root/initialization sensitivity, assignment validity and endpoint differences before interpreting held-out discrepancies.

## Authorized test scope

This tests whether one fixed four-parameter standard transmon plus one resonator Hamiltonian, with adopted endpoint averaging and cross-cooldown calibration transfer, extrapolates from its lowest two transitions and cavity shifts to three additional measured transitions. Exact low-frequency calibration has zero residual degrees of freedom and is not itself predictive success. A failure limits this operational model under these premises; it does not falsify the Hilbert-space or compact-phase machinery generally, uniquely establish Josephson harmonics, or prove any lattice-framework derivation. The prior square/transmon bridge review is not re-audited here.
