# Focused native joining check

Disposition: PASS for the fixed-g, finite-array joining test, including exact neutral intraband darkness at the physical endpoint g=Jz. No infinite-embedding or all-feature conclusion follows.

## Interface energy and its restricted minimum

For two aligned halves the existing joining bonds give -g sum_xy sA_xy sB_xy. If both halves are in their plaquette-positive pattern sets, sA=aA bA and sB=aB bB, this factorizes exactly as in the draft. A relative gauge pattern changing a of the four x labels and b of the six y labels mismatches 6a+4b-2ab columns. The minimum nonzero mismatch is four, attained by flipping a complete length-four row. Thus the minimum mismatch energy within these two gauge-pattern sets is 2g times four, namely 8g. Positive g is minimized only when the physical patterns agree; the a,b parametrization redundancy does not create another physical pattern.

The qualifier matters: 8g is not the unrestricted microscopic interface excitation gap at lambda=0. An arbitrary relative column pattern can mismatch a single column and cost 2g. The draft explicitly says relative gauge patterns, so its claim is correct. For every fixed positive g these interface costs precede transverse small-lambda scales. At g=0 there are independent halves, and the argument does not apply uniformly through that point.

## Joined plane representation and neutral selection

At g=Jz this is exactly the original directional Hamiltonian on an open 4x6x10 array, with the previously absent vertical bonds restored at native strength. No new interaction type or weak mediator coupling is introduced. Full X planes and Y planes intersect on ten sites and commute; their intersections with Z planes have even transverse lengths as well.

On a fully aligned joined column pattern, a Y plane has phase i^(4*10) times product_x s_xy^10=+1. X planes have no phase. The combined total X/Y product has phase i^240=+1 and equals Z_all, which is +1 on aligned columns. Thus the plaquette-positive patterns form the regular representation of the row/column-flip quotient with 2^(4+6-1)=512 distinct characters, each occurring once.

For sufficiently small lambda at the fixed dimensions, the isolated continuation of this plaquette-positive band retains one state per character by symmetry and continuity of character ranks. Every operator commuting with all full physical planes is diagonal within this band. There can therefore be no inelastic matrix element between two distinct states of this band, even if their energies split by tiny amounts. This is exact selection, not only a leading-order cancellation.

Each original longitudinal distance-two ZZ term commutes with the full planes. The diagnostic restricted to either old half, the full joined diagnostic, and terms crossing the former interface are all neutral. Consequently the finite odd-half neutral low-band activation cannot remain as a neutral transition inside the joined plaquette-positive band. It could reorganize into transitions to other bands; the selection rule does not exclude those or imply that all responses vanish. It also does not identify a continuation of individual odd-half eigenstates through the singular g=0 limit.

## Inhomogeneous pair-column amplitude

At minimal transverse order, both neighboring columns are flipped together on selected longitudinal layers. This reduces the path problem to an open Ising chain of ten pair variables with couplings 2J_i and transverse flip magnitude Jperp. A proper flipped subset S has excitation cost 4 sum_(i crossing S) J_i. The leading tunneling amplitude between the two fully aligned configurations is

 t_L=Jperp^L / product_(i=1,...,L-1)(2J_i).

One derivation is the leading edge-Majorana coupling of that open transverse Ising chain: iterating the zero-mode recurrence multiplies Jperp/(2J_i) along the L-1 internal bonds, with one remaining endpoint Jperp; normalization corrections start at higher transverse order for fixed positive couplings. This is also precisely the native minimal-word path sum. For even L the X and Y pair amplitudes have the same Hamiltonian sign -t_L.

Here eight J_i equal Jz and the interface bond equals g, giving t10=Jperp^10/[(2Jz)^8(2g)]. At g=Jz this is Jz lambda^10/512. An independent exact Fraction recursion over all 1024 layer subsets confirmed the product denominator at Jz=1 and g=1,1/3,2; results are saved in /private/tmp/neutral-native-join-independent.json. These checks supplement the Ising-chain derivation, not a full 240-spin diagonalization.

The coefficient is meaningful as lambda tends to zero at fixed g>0. Its 1/g factor does not license extrapolation to g comparable to a transverse tunneling scale, much less to g=0. Pair-column tunneling itself still leaves P+ and must not be identified directly with its ground-band splitting.

## Scope

This test exposes a specific boundary dependence of finite odd-array neutral activation: joining two such arrays using their native bonds restores an even-height, multiplicity-one character band and exact neutral darkness there. It neither excludes other connected feature constructions nor proves an actual infinite-lattice embedding theorem. No conclusion about all forces or a universal absence of scalar phenomena is supported.

Checked /private/tmp/neutral_native_join_root.md. No repository edits or formal audit.
