# Item 8 — `sympy.nsimplify` per-site analysis

Scope: only the 21 supplied sites, only their ~10-line neighbourhoods.
NO file edits. All paths below are under
`/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/gravity-toe-lane-work-427b0b/`.

## 0. The hazard, measured rather than assumed (sympy 1.14.0)

`nsimplify(expr)` with default args is a **no-op on ordinary exact Rationals**
and a **passthrough on symbolic expressions and on exact radicals**:

```
15/64 -> 15/64      667/912 -> 667/912      1/26542080 -> 1/26542080
x/y   -> x/y        sqrt(2)*x -> sqrt(2)*x  5/21 - 2*sqrt(466)/105 -> unchanged
```

It flips only when the Rational's decimal expansion matches an algebraic
constant to roughly 8–15 significant digits:

```
707106781/500000000        -> sqrt(2)          <<< CHANGED
323606797749979/2e14       -> 1/2 + sqrt(5)/2  <<< CHANGED
16180339887499/1e13 (13 digits of phi) -> unchanged
```

**So the corruption channel is narrow but real, and it is *silent*.** The two
confirmed lane incidents (the b164 checker's first run; the b165 solve's
PSD-deciding routine) sat on **characteristic-polynomial coefficients**, which
is the worst case: charpoly coefficients of an 8x8 exact-rational matrix are
long rationals, they are what a positivity decision reads, and a radical there
changes a sign test. b165 struck it:
`scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py:764` —
*"NO sympy.nsimplify. … it is STRUCK here"*, and the b165 note gates
`nsimplify_flag` in its own disclosures.

Two downstream failure modes matter for the ratings below:

* `sp.Rational(sqrt(2))` → **TypeError** (fail-loud).
* `sp.numer(sqrt(2)) = sqrt(2)`, `sp.denom(sqrt(2)) = 1` → **silently wrong**
  (fail-quiet). Same for `numer/denom` of `1/2 + sqrt(5)/2`.

## 1. Per-site table

