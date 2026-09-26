# Referee: deferred-20260925-integer-gauge a1

Attempt `w-jonathonsmac4f50-j8ab2`. The stencil, the planar moves, and the connected-support search are rebuilt here. The attempt's script is not imported.

The stencil is `(Gp)_j(x) = p_jj(x+e_j) - p_jj(x) + Σ_{i≠j}[p_ij(x) - p_ij(x-e_i)]`. A move is a nonzero finite-support symmetric tensor with `Gp = 0`.

## Verdicts

**Stencil.** On twelve deterministic integer tensors, the lattice formula agrees with `div Q` after the translation `Q_jj = t_j^{-1} P_jj`.

**Planar moves.** In each coordinate plane the named displacement has ten nonzero slots, L1 norm 12, and lies in the kernel. It is the Airy tensor of a monomial: `Q_aa = (1-t_b)^2 φ`, `Q_bb = (1-t_a)^2 φ`, `Q_ab = -(1-t_a)(1-t_b) φ`.

**Divisibility.** The Airy triple and the one-diagonal family `(-2 u_2 u_3, u_1 u_3, u_1 u_2, -u_1^2)` solve the symbolic row equations. With no diagonal, the third row is `-2 u_1 u_2 a`. A two-term polynomial has a double root at `t = 1` only when the exponents agree, because the coefficient determinant is `n - m`. Three nonzero integers with sum zero have L1 norm at least 4.

**Search.** Supports are enumerated in doubled coordinates, with the lexicographically least slot fixed at one of six anchors, and with every touched row forbidden from carrying exactly one support slot. Through size 12 the six anchors produce 1,954,858 nodes and 103 closed leaves. Exactly three leaves have a rational kernel. Each has size 10 and is a planar move, one per plane.

A move whose slots do not all meet through shared rows splits into smaller moves. The search therefore excludes every nonzero move of support at most 9, and every move of support at most 12 is a multiple of a planar move. The planar L1 norm is `12|c|`, so the integer minimum is 12, attained at `±` the named displacements.

**Amplitude.** The monotone paths that build one planar move, in steps of one unit, form a box of 2304 partial states. Only the empty state and the finished move have zero stencil energy. The summed weight is `111150053/31850496`.

## What stays open

The clock-slot table for `Z_N` was not rebuilt. The unit-entry gap between support 14 and the reported 20 was not searched. Whether an integer move of L1 norm 14 exists was not decided.

## Result

HIT: confirmed. Every nonzero finite-support integer move found by the box-free search through support 12 is a planar move. The minimum support is 10 and the minimum L1 norm is 12.
