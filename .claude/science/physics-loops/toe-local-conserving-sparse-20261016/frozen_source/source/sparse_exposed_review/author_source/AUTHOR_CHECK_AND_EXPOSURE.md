# Author check, qualifications and exposure

This is a same-author, same-model continuation of the frozen local-control candidate. It is not an independent validation of that parent, and both parent and extension remain pending root acceptance. Only the pinned local parent and primary Bai–Marvian v3 paper were used as mathematical parents. The separate root proposal and review directories were not read. No agent or model override was used.

## Controlling scope

The proposed polynomial bound concerns the nominal driven evolution beginning with the supplied coherent sine reservoir and one clean ancilla, on the parent's connected path through all old sites and with explicit full-SWAP edge permission. It excludes preparation and classical compilation time. No microscopic driver/clock supplier, autonomous halt, general nonhomogeneous old Hamiltonian, one-old-port implementation, XY+Z-only path universality or indefinite reuse is inferred.

The target is the parent's full U_L(V), including the unoccupied top complete sector and identity on all other prefix/nonprefix data states. The complete physical C on an initially zero ancilla implements it as an isometry; C on an initially one ancilla is also retained but need not be identity. Exact global phases are checked in the logical construction and the positive-pulse scalar is retained separately.

## Analytical checks actually performed

* Counted all selected labels directly: a_count=L+q+1 sectors, d=2^q basis states each. Distinguished that structural count from the V-dependent minimal changed-column support, which is not assumed decidable.
* Reconstructed determinant-one Givens elimination on one d-dimensional V. The first d-1 final pivots are one, leaving only det(V), so the cost is p=d(d-1)/2 special two-level gates plus one phase per sector.
* Recounted the primary's elementary identities in the parent's actual forward-sqrt(iSWAP)/Z alphabet. Variable XY costs 12; a one-bit controlled XY costs 50; a controlled general SU(2) costs 152; a controlled iSWAP or its inverse, with control bit one, costs 34. Inverse powers and paired S scalars were included.
* Reproved the split-control commutator on all four match/nonmatch sectors and the parity induction for T(k). This introduces no extra ancilla or uncomputed classical flag.
* Checked the prefix-code Hamming distance formula, the i^(t-1) basis-routing phase, and the nonvacuum ancilla partner used for the one residual phase per block. The selected top sector was not removed to reduce the count.
* Propagated those costs through actual spatial full-SWAP routing. The resulting Gbar is an explicit integer function, bounded by K_q L^4. Fixed-duration zero-padding makes the total endpoint independent of target angles.
* Checked the norm-certificate interface without support, pivot or principal-argument equality tests. A finite angle grid gives a word with an operator-norm margin. A trace-power upper bound with the adjoint verifies that margin; a dimension-unadjusted Frobenius acceptance test was explicitly rejected.
* Rechecked all resource powers against the parent's integrated error ledger: global static and pulse errors of order epsilon^5, per-new-site static errors of order epsilon^6, endpoint time of order epsilon^2, and cancellation-sensitive Delta/pi evaluation requests of order epsilon^9. These are sufficient precision requests, not oracle-time bounds.
* Added a separately stated guarded pulse-start model after noticing that angle/area tolerances do not price timing history. Translation of the cosine pulse costs at most 4Q_*|shift|/h in integrated generator norm. Two idle guard slots, absolute start precision of order epsilon^5 and the stated overlap bound preserve the common cap/slew. A worst-case accumulating period error needs order epsilon^9 for its start-time component. This extension is analytical and was not part of the finite executable's coverage.

## Exact finite check and preserved failure

`PRECHECK_FINDINGS.md` copies the provisional checkpoint written before the exact source was constructed and launched. It was copied for preservation after the run and was not cryptographically sealed in advance. It records the candidate count and the named exchange/phase risk; it did not require a desired PASS count.

The single scientific source was written from direct Pauli computational-basis matrices and exact integer enumeration, without importing any parent checker. It first entered a launcher that failed in `preexec_fn`; source execution did not start. That original source snapshot, launcher, receipt and full streams remain in `runs/exact_sparse_check/`.

The retry ran exactly the same scientific source, removed the attempted address-space limit, and retained a 90-second wall/60-second CPU limit. Its source-at-launch SHA256 is `2ede311427e4e765dfa0f75ac3ad7feeb4af31f5873f42a5bb1c787216c7d565`. The run finished with exit code zero in approximately 1.48 seconds. The complete stdout and empty stderr were inspected. Source, launcher and stream hashes were checked against both receipts.

The wrong-adjoint and omitted-inverse variants gave exact nonzero squared residuals 16 and 32/5. The complex four-dimensional decomposition used six special Givens rotations and residual phase -i. The q=2,L=1 prefix instance had 16 selected states in four sectors and maximum internal distance four. These are finite exact checks of named identities/interfaces, not a generated general sparse compiler or an independent acceptance of the resource theorem.

## Failed shortcuts and refinements retained

1. Importing a generic exponential circuit count would not establish polynomial nominal runtime. The count is instead reconstructed from individual blocks and a checked two-level supplier.
2. Assigning inverse sqrt(iSWAP) unit cost would change the allowed alphabet. Forward powers seven and six are explicitly paid.
3. Omitting the determinant phase would implement the wrong target on an entire sector; replacing it by an unspecified global phase would also affect the off-code identity contract. The one-clean-ancilla pair fixes the exact relative phase.
4. The exact QR/pivot and Euler branch choices can be discontinuous. The proof separates finite-real existence from a certifying finite-error grid search, with no exact-zero oracle.
5. A coarse angle grid followed by a full Frobenius acceptance bound can lose an exponential dimension factor. The acceptance condition uses a computable operator-norm upper certificate; the target-entry error uses its repeated-block structure.
6. An exact ceiling of an arbitrary computable accuracy expression is not silently assumed decidable. The final resource constants use the rational-enclosure selection L=floor(rho)+2, with its explicit additive slack.
7. The first launcher failed before the scientific execution. No successful result or installed memory limit is attributed to that attempt. The cause was not exposed by subprocess, so removing the address-space request is recorded as a successful retry change, not a proven diagnosis.
8. One patch invocation used a nonexistent path missing a directory component and failed before changing any file. It was retried against the assigned path. This was an editing error, not a scientific execution.

Only the assigned new directory was written. Parent freezes, canonical sources, Git/PR state, audit/cache/locks, prompts and axioms remain unchanged. Root owns acceptance and publication. The proposed next independent check is an emitted end-to-end elementary word for a complex two-old-qubit target, including full determinant phase, clean-ancilla isometry and physical routing count; it has not been executed here.
