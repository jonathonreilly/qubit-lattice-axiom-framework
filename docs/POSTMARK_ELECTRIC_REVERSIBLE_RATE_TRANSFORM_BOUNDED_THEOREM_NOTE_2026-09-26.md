---
claim_id: postmark_electric_reversible_rate_transform_2026_09_26
claim_type: bounded_theorem
claim_scope: Conditional on the supplied finite-spin one-vacancy path, exact row factorization, and signed Casimir labels,
  the staggered Jacobi matrix is unitarily equivalent to an explicit finite reversible birth-death Laplacian.
  No eigenphase, kernel, fixed-time readout, or framework-axiom conclusion is claimed.
upstream_dependencies:
- fast_vacancy_motion_after_formation_bounded_theorem_note_2026-09-24
- postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
- zero_mode_and_goegenbauer_limit_bounded_theorem_note_2026-09-24
runner: scripts/postmark_electric_reversible_rate_transform_2026_09_26.py
---

# Exact reversible-rate transform for the post-mark Jacobi operator

**Date:** 2026-09-26
**Type:** bounded theorem
**Status:** proposed_retained

## Result

Conditional on the supplied finite-spin one-vacancy factorization, the staggered operator is exactly a reversible nearest-neighbor Laplacian after conjugation by its positive zero mode. The rates are the individual Casimir factors already present in the two-hop rows. This gives a simpler scalar recurrence for the finite-spin spectrum and a concrete starting point for a block-transfer or matrix-orthogonal-polynomial analysis.

It does not solve the fixed-time electric scalar. In particular, the transformed recurrence still has a five-residue coefficient pattern, and no global moving-index phase or overlap estimate follows from this identity.

## Definitions and exact statement

Let (C=S(S+1)), (I_S=[-5S,5S-4]\cap\mathbb Z), and (N_S=J A_S^*A_S J), where (J|n\rangle=(-1)^n|n\rangle). For each in-domain edge (n\to n+1), write the supplied row of (A_S) as

\[
(A_S)_{r,n}=-\sqrt{w^+_{S,n}},\qquad
(A_S)_{r,n+1}=-\sqrt{w^-_{S,n}},\qquad
w^+_{S,n}=\frac{R_{m_L(n)}}{C},\quad
w^-_{S,n}=\frac{R_{m_R(n)}}{C},
\]

where (R_m=C-m(m+1)), and (m_L,m_R\in[-S,S-1]\) are the exact effective labels in the [zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md). Let (g_S>0) be the normalized vector proportional to the unique zero mode of (N_S), and set \(\pi_S(n)=g_S(n)^2\). Define the endpoint rates to be zero when the corresponding neighbor lies outside (I_S). Then the isometry

\[
U_S:\ell^2(I_S,\pi_S)\to\ell^2(I_S),\qquad (U_Sf)(n)=g_S(n)f(n),
\]

satisfies the exact identity below, with each neighbor term included only
when that neighbor lies in \(I_S\):

\[
(U_S^{-1}N_SU_Sf)(n)
=w^+_{S,n}\,[f(n)-f(n+1)]
+w^-_{S,n-1}\,[f(n)-f(n-1)].
\tag{1}
\]

Thus (U_S^{-1}N_SU_S) is a positive reversible birth-death Laplacian with detailed-balance conductance

\[
\kappa_{S,n}=\pi_S(n)w^+_{S,n}=\pi_S(n+1)w^-_{S,n}.
\tag{2}
\]

After multiplying (1) by (C), the rates are the integer quadratics (R_{m_L(n)}) and (R_{m_R(n-1)}), rather than square roots of products. The signs in (1) follow from the staggering (J); the corresponding continuous-time Markov generator would be the negative of this positive Laplacian. The statement here is an operator identity, not an added stochastic physical law.

## Proof

The null equation for each row of (A_SJ) gives

\[
\frac{g_S(n+1)}{g_S(n)}
=\sqrt{\frac{w^+_{S,n}}{w^-_{S,n}}}.
\]

