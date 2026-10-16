# Focused causal-neighborhood check — v1

All requested mathematical mechanisms are supported on their intended domains, with one narrow missing domain restriction in the general bias-bound sentence. No empirical validation or formal audit verdict is assigned.

## Frozen source

The complete source was read and independently reconstructed before reading the complete runner, controls and execution receipt. Source SHA256: eca7acf773082a89478fcabff9c47d3b5c2bc64659e304bcadb6805154fabcf8. Runner SHA256: 922ab9ddca827507e22aa350e87d86e26a128697170b9c50b61361fcb3f558ef. frozen_sources.json and author_output_hashes.json bind all original artifacts; hashes were rechecked unchanged after reproduction. No preceding unit was rerun or extended.

## Finding: tau needs its probability-bias domain

The displayed q=1-(1/2-tau)^2 is valid for 0<=tau<=1/2. That range is not explicitly stated in v1's general theorem sentence. Literally, tau=3/4 permits deterministic independent X=Y=0 because each marginal deviation is 1/2<=tau; constant zero outputs then win with probability1, exceeding the displayed q=15/16. The step multiplying two lower bounds requires nonnegative lower bounds. Explicitly state 0<=tau<=1/2, or use min(tau,1/2). This does not alter the exposed experimental input tau=1.08e-5 or any reported control value.

## Independent derivations and scope checks

The complete proof reconstruction is derivation_before_code.md. The local parity contradiction supports the 3/4 bound with arbitrary past memory, provided the stipulated conditional freshness/factorization holds for the complete latent variables and response seeds. An observable lack of signaling alone does not establish those premises. Conditional independent biased inputs yield the minimum-pair bound within the tau range above; marginal biases without conditional joint independence are insufficient.

The fixed-N binomial tail follows by backward induction on a continuation payoff increasing in accumulated wins. It needs only the uniform conditional win bound at every history, not independent output devices, and is not an anytime stopping statement. Predictable exception eligibility with conditionally uniform fresh settings gives mean .75+.25lambda and the ideal quantum resource threshold sqrt(2)-1. If the inputs are instead treated with a biased q, the mixture expression would be q+(1-q)lambda; the given .75 expression is the uniform-setting case. Eligibility correlated with current inputs is excluded.

All E_gamma pair tables are normalized/nonnegative, no-signaling, isotropic and have the stated reversal, exchange and same-axis properties. Their CHSH values follow directly from the four dot products. Pairwise consistency does not establish quantum or multisystem composability, or a local implementation, and the source does not claim those. The affine ball-state lemma follows from transitivity, the axis stabilizer, reversal and calibration. Its physical operational state sufficiency and mixture premise are imports. The two preparation mixtures give the claimed different nonlinear responses despite identical average vectors; their physical equivalence cannot be asserted just by assigning that vector.

## Evidence

The independent exact implementation enumerates all 16 deterministic local tables, nine biased-product cases, a history-dependent win process and an exact rational binomial recurrence. The exposed N=245, wins=196, tau=1.08e-5 give tail 0.039109972413714174. This reproduces a published-input calculation, with the approximately 0.039 report interpreted at its stated precision; it is not a raw-data reanalysis, a new exact experimental bound of 0.039000..., or a posterior probability of a model. independent_execution.json records the successful 120-second-bounded run (about 0.05 seconds).

The author probe reproduces exactly with seven passing controls and zero failures. execution.json records the actual command and 120-second bound; reproduced_controls.json and reproduction.stdout preserve output. The only interception redirects its final JSON write into this directory; mathematics and source-path hashes are unchanged. The probe's input-bias examples are all within the valid tau range, so they do not test the omitted domain. No computation failure or timeout occurred.

The primary experimental and communication papers were not re-audited in this focused mathematical check. Their summaries remain exposed development inputs, and no raw timing, source calibration or device data is asserted independently verified. The Toner-Bacon reference supplies no premise to these proofs. All network locality, operational state, preparation and measurement identifications remain conditional. No author files, git state, publication or formal audit status was changed. Await a narrow domain amendment for full-source confirmation.
