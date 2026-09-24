---
claim_id: postmark_electric_moving_index_cell_symbol_2026_09_24
claim_type: bounded_theorem
claim_scope: "Conditional on the supplied finite-spin one-vacancy hop map, the bulk 15-cell symbol of the staggered Jacobi matrix has folded cosine bands, and its first subprincipal cell matrix splits the mod-3-coupled folded crossings with the displayed coefficients. This local symbol calculation does not establish a global finite-spin spectral gap or propagate the prepared state."
upstream_dependencies:
  - fast_vacancy_motion_after_formation_bounded_theorem_note_2026-09-24
  - zero_mode_and_goegenbauer_limit_bounded_theorem_note_2026-09-24
runner: scripts/postmark_electric_moving_index_cell_symbol_2026_09_24.py
---

# The 15-cell symbol and its mod-3 resonances

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** proposed_retained

## Result up front

The leading bulk symbol of the staggered positive Jacobi matrix is the scalar dispersion

\[
\nu(u,q)=2(1-u^2)(1-\cos q),\qquad -1<u<1.
\]

The 15-cell representation folds this into bands indexed by \(\ell=0,\ldots,14\). The vacancy character \(V|n\rangle=e^{2\pi i n/3}|n\rangle\) couples bands separated by five. At two reduced-zone boundaries, those coupled bands cross in the leading symbol. The first residue-dependent correction, of size \(1/S\) in the Jacobi matrix, opens local cell-symbol gaps

\[
\frac{8|u|}{5S}+O(S^{-2}),\qquad
\frac{8\sqrt3|u|}{15S}+O(S^{-2}).
\]

The fixed-time propagator multiplies these gaps by \(C=S(S+1)\), so the corresponding frozen-cell phase splitting grows as \(S|u|\). At the prepared-state scale, \(|u|=O(S^{-1})\), this contribution is order one and is evaluated together with the finite-support correction. This is a theorem about the local frozen-cell symbol; it does not establish a full-operator gap or a fixed-time readout result.

## Exact target and proof dependency graph

**Exact target.** Conditional on the supplied six-site integer-spin hop factors and signed residue labels, derive the bulk 15-cell principal symbol of the staggered Jacobi matrix, the action of the mod-3 character on its Bloch bands, and the first-order compressed matrices at the two folded crossings, uniformly on each fixed compact interval \(\varepsilon\le |u|\le1-\varepsilon\).

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Exact finite-spin edge factors and signed residue labels | Imported condition | Canonical supplied-model and zero-mode notes cited below; not derived from the four axioms. |
| Uniform scalar and Jacobi-coefficient expansion on a compact bulk interval | Proved here | Exact Casimir identity followed by a uniform Taylor expansion away from \(|u|=1\). |
| Principal Bloch bands and mod-3 band-selection rule | Proved here | Direct diagonalization of the 15-cell circulant matrix and the character's residue multiplier. |
| Crossing locations and first-order compressed matrices | Proved here | Finite Fourier sums in the stated basis; exact symbolic and explicit-matrix checks are corroborative. |
| Global finite-spin spectrum, prepared-state propagation, and actual readout | Open | Requires global transport/scattering, central and endpoint matching, and state-tail/output bounds. |

The statement covers compact bulk intervals and the two specified crossing pairs. It excludes the central stationary region \(u\to0\), the electric edges \(|u|\to1\), and any global spectral or propagation conclusion. The strongest missing lemma for the campaign target is a fixed-time estimate for the period-three observable through the crossing and central regions, with finite-endpoint effects controlled.

## Imported inputs

