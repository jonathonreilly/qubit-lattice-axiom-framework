---
claim_id: admissibility_dirac_kahler_heavy_metric_operator_completion_bounded_theorem_note_2026-08-26
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_HEAVY_METRIC_OPERATOR_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-26.md
claim_type: bounded_theorem
claim_scope: "At T = 16, unit volume, one core, the interior window D = {2,3,4}, and exactly the two rational fixtures (m,c) = (9/20,5/13) and (1/2,1/3), the heavy U = -1 compression T_h has an exact rational positive symmetrizer cone: the symmetric intertwiner system has dimension 6, contains explicit positive-definite members, and every positive-definite member makes Theta T_h symmetric positive definite because T_h obeys z^2 - tau z + 1 with tau > 2. The one-site-shift condition leaves a two-dimensional displayed family and the declared Block-197 completion acts as identity on this heavy sector. These two tested conditions do not select a ray; other selectors are unclassified. No OS, gravity, continuum, generic-parameter, energy, or dynamics claim is made."
runner: scripts/admissibility_dirac_kahler_heavy_metric_operator_completion_2026_08_26.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite heavy-sector positive symmetrizer on the declared interior window"
source_of_blocker_text: review_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Classify additional physically motivated selector conditions, if any, without treating the two conditions tested here as exhaustive."
conditional_surface_status: "stacked on unmerged ancestor artifacts; scientific content is proposed for retention and remains audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact rational finite-dimensional theorem at two declared fixtures; no sampled continuum or generic-parameter extrapolation"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block198-spatial-embedding-momentum-boundary-20260826
parent_commit: e784ffc1ef94489383b0869f058962ccd2af7f74
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# Exact positive symmetrizers for the finite heavy compression

**Date:** 2026-08-26

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author proposal only; an independent audit is
required before any effective retained status.

**Standing:** conditional support on an unmerged PR stack. Nothing is registered,
adopted, or added to the axioms.

## Result

At `T = 16`, unit volume, the interior window `D = {2, 3, 4}`, and each of the
two declared rational fixtures, the descended two-step operator's heavy
`U = -1` compression `T_h` has a nonempty cone of exact rational positive
symmetrizers. More precisely:

1. the OS Gram `K_h` does not symmetrize `T_h`; its exact defect
   `K_h T_h - T_h^T K_h` has rank `2` and `8` nonzero entries;
2. the linear system

   ```text
   Theta = Theta^T,       Theta T_h = T_h^T Theta
   ```

   has ten symmetric unknowns, coefficient rank `4`, and hence solution-space
   dimension `6`;
3. the solution space contains explicit positive-definite rational matrices;
4. every positive-definite member of that six-dimensional solution space makes
   `Theta T_h` symmetric and positive definite;
5. imposing the declared one-site-shift compatibility leaves a displayed
   two-dimensional family, and the declared Block-197 completion restricts to
   `I_4` on this heavy sector.

Item 5 says only that these two named conditions do not select a unique ray in
the displayed family. It does **not** classify all commuting symmetries or all
possible physical selection principles.

## Dependency and landing status

The construction is defined by the following stacked inputs:

- [spatial embedding and momentum boundary](ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_EMBEDDING_MOMENTUM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md),
  the immediate branch parent;
- [sectored interior OS reconstruction](ADMISSIBILITY_DIRAC_KAHLER_SECTORED_INTERIOR_OS_RECONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md),
  which defines the interior quotient and the heavy defect;
- [hidden involutive isometry](ADMISSIBILITY_DIRAC_KAHLER_HIDDEN_INVOLUTIVE_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md),
  which supplies the sector projectors and completion form;
- [width-family transfer monodromy](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md),
  [transfer-package parameter probe](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md),
  and [boundary-mode volume sensitivity](ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md),
  which fix the finite carrier conventions and comparison polynomials; and
