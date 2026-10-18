# A repulsion-protected controlled link in a finite clock network

One exactly calibrated mediator device supplies an old-\(X_1X_2\)-controlled hopping link inside a specified finite number-conserving clock network. A positive double-occupancy penalty suppresses the link's pair-creation channel, with all leakage included in a complete-output error bound. Positive onsite compensation can remove the virtual vacancy energy from the global one-head comparison. The actual dynamics need not conserve head number.

The four new source/check bodies in §8 have been fully read and accepted by ROOT at this conditional **single-link** scope. This manuscript is exposition, not another independent check or retained audit. It constructs no completed logical gate, common outgoing profile, return suppression or halt, and does not compose multiple mediated links sharing the old gap.

Intended canonical path: `docs/REAL_MEDIATED_VACANCY_NETWORK_BOUNDED_THEOREM_NOTE_2026-10-18.md`. Proposed new evidence root: `outputs/real_mediated_vacancy_network_2026_10_18/source_checks/`. The direct mathematical parent is the [exact mediator theorem, §10](REAL_TWO_BODY_GAP_MEDIATION_BOUNDED_THEOREM_NOTE_2026-10-18.md#10-an-exactly-calibrated-mediator-with-no-old-only-counterterm), at the exact source/check pins in §8.

## 1. Supplied physical mediator and its checked interface

The old pair has \(K=2I+Z_1Z_2\), and \(X=X_1X_2\), so \([K,X]=0\). Write \(n_v=|1\rangle\langle1|_v\) for an occupation projector. Two selected clock sites a,b and mediator m occupy the parent's nearest-neighbor geometry:
\[
 1=(0,0,0),\quad 2=(1,0,0),\quad
 a=(0,1,0),\quad b=(1,1,0),\quad m=(0,0,1).
\]
For \(0<\lambda\le10^{-3}\), define exactly
\[
 \begin{gathered}
 \ell=\lambda^2,\quad
 x=\frac{3\ell(2-\ell)}{1-\ell},\quad g=\sqrt{x},
 \quad A_0=4+2\ell+x,\\
 a_{\rm eff}=\frac{\sqrt{A_0+4\ell}+\sqrt{A_0-4\ell}}2,\qquad
 b_{\rm eff}=\frac{\sqrt{A_0+4\ell}-\sqrt{A_0-4\ell}}2,\qquad
 c_{\rm eff}=2\lambda+g+2-a_{\rm eff}.
 \end{gathered}
 \tag{NV1}
\]
The base Hamiltonian is the sum of five supplied positive real blocks
\[
 H_{\rm med}=K+\lambda(I+Y_1Y_a)+\lambda(I+Y_2Y_b)
                     +4n_m+g(I+X_1X_m).
 \tag{NV2}
\]
It contains the literal K once and no old-only counterterm. Its full-support incident loads are \(3+2\lambda+2g\) on old1, \(3+2\lambda\) on old2, \(2\lambda\) on each selected clock, and \(4+2g\) on m. The fixed gap and nonlinear calibration remain suppliers; \(g<3\lambda\) and \(0<b_{\rm eff}\le\lambda^2\).

The pinned exact theorem supplies a real orthogonal proof transformation \(\mathcal U\), with \(\|\mathcal U-I\|\le82\lambda\), such that
\[
 H_{\rm med}=c_{\rm eff}I+\mathcal U
       (K-b_{\rm eff}XY_aY_b+2a_{\rm eff}n_m)\mathcal U^\dagger.
 \tag{NV3}
\]
For any bounded selfadjoint physical addition A, extended to declared finite spectator sites, it gives
\[
 \|e^{-it(H_{\rm med}+A)}
  -e^{-ic_{\rm eff}t}e^{-it(K-b_{\rm eff}XY_aY_b+2a_{\rm eff}n_m+A)}\|
 \le\min\{2,164\lambda(1+|t|\|A\|)\}.
 \tag{NV4}
\]
This unchanged interface includes all mediator inputs and arbitrary correlations. It uses effective aging \(2a_{\rm eff}n_m\), not bare-gap aging \(4n_m\). Its exact-spectrum proof is a pinned dependency; no new independent check of it is claimed here.

## 2. Exact pair rotation, hopping and vacancy phase

On the selected pair write
\[
 T=Y_aY_b,\quad P_{00}=|00\rangle\langle00|,\quad
 P_{11}=|11\rangle\langle11|,\quad
 J_{ab}=|01\rangle\langle10|+|10\rangle\langle01|,\quad
 H_{\rm pair}=U P_{11}-XT,\quad U>0 .
 \tag{NV5}
\]
On the pair's one-head subspace, \(H_{\rm pair}=-XJ_{ab}\) exactly. In an old-X sector \(p=\pm1\), its even block in the order \((|00\rangle,|11\rangle)\) is
\[
 \begin{pmatrix}0&p\\p&U\end{pmatrix}.
 \tag{NV6}
\]
Define \(\Omega=\sqrt{U^2+4}\), \(r=(\Omega-U)/2=2/(\Omega+U)\), and \(\alpha=\arctan r\). Then \(r(U+r)=1\) and \(0<r\le1/U\). The normalized eigenvectors with eigenvalues \(-r,U+r\) are the two columns of
\[
 D_p=\begin{pmatrix}
 \cos\alpha&p\sin\alpha\\
 -p\sin\alpha&\cos\alpha
 \end{pmatrix}.
 \tag{NV7}
\]
For example, \(\sin\alpha=r\cos\alpha\) verifies the lower eigenvector and its minus sign. Use identity on the pair's one-head subspace and take the direct sum over p. This gives an exact real orthogonal D on old-plus-pair space with
\[
 H_{\rm pair}=D H_{\rm diag}D^\dagger,\qquad
 H_{\rm diag}=-XJ_{ab}-rP_{00}+(U+r)P_{11},\qquad
 \|D-I\|=2\sin(\alpha/2)\le1/U .
 \tag{NV8}
\]
D is analytical; no old-controlled higher-body rotation is physically installed.

The actual and diagonal even generators have the same scalar \(U/2\) and frequency \(\Omega/2\). Their Pauli axes differ by \(2\alpha\), so direct subtraction of their exponentials gives the exact full norm
\[
 \|e^{-isH_{\rm pair}}-e^{-isH_{\rm diag}}\|
   =2\sin\alpha\,|\sin(\Omega s/2)|\le2/U
   \quad(s\in\mathbb R).
 \tag{NV9}
\]
The odd sector contributes zero. This uniform bound retains actual double occupancy rather than projecting it away. For an initial pair vacancy the comparison contributes \(e^{irs}|00\rangle\), independently of p. On a coherent vacancy/one-head superposition, \(-rP_{00}\) is a relative energy, not a global scalar. Removing it would add \(2|\sin(rs/2)|\le|s|r\) to the local comparison.

## 3. Extending the dressing to a finite network

Let \(L\ge2\) be the number of clock qubits, including a,b, with global occupation \(N=\sum_jn_j\) and one-head projector \(P_1\). Let B be bounded selfadjoint and clock-only, with \([B,N]=0\). It may move the head into or out of a,b; local pair occupation need not be conserved. All other clocks occupy distinct supplied sites, with any physical geometry specified separately.

Extend D by identity on the other clocks, mediator and passive systems. For any such network B, the full-space calculation gives
\[
 D^\dagger BD-B=D^\dagger B(D-I)+(D^\dagger-I)B,\qquad
 \|D^\dagger BD-B\|\le2\|D-I\|\|B\|.
 \tag{NV10}
\]
Conjugation, Duhamel for this difference and both endpoint rotations therefore imply
\[
 \|e^{-is(H_{\rm pair}+B)}
        -e^{-is(H_{\rm diag}+B)}\|
 \le\min\{2,(2/U)(1+|s|\|B\|)\}.
 \tag{NV11}
\]
The norm is the full network norm. Neither \(\|P_1BP_1\|\) nor a local one-head norm substitutes for it. This argument needs no local no-double invariance. Actual pair creation from a vacancy may turn an initial global one-head state into three heads; these outputs remain in (NV11).

The comparison \(H_{\rm diag}+B\) does conserve N. On \(P_1\), \(P_{11}=0\) and \(P_{00}=I-n_a-n_b\), giving the exact restricted target
\[
 H_{\rm one}=-XJ_{ab}+B|_{P_1}-rI+r(n_a+n_b).
 \tag{NV12}
\]
Thus the head can leave the pair in the target while this restriction remains valid. The controlled global one-head sector, rather than the pair's local one-head sector, is the required invariant space.

## 4. Positive compensation and its full norm

Optionally add the positive, number-conserving operator
\[
 B_{\rm comp}=r\sum_{j\notin\{a,b\}}n_j .
 \tag{NV13}
\]
On the global one-head sector it is exactly \(r(I-n_a-n_b)\). It cancels the entire vacancy term in (NV12), leaving
\[
 H_{\rm one,comp}=-XJ_{ab}+B|_{P_1}.
 \tag{NV14}
\]
No extra vacancy phase is then appended: that would count the cancellation twice. Without compensation, keep (NV12), including its relative onsite shift.

This cancellation is only a one-head identity. On the complete clock Hilbert space all outside occupations may simultaneously equal one, so
\[
 \|B_{\rm comp}\|=r(L-2),\qquad
 \|B+B_{\rm comp}\|\le\|B\|+r(L-2).
 \tag{NV15}
\]
The extensive norm in (NV15), not the one-head norm r, is used in the dressing bound. For \(L=2\) the compensation sum is empty and the formulas reduce correctly.

## 5. Actual positive inventory, geometry and counts

For a physical realization, supply a finite embedding containing the base geometry and a listed decomposition \(B=\sum_{\nu=1}^q B_\nu\). Each \(B_\nu\) is positive and real on an allowed onsite or nearest-neighbor pair support, and the total B commutes with N. Abstract selfadjointness and number conservation alone do not provide this decomposition or embedding.

In addition to the five blocks in (NV2), install
\[
 b_{\rm eff}U n_an_b,\qquad
 b_{\rm eff}B_\nu\ (\nu=1,\ldots,q),\qquad
 b_{\rm eff}r n_j\ (j\notin\{a,b\})
 \ \text{if compensated}.
 \tag{NV16}
\]
The repulsion is finite and positive, with its full norm charged at both endpoints. There are \(L+3\) qubits. Without compensation there are \(6+q\) listed positive blocks; with compensation there are \(L+4+q\). Repeated supports remain separately counted. This does not assert that an arbitrary requested graph admits the specified geometry.

Define \(L_B(v)=\sum_{\nu:\,v\in\operatorname{supp}B_\nu}\|B_\nu\|\). Actual incident loads are
\[
 \begin{array}{c|c}
 \text{site}&\text{incident norm sum}\\ \hline
 1&3+2\lambda+2g\\
 2&3+2\lambda\\
 m&4+2g\\
 a&2\lambda+b_{\rm eff}[U+L_B(a)]\\
 b&2\lambda+b_{\rm eff}[U+L_B(b)]\\
 \text{outside clock }j&
   b_{\rm eff}L_B(j)+b_{\rm eff}r\ \text{if compensated}\\
 \text{outside clock }j&
   b_{\rm eff}L_B(j)\ \text{otherwise}.
 \end{array}
 \tag{NV17}
\]
Every row must obey the supplied cap; endpoint sums are evaluated individually. The network's degree and supports are those of its actual inventory. No uniform degree bound for an unspecified B is inferred from the local five-qubit geometry.

## 6. Two-stage complete-output theorem and simultaneous budgets

Put \(B_{\rm tot}=B\) or \(B+B_{\rm comp}\), and respectively
\[
 M_B=\|B\|\quad\text{or}\quad \|B\|+r(L-2),\qquad s=b_{\rm eff}t.
 \tag{NV18}
\]
The actual generator is \(H_{\rm phys}=H_{\rm med}+b_{\rm eff}(UP_{11}+B_{\rm tot})\), interpreted as the positive inventory in (NV16). Its added norm is at most \(b_{\rm eff}(U+M_B)\). Applying (NV4) first compares its evolution with
\[
 e^{-ic_{\rm eff}t}e^{-itK}
       e^{-is(H_{\rm pair}+B_{\rm tot})}
                   \otimes e^{-it\,2a_{\rm eff}n_m}
 \tag{NV19}
\]
at error at most \(164\lambda[1+|s|(U+M_B)]\).
The factorization of K uses that B is clock-only and \([K,X]=0\).
Apply (NV11) second, then restrict only the initial clock support to \(P_1\).

Let \(\iota_1\) embed the full old/one-head-clock/mediator input into the complete physical output space, preserving any passive reference. With \(H_*=H_{\rm one}\) or \(H_{\rm one,comp}\), the result is
\[
 \begin{aligned}
 \big\|e^{-itH_{\rm phys}}\iota_1
  -e^{-ic_{\rm eff}t}\iota_1
      \big[e^{-itK}e^{-isH_*}\otimes
                    e^{-it\,2a_{\rm eff}n_m}\big]\big\|
 &\le E(s),\\
 E(s)&=164\lambda[1+|s|(U+M_B)]
                  +\frac2U(1+|s|M_B).
 \end{aligned}
 \tag{NV20}
\]
The bound may be capped at two. Every actual extra head and mediator output remains in this norm. No projection, measurement or reset is performed at the end. The two stages respectively pay for mediator simulation with the full repulsion/background norm, and for the pair rotation in that full network.

The initial old, one-head clock and mediator may be arbitrarily correlated, with arbitrary passive extensions. No mediator preparation is required. Its comparison profile is the explicitly retained effective aging, not bare-gap aging or a common product output for correlated seeds. A definite one-head basis seed is a real product clock input, but the target propagation can depend coherently on the old state; (NV20) supplies no common outgoing profile.

The scalar \(c_{\rm eff}\) and full elapsed K are retained once. Any scalar in B stays in its target exponential. The uncompensated vacancy energy remains in \(H_{\rm one}\); the compensated target has no additional vacancy scalar.

For a fixed finite network, horizon \(S\ge0\), tolerance \(0<\epsilon\le1\), set \(b_{\rm norm}=\|B\|\) and \(d=L-2\) with compensation, \(d=0\) otherwise. Choose
\[
 U\ge\max\left\{1,\frac{16(1+Sb_{\rm norm})}{\epsilon},
                         \sqrt{\frac{16Sd}{\epsilon}}\right\}.
 \tag{NV21}
\]
Since \(r\le1/U\), the clock term over \(|s|\le S\) is bounded by
\[
 \frac{2(1+Sb_{\rm norm})}{U}+\frac{2Sd}{U^2}
       \le\epsilon/8+\epsilon/8=\epsilon/4.
 \tag{NV22}
\]
When \(Sd=0\), the second summand vanishes. Next choose
\[
 \lambda\le\min\left\{10^{-3},
  \frac{\epsilon}{656[1+S(U+b_{\rm norm}+d/U)]}\right\}.
 \tag{NV23}
\]
The mediator term is then at most \(\epsilon/4\), and (NV20) gives complete isometry error at most \(\epsilon/2\) throughout \(|b_{\rm eff}t|\le S\). The unhalved complete channel distance is at most \(\epsilon\).

For explicit cap feasibility put
\[
 C_{\rm load}=U+\sum_\nu\|B_\nu\|+\frac dU.
 \tag{NV24}
\]
Using \(g<3\lambda\), \(b_{\rm eff}\le\lambda^2\), and the actual loads (NV17), every site is bounded by \(4+8\lambda+\lambda^2C_{\rm load}\). For a compensated outside site, \(r\le d/U\) when \(d\ge1\); if \(d=0\) no such term exists. Any \(\Lambda>4\) therefore permits the further conditions
\[
 \lambda\le\min\left\{\frac{\Lambda-4}{16},
                    \sqrt{\frac{\Lambda-4}{2C_{\rm load}}}\right\}.
 \tag{NV25}
\]
They allocate half the cap margin to each of the last two terms. These conditions are simultaneous for fixed finite supplied data. They include \(L=2\) and \(S=0\). A growing network requires evaluation of its actual background norm, block norm sum, size and geometry; no volume-independent resource claim is inferred.

## 7. Scope

The conclusion is one controlled hopping link in a supplied target network, with an optional positive cancellation of its one-head vacancy shift. It allows the head to leave the pair in the target and pays actual leakage on a stated horizon. It chooses no graph implementing W, proves no ordered logical action or common outgoing profile, and gives no return/reflection bound, released-gate retention, capture, reset or permanent halt.

Several mediated links sharing the same old gap cannot be substituted or added under this single-link theorem. Their cross terms and actual combined spectrum need a separate argument. The exact coefficient calibration, old K, gap, positive local network inventory, embedding, initial global one-head support and observation horizon remain suppliers. No native microscopic or preparation mechanism is derived.

## 8. Frozen sources, review status and exposure

The four new packet bodies are mapped below. Historical pending-review labels remain unchanged inside those sources; current support comes from their actual distinct checks.

| New source/check | Bytes / lines | SHA256 |
|---|---:|---|
| [Local vacancy primitive](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation/VACANCY_HOPPING_PROBE.md) | 9334 / 124 | `7ce327a279b7c89e6ee48dd94555a78bdb357dd183b4333618f958e4d387da00` |
| [Distinct local check](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation_check/VACANCY_HOPPING_REVIEW.md) | 10856 / 107 | `f1e754ed52ccb2ea27c3831659467a3f94f51d8ce75b26c8b7ce882a4b7e9df3` |
| [Network interface](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation/NETWORK_VACANCY_INTERFACE.md) | 9142 / 124 | `de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e` |
| [Distinct network check](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation_check/NETWORK_VACANCY_REVIEW.md) | 9450 / 91 | `88169175decc90a4f706ea3a1168ae54bf763e5a0cb5d3cb516b749fd65b9066` |

The inherited exact-mediator [source](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/EXACT_ALL_TIME.md), SHA256 `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`, and [check](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/EXACT_ALL_TIME_REVIEW.md), SHA256 `80c09db471dea4542ccfe9b236b91ccd2cd285502ce4b091d59cbcfbfa7e1e70`, stay mapped to the parent packet. Their checked hypotheses and exact functional coefficients are reused; the earlier \(\sqrt6\,\lambda\) second-order device and the clock-return gate are not proof imports.

The writer fully read all four new bodies, and previously fully read the unchanged exact-mediator source/check. ROOT proposed the repulsion, global one-head and compensation routes; authors and checker disclosed shared campaign/design and same-model exposure. This manuscript reconstructs their exposition without claiming another independent, blind or model-diverse check. No retained-audit or publication status is assigned.

Only `NETWORK_NOTE.md` was written for this task. Work comprised complete reading, analytical exposition, deterministic metadata checks and full manuscript readback. No scientific executable, simulation, external search, Git/canonical/checkpoint/prompt/axiom change, delegation, model/effort override or publication was performed. Source links are proposed packet locations; ROOT owns integration and publication.
