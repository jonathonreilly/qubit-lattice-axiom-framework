# Primary literature and model matching for the sea construction

Fresh access: 2026-10-29. Complete external PDFs and extracted pages are
cached only in `/private/tmp/source-sea-literature`, excluded from repository
packaging. This ledger contains original short summaries, no paper copies.

| Block | Exact source and read coverage | Reuse and hypothesis match |
|---|---|---|
| Algebraic reflection positivity and chessboard | Fröhlich–Israel–Lieb–Simon, *Phase transitions and reflection positivity I*, Commun. Math. Phys. **62** (1978), 1–34; [original PDF](https://math.caltech.edu/SimonPapers/93.pdf), [DOI](https://doi.org/10.1007/BF01940327). Read printed pp.5–6, Theorems 2.1–2.3; pp.19–21, Theorems 4.1–4.3 and their algebraic proof. | Theorem 4.3 is the site-plane chessboard result. The present gauge model supplies its own positive reflection form by conditioning on shared boundary links. This step must also hold for every real nonnegative cell penalty. No statement about fixed coarse V is imported. |
| Closed-cell theorem with arbitrary even side | Marek Biskup, *Reflection positivity and phase transitions in lattice spin models*, [arXiv:math-ph/0610025v2](https://arxiv.org/pdf/math-ph/0610025v2). Read printed pp.38–40, Definition 5.1, Lemma 5.2 and Corollary 5.4; pp.44–46, closed-block convention, Theorem 5.8, equations (5.34)–(5.35), full maximizer/run argument; p.47, Lemma 5.9. | Closed blocks may share boundary variables; L/B is even. The proof uses the reflection-positive block algebras and translations, so it applies to cell link algebras after the separate reflection verification. The original-cell event is invariant under the reflected placements. No dyadic-size restriction is added. |
| Proposed next localization theorem | J. Dimock, *The Renormalization Group According to Balaban II. Large Fields*, [arXiv:1212.5562v2](https://arxiv.org/pdf/1212.5562v2), fresh parsed access to printed pp.70 and91–92: Lemma 3.18 with (503)–(506), Appendix F Theorem F.1, (633)–(638) and proof continuation. | F.1 assumes independent fluctuation variables under an ultralocal probability law, a local interaction and a uniform small interaction bound on its support. The actual all-cut gauge sea has not been converted into this input. This is a reusable consumer, not a missing covariance theorem or proof of its hypotheses. |
| Constrained covariance and independent variables | J. Dimock, *Covariant Axial Gauge*, [arXiv:1410.2798v3](https://arxiv.org/pdf/1410.2798v3). Read printed pp.14–21: coercivity proof ending (99), §3.7, (100)–(109); §3.8, (110)–(140); §3.9, (141)–(150); §3.10, (151)–(152). Initially inspected v1, then selected and checked v3 after reading the version history. | Local coordinates C solve QZ=0 and tau Z=0; the covariance is `(C^T Delta_k C)^-1`, distinct from the minimizer. Propositions7–8 give constrained resolvent representations and the square-root integral; (152) uses independent unit Gaussians. This is abelian with exact linear constraints. Our soft SU(N) kernel, gauge slice, background, holes and nonlinear/source remainder still need an exact dictionary. No automatic four-dimensional extension or soft-kernel identification is imported. |

The imported classical statements above are established results. The
penalty-independent cap estimate, infinite-penalty reference limit, actual
joint kernel refinement and original-source budget are proved in the owned
note. Their application is the contribution here, not a claim to a new
generic chessboard theorem.

## Existing lane results deliberately reused

The frozen predecessor review's [literature ledger](review_source_history_literature.md)
and full review were read. They establish the scope of Fernández–Procacci,
`math-ph/0605041v2`, Theorem 1, for the already constructed successful
pointwise gas. It does not localize a correlated outer average. Their
Balaban CMP122 coverage explicitly retains the small-effective-coupling
hypothesis; no conclusion here imports that hypothesis as proved.

`PROOF.md`, lines4066–4143, already contains the unpenalized closed-cell
Wilson chessboard estimate and first-step ribbon route. `RLARGE.md`,
lines965–1027, supplies the normalized soft-kernel cap/tail argument.
`HW.md`, lines90–130, supplies the probability/reference distinction.
`REVIEW_RLARGE_V2.md`, lines105–220, warns against multiplying probabilities
under different laws and promoting a fully averaged bound to fixed V.
`SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md` and its independent review supply
the actual joint replacement identity, failures and counterexample.

Scoped current-main searches used immutable revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`. The native Majorana flux
discussion in `docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md`,
lines420–480, concerns another density and an unconditional chessboard
bound. It does not supply the present gauge penalty-family normalization.
Narrow searches for penalty/reflection, tilted/chessboard and
exact-bad/all-good reference statements found no equivalent producer in
the scoped lane/current-main files. This is not an exhaustive novelty claim.

## Access and search audit

Fresh searches combined Wilson gauge, weak coupling, large fields,
reflection positivity and chessboard; then exact FILS/Biskup/Dimock titles
and identifiers. The original FILS journal text and versioned arXiv PDFs
were preferred to tertiary summaries. Abstract-only or unrelated purported
Yang–Mills proofs were not used.

Python `requests` was unavailable in the first fetch attempt; urllib had a
certificate-verification failure. `curl` fetched the versioned Biskup PDF.
The `www.math.caltech.edu` hostname failed certificate matching; the
original `math.caltech.edu` URL succeeded. `pdftotext` was absent; `pypdf`
successfully extracted the stated locally cached pages. The FILS displayed
formula has imperfect OCR; Biskup's clean rendering and full proof were
used for the explicit inequality. These access failures are not evidence
against the scientific statements and are retained in the fetch record.
PDF SHA-256 values, URLs and repository input hashes are in the manifest.

Fresh attempted access to Balaban CMP95, DOI `10.1007/BF01215753`, and
CMP99, DOI `10.1007/BF01240355`, returned publisher abstracts/paywall pages;
a Project Euclid request failed. Those are discovery pointers only, with no
theorem imported from these unread full papers. The subsequently obtained
versioned Dimock covariance text supplies the explicit readable route above.

No new title is cited from a search snippet alone. No external theorem is
claimed to establish four-dimensional continuum existence, scale-uniform
coupling control or a physical mass gap in this unit.
