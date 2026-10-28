# gt1 / gt2 criteria — PRE-REGISTERED, written before any script exists

Written 2026-10-28, after GREENT.md §G0-§G1 and **before** `gt1_green.py` / `gt2_sweep.py` existed.
Owner: the Green's-tail worker (GREENT.md).

**No numeric threshold below is a constant derived in this session.** Every verdict is one of
(a) a structural 0/1 identity, (b) a comparison between two *independently computed* quantities (one from a proof
formula, one from an exact linear-algebra computation of the object itself), or (c) a monotonicity/growth separation,
which has no threshold at all. Where §G2's proven constants C_1, C_2 appear, they appear only on one side of an
inequality against a measured maximum; the criterion is "proof ≥ measurement", not "measurement ≤ <number>".

## Objects

Λ = (Z/R)^d. Scalar Laplacian (Δf)(z) := Σ_{μ=1}^d [2f(z) − f(z+e_μ) − f(z−e_μ)].
G = the mean-zero inverse of Δ, i.e. ΔG = δ_0 − R^{−d} and Σ_z G(z) = 0.
(∇_μ f)(z) := f(z+e_μ) − f(z). d, d^* = the standard cubic-lattice exterior derivative and its adjoint.
r(x) := |x|_2 with coordinates taken in (−R/2, R/2].

## gt1 — exact rational, d-dimensional Fourier representation (plain python `fractions`, no numpy, no BLAS, no lock)

Only R ∈ {3, 4, 6} admit exact rational arithmetic (cos(2πk/R) is rational exactly for R | 1,2,3,4,6; Niven), so the
exact runs are d ∈ {3, 4} × R ∈ {3, 4, 6}.

- **gt1-A (structural; CAN FAIL).** On 2-forms, (d d^* + d^* d)F = Δ F componentwise, entrywise exactly, for 10 random
  integer 2-forms at each (d, R). The operators d, d^* are assembled independently from the combinatorial incidence
  definition; Δ is assembled from its own formula above. The two sides share no code path.
  **PASS iff 0 discrepancies out of all entries. FAIL otherwise.**
  *Independent construction tested against:* the combinatorial complex, versus the scalar-Laplacian formula.
  *Why it can fail:* a sign or orientation convention error in d^*, or the tensor-product claim being false on 2-forms.

- **gt1-B (solver validation; a self-consistency clause, NOT evidence for the theorem).** The computed G satisfies
  ΔG = δ_0 − R^{−d} and Σ_zG(z) = 0 exactly (rational).
  **PASS iff 0 nonzero residual entries. FAIL otherwise.** Labelled as solver validation in the record.

- **gt1-C (the main bound; CAN FAIL).** Compute
  m_1(d,R) := max{ r(x)^{d−1}·|∇_μG(x)| : x ≠ 0, all μ } and
  m_2(d,R) := max{ r(x)^{d}·|∇_μ∇_λG(x)| : r(x) ≥ 2, all μ, λ }.
  **PASS iff C_1 ≥ m_1(4,R) and C_2 ≥ m_2(4,R) for every R ∈ {3,4,6}**, where C_1, C_2 are the constants that §G2's
  proof produces, evaluated by a routine that never reads G.
  **FAIL if either proven constant is below the exactly computed maximum** — that is, a FAIL here refutes §G2.
  *Independent construction tested against:* the exact rational Green's function, computed by d-dimensional Fourier
  inversion; the proof constants come from 1D heat-kernel inequalities and a time integral and share no code with it.

- **gt1-D (the moment-cancellation mechanism; CAN FAIL, and a FAIL refutes Proposition NL-8 (ii)).** For each (d, R)
  compute two responses:
  * **bare**: b_B := d^*Δ^{−1}(δ_P − mean) for a single level-0 plaquette source δ_P — i.e. one column of the kernel 𝒢;
  * **cancelling**: b_A := d^*Δ^{−1}(dB) for B a fixed 1-form supported on a single link (so dB is exact, hence of zero
    mean componentwise, and supported in a 2(d−1)-plaquette neighbourhood).
  Let ρ_A(s) := max{ r(x)^d|b_A(x)| : r(x) ∈ [s, s+1) } and ρ_B(s) likewise.
  **PASS iff, at the largest R available, ρ_B is strictly increasing over the available shells while ρ_A is not**, i.e.
  the zero-mean source gains the extra power and the bare kernel does not.
  **FAIL if ρ_B does not increase** (then the gate has no power: the d-th power would be satisfied by a source with no
  cancellation and gt1-D would be vacuous — pre-registered failure mode (G-F4)) **or if ρ_A increases** (then the
  claimed extra power is absent and Proposition NL-8 (ii) is refuted, outcome (G-O4)).
  *Independent construction tested against:* two exactly computed responses that differ **only** in whether the source
  has vanishing mean. This is the designed-FAIL control: ρ_B is the arm that is designed to fail the d-th-power claim.

## gt2 — float sweep for R-uniformity and the exponent (numeric lock taken, single thread, scalar python, no numpy)

Runs only if `uptime` load < 8 and the lock is obtained; otherwise reported as NOT RUN. Precision: IEEE double,
d-dimensional cosine sums, no array libraries. Points: the axis direction x = (s,0,0,0) and the diagonal
x = (s,s,s,s), s = 1 … ⌊R/2⌋, at d = 4, R ∈ {8, 12, 16, 24}.

- **gt2-E (R-uniformity; CAN FAIL).** M_1(R) := max_s s^{3}|∇_1G((s,0,0,0))| and the diagonal analogue.
  **PASS iff M_1(R) does not grow by more than a factor 2 between R = 8 and R = 24**, and likewise for the
  two-derivative quantity M_2(R) := max_{s≥2} s^{4}|∇_1∇_1G((s,0,0,0))|.
  (The factor 2 is a round bracket fixed here in advance; it is not derived from any computation of mine.)
  **FAIL if either grows past it** — that is pre-registered failure mode (G-F2), the R-leak.

- **gt2-F (the exponent is exactly d−1 and d; CAN FAIL, and it is the second designed-FAIL arm).**
  **PASS iff** s^{3}|∇_1G| is bounded (varies by less than a factor 2 over s ≥ 2 at R = 24) **while**
  s^{4}|∇_1G| grows monotonically over s ≥ 2 at R = 24, **and** s^{4}|∇_1∇_1G| is bounded while s^{5}|∇_1∇_1G| grows.
  **FAIL otherwise.** A FAIL of the first half refutes (GT-1)/(GT-2); a FAIL of the second half means the exponent test
  is vacuous (it would pass any exponent), which is (G-F4).

## Reporting rules adopted

A FAIL is reported as a FAIL; the failing script and output are kept unaltered; any re-run uses a new id with these
criteria untouched; any probe run after seeing a result is labelled **post-hoc**.
