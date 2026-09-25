---
claim_id: postmark_electric_exact_side_fixed_index_kernel_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional exact reduction of the supplied finite-spin prepared-state readout to a fixed-index mod-3
  kernel, an energy-buffered electric-endpoint eigenfunction barrier, and a vanishing prepared-state mass bound
  for shrinking relative endpoint strips. The interior phase sum and fixed-time readout limit remain open.
upstream_dependencies:
- fast_vacancy_motion_after_formation_bounded_theorem_note_2026-09-24
- postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
- short_time_scaling_bounded_theorem_note_2026-09-24
- zero_mode_and_goegenbauer_limit_bounded_theorem_note_2026-09-24
runner: scripts/postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py
---

# Exact-side fixed-index kernel at fixed laboratory time

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** proposed_retained

## Result up front

In the supplied one-vacancy finite-spin path, staggering the exact Jacobi operator factors the generator into a strongly convergent prepared profile and a long-time unitary. At fixed laboratory time, the actual period-three readout differs from a single scalar quadratic form of the limiting profile by an explicit O(S^-2) bound at t=1/4. This removes the need to control every fixed-index kernel entry.

\[
K_S(a,b;t)=\langle a|e^{-it C N_S}V e^{it C N_S}|b\rangle,
\qquad C=S(S+1),\quad V|n\rangle=\omega^n|n\rangle,
\quad \omega=e^{2\pi i/3}.
\]

Entrywise decay of every fixed-index kernel entry is one sufficient route to the scalar limit, but it is stronger than necessary. The present work does not establish the scalar limit or the actual readout limit.

The exact coefficient table also yields an energy-buffered endpoint barrier. For each fixed \(0<\epsilon\le4\), a normalized eigenvector of \(N_S\) with eigenvalue \(\lambda\ge\epsilon\) has exponentially small mass in

\[
\mathcal C_{S,\epsilon}=\left\{n\in I_S:4\left(1-\left(\frac{n}{5S}\right)^2\right)\le\frac{\epsilon}{2}\right\}.
\]

This excludes endpoint leakage for that spectral range. It does not cover \(\lambda<\epsilon\), and by itself it does not control \(K_S\). The prepared-state combination with the low-energy spectral measure is proved below.

## Exact target and proof dependency graph

**Exact target.** Conditional on the supplied finite-spin one-vacancy path,
its integer-spin hop factors, and the first-mark preparation \(|0\rangle\),
prove the exact factorization and quantitative \(t=1/4\) scalar reduction,
the fixed-index spectral identities, and the prepared-state endpoint-strip
bound together with its transfer to the endpoint term of \(q_S(1/4)\); make
no claim about the remaining interior scalar limit.

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Supplied path, hop factors, initial state, and period-three output map | Open imported condition | Specified by the canonical fast-vacancy, zero-mode, and post-mark core notes at source revision `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`; not derived from the four axioms or asserted formally retained here. |
| Staggered Jacobi factorization, reflection, and exact finite spectral representation | Proved here conditional on the imported model | Direct finite-matrix identities from the supplied coefficient table. |
| Strong and quantitative prepared-profile convergence and the scalar reduction | Proved here conditional on the imported model | Weighted Jacobi coefficient estimate, Fourier moment bounds, Duhamel formula, and operator-norm estimate (10)–(12). |
| Fixed-profile truncation and translation-invariant reference kernel | Proved here | Fourier contour tail bound and exact Fourier/Bessel coefficient calculation; runner comparisons are corroborative. |
| Buffered endpoint eigenfunction barrier | Proved here | Weighted resolvent estimate with its fixed energy buffer in (8). |
| Low-energy spectral mass and prepared-state endpoint-strip estimate | Proved here | Strong convergence gives the arcsine spectral measure; its low-energy mass combines with (8) to prove (9). |
| Transfer of the endpoint-strip estimate to the endpoint term of \(q_S(1/4)\) | Proved here | The truncated limiting profile differs from \(\eta_S\) by \(o(1)\), the long unitary preserves that error, and \(V\) commutes with the spatial strip projector. |
| Limit of the interior phase sum or rigorously separated subsequences of the actual readout | Open; not asserted | Requires uniform global eigenphase/overlap control through both mod-three crossings and the central layer, or a certified actual-readout separation. |

The strongest missing lemma is a uniform bound for the interior off-diagonal
spectral phase sum at \(\theta=C/4\), including the two crossings and central
stationary layer. Independent final-source review and formal audit also remain
open; the source revision and conditional dependencies are identified above.

## Imports and supplied finite model

