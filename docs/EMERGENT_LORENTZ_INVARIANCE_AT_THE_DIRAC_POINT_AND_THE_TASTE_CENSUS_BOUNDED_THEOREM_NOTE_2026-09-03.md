---
claim_id: emergent_lorentz_invariance_dirac_point_taste_census
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, carrying one fermionic mode per coarse vertex, with the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2} of the landed staggered kinetic-form clause read on that lattice, free nearest-neighbour hopping only, and on the named finite grids and tori only: (T1) the minimal magnetic cell of that sign field is 2x2x1, four coarse sites, on which H4(Q)^2 = (6 + 2 cos Q1 + 2 cos Q2 + 2 cos 2Q3) I with tr H4 = 0 symbolically -- direction 3 carries one site per cell, so its hop is diagonal and enters squared as 4 cos^2 Q3 = 2 + 2 cos 2Q3 -- hence Q = (pi,pi,pi) is not a node, its spectrum being (-2,-2,2,2); E4 = 0 exactly when cos Q1 = cos Q2 = cos 2Q3 = -1, and an exhaustive 60^3 scan of the magnetic BZ finds exactly the two 4-fold touchings Q = (pi,pi,pi/2) and Q = (pi,pi,3pi/2); the 2x2x2 cell folds both onto q = (pi,pi,pi) as one 8-fold touching, its spectrum at (Q1,Q2,2Q3) being the union of the 2x2x1 spectra at Q3 and Q3 + pi at 3.6e-15. (T2) At q = (pi,pi,pi) the velocity matrices are M_a = dH/dp_a = -Gamma_a exactly, all speeds 1, and the chirality operator X = -i m1 m2 m3 with m_a = M_a/v_a has spectrum +1 fourfold and -1 fourfold: two right-handed and two left-handed Weyl fermions of two components each, N_f = 2 four-component Dirac fields, net chirality 0; each 2x2x1 node separately carries 1R + 1L with speeds (1,1,2) in that cell's coordinates; in the intertwiner branch U Gamma_a U^dag = -sigma_a (x) T the transported velocity matrices are exactly sigma_a (x) T, so X = I (x) T exactly and T = +1 is the two right-handed Weyl while T = -1 is the two left-handed, a branch swap exchanging only the labels; the coarse tori L = 4, 6, 8 carry 8, 0, 8 zero modes at 1e-9, matching 'q_a = 4 pi m / L hits pi iff 4 | L'. (T3) E(pi + p)^2 = sum_a (2 - 2 cos p_a) exactly, expanding as |p|^2 - (1/12) sum_a p_a^4 + (1/360) sum_a p_a^6 + O(p^8), so v = E/|p| = 1 - (|p|^2/24) sum_a nhat_a^4 + O(p^4) with no free parameter; the [100]/[111] velocity spread is |p|^2/36 + O(p^4) over |p| = 0.8, 0.4, 0.1, 0.05, 0.0125 with log-log anisotropy exponent 1.998; and U H(pi+p) U^dag = sum_a sin p_a (sigma_a (x) T) + sum_a (1 - cos p_a)(I (x) B_a) to 4e-16, the taste-mixing term being O(p^2) and commuting with every spin generator. (T4) P(q)_{ss'} = delta_{ss'}/2 - H(q)_{ss'}/(2E(q)) has every entry with popcount(s XOR s') != 1 identically zero and P_ss = 1/2, so P_vu = 0 exactly whenever v - u has other than exactly one odd component; on a 288^3 cell-momentum grid the surviving entries satisfy |P_vu| |r|^3 -> (4/pi^2)|nhat_a| = 0.405285 |nhat_a|, with axis ratios 1.0049, 1.0024, 1.0019 at n = 41, 61, 81 and stride-subsampled shell means 0.21145, 0.20353, 0.20213 over 6 <= |r| <= 24, 30 <= |r| <= 50 and 60 <= |r| <= 90 against same-sample prediction means 0.21018, 0.20340, 0.20202, both falling to the sphere average 2/pi^2 = 0.202642. (T5) On the 8^3 coarse torus with one antiperiodic direction and on the 6^3 periodic torus, P_vv = 1/2 at every site and sum_{u != v} P_vu^2 = P_vv - P_vv^2 = 1/4 at 1e-15, and det [[P_vv, P_vu],[P_uv, P_uu]] <= P_uu P_vv on all 262144 ordered pairs with zero excess; on the 8^3 periodic torus the eight zero modes make half filling ambiguous -- proj(E < 0) has rank 252 and P_vv = 252/512 -- and that is reported, not used. Nothing here is derived from any axiom, no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py
---

# Emergent Lorentz invariance at the Dirac point, and the taste census

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py`](../scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.txt`](../logs/runner-cache/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

A staggered sign field on the coarse lattice `2Z^3` has a gapless point. What sits at that point is the question here, and it has three parts: how
many touchings the sign field really has and how many modes each carries; whether the modes disperse at one speed in every direction; and whether the
equal-time correlations they produce carry the coefficient a free massless Dirac field would carry. All three close on named finite grids and tori.
Along the way one reading of the eight-mode cell is corrected -- not its arithmetic, which stands, but the names attached to the factors.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact and named-grid theorems about the free coarse-lattice staggered hopping: the magnetic cell and its two nodes, the chirality census of the zero modes, the exact dispersion and its single isotropic velocity, the equal-time propagator's exact selection identity and its continuum coefficient, and the projector sum rule with negative association. Groups A-C are symbolic or exhaustive where tagged exact; the tagged numerical items are floating-point evaluations at the stated tolerance on the grids named."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: whether any clause supplies a mass term, and what the fine-lattice hopping pattern does to the isotropy."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`-`C` are exact where tagged --
symbolic identities in `sympy`, integer and `Z[i]` matrix arithmetic at zero tolerance, exhaustive scan -- and the items tagged `[numerical]` are
floating-point evaluations, at the stated tolerance, on the grids and tori named.

1. `T1` (`A`). The magnetic cell of the sign field and the two nodes it carries, and their folding onto one 8-fold touching.
2. `T2` (`B`). The chirality census of the zero modes, and the relabelling of the eight-mode cell that follows from it.
3. `T3` (`C`). The exact dispersion at the node, the `-1/12`, the single isotropic velocity and the `|p|^2/36` spread.
4. `T4` (`D`). The equal-time propagator: an exact selection identity, and the free massless Dirac coefficient.
5. `T5` (`E`). The projector sum rule and Pauli repulsion in the records.

## Imports and authority

Imported scientific authority: none load-bearing. The Kawamoto-Smit staggering, the Dirac-Kahler spin-taste basis, the Nielsen-Ninomiya counting and
the free massless Dirac equal-time propagator are standard methodology; every object is redeclared here and the runner recomputes every statement. No
observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency
weight:

- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): the coarse lattice, the `Cl(6)`
  cell algebra, the intertwiner `U` with `T = diag(1,1,-1,-1)`, and the `2 A1 + 2 T1` content of its Theorem 4. Pointer only; the cell algebra and `U`
  are redeclared below and rebuilt by this runner from scratch.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`: the kinetic-form clause and the corner-structure clause quoted below.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full
one-site possibility domain has algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations", and "For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one admissible local
possibility", "records are permanent", "Only records are readable."

The landed kinetic clause read on the coarse lattice is, verbatim:

> **Kinetic-form clause.** Within the declared kinetic class (the naive-Dirac kinetic form on nearest-neighbor `Z^3` links, made
> compatible with the matter-statistics clause by site-local spin diagonalization), the kinetic operator is the staggered operator
> `D = (1/2) Σ_{x,μ} η_μ(x) (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})` with the Kawamoto-Smit phases `η_1 = 1, η_2(x) = (−1)^{x_1},
> η_3(x) = (−1)^{x_1+x_2}`, unique as a local Z2 gauge class.

and its corner-structure clause reads:

> **Corner-structure clause.** The free staggered operator has the
> 8-element BZ-corner (taste-cube) doubler set, decomposing uniquely
> by Hamming weight as `1 + 3 + 3 + 1`; the hw=1 triplet carries an
> exact irreducible `M_3(C)` algebra (translations + `C_3[111]`)
> with no proper exact quotient.

Everything below reads that sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, free nearest-neighbour hopping only.
Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the
KS sign field on it, the magnetic cells, the cell algebra and the intertwiner. `P1` (`A`) is the magnetic cell and its two nodes; `P2` (`B`) the
chirality census; `P3` (`C`) the exact dispersion and the velocity; `P4` (`D`) the equal-time projector, its selection identity and its coefficient;
`P5` (`E`) the sum rule and negative association. `P3`, `P4` use `P1`'s node; `P2`, `P3` share `P0`'s intertwiner. Scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; the **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`,
`eta_3(v) = (-1)^{v_1+v_2}`, the clause's phases read in coarse coordinates. The hopping matrix is `H_{wv} = eta_a(v)` on each coarse bond and zero otherwise,
hermitian, no on-site term.

