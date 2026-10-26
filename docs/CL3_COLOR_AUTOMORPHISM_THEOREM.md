# Selected symmetric-base SU(3) embedding and dimension fraction

**Type:** bounded_theorem
**Primary runner:** `scripts/verify_cl3_sm_embedding.py`
**Correction:** 2026-10-21. Supplied finite carrier only.

The original note is recoverable at commit
`f24d17d97d372df977476e4a69674577f31af575` under this path.
The [paired carrier theorem](CL3_SM_EMBEDDING_THEOREM.md) supplies the explicit
finite definitions used here. No physical color, lepton, generation or coupling
identification follows from this construction.

On the chosen complex base C² tensor C², swapping the factors has a
three-dimensional symmetric eigenspace and one-dimensional antisymmetric
eigenspace. An orthonormal basis of the former is |00>, |11>, and
(|01>+|10>)/sqrt(2). Let E be its isometric inclusion. For the eight standard
Hermitian traceless generators T_a of su(3), with Tr(T_a T_b)=delta_ab/2,
set C_a=(E T_a E†) tensor I₂ on the supplied eight-dimensional carrier.
Since E†E=I₃, this preserves commutators and defines the selected Lie-algebra
embedding. The group acts as SU(3) on the symmetric base and identity on the
antisymmetric base. It commutes with fiber I₄ tensor SU(2). It also commutes
with the supplied Y=P_sym/3-P_anti because Y is scalar on each base block.
The physical identification of any of these groups remains open.

The matrix-unit completeness identity, after removing the identity direction,
is

    sum_a (T_a)_ij (T_a)_kl = delta_il delta_kj/2 - delta_ij delta_kl/6.

Including T_0=I₃/sqrt(6) restores delta_il delta_kj/2. Thus the traceless
subspace of End(C³) has complex dimension eight, compared with total dimension
nine. The dimension fraction is exactly 8/9. This is not a universal fraction
of a bilinear, amplitude or coupling: the traceless projection
Q(A)=A-Tr(A)I₃/3 gives Q(I₃)=0 and Q(A)=A for traceless A. These controls
rule out a matrix-independent 8/9 projection fraction. No finite-N correction
estimate or EW coefficient follows from counting dimensions.

The choice of symmetric base supplies dimension three; spatial axis counting
alone does not establish its physical identification. The current primary
checks the explicit embedding, Fierz identity, commutators and projection
controls. Its pass count is finite algebra evidence, not physical closure.
Historical references to native gauge, R_conn, EW matching and running were
contextual routes; no theorem from those lanes is a premise here.
