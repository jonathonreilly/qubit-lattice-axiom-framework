# Panel 6 — Lens 4: FALSIFICATION

Object under test (**R0**, the candidate generator): `P(r | trail) = W(trail·r) / W(trail)`, with `W` the slice-Gram weight of a
record-compatible world on the positive `s_t = 0` slices. All of it pre-registered: exact rationals, no `nsimplify`, every statistic
carrying its denominator, and a claimed zero must be **symbolic** — four `nsimplify` repair sites are queued, one fail-quiet, and a
fail-quiet zero would manufacture or erase a separation.

## 0. Pre-registration hygiene — frozen before any construction runs

- **P0-a. Pin `W`.** Determinant of the principal record block, trace, Rayleigh quotient, Schur complement? Unpinned, every failure
  below is absorbed by redefining `W` — the shim moved into the definition.
- **P0-b. Pin `A(trail)`**, the admissible-continuation set, and its minimum size: the coarse-graining tests (F5 / D3) are
  **vacuous at `|A| = 2`** and require `|A| >= 3`.
- **P0-c. Pin the fixtures.** Bench `12x4` (`T_phys = 6`, `L_x = 4`); control `8x4` / `8x6` (`T_phys = 4`). Carriers
  `sigma in {1/5, 2/5, 3/5}` + flat + symbolic; `m in {1/3, 1, 3, 10}` + symbolic; `s_t in {1/4, 1/2}` + symbolic; holonomy dial
  `g_t = g_re + i·g_im`; Wilson dial `lambda_w in {0, ±1, 20}`.
- **P0-d. Inertia convention inline.** Two landed helpers disagree on triple order (`(n_+,n_-,n_0)` vs `(n_+,n_0,n_-)`), so the
  literal `(4,4,0)` reads PSD in one and fully hyperbolic in the other; every positivity verdict feeding a weight must carry its
  convention in the same string.

## 1. Consistency falsifiers — R0 dies here without any rival

- **F1. Sibling additivity / sum-to-1.** `sum_{r in A(trail)} W(trail·r) = W(trail)` exactly, as a rational
  identity. Gram functionals are not generally additive over a partition of the extended slice.
- **F2. Trail-functionality (path independence).** Two distinct admissible histories realizing the *same* record word must give the
  same `W`; if not, `P(· | trail)` is not a function of the trail and the chain rule `P(r1 r2 | t) = P(r1 | t)·P(r2 | t·r1)` is a
  telescoping artifact of one chosen representative.
- **F3. Support and sign.** `W >= 0` on every record-compatible extension, `W = 0` exactly off it, `W(trail) > 0` on every admissible trail (no `0/0`); a negative or complex value kills.
- **F4. Superselection block-diagonality.** Records are superselection labels, so the slice Gram must carry **zero** off-diagonal
  between distinct record labels. Nonzero leakage means "the weight of a record" needs a choice, and that choice is an extra
  probability input — the exact gap the frequency-boundary note names.
- **F5. Coarse-graining additivity.** `P(r1 v r2 | t) = P(r1 | t) + P(r2 | t)` exactly, at `|A| >= 3`.
  **F6. Relabel covariance.** Permuting record atoms permutes the profile and changes nothing else.
  **F7. Wrap agreement.** Every identity passing at `T_phys = 4` must re-pass at `T_phys = 6` (§4).
- **F8. Factorization / memorylessness.** At `s_t = 0` the committed `C = s_t·C1` vanishes and the calibrated pairing is
  `m·diag(D_c) ⊕ 0`, block-diagonal across slices. If the slice Gram factorizes over the record partition then
  `W(trail·r) = W(trail)·W(r)` identically and `P(r | trail) = P(r)`: trail-blind, and R0 collapses into R5. **Structural, not
  numerical** — checkable symbolically before any fixture is evaluated.

## 2. The rival slate, and the finite separating computation for each

