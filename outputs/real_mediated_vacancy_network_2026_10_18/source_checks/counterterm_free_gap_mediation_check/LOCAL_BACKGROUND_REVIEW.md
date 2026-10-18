# Distinct check of the local-background sharpening

Disposition: **supported at the stated single-link, finite-network scope; no required correction found.** The full-space near-support norm can replace the full background norm in both dynamical estimates. Distant background terms and compensation remain in the target and physical inventory. This establishes no propagation, common outgoing state, gate or retention property.

Reviewed source: [LOCAL_BACKGROUND_SHARPENING.md](../counterterm_free_gap_mediation/LOCAL_BACKGROUND_SHARPENING.md), 8,466 bytes, 102 lines, SHA256 e18c49d6a664a382e26b7b658da4ed3bc593738ccd1806772254181c5d0d6f67, frozen by its author at 2026-10-18 10:54:36 UTC. I read the complete body before checking it. Its historical “pending distinct check” label is preserved.

## 1. Exposure and dependency boundary

ROOT proposed the locality route, and I received that proposal before reading this source. Another agent authored it. I authored the earlier NETWORK_NOTE.md exposition and exact-mediator publication appendix; I did not author this new locality proof. This is a source-exposed, same-model reconstruction with shared ancestors, not blind review or independent model-family evidence.

These unchanged pairs were fully read in preceding work. For this check I verified all six hashes and refreshed the polar-dressing passage and its review, the explicit vacancy rotation, and the complete network-interface source. Their spectral calculations are reused checked premises, not newly re-audited results.

| File | SHA256 |
|---|---|
| [EXACT_ALL_TIME.md](../counterterm_free_gap_mediation/EXACT_ALL_TIME.md) | 37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34 |
| [EXACT_ALL_TIME_REVIEW.md](EXACT_ALL_TIME_REVIEW.md) | 80c09db471dea4542ccfe9b236b91ccd2cd285502ce4b091d59cbcfbfa7e1e70 |
| [VACANCY_HOPPING_PROBE.md](../counterterm_free_gap_mediation/VACANCY_HOPPING_PROBE.md) | 7ce327a279b7c89e6ee48dd94555a78bdb357dd183b4333618f958e4d387da00 |
| [VACANCY_HOPPING_REVIEW.md](VACANCY_HOPPING_REVIEW.md) | f1e754ed52ccb2ea27c3831659467a3f94f51d8ce75b26c8b7ce882a4b7e9df3 |
| [NETWORK_VACANCY_INTERFACE.md](../counterterm_free_gap_mediation/NETWORK_VACANCY_INTERFACE.md) | de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e |
| [NETWORK_VACANCY_REVIEW.md](NETWORK_VACANCY_REVIEW.md) | 88169175decc90a4f706ea3a1168ae54bf763e5a0cb5d3cb516b749fd65b9066 |

The operative imports are the local exact mediator dressing at distance at most \(82\lambda\), the explicit vacancy dressing at distance at most \(1/U\), and the specified positive inventory. ROOT reports these predecessor pairs accepted at bounded scope. No audit status, native realization or multi-link result is imported.

## 2. Exact support and comparison lemma

On the five-qubit device the predecessor constructs a particular polar unitary V satisfying

\[
H_{\rm med}=c_{\rm eff}I+V H_{\rm eff}V^\dagger,\quad
H_{\rm eff}=K-b_{\rm eff}X_1X_2Y_aY_b+2a_{\rm eff}n_m,\quad
\|V-I\|\le82\lambda .
\]

Extend this V by identity on all other clocks and passive references. Spectator degeneracies do not require choosing new global eigenvectors. The exact identity and norm bound persist.

The vacancy rotation D acts only on old1, old2, a, b. In the old \(X_1X_2=p\) even-pair sector it is

\[
D_p=\begin{pmatrix}\cos\alpha&p\sin\alpha\\-p\sin\alpha&\cos\alpha\end{pmatrix},
\quad \alpha=\arctan r,\quad
r=\frac{2}{\sqrt{U^2+4}+U}\le U^{-1}.
\]

