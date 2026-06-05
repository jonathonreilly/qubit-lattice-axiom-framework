# Flavor — the Heisenberg–Weyl / Clifford symmetry axis does not force r=1/2: "self-dual at 1/√2" is a magnitude coincidence, F-covariance forces only the off-diagonal balance b=c, and the Clifford-intrinsic landmarks sit at r=1

**Date:** 2026-06-02
**Claim type:** open_gate.
**Review boundary:** source proposal for independent audit. No verdict or
downstream grade is set here.
**Runner:** `scripts/flavor_hw_clifford_does_not_constrain_r_2026_06_02.py` (SCORECARD 5/5).

## Question
The generation factor `ℂ³` carries the qutrit **Heisenberg–Weyl** group — shift `X = C` (the hopping,
coefficient `b`), clock `Z = diag(1,ω,ω²)`, Weyl relation `ZX = ωXZ`, and the Fourier transform `F`
(a Clifford element) with `FXF† = Z`. Since `r=1/2 ⟺ |b|/a = 1/√2` is the equal-superposition
magnitude, does an HW/Fourier **self-duality** or HW-covariance *force* `r=1/2` — a symmetry principle
rather than an imported measure?

## Result — no. The symmetry axis adds no value-forcing principle.
1. **"Self-dual at 1/√2" is a magnitude coincidence, not a fixed point.** The pure-shift operator
   `H = aI + bX + b̄X²` is **not** an `F`-eigenoperator at `r=1/2`: `F` maps it onto the orthogonal
   *clock* line `aI + bZ + b̄Z²`, and `‖FHF† − H‖ = 2.449 ≠ 0`. `H` is `F`-fixed only at `b=0` (`r=0`).
   So `1/√2` satisfies no Fourier-eigen equation — the coincidence is purely verbal.
2. **The genuine F-self-dual family carries a free parameter.** The clock-augmented operator
   `K = aI + g(X + Z + X² + Z²)` is `F`-fixed for **all** `g` (verified at `g²= 0.01…6.25`), so
   `r = g²` is a **free dial**; `1/2` is an unmarked member. The only Clifford-intrinsic spectral
   landmark on the family is `det(K)=0` at `g²=1/4`, *not* `1/2`.
3. **HW-covariance forces the off-diagonal balance `b=c`, not r.** For the self-dual clock-enriched
   operator `G = aI + b(X+X²) + c(Z+Z²)`, `F`-invariance forces only `b=c` (equal shift- and
   clock-weight), while leaving the **diagonal `a` completely free** (verified). So even granting clock
   content, `r = |b|²/a²` stays free — the forced quantity is an off-diagonal symmetry, never the
   on-site:hopping ratio.
4. **`r` is Clifford-invariant but its value is unselected.** `Tr(H)/3` and the traceless HS norm are
   each separately conjugation-fixed, so `r` is meaningful and Clifford-invariant — but the Clifford
   group supplies no equation relating on-site to hopping. The genuinely Clifford-intrinsic
   discriminators (discrete-Wigner negativity onset, the PSD edge, full-orbit equal-amplitude) all land
   at **r=1**, giving the dimension default new independent positivity evidence — though not making
   r=1 forced either.

## Consequence
The symmetry axis re-confirms, from an independent direction, that **`r=1/2` is the unforced
equal-block Hilbert–Schmidt weight `3a²=6|b|²` (= `AC_φλ`)**, not a symmetry fixed point. Two genuine
new derived facts: the **`b=c` off-diagonal F-covariance constraint**, and the convergence of the
Clifford-intrinsic value-discriminators on **r=1**. Across measure, structure, action, and now
symmetry axes, the framework's native value is `r=1` (Q=1); `r=1/2` is the single unforced block-count
import.

## The next paths this opens (not closing)
- The `b=c` off-diagonal constraint is a clean derived fact worth testing against the CKM/quark
  sector (does equal shift=clock weight constrain mixing?).
- The genuinely untouched lever is the **readout class**: the signed-eigenvalue (Brannen) readout vs
  the singular-value (Yukawa) readout differ at `r=1/2`; whether a discrete-Wigner **sign** structure
  privileges the signed (comparator-compatible) readout that load-bears `Q=2/3` is unexamined.

## No-Go Discipline Gate

This gate is restricted to one route statement: the qutrit
Heisenberg-Weyl / Clifford symmetry axis tested here does not force the
Koide `r=1/2` value.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Pure-shift Fourier fixed point | Treat `|b|/a=1/sqrt2` as self-dual. | The operator is not Fourier-fixed at that value. |
| True Fourier self-dual family | Add clock terms and impose `F`-invariance. | The family is fixed for all `g`; `r` remains free. |
| Heisenberg-Weyl covariance | Force equal shift and clock weights. | It forces `b=c`, not the on-site/hopping ratio. |
| Clifford invariant ratio | Use invariance of trace and traceless norm. | The ratio is meaningful but unselected. |
| Positivity / Wigner landmarks | Use intrinsic Clifford landmarks. | The tested landmarks sit at `r=1`, not `r=1/2`. |
| Readout-sign route | Use the signed Brannen readout. | Open and independent of this symmetry-axis test. |

### N2 - Wall Independence

The collapsed residual is value selection. Off-diagonal symmetry and
on-site/hopping weighting are independent.

### N3 - Hidden-Wall Scan

"Self-dual" is used only for the explicit Fourier-conjugation equations in the
runner. No clock content or signed readout rule is smuggled in as an axiom.

### N4 - Residual Matching

The tested residual is `r=1/2` as a symmetry-fixed value. It is not a claim
about Koide readout class, scale, or cross-sector matching.

### N5 - Rhetoric Audit

The negative statement is route-local. It does not claim that every possible
symmetry or readout principle fails.

### N6 - Partial-Closure Path Scan

A future sign/readout theorem, block-count principle, or approved admission
could still select `r=1/2`. This note leaves those paths open.

### N7 - Steelman

A hostile reviewer can argue that the right symmetry object is not the
pure-shift operator but a larger clock-shift/readout package. The runner tests
one such self-dual family and finds `r` free, but broader packages remain open.

### N8 - Cross-Cycle Echo

This matches the broader flavor pattern: structural symmetries often make the
ratio well-defined without selecting the Koide value. The note adds the
Heisenberg-Weyl / Clifford instance of that split.

**Gate result:** pass for the narrow symmetry-axis boundary only.

## Provenance (verified 2026-06-02)
- Weyl relation and `FXF†=Z`; `‖FHF†−H‖>0` at r=1/2 (H not F-fixed); pure-shift F-fixed only at r=0;
  `K` F-fixed for all g (r free); `G` F-fixed iff `b=c` with `a` free: verified directly (runner 5/5).
  From the Heisenberg–Weyl symmetry-axis workflow (`wf_9d805980`).
- This note records that the tested HW/Clifford structure does not constrain
  `r` and re-confirms `r=1/2` as the unforced equal-block weight.