The positive off-diagonal entry of (A_S^*A_S) on edge (n\to n+1) is \(\sqrt{w^+_{S,n}w^-_{S,n}}\); conjugation by (J) changes its sign. Its contribution after conjugation by (g_S) is therefore

\[
-\sqrt{w^+_{S,n}w^-_{S,n}}\,\frac{g_S(n+1)}{g_S(n)}=-w^+_{S,n}.
\]

The diagonal of (N_S) is (w^+_{S,n}+w^-_{S,n-1}). The left off-diagonal term similarly becomes \(-w^-_{S,n-1}\), yielding (1). Multiplying the zero-mode ratio by the edge coefficient gives (2); this proves detailed balance and the Dirichlet form

\[
\langle f,U_S^{-1}N_SU_Sf\rangle_{\pi_S}
=\sum_{n,n+1\in I_S}\kappa_{S,n}|f(n+1)-f(n)|^2.
\]

At either endpoint the term toward the missing neighbor is omitted; equivalently, its rate is set to zero and its out-of-domain value is unused. This is an edge-domain convention, not a claim that an out-of-domain Casimir factor vanishes. With that convention the same formula holds without an extra boundary condition or boundary term.

For an eigenfunction \(L_S f=\lambda f\), where \(L_S=U_S^{-1}N_SU_S\), define the edge flux \(J_n=\kappa_{S,n}[f(n+1)-f(n)]\). Multiplying the eigen-equation by \(\pi_S(n)\) gives the exact flux balance

\[
J_n-J_{n-1}=-\lambda\,\pi_S(n)f(n).
\]

For any two solutions \(f,g\) at the same eigenvalue, the discrete Wronskian
\[
W_n=\kappa_{S,n}\bigl(\overline{g(n)}f(n+1)-\overline{g(n+1)}f(n)\bigr)
\]
is independent of \(n\) on the common interior domain. These identities expose a transfer invariant; they do not provide its large-\(S\) connection coefficients.

## Verification and scope

The runner reconstructs \(A_S^*A_S\) from the physical charge/electric-flux legal-hop enumeration in `scripts/core_derivation.py`, constructs the positive zero mode by the exact row recurrence, and checks (1), (2), the zero-mode equation, and endpoint behavior for every site at sentinel spins (1,2,3,5,8,12,20,32). This is finite corroboration of the algebraic proof, not a substitute for it.

The exact rate form may support a five-site block-transfer or matrix-valued orthogonal-polynomial route. For the formal recurrence with (C) held fixed, a degree-one scalar-cell ansatz (F_s(h)=h+c_s) is inconsistent. Its (h^2) coefficients force

\[
(c_0,c_1,c_2,c_3,c_4)=(c,c+1/5,c+2/5,c+3/5,c+4/5).
\]

Substitution into the (h^1) coefficients then gives (E=2/5) from residue (s=0) and (E=0) from residue (s=2), a contradiction. This only rejects that elementary ansatz for the formal five-residue recurrence; it does not rule out a matrix-polynomial solution, an exact finite-spin diagonalization, or other spectral methods.

The remaining electric obligation is still the limit, or a rigorously separated subsequence, of the fixed weighted interior kernel scalar at (t=1/4). Equation (1) does not control the long-time phases (T=C/4\), the two same-fiber crossings, or the central moving-index layer. The finite-spin dynamics, preparation, and output remain supplied model inputs; this note derives no bridge from the four framework axioms and proposes no axiom update.

## Provenance

The runner takes its signed effective-label table from scripts/postmark_electric_five_site_inter_fiber_phase_2026_09_24.py; the independent physical hop reconstruction is in scripts/core_derivation.py.

The exact coefficient and zero-mode hypotheses are stated in the canonical [zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md), whose fixed-index conclusion does not cover the moving-index phases. The physical hop reconstruction is in `scripts/core_derivation.py`. The runner records hashes of these inputs and makes no audit-status change. Formal independent audit is required before this author-proposed status could be effective retained status.
