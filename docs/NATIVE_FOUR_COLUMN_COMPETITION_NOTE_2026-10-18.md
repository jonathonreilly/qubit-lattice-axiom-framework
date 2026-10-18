# Collective motion when native column processes compete

Status: conditional-support. The supplied one-qubit directional Hamiltonian generates a complete leading two-dimensional column Hamiltonian with a fixed interaction ratio and a derived microscopic readout. Finite spectra show a strong neutral peak with positive finite-momentum energy shifts. An auxiliary expansion identifies a propagating four-spin droplet. Neither establishes a relativistic scalar, an infinite-grid pole, or a physical particle identification.

Premises are Jx=Jy=lambda Jz>0, open longitudinal columns of length four, and periodic transverse circumferences greater than four. Column coordinates describe four original physical qubits; no site Hilbert space or microscopic interaction is added. The open column ends are a geometry premise, not a derivation of a finite feature embedded in an infinite bulk. All cases below are exposed model development, with no empirical calibration or independent observational test.

## Both processes arise at the same order

The [plaquette calculation](NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md) and [column tunneling](NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md) extend to length four after retaining the off-diagonal processes at the same order. Write P for the product of four column Z coordinates on an elementary transverse square, and T=sum_<ij> Xbar_i Xbar_j. Up to a scalar,

H_eff,4 = -Jz lambda^4 [(9/64) sum P + (1/8) T].

Thus t/K=8/9, where K=9 Jz lambda^4/64 and t=Jz lambda^4/8. This ratio is computed, not fitted to produce a mode. At fourth order, a return to aligned columns is either a repeated-edge scalar walk, a same-height plaquette loop, or a complete reversal of two neighboring length-four columns. The latter uses the same transverse edge once at each height. There are no other nonconstant fourth-order operators. Folded second-order terms are scalar. Both X and Y reversals give the same sign at even length. Transverse periods greater than four exclude additional winding loops at this order; odd periods do not justify an automatic even-power remainder.

A direct check retains all 65,536 states of an open 2x2x4 physical grid. Block eigensolvers recover its sixteen low states; polar alignment to the sixteen unperturbed column configurations gives a Hermitian effective matrix and the projected original readout. At lambda=.1,.2 the largest eigen-residuals are 6.7e-12,9.5e-12. After subtracting scalar traces and dividing by lambda^4, the operator-norm errors against the fourth-order Hamiltonian are .005720,.022266, and against the readout below .027132,.104639. The approximately quadratic reduction is a finite microscopic check of these coefficients, not a large-grid error theorem.

## The original observable largely follows energy, but not exactly

Let C=sum_(column,j) Z_j Z_(j+2) be the original longitudinal distance-two observable. Its nonconstant fourth-order projection is

C_eff,4 = lambda^4 [-(51/128) sum P -(3/8) T]
        = (3/Jz) H_eff,4 +(3 lambda^4/128) sum P.

The second term is the inelastic zero-momentum source in a stationary eigenstate. The first is conserved at zero momentum. The decomposition does not imply that a local energy density has no response at nonzero momentum. The momentum tests below concern the plaquette channel; converting a nonzero-momentum original-C source requires its local operator distribution and is not done here.

The off-diagonal coefficient includes direct readout dressing, not just ground-state mixing. Introduce H+sC only to differentiate the existing observable. For an open pair of aligned length-L columns, the virtual tunneling chain is -Kz sum Z_j Z_(j+1)-g sum X_j+2s sum Z_j Z_(j+2), Kz=2Jz. Its leading tunneling coefficient is t_L=g^L/Kz^(L-1). For every fixed L>=3,

t'_L/t_L = 3(L-2)/Kz

for that leading coefficient. This is not an exact formula for the finite-g splitting or a uniform growing-L expansion.