| Role | Imported input | Provenance at the frozen base | Open bridge |
|---|---|---|---|
| Finite-spin path and coefficients | One-vacancy path, integer-spin link factors, signed labels, and generator `G_S=M_S^2-CM_S` | Canonical [fast-vacancy note](FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md) and [zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md), both at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6` | The supplied dynamics and hop law are not derived from the four minimal axioms. |
| First-mark coordinate and output | The selected first-mark state is basis vector `n=0`; `O=1[n mod 3=0]=(I+V+V*)/3` with `V|n>=omega^n|n>` | [Post-mark core note](POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md) at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`; it records the frozen state and observable under the supplied six-site model | The output map is exact within the supplied path; its physical selection from the framework axioms remains open. |
| Qualitative fixed-time profile convergence | Strong convergence of the zero-extended `exp(-itN_S^2)|0>` profile | [Short-time scaling note](SHORT_TIME_SCALING_BOUNDED_THEOREM_NOTE_2026-09-24.md) at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`; the stronger quantitative bound is reproved below | It is not an additional open premise for (11), which is derived here from the coefficient estimates and Duhamel's formula. |

The imported results are conditional model statements, not ratified framework
inputs. The proof below derives the stated finite-matrix bounds from their exact
coefficient data and does not promote the supplied dynamics or preparation.

## Finite-spin definitions and exact factorization

Work conditional on the imported path and first-mark coordinate above.

Let \(I_S=[-5S,5S-4]\cap\mathbb Z\), \(M_S=-H_{2,S}=A_S^*A_S\), \(J|n\rangle=(-1)^n|n\rangle\), and \(N_S=JM_SJ\). The exact one-vacancy generator is \(G_S=M_S^2-CM_S\). Since \(J\) commutes with \(V\), fixes \(|0\rangle\), and \(G_{N,S}:=N_S^2-CN_S=JG_SJ\), the physical period-three expectation is unchanged if it is evaluated with \(G_{N,S}\).

Define

\[
\eta_S(t)=e^{-itN_S^2}|0\rangle,
\qquad
B_S(t)=e^{-it C N_S}V e^{it C N_S}.
\]

All factors are functions of the same finite self-adjoint matrix except for \(V\), so

\[
e^{-itG_{N,S}}|0\rangle=e^{it C N_S}\eta_S(t),
\qquad
\langle V\rangle_{S,t}=\langle\eta_S(t),B_S(t)\eta_S(t)\rangle.
\tag{1}
\]

By the fixed-time strong-convergence argument in the short-time source note, zero-extended \(\eta_S(t)\) converges strongly in \(\ell^2(\mathbb Z)\) to \(J e^{-itM_\infty^2}|0\rangle\), where \(M_\infty=2I+U+U^*\) in the source convention. Here \(N_\infty=JM_\infty J=2I-U-U^*\). Strong convergence follows directly from the source's uniform Jacobi norm bound and convergence on finitely supported vectors; conjugation by the fixed unitary \(J\) preserves it.

## Reduction to one fixed-profile scalar

The entrywise condition below is convenient but stronger than the physical
readout problem. Embed the finite interval \(I_S\) in \(\ell^2(\mathbb Z)\),
let \(P_S\) project onto it, and set

\[
\widetilde B_S(t)=P_S e^{-itCN_S}V e^{itCN_S}P_S,
\qquad
\eta_\infty(t)=e^{-itN_\infty^2}|0\rangle,
\quad N_\infty=2I-U-U^*.
\]

The zero-extended prepared profiles \(\widehat\eta_S(t)\) converge strongly
to \(\eta_\infty(t)\), and \(\|\widetilde B_S(t)\|\le1\). Define the single
scalar

\[
q_S(t)=\langle\eta_\infty(t),\widetilde B_S(t)\eta_\infty(t)\rangle.
\]

Then

\[
\left|\langle V\rangle_{S,t}-q_S(t)\right|
\le 2\|\widehat\eta_S(t)-\eta_\infty(t)\|\longrightarrow0,
\]

and hence

\[
\left|\langle O\rangle_{S,t}-\left(\frac13+
\frac23\operatorname{Re}q_S(t)\right)\right|
\le\frac43\|\widehat\eta_S(t)-\eta_\infty(t)\|\longrightarrow0.
\]

This is the single-scalar reduction supplied by the strong-profile theorem:
to establish the fixed-time readout limit it suffices, and is necessary up to
an \(o(1)\) error, to control only \(\operatorname{Re}q_S(t)\). There is no
need to prove weak-operator convergence of \(\widetilde B_S\) on every fixed
pair of sites. For \(R\) fixed and \(S\) large enough that
\([-R,R]\subset I_S\), the finite-core approximation is

\[
q_{S,R}(t)=\langle P_R\eta_\infty,
\widetilde B_S(t)P_R\eta_\infty\rangle
=\sum_{a,b=-R}^{R}\overline{\eta_\infty(a)}
K_S(a,b;t)\eta_\infty(b),
\]

with the uniform truncation estimate

\[
|q_S(t)-q_{S,R}(t)|
\le2\|\eta_\infty-P_R\eta_\infty\|.
\]

The translation-invariant profile has the exact Fourier coefficient formula

\[
\eta_\infty(n;t)=\frac1{2\pi}\int_{-\pi}^{\pi}
e^{-it(2-2\cos k)^2}e^{ink}\,dk.
\]

It also has an explicit truncation bound. For any \(y>0\), shifting the
Fourier contour to \(k+i y\) for \(n>0\), and to \(k-i y\) for \(n<0\),
gives

\[
|\eta_\infty(n;t)|\le
\exp\!\left(|t|(2+2\cosh y)^2-|n|y\right).
\]

Consequently, for \(R\ge0\),

\[
\|\eta_\infty-P_R\eta_\infty\|
\le\left[\frac{2\exp\!\left(2|t|(2+2\cosh y)^2-2y(R+1)\right)}
{1-e^{-2y}}\right]^{1/2}.
\]

At \(t=1/4\), \(y=3/2\), and \(R=24\), this bound is less than
\(6\times10^{-12}\). Thus the target scalar is uniformly reduced, up to a
known tiny profile-tail error, to the quadratic form on 49 profile coefficients (49 by 49 kernel entries) on
\([-24,24]\). This controls the profile truncation only; the spin-dependent
long-time kernel remains the central open obligation.

Thus a proof may target one fixed weighted sum of finitely many kernel entries
and then send \(R\to\infty\). The entrywise decay condition in the next
section remains a simple sufficient route to \(q_S\to0\), but it is not the
weakest obligation and should not be treated as the wall itself.

## Quantitative convergence of the prepared profile

The strong convergence used above has a direct \(O(S^{-2})\) bound at the
frozen time \(t=1/4\). Let \(\overline N_S\) denote the zero extension of
\(N_S\) to \(\ell^2(\mathbb Z)\), and put

\[
D_S=\overline N_S-N_\infty,\qquad w_n=1+n^2.
\]

For every diagonal or nearest-neighbor coefficient, the signed-label table
gives \(|m-n/5|\le6/5\) for factors incident to node \(n\), hence
\(|m|\le|n|+2\) and

\[
0\le m(m+1)\le(|n|+2)(|n|+3)\le6w_n.
\]

Since \(C\ge S^2\), each incident factor satisfies
\(0\le1-g_m\le6w_n/S^2\). The diagonal has two such terms. For an interior
link, \(g_a,g_b\in[0,1]\) and

\[
0\le1-\sqrt{g_ag_b}\le(1-g_a)+(1-g_b),
\]

so its difference from the constant link \(-1\) is at most
\(12w_n/S^2\). The zero extension's missing boundary links and exterior
diagonal also obey that bound, since those nodes satisfy \(|n|\ge5S-4\).
Thus, for all \(n\in\mathbb Z\),

\[
|(D_S)_{n,n}|,\ |(D_S)_{n,n+1}|
\le\frac{12w_n}{S^2}.
\]

Using \(w_{n-1}\le3w_n\) and the tridiagonal form gives the weighted estimate

\[
\|D_S f\|_2\le\frac{60}{S^2}
\left(\sum_n w_n^2|f_n|^2\right)^{1/2}.
\tag{10}
\]

For \(f_s=e^{-isN_\infty^2}|0\rangle\), Fourier transform identifies its
symbol as \(F_s(k)=e^{-isE(k)^2}\), with \(E(k)=2-2\cos k\). Parseval and
\(\|F_s'\|_\infty\le16s\),
\(\|F_s''\|_\infty\le24s+256s^2\) yield

\[
\|w f_s\|_2\le
\sqrt{1+2(16s)^2+(24s+256s^2)^2}\le\sqrt{517}
\quad(0\le s\le1/4).
\]

For \(N_\infty f_s\), the Fourier symbol is \(E F_s\); its zeroth, first,
and second derivative norms are bounded respectively by \(4\),
\(2+64s\), and \(2+160s+1024s^2\). Therefore

\[
\|w N_\infty f_s\|_2\le
\sqrt{16+2(2+64s)^2+(2+160s+1024s^2)^2}
\le\sqrt{11900}.
\]

Now \(\overline N_S^2-N_\infty^2=
\overline N_S D_S+D_SN_\infty\), and the row-sum bound above gives
\(\|\overline N_S\|\le4+24/S\le28\). Duhamel's formula for these bounded
self-adjoint operators gives the explicit estimate

\[
\|\widehat\eta_S(1/4)-\eta_\infty(1/4)\|_2
\le\frac{15(28\sqrt{517}+\sqrt{11900})}{S^2}
<\frac{1.12\times10^4}{S^2}.
\tag{11}
\]

Combining (11) with the one-vector reduction proves

\[
\left|\langle O\rangle_{S,1/4}-
\left(\frac13+\frac23\operatorname{Re}q_S(1/4)\right)\right|
<\frac{1.50\times10^4}{S^2}.
\tag{12}
\]

This closes the prepared-profile approximation with a quantitative rate. The
constant is deliberately coarse. Equation (12) does not control the remaining
scalar \(q_S(1/4)\), whose conjugated evolution still runs for time
\(C/4\asymp S^2\).

## Stronger entrywise sufficient criterion

For fixed integers \(a,b\), once they lie in \(I_S\), set

\[
K_S(a,b;t)=\langle a|B_S(t)|b\rangle.
\]

Assume, at one fixed time \(t\),

\[
K_S(a,b;t)\longrightarrow0
\quad\text{for every fixed }a,b\in\mathbb Z.
\tag{2}
\]

Then \(\langle V\rangle_{S,t}\to0\), and for \(O=(I+V+V^*)/3\),

\[
\langle O\rangle_{S,t}=\frac13+\frac23\operatorname{Re}\langle V\rangle_{S,t}
\longrightarrow\frac13.
\tag{3}
\]

To prove this, first take a fixed finitely supported vector \(\psi\). Its quadratic form \(\langle\psi,B_S\psi\rangle\) is a finite sum of entries in (2), and hence tends to zero. The operators \(B_S\) have norm one. Strong convergence \(\eta_S\to\eta_\infty\) lets us approximate \(\eta_S\), uniformly for all sufficiently large \(S\), by one such \(\psi\):

\[
\left|\langle\eta_S,B_S\eta_S\rangle-
\langle\psi,B_S\psi\rangle\right|
\le(\|\eta_S\|+\|\psi\|)\,\|\eta_S-\psi\|.
\]

Take \(S\to\infty\), then make \(\|\eta_\infty-\psi\|\) arbitrarily small. Equation (1) gives the claim. No uniform estimate on the fast state itself is needed beyond the sourced strong convergence of \(\eta_S\).

Failure of (2), including one nonzero or nonconvergent fixed entry, only defeats this sufficient route. It does not by itself falsify (3). A wall for the physical readout requires a rigorously separated subsequence of the actual prepared-state expectations.

## Exact finite spectral identities

Let \(\{\phi_j\}\) be a real orthonormal eigenbasis of the Jacobi matrix \(N_S\), with eigenvalues \(\lambda_j\). Direct insertion of the spectral resolution gives

\[
K_S(a,b;t)=\sum_{j,k}
 e^{-itC\lambda_j}e^{itC\lambda_k}
 \phi_j(a)\phi_k(b)
 \sum_{n\in I_S}\omega^n\phi_j(n)\phi_k(n).
\tag{4}
\]

For the finite-core approximation to the physical scalar, define
\(c_j=\langle\phi_j,P_R\eta_\infty(1/4)\rangle\) and
\(v_{jk}=\langle\phi_j,V\phi_k\rangle\). Its exact spectral decomposition is

\[
q_{S,R}(1/4)=\sum_{j,k}\overline{c_j}c_kv_{jk}
 e^{iC(\lambda_k-\lambda_j)/4}
=d_{S,R}+r_{S,R},
\tag{13}
\]

where
\[
d_{S,R}=\sum_j|c_j|^2v_{jj},\qquad
r_{S,R}=\sum_{j\ne k}\overline{c_j}c_kv_{jk}
 e^{iC(\lambda_k-\lambda_j)/4}.
\tag{14}
\]

Every internal link is nonzero: its effective labels lie in [-S,S-1], so
R_m=(S-m)(S+m+1)>0. The eigenvector recurrence for an irreducible
real Jacobi matrix determines all entries from the first one; a zero first
entry forces the whole vector to vanish. Hence each eigenspace has
dimension one, and real symmetry implies simple spectrum.

The first term is the exactly zero-frequency part in this finite spectral
representation; the second contains all distinct-eigenvalue interference.
The runner reports both for the radius-24 profile truncation. At \(S=512\),
the computed diagonal term has magnitude \(2.17\times10^{-4}\), while the
off-diagonal term has magnitude \(1.27\times10^{-2}\). The analytic profile
tail bound already stated controls the difference between this finite-core
quadratic form and \(q_S\); these sampled diagonal values do not prove a
uniform decay estimate. The unresolved task remains a bound on the
off-diagonal near-resonant phases, including the two mod-three band crossings
and their central layer.

A commutator identity alone does not give a pointwise large-time bound. For a
bounded operator \(X\) and vector \(\psi\) with \(\|\psi\|\le1\), set
\[
F_X(\theta)=\langle\psi,e^{-i\theta N_S}Xe^{i\theta N_S}\psi\rangle.
\]
Direct differentiation gives
\[
\langle\psi,e^{-i\theta N_S}[N_S,X]e^{i\theta N_S}\psi\rangle
=iF_X'(\theta).
\]
It follows that the time average of the commutator term over \([0,T]\) is
bounded in magnitude by \(2\|X\|/T\). At one selected \(\theta\), the
identity only rewrites the value as a derivative; decay still requires a
pointwise phase-sum or propagation estimate. Thus a commutator solution can
organize the resonant pairs but is not, by itself, the missing fixed-time
proof.

There is also an exact echo form. Since \(V|b\rangle=\omega^b|b\rangle\) and \(Ve^{itCN_S}V^*=e^{itC VN_SV^*}\),

\[
K_S(a,b;t)=\omega^b\langle a|
e^{-itCN_S}e^{itC VN_SV^*}|b\rangle.
\tag{5}
\]

The same signed-label table gives an exact reflection symmetry of the full
finite path. Define \(R_S|n\rangle=|-4-n\rangle\); this maps
\(I_S=[-5S,5S-4]\) to itself. For edge \(n\to n+1\), the reflected edge is
\(-5-n\to-4-n\). Its two factors have the same Casimir values, possibly
interchanged, because the table and \(m(m+1)=(-m-1)(-m)\) give

\[
\{m_L(n)(m_L(n)+1),m_R(n)(m_R(n)+1)\}
=\{m_L(-5-n)(m_L(-5-n)+1),
m_R(-5-n)(m_R(-5-n)+1)\}.
\]

The two factors on each diagonal row are reflected into one another. Thus
\(R_SN_SR_S=N_S\). Also

\[
R_SVR_S=\omega^{-1}V^*,\qquad
R_SB_S(t)R_S=\omega^{-1}B_S(t)^*,
\]

and the kernel obeys

\[
K_S(-4-a,-4-b;t)
=\omega^{-1}\overline{K_S(b,a;t)}.
\]

This halves redundant kernel checks and gives a parity decomposition for the
Jacobi eigenvectors. It does not by itself determine the prepared-profile
quadratic form, since the limiting profile centered at \(0\) is not invariant
under reflection about \(-2\).

These are exact finite-spin identities, not asymptotic formulas. They expose the load-bearing task: control a double spectral sum with phases of size \(C\asymp S^2\) while the path has length \(O(S)\). A low fixed-index spectral truncation cannot control it.

## Translation-invariant reference kernel

The strong local limit is \(N_\infty=2I-U-U^*\), with \(U|n\rangle=|n+1\rangle\). It gives a useful exact comparison problem, but not a uniform approximation at the target time. Use the Fourier convention \(\widehat\psi(k)=\sum_n\psi_n e^{-ink}\), \(\phi=2\pi/3\), and \(E(k)=2-2\cos k\). Then \(\widehat{V\psi}(k)=\widehat\psi(k-\phi)\), so

\[
\widehat{B_\infty(\theta)\psi}(k)
=e^{i\theta[E(k-\phi)-E(k)]}\widehat\psi(k-\phi),
\quad
E(k-\phi)-E(k)=2\sqrt3\cos(k+\pi/6).
\]

The Jacobi kernel is therefore

\[
K_\infty(a,b;\theta)
=e^{ib\phi}i^{a-b}e^{-i(a-b)\pi/6}
J_{a-b}(2\sqrt3\,\theta).
\tag{15}
\]

For fixed \(a-b\), stationary phase at the two nondegenerate critical points gives \(K_\infty=O(\theta^{-1/2})\). Substituting \(\theta=tC\), with fixed nonzero \(t\), gives \(O(S^{-1})\) for this translation-invariant reference. The runner compares (15) with independent uniform Fourier quadrature at fixed modes and several \(\theta\) values.

This does not prove the finite-spin result. Strong convergence \(N_S\to N_\infty\) controls fixed propagation times, whereas \(\theta=tC\) grows like \(S^2\). The finite-spin coefficients vary over a path of length \(O(S)\), the central scaled correction \(C(N_S-N_\infty)\) has a nonzero operator limit on the finite-support core, and resonant bands accumulate order-\(S\) phases. No uniform Duhamel or scattering estimate currently compares (15) with \(K_S\) in this regime.

## Buffered endpoint barrier

For an edge \(n\to n+1\), the supplied coefficients use factors

\[
g_m=1-\frac{m(m+1)}{C}.
\]

The negative-residue labels obey \(m^-=-m^+-1\); the exact identity \(m(m+1)=(-m-1)(-m)\) lets every edge factor be represented by the signed labels \(\widehat m=3\lfloor n/15\rfloor+L_r^+\) or \(3\lfloor n/15\rfloor+R_r^+\), where \(n=15k+r\). The tables give \(|\widehat m-n/5|<1\) for either factor on edge \(n\to n+1\). A factor from the preceding edge differs from \(n/5\) by at most \(6/5<2\). These bounds include a missing-edge ghost factor at an endpoint. Therefore, for \(x_n=n/(5S)\), write \(m=Sx_n+q\), \(|q|\le2\). Then

\[
\left|\frac{m(m+1)}{S(S+1)}-x_n^2\right|
=\left|\frac{S(2x_nq+x_n(1-x_n))+q(q+1)}{S(S+1)}\right|
\le\frac{6}{S}
\tag{6}
\]

uniformly, with the same estimate for either edge incident to \(n\). The diagonal of \(N_S\) is the sum of two such factors. Each neighboring absolute link is a square root \(\sqrt{g_ag_b}\), bounded above by \((g_a+g_b)/2\). Hence the full absolute row sum obeys

\[
\sum_j |(N_S)_{nj}|
\le4(1-x_n^2)+24/S
\tag{7}
\]

uniformly through the endpoints: each of the four nonnegative contributions is at most \(1-x_n^2+6/S\). In particular \(0\le N_S\) and its spectrum is at most \(4+24/S\).

Fix \(0<\epsilon\le4\), and enlarge the endpoint cap to

\[
\mathcal D_{S,\epsilon}=\left\{n:4(1-x_n^2)\le\frac{3\epsilon}{4}\right\}.
\]

The compression \(H_D=\mathbf1_DN_S\mathbf1_D\) is positive and, by (7),

\[
\|H_D\|\le3\epsilon/4+24/S.
\]

For all sufficiently large \(S\), every \(\lambda\ge\epsilon\) is at distance at least \(\delta=\epsilon/8\) from the spectrum of \(H_D\). The smaller cap \(\mathcal C_{S,\epsilon}\) is separated from \(\mathcal D_{S,\epsilon}^{\,c}\) by at least

\[
L_\epsilon S-O(1),\qquad
L_\epsilon=5\left[\sqrt{1-\epsilon/8}-\sqrt{1-3\epsilon/16}\right]>0.
\]

For an eigenvector \(N_S\phi=\lambda\phi\), restricting its equation to \(D\) gives

\[
(\lambda-H_D)\phi_D=B\phi_{D^c},
\]

where \(B\) is supported on the two inner boundary links and has norm at most one per link. A weighted conjugation by \(e^{\gamma n}\) for a finite Jacobi matrix with links of magnitude at most one changes \(H_D\) in operator norm by at most \(2(e^\gamma-1)\). Choose \(\gamma_\epsilon>0\) with this perturbation at most \(\delta/2\). The resolvent identity and \(\operatorname{dist}(\lambda,\sigma(H_D))\ge\delta\) then give

\[
|[(\lambda-H_D)^{-1}]_{ij}|
\le\frac{2}{\delta}e^{-\gamma_\epsilon|i-j|}.
\]

Summing the geometric tail from each boundary source yields constants \(A_\epsilon,c_\epsilon>0\), independent of \(S\), \(\lambda\), and the normalized eigenvector, such that

\[
\|\mathbf1_{\mathcal C_{S,\epsilon}}\phi\|
\le A_\epsilon e^{-c_\epsilon S}.
\tag{8}
\]

The estimate is for a fixed buffered cap. The unbuffered local turning set \(4(1-x^2)<\lambda\) is larger and is not covered; high-energy eigenvectors can retain mass near their own turning points. The low-energy sector \(\lambda<\epsilon\) is also not covered. No conclusion about the exact kernel follows from (8) without an additional spectral and phase argument.

## Prepared-state electric-endpoint tail

The fixed buffered cap in (8) also yields a bound for the actual prepared
state once its low-energy spectral weight is included. Let
\(\Psi_S(\theta,t)=e^{i\theta N_S}\eta_S(t)\), where
\(\eta_S(t)=e^{-itN_S^2}|0\rangle\), and for \(0<\delta\le1/4\) define
\[
E_{S,\delta}=\left\{n\in I_S:1-\frac{|n|}{5S}\le\delta\right\}.
\]
Then, for every fixed \(t\),
\[
\limsup_{S\to\infty}\sup_{\theta\in\mathbb R}
\left\|\mathbf1_{E_{S,\delta}}\Psi_S(\theta,t)\right\|_2^2
\le \frac1\pi\arccos(1-8\delta).
\tag{9}
\]
The right side is \(4\sqrt{\delta}/\pi+O(\delta^{3/2})\) as
\(\delta\downarrow0\). Since the period-three character \(V\) is diagonal in
the path basis, its contribution from this endpoint strip is bounded by the
same mass. Thus the endpoints can be removed from the actual prepared-state
readout with an error that vanishes as the relative strip shrinks, uniformly
in the long phase \(\theta\).

To prove (9), zero-extend \(N_S\) to \(\ell^2(\mathbb Z)\). The coefficient
formula and uniform row-sum bound above give \(\overline N_S\to N_\infty\)
strongly with uniformly bounded norms. Hence the spectral measures of
\(|0\rangle\) converge weakly to that of \(N_\infty=2I-U-U^*\). Fourier
transform identifies the limit as the arcsine law
\[
d\mu_0(\lambda)=\frac{\mathbf1_{(0,4)}(\lambda)}
{\pi\sqrt{\lambda(4-\lambda)}}\,d\lambda.
\]
The phase \(e^{-itN_S^2}\) does not change spectral weights, so for every
fixed \(0<\epsilon\le4\),
\[
\lim_{S\to\infty}
\left\|\mathbf1_{[0,\epsilon)}(N_S)\eta_S(t)\right\|_2^2
=\mu_0([0,\epsilon])
=\frac1\pi\arccos(1-\epsilon/2).
\tag{16}
\]
The interval endpoints carry no limiting spectral mass. On the complementary
spectral subspace \(\lambda\ge\epsilon\), (8) bounds each normalized
eigenvector's norm in \(\mathcal C_{S,\epsilon}\) by
\(A_\epsilon e^{-c_\epsilon S}\). There are \(10S-3\) path sites, so
Cauchy--Schwarz gives the phase-uniform high-energy estimate
\[
\left\|\mathbf1_{\mathcal C_{S,\epsilon}}
e^{i\theta N_S}\mathbf1_{[\epsilon,\infty)}(N_S)\eta_S(t)\right\|_2
\le A_\epsilon\sqrt{10S-3}\,e^{-c_\epsilon S}.
\]
For \(n\in E_{S,\delta}\), \(4(1-x_n^2)\le8\delta\). Set
\(\epsilon=16\delta\), so \(E_{S,\delta}\subseteq\mathcal C_{S,\epsilon}\).
The low-energy component has unchanged norm under \(e^{i\theta N_S}\),
while the high-energy endpoint mass tends to zero by the preceding display.
Taking \(S\to\infty\) proves (9). This result controls spatial endpoint mass
for the prepared state. It also controls the endpoint term in the reduced
scalar \(q_S(1/4)\), despite that scalar using the limiting profile. To see
this, write \(\xi_S=P_S\eta_\infty(1/4)\), where \(P_S\) projects onto
\(I_S\). Strong convergence of the interval projections and (11) give
\(\|\xi_S-\eta_S(1/4)\|_2\to0\). Applying the same unitary
\(e^{iCN_S/4}\) preserves this difference, uniformly in its phase. Thus
\(e^{iCN_S/4}\xi_S\) differs in norm by \(o(1)\) from the actual prepared
state \(\Psi_S(C/4,1/4)\). Since \(V\) commutes with the spatial strip
projector, the endpoint and interior pieces of
\(q_S(1/4)=\langle e^{iCN_S/4}\xi_S,V e^{iCN_S/4}\xi_S\rangle\)
split without cross terms; the endpoint piece is bounded in magnitude by
the strip mass. Equation (9), followed by \(\delta\downarrow0\), therefore
removes the endpoint contribution to \(q_S\) as well. The remaining interior
spectral phase interference is open.

## Verification and limitations

The companion runner reconstructs the exact finite-spin Jacobi entries, compares both the physical positive links and their staggered signs with direct charge/electric two-hop enumeration for \(S=1,2,3,5,8\), checks the signed-label reflection and weighted coefficient majorant on selected finite spins, checks the finite generator and echo identities against independent dense matrix exponentials, checks the homogeneous Bessel-kernel formula against independent Fourier quadrature, independently cross-checks the limiting-profile Fourier coefficients by an operator-power series, and evaluates the finite spectral representation by tridiagonal eigensolves in float64 at \(t=1/4\), up to \(S=512\). The new endpoint diagnostic reports the low-energy spectral weight, its arcsine prediction, and the actual state mass in the buffered cap. These scans are not interval-enclosed and prove neither convergence nor nonconvergence; they corroborate but do not replace the displayed analytic arguments.

The prepared-state endpoint contribution is now controlled by (9) after sending the relative endpoint width to zero. The remaining direct obligation is to prove \(\operatorname{Re}q_S(1/4)\to0\), prove a different fixed-time limit for this scalar, or find rigorously separated subsequences of the actual readout. Entrywise convergence (2) remains a stronger route but is not required. The current best analysis route is a spectral-phase treatment of the selected profile quadratic form in the interior, with the two resonant band pairs and the central stationary layer. Literature on smooth recurrences and fixed-operator spectral asymptotics does not supply this finite, crossing-coupled, \(O(S^2)\)-time estimate under the assumptions here. No supplied-model discrepancy has been established, and no framework axiom or primitive is updated.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_exact_side_fixed_index_kernel_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "conditional on the supplied one-vacancy path, integer-spin link representation, generator, and first-mark preparation"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The exact reduction and buffered eigenvector barrier are conditional finite-model mathematics. The fixed-time kernel and physical readout limits remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Control the interior fixed-profile scalar Re(q_S(1/4)) or obtain a rigorously separated actual-readout subsequence; entrywise kernel decay is sufficient but stronger than necessary. The prepared-state electric-endpoint tail is controlled in the double limit by the arcsine low-energy mass and buffered eigenfunction barrier."
```

