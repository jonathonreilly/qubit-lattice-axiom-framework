# Cubical-Ball All-R Boundary-Link Disk Theorem

**Date:** 2026-05-30
**Claim type:** positive_theorem
**Claim scope:** the all-R boundary-vertex link disk property of the cubical
ball `B_R` in `Z^3`: for **every** radius `R >= 2` and **every** boundary
vertex `v` of `B_R`, the vertex link `link(v, B_R)` is a PL 2-disk. The
theorem removes the finite-radius truncation of the boundary-link disk
certificate ([S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md))
by discharging its single open algebraic gap (the large-coordinate
`v_i <= -2` bridge lemma) analytically. The proof consumes only the
cube-corner membership predicate already used by the finite certificates;
no new axiom, no plaquette numerics, no gauge data, no continuum limit. The
PL `S^3` cone-cap identification is **explicitly out of scope** (see
"Out of scope" below); this note proves the topology of the boundary-vertex
links, not the compactification.
This source note records a proposed theorem surface; it does not set or
predict downstream review outcomes.
**Runner:** [`scripts/frontier_s3_all_r_boundary_link_disk.py`](./../scripts/frontier_s3_all_r_boundary_link_disk.py)
(13 PASS / 0 FAIL, all EXACT)

---

## Why this matters

The existing boundary-link disk certificates are finite-radius. The runner
`scripts/frontier_s3_boundary_link_theorem.py` verifies the disk property
directly for `R = 2..10` (5,778 boundary vertices) and verifies its bridge
lemma `link(v, B_R) = K_simp(P)` empirically only for `R = 2..6` (1,162
vertices, one of the two `[BOUNDED]` checks there; the observed-type
enumeration is the other). Two ingredients are already
unconditional:

- **Property 2 / 2a** (present cube set = connected downset, absent set =
  connected upset), proved for all `R` from the coordinate-separability
  `Phi(s) = sum_i f_i(s_i)`; and
- **Proposition Z** (every `Q_3`-both-connected octahedral subset closure
  `K_simp(P)` is a PL 2-disk), proved by exhaustive 126-subset enumeration.

The only thing standing between these and an all-R disk theorem is the
**bridge lemma in the `v_i <= -2` regime**, which the note's own text marks
as "the single remaining algebraic gap." This note closes that gap with an
R-free per-coordinate identity, supplying the genuinely new content the
family lacks.

---

## Setup and definitions

All objects coincide with those in
[S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md) and are
reproven from the cube-corner primitive in the runner.

**Cubical ball.** `B_R` is the union of all unit cubes whose 8 corners lie
within Euclidean distance `R` of the origin. A lattice point `w` is a
**site** of `B_R` iff some unit cube containing `w` lies entirely in the
ball. Each vertex `v = (v_1, v_2, v_3)` of `B_R` is incident to 8 unit
cubes, indexed by sign vectors `s = (s_1, s_2, s_3) ∈ {0, -1}^3`, with cube
min-corner `v + s`:

```text
C_s = [v_1+s_1, v_1+s_1+1] x [v_2+s_2, v_2+s_2+1] x [v_3+s_3, v_3+s_3+1].
```

**Per-axis penalty and farthest-corner distance.** For a cube whose
min-corner has axis value `t`, the farthest-corner squared distance along
that axis is

```text
g(t) := max(t^2, (t+1)^2).                                             (g)
```

The farthest-corner squared distance of the incident cube `C_s` is

```text
Phi(s) = g(v_1+s_1) + g(v_2+s_2) + g(v_3+s_3),                         (Phi)
```

and `C_s ⊆ B_R` iff `Phi(s) <= R^2`. (`g` is the runner's `compute_fi(t, 0)`;
`Phi` is `compute_phi`.)

**Octahedral link.** `link(v, Z^3)` is the boundary of the cross-polytope:
6 axis-vertices `v +- e_i`, 12 edges (orthogonal axis-direction pairs), 8
triangles (mutually orthogonal axis-direction triples), one triangle per
incident cube. `link(v, B_R)` is the subcomplex whose triangle `s` is present
iff `C_s ⊆ B_R`, whose edge is present iff the shared square face is in
`B_R`, and whose axis-vertex `v + d` is present iff `v + d` is a site.

