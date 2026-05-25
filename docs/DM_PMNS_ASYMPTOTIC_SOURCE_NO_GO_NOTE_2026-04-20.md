# DM PMNS Asymptotic Pure-Source No-Go (Enumerated Representatives)

**Date:** 2026-04-20  
**Lane:** DM A-BCC basin enumeration / open import `I11`  
**Status:** algebraic no-go for the stated constraints and enumerated algebraic
representatives only. Exact `chi^2 = 0` PMNS basins cannot escape to infinity
along the enumerated pure-source chamber representatives (six row permutations
times two real CP branches `delta_CP in {0, pi}`). The universal claim across
every asymptotic direction in the affine source family is deferred pending a
`T_m / T_delta / T_q` bridge derivation.  
**Primary runner:**
`scripts/frontier_dm_pmns_asymptotic_source_no_go_2026_04_20.py`

---

## 0. Question

The open-import register still flags basin exhaustiveness:

```text
{Basin 1, Basin N, Basin P, Basin X}
```

as empirical rather than structural. The first unresolved loophole is obvious:
could there be additional exact `chi^2 = 0` basins arbitrarily far out in the
active chamber?

This note closes that loophole.

## 1. Bottom line

For the enumerated algebraic representatives, no.

Under the stated constraints, if a sequence of exact PMNS-fit source points
escaped to infinity, then after dividing by its norm the affine Hermitian
family would converge to the pure-source real-symmetric family

```text
J(m, delta, q_+) = m T_m + delta T_delta + q_+ T_q.
```

So any basin at infinity reachable along the enumerated representatives would
have to be realized by a **real orthogonal** PMNS matrix with the target angles.

For each of the six row permutations and each real CP branch `delta_CP = 0, pi`
(the enumerated representatives covered by this packet), write

```text
J = U diag(lambda_1, lambda_2, lambda_3) U^T,
```

with `U` the corresponding real orthogonal PMNS matrix. Membership in the
three-parameter pure-source family imposes exactly the linear constraints

```text
J_22 + J_33 = 0,
J_13 - J_12 - 2 J_22 = 0,
2 J_11 - 2 J_23 + J_12 + J_13 = 0.
```

These become a `3 x 3` homogeneous linear system

```text
A_(perm,delta_CP) lambda = 0.
```

The runner verifies that for all six row permutations and both real CP branches
the matrix `A_(perm,delta_CP)` has full rank. Therefore the only solution is

```text
lambda_1 = lambda_2 = lambda_3 = 0,
```

which is not a physical asymptotic source direction.

So no exact `chi^2 = 0` PMNS fit exists at infinity along the enumerated
representatives.

## 2. Theorem (enumerated representatives)

**Theorem (asymptotic pure-source no-go, enumerated representatives).** Fix the
target angle triple

```text
(s12^2, s13^2, s23^2) = (0.307, 0.0218, 0.545).
```

Restrict to the enumerated algebraic representatives: the six row permutations
of the PMNS matrix paired with the two real CP branches `delta_CP in {0, pi}`.

Assume there exists an unbounded sequence of exact PMNS-fit points on the
affine source family

```text
H = H_base + m T_m + delta T_delta + q_+ T_q
```

whose normalized limit lies in one of the enumerated representatives. Then
after dividing by the Euclidean norm of `(m, delta, q_+)` and taking a
convergent subsequence, one obtains a nonzero pure-source matrix

```text
J = m T_m + delta T_delta + q_+ T_q
```

whose PMNS angles equal the target angles in that representative.

But `J` is real symmetric, so its diagonalizing matrix is real orthogonal. For
each enumerated real-orthogonal PMNS representative with the target angles, the
pure-source family constraints reduce to a full-rank homogeneous linear system
in the three eigenvalues. Hence the only solution is the zero matrix.

Therefore no such nonzero `J` exists in any enumerated representative, and no
exact PMNS-fit basin can escape to infinity along those representatives. QED.

**Out of scope.** The theorem does not yet cover every asymptotic direction in
the actual affine source family `H_base + m T_m + delta T_delta + q_+ T_q`. A
universal extension would require a derivation that bridges the generic
asymptotic direction to one of the enumerated representatives (the
`T_m / T_delta / T_q` bridge derivation, deferred as future work in section 5).