A **magnetic cell** is a block of coarse vertices on which the sign field is periodic, so that Bloch's theorem applies with that block as unit cell;
`H(Q)` denotes the corresponding block matrix and `E(Q)` its positive eigenvalue branch. A **node** is a `Q` with `E(Q) = 0`. The **velocity
matrices** at a node are `M_a = dH/dp_a` there; the **speeds** are `v_a = sqrt((M_a M_a)_{11})`, the **chirality operator** is `X = -i m_1 m_2 m_3`
with `m_a = M_a / v_a`, and a zero mode is **right-handed** when `X = +1` and **left-handed** when `X = -1`. On a `2x2x2` cell the algebra is

```text
Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3),  Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3),  T = diag(1,1,-1,-1),  B = (XX, XY, XZ)
H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a],   U Gamma_a U^dag = -sigma_a (x) T,   U Xi_a U^dag = I (x) B_a
```

with `U` rebuilt here by Clifford averaging over the `64` words of the generated group. The **equal-time projector** of the half-filled sea is
`P = proj(E < 0)`, whose Bloch form is `P(q) = (1/2)(I - H(q)/E(q))`; `P_vu` is its coarse-real-space matrix element and `r = v - u`, `nhat = r/|r|`.

## Theorem 1 -- the magnetic cell has two nodes, and they fold onto one

