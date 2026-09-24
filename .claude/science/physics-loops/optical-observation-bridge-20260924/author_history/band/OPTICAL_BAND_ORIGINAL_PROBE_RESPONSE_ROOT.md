# Optical-band overlap of the original local prepared probe

Root author candidate, 2026-09-24, personally derived under the user's explicit
additional twelve-hour campaign authorization. Conditional mathematical and
units result; independently unchecked at sealing. No physical identification,
finite-parameter laboratory prediction or framework exclusion is asserted.

## 1. Sources and scope

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

## 2. Exact spectral overlap on a finite torus

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

## 3. A volume-independent upper bound

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

## 4. What the bound says about original counts

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

## 5. Conditional observational scale diagnostic

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

## 6. A bound needing only mean reference energy

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

## 7. Evidence status


Personal analytic proof above; finite Fourier controls check normalization,
mode counting, empty bands and the bound for several even sizes and cutoffs.
They are floating consistency checks, not interval certificates or independent
proofs. SI arithmetic uses high precision to avoid rounding the tiny relative
excess to zero when added to one. Full code, every row and execution are saved.
Independent reconstruction is required before publication promotion.