The canonical upstream notes above are present, byte-for-byte, at current `origin/main` revision `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`. Their supplied-model scope remains conditional; this checkpoint makes no axiom-level claim and applies no audit verdict.


## Review scope and recovery

The complete conditional proofs above remain the scientific source. Historical
revision/hash statements and dated numerical values describe the author snapshot;
current execution is bound to the source and actual current inputs in the paired
runner cache. No historical seal or audit output grants authority.
The original PR branches preserve the full campaign packet, failed attempts,
Schur/pole probes, weighted lag decompositions and large-spin diagnostics.
Their broader fixed-time cancellation target remains open. No finite sample or
principal counting law supplies the missing phase-accurate weighted estimate.

- **N1 — Domain:** supplied integer-spin one-vacancy matrix, preparation and stated limit order.
- **N2 — Alternatives:** other preparations, laws and cancellation methods remain possible.
- **N3 — Imports:** model, Hilbert kinematics and readout are supplied, not native premises.
- **N4 — Dependencies:** linked current sources govern; no retained grade is inherited.
- **N5 — Resolution:** finite floating diagnostics corroborate algebra, not asymptotic certification.
- **N6 — Residual:** the interior two-energy phase sum remains unresolved.
- **N7 — Counterroute:** failure of a sufficient kernel or termwise approximation would not alone refute readout convergence.
- **N8 — Authority:** source review only; no audit verdict or framework admission.


