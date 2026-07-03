# G Bare Parent Finite-Link/Wilson Beta=6 Bridge

**Date:** 2026-06-18 (same-slot surface-definition repair 2026-07-01: the
same-scalar-slot identification is restated as an explicit declared surface
definition `(SD)` on the theorem surface rather than an asserted
cross-surface theorem, and the paired runner now constructs both scalar
slots from the supplied link/plaquette data and compares them instead of
assigning `g_wilson_sq = g_link_sq` — see
`## 2026-07-01 same-slot surface-definition repair`.)
**Claim type:** bounded_theorem
**Audit status:** set only by the independent audit lane. This source note
does not set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py`](../scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py)

## Purpose

The parent note `G_BARE_DERIVATION_NOTE.md` needs a non-circular supply of
the `beta = 6` surface. This sentence names the target parent but is not a
citation-graph dependency of this bridge note. The older route mixed two
steps:

```text
beta = 2 N_c = 6
g_bare^2 = 2 N_c / beta = 1
```

This bridge separates the supply into three ingredients and labels each
honestly:

- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md)
  (theorem, cited at its audited scope) supplies the finite-link canonical
  scalar slot: once the fixed canonical `SU(3)` generator basis is chosen,
  there is no independent scalar multiplier in the link exponent. In
  canonical finite-link coordinates this is the `s = 1` slot
  (`g_link^2 = 1`).
- [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md)
  (theorem, cited at its audited scope) supplies the Wilson coefficient
  identity inside the supplied standard Wilson plaquette action:

```text
beta g_bare^2 = 2 N_c.
```

- The identification of the Wilson `g_bare` with the finite-link canonical
  scalar `s` — the statement that both occupy the same scalar slot on the
  parent surface — is **not** supplied by either cited authority and is
  **not** a construction-level fact of the link/plaquette data (Theorem 2
  below). It is supplied by this note as the explicit declared surface
  definition `(SD)`.

The pre-repair version of this note asserted the identification as if the
two cited authorities proved it. The 2026-06-21 audit graded that
assertion a renaming; this repair answers the second-auditor question
directly: the same-scalar-slot move is intentionally stipulated as a
surface definition, and the note now declares it as such and proves
exactly the bounded theorems that locate what the declaration does.

## Declared surface definition

```text
(SD)  The parent surface instantiates the supplied standard Wilson
      plaquette surface with its gauge field taken to be the finite-link
      canonical coordinate:

          A^a := C^a    (equivalently  g_bare := s).