| Role | Imported input | Provenance at the frozen base | Open bridge |
|---|---|---|---|
| Supplied physical model | One-vacancy path, integer-spin link factor, and signed edge labels | Canonical [fast-vacancy note](FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md) and [zero-mode note](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md) at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`; inherited from the supplied six-site construction | The four minimal axioms do not derive or select these dynamics; the axiom-to-model bridge remains open. |
| Mathematical tools | Finite-dimensional Bloch diagonalization, degenerate perturbation on an isolated two-dimensional eigenspace, and Taylor expansion | Standard finite-dimensional algebra applied directly in the displayed compact-interval calculation | No separate physical import; the required isolation and compact-interval hypotheses are checked in the proof. |

## Imported model and exact cell coefficients

The calculation is conditional on the supplied path and link rule in the canonical source note [FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md](FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md), present at main `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6` (SHA-256 `d235b264783de82bd563d17c217c0b3bc22718638223106215ae43edfd7dbb23`). Historical proposal PR #8831 is closed without merge; its conditional model argument is now represented by that canonical main note. Write \(M_S=A_S^*A_S\), \(C=S(S+1)\), \(N_S=J M_S J\), and \(J|n\rangle=(-1)^n|n\rangle\). This note uses the exact edge-label table in [ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md](ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md), at the same main revision (SHA-256 `b697aecbc9c8551df69eea76ea2e2aeb404dc0478fdc32e4dd1554b26a08fec8`):

```text
L+ = ( 0,  1,  0,  1,  1,  1,  2,  1,  2,  2,  2,  3,  2,  3,  3)
R+ = ( 0,  0,  0,  1,  0,  1,  1,  1,  2,  1,  2,  2,  2,  3,  2)
L- = (-1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3, -4, -4)
R- = (-1, -1, -1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3)
```

For a positive cell \(n=15k+r\), set \(u=3k/S\) and use \(m_L=3k+L_r^+\), \(m_R=3k+R_r^+\). For a negative cell \(n=-15K+r\), set \(u=3K/S\) and use \(m_L=3K+L_r^-\), \(m_R=3K+R_r^-\). With \(R_m=C-m(m+1)\), the scalar factor has the exact expansion

\[
\frac{R_{uS+a}}{C}
=(1-u^2)+\frac{\alpha_a(u)}{S}
-\frac{(u-a)(u-a-1)}{S^2(1+S^{-1})},
\qquad \alpha_a(u)=u^2-u(2a+1).
\]

For fixed \(\varepsilon>0\), this gives uniform first-order expansions on \(\varepsilon\le |u|\le1-\varepsilon\). Let \(b_{S,n}=(M_S)_{n,n+1}\). The exact edge and diagonal identities are

\[
b_{S,n}=\sqrt{(R_{m_L}/C)(R_{m_R}/C)},\qquad
(M_S)_{n,n}=R_{m_L(n)}/C+R_{m_R(n-1)}/C.
\]

Thus, on either side,

\[
b_{S,15k+r}=1-u^2+S^{-1}b_{1,r}^{\pm}(u)+O_\varepsilon(S^{-2}),
\quad
b_{1,r}^{\pm}=\frac{\alpha_{L_r^\pm}+\alpha_{R_r^\pm}}2,
\]

and

\[
(M_S)_{n,n}=2(1-u^2)+S^{-1}d_{1,r}^{\pm}(u)+O_\varepsilon(S^{-2}),
\quad
d_{1,r}^{\pm}=\alpha_{L_r^\pm}+\alpha_{\widetilde R_{r-1}^\pm}.
\]

For \(r>0\), \(\widetilde R_{r-1}=R_{r-1}\). At the cell seam,
\(\widetilde R_{-1}^+=R_{14}^+-3\) and
\(\widetilde R_{-1}^-=R_{14}^-+3\). Staggering changes the off-diagonal sign, so the local 15-cell symbol of \(N_S\) is

\[
\mathcal N_S^\pm(u,\theta)
=(1-u^2)\mathcal N_0(\theta)
+S^{-1}\mathcal N_1^\pm(u,\theta)+O_\varepsilon(S^{-2}),
\]

where \(\mathcal N_0\) has diagonal 2 and nearest-neighbor entries \(-1\), with Bloch twists \((\mathcal N_0)_{0,14}=-e^{-i\theta}\) and \((\mathcal N_0)_{14,0}=-e^{i\theta}\). Its eigenvectors are \(e^{iq_\ell r}/\sqrt{15}\), where

\[
q_\ell=\frac{\theta+2\pi\ell}{15},\qquad
\nu_\ell(u,\theta)=2(1-u^2)(1-\cos q_\ell).
\]

## The character selection rule and phase geometry

Within a 15-cell, \(V\) multiplies residue \(r\) by \(e^{2\pi i r/3}\). Since \(2\pi/3=2\pi\cdot5/15\), it maps Bloch band \(\ell\) to \(\ell+5\) modulo 15. The leading eigenvalue difference is

\[
\Delta_\ell(u,\theta)
=\nu_{\ell+5}-\nu_\ell
=2\sqrt3(1-u^2)\sin(q_\ell+\pi/3).
\]

Use the signed cell coordinate \(x=3k/S\), with \(n=15k+r\). The negative-side offsets obey \(L_r^-=-L_r^+-1\) and \(R_r^-=-R_r^+-1\), while \(\alpha_{-a-1}(|x|)=\alpha_a(x)\) for \(x<0\). Thus the two signed tables describe one coefficient expansion across \(x=0\). The simultaneous equations \(\partial_x\Delta=\partial_\theta\Delta=0\) have no solution for \(0<|x|<1\): the first requires \(\sin(q+\pi/3)=0\), while the second requires \(\cos(q+\pi/3)=0\). The principal phase has nondegenerate stationary points at \(x=0\), \(q=\pi/6\) or \(7\pi/6\); its Hessian determinant in \((x,\theta)\) is \(8/75\). The center is a stationary layer of the smooth signed coefficient family; its order-one phase uses the central second-order terms derived in the companion note.

The other special points are principal band crossings, where \(\Delta=0\) and \(\partial_\theta\Delta\ne0\). At \(\theta=0\), bands 5 and 10 meet at \(q=2\pi/3,4\pi/3\). At \(\theta=\pi\), bands 12 and 2 meet at \(q=5\pi/3,\pi/3\). Projection of \(\mathcal N_1^\pm\) onto each two-dimensional degenerate eigenspace gives:

| Side | Boundary | Projected first-order matrix | Coupling magnitude | Frozen-cell gap |
|---|---:|---|---:|---:|
| positive | \(\theta=0\), bands 5/10 | \(u(3u-11)I+\begin{psmallmatrix}0&2u(1+i\sqrt3)/5\\2u(1-i\sqrt3)/5&0\end{psmallmatrix}\) | \(4u/5\) | \(8u/(5S)+O(S^{-2})\) |
| negative | \(\theta=0\), bands 5/10 | \(u(3u+11)I+\begin{psmallmatrix}0&2u(-1-i\sqrt3)/5\\2u(-1+i\sqrt3)/5&0\end{psmallmatrix}\) | \(4u/5\) | \(8u/(5S)+O(S^{-2})\) |
| positive | \(\theta=\pi\), bands 12/2 | \(u(5u-17)I/5+\begin{psmallmatrix}0&2u(3-i\sqrt3)/15\\2u(3+i\sqrt3)/15&0\end{psmallmatrix}\) | \(4\sqrt3u/15\) | \(8\sqrt3u/(15S)+O(S^{-2})\) |
| negative | \(\theta=\pi\), bands 12/2 | \(u(5u+17)I/5+\begin{psmallmatrix}0&-2u(3-i\sqrt3)/15\\-2u(3+i\sqrt3)/15&0\end{psmallmatrix}\) | \(4\sqrt3u/15\) | \(8\sqrt3u/(15S)+O(S^{-2})\) |

At fixed laboratory time, the local propagator uses \(G_S=N_S^2-CN_S\), with eigenphase \(t(C\nu-\nu^2)\). For fixed \(u>0\), the first crossing therefore accumulates a phase difference \((8t/5)uS+O(1)\), and the second \((8\sqrt3t/15)uS+O(1)\). These are subprincipal-in-\(N_S\) effects but large phases in the target evolution. When \(u=O(S^{-1})\), the first-order gap contributes only order one; the finite-support operator correction and the central matching problem matter.

## What this establishes and what remains open

The exact algebra establishes the local 15-cell principal symbol, its mod-3 band-selection rule, the crossing locations, and the displayed first-order projected matrices. The runner also checks the principal Bloch eigenvalues at 15 \((u,\theta)\) samples and samples the finite-spin coefficient expansion for both signs at \(S=64,128,256,512,1024\); the maximum \(S^2\)-scaled remainder is below 30.4. Its floating checks corroborate the expansions and do not prove propagation.

The computed subprincipal term contributes the displayed large fixed-time phase in the frozen-cell model. This note does **not** prove that a frozen-cell avoided crossing is a gap of the global finite Jacobi operator, does not determine the prepared state's mass in the crossing region, and does not give a fixed-time limit or discrepancy. A global result needs estimates for the two resonant band pairs, the order-one central stationary contribution at \(x=0\), and the finite electric endpoints and output. The candidate-domain and complete \(H_4\)/output comparison are still open. All conclusions remain conditional on the supplied model at the cited main revision; the model is not an approved primitive, and no axiom or primitive is changed.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026-09-24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: conditional on the supplied six-site hop map, integer-spin factors, and first-mark output
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The theorem gives a conditional local-cell symbol and exact subprincipal coupling calculation. It does not prove a global spectral or fixed-time propagation conclusion."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Use the cell symbol and corrected crossing matrices as inputs to a uniform interior eigenphase/overlap sum for the single fixed-profile scalar at t=1/4; fixed-index kernel decay remains a stronger target."
```

