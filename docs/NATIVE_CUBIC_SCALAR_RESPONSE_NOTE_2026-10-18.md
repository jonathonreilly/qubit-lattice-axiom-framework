# Native scalar diagnostics and finite-grid readout

**Status:** bounded-support.
**Primary runner:** `scripts/native_cubic_scalar_response.py`

This block tests the supplied one-qubit compass Hamiltonian directly, beyond
its weak-transverse-coupling expansion. It constructs a scalar observable
from the existing interactions and resolves its finite-grid response. It
also checks the previously supplied readout on a larger rectangular grid.
It does not derive a light cosmological field, a thermodynamic particle, an
empirical detector identification, or a ground-state selection principle.

The prior [slow-composite correction note](NATIVE_SLOW_COMPOSITE_CONTROL_NOTE_2026-10-18.md)
left the large feature's energy near8Jz. The present route challenges that
mass obstacle near isotropic coupling, rather than assuming that internal
size makes an excitation light. All inputs and comparisons are exposed model
development; no independent observation data are used.

## Supplied model and generated diagnostic

On a periodic grid, with one physical qubit per site, use

    H=Hx+Hy+Hz,  Ha=-J sum_(a-bonds e) A_e,
    A_e=sigma_i^a sigma_j^a,  J=1 in the calculations.

The interaction, geometry, isotropic coefficient choice, and candidate ground
sector remain premises. No interaction is appended. Define the diagnostic

    Q=sum_a [Ha,[H,Ha]].

Q is a cubic scalar on a cubic grid. This is a derived operator, not a new
Hamiltonian term or a derived measurement protocol. For each b-bond f, let
K_af be the sum of the four a-bonds anticommuting with A_f, a!=b. Bond algebra
gives exactly

    Q=4 J^3 sum_(b,f;a!=b) A_f K_af^2.

Expanding the square gives a bond contribution -32J^2 H and four-spin
strings from pairs of distinct incident a-bonds. Independent binary-Pauli
contractions agree with the nested commutator:1053 terms on3x3x3 and1404 on
3x3x4. For an exact ground state,

    <Q>=2 sum_(a,n) (En-E0) |<n|Ha|0>|^2 >=0.

This expectation identity does not make Q a positive operator. It supplies
a native fluctuation diagnostic; it does not specify an apparatus coupling.
For comparison S sums four-spin plaquettes, with the spin component normal
to each plaquette. S is another chosen scalar probe on a cubic grid.

## Exact finite symmetry reductions

On3x3x3 the plane-Pauli algebra has a six-dimensional center and a protected
two-dimensional factor. Fixing a maximal commuting subgroup gives2^20
coordinates for27 physical qubits. At isotropy, translations and cubic axis
permutations organize64 central characters into four spectral classes,
with multiplicities1,9,27,27. Numerical lowest energies in their representatives
are -38.19164989239814, -37.72770357890127, -37.09419276294261 and
-36.39380011348631. These are eigensolver ground candidates, not rigorous
spectral lower-bound certificates. The lowest other-central-sector candidate
gap .463946313497 is not a neutral scalar gap.

On3x3x4, all three X planes, all three Y planes, and three adjacent Z-plane
products commute, but have rank8, not9. Their product relation is retained.
The chosen positive sector has2^28 coordinates for36 physical qubits.
Translations reduce it exactly to7,458,416 zero-momentum coordinates.
Adding xy coordinate reflections, xy interchange with the global phase gate
S_site=diag(1,i), and z reflection gives576 signed monomial maps. Global Z
is positive in this sector, so the phase i^(number of down spins) is real.
The fully invariant subspace has475,194 coordinates, independently verified
by a signed Burnside calculation. No physical qubits are added.

The original36-site candidate ground projects into that smaller subspace
with vector error1.92e-14. Its energy is -49.970264103705546 and direct
residual1.52e-13. Physical stabilizer-orbit checks, translation group laws,
signed phases, sparse matrix entries, and8-site full-Hilbert intertwining
were checked independently. These are selected-sector results. The rectangular
shape breaks cubic symmetry; its lines cannot be labeled3D scalar irreducible
modes solely from this reduction.

## Resolved finite responses

On the cubic27-site grid, the checked scalar line has gap3.763565915973J,
S weight58.3365873119, and Q weight7094.98109499. A separate low-spectrum
calculation agrees with direct reconstruction of the response vectors. The
lower gap1.423237955386 couples to the directional observable
B=Hz-(Hx+Hy)/2. Its total B weight is5.3661775445; S and Q weights in that
low eigenspace are numerically negligible. The lower directional excitation
is therefore not evidence for the scalar probe's lightening.

The original readout Cz=sum_r Z_r Z_(r+2ez) aliases -Hz on a length-three
periodic axis. Thus on this cube Cz=-(2B+H)/3 and its nonzero-frequency weights
are4/9 of B's. That is a finite-box alias, not a bulk coupling theorem.

The length-four axis removes this specific alias. On3x3x4 the supplied Cz
has variance115.46267316195033. Twenty directly checked low eigenpairs
capture81.85782138594152 of that weight. Representative lines are:

| gap/J | Cz weight | S weight | Q weight |
|---:|---:|---:|---:|
| .880768157429 |4.82939073142|.279847795599|71.4453933668|
|2.00229775809|2.28815957136|16.9920469952|3194.67707896|
|3.58195863359|1.30217860998|33.6684145315|4423.42571079|
|3.86135256997|18.7515520799|4.83621072369|105.913577403|
|4.42954788612|25.1203963823|.139714302193|490.111855304|

These listed residuals are below2.3e-13. The largest residual among all20
stored low eigenpairs is9.1e-12. The table derives response weights from
this finite Hamiltonian and the stated operators. Different shapes, source
normalizations and symmetry groups prevent interpreting it as a controlled
finite-size scaling law. It does not establish a universal scalar coupling.

## Preserved failed calculations and decisive controls

An initial100-step response quadrature on the36-site translation sector did
not resolve several apparent peaks. For example, the apparent S line near
3.581961 had residual .0031 and was rejected. The additional exact symmetry
reduction enabled direct eigenpair resolution at3.58195863359 with residual
2.27e-13. Rejected quadrature nodes were not counted as physical modes.

A second implementation error arose when composing separately projected Hx
and Hy inside the xy-invariant sector. Those individual operators do not
preserve that sector, even though their sum and Q do. The resulting Q mean
3247.808 was wrong. The corrected code forms the entire commutator in the
larger Pauli algebra before projecting once. It gives Q mean2920.77195545254
and variance112848.65238604, agreeing with the independent translation-only
calculation. The failed JSON is preserved explicitly as diagnostic evidence,
not as a result. This correction does not change H, its eigenpairs, S, B or Cz.

## Reproduction and remaining obstacle

The [runner](../scripts/native_cubic_scalar_response.py) replays a full8-site
intertwiner and the27-site scalar/directional response, and verifies SHA256
identities of the frozen larger calculations. It does not rerun the36-site
calculation by default. Exact source files, outputs, independent checks and
scratch regeneration commands are in the campaign's native/cubic_results
identity packet. Large basis arrays and eigenvectors are temporary computation
products, not required repository payloads.

The interaction itself generates nontrivial scalar fluctuation operators and
finite response lines. The unresolved steps are their infinite-grid spectrum,
propagation and stability, an appropriate state, a light scale, and a derived
connection to actual sources and detectors. A chosen diagnostic and a discrete
finite-box spectral line do not retire those assumptions.
