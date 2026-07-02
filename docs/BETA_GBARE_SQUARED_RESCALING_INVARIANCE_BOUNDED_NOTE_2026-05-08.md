# β·g_bare² = 2 N_c Abstract Joint-Rescaling Algebra Lemma

**Date:** 2026-05-08. Repair narrowing: 2026-05-27; abstract-algebra
narrowing: 2026-06-20.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_beta_gbare_squared_rescaling_invariance.py`](../scripts/frontier_beta_gbare_squared_rescaling_invariance.py)
**Runner cache:** [`logs/runner-cache/frontier_beta_gbare_squared_rescaling_invariance.txt`](../logs/runner-cache/frontier_beta_gbare_squared_rescaling_invariance.txt)

**Type:** conditional / support
**Status authority:** independent audit lane only.

## 2026-05-28 Prior Repair Context (superseded by 2026-06-20 narrowing)

Historical context only: the 2026-05-28 repair treated `WM` as an admitted
Wilson action-surface matching premise and kept the physical Wilson-surface
reading conditional. That prior framing is superseded for this row's current
load-bearing claim by the 2026-06-20 narrowing below.

The current row no longer uses an admitted physical `WM` premise as a
load-bearing input. Its current content is the abstract polynomial identity
with symbolic naming `(g, N) = (g_bare, N_c)`.

## 2026-06-07 Science-Fix Source Packet for `WM`

Reader context only: a separate source packet,
`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`,
addresses the exact Wilson small-`a` coefficient matching premise, with runner
`scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py`
and cache
`logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt`.

The new packet proves

```text
standard Wilson plaquette action
  + Tr(T_a T_b)=delta_ab/2
  + small-a plaquette expansion
  => beta = 2 N_c / g_bare^2.
```

It does not derive Wilson action-surface selection, `g_bare = 1`, or
`beta = 6` as a physical value. The physical Wilson-surface interpretation
remains conditional on the supplied standard Wilson action form and on any
separate action-selection authority. After the 2026-06-20 narrowing below,
that packet is not load-bearing for this row's current claim.

## 2026-06-20 Narrowing (abstract joint-rescaling algebra)

This revision narrows the row to the abstract joint-rescaling algebra and
refreshes the runner/cache. It does **not** supply any
Wilson-action-surface authority for the generator-basis induction
`T_a -> c · T_a => (g_bare² -> g_bare²/c², β -> c²·β)`.
It supersedes the prior admitted-`WM` framing for this row's current
load-bearing claim.

- **Load-bearing (in scope, narrowed):** Define the rational function
  `β(g, N) := 2 N / g²` on abstract symbolic variables `(g, N)` with
  `g > 0`. As pure polynomial algebra, the product `β(g, N) · g² = 2 N` is
  invariant under the abstract joint rescaling `(g, β) ↦ (g/c, c²·β)` for
  any `c > 0`. Naming the abstract variables `(g, N) = (g_bare, N_c)` is a
  symbolic relabeling only; nothing about the *physical* Wilson action
  surface is asserted. The runner verifies this abstract joint-rescaling
  identity at exact rational precision for the enumerated values.
- **NON-load-bearing (open, not supplied here):** The identification of the
  abstract joint rescaling with a *physical* induction on the Wilson action
  surface — i.e. that a generator-basis rescaling `T_a -> c · T_a` actually
  induces `g_bare² -> g_bare²/c²` and `β -> c²·β` on the Wilson plaquette
  action — requires the named bridge authority and is **not** supplied by
  this row. The physical Wilson-surface reading therefore remains
  conditional on that unsupplied retained authority and is open. Likewise
  the Wilson-matching relation `WM: β = 2 N_c / g_bare²` as a *physical*
  action-surface matching statement is not derived or retained here; it is
  recorded only as the symbolic naming `β(g_bare, N_c) = 2 N_c / g_bare²`.

No new axiom, import, comparator, or retained bridge is introduced. The
abstract joint-rescaling algebra is the load-bearing content; the physical
Wilson-action-surface induction stays open until a retained authority for
it lands.

## Claim

This row is an explicitly conditional arithmetic lemma. Its load-bearing
content is the **abstract joint-rescaling algebra**: on abstract symbolic
variables `(g, N)` with `g > 0`, defining the rational function

```text
β(g, N)  :=  2 N / g²,
```

the product identity

```text
β(g, N) · g²  =  2 N
```

is ordinary polynomial algebra, and the abstract joint rescaling
`(g, β) ↦ (g/c, c²·β)` (equivalently the paired maps `g² ↦ g²/c²`,
`β ↦ c²·β`) leaves the product invariant for any `c > 0`:

```text
β'(c) · g'²(c)
  = (c² β) · (g² / c²)
  = β · g²
  = 2 N.
