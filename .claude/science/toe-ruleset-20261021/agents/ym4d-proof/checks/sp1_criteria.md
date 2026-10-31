# sp1 criteria — pre-registered PASS/FAIL verdicts for target T55-R (`SPD_SIGMA.md`)

Written 2026-10-28T22:08Z, **after** `SPD_SIGMA.md` §S0 and **before** `sp1_sigma.py` exists.
No constant below is derived in this session: L, d and the exponents −3, +4, −2, +4 are read from
`BFT_A.md` l.1510-1512 and l.1024-1048; σ, α, θ are free parameters of the gate, not measurements.

Arithmetic: exact `fractions.Fraction` and Python ints only. No numpy, no BLAS, one thread, no
numeric lock (rule 6). Nothing here is floating point, so there are no tolerances.

---

## sp1-A — the §18.5 Step 3 exponent identity

For every integer triple with 0 ≤ l < m ≤ k, k ≤ 12, the integer
`E(k,l,m) := -3*(k-l) + 4*(m-l) - 2*(k-l) + 4*(k-m)` must equal `-(k-l)`.

- **PASS** iff the identity holds at every triple in the grid.
- **FAIL** otherwise, and then the σ-generalisation of §18.5 Step 3 is not a bookkeeping change and
  this target's §S4 is withdrawn.

## sp1-A′ — the σ-shifted identity

With the (SPD-H_σ) weight, the same quantity shifted by `(1-σ)*(m-l)` must equal
`-(k-l) + (1-σ)*(m-l)`. Checked exactly at σ ∈ {1, 3/4, 1/2, 1/4, 1/8} over the same grid.

- **PASS** iff equality is exact (Fraction) at every (triple, σ).
- **FAIL** otherwise.

## sp1-B — the closed form of the double sum

Claim to be tested: for L ≥ 2 an integer and 0 < σ ≤ 1 with L^σ rational,

    Σ_{t=1}^{∞} Θ_σ(t) L^{-t}  =  1 / ((L-1)(1 - L^{-σ})),   Θ_σ(t) := Σ_{j=0}^{t-1} L^{(1-σ)j}.

Tested at (L, σ) ∈ {(3,1), (9,1/2), (16,3/4), (16,1/4), (81,1/4), (4,1/2)} by exact partial sums to
t = T_max with a rigorous exact tail bound: for σ < 1 the tail Σ_{t>T} Θ_σ(t)L^{-t} ≤
L^{-σT}·L^{-σ}/((L^{1-σ}-1)(1-L^{-σ})); for σ = 1 the tail is Σ_{t>T} t L^{-t} ≤ (T+2)L^{-T}/(L-1)·L/(L-1).

- **PASS** iff |partial sum − closed form| ≤ tail bound, exactly, at every (L, σ), for T_max = 60.
- **PARTIAL** if it holds for some (L, σ) and not others — then report which.
- **FAIL** otherwise, and §S4's constant must be restated.

## sp1-C — convergence of the CO-B_σ Hölder sum

`S(α,σ,L,T) := Σ_{t=1}^{T} E_σ(t) L^{-(1-α)t}`, `E_σ(t) := (t+1)Θ_σ(t+1)`.

The gate is a **Cauchy-ratio** gate, not an eyeball: let `rho(T) := S(α,σ,L,T) / S(α,σ,L,T-1)`.

- **PASS** iff, at every tested (α, σ) with `0 < α < σ ≤ 1`, the increment ratio
  `(S(T) - S(T-1)) / (S(T-1) - S(T-2))` is ≤ `9/10` for all 10 ≤ T ≤ 40 (geometric decay, hence
  convergence), **and** `S(40) ≤ 10^6`.
- **FAIL** otherwise.

Tested pairs with α < σ: (α,σ) ∈ {(1/4,1/2), (1/8,1/4), (1/16,1/8), (1/4,1), (1/2,3/4)} at L = 3.

## sp1-D — DESIGNED-FAIL CONTROL: σ = 0

Run sp1-B's and sp1-C's gates at σ = 0.

- The control **FIRES** (the intended outcome) iff sp1-B's closed form is singular at σ = 0
  (denominator `1 - L^{-0} = 0`) **and** sp1-C's increment-ratio gate is violated at σ = 0 for every
  α ≥ 0 tested, with `S(40)` exceeding 10^6 at α = 1/4.
- If the control does **not** fire — i.e. if σ = 0 passes the same gates — then the gates cannot
  decide anything and §S4 and §S5 of `SPD_SIGMA.md` are withdrawn as unsupported.

## sp1-E — DESIGNED-FAIL CONTROL: α = σ

Run sp1-C's gate at α = σ for σ ∈ {1/2, 1/4}.

- The control **FIRES** iff the increment-ratio gate is violated (ratio → 1 from below is not ≤ 9/10
  for large T) at both σ.
- If it does not fire, the claim "CO-B_σ needs α < σ strictly" is not supported by this check and must
  be labelled on the algebra alone.

## sp1-F — DESIGNED-FAIL CONTROL: a wrong exponent

Re-run sp1-A with the Step-3 exponent `+4*(m-l)` replaced by `+3*(m-l)` (a single-digit mutation of a
constant, not of an assertion).

- The control **FIRES** iff the identity then fails for some triple with m > l.
- If it does not fire, sp1-A is a tautology and carries no weight.

---

**What no gate here can decide.** These are gates on *bookkeeping*: they test the exponent algebra and
the convergence of the level sums, nothing else. They cannot test whether §18.5's and §23.4-23.11's
per-step bounds are correct, whether the (COMM) row has a centring cancellation, or whether any
statement in `BFT_A.md` is true. §S6 and §S7 of `SPD_SIGMA.md` are decided by proof or not at all, and
must be labelled accordingly.
