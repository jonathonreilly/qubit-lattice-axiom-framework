# EW-CKM Lattice cos²(θ_W) Complement Bridge: Bounded-Support Four-Way Equality, Support-Tier F5 Companion, and M_W/M_Z Closed Form

**Date:** 2026-04-26

**Status:** bounded support note; dependency-gated EW-CKM lattice-scale
complement bridge. This note preserves the exact value-level
`cos²(θ_W)|_lattice = 5/9` arithmetic and the associated M_W/M_Z closed
form, but it does **not** certify a retained theorem on the current
authority surface. Several authorities that the older version called
retained are now `unaudited`, `meta`, or decoration-scoped in the audit
ledger, and the YT_EW source has been repaired into a kappa-family no-go
surface rather than the old unconditional bare-coupling theorem.

**Reviewer correction (2026-04-26)**: an earlier draft of this note
claimed a "five-way retained identity" that included F5 from the
support-tier `CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`
inside the load-bearing equality. That overpromoted the support-tier
Koide-bridge surface. The current repair also demotes the older four-way
retained framing: the equality remains exact bounded support, with F5
kept as a SEPARATE auxiliary corroboration only (not load-bearing for
the bridge).

**Explicitly not a below-Wn closure**: like its sister bridge
`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`, this
note is a bounded cross-surface lattice-scale equality, not a below-Wn
derivation closure. The labeling follows the lesson from
`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`:
consistency equalities at current value-level inputs are useful support,
but not retained closure when their dependencies are not retained-grade.

**Primary runner:**
`scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py`

## Headline Identities (NEW)

```text
(C1)  cos²(θ_W)|_lattice  =  M_W² / M_Z² |_lattice
                          =  1 - A^4
                          =  (N_color² - N_pair²) / N_color²
                          =  (N_quark - 1) / N_color²
                          =  5/9                                  [FOUR-WAY BOUNDED EQUALITY]

(C1.aux) Support-tier companion reading (NOT part of the bounded
         four-way equality; auxiliary corroboration only):
            F5 (CKM n/9 family, support-tier) = 5/9.
         The matching value 5/9 is a NUMERICAL coincidence with the
         four-way bounded equality, not a fifth retained route.

(C2)  M_W / M_Z |_lattice =  √(N_quark - 1) / N_color
                          =  √5 / 3
                          ≈  0.7454                                [NEW closed form]

(C3)  tan²(θ_W)|_lattice  =  N_pair² / (N_quark - 1)
                          =  4/5                                   [NEW closed form]

(C4)  Structural-integer readings of historical YT_EW bare couplings (NEW
      structural interpretations at bounded values via S1):
        g_2² |_lattice  =  1/(d+1)  =  1/N_pair²
        g_Y² |_lattice  =  1/(d+2)  =  1/(N_quark - 1)
      Consistency-at-bounded-values reading; not a load-bearing closure
      that g_2² = 1/N_pair² is derived without YT_EW.

(C5)  SM-specific structural identity (NEW):
        N_color² - N_pair²  =  N_quark - 1
      Derivable from the W2 primitive `N_pair = N_color - 1`
      together with `N_color = 3`; specific to SM matter content
      (does NOT generalize to other N_pair, N_color).
```

## Reviewer Frame

This note explicitly:

- **Does NOT claim** below-W2 derivation closure for `cos²(θ_W)|_lattice`,
  `1 - A^4`, or `M_W² / M_Z² |_lattice`. It also does **not** claim the
  four-way equality is retained on the current surface.
- **Does claim**: exact bounded support for the four-way EW/CKM value-level
  equality at lattice scale
  (`cos²(θ_W) = 1 - A^4 = (N_color² - N_pair²)/N_color² = (N_quark - 1)/N_color² = 5/9`),
  a bounded closed form for the lattice-scale W/Z mass-squared ratio,
  structural-integer consistency readings of the historical YT_EW bare
  couplings via S1, and an SM-specific structural identity
  `N_color² - N_pair² = N_quark - 1` at the extracted S1 values.
- **Auxiliary support reading**: F5 = 5/9 from the support-tier
  `CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`
  is reported as a NUMERICAL companion reading only — NOT a load-bearing
  fifth route inside the bounded equality.

