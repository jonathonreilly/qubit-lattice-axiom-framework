# The Brannen-δ Azimuth Selector Is Chirality-Odd on the Records Simplex — Mirror-Degeneracy No-Go

**Date:** 2026-06-08
**Claim type:** no_go (records-side negative route pruning)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_koide_delta_azimuth_chirality_necessity.py`](../scripts/frontier_koide_delta_azimuth_chirality_necessity.py)
**Cached log:**
[`logs/runner-cache/frontier_koide_delta_azimuth_chirality_necessity.txt`](../logs/runner-cache/frontier_koide_delta_azimuth_chirality_necessity.txt)
(TOTAL: PASS=32 FAIL=0)

## 0. The precise hole this note targets

The retained-bounded Fisher-Rao reorganization
[`KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01`](KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01.md)
puts the charged-lepton `√m` record point on the Fisher-Rao 2-sphere with
**polar angle** `θ_p` fixed by `cos²θ_p = 1/(3Q)` (so `θ_p = π/4 ⟺ Q = 2/3`, the
**firewalled** block-weight `r = 1/2`) and **azimuth** `φ = δ` equal to the Brannen
phase. Its demarcation is that the round metric has `g_φφ = sin²θ` — the azimuth is a
**Killing direction** — so "the metric alone cannot select the value `2/9`," and its N6
leaves the route open with: *"an additional source functional would be needed to break
the azimuthal isometry and select a longitude"* / *"a records/Born functional on the
simplex could close the route without an axiom change."*

This note **closes the achiral subclass of that opening**. It proves a finite, exact
fact: on the einselected three-outcome **records simplex**, the reflection `δ → −δ` acts
as the generation transposition, so **every permutation-symmetric ("achiral")
records/Born functional is mirror-degenerate** — `F(+δ) = F(−δ)` identically — and
therefore **cannot uniquely select the chiral physical azimuth `+δ_*` over its distinct
mirror `−δ_*`**. The records/Born functional the Fisher-Rao note hoped for must be
**chirality-odd**. This routes the records-side azimuth-selection residual to the same
chirality gate the operator-side note
[`KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05`](KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md)
identifies on the Dirac kernel (the on-site Clifford chirality `γ₅`).

It does **not** select the magnitude `2/9`, does **not** close the radian-unit
admission, and does **not** touch the `r = 1/2` firewall.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role here |
|---|---|---|---|
| azimuth `φ = δ`; polar `cos²θ_p = 1/(3Q)`; azimuthal-Killing demarcation + N6 | [`KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01`](KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01.md) | `retained_bounded` | the residual this note advances |
| records-Fisher tangent: zero-mean score, exponential chart, signed-record unit `ε` | [`SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06`](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md) | `retained` | the records-functional toolkit the theorem ranges over |
| `Q = 2/3` for the `√2` Brannen ansatz at every `δ` (cone is phase-blind) | [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` | the firewalled cone (untouched) |
| magnitude `2/9 = L_3(1,2)` as the `C_3` fixed-point (Lefschetz/Molien) density | [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md), [`AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md) | `retained_bounded` | the **value** source (separate residual) |
| Type-A/Type-B split; the radian-unit residual `δ = 2/9 rad` vs index phase `2π/9` | [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md) | `retained_no_go` | the **unit** residual (separate, untouched) |
| operator-side selector = on-site Clifford chirality `γ₅` (domain-wall edge) | [`KOIDE_DELTA_RANK2_SELECTOR_..._BOUNDED_NOTE_2026-06-05`](KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md) | `unaudited` | **context only** (named, not a citation-graph dependency) |

The operator-side rank-2 selector note is `unaudited`; it is named in plain text as the
sibling surface, **not** consumed as load-bearing authority. No PDG value is
load-bearing for the theorem (Sections 3–5); PDG enters only the Section 7 comparator.
No new axiom, no new import, no new vocabulary.

## 2. The records simplex and the azimuth

On the firewalled cone, the charged-lepton record is the positive `√m` triple in
Brannen form, parametrized by the single azimuth `δ`:

```text
λ_k(δ) = 1 + √2 cos(δ + 2π k / 3),   k = 0, 1, 2,        (B)
```

with the einselected Born weights `p_k(δ) = λ_k(δ)² / Σ_j λ_j(δ)²` on the three-outcome
records simplex. The cone `Q = 2/3` (equivalently `θ_p = π/4`, the block-weight
`r = 1/2`) holds for **every** `δ` (runner `C_*`): the cone is phase-blind, and the only
free datum is the azimuth `δ`.

## 3. Lemma (the reflection is the generation transposition)

**`δ → −δ` permutes the records by the transposition `(1 2)`.** From (B),
`cos(−δ + 2π k/3) = cos(δ − 2π k/3)`, so `λ_k(−δ) = λ_{−k}(δ)`, i.e.

```text
λ(−δ) = (1 2) · λ(δ)      and therefore     p(−δ) = (1 2) · p(δ),
```

the permutation fixing outcome `0` and swapping outcomes `1 ↔ 2`. The runner verifies
this on both amplitudes and Born weights to machine precision over a `δ`-sweep (`L_*`,
`max ≈ 7·10⁻¹⁶`).

This is the records-simplex shadow of the `C_3` generation cycle's **orientation**: the
two cyclic orderings `(0→1→2)` and `(0→2→1)` are exchanged by `δ → −δ`.

## 4. Theorem (mirror-degeneracy: achiral functionals cannot select the chiral azimuth)

Let `F` be any **permutation-symmetric** functional of the Born weights — i.e. any
records/Born scalar invariant under relabelling the three outcomes (Shannon entropy,
collision/purity `Σ p²`, the variance `Σ(p−1/3)²`, any `Σ p^n`, `KL(p‖uniform)`, any
symmetric records `I`-readout). By the Lemma, `p(−δ)` is a relabelling of `p(δ)`, hence

```text
F(+δ) = F(−δ)        for all δ          (mirror degeneracy).
```

Consequences (all verified):

1. **The stationary set of `F` is `δ → −δ`-symmetric.** Its critical azimuths come in
   mirror pairs `±δ_c` together with the reflection-axis points. So `F` cannot deliver a
   single chiral longitude: any value it stationary-selects at `+δ_*` it equally selects
   at `−δ_*` (`T_mirror_*`: `F(+2/9) = F(−2/9)` exactly for all five tested functionals).
2. **The mirror is a genuinely different record.** `+δ_*` and `−δ_*` are distinct mass
   configurations — they swap the two non-leading generation slots
   (`max|p(+2/9) − p(−2/9)| ≈ 0.056`, runner `N_plus_minus_..._distinct`). The physical
   charged-lepton point is the chiral one; its mirror is not realized.
3. **For the natural achiral functionals the critical azimuths are `π`-commensurate, not
   `2/9`.** All five land their `[0, π/2]` critical points at the `D_3` axes
   (`δ = π/3`, etc.), none within `5·10⁻³` of `2/9` (`crit_pi_rational_not_two9_*`). The
   bare rational `2/9` sits off the `π`-commensurate lattice that symmetric records
   stationarity produces — the radian wall reappearing in the records algebra.

Therefore **no permutation-symmetric records/Born functional's stationarity selects the
chiral physical azimuth.** Any functional that does must be permutation-**antisymmetric**
(chirality-odd).

## 5. Non-vacuity (the chirality-odd witness — the records-side image of `γ₅`)

The obstruction is specifically about chirality, not a blanket impossibility. The
imaginary part of the `C_3` character weighted by the record,

```text
A(δ) = Σ_k p_k(δ) sin(2π k / 3),
```

is permutation-**odd** — `A(−δ) = −A(δ)` exactly (runner `N_witness_is_chirality_odd`) —
and it **distinguishes** `+δ_*` from `−δ_*`: `A(+2/9) = −0.04836`, `A(−2/9) = +0.04836`
(`N_witness_distinguishes_*`). `A` is the cyclic **orientation** of the three generations
(the signed area / `Im` of the regular `C_3` character). A records functional sensitive to
`A` is exactly a functional that reads the generation-cycle handedness — the records-side
image of the on-site Clifford chirality `γ₅` that the operator-side note selects on the
Dirac kernel. The achiral functionals are, by the control checks, even in `δ`
(`control_*_is_even`) and blind to `A`.

## 6. One gate, two surfaces

| Surface | Object | Achiral candidates | What is forced |
|---|---|---|---|
| Dirac kernel (rank-2 zero modes) | Wilson/APS **marks** | scalar marks act as `λI`, cannot split | selector = Clifford chirality `γ₅` (unaudited sibling) |
| records simplex (Born weights) | **records/Born functionals** | symmetric `F` are mirror-degenerate, cannot select `±δ` | selector must be chirality-odd (this note) |

The two recently-active surfaces — the Fisher-Rao/records lane (`retained_bounded`
2026-06-01, `retained` 2026-06-06) and the operator/chirality lane (2026-06-05) — name
the **same gate**: the charged-lepton azimuth selection requires the generation-cycle
chirality. This note supplies the records-side **necessity** that the operator-side
mark-no-go does not address, closing exactly the records/Born functional class the
Fisher-Rao N6 left open.

## 7. Scope — what this note does and does not establish

**Establishes (exact, finite):**
- `δ → −δ` is the generation transposition `(1 2)` on the Brannen records (Lemma).
- Every permutation-symmetric records/Born functional is mirror-degenerate, so cannot
  select the chiral physical azimuth; the selector must be chirality-odd (Theorem).
- The necessity is non-vacuous: an explicit chirality-odd records functional distinguishes
  `±δ_*` (Section 5).

**Does NOT establish (named separate residuals, untouched):**
- **Magnitude.** It does not derive `δ_* = 2/9`. The value `2/9 = L_3(1,2)` is the
  `C_3` fixed-point density (`retained_bounded`, cited; reproven cyclotomically in the
  runner, `V_*`), a separate result. This note fixes only that the selector is
  chirality-odd, not the longitude it lands on.
- **Radian unit.** It does not close the radian-unit admission. The physical phase is
  `δ ≈ 2/9` **bare radians** (runner `R_*`: `δ_PDG = 0.222230`), distinct from the
  index-theory phase `2π/9 = 0.69813` — the factor-`π` admission isolated by the retained
  radian-bridge no-go remains open.
- **The `r = 1/2` firewall.** The cone `Q = 2/3` (`θ_p = π/4`, block-weight `r = 1/2`) is
  the registered charged-lepton pattern and is held fixed for all `δ` (runner `C_*`); it
  is never forced or derived here.
- **The chirality gate itself.** Whether the framework supplies the required
  orientation-odd ingredient on the generation `R³` factor is the open chirality gate
  shared with Koide `Q = 2/3` and generation identification; it is not discharged here.

## 8. Honest verdict

The records/Born route to selecting the charged-lepton Brannen azimuth — the route the
retained-bounded Fisher-Rao note left open — **cannot be closed by any achiral functional**:
the reflection `δ → −δ` is the generation transposition, so symmetric records stationarity
is mirror-degenerate and `π`-commensurate, while the physical point is a single bare-radian
chiral longitude. The route therefore demands a **chirality-odd** records functional, which
is the records-side image of the operator-side `γ₅` selector. This is a strict narrowing,
not a closure: it converts "find a records/Born functional that selects the azimuth" into
"supply the generation-cycle chirality," unifying the records lane with the operator lane on
the framework's central chirality gate — while leaving the magnitude `2/9 = L_3(1,2)` and
the radian unit as the two named, separate residuals.

## 9. No-Go Discipline Gate

**Status:** PASS for this bounded records-side obstruction. The negative boundary is
narrow: achiral records/Born functionals cannot select the chiral azimuth. It is **not**
claimed that `δ` cannot be derived, that the chirality is unavailable, that `2/9` is
unreachable, or that the route is closed.

**N1 — Alternative-route enumeration.**

| Route against the boundary | Marker | Result |
|---|---|---|
| symmetric records functional (entropy/purity/variance/`Σpⁿ`/KL) | ATTEMPTED | mirror-degenerate; `π`-commensurate critical azimuths; misses `2/9` |
| chirality-odd records functional (orientation `A`) | ESCAPES BOUNDARY | distinguishes `±δ` — the required class |
| metric selection (round Fisher-Rao) | RULED OUT UPSTREAM | azimuthal Killing direction (Fisher-Rao note) |
| operator-side Wilson/APS mark | OUT OF SCOPE (sibling) | scalar on rank-2 kernel (rank2-selector note) |
| magnitude `2/9` | SEPARATE RESIDUAL | `L_3(1,2)` fixed-point density (cited) |
| radian unit `2/9 rad` vs `2π/9` | SEPARATE RESIDUAL | retained radian-bridge no-go |

**N2 — Wall-independence audit.** The chirality necessity (this note), the magnitude
`2/9`, the radian unit, and the `r = 1/2` cone are four independent objects; this note
resolves only the first and explicitly fixes the other three as untouched.

**N3 — Hidden-wall scan.** "Chirality," "orientation," and "`γ₅`" are not used as hidden
premises for the theorem; the theorem uses only the permutation action `δ → −δ = (1 2)`
and the definition of a symmetric functional. Chirality appears only as the *name* of the
escaping class (Section 5).

**N4 — Residual matching.** The residual named here — a chirality-odd records functional /
the generation-cycle orientation — is exactly the records-side image of the operator-side
`γ₅` gate, not the magnitude and not the unit.

**N5 — Rhetoric audit.** The claim is necessity within the records/Born functional class
(symmetric `⇒` cannot select), proven by exact mirror-degeneracy. It is not a selection of
`δ`, not a derivation of `2/9`, not a radian-unit closure.

**N6 — Partial-closure path scan.** The legitimate next step is a framework-native,
orientation-odd records functional whose chirality is supplied by the on-site Clifford
grade — i.e. discharging the shared chirality gate — at which point the records and
operator surfaces would close together. No new axiom is requested.

**N7 — Steelman.** A hostile reviewer can accept the mirror-degeneracy and still reject any
closure, because (i) chirality-odd-ness is necessary but not shown sufficient for `2/9`,
and (ii) the radian unit is untouched. This note agrees on both — they are the named
separate residuals.

**N8 — Cross-cycle echo.** This preserves and connects the retained-bounded Fisher-Rao
azimuthal-Killing demarcation, the retained-bounded `L_3(1,2)` value, the retained
radian-bridge no-go, and the (unaudited) operator-side chirality identification, without
overruling any by prose. It echoes the standing convergence that the charged-lepton phase,
Koide `Q = 2/3`, and generation identification share one chirality gate.

## 10. Forbidden-imports check

- **No new axioms.** Inputs are the cited retained/retained-bounded rows plus the Brannen
  algebraic form; the framework baseline is untouched.
- **No new transcendental constant, no fitted/PDG load-bearing input** (PDG enters only the
  Section 7 comparator), **no new vocabulary**, **no forcing of `r = 1/2`**.
- The operator-side `unaudited` sibling is named as context only, not a citation-graph
  dependency.

## 11. Command

```bash
python3 scripts/frontier_koide_delta_azimuth_chirality_necessity.py
```

Expected: `TOTAL: PASS=32 FAIL=0`. Single deterministic run, numpy + stdlib only,
3-vectors throughout (memory-safe). The runner verifies the permutation action, the exact
mirror-degeneracy of five symmetric functionals, the `π`-commensurate-not-`2/9` critical
azimuths, the non-vacuous chirality-odd witness, the cyclotomic `L_3(1,2) = 2/9` value
source, the phase-blind `Q = 2/3` cone, and the bare-radian-vs-index-phase comparator.