One derivation uses the free Majorana chain at s=0. Put r=g/Kz and C_jk=<i b_j a_k>. Occupying its soft mode changes C_jk by 2r^(L-j+k-1)[1+O(r^2)]. The background nearest contraction is 1+O(r^2), and the next-dimer contraction is r/2+O(r^3). Wick's identity for W_j=Z_j Z_(j+2) gives C_j,j+1 C_j+1,j+2 - C_j,j+2 C_j+1,j+1. The two direct changes contribute 4r^L; the crossed contraction subtracts r^L. Therefore Delta<W_j>=3r^L+O(r^(L+2)) at every internal j. Hellmann–Feynman with +2s sum W gives the stated derivative. No solvability at nonzero s is assumed. At L4 this is t'_4=3t_4/Jz, yielding -3lambda^4 T/8. The canonical connection cannot modify this leading nonconstant coefficient because all lower effective energies are scalar. Independent proof and finite subset calculations are preserved in the campaign pack.

## The finite spectra include all defect numbers

Choose the simultaneous positive logical row/column-X symmetry sector. In a column-Z description, each allowed plaquette pattern represents the normalized equal superposition over its 2^(Nx+Ny-1) column-sign fiber. There are 2^((Nx-1)(Ny-1)) basis states. Pair flips map fibers with unit amplitude. For even-by-even tori, also select positive global logical-Z parity; this halves the dimension. These are explicit sector choices. The earlier four-defect restriction is not used.

The Hamiltonian in units K is -sum P-(8/9)T. The zero-momentum source is sum P/sqrt(Ncolumns), centered in its computed ground state. Residuals are checked directly on reconstructed vectors, not inferred from a Lanczos node.

| Transverse grid | Dimension | Ground energy/column | Lowest source gap/K | Plaquette-source weight | Excited residual |
|---|---:|---:|---:|---:|---:|
| 5x5 | 65,536 | -1.849711204 | 11.97263094 | .90650844 | 2.2e-14 |
| 5x6 | 1,048,576 | -1.849466980 | 12.22552530 | .89868379 | 5.4e-14 |
| 6x6 | 16,777,216 | -1.849236330 | 12.40289923 | .87741164 | 3.2e-9 |

The 6x6 ground residual is 2.1e-11. Higher quadrature nodes with large residuals are preserved as unresolved, not reported as eigenmodes. Size dependence remains visible; three finite grids do not prove an infinite-volume pole. The original normalized C source's leading q=0 weight is (3lambda^4/128)^2 times the table's plaquette weight. Normalizing per physical site rather than per column divides this by four.

At 6x6, plaquette sources with momentum indices (1,0),(1,1),(2,0) have lowest significant gaps 13.13368761,13.71222617,13.34068779 in units K, with direct residuals below 2.8e-8. These exceed the q=0 gap and are consistent with positive dispersion near the minimum. They are finite momentum comparisons, not a measured continuum curvature or a Lorentz-invariant cone.

## A local derivation identifies the moving droplet

An auxiliary expansion of the coefficient model at K/t small clarifies its low neutral excitation. This is a diagnostic expansion; its control at the native K/t=9/8 has not been proved. In the X-ferromagnetic reference, four minus spins on a 2x2 square cost 16t. At fixed positive row/column charges, this is the minimal finite droplet of perimeter eight. On an even torus the all-minus vacuum and complementary droplets also occur; choose positive global spin-flip parity, or specify the infinite-volume plus phase. The stated local expansion assumes a sufficiently large torus to exclude short winding alternatives.

Second-order plaquette flips move the droplet. The vacuum intermediate contributes +K^2/(16t). The other intermediate is the symmetric difference of the two droplet squares. Its energy is 24t for displacements (1,0),(2,0) and their rotations, and 28t for (2,1) and its rotations/reflections. The resulting hoppings are respectively -K^2/(16t) and -K^2/(48t). Disconnected displacements have intermediate energy 32t and cancel the vacuum path. The vacuum-subtracted diagonal coefficient is -13K^2/(24t).

Consequently

E(q)=16t+(K^2/t)[-13/24 -(cos qx+cos qy+cos 2qx+cos 2qy)/8 -(cos 2qx cos qy+cos qx cos 2qy)/12]+higher orders.