The lesson from `feedback_consistency_vs_derivation_below_w2.md`:
consistency equalities cannot load-bear below-Wn closures. This repaired
note is framed as bounded support until its dependency gates are audited
and retained independently.

## Statement

On current source files, with ledger dependency gates made explicit:

```text
(P1)  Historical YT_EW bare lattice couplings used by the old bridge:
        g_2² = 1/(d+1) = 1/4,   g_Y² = 1/(d+2) = 1/5,    d = dim(Z³) = 3.
      On current `main`, `YT_EW_COLOR_PROJECTION_THEOREM.md` is a
      kappa-family no-go/support surface, so this input is value-level
      bounded support rather than a retained dependency closure.

(P2)  EW Higgs gauge-mass diagonalization:
        cos²(θ_W) = g_2² / (g_2² + g_Y²),
        M_W² / M_Z² = cos²(θ_W),  ρ_tree = 1.

(P3)  W2 value: A² = N_pair / N_color = 2/3.
      ⇒ A^4 = (2/3)² = 4/9.

(P4)  S1 source literal:
      Q_L : (2,3)_{+1/3} in LEFT_HANDED_CHARGE_MATCHING_NOTE
      sources both N_pair = dim_SU2(Q_L) = 2 and
      N_color = dim_SU3(Q_L) = 3, with N_quark = N_pair × N_color = 6.

(P5)  Auxiliary support-tier CKM n/9 companion:
      F5 = (N_quark - 1)/N_color² = 5/9 = (1-A²)(1+A²) = 1 - A^4.

(P6)  Z³ axiom: spatial substrate dim d = 3,
      with structural SU(3)_c emerging via graph-first SU(3) integration
      (so the Z³-axiom d = 3 and S1's N_color = dim_SU3(Q_L) = 3 are tied
      by the framework's graph-first construction, not as two independent
      integers).
```

### Headline conclusions

```text
(T1)  cos²(θ_W)|_lattice  =  g_2²/(g_2² + g_Y²)   [from P1, P2]
                          =  (1/(d+1)) / [(1/(d+1)) + (1/(d+2))]
                          =  (d+2) / (2d + 3)
                          =  5/9                  [at d = 3].

(T2)  cos²(θ_W)|_lattice  =  1 - sin²(θ_W)|_lattice
                          =  1 - A^4               [from sister bridge value: sin²(θ_W) = A^4]
                          =  1 - 4/9
                          =  5/9                   [bounded consistency at current values].

(T3)  At extracted S1 values: N_pair = 2, N_color = 3, N_quark = 6.
      (N_color² - N_pair²) / N_color² = (9 - 4)/9 = 5/9.
      (N_quark - 1) / N_color²        = 5/9.

(T4)  FOUR-way BOUNDED equality at 5/9:
        cos²(θ_W)|_lattice  =  1 - A^4
                            =  (N_color² - N_pair²)/N_color²
                            =  (N_quark - 1)/N_color²
                            =  5/9.

(T4-aux)  Auxiliary support-tier companion:
          F5 (CKM n/9 family, support-tier) = 5/9.
          This is numerically compatible with T4 but is NOT a fifth
          retained route inside the bounded equality.

(T5)  M_W²/M_Z² |_lattice = cos²(θ_W)|_lattice = 5/9.
      ⇒ M_W/M_Z |_lattice = √5/3 = √(N_quark-1)/N_color ≈ 0.7454.

(T6)  tan²(θ_W)|_lattice  =  sin²/cos² = (4/9)/(5/9) = 4/5
                          =  N_pair²/(N_quark - 1).

(T7)  Structural-integer readings of historical YT_EW couplings at bounded values
      (via S1 + Z³ axiom; consistency at bounded values, NOT a
      derivation that g_2² = 1/N_pair² without YT_EW):
        g_2²|_lattice = 1/(d+1) = 1/(N_color + 1) = 1/N_pair²    [via S1: N_pair=2, with N_color=3]
        g_Y²|_lattice = 1/(d+2) = 1/(N_color + 2) = 1/(N_quark - 1)  [via S1+W2: N_quark-1=5, with N_color=3]

(T8)  SM-specific structural identity:
        N_color² - N_pair² = N_quark - 1.
      Equivalent to (N_color - N_pair)(N_color + N_pair) = N_quark - 1.
      With W2 primitive N_pair = N_color - 1:
        (1)(2N_color - 1) = N_color(N_color - 1) - 1
        ⇒ N_color² - 3N_color = 0
        ⇒ N_color = 3 (positive root).
      So at the W2 primitive N_pair = N_color - 1, the identity
      T8 holds iff N_color = 3 — a sharp SM-specific structural identity.
```

