# What would justify a dispersion conclusion from energy-only moment bounds (ring model, pure-ring point)

Worker `w-jonathonsmac4f50-j3764` (Claude Sonnet 5.5), unit `J:derive:deferred-20260925-ring-limits:a1`.

**Provenance.**
- The claim printed no prior attempts, so nothing here duplicates an earlier probes attempt.
- I read open PRs #9220, #9236 and #9239 on their branch heads.
  - They are by the owner's other Claude session, the same model family as this worker.
  - They are unrefereed.
- The task is owner-requested. It is not one of this machine's supervisor's blocks.
- Nothing is adopted. This attempt makes no photon claim.
- PR #9236's `Ice` class, `exact_L2` and `triple` are vendored unchanged in `pr9236_lib.py`. Definitions only.

## 1. What is attempted

**The question.** Which estimates would justify a dispersion conclusion from PR #9236's energy-only bounds, and which of them the current estimators can supply.

**Setting** (PR #9236, supplied).
- Take a transverse mode O of the flip component's ground state |0⟩. Its spectral measure is ν = Σ_{n≥1} w_n δ(ω − ω_n), with w_n = |⟨n|O|0⟩|² and ω_n = E_n − E_0.
- Write M_p = Σ w_n ω_n^p.
- M_1 = 2us² is exact (f-sum rule). M_{−1} = χ/2 is read from ground-state energies in a weak field.
- The bounds are ω_min ≤ M_0/M_{−1} ≤ M_1/M_0 and M_0 ≤ (M_{−1}M_1)^{1/2}.

**Choice of estimator** (the task's first item).
- **Estimator.** The energy-difference estimators. Both χ from E(h), and the new M_0 from E(ν) below, are differences of mixed-estimator ground-state energies.
- **Sampled distribution.** ψ_T·ψ_0 of the fixed-population projector. The mixed energy estimator is exact in expectation for any guide.
- **Exact observable.** The ground-state energy E_0(h) or E_0(ν) of the perturbed Hamiltonian in the canonical zero-winding flip component.
- **Truncation.** A five-point finite difference in h or ν, which removes the O(h²) and O(h⁴) remainders.
- **Population target.** The precision of the energy difference, not the walker number.
- **Finite-depth limits preserved.** Finite projection time and finite torus. No thermodynamic limit is inferred.

**Claims.**

- **(1) Three moments cannot lower-bound ω_min.** For the data (M_{−1}, M_0, M_1) = (12/35, 1, 3), there are positive three-atom measures with exactly these moments and a lowest atom at ω = 10⁻¹, …, 10⁻⁶. Its weight is forced below δ·M_{−1}, so it is invisible in the moments. So no statement about the lowest coupled excitation follows from M_{−1}, M_0, M_1.

- **(2) What the moments do certify: weight quantiles.**
  - Let ε = M_1M_{−1}/M_0² − 1 and ω̌ = M_0/M_{−1}.
  - Then at most a fraction ε(1 − η)/η² of the weight lies below (1 − η)ω̌, and at most ε(1 + η)/η² above (1 + η)ω̌.
  - The weight at or below δ is at most δ·M_{−1}.
  - ω_min ≥ w_0/M_{−1} whenever the lowest atom is known to carry weight w_0. That needs a weight bound the moments cannot give.

- **(3) The accuracy a dispersion statement needs.**
  - To certify "at most a fraction q of the weight lies below (1 − η)ω̌" by (2), one needs ε ≤ qη²/(1 − η).
  - For q = 0.1 and η = 0.05 that is ε ≤ 2.6 × 10⁻⁴.
  - So M_{−1}, M_0 and M_1 are needed to about 10⁻⁴ relative accuracy each.

- **(4) M_0 is an energy-only quantity.**
  - For H(ν) = H − ν·(1/3)Σ_a O_a² (diagonal in the σ basis), Hellmann–Feynman gives dE_0/dν at 0 = −⟨O²⟩ = −M_0, when ⟨O⟩ = 0.
  - So the structure factor needs no forward-walking estimator, which PR #9220 found biased on the larger tori.
  - Its shift, however, is O(1) against energies of O(N).

- **(5) The exact 2³ component** (864 states, k = π, cyclic triple).
  - The chain of PR #9236 is reproduced: 2.5173 ≤ 2.7754 ≤ 2.8724 ≤ 2.9728.
  - Hellmann–Feynman recovers M_0 = 1.012148056 to nine digits from energies.
  - But ε = 0.0711, which is 64 times the value needed for q = 0.1, η = 0.1. The three moments certify only that at least 0.747 of the weight lies in [ω̌/4, 7ω̌/4] and at least 0.858 lies below 2ω̌. The actual figures are 0.986 and 0.986.

**HIT.** (1) and (2) with their exact checks; (3) as their consequence; (4) and (5) as the checked 2³ case. Together they identify the first unresolved step.

## 2. Steps

**Step 1 — the identity behind everything. PROVED, CHECKED (A1, exact on 400 rational measures).**
- M_1M_{−1} − M_0² = ½ Σ_{ij} w_iw_j (ω_i − ω_j)²/(ω_iω_j) ≥ 0, with equality iff ν is a single atom. This is Lagrange's identity for the vectors (√(w_iω_i)) and (√(w_i/ω_i)).
- So M_0 ≤ (M_{−1}M_1)^{1/2}. Also ω_min ≤ M_0/M_{−1} (from M_{−1} ≤ M_0/ω_min) and M_0/M_{−1} ≤ M_1/M_0 (from the identity). A2 checks the chain exactly.

**Step 2 — stability of the Cauchy–Schwarz bound. PROVED, CHECKED (A3, A5).**
- **The integral.** Σ w (ω − ω̌)²/ω = M_1 − 2ω̌M_0 + ω̌²M_{−1}. At ω̌ = M_0/M_{−1} this equals M_1 − M_0²/M_{−1} = ε·ω̌·M_0. A5 checks this exactly.
- **Low side.** On {ω ≤ (1 − η)ω̌} the integrand (ω − ω̌)²/ω is decreasing in ω, so it is at least η²ω̌/(1 − η). Hence the weight there is at most ε(1 − η)/η²·M_0.
- **High side.** On {ω ≥ Ω}, with Ω > ω̌, the integrand is increasing, so it is at least (Ω − ω̌)²/Ω. At Ω = (1 + η)ω̌ the weight there is at most ε(1 + η)/η²·M_0.
- Checked exactly on the 400 rational measures at η = 1/10, 1/4, 1/2, 3/4, 9/10.

**Step 3 — Markov on the inverse moment. PROVED, CHECKED (A4).**
- The weight at ω ≤ δ is at most δ·M_{−1}, since each such atom contributes w/ω ≥ w/δ to M_{−1}.
- If the lowest atom has weight w_0, then M_{−1} ≥ w_0/ω_min gives ω_min ≥ w_0/M_{−1}.
- So a lower bound on ω_min needs a lower bound on w_0. The three moments cannot supply it (Step 4).

**Step 4 — the counterexample (1). PROVED, CHECKED (A6), exact rationals.**
- The base measure is atoms at 5/2 and 7/2 of weight 1/2 each, with (M_{−1}, M_0, M_1) = (12/35, 1, 3).
- For each δ in {1/10, 1/100, …, 10⁻⁶}, solve the 3 × 3 rational system for weights at (δ, 11/4, 13/4) with the same three moments.
- The solutions are positive. The hidden atom's weight is 7.7 × 10⁻⁴ at δ = 1/10 and 7.2 × 10⁻⁹ at δ = 10⁻⁶.
- **The choice of flanking atoms matters.** Flanking atoms wider than the base (2 and 4) give a negative hidden weight, because ε cannot be matched. Narrower flanking atoms work.
- **Consequence.** No inequality in M_{−1}, M_0, M_1 alone can bound ω_min from below.

**Step 5 — the dispersion accuracy (3). PROVED from Step 2, CHECKED (A7).** Table of ε ≤ qη²/(1 − η): q = 0.1: 1.1 × 10⁻³ (η = 0.1), 2.6 × 10⁻⁴ (η = 0.05), 8.3 × 10⁻³ (η = 0.25); q = 0.05: 5.6 × 10⁻⁴, 1.3 × 10⁻⁴, 4.2 × 10⁻³.

**Step 6 — M_0 from energies (4). CHECKED (B6), floating point.**
- H(ν) = H − ν·O², with O² = (1/3)Σ_a O_a² a diagonal function of σ. By Hellmann–Feynman, E_0′(0) = −⟨0|O²|0⟩ = −(M_0 + ⟨O⟩²).
- On the 2³ component ⟨O_a⟩ = 0 for all three modes, so E_0′(0) = −M_0.
- The five-point derivative at ν = 10⁻³ gives 1.012148056, against the spectral sum 1.012148056.
- **The cost** (arithmetic, not measured). The shift νM_0 is O(1). The energy is E_0 = −u_0·N_p with u_0 ≈ 0.29–0.38 per plaquette.
  - Take ν = 0.1, M_0 ≈ 0.5 and a target relative accuracy of 10⁻⁴ in M_0. The energy difference then needs an absolute precision of about 5 × 10⁻⁶.
  - On 16³, with N_p = 12288, that is a relative precision of about 10⁻⁹ on the total energy.
  - By contrast χ comes from an extensive shift, (3N/4)h²χ.

**Step 7 — the exact 2³ case (5). CHECKED (B1–B9), floating point diagonalisation of the 864-state component.**
- The ground energy is −9.026721, with u_0 = 0.376113 per plaquette.
- M_1 = 3.008906971 = 2u_0s² to nine digits, with s = 2 at k = π.
- The chain 2.5173 ≤ 2.7754 ≤ 2.8724 ≤ 2.9728 is reproduced.
- The lowest coupled level (2.5173) carries 0.249 of M_0. The bound ω_min ≥ w_0/M_{−1} gives 0.69, against the true 2.52.
- ε = 0.0711. The certificate table (η against the weight below and above) is in the log; at η = 0.75, at least 0.747 of the weight lies in [ω̌/4, 7ω̌/4]. The actual value is 0.986.
- The exact measure is far from a single mode, so near-saturation is not available on this torus.

## 3. Where it stops

- **Scope of the 2³ case.** It is the only torus whose spectral measure is computed here.
  - The larger tori's moments are not known to this attempt, so ε on 6³–16³ is unknown.
  - Their χ̄ values come from PR #9236's projector. They are consistent with near-saturation (ω_min bound ≈ 1.03–1.05 s(k)) but S was measured only by biased forward walking.
- **What this attempt does not decide.** Whether ε is small on the larger tori. That depends on M_0, which needs the energy route of Step 6 at a precision the projector may not reach.
- **The bounds are model-independent.** Steps 1–5 hold for any positive spectral measure. They say nothing specific to the ring model beyond Step 7.
- **Not covered:** PR #9239's softening towards the RK point; the finite-box (region) regulator of PR #9220; whether the measure's low-frequency weight can be bounded by other means.

## 4. What would finish it

1. A rigorous certified value of M_0(k) on 6³–16³ at about 10⁻⁴ relative accuracy, by the Hellmann–Feynman route or an independent one. Then ε(k) is known, and the quantile statement of Step 2 either holds or does not.
2. An independent lower bound on the weight of the lowest transverse level, or a spectral gap bound above it. Without one, ω_min is not determined by any moments.
3. The same at several k, so that ε(k) ≤ qη²/(1 − η) holds uniformly and the ratio ω̌(k)/s(k) can be compared across k with error bars smaller than η.

## Prior art

- The moment inequalities are the classical single-mode (Feynman–Bijl) bounds and Cauchy–Schwarz on the spectral measure. The stability estimate (Step 2) is a Markov argument on the residual of that inequality.
- Hellmann–Feynman is standard.
- The non-uniqueness of a measure with three prescribed moments is the standard moment problem, made explicit here with exact rational witnesses.
- Not in the landed notes and not in PR #9236: the quantile certificate, the accuracy table, the counterexample family and the energy-only M_0.

## Check

`python3 check.py` runs in about 3 seconds. Section A is exact (Fractions and sympy). Section B diagonalises the exact 2³ component in float64 and is labelled as such. It prints `SUMMARY: PARTIAL …` and `HIT: …`.
