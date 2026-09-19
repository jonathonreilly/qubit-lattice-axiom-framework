# formation-clauses-in-level-time, attempt 2 (worker w-macbookpro90c72-jb240, model grok-4.6)

## (1) The statement attempted

Objects: six-axis product rule `(p, q, r)`; sequential one-site formation `r(s | A)` of block 01; the monotone
class / NEC automaton of block 12 (S0–S1); rate-clause clocks of block 14; unit-clause joint vs sequential of
block 15; unrecorded free-window vs integrated-exterior of block 24 (which does not change a *fully recorded*
formation process on a window, and is set aside for the induced `Z^3` law).

**Statement (PARTIAL).**
(a) The north-east-centre product kernel on each level, with noise map S1
`ε_0 = 1 − p³/(p³ + q³ + 4r³)` (unanimous),
`ε_{2:1} = 1 − p² r / (r(p² + q²) + r²(p + q) + 2r³)` (orthogonal 2:1),
`ε_{anti} = 1 − p² q / (pq(p + q) + 4r³)` (antipodal 2:1),
and tie `P(a | a,b,c) = p/(3(p+q))`, is exactly the law of the **monotone sequential class** (every site
forms after its three past-octant neighbours). It is *not* the law of: (rate-a) uniform clocks (a random
permutation: on the cube `P(k) ≈ (1/4,…,1/4)` for `k = 0,1,2,3`); (rate-b seeded) clocks that fire only
next to records (on the cube, 1080 growth orders from a seed, `P(k=1) = 0.439` vs monotone `0.375`; mean
NEC-triples `0.189` per site vs `0.125`); (unit: joint window) the static law.
(b) The six ordered states of the monotone class are the six axis-aligned values, selected by the majority
preference `p > max(q, r)` (S1). Seeded growth replaces majority by a typical `k=1` copy-kernel
`P(s | a) = φ(s,a)/Z_1`, which has no 2-of-3 vote and does not inherit S2's eroder bound. Different corner
orders of the cube give distinct sequential laws (`TV = 201510245581/4092954053760 ≈ 0.04923` at `(3,1,2)`
between the `(0,0,0)` and `(1,0,0)` corners), so the "six invariant laws" of the monotone class are
corner-dependent as laws on a finite window; on `Z^3` they are the eight corner classes of block 12.
(c) The unique recorded clause that makes the finished-window law independent of order is the unit clause
"the unit is the whole window" (joint = static). Sequential site units depend on the order as soon as a
cycle is present (U2); on the cube `TV(monotone, joint) = 1182193085/23402354976 ≈ 0.05052` at `(3,1,2)`.

Exact on the `2×2×2` cube (all `6^8` patterns) and the `3×3×2` slab (k-histograms; 18-site laws not enumerated).

## (2) Steps

**Step 1 — S1 noise map (PROVED; CHECKED).** Direct evaluation of `Π_i φ(s, a_i)/Z_3` reproduces the closed
forms of block 12 S1 at `(3,1,2)`, `(5,2,4)`, `(10,1,2)`. Majority preference on a 2:1 triple holds at
`(3,1,2)` and fails at `(1,3,2)`.

**Step 2 — monotone class on the cube and slab (CHECKED).** Level-then-lex order on the cube has
`k`-sequence `(0,1,1,1,2,2,2,3)` (one NEC triple, the last vertex). On the `3×3×2` slab,
`k ∈ {0:1, 1:5, 2:8, 3:4}` (four NEC triples). This is the finite-window shadow of S0: only sites whose
entire past octant of neighbours lies in the window and formed first see the S1 kernel.

**Step 3 — rate clauses change `k` (CHECKED).** Uniform random orders (2000 samples) on the cube give
`P(k) ≈ 1/4` each. Seeded growth (all 1080 connected build-orders from the origin): `P(k=1) = 0.439`,
`P(k=3) = 0.189`. Slab growth-sample (400 trajectories): `P(k=1) = 0.419` vs monotone `0.278`, and a
positive `P(k=4), P(k=5)` (in-plane neighbours of the `z`-layers). Seeded rate therefore does **not**
reduce to NEC: the typical recorded neighbourhood is one neighbour (copy with noise `1 − p/Z_1`), not
three. The leading ordering mechanism of S2–S6 is not inherited.

**Step 4 — unit clause: sequential ≠ joint on the cube (CHECKED).** At `(3,1,2)`,
`TV(μ_{monotone}, μ_{joint}) = 1182193085/23402354976`. U2 predicts this: the last vertex records three
inside neighbours. Opposite-corners-first (a non-growth, two `k=0` sites) has
`TV(·, joint) ≈ 0.0822` and `TV(·, monotone) ≈ 0.0725`. Two corner monotone orders differ
(`TV ≈ 0.04923`). So (b) the finite-window "ordered" sequential law is corner-dependent; (c) only joint
formation of the whole cube is order-independent.

**Step 5 — joint of a level does not change S0 (PROVED).** A level `{x : x_1+x_2+x_3 = t}` is an independent
set of `Z^3` (adjacent sites differ by 1 in the level). Joint formation of a level given the previous
level is a product of one-site conditionals given the three past neighbours, equal to sequential
formation in any in-level order. The unit clause "form each level jointly" is therefore the same as
monotone sequential, and is order-independent *within* the level.

**Step 6 — unrecorded-sites clause (PROVED as a non-contribution).** Free-window vs integrated-exterior
(Q1–Q5) compare two *static* readings of a partially recorded window. A formation process that records
every site of the window never consults an exterior component, so this pair does not change the induced
`Z^3` formation law. It would matter for a clause that leaves a positive density unrecorded.

## (3) Where the route stops

The cube/slab computations are exact for sequential vs joint vs growth *as finite-window laws*. They do
not compute the infinite-volume invariant laws or the ordering threshold as a function of `(p,q,r)` for
seeded growth (that would need a different automaton: Eden growth with a `k=1` kernel). One listed
growth order on the cube had `TV = 0` against monotone (a shelling with a different `k`-sequence but
equal law — possible if the two orders present the same recorded neighbourhoods up to a measure-zero
relabelling; not used as a separator). Opposite-first and the other corner *are* separators.

## (4) What would finish it

(1) The Eden-growth automaton on `Z^3` with kernel `r(· | k=1,2,3)` at the empirical interface
`P(k)`, and its eroder/non-eroder status. (2) Infinite-volume uniqueness region for uniform clocks
(mixture over all orders — already not static on any cycle, block 16). (3) Joint formation of a
covariant *plaquette* unit as a 3D process (block 15 U3 says it differs from sequential on each
plaquette).
