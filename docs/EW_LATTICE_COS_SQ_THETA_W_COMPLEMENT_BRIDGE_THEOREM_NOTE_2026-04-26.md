# EW-CKM Lattice cos²(θ_W) Complement Bridge (Historical Title; Defined-Readout Scope)

**Date:** 2026-04-26

**Type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not
set an audit verdict or effective status. It proves exact equalities among
defined scalar readouts and separately supplied count/coupling values; any
physical weak-angle or particle-mass interpretation remains an open premise.

**Reviewer correction (2026-04-26)**: an earlier draft of this note
claimed a "five-way retained identity" that included F5 from the
support-tier `CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`
inside the load-bearing equality. That overpromoted the support-tier
Koide-bridge surface. The retained result is correctly framed here as
a FOUR-way EW/CKM equality at retained tier, plus a SEPARATE
support-tier F5 companion reading that is auxiliary corroboration
only (not load-bearing for the bridge).

**Explicitly not a below-Wn or physical-EW closure**: like its historical sister bridge
`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`, this
note is a retained cross-surface lattice-scale identity, not a
below-Wn derivation closure. The labeling follows the lesson from
`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`:
consistency equalities at supplied values are algebraically valid but are not
load-bearing below-Wn or physical-observable closures.

**Primary runner:**
`scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py`

**2026-07-16 dependency repair:** the cited diagonalization theorem now proves
only a defined `C^2` quadratic-form identity. Accordingly, every use below of
`cos²(theta_W)`, `M_W²`, `M_Z²`, `M_W/M_Z`, or `rho_tree` that descends from
that theorem denotes the formal scalar labels `c²`, `MW2`, `MZ2`,
`sqrt(MW2/MZ2)`, and `rho`; the legacy symbols do not identify a physical weak
angle or particle masses. The exact `5/9` coincidence survives as defined
algebra after the separate coupling values are supplied. Its lattice-EW,
W/Z-mass, and physical interpretation remains an open bridge not furnished by
this note or the diagonalization theorem.

## Headline identities

```text
(C1)  c²|_assigned couplings  =  MW2 / MZ2
                          =  1 - A^4
                          =  (N_color² - N_pair²) / N_color²
                          =  (N_quark - 1) / N_color²
                          =  5/9                                  [FOUR-WAY FORMAL EQUALITY]

(C1.aux) Support-tier companion reading (NOT part of the retained
         four-way equality; auxiliary corroboration only):
            F5 (CKM n/9 family, support-tier) = 5/9.
         The matching value 5/9 is a NUMERICAL coincidence with the
         four-way formal equality, not a fifth retained route.

(C2)  sqrt(MW2/MZ2) =  √(N_quark - 1) / N_color
                          =  √5 / 3
                          ≈  0.7454                                [NEW closed form]

(C3)  s²/c² at the assigned couplings = N_pair² / (N_quark - 1)
                          =  4/5                                   [NEW closed form]

(C4)  Structural-integer readings of YT_EW retained bare couplings (NEW
      structural interpretations at retained values via S1):
        g_2² |_lattice  =  1/(d+1)  =  1/N_pair²
        g_Y² |_lattice  =  1/(d+2)  =  1/(N_quark - 1)
      Consistency-at-retained-values reading; not a load-bearing closure
      that g_2² = 1/N_pair² is derived without YT_EW.

(C5)  SM-specific structural identity (NEW):
        N_color² - N_pair²  =  N_quark - 1
      Derivable from retained primitive `N_pair = N_color - 1` (W2)
      together with `N_color = 3`; specific to SM matter content
      (does NOT generalize to other N_pair, N_color).
```

## Reviewer Frame

This note explicitly:

- **Does NOT claim** below-W2 derivation closure for the formal `c²` or
  `MW2/MZ2`, `1 - A^4`, or any physical weak-angle/mass ratio. Each algebraic side has
  its own retained authority, and their numerical coincidence at `5/9` is
  a CONSISTENCY EQUALITY at retained values.
- **Does claim**: an exact four-way formal equality
  (`c² = 1 - A^4 = (N_color² - N_pair²)/N_color² =
  (N_quark - 1)/N_color²`) after the named values are supplied, a closed form
  for the formal scalar-readout ratio, structural-integer readings of the
  supplied couplings, and the SM-specific structural identity
  `N_color² - N_pair² = N_quark - 1`.
- **Auxiliary support reading**: F5 = 5/9 from the support-tier
  `CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`
  is reported as a NUMERICAL companion reading only — NOT a load-bearing
  fifth route inside the retained equality.

