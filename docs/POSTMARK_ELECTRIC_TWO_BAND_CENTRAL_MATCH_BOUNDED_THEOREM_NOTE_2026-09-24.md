---
claim_id: postmark_electric_two_band_central_match_2026_09_24
claim_type: bounded_theorem
claim_scope: Conditional on the supplied six-site integer-spin one-vacancy hop map, the two mod-3-coupled folded
  crossings have the stated frozen-cell 2x2 normal forms on compact bulk intervals, and S^2(N_S-N_infinity) converges
  on finitely supported vectors to the explicit polynomial Jacobi operator Q. The resulting order-one generator
  correction is only a core limit; it does not establish a global spectral or fixed-time propagation result.
upstream_dependencies:
- fast_vacancy_motion_after_formation_bounded_theorem_note_2026-09-24
- postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
- postmark_electric_moving_index_cell_symbol_2026_09_24
- zero_mode_and_goegenbauer_limit_bounded_theorem_note_2026-09-24
runner: scripts/postmark_electric_two_band_central_match_2026_09_24.py
---

# Two-band normal forms and the central coefficient match

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** proposed_retained

## Result up front

For the supplied finite-spin Jacobi matrix, the folded bands that the mod-3 vacancy character couples have isolated two-dimensional crossings at reduced-zone boundaries θ=0 and θ=π. On any compact bulk interval ε≤|u|≤1-ε, projection onto each crossing pair gives a linear detuning term and the first-order couplings listed below. The local gap therefore has the usual square-root two-level shape to the order controlled by the frozen 15-cell expansion.

At the central scale, the finite-support operator expansion is different in an important way. With $N_S=J M_SJ$, $N_\infty=2I-T-T^*$ on $\ell^2(\mathbb Z)$, and $C=S(S+1)$, there is an explicit symmetric Jacobi operator $Q$ on $c_{00}(\mathbb Z)$ such that

\[
 S^2(N_S-N_\infty)f\longrightarrow Qf,
 \qquad
 (G_S+C N_\infty)f\longrightarrow (N_\infty^2-Q)f,
 \quad f\in c_{00}(\mathbb Z),
\]

where $G_S=N_S^2-CN_S$. This is coefficientwise/core convergence only: $Q$ has quadratic coefficients and is unbounded. This convergence alone supplies no bounded-perturbation estimate for fixed laboratory times.

The crossing projection of $Q$ also exposes the matching scale. Its coupling grows linearly with the cell index, reproducing the outer $1/S$ coupling in the overlap, and has a nonzero constant central offset. Since $C/S^2\to1$, that remainder contributes an order-one phase to the frozen two-band model. This is a central coefficient result and does not establish a global avoided-crossing law, scattering law, or readout limit.

## Exact target and proof dependency graph

**Exact target.** Conditional on the supplied six-site integer-spin hop map, derive the local two-band normal forms on compact bulk intervals and prove the finite-support coefficient limit \(S^2(N_S-N_\infty)f\to Qf\), including the actual \(n=-1/0\) interface, for every \(f\in c_{00}(\mathbb Z)\).

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Exact signed hop labels and finite-spin Jacobi factors | Imported condition | Supplied-model and zero-mode notes cited below; not derived from the framework axioms. |
| Bulk crossing detuning and first-order coupling | Proved here conditionally | Finite 15-cell Fourier compression with the compact-interval remainder inherited from the local-symbol expansion. |
| Central coefficient operator \(Q\) and core convergence | Proved here | Exact fixed-index label formulas, square-root expansion, and the generator identity on \(c_{00}\). |
| Frozen-cell projections and central/outer coefficient match | Proved here | Exact finite Fourier sums and polynomial identities; the physical-state runner is a finite-window cross-check. |
| Global spectrum, propagator, tails, and actual output | Open | The local cells and core limit do not supply global transport or statewise bounds. |

