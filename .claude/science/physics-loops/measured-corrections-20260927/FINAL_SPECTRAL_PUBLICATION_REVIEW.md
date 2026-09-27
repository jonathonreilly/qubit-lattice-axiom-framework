# Final spectral publication review

**Disposition:** no material mathematical, implementation or claim-coverage defect found in the consolidated revision. One minor wording precision is recommended below. This is a selective independent milestone source review, not a formal retained audit or empirical validation.

## Reviewed coverage and evidence reuse

Read the complete consolidated note, primary runner and all four helpers. Verified that all four helper ASTs are identical to the previously checked working sources after removing their unused `__main__` blocks; the copied arithmetic and proposal routines have no consequential changes. Confirmed the earlier certificate source hashes remain unchanged, so their independent determinant-count and interval evidence remains applicable. Both parent-source identities below also match the previously inspected premises.

The consolidated argument correctly distinguishes exact microscopic block reduction, formal fixed-support first coefficient, form-defined approximate operator, and exact finite-case spectral enclosures. The positive eliminated block and positive Schur multiplier give the claimed global indexing within the fixed two-positive-record sector. The finite-spin boundary coefficients, rotor-tail bound, unbounded-hopping form argument and corrected tail self-energy match the independently reviewed derivations. The six-case table is the independently checked upward rounding of the rational maximum absolute gap-error bounds.

The primary runner imports every load-bearing numerical helper, calls the exact count checks at all endpoints, and derives error intervals by conservative rational subtraction. Floating Schur roots and tridiagonal eigenvalues only propose brackets. Failed counts, failed positivity or zero pivots propagate as failure. It produces all intervals and count labels it claims; a printed count label is emitted only after its associated check succeeds. No external measurement or device fitting enters this runner.

Fresh execution of the consolidated primary completed successfully. All six microscopic/rotor/approximate interval sets and every microscopic-minus-approximate difference interval and maximum error bound equal the earlier independently checked records exactly. Full output is `independent_final_spectral_publication.log`; helper AST comparisons are `independent_final_helper_comparison.json`.

The exact physical operator identification, first-coefficient algebra and form proofs are analytic premises checked by the source review. The numerical runner does not by itself rederive them or independently reconstruct the microscopic state matrix. The note accurately describes the actual independent scope: finite S20 at the larger ratio; both rotor cases; all six corrected-operator cases; all interval subtractions and upward rounding; plus fresh same-implementation runs for every case. Its three PASS categories must retain the declared computational, non-empirical meaning.

## Minor actionable precision

In the compactness paragraph, “its norm-bounded tails are O(L^-2)” should specify **squared** ell² tails, for example:

    sum_{|n|>L}|psi_n|² <= L^−2 ||n psi||².

The ell² tail norm itself is O(L^−1) on a bounded D(n) ball. The intended compact-embedding proof is correct, and the distinction does not affect any enclosure or table value. This is a wording correction, not a blocking spectral defect.

## Limits and source identities

The result remains conditional on the supplied microscopic law and closed sector. The H1 calculation is formal on fixed support, while the table gives actual named-case errors for the full approximate operator spectrum. No uniform asymptotic remainder, coupled-device proof, physical spin identification, microscopic readout derivation, statistical rejection or empirical improvement follows. These boundaries are preserved in the note and runner.

No publication files were modified, and no audit or publication action was taken. Relevant subsequent source changes require a targeted refresh. SHA-256 identities:

- `docs/SQUARE_MICROSCOPIC_SPECTRAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-27.md`: `f486707ae5154c70f756477e30163779f8c643e6cd5fa9f5cbea9a8c5b404018`
- `scripts/square_microscopic_spectral_certificate_2026_09_27.py`: `4104f7d6e7f48fef0c65945c8df6b050ea72f2094de948a0ba3d79b7a92609ce`
- `scripts/square_schur_proposals_2026_09_27.py`: `3ab1177c846d0d967f4fb3b13b1ef9b35d6fbe146c7d7f909477d4bfe3135bd4`
- `scripts/square_rational_inertia_2026_09_27.py`: `ee1cae6d9616a715ba3b252556a71709436958fedee78f5e1bbbab26f86e0c42`
- `scripts/square_rotor_tail_2026_09_27.py`: `c5fd657fb4bcd95cc4029986c3c9bbdc2f61739a45d386333d492be529355f96`
- `scripts/square_corrected_tail_2026_09_27.py`: `48dd82076fe2ad5d773c00a1de76b169fd839e4562ad65dbacd7897df1156d09`
- `docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`: `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a`
- `docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`: `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`
