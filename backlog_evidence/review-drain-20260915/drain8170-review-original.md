# PR8170 original independent review

Original `f9e1177003afa991ec87831d2be70611068a09ab`; actual merge-base `6dda46fc1af02827e9c6b64b2f7d05c381a3ce07`; frozen current-main `e6e9cfe996c7f4b9f2a1bb02492dddba444259e9`.

**Needs narrow source repair. No landing PASS.** Partial science salvage is viable; complete original recovery is mandatory. One review iteration, 25 original paths, 8 material findings; no commits, primary executions, full pipelines or audit actions.

## Findings

### 8170-1 — False derivative bound and invalid Langevin proof
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:102

At kappa=1, sinh(1)^2>62/45>4/3, so A'(1)>1/4, contradicting A'<=1/(3+kappa^2). The implication from the lower bound on sinh² reverses direction. B2 and the exact control verify coefficients and identities, not this inequality, yet print the false implication as PASS.

**Narrow repair:** Delete derivative upper bound. Prove A(k)<k/3 via f(k)=(k²+3)sinh(k)-3k cosh(k)=sum_{n>=2}4n(n-1)k^(2n+1)/(2n+1)!>0. Update B2 and negative controls to test the actual coefficient/sign argument; preserve historical false PASS unchanged in recovery.

### 8170-2 — Exact conditional mean is not gain one
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:108

For common predecessor rotation theta, E[s_perp]=A(3beta)sin(theta), hence derivative A(3beta)<1. Covariance rotates a mean of length A(3beta), not a unit vector. The quadratic exponent has its maximum at the average (negative Hessian); the normalized mean direction has gain one. These do not make the exact noisy nonlinear mean gain one. Combining its exact noise with Gaussian gain is a declared auxiliary model, not an exact linearization theorem for every beta.

**Narrow repair:** Separate exact mean Jacobian A(3beta)/3 times the sum, mode/direction statement, and explicitly supplied gain-one additive-noise recursion. Retain T5 only for that auxiliary recursion; e^-v is a declared proxy, not nonlinear magnetization or an exact sphere observable. Use asymptotic equivalence notation gamma~sqrt(3)/(4pi beta), not convergence to a beta-dependent value.

### 8170-3 — No nonlinear diffusive memory-time theorem
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:137

T4 establishes a minorization rate (1-delta^(L²))^t, not a beta L² estimate or lower bound on forgetting time. Two finite sizes and finite single histories cannot exclude finite-size effects, interchange t and L limits, or prove cubic terms always accelerate decay. 256²/20000=3.2768, not >10; 512²=262144, not half a million sites.

**Narrow repair:** Remove the claimed exclusion and attribution to T4. Keep finite-plane uniqueness/rotation invariance and exact L=1 recursion. Describe beta L² as an auxiliary-model heuristic if retained, with nonlinear scaling open.

### 8170-4 — Historical table contradicts universal exponent and observable claims
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:153

Independent beta12 history has slopes 0.0076 and 0.0103 below gamma≈0.011167; beta24 early slope 0.0055 is below 0.00566. The fit selects m_z where available, whereas prose calls it |m|. Independent beta12 stores only |m|, so its projection cannot be recovered. Historical checker says differences <10^-3, but controls reach 0.01189. Rounded six-axis 1.00000 observations are not proof of zero dissent at all times.

**Narrow repair:** Preserve all rows including below-gamma fits, negative projections and NaNs. Label each observable and rounded sampling cadence; use finite-history exploratory descriptions without universal ordering, monotonicity, plateau exclusion, or asymptotic exponent inference.

### 8170-5 — Fit does not discover landed raw inputs
.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block26_fit.py:5

Fit globs sim_b*_L*_T*.txt/ref_sphere_b*_L*.txt/ref_linear_b*_L*.txt. No such files are in the frozen packet; the data are concatenated in three differently named outputs. It therefore silently emits no rows on the shipped tree. Refuter source now prints m_z but beta12 historical output did not: do not restamp as current execution.

**Narrow repair:** Supply a deterministic parser of the existing concatenated files or pinned split-input materialization, fail on absent expected series, declare actual raw input paths, and reproduce the table cheaply. Do not rerun expensive simulations merely to replace history; maintain historical source/output limitations explicitly.