**Conclusion.** For the KS sign field on `2Z^3`:

1. The minimal magnetic cell is `2x2x1`, four coarse sites, and there `H4(Q)^2 = (6 + 2 cos Q_1 + 2 cos Q_2 + 2 cos 2Q_3) I` with `tr H4 = 0`: two
   doubly degenerate bands `+- E4`.
2. Direction `3` carries one coarse site per cell, so its hop is diagonal and enters squared, `4 cos^2 Q_3 = 2 + 2 cos 2Q_3`. Hence `Q = (pi, pi, pi)`
   is **not** a node of the `4x4`: its spectrum there is `(-2, -2, 2, 2)`.
3. `E4 = 0` exactly when `cos Q_1 = cos Q_2 = cos 2Q_3 = -1`, so there are exactly two nodes in the magnetic BZ, `Q = (pi, pi, pi/2)` and
   `Q = (pi, pi, 3pi/2)`, each a 4-fold touching. An exhaustive `60^3` scan finds these and no others.
4. Taking a `2x2x2` cell instead folds both onto the single point `q = (pi, pi, pi)`: the `8x8` spectrum at `(Q_1, Q_2, 2Q_3)` is the union of the
   `2x2x1` spectra at `Q_3` and `Q_3 + pi`, and the folded point is one 8-fold touching.

**Proof.** Items 1 and 2 are symbolic identities in the three cell momenta, the `4x4` square and trace expanded term by term against the hopping rules
and the double-angle identity checked in closed form. Item 3 is the observation that each of the three terms is bounded below by `-2`, so the sum
vanishes only when all three saturate, together with an exhaustive scan of a `60^3` grid over the magnetic BZ and an eigenvalue count at each hit.
Item 4 evaluates both cells at matched momenta over `60` random points, `[numerical, 1e-11]`, and counts the kernel dimension at the folded point.
Items 1-3 exact.

**Reading, not theorem.** The alternating signs repeat over a block of four sites, not eight, and that block has two places where the spectrum closes
rather than one. Writing the same field on the larger block puts both places on top of each other. The larger block is convenient but it is not where
the touchings are; the count of modes is the same either way.

## Theorem 2 -- the chirality census, and what the eight modes are

**Conclusion.**