## 3. Consequence for basin completeness

This does **not** yet give full compact-region completeness, and it does not
yet rule out asymptotic basins along directions outside the enumerated
representatives. Within scope, it gives one structural reduction the open
register was missing:

- the remaining basin-completeness problem is now compact for the enumerated
  representatives;
- any additional exact basin reachable via an enumerated representative would
  have to live in a finite-radius region;
- the old loophole "maybe there are more exact basins arbitrarily far out along
  an enumerated representative" is gone.

So `I11` is partially reduced (within the enumerated representatives only)
from

```text
global completeness
```

to

```text
compact-basin completeness.
```

The reduction does not yet apply to asymptotic directions in the affine source
family that fall outside the enumerated representatives; that extension is
deferred (see section 5).

## 4. Numeric corroboration

The same runner also performs a chamber-sphere minimization on the pure-source
family and finds a strictly positive asymptotic floor:

```text
chi^2_inf >= 1.0e-3
```

across the tested chamber directions and row permutations. That numeric floor
is corroborating evidence for the theorem-level linear-algebra no-go above.

## 5. Scope

What is closed (within scope):

- the unbounded pure-source basin family **restricted to the enumerated
  algebraic representatives** (six row permutations times two real CP
  branches);
- the infinity-tail loophole in `I11` **along those enumerated
  representatives**.

What remains open:

- a compact-region completeness theorem ruling out additional bounded basins;
- the universal extension of the no-go to every asymptotic direction in the
  affine source family `H_base + m T_m + delta T_delta + q_+ T_q`, which is
  deferred pending a `T_m / T_delta / T_q` bridge derivation showing every
  generic asymptotic direction reduces to one of the enumerated
  representatives.

## 5a. No-Go Discipline Gate (N1-N8)

**Status:** PASS for the narrowed enumerated-representative no-go only.

- **N1 alternative routes considered.** (1) six row permutations: exhausted by
  the runner's full-rank linear systems; (2) real CP branch `delta_CP=0`:
  exhausted by the same rank test; (3) real CP branch `delta_CP=pi`:
  exhausted by the same rank test; (4) nonzero degenerate-eigenvalue escape:
  blocked because full rank forces the entire eigenvalue vector to zero; (5)
  chamber-sphere numerical floor: corroborates the algebraic obstruction on
  tested chamber directions, but is not load-bearing; (6) generic affine
  asymptotic directions outside the enumerated representatives: explicitly
  not closed and moved out of scope.
- **N2 wall independence.** The remaining open items are not inflated into
  independent retained walls: compact-region completeness and the generic
  `T_m / T_delta / T_q` bridge are separate future tasks, and neither is
  needed for the enumerated-representative no-go.
- **N3 hidden-wall scan.** The only hidden candidate is the bridge from a
  generic asymptotic direction to the enumerated real-orthogonal PMNS
  representatives; it is surfaced explicitly as out of scope.
- **N4 residual matching.** The residual being closed is exact
  `chi^2=0` escape to infinity along enumerated pure-source chamber
  representatives. The note does not cite the rank test as evidence against
  compact basins or generic affine directions.
- **N5 rhetoric audit.** Universal phrases are narrowed to "along the
  enumerated representatives"; broader basin-completeness wording is marked
  open.
- **N6 partial-closure path scan.** No new axiom is requested. The future path
  is a bridge derivation relating generic affine directions to enumerated
  representatives, or a compact-basin completeness theorem.
- **N7 steelman.** A hostile reviewer can still object that a generic
  affine-source direction need not reduce to one of the twelve enumerated
  representatives; this objection is accepted and is exactly why the universal
  no-go is deferred.
- **N8 cross-cycle echo.** Prior source-surface no-go overclaims in this lane
  failed by treating one tested family as universal. This note avoids that
  echo by retaining only the exhaustively enumerated algebraic representatives.

## 6. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_asymptotic_source_no_go_2026_04_20.py
```

Expected final line:

```text
PASS=26 FAIL=0
```
