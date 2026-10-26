# Supplied three-sector pair flow and determinant-loop identities

**Date:** 2026-10-24
**Type:** bounded_theorem
**Primary runner:** `scripts/supplied_three_sector_pair_flow_and_loop_identities_2026_10_24.py`
**Scope:** finite integer arithmetic and conditional determinant-degree identities. No physical tick, anomaly law, family selection, symmetry exclusion or adoption is derived. This source draft is pending independent confirmation.

## Supplied pair in a free abelian group

Work in Z³ with independent basis e_0,e_1,e_2; subscripts are modulo three. These basis vectors are not identified with complex roots of unity. Supply one positive-handed object of label q_l and one negative-handed object of label q_m, with labels in {0,1,2}. Define f(q,h)=h(e_(q+2)-e_(q+1)), h in {+1,-1}, and W=f(q_l,+1)+f(q_m,-1). Direct substitution gives:

| q_l | q_m | W |
|---|---|---|
| 0 | 0 | (0,0,0) |
| 0 | 1 | (-1,-1,2) |
| 0 | 2 | (1,-2,1) |
| 1 | 0 | (1,1,-2) |
| 1 | 1 | (0,0,0) |
| 1 | 2 | (2,-1,-1) |
| 2 | 0 | (-1,2,-1) |
| 2 | 1 | (-2,1,1) |
| 2 | 2 | (0,0,0) |

**Proof.** The three positive flow columns are F_0=(0,-1,1), F_1=(1,0,-1), F_2=(-1,1,0), and W=F_ql-F_qm. Their nine differences are precisely the table. The six unequal-label vectors are ±((1,1,1)-3e_a). This normalization follows from the supplied single pair of opposite hands; it is not implied by an arbitrary nonzero vector. Fix W_F=(-2,1,1) for the pair (2,1).

## Supplied congruences and explicit controls

Supply N in Z_{≥0} and impose N(q_l-q_m)=0 modulo three. Equal labels give all nonnegative N. For unequal labels q_l-q_m is invertible modulo three, so exactly N in 3Z_{≥0} solve it. Alternatively, for the separately supplied componentwise condition N W_F=0 modulo three, the second component requires 3|N and this suffices for every component. The same conclusion holds for any of the six primitive table vectors, all of whose components are congruent to the same nonzero residue modulo three.

The normalization matters: 2W_F=(-4,2,2) has all components nonzero and even; it is not an odd multiple of W_F. Also 3W_F=(-6,3,3) has all components nonzero but vanishes componentwise modulo three. Consequently N(3W_F)=0 modulo three admits every nonnegative N. The primitive constraint admits both N=3 and N=6, as well as N=0; it does not select exactly three. These are arithmetic facts about imposed congruences, not an anomaly derivation or a construction of a symmetric gap.

If multiple pairs are combined, N W assumes equal multiplicity and the same ordered charge pair for every copy. In a heterogeneous sum, sector contributions can cancel: W(2,1)+W(1,2)=0 despite both terms being nonzero. A total cancellation cannot be interpreted as a pairing rule without additional assumptions.

## Determinant degrees on supplied loops

Let k be the coordinate of R/(2pi Z). Supply a continuous periodic U:S¹→U(d), a fixed unitary T with T³=I, and [U(k),T]=0 for every k. The eigenspaces E_a of T with eigenvalues omega^a, omega=exp(2pi i/3), are fixed and orthogonal. Thus U restricts to continuous unitary blocks U_a(k). For a nonempty block define d_a(k)=det U_a(k) in U(1). For an empty block define d_a=1 and W_a=0.

For any continuous circle-valued loop d, lift its restriction to [0,2pi] to a continuous real phase phi with d(k)=exp(i phi(k)). Such a lift exists by subdividing the compact interval into finitely many pieces whose images lie in arcs with continuous arguments, choosing each branch to match at the preceding endpoint. Periodicity implies phi(2pi)-phi(0)=2pi n for an integer n. Any two lifts differ by a constant integer multiple of 2pi, so n is well-defined. Define deg d=n and W_a=deg d_a.

