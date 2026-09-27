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

Conditional on the supplied finite-spin one-vacancy factorization, the staggered operator is exactly a reversible nearest-neighbor Laplacian after conjugation by its positive zero mode. The rates are the individual Casimir factors already present in the two-hop rows. This gives a simpler scalar recurrence for the finite-spin spectrum and a concrete starting point for a block-transfer or matrix-orthogonal-polynomial analysis. For the auxiliary cell obtained by periodicizing the site rates, its determinant-one transfer and twisted Floquet boundary are exactly equivalent to the corresponding five-site Hermitian block; that periodic cell has a wrap-link convention distinct from the existing slowly varying local symbol.

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

Combining this balance with the definition of \(J_n\) gives an exact two-component transfer across every in-domain edge:
\[
\begin{pmatrix}f(n+1)\\J_n\end{pmatrix}
=
\begin{pmatrix}
1-\lambda\pi_S(n)/\kappa_{S,n}&1/\kappa_{S,n}\\
-\lambda\pi_S(n)&1
\end{pmatrix}
\begin{pmatrix}f(n)\\J_{n-1}\end{pmatrix}.
\]
Each transfer matrix has determinant one. The finite path's left boundary starts with \(J_{n_{\min}-1}=0\); its right endpoint supplies the terminal eigenvalue condition. This is an exact scalar transfer representation, although its coefficients still vary with \(n\).

For any two solutions \(f,g\) at the same eigenvalue, the discrete Wronskian
\[
W_n=\kappa_{S,n}\bigl(\overline{g(n)}f(n+1)-\overline{g(n+1)}f(n)\bigr)
\]
is independent of \(n\) on the common interior domain. These identities expose a transfer invariant; they do not provide its large-\(S\) connection coefficients.

## First-subprincipal cell coefficients with the gauge restored

Write \(n=5h+s\), \(u=h/S\), \(w=1-u^2\), and use the supplied five-site edge offsets
\[
\ell=(0,1,0,1,1),\qquad \rho=(0,0,0,1,0).
\]
For \(u\) in any fixed compact subset of \((-1,1)\), expansion of the exact Casimir factor gives, uniformly there,
\[
\frac{R_{h+a}}{C}=w+\frac{\alpha_a(u)}{S}+O(S^{-2}),\qquad
\alpha_a(u)=u^2-u(2a+1).
\]
On an edge inside the cell, the zero-mode recurrence therefore gives
\[
\frac{g_{h,s+1}}{g_{h,s}}
=1+\frac{\alpha_{\ell_s}-\alpha_{\rho_s}}{2wS}+O(S^{-2}).
\]
The same expression holds on the edge \(s=4\) when its endpoint is read as \((h+1,0)\); this is the cell-wrap edge, not a periodicity assumption on \(g\).

The Hermitian matrix is \(N_S=G L_S G^{-1}\), where \(G\) is multiplication by \(g_S\). Consequently the positive Hermitian link magnitude on the edge \((h,s)\to(h,s+1)\) is the rate \(R_{h+\ell_s}/C\) times \(g_{h,s}/g_{h,s+1}\), including the cell-wrap edge. Its \(S^{-1}\) coefficient is
\[
\alpha_{\ell_s}-\frac{\alpha_{\ell_s}-\alpha_{\rho_s}}{2}
=\frac{\alpha_{\ell_s}+\alpha_{\rho_s}}{2}.
\]
The diagonal coefficient is unchanged by the diagonal gauge and is
\[
\alpha_{\ell_s}+\alpha_{b_s},
\]
where \(b=(-1,0,0,0,1)\) is the preceding-edge offset tuple supplied by the signed-label table. These are exactly the Hermitian first-subprincipal links and diagonals in the existing five-site symbol note. This calculation repairs the local coefficient comparison for the non-symmetric rate recurrence. The expansion is not uniform at \(|u|\to1\), and it gives no transport, crossing connection, central-layer, or long-time phase estimate.

## Second-order frozen-band coefficient away from crossings

For this paragraph, \(N_S(u,k)\) denotes the frozen five-by-five Hermitian Bloch matrix obtained by setting \(h=uS\) in the exact cell coefficients and taking the cell phase \(\theta=5k\pmod{2\pi}\). Its principal matrix \(H_0\) has diagonal \(2w\) and nearest-neighbor link magnitude \(w\). Writing \(\varepsilon=S^{-1}\), the exact rate expansion one order further is
\[
\frac{R_{h+a}}{C}
=w+\frac{\alpha_a}{S}+\frac{\gamma_a}{S^2}+O(S^{-3}),
\qquad
\gamma_a(u)=-(u-a)(u-a-1).
\]
Indeed,
\[
\frac{R_{h+a}}{C}
=\frac{w+\varepsilon[1-u(2a+1)]-\varepsilon^2a(a+1)}
{1+\varepsilon},
\]
and division gives the displayed \(\alpha_a,\gamma_a\). Since \(w\) is bounded away from zero on each compact interior set, Taylor expansion of the square root of two rate factors is uniform and gives the stated \(\beta_s^{(2)}\).
Thus the Hermitian cell matrix \(N_S(u,k)\) has the expansion
\[
N_S(u,k)=H_0(u,k)+S^{-1}H_1(u,k)+S^{-2}H_2(u,k)+O(S^{-3}),
\]
uniformly when \(u\) stays in a compact subset of \((-1,1)\). The diagonal coefficients in \(H_1,H_2\) are
\[
d_s^{(1)}=\alpha_{\ell_s}+\alpha_{b_s},\qquad
d_s^{(2)}=\gamma_{\ell_s}+\gamma_{b_s},
\]
and the positive-link coefficients are
\[
\beta_s^{(1)}=\frac{\alpha_{\ell_s}+\alpha_{\rho_s}}2,\qquad
\beta_s^{(2)}=\frac{\gamma_{\ell_s}+\gamma_{\rho_s}}2
-\frac{(\alpha_{\ell_s}-\alpha_{\rho_s})^2}{8w}.
\]
The corresponding off-diagonal matrix entries are the negatives of these link coefficients, with the five-site Bloch wrap phase on the fifth edge.