1. At `q = (pi, pi, pi)` on the `2x2x2` cell the velocity matrices are `M_a = -Gamma_a` **exactly**, all three speeds are `1`, and the chirality
   operator has spectrum `+1` fourfold and `-1` fourfold. The eight zero modes are two right-handed and two left-handed Weyl fermions of two
   components each: `N_f = 2` four-component Dirac fields, net chirality `0`, as Nielsen-Ninomiya requires.
2. Each `2x2x1` node separately carries `1R + 1L`, with speeds `(1, 1, 2)` in that cell's coordinates. The two nodes together are `2R + 2L`, the same
   vector-like `N_f = 2`.
3. In the intertwiner branch `U Gamma_a U^dag = -sigma_a (x) T` the transported velocity matrices are exactly `sigma_a (x) T`, so `X = I (x) T`
   **exactly** and `H(pi + p) = sum_a p_a (sigma_a (x) T) + O(p^2)`. `T = +1` is the two right-handed Weyl (`det v = +1`) and `T = -1` the two
   left-handed (`det v = -1`); the other branch exchanges the two labels and nothing else, so the relative assignment is branch-independent.
4. The coarse tori `L = 4, 6, 8` carry `8, 0, 8` zero modes, exactly the count from `q_a = 4 pi m / L` reaching the node value `pi` precisely when
   `4 | L`.

**Conclusion, relabelling.** PR #7844's reading of the eight-mode cell as "a two-component spin and a four-component taste label" factors `8 = 2 x 4`.
The census factors the same `8` as `2` (Weyl components) `x 2` (chiralities) `x 2` (tastes). The multiplicities are unchanged, the `Cl(6)` structure
is unchanged, and the `2 A1 + 2 T1` decomposition of that note's Theorem 4 is unchanged; what changes is the name of the four-dimensional factor. Its
`T` grading is the chirality, not an internal quantum number, so the physical taste multiplicity is `2` and not `4`, and the field content is
`N_f = 2` four-component Dirac fields rather than four of anything.

**Proof.** Item 1's `M_a = -Gamma_a` is a symbolic differentiation of the `8x8` Bloch matrix followed by an exact comparison over `Z[i]` at
`q = (pi, pi, pi)`; the speeds and the spectrum of `X` follow from the `Cl(6)` relations and are evaluated exactly. Item 2 builds each `2x2x1` node's
velocity matrices by the same differentiation and reads the census, `[numerical, 1e-12]`. Item 3 rebuilds `U` on both branches by Clifford averaging,
verifies both intertwining relations and the transported `M_a` at zero tolerance, and reads `X = I (x) T` as an exact matrix identity; the handedness
is the sign of the determinant of the `3x3` velocity matrix on each two-dimensional spin block. Item 4 diagonalises the three tori directly, `[numerical, 1e-9]`, against the momentum-grid
count. The relabelling is item 3 read back: nothing is recomputed for it.

**Reading, not theorem.** The eight states at the closing point split into two mirror-image halves, one turning one way and one the other, and each
half is itself doubled. Counting the halves as a single four-way label hides the mirror. Counted properly there are two copies of one particle, each
copy carrying its own left and right halves, and the two copies are otherwise identical. The arithmetic that produced the four was right; the four was
a chirality pair times a genuine pair, not four of one thing.

## Theorem 3 -- one velocity, and where isotropy first fails

**Conclusion.**

1. `E(pi + p)^2 = sum_a (2 - 2 cos p_a)` exactly, with expansion `|p|^2 - (1/12) sum_a p_a^4 + (1/360) sum_a p_a^6 + O(p^8)`. The `O(p^2)` term is
   exactly isotropic and the leading anisotropy is the unique quartic cubic invariant with coefficient exactly `-1/12`.
2. Hence `v(nhat, |p|) = E/|p| = 1 - (|p|^2/24) sum_a nhat_a^4 + O(p^4)`: one velocity `v -> 1` in every direction, for every taste and both
   chiralities, with no free parameter anywhere in the statement.
3. The `[100]`/`[111]` velocity spread is `|p|^2/36 + O(p^4)`, tabulated at `|p| = 0.8, 0.4, 0.1, 0.05, 0.0125`, with log-log anisotropy exponent
   `1.998` against the exact value `2`.
4. `U H(pi + p) U^dag = sum_a sin p_a (sigma_a (x) T) + sum_a (1 - cos p_a)(I (x) B_a)` to `4e-16`. The taste-mixing second sum is `O(p^2)` and
   commutes with every spin generator -- a spin singlet -- so it does not enter the velocity at leading order.