For loops d,e, adding their phase lifts gives deg(de)=deg d+deg e. Negating a lift gives deg(conj d)=deg(d^-1)=-deg d. Reversing the parameter path exchanges endpoints, so deg(d(-k))=-deg d. For same-space matrix loops A,B, determinant multiplicativity therefore gives deg det(AB)=deg det A+deg det B. Since det A†=conj(det A) for unitary A, adjoint and entrywise conjugation both negate determinant degree. No differentiability or phase-sampling algorithm is needed for these statements.

For every supplied integer triple m, the diagonal loop U(k)=diag(exp(i m_0 k),exp(i m_1 k),exp(i m_2 k)), with T=diag(1,omega,omega²), realizes W=m. It is periodic because the m_a are integers; its phase lifts are m_a k. This is an explicit finite-dimensional loop, not a realization of a local lattice tick, a wall spectrum or a physical update rule.

## Conditional sector-map transformation identities

Supply an invertible unitary or antiunitary map Theta that maps E_a to E_sigma(a), for a specified permutation sigma with matching sector dimensions. It must identify the sectors globally and periodically, not only at sampled momenta. For a fixed map, impose one of these three identities for every k:

1. Unitary chiral convention: Theta U(k) Theta^-1=U(k)†.
2. Unitary axis-reversal convention: Theta U(k) Theta^-1=U(-k).
3. Antiunitary Floquet convention: Theta U(k) Theta^-1=U(-k)†.

Write b=sigma(a). In case 1, determinants on E_b give d_a(k)=conj d_b(k), because unitary conjugation preserves the determinant. Taking degrees gives W_a=-W_b. In case 2, d_a(k)=d_b(-k), again giving W_a=-W_b from orientation reversal. In case 3, represent the antiunitary map between sector bases as V times complex conjugation. Its left determinant is conj d_a(k); the right determinant is conj d_b(-k). Hence -W_a=+W_b: complex conjugation on the left contributes minus, while adjoint and orientation reversal on the right contribute two minus signs. Thus W_a=-W_b in this convention also.

The same determinant calculation holds for k-dependent sector identifications if they are continuous, periodic and globally compatible with the displayed equations and fixed permutation. Pointwise cancellation of their determinant factors supplies the same loop equations; finite sample agreement cannot supply those hypotheses.

If a fixed Theta additionally satisfies Theta T Theta^-1=omega^c T^s with c modulo three and s in {+1,-1}, its literal label map is b=s(a-c) for unitary Theta and b=s(-a-c) for antiunitary Theta, modulo three. Indeed, applying Theta T to an a-sector vector yields omega^a Theta v in the unitary case and omega^-a Theta v in the antiunitary case; the right side gives omega^(c+s b) Theta v. Equating exponents and using s²=1 proves both conventions.

As a constructive example, m=(1,-1,0) and the permutation swapping sectors 0 and 1 realize cases 1 and 2 with the corresponding unitary permutation matrix. Composing that matrix with entrywise conjugation realizes case 3. For diagonal monomials, the displayed determinant identities reduce exactly to integer exponent equalities. The primary checks those equalities and the sector-map convention; this does not verify a physical symmetry representation.

## Evidence and scope boundary

The primary declares this note as input, uses exact integers and a literal120-second cap, and exits nonzero for any failed check. It checks all nine pairs, residues and supplied multiplicities 0,1,2,3,6; explicit multiples2 and3; analytic monomial degrees; sign/orientation rules; and controls that reject altered primitive normalization, congruence and transformation signs. No capture is claimed by this draft.

Only the transformation identities and constructive examples are asserted. This note does not derive or ship a zero-component exclusion, physical T/CP breaking, a unique Floquet escape, family-count selection, gappability, least-information selection, fold or gap/energy theorem. Those conclusions require separate specified premises, owners and applicable review. The register and unreviewed dependency branches are not premises of this proof. Earlier stronger claims and failed cases remain in exact-head review recovery; nothing here grants or revokes reported adoption intent or enrolls another PR.
