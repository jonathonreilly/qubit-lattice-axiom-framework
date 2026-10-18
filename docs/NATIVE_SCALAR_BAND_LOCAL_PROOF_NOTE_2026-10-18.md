# Complete neutral scalar band and local composite dynamics

Status: exact-support for the stated symmetry count and formal local coefficients;
bounded-support for finite full-H eigenpair tests. This strengthens the native
composite candidate of [the domain resonance note](NATIVE_NEUTRAL_DOMAIN_RESONANCE_NOTE_2026-10-18.md).
It does not establish an infinite native pole, a cosmological scalar, gravity,
fermions or a TOE. The microscopic Hamiltonian, positive rung parity, periodic
2×2×L geometry, invariant state/source and small positive λ=Jperp/Jz remain premises.
No new interaction or physical qubit is introduced.

No observational dataset enters. Sizes, momenta and coupling ratios are exposed
model-development tests. Independent mathematical checks are not independent
empirical tests. No physical unit scale, mass or detector identification is fitted.

## Complete scalar subspace of the unperturbed band

For even L, the complete band at excitation 8Jz consists of one interval of color b
in color a, at physical Hamming distance two. The three plane generators have
compressed flip masks6,1,5 and are transitive on the eight colors. The last has
local phase −(−1)^popcount(b&5). The exact square/spin symmetry and transverse
reflection further identify the four native-edge differences and the two diagonal
differences. The reflection here swaps transverse columns; it is not longitudinal
reflection and does not exchange momentum q and −q.

For the diagonal difference physical XOR6 (compressed label3), reflection times
square fixes representative colors0000 and0110 with phases−1,+1. Its global phase
on an interval of length ell is (−1)^ell. Odd diagonal intervals therefore cannot
belong to the invariant transverse scalar sector. Even intervals admit a positive
color average. This is a selection rule from the native symmetries, not an imposed
removal of inconvenient states.

Write q=2πm/L. An explicit normalized edge vector is proportional to

    E_ell(q) = sum_(a,b,start) h[b,a]^ell exp[iq(start+(ell−1)/2)]
                 |b on interval ell; a elsewhere>.

The sum is over all oriented native-edge pairs. A diagonal D_ell uses the same
phase and equal amplitudes for both physical diagonal differences6,9, with ell
even. Both constructions use existing product configurations of physical qubits.
Under a signed exact color symmetry, h[b',a']=s(b)s(a)h[b,a]; for even L this
transforms h[b,a]^ell by exactly the global configuration sign. Hence these vectors
are invariant. Background/edge transitivity bounds each length orbit's invariant
multiplicity by one; the nonzero explicit vector attains it.

Color interchange identifies ell and L−ell with phase (−1)^m. The terminal
ell=L/2 therefore vanishes when m is odd. All other listed vectors have disjoint
length/type supports. The complete dimensions are

    n_edge = L/2 − (m mod2),
    n_diagonal = floor(L/4) − 1_(4 divides L and m odd).

At q0 this is L/2+floor(L/4). It holds at qπ as well, even though first-order
hopping then vanishes and a source-generated Krylov basis collapses. Exact signed
orbit counting checks q0 for even L4..24. Explicit vectors check all momenta for
L4,6,8,10,12,16: orthogonality, all six symmetry actions, closure under the complete
K1/K2/K3 matrices, and first-order edge hopping2cos(q/2), with sqrt2 terminal factor.
This avoids the conditioning failure of the earlier numerical Krylov construction.

Every equivariant canonical effective operator within this complete unperturbed
band preserves the counted symmetry sector. This removes missing same-symmetry
E8 channels as an assumption. It does not make the bare E8 subspace invariant
under full H, prove spectral isolation at fixed coupling uniformly in L, or force
higher-order effective interactions to remain nearest-neighbor.

## Local fourth-order coefficients

A four-operation diagonal return can involve at most two active rungs, since the
native transverse h has zero diagonal. For nonadjacent active rungs, excitation
costs a,b add. Direct interleavings contribute −(a+b)/(a²b²), and folded terms
+(1/(a²b)+1/(ab²)); the disconnected contribution cancels. Only one-rung and
adjacent-pair connected terms remain.

