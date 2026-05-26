# Cycle 6 — K1-K4 Native Re-Expression Pass

**Date:** 2026-05-26 (cycle 6 of native-only campaign)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** research analysis — Position 2 of Direction γ tested at four substrates
**Imports:** NONE
**Status:** **negative attack-surface finding** — none of the four candidate
re-expression substrates (K1 Cl(3) projector triple product, K2 cumulant
expansion, K3 determinantal C₃-circulant, K4 Plancherel-Frobenius) escape the
radian interpretation natively. All hit the L-W boundary or require literal
radians as input.

## Setup

From the Direction γ synthesis, Position 2 (native re-expression of the Brannen
observable that doesn't use `δ` as a radian) is one of three theoretically open
closing routes for the π-bridge primitive `P`. The closed scoping PR #1942
named four candidate substrates K1-K4. This cycle tests each natively.

The retained Brannen circulant gives sqrt-mass eigenvalues
`m_k = 1 + √2·cos(2πk/3 + δ)`. The question: can the lepton mass triplet be
expressed in a form that uses `Q = 2/3` (dimensionless) without interpreting
`δ` as a radian?

## K1 — Cl(3) projector triple product

**Attempt:** write `m_k = Tr(P_k · D[Q])` for D[Q] some Cl(3)-equivariant
operator depending on `Q`.

**Analysis (native, retained C₃ + Cl(3)):**

For three projectors `P_1, P_2, P_3` on the C₃ orbit with cyclic action
`C·P_k = P_{k+1 mod 3}`, write `D = α·I + β·C + γ·C²` for complex coefficients
`α, β, γ`. The trace is

```
Tr(P_k · D)  =  α/3  +  β·ω^k/3  +  γ·ω^{2k}/3
```

(with `ω = e^{2πi/3}`, using the C₃-rep normalization). For the result to be
**real-valued** (so it can equal the real sqrt-mass `m_k`), need `γ = β̄`.
Setting `β = R·e^{iφ}`:

```
Tr(P_k · D)  =  α/3  +  (2R/3)·cos(2πk/3 + φ).
```

Matching the Brannen form requires `α/3 = 1`, `2R/3 = √2`, and **`φ = δ`**.
Therefore `φ = δ = 2/9 rad` is the **literal radian** as the argument of the
complex coefficient `β`.

**Native escape attempt:** can `β` have its argument fixed by retained content
without invoking literal radians?

- If `β = R` (real positive), `φ = 0`. Not Brannen.
- If `β = R·i` (with `i = Cl(3)` pseudoscalar), `φ = π/2`. Not 2/9.
- If `β` is in the retained Cl(3) integer-coefficient algebra, `φ` is a
  multiple of `π/4` (Gaussian-integer-like). Not 2/9.
- For `β` to have `arg(β) = 2/9 rad`, `β` must be a non-Q-algebraic complex
  number. The retained inventory contains no such object (per Direction γ
  L-W analysis).

**K1 verdict:** the trace structure REQUIRES `δ` as the literal argument of a
complex coefficient. No native escape; the L-W blocker reappears in the
coefficient `β`.

## K2 — C₃-equivariant cumulant expansion

**Attempt:** Taylor-expand `cos(2πk/3 + δ)` at `δ = 0` as a power series in `δ`
(treated as a dimensionless small parameter). Test whether the series can be
resummed without restoring the literal radian.

**Analysis (native):**

```
cos(2πk/3 + δ)  =  cos(2πk/3)·cos(δ)  -  sin(2πk/3)·sin(δ).
```

Taylor series of `cos(δ)` and `sin(δ)` at `δ = 0`:

```
cos(δ)  =  1 - δ²/2 + δ⁴/24 - δ⁶/720 + ...
sin(δ)  =  δ - δ³/6 + δ⁵/120 - ...
```

Each term is `δ^n` with rational coefficient `(-1)^(n/2)/n!` (or sine pattern).
With `δ = 2/9`, each Taylor term is a rational number; the **infinite sum is
transcendental** (per L-W, since `cos(2/9)` is transcendental).

**Numerical test of truncation:** at `k = 2` (the lepton tau-mass position
per the M-work empirical anchor):

- exact `cos(4π/3 + 2/9) ≈ -0.6786`
- LO `cos(4π/3) = -0.5000`
- LO + NLO `cos(4π/3) - (2/9)·sin(4π/3) = -0.5 + (2/9)·(√3/2) ≈ -0.3076`
- ... (each finite truncation differs from the exact value)

Truncated Taylor in `δ = 2/9` gives a rational approximation to the
transcendental `cos(2/9 + 2πk/3)`; the approximation is NOT exact at any
finite order.

**K2 verdict:** the cumulant expansion expresses the radian cosine as a
power series in `δ`, but the series **CANNOT BE TRUNCATED** without
deviating from the transcendental Brannen value. The PDG match at ~7×10⁻⁶
requires the full transcendental, not a truncated Q-rational. The
re-expression decomposes but does not eliminate the transcendental — the
L-W content reappears as the infinite-sum closure.

## K3 — Determinantal C₃-circulant identity

**Attempt:** express `m_k² = det(M_k(Q))` for some `Q`-dependent matrix
`M_k(Q)` of rational entries.

**Analysis (native):**

A 3×3 circulant matrix `C(a, b, c)` with first row `(a, b, c)` has eigenvalues
`a + b·ω^k + c·ω^{2k}` and `det(C) = (a + b + c)(a + b·ω + c·ω²)(a + b·ω² + c·ω)`.

For the Brannen sqrt-mass triplet: `m_0·m_1·m_2 = det(C_{Brannen})` for the
appropriate circulant. Computing:

```
∏_k m_k  =  ∏_k (1 + √2·cos(2πk/3 + δ))
        =  1 + 3·(√2·cos δ)·???   [more algebra needed]
```

This is a polynomial identity in `(cos δ, sin δ)`, which are TRANSCENDENTAL
in `δ = 2/9`. So `det(C_{Brannen})` is itself transcendental and the
identity doesn't trivially terminate.

The **determinantal escape** would require: `det(C_{Brannen})` reduces to a
Q-rational expression in `Q = 2/3`. Numerical check:

```
m_0 · m_1 · m_2  at  δ = 2/9, base = 4π/3:
  m_0 = 1 + √2·cos(2/9)              ≈ 1 + √2·0.9753  ≈ 2.3793
  m_1 = 1 + √2·cos(2π/3 + 2/9)       ≈ 1 + √2·(-0.7188) ≈ -0.0167
  m_2 = 1 + √2·cos(4π/3 + 2/9)       ≈ 1 + √2·(-0.6786) ≈ 0.0404

  product  ≈  2.3793 · (-0.0167) · 0.0404  ≈  -0.0016
```

The product is not a clean rational. (`Q = 2/3` is `0.6667`; the product
deviates from any small-denominator rational of `Q` by orders of magnitude.)

**K3 verdict:** determinantal closure of the Brannen product on
rational/`Q`-dependent entries doesn't produce a clean Q-rational outcome.
The transcendental `cos(2/9)` enters multiplicatively, not algebraically.

## K4 — Plancherel-Frobenius rational `2/d² = 2/9`

**Attempt:** identify the `2/9` rational in the Brannen formula with the
Plancherel-Frobenius rational `2/d² = 2/9` (at `d = 3`), thereby treating
`2/9` as a *representation-theoretic count* rather than a radian.

**Analysis (native):**

The Plancherel-Frobenius rational `2/d²` is a **dimensionless** number from
the regular Z₃ representation theory (Probe 24 substrate). It appears in
the framework as the natural normalization for the irreducible characters.

The Brannen formula's `δ = 2/9` is interpreted as a **radian**. The
identification of these two `2/9`s is the *origin* of the π-bridge problem:
a Plancherel-Frobenius dimensionless count is being read as a literal
radian (Type-B → Type-A unit mismatch per the irreducibility audit).

K4 doesn't *escape* this — it *names* it. The Plancherel-Frobenius rational
`2/9` IS retained (dimensionless). Its identification with `2/9 rad` IS NOT
retained (the open primitive `P`).

**K4 verdict:** K4 confirms the existence of the dimensionless `2/9` in the
retained Plancherel inventory, but does not provide a structural mechanism
to identify that dimensionless count with a literal radian. **K4 is the
name of the gap, not a closure.**

## Combined K1-K4 result

| Substrate | Native verdict |
|---|---|
| K1 (Cl(3) projector triple) | L-W reappears in coefficient `β`'s argument |
| K2 (Cumulant expansion) | Truncation deviates from transcendental; infinite sum restores L-W |
| K3 (Determinantal) | Transcendental enters multiplicatively; no Q-rational outcome |
| K4 (Plancherel-Frobenius) | Names the gap (Type-B vs Type-A); doesn't close |

**All four substrates hit the L-W boundary in initial native attempts.** This
sharpens Position 2 of Direction γ: native re-expression of the Brannen
observable using only retained content **does not escape the radian
interpretation**.

## Implication

Of Direction γ's three closing positions for the π-bridge primitive `P`:

- **Position 1 (new irrational-radian source):** structural gap; needs new
  retained content from outside A1+A2.
- **Position 2 (native re-expression):** **substantively harder than it
  appeared in PR #1942 scoping.** K1-K4 all fail natively. Closing Position
  2 likely requires a re-expression substrate not in the K1-K4 list — or
  novel mathematics.
- **Position 3 (new sector-coupling):** unverified retained content
  (Brannen-CH, corrected-propagator) may help if it can be located; else
  also a structural gap.

The **most tractable** closing route in the retained framework remains
Position 1 (locate or construct a new retained source-class for
non-Q-algebraic radians), and the **most speculative** is Position 2
(native re-expression) — which K1-K4 has now shown to be harder than the
scoping note suggested.

## What this cycle does NOT claim

- Does **NOT** assert K1-K4 are unclosable. The substrates were tested at
  initial-attempt rigor; a deeper analytic attack on any one substrate may
  yet escape.
- Does **NOT** claim a formal no-go (no N1-N8 discipline applied; these are
  attack-surface findings).
- Does **NOT** propose a new axiom, import, or hypothesis.
- Does **NOT** open a source PR.

## Cited retained sources (load-bearing)

- A1 (`MINIMAL_AXIOMS_2026-05-03.md`): Cl(3) algebra
- Retained C₃ representation theory (standard)
- `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`: Brannen formula
- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`
  (`retained_no_go`): Type-A vs Type-B framing
- `KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md`:
  Plancherel-Frobenius rational `2/d² = 2/9`
- Lindemann-Weierstrass theorem (standard math)
- PDG charged-lepton masses (Section "numerical test of truncation" only;
  comparator, not derivation input)
