lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T13:07Z

# b98-gate: line-by-line check of library/b98.md (FINISH row 374)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, commit 392550b85. One reading by one other model; not an audit. Kind of result: check of our own rebuild of cited statements of Sussman and Alpoge's complete account (CA), which credits Balaban (CMP 98, CMP 99a, CMP 109). CA-I and CA-II were fetched at 31a47c543775 into a scratch folder; their SHA-256 hashes equal those in b98 §5. Balaban's OCR text and PDFs were read in ~/ym4d-papers. cp12 Lemma 5 (frozen, checked) was read as an input.

Status: in progress. Sections below are written as the check proceeds.

## Draft findings so far (to be finalized)

- Lemma 8: the five-term formula (A5) was re-derived here from definition (5) with left perturbations. All five coefficients and their signs match CA-I 24356-24378 exactly. The quadratic remainder bound holds as stated.
- Lemmas 9-12: no failing step found yet. Balaban's current normalization was checked against CMP 99a (1.1)-(1.2), OCR 77-100: D* carries the factor 1/eta and the plaquette field is U(dp) itself, so (31) holds.
- Lemma 5 / target B: the account's only consumer (CA-II 8.11:lem-weighted-flux, about L123076-123216) applies the signed bound to V = \bar U^{k_o}(U), the k_o-fold iterate of the one-step map of Definition 1.5, with block side n = L^{k_o}. b98 proves (8) for a single averaging step with block side n. The iterate is not covered. Details and a repair follow.
