# Flavor — the Heisenberg–Weyl / Clifford symmetry axis does not force r=1/2: "self-dual at 1/√2" is a magnitude coincidence, F-covariance forces only the off-diagonal balance b=c, and the Clifford-intrinsic landmarks sit at r=1

**Date:** 2026-06-02
**Claim type:** a symmetry-axis result (HW/Clifford structure does not constrain the value r; it re-confirms r=1/2 as the unforced equal-block weight). Not closure.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade.
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

## Provenance (verified 2026-06-02)
- Weyl relation and `FXF†=Z`; `‖FHF†−H‖>0` at r=1/2 (H not F-fixed); pure-shift F-fixed only at r=0;
  `K` F-fixed for all g (r free); `G` F-fixed iff `b=c` with `a` free: verified directly (runner 5/5).
  From the Heisenberg–Weyl symmetry-axis workflow (`wf_9d805980`).
- This note sets no audit status; it records that the HW/Clifford structure does not constrain r and
  re-confirms r=1/2 as the unforced equal-block weight.
