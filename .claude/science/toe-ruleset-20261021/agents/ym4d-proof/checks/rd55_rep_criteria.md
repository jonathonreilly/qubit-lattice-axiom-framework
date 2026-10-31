# rd55_rep — criteria (written 2026-10-28, BEFORE the script rd55_rep.py exists)

Author: Opus 5.5 worker (claude-opus-5-5), deliverable ROTDEF.md (T56-R4).

## Purpose
Decide, by exact integer character arithmetic over the hyperoctahedral group H(4) = B_4 (all 4x4 signed
permutation matrices, order 384), whether the lattice symmetry H(4) allows a gauge-invariant DIMENSION-4 local
operator (the space tr(F_{mu nu} F_{rho sigma}), i.e. S^2(A) with A = Lambda^2 R^4) to carry the representation A
of an infinitesimal rotation generator J. If it can, the rotation-breaking insertion of the lattice rotation
identity could have an O(1) (unsuppressed) dimension-4 part. If it cannot, the leading allowed part is of
dimension >= 6 (dimension 5 is excluded separately, by total inversion, in ROTDEF.md).

## Definitions (fixed before running)
- h ranges over the 384 signed permutation matrices; chi_V(h) = tr h; det(h) = sign(pi) * prod(signs).
- chi_A(h) = (tr(h)^2 - tr(h^2))/2; chi_{S2A}(h) = (chi_A(h)^2 + chi_A(h^2))/2; chi_{L2A}(h) = (chi_A(h)^2 - chi_A(h^2))/2.
- chi_{Sym2V}(h) = (tr(h)^2 + tr(h^2))/2; chi_diag(h) = #fixed points of the underlying permutation;
  off-diagonal symmetric rep "6'": chi_{6'} = chi_{Sym2V} - chi_diag.
- Multiplicity m(rho in sigma) = (1/384) * sum_h chi_rho(h) chi_sigma(h) (all characters are integers; real reps).

## Pre-registered PASS/FAIL
- C1 (group): exactly 384 distinct matrices, closed under multiplication. FAIL otherwise.
- C2 (irreducibility): <chi_V,chi_V> = 1 and <chi_A,chi_A> = 1. FAIL otherwise. (C2 for A re-tests the lane's
  GT claim "Lambda^2 R^4 is absolutely irreducible under B_4".)
- C3 (dimensions): chi_{S2A}(1) = 21, chi_{L2A}(1) = 15. FAIL otherwise.
- C4 (R1, scalars): m(trivial in S2A) = 1 (only sum tr F^2) and m(det in S2A) = 1 (only tr F Ftilde).
  Reported value decides R1; R1 HOLDS iff m(trivial in S2A) = 1.
- C5 (R2, DECISIVE): m(A in S2A) reported. R2 HOLDS (no dimension-4 operator carries the rotation-generator
  representation) iff m(A in S2A) = 0. Also report m(A x det in S2A).
- C6 (control that must fire): m(A in L2A) >= 1 and m(A in A x A) = m(A in S2A) + m(A in L2A). If m(A in L2A) = 0,
  the script is declared BROKEN (the commutator structure [F,F] must contain A) and no R2 verdict is drawn.
- C7 (dimension-6 breaking exists): for an abelian plane wave A_nu = eps_nu e^{ikx}, F_{mu nu} -> k_mu eps_nu - k_nu eps_mu,
  evaluate Q_cub = sum_{mu,nu} k_mu^2 F_{mu nu}^2 / (|k|^4 |eps|^2) and the O(4) control
  Q_inv = sum_{mu,nu} |k|^2 F_{mu nu}^2 / (|k|^4 |eps|^2) at (k,eps) = ((1,0,0,0),(0,0,1,0)) and ((1,1,0,0),(0,0,1,0)),
  exact rationals. PASS iff Q_cub differs between the two and Q_inv is equal. (Supports: a non-O(4)-invariant,
  H(4)-invariant dimension-6 term exists, so the leading breaking is genuinely dimension 6, not absent.)
- C8 (6' vs A): <chi_{6'},chi_{6'}> = 1 and <chi_{6'},chi_A> = 0. FAIL otherwise.

## What this check cannot decide
It is a representation-theory (selection-rule) computation. It bounds nothing in the quantum measure; the
non-perturbative size of the dimension-6 insertion is the separate input SRC in ROTDEF.md.