The compact-bulk statement excludes \(u=0\) and the electric endpoints; the central statement is coefficientwise on finite-support vectors and includes the exact label join. Neither statement covers vectors whose support grows with \(S\), global spectral gaps, or fixed-time propagation. For the exact-side readout, the next sufficient lemma is pointwise convergence of the fixed-index kernel \(K_S(a,b;t)=\langle a|e^{-itCN_S}Ve^{itCN_S}|b\rangle\) at a frozen time. Together with the sourced strong limit of \(e^{-itN_S^2}|0\rangle\), it controls the actual first-mark state without a separate fast-state tail theorem. The full exact-versus-candidate comparison still needs a selected candidate extension and its output control.

## Imported inputs

| Role | Imported input | Provenance at the frozen base | Open bridge |
|---|---|---|---|
| Supplied physical model and first-mark output | One-vacancy path, integer-spin link factors, signed labels, and frozen first-mark output | Canonical [fast-vacancy note](FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md), [zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md), and conditional [post-mark core note](POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md), all at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6` | These supplied dynamics and preparation are not derived from the four minimal axioms; the axiom-to-model bridge remains open. |
| Independent finite-spin check | Enumeration of supplied charge/electric states and legal two-hop paths | `scripts/core_derivation.py` at the frozen base; it checks finite spins and a finite coordinate window | It does not establish the all-index limit, global propagation, or physical model selection. |
| Mathematical tools | Finite-dimensional degenerate perturbation and Taylor expansion of the square root | Standard finite-dimensional algebra applied with the displayed compact-bulk or finite-support hypotheses | No separate physical import; the required isolation and support hypotheses are checked in the proof. |

## One signed coefficient family across the central join

Write \(f(m)=m(m+1)\). The supplied residue arrays obey \(L_r^-=-L_r^+-1\) and \(R_r^-=-R_r^+-1\) for every \(r=0,\ldots,14\), and \(f(-m-1)=f(m)\). For \(n=15k+r<0\), the negative labels therefore satisfy

\[
f(3|k|+L_r^-)=f(3k+L_r^+),\qquad
f(3|k|+R_r^-)=f(3k+R_r^+).
\]

For \(k\ge0\), these identities hold by the positive label definition. Thus the exact finite-spin Jacobi coefficients throughout the path use one signed-cell polynomial family. With

\[
g_S(k,a)=1-\frac{f(3k+a)}{C},\quad k=\lfloor n/15\rfloor,\quad r=n\bmod15,
\]

the entries are

\[
(N_S)_{nn}=g_S(k,L_r^+)+g_S(k-\mathbf1_{r=0},R_{(r-1)\bmod15}^+),\qquad
(N_S)_{n,n+1}=-\sqrt{g_S(k,L_r^+)g_S(k,R_r^+)}.
\]

The second formula applies to edges in \(I_S\), with the physical forbidden edge factor equal to zero at an endpoint. In particular, the actual labels \((-1,0)\) on edge \(-1\to0\) and the positive-family labels \((0,-1)\) give the same Casimir factors. This is an exact coefficient identity; it removes a sign-induced coefficient defect at the origin. The central \(O(S^{-1})\)-index scaling is still needed to collect order-one phase terms at the stationary point, and this identity supplies no global propagation estimate.

## Conditional model and outer two-band normal form

The calculation is conditional on the exact hop factors (R_m=C-m(m+1)) in the canonical source note [FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md](FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md), present at main `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6` (SHA-256 `d235b264783de82bd563d17c217c0b3bc22718638223106215ae43edfd7dbb23`). The finite-support correction is also stated in [POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md](POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md), SHA-256 `6b791a007320753af0ac5f2d3a11ea713598360ab757185b3bc3c1c2c77d808e`. Historical proposal PR #8831 is closed without merge; its conditional model argument is represented in that main note. The preceding local-symbol note [POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md](POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md) gives

\[
\mathcal N_S^\pm(u,\theta)= (1-u^2)\mathcal N_0(\theta)
  +S^{-1}\mathcal N_1^\pm(u,\theta)+O_\varepsilon(S^{-2}),
\quad \nu_\ell=2(1-u^2)(1-\cos q_\ell),
\quad q_\ell=(\theta+2\pi\ell)/15.
\]

Here $u=|x|$, the sign distinguishes the positive and negative flux halves, and $\varepsilon\le|u|\le1-\varepsilon$. The two crossing pairs are $(\ell,\ell')=(5,10)$ at $\theta_*=0$ and $(12,2)$ at $\theta_*=\pi$. Put $w=1-u^2$, $\delta=\theta-\theta_*$, $a=\sqrt3 w/15$, and $\sigma_*=+1$ at $\theta_*=0$ and $-1$ at $\theta_*=\pi$. In the same Bloch basis convention as the preceding note, the projected matrix is

\[
 \nu_* I+\sigma_*\delta\begin{pmatrix}a&0\\0&-a\end{pmatrix}
 +S^{-1}\left(s_\pm(u)I+
 \begin{pmatrix}0&c_\pm(u)\\\overline{c_\pm(u)}&0\end{pmatrix}\right)
 +O_\varepsilon\big((|\delta|+S^{-1})^2\big),
\]

The scalar center and coupling are:

| side | boundary | bands | $\nu_*$ | first-band detuning slope | $s_\pm(u)$ | $c_\pm(u)$ |
|---|---:|---:|---:|---:|---:|---:|
| positive | $\theta=0$ | 5/10 | $3w$ | $+a$ | $u(3u-11)$ | $2u(1+i\sqrt3)/5$ |
| negative | $\theta=0$ | 5/10 | $3w$ | $+a$ | $u(3u+11)$ | $2u(-1-i\sqrt3)/5$ |
| positive | $\theta=\pi$ | 12/2 | $w$ | $-a$ | $u(5u-17)/5$ | $2u(3-i\sqrt3)/15$ |
| negative | $\theta=\pi$ | 12/2 | $w$ | $-a$ | $u(5u+17)/5$ | $-2u(3-i\sqrt3)/15$ |

In a fixed basis of the two degenerate Bloch vectors, the compressed derivative of $\mathcal N_0/w$ is exactly $\operatorname{diag}(\sqrt3/15,-\sqrt3/15)$ at $\theta=0$ and its negative at $\theta=\pi$. Thus the detuning term above is a degenerate perturbation calculation, not only a difference of band eigenvalue slopes.

For $|\delta|=O(S^{-1})$, the corresponding local gap is

\[
 \sqrt{4a^2\delta^2+4S^{-2}|c_\pm(u)|^2}
 +O_\varepsilon(S^{-2}).
\]

At $\delta=0$ this recovers $8u/(5S)+O_\varepsilon(S^{-2})$ at $\theta=0$ and $8\sqrt3u/(15S)+O_\varepsilon(S^{-2})$ at $\theta=\pi$. The 15-by-15 complementary bands remain uniformly separated on the stated compact bulk set, which justifies the local two-dimensional projection. Nothing here supplies an eigenvalue gap for the nonperiodic finite-spin operator.

## Exact central operator on the finite-support core

For each edge $n\to n+1$, use the supplied signed labels

\[
(m_L(n),m_R(n))=\begin{cases}
(3k+L_r^+,3k+R_r^+),&n=15k+r\ge0,\\
(3K+L_r^-,3K+R_r^-),&n=-15K+r<0,
\end{cases}
\qquad r=0,\ldots,14.
\]

Let $f(m)=m(m+1)$. The exact Jacobi entries in the staggered basis are

\[
 (N_S)_{nn}=2-\frac{f(m_L(n))+f(m_R(n-1))}{C},\qquad
 (N_S)_{n,n+1}=-\sqrt{\left(1-\frac{f(m_L(n))}{C}\right)
                           \left(1-\frac{f(m_R(n))}{C}\right)}.
\]

Define on $c_{00}(\mathbb Z)$

\[
 d_n=-f(m_L(n))-f(m_R(n-1)),\qquad
 c_n=\tfrac12\left[f(m_L(n))+f(m_R(n))\right],
\]

and $(Q\psi)_n=c_{n-1}\psi_{n-1}+d_n\psi_n+c_n\psi_{n+1}$. Since each fixed-support vector sees only finitely many labels and $S^2/C\to1$, expanding the square root gives $S^2(N_S-N_\infty)\psi\to Q\psi$ in $\ell^2$. Also $N_S\psi\to N_\infty\psi$, hence $N_S^2\psi\to N_\infty^2\psi$. The exact identity

\[
G_S+C N_\infty=N_S^2-C(N_S-N_\infty)
\]

then proves the displayed generator core limit. The central label join is included in these global formulas: the incoming edge at $n=-1$ has labels $(-1,0)$, and $f(-1)=f(0)=0$. This verifies the exact central coefficients without replacing them by either half-line's periodic continuation.

There is also a growing-window coefficient estimate. If $|k|\le K_S=o(\sqrt S)$, each label is $O(K_S+1)$ and $A=f(m_L),B=f(m_R)=O((K_S+1)^2)$. The exact diagonal error after multiplying by $S^2$ is $O((K_S+1)^2/S)$. For the offdiagonal, Taylor expansion of $\sqrt{(1-A/C)(1-B/C)}$ gives error $O((K_S+1)^2/S+(K_S+1)^4/S^2)$ after the same scaling. Both tend to zero uniformly in that window. Thus the core coefficient approximation has an overlap with cells whose index grows, but this is not an operator-norm or propagation estimate.

## Frozen-cell projections of the central coefficient

For a cell with $n=15k+r$ on the positive side or $n=-15K+r$ on the negative side, $Q$'s 15-cell frozen projection onto the same crossing pair has the following matrices. Here $k\ge1$ on both sides (write $K$ for the negative cell index); these are projections of coefficient arrays, not spectra of $Q$ or of the full finite-spin operator.

| side | boundary | projected matrix for $Q$ |
|---|---:|---|
| positive | $\theta=0$ | \(\left(-27k^2-33k-\frac{62}{5}\right)I+\begin{psmallmatrix}0&\frac{6k+4+6i\sqrt3(k+1)}5\\\frac{6k+4-6i\sqrt3(k+1)}5&0\end{psmallmatrix}\) |
| negative | $\theta=0$ | \(\left(-27k^2+33k-\frac{62}{5}\right)I+\begin{psmallmatrix}0&\frac{4-6k-6i\sqrt3(k-1)}5\\\frac{4-6k+6i\sqrt3(k-1)}5&0\end{psmallmatrix}\) |
| positive | $\theta=\pi$ | \(\left(-9k^2-\frac{51k}{5}-\frac{58}{15}\right)I+\begin{psmallmatrix}0&\frac{18k+8-i\sqrt3(6k+2)}{15}\\\frac{18k+8+i\sqrt3(6k+2)}{15}&0\end{psmallmatrix}\) |
| negative | $\theta=\pi$ | \(\left(-9k^2+\frac{51k}{5}-\frac{58}{15}\right)I+\begin{psmallmatrix}0&\frac{8-18k-i\sqrt3(2-6k)}{15}\\\frac{8-18k+i\sqrt3(2-6k)}{15}&0\end{psmallmatrix}\) |

The four coupling magnitudes are respectively

\[
\frac25\sqrt{36k^2+66k+31},\quad
\frac25\sqrt{36k^2-66k+31},\quad
\frac2{15}\sqrt{108k^2+90k+19},\quad
\frac2{15}\sqrt{108k^2-90k+19}.
\]

As $k\to\infty$, they equal

\[
\frac{12k}{5}+\frac{11}{5}+O(k^{-1}),\quad
\frac{12k}{5}-\frac{11}{5}+O(k^{-1}),\quad
\frac{4\sqrt3k}{5}+\frac{\sqrt3}{3}+O(k^{-1}),\quad
\frac{4\sqrt3k}{5}-\frac{\sqrt3}{3}+O(k^{-1}).
\]

The linear terms match $S|c_\pm(u)|$ after $u=3k/S$, the central rescaling of the outer $S^{-1}c_\pm(u)$ coupling. The constants are the offset correction. The frozen-cell gap of the central correction is $2|c_k|/S^2+o(S^{-2})$ for fixed cell index, so multiplication by $C$ leaves the finite phase scale $2|c_k|$ in the projected model; this remains a local frozen-cell statement. The exact scalar identity

\[
\frac{R_{3k+a}}{C}=1-\frac{(3k+a)(3k+a+1)}{S(S+1)}
\]

shows its source: when $u=3k/S$, the $-S^{-2}(u-a)(u-a-1)$ term of the outer coefficient expansion contributes at the same $S^{-2}$ order as the nominal principal and first-subprincipal terms. The runner verifies this match through $S^{-2}$ exactly and checks the finite-spin coefficients for $S=64,128,256,512$ on $|n|\le60$. Those floating checks corroborate the algebra; they do not establish uniformity for moving $n$.

## What remains open

Because $d_n,c_n=O(n^2)$, $Q$ is unbounded. Core convergence of $G_S+C N_\infty$ does not give norm convergence, strong-resolvent convergence, or convergence of $e^{-itG_S}$. At fixed laboratory time, the dominant fast phase uses $C=S(S+1)$ and the finite electric boundary is at distance $O(S)$. The prepared vector starts at $n=0$; its fast evolution can populate indices growing with $S$, and the present two-band and central calculations do not control that propagation or its mod-3 Fourier expectations. A full result needs global estimates for the two resonant band pairs, the central stationary layer, and endpoint reflection, as well as the complete $H_4$/output comparison. The signed-label identity above removes a separate coefficient seam from this list. All statements remain conditional on the supplied model at the cited main revision; the model is not an approved primitive, and no axiom or primitive is changed.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: conditional on the supplied six-site hop map and frozen first-mark output
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "This theorem gives local two-band frozen-cell normal forms and a coefficientwise generator-core limit. It provides no global spectral or fixed-time propagation estimate."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Use the bulk and central coefficient expansions as inputs to a uniform interior eigenphase/overlap sum for the single fixed-profile scalar at t=1/4; then treat the candidate extension and complete exact-versus-candidate output comparison."
```

The earlier checkpoint PR #8943 is closed without merge. Its conditional source is represented in current main at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`; the fixed-time obligation remains open.

## Verification

[`postmark_electric_two_band_central_match_2026_09_24.py`](../scripts/postmark_electric_two_band_central_match_2026_09_24.py) reconstructs the four outer crossing matrices and their detuning slopes symbolically, derives the four polynomial central projections, checks their coupling magnitudes and large-cell matching constants, expands the exact Casimir factor to second order, and compares central coefficients against an independent physical-state legal-hop enumeration for four spins on $|n|\le60$. It also checks the signed-label join at $n=-1/0$. On this fixed window, the maximum diagonal and link discrepancies decrease approximately as $1/S$ when $S$ doubles; these finite samples corroborate the coefficient formula but do not prove its limit. The exact JSON is [result JSON in current runner stdout](../logs/runner-cache/postmark_electric_two_band_central_match_2026_09_24.txt), and the content-bound execution record is [postmark_electric_two_band_central_match_2026_09_24.txt](../logs/runner-cache/postmark_electric_two_band_central_match_2026_09_24.txt). No propagation, global gap, scattering, or tail claim is checked by this runner.


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
