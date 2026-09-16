# Premises, dependency graph and boundary stress tests

The dependency graph is: supplied clock jump law + supplied g/delta + Poisson identity -> calibration and moment bounds -> exact coupled transfer consistency -> strong physical product limit; classical theta product + calibration -> all-mode floor -> compactness -> norm resolvents -> physical spectra and Gibbs operators. The second theorem depends provisionally on the first. No native formation law is a node in this graph.

| Premise | Role | What happens if removed |
| --- | --- | --- |
| Fixed finite spatial complex and finite matter dimension | Compact rotor resolvent, finite multiplier bounds, trace majorant | Thermodynamic conclusions need new uniform estimates |
| Fixed positive supplied g | Unique calibration, elliptic kinetic floor | No uniform g->0 or g->infinity statement here |
| N->infinity and delta->0 | Vanishing low-mode error and removal of modular Gauss aliases | Fixed N remains a different finite-clock theory |
| Integer commuting charge labels and gauge-compatible finite Laurent matter generator | Exact physical projectors and eventual no-alias core | Other matter constructions need their own source/core checks |
| Scalar shift making the supplied matter multiplier nonnegative | Positive contractions and min-max comparison | A known fixed-graph scalar energy shift must be tracked |
| Exact normalized Villain spatial factor with y=delta/(2g^2) | Correct limiting cosine potential | Naively taking its beta proportional to delta erases this term |

## N1 — Distinct routes actually tested

Naive sampled rotor scaling was derived and tested: at finite delta g^2 N^2/2 it retains a reduced kinetic coefficient. Exact variance matching removes that specific mismatch. Strong consistency alone was not promoted to ground-state convergence; the separate all-mode product estimate supplies the missing compactness. Commuting-factor substitution is explicitly avoided and an unsandwiched mutation is rejected. These are tests of bounded inferences, not a catalog of physical no-go results.

## N2 — Independent walls

Clock/time matching, spatial thermodynamic control, fixed payload, native dynamics and gapless interacting matter are distinct obligations. Closing the first does not close the others. The new spectral result eliminates high-frequency spectral escape only at fixed finite graph.

## N3 — Hidden assumptions

There is no uniform small-mode expansion over the clock spectrum, no finite Fourier-degree claim for exp(-delta h), no equality of modular and integer Gauss spaces at finite N, and no implicit scalar ground-state uniqueness. All matter and coupling choices are supplied.

## N4 — Residual matching

The proved error on the core is C_f(delta^2+delta/N^2). The all-mode floor has constant2g^2/pi^2. The compactness tail takes j->infinity before the Fourier cutoff grows. Heat traces carry a factor[sum exp(-t a n^2)]^E and therefore do not remain constant as spatial volume grows. These quantitative residuals are the reasons the scope stays finite volume.

## N5 — Resolution and rhetoric

The tiny-gap fault and all three Block03 failed attempts are preserved. More rejected mutations do not establish independence. The language is author proposal and conditional support; no full TOE, fixed-g photon phase, forced axiom update or broad impossibility is claimed.

## N6 — Positive remaining paths

A phase estimate uniform in physical time refinement could pass through this finite-volume identification. Alternatively a direct Hamiltonian argument could bypass Euclidean anisotropy. The repository's finite-clock two-defect route remains live but cannot drop the mixed carrier or mutual phase. Heavy-fermion temporal-run resummation is another distinct necessary bridge worth testing.

## N7 — Strongest objection

An arbitrary joint limit might hide modular states of low energy. The new theta-product floor, positive product decomposition and strong-projector/compact-resolvent argument directly address that objection. They do not address collective states whose spatial support grows without bound. A challenge to the finite result should identify a failure of one of these explicit steps or a hypothesis mismatch.

## N8 — Prior-route comparison

Main already has fixed-N logarithmic temporal matching and inverse-logarithmic spatial Villain matching. Prior personal PR8159 already has other fixed-volume ground/Gibbs rotor limits. Main also has local hard-flux-cutoff dynamics. The bounded additional result here is one exactly calibrated positive transfer on every simultaneous clock/time path, including its finite-volume physical spectral and thermal states. No prior theorem is silently upgraded to a spatial phase result.
