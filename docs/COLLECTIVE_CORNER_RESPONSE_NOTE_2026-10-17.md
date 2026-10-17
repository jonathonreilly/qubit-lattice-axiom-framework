# Collective response of the supplied corner lattice

Status: conditional-support. Direct research, not a formal audit or a derived cosmological scalar. No observational data were fitted or tested in this block.

## Question and supplied inputs

Can a large feature on a one-qubit-per-site grid supply its own scalar coupling? This block tests the most concrete current candidate: the staggered mass channel of PR9671, frozen at a96cefd1901938c6e4b6155a3576477d78ed6c87. The complete numerical candidate, upstream source identities and normalizations are in `data/collective_corner_response/candidate.json`; the upstream runner was replayed with17 passing controls. Its12-orbital coarse-cell Hamiltonian, flux sector, coefficients, conjugation-odd hopping and mass operator are supplied. The earlier qubit embedding uses chosen blocks and spectator sites; this calculation does not derive those blocks from a uniform fine-grid rule or demonstrate a self-bound fermion.

Write h(k) for the supplied Bloch Hamiltonian and M for its Hermitian mass matrix, normalized by max|Mij|=1. The applied source m couples k to k+Q, Q=(pi,pi,pi). Its upstream channel transforms as a pseudoscalar; identifying it with the cosmological conformal scalar would require an additional symmetry and measurement argument. Neither the12-orbital effective description nor the number of sites occupied by a feature supplies that argument.

We explicitly choose grand-canonical development states at chemical potential mu=-2.28284271247462 and positive temperatures T=.1,.03,.01 in the model's energy units. These are not derived initial states or observed temperatures. All meshes and state choices are exposed development calculations, not independent empirical tests.

## Response derived from the fixed Hamiltonian

For H(m)=H0+m O and free-fermion grand potential

    Omega(m) = -T Tr log(1+exp((mu-h(m))/T)),

let f_a be the Fermi occupation of eigenvalue E_a. The isothermal response per original coarse cell is

    chi_iso = -Omega''(0)/Nc
            = (1/Nc) sum_ab (f_a-f_b)/(E_b-E_a) |O_ba|^2.

For coincident energies the divided difference is f(1-f)/T. The sum includes the entire degenerate block, making it invariant under basis rotations within that block. Positivity follows because the Fermi function decreases with energy. This is an exact conditional free-fermion identity, evaluated numerically for the stored matrices.

In Bloch form O_ba becomes [U(k+Q)^dagger M U(k)]_ba and the prefactor is1/Nk over the full Brillouin zone. A folded24-dimensional free-energy calculation over the full zone instead requires1/(2Nk), because it counts every Q-pair twice. An independent checker uses only one representative per pair and needs no extra half.

At nonzero imaginary frequency, the corresponding finite isolated response is

    chi(i omega) = (1/Nk) sum_kab D_ab |M_ba|^2
                                  Delta_ab^2/(Delta_ab^2+omega^2).

Here D is the positive static divided difference. Exactly degenerate terms contribute zero at nonzero frequency. Thus, on these finite collisionless grids,

    chi_dyn(0+) = chi_iso - chi_degenerate.

This distinction is material: changing equilibrium occupations is not evidence of a propagating collective mode. No relaxation law, real-frequency isolated pole or continuum order-of-limits theorem is supplied by this calculation.

## Numerical results and controls

`scripts/collective_corner_response.py` records44 passing controls and the full18-row mesh/state scan in `outputs/collective_corner_response/result.json`. At N=4,T=.03, unshifted grid:

- Bloch static response:7.157298788740841.
- Independently assembled768-dimensional real-space response:7.157298788740856.
- Independent32-pair folded response:7.157298788740817.
- Degenerate contribution:1.0811934946903061.
- Collisionless zero-frequency limit:6.076105294050535.

The independent folded free-energy finite difference agrees within8e-9 at its smaller steps. This is implementation validation, not an independent physical observation.

The two applied-source vertex singular values are1.4040589577986065 and1.4040589577986051. For the four exactly sampled node states at mu, their equilibrium contribution is lambda^2/(T N^3), here1.0267612275908902. It is only part of the degenerate response. Its finite-volume1/(TN^3) behavior must not be mistaken for a bulk instability.

| N | mesh shift | T | chi_iso |
|---|---|---|---|
|4|0|.03|7.157299|
|4|.5|.03|5.868187|
|8|0|.03|6.360754|
|8|.5|.03|6.347911|
|12|0|.03|6.349473|
|12|.5|.03|6.352639|
|12|0|.01|6.063892|
|12|.5|.01|6.280182|

The colder scan retains appreciable mesh dependence. No certified thermodynamic limit or physical filling is claimed. The degeneracy tolerance1e-9 is numerical, not a derived linewidth.

## What would turn response into a collective field?

A separately postulated static mean-field functional Omega(m)/Nc+m^2/(2G) has quadratic curvature G^-1-chi_iso. At N=12,half-shift,T=.03 its sign changes at G=0.15741488548471327. This is merely a conditional curvature diagnostic: G is absent from the fixed quadratic candidate. An all-to-all interaction -G O^2/(2Nc) would supply such a saddle but would be a new nonlocal interaction. A local interaction requires an actual operator, justified approximation and analysis of competing channels. We add neither interaction as a framework premise. A sign change alone establishes neither a stable phase nor a scalar particle.

Even with an interaction, the canonical coupling requires the collective propagator's pole and residue. The number1.404059 is a vertex relative to an arbitrarily normalized applied source M; it is not a canonical Yukawa coupling. A field rescaling changes that number until the field's own kinetic normalization is derived. Spatial dispersion, stability, coupling to extended source/detector states, and identification with the cosmological field remain open.

There is a useful exact check on the earlier common-rescaling route: for a uniform source O=H0, [H0(t),H0(0)]=0, so its isolated retarded commutator response vanishes. The isothermal response beta Var(H0)/Nc can nevertheless be nonzero. This identity concerns this uniform conserved operator only; it does not rule out local energy transport, interactions or other collective modes.

## Prior work and next calculation

The repository's September4 generated-staggered-mass response note already treats a supplied Hartree interaction, gap equation and metric dressing; mean-field mass generation is not new here. This block checks the newer corner candidate's full-band response and distinguishes equilibrium degeneracy response from dynamics. See `docs/THE_GENERATED_STAGGERED_MASS_RESPONDS_TO_THE_DIAGONAL_METRIC_AND_TO_NO_SHEAR_A_LENGTH_DRESSED_NN_LAW_IS_SHEAR_BLIND_AND_THE_VACUUMS_EVEN_SUM_TRANSLATIONS_FORBID_ANY_NN_T2_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-04.md`, including its corrections and conditional scope.

The next decisive task is to extract an interaction and fluctuating operator from the actual fine-qubit Hamiltonian, retaining its noncommuting terms rather than fixing them to flux numbers. Then compute the collective spectral response and its normalization before identifying a scalar coupling. Larger support for a feature may provide room for such internal dynamics, but feature size alone derives neither the interaction nor a scalar. No remaining physical assumption is retired by the present calculation.
