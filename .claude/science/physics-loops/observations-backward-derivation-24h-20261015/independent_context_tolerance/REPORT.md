# Focused context-tolerance check

PASS within the stated finite unit-orientation, unitary-transport and closed-anchor domains. No material mathematical or code-source defect found. No empirical accuracy, physical context model, audit verdict or general quantum conclusion is established.

Complete note was read and the independent proof saved in derivation_before_code.md before code inspection. Complete runner and control JSON were then read; the normally imported echo helper is identical to its earlier same-session checked revision. All sources and dependencies are frozen below:

- NETWORK_EVOLUTION_BLOCK14_v1.md: a219261cee69f71d24855a55f8724d02aa2fdd39979171ad222e55eb5a553344
- probe_context_tolerance_v1.py: ddb0e268da9ff3fe39e2742cf077f7f92d0567525f2b04948454594b6c326be1
- CONTEXT_TOLERANCE_CONTROLS_v1.json: 1313ad5ecad196ec51ad9810f7e22da2f82ab00e5e88dba98c9804a9aa9fd7de
- NETWORK_EVOLUTION_BLOCK12_v1.md: e5fe9458c1794b28562bd5215b090083362cda6daf472e441ba2f3e651c90f1e
- probe_context_echo_v2.py: 1495843bdc467731645d18ebfc6a7468d682766c27a060a78eb8fb00c5f8fbd8

The z→x→latitude connector and its reverse have nonnegative endpoint dots for both north and proper-x-rotated south loops. With N>=4 the latitude dots are also nonnegative. This removes the previous near-antipodal connector even at small positive beta, and each loop has N+4 edges. Conjugation preserves the reference phase and reversal cancels connector crosses, preserving the previous full SU(2) equality and context discriminator. This is a new ideal path, not a claim that a device can perform it without additional timing or control effects.

The pair bound follows directly from Pauli operator norms, the reverse norm inequality for numerator norms, and the common positive edge gap. The eta=1-2delta bound uses unit perturbed vectors and delta<1/2; it therefore guarantees actual admissibility. Unitary telescoping has no exponential factor and permits arbitrary correlated errors. The disk arcsin certificate is valid for S<1 and local continuous/unwrapped phase differences; raw principal-angle subtraction across a branch cut is not a global error metric. The note explicitly retains the unwrapping requirement.

Edge-dependent contextual twists still commute when transported to the same anchor, yielding the stated drift bound. Geometry cross-product subtraction yields the sum(ea+eb) bound with no omitted quadratic term, because actual endpoints remain unit vectors. Combined bounds require genuinely closed paths at the identified anchor or separately controlled preparation/readout mismatch. Open paths do not automatically have the stated closed-path eigenphase. The runner fixes endpoint anchors, matching this condition. Drift must use actual edge cross lengths or a justified upper bound. Unknown coupling/context size does not supply a numerical error certificate without independent bounds.

Independent check.py uses real quaternion products, 24 north/south cases including beta=1e-5, exact tangent-disk examples through S=.999, and 100 independently selected edge perturbations. Total independent assertions: 155. Author runner reproduced its full JSON exactly: five passing families, including 16 path geometries, 952 pair controls, 200 path controls and 200 drift controls. The selected planning phase bound is 0.0016970735172023193 radians, a conditional calculation rather than instrument performance. Counts overlap and are not empirical trials.

All source hashes were rechecked unchanged. Executions were bounded by 120 seconds; actual commands, elapsed times and return codes are in check_receipt.json and reproduction_receipt.json. Stdout/stderr are preserved. No failure or timeout occurred. No canonical or author file was edited.
