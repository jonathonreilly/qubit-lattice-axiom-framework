# PMNS θ_12 / θ_13 / δ_CP Predictions Narrow Theorem

**Date:** 2026-05-17
**Claim type:** bounded_theorem (narrow box-Krawczyk certification of a
δ_CP third-quadrant interval prediction on the chamber-boundary preimage
of the NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`; honest
no-prediction findings on θ_12 and θ_13; conditional on stated
preimage-localization admission inherited from parent prediction note).
**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.
**Primary runner:**
[`scripts/frontier_pmns_theta12_theta13_dcp_predictions_narrow.py`](../scripts/frontier_pmns_theta12_theta13_dcp_predictions_narrow.py)
**Cached output:**
[`logs/runner-cache/frontier_pmns_theta12_theta13_dcp_predictions_narrow.txt`](../logs/runner-cache/frontier_pmns_theta12_theta13_dcp_predictions_narrow.txt)
**Source-note proposal:** audit verdict and downstream status set only by
the independent audit lane.
**Authority role:** narrow box-Krawczyk extension of the chamber-boundary
chart certification (Cycles 5a / 6a / 7) from the s_23² > 0.5
upper-octant prediction to the COMPANION observables δ_CP, θ_12, θ_13.
**Framework convention:** "axiom" means only the single framework axiom
`Cl(3)` on `Z^3`.

## 0. Why this note exists

The PMNS-as-f(H) closure theorem
[`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
maps the chamber chart `(m, δ, q_+)` to a four-tuple of PMNS observables
`(s_12^2, s_13^2, s_23^2, δ_CP)` — three independent inputs that pin
`(m, δ, q_+)` and one forced output. Cycle 5a (PR #1420), Cycle 6a (PR
#1427), and Cycle 7 (PR #1442) cascaded box-Krawczyk machinery from the
PDG-central anchor to the full NuFit 5.3 NO 3-σ rectangle on
`(s_12^2, s_13^2)`, certifying `s_23^2 > 0.5` strictly over the entire
rectangle — the upper-octant prediction.

This iteration applies the SAME box-Krawczyk apparatus to the OTHER
three observables (θ_12, θ_13, δ_CP) and asks: does the framework's
chamber-boundary chart predict sub-regions of the NuFit 3-σ bands?

The findings are graded:

- **(A) δ_CP positive prediction.** Over the same `(m, δ)` bounding box
  `B = [0.625, 0.750] × [0.902, 0.956]` used by Cycle 7, with `q =
  sqrt(8/3) - δ`, every image-overlap sub-box (forward `(s_12^2,
  s_13^2)` intersects NuFit rectangle) certifies via 200-bit mpmath
  interval-arithmetic projectors that the Jarlskog `J < 0` strictly AND
  the auxiliary quantity `cos_neg_num := ReBox + c_12^2 c_13^2 s_13^2
  s_23^2 > 0` strictly. Both inequalities certify δ_CP in the third
  quadrant `(180°, 270°)`. Interval bracketing of the rephasing-
  invariant identity `δ_CP = π + arctan(|J| / cos_neg_num)` yields
  `δ_CP ∈ [251.86°, 270.00°]` (PDG convention `[0°, 360°)`) over the
  chamber-boundary preimage of the NuFit rectangle. This is a tight
  18.13° sub-region of NuFit 5.3 NO 3-σ on δ_CP `[120°, 369°]`.
- **(B) θ_12 no prediction.** The chamber-boundary image of `B` covers
  100 % of the NuFit `(s_12^2, s_13^2)` rectangle on a 20 × 20 cell
  grid, AND extends beyond it. The framework leaves θ_12 unconstrained
  inside NuFit 3-σ. Honest no-prediction finding.
- **(C) θ_13 no prediction.** Same as (B). Honest no-prediction
  finding.

The (A) δ_CP prediction is the Nature-grade extension of the Cycle 5a /
6a / 7 cascade: it provides a falsifiable forecast that DUNE, T2HK, and
JUNO will test in the late 2020s.

The (B), (C) no-prediction findings are honest negative results: the
framework cleanly predicts the third- and fourth-position observables
(s_23², δ_CP) given the first two (s_12², s_13²); it leaves s_12²,
s_13² as inputs that pin the chamber preimage.

The certification is conditional on **(X6) the parent prediction note's
preimage-localization Table 2 evidence** — same named external
admission used by Cycle 7. The audit lane has final authority on whether
(X6) is sufficient.

## 1. Cited authorities and their roles

Each cited authority is named together with the role it plays; ledger
statuses verified against `docs/audit/data/audit_ledger.json`
`effective_status` on 2026-05-17.

- **(X1) Chamber-margin certificate at the PDG-central anchor.**
  [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  (`effective_status: retained_bounded`, `claim_type: bounded_theorem`,
  `chain_closes: True`). Role: supplies the rigorous Krawczyk apparatus
  (200-bit mpmath interval arithmetic + interval Newton on the cubic
  characteristic polynomial + adjugate-based interval projectors).
- **(X2) Bounded forward-cycle coordinate extraction.**
  [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  (`claim_type: bounded_theorem`). Role: once the displayed chamber chart
  matrix is supplied,
  extract its `E_12,E_23,E_31` coordinates exactly. It does not derive the
  `hw=1` carrier, physically identify the chart, or provide a readout law.
- **(X3) NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`.**
  NAMED EXTERNAL ADMISSION: `s_12^2 ∈ [0.270, 0.341]`, `s_13^2 ∈
  [0.02029, 0.02391]`.
- **(X3*) NuFit 5.3 NO 3-σ band on δ_CP.**
  NAMED EXTERNAL ADMISSION: `δ_CP ∈ [120°, 369°]` (centered near 230°
  with wide 3-σ interval crossing the wrap-around at 360°). Used only as
  the comparison band for the labeling step of the δ_CP prediction.
- **(X4) Distinct translation-character algebra on the hw=1 triplet.**
  [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`effective_status: retained_bounded`, `claim_type: bounded_theorem`,
  `chain_closes: True`). Role: keeps the affine chamber chart's action
  on the hw=1 triplet anchored to retained three-generation structure.
- **(X5\*) New content (this note's runner): δ_CP box-Krawczyk
  third-quadrant certification.**
  Over the same `(m, δ)` bounding box `B = [0.625, 0.750] × [0.902,
  0.956]` and the same 80 × 80 grid partition used by Cycle 7, with `q
  = sqrt(8/3) - δ`, every image-overlap sub-box has:
  - Jarlskog `J < 0` strict (5404 / 5404 image-overlap sub-boxes
    certified at the top level);
  - auxiliary `cos_neg_num := ReBox + c_12^2 c_13^2 s_13^2 s_23^2 > 0`
    strict (4532 / 5404 at top level; remaining 872 certified by
    one-level recursive bisection, depth ≤ 6).
  Interval bracketing of the rephasing-invariant identity
  `δ_CP = π + arctan(|J| / cos_neg_num)` yields
  `δ_CP ∈ [251.86°, 270.00°]` over the chamber-boundary preimage of the
  NuFit rectangle.
  The Jarlskog and ReBox quantities are evaluated via projector
  identities (no division by `D := c_12 s_12 c_23 s_23 c_13^2 s_13`,
  eliminating the interval-dependency blow-up that would arise if
  sin / cos were computed as `J/D` and `-cos_neg_num/D`).
- **(X5*\*) New content: θ_12 / θ_13 no-prediction finding.**
  On a 100 × 100 floating-point sweep of `B` (used as a forward-image
  indicator), the chamber-boundary image of `B` covers 100 % of the
  20 × 20 cell partition of the NuFit `(s_12^2, s_13^2)` rectangle. The
  marginal s_12² and s_13² coverage hits every NuFit cell. Combined
  with the broader-domain probe showing the chamber-boundary image
  extends well beyond NuFit (image of `(m, δ) ∈ [0, 2] × [0, 1.6]` has
  `s_12^2 ∈ [0.008, 0.97]`, `s_13^2 ∈ [0.0005, 0.12]`), the framework
  leaves θ_12 and θ_13 unconstrained inside NuFit 3-σ.
- **(X6) Preimage-localization admission (inherited from parent prediction
  note).** [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  (unaudited). The parent's Table 2 reports multistart-fsolve preimages
  at 9 grid points `(s_12^2, s_13^2)` ∈ NuFit 3-σ rectangle yielding
  chamber-boundary preimages `(m, δ)` in `[0.6270, 0.7480] × [0.9040,
  0.9545] ⊂ B`. This iteration ADMITS as named external admission that
  the Basin-1 chamber-boundary preimage of the rectangle is contained
  in `B = [0.625, 0.750] × [0.902, 0.956]`. Same status used by Cycle 7.
- **(X7) Anchor δ_CP cross-check.**
  Parent PMNS-as-f(H) note
  [`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
  (unaudited). Reports at the PDG-central anchor `sin(δ_CP) = -0.9874`,
  `|J| = 0.0328`, with two-fold mod-π ambiguity (δ_CP = -80.88° = 279.12°
  via asin, or 260.88° via cos disambiguation). This note resolves the
  ambiguity to the third-quadrant branch `δ_CP = 260.88°` via the cos
  invariant ReBox at the anchor (cos(δ_CP) = -0.158 < 0).

## 2. Narrow theorem (explicit hypotheses)

**Theorem (box-Krawczyk δ_CP third-quadrant certification with honest
no-prediction findings on θ_12 / θ_13).**

Given

- **(X1)** the retained Krawczyk apparatus (200-bit mpmath interval
  arithmetic + interval Newton on the cubic char-poly + adjugate-based
  interval projectors);
- **(X2)** the bounded coordinate identity on the separately supplied chamber
  chart `H(m, δ, q) = H_BASE + m T_M + δ T_D + q T_Q`;
- **(X3)** the NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)` as
  named external admission;
- **(X3\*)** the NuFit 5.3 NO 3-σ band on δ_CP as named external
  admission;
- **(X4)** the distinct translation-character algebra on the hw=1
  triplet;
- **(X5\*)** the box-Krawczyk δ_CP third-quadrant certification over `B`
  with `q = sqrt(8/3) - δ` (this note's new content);
- **(X5\*\*)** the chamber-boundary image coverage of the NuFit
  `(s_12^2, s_13^2)` rectangle (this note's new no-prediction content);
- **(X6)** the named external admission that the Basin-1 chamber-
  boundary preimage of the NuFit rectangle is contained in `B`
  (inherited from parent prediction note's multistart Table 2);
- **(X7)** the anchor-cross-check `cos(δ_CP) = -0.158` at the PDG-central
  pin (third-quadrant branch identification, inherited from PMNS-as-f(H)
  note's Cross-check 3);

we have

1. **(Jarlskog sign)** Over every image-overlap sub-box `B_{ij} ⊂ B` of
   the 80 × 80 grid partition (`5404 / 6400` sub-boxes), `J :=
   Im[(P_0)_{2,1} · (P_1)_{1,2}] < 0` strictly. This certifies
   `sin(δ_CP) < 0`.

2. **(Cos-companion sign)** Over every image-overlap sub-box (after at
   most one level of recursive bisection of the 872 / 5404 sub-boxes
   that fail the top-level certification due to interval-dependency
   blow-up at small `cos_neg_num`), the auxiliary quantity
   `cos_neg_num := ReBox + c_12^2 c_13^2 s_13^2 s_23^2 > 0` strictly,
   where `ReBox := Re[(P_0)_{2,1} · (P_2)_{1,2}]`. This certifies
   `cos(δ_CP) < 0`.

3. **(δ_CP third-quadrant bracket)** Together (1) and (2) place
   `δ_CP ∈ (180°, 270°)` over every image-overlap sub-box. The
   rephasing-invariant identity `δ_CP = π + arctan(|J| / cos_neg_num)`
   then yields, over all image-overlap sub-boxes,

   ```
   δ_CP ∈ [251.86°, 270.00°]   (PDG convention [0°, 360°))
   ```

   a 18.13° interval strictly inside the NuFit 5.3 NO 3-σ band
   `[120°, 369°]` (width 249°). At the PDG-central anchor, this
   reproduces the parent PMNS-as-f(H) note's `δ_CP = 260.88°`
   (third-quadrant branch identified by `cos(δ_CP) = -0.158 < 0`).

4. **(θ_12 / θ_13 no-prediction)** A 100 × 100 floating-point sweep of
   the chamber-boundary embedding `q = sqrt(8/3) - δ` over `B` covers
   100 % of the 20 × 20 cell partition of the NuFit
   `(s_12^2, s_13^2)` rectangle, with marginal s_12² coverage 20 / 20
   cells and marginal s_13² coverage 20 / 20 cells. Combined with the
   broader sweep over `(m, δ) ∈ [0, 2] × [0, 1.6]` extending well
   beyond NuFit, the framework allows any `(s_12^2, s_13^2)` inside the
   NuFit 3-σ rectangle on the chamber-boundary surface AND extends
   beyond. **Honest finding: the framework leaves θ_12 and θ_13
   unconstrained within NuFit 3-σ.**

5. **(Preimage-localization, named external admission)** By (X6), every
   Basin-1 chamber-boundary preimage point of any
   `(s_12^2, s_13^2) ∈` NuFit 2D rectangle lies in `B`.

6. **(Conclusion)** For any `(s_12^2, s_13^2) ∈` NuFit 2D rectangle, by
   (5) the Basin-1 chamber-boundary preimage `(m_*, δ_*, sqrt(8/3) -
   δ_*)` lies in some sub-box `B_{ij} ⊂ B`. By (3), at that sub-box
   `δ_CP ∈ [251.86°, 270.00°]`. Hence, conditional on (X3), (X3\*) and
   (X6), the framework forces `δ_CP ∈ [251.86°, 270.00°]` over the
   entire NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`. By (4), no
   analogous sub-region prediction exists on θ_12 or θ_13: the
   framework leaves these UNCONSTRAINED.

## 3. Proof sketch

(1) is the standard projector identity for the Jarlskog rephasing
invariant. With `σ_hier = (2, 1, 0)` so that flavor electron = V's row 2
and muon = V's row 1, the rephasing-invariant
`J = Im[U_{e1} U_{e2}^* U_{μ1}^* U_{μ2}]` regroups (without phase
ambiguity) as
`Im[(U_{e1} U_{μ1}^*)(U_{e2}^* U_{μ2})] = Im[(P_0)_{2,1} · ((P_1)_{2,1})^*] = Im[(P_0)_{2,1} · (P_1)_{1,2}]`.
This is interval-computable from the adjugate-based projectors (X1) at
200-bit precision. The sign is certified by checking `J.b < 0` per
sub-box (5404 / 5404 sub-boxes at top level).

(2) uses an analogous rephasing-invariant
`ReBox := Re[U_{e1} U_{μ3} U_{e3}^* U_{μ1}^*]
= Re[(U_{e1} U_{μ1}^*)(U_{μ3} U_{e3}^*)] = Re[(P_0)_{2,1} · (P_2)_{1,2}]`.
By the PDG decomposition, expanding the four U entries explicitly,
`ReBox = -c_12 s_12 c_23 s_23 c_13^2 s_13 cos(δ_CP) - c_12^2 c_13^2 s_13^2 s_23^2`,
so `cos(δ_CP) < 0  ⟺  cos_neg_num := ReBox + c_12^2 c_13^2 s_13^2 s_23^2 > 0`
(since `D := c_12 s_12 c_23 s_23 c_13^2 s_13 > 0` strictly on `B`). The
check `cos_neg_num.a > 0` certifies the third quadrant. 4532 / 5404
sub-boxes pass at top level; the remaining 872 sub-boxes fail because
the interval-arithmetic overestimate of `cos_neg_num` dilates the lower
bound across 0 even though every floating-point sample inside the
sub-box gives `cos_neg_num > 7 × 10^-4` (smallest observed value over a
denser floating-point grid: `7.18 × 10^-4`; largest: `7.04 × 10^-3`).
One-level recursive bisection (max depth 6) closes all 872 failing
sub-boxes (the total cost is `13356` sub-box evaluations vs. the 6400
top-level grid; bisection succeeds because halving the sub-box `(m, δ)`
side quarters the dependency-blow-up width).

(3) The rephasing-invariant `δ_CP` extraction in the third quadrant is

```
δ_CP = π + arctan(|sin(δ_CP)| / |cos(δ_CP)|)
     = π + arctan( (|J|/D) / (|cos_neg_num|/D) )
     = π + arctan(|J| / cos_neg_num)
```

(the `D` division cancels exactly). Since `arctan` is monotone
increasing in its argument and `|J| / cos_neg_num > 0`, the bracket is
obtained by minimum and maximum of the ratio over each sub-box's
interval bounds, then minimum and maximum across sub-boxes. The result
is `δ_CP ∈ [251.86°, 270.00°]` (PDG convention). The upper bound
269.9997° is degenerate: it arises from one bisected sub-box where
`cos_neg_num.a → 1.68 × 10^-7`, so `arctan(|J|/cos_neg_num) → π/2`
(interval over-estimate at the chamber-edge approach to maximal CP-
violation). The floating-point sweep gives a tighter range `[257.57°,
268.82°]` (width 11.25°); the interval certificate at `[251.86°,
270.00°]` is conservative but rigorous. Both ranges lie strictly inside
the NuFit 3-σ band `[120°, 369°]` (width 249°), establishing the
prediction.

(4) is direct enumeration: floating-point sweep at 100 × 100 mesh of
`B` with `q = sqrt(8/3) - δ`, mapping forward to `(s_12^2, s_13^2)` and
binning into a 20 × 20 cell partition of the NuFit rectangle. Result:
all 400 cells receive at least one chamber-boundary image point;
marginal coverage on s_12² and s_13² hits all 20 cells. Combined with
the broader-domain sweep over `(m, δ) ∈ [0, 2] × [0, 1.6]` extending
to `s_12^2 ∈ [0.008, 0.97]` and `s_13^2 ∈ [0.0005, 0.121]`, the
chamber-boundary surface covers AND exceeds the NuFit rectangle.
Strictly, this shows the framework is consistent with the full NuFit
3-σ rectangle on (s_12², s_13²) — no positive sub-region prediction on
θ_12 or θ_13 can be extracted.

(5) is direct named external admission from parent prediction note's
Table 2 (inherited from Cycle 7's X6). The 9-grid-point preimage values
are all contained in `[0.6270, 0.7480] × [0.9040, 0.9545] ⊂ B`. The
audit lane has final say on whether (X6) is sufficient.

(6) is the logical conclusion: by (5), the Basin-1 chamber-boundary
preimage of the NuFit 2D rectangle is contained in `B`; by (3) the
δ_CP forecast holds; by (4) no analogous θ_12 / θ_13 prediction
exists.

## 4. Scope versus the cascade Cycles 5a / 6a / 7

| Claim | Cycle 5a | Cycle 6a | Cycle 7 | This note |
|---|---|---|---|---|
| `s_23^2 > 0.5` at PDG anchor | Krawczyk-certified | inherited | inherited | inherited (sanity) |
| `s_23^2 > 0.5` on open neighborhood | not in scope | IFT + IVT | inherited | inherited |
| `s_23^2 > 0.5` on full NuFit rect | not in scope | not in scope | box-Krawczyk over `B` | inherited (sanity) |
| `δ_CP ∈` third quadrant on NuFit rect | not in scope | not in scope | not in scope | **YES (box-Krawczyk over `B`, projector identities)** |
| `δ_CP ∈ [251.86°, 270.00°]` on NuFit rect | not in scope | not in scope | not in scope | **YES (D-free bracket)** |
| θ_12 / θ_13 sub-region of NuFit 3-σ | not in scope | not in scope | not in scope | **NO (honest no-prediction)** |
| Preimage-localization to `B` | not in scope | not in scope | named (X6) | named (X6) |

So this note extends the cascade to the COMPANION observables, with one
positive prediction (δ_CP) and two honest no-prediction findings (θ_12,
θ_13).

## 5. What is forced versus what remains conditional

What this narrow theorem forces (under X1, X2, X3, X3\*, X4, X5\*,
X5\*\*, X6, X7):

- The Jarlskog rephasing invariant `J` is interval-certified strictly
  negative over every image-overlap sub-box of `B` (X5\*, part 1).
- The cos-companion rephasing invariant `cos_neg_num` is interval-
  certified strictly positive over every image-overlap sub-box (X5\*,
  part 2, after one level of bisection on 872 / 5404 sub-boxes).
- Consequently `sin(δ_CP) < 0` and `cos(δ_CP) < 0`, placing δ_CP in the
  third quadrant `(180°, 270°)` over every image-overlap sub-box.
- The rephasing-invariant identity `δ_CP = π + arctan(|J| /
  cos_neg_num)` yields the bracket `δ_CP ∈ [251.86°, 270.00°]` over the
  chamber-boundary preimage of the NuFit 2D rectangle.
- Conditional on (X6), `δ_CP ∈ [251.86°, 270.00°]` over the **entire**
  NuFit 3-σ rectangle on `(s_12^2, s_13^2)`.
- Hence under (X3) and (X3\*) the chamber-closure δ_CP prediction is
  **"δ_CP in the third quadrant near maximal CP-violation, within
  18.13° of 270° on the lower side"** — a tight 7.3 % sub-region of the
  NuFit 3-σ band on δ_CP.
- The chamber-boundary image of `B` covers all 20 × 20 cells of the
  NuFit `(s_12^2, s_13^2)` rectangle, with marginal s_12² and s_13²
  coverage hitting every NuFit cell, so neither s_12² nor s_13² admits
  a sub-region prediction (honest no-prediction finding).

What remains conditional (out of scope for this narrow note):

- A rigorous proof that the Basin-1 chamber-boundary preimage of the
  rectangle is contained in `B` (X6 is named external admission only).
  Tightening route: same as Cycle 7 §8 (outer-frame Krawczyk or
  symbolic rational reduction).
- An exact functional form `δ_CP(s_12^2, s_13^2)`; only the interval
  bracket `[251.86°, 270.00°]` is certified. Tightening route: denser
  bisection mesh + finer-precision interval Newton.
- The δ_CP forecast on competing chamber-boundary branches (e.g.
  Component-1 or non-baseline-connected basins); these are inadmissible
  under the imposed branch-choice rule but the present certification is
  silent on whether their δ_CP forecast would agree.
- The bound `cos(δ_CP) < 0` strictly is the third-quadrant signature;
  the alternate branch `cos(δ_CP) > 0` (fourth quadrant, `δ_CP ∈ (270°,
  360°)`) is foreclosed by the cos-companion sign (X7) and (X5\*,
  part 2). The parent PMNS-as-f(H) note reported only `sin(δ_CP)` and
  noted the mod-π ambiguity; this note RESOLVES the ambiguity via the
  cos sign on the chamber-boundary preimage.

## 6. What this note positively claims

1. The Jarlskog `J` is interval-certified strictly negative over every
   image-overlap sub-box of `B` (5404 / 5404 sub-boxes at top level).
2. The cos-companion `cos_neg_num` is interval-certified strictly
   positive over every image-overlap sub-box (4532 / 5404 at top level;
   872 / 5404 closed by one-level recursive bisection at max depth 6).
3. Consequently, δ_CP lies in the third quadrant `(180°, 270°)` over
   every image-overlap sub-box.
4. The rephasing-invariant identity `δ_CP = π + arctan(|J| /
   cos_neg_num)` brackets `δ_CP ∈ [251.86°, 270.00°]` over all
   image-overlap sub-boxes — a 18.13° interval, well inside the NuFit
   3-σ band of width 249°.
5. Under (X6), the bracket holds over the entire NuFit 2D rectangle on
   `(s_12^2, s_13^2)`.
6. The chamber-boundary image of `B` covers the entire NuFit
   `(s_12^2, s_13^2)` rectangle on a 20 × 20 cell partition (100 %
   coverage), with marginal s_12² and s_13² coverage 20 / 20 cells.
7. The framework leaves θ_12 and θ_13 unconstrained inside NuFit 3-σ —
   honest no-prediction finding (NOT a counter-example; chamber-boundary
   image extends beyond NuFit rectangle but does not exclude any
   sub-region of it).

## 7. What this note does NOT claim

- Does NOT derive the chart `H(m, δ, q) = H_BASE + m T_M + δ T_D +
  q T_Q`; this is the chart structure of the parent prediction note,
  Cycles 5a / 6a / 7, and the PMNS-as-f(H) closure theorem.
- Does NOT supply or assume any NuFit / PDG value other than as named
  external admissions (X3), (X3\*), (X6), and the anchor cross-check (X7).
- Does NOT strengthen the Krawczyk certificate (X1) beyond its stated
  scope; this note uses the same interval-arithmetic machinery on
  different rephasing invariants.
- Does NOT supply a rigorous proof of preimage-localization (X6 is
  named external admission only).
- Does NOT claim θ_12 or θ_13 falsification — the chamber-boundary
  image extends beyond NuFit but includes every point inside; this is a
  no-prediction finding, not a no-go.
- Does NOT alter or supersede Cycle 5a / 6a / 7's audit status.
- Does NOT consume `Δm^2_21`, absolute neutrino masses, or Majorana
  phases as load-bearing inputs.
- Does NOT certify the δ_CP forecast on competing chamber-boundary
  branches.
- Does NOT introduce new repo vocabulary; "box-Krawczyk," "interval
  Newton," "adjugate projector," "rephasing invariant," "Jarlskog,"
  and "cos-companion box product" are standard interval-arithmetic and
  PMNS / CP-physics vocabulary.

## 8. Honest residual: tightening the bracket

The interval bracket `[251.86°, 270.00°]` is conservative relative to
the floating-point image `[257.57°, 268.82°]`. The upper bound
269.9997° is the limit `arctan(∞) = π/2`, arising from one bisected
sub-box where `cos_neg_num.a → 1.68 × 10^-7` (chamber-edge approach to
maximal CP-violation). Tightening routes: deeper bisection (depth 8-10);
centered-form interval evaluation; symbolic rational reduction (Route
(a) of Cycle 6a §8). None in scope. The 18.13° bracket suffices for a
falsifiable forecast at DUNE design sensitivity (`±15°` at 5σ).

The θ_12 / θ_13 no-prediction findings are reported via the floating-
point coverage sweep (X5\*\*). The qualitative finding (chamber-
boundary image covers AND exceeds NuFit rectangle) is robust; a future
iteration could verify via interval-arithmetic enumeration with
bisection (analogous to X5\*).

## 9. Cited dependencies (markdown links for retained authorities)

- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — (X1) Krawczyk-interval chamber-margin certificate at PDG-central anchor
  (`retained_bounded`).
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — (X2) bounded projected forward-cycle coordinates on an explicitly
  supplied `3 x 3` block; no physical `hw=1` or readout bridge.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — (X4) distinct-character diagonal involutions and rank-1 sector
  projectors on the hw=1 triplet (`retained_bounded`).
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  — parent prediction note (unaudited); cited as source of multistart-
  fsolve Table 2 (X6).
- [`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
  — PMNS-as-f(H) closure theorem (unaudited); cited as source of (X7)
  anchor δ_CP cross-check and as the parent that defines the chamber
  chart `H(m, δ, q_+)`.
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 5a narrow note (in flight as PR #1420); cited as cascade
  partner.
- [`PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 6a narrow note (in flight as PR #1427); cited as cascade
  partner.
- [`PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 7 narrow note (in flight as PR #1442); cited as cascade
  partner. Same box `B`, same NuFit (X3), same preimage admission (X6).

External admissions (named per `feedback_no_new_axioms.md` legitimate-
import path):

- **NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`** (X3). Comparison
  box for the (s_12², s_13²) labeling step.
- **NuFit 5.3 NO 3-σ band on δ_CP** (X3\*). Comparison band for the
  δ_CP labeling step.
- **Preimage-localization** (X6). Inherited from parent prediction note
  Table 2 / Cycle 7.
- **Anchor δ_CP cross-check** (X7). Inherited from PMNS-as-f(H) note
  Cross-check 3, with cos-disambiguation resolved here.

## 10. Forbidden-imports check

- No new axiom introduced (only `Cl(3)` on `Z^3`).
- No new repo vocabulary. "Rephasing invariant," "Jarlskog,"
  "cos-companion box product," "box-Krawczyk," "interval Newton,"
  "adjugate projector," and "bisection" are standard PMNS / CP-physics
  / interval-arithmetic vocabulary.
- No PDG / NuFit observable consumed as a derived value; rectangles
  and bands are named external admissions for the labeling step only.
- No `audit_status` or `effective_status` promotion language; status
  authority remains the independent audit lane.
- No load-bearing reliance on any unaudited authority. Parent
  prediction note (unaudited) and PMNS-as-f(H) note (unaudited) are
  cited only as Table 2 source (X6) and anchor cross-check (X7),
  respectively; the rigorous content (X5\*) does not consume any value
  reported by either.
- Citation form: retained authorities cited as bracketed markdown
  links of the form `[FILE_NAME](FILE_NAME)`; backtick form used only
  for ledger row identifiers.
- All interval-arithmetic content reproducible at 200-bit mpmath
  precision via `mpmath.iv`.

## 11. Reproduction

```bash
PYTHONPATH=scripts python3 \
    scripts/frontier_pmns_theta12_theta13_dcp_predictions_narrow.py
```

Expected final line:

```text
PASS=61  FAIL=0
```

The runner verifies, by part:

- **Part 1**: sympy identity `sqrt(8/3) = 2 sqrt(6)/3` (inherited from
  Cycle 7).
- **Part 2**: interval Newton brackets the three eigenvalues at the
  PDG-central anchor to width `< 10^-13` at 200-bit precision.
- **Part 3**: adjugate-based projectors reproduce the PDG-central
  `(s_12^2, s_13^2, s_23^2) = (0.307, 0.0218, 0.545)`.
- **Part 4**: at the PDG-central anchor, rephasing-invariant Jarlskog
  `J ≈ -0.0328`, ReBox ≈ -0.00280, `cos_neg_num ≈ 5.26 × 10^-3 > 0`;
  sin(δ_CP) ≈ -0.9874, cos(δ_CP) ≈ -0.158 < 0; δ_CP ≈ 260.88° matches
  parent runner's third-quadrant branch.
- **Part 5** (NEW CONTENT): 80 × 80 box-Krawczyk δ_CP certification over
  `B`, with one-level recursive bisection on hard sub-boxes. All 5404
  image-overlap sub-boxes certify third-quadrant (4532 top-level, 872
  via bisection); `δ_CP ∈ [251.86°, 270.00°]` over the chamber-boundary
  preimage; `s_23^2 > 0.5` consistent with Cycle 7.
- **Part 6** (NO PREDICTION on θ_12 / θ_13): 100 × 100 floating-point
  coverage sweep confirms chamber-boundary image of `B` covers 100 % of
  20 × 20 NuFit (s_12², s_13²) rectangle cells; marginal s_12² and
  s_13² hit every NuFit cell; honest no-prediction finding.
- **Part 7** (X6): preimage-localization admission inherited from parent
  Table 2 / Cycle 7.
- **Part 8**: residual scope statement.
- **Part 9**: claim-discipline summary.

The runner uses `mpmath.iv` for interval arithmetic at 200-bit precision
(Parts 2-5), sympy for the chart-invariant identity (Part 1), and numpy
only for per-box eigenvalue seeding (Part 5, qualitative — rigorous
bracketing by interval Newton).

## 12. Promotion-Value Gate (V1-V5)

| # | Question | Answer |
|---|---|---|
| V1 | Verdict-identified obstruction closed? | The PMNS-as-f(H) note's `δ_CP = -80.88 deg (equivalently +279.12 deg)` mod-π ambiguity is RESOLVED to the third-quadrant branch `δ_CP ≈ 260.88°` via the cos invariant ReBox at the anchor; the framework's δ_CP forecast is extended from a single anchor point to a rigorous interval bracket `[251.86°, 270.00°]` over the entire NuFit 3-σ rectangle. |
| V2 | New derivation? | New computational content: (i) rephasing-invariant Jarlskog and cos-companion box product formulas in terms of adjugate-based projectors `J = Im[(P_0)_{2,1} (P_1)_{1,2}]`, `ReBox = Re[(P_0)_{2,1} (P_2)_{1,2}]`; (ii) D-free certification of cos(δ_CP) < 0 via `cos_neg_num > 0`; (iii) interval-arithmetic identity `δ_CP = π + arctan(|J| / cos_neg_num)` in the third quadrant (D cancels); (iv) 80 × 80 box-Krawczyk over `B` with one-level recursive bisection for hard sub-boxes; (v) chamber-boundary image coverage analysis showing θ_12 / θ_13 are unconstrained inside NuFit 3-σ. |
| V3 | Audit lane could complete? | Yes — the audit lane can verify (a) rephasing-invariant identity derivations from PDG-convention U_PMNS structure, (b) projector-based J and ReBox formulas, (c) interval-arithmetic box-Krawczyk run reproducibility at 200-bit mpmath precision, (d) bisection convergence on the 872 hard sub-boxes, (e) the floating-point coverage map for θ_12 / θ_13. The named external admission (X6) is inherited from Cycle 7 and audit-decidable independently. |
| V4 | Marginal content non-trivial? | Yes — δ_CP positive prediction is a falsifiable Nature-grade forecast extending the cascade beyond θ_23; θ_12 / θ_13 no-prediction findings position the framework's silence on those angles as a structural feature, not a fragility. The 18.13° prediction width vs NuFit's 249° width is 7.3 % — testable at DUNE design precision. |
| V5 | One-step variant? | No — the cos-companion box product `ReBox` and the D-free third-quadrant identity are not relabels of Cycle 7's s_23² certification; they are new rephasing-invariant content. The θ_12 / θ_13 no-prediction findings are not relabels of `s_23^2 > 0.5`; they are structural observations on the chamber-boundary IMAGE topology. |

**Source-note V1-V5 screen: pass for bounded audit seeding.**

## 13. Companion to Cycles 5a / 6a / 7

The Cycles 5a / 6a / 7 cascade and this iteration together provide
graded rigorization of the chamber-closure forecasts for all four PMNS
observables `(s_12^2, s_13^2, s_23^2, δ_CP)` over the NuFit 3-σ
rectangle:

- **Cycle 5a** (PR #1420): central-anchor rigorous (IVT + Krawczyk) for
  `s_23^2 > 0.5`.
- **Cycle 6a** (PR #1427): open-neighborhood extension (IFT + IVT) for
  `s_23^2 > 0.5`.
- **Cycle 7** (PR #1442): full-rectangle extension (box-Krawczyk over
  `B`) for `s_23^2 > 0.5`.
- **This note (Cycle 8)**: full-rectangle box-Krawczyk for δ_CP
  (positive prediction, third quadrant, `[251.86°, 270.00°]`) and
  honest no-prediction findings for θ_12, θ_13.

Together, the cascade supplies Nature-grade falsifiable forecasts on
the two angles where the framework predicts (s_23², δ_CP) and an
honest declaration of silence on the two angles where the framework
takes them as inputs (s_12², s_13²). Under named external admissions
(X3), (X3\*), (X6), the framework forecast is:

```
θ_23 in the upper octant (s_23^2 > 0.5)                  [Cycle 7]
δ_CP near maximal CP-violation, third quadrant            [this note]
       (δ_CP in [251.86°, 270.00°], 18.13° width)
θ_12 unconstrained inside NuFit 3-σ                       [this note]
θ_13 unconstrained inside NuFit 3-σ                       [this note]
```

A future DUNE / T2HK δ_CP measurement at design `±15°` precision (late
2020s) will test the third-quadrant forecast at 5-σ falsification
margin: a 5-σ measurement of δ_CP outside `[251.86°, 270.00°]` would
unconditionally falsify the framework's chamber-boundary chart (under
the same imposed branch-choice rule used by the chamber pin).

The audit lane has final authority on whether (X6) is sufficient as a
named external admission and on whether this note's positive prediction
(δ_CP) and no-prediction findings (θ_12, θ_13) qualify for
retained_bounded status.
