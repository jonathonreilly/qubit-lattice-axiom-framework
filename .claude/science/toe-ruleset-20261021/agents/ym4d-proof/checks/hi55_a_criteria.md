# hi55_a — comparator-side exact identities (criteria, written before the script)

Owner: HINT55.md (Opus 5.5 worker, model claude-opus-5-5). Written 2026-10-28, after HINT55 PRE-STATED (23:45:27 UTC),
before `hi55_a_comparator.py` exists. Plain Python, `fractions.Fraction` only; no floats anywhere in a verdict.
Pseudo-random rationals from `random.Random(5501)`; momenta p ∈ Q⁴ with numerators in [-9, 9], denominators in [1, 7],
p ≠ 0. d = 4.

Definitions used (HINT55 §1): T^I_{μν,ρσ}(p) := p_μp_ρδ_νσ − p_μp_σδ_νρ − p_νp_ρδ_μσ + p_νp_σδ_μρ;
v^λ_{μν}(p) := p_μδ_νλ − p_νδ_μλ.

**A1 (Gram form and trace).** For 25 momenta: T^I_{μν,ρσ}(p) = Σ_λ v^λ_{μν}(p)v^λ_{ρσ}(p) for all 4⁴ index quadruples,
and Σ_{μ,ν}T^I_{μν,μν}(p) = 6p². PASS iff every equality is exact.
**A1-F (designed fail).** Same with the third term's sign flipped (+p_νp_ρδ_μσ). PASS of the control iff the Gram
equality FAILS for at least one momentum (the A1 gate can fail).

**A2 (gauge-parameter independence of the field-strength trace).** With D_μν := (δ_μν − (1 − ξ)p_μp_ν/p²)/p², compute
S := Σ_{μ,ν}[p_μp_μD_νν − p_μp_νD_νμ − p_νp_μD_μν + p_νp_νD_μμ]. PASS iff S = 6 exactly for ξ ∈ {0, 1/3, 1, 7/2, 10} at
25 momenta.
**A2-F (control).** p²Σ_μD_μμ = 3 + ξ must take at least 2 distinct values over the same ξ list (the A2 cancellation
is not automatic).

**A3 (contact-term counterexample).** ŝ_ε(u) := 1/u − ε + ε²u. With L_k(t) := k!/(2t)^{k+1} (the Gamma integral
∫_0^∞u^ke^{−2tu}du, used as a definition, not tested) put F_ε(t) := t²[L_1(t) − εL_2(t) + ε²L_3(t)]
(= (32π²/3)·t²⟨E(t)⟩ per unit coupling).
- (a) ŝ_ε(u) − ε = (1 − εu)²/u exactly, for ε ∈ {1, 1/3, 5} and 25 rational u > 0. PASS iff exact.
- (b) F_ε(t) = 1/4 − ε/(4t) + 3ε²/(8t²) exactly at 25 rational t > 0 and the three ε. PASS iff exact.
- (c) With ε = 1: F_1(t₂) − F_1(t₁) > 0 for (t₁, t₂) ∈ {(4, 8), (6, 12), (10, 1000), (7/2, 7), (3, 300)}. PASS iff all
  strictly positive.
- (d) Non-monotonicity (the sign is not automatic): F_1(1) − F_1(1/2) < 0. PASS iff strictly negative.
- (e) UV growth: F_1(1/k) ≥ k²/4 for k = 2, …, 50. PASS iff all hold.
**A3-F (control).** ε = 0: F_0(t₂) − F_0(t₁) = 0 exactly for the five pairs of (c) (massless free field: W = 0).

**A4 (leading-order coefficient).** (1/4)·6·(1/16)·L_1(1)·1 = 3/128 exactly, i.e. t²⟨E(t)⟩ = 3e²/(128π²) per colour
with the π² factored as in HINT55 §2.1. PASS iff exact.

Verdict: PASS iff A1, A2, A3(a)-(e), A4 PASS and both controls A1-F, A2-F, A3-F behave as stated. Load-bearing for
HINT55: A3 (the counterexample's arithmetic) and A1/A2 (the trace identity used in every comparator formula). A4 is a
cross-check of hand arithmetic.