### 8170-6 — Older phase assertions are promoted despite corrected current-main scope
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:19

Current main's static six-axis reflection/contour note defers unconditional phase conclusions. Sphere static sufficient bound is conditional on corrected zero-field parent and explicit mathematical imports. The present finite simulations establish neither side of a settled four-cell memory map. Sibling evidence-address wording does not neutralize conclusions actually used in the headline comparison.

**Narrow repair:** Remove unconditional old static/formation-order and exponential-memory assertions; either link precise current conditional scopes as context or omit the comparison. Keep the fully declared supplied sphere model self-contained. Block01 contributes finite records-only product-rule vocabulary, not a selected sphere law, coupling, schedule or physical process.

### 8170-7 — Negative packet overstates tested resolutions and twist exclusion
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:172

N1 mixes diagnostics, one formal route, and unproved finite-size exclusion; it is not five closed distinct attacks on a quantified no-go. Fixed-twist entropy cost proportional to T does not rule out all T-dependent twists/limits. N5 claims infinite-plane simulation though all executions are finite periodic histories; T1-T5 blanket proof is false as submitted.

**Narrow repair:** Keep twist as an unsuccessful outlined attempt with terminal entropy-control obligation open, not closed-negative/no bounded-cost twist theorem. Withhold broad negative certification explicitly; retain valid finite-plane theorem and auxiliary-field variance obstruction separately with honest written-proof versus finite-execution domains. No invented route count or certificate.

### 8170-8 — Dependency and evidence publication wiring absent
docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md:60

Axiom and Block01 are code-formatted paths, not markdown links. Original topology manifest confirms out_degree=0 despite two claimed dependencies. Primary reads only three notes; historical simulations/fit outputs are not declared inputs. Campaign certificates and author PASS records are not current science authority.

**Narrow repair:** Add repo-portable markdown links to actual load-bearing authorities and primary/cache, declare any retained evidence parser inputs, regenerate topology acknowledgment on final current-main candidate. Preserve complete histories in durable recovery, prevent historical certificates from asserting current standing, and defer current cache capture/combined gate to coordinator's authorized placement.

## Independent checks

- Manual reconstruction of T1 moments by differentiated normalizer; exact kappa=1 derivative counterexample; positive-series repair derivation.
- Manual exact common-rotation conditional mean derivative and quadratic exponent Hessian.
- Manual T3 Fourier symbol, determinant 1/27, Gaussian integral constants and all-k upper/lower proof, harmonic-tail assembly.
- Independent integer convolution k<=150 (floating comparison against local-limit constant); output maximum deficit 0.13947154653231575.
- Manual T4 minorization, monotonicity and rotation-unique invariant-law argument; L=1 tower recursion.
- Manual auxiliary T5 independent noise path variance/no finite-variance stationary law; account P0=1 in upper sum (143.41322<150).
- Read complete historical control/refuter algorithms, raw outputs, fit and cached primary; no original primary run.

## Salvage and provenance

Correct exact sphere moments and A<k/3 with repaired proof; exact mean Jacobian plus quadratic-mode distinction; T3 local-limit bounds and harmonic estimate; finite-plane Doeblin theorem; explicitly supplied auxiliary-field T5; honest historical finite observations.

Nonlinear infinite-plane memory decay/exponent, physical selection, nonlinear diffusion scaling, broad twist impossibility, unconditional old phase map.

Every original path, full shared-history content, complete proof, scripts and raw outputs preserved with original modes/blobs/hash; base/current-main shared files also snapshotted. No branch deletion warranted for unlanded/deferred science.

Per-path modes, Git blobs, SHA-256 and dispositions are in the JSON report and `drain8170-original/manifest.json`; exact original/current authority/input pins are in `drain8170-original/input-bindings.json`. Bounded control script and output are in `check8170/`. Installed review-loop entry and all used references byte-match frozen current main.

Current-main preservation remains an integration obligation: shared campaign boards and topology cannot be replaced wholesale by this stale branch. No generated train outputs were read or changed.

## Return state

PR remains OPEN, non-draft, base main, exact original head rechecked. Slot HEAD `f9e1177003afa991ec87831d2be70611068a09ab`; tracked/untracked/ignored status empty. Root owns slot release. Reviewer session retained for affected/cold/final confirmation.
