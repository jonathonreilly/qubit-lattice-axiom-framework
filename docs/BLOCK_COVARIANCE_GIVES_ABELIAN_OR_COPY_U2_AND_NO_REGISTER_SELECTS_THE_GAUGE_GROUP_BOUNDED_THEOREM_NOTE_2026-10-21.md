---
claim_id: block_covariance_gives_abelian_or_copy_u2_and_no_register_selects_the_gauge_group_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "On the supplied 8-corner block with its 24 rotations and one mode per corner: plain covariance leaves a U(1)^4 one-body commutant, the spin-3/2 twist of the coin leaves M_2(C) (a copy U(2)) which the coin breaks to U(1) x U(1), site-diagonal covariant operators are scalars, and no covariant one-body su(3) exists; on the 4^3 torus only the body-diagonal copy generator commutes with the massless tick; per-site register size selects no gauge group; and on a supplied Fock register Lambda(C^p + C^q) with the even sector read as left-handed, vacuum neutrality and anomaly freedom fix Y = N2/2 - N3/3 for 3+2 but hold for every split with p+q from 4 to 6. No gauge group, 3+2 split, chirality or non-abelian carrier is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/block_covariance_gives_abelian_or_copy_u2_and_no_register_selects_the_gauge_group_2026_10_21.py
---

# Block covariance gives an abelian or copy U(2) commutant, and no register selects the gauge group

Claim type: bounded_theorem.
Primary runner: `scripts/block_covariance_gives_abelian_or_copy_u2_and_no_register_selects_the_gauge_group_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks whether the block structure of the register's tick, or the size of a per-site or per-link register, selects a non-abelian gauge group. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the registers used.

## One-body covariance on a block

- Plain corner permutations split the 8 modes into multiplicity-free summands of dimension 1, 1, 3 and 3 (A1 + A2 + T1 + T2). The commutant has dimension 4 and is abelian (max [X, Y] = 4e-16), so it is U(1)^4.
- Under the spin-3/2 twist each rotation sends a corner mode to a unit phase times its image, and the coin W0 is covariant (error 6e-15).
- Twisted, |chi| is 8 at the identity, 2 on the 8 body-diagonal turns and 0 elsewhere, so 8 = 2 x (spin 3/2). The commutant is M_2(C): dimension 4, non-commutative (max [X, Y] = 0.71) with a one-dimensional centre. This is a forced copy U(2).
- There is one covariant operator per corner distance 0, 1, 2, 3. W0 lies in the copy algebra with eigenvalues +1 and -1, four of each.
- Covariant site-diagonal block operators are scalars only, so a per-site phase register can compensate only the U(1) block phase.
- The commutant of the rotations and the coin is span{1, W0}: the coin breaks the copy U(2) to U(1) x U(1).
- The symmetric-base su(3) used in the repository's Cl(3) colour embedding is not rotation covariant, plain or twisted (max ||[V_R, T^a]|| = 2.00). No su(3) fits in u(1)^4 or u(2), so no covariant one-body SU(3) acts on a block.

## The copy algebra on the tick

Lift the three copy generators to all even blocks of the two-partition tick on the 4^3 torus (64 modes). Exactly one commutes with the massless tick, the body-diagonal one (singular values 9.238, 8.222, 0.0), because it anticommutes with both half-ticks. A mass a = 0.3 breaks it by 2.26. The copy SU(2) is not a symmetry of the tick.

## Register size selects nothing

For link registers in G_L x G_R with the link operator in (N, N-bar), (N,1) + (1,N) carries covariant link operators in 2N states (dimension 2 for N = 2, 1 for N = 3), while (2,2) and (3,1) + (1,3-bar) carry none. Counting SU products that fit in m qubits gives 0, 1, 4, 11, 22, 43 for m = 1 to 6, of which 0, 1, 2, 3, 4, 5 fill exactly. SU(3) x SU(2) never fits exactly, since 2 x 6 is not a power of 2, and no SU(3) factor ever fills a qubit register.

## A supplied Fock register

Take Lambda(C^p + C^q) and read the even-parity sector as left-handed Weyl states. For (3, 2) the even sector is (3,2) + (3b,1) + (3b,1) + (1,2) + (1,1) + (1,1). Y = N2/2 - N3/3 is vacuum-neutral and free of the gravitational, Y^3, SU(3)^2 Y, SU(2)^2 Y and SU(3)^3 anomalies, with Q : u^c : d^c : L : e^c = 1 : -4 : 2 : -3 : 6. Without vacuum neutrality the anomaly-free U(1)s form span{Y, B - L} with B - L = 1 - 2 N3/3, and the empty register is neutral only for Y. A unique vacuum-neutral anomaly-free U(1) exists for every split with p + q in {4, 5, 6} and for none with p + q <= 3, so the condition fixes the U(1) once a split is given but does not choose 3 + 2. A block offers no covariant 3 + 2 split: twisted invariant mode subspaces have dimension 0, 4 or 8, and the plain block has only 1, 1, 3, 3 summands.

## Many-body sectors

The twisted block rotations on n-particle Fock sectors carry multiplicities up to 10, so U(m) commutants with m >= 3 occur. They act on n-particle states, not as one-body transformations of the modes, so they are not minimal-coupling gauge groups.

## Checks

The runner prints `TOTAL: PASS=15 FAIL=0`. Its PASS lines cover the plain and twisted commutants, coin covariance, the operators by corner distance, the scalar site-diagonal operators, the coin-broken commutant, the non-covariance of the su(3) embedding, the copy generator on the tick, the link-register count, the qubit-register count, the 3 + 2 hypercharge, the two-dimensional anomaly-free span, the split survey, the absence of a covariant 3 + 2 subspace, and the many-body multiplicities. As an estimate, LEP colour factors C_A = 2.89 +- 0.21 and C_F = 1.30 +- 0.09 agree with SU(3)'s 3 and 4/3.

## Supplied and boundary

Supplied: the block, its 24 rotations, the spin-3/2 twist from the coin, one mode per corner, the link-register definition, the Fock register and its split, the even sector read as left-handed (a chirality choice), and vacuum neutrality (a normal-ordering choice). A register of more than one qubit per site would change the qubit axiom. No gauge group, 3 + 2 split, chirality or non-abelian carrier is established.