Every separation `D` is a max-over-atoms absolute difference of normalized profiles, exact rational. **Null fixture:** at the flat
carrier the `s_t = 0` calibration is `m·1 ⊕ 0`, so R0's profile is *exactly* uniform — that carrier separates nothing, is the
built-in control (analogue of the census's half-support scope), and no separation may be benched there.

- **R1 — uniform over admissible continuations.** `D1 = max_r |P_R0(r) − 1/|A||` at `sigma = 1/5, 2/5, 3/5` on `12x4`. Expected:
  **strictly positive** at every non-flat carrier, **exactly zero** at flat. `D1 = 0` at all three carriers means R0 is
  uniform-in-disguise and its whole content is carrier moduli.
- **R2 — count-proportional (the measured-failed one).** Frequency agreement is now uninformative in both directions; what remains
  informative is a **blindness-transfer test**. Count profiles are combinatorial, hence carrier-blind by construction, so
  `Delta_sigma(count profile) = 0` identically. Compute `D2 = |profile_R0(sigma = 1/5) − profile_R0(sigma = 3/5)|` — one carrier
  pair, one difference. Expected **strictly positive** for a weight law; `D2 = 0` makes R0 count-proportional in disguise,
  inheriting the boundary result's kill with no new counting run at all.
- **R3 — `|W|^p`, `p != 1` (Gleason-adjacent).** Separate by identity, not numerically. With `w1 != w2` and at least one atom
  outside the merged pair (`B = sum_others w^p > 0`), the F5 defect `Delta = P_coarse(r1 v r2) − [P_fine(r1) + P_fine(r2)]` carries
  the sign of `(w1+w2)^p − (w1^p + w2^p)`, since `x -> x/(x+B)` is increasing: **negative for `p < 1`** (concave, subadditive),
  **positive for `p > 1`**, **exactly zero only at `p = 1`**. One exact-rational triple with distinct weights kills the entire
  family at once, and the same triple simultaneously tests R0.
- **R4 — connection-blind shims of R0** (the anti-shim discriminator). The shim class must be the **general** one: the H3 lesson is
  that a narrower shim class failing to reproduce is not a pass — the general class reproduced the object bit for bit where a bare
  corner-diagonal shim did not. (a) *Holonomy dial*: recompute the profile under `g_t = g_re + i·g_im`; framework transport-carrying
  objects **move**, a shim is **identical entry for entry**. (b) *Transport off*: `s_t = s_x = 0`, where the action collapses to the
  mass term. Expected: R0 gives **nonzero** difference under both, and **exact zero** under either is the anti-shim verdict.
  Standing hazard — R0 lives *on* `s_t = 0` slices where the committed `C` is already dead, so (b) risks exact zero by construction;
  pre-register what that would mean before running, not after. (c) *Affine-pencil guard*: if `W` (or the quotiented action feeding
  it) is affine in a dial, the admissible dial region is automatically a convex interval, so a bounded "good window" is shim
  self-damage, not content.
- **R5 — trail-blind marginal, `P(r | trail) = P(r)`** (the IID null the boundary note says must be supplied as an extra model).
  `D5 = |P_R0(r | trail A) − P_R0(r | trail B)|` for two equal-length trails of different content. Expected **strictly positive**
  for a genuine generator, **exactly zero** iff F8 factorization holds; D5 and F8 are one falsifier measured two ways — run F8
  first, symbolic and cheaper.
- **R6 — carrier-blind Gram** (`H -> m·1` inside the weight, records fixed): separates "the weight sees the geometry" from "the
  weight sees only record combinatorics"; expected **nonzero**. Caution from the H3 disposal — carrier sensitivity is *not* the
  discriminator, since every object with an `H` in it is carrier-sensitive, `H` included; R6 is necessary, never sufficient, and
  R4(a) is the sufficient leg.

## 3. Census-collision interaction

A collision = two distinct weight profiles sharing one frequency profile.

- **Survive intact** (all internal to R0; no frequency data enters): F1–F8 entire, R3's coarse-graining identity, R4(a)(b)(c), R6,
  and the candidate legs of D1/D2/D5 — a collision changes nothing about whether R0 is consistent and transport-carrying.
- **Become undecidable**: every verdict of the form "R0 reproduces the observed frequency profile". Under a collision the frequency
  profile is a strictly coarser invariant than the weight profile, so frequency agreement stops being evidence *for* R0 and stops
  being evidence *against* R1 or R2; D2's transfer-kill survives only in its carrier-variation form, never in any matching form. The
  slate demotes from "which generator is derived" to "which generator is consistent and transport-carrying", and R1 / R2 are then
  excludable only by identity and by carrier/holonomy sensitivity.
- **The converse collision** (one weight profile, two frequency profiles) is not a rival question at all: it falsifies the bridge as
  a function — `W` does not determine frequency — and R0 dies with it. Rank it with the §1 falsifiers, not here.

## 4. Wrap-artifact guard — what must run at `T_phys >= 6`

At `T_phys = 4`, `2 ≡ −2 (mod 4)`: forward and backward two-step hops are self-congruent. Landed contamination — the committed corner
is hollow at `12x4` and non-hollow at `8x6`; homogeneous displacement-2 content reads corner rank **0 of 72** at `8x6` against
**36 of 72** inhomogeneous, the survivor exactly anti-Hermitian so `herm()` annihilates it; and the wrap breaks the `s_t`-evenness of
`K` at `8x6` while it holds at `12x4`.

- **Must be `T_phys >= 6`**: F2 and D5 (any trail extension spanning two slices — the trail's arrow is not resolvable at
  `T_phys = 4`); F8 (slice factorization is a two-slice statement); any statistic keyed on `s_t` parity; and **R4 in full**, because
  at `T_phys = 4` genuine transport-carrying content can be annihilated by the wrap, producing **false shim positives** — the most
  expensive error available here.
- **May run at `T_phys = 4` as a cheap control, never as the verdict**: F1, F3, F5, F6, R3, D1 — single-slice and algebraic; require
  agreement across both sizes (F7). Homogeneity, not displacement, is what the wrap kills, so an inhomogeneous `T_phys = 4` fixture
  is not automatically safe either — merely differently contaminated.

## 5. Ranking by kill-power per unit compute

| # | test | compute | what it kills |
|---|---|---|---|
| 1 | **F8** factorization at `s_t = 0` | one symbolic block-structure check | R0 as a *generator* (collapses to R5) |
| 2 | **F1** sibling additivity | one exact sum per fixture | R0 outright |
| 3 | **R4(a)** holonomy dial | one recompute under complex `g_t` | R0 as physics-empty, by the program's own shim theorem |
| 4 | **R3 / F5** coarse-graining, 3+ atoms | one exact triple | the entire `p != 1` family **and** tests R0, same triple |
| 5 | **D1** flat-carrier degeneracy | trivial | kills nothing; bounds R0's content to carrier moduli and fixes the null fixture excluded from all benches |
| 6 | **D2** carrier-variation transfer | one carrier pair | R0 by inheritance from the boundary result, if `D2 = 0` |
| 7 | **F2** path independence | two histories per record word | R0's trail-functionality |
| 8 | **F3**, **F4**, **F6**, **R6**, **F7** | small, each; F7 doubles what it guards | well-posedness, the necessary (not sufficient) geometry leg, and artifacts |
| 9 | the census | one block | nothing directly — the theorem-or-axiom decider, not a falsifier |

Tests 1–4 all run before a single fixture sweep, and three of the four are symbolic.