The earlier checkpoint PR #8943 is closed without merge. Its conditional source is represented in current main at `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`; the fixed-time obligation remains open.

## Verification

[`postmark_electric_moving_index_cell_symbol_2026_09_24.py`](../scripts/postmark_electric_moving_index_cell_symbol_2026_09_24.py) rebuilds the two signed residue corrections from the exact hop-label arrays, verifies all four projected crossing matrices with SymPy, checks the folded 15-band principal matrix against direct Hermitian eigensolves, and samples the first-order expansion against the finite-spin Jacobi coefficients. The exact JSON result is [CELL_SYMBOL_RESULTS.json](../outputs/postmark_moving_index_2026_09_24/CELL_SYMBOL_RESULTS.json), and the content-bound run is recorded in [postmark_electric_moving_index_cell_symbol_2026_09_24.txt](../logs/runner-cache/postmark_electric_moving_index_cell_symbol_2026_09_24.txt). The eigensolves and finite-spin remainder scans are diagnostics; the note's algebra supplies the local-symbol derivation. The runner establishes no global transport estimate or readout limit.

All displayed complex matrices use \(v_q[r]=e^{+iqr}/\sqrt{15}\) and the projection \(\langle v_q|\mathcal N_1|v_{q'}\rangle\). An early scratch calculation transposed this projection, conjugating the off-diagonal phases while leaving every gap magnitude unchanged. The companion central-match runner checks all four corrected first-order matrices against explicit full 15-by-15 constructions in that stated basis.


## Review record

The early scratch version transposed the complex projection and conjugated the off-diagonal phases. This note uses the stated \(\langle v_q|\mathcal N_1|v_{q'}\rangle\) convention; the gap magnitudes were unchanged by that correction. The result ends at frozen-cell algebra and does not replace or narrow any global fixed-time claim.