**Proof.** Items 1 and 2 are `sympy` identities: the closed form of `E^2` at the shifted momentum, its series in a scale parameter along a fixed
direction, and the resulting series for `E/|p|` on the unit sphere, each residual reported as exactly zero. Item 3 evaluates the exact dispersion
along three directions and fits the spread, `[numerical]`. Item 4 compares the transported Bloch matrix against the closed form over random momenta at
three scales, `[numerical, 4e-16]`, and checks the commutator of each `I (x) B_a` with each spin generator at zero tolerance.

**Reading, not theorem.** Near the point where the spectrum closes, the matter travels at one speed in every direction, and it comes in two matched
copies of the same four-part particle, a left-handed and a right-handed half each. Nothing was tuned to make the speed the same along an axis and
along a diagonal; it comes out that way from the alternating signs alone. The first place the directions differ is small and known: the difference
between axis and diagonal grows like the square of the momentum, with the fixed factor `1/36`.

## Theorem 4 -- the equal-time propagator is the free massless Dirac one

**Conclusion.**

1. Every entry of `Xi_a` and `Gamma_a` whose row and column differ in other than exactly one bit vanishes, and their diagonals vanish. Hence
   `P(q)_{ss'} = delta_{ss'}/2 - H(q)_{ss'}/(2E(q))` is identically zero off the one-odd-component set, and `P_{ss} = 1/2`. So `P_vu = 0` **exactly**
   whenever `r = v - u` has zero or two or three odd components: an identity of the projector at every momentum, not an asymptotic statement.
2. On the surviving set, with `a` the unique odd component, `|P_vu| |r|^3 -> (4/pi^2) |nhat_a| = 0.405285 |nhat_a|`. On a `288^3` cell-momentum grid
   the axis ratios `|P| n^3 pi^2/4` along `(n,0,0)` are `1.0049`, `1.0024`, `1.0019` at `n = 41, 61, 81`.
3. Stride-subsampled shell means of `|P_vu| |r|^3` are `0.21145`, `0.20353`, `0.20213` over `6 <= |r| <= 24`, `30 <= |r| <= 50` and `60 <= |r| <= 90`,
   against same-sample means of the prediction `(4/pi^2)|nhat_a|` of `0.21018`, `0.20340`, `0.20202`. Both fall to the sphere average
   `2/pi^2 = 0.202642`. The landed `d^-3` value `0.21` is the finite-`|r|` value of this same law, not a different one.

**Proof.** Item 1 is an entrywise check of the six generators over all `64` index pairs at zero tolerance, together with the definition of `P(q)`.
Items 2 and 3 evaluate `P` per momentum on a half-shifted `288^3` grid of cell momenta -- a grid that misses the node exactly -- by one inverse FFT
per surviving cell-index pair, so no `V x V` object is ever formed; the shells are enumerated with the strides `1`, `2`, `3` recorded in the runner.
`[numerical]` throughout, on the grid named.

**Reading, not theorem.** The pattern of odds around a particle falls off as the inverse cube of distance with the coefficient a free Dirac field
would give. It is exactly zero in most directions -- not small, zero -- and where it is not zero it is fixed in size by nothing but the distance and
the direction. Nothing was fitted to reach that number; it is what the nearest-neighbour hop with the alternating signs produces on its own.

## Theorem 5 -- the sum rule and Pauli repulsion in the records

**Conclusion.** On the `8^3` coarse torus with one antiperiodic direction, which lifts the eight zero modes and leaves an exact half-filled projector,
and on the `6^3` periodic torus:

1. `P_vv = 1/2` at every site and `sum_{u != v} P_vu^2 = P_vv - P_vv^2 = 1/4` exactly, at `1e-15`. The number variance of the whole torus is zero:
   perfect screening.
2. `det [[P_vv, P_vu],[P_uv, P_uu]] <= P_uu P_vv` on all `262144` ordered pairs, with maximum excess exactly `0`. The record process is negatively
   associated -- repulsive, Pauli.
3. On the `8^3` **periodic** torus the eight zero modes make half filling ambiguous: `proj(E < 0)` has rank `252` and `P_vv = 252/512` uniformly, so
   the sum rule closes at `0.2499390` rather than `1/4` while the projector identity itself still holds at `4.4e-16`. That torus is reported here and
   is not used for the `1/4`.

