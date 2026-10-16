# Final empirical envelope identity confirmation v1

The final source, products and successful cache agree with the preserved empirical correspondence review. No unresolved identity or empirical-output discrepancy was found. This closes only the separate final-envelope confirmation left pending in AUTHOR_CORRESPONDENCE_REVIEW_v2.md; that report and its identity remain unchanged. This is not a formal audit, new raw-data reconstruction, mathematical-suite rerun or physical validation.

The reviewer ran final_envelope_identity_check_v1.py without importing any author module. It hashed the declared source and four already registered local raw inputs, parsed the saved result objects, compared exact historical/current JSON trees, recomputed the cache input fingerprint independently, and streamed the two gzip ledgers solely to verify uncompressed hashes and line counts. It did not decode raw observations or recompute any scalar, count, quotient or lattice result. All checks completed with exit code 0. The complete evidence is FINAL_ENVELOPE_CHECK_v1.json.

| Bound final object | SHA-256 |
| --- | --- |
| logs/runner-cache/scalar_phase_quotient_check.txt | 8e75f43ab810d290e779a792a3b88d2df58e2854ead46783b79318476a1de5f2 |
| runtime M8_CANONICAL_EXECUTION_v2.json | 2f1c1e107d3ea8a0594fc4756931936a745ae05161b4193df151e2d1041dbe07 |
| outputs/scalar_phase_quotient/summary.json | 6ca043e5985467092fa3cad22e5faae3082787e4deb1f74d87ba98cb13e2fc46 |
| outputs/scalar_phase_quotient/QUOTIENT_DEVELOPMENT_RESULTS_v1.json | 8916e82b919e54ce9e1b5a7859652aa90d0c42605ab70659ae320fcbf6846879 |
| outputs/scalar_phase_quotient/mathematics.json | dd345ef49b140c5b554abdfe185c9406ca5bc055d53a35959f2ab745245906a6 |

The cache has status ok, exit code 0 and empty stderr. Its elapsed time is 7.64 seconds in the header, consistent with the receipt's 7.639117002487183 seconds, below the declared 180 seconds. The JSON portion of cached stdout equals the final summary exactly. The separately recomputed seven-input fingerprint is 9cfa7c4e53f17bde6202e927dd31d8d3e28fb6f0ed9c4d5825f3d62286ded2b7, equal to the cache; the separate primary-runner hash also agrees. This establishes freshness against the checked bytes, not merely trust in the receipt's label.

All eight summary source hashes match current bytes. The primary, data helper, mathematical helper and note also match the exact source copies bound by the v2 correspondence identity. The data helper is ebc2df3069731b47eb446b9ed267008af22a6d53ac230dd0b520c7c951ebc4e5; the only change from its earlier fully compared 1cddc8b9 source remains the previously checked timeout declaration. The mathematical helper is 6d0f57373f34b9584ff5b6cacd00799b0b50d86f53f4fa1a6f8e1050d3f3f680 and the note is d333d64f1eec02799a1a03c18cb8aa3b6ad0bcfe64824c3fbd68cf356de1a12e. The mathematical helper's general proof remains the other reviewer's scope; this supplement binds its saved execution rather than independently certifying that proof.

The final development JSON differs from preserved preliminary canonical object ae8c538440be5d1bf1867daa92f189f3c28f7997b2d65ce285f340dcd38a0c45 at exactly one field: its data-helper source_sha256 changes from 1cddc8b9 to ebc2df30. Every other value, including complete row/metadata inventories, duplicate-candidate counts, chains, triple counts, extrema, descriptive bins, source records and declared scope, is exactly unchanged.

Both deterministic ledgers retain the exact compressed and uncompressed identities previously checked against the independent extraction:

| Ledger | Rows | Compressed SHA-256 | Uncompressed SHA-256 |
| --- | ---: | --- | --- |
| QUOTIENT_ROWS_v1.jsonl.gz | 91664 | 04b7af8c9911b71ec6fa011441fca25de2eb2ba262caa7f8b7b4f431d8edb59a | 79a0e0dff422559c0620450afdf551dbe2a4dd22c0382ba7dbe0e49873b5ae08 |
| QUOTIENT_TRIPLES_v1.jsonl.gz | 91593 | f5f6db505b0e142728c445f8f6dc59574854fa9319462b664139ac622f05c973 | c3c8738eee6c0fae6aaf6f2b11694177839068cc83261cb550d40ececc338ddf |

Relative to the historical summary 3b8ce975c9edb4a4b1d9a6c1959b111cf165d448facd05ecacea5bdccaf389c4, exactly seven JSON leaves change: mathematical controls 34 to 38; total controls 45 to 49; note, mathematical-helper and data-helper hashes; and the mathematics/data-result product hashes. The same eleven development controls remain true. The final saved mathematics object records 38 true controls and zero failures. The four extra controls are mathematical/error-bound fixtures, not extra empirical observations. The exact change ledger is retained in FINAL_ENVELOPE_CHECK_v1.json.

The final summary still records zero independent empirical tests, fitted parameters, physical energy estimates and inferred physical-error bounds. No forward history, quality clipping or physical noise certificate is introduced by these identity changes. The established empirical scope remains consistency of dependent, exposed archive products, with both duplicate endpoint variants retained in the row evidence and linked to their numeric triple.

All twenty files bound in AUTHOR_CORRESPONDENCE_IDENTITY_v2.json were rehashed and remain unchanged. The corrected report e919de64201449bd8851a9a599b3aa860e5b5388e7bf4131930cfb389866ad7f, its identity 6e8f66663e2fa8c573fbbfb088ef0e2f6fb81ea99f0bbbb6c256fc600411ce6e, the original v1 report, and the one-token provenance repair record remain separately preserved. No historical cache or report has been relabeled as this final evidence. Exact copies of the small final cache, execution receipt and summary accompany this supplement.

Only this independent reviewer directory was written. No source, branch, index, lock, status, publication, raw input or author product was modified, and no network call occurred.