```

`(SD)` is a definition of the parent surface, not a theorem. It is not
derived from the cited authorities. Theorem 3 below shows it is exactly
equivalent to the normalization point `beta = 2 N_c` on the Wilson
surface: choosing `(SD)` and choosing `beta = 2 N_c` are the same choice,
made once, and this note makes it in the open.

Notation: this note writes the canonical finite-link coefficients as `C^a`
(the rigidity note writes them `A^a`) so that the Wilson-surface matched
field variable can be written `A^a` without collision.

## Claim

Setup (supplied surfaces, cited at audited scope):

1. Finite-link canonical surface (rigidity note): links are expressed in
   canonical generator coordinates `U = exp(i C^a T_a a)` with
   `Tr(T_a T_b) = delta_ab / 2`; scalar dilation of the fixed `T_a` basis
   is not an allowed ambiguity of the canonical normalization, so the
   canonical coordinate surface is `s = 1`. A genuine scalar dilation
   `U = exp(i s C^a T_a a)` with `s != 1` changes the link; it is not a
   redundancy of the data.

2. Standard Wilson plaquette surface (Wilson small-a note): action
   `S_W = beta sum (1 - (1/N_c) Re Tr U_P)` with canonical trace
   normalization, and the small-a matching demand that the matched gauge
   field carry the continuum kinetic normalization
   `(1/4) F^a_{mu nu} F^a_{mu nu}`. Inside that surface,
   `beta g_bare^2 = 2 N_c`.

**Theorem 1 (plaquette exponent construction).** For plaquettes built from
links in canonical coordinates, the small-`a` exponent is

```text
U_P = exp(i a^2 F^a[C] T_a + O(a^3)),
F[C; 1] = Delta_mu C_nu - Delta_nu C_mu + i [C_mu, C_nu],
```

with unit scalar coefficient in the canonical `T_a` basis: the difference
term and the commutator term enter with equal weight, and the exponent
lies in the canonical generator span.

**Theorem 2 (exact split redundancy).** For every `gamma != 0`, the
standard-convention split `(g_bare, A) = (gamma, C / gamma)` reproduces
every link matrix, every plaquette matrix, and every Wilson action value
identically, and, with `F[A; g] = Delta_mu A_nu - Delta_nu A_mu
+ i g [A_mu, A_nu]` the standard-convention field strength,

```text
gamma * F[C/gamma; gamma] = F[C; 1]        (exactly, at finite a).
```

The split scalar is therefore not a function of the constructed
link/plaquette/action data. Whether the Wilson `g_bare` occupies the
same scalar slot as the finite-link canonical scalar `s` is not a
construction-level fact; within this packet's supplied surfaces it is
fixed only by a normalization demand on the field variable itself, such
as `(SD)`. (Contrast with Setup item 1: the dilation `C -> s C` changes
the data; the split `(gamma, C/gamma)` does not. The rigidity theorem
removes the first freedom. The second is what `(SD)` fixes.)

**Theorem 3 (matched-slot family and pin equivalence).** The Wilson
matching demand applied at action parameter `beta` to the constructed
plaquette action determines the matched scalar

```text
gamma*(beta)^2 = 2 N_c / beta,
```

which is `beta`-dependent, while the link-canonical slot `s = 1` is
`beta`-independent. Hence

```text
gamma*(beta) = s      if and only if      beta = 2 N_c.
```

The same-slot statement is exactly equivalent to the normalization point
`beta = 2 N_c`.

**Composition (under `(SD)`).** Under the declared surface definition,
`g_bare = s = 1` on the canonical coordinate branch, and the Wilson
coefficient identity gives, in exact rational arithmetic,

```text
g_bare^2 = 1
beta = 2 N_c.
```

For `N_c = 3`, this gives

```text
beta = 6.
```

Every downstream consumption of `beta = 6` from this row is a consumption
of the pair {the two cited theorems, the declared `(SD)`}; the declaration
is part of the supplied surface, not a derived output of this note.

## Proof

**Theorem 1.** Baker-Campbell-Hausdorff expansion of the four-link
plaquette product `U_mu(x) U_nu(x+a mu) U_mu(x+a nu)^dagger
U_nu(x)^dagger` with `U = exp(i a C)`: the `O(a)` terms cancel around the
loop, the `O(a^2)` terms assemble the forward-difference curl plus the
group commutator, giving `i a^2 (Delta_mu C_nu - Delta_nu C_mu
+ i [C_mu, C_nu]) + O(a^3)`. The runner verifies this constructively:
exact matrix exponentials, exact plaquette products, principal logarithm,
Richardson extrapolation in `a`, remainder-order scaling, and projection
onto the canonical `T_a` basis.

**Theorem 2.** Link-by-link, `exp(i a gamma (C/gamma)) = exp(i a C)`; the
matrices are equal, so all plaquettes and all action values (which are
functions of the link matrices and `beta` only) coincide. For the field
strength, one line of algebra:

```text
gamma * F[C/gamma; gamma]
  = gamma (Delta (C/gamma) - Delta (C/gamma)) + i gamma^2 [C/gamma, C/gamma]
  = Delta C - Delta C + i [C, C]
  = F[C; 1].
```

Since every constructed object is invariant under the split
reparametrization, no functional of the constructed data separates
`(gamma, C/gamma)` from `(1, C)`.

**Theorem 3.** By Theorem 1 and the canonical trace normalization, the
constructed per-plaquette action is

```text
beta (1 - (1/N_c) Re Tr U_P)
  = (beta a^4 / (4 N_c)) F^a[C] F^a[C] + higher order.