**Simplicial closure of the present set.** Let `P = {s ∈ {0,-1}^3 :
Phi(s) <= R^2}` be the present-cube set. `K_simp(P)` is the subcomplex of the
octahedron whose triangles are `P`, with all their faces. The forward
inclusion `K_simp(P) ⊆ link(v, B_R)` is immediate (a present cube contributes
its full simplicial data). The content of the bridge lemma is the **reverse
inclusion**: that no simplex of the true link arises from a cube outside the
8 incident to `v`.

---

## The all-R closure: three lemmas and the bridge theorem

### Lemma H (closed form of the least incident-cube penalty)

Define `H(t) := min(g(t), g(t-1))`, the least per-axis penalty among the two
incident cubes that share axis value `t`. Then

```text
H(t) = t^2   for |t| >= 1,        H(0) = 1.                            (H)
```

*Proof.* For integer `t >= 0`, `g(t) = (t+1)^2` and `g(t-1) = t^2`, so the
min is `t^2`; for `t >= 1` this is `t^2`, and for `t = 0` it is `0`, but the
two incident cubes that share axis value `0` are those with min-corner axis
value `0` and `-1`, giving `g(0) = 1` and `g(-1) = 1`, so `H(0) = 1`. For
`t <= -1`, `g(t) = t^2` and `g(t-1) = (t-1)^2`, so the min is `t^2`. ∎

(The runner reproves `(H)` exactly over `|t| <= 200` with 0 violations.)

### Lemma SITE (closed-form site membership)

For any lattice point `w`,

```text
w ∈ sites(B_R)   <=>   B(w) := H(w_1) + H(w_2) + H(w_3) <= R^2.        (S)
```

*Proof.* `w` is a site iff some incident cube of `w` lies in `B_R`, i.e. iff
`min_s Phi(w, s) <= R^2`. By separability of `Phi` over coordinates, the
minimizing sign in each coordinate is chosen independently, and the per-axis
minimum is exactly `min(g(w_i), g(w_i - 1)) = H(w_i)`. Hence
`min_s Phi(w, s) = B(w)`. ∎

(The runner cross-checks `(S)` against the canonical `cubical_ball` site set
over all `(point, R)` with `R = 2..22`, 0 mismatches, and confirms
`B(w) = min_s Phi(w, s)` over the `31^3` lattice box.)

### Lemma FORCED (the new all-R content; closes the `v_i <= -2` regime)

For every integer `v_a` and every direction `eps ∈ {+1, -1}`, with the
**forced sign** `s_a^forced := 0 if eps = +1, else -1`,

```text
g(v_a + s_a^forced) = max( H(v_a), H(v_a + eps) ).                     (F)
```

This is an **equality** — not merely an inequality — holding region-by-region
for every integer `v_a`, toward-origin as well as away-from-origin. It is the
analytic counterpart of the empirical `v_i <= -2` check the note left open.

*Proof.* Take `eps = +1`, so `s_a^forced = 0` and the left side is `g(v_a)`.

- `v_a >= 1`: `g(v_a) = (v_a+1)^2`. By `(H)`, `H(v_a) = v_a^2` and
  `H(v_a+1) = (v_a+1)^2`, so the right side is `(v_a+1)^2`. Equal.
- `v_a = 0`: `g(0) = 1`; `H(0) = 1`, `H(1) = 1`, right side `1`. Equal.
- `v_a = -1`: `g(-1) = 1`; `H(-1) = 1`, `H(0) = 1`, right side `1`. Equal.
- `v_a <= -2`: `g(v_a) = v_a^2`. By `(H)`, `H(v_a) = v_a^2` and
  `H(v_a+1) = (v_a+1)^2 <= v_a^2`, so the right side is `v_a^2`. Equal.

The case `eps = -1` (forced sign `-1`, left side `g(v_a - 1)`) is the mirror
of `eps = +1` under `t -> -t` and is verified by the same four-region split. ∎

(The runner reproves `(F)` as a strict equality over `|v_a| <= 500` for both
directions, 0 violations, and confirms the valley identity
`g(v_k + s_k^pref) = H(v_k)` for the preferred free-axis sign.)

The geometric reading of `(F)`: the **V-shape of `g`** (the obstruction the
note flagged — a non-incident cube with min-corner `v_1 + 1` can be in `B_R`
while the incident cube with min-corner `v_1` is not) is exactly absorbed by
the right-hand `max`. The forced incident cube's penalty never exceeds the
larger of the two endpoint potentials `H(v_a)` (from `v`) and `H(v_a + eps)`
(from the axis-neighbour). There is no residual `v_i <= -2` case.

### Bridge Theorem (all R)

**Statement.** For every `R >= 2` and every boundary vertex `v` of `B_R`,
`link(v, B_R) = K_simp(P)`.

