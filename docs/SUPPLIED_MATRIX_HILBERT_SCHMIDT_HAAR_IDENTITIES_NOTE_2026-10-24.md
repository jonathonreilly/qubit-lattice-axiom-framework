# Supplied matrix decompositions, endpoint Haar moments and common-factor identities

**Date:** 2026-10-24
**Type:** bounded_theorem
**Scope:** positive algebraic identities on the supplied finite matrix objects below.
**Status:** source proposal; independent review/audit owns all retained status.
**Primary runner:** [supplied_matrix_hilbert_schmidt_haar_identities_2026_10_24.py](../scripts/supplied_matrix_hilbert_schmidt_haar_identities_2026_10_24.py).

## 1. Hilbert–Schmidt identity

Let integer `N>=2`, `M` be a complex `N x N` matrix, and let `t_A`, A=1,...,N²-1, be a COMPLETE orthonormal basis of the
traceless Hermitian matrices, normalized by `Tr(t_A t_B)=delta_AB/2`. Define

```text
T=Tr(M M^dag), S=|Tr M|^2/N, C=2 sum_A |Tr(M t_A)|^2.
```

The matrices `I/sqrt(N)` and `sqrt(2)t_A` form an orthonormal basis
for the complex matrix space with Hilbert–Schmidt inner product.
Parseval gives `T=S+C`. Thus `S,C>=0`; when `T>0` their fractions
sum to one. In the explicit fixture `M=I_N`, `(S,C,T)=(N,0,N)`.
A separate exact subset fixture makes the completeness premise concrete:
for N=2, M=sigma_x and only t=sigma_z/2, `(T,S,C_subset)=(2,0,0)`;
with the complete three Pauli generators divided by two,
`(T,S,C_complete)=(2,0,2)`. The runner verifies these exact values.
The theorem applies to the complete family, and the subset values are
recorded as a discriminating finite fixture.

## 2. Positive endpoint Haar moment

Fix a nonzero M and independent Haar `U,V in SU(N)` acting as
`M'=U M V^dag`. Then `T'=T`, and the first matrix-element second moment
`E[W_ij conjugate(W_kl)]=delta_ik delta_jl/N`, for Haar `W=V^dag U`, gives

```text
E|Tr(W M)|^2= sum_ij |M_ji|^2/N=T/N,
E S'=T/N^2, E C'=(1-1/N^2)T.
```

At N=3 the second fraction is 8/9. The hypotheses specify independent
endpoint averaging; same-endpoint conjugation or a physical gauge ensemble
is a different object. The runner samples these stated averages with fixed
seeds; the general identity is the displayed analytic second-moment proof.

## 3. Epsilon reflection and tensor products

Supply an invertible matrix `D` and Hermitian involution `eps` with
`D^dag=eps D eps`. Taking inverses yields `G^dag=eps G eps` for `G=D^-1`.
For a site-diagonal involution with scalar entries eps(x) in {+1,-1},
site blocks M=G(x,y) and p=eps(x)eps(y), `G(y,x)=p M^dag`, hence
`Tr[G(x,y)G(y,x)]=p T=p(S+C)`. Opposite-parity fixtures have raw trace
`-T`; the original unsigned-identity falsifier is preserved as this explicit
finite value, with its original recovery and numerical predicates.

For the supplied tensor-product kernel `(Q tensor M)(Q tensor p M^dag)`,
trace factorization gives `p Tr(Q^2)(S+C)`. The fixture Q=diag(1/2,-1/2),
M=I_3 gives `Tr(Q^2)=1/2`, S=3, C=0. Physical point-split current
construction, vertex factors, Wick contractions and continuum matching are
unperformed objectives, not conclusions of this theorem.

## 4. Scalar, projection and parameterized identities

Scalar multiplication M->zM sends `(S,C,T)` to `|z|^2(S,C,T)`.
The equivariant projector `P_adj(M)=M-(Tr M/N)I` has `(S',C',T')=(0,C,C)`;
`P_adj(U M U^dag)=U P_adj(M)U^dag` follows by trace invariance.
These are specified matrix maps, with no OZI or planar interpretation.

For the defined polynomial `Pi_k=C+k S`, direct evaluation gives
`Pi_0=C`, `Pi_1=T`. For supplied F=8/9 and a positive denominator,
`K(k)=1/[F+k(1-F)]` gives `K(0)=9/8`, `K(1)=1`.
For nonzero real `(g1b,g2b)` and K>0, defining gi=sqrt(K)gib yields
`g1^2/(g1^2+g2^2)=g1b^2/(g1b^2+g2b^2)` by cancellation.
These are parameterized identities only; no identifiability theorem or
physical selection claim is made from them.

## 5. Provenance and scope

This is a distinct positive mathematical owner. Positive subarguments were
extracted from the preserved unlanded proposal at Git
`ee6fd241ce2af117bf9935914f201e20604723fa`. The original object-pin and
registration note/runner/cache trios are unchanged by this extraction and
remain outside its approval. Their negative claims and N1–N8 limitations
remain held; this source neither retires nor certifies those claims.
The earlier source and cache recovery is retained with all original54 PR
paths. No former negative conclusion is a premise of the proofs above.
Physical current construction, matching and parameter selection remain
unperformed research objectives. This theorem only gives the stated
positive identities on supplied objects.

## 6. Verification

The runner retains seeded finite matrix, inverse-reflection, Haar-sample,
scalar/projection and parameter-evaluation checks. Numerical examples
support these identities; universal proofs are given above. It reads no
repository file or local helper; its own-note declaration intentionally
binds this argument for the execution record. No physical or negative-claim
packet verdict is produced. Cache refresh awaits independent source review.
