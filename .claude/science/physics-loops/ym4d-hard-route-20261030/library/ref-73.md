# Reference-torus inputs to Proposition 7.3 (row 168)
Provenance: Codex (GPT-6; exact serving ID unavailable), max effort requested (runtime setting unavailable); checkout `6b9d348b8132e27a5a927a94c4af2452ac64abb7`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

## 1. Scope and sources

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. `SA` means their `YM4_sketch_500.tex` at the pinned commit. Balaban's papers are credited where used.

The target is `tu10.md` Section 4, for T0 nodes F2, S15 and S16. The order is (a) exact sourced representation, (b) positive reference estimate, (c) source normalization, then (d) common-normalizer transfer. The first failed proof obligation stops this attempt.

Input (a) concerns SA's law on history classes, block fields and stored fields. The elementary Wilson identity on bare fields cannot replace that law in the later estimates. Source identities, positivity and differentiation must hold for the same representation.

## 2. Input (a): finite transport and differentiation

Fix a finite reference torus, cutoff and frozen run. Set \(X_i=\mathcal O(f_i)\), \(B_i=\sup_U|X_i(U)|<\infty\). Finiteness follows because the Wilson observable sums finitely many bounded plaquette functions. The unsourced Wilson density \(\rho_0\) is continuous and strictly positive on a compact product of groups. Put \(Z(z)=\int e^{z_1X_1+z_2X_2}\rho_0\,dU\). Then \(0<Z(0)<\infty\); write \(\mu\) for its normalization.

SA 17499–17517 and 22562–22576 define transport by source-independent positive kernels. Their finite normalization can be checked directly. A test splits mass through \(\chi+(1-\chi)=1\). A map uses a Dirac measure. A gauge draw uses a normalized probability measure. Deleting a variable takes a marginal. A reference replacement draws \(r(v)\,dv/\int r\); an invalid denominator takes the prescribed drop-out branch. Each move has total mass one after summing its outcomes. Induction on the finite number of moves gives a kernel \(K(U,dy)\) of mass one. Here \(y=([h],V,\xi)\) keeps precisely the standing class and its retained fields. Grouping classes and forgetting other variables also preserve mass.

Balaban, CMP **119** (1988), Section 3, uses the finite test partitions underlying these moves. The partition identity is rebuilt here: expanding \(\prod_C[\chi_C+(1-\chi_C)]\) gives one term for each outcome and sums to one. No stability theorem from that paper is used. This argument applies to the total kernels as defined. It does not prove that an RG formula with localized activities equals their output.

Define measures on these same retained variables by
\[
 P(dy)=\int\mu(dU)K(U,dy),\qquad
 M_z(dy)=\int e^{z_1X_1+z_2X_2}\mu(dU)K(U,dy).
\tag{1}
\]
For a multi-index \(\alpha\), the signed moment measure
\(\int X^\alpha\mu(dU)K(U,dy)\) has total variation at most \(B^\alpha P\). Its Radon–Nikodym density \(q_\alpha\) therefore satisfies \(|q_\alpha|\le B^\alpha\), with \(q_0=1\). Choose these versions outside one common null set. The countable power series
\[
 G_z=\sum_\alpha\frac{z^\alpha q_\alpha}{\alpha!},\qquad
 \|G_z-1\|_{L^\infty(P)}\le e^{B_1|z_1|+B_2|z_2|}-1
\tag{2}
\]
converges in \(L^\infty(P)\), uniformly on compact source sets. Integrating its absolutely convergent series shows \(M_z=G_zP\).

On \(B_1|z_1|+B_2|z_2|<1/4\), the last bound is less than \(1/3\). Indeed, \(e^{1/4}\le\sum_{n\ge0}4^{-n}=4/3\). The logarithm series defines \(\Phi=\log G_z\), with \(\Phi(0)=0\), uniformly in \(L^\infty(P)\). Hence
\[
 \frac{Z(z)}{Z(0)}=\int M_z=\mathbb E_Pe^{\Phi(z)},\qquad
 S^T_{2,*}(f_1,f_2)=\operatorname{Cov}_P(\Phi_1,\Phi_2)+\mathbb E_P\Phi_{12}.
\tag{3}
\]
All differentiations follow from the uniformly convergent series. Explicitly,
\(\Phi_i=q_{e_i}\) and \(\Phi_{12}=q_{(1,1)}-q_{(1,0)}q_{(0,1)}\). Substitution gives \(\mathbb E_\mu X_1X_2-\mathbb E_\mu X_1\mathbb E_\mu X_2\), as required.

This proves the finite identity at every defined frozen level, including \(k_0\) and \(k_1\). It needs neither D1 nor a uniform partition floor. Its source radius may shrink with the cutoff. Identifying \(\Phi\) with SA's localized sourced exponent requires the exact presentation in 4.6 and 2.11. That further input is not supplied by (1)–(3).

## 3. First unproved step: the exponent required in (a)

**The exact transport identity survives. Its identification with the exponent used at SA 26094 remains open.** This is the stopping point. It is a gap, not a refutation of the Wilson identity.

