# The Brannen-δ Phase Chirality and the Generation Count Share One Z₂ Orientation

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a records-level unification)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_koide_delta_phase_count_one_z2_orientation.py`](../scripts/frontier_koide_delta_phase_count_one_z2_orientation.py)
**Cached log:**
[`logs/runner-cache/frontier_koide_delta_phase_count_one_z2_orientation.txt`](../logs/runner-cache/frontier_koide_delta_phase_count_one_z2_orientation.txt)
(TOTAL: PASS=16 FAIL=0)

## 0. What this note adds

Two charged-lepton flavor residuals have, until now, been treated as separate selectors:

1. **the generation COUNT** — breaking the (physically unbroken) `S_3` axis-symmetry of the
   `hw=1` triplet down to `C_3`. The retained-bounded pair
   [`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md)
   and [`POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md)
   prove the only one-dimensional breaker is the **orientation (sign) representation** of
   `S_3` — the sign of the `Cl(3)` pseudoscalar / volume form — whose positive level set is
   exactly `A_3 = C_3`, leaving open *"does the framework force a global handedness
   selection?"*

2. **the Brannen PHASE chirality** — selecting the physical azimuth `+δ_*` (`δ_* ≈ 2/9`)
   over its mirror `−δ_*`. The companion mirror-degeneracy result (records-side, branch
   `science/koide-delta-azimuth-chirality-necessity-2026-06-08`, named in plain text, not a
   citation-graph dependency) shows `δ → −δ` is the generation transposition `(1 2)`, so
   every achiral records/Born functional has `F(+δ)=F(−δ)` and the selector must be
   chirality-odd.

**This note proves these are the same object.** The canonical chirality-odd functional on
the records simplex is the **generation Vandermonde / discriminant**
`Δ(p) = (p_0−p_1)(p_1−p_2)(p_2−p_0)`, which transforms by the `S_3` **sign** representation
`Δ(σ·p) = sgn(σ)Δ(p)` — i.e. it *is* the orientation-sign object the POSITIVITY notes use
for the count, with `sgn(σ) = det(ρ_perm(σ))`. Hence the residual that selects the Brannen
phase (after the `C_3` chamber is fixed) and the residual that breaks `S_3 → C_3` for the
count are **one and the same global Z₂** = `sign(Δ)` = the `Cl(3)` pseudoscalar /
volume-form handedness.

It does **not** supply the realized handedness, does **not** select the magnitude `2/9`,
and does **not** touch the `r = 1/2` firewall.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| orientation sign = `S_3` sign rep = `Cl(3)` pseudoscalar/volume-form sign; positive set `= C_3`; open global-handedness bridge | [`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md), [`POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | the orientation object (this note ties the phase to it) |
| generations = `hw=1` BZ-corner `C_3` axis triplet; `C_3[111]` cycles the three spatial axes | [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) | `retained` (corollary) | identifies the `S_3` as axis-permutations |
| spatial inversion is the identity on the triplet (bare lattice parity-symmetric) | [`PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23`](PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | why the handedness is an extra input |
| frame-free `Cl(3)` pseudoscalar acts as a scalar `cI₃` (Schur); selective handedness needs the frame-broken axis structure | [`CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02`](CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02.md) | `retained_no_go` | scopes the orientation as frame-broken/global |
| operator no-go: no `C_3`-equivariant Hermitian operator in `Sym(R³)` anticommutes with `Γ_χ` | [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) | `retained_bounded` | the operator-level obstruction this note operates *beside* (records level) |
| magnitude `2/9 = L_3(1,2)` (C₃ fixed-point density) | [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) | `retained_bounded` | the separate magnitude residual |

No PDG value is load-bearing for the theorem; PDG enters only the Section 6 comparator. No
new axiom, import, or vocabulary. The mirror-degeneracy companion and the operator-side
`KOIDE_DELTA_RANK2_SELECTOR` note (`unaudited`) are named as context, not dependencies.

## 2. Setup

On the firewalled cone (`Q = 2/3`, block-weight `r = 1/2`, held fixed for all `δ`), the
charged-lepton record is the Born triple `p_k(δ) = λ_k(δ)²/Σ_j λ_j(δ)²` with
`λ_k(δ) = 1 + √2 cos(δ + 2π k/3)` on the three-outcome records simplex. The three outcomes
are the three generations `= hw=1` BZ corners `= the three spatial axes`
(`THREE_GENERATION_OBSERVABLE_THEOREM`), so the symmetric group `S_3` acting on the outcomes
is the **axis-permutation group**, and `C_3[111]` is the cyclic rotation of the axes.

## 3. The canonical chirality-odd functional is the orientation sign rep

The companion mirror-degeneracy result shows the azimuth selector must be **chirality-odd**:
odd under `δ → −δ`, which on the Born weights is the transposition `(1 2)` (runner `M_*`).
The canonical, basis-independent, fully `S_3`-covariant chirality-odd functional is the
**generation Vandermonde / discriminant**

```text
Δ(p) = (p_0 − p_1)(p_1 − p_2)(p_2 − p_0).
```

**Theorem (the phase chirality is the orientation sign rep).**

1. `Δ` carries the `S_3` **sign** representation: `Δ(σ·p) = sgn(σ) Δ(p)` for every
   `σ ∈ S_3` (runner `U_vandermonde_is_S3_sign_rep`, exact).
2. `sgn(σ) = det(ρ_perm(σ))` — identically the orientation-sign object the POSITIVITY notes
   use for the count, with positive level set `{σ : sgn(σ)=+1} = A_3 = C_3` (runner
   `U_sgn_equals_det_perm_count_orientation`).
3. `Δ` is odd under the reflection `δ → −δ`, so `sign(Δ)` distinguishes the physical
   `+δ_*` from its mirror `−δ_*`: `Δ(+2/9) = +0.04675`, `Δ(−2/9) = −0.04675`
   (runner `U_vandermonde_odd_under_reflection`, `U_sign_..._orientation_Z2`).
4. `+δ_*` and `−δ_*` share the **same** sorted Born multiset (the same `C_3` chamber) and
   differ **only** in `sign(Δ)` (runner `U_mirror_shares_chamber_opposite_orientation`). So,
   once the `C_3` chamber is fixed by the positive ordering, the residual that selects the
   Brannen phase is exactly `sign(Δ)`.

**Corollary (one Z₂).** The generation **count** breaker (`S_3 → C_3`, POSITIVITY notes) and
the Brannen **phase** selector (`+δ_*` vs `−δ_*`) are governed by the *same* single global
`Z_2 = sign(Δ) = sgn` = the `Cl(3)` pseudoscalar / volume-form handedness. Two apparently
independent charged-lepton flavor residuals collapse to one orientation.

## 4. This lives at the records-functional level (and operates beside the operator no-go)

The orientation enters as a **chirality-odd functional of the Born data** (the discriminant
`Δ`), not as an operator. This matters for three retained obstructions:

- **Operator anticommuting no-go** (`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO`,
  `retained_bounded`) forbids a `C_3`-equivariant Hermitian operator in `Sym(R³)` that
  *anticommutes* with `Γ_χ`. A scalar sign `sI` (`s ∈ {±1}`) is **not** such an operator:
  `{sI, Γ_χ} = 2s Γ_χ ≠ 0` (runner `E_scalar_op_*`). The Z₂ orientation is therefore
  **outside** the operator no-go — it is a functional on the data, not an anticommuting
  grading. (Equally, a scalar *operator* does no work — `KOIDE_ORIENTATION_BLIND_COUNT`,
  `retained_bounded` — which is exactly why the content must live at the functional level,
  not the operator level.)
- **Frame-free no-go** (`CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING`, `retained_no_go`): the
  pseudoscalar used frame-free is a Schur scalar; a *selective* handedness needs the
  frame-broken axis structure. The discriminant `Δ` is built on the axis-labeled
  generations (the frame-broken structure that no-go leaves open), consistent with its scope.
- **Reconciliation with the operator-side δ-selector** (`KOIDE_DELTA_RANK2_SELECTOR`,
  `unaudited`): that note works on the rank-2 *zero-mode operator* sector, where the scalar
  site-parity `ε = −I₃` cannot split the doublet and the full `γ_5` grading is invoked. The
  present statement is **upstream**, on the `C_3` generation Born data, where the orientation
  is a measure/functional (`sign Δ`), not an operator on a doubled kernel. The two are
  consistent: at the records level the requirement is the single Z₂ `sign(Δ)`; the
  operator-level `γ_5` is the reconstruction that implements it on the zero-mode sector.

## 5. Scope — what this does and does not establish

**Establishes (exact, finite):**
- `Δ(p)` carries the `S_3` sign rep `= det(ρ_perm)` `=` the POSITIVITY count-orientation.
- `sign(Δ)` is the residual selecting `+δ_*` over its mirror after the `C_3` chamber — i.e.
  the phase chirality **is** the orientation sign.
- One global Z₂ (`Cl(3)` pseudoscalar handedness) governs both the count and the phase.
- The orientation is a records functional, outside the operator anticommuting no-go.

**Does NOT establish (named separate residuals, untouched):**
- **Realized handedness.** It does not pick *which* sign of `Δ` is realized. Both
  orientations are valid records; the realized global handedness is the **open**
  global-orientation residual the POSITIVITY note names — tied to the lattice volume form /
  arrow of record accumulation (the bare lattice is parity-symmetric, so the sign is not
  supplied by the unoriented lattice; `PARITY_VIOLATION_..._TRIPLET`). `no_per_site_chirality`
  requires it be global, not per-site — consistent with `sign(Δ)` being one global sign.
- **Magnitude.** It does not select `|δ_*| = 2/9`. The orientation supplies only the **sign**;
  `|Δ(2/9)| = 0.047 ≠ 2/9`. The magnitude `2/9 = L_3(1,2)` is the separate retained-bounded
  C₃ fixed-point density.
- **The `r = 1/2` firewall.** The cone `Q = 2/3` is held fixed for all `δ` (runner
  `firewall_*`); never forced or derived.

## 6. Honest verdict

The charged-lepton flavor program has carried the generation **count** (why three /
`S_3 → C_3`) and the Brannen **phase** chirality (`+δ_*` vs mirror) as separate open
selectors. They are not separate: both reduce, at the records-functional level, to one
global `Z_2` — `sign(Δ)`, the `Cl(3)` pseudoscalar / volume-form handedness, exactly the
orientation sign rep the retained POSITIVITY notes identified for the count. This is a strict
unification, not a closure: the **realized** handedness (which orientation), the **magnitude**
`2/9 = L_3(1,2)`, and the **radian unit** remain the named separate residuals, and the
`r = 1/2` cone stays firewalled. The payoff is that the open global-handedness bridge the
POSITIVITY notes left for the count is now *the same* residual as the Brannen-phase chirality
— one Z₂ to derive (from the lattice volume form / arrow), not two.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded records-level unification. It does **not** claim the
handedness is derived, the phase is closed, or `2/9` is reached — only that the count's and
the phase's chirality are one orientation object.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| symmetric records functional | RULED OUT (companion) | mirror-degenerate, cannot select `±δ` |
| Vandermonde / `S_3` sign-rep functional | IS THE OBJECT | `Δ(σp)=sgn(σ)Δ(p)`; `sign(Δ)` selects `±δ` |
| count-orientation (POSITIVITY) | SHOWN IDENTICAL | `sgn = det(ρ_perm)`, positive set `= C_3` |
| scalar operator `sI` | OUTSIDE / INERT | not anticommuting; does no operator work |
| realized handedness | OPEN RESIDUAL | global orientation / arrow (POSITIVITY open bridge) |
| magnitude `2/9` | SEPARATE RESIDUAL | `L_3(1,2)` density |

**N2 — Wall-independence.** Orientation *object* (this note), realized *handedness*,
magnitude `2/9`, radian unit, and the `r=1/2` cone are independent; this note unifies the
first across count/phase and fixes the rest as untouched.

**N3 — Hidden-wall scan.** The theorem uses only `δ→−δ = (1 2)`, the definition of `Δ`, and
finite `S_3` rep theory; "chirality", "pseudoscalar", "arrow" name the object/residual, not
hidden premises.

**N4 — Residual matching.** The residual named is the realized global handedness (= the
POSITIVITY open bridge), not the magnitude and not the unit.

**N5 — Rhetoric audit.** Claim is the identity of two orientation requirements and the
collapse to one Z₂; not a phase derivation, not a handedness derivation.

**N6 — Partial-closure path scan.** Next step: derive the global handedness (the realized
`sign Δ`) from the lattice volume form / monotone record accumulation — closing count and
phase together. No new axiom requested.

**N7 — Steelman.** A reviewer may hold that unifying two *open* residuals does not reduce the
total unknown. Granted in arithmetic; the value is structural — it shows the lattice volume
form / arrow is the *single* lever for both, and that the operator no-go does not block the
records-level orientation. The realized sign remains open, as stated.

**N8 — Cross-cycle echo.** Preserves the retained POSITIVITY count-orientation, the retained
parity-trivial-on-triplet and frame-free no-go scoping, the operator anticommuting no-go, and
the retained-bounded `L_3(1,2)` magnitude — connecting them without overruling any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained / retained-bounded /
  retained-no-go rows plus the Brannen algebraic form.
- **No PDG/fitted load-bearing input** (PDG only in the Section 6 comparator); **no forcing of
  `r = 1/2`**; **no new transcendental constant.**
- The `unaudited` companion and `KOIDE_DELTA_RANK2_SELECTOR` are named as context, not
  citation-graph dependencies.

## 9. Command

```bash
python3 scripts/frontier_koide_delta_phase_count_one_z2_orientation.py
```

Expected: `TOTAL: PASS=16 FAIL=0`. numpy + stdlib, deterministic, 3-vectors throughout
(memory-safe). The runner verifies the reflection-as-transposition recap, the Vandermonde
sign-rep identity, `sgn = det(ρ_perm)`, the orientation-Z₂ selecting `±δ_*`, the
scalar-operator-is-not-anticommuting evasion, the single global Z₂, the separate magnitude
`L_3(1,2)`, and the phase-blind `Q = 2/3` cone.