*Proof.* The forward inclusion is immediate. For the reverse inclusion, let
`sigma` be any simplex of the true link `link(v, B_R)`, with constrained axes
`C` (each carrying a direction `eps_a`, `|C| ∈ {1,2,3}` for a
vertex / edge / triangle) and free axes `F = {0,1,2} \ C`. Build the
**forced witness incident cube** `W`: forced sign `s_a^forced` on each
`a ∈ C`, and the valley (preferred) sign on each `k ∈ F`. By `(F)` on the
constrained axes and the valley identity on the free axes,

```text
Phi(W) = sum_{a∈C} g(v_a + s_a^forced) + sum_{k∈F} g(v_k + s_k^pref)
       = sum_{a∈C} max(H(v_a), H(v_a + eps_a)) + sum_{k∈F} H(v_k)
      <= max over corners q of sigma of [ H(q_1) + H(q_2) + H(q_3) ]
       = max over corners q of sigma of B(q),
```

where `q` ranges over `v + (any subset of {eps_a e_a : a ∈ C})`. The
inequality is the elementary fact that a sum of per-coordinate maxima is at
most the maximum, over the product set of corner choices, of the
corresponding corner sums (each coordinate's max is realized at one of its
two endpoint potentials `H(v_a)` or `H(v_a + eps_a)`, and the maximizing
corner `q` collects the realizing endpoint in every constrained coordinate).
Every such corner `q` is a corner of the true-link simplex `sigma`, hence a
site of `B_R`, hence `B(q) <= R^2` by `(S)`. Therefore `Phi(W) <= R^2`: the
forced witness cube `W` is present, and `W` carries `sigma`. So
`sigma ∈ K_simp(P)`, and no simplex outside `K_simp(P)` appears. This holds
for **all `R`** — `R` enters only as the uniform threshold `R^2`, with no
residual large-coordinate case. ∎