```

Naming the abstract variables `(g, N) = (g_bare, N_c)` is a symbolic
relabeling only; it does **not** assert any physical Wilson action-surface
fact.

The symbolic relation `WM: β = 2 N_c / g_bare²` is, on this narrowed
surface, only the abstract definition `β(g_bare, N_c) = 2 N_c / g_bare²`.
As a *physical* Wilson action-surface matching statement it is not proved
here, is not a retained conclusion of this row, and is not imported from
any Ward-route coupling-closure note.

The pure algebraic core is the already audited standalone identity in
[`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md),
specialized only by naming the abstract variables as `(g, N) =
(g_bare, N_c)`.

The **open bridge** (not supplied here): that a physical generator-basis
rescaling `T_a -> c · T_a` (equivalently `A -> c · A`) induces
`g_bare² -> g_bare²/c²` and `β -> c²·β` *on the Wilson action surface*. That
induction requires the named retained authority and is left open; the scoped
map note `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`
likewise treats this routing as a separate normalization theorem it does
not supply. The physical Wilson-surface interpretation therefore remains
conditional and open.

This note does not introduce a new axiom, does not prove Wilson matching,
does not derive the physical Wilson action-surface induction, does not
modify the retained theorem family, and does not promote any status row.

## Inputs and Authorities

| Item | Role |
|---|---|
| [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md) | load-bearing pure polynomial-algebra identity for `β(g,N)=2N/g²`, `β(g/c,N)=c²β(g,N)`, and joint-rescaling invariance of `β·g²`; the narrowed claim is exactly this algebra specialized by naming `(g, N) = (g_bare, N_c)` |
| Symbolic naming `β(g_bare, N_c) = 2 N_c / g_bare²` | a symbolic relabeling of the abstract variables only; NOT a physical Wilson action-surface matching statement, not derived or imported as a retained theorem here |
| Physical Wilson action-surface induction `T_a -> c·T_a => (g_bare² -> g_bare²/c², β -> c²·β)` | OPEN bridge; requires the named retained authority, not supplied by this row |
| `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md` | reader context for the scoped generator-basis rescaling map; it also treats the Wilson routing as a separate input rather than deriving it; not load-bearing on the narrowed abstract-algebra claim |

The dependency structure is therefore: the load-bearing content is the
retained abstract joint-rescaling algebra, named `(g, N) = (g_bare, N_c)`.
The physical Wilson action-surface induction is the open bridge and is not
supplied. No Ward-route coupling-closure result is used as authority for the
Wilson reading.

## Arithmetic Identity Table

Let `q = g_bare² > 0` and use the abstract definition
`β = β(g_bare, N_c) = 2 N_c / q`. For any positive rational rescaling `c`,
the abstract joint rescaling gives

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

The representative `q = 1` row is only a test point for the abstract
joint-rescaling algebra. It is not a derivation of a physical canonical
value for `g_bare`.

## Boundaries

This is a **conditional bounded arithmetic lemma only**, narrowed to the
abstract joint-rescaling algebra. In particular, this note does not
establish, and does not claim to establish:

- the physical Wilson action-surface induction
  `T_a -> c·T_a => (g_bare² -> g_bare²/c², β -> c²·β)` (the OPEN bridge;
  it requires the named retained authority, not supplied here);
- Wilson matching `β = 2 N_c / g_bare²` as a physical action-surface
  statement, or from the framework axioms;
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

The single load-bearing step is class (A) polynomial algebra on the
abstract symbolic variables `(g, N) = (g_bare, N_c)`: the joint rescaling
`(g, β) ↦ (g/c, c²·β)` leaves `β·g² = 2 N` invariant, verified at exact
rational precision for the enumerated `c` values and additional positive
rational `g_bare²` values. The runner performs these checks with Python
`fractions.Fraction`. The physical Wilson-surface identification of this
algebra is the open bridge and is not part of the load-bearing content.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_beta_gbare_squared_rescaling_invariance.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: abstract joint-rescaling algebra lemma passes; with the abstract
naming (g, N) = (g_bare, N_c), β · g_bare² = 2 N_c is invariant under the
abstract joint rescaling for c ∈ {1/2, 1, 2, 3} at exact rational
precision; the physical Wilson-action-surface induction is the open bridge
and is not asserted.
```
