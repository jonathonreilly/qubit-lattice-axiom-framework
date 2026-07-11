# G Bare Finite-Link/Wilson Split-Redundancy and Pin-Equivalence Theorem

**Date:** 2026-06-18; algebra/convention split completed 2026-07-11.
**Claim type:** bounded_theorem
**Audit status:** set only by the independent audit lane. This source note
does not set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py`](../scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py)

## Purpose

The parent note `G_BARE_DERIVATION_NOTE.md` needs a non-circular account of
the finite-link/Wilson scalar slots. This sentence names the target parent but
is not a citation-graph dependency of this theorem note. The theorem surface
contains only the following algebraic ingredients:

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

- Theorems 1–3 below prove the plaquette exponent construction, the exact
  split redundancy, and the pin equivalence
  `gamma*(beta) = s` if and only if `beta = 2 N_c`.

## Non-load-bearing convention context

The same-slot definition and its displayed `N_c = 3` bookkeeping are recorded
separately in the meta convention note
`G_BARE_SAME_SLOT_BETA6_CONVENTION_NOTE_2026-07-11.md`.
That note is non-load-bearing context for this theorem. Nothing here chooses
the same-slot convention or treats its displayed values as theorem outputs.

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

**Audited claim-surface statement.**

> This note's audited claim surface is exactly Theorems 1–3 and the
> mismatched-slot exhibit: independently auditable construction-level facts.
> Same-slot naming and normalization conventions are outside this theorem and
> live only in the linked meta convention note.

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
link/plaquette/action data. Whether the Wilson `g_bare` occupies the same
scalar slot as the finite-link canonical scalar `s` is not a
construction-level fact; it can be fixed only by a separate normalization or
identification convention. (Contrast with Setup item 1: the dilation
`C -> s C` changes the data; the split `(gamma, C/gamma)` does not. The
rigidity theorem removes the first freedom. The second remains outside this
theorem.)

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

The equality condition `gamma*(beta) = s` is exactly equivalent to
`beta = 2 N_c`. This theorem locates the pin but does not choose it.

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
`gamma*(beta)^2 = 2 N_c / beta`. Because the constructed link-canonical
slot is `s = 1`, the equality condition `gamma*(beta) = s` holds exactly
when `beta = 2 N_c`. No same-slot convention is chosen in this argument.

## Mismatched-slot exhibit

What a mismatched-slot reading gives, on identical constructed data: at
`beta = 24` the same canonical links, the same plaquette matrices, and
the same per-plaquette action values yield the constructed matched scalar

```text
gamma*(24)^2 = 6/24 = 1/4,    gamma*(24) = 1/2 != 1 = s,
```

with the Wilson identity holding as `24 * (1/4) = 6 = 2 N_c`, and the
same-slot statement false. Nothing in the constructed surface data
changed between the same-slot pin `beta = 2 N_c` and `beta = 24`. This
exhibits that the same-slot identification does real selecting work — it is the choice of
the `beta = 2 N_c` point on the one-parameter family
`beta = 2 N_c / gamma*^2` — and is therefore a declaration, not a
construction-level consequence.

## Boundary

This note does not claim:

- that the Wilson field coordinate and finite-link canonical coordinate
  occupy the same scalar slot; that convention is outside this theorem;
- Wilson plaquette action-surface selection from framework axioms;
- exclusion of improved or non-Wilson gauge actions;
- a continuum running-coupling value;
- global logarithm-branch selection;
- a phenomenological fitted coupling;
- a dynamical fixed point;
- an audit verdict or any effective-status promotion.

A framework-native derivation of the same-slot identification from the
operator/Hamiltonian side (for example a transfer-matrix or heat-kernel route)
remains outside this row.

**2026-07-11 downstream hygiene.** This note's citable surface is Theorems
1–3 and the mismatched-slot exhibit. Downstream notes must not cite this
note as choosing the same-slot identification or as deriving the convention
recorded in
`G_BARE_SAME_SLOT_BETA6_CONVENTION_NOTE_2026-07-11.md`.
That meta note is non-load-bearing convention context. A retained derivation
of the same-slot identification from the operator/Hamiltonian surface remains
the named open target. This dated line itself moves the note hash so the row
re-enters for re-audit.

The bounded theorem surface internal to the finite-link canonical Wilson
surface is exactly Theorems 1–3 plus the mismatched-slot exhibit.

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

The runner checks these as source-boundary and construction checks rather
than audit verdicts.

## Verification

Run:

```text
python3 scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py
```

Expected after the 2026-07-11 algebra/convention split:

```text
TOTAL: PASS=105 FAIL=0
```

## Repair Note

**Date:** 2026-07-11

**Notes for re-audit (verbatim):**

> "missing_bridge_theorem: supply retained authority deriving the same-slot
> identification from the operator/Hamiltonian surface, or separate the
> beta=6 definition-level contribution from the independently auditable
> Theorems 1–3."

This repair takes the **SEPARATION arm** literally. The bounded theorem now
contains only Theorems 1–3 and the mismatched-slot exhibit. The same-slot
definition and its displayed normalization values live in the separate
`Type: meta` convention note linked above. The paired runner checks the
algebraic theorem and verifies that the convention content is absent here and
present only on the meta surface. No audit output or status is authored.
