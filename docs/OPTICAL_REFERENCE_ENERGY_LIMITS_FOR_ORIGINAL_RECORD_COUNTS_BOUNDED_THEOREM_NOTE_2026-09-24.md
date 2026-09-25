---
claim_id: optical_reference_energy_limits_for_original_record_counts_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional finite-volume reference energy and spectral-overlap bounds for one supplied original-record
  probe, plus a scoped comparison with a primary optical experiment. No actual photon absorption, finite laboratory
  error certificate or empirical exclusion.
upstream_dependencies:
- minimal_axioms
- original_record_calibration_and_prepared_matter_probe_bounded_theorem_note_2026-09-24
- photon_dispersion_observational_constraints_and_live_formation_response_bounded_theorem_note_2026-09-24
- prepared_original_record_probe_energy_vacuum_response_and_clock_scope_bounded_theorem_note_2026-09-24
- weak_field_wave_packets_from_mobile_record_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/optical_reference_energy_limits_for_original_record_counts_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; no retained audit verdict.

# Optical energy and the original local record response

The previously constructed positive reference-excitation signal does not by
itself describe detection of optical light. Under the same explicitly
conditional photon/clock identification, a small finite lattice has no optical
reference mode. On a sufficiently large lattice, restricting a one-excitation
input to optical reference energies sharply bounds the response of this one
local prepared mark. A bound on mean energy gives a weaker constraint than a
hard spectral band; rare high-energy components cannot be discarded.

The primary optical comparison identifies the remaining source, collective
matter response and physical-time error obligations. It supplies no measured
agreement or disagreement with the framework. Original formation channels,
Gauss-consistent charged preparation and full matter/field dynamics remain
those of the parents. Reference energies, full charged-system energy and
absorbed heat are distinct. Uniform static inequalities do not supply uniform
full-process errors at physical volumes or observation times.