The lesson from `feedback_consistency_vs_derivation_below_w2.md`:
consistency equalities are valid retained identity theorems but cannot
load-bear below-Wn closures. This note is framed as the former, NOT the
latter — exactly like the retained sister bridge for the `4/9` side.

## Statement

Given the following cited algebraic/count inputs:

```text
(P1)  Supply the numerical coupling assignment for this formal theorem:
        g_2² = 1/(d+1) = 1/4,   g_Y² = 1/(d+2) = 1/5,    d = dim(Z³) = 3.
      No physical scale or electroweak interpretation is inferred.

(P2)  Defined C^2 quadratic-form diagonalization:
        c² = g_2² / (g_2² + g_Y²),
        MW2 / MZ2 = c²,  rho = 1.
      These are formal labels, not a physical weak angle or mass relation.

(P3)  W2 retained: A² = N_pair / N_color = 2/3.
      ⇒ A^4 = (2/3)² = 4/9.

(P4)  S1 (Identification Source Theorem, just landed):
      Q_L : (2,3)_{+1/3} retained in LEFT_HANDED_CHARGE_MATCHING_NOTE
      sources both N_pair = dim_SU2(Q_L) = 2 and
      N_color = dim_SU3(Q_L) = 3, with N_quark = N_pair × N_color = 6.

(P5)  Auxiliary support-tier CKM n/9 companion:
      F5 = (N_quark - 1)/N_color² = 5/9 = (1-A²)(1+A²) = 1 - A^4.

(P6)  Z³ axiom (MINIMAL_AXIOMS): spatial substrate dim d = 3,
      with structural SU(3)_c emerging via graph-first SU(3) integration
      (so the Z³-axiom d = 3 and S1's N_color = dim_SU3(Q_L) = 3 are tied
      by the framework's graph-first construction, not as two independent
      integers).
```

### Headline conclusions

```text
(T1)  c²|_assigned couplings  =  g_2²/(g_2² + g_Y²)   [from P1, P2]
                          =  (1/(d+1)) / [(1/(d+1)) + (1/(d+2))]
                          =  (d+2) / (2d + 3)
                          =  5/9                  [at retained d = 3].

(T2)  c²|_assigned couplings  =  1 - s²|_assigned couplings
                          =  1 - A^4               [from retained S5: sin²(θ_W) = A^4]
                          =  1 - 4/9
                          =  5/9                   [consistency at retained values].

(T3)  At retained values (S1): N_pair = 2, N_color = 3, N_quark = 6.
      (N_color² - N_pair²) / N_color² = (9 - 4)/9 = 5/9.
      (N_quark - 1) / N_color²        = 5/9.

(T4)  FOUR-way FORMAL equality at 5/9:
        c²|_assigned couplings  =  1 - A^4
                            =  (N_color² - N_pair²)/N_color²
                            =  (N_quark - 1)/N_color²
                            =  5/9.

(T4-aux)  Auxiliary support-tier companion:
          F5 (CKM n/9 family, support-tier) = 5/9.
          This is numerically compatible with T4 but is NOT a fifth
          retained route inside the load-bearing equality.

(T5)  MW2/MZ2 = c² = 5/9.
      Therefore sqrt(MW2/MZ2) = √5/3 = √(N_quark-1)/N_color.

(T6)  s²/c² at the assigned couplings = (4/9)/(5/9) = 4/5
                          =  N_pair²/(N_quark - 1).

(T7)  Structural-integer readings of YT_EW couplings at retained values
      (via S1 + Z³ axiom; consistency at retained values, NOT a
      derivation that g_2² = 1/N_pair² without YT_EW):
        g_2²|_lattice = 1/(d+1) = 1/(N_color + 1) = 1/N_pair²    [via S1: N_pair=2, with N_color=3]
        g_Y²|_lattice = 1/(d+2) = 1/(N_color + 2) = 1/(N_quark - 1)  [via S1+W2: N_quark-1=5, with N_color=3]

(T8)  SM-specific structural identity:
        N_color² - N_pair² = N_quark - 1.
      Equivalent to (N_color - N_pair)(N_color + N_pair) = N_quark - 1.
      With retained primitive N_pair = N_color - 1 (W2):
        (1)(2N_color - 1) = N_color(N_color - 1) - 1
        ⇒ N_color² - 3N_color = 0
        ⇒ N_color = 3 (positive root).
      So at the retained primitive N_pair = N_color - 1, the identity
      T8 holds iff N_color = 3 — a sharp SM-specific structural identity.
```

