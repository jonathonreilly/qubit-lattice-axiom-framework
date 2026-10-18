# Actual microscopic ground response on the composite time scale

**Status:** bounded-support.
**Primary runner:** [scripts/native_ground_window.py](../scripts/native_ground_window.py)

The preceding [native readout result](NATIVE_COMPOSITE_READOUT_NOTE_2026-10-18.md)
left two important gaps: it described a coefficient operator, and it used a
chosen polarized reference. This block bounds the actual microscopic
finite-time response and removes the choice of a particular reference within
the stated ground-state problem. It does not establish a microscopic outgoing
pole or select the state of the universe.

Keep the supplied one-qubit XX/YY/ZZ Hamiltonian with
Jx=Jy=lambda Jz and small positive lambda. Consider even periodic cubes with
side L proportional to lambda^(-4), and times T=c lambda^(-4)/Jz. The constant
in L is sufficiently large for the fixed-order locality bounds. This joint
weak-coupling/growing-volume regime is essential.

## Derived ground manifold and actual microscopic comparison

The [root proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md)
first establishes a positive form bound for the actual fixed-order normal
form B_m, in Jz units:

    B_m-Evac >= (2-C_m lambda)N
                  +(lambda^4/128) sum_(x,y,z) (1-P_xyz)/2.

N counts broken vertical bonds and P is an elementary transverse plaquette.
Every term that can change spins must encounter a wall. Its negative part is
therefore bounded by C_m lambda N. Away from walls, plane-flip symmetry makes
local diagonal terms functions of plaquette defects. The derived positive
fourth-order plaquette energy dominates all higher fixed-order corrections
for sufficiently small lambda. No new stabilizing term is added.

The coefficient ground manifold is exactly the span of column patterns
s_xy=a_x b_y, with no vertical walls or bad plaquettes. It has2^(2L-1)
basis configurations. On the stated growing cubes the gap above this entire
manifold is bounded below by a positive constant. For order40, the exact
microscopic remainder has global norm O(Jz lambda^29). Thus the microscopic
lowest **cluster** lies close to this manifold. Splitting within the cluster
is allowed; the exact true ground space need not have the same dimension.

Plane-invariant local correlations are the same throughout the coefficient
ground manifold on the relevant time window. Locality prevents an operator
from connecting different whole-column backgrounds, while plane symmetry
equates its diagonal expectations. This is an operator identity after
localization, so the enormous ground degeneracy introduces no dimension
factor. Every actual microscopic ground density can consequently be used,
including mixtures and coherent superpositions.

## A response statement with a controlled error

Use the original diagnostic

    C = sum_r Z_r Z_(r+2ez) / sqrt(V).

For a fixed smooth compact time window psi, define the centered response

    S_T(omega) = integral dt/T psi(t/T) exp(i omega t) <C(t)C>_connected.

Uniformly for omega/Jz in [7,9], the actual microscopic ground-state response
agrees with the complete compact four-wall coefficient response, including
its correctly transformed source, up to **O(lambda^8)**. The frequency
resolution is of order Jz lambda^4. This error is smaller than the previously
derived lambda^6 residue scale.

The error accounting is explicit:

| Contribution | Bound in the stated scaling |
|---|---:|
| Actual dynamics versus order40 normal form | O(lambda^13) |
| Actual ground density versus coefficient ground manifold | O(lambda^17) |
| Exact versus truncated transformed source | O(lambda^29) |
| Smooth-window suppression of higher-wall sectors | O(lambda^8) |
| Finite-volume winding and boundary effects | Smaller than every power of lambda |

The normalized dt/T window adds no extra factor of T. Higher-wall sectors
are separated from this frequency interval by the form bound. To use locality
for the four-wall response, the proof extracts each local source's wall-number
charge component with a commuting-N Fourier average. That operation remains
local; it does not insert a nonlocal spectral projector into a locality bound.
The full finite-volume sector is included before controlling winding effects.

The [gap check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_NORMALFORM_GAP.md),
[window check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_WINDOWED_RESPONSE.md)
and [ground-state extension](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_GROUND_WINDOW.md)
are preserved separately. The runner enumerates65,536 transverse sign
patterns and589,824 rectangle comparisons, and checks plane-invariant Pauli
response coefficients through fourth order on81 physical one-qubit sites.
This is sparse Pauli algebra, not diagonalization of an81-qubit Hilbert space
or numerical evaluation of the order40 theorem.

## Remaining physics

The comparison keeps the entire coefficient response, including fast
background and fine structure. It does not turn a complex resonance residue
into a positive isolated spectral line. The mode remains massive near8Jz,
and no full-H outgoing-pole theorem follows.

The Hamiltonian, weak-coupling regime, ground-state restriction, diagnostic,
units and cosmological identification remain premises or open bridges.
A particular polarized reference is no longer needed for this ground-response
comparison; a cosmological preparation has not been derived. Constants may
depend strongly on fixed order, so no useful numerical lambda threshold is
certified. This is not a fixed-lambda infinite-volume ground-state claim.
No observation is fitted or independently tested.