## Inputs and Current Dependency Gates

| Input | Source on `main` | Current gate | Role |
| --- | --- | --- | --- |
| Historical `g_2² = 1/(d+1)`, `g_Y² = 1/(d+2)`, `d = 3` | [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md) | Current note is a kappa-family no-go/support surface; old literals are not a retained dependency closure | T1, T7 bounded arithmetic source |
| `cos²(θ_W) = g²/(g²+g_Y²)`, `M_W²/M_Z² = cos²(θ_W)`, `ρ_tree = 1` | [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md) | retained in ledger | T1, T5 dictionary |
| `(W2)` `A² = N_pair/N_color = 2/3` | [`WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md`](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md) | unaudited in ledger | T2, T3 source |
| `Q_L : (2,3)_{+1/3}` (S1 source); `u_R, d_R : (1,3)` cross-check | [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md), [`ONE_GENERATION_MATTER_CLOSURE_NOTE.md`](ONE_GENERATION_MATTER_CLOSURE_NOTE.md) | decoration-scoped / unaudited in ledger | S1 / P4 source for N_pair, N_color |
| `sin²(θ_W)|_lattice = A^4 = 4/9` (sister bridge) | [`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`](CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md) | unaudited in ledger | T2 complement source |
| `N_pair = N_color - 1`; `N_pair = 2`, `N_color = 3` | [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | unaudited in ledger | T8 derivation |
| Z³ spatial substrate; SU(3)_c via graph-first integration | [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md), [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | old axiom note is meta/superseded; graph-first bridge is bounded | P6: ties d = N_color via graph-first construction |

**Auxiliary support-tier reading (NOT load-bearing for the bridge):**

| Input | Authority on `main` | Tier | Role |
| --- | --- | --- | --- |
| F5 = 5/9 = (N_quark-1)/N_color² = 1 - A^4 | [`CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`](CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md) | **support-tier** | T4-aux: companion numerical reading; NOT counted in the four-way equality |

The four-way equality is therefore a bounded-support equality on current
main: exact Fraction arithmetic verifies the shared value, but the row is
not ready to be treated as a retained theorem until the dependency gates
above are independently retained. The F5 reading is reported as a SEPARATE
support-tier auxiliary companion at the same numerical value — NOT a
load-bearing fifth route. T7 structural readings are consistency-at-bounded
values interpretations (NOT derivations). T8 is an SM-specific structural
identity at the extracted S1/W2 values.

## Derivation

### T1: cos²(θ_W)|_lattice from EW Higgs diagonalization + YT_EW

`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`
gives:

```text
cos²(θ_W) = g² / (g² + g_Y²)
M_W² / M_Z² = cos²(θ_W)  (with ρ_tree = 1).
```

Substituting the historical YT_EW bare-coupling values used by the old
bridge (`g_2² = 1/(d+1)`, `g_Y² = 1/(d+2)`, `d = 3`):

```text
cos²(θ_W)|_lattice = (1/(d+1)) / [(1/(d+1)) + (1/(d+2))]
                   = (d+2) / [(d+2) + (d+1)]
                   = (d+2) / (2d+3).
```

At `d = 3`: `cos²(θ_W)|_lattice = 5/9`.

### T2: Pythagorean complement to `A^4 = sin²(θ_W)|_lattice`

The sister bridge `CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`
carries the value `sin²(θ_W)|_lattice = A^4 = 4/9` at lattice scale.
On current main that row is dependency-gated rather than retained-grade.
Trivially:

```text
cos²(θ_W)|_lattice = 1 - sin²(θ_W)|_lattice = 1 - A^4 = 1 - 4/9 = 5/9.
```

This consistency equality holds at the bounded value-level inputs.

### T3, T4: Structural-integer readings via S1

S1 gives `N_pair = 2`, `N_color = 3`, `N_quark = 6` via the
`Q_L : (2,3)_{+1/3}` literal in
`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`. On current main this is a
dependency-gated source literal, not a retained corollary.

```text
(N_color² - N_pair²) / N_color² = (9 - 4)/9 = 5/9.
(N_quark - 1) / N_color²        = (6 - 1)/9 = 5/9.
```

These match `cos²(θ_W)|_lattice = 5/9` from T1 and `1 - A^4 = 5/9` from
T2 at bounded values, completing the **FOUR-WAY BOUNDED EQUALITY**:

```text
cos²(θ_W)|_lattice  =  1 - A^4  =  (N_color² - N_pair²)/N_color²
                                =  (N_quark - 1)/N_color²
                                =  5/9                    [FOUR-WAY BOUNDED].
```

A SEPARATE support-tier numerical companion reading at the same value:

```text
F5 (CKM n/9 family, support-tier) = 5/9  [auxiliary, NOT load-bearing].
```

`F5` is from `CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`
(support-tier; explicitly NOT a fifth retained route inside the
four-way equality — its agreement at 5/9 is a numerical companion,
not load-bearing for the bounded T1-T3b chain).

### T5: M_W²/M_Z²|_lattice closed form (NEW)

From T1 + `M_W²/M_Z² = cos²(θ_W)`:

```text
M_W²/M_Z² |_lattice = (N_quark - 1)/N_color² = 5/9.
M_W/M_Z |_lattice    = √(N_quark - 1)/N_color = √5/3 ≈ 0.7454.
```

This is a bounded closed form for the W/Z mass-squared ratio at lattice
scale, derived from the S1 source literal plus the historical YT_EW values
and EW Higgs diagonalization.

### T6: tan²(θ_W)|_lattice closed form (NEW)

```text
tan²(θ_W)|_lattice = sin²/cos² = (4/9)/(5/9) = 4/5
                   = N_pair²/(N_quark - 1).
```

NEW closed form derivable from the four-way structural integer fingerprint.

### T7: Structural-integer readings of g_2², g_Y² at bounded values

Substituting the extracted S1 values (`N_pair = 2`, `N_color = 3`, `N_quark = 6`)
and Z³ axiom (`d = 3 = N_color` by graph-first SU(3) integration):

```text
g_2²|_lattice = 1/(d+1) = 1/(N_color + 1) = 1/4 = 1/N_pair²
                                           [since N_pair² = (2)² = 4 = N_color + 1
                                            specifically at SM values
                                            via T8 below].

g_Y²|_lattice = 1/(d+2) = 1/(N_color + 2) = 1/5 = 1/(N_quark - 1)
                                           [since N_quark - 1 = 5 = N_color + 2
                                            specifically at SM values, since
                                            N_quark = N_color × N_pair = N_color(N_color - 1)
                                            with N_color = 3 gives 6,
                                            so N_quark - 1 = 5 = N_color + 2 only when N_color = 3].
```

These are structural readings of the historical YT_EW couplings via S1.
They are CONSISTENCY EQUALITIES at bounded values (per the rejected
A²-below-W2 lesson, they cannot load-bear a below-Wn closure), not
retained identity readings on the current surface.

### T8: SM-specific structural identity N_color² - N_pair² = N_quark - 1 (NEW)

Setting `N_pair = N_color - 1` (W2 primitive) and substituting
into `N_color² - N_pair² = N_quark - 1 = N_pair × N_color - 1`:

```text
N_color² - (N_color - 1)² = N_color(N_color - 1) - 1
N_color² - N_color² + 2N_color - 1 = N_color² - N_color - 1
2N_color - 1 = N_color² - N_color - 1
N_color² - 3N_color = 0
N_color(N_color - 3) = 0
⇒ N_color = 3 (positive root, dropping N_color = 0 as unphysical).
```

So **`N_color² - N_pair² = N_quark - 1` holds, given
`N_pair = N_color - 1`, IFF `N_color = 3`** — the SM value.

This provides a sharp algebraic characterization of the SM matter content:
the identity T8 fails for any other (`N_color, N_pair, N_quark`) consistent
with `N_pair = N_color - 1`. This is a NEW structural fingerprint of the
SM at the level of the CKM count primitive.

## Numerical Verification

All identities verified to **exact integer/Fraction arithmetic** in the runner.

| Identity | Source | Value | Match? |
| --- | --- | ---: | --- |
| T1: cos²(θ_W) = g_2²/(g_2² + g_Y²) | historical YT_EW values + EW Higgs diag | 5/9 | ✓ |
| T2: cos²(θ_W) = 1 - A^4 | sister bridge + W2 value | 5/9 | ✓ |
| T3a: (N_color² - N_pair²)/N_color² | S1 source literal | 5/9 | ✓ |
| T3b: (N_quark - 1)/N_color² | S1 source literal | 5/9 | ✓ |
| T4: FOUR-WAY BOUNDED equality at 5/9 | T1 ∧ T2 ∧ T3a ∧ T3b (dependency-gated) | 5/9 | ✓ |
| T4-aux: F5 support-tier companion at 5/9 | CKM_N9_FAMILY (support, NOT load-bearing) | 5/9 | ✓ (auxiliary only) |
| T5: M_W²/M_Z²|_lattice | T1 + EW Higgs | 5/9 | ✓ |
| T5b: M_W/M_Z|_lattice | square root of T5 | √5/3 ≈ 0.7454 | ✓ |
| T6: tan²(θ_W)|_lattice | sin²/cos² | 4/5 | ✓ |
| T7a: g_2² = 1/N_pair² (consistency) | YT_EW + S1 | 1/4 | ✓ |
| T7b: g_Y² = 1/(N_quark - 1) (consistency) | YT_EW + S1 | 1/5 | ✓ |
| T8: N_color² - N_pair² = N_quark - 1 (SM) | W2 primitive + N_color = 3 | 5 = 5 | ✓ |
| T8 derivation: N_color² - 3N_color = 0 ⇒ N_color = 3 | algebra | N_color = 3 | ✓ |

## Science Value

### What this lets the framework state cleanly

Previously the `A^4 = sin²(θ_W)|_lattice = 4/9` bridge
(`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`) tied
the EW Weinberg angle (lattice) and the Wolfenstein A parameter via a
two-way consistency equality.

This complement bridge gives bounded support for:

1. **Four-way bounded equality + support-tier F5 companion**:
   `cos²(θ_W)|_lattice = 1 - A^4 = (N_color² - N_pair²)/N_color² = (N_quark - 1)/N_color² = 5/9`
   ties the EW gauge sector, Wolfenstein A, and S1 structural integers
   in a four-way dependency-gated equality. The support-tier F5 = 5/9
   reading from the CKM n/9 family is a SEPARATE numerical companion
   at the same value, NOT a load-bearing fifth route inside the
   bounded equality.

2. **NEW W/Z mass ratio**: `M_W/M_Z|_lattice = √(N_quark - 1)/N_color = √5/3`,
   a NEW closed form for a directly observable physical quantity at
   lattice scale (SHARP structural prediction; running provides physical
   M_Z scale value).

3. **NEW structural readings of YT_EW**: `g_2²|_lattice = 1/N_pair²` and
   `g_Y²|_lattice = 1/(N_quark - 1)` are NEW interpretations of the
   historical YT_EW bare couplings via S1. These are consistency-at-bounded-values
   readings (per the rejected A²-below-W2 lesson, NOT load-bearing for
   below-Wn closures), but are NEW structural-integer interpretations.

4. **NEW SM-specific structural identity**: `N_color² - N_pair² = N_quark - 1`,
   sharp algebraic characterization of the SM matter content given the
   `N_pair = N_color - 1` primitive. This identity fails for
   any other (N_color, N_pair) consistent with the primitive — a new
   SM-fingerprint structural relation.

### NEW structural form of M_W/M_Z at lattice scale

The W/Z mass ratio at lattice scale is:

```text
M_W/M_Z |_lattice  =  √(N_quark - 1) / N_color  =  √5/3 ≈ 0.7454.
```

PDG values (physical, at M_Z): M_W ≈ 80.379 GeV, M_Z ≈ 91.188 GeV.
M_W/M_Z |_PDG ≈ 0.8815. The framework's lattice-scale prediction
`0.7454` differs because the running from lattice to physical scale
shifts cos²(θ_W) substantially (similarly to how `sin²(θ_W)|_lattice = 4/9 ≈ 0.4444`
runs to `sin²(θ_W)|_PDG ≈ 0.2312`).

The lattice-scale identity is the structural anchor; running provides
the physical match if the needed running bridge is supplied separately.

### Structural-integer readings via S1

The previous A²-below-W2 closure attempt (rejected) tried to use
`g_2² = 1/N_pair²` as a load-bearing route — the reviewer dismissed
this as a numerical coincidence. The lesson preserved here is:
structural-integer readings of YT_EW retained couplings are valid
**interpretations at bounded values** but cannot load-bear a
below-Wn closure on their own.

Here we use them honestly: the structural readings T7a, T7b are
labeled "consistency at bounded values"; they are not used to close a
retained theorem.

### What this does NOT claim

- Does NOT claim below-Wn closure for `cos²(θ_W)|_lattice`,
  `1 - A^4 = 5/9`, or `M_W²/M_Z²|_lattice`. The current row is bounded
  support because several dependency gates are not retained-grade.
- Does NOT promote any support-tier theorem to retained.
- Does NOT predict physical `M_W/M_Z` at the M_Z scale (the lattice
  ratio `√5/3` runs to PDG `≈ 0.8815` via separate framework running).
- Does NOT modify the sister bridge `A^4 = sin²(θ_W) = 4/9`;
  this note COMPLEMENTS it.
- Does NOT derive `g_2² = 1/N_pair²` or `g_Y² = 1/(N_quark - 1)` as a
  closed-form below-Wn route — these are CONSISTENCY-AT-BOUNDED-VALUES
  readings only (per the rejected A²-below-W2 lesson).

### Falsifiable structural claims

1. `cos²(θ_W)|_lattice = 5/9` (sharp lattice-scale prediction).
2. `M_W²/M_Z²|_lattice = 5/9`, `M_W/M_Z|_lattice = √5/3` (NEW direct W/Z
   ratio prediction at lattice scale).
3. `N_color² - N_pair² = N_quark - 1` (SM-specific structural identity;
   FAILS for any other N_color consistent with W2 primitive).
4. Four-way bounded equality `cos²(θ_W)|_lattice = 1 - A^4 = (N_color² - N_pair²)/N_color²
   = (N_quark - 1)/N_color² = 5/9` at current value-level inputs,
   plus a separate support-tier F5 = 5/9 numerical companion that is
   auxiliary, not a fifth retained route.

### Why this counts as pushing the science forward

1. **NEW unified FOUR-WAY BOUNDED equality at lattice scale (plus
   support-tier F5 companion)**: previously only `4/9` had been
   bridged across EW-CKM. Now the COMPLEMENT `5/9` is bridged across
   four dependency-gated value-level surfaces (EW gauge, Wolfenstein A, structural
   integers via S1 in two equivalent forms, M_W/M_Z mass ratio), with
   the support-tier F5 = 5/9 reading from the CKM n/9 family included
   only as a separate numerical companion (not a fifth retained route).

2. **NEW W/Z mass ratio closed form at lattice scale**: `M_W/M_Z|_lattice
   = √(N_quark - 1)/N_color = √5/3` is a direct physical observable
   prediction (modulo running) derived from the framework's structural
   integer source theorem (S1).

3. **NEW SM-specific structural identity**: `N_color² - N_pair² = N_quark - 1`
   provides a SHARP algebraic characterization of the SM matter content
   given the W2 primitive. The identity fails for any non-SM
   value of N_color, making it a structural fingerprint of the framework's
   SM closure.

4. **Honest framing**: explicit non-promotion of consistency equalities
   to closure status (per the rejected A²-below-W2 lesson). The bridge
   is labeled as bounded support, NOT a retained lattice-scale identity
   theorem and NOT a below-Wn closure.

## What This Claims

- `(C1)`: cos²(θ_W)|_lattice = 1 - A^4 = (N_color² - N_pair²)/N_color² = (N_quark-1)/N_color² = 5/9.
- `(C2)`: M_W/M_Z|_lattice = √(N_quark-1)/N_color = √5/3.
- `(C3)`: tan²(θ_W)|_lattice = N_pair²/(N_quark-1) = 4/5.
- `(C5)`: SM-specific structural identity N_color² - N_pair² = N_quark - 1
  (derivable from W2 primitive + N_color = 3).

## What This Does NOT Claim

- Does NOT promote any support-tier theorem to retained.
- Does NOT use consistency equalities as load-bearing closure routes.
- Does NOT claim below-Wn derivation for cos²(θ_W) or M_W/M_Z.
- Does NOT predict physical M_W/M_Z at PDG scale (lattice anchor only).
- Does NOT modify sister bridge A^4 = 4/9.
- Does NOT cite any unmerged branches as retained authorities.

## Reproduction

```bash
python3 scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py
```

Expected result:

```text
TOTAL: PASS=N, BOUNDARY=M, HARD_ISSUES=0
COS_SQ_THETA_W_LATTICE_COMPLEMENT_BRIDGE_VERIFIED = TRUE
M_W_M_Z_LATTICE_RATIO_DERIVED = TRUE
SM_STRUCTURAL_IDENTITY_N_COLOR_3_DERIVED = TRUE
```

The runner:

1. Reads each cited authority file from disk and checks ledger
   `effective_status` dependency gates.
2. Checks whether the old YT_EW closed forms `g_2² = 1/(d+1)`,
   `g_Y² = 1/(d+2)` are still present in
   `YT_EW_COLOR_PROJECTION_THEOREM.md`; missing old literals are reported
   as a boundary, not as retained authority.
3. Extracts Q_L representation literal `(2,3)` from
   `LEFT_HANDED_CHARGE_MATCHING_NOTE.md` (S1 source literal).
4. Checks `cos²(θ_W)|_lattice` via T1 (EW Higgs + historical YT_EW values) and verifies
   it equals 5/9 by exact Fraction arithmetic.
5. Cross-checks via T2 (1 - A^4), T3 (S1 structural integers), and T8
   (SM-specific identity).
6. Derives `M_W/M_Z|_lattice = √5/3` via T5.
7. Derives `tan²(θ_W)|_lattice = 4/5` via T6.
8. Verifies T8: `N_color² - N_pair² = N_quark - 1` at extracted values,
   AND solves the algebraic constraint to confirm `N_color = 3` is the
   unique positive solution given W2 primitive.

## Cross-References

**Current dependency gates used in T1-T6:**

- [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  — current kappa-family no-go/support surface; the old bare-coupling
  literals are bounded historical inputs here.
- [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
  — retained ledger dependency; `cos²(θ_W) = g²/(g² + g_Y²)`, `M_W²/M_Z² = cos²(θ_W)`.
- [`WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md`](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md)
  — current ledger gate is unaudited for `(W2)` `A² = N_pair/N_color = 2/3`.
- [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md)
  — decoration-scoped ledger gate; `Q_L : (2,3)_{+1/3}` source for S1 (P4).
- [`ONE_GENERATION_MATTER_CLOSURE_NOTE.md`](ONE_GENERATION_MATTER_CLOSURE_NOTE.md)
  — unaudited ledger gate; `u_R, d_R : (1,3)` cross-check on N_color via S1.
- [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md)
  — unaudited ledger gate for `N_pair = N_color - 1` primitive (W2 source for T8).
- [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md) — superseded/meta
  framework source for the old Z³ wording.
- [`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`](CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md)
  — sister bridge; `sin²(θ_W)|_lattice = A^4 = 4/9` (T2 complement source).
- [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md)
  — preceding branch; S1 Identification Source Theorem.

**Support-tier auxiliary reading (NOT load-bearing for T1-T6):**

- [`CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`](CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md)
  — support-tier; F5 = 5/9 = (N_quark-1)/N_color² = 1 - A^4 (auxiliary companion reading).

**Bounded-retained framework:**

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  — bounded-retained structural gauge theorem; ties Z³ axiom (d=3) to
  emergent structural SU(3)_c, supporting the d = N_color identification.

**NOT cited as derivation input:**

- CL3_TASTE_GENERATION_THEOREM (support-tier; not used).
- Any unmerged branches.