## Retained Inputs (Explicitly Tagged by Authority Tier)

| Input | Authority on `main` | Tier | Role |
| --- | --- | --- | --- |
| `g_2² = 1/(d+1)`, `g_Y² = 1/(d+2)`, `d = 3` | explicit assignment in this note; `YT_EW_COLOR_PROJECTION_THEOREM.md` is historical context only | supplied, not derived | T1, T7 input |
| formal `c² = g²/(g²+g_Y²)`, `MW2/MZ2 = c²`, `rho = 1` | [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md) | defined finite-dimensional algebra; no physical identification | T1, T5 algebra |
| `(W2)` `A² = N_pair/N_color = 2/3` | [`WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md`](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md) | **retained** | T2, T3 source |
| `Q_L : (2,3)_{+1/3}` (S1 source); `u_R, d_R : (1,3)` cross-check | [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md), [`ONE_GENERATION_MATTER_CLOSURE_NOTE.md`](ONE_GENERATION_MATTER_CLOSURE_NOTE.md) | **retained corollary**, **retained** | S1 / P4 source for N_pair, N_color |
| `s²|_assigned couplings = A^4 = 4/9` (sister bridge) | [`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`](CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md) | **retained** | T2 complement source |
| `N_pair = N_color - 1`; `N_pair = 2`, `N_color = 3` | [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | **retained** | T8 derivation |
| Z³ spatial substrate; SU(3)_c via graph-first integration | [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md), [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | **retained** framework + **bounded-retained** | P6: ties d = N_color via graph-first construction |

**Auxiliary support-tier reading (NOT load-bearing for the bridge):**

| Input | Authority on `main` | Tier | Role |
| --- | --- | --- | --- |
| F5 = 5/9 = (N_quark-1)/N_color² = 1 - A^4 | [`CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`](CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md) | **support-tier** | T4-aux: companion numerical reading; NOT counted in formal four-way equality |

The formal four-way equality uses cited supplied values plus the defined
quadratic-form theorem
(T1, T2, T3a, T3b — the four routes are defined ratio + assigned couplings, sister A^4
complement, S1-derived (N_color²-N_pair²)/N_color², S1-derived
(N_quark-1)/N_color²). The F5 reading is reported as a SEPARATE
support-tier auxiliary companion at the same numerical value — NOT a
load-bearing fifth route. T7 structural readings are
consistency-at-retained-values interpretations (NOT derivations). T8
is an SM-specific structural identity derivable from retained W2 +
N_color = 3.

## Derivation

### T1: formal c² from defined diagonalization plus supplied coupling values

`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md` gives only:

```text
c² = g² / (g² + g_Y²)
MW2 / MZ2 = c²  (with formal rho = 1).
```

Substituting the supplied coupling assignment (`g_2² = 1/(d+1)`,
`g_Y² = 1/(d+2)`, `d = 3`):

```text
c²|_assigned couplings = (1/(d+1)) / [(1/(d+1)) + (1/(d+2))]
                   = (d+2) / [(d+2) + (d+1)]
                   = (d+2) / (2d+3).
```

At `d = 3`: the defined readout is `c² = 5/9`.

### T2: Pythagorean complement to retained `A^4 = s²|_assigned couplings`

The retained sister bridge `CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`
retains `s²|_assigned couplings = A^4 = 4/9` at lattice scale. Trivially:

```text
c²|_assigned couplings = 1 - s²|_assigned couplings = 1 - A^4 = 1 - 4/9 = 5/9.
```

This consistency equality holds at retained values.

### T3, T4: Structural-integer readings via S1

S1 (Identification Source Theorem) gives `N_pair = 2`, `N_color = 3`,
`N_quark = 6` via the retained `Q_L : (2,3)_{+1/3}` literal in
`LEFT_HANDED_CHARGE_MATCHING_NOTE.md` (retained corollary).

```text
(N_color² - N_pair²) / N_color² = (9 - 4)/9 = 5/9.
(N_quark - 1) / N_color²        = (6 - 1)/9 = 5/9.
```

These match `c²|_assigned couplings = 5/9` from T1 and `1 - A^4 = 5/9` from
T2 at retained values, completing the **FOUR-WAY FORMAL EQUALITY**:

```text
c²|_assigned couplings  =  1 - A^4  =  (N_color² - N_pair²)/N_color²
                                =  (N_quark - 1)/N_color²
                                =  5/9                    [FOUR-WAY FORMAL].
```

A SEPARATE support-tier numerical companion reading at the same value:

```text
F5 (CKM n/9 family, support-tier) = 5/9  [auxiliary, NOT load-bearing].
```

`F5` is from `CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`
(support-tier; explicitly NOT a fifth retained route inside the
four-way equality — its agreement at 5/9 is a numerical companion,
not load-bearing for the retained T1-T3b chain).

### T5: formal MW2/MZ2 closed form

From T1 plus the defined `MW2/MZ2 = c²`:

```text
MW2/MZ2 = (N_quark - 1)/N_color² = 5/9.
sqrt(MW2/MZ2) = √(N_quark - 1)/N_color = √5/3 ≈ 0.7454.
```

This is a closed form for the defined scalar-readout ratio, derived from the
cited count/coupling sources plus defined matrix algebra. No physical W/Z mass
ratio follows without a separate physical identification.

### T6: (s²/c²)|_assigned couplings closed form (NEW)

```text
(s²/c²)|_assigned couplings = sin²/cos² = (4/9)/(5/9) = 4/5
                   = N_pair²/(N_quark - 1).
```

NEW closed form derivable from the four-way structural integer fingerprint.

### T7: Structural-integer readings of g_2², g_Y² at retained values (NEW)

Substituting retained S1 (`N_pair = 2`, `N_color = 3`, `N_quark = 6`)
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

These are NEW STRUCTURAL READINGS of the retained YT_EW couplings via S1.
They are CONSISTENCY EQUALITIES at retained values (per the rejected
A²-below-W2 lesson, they cannot load-bear a below-Wn closure), but they
ARE valid retained identity readings.

### T8: SM-specific structural identity N_color² - N_pair² = N_quark - 1 (NEW)

Setting `N_pair = N_color - 1` (retained W2 primitive) and substituting
into `N_color² - N_pair² = N_quark - 1 = N_pair × N_color - 1`:

```text
N_color² - (N_color - 1)² = N_color(N_color - 1) - 1
N_color² - N_color² + 2N_color - 1 = N_color² - N_color - 1
2N_color - 1 = N_color² - N_color - 1
N_color² - 3N_color = 0
N_color(N_color - 3) = 0
⇒ N_color = 3 (positive root, dropping N_color = 0 as unphysical).
```

So **`N_color² - N_pair² = N_quark - 1` holds, given retained
`N_pair = N_color - 1`, IFF `N_color = 3`** — the SM value.

This provides a sharp algebraic characterization of the SM matter content:
the identity T8 fails for any other (`N_color, N_pair, N_quark`) consistent
with `N_pair = N_color - 1`. This is a NEW structural fingerprint of the
SM at the level of the retained CKM count primitive.

## Numerical Verification

All identities verified to **exact integer/Fraction arithmetic** in the runner.

| Identity | Source | Value | Match? |
| --- | --- | ---: | --- |
| T1: formal c² = g_2²/(g_2² + g_Y²) | supplied couplings + defined matrix algebra | 5/9 | ✓ |
| T2: formal c² = 1 - A^4 | sister bridge + W2 | 5/9 | ✓ |
| T3a: (N_color² - N_pair²)/N_color² | S1 (retained) | 5/9 | ✓ |
| T3b: (N_quark - 1)/N_color² | S1 (retained) | 5/9 | ✓ |
| T4: FOUR-WAY FORMAL equality at 5/9 | T1 ∧ T2 ∧ T3a ∧ T3b (all retained) | 5/9 | ✓ |
| T4-aux: F5 support-tier companion at 5/9 | CKM_N9_FAMILY (support, NOT load-bearing) | 5/9 | ✓ (auxiliary only) |
| T5: formal MW2/MZ2 | T1 + defined matrix algebra | 5/9 | ✓ |
| T5b: formal sqrt(MW2/MZ2) | positive square root of T5 | √5/3 ≈ 0.7454 | ✓ |
| T6: (s²/c²)|_assigned couplings | sin²/cos² | 4/5 | ✓ |
| T7a: g_2² = 1/N_pair² (consistency) | YT_EW + S1 | 1/4 | ✓ |
| T7b: g_Y² = 1/(N_quark - 1) (consistency) | YT_EW + S1 | 1/5 | ✓ |
| T8: N_color² - N_pair² = N_quark - 1 (SM) | W2 primitive + N_color = 3 | 5 = 5 | ✓ |
| T8 derivation: N_color² - 3N_color = 0 ⇒ N_color = 3 | algebra | N_color = 3 | ✓ |

## Science Value

### What this lets the framework state cleanly

Previously the retained `A^4 = s²|_assigned couplings = 4/9` bridge
(`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`) tied
the EW Weinberg angle (lattice) and the Wolfenstein A parameter via a
retained two-way consistency equality.

This complement bridge tightens that to:

1. **Four-way retained equality + support-tier F5 companion**:
   `c²|_assigned couplings = 1 - A^4 = (N_color² - N_pair²)/N_color² = (N_quark - 1)/N_color² = 5/9`
   ties the EW gauge sector, Wolfenstein A, and S1 structural integers
   in a four-way formal equality. The support-tier F5 = 5/9
   reading from the CKM n/9 family is a SEPARATE numerical companion
   at the same value, NOT a load-bearing fifth route inside the
   retained equality.

2. **Formal readout ratio**:
   `sqrt(MW2/MZ2) = √(N_quark - 1)/N_color = √5/3` is a closed form for
   defined scalar labels. It is not a directly observable W/Z mass ratio.

3. **NEW structural readings of YT_EW**: `g_2²|_lattice = 1/N_pair²` and
   `g_Y²|_lattice = 1/(N_quark - 1)` are NEW interpretations of the
   retained YT_EW bare couplings via S1. These are consistency-at-retained-values
   readings (per the rejected A²-below-W2 lesson, NOT load-bearing for
   below-Wn closures), but are NEW structural-integer interpretations.

4. **NEW SM-specific structural identity**: `N_color² - N_pair² = N_quark - 1`,
   sharp algebraic characterization of the SM matter content given the
   retained `N_pair = N_color - 1` primitive. This identity FAILS for
   any other (N_color, N_pair) consistent with the primitive — a new
   SM-fingerprint structural relation.

### Structural form of the formal readout ratio

The positive square root of the defined readout ratio is:

```text
sqrt(MW2/MZ2) = √(N_quark - 1) / N_color = √5/3 ≈ 0.7454.
```

No PDG comparison or running statement is licensed by this identity. A
physical W/Z-mass interpretation and the scale/running map needed for such a
comparison are separate open premises.

### Structural-integer readings via S1

The previous A²-below-W2 closure attempt (rejected) tried to use
`g_2² = 1/N_pair²` as a load-bearing route — the reviewer dismissed
this as a numerical coincidence. The lesson preserved here is:
structural-integer readings of YT_EW retained couplings are valid
**interpretations at retained values** but cannot load-bear a
below-Wn closure on their own.

Here the structural readings T7a and T7b are labeled "consistency at supplied
values". T1 uses the separately supplied coupling values and the defined
quadratic-form identity, not a physical electroweak interpretation.

### What this does NOT claim

- Does NOT claim below-Wn closure for `c²`, `1 - A^4 = 5/9`, or
  `MW2/MZ2`. Their numerical coincidence is a formal consistency equality
  after the cited values are supplied.
- Does NOT promote any support-tier theorem to retained.
- Does NOT predict physical `M_W/M_Z` at any scale and does not make a PDG or
  running comparison.
- Does NOT modify the retained sister bridge `A^4 = sin²(θ_W) = 4/9`;
  this note COMPLEMENTS it.
- Does NOT derive `g_2² = 1/N_pair²` or `g_Y² = 1/(N_quark - 1)` as a
  closed-form below-Wn route — these are CONSISTENCY-AT-RETAINED-VALUES
  readings only (per the rejected A²-below-W2 lesson).

### Falsifiable structural claims

1. The formal scalar identity `c² = 5/9` after the cited coupling assignment.
2. The formal identities `MW2/MZ2 = 5/9` and
   `sqrt(MW2/MZ2) = √5/3`; neither is a direct W/Z prediction.
3. `N_color² - N_pair² = N_quark - 1` (SM-specific structural identity;
   FAILS for any other N_color consistent with W2 primitive).
4. Four-way formal equality `c²|_assigned couplings = 1 - A^4 = (N_color² - N_pair²)/N_color²
   = (N_quark - 1)/N_color² = 5/9` at retained values (NEW unification),
   plus a separate support-tier F5 = 5/9 numerical companion that is
   auxiliary, not a fifth retained route.

### Why this counts as pushing the science forward

1. **Unified four-way formal equality at the assigned values (plus
   support-tier F5 companion)**: previously only `4/9` had been
   bridged across EW-CKM. Now the COMPLEMENT `5/9` is bridged across
   four algebraic surfaces (the formal coupling ratio, Wolfenstein A,
   structural integers via S1 in two equivalent forms, and the formal
   scalar-readout ratio), with
   the support-tier F5 = 5/9 reading from the CKM n/9 family included
   only as a separate numerical companion (not a fifth retained route).

2. **Formal scalar-readout closed form**:
   `sqrt(MW2/MZ2) = √(N_quark - 1)/N_color = √5/3` is exact defined
   algebra. A physical W/Z interpretation is not derived.

3. **NEW SM-specific structural identity**: `N_color² - N_pair² = N_quark - 1`
   provides a SHARP algebraic characterization of the SM matter content
   given the retained W2 primitive. The identity FAILS for any non-SM
   value of N_color, making it a structural fingerprint of the framework's
   SM closure.

4. **Claim boundary**: consistency equalities are not promoted to physical or
   below-Wn closure claims. Audit status remains external to this note.

## What This Claims

- `(C1)`: formal `c² = 1 - A^4 = (N_color² - N_pair²)/N_color² = (N_quark-1)/N_color² = 5/9` after the cited coupling assignment.
- `(C2)`: formal `sqrt(MW2/MZ2) = √(N_quark-1)/N_color = √5/3`.
- `(C3)`: the formal complementary ratio is `N_pair²/(N_quark-1) = 4/5`.
- `(C5)`: SM-specific structural identity N_color² - N_pair² = N_quark - 1
  (derivable from W2 primitive + N_color = 3).

## What This Does NOT Claim

- Does NOT promote any support-tier theorem to retained.
- Does NOT use consistency equalities as load-bearing closure routes.
- Does NOT identify a physical weak angle, W/Z mass, or W/Z mass ratio at any
  scale.
- Does NOT modify retained sister bridge A^4 = 4/9.
- Does NOT cite any unmerged branches as retained authorities.

## Reproduction

```bash
python3 scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py
```

Expected result:

```text
TOTAL: PASS=N, FAIL=0
COS_SQ_THETA_W_LATTICE_COMPLEMENT_BRIDGE_VERIFIED = TRUE
M_W_M_Z_LATTICE_RATIO_DERIVED = TRUE
SM_STRUCTURAL_IDENTITY_N_COLOR_3_DERIVED = TRUE
```

The legacy runner performs exact arithmetic and source-shape checks. Its
results certify the formal identities only; prose/status tokens are not
scientific evidence. It:

1. Reads the cited source files to confirm the named algebraic inputs.
2. Extracts retained YT_EW closed forms `g_2² = 1/(d+1)`, `g_Y² = 1/(d+2)`
   from `YT_EW_COLOR_PROJECTION_THEOREM.md`.
3. Extracts retained Q_L representation literal `(2,3)` from
   `LEFT_HANDED_CHARGE_MATCHING_NOTE.md` (S1 source).
4. Derives the formal `c²` via T1 and verifies
   it equals 5/9 by exact Fraction arithmetic.
5. Cross-checks via T2 (1 - A^4), T3 (S1 structural integers), and T8
   (SM-specific identity).
6. Derives `sqrt(MW2/MZ2) = √5/3` via T5.
7. Derives `s²/c² = 4/5` via T6.
8. Verifies T8: `N_color² - N_pair² = N_quark - 1` at retained values,
   AND solves the algebraic constraint to confirm `N_color = 3` is the
   unique positive solution given W2 primitive.

## Cross-References

**Retained-tier authorities used in T1-T6 (load-bearing for the bridge):**

- `YT_EW_COLOR_PROJECTION_THEOREM.md` — historical context only; it is not
  cited as authority for the supplied coupling assignment used here.
- [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
  — defined `C^2` algebra only: `c² = g²/(g² + g_Y²)` and
  `MW2/MZ2 = c²`; no physical weak-angle or mass identification.
- [`WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md`](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md)
  — retained `(W2)` `A² = N_pair/N_color = 2/3`.
- [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md)
  — retained corollary; `Q_L : (2,3)_{+1/3}` source for S1 (P4).
- [`ONE_GENERATION_MATTER_CLOSURE_NOTE.md`](ONE_GENERATION_MATTER_CLOSURE_NOTE.md)
  — retained; `u_R, d_R : (1,3)` cross-check on N_color via S1.
- [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md)
  — retained `N_pair = N_color - 1` primitive (W2 source for T8).
- [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md) — retained
  framework primitives (Z³ axiom 2; SU(2), SU(3) current consequences).
- [`CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md`](CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md)
  — sister bridge; `s²|_assigned couplings = A^4 = 4/9` (T2 complement source).
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
