# Working join to the actual dynamical gauge transfer

Personal derivation in progress, 2026-09-16. This file records hypotheses before the finite check. It does not promote either the current Block02-03 proposals or prior PR8162 to independently retained premises.

Use the exact positive paired multiplier F_pair,delta(theta) of Block03 and the calibrated clock kernel Q_delta,N of prior PR8162, frozen at0f02dc5127416f347e231bbd8aa7c2a8b58a02fa. The spatial Villain factor B_delta(theta) is the actual normalized factor of that prior pack, with y=delta/(2g²). Define

    M_delta(theta)=B_delta(theta)^(1/2) F_pair,delta(theta)^(1/2),
    T_delta,N=M_delta,N Q_delta,N M_delta,N.

The scalar B commutes with F_pair. This makes T positive and gauge compatible. For an open slab with M_t matter/spatial slices and M_t-1 temporal gauge transitions, the candidate boundary vector is

    v_delta(theta)=M_delta(theta) Omega_pair,
    Z_delta,N=<v_delta,T_delta,N^(M_t-1) v_delta>.

Expanding kernels should give a product of B_delta at every slice and the exact paired Wilson determinant from Block03. The endpoint M factors in v are necessary: using Omega_pair as the boundary vector would leave only half of each endpoint matter/spatial slice. Haar normalization and the discrete Markov-kernel normalization must be checked explicitly. Omega_pair is sitewise neutral, so this vector lies in the physical Gauss sector and an additional physical projector acts as the identity on it. Temporal gauge fixing on an open interval has no Polyakov obstruction.

On a fixed spatial graph, the exact multiplier has

    F_pair,delta=I-delta H_pair+O_graph(delta²),
    M_delta=I-delta(V+H_pair)/2+O_graph(delta²).

Its Fourier series need not be finite. What is finite Laurent is its first derivative V+H_pair; the uniform O(delta²) multiplier remainder is sufficient for the finite-Fourier core argument in prior PR8162. A graph-dependent declared scalar energy shift should make the actual M_delta contractive for every sufficiently small delta. One may take a bound from ||F_pair,delta||<=exp(C delta), rather than incorrectly assuming the normalized boundary amplitude is at most1.

The expected joint delta->0,N->infinity Hamiltonian is

    H=(g²/2)sum E_l²+g^-2 sum_p(1-cos curl theta_p)+H_pair(theta),

with integer Gauss constraint D E=Q_first-Q_second, and the specified neutral boundary state. The same one-step, all-mode kinetic-floor and compactness arguments should give the fixed-graph product, resolvent, ground-space and Gibbs limits after the scalar shift. These state conclusions are conclusions about the positive transfer; the original open determinant represents its particular boundary amplitude, not its thermal trace. No infinite-volume or fixed finite-N phase follows.

## Planned independent finite construction

Use a two-site single-edge spatial graph. It has a nontrivial local Gauss constraint and matter hopping, but no spatial plaquette or propagating gauge mode. In a basis diagonalizing the spectator spin, the four-component Wilson operator is two unitarily equivalent two-component blocks. The half-filled Fock sector of one block has dimension6. Two copies and their two conjugates give dimension6^4=1296. Verify the original four-component determinant against these reduced blocks before using the reduction.

On the physical one-edge space, each matter basis state fixes the centered electric label modulo N by its site charge. The exact transfer can therefore be applied in the1296-dimensional matter space using four tensor factors and the diagonal calibrated electric eigenvalue. Compare its open amplitude, including endpoint M factors, with direct summation over short finite-clock gauge histories and the original time-Dirac determinant. Then compare joint time/clock refinement with a separately built sparse CAR Hamiltonian plus the integer electric energy. The lack of spatial plaquettes limits this check; the general magnetic factor follows from the scalar product expansion only if that algebra is actually verified.
