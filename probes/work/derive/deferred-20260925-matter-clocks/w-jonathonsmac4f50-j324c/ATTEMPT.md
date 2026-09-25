# Deferred science, unit 23 (PR #9164): when formation-weighted averaging dephases — attempt a1

Worker `w-jonathonsmac4f50-j324c`, model `claude-opus-5-5`. PR #9164 was written by a Claude session, the same model family. The referee should be of another family.

**Inspection before work.**
- `origin/main` is `ef918c1910ccf8b7a1125fbbdfc54eb84186176e`.
- The three bundled PR #9164 sources verify against their SHA256. The accepted paths on main match `accepted_sha256`.
- The landed note, `docs/FORMATION_RATE_FUNCTIONS_THE_AXIOM_TEXT_ADMITS_..._2026-09-24.md` (review findings: "both iterated infinite-window/slow-rate limits dephase; add exact finite-window controls"), gives:
  - the constant-clock window average `z = f[1 − e^{−(f−iω)T}]/[(f − iω)(1 − e^{−fT})]`, its two iterated limits, and "Both iterated limits eventually give the field-dephased average if T also tends to infinity";
  - hazards that are **supplied** ("a nonnegative measurable conditional hazard f(t)"), with "no admission classification".
- No attempt exists on `deferred-20260925-matter-clocks` or `deferred-20260925-conditional-dynamics`.
- `deferred-20260924-formation` (w-macbookpro9927a) works block 34's sphere-law memory, a different residual. Nothing from it is reused.

## 1. Statement attempted: one finite-window scaling question

**Setting.** The landed note's supplied setting; nothing is derived from the axioms.
- Qubit precession `r(t) = r_∥ + cos(ωt) r_⊥ + sin(ωt) ĥ × r_⊥`, with `ω = |h| > 0`.
- A **supplied** nonnegative measurable hazard `f(t)`, survival `S`, formation density `w = fS`.
- Formation before `T` has positive probability, and `w_T = w/(1 − S(T))`.

**Question.** When does the formation-weighted Bloch average `r̄_T = ∫_0^T w_T(t) r(t) dt` lose its perpendicular part (dephase)? In particular:
- does the joint limit exist for the constant clock (the landed note gives only iterated limits);
- do slow formation and long windows suffice for general hazards?

**Answer.**
- **(A) Characteristic function.** `r̄_T = r_∥ + Re z r_⊥ + Im z ĥ × r_⊥`, where `z = E[e^{iωτ} | τ < T]` is the characteristic function of the conditioned formation time at the precession frequency. So dephasing is exactly `z → 0`.
- **(B) Constant clock, joint bound.** For every `f, T > 0`, `|z| ≤ 2f/(ω(1 − e^{−fT})) ≤ 2(f/ω + 1/(ωT))`.
  - Hence the joint limit `(f, 1/T) → (0, 0)` exists along every path and is the dephased average. The two iterated limits are special paths.
  - Each term is sharp: to within a factor 2 for the `f/ω` term, and attained at `ωT = π` for the `1/(ωT)` term.
- **(C) Bounded variation suffices.** For any supplied hazard whose `w_T` has bounded variation, `|z| ≤ (w_T(0⁺) + w_T(T⁻) + TV(w_T))/ω`. This is `2 max w_T/ω` for a monotone or unimodal `w_T`, for example the landed linear hazard.
- **(D) Slow and long do not suffice.**
  - A hazard modulated at the precession frequency keeps `|z| = 1/2` (cosine modulation) or `z → 2/π` (half-period square wave), while `sup f → 0` and `T → ∞`.
  - Every probability density on `[0, T]` is the conditioned formation density of some supplied hazard.
  - A record-determined clock is constant between neighbour events (landed note). Neighbour events synchronized with the field phase would produce exactly the square wave.

**No clock is selected, and no formation law is derived.** The corrected fact that both iterated limits dephase is kept. No noncommutation claim is made: (B) shows the joint limit exists.

## 2. Steps

1. **PROVED and CHECKED (E1, E1b) — (A).**
   - Average the exact precession against the probability density `w_T`. `∫ w_T cos(ωt) = Re z` and `∫ w_T sin(ωt) = Im z`.
   - For the constant clock, `z` equals the landed note's formula (E1).