| # | site | what flows in | consumer | load-bearing? | risk |
|---|---|---|---|---|---|
| 1 | `scripts/…adm_seam_two_history_gram_2026_08_15.py:861` | exact `Rational`: `sp.det` of `dressed[:k,:k]`, where the pins are the hardcoded `DRESSING_CERTIFICATE_PARAMS` (l.848) | `certificate_positive = all(minor > 0)` (l.863) — **Sylvester leading-minor PD certificate** | **LOAD-BEARING** (decides a positive-definiteness certificate) | **NEEDS-REPAIR** |
| 2 | `scripts/…shear_gauge_classification_2026_08_20.py:511` | coefficients of `Poly(charpoly(matrix))` — exact `Rational` when the carrier is pinned, symbolic otherwise | `charpoly()` — "Exact characteristic polynomial coefficients, root-free (H5)" | **LOAD-BEARING** (spectral/root-free comparisons) | **NEEDS-REPAIR** — *this is the exact call-site class b165 struck* |
| 3 | `…shear_gauge_classification_2026_08_20.py:577` | `shear = simplify(-b/a)`, `volume`; both already forced numeric-comparable by the cone tests `volume > 0`, `Abs(shear) < 1` at l.575 | `field[cell] = (…)` — the carrier field | load-bearing (it *is* the carrier) | **safe** — no-op on cone-admissible rationals; delete for hygiene |
| 4 | `…bare_character_2026_08_20.py:1671` | exact `Rational` — a `nullspace()` basis-vector entry | `direction` substitution; the only test is `MASS not in …free_symbols` (l.1674–78) | **display-only in effect** — the gate reads symbol membership, not the value | **safe** (structurally immune: no value can inject `MASS`) |
| 5 | `…residue_transversality_gate_2026_08_20.py:1399` | numeric: `normalizer` is guarded symbol-free at l.1397 | appended into `found` as a recorded coefficient | display-leaning (the note quotes the ratio) | **display-only** |
| 6 | `…residue_transversality_gate_2026_08_20.py:1518` | `CONE_TAU`, a module constant | element of the `cone_witness` record tuple | display | **display-only** (pure no-op) |
| 7 | `…residue_transversality_gate_2026_08_20.py:1624` | exact `Rational` `-a/b` from two expanded rational matrices | `ratio != value` → `consistent` → `feasible += 1`, `edges_hit`, `ratios` | **LOAD-BEARING** (feasibility count) | **safe** w.r.t. nsimplify (deterministic, equal inputs → equal outputs). **Separate flag:** l.1627 uses a *structural* `!=`, where the sibling routine at `quotient_gate:1221` uses the *semantic* `sp.simplify(ratio - candidate) != 0`. Inconsistent robustness, independent of nsimplify |
| 8 | `…residue_transversality_gate_2026_08_20.py:1695` | `ATLAS_TAU` and `CONE_TAU`, module constants | `sp.nsimplify(ATLAS_TAU) != CONE_TAU` inside `boundary_corners` — the disclosure "the cone witness's ratio is not 3/4" | **LOAD-BEARING** (a disclosure gate) | **safe** (no-op on constants). Minor flag: the comparison is *asymmetric* — one side is nsimplify'd and the other is not, so a hypothetical rewrite would make the `!=` pass spuriously |
| 9 | `…quotient_gate_2026_08_20.py:633` | `matrix.eigenvals()` of `gl.inv()·cross·gr.inv()·crossᵀ` — **principal cosines squared, generically IRRATIONAL** | `out`, then l.634 `sorted(out, key=lambda v: -sp.Rational(v))` | **LOAD-BEARING** (principal cosines / subspace angles) | **NEEDS-REPAIR** — the next line calls `sp.Rational(v)`, which **raises TypeError** on any radical. The routine therefore has an *undeclared rationality assumption* and its correctness depends on nsimplify's tolerance behaviour rather than on an assertion. Fail-loud, but wrong by design |
| 10 | `…quotient_gate_2026_08_20.py:1218` | exact `Rational` `-a/b` | compared by `sp.simplify(ratio - candidate) != 0` (l.1221) — semantic | **LOAD-BEARING** (rejects the point) | **safe** (semantic comparison is robust to any canonical form) |
| 11 | `…quotient_gate_2026_08_20.py:1622` **and** `:1623` | `tau` — produced by the `nsimplify(-a/b)` routines at l.1218 / l.1763 | `SHEAR_X: sp.numer(sp.nsimplify(tau))`, `SHEAR_T: sp.denom(sp.nsimplify(tau))`, substituted into `residue[key]` → `span.rank()`, `base_rank`, `distinct`, the inertness rows | **LOAD-BEARING** (feeds rank and inertness gates) | **NEEDS-REPAIR** — the only **fail-quiet** site in the list. If `tau` ever came back as a radical, `numer/denom` return `(α, 1)` with no error and the substitution `SHEAR_X = α, SHEAR_T = 1` is silently wrong. Also an undocumented rationality assumption on `tau` |
| 12 | `…quotient_gate_2026_08_20.py:1763` | exact `Rational` `-a/b` | l.1766 `ratio != candidate` — **structural**, then returned as `tau` and consumed by site #11 | **LOAD-BEARING** | **safe** w.r.t. nsimplify; same structural-vs-semantic inconsistency flag as #7 (l.1766 vs l.1221 in the *same file*) |
| 13 | `…validation_battery_2026_08_20.py:658` | exact `Rational` — `trace(gram⁻¹ · stackᴴ P_even stack)/dim`, docstring "basis-free and EXACT" | `even_content_of_nullspace` → the fence numeral *"the nulls at lambda = 1 have even-x content EXACTLY 0"* | **LOAD-BEARING** (a quoted fence claim) | **safe** (no-op) — but on a decision path; strike recommended |
| 14 | `…validation_battery_2026_08_20.py:699` | exact `Rational` moduli from the committed carrier field | `odd_moment_vector` | load-bearing (the odd-moment locus) | **safe** (no-op) |
| 15 | `…validation_battery_2026_08_20.py:1088` | `primary.eigenvals()` — may be irrational | dict **keys** in the `exact` spectrum record | **display-only** — the inertia at l.1082 is decided by `congruence_inertia`, not by these | **display-only** |
| 16 | `…validation_battery_2026_08_20.py:1089` | `odd_object.eigenvals()` — may be irrational | same record; the fence quotes spectra `{4/5 ×4, 0 ×4}` vs `{4/5 ×2, …}` as the non-unitary-relatedness evidence | **display-only** (same reason as #15) | **display-only** |
| 17 | `…validation_battery_2026_08_20.py:1293` | `second.eigenvals()` — the second-order `C` block; the fence's `{-375/51296, -1215/263168, -1215/253952, -507/1294336}` | sorted-by-`str` display tuple; the inertia `(0,4,4)` is from `congruence_inertia(second)` at l.1290 | **display-only** | **display-only** (note: the `key=str` sort is stringly and fragile, but deterministic — separate from this item) |
| 18 | `…mass_survival_stratum_2026_08_20.py:837` | exact `Rational` — `cancel(form[0,0]/stratum_form[0,0])` | `scalars[key]`, immediately **self-verified** at l.840–842: `identity_holds and expand(form - scalars[key]*pullback) == zeros` | **LOAD-BEARING** | **safe** — best-designed site in the list: a corrupted scalar makes the identity gate **fail loud** rather than pass |
| 19 | `…mass_survival_stratum_2026_08_20.py:1139` | ratios of the already-identity-verified `scalars` | `committed_scalars` display tuple | **display-only** | **display-only** |
| 20 | `…mass_survival_stratum_2026_08_20.py:1142` | exact `Rational` after the `GENERIC` carrier substitution | `generic_diagonals` display tuple | **display-only** | **display-only** |
| 21 | `…interpretation_discriminators_2026_08_21.py:1000` | exact `Rational` — `m_kappa2_value / mass`, already gated `m_kappa2_constant` and `m_kappa2_is_scalar` | `out["kappa2_by_mass"]`, checked at l.1791 against `tuple((mass, sp.nsimplify(MARGIN_CONSTANT/mass)) …)` | display, with a **symmetric** gate | **display-only / safe** — nsimplify is applied to *both* sides of the l.1790–92 comparison, so any rewrite is applied consistently |

## 2. Sites found in the neighbourhoods but NOT on the supplied list

* `…interpretation_discriminators_2026_08_21.py:1791` — the gate side of site #21.
  Symmetric with #1000, so **safe**, but it should be on the grep list.
* Nothing else new; the b167 and b168 runners are clean
  (`grep nsimplify` returns only prose lines asserting the absence).

**Discipline note, not a defect.** b166's header (l.90, l.170) says the inertia
helper *"carries NO sympy.nsimplify"* — that claim is scoped to the **helper**
and is true; the runner itself still carries two calls (l.1000, l.1791), both
display/symmetric. b169's disclosure 6 claims "no `nsimplify`" for its own
runner, which is a stronger and cleaner standard.

## 3. Repair sizing (for whoever executes it — nothing executed here)

All four NEEDS-REPAIR sites have the same one-line fix shape and none of them
changes any recorded numeral on correct input:

| site | fix |
|---|---|
| #2 `shear_gauge:511` | drop the wrapper — `Poly(...).all_coeffs()` on an exact matrix is already exact |
| #1 `adm_seam:861` | drop the wrapper — `sp.det` of an exact rational matrix is already a `Rational` |
| #9 `quotient_gate:633` | either `nsimplify(..., rational=True)` (verified total no-op on Rationals) or an explicit `assert v.is_Rational` so the assumption is declared |
| #11 `quotient_gate:1622/1623` | assert `tau.is_Rational` before `numer`/`denom`, or use `sp.fraction(sp.Rational(tau))`; this is the one that fails quiet |

## VERDICT / stdout summary

21 sites analysed. **4 NEEDS-REPAIR** (5 lines): `shear_gauge:511` —
nsimplify on characteristic-polynomial coefficients, the exact pattern b165
struck from the PSD-deciding routine; `adm_seam:861` — feeds a Sylvester
leading-minor PD certificate; `quotient_gate:633` — an undeclared rationality
assumption that `sp.Rational(v)` turns into a crash on generically irrational
principal cosines; and `quotient_gate:1622/1623` — the **only fail-quiet**
site, where `numer`/`denom` of a radical would return `(α, 1)` and silently
corrupt a rank/inertness substitution. **10 display-only.** **7 safe**,
including the best-designed one (`mass_survival_stratum:837`, self-verified by
an identity gate that fails loud). Measured probability of an actual flip is
low — nsimplify is a verified no-op on every exact Rational the lane produces
and only rewrites values that match an algebraic constant to ~8–15 digits — so
**no landed numeral is presumed wrong**; every one of the four is a *no-op on a
decision path*, which is precisely the standard b165 already applied to itself.
Two unrelated robustness flags surfaced in passing: `residue:1624` /
`quotient_gate:1763` compare ratios **structurally** (`!=`) where
`quotient_gate:1218` compares them **semantically** in the same lane, and
`residue:1695` compares an nsimplify'd value against a raw one asymmetrically.