**Proof.** Direct diagonalisation of each torus hopping matrix, projection onto the negative-energy subspace, and evaluation of the identities
entrywise. `[numerical, 1e-15]` for items 1 and 2, `[numerical]` for item 3's rank and value. The largest object formed is `512 x 512`.

**Reading, not theorem.** Fill every state below zero and the sites are each half occupied, with the fluctuation in the total exactly cancelled, and two
sites are never more likely to be occupied together than apart. That is what fermions do, and it is here with no statistics assumption added: it
follows from the filled sea being a projector.

## Corollary -- what the staggered sector's low-energy content is

Within the setting declared above, on the grids and tori named, and for free hopping only:

1. The low-energy content of the coarse-lattice staggered sector is **two tastes of one four-component Dirac field**, with a single isotropic velocity
   and a free massless Dirac equal-time propagator: contact with known physics at the level of the free Dirac field, and at that level only.
2. The content is **vector-like**: net chirality `0` at every node and in total, as Nielsen-Ninomiya requires on a lattice.
3. PR #7844's multiplicities stand unchanged; its four-dimensional factor is a chirality pair times a taste pair, so the physical taste multiplicity
   is `2`.

**What this is not.** No chiral sector: the content is vector-like and nothing here produces a chiral one. No generations from tastes: `N_f = 2` is two
identical copies of one field, with no distinguishing quantum number, no mass splitting and no label attached here. Not a proof of Lorentz symmetry of
correlators: what is shown is the isotropy of the one-particle dispersion and one equal-time kernel, with no dynamics attached, and boost covariance of
interacting correlators is untouched. Coarse lattice only: the fine `(4,2,2)` pattern's tetragonal anisotropy is not examined here.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice and the sign field are declared objects and the theorems are about them.
- No update rule, formation site, rate, coupling, mass, or absolute unit appears, and no dynamical clause is supplied.
- No corner of the taste cube is identified with any named species; the relabelling names none either.

## Interfaces named for other lanes, not moved here

- **The fine-lattice anisotropy.** The velocity statement is proved for the coarse hopping. The fine `(4,2,2)` role pattern is tetragonal, and what
  its encoded hopping does to the `|p|^2/36` spread is not examined here. A lane wanting isotropy on the fine lattice must supply it.
- **Interactions.** Only free hopping is compared; a four-fermion term could move the velocity and either coefficient, and nothing here bounds that.
- **A mass term.** The spectrum is exactly gapless at the node and no clause quoted here supplies a mass; that is the next lane's question.
- **The chiral sector.** Absent, by corollary item 2; a lane wanting chiral matter must break the pairing, and nothing here says how.

## Remaining live routes

