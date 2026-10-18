# A repulsion-protected controlled link in a finite clock network

One exactly calibrated mediator device supplies an old-\(X_1X_2\)-controlled hopping link inside a specified finite number-conserving clock network. A positive double-occupancy penalty suppresses the link's pair-creation channel, with all leakage included in a complete-output error bound. Positive onsite compensation can remove the virtual vacancy energy from the global one-head comparison. The actual dynamics need not conserve head number.

The four new source/check bodies in §8 have been fully read and accepted by ROOT at this conditional **single-link** scope. This manuscript is exposition, not another independent check or retained audit. The finite-network interface in sections 1–8 constructs no completed logical gate, common outgoing profile, return suppression or halt, and does not compose multiple mediated links sharing the old gap.

Exact source identities and integration provenance are recorded in [SOURCES.json](../outputs/real_mediated_vacancy_network_2026_10_18/SOURCES.json). The direct mathematical parent is the [exact mediator theorem, §10](REAL_TWO_BODY_GAP_MEDIATION_BOUNDED_THEOREM_NOTE_2026-10-18.md#10-an-exactly-calibrated-mediator-with-no-old-only-counterterm), at the exact source/check pins in §8.

Sections 9–11 add the checked local-support refinement, an explicit positive six-clock stationary interferometer and a normalized narrowband scattering-packet interface. These results retain the literal gate and common phase. The packet construction uses infinite comparison leads; no physical product-seed launcher, finite cut or finite-time released-output window is established. Historical author-time pending labels below are superseded only by the identified scoped reviews.

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
In this baseline estimate the extensive norm in (NV15), not the one-head norm r, is used in the dressing bound. Section 9 sharpens this using exact support commutators, without dropping the far dynamics. For \(L=2\) the compensation sum is empty and the formulas reduce correctly.

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

The conclusion of sections 1–6 is one controlled hopping link in a supplied target network, with an optional positive cancellation of its one-head vacancy shift. It allows the head to leave the pair in the target and pays actual leakage on a stated horizon. It chooses no graph implementing W, proves no ordered logical action or common outgoing profile, and gives no return/reflection bound, released-gate retention, capture, reset or permanent halt.

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

The unchanged manuscript is frozen as AUTHOR_NOTE.md in the evidence packet. ROOT integrated the canonical note and evidence packet. This publication adds no independent mathematical check or retained-audit status. Physical axioms and editable prompts were unchanged.


## 9. Local-support refinement

The following frozen derivation has been fully read and accepted by ROOT at the scope of its [distinct review](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation_check/LOCAL_BACKGROUND_REVIEW.md). The original source and review identities are pinned in SOURCES.json. Historical pending labels and task-only provenance are preserved as author-time statements. This integration is not another independent check.

Status: new author sharpening, pending distinct check. ROOT proposed separating background blocks disjoint from the active clock pair. This note proves the two required exact commutators, retains the entire background evolution, and gives the resulting finite-network budget. Earlier bounds remain valid and unchanged; no new gate or finite-release theorem is inferred.

Dependencies: EXACT_ALL_TIME.md SHA `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`; VACANCY_HOPPING_PROBE.md SHA `7ce327a279b7c89e6ee48dd94555a78bdb357dd183b4333618f958e4d387da00`; NETWORK_VACANCY_INTERFACE.md SHA `de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e`. ROOT reports these accepted at their scoped interfaces. Their arguments were fully read/authored previously and are reused at unchanged identities. This is shared-design author evidence, not a further independent review.

### Support is the decisive hypothesis

Take a finite network of clock qubits containing the neighboring pair a,b, plus the two old qubits and mediator m. The exact mediator polar dressing U_med from EXACT_ALL_TIME is constructed entirely from spectral projectors of operators on old1,old2,a,b,m. When this device is embedded in the clock network, use U_med tensor identity on every other site and passive reference. It retains its exact intertwining identity and ||U_med−I||<=82lambda. Degeneracies introduced by spectators do not require a new arbitrary global spectral choice: this explicitly extended local dressing already proves the identity.

The vacancy rotation D_vac is likewise the explicit pair rotation, controlled by the old operator X1X2. It acts only on old1,old2,a,b and has ||D_vac−I||<=1/U, where U>0 is the dimensionless repulsion. Neither dressing is installed as a physical block.

Let the actual clock-only background inventory be B=sum_ell B_ell, with bounded real positive allowed local blocks and [B,N]=0, N=sum_clock n_j. Split the LISTED blocks into

    B_near=sum_{supp(B_ell) intersects {a,b}} B_ell,
    B_far =sum_{supp(B_ell) disjoint from {a,b}} B_ell.

The blocks act trivially on old and mediator sites. Their local supports give exactly

    [B_far,U_med]=[B_far,D_vac]=0.                 (1)

The optional vacancy compensation B_comp=r sum_{j outside {a,b}}n_j, r=(sqrt(U²+4)−U)/2, also commutes with both dressings. These are support statements on the full occupation Hilbert space, not expectations on a one-head input. If a background term acts on an old qubit or mediator, disjointness from {a,b} alone would not prove (1); that different inventory is excluded here.

It is not necessary that B_near commute with B_far or that each part separately conserve N. The actual target retains their sum and its assumed global number conservation.

### Physical mediator comparison with the full far background retained

Use H_med=c_eff I+U_med H_eff U_med†, with

    H_eff=K−b_eff X1X2Y_aY_b+2a_eff n_m.

Install the physical background

    b_eff[U n_a n_b+B_near+B_far+B_comp].

On conjugating it by U_med, only U n_a n_b+B_near can change. With M=||B_near||, the transformed-minus-original background norm is therefore at most

    2||U_med−I|| b_eff(U+M).

The outside dressing factors plus Duhamel give, with s=b_eff t,

    mediator error <=164lambda[1+|s|(U+M)].        (2)

The comparator contains the ENTIRE B_far and B_comp. Their norms do not enter (2) because their conjugation error is exactly zero, not because their dynamics were discarded or replaced by a one-head compression. Duhamel between selfadjoint finite matrices bounds the difference by the perturbation norm independently of the sizes of the common terms. No commutation of these common terms with the retained near terms is needed.

### Vacancy comparison and global one-head restriction

At the clock level H_pair=U P11−X1X2Y_aY_b=D_vac H_diag D_vac† with

    H_diag=−X1X2 J_ab−rP00+(U+r)P11.

Using (1), conjugation of B_near+B_far+B_comp changes only B_near. The same two-endpoint and Duhamel estimate gives

    vacancy error <=(2/U)(1+|s|M).                (3)

Again all far dynamics and compensation remain in the comparison. H_diag+B+B_comp commutes with global N. Restrict its comparison evolution, but not the actual evolution, to the initial global one-head subspace. There P11=0, P00=I−n_a−n_b and B_comp=r(I−n_a−n_b). The vacancy shift cancels exactly. The resulting target is generated by

    −X1X2 J_ab+B|_{N=1}.

Actual pair-creation leakage is included in (3). No final projection, reset or selection of a rare outcome is performed.

Combining (2)-(3), the complete no-double/global-one-head input isometry is within

    E(s)=164lambda[1+|s|(U+M)]
                          +(2/U)(1+|s|M)         (4)

of

    exp(−it c_eff) exp(−itK)
       exp[−is(−X1X2 J_ab+B|_{N=1})]
                       tensor exp(−it2a_eff n_m).

The product factors commute for this clock-only background. The target applies to arbitrary old/clock/mediator correlations initially supported on one clock head and to arbitrary passive references. A definite head at one vertex is a real product clock input. The initial mediator is unrestricted. The scalar and effective mediator aging are retained as in the source; no bare-gap or reset replacement is made.

Without compensation use the same bound (4) and retain −rI+r(n_a+n_b) in the restricted target generator. There is then no extra compensation inventory.

### Explicit budgets, caps and what remains extensive

For a specified finite clock network, scaled horizon |s|<=S and 0<epsilon<=1, it suffices to take

    U>=8(1+SM)/epsilon,
    lambda<=min{1/1000,
                  epsilon/[656(1+S(U+M))]}.

Then each term in (4) is <=epsilon/4, so the complete vector error is <=epsilon/2 and the unhalved complete channel error <=epsilon. A readily evaluated bound is M<=sum_{ell incident a or b}||B_ell||, counting each listed block once in this union. This is a full-support operator norm bound; it is not its one-head restriction.

The compensation still has L−2 installed positive onsite blocks for L clocks, full norm r(L−2), and load b_eff r at each outside clock. Its extensive norm is absent from (4) because of exact (1), not because those hardware resources disappear. Counts remain L+3 qubits and L+4+q positive blocks with q listed B blocks, as in the frozen network source. The repulsion block costs b_eff U at each of a,b. All B blocks incur b_eff||B_ell|| at each incident site.

For a simple sufficient cap condition, put K_load=max_v sum_{ell incident v}||B_ell|| over clock sites, and C_load=U+K_load+r. The original source gives g<3lambda, b_eff<=lambda². Every incident load is then <=4+8lambda+lambda² C_load. For any Lambda>4, additionally choosing

    lambda<=min{(Lambda−4)/16,
                    sqrt((Lambda−4)/(2C_load))}

ensures the cap. This condition pays the local far-block load even though their total norm is absent from the dynamical error. Constants can depend on the chosen local inventory; no uniform bound is assumed for an unspecified graph with growing incident weights.

This proof is for each finite network. It does not construct an infinite-volume many-head generator or justify exchanging an infinite-volume limit with evolution. It does show that this particular finite-network dynamical error need not grow with distant arm length when the near inventory and local cap remain fixed. Source preparation, actual propagation, common head output and boundary-return errors remain separate obligations.

### Scope and work record

The improved estimate is a local-support consequence of two already explicit finite dressings. It neither changes the actual Hamiltonian nor improves unproved packet or gate properties. It does not justify multiple shared-gap mediated edges, a released literal W, capture, reset, or permanent halt. Positivity, calibrated coefficients, finite geometry, initial one-head support and the chosen finite observation horizon remain supplied.

ROOT proposed the locality sharpening; the support commutators, retained-background Duhamel argument and budgets were reconstructed here. No scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication, delegation or predecessor edit occurred. Only this new source was written. Distinct checking is required before downstream promotion.


## 10. Positive two-plaquette stationary phase

The following frozen derivation has been fully read and accepted by ROOT at the scope of its [distinct review](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation_check/LADDER_SCATTERING_REVIEW.md). The original source and review identities are pinned in SOURCES.json. Historical pending labels and task-only provenance are preserved as author-time statements. This integration is not another independent check. The left lead extends from (0,1,-1) along decreasing x and the right from (1,1,1) along increasing x; these supplied sparse rays avoid the old and mediator sites. No negative decision-note result is needed for the positive algebra below.

Status: new author calculation, pending distinct check. This note gives an explicit feasible stationary solution, not a finite launched/released gate. ROOT proposed investigating the ladder; the Schur reduction and coefficients below were derived algebraically without a coefficient scan. NEXT_RELEASE_DECISION.md SHA `d1e9fc151e85d3d525b06b066402dc0d4b0822aa3d7479a6e8171c260887a417` remains frozen. The physical controlled-link interface is NETWORK_VACANCY_INTERFACE.md SHA `de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e`, reported checked by ROOT at its exact scope.

### Geometry, actual positive clock inventory and conventions

Use the six clocks of the decision note. Ports are L=a_-=(0,1,−1), R=b_+=(1,1,1). Other vertices are v=b_-=(1,1,−1), A=a=(0,1,0), B=b=(1,1,0), w=a_+=(0,1,1). The controlled edge A-B has one-head hopping −p, p=old X1X2=±1, with no ordinary parallel A-B hopping. Six ordinary positive exchange blocks have weights

    q1: L-v; q2: L-A; q3: v-B;
    q4: A-w; q5: B-R; q6: w-R.

An edge of weight q contributes q(n_i+n_j−sigma_i^+sigma_j^−−sigma_i^−sigma_j^+) and has full-support norm 2q. Each clock also may have a positive onsite eta_i n_i. Attach unit-weight semi-infinite leads at L and R along the disjoint rays stated in the decision note. The lead contribution to each port diagonal is 1. Lead interiors have diagonal 2 and hopping −1. All this is the compensated effective one-head comparison: its physical realization retains the separately paid repulsion, mediator and compensation blocks.

At E=2−2cos k, 0<k<pi, number the lead coordinate n=0 at its port, increasing outward. Left incidence has amplitude e^{-ikn}+r_p e^{ikn}; the right outgoing wave is t_p e^{ikn}. This convention fixes the common phase, without adding an unmentioned edge-length phase.

### General rational Schur reduction

Let d_i be the actual diagonal of H−E at vertex i:

    dL=q1+q2+1+eta_L−E, dR=q5+q6+1+eta_R−E,
    dv=q1+q3+eta_v−E, dw=q4+q6+eta_w−E,
    dA=q2+q4+eta_A−E, dB=q3+q5+eta_B−E.

Assume dv,dw are nonzero and define

    f=q1 q3/dv, h=q4 q6/dw,
    alpha=dA−q4²/dw, beta=dB−q3²/dv,
    D=alpha beta−1,
    l0=dL−q1²/dv, r0=dR−q6²/dw.

Assume D!=0. Eliminate v,w first, leaving A,B with matrix [[alpha,−p],[−p,beta]]. Their inverse is D^{-1}[[beta,p],[p,alpha]]. The final two-port H−E Schur matrix is [[ell_p,−h_p],[−h_p,rho_p]], where

    ell_p=l0−[beta q2²+2p q2 f+alpha f²]/D,
    rho_p=r0−[beta h²+2p h q5+alpha q5²]/D,
    h_p=[beta q2 h+alpha f q5+p(q2 q5+f h)]/D.    (1)

These formulas include all onsite sums from positive blocks; no diagonal has been silently flattened. The internal determinant is dv dw D, so the stated exclusions precisely justify this elimination.

Outgoing lead matching gives

    ell_p(1+r_p)−h_p t_p−(e^{-ik}+r_p e^{ik})=0,
    −h_p(1+r_p)+(rho_p−e^{ik})t_p=0.             (2)

In particular zero reflection requires

    h_p²=(ell_p−e^{-ik})(rho_p−e^{ik}).           (3)

All quantities in (1) are real at real nonsingular E. Since sin k>0, (3) implies ell_p=rho_p. Then with A_p=ell_p−cos k and y=sin k,

    h_p²=A_p²+y², t_p=h_p/(A_p−iy).             (4)

Both sector equations and their transmission ratio must be checked; equal probabilities alone do not implement a coherent old-sector gate.

### Symmetric reduction and constructive solution

Impose the explicitly allowed inversion symmetry

    q1=q6=a, q2=q5=b, q3=q4=c,
    eta_L=eta_R, eta_v=eta_w, eta_A=eta_B.

Then dv=dw=d, f=h=ac/d, alpha=beta=z, D=z²−1, l0=r0. Consequently ell_p=rho_p and

    ell_p=l0−[z(b²+f²)+2pbf]/D,
    h_p=[2zbf+p(b²+f²)]/D.                       (5)

One constructive branch sets k=pi/2, z=0, l0=0. Then D=−1, ell_p=2pbf and h_p=−p(b²+f²). Transparency (4) reduces to (b²−f²)²=1. The desired relative phase is obtained by choosing b=3f and f²=1/8, since

    (b²−f²)/(2bf)=4/3=tan theta.

Here is a complete positive realization of those constraints:

    f=1/sqrt(8), a=c=f/2, b=3f,
    eta_L=eta_R=1−5f/2,
    eta_A=eta_B=2−5f/2,
    eta_v=eta_w=2−3f/4.                            (6)

All weights and onsite coefficients are strictly positive. For example 5f/2=5/(4sqrt2)<1 since 25<32. At E=2 their actual shifted diagonals are dL=dR=f, dv=dw=f/4, dA=dB=f. Thus ac/d=f, z=f−c²/d=0, l0=f−a²/d=0. The internal determinant is −f²/16, nonzero. Every use of (1) is therefore legitimate at this energy.

Equations (5)-(6) give

    ell_p=rho_p=3p/4, h_p=−5p/4,
    r_+=r_-=0,
    t_+=−(3+4i)/5, t_-=−(3−4i)/5.                (7)

Indeed |h_p|²=25/16=(3/4)²+1. Therefore

    t_+/t_-=exp(2i theta),
    t_p=−exp(−i theta) w_p.                      (8)

The real inversion-symmetric core has the same matched transmission for incidence from the other lead. Its two-port scattering matrix is S_p=t_p X_ports at k=pi/2. The complete on-shell logical operation is consequently the literal W times the common scalar −exp(−i theta), along with swapping input/output port labels. For arbitrary coherent old inputs and passive references this statement follows from the orthogonal old-X sector decomposition; it is not a classical choice of p.

### Positive inventory and unresolved packet obligations

The core clock background uses six ordinary exchange blocks and six positive onsite blocks, q_core=12. Their actual coefficients are (6). Its sum-of-full-norm bound is

    2 sum_edges q_e +sum_vertices eta_i
       =16f+(10−23f/2)=10+9f/2.

This is a conservative full-space bound, not the one-head spectral norm. Additional finite lead bonds and endpoint/source repairs must be listed and paid. With M_I,M_O additional finite lead vertices and no such repairs yet, L=6+M_I+M_O clocks and q=12+M_I+M_O ordinary background blocks. The compensated physical inventory formula is L+3 qubits and L+4+q blocks. These counts alone do not specify a launched finite device: the finite boundary diagonal and source preparation still need a design.

The literal old K, actual mediator phase and effective mediator aging remain those of the pinned interface; (8) adds the common stationary phase −exp(−i theta). This source derives no time-independent common clock output, no normalizable stationary state, and no ready-to-use finite runtime. It has two infinite leads only as an on-shell scattering calculation; the positive physical approximation theorem applies after specifying a finite network and its norm/horizon budget.

The next decisive proof is now concrete rather than a coefficient search: derive a pole-free momentum interval about pi/2 from (1), bound the derivatives of both full scattering columns and all internal maps, and show the relative phase/profile error is small for an explicitly normalized narrow packet. At the center energy the flux velocities match because the two lead dispersions are identical; away from it, sector-dependent group delay and reflected amplitudes must be paid. Then construct an actual product endpoint-seed launch, finite cuts and an output window before return, preserving all mediator/clock/reference outputs. Existing unrelated launch or release theorems are not imported by analogy.

The compensated-network physical error remains additional to those packet errors. In the original bound it pays ||B||+r(L−2) on the complete finite network; any sharper locality estimate needs its own proof. No permanent halt, capture, reset or native supplier is established by perfect transmission at one energy.

This new exact solution was obtained by symbolic hand reduction of the symmetric equations, without a coefficient scan or scientific executable. ROOT supplied the ladder task; the source is shared-lineage author work pending distinct check. Only this note was written; frozen sources, Git, canonical/checkpoint/editable-prompt/model settings remain unchanged.


## 11. Pole-free band and normalized scattering packets

The following frozen derivation is accepted at its infinite-graph constructed-packet scope following the [distinct bandwidth review](../outputs/real_mediated_vacancy_network_2026_10_18/source_checks/counterterm_free_gap_mediation_check/BANDWIDTH_REVIEW.md), fully read by ROOT. The review explicitly controls the phase-curvature term in the half-line Fourier-tail estimate and the extension by density. No finite launcher or retention result follows. Historical pending and task-only provenance below are author-time statements; identities are pinned in SOURCES.json.

Status: new bounded author derivation, pending distinct check. The exact center solution is LADDER_SCATTERING_REDUCTION.md SHA `4f22fdb84d7636a6caad536323e5f02f971fba04a22ae9e8292e3c4e234929cc`, currently undergoing distinct check. This note is conditional on that source's explicit finite matrices; their norms are bounded independently below. No endpoint-seed, finite-cut or release-time theorem is imported.

ROOT requested an explicit band and derivative interface. The constants here are deliberately coarse and obtained analytically, with no scan or scientific executable. Frozen predecessors remain unchanged.

### Finite matching matrix and normalization convention

Use exactly the six-vertex core, positive coefficients and unit leads of the center source. Write k0=pi/2, E(k)=2−2cos k, z(k)=exp(ik). The core matrix H_core includes the unit lead bond's +1 diagonal at each port but not the external lead vertices. Let P:C²->C⁶ insert the left/right port amplitudes. Conditional on old X1X2=p, define

    F_p(k)=H_core,p−E(k)I−z(k)PP†.                (1)

For incoming channel amplitude a in C², the complete six-core stationary field and outgoing channel amplitudes are

    T_p(k)a=−2i sin(k) F_p(k)^{-1}P a,
    S_p(k)a=P†T_p(k)a−a.                          (2)

Indeed on either lead the amplitude is a_j e^{-ikn}+(S_pa)_j e^{ikn}, n>=0, with n=0 the port. At n=1 it equals z times the port amplitude plus (z^{-1}−z)a_j. Substitution gives (1)-(2). The four internal-head map is T_int,p=P_int T_p. Port vertices are counted once, as n=0 on their leads.

These are amplitudes with equal lead flux because both leads have the same dispersion and velocity 2sin k. The old sectors share this same channel measure and velocity. No momentum or flux Jacobian is missing between sectors.

### Explicit center inverse bound

Let f=1/sqrt(8). At k0 the four-internal-vertex matrix K_p has outer diagonal d=f/4 at v,w. Eliminating them leaves the two-by-two matrix [[0,−p],[−p,0]] on A,B, whose inverse norm is 1. Each outer-to-inner elimination coefficient is c/d=2. The resulting K_p^{-1} has outer diagonal block bounded by d^{-1}+4, off-diagonal block norm <=2, and inner block norm <=1. Its norm is bounded by the norm of the real symmetric two-by-two comparison matrix

    [d^{-1}+4  2; 2  1],

which is at most its maximum row sum d^{-1}+6=8sqrt(2)+6<18. The block comparison follows by applying the triangle inequality to the norms of the outer and inner vector components; it does not depend on signs of p.

The port/internal coupling matrix C has orthogonal columns of squared norm (f/2)²+(3f)²=37/32, so ||C||<2. At k0 the port Schur matrix after outgoing lead elimination is

    [3p/4−i   5p/4; 5p/4   3p/4−i].

Its eigenvalues are 2p−i and −p/2−i, giving inverse norm 2/sqrt(5)<1. The full block inverse of F_p is the sum of the internal inverse block and a lifted Schur inverse. Consequently

    ||F_p(k0)^{-1}||
       <=18+(1+18*2)²<1400.                       (3)

For example the lifted part is [I;−K_p^{-1}C] times the Schur inverse times [I,−C†K_p^{-1}], whose two outside norms are each <=1+||K_p^{-1}C||. Thus (3) is a full six-dimensional norm bound, not just a port estimate.

### Pole-free interval and first derivatives

For real k, ||F_p(k)−F_p(k0)||<=3|k−k0|, since |E'|<=2 and |z'|=1. On the closed interval

    I={k: |k−pi/2|<=10^{-4}},

the Neumann product in (3) is <=0.42<1/2. Therefore uniformly for p=±1,

    ||F_p(k)^{-1}||<=2800.                         (4)

The internal K_p(k) separately remains invertible there: ||K_p(k)−K_p(k0)||<=2|k−k0| and ||K_p(k0)^{-1}||<18. Thus this interval is free both of the internal elimination poles and of full outgoing matching poles. No determinant sign is inferred only from numerical proximity.

With R_p=F_p^{-1}, one has R_p'=−R_p F_p'R_p and ||F_p'||<=3. It follows that

    ||R_p'||<=23,520,000,
    ||T_p||,||T_int,p||<=5600,
    ||T_p'||,||T_int,p'||,||S_p'||<=48,000,000.      (5)

Indeed differentiating (2) costs at most 2||R_p||+2||R_p'||<=47,045,600. The larger stated integer constant covers all three maps. All six core fields, including both ports, are included in T_p; no hidden internal mode is dropped. These constants are uniform on I and may be very far from sharp.

At any real k in I the stationary solution conserves probability current. Summing the finite-core stationary continuity equations leaves only the two lead currents, each 2sin k times incoming norm squared minus outgoing norm squared. Thus ||S_pa||=||a|| for all a, and the square two-by-two S_p is unitary. This can also be verified directly from F_p−F_p†=−2i sin k PP† and (2). Its norm is exactly 1, despite the coarse inverse bound.

The center source gives S_p(k0)=t_p X_ports, with t_p=−exp(−i theta)w_p. Therefore, on any narrower support |k−k0|<=h<=10^{-4},

    ||S_p(k)−t_p X_ports||<=48,000,000 h.          (6)

This is a full two-port column/operator bound, including reflection. It does not only compare transmission phases or probabilities. In particular sector-dependent delay is paid by (6) on a narrow band, rather than presumed equal.

### Exact packet normalization without a completeness assumption

For completeness, (1)-(5) support a normalized stationary-superposition interface. Let g be a C² compactly supported incoming two-port amplitude in the interior of I with integral ||g(k)||² dk=1. Form the lead fields

    psi_j(n,t)=1/sqrt(2pi) integral
        [e^{-ikn}g_j(k)+e^{ikn}(S_p(k)g(k))_j]
                         e^{-itE(k)} dk,

for n>=0, and use T_int,p(k)g(k) in the same integral for the four internal vertices. At n=0 formula (2) makes the port values exactly T_p g, so they are not independently added again. This superposition solves the bounded one-head Schrodinger equation of the infinite two-lead graph exactly. Smooth compact support and the analytic inverse on I justify differentiation; all fields are square summable for each finite t.

Here is a direct norm argument, rather than an assumption of scattering completeness. Extend g by zero to the full circle. Parseval makes the complete integer-lattice incoming Fourier sequence have norm 1. As t tends to minus infinity, its mass lies on n>=0: on the excluded negative indices the phase derivative has fixed sign and magnitude at least |n|+v_min|t|, where v_min=min_I 2sin k>0. One integration by parts with the compactly supported smooth amplitude bounds the corresponding squared tail by a constant times sum_{n>=0}(n+v_min|t|)^{-2}, which tends to zero. The outgoing sequence on n>=0 has the same nonstationary bound at negative times, with amplitude S_p g; (5) supplies its first derivative. Each of the four internal integrals tends to zero by one integration by parts in E(k), again because E'(k)>=v_min. Cross terms vanish by Cauchy-Schwarz.

Thus the full packet norm tends to 1 in the remote past. Its exact bounded selfadjoint evolution conserves norm, so it is exactly 1 at every finite time. At positive infinite time the same argument removes the incoming and internal pieces; the outgoing spectral amplitude is exactly S_p g. This constructs the needed packet and its asymptotic channel normalization without asserting that these packets span all states or that a local product seed has no bound-state component.

The argument extends to finite-dimensional coherent old-sector and passive-reference amplitudes using the same operator bounds. Infinite passive extensions follow by the norm bounds and finite-rank approximation. For arbitrary such normalized incoming amplitudes supported within h, (6) and Parseval give outgoing spectral L² error <=48,000,000 h against the common ideal amplitude

    −exp(−i theta) W X_ports g(k).

The comparator has norm 1 because W and X_ports are unitary. This is an asymptotic scattering-packet error statement, not a finite-time full-output bound against an already departed packet. No fixed-time internal tail constant or physical endpoint-source normalization has been imported.

### What remains before finite release

The explicit pole-free band and full internal first-derivative bounds now provide a conservative scattering interface. A finite product-seed theorem still needs a launcher with sufficient spectral weight in that band, an explicit vector comparison to the packet above, cut/return estimates, quantitative internal and source vacancy bounds at the chosen output interval, and the separately charged mediator/vacancy physical errors. A microscopic product input need not lie in this constructed continuum subspace. These obligations cannot be waived by perfect center transmission or by unitarity of S_p.

Only this note was written. The matrix bounds and packet norm argument were derived analytically with no scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication or delegation. Predecessor sources remain frozen. Distinct checking is required before promotion.