2. **PROVED and CHECKED (E2a–E2e) — (B).** With `x = f/ω`, `κ = fT`, `τ = ωT`:
   - `z = x(1 − e^{−κ}e^{iτ})/((x − i)(1 − e^{−κ}))`.
   - `|z|² = x²(1 − 2e^{−κ}cos τ + e^{−2κ})/((1 + x²)(1 − e^{−κ})²) ≤ x²(1 + e^{−κ})²/((1 + x²)(1 − e^{−κ})²)`. The difference is `2x²e^{−κ}(1 + cos τ)/(…) ≥ 0` (E2b).
   - So `|z| ≤ 2x/(1 − e^{−κ})`.
   - Lemma: `1/(1 − e^{−y}) ≤ 1 + 1/y`, because `(y + 1)(1 − e^{−y}) − y` vanishes at 0 and has derivative `y e^{−y} ≥ 0` (E2a).
   - Hence `|z| ≤ 2x(1 + 1/κ) = 2(f/ω + 1/(ωT))`. E2c spot-checks this at 64 points to 40 digits.
   - **Sharpness.** At fixed `T`, `f → 0`, `z → (e^{iωT} − 1)/(iωT)`, with modulus `2/π = 2/(ωT)` at `ωT = π` (E2d). At fixed `f`, `T → ∞`, `|z| → f/√(f² + ω²)` (E2e).
3. **PROVED — (C), Riemann–Stieltjes integration by parts.**
   - `z = ∫_0^T e^{iωt} dW(t)` with `W = ∫ w_T`. Then `iω z = [e^{iωt} w_T]_{0⁺}^{T⁻} − ∫ e^{iωt} dw_T(t)`.
   - So `ω|z| ≤ w_T(0⁺) + w_T(T⁻) + TV(w_T)`.
   - For monotone or unimodal `w_T` the right side is `2 max w_T`.
   - The landed linear hazard `βt` has a unimodal density with peak `√β e^{−1/2}` at `t = 1/√β` (E3). So it dephases jointly as `β → 0` with `βT² → ∞`.
4. **PROVED and CHECKED (E4a–E4d) — (D).**
   - **Every density is a hazard's.** For any probability density `w` on `[0, T]` and any `m ∈ (0, 1)`, the hazard `f = m w/(1 − m W)`, `W = ∫_0^t w`, has survival `1 − m W`, formation density `m w`, and formation probability `m` before `T` (E4b).
   - **Cosine modulation.** With `w = (1 + cos ωt)/T` and `T = 2πN/ω`, `z = 1/2` exactly for every `N` (E4a), while `sup f ≤ 2m/(T(1 − m)) → 0`.
   - **Half-period square wave.** The hazard `f₀` switched on only where `cos ωt > 0` has formation time uniform on the on-intervals as `f₀ → 0`, so `z → (1/π)∫_{−π/2}^{π/2} e^{iφ} dφ = 2/π` for every `N` (E4c). E4d checks it exactly over one period.
   - Along `f₀ = N^{−2}`, `N → ∞`, the rate goes to 0, the window grows, and `z → 2/π`.
   - The total variation of these densities stays of order `ω`, as (C) requires for any non-dephased case.

## 3. First failing step

None for the statement above.

**Scope.** Everything holds for the supplied single-site precession, with the field fixed. Many-site hazard laws, and whether any supplier of hazards meets the complete axiom set, remain open, as the landed note says.

## 4. What would finish it, and the next obligations

- **Sufficient conditions for record-determined clocks.** In an interacting two-site model, the neighbour-event times are themselves random, so resonance is not automatic.
  - A sufficient condition: the characteristic function of the neighbour-event process at `ω` decays.
  - A candidate counterexample: a neighbour whose record clock locks to the field phase.
- **Many-site hazard laws**, and the selection question: which supplied hazards meet the other axioms. The landed note leaves both open.
- **The interacting two-qubit trajectories of the landed runner.** Replace a single `ω` by the spectrum of the joint dynamics. The criterion becomes the characteristic function at each Bohr frequency.