1. Larger grids and other tori. The `288^3` momentum grid and the tori `4^3`, `6^3`, `8^3` are what is used; nothing is claimed beyond.
2. Subleading structure. Only the leading `|r|^-3` coefficient is measured, and only the projector's two-point content is examined.
3. The `8^3` periodic torus. Its zero modes leave half filling ambiguous; a lane wanting the `1/4` there must fix the filling.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one mode per coarse vertex, KS signs eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}, free nearest-neighbour hopping; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
cell_algebra: Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3), Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3), T = diag(1,1,-1,-1), B = (XX, XY, XZ); H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a]; U Gamma_a U^dag = -sigma_a (x) T, U Xi_a U^dag = I (x) B_a, rebuilt by Clifford averaging
magnetic_cell_and_nodes: minimal cell 2x2x1; H4^2 = (6 + 2cos Q1 + 2cos Q2 + 2cos 2Q3) I, tr H4 = 0; (pi,pi,pi) not a node, spectrum (-2,-2,2,2); exactly two 4-fold nodes (pi,pi,pi/2) and (pi,pi,3pi/2) by exhaustive 60^3 scan; 2x2x2 cell folds both onto q = (pi,pi,pi), 8-fold, union of spectra at 3.6e-15
census: M_a = -Gamma_a exactly, speeds 1, X = -i m1 m2 m3 spectrum +1 x4 / -1 x4 = 2R + 2L Weyl = N_f = 2 four-component Dirac, net chirality 0; each 2x2x1 node 1R + 1L, speeds (1,1,2); X = I (x) T exactly, T = +1 right-handed, T = -1 left-handed, branch swap exchanges labels only; tori L = 4, 6, 8 carry 8, 0, 8 zero modes
relabelling: landed 8 = 2 (spin) x 4 (taste) reads here as 8 = 2 (Weyl) x 2 (chiralities) x 2 (tastes); multiplicities and 2 A1 + 2 T1 unchanged; physical taste multiplicity 2
dispersion: E(pi+p)^2 = sum_a (2 - 2cos p_a) exactly = |p|^2 - (1/12) sum p_a^4 + (1/360) sum p_a^6 + O(p^8); v = 1 - (|p|^2/24) sum nhat_a^4 + O(p^4), no free parameter; [100]/[111] spread = |p|^2/36, log-log exponent 1.998; Dirac form to 4e-16, taste-mixing O(p^2) and a spin singlet
propagator: P(q)_{ss'} = delta/2 - H(q)_{ss'}/(2E) zero off the one-odd-component set exactly, P_ss = 1/2; |P_vu| |r|^3 -> (4/pi^2)|nhat_a| = 0.405285|nhat_a|; axis ratios 1.0049, 1.0024, 1.0019 at n = 41, 61, 81 on 288^3; shell means 0.21145, 0.20353, 0.20213 vs same-sample prediction 0.21018, 0.20340, 0.20202 -> 2/pi^2 = 0.202642; landed 0.21 is the finite-|r| value
sum_rule: 8^3 with one antiperiodic direction and 6^3 periodic: P_vv = 1/2, sum_{u != v} P_vu^2 = P_vv - P_vv^2 = 1/4 at 1e-15; negative association on all 262144 ordered pairs, max excess 0; 8^3 periodic has 8 zero modes, rank 252, P_vv = 252/512, reported not used
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=18 FAIL=0
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3` only, for **free nearest-neighbour hopping** only. Nothing is claimed for the fine lattice
`Z^3`, for infinite lattices, or beyond the `60^3` scan grid, the `288^3` cell-momentum grid and the tori `4^3`, `6^3`, `8^3` named above. The `288^3`
grid is a half-shifted grid of cell momenta, which misses the node exactly; the shell means are stride-subsampled with the strides `1`, `2`, `3`
recorded in the runner, so they are means over a declared sample of separations and not over every separation in the shell.

The `-1/12` and the `4/pi^2` are properties of **this** hop: the nearest-neighbour `pi`-flux hopping with the KS signs and no other term. They are not
properties of the framework, of any dynamical clause, or of any interacting theory. No coefficient, coupling, mass, rate or unit appears anywhere, and
no clause quoted here selects the half-filled sea whose projector Theorem 5 uses; that filling is a declared object.

The chirality assignment of Theorem 2 item 3 is stated in one intertwiner branch. The other branch exchanges the labels `T = +1` and `T = -1`; only
the relative assignment -- that the two `T` eigenspaces carry opposite chirality with two Weyl components each -- is used, and only that is
branch-independent. The relabelling corrects a **reading** of PR #7844, not any number in it: every multiplicity, spectrum and representation content
of that note stands.

Theorem 5's `1/4` requires an exactly half-filled projector; on the `8^3` periodic torus the eight zero modes prevent that, and the result there is
reported as ambiguous, not used.

## Review record

An honest auditor should come away with: a corrected count of where the coarse staggered spectrum closes, two nodes and not one, with the same eight
modes either way; a chirality census making those modes two tastes of one four-component Dirac field, vector-like, the four-dimensional factor of the
landed spin-taste reading resolved into a chirality pair times a taste pair; an exact dispersion, isotropic at leading order with no free parameter and
first anisotropic at `|p|^2/36`; an equal-time propagator with an exact selection identity and the coefficient `4/pi^2`; and a projector sum rule with
negative association where half filling is exact. Deliberately not decided: whether any clause supplies a mass, what the fine lattice does to the
isotropy, and whether interactions preserve any of it. The ambiguous torus is flagged not used, and the shells' stride subsampling is declared.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the three
context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache
pair closing at `PASS=18 FAIL=0`, runtime under the declared `120` seconds, stdout under `5500` characters, a current zero-dependency citation-manifest
entry, and passing pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