It is identity on the pair one-head sector and \(\|D-I\|\le U^{-1}\). Any clock-only block supported away from a,b therefore commutes with both dressings on the full occupation space. So does \(B_{\rm comp}=r\sum_{j\notin\{a,b\}}n_j\). A block also acting on an old qubit or m would not satisfy this conclusion merely by avoiding a,b; that inventory is excluded.

For clarity, let W be unitary, A selfadjoint and c real. Suppose \(H=cI+WAW^\dagger\), with added selfadjoint \(C=C_n+C_f\) and \([W,C_f]=0\). Then

\[
\begin{aligned}
H+C&=cI+W(A+W^\dagger CW)W^\dagger,\\
\|W^\dagger CW-C\|
&=\|W^\dagger C_nW-C_n\|
\le2\|W-I\|\|C_n\|,\\
\|e^{-it(H+C)}-e^{-itc}e^{-it(A+C)}\|
&\le2\|W-I\|(1+|t|\|C_n\|).
\end{aligned}
\]

The last line pays two outside W factors and Duhamel. All intermediate propagators have norm one. No commutation between near and far parts, separate number conservation, or bound on the far norm is used. In particular, a large common far Hamiltonian does not multiply the perturbation norm.

The split uses the actual listed supports: a block touching a or b belongs wholly to the near part, including identity terms. Thus \(M=\|B_{\rm near}\|\) can be bounded by the sum of full norms of listed blocks incident to the union of a,b, each counted once. No one-head compression replaces this norm.

## 3. Both stages and complete target

For the mediator stage set

\[
C_n=b_{\rm eff}(U n_an_b+B_{\rm near}),\qquad
C_f=b_{\rm eff}(B_{\rm far}+B_{\rm comp}).
\]

Then \(\|C_n\|\le b_{\rm eff}(U+M)\), and with \(s=b_{\rm eff}t\) the lemma gives

\[
E_{\rm med}(s)\le164\lambda[1+|s|(U+M)].
\]

The comparator retains the entire far background, compensation and repulsion. Its scalar is \(c_{\rm eff}\); mediator aging is \(2a_{\rm eff}\). Neither the bare gap four nor \(\lambda^2\) can replace the exact effective quantities.

For the vacancy stage use the inherited exact identity

\[
UP_{11}-X_1X_2Y_aY_b=D H_{\rm diag}D^\dagger,\qquad
H_{\rm diag}=-X_1X_2J_{ab}-rP_{00}+(U+r)P_{11}.
\]

Only \(B_{\rm near}\) changes under D, so

\[
E_{\rm vac}(s)\le\frac2U(1+|s|M).
\]

Both comparisons hold on the full space before input restriction. The triangle inequality therefore gives

\[
E(s)=164\lambda[1+|s|(U+M)]+\frac2U(1+|s|M).
\]

There is no uncharged restriction of an intermediate actual state. Actual pair-created extra heads are included.

Let \(P_1\) be the global one-head projector. Total \([B,N]=0\) suffices: \(H_{\rm diag}+B+B_{\rm comp}\) preserves \(P_1\), even if the near and far parts separately do not. On that sector,

\[
P_{11}=0,\quad P_{00}=I-n_a-n_b,\quad
B_{\rm comp}=r(I-n_a-n_b).
\]

The complete vacancy shift cancels, leaving \(H_1=-X_1X_2J_{ab}+B|_{P_1}\). There is no residual global vacancy phase. Without compensation retain \(H_1-rI+r(n_a+n_b)\); the same error bound holds but that relative onsite shift cannot be discarded.

Because \(K=2I+Z_1Z_2\) commutes with \(X_1X_2\) and clock-only B, the complete target on the initial \(P_1\) domain is

\[
e^{-itc_{\rm eff}}e^{-itK}e^{-isH_1}
\otimes e^{-it2a_{\rm eff}n_m}.
\]

The \(2I\) in K and all scalars in B remain. This is an isometry into the full physical output, with no final projection or normalization. Arbitrary old/clock/mediator correlations within the initial one-head domain and arbitrary passive extensions are permitted. Factorization of the target operator does not turn correlated inputs into product outputs. No common head profile or mediator reset follows.

