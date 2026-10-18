# Independent infinite-tiling cluster acceleration check

Independently reproduced the 2x2x2 seed-0 trial's composite acceleration using `/private/tmp/native-cluster-acceleration-control.py`; full output is `/private/tmp/native-cluster-acceleration-control.json`.

The check reuses this reviewer's separate infinite-coordinate binary symplectic commutator implementation from the earlier transport check, not the root's acceleration contraction. It builds C0 with three terms, D C0 with 24 terms, and D² C0 with 207 terms. D in that implementation is i[+sum bonds,.], so the present H=−sum bonds requires a factor (−1)^n on derivative n. There is no periodic lattice used in the derivative construction.

For each of the eight possible anchor positions inside the repeating block, the resulting Pauli words are grouped into actual infinite-tiling blocks using integer floor division, including negative coordinates. Within each block, an explicit 256x256 Kronecker Pauli matrix is constructed, with the highest bit on the left, matching little-endian bit indices and the supplied itertools.product site ordering. Expectations in the supplied normalized NPZ state then factor across blocks. Three hundred distinct local matrix expectations were evaluated.

Results averaged over the eight block anchors:

- <C0>=0.8679072532570364;
- d<C0>/dt=5.341362447431096e−16, consistent with zero at numerical precision;
- d²<C0>/dt²=−9.301400048992662.

Imaginary numerical residuals are at most 1.6e−16. Every anchor separately has the same second derivative to about 2e−14. The root's reported second derivative −9.301400048992663 therefore agrees with an independently constructed operator and explicit local-matrix contraction. This check covers only the 2x2x2 NPZ state, not the larger-block numbers.

The nonzero second derivative is a direct local nonstationarity witness for this specified infinite product tiling under the native Hamiltonian. Unlike merely inspecting extensive finite-volume variance, it establishes change in a local observable without a finite-torus alias or a thermodynamic inference. A nearly zero first derivative does not establish stationarity; a real or symmetry-constrained trial can have zero initial slope and nonzero acceleration. At J=1, the initial expansion is <C0(t)>=0.8679072532570364−4.650700024496331 t²+o(t²), with the linear coefficient numerically zero. Restoring H=−J sum bonds multiplies the acceleration by J² (and by hbar^−2 if hbar is restored).

This is prepared-state dynamics of the chosen trial. It is not an equilibrium spectral function, a scalar-pole identification, or evidence for the cosmological scalar/environment connection.