- [the shifted-origin Hodge construction](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
  whose `shear_hodge(c, v)` is imported through the Block-128 runner.

Those artifacts exist in the declared stacked base, but the stack is not yet on
`main`. Therefore this note is not independently landable ahead of its
ancestors. This is a dependency fact, not a defect in the theorem below.

## Finite construction

The runner rebuilds, over exact rationals, the staggered Dirac–Kähler carrier on
`Z_16 × Z_4`, the reflection completion `Q`, its inverse, the interior reflected
pairings, the quotient section, and the `U = -1` heavy compression. It performs
exactly two `64 × 64` inversions, one at each fixture, and reuses their results.

At both fixtures the following identities are gated:

- `d_K^2 = 0` entrywise;
- `Ps H Ps - H = 0` and `Ps Q Ps - Q^T = 0` entrywise;
- `rank(Q) = 64`, with both inverse residuals zero;
- `rank(K_AD) = 8`, `dim ker(K_AD) = 4`, and the two-step form annihilates
  that kernel;
- the quotient Gram `K_c` is symmetric positive definite by all eight leading
  principal minors;
- the two-site shift is a `K_c`-isometry and commutes with the quotient
  operator; and
- the heavy OS self-adjointness defect has rank `2` and `8` nonzero entries.

The runner applies fixture-specific forced relations only at the fixture where
they were derived. At the second fixture it separately gates the complete
family, parameterization, minimal-polynomial, and positive-definiteness
residuals. This prevents the former false pass in which nonzero residuals were
printed but not used by a gate.

## Positive-cone theorem

Let `Theta` be any positive-definite member of the symmetric intertwiner space,
so

```text
Theta = Theta^T,          Theta T_h = T_h^T Theta.
```

At the primary fixture the runner proves exactly

```text
T_h^2 - tau T_h + I_4 = 0,
tau = 233631106 / 22569375,
tau - 2 = 188492356 / 22569375 > 0.
```

The corresponding integer polynomial is

```text
22569375 z^2 - 233631106 z + 22569375,
```

with discriminant `52545986939220736 > 0`, positive root sum, and root product
`1`. Its two roots are therefore real, distinct, and strictly positive.

Define

```text
N = Theta^(1/2) T_h Theta^(-1/2)
  = Theta^(-1/2) (Theta T_h) Theta^(-1/2).
```

The intertwining equation makes `N` symmetric. Similarity carries the exact
quadratic identity to `N^2 - tau N + I_4 = 0`, so every eigenvalue of `N` is
one of the two positive roots. Hence `N` is positive definite. Finally,

```text
Theta T_h = Theta^(1/2) N Theta^(1/2)
```

is positive definite by congruence. No numerical diagonalization, radical
evaluation, float, or tolerance enters this proof.

One primitive integer witness is

```text
Theta_D = diag(902775, 902775, 1581193, 1581193),
```

whose four leading principal minors are

```text
(902775,
 815002700625,
 1288676565209345625,
 2037646364173060836830625).
```

The runner also gates a second rational positive-definite witness outside the
one-site-shift-compatible plane, so the six-dimensional cone is not inferred
from the diagonal point alone.

## The two measured compatibility conditions

Compressing the one-site shift to the heavy sector gives `S_h^2 = -I_4` and
`[S_h, T_h] = 0`. Adding

```text
S_h^T Theta S_h = Theta
```

raises the coefficient rank from `4` to `8`, leaving an exact two-parameter
family. In the runner's coordinates,

```text
A = (150553/22320) a + (902775/1581193) b,
r = 26093/8928.
```

Its Sylvester minors are verified symbolically as

```text
M1 = A,
M2 = A^2,
M3 = A (A b - (1 + r^2) a^2),
M4 = (A b - (1 + r^2) a^2)^2.
```

The closed rational box

```text
|a| <= 1/100,        1/2 <= b <= 3/2
```

is contained in the open positive-definite region, because the runner proves
strict positive lower bounds for both `A` and
`A b - (1 + r^2) a^2` over the whole box. The box has two-dimensional
interior, so this displayed positive-definite set is not a ray.

For the second declared condition, the sector projector identities

```text
pi_0 B_h = 0,        pi_2 B_h = 0,        P_h B_h = B_h
```

hold exactly. Therefore every operator of the declared form

```text
B_2 X pi_0 + B_0 X' pi_2 + P_h
```

restricts to `I_4` on the heavy sector. This condition does not further cut the
displayed family. No statement is made about compatibility conditions outside
these two declared forms.

## Second-fixture persistence

At `(m, c) = (1/2, 1/3)` the runner independently gates the same construction
pattern with different coefficients:

- the symmetric intertwiner space again has dimension `6`;
- the one-site-shift condition again leaves dimension `2`;
- `T_h^2 - tau_2 T_h + I_4 = 0` with
  `tau_2 = 7258/739` and `tau_2 - 2 = 5780/739 > 0`;
- the displayed family has
  `A_2 = (85/14) a + (739/1165) b` and `r_2 = 71/28`; and
- `diag(739, 739, 1165, 1165)` is a gated positive-definite witness.

This is two-fixture persistence only. It is not a theorem for generic `(m, c)`.

## Scope and nonclaims

- `Theta` is a different exact rational inner product; it is not the OS Gram.
- The finite heavy operator is not an OS reconstruction, semigroup, generator,
  Hamiltonian, energy, or mass.
- One width, one interior window, one core, one unit volume, and two rational
  fixtures do not establish a continuum or all-parameter theorem.
- No lapse, shift, ADM phase space, Hamiltonian constraint, momentum constraint,
  first-class constraint algebra, Dirac closure, observable, gauge orbit, or
  quotient is supplied.
- The two tested compatibility conditions do not choose a ray. Other physical
  selectors are unbuilt and unclassified, not refuted.
- No axiom is amended, and there is no obligation or TOE-percentage movement.

## Repair and review record

The repair preserves the exact cone theorem, both rational fixtures, and all
valid rank and positivity lemmas. It makes four honesty corrections:

1. fixture-specific forced relations are no longer applied at the second
   fixture;
2. the second fixture's family, parameterization, and positive-definiteness
   residuals are now load-bearing gates with adversarial mutations;
3. the claim that the two measured cuts exhaust symmetry-based selection is
   withdrawn; and
4. the rational-box statement is called a closed box contained in an open cone,
   rather than an open box defined by weak inequalities.

The source status remains `proposed_retained`; a disjoint exact checker must
confirm the repaired runner before the PR branch is updated.

## Reproduction

```bash
python3 scripts/admissibility_dirac_kahler_heavy_metric_operator_completion_2026_08_26.py
python3 scripts/admissibility_dirac_kahler_heavy_metric_operator_completion_2026_08_26.py --list-mutations
```

The baseline must report `PASS=35 FAIL=0`. Every declared mutation must exit
nonzero and flip only its intended gate family.

## N5 scope certificate

```text
N5: per_element: Exact rational matrix entries, polynomial identities, and Sylvester minors are checked at the two declared fixtures only.
per_site: The carrier is checked on Z_16 x Z_4 at one core and the interior window D = {2, 3, 4}; no other site domain is claimed.
per_mode: The measured object is the U = -1 heavy compression; the light sector and other momentum sectors are outside this theorem.
per_block: The positive cone theorem and both compatibility ranks are exact for the declared finite constructions and their gated parameterizations.
lattice_wide: checked and not executed -- no lattice-wide, continuum, all-parameter, or exhaustive-selector statement is made by this runner.
```