```

For a candidate split `A = C/gamma` the same value reads
`(beta gamma^2 a^4 / (4 N_c)) F^a[A] F^a[A] + higher order` (using
Theorem 2's identity componentwise, `F^a[C] = gamma F^a[A]`). The Wilson
note's matching demand fixes the coefficient per unordered plaquette
plane at `1/2`, i.e. `beta gamma*^2 / (4 N_c) = 1/2`, hence
`gamma*(beta)^2 = 2 N_c / beta`. Setting `gamma*(beta) = s = 1` gives
`beta = 2 N_c`; conversely `beta = 2 N_c` gives `gamma* = 1`.

**Composition.** Substitute the declared `(SD)` value `g_bare := s = 1`
into the Wilson coefficient identity:

```text
beta g_bare^2 = 2 N_c
g_bare^2 = 1
beta = 2 N_c.
```

At `N_c = 3`, exact rational arithmetic gives `beta = 6`.

## Mismatched-slot exhibit

What a mismatched-slot reading gives, on identical constructed data: at
`beta = 24` the same canonical links, the same plaquette matrices, and
the same per-plaquette action values yield the constructed matched scalar

```text
gamma*(24)^2 = 6/24 = 1/4,    gamma*(24) = 1/2 != 1 = s,
```

with the Wilson identity holding as `24 * (1/4) = 6 = 2 N_c`, and the
same-slot statement false. Nothing in the constructed surface data
changed between `beta = 6` and `beta = 24`. This exhibits that the
same-slot identification does real selecting work — it is the choice of
the `beta = 2 N_c` point on the one-parameter family
`beta = 2 N_c / gamma*^2` — and is therefore a declaration, not a
construction-level consequence.

## Boundary

This note does not claim:

- that `(SD)` is derived — it is the declared instantiation definition of
  the parent surface, not derived from the cited authorities, and
  Theorems 2–3 locate precisely why a declaration (or an equivalent
  normalization demand on the field variable) is required at this step;
- Wilson plaquette action-surface selection from framework axioms;
- exclusion of improved or non-Wilson gauge actions;
- a continuum running-coupling value;
- global logarithm-branch selection;
- a phenomenological fitted coupling;
- a dynamical fixed point;
- an audit verdict or any effective-status promotion.

A framework-native derivation of the Wilson-surface normalization from
the operator/Hamiltonian side (for example a transfer-matrix or
heat-kernel route) would upgrade `(SD)` from declared definition to
theorem; that is the next derivation surface this separation opens, and
it is outside this row.

The result is a bounded composition theorem internal to the finite-link
canonical Wilson surface, conditional on the declared `(SD)`.

## Falsifiers

The packet would fail if any of the following were true:

- the plaquette exponent built from canonical links were not
  `a^2 F[C; 1] + O(a^3)` in the canonical `T_a` basis (Theorem 1);
- some `gamma != 1` split changed a link matrix, a plaquette matrix, or a
  Wilson action value, or `gamma * F[C/gamma; gamma] != F[C; 1]`
  (Theorem 2 — this would mean the slot is constructible after all and a
  declaration is the wrong shape for this step);
- the constructed matched scalar deviated from
  `gamma*(beta)^2 = 2 N_c / beta` (Theorem 3);
- the constructed link-canonical readback gave `s != 1`;
- the two constructed slots agreed at some tested `beta != 2 N_c` or
  disagreed at `beta = 2 N_c` (pin equivalence);
- exact rational arithmetic failed to give `beta = 6` at `N_c = 3` under
  `(SD)`.

The runner checks these as source-boundary and construction checks rather
than audit verdicts.

## Verification

Run:

```text
python3 scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=100 FAIL=0
```

## 2026-07-01 same-slot surface-definition repair

This block is a source-only repair. No new axioms, no new imports, no
audit verdict edits. Status authority remains with the independent audit
lane.

### Audit issue addressed

The 2026-06-21 audit graded this row `audited_renaming`: the load-bearing
move asserted that the Wilson plaquette `g_bare` is the same scalar slot
as the finite-link canonical scalar `s`, while neither cited authority
derives that scalar-slot identity across the finite-link and Wilson
plaquette surfaces, and the paired runner assigned
`g_wilson_sq = g_link_sq` rather than deriving it. The second auditor
asked whether the same-scalar-slot move is intentionally stipulated as a
surface definition.

### Answer

It is a stipulation, and the note now says so. The decision is not a
concession by default: the repair first checked whether the identity is
derivable from the supplied constructions, and Theorems 2–3 record the
outcome of that check as theorems. The constructed link/plaquette/action
data is exactly invariant under the standard-convention split
`(gamma, C/gamma)`, so no construct-and-compare path inside this packet's
supplied surfaces determines the split scalar; and the Wilson-matched
scalar is `beta`-dependent (`gamma*(beta)^2 = 2 N_c / beta`) while the
link-canonical slot is `beta`-independent, so the same-slot statement is
exactly equivalent to `beta = 2 N_c` — the very normalization the bridge
supplies. An identification with that shape is a definition, and the
honest form of this row is to declare it.

The repair:

1. declares the identification explicitly as the surface definition
   `(SD)` on the theorem surface (mirroring the explicit-premise pattern
   of the rigidity note's `(HF)` repair);
2. adds Theorems 1–3 as the derivable content in the neighborhood: the
   plaquette exponent construction, the exact split redundancy, and the
   matched-slot family with the pin equivalence
   `gamma*(beta) = s iff beta = 2 N_c`;
3. rewrites the paired runner to construct both scalar slots from the
   link/plaquette data and compare them — the link slot via the
   principal-logarithm readback of constructed links, the Wilson slot via
   the matching demand applied to constructed plaquette actions — with
   the mismatched-slot exhibit at `beta = 24` as the refutation-shaped
   negative; the assignment `g_wilson_sq = g_link_sq` is gone;
4. narrows every downstream-facing sentence to the `(SD)`-conditional
   scope.

### What did not change

- The two citations and their audited scopes are used as before, at
  scope.
- The parent note `G_BARE_DERIVATION_NOTE.md` is not edited by this
  repair; its sentence that the scalar-slot compatibility is "recorded
  and checked" by this row matches the declared-definition reading.
- The claim type remains `bounded_theorem`; the theorem content is
  Theorems 1–3 plus the `(SD)`-conditional composition.
- Status authority: the independent audit lane retains sole authority
  over the effective status of this row. This repair does not promote,
  retain, or change any audit status.