Let \(k_r=k+2\pi r/5\), \(v_r(s)=5^{-1/2}e^{ik_rs}\), and \(\mu_r=2w-2w\cos k_r\), for \(r=0,\ldots,4\). If the selected principal band is separated from the other four by a fixed positive gap, finite-dimensional Hermitian perturbation theory gives
\[
\lambda_S(u,k)=\mu_0+\frac{\nu_1(u,k)}S+\frac{\nu_2(u,k)}{S^2}+O(S^{-3}),
\]
where
\[
\nu_1=\langle v_0,H_1v_0\rangle,\qquad
\nu_2=\langle v_0,H_2v_0\rangle+
\sum_{r=1}^4\frac{|\langle v_r,H_1v_0\rangle|^2}{\mu_0-\mu_r}.
\]
The first coefficient agrees with the five-site note's
\[
\nu_1=2u^2(1-\cos k)+\frac{u(18\cos k-16)}5.
\]
The mixing terms in \(\nu_2\) cannot be dropped. Standard finite-dimensional Hermitian perturbation theory, with the positive band-gap lower bound and the uniform matrix remainder above, yields the stated \(O(S^{-3})\) remainder uniformly on compact sets of \((u,k)\) that stay away from degeneracies. At \(T=C/4\), the \(S^{-2}\) eigenvalue term contributes an order-one phase, so first-subprincipal data alone are insufficient for the fixed-time readout.

This is a frozen, nondegenerate cell expansion. Its error statement is uniform only on compact interior \(u\)-sets and band sets with a positive gap. It does not cover Bragg crossings, the central moving-index layer, turning points, endpoints, global quantization, or the prepared-state overlap sum. The runner checks the coefficient formula at one gap-separated sample; that check is corroboration, not proof of the uniform perturbation bound.

## Periodicized rate cell and the wrap convention

There is also an exact transfer representation for one explicitly periodicized auxiliary cell. Freeze the site forward and backward rates as \(p_s=R_{h+\ell_s}/C\) and \(q_s=R_{h+b_s}/C\), where \(b=(-1,0,0,0,1)\) is the preceding-edge tuple and indices \(s\) are periodic modulo five. This is a defined auxiliary periodic operator; it is not the slowly varying finite-spin operator with its coefficients held at every physical edge.

Set \(\pi_0=1\) and \(\pi_{s+1}=\pi_s p_s/q_{s+1}\), with \(q_5=q_0\), and write \(\Gamma=\sqrt{\pi_5}\). Detailed balance on each periodic edge gives \(\pi_s p_s=\pi_{s+1}q_{s+1}\); conjugation by \(\sqrt{\pi_s}\) therefore gives a Hermitian block with diagonal \(p_s+q_s\) and link magnitude \(\sqrt{p_s q_{s+1}}\), including wrap link \(\sqrt{p_4q_0}\). For a Bloch state \(\psi_{s+5}=z\psi_s\), the rate variable \(f_s=\psi_s/\sqrt{\pi_s}\) obeys \(f_{s+5}=z\Gamma^{-1}f_s\). The conductance flux scales as \(J_{s+5}=z\Gamma J_s\), so the cell transfer boundary is \(P y=z\,\mathrm{diag}(\Gamma^{-1},\Gamma)y\), where \(z=e^{i5k}\). Since both transfer and twist have determinant one, \(\det(P-zD)=1-z\operatorname{tr}(P^{-1}D)+z^2\), and the block eigenvalue condition is \(\operatorname{tr}(P^{-1}D)=z+z^{-1}=2\cos(5k)\), with \(D=\mathrm{diag}(\Gamma^{-1},\Gamma)\). The runner checks this condition at every eigenvalue of the five-by-five Hermitian block for five large-spin sentinels; its largest residual is below \(4.7\times10^{-14}\). Using the residue-four edge reverse factor instead of the periodic site-zero backward rate \(q_0\) fails this check, with residual \(2.17\times10^{-2}\) at \(S=320\).

This auxiliary periodicization changes only the wrap link at first subprincipal order relative to the existing local frozen-cell symbol. Its wrap coefficient changes by \(u/S+O(S^{-2})\), so the selected principal plane wave's first eigenvalue coefficient changes by \(-2u\cos k/5\). Thus the periodic transfer coefficient is \(\nu_1-2u\cos k/5\), where \(\nu_1\) is the coefficient in the preceding frozen-cell section. This exact auxiliary Floquet match resolves the local boundary-index ambiguity; it does not identify the correct global WKB transport convention for the varying operator. The product of varying edge transfers, connection data at the Bragg and central layers, phase control at time \(C/4\), and the actual weighted readout remain open.

## Verification and scope

The symbolic and finite-spin gauge and band checks are in scripts/postmark_electric_reversible_rate_transform_2026_09_26.py and .claude/science/postmark_interior_phase_20260926/REVERSIBLE_RATE_TRANSFORM_RESULTS.json.

The new symbolic gauge check in scripts/postmark_electric_reversible_rate_transform_2026_09_26.py derives the within-cell zero-mode coefficients \((0,0,-u/w,-u/w,-u/w)\) and verifies that the corrected links match the Hermitian five-site coefficients exactly.

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
