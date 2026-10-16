# Focused finite-test blindness check

PASS for this exact finite-test counterexample. No material mathematical or implementation defect found. Complete note read and derivation_before_code.md saved before complete runner/output inspection. Exact source binding:

- NETWORK_EVOLUTION_BLOCK19_v1.md: 1a20e73adb8cf110e985556852dad26386a45bdee98d1a85d88664ed8d8f3c7d
- probe_weak_test_blindness_v2.py: a350f04276bc7d154a6ad5cc9e5e4ed51279c4a1edcb3639e50be7c82885db77
- WEAK_TEST_BLINDNESS_CONTROLS_v2.json: 797e2d93760ce8bd7539885de08305381b37b96853a09699a839fdbb009b2f03

For q=1+t, the derivative parts of K_j have degree at most j+4; the positive Omega2 term has degree j+6. The first four kernels therefore have degrees 6,7,8,9 and are exactly orthogonal to shifted P10. The pointwise operator has degree12 with leading coefficient eta*Omega2*binomial(20,10), so the modified response cannot arise solely from another hidden preparation of the same fixed action. The j=4 test has the exact nonzero projection eta*5*Omega2/277134. No frequency, zero-crossing or initial-state ambiguity is needed for this witness.

Independent check.py constructs shifted Legendre polynomials using Rodrigues differentiation and integrates coefficients directly rather than using the author's Legendre/integrate route. Sixteen assertions passed, including full v2 reproduction: seven passing author families. The exact v1→v2 diff is only native-int conversion of the degree metadata. The original traceback records a JSON serialization TypeError, not a mathematical failure; this evidence was read and hash-bound separately. All author source hashes remain unchanged. Actual commands, 120-second limits, elapsed times, successful independent/reproduction return codes and complete stdout/stderr are preserved. No independent execution failed or timed out.

This is a counterexample to sufficiency of the selected four tests for the stated trajectory/window. It does not invalidate the necessary weak identity, demonstrate that the previously simulated trajectories fail it, or prove a universal observational impossibility. It supports additional independent test functions and a justified model-error/bandwidth contract. The perturbation is synthetic; no actual data were changed. No audit verdict is applied and no author/canonical files were edited.

## Final exploration-report consistency

The complete updated NETWORK_EXPLORATION_REPORT_2026-10-16.md was read after blocks18/19 were included; its exact hash is in supporting_hashes.json. The block18 zero-crossing claim, zero-path blindness, block19 finite-span counterexample and seven-family count are consistent with the checked sources. The report correctly preserves v1 serialization failure and describes v2 as metadata conversion only. The prior signed-coherence correction remains accurately stated.

The narrative distinguishes necessary tests from action derivation, simulated reserved shapes from independent empirical validation, and conditional classical mechanisms from an explanation of quantum superposition. Earlier checked numerical summaries and family counts remain consistent. No further material source-scope finding was identified. This check does not inspect figure pixels, verify external PR state, rerun historical archive intake, or grant integrated landing/audit status. Later report edits require affected confirmation rather than borrowing this hash binding.