Exact rational enumeration gives vacuum single1/64 and adjacent pair−5/192,
thus periodic vacuum fourth-order density−1/96. One diagonal wall changes two
singles to1/8 and three pairs to−9/64,−1/12,−9/64. Its vacuum-subtracted excess is

    2(1/8−1/64)+2(−9/64+5/192)+(−1/12+5/192)=−13/192.

Two walls with both domains at least three rungs long give−13/96. Moving a wall by
two rungs requires two operations on each changed rung and exhausts all four;
the exact local sum is−3/64 for all16 oriented diagonal-color pairs. The local K2
and metric columns are diagonal, so no folded off-diagonal correction survives.
The single-wall kernel also gives zero for displacement±1. These local statements
are independent of remote length under the stated separation conditions. Shifts
into short domains or folded endpoints need their own controls.

At length2, the scalar Rayleigh–Schrödinger shortcut fails: K2 has bright components.
The complete canonical formula retains these in the folded anticommutator. Its
local ground-subtracted matrix in the two diagonal colors at fixed background is

    [[47/192, −5/8], [−5/8, 47/192]].

The symmetric submatrix eigenvalue is−73/192; antisymmetric is167/192. Neither alone
is an eigenvalue of the full effective Hamiltonian. All eight backgrounds agree;
an independent sequential path implementation agrees for patchesN6,8. Local
connected support extends this coefficient when the remote background arc has at
least four rungs. The failed scalar-RS value−1/192 is preserved and excluded.

These arguments establish the named local coefficients, not a uniform perturbative
remainder or a complete all-order halfline Hamiltonian. In particular the exact
symmetry-space count is distinct from proving any truncated dark-only dynamics.

## Full native finite-lattice check

The supplied replay script constructs the periodic 32-physical-site Hamiltonian
and the original O/sqrt(L), O=sum_(j,a) Z_(j,a)Z_(j+2,a), in a selected commuting
plane sector of dimension2,097,152. It does not add the effective oscillator to H.
Ground states are solved directly; source Lanczos vectors are reconstructed and
accepted only with small full-H residuals. Four large-residual quadrature nodes
per ratio are explicitly rejected. This is not a completeness or isolated-eigenvalue
certificate, and near-degeneracies can affect numerical individual weights.

Before these runs, the finite L8 effective prediction was fixed by the matrix

    [[−73/192−1, −3sqrt(2)/32], [−3sqrt(2)/32, −13/96]].

Its lowest eigenvalue is E4=−1.394173009735397 and original-source coefficient
2Z=1.9780554006912363. The prediction is gap/Jz=8−2λ²+λ⁴E4 and weight=2Zλ⁴.

| λ | Full-H gap/Jz | Eigenvector residual | Weight/λ⁴ | Gap error/λ⁶ |
|---|---:|---:|---:|---:|
| .1 | 7.979862132699804 | 5.95e−10 | 1.95563198085 | 1.55000 |
| .2 | 7.917871772902544 | 9.92e−12 | 1.88471235635 | 1.60078 |

Ground residuals are below1e−12. The two-point errors are consistent with the
expected higher-order corrections; they do not prove an asymptotic law. A separate
physical16-spin check validates reduced periodic H and source implementation at
L4 below1e−15, and a finite bright-host Schur check reproduces the extra−1 above.
No finite Hermitian eigensystem here measures a decay width. The proposed infinite
width remains conditional on the earlier effective model and limiting assumptions.

## Artifacts and remaining target

[Runner](../scripts/native_scalar_band_local_proof.py) replays local coefficient,
orbit and explicit-basis controls. It reads a declared frozen full-H output rather
than silently repeating a costly eigensolve. Source and output are supplied under
[the campaign native pack](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/LOCAL_PROOF_PROVENANCE.md).

The next constructive target is the qπ degeneracy, where the earlier bright-host
small-λ expansion is nonuniform. The explicit complete basis permits direct
degenerate perturbation there without inserting a new mode. Uniform large-L
control, equal coupling, larger transverse features, physical state selection and
observational coupling remain unresolved.