## 4. Error budget and actual hardware

For \(S\ge0\), \(0<\epsilon\le1\), choose

\[
U\ge8(1+SM)/\epsilon,\qquad
0<\lambda\le\min\{10^{-3},\epsilon/[656(1+S(U+M))]\}.
\]

Uniformly over \(|s|\le S\), the vacancy term is at most \(\epsilon/4\), and the mediator term is at most \((164/656)\epsilon=\epsilon/4\). Thus the complete isometry error is at most \(\epsilon/2\). The two-isometry inequality gives unhalved complete channel distance at most \(\epsilon\), including mixed inputs and references.

The counts remain \(L+3\) qubits and \(5+1+q+(L-2)=L+4+q\) listed positive blocks with compensation; without it there are \(6+q\) blocks. For \(L=2\) compensation is empty and both counts agree. Repeated supports remain separately charged.

Put \(k_v=\sum_{\ell\ni v}\|B_\ell\|\), \(K_{\rm load}=\max_vk_v\). The actual loads are old1 \(3+2\lambda+2g\), old2 \(3+2\lambda\), mediator \(4+2g\), clock endpoint \(2\lambda+b_{\rm eff}(U+k_v)\), and outside clock \(b_{\rm eff}k_v+b_{\rm eff}r\) when compensated. Without compensation omit its last term.

Using \(g<3\lambda\) and \(b_{\rm eff}\le\lambda^2\), every load is at most

\[
4+8\lambda+\lambda^2C_{\rm load},\qquad
C_{\rm load}=U+K_{\rm load}+r.
\]

For \(\Lambda>4\), the further bounds

\[
\lambda\le(\Lambda-4)/16,\qquad
\lambda\le\sqrt{(\Lambda-4)/(2C_{\rm load})}
\]

give at most \((\Lambda-4)/2\) from each nonconstant contribution, hence load at most \(\Lambda\). The conditions are simultaneously feasible for a specified finite inventory: choose U, then positive \(\lambda\) below every bound. They do not supply coefficients or an embedding.

The compensation norm \(r(L-2)\) is extensive. It disappears from this dynamical estimate because of exact commutation, while all \(L-2\) onsite blocks and their local loads remain. Remote incident weights likewise remain in \(K_{\rm load}\).

## 5. Challenges and scope

I checked the possible failure points directly. Overlap of near and far blocks at an outside site can make them noncommuting, but the proof never factors their evolutions. Large far norms remain common terms in the compared generators. The dressings need not conserve total head number: the comparison is full-space, and only the final invariant comparison domain is restricted. Total number conservation of B is required for the stated one-head target, although the full-space norm comparisons themselves need no such restriction.

The boundary cases \(S=0\), \(M=0\), and \(L=2\) create no singular prescription or missing compensation term. The sufficient bounds are allowed to be loose there. Blocks on old or mediator sites, nonlocal blocks presented as local, and compressed norms substituted for M are excluded. The result holds for each finite network; it establishes no infinite-volume dynamics or interchange of limits.

The claimed improvement is therefore valid: distant arm length need not enter this particular dynamical error when the near inventory and local cap remain fixed. Propagation, a common output, boundary-return control, multiple mediated links sharing the old gap, a gate, capture and permanent halt remain separate obligations. No generic matrix-error tolerance or native preparation/calibration result is established.

## 6. Verification record

The check reconstructed the support commutators, two-endpoint Duhamel estimate, invariant-sector restriction, phases, arithmetic allocations, counts and actual loads. No numerical solver, scientific executable, parameter scan, external search, delegation or model override was used. Python standard-library reads and hashes checked identities; the final review was read back completely.

Only this new LOCAL_BACKGROUND_REVIEW.md was written. The frozen NETWORK_NOTE.md, predecessor sources/reviews, canonical files, Git, checkpoints and editable prompts remain unchanged. This is bounded mathematical review, not retained certification or authorization to publish.