## Recovered finite Schur identity and phase-accuracy condition

The campaign's Schur probe supplies a useful representation independent of any
cancellation claim. Split a finite real symmetric H into anchor/interior blocks
A,B,D, with H=[[A,B],[B^T,D]]. For real z,w outside spec(D), put
R_z=(zI-D)^(-1), T_z=[I;R_z B^T] and S(z)=A-zI+B R_z B^T.
For the block-diagonal character V=diag(V_A,V_I), direct multiplication gives

    T_z^* V T_w = V_A + B R_z V_I R_w B^T = Q_V(z,w).

At an eigenvalue z away from the poles, an eigenvector is T_z x where
S(z)x=0; this follows from its interior row equation. For V=I,
the resolvent identity gives

    Q_I(z,w) = -(S(z)-S(w))/(z-w),
    Q_I(z,z) = I+B R_z^2 B^T = -S'(z) > 0.

Thus T_z Q_I(z,z)^(-1/2) is an isometry and the correspondingly normalized
two-energy Q_V has norm at most one when ||V||<=1. These identities hold
away from eliminated-block poles; they supply no uniform inverse or pole-mass
estimate. The original four-site continuant and large-spin pole scans remain
historical exploratory inputs on the recovery branch.

For the actual generator at t=1/4, Phi_C(lambda)=(C lambda-lambda^2)/4.
Exactly,

    Phi_C(lambda)-Phi_C(mu)=(lambda-mu)(C-lambda-mu)/4.

Since the bounded eigenvalues have C asymptotic to S^2, an O(S^-2)
eigenvalue approximation guarantees only O(1) phase error. Uniform termwise
o(1) phase replacement requires o(S^-2), unless a separate argument tolerates
order-one phase errors. This does not exclude an averaged cancellation proof.
