## Block117 checkpoint: Schur/scalar-LSZ strict artifact resolver

This checkpoint resolves the strict Schur/scalar-LSZ pole-authority contract
against the current PR230 head. It adds a strict artifact resolver that checks
for K-prime pole rows, Schur/Feshbach or transfer-kernel derivative authority,
source projection numerator, scalar-LSZ moment/threshold/FV authority, and the
required source-Higgs/W/Z/neutral bridge root.

Result: exact negative boundary. The current head has no strict
Schur/scalar-LSZ pole authority artifact. The complete finite Schur A/B/C
packet remains support-only; strict K-prime pole rows, scalar-LSZ
moment/threshold/FV authority, finite-packet promotion, finite-moment residue
authority, and physical bridge roots are absent. The scan saw `460`
Schur/scalar-LSZ-adjacent candidate output files and `0` strict certificate
hits.

Validation:

```text
block117 Schur/scalar-LSZ strict artifact resolver PASS=12 FAIL=0
campaign status PASS=437 FAIL=0
assumption/import stress PASS=120 FAIL=0
full positive closure assembly PASS=200 FAIL=0
retained closure route PASS=325 FAIL=0
positive closure completion audit PASS=79 FAIL=0
strict audit lint OK: no errors; 5 known warnings
audit pipeline complete; generated docs/audit churn restored
git diff --check OK
```

No retained or `proposed_retained` closure is claimed. PR #230 remains draft
and open. The next admissible Schur/scalar-LSZ action is a real strict
artifact with pole coordinate, K-prime derivative or exact Schur/Feshbach
equivalent, source projection numerator, threshold/FV/IR/contact authority,
and canonical `O_H`/source-overlap or a physical W/Z/neutral bridge. Otherwise
pivot to a fresh source-Higgs, W/Z, or neutral strict packet.