The exact parents are the [weak-field packets](WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[conditional photon timing bridge](PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[prepared original-record probe](ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md) and its
[energy, response and clock scope](PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
All supplied premises and ordered limits of those parents are retained.
Equation numbers are local to each part.

## A. Finite-volume reference energy and conditional optical scale

Use exactly the harmonic dispersion of the photon-observation parent,
SHA acf74cfce461cfbf607f7ba2994ff0a3d5986b9571bf7c5efacecebdf9ab5d7b:
for the equal-period cubic torus, D(k)=4 sum_mu sin²(k_mu/2),
omega(k)=(c/a)sqrt(D(k)). Nonzero transverse Fourier momenta have
k_mu=2pi n_mu/L. The harmonic zero modes are excluded from the transverse
one-excitation family under discussion. This gives the exact lowest nonzero
REFERENCE frequency

    omega_min(L)=(2c/a) sin(pi/L), even L>=6 in this construction.

Proof: each nonzero lattice momentum has at least one component whose circular
integer distance from zero is >=1 and <=L/2; sin is increasing on [0,pi/2].
Thus D>=4sin²(pi/L), attained by a single component +/-2pi/L and either
transverse polarization. Every normalized superposition of these nonzero
one-excitation modes has reference mean energy >=hbar omega_min.
This concerns their reference harmonic excitation energy, not the ordinary
full charged-probe energy already shown to be broad and of order g^-2.

Add ONLY the same physical photon/clock/proper-spacing/cosmology identifications
used for the archival LHAASO2024v2 ML/MINOS conversion. The necessary
unknown-orientation bound a<6hbar c/E_QG,min then implies

    E_ref,min(L) > (E_QG,min/3) sin(pi/L).

Consequently the L=16 coefficient example cannot itself contain an optical
one-excitation reference packet under that identification. No choice of g
changes this displayed leading reference dispersion. This does not show that
a larger graph, other sectors, collective degrees of freedom or another
physical identification cannot describe optics.

If a nonzero reference mode with energy <=E_lab is to be available and
0<3E_lab/E_QG,min<1, a necessary finite-volume condition is

    L > pi/arcsin(3E_lab/E_QG,min).

This is a consequence of combining a supplied photon identification and a
conditional archival bound, not a size selected from the framework. The
actual fixed-graph weak-field error estimates do not provide a uniform
large-volume source-to-detector approximation at those L. That is the specific
new missing estimate identified here. No claim of required computational
resources, minimum detector resolution, physical preparation, or exclusion
is made. The printed observational lower limit carries its original
confidence and source-model premises; the arithmetic adds no coverage.


## B. Spectral overlap and the original count contrast

### 1. Sources and scope

Use the prepared original-record probe from PR9143, note SHA
14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b,
and its response-ratio/clock corollary in PR9147, note SHA
2dd49ffa004fa09726b2388decb7c4a36dd69f2cdaf5f3bbb8ffe3e829a47c6d.
The weak-field packet parent SHA
651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf
and photon-observation parent SHA
acf74cfce461cfbf607f7ba2994ff0a3d5986b9571bf7c5efacecebdf9ab5d7b
fix the harmonic transverse reference, mode dispersion and conditional SI map.
Retain their supplied compensated full matter/field dynamics, original mark,
Gauss-consistent two-branch charged preparation, and original formation outputs.

Fix an equal-period simple cubic torus with even L>=6 and V=L³ vertices.
The local selected effect remains I-Re W_p, for one elementary xy plaquette.
Let C be the original oriented curl matrix, c_p its plaquette row, and
f_r a real orthonormal nonzero transverse eigenbasis of C* C with eigenvalues
lambda_r. The field packet notation is

    d_pr=(c_p f_r)/sqrt(2 sqrt(lambda_r)),
    v_p=sum_r d_pr²,
    chi_p=sum_r alpha_r d_pr, sum_r |alpha_r|²=1.

The claim below concerns a restriction on the REFERENCE one-excitation modes,
not spectral support for the actual charged Hamiltonian. Its energies and
ordinary energy spread are different, as already shown in the parent. Harmonic
zero modes are excluded from this transverse packet class and c_p is
orthogonal to them. No global electric direction is discarded after a birth.

### 2. Exact spectral overlap on a finite torus

Write k_mu=2pi n_mu/L with centered integer representatives, and

    D(k)=4 sum_mu sin²(k_mu/2),
    D_xy(k)=4[sin²(k_x/2)+sin²(k_y/2)].

For each k!=0, the two transverse eigenvalues are D(k). In positive-coordinate
link orientation the plaquette row has Fourier components
(1-exp(ik_y), exp(ik_x)-1, 0)/sqrt(V), up to an irrelevant common phase.
It annihilates the gauge-gradient vector (exp(ik_mu)-1)_mu. Summing its squared
projections over the TWO transverse polarizations therefore gives D_xy(k)/V.
The original A-to-B link orientation differs by an orthogonal sign convention;
it does not change these scalar norms. The real cosine/sine eigenbasis and
complex Fourier sum give the same spectral quadratic form, with no extra
polarization or plus/minus-momentum factor. Consequently

    v_p = (1/(2V)) sum_{k!=0} D_xy(k)/sqrt(D(k)),
    v_p,epsilon = (1/(2V)) sum_{0<D(k)<=epsilon²}
                                      D_xy(k)/sqrt(D(k)).             (1)

The second quantity is the squared norm of the mode vector restricted to
reference energies hbar omega<=epsilon hbar c/a. Cauchy-Schwarz gives

    eta=|chi_p|²/v_p <= v_p,epsilon/v_p                           (2)

for any normalized one-excitation packet supported in this band. If the
band is nonempty, the upper value is attained when alpha is proportional
to the restricted d vector, provided that vector is nonzero. If the restricted
d vector vanishes, every such packet has zero excess. If the band contains
no transverse mode at all, no normalized band packet is being asserted.

### 3. A volume-independent upper bound

The plaquette row is a unit circulation on four distinct links: ||c_p||²=4.
It lies entirely in the transverse nonzero-mode subspace, and D(k)<=12.
Hence

    v_p >= ||c_p||²/(2 sqrt(12)) = 1/sqrt(3).                    (3)

For centered |k_mu|<=pi, sin(|k_mu|/2)>=|k_mu|/pi, so
D(k)>=4|k|²/pi². A mode with sqrt(D)<=epsilon lies in the integer ball
|n|<=L epsilon/4 and thus in its enclosing cube. For 0<epsilon<=2,

    N_epsilon <= (2 floor(L epsilon/4)+1)³-1.

A nonempty band also has epsilon>=2 sin(pi/L)>=4/L. Thus
L epsilon>=4, and

    N_epsilon <= (L epsilon/2+1)³ <= (3L epsilon/4)³.

Since D_xy<=D, each summand in (1) is at most epsilon. Including the empty
band separately gives the bound for every finite even L>=6:

    v_p,epsilon <= (27/128) epsilon^4,
    eta <= (27 sqrt(3)/128) epsilon^4.                         (4)

These constants are deliberately non-sharp. No continuum approximation,
thermodynamic state limit, spectral gap uniform in L, or full dynamical
large-volume limit is used. The fourth power comes from the number of low
momentum modes and the curl mode weight of this local measurement.

### 4. What the bound says about original counts

For the uncut harmonic reference the already-proved exact ratio is

    r_1/r_0 = 1+2 eta x/(exp(x)-1), x=g²v_p/2>0.

Equation(4) and x/(exp(x)-1)<=1 imply

    r_1/r_0-1 <= (27 sqrt(3)/64) epsilon^4.                   (5)

This exact expression is a harmonic-reference calculation. For the actual
normalized compact packets and original full process at each fixed graph,
the parent's positive window b=o(tau g³), tau=a/c, gives instead

    lim_{g->0}[p_1/p_0-1] = 2 eta
                           <= (27 sqrt(3)/64) epsilon^4,     (6)

where p_n is the probability of at least one selected original mark. All
background channels remain included through the parent theorem. Its error
constants can depend on L, and it supplies no uniform rate for a coupled
L->infinity, g->0, finite laboratory-time schedule. Uniformity of the algebraic
bound (4) must not be confused with that missing dynamical estimate.

The broad-band choice alpha proportional to the complete d vector, which
approaches the general ratio ceiling three, is therefore not a freely
available optical-energy packet under a restrictive physical energy band.
This does not invalidate the earlier general ratio theorem. It identifies
the extra packet-selection premise needed before calling its maximal
contrast an optical-detector response.

### 5. Conditional observational scale diagnostic

Only if the same harmonic modes are measured photons with E=hbar omega,
c the physical light speed and a the same proper physical spacing, does a
supplied optical ceiling E_lab define epsilon=a E_lab/(hbar c). Reuse the
archival LHAASO2024v2 ML/MINOS lower limit E_QG,min=6.9e11GeV, including all
source, cosmology, orientation and propagation assumptions of the parent.
Its necessary unknown-orientation bound a<6hbar c/E_QG,min gives

    epsilon < 6 E_lab/E_QG,min,
    lim_{g->0}[p_1/p_0-1] <
           (27 sqrt(3)/64)(6 E_lab/E_QG,min)^4.                (7)

The dimensionless right side is computed for supplied E_lab=1,2,3eV in the
control. It is not an experimentally measured dark rate, a fitted parameter,
a confidence statement beyond the inherited benchmark, or a full charged
energy gap. The strict upper limit is only conditional on interpreting the
printed observational bound as strict at its quoted coverage.

The finite-volume diagnostic separately shows that available optical modes
require an enormous L in lattice units at that conditional spacing. Even
when such a band exists, equation(7) constrains the limiting contrast of this
ONE local microscopic prepared mark. It does not bound a macroscopic collective
or spectrally selected detector, arbitrary preparations, many excitations,
long-time histories, or physically different clock/field identifications.
The local vacuum reference is not the charged apparatus ground state.

The remaining observation bridge is a derived source and stable collective
matter response with a physical energy/clock identification and quantified
errors over actual observation times. This specific construction's optical
interpretation is much more restricted than its abstract one-excitation
contrast. No new instrument or axiom is adopted to escape that conclusion.

### 6. A bound needing only mean reference energy

A hard spectral cutoff is stronger than a measured mean photon energy. Let
Omega=diag(sqrt(lambda_r)) on the same nonzero transverse one-particle space.
A normalized packet with mean reference energy <=E_lab obeys
<alpha,Omega alpha><=epsilon=a E_lab/(hbar c). Weighted Cauchy-Schwarz gives

    |chi_p|² <= <alpha,Omega alpha> sum_r d_pr²/sqrt(lambda_r).

For the cubic torus, the second factor is exact:

    w_p=(1/(2V)) sum_{k!=0} D_xy(k)/D(k)=(V-1)/(3V).           (8)

To prove the last equality, coordinate permutation makes the sums of
D_x/D, D_y/D and D_z/D equal; their sum is V-1 because D>0 at every
nonzero momentum. D_xy is the sum of two components. Therefore

    eta <= epsilon (V-1)/(3V v_p) <= epsilon/sqrt(3),
    lim_{g->0}[p_1/p_0-1] <= 2 epsilon/sqrt(3).                (9)

Under the SAME additional observational identification used in section5,

    lim_{g->0}[p_1/p_0-1] < 4 sqrt(3) E_lab/E_QG,min.          (10)

This is weaker than the hard-band fourth-power bound but does not ignore
rare high-energy components. The prerequisite is a mean REFERENCE excitation
energy in the one-excitation sector, not the mean energy of the entire charged
probe. It cannot be transferred to an arbitrary multiparticle distribution by
calling its total energy a single photon. Each inequality extends by convexity
to a density matrix supported in the reference one-particle space, using its
mean excitation energy; no coherent pure source is required for this extension.

For an approximate hard-band state with high-band probability w instead,
ordinary orthogonal-projection Cauchy-Schwarz gives

    eta <= [sqrt((1-w) v_p,epsilon/v_p)
                      +sqrt(w (1-v_p,epsilon/v_p))]².

Thus tiny spectral tails should not simply be dropped from a claimed
fourth-power bound. The mean-energy result (9) avoids a hard support claim.
It still does not supply a finite-g dynamical error estimate at laboratory
parameters. Uniform algebraic constants alone are not that missing estimate.

### 7. Evidence status


Personal analytic proof above; finite Fourier controls check normalization,
mode counting, empty bands and the bound for several even sizes and cutoffs.
They are floating consistency checks, not interval certificates or independent
proofs. SI arithmetic uses high precision to avoid rounding the tiny relative
excess to zero when added to one. Full code, every row and execution are saved.
The separate sealed independent PRE and released comparison provide the stated scoped reconstruction; the review packet records their exact sources and limits.

## C. Comparison scope for a primary optical experiment

### Primary evidence and what its numbers mean

[Brouri et al., arXiv quant-ph/0007032v1](https://arxiv.org/pdf/quant-ph/0007032v1)
reports NV fluorescence at637–800nm, continuous514nm excitation, and a
Hanbury-Brown–Twiss apparatus using two avalanche photodiodes. It estimates
photodiode quantum efficiency0.7. Figure3 uses1ns bins,11450s integration and
count rates5780/s and5990/s. Its signal fraction rho=S/(S+B)=0.34 corrects
stray fluorescence coincidences under a stated independence assumption. That
background is not a calibrated quantum-vacuum input to our prepared mark.
The paper is an antibunching experiment, not a supplied vacuum-versus-one-
photon trial on our charged preparation. Full methods, normalization, results
and captions reread; no digitization, likelihood fit or new measurements.

Local PDF SHA a5759a2a381b2039448484e321b740f2bf2b73d3c8265e58f1e76d8b08a3cb6a.
Only the recorded primary evidence is used. The text's fluorescence interval
is not a certified sharp support condition on every detected photon.

### Energy and time translations, explicitly conditional

If the quoted spectral wavelengths are used as vacuum-frequency labels, hc/
lambda gives reference photon energies approximately1.55–1.95eV. The arithmetic
record preserves both endpoints. A supplied2eV mean-reference-energy ceiling
is therefore a motivated illustration, not a measured exact bound on the
experimental state. In Part B’s original-local-probe result,
that premise and the same archival LHAASO/photon/clock identification give a
limiting relative excess below2.00817485e-20. It is a statement about the
model's reference sector and its ordered limit, not detector efficiency0.7.

Under that same clock identification, the earlier necessary tau upper bound
is5.72358223436e-36s. A1ns measurement bin has b/tau>1.74715756506e26.
The current positive-window proof instead needs b/(tau g³)->0. Its sufficient
regime supplies no controlled error for this1ns experiment at a chosen finite
g. This large ratio diagnoses a missing theorem; it does not establish a
necessary physical detector time resolution or prohibit a longer-time law.

### Why there is still no experimental exclusion or confirmation

The required identifications are not supplied by the paper or by the existing
proofs. In particular: the APD is a macroscopic dissipative detector, while our
statistic uses one local original mark in a deliberately charged/coherent
preparation; its source stream and registered1ns coincidences are not our
fresh single-excitation/vacuum positive-bin experiment; the reference photon
energy is not the broad ordinary energy of that charged preparation; and
finite physical g, volume and observation-duration errors remain unbounded
for the proposed mapping. The archival timing bound itself also retains its
source, cosmology, orientation and photon-transport assumptions.

Thus neither the quoted detector-efficiency estimate nor the optical antibunching trace can
be directly compared with the tiny limiting relative excess to declare the
framework excluded. Conversely, the existence of a positive abstract signal
does not reproduce either measurement. A successful next bridge must derive
a physical source and collective energy-selective matter response from the
same instrument, specify the observed count functional and its calibration,
and control errors at the actual scale and measurement duration. No new
primitive is adopted here to supply that missing step.

## D. Independent checks and current observational disposition

The independent PRE reconstructs the reference gap, mode normalization, both
polarizations, zero-mode treatment, hard-band optimization and mean-energy
bound from the named parents, before disclosure of the new author packets.
It also derives stronger static constants, an explicit continuum-sum enclosure,
a mean-constrained optimizer and examples with high-energy tails. Those added
calculations are attributed in the separate PRE; Part B retains its own stated
bounds. They do not silently enlarge the scope of the inherited dynamics.

The released comparison checks Parts A/B against that PRE and separately
reviews Part C against the primary optical paper and its unit conversions.
Its primary-source comparison occurs after disclosure; it is not credited
to the blind PRE. The publication correspondence check binds the final note,
runner, source inputs and fresh output. None is a formal audit verdict.

The canonical runner reuses the three disclosed author controls. The Fourier
calculation is unchanged except that a result field is called
projected_weight_fraction, making clear that zero weight in an empty band is
not an attained optimum over normalized excitations. Its feasibility flag is
retained. Arithmetic blocks are wrapped in functions and their result groups
are combined; full logs and source comparisons are preserved. It does not
simulate actual charged dynamics or fit an experiment. Floating spectral
cutoff membership is not an exact integer-shell certificate.

A physical prediction still needs a selected source/preparation, a stable
collective energy-selective response, a measured energy/clock identification
and a controlled full-process approximation for the actual experiment.
The displayed asymptotic limits and archival conditional constraints do not
supply those missing derivations. No new instrument or primitive is adopted,
no science is merged and no TOE completion is claimed.

## Landing-review boundary and No-Go Discipline Gate

N1: the supplied model and stated preparation only. N2: other physical routes remain open. N3: no new premise or parameter identification is adopted. N4: Fixed finite reference one-particle sector, hard band versus mean-energy constraint, uniform static inequalities versus fixed-volume dynamics, and conditional archival photon/clock conversion remain distinct. N5: independent exact or explicitly numerical controls supplement the written argument. N6: no universal framework exclusion or empirical confirmation follows. N7: source, stable response and measurement identification remain obligations. N8: later audit is separate; historical author checks are provenance only.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Complete original source remains recoverable at PR #9150's frozen head. No audit verdict or retained grade is applied.
