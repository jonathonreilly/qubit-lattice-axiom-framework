# Focused independent orientation-transport check

PASS for the declared conditional mathematics. No material error found in the complete source or its supplied-premise boundary. This is not a formal audit verdict, empirical validation, physical selector certification or novelty judgment.

## Exact source and coverage

Complete source read: NETWORK_EVOLUTION_BLOCK03_v1.md, SHA256 d13c99fd593e1b2761aa82b518d1c699b112c5e9ae4a4fc7b0fa4c159fb289e2. Complete author code read after independent derivation: probe_orientation_transport_v1.py, SHA256 f1e8b5964c95e26a78ceeaf5ee27b4207a7bf8a85e908241d41eda374c3c0ee5. Identities were frozen before reconstruction in frozen_sources.json; author outputs have separate hashes in author_output_hashes.json. Original frozen files were checked unchanged after execution.

All sections were considered: motivation/provenance, class hypotheses, uniqueness, antipodal obstruction, relaxed-premise examples, exact loop, flat chart, causal/observational boundary, and computation scope. The complete current Minimal Axioms memo and premise registry were already read earlier in this same checker session; their hashes are in premise_boundary_hashes.json. Adjacent SU(3)/walk results are explicitly not premises and were not imported. Primary literature is motivational and was not independently re-audited; no empirical statement was used to establish the algebra.

## Decisive independent proof

The pre-code proof is derivation_before_code.md. The key reversal step is sound: for non-antipodal distinct a,b a pi rotation around their bisector exchanges a and b while sending the oriented + eigenspace at a to the oriented + eigenspace at b. It does not swap + with -. For coincident axes the identity suffices. Extracting stabilizer eigenvalues by Tr(P_a± K) makes their continuity and covariance explicit. Therefore both eigenvalues depend only on c and retain their labels upon reversal. Exact matrix reversal then forces Hermitian K, and continuity plus diagonal normalization remove the three other sign pairs. Determinant one is a consequence, not a hidden hypothesis.

The antipodal obstruction follows independently from the stabilizer of (a,-a): covariance under every rotation about a forces commutation with A, inconsistent with conjugating A to -A. This is a genuine obstruction in the stated pair-only SO(3)-equivariant class.

The third-vector twist retains unitary axis transport, diagonal identity, simultaneous covariance and exact reversal with fixed n. The inverse identity uses U A=B U, so does not incorrectly commute the twist through unrelated axes. It defeats uniqueness once pair-only dependence is relaxed; its free kappa remains supplied. Channel-level reversal also fails to select scalar phase: exp(i chi(c)) cancels under conjugation but generally fails exact phase-sensitive reciprocity. These are correctly scoped counterfamilies.

Direct Pauli multiplication yields the stated octant loop diag(exp(-i*pi/4),exp(+i*pi/4)). The inserted third-context twist transports back to Z and adds kappa/2 to its eigenphases. Reversing edge order with identical contexts cancels exactly. A coherent junction's cosine fraction is conditional on the additional comparison/readout model; a single spinor norm cannot observe the loop phase.

The flat chart connection telescopes exactly. An independent covariance witness is the trace: its transports for ordered pairs (z,x) and (x,y) have traces sqrt(2) and 1 despite equal pair dot product zero. Since the pairs are related by a proper rotation and trace is conjugation-invariant, full pair-only covariance fails. Thus endpoint flatness is an imported connection choice, not a consequence of transport and reversal alone.

## Computation and preserved failure

Independent algebraic computations (independent_check.py) verify loop order/sign, symbolic twist relocation, the stabilizer projector identity over the entire orbit parameter range, flat-loop cancellation and the distinct-trace covariance witness. These supplement the proof, not replace it.

The first independent computation returned exit 1 on a symbolic simplification assertion: c was merely declared real, insufficient for conjugating square roots involving 1+c and 1-c^2. Its exact code, command receipt, stdout and traceback are preserved with .attempt1 suffixes. The repair used the explicit nonnegative half-angle parameter t, c=(1-t^2)/(1+t^2), covering -1<c<=1 and carrying the square-root domain into the symbolic expression. The corrected independent check passed under its recorded 30-second bound. This was a checker representation failure, not a counterexample or change to source mathematics.

The author code was then reproduced separately with a narrow output-write redirection into this directory; no formulas or source paths were changed. Complete JSON/stdout and the real bounded command are recorded in reproduced_controls.json, reproduction.stdout and execution.json. Exact equality with the original author control JSON was checked. The author controls are finite/symbolic development evidence: the generic diagonal antipodal check alone would not prove the global obstruction, and its rational-axis grid alone would not prove uniqueness; the independent arguments above establish those claims. No empirical likelihood, global numerical proof or lattice implementation is inferred.

## Physics boundary and unresolved obligations

U(2) unitarity, continuous SO(3) covariance, oriented axes, coherent phase comparison, exact phase-sensitive reversal, diagonal identity and pair-only locality are supplied. None follows just from M2(C) or cubic spatial covariance. The third-neighbor counterfamily makes this limitation concrete. Coherent amplitude composition, unitary hardware, calibrated third context and phase echo, ordinary dynamical-phase separation, formation/readout, resource renewal, and a nearest-neighbor lattice realization remain open. The source does not disguise them as derived or equate permanent which-path records with an unrecorded orientation context. No scalar-gravity or established physical selection conclusion follows.

No source files, commits, pushes or formal audit statuses were changed. This conclusion is reusable only for the frozen source identities and stated scope.