Write \(\widehat\tau^z_{[h]}\) for the unnormalized transported measure on \((V,\xi)\), after grouping the histories. The missing statement is
\[
 \widehat\tau^z_{[h]}(dV,d\xi)
   =e^{\mathcal F_{[h]}(z,V,\xi)}m_{[h]}(dV,d\xi),
 \qquad m_{[h]}\ge0\text{ independent of }z,
\tag{4}
\]
where \(\mathcal F\) is **the formed exponent of 4.6**, with its specified regular, pointed and live terms. It cannot be an arbitrary logarithm. Equation (4) must hold for the actual retained variables and the sourced moves, on the asserted analytic domains.

If (4) holds, its normalized density ratio equals \(G_z\) from (2). A countable dense source set and holomorphy give equality outside one common \(P\)-null set. Both logarithms vanish at zero. Their difference is continuous and takes values in \(2\pi i\mathbb Z\), so it vanishes near zero. Thus \(\mathcal F(z)-\mathcal F(0)=\Phi(z)\), and (3) applies to precisely SA's derivatives. This proves the remaining identification **conditional on (4)**.

But the kernel argument does not prove (4). It gives only
\[
 \Phi_i=\mathbb E[X_i\mid y],\qquad
 \Phi_{12}=\operatorname{Cov}(X_1,X_2\mid y).
\tag{5}
\]
Conditioning in (5) uses the joint law \(\mu(dU)K(U,dy)\). These functions have no established local activity decomposition or cutoff-uniform source bounds. Their elementary bounds involve \(B_i\), not \(x^{-1}\). Replacing SA's exponent by this logarithm would therefore leave its subsequent estimates unjustified.

SA 22879 invokes the holomorphic one-step theorem 1.6 and the large-field operations to establish the sourced format. SA 19443 requires exact preservation of the presentation, separately for every standing part. The checked partial notes below do not establish that sourced preservation. D1's upper bound also cannot establish equality of measures in (4).

Balaban's CMP **119**, Theorem 1, states preservation of its inductive class for its run. Its Section 3 supplies the test partitions rebuilt above. Importing its full induction would require a proof and a match to these sourced, resummed histories. Neither is supplied here. No Balaban estimate is counted as proved by citation.

## 4. Dependency record at the stop

The later entries are an inventory, not further proof attempts. Paths are relative to this loop folder.

| Requested input | Checked pieces and remaining obligation |
|---|---|
| **(a), D1's source-format prerequisites** | `library/sa-2.13.md` and `sa-2.13-2.md` supply conditional denominator, reserve, chart and source-domination lemmas. Claude checked them in `library/pre-213.md` Section 1; its final paragraph leaves the actual-operation premises open. `gates/ref-chart-regate.md` checks the reference chart under its named premises, but leaves the complete prepared/inner/activity comparison open. The new prepared comparison in `pre-213.md` is not yet checked. These pieces do not supply (4), 2.10's sourced healed sum, or the complete holomorphic step. |
| **(b), live terms: 4.14 at SA 26103–26117** | Required: the weighted lineage tail for the same class marginal, including \(\sum_a L^{8a}\tilde\nu(\mathfrak{lv}^{\ge a}_{k}(\mathfrak c))\). No checked producer was identified. `t0-skeleton.md` Section 3.6 leaves 4.14 and D3 open. A bound for creation alone would not supply this age sum. |
| **(b), interacting Gaussian comparison: SA 26156–26165** | `library/flat-port.md`, checked by Claude in `gates/flat-port-gate.md`, supplies linear estimates at the trivial background. It does not compare the interacting fluctuation integral with that Gaussian. SA 28205 explicitly retains the complete-force term involving old activities and exterior data. No checked bound for that term was identified. Thus no positive \(c_{\rm ref}x^{-2}A\) lower bound, or matching upper bound, is established here. |
| **(c), Lemma 7.2** | Its source-normalization bounds require the formed source slopes in 4b, SA 22879–22888. E1's drift bounds do not control those derivatives. No checked producer was identified. `tu10.md` Section 4 already leaves this input open. |
| **(d), ET5 and translations** | D1, chessboard domination, and compatible source and vacuum terms are still required. ET8–ET10, SA 26872–26931, add the nonwrapping companion assumptions. `gates/uv-ct-upper-chain-41489e4876.md` checks a conditional interface and leaves UV-CT open; it does not prove D1 or ET5. `tu10.md` proves only the transfer arithmetic from a common normalizer and joint translation invariance. Neither premise is established here. |

For (d), the finite Wilson reference is invariant under lattice translations: relabeling bonds preserves Haar measure and the action. The same invariance must hold for the periodic state before their covariance difference \(D\) is jointly invariant. SA 3170–3176 obtains it from site and link reflections; their composition is a unit translation. That all-state reflection input must be supplied. A state's unspecified period alone is insufficient.

## Result

The finite probability identity and differentiation are proved by hand for the frozen total kernels. The first unproved step is **(a)'s identification with the localized sourced exponent used in Proposition 7.3**, equation (4). The attempt stops there. Inputs (b)–(d), the coarse positive reference estimate and TU10 remain open. No Wilson counterexample is claimed. The new finite argument has not been checked by another model; this note grants no status.