At q=0 the correction is -29K^2/(24t); the coefficient of qx^2+qy^2 is +25K^2/(48t). The plaquette source creates the normalized droplet with leading weight one. Exact local signed-denominator checks establish these expansion coefficients. Finite coefficient spectra at auxiliary t/K=4 are separate development controls; they do not promote the expansion at the native ratio.

## Charged features change the readout without a supplied source potential

The same leading Hamiltonian can be represented in X-spin variables with specified row and column parities. A single minus spin changes one row and one column charge; their conservation prevents its isolated translation. A neighboring vertical pair can move horizontally, while a horizontal pair can move vertically. These are charge-constrained grid features, not identified fermions. A neutral square droplet can move in both transverse directions.

Full logical-Hamiltonian checks at 3x3,3x4,4x4 verify the affine charge representation and seed operator maps exactly; these small boxes are representation controls only. The native coefficient calculations use periods greater than four. At 5x6, the computed lowest sector gaps/K are 6.60187327 for a single charged feature, 8.10416943 for an adjacent vertical pair, and 11.75117316 for a vertically separated pair. Sector ground residuals are below 1e-11. The specified column-Z seed has squared matrix element .97077735 to the single-feature state. Vector dot products across the coordinate arrays represent that seed operator; they are not overlaps of physically orthogonal charge sectors.

Let Delta E be a sector gap in units K, and Delta P the change in total plaquette expectation. The original readout difference follows from the operator identity above:

Delta C/lambda^4 = (27/64) Delta E +(3/128) Delta P,
Jz Delta C/Delta E_physical = 3+Delta P/(6 Delta E).

On 5x6 the last ratio is 3.02861809,3.06653425,3.07055241 for the single, adjacent vertical and separated vertical features. The differing responses are derived within one Hamiltonian, with no added potential. They are static microscopic readout differences, not a proved force law, an equivalence-principle measurement, or an emission vertex for a canonically normalized scalar. A universal physical source/detector identification remains open.

## Limits and next bridge

Finite open-column geometry, supplied anisotropy/Hamiltonian, selected state/sector, higher-order native corrections, infinite-area stability, three-dimensional propagation, particle statistics and measurement identification remain open. In particular, a finite slab cannot be called an embedded bulk feature by ignoring its end bonds. The next route is the finite segment with real longitudinal walls in the uncut bulk, including the interaction that confines or destabilizes it.

Plaquette and compass models with subsystem symmetries have substantial prior literature, including [Xu and Moore](https://arxiv.org/abs/cond-mat/0312587) and [Nussinov and Fradkin](https://arxiv.org/abs/cond-mat/0410720). That context does not identify this nearest-neighbor pair-flip Hamiltonian with a single-transverse-field model or import its phase diagram. No novelty claim or empirical validation follows from the analogy.

## Reproduction and review

Run `python scripts/native_four_column_competition.py`. It replays the exact local droplet paths, full 5x5 momentum and charge calculations, and the 16-physical-qubit check. It verifies source/result hashes for the frozen larger grids, explicitly without replaying 5x6 or 6x6. Exact original reproducer bytes and scratch output paths are preserved in `native/column_four_results/PROVENANCE.json` and its sibling sources. Independent coefficient, all-length source, quotient, charge and droplet checks are recorded in the campaign pack. No empirical input is used.

The frozen 6x6 momentum run additionally reads a large ground-state checkpoint, which is not committed. From the native source directory, run `python neutral_four_column_model_v2.py 6 6 32` at its default native ratio 8/9, then `python neutral_four_column_momentum_six.py 6 6`. Both use the explicit `/private/tmp/neutral_four_column_gs_6x6.npz` path. The provenance manifest records the original checkpoint SHA-256 and ordered recipe. A regenerated eigensolver vector may differ by sign or rounding; compare energy and direct residuals, rather than requiring byte-identical regeneration. Set `VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 NUMBA_NUM_THREADS=4` for these larger runs.