(The runner verifies the forced-witness domination inequality
`Phi(W) <= max_q B(q)` as a universal integer fact over the lattice box
`|coord| <= 20` for all simplex types, 0 violations, and confirms the
assembled end-to-end equality `link(v, B_R) = K_simp(P)` for every boundary
vertex over `R = 2..24` — 84,238 vertices, 0 mismatches — far beyond the
note's `R = 2..6`.)

---

## All-R boundary-link disk theorem (assembled)

**Theorem.** For every `R >= 2` and every boundary vertex `v` of `B_R`, the
vertex link `link(v, B_R)` is a PL 2-disk.

*Proof.* By the **Bridge Theorem**, `link(v, B_R) = K_simp(P)` for every
boundary vertex and every `R`. By **Property 2 / 2a**
([S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md), all-R),
the present set `P` is a `Q_3`-both-connected partition (a connected downset
with connected complement upset). By **Proposition Z**
([S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md),
exhaustive 126-subset enumeration), every `Q_3`-both-connected subset closure
`K_simp(P)` is a PL 2-disk. Hence `link(v, B_R)` is a PL 2-disk. The argument
is uniform in `R`: the only `R`-dependence is the threshold `R^2` inside the
membership predicate, and every supporting lemma is `R`-free. ∎

This **removes the finite-radius bound** on the boundary-vertex link disk
property: where the certificate previously established the disk property only
for the checked `R = 2..10` and the bridge only for `R = 2..6`, the disk
property now holds for **every** `R`, with the bridge discharged analytically.

### Structural corroboration: type stabilization and `O_h` orbits

The closure above does **not** rely on finite type-enumeration; the
`R`-free FORCED identity carries it. The following stabilization is the
descriptive structural account of the note's existing "102 cubical-ball-
realizable preference-order downset types," not a load-bearing step.

The labelled present-set types saturate: the cumulative count of distinct
labelled present sets `P` over boundary vertices is

```text
R = 2 : 26      R = 3 : 58      R = 4 : 78      R = 5 : 78      R = 6 : 102
```

and is then **frozen at 102 for all `R = 6..25`** (`R_0 = 6`; the runner
checks `R = 2..25`). Under the cube symmetry group `O_h = Aut(Q_3)` (order
48: coordinate permutations together with per-coordinate sign flips
`0 <-> -1`), these 102 labelled types form exactly **8 orbits**, of sizes

```text
{6, 8, 8, 8, 12, 12, 24, 24}   (sum = 102),
```

and the realized set is `O_h`-closed. The orbits organize by present-cube
count `|P|` (one orbit for each of `|P| = 1, 2, 3, 5, 6, 7`, and two orbits
for `|P| = 4`), matching the geometric reading: `|P| = 1` a convex corner,
`|P| = 7` a concave corner, the intermediate counts the axis-edge and
face-flat boundary types. This is the symmetry-quotient explanation of the
102-type count; the all-R disk property is proven independently of it via the
separable forced-cube identity.

The interior-vertex links are the full octahedral `S^2` (6 vertices, 12
edges, 8 triangles), `R`-independently, by the local 3x3x3 argument (the
runner verifies 10,316 interior vertices over `R = 2..11`, 0 non-full).

---

## What this supports

The all-R boundary-link disk theorem is the genuinely new content the finite
certificates lacked. It bears directly on the four finite-radius source notes
in the S3 / PL-topology family:

- [S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md)
  has its **bridge lemma `v_i <= -2` gap closed analytically** by Lemma
  FORCED, and its boundary-link disk property now has a proposed all-R source
  proof rather than only the checked `R = 2..10` certificate. This note
  supplies the missing all-R content of that note's Part A.
- [S3_GENERAL_R_DERIVATION_NOTE.md](S3_GENERAL_R_DERIVATION_NOTE.md)
  has its **Part A** (boundary-vertex link disk certificate) supported by the
  all-R theorem above. Its Part B (finite cone-cap construction) is unaffected
  and remains outside this theorem.
- [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md):
  unaffected — its finite cone-cap construction certificate (`R = 2..5`) is
  the cap step (Part B), which this note does not touch.
- [PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
  is unaffected — its finite cone-cap certificate (`R = 2..4`) is the cap step
  (Part B).

No on-main source note currently carries this all-R boundary-link bridge
theorem under this scope, so this note is new source content rather than a
restatement of an existing source note.

---

## Out of scope (the topology is the theorem)

This note proves the **boundary-vertex link disk property for all `R`** and
nothing further. The PL `S^3` cone-cap identification — the chain

```text
all-R boundary links are PL 2-disks  =>  partial B_R is a PL 2-sphere
  =>  B_R is a PL 3-ball  =>  M_R = B_R cup cone(partial B_R) ~ PL S^3
```

is **not** discharged here. The cap step requires external PL facts that are
not part of this theorem and are not registered framework import nodes:

- the cone on a PL `(n-1)`-sphere is a PL `n`-ball (Newman; cf.
  Rourke–Sanderson, *Introduction to Piecewise-Linear Topology*);
- "`partial B_R` is a PL `2`-sphere `=>` `B_R` is a PL `3`-ball" needs PL
  Schoenflies in dimension 3 (Alexander, 1924), since `B_R` is not convex for
  `R >= 3`;
- the closed-manifold identification additionally invokes van Kampen
  (`pi_1 = 0`), the PL Poincaré conjecture (Perelman, 2003), and TOP = PL in
  dimension 3 (Moise).

These are cited here only as the names of the steps that the cap closure would
require; they are **not** consumed as inputs to the present theorem, and none
is asserted. The framework-`S^3` identification and any physical-closure
interpretation are likewise out of scope. The single self-contained
contribution of this note is the all-R disk property of the boundary-vertex
links, proven from the cube-corner membership primitive alone.

---

## Reproducibility

```text
python3 scripts/frontier_s3_all_r_boundary_link_disk.py
```

Expected: 13 PASS / 0 FAIL, all EXACT. The runner reproves Lemma H
(`|t| <= 200`), Lemma SITE (`R = 2..22` against the canonical site set;
`min_s Phi` over `31^3`), Lemma FORCED (`|v_a| <= 500`, both directions, as a
strict equality), the forced-witness domination inequality (all simplex types,
`|coord| <= 20`), the assembled bridge `link(v, B_R) = K_simp(P)`
(`R = 2..24`, 84,238 boundary vertices, 0 mismatches), Proposition Z
(126 / 126 disks), Property 2 / 2a consistency (every realized present set is
`Q_3`-both-connected), the assembled all-R disk theorem, type stabilization
(`R_0 = 6`, frozen `R = 6..25`), the 8 `O_h` orbits, and the interior-link
octahedral property. The runner reuses the canonical primitives in
`scripts/frontier_s3_boundary_link_theorem.py` (`cubical_ball`,
`vertex_link_BR`, `compute_phi`, `enumerate_combinatorial_disk_certificate`,
`verify_link_equals_simplicial_closure`) as a single source of truth.
