# Primary-literature applicability record

Reviewer: separate-context Astra/max, 2026-10-29. This is a scoped search for
the actual hard-history/source-return unit. A primary theorem is reusable only
after its hypotheses are matched; neither a title nor a generic cluster theorem
supplies an actual gauge-field activity estimate. The search is not exhaustive.

| Proof block | Primary source and exact read scope | Applicability and remaining work |
| --- | --- | --- |
| H21–H25, complex pointwise gas | [Fernández–Procacci, arXiv:math-ph/0605041v2](https://arxiv.org/html/math-ph/0605041v2), §2 (2.1)–(2.15), §3 Theorem 1 (3.1)–(3.3) | Directly reusable. The polymer set is the finite set of G2-connected Y; self-incompatibility and pair incompatibility mean overlapping A(Y). Set the paper's nonnegative majorant to `rho_Y=sup|a_Y| exp(mu|A(Y)|)` and its comparison variable to `nu_Y=rho_Y exp(|A(Y)|)`. H22 gives `sum_incompatible nu_Z <= d_q|A(Y)| <= |A(Y)|`, the KP subcriterion of their stronger theorem. It yields the all-order pinned absolute majorant for complex activities. This imports combinatorics only; H15–H20 must still produce rho from the actual Wilson/normalized-soft density. |
| Improved convergence criteria | [Jansen–Kolesnikov, arXiv:2112.13134v3](https://arxiv.org/html/2112.13134v3), §2.1 Theorem 2.1, Remark 2.1, Corollaries 2.2–2.3; §2.2 Proposition 2.4 | Theorem 2.1 requires a nonnegative family satisfying explicit sign-flipped Kirkwood–Salsburg inequalities. Nonnegative pair potentials give necessity as well as sufficiency. Remark 2.1 permits complex activities through absolute majorants. For this gas the hard-core potential is nonnegative, and Corollary 2.2 with stability constant zero is already met by H22. Proposition 2.4 can improve a supplied activity budget; it cannot generate a bound on f_Y or establish sea mixing. There is no reason to replace an adequate H21 bound merely to optimize constants. |
| Fixed holes, H26–H27, possible future sea expansion | [Dimock, arXiv:1212.5562v2](https://arxiv.org/html/1212.5562v2), introduction (1)–(12), §3.3 Theorem 3.1 and (199)–(214), §3.14 Lemmas 3.18–3.21, Appendix F Theorem F.1 and proof (633)–(646) | F.1 assumes an **ultralocal probability measure**, fields independent at distinct sites, local interactions bounded by `H_0 exp(-kappa d_M(X mod holes))`, small H_0, and `kappa>=3kappa_0+3`. It produces localized logarithms and local influence; the latter gives boundary cancellation. This is a concrete construction worth reusing after localization. The encompassing model is scalar phi-four in three dimensions, with chosen mass/energy counterterms, large L,M and small running coupling. The current gauge cut sea is not shown to be ultralocal or to have the required small localized interactions. Its failure families cannot be silently treated as fixed holes. |
| Multilevel actual gauge densities | [Balaban, CMP119 (1988)243–285, DOI](https://doi.org/10.1007/BF01217741), [original scanned paper](https://scispace.com/pdf/convergent-renormalization-expansions-for-lattice-gauge-29jyexd38e.pdf), printed243–244,260–263, especially (0.1), (2.40)–(2.42), Theorem 1 | The transformation (0.1) is a hard group-delta block constraint. A separate R operation changes the large-field part. Theorem 1 assumes the specified recursive coupling sequence and inequalities imported from Part I, all its constant restrictions, and the full inductive density structure. The localized boundary terms have specified regularity/analyticity domains. The source's soft normalized S4′ kernel, raw one-generation cut reference, and minimum-defined selector have not been identified with this RT transformation. The inspected statement is a useful target architecture, not a verified import. The entire upstream theorem chain was not read or validated here. |
| Large-field normalization and return | [Balaban, CMP122 (1989)355–392, DOI](https://doi.org/10.1007/BF01238433), [original scanned paper](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf), printed355–356 and388–391, Theorem 1, (1.90)–(1.103) | Theorem 1 assumes every effective coupling lies in `(0,gamma]` for sufficiently small gamma; the following paragraph explicitly retains this hypothesis because its proposed removal relied on an unpublished perturbative proof. The conclusion is the inductive density package of CMP119 §2 and ultraviolet stability. The later return constructs activities, bounds them before exponentiation, and allocates the resulting terms to bulk or large-field boundary contributions. The normalized operations mentioned in (1.103) are particular operators from that construction. They are not identified with H6/H8 by their names. Useful lesson: localize and pay the new large-field boundary contributions before exponentiating them. No soft-kernel/sea theorem is imported. |
| Localization before cluster expansion | [Balaban, CMP116 (1988)1–22, DOI](https://doi.org/10.1007/BF01239022), [original scanned paper](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), printed1–2 only | The introduction separates localization of the small-field fluctuation action, using propagator/minimizer random-walk expansions, from exponentiation of the resulting local integral. This supports a concrete next construction, not an unproved transfer of its estimates. The body and complete theorem hypotheses of this paper were not read, so no theorem import is claimed. |

Recent candidate checked independently: [Faizal–Shabir, arXiv:2606.19362v1](https://arxiv.org/pdf/2606.19362v1).
In attached Part III, printed34 (one-based PDF399), Lemma5.2 uses (5.28), an
unrestricted Haar integral bounded by `exp(-c1 lambda+c2)` for large lambda.
Its Appendix A.3, printed86–87 (PDF451–452), assumes a similar all-field
Laplace bound (A.19). The polynomial Haar-cap lower bound below rejects this
proposed import. This is a finding about these equations, not a review of all
593 pages or a global verdict on any proof route.

For SU(2), write `delta(U)=||I-U||_F^2/2=||I-U||op^2`.
On the ball of operator radius `lambda^(-1/2)`, the specified phi is linear,
so the integrand is at least `exp(-1)`. Haar radial density is
`(2/pi)sin(theta)^2 dtheta`; hence for lambda>=1 the integral is at least
`exp(-1)/(6 pi) lambda^(-3/2)`. This contradicts every fixed positive
exponential rate as lambda grows. For a fixed finite Wilson lattice the
corresponding all-links-near-identity cap also has polynomial mass. A genuine
fixed-threshold bad-set indicator instead permits an exponential penalty.
[Independent diagnostic](review_source_history_literature_laplace.py) and
[output](review_source_history_literature_laplace_attempt01.json) check that distinction.

Searches on 2026-10-29 included Balaban large-field renormalization, complex
polymer convergence, conditioning/cluster expansions, and arXiv Yang–Mills
weak-coupling/large-field/cluster work with 2024–2026 qualifiers. The newer
Nair arXiv:2608.10133 result was screened only at its abstract/title: it is
three-dimensional, and no import or theorem verdict is made. No search result
establishes that relevant work does not exist. The current reusable import is
the abstract successful-gas theorem; a gauge-specific producer for the outer
sea/failure expression remains required.

Access honesty: the arXiv HTML statements above were read directly. Balaban
statements were read from the web tool's parsed original scanned PDFs, not
SciSpace AI summaries. Some mathematical OCR in those scans is degraded;
unreadable constants were not reconstructed or certified. DOI/Springer access
failed, the first UCLA KP mirror returned404, and direct curl attempts on the
Balaban mirrors returned HTML or a CloudFront error PDF. Those hashes in the
[fetch record](review_source_history_literature_fetches.json) are explicitly
**not** paper hashes. The recent arXiv PDF was fetched in memory and its bytes
were hashed; no full paper was saved into the repository. The failed access
routes were not represented as successful primary-source reads.
