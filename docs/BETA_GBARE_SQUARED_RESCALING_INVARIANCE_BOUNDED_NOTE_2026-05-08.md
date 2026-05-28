# β·g_bare² = 2 N_c Conditional Wilson-Matching Arithmetic Lemma

**Date:** 2026-05-08. Repair narrowing: 2026-05-27.
**Claim type:** bounded_theorem
**Proposal allowed:** false
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_beta_gbare_squared_rescaling_invariance.py`](../scripts/frontier_beta_gbare_squared_rescaling_invariance.py)
**Runner cache:** [`logs/runner-cache/frontier_beta_gbare_squared_rescaling_invariance.txt`](../logs/runner-cache/frontier_beta_gbare_squared_rescaling_invariance.txt)

## 2026-05-28 Science-Fix Re-Audit Scope

The re-audit target is only the algebraic invariant
`beta * g_bare^2 = 2 N_c` under the stated Wilson-action normalization
premise WM. WM is not cited as an effective framework theorem by this row.
The row should not be used as Wilson matching authority unless a separate WM
authority is audited.

## Claim

This row is an explicitly conditional arithmetic lemma. It assumes the
Wilson action-surface matching premise

```text
WM:  β = 2 N_c / g_bare²
```

for positive `g_bare²` and fixed color rank `N_c`. The Wilson matching
premise is not proved here, is not a retained conclusion of this row, and
is not imported from any Ward-route coupling-closure note.

Under `WM`, the product identity

```text
β · g_bare² = 2 N_c
```

is ordinary algebra. Under the scoped generator-basis rescaling map
`T_a -> c · T_a` (equivalently `A -> c · A`) discussed by
[`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md),
the matched coefficient transforms as `β -> c² · β` when `WM` is held as
the action-surface premise. Pairing that map with
`g_bare² -> g_bare² / c²` gives

```text
β'(c) · g_bare'²(c)
  = (c² β) · (g_bare² / c²)
  = β · g_bare²
  = 2 N_c.
```

The pure algebraic core is the already audited standalone identity in
[`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md),
specialized only by naming the abstract variables as `(g, N) =
(g_bare, N_c)`. The physical Wilson-surface interpretation remains
conditional on `WM`.

This note does not introduce a new axiom, does not prove Wilson matching,
does not modify the retained theorem family, and does not promote any
status row.

## Inputs and Authorities

| Item | Role |
|---|---|
| Explicit premise `WM: β = 2 N_c / g_bare²` | scoped Wilson action-surface assumption; not derived or imported as a retained theorem here |
| [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md) | retained pure polynomial-algebra identity for `β(g,N)=2N/g²`, `β(g/c,N)=c²β(g,N)`, and invariance of `β·g²` |
| [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) | scoped generator-basis rescaling map; it also treats Wilson matching as an input rather than deriving it |

The dependency structure is therefore: retained abstract algebra plus a
scoped rescaling map, with `WM` declared as an explicit premise. No
Ward-route coupling-closure result is used as authority for `WM`.

## Arithmetic Identity Table

Let `q = g_bare² > 0` and assume `WM`, so `β = 2 N_c / q`. For any
positive rational rescaling `c`,

```text
β'(c) = c² · β,
g_bare'²(c) = q / c²,
β'(c) · g_bare'²(c) = 2 N_c.
```

For the representative specialization `N_c = 3` and `q = 1`, the exact
rational table is:

| `c` | `β'(c) = c² · β` | `g_bare'²(c) = q / c²` | product `β'(c) · g_bare'²(c)` |
|---|---|---|---|
| `1/2` | `3/2` | `4` | `6 = 2 N_c` |
| `1` | `6` | `1` | `6 = 2 N_c` |
| `2` | `24` | `1/4` | `6 = 2 N_c` |
| `3` | `54` | `1/9` | `6 = 2 N_c` |

The representative `q = 1` row is only a test point for the conditional
arithmetic. It is not a derivation of a physical canonical value for
`g_bare`.

## Boundaries

This is a **conditional bounded arithmetic lemma only**. In particular,
this note does not establish, and does not claim to establish:

- Wilson matching `β = 2 N_c / g_bare²` from the framework axioms;
- a Wilson plaquette action selector, Symanzik/improved-action exclusion,
  or continuum-limit theorem;
- any retention or promotion of `g_bare = 1` or any other physical
  coupling lane;
- that a Ward-route coupling-closure theorem carries the Wilson matching
  premise;
- a modification of the imported abstract polynomial identity;
- a modification of the scoped generator-basis rescaling theorem;
- a new claim about canonical Cl(3) connection normalization
  `Tr(T_a T_b) = δ_ab / 2`;
- any parent theorem/status promotion.

The single load-bearing step is class (A) algebraic substitution under
the explicit `WM` premise, verified at exact rational precision for the
enumerated `c` values and additional positive rational `g_bare²` values.
The runner performs these checks with Python `fractions.Fraction`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_beta_gbare_squared_rescaling_invariance.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: conditional bounded arithmetic lemma passes; assuming WM,
β · g_bare² = 2 N_c is invariant under the scoped joint rescaling for
c ∈ {1/2, 1, 2, 3} at exact rational precision.
```
