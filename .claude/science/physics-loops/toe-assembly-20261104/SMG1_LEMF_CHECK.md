# SMG1 referee closure Lemma F: one check

Checker: Codex gpt-6-astra, reasoning effort low, read-only, laptop, 2026-11-07 (run log ~/toe-lap/prior/check_lemF.log). One check of one proof: SMG1_REFEREE.md Lemma F. The lead (Claude Opus 5.5) copied the checker's final message below unchanged.

Lemma F proves its precise statement: \(1\in\sigma(U|_{H_1})\). Infinite volume and \(H_1\ne\{0\}\) are already explicit hypotheses. Nontrivial local dynamics is unnecessary.

| # | Step | Assessment |
|---|---|---|
| 1 | Setting: local invariant-even algebra is dense; disjoint elements commute. | **CORRECT.** Local gauge averaging preserves locality in this carrier. Taking the even part preserves gauge invariance. Even CAR elements on disjoint supports commute. |
| 2 | H1 follows from NN-a. | **CORRECT.** Fixed finite depth gives finite propagation. Even gates preserve parity. Gauge invariance of the **complete update** preserves the invariant algebra. Individual gates need not be gauge invariant. |
| 3 | Construct \(U\), fix \(\Omega\), and reduce to \(H_1\). | **CORRECT.** Stationarity gives an isometry on GNS vectors. Surjectivity follows from \(\alpha(\mathfrak B^+)=\mathfrak B^+\). Thus \(U\) is unitary and \(\Omega^\perp\) reduces it. |
| 4 | Proof Step 1: choose \(z,\xi,A,B\). | **CORRECT.** Nonzero \(H_1\) gives nonempty spectrum. Unitarity gives approximate eigenvectors. Density and centering give the stated \(3\varepsilon\) bound. H1 makes \(B=\alpha(A)\) local and invariant-even. |
| 5 | Step 2: translate and multiply approximate excitations. | **CORRECT.** Covariance gives \(\alpha(A_n)=B_n\). Infinite lattice translations allow arbitrarily separated copies. Separate translates of the **union** of the supports of \(A\) and \(B\). |
| 6 | Step 2: obtain product expectations from clustering. | **CORRECT.** Each previously chosen \(P_m(D)\) is local. H3 applies to it and the next copy. Translation invariance supplies identical single-copy expectations. Pairwise clustering suffices by this sequential construction. Evenness gives the three product identities. The stated induction bound is generous but valid. |
| 7 | Step 3: compute the residual at \(z^n\). | **CORRECT.** With the inner product linear in its second argument, \(zw=a(1+\rho)\). Cauchy–Schwarz gives \(|\rho|<4\varepsilon\). The cross-term sign, conjugation, and \(4n\delta\) error bound are correct. |
| 8 | Step 3: project off \(\Omega\) and normalize. | **CORRECT.** Clustering makes the vacuum overlap small while the norm approaches \(a^{n/2}>0\). For each fixed \(n\), first choose small \(\varepsilon\), then choose \(\delta\) depending on the resulting \(A,B\). This is the precise quantifier reading of the limit sentence. It proves \(z^n\in\sigma(U|_{H_1})\). |
| 9 | Step 4: positive powers approach \(1\). | **CORRECT.** The circle pigeonhole argument gives positive integers \(m\) with \(|z^m-1|\le2\pi/N\). Step 3 and closedness of the spectrum finish the proof. |
| 10 | Corollary: extend to the invariant sector and full GNS space. | **CORRECT.** \(H_1\) is a reducing subspace of both vacuum-orthogonal spaces. Its spectrum is therefore contained in theirs. Gauge invariance or purity of the state is not additionally needed. |

The gap notion must be stated precisely: some neighbourhood of \(1\) contains **no spectrum of \(U|_{\Omega^\perp}\)**. This is the referee’s operative definition. Lemma F excludes that gap. It does **not** prove that \(1\) is non-isolated, or exclude a gap after removing the entire fixed-vector space. For the identity tick, \(U|_{H_1}=1\); the lemma holds entirely through static vectors.

This differs from SMG1’s R-GEN energy gap and from LZ1’s bands, nodes, and propagating species. D1 alone supplies neither clustering nor nonzero \(H_1\). Finite rings and segments fall outside H2; arbitrary numbers of separated copies are essential.

Read-only check completed. No files changed. No git commands ran.

VERDICT: Lemma F holds