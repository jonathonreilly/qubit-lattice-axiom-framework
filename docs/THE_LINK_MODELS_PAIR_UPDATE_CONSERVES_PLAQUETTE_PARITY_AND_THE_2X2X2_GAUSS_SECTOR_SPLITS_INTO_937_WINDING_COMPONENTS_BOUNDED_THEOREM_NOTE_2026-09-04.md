---
claim_id: link_model_qmc_pair_update_parity_winding_sectors_2x2x2
claim_type: bounded_theorem
claim_scope: "On TWO NAMED FINITE GEOMETRIES carrying ONE DESIGNED SPIN-1/2 LINK ROLE per edge in the conventions of PR #7911 -- the fully periodic 2x2x2 torus (24 links, 8 vertices at coordination z_v = 6, 24 four-link faces, rho_v = 0 parity-admissible and neutral) and the height-1 cylinder ladder at L = 8 (24 links, 16 vertices at z_v = 3, 8 faces, with PR #7911's declared staggered background 2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i) -- for the ONE DECLARED PURE-GAUGE LAW H = -lambda sum_f P_f with P_f = W_f + W_f^dag the oriented four-link ring exchange, lambda supplied and set to 1, no matter, and the electric term a c-number at spin 1/2 by PR #7893 T3(6): (T1) [exact] the 2x2x2 Gauss sector has dimension 9600, confirming PR #7911, and under single plaquette flips it is not one connected component but 937, with the full size multiset 864 x 1, 464 x 6, 252 x 12, 136 x 8, 36 x 6, 6 x 144, 1 x 760; the analytic Gauss-law-zero configuration e(v,x) = (-1)^{v_y+v_z}, e(v,y) = (-1)^{v_z+v_x}, e(v,z) = (-1)^{v_x+v_y} has G_v = 0 at every vertex of any even L^3 torus and exactly half its faces applicable (12/24, 96/192, 324/648 at L = 2, 4, 6); the global ground state E_0 = -9.0267209135 of the full sector lies in the 864-state component containing that configuration, with ground-vector weight 1 there, while the full-sector first excitation Delta_1 = 1.6276099336 carries weight 1.1e-29 on it and the component's own internal gap is 2.2257853859, larger by 36.8 per cent. (T2) [exact] A same-plaquette operator-pair switch creates and destroys off-diagonal operators two at a time at one face, so it changes every face's flip count by 0 or +-2 and samples only closed walks of even plaquette parity; the six faces of a unit cube have link-sets XORing to zero at all 8 cubes of the 2x2x2 torus, so odd-parity closed walks exist there and one is exhibited; the configuration graph has 47 nodes, 104 edges and 58 independent cycles on the ladder and 864, 3456 and 2593 on the torus, and the rank of the plaquette-parity map on the whole cycle space -- an invariant, unlike any fundamental-cycle count -- is 0 on the ladder, where every closed walk has even parity and the restriction is empty, and 10 on the torus, where the even-parity walks are an index-1024 subgroup. (T3) [witness, declared seed 20260903] The embedded sign-free SSE, compiled by the runner, validates on the ladder at L = 8 -- E(beta) within 0.17, 0.28, 0.33, 1.12 sigma of the exact 47-state-component values -4.5151826280, -4.8053520382, -4.8305435458, -4.8309585028 at beta = 2, 4, 8, 16 -- and does not on the 2x2x2 torus, where E(beta = 8) = -8.118460(6703) against the exact -9.0267206703, a deviation of 135.5 sigma, reproduced at diagonal weights C = 1, 4, 8 which agree with each other to 1.8 sigma; exact diagonalisation reproduces PR #7911's E_0 = -4.8309586723 and <P_f> = 0.6038698340 on the ladder, whose exact L = 8 energy density is -0.6038698340 lambda L, PR #7911's -0.6035607 being the L -> infinity value; in every run closure_err = 0, illegal = 0 and G_E(0) = 0.250000. (T4) [statement] An unguided six-face block proposal accepts with probability (lambda/C)^6 N_s / C(N_p, 6), which at C = 2 is 9.3e-07 on the 2x2x2 torus and 1.6e-11 at 4^3, so a worm, a directed loop or a genuine cube cluster is what changes per-face flip parity at a usable rate; compute is not the obstacle, a 4^3 sweep at beta = 16 costing 0.30 ms at string length M = 10871, about 59 s per 2e5 sweeps on one core; and any winding-conserving sampler reads a sector-internal gap, not a full-sector one. The link role is designed, not derived; lambda is supplied; the background convention on the ladder is PR #7911's declared one. NO PHASE CLAIM IS MADE FOR THREE DIMENSIONS: whether the pure link sector is gapped, gapless, Coulomb or ordered in three dimensions is not decided here and no reading is offered in either direction; the 4^3 numbers of the source computation are recorded as a restricted-sub-ensemble baseline only. No continuum limit is taken; no claim is made that this U(1) is electromagnetism. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.py
---

# The link model's pair update conserves plaquette parity, and the 2x2x2 Gauss sector splits into 937 winding components

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.py`](../scripts/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.txt`](../logs/runner-cache/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

PR #7911 priced the spin-1/2 link ring exactly, found it gapped and confining, and named its own next tool: the ring has no transverse direction, exact diagonalisation is
out of reach at any three-dimensional size, and the model carries no sign problem, so **quantum Monte Carlo** is what the photon question needs. This note tools that
route and prices it. A sign-free stochastic series expansion for `H = -lambda sum_f P_f` is built, and it validates on PR #7911's ladder to a fraction of a sigma at four
temperatures. On the smallest three-dimensional torus it does not, by 135 sigma against an exact answer -- and the reason is provable rather than incidental. Two exact
facts about the smallest three-dimensional Gauss sector come out of chasing it: the sector is not one ergodic component under plaquette flips but 937, and its cheapest
excitation sits in a different one from its ground state. The three-dimensional question stays open, now with its tooling requirement stated exactly.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-geometry theorems about one declared pure-gauge law on one designed spin-1/2 link role per edge, on the 2x2x2 torus and the height-1 ladder at L = 8: the Gauss-sector census, its decomposition into plaquette-flip components, the placement of the ground state and the first excitation, the analytic Gauss-law-zero configuration on any even L^3 torus, and the plaquette-parity obstruction of the same-plaquette operator-pair update stated as the rank of a map on the cycle space. Those items are integer and bit arithmetic with no floating-point step; the spectral and thermal items are floating-point cross-checks at the stated tolerance; the sampler rows are witnesses at a declared seed with a compiled engine, and are labelled as such."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-geometry theorem, and route to its owner the question this note does not decide: whether the link sector carries a gapless transverse mode in three dimensions, for which the tooling requirement is now exact -- a worm, directed-loop or cube-cluster update that changes per-face flip parity, together with the sector bookkeeping of T1."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the four statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `C1`, `C2`, `E1` and `E4` are exact -- integer and
bit arithmetic on explicit Gauss-sector bases, with no floating-point step -- `C3`, `C4` and `E3` are floating-point cross-checks at the stated tolerance, and group `D`
together with `E2` are `[witness]` rows: a compiled sampler at a declared seed, and a wall-clock rate.

1. `T1` (`A`). The 2x2x2 Gauss sector, the analytic Gauss-law-zero configuration, the split into 937 plaquette-flip components with its full size multiset, and where the
   ground state and the first excitation sit.
2. `T2` (`B`). The pair update's plaquette-parity obstruction: the cube relation, the fundamental-cycle census, and the tree-independent rank.
3. `T3` (`C`, `D`). The exact references on both geometries, and the `[witness]` sampler rows against them.
4. `T4` (`E`). What a correct three-dimensional sampler needs, and the scope this note keeps.

## Imports and authority

Imported scientific authority: none load-bearing. The quantum-link (gauge-magnet) presentation, the ring-exchange plaquette term, the stochastic series expansion with
identity padding, worm and directed-loop updates, and the spanning-tree/fundamental-cycle vocabulary are standard methodology; **every object is redeclared here and
every statement is recomputed by the runner**, the sampler included -- its C source is embedded in the runner and compiled at run time, so no binary and no external
datum is trusted. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, no grade and no dependency weight:

- `THE_SPIN_HALF_LINK_RING_IS_GAPPED_AND_CONFINING_THE_PHOTON_QUESTION_NEEDS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7911): the conventions used
  here verbatim -- `E_e = Z^L_e/2`, `U_e = sigma^+_e`, `G_v = (div E)_v - rho_v`, `P_f = W_f + W_f^dag`, the ladder's declared staggered background, `dim(Gauss) = 49` at
  `L = 8` and `9600` at `2x2x2`, `E_0 = -4.8309586723`, `Delta_1 = 1.6276099336`, and the sign-structure result that makes sampling available. Its named route --
  quantum Monte Carlo in three dimensions -- is what this note tools and prices.
- `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7893): the link algebra and `E_e^2 = I/4`, which is why the electric term supplies no dynamics at spin 1/2.
- `NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md` (`origin/main`): no pair `(a, a†)` in `A_x ≅ M_2(C)` satisfies `[a, a†] = I_2`, which is why the carrier here is a qubit-valued link and not a site-local oscillator.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms, quoted in "Setting" and nowhere used as a premise.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." The lattice is physical. **Qubit**: "Each site has a domain of local possibilities." and "The full one-site
possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
**Record**: "Records form.", "When present, a record locks exactly one admissible local possibility.", "A site never carries more than one record; records are
permanent.", "Only records are readable." and "A readout value is determined by record content alone."

**Why the carrier is a link qubit, and what registers.** The Qubit axiom gives each site `M_2(C)`, and the pointer note above shows by the trace identity that no
`(a, a†)` inside `M_2(C)` satisfies `[a, a†] = I_2`, so a site-local bosonic oscillator is not available in this algebra. The `U(1)` carrier PR #7893 declares instead is
a **designed role**: one further two-state site per edge, assigned by design and derived from no axiom. `E_e = Z^L_e/2` is a one-record value on that site, so **the flux
registers**: it is record content, readable by the Record axiom. `U_e` and `P_f` carry `X` in every monomial, have no record-diagonal part, and register only through
correlations among records. Composition is **ordinary** throughout. Nothing below is derived from any axiom.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the two geometries, the link role, the
pure-gauge law and the background conventions. `P1` (`A`) is the 2x2x2 Gauss sector and its plaquette-flip components; `P2` (`B`) the parity obstruction of the pair
update; `P3` (`C`) the exact references on both geometries; `P4` (`D`) the `[witness]` sampler rows against `P3`; `P5` (`E`) the tooling statement. `P1` and `P2` use
`P0` only; `P3` uses `P0`; `P4` uses `P3`; `P5` uses `P1`, `P2` and `P4`. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **torus** is the fully periodic `L^3` cubic lattice, links owned by their tail site; at `L = 2` it has `24` links, `8` vertices at `z_v = 6` and `24` four-link
faces. The **ladder** is PR #7911's height-1 cylinder at `L = 8`: `24` links, `16` vertices at `z_v = 3`, `8` faces.

```text
E_e = (1/2) Z^L_e   (eigenvalues +-1/2),      U_e = (X^L_e + i Y^L_e)/2 = sigma^+_e
(div E)_v = sum_{e at v} s_{v,e} E_e,         s_{v,e} = +1 out of v, -1 into v
G_v = (div E)_v - rho_v,       rho_v = a STATIC background charge (no matter, so no n_v)
W_f = the oriented four-link ring product,    P_f = W_f + W_f^dag
H = -lambda sum_f P_f                                          THE DECLARED PURE-GAUGE LAW
rho_v = 0 on the torus (z_v = 6 even);  2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i on the ladder
```

`P_f` is **applicable** on a configuration iff `b_p = b_q`, `b_u = b_w` and `b_p != b_u` on its ordered quadruple, and its action is the XOR of the four link bits.
The **configuration graph** of a Gauss sector is the graph whose nodes are its states and whose edges are single applications of some `P_f`, each edge labelled by the
face it uses. A closed walk's **plaquette parity** is the vector over `GF(2)`, one entry per face, of its flip counts mod 2. `lambda` is **supplied** and set to `1`.

**The sampler, declared.** Put `H_{1,f} = C I` (diagonal, weight `C`, applicable in every configuration) and `H_{2,f} = lambda P_f`, so `H = N_p C - K` with
`K = sum_f (H_{1,f} + H_{2,f})`, and expand `Z = e^{-beta N_p C} Tr e^{beta K}` at fixed string length `M` with identity padding, `E = N_p C - <n>/beta`. The updates
are (1) diagonal insertion and removal of `H_{1,f}`, which never inspects the configuration because `H_{1,f}` is state-independent; (2) **the pair switch** -- for two
consecutive operators at the **same** face, with no off-diagonal operator on any link-sharing face strictly between them, switch both between type 1 and type 2; and
(3) a uniform cyclic rotation of the padded string, which is what turns `<alpha|e^{-beta H}|alpha>` into a trace. It is update (2) that Theorem 2 is about.

## Theorem 1 -- the smallest three-dimensional Gauss sector and its winding components

**Conclusion.** (1) `dim(Gauss) = 9600` on the 2x2x2 torus at `rho_v = 0`, confirming PR #7911, every state re-derived against `G_v = 0` with `max |2 (div E)_v| = 0`.
(2) The analytic configuration `e(v,x) = (-1)^{v_y+v_z}`, `e(v,y) = (-1)^{v_z+v_x}`, `e(v,z) = (-1)^{v_x+v_y}` -- declared, not searched -- has `G_v = 0` at every
vertex of any even `L^3` torus and **exactly half** its faces applicable: `12/24`, `96/192`, `324/648` at `L = 2, 4, 6`. (3) Under single plaquette flips the sector is
**not one connected component but 937**, with the full size multiset `864 x 1, 464 x 6, 252 x 12, 136 x 8, 36 x 6, 6 x 144, 1 x 760`, summing to `9600`. (4) The
analytic configuration lies in the `864`-state component, and so does the global ground state: `E_0 = -9.0267209135` on the full `9600`-state sector equals `E_0` on that
component, and the full-sector ground vector carries weight `1` there. (5) `[1e-9]` The full-sector first excitation `Delta_1 = 1.6276099336` carries weight `1.1e-29`
on that component -- it lives in **other winding sectors** -- while the component's own internal gap is `2.2257853859`, larger by `36.8` per cent.

**Proof.** Item 1 builds the sector by a slab sweep that assigns each site's unassigned incident links and enforces `G_v = 0` there, then re-derives `2 (div E)_v` from
the listed bit patterns. Item 2 evaluates the declared formula and counts applicable faces directly at `L = 2, 4, 6`. Item 3 assembles the flip graph on the `9600`
states and takes its connected components. Items 4 and 5 diagonalise the `864 x 864` component densely and the `9600`-row sparse `H` by Lanczos from a deterministic
starting vector, then project the full-sector vectors onto the component's index set. Items 1 to 3 are exact integer and bit arithmetic; items 4 and 5 are `[1e-9]`.

**Reading, not theorem.** Give every link one unit of flux either way so that as much flows into each vertex as out, and let the faces flip. The configurations that
satisfy the vertex rule number `9600` on the smallest cube, but they do not all reach one another: they fall into `937` separate families, and the largest holds `864`.
The cheapest configuration of all is in that largest family. The cheapest **excitation** is not -- it sits in a different family, and no amount of face-flipping gets
from one to the other.

## Theorem 2 -- the pair update conserves a plaquette parity

**Conclusion.** (1) The pair switch creates and destroys off-diagonal operators **two at a time at one face**, so it changes every face's flip count by `0` or `+-2`:
the plaquette parity of the sampled closed walk is a conserved quantity of the chain, and starting from the empty string only **even-parity** closed walks are ever
reached. (2) `[exact]` Odd-parity closed walks exist in three dimensions because each of the `12` edges of a unit cube lies in exactly two of its six faces, so the six
face link-sets XOR to zero, at all `8` cubes of the 2x2x2 torus; one odd-parity closed walk is exhibited from the analytic configuration. (3) `[exact]` The
configuration graph has `47` nodes, `104` edges and `58` independent cycles on the ladder and `864`, `3456` and `2593` on the torus. Under the runner's canonical
depth-first tree `0` of `58` ladder cycles and `2159` of `2593` torus cycles carry odd parity; under its breadth-first tree, `0` and `1573`. **The odd counts are
properties of the tree; the node, edge and cycle counts are not.** (4) `[exact]` The tree-independent statement is the rank of the plaquette-parity map on the whole
cycle space: **`0` on the ladder and `10` on the 2x2x2 torus**. Rank `0` says every closed walk on the ladder has even parity at every face, so the restriction is
**empty** there; rank `10` makes the even-parity closed walks an **index-1024** subgroup on the torus.

**Proof.** Item 1 is the update's definition: the switch acts on a pair `(pp, p)` at the same face and is an involution, so each face's operator count changes by an
even number. Item 2 XORs the six face link-sets at every cube and compares to zero, then walks the graph from the analytic configuration and returns the first
fundamental cycle of non-zero parity. Items 3 and 4 grow a spanning tree from the starting configuration with every adjacency list in the canonical order (face index,
then endpoint), form the fundamental cycle of each non-tree edge, and reduce the resulting parity vectors over `GF(2)` to a basis. All exact bit arithmetic.

**Reading, not theorem.** The update turns face-flips on and off in pairs at the same face, so whatever it does, it leaves each face flipped an even number of times
over any closed circuit. On the ladder that costs nothing: nothing the sampler would ever need requires an odd count. On a cube it costs almost everything: the six
faces of a cube close up on their own, using each exactly once, and that is the shape of most of what the sampler needs. Same update, empty restriction on one geometry
and a dominant one on the other.

## Theorem 3 -- the exact references, and the sampler against them

**Conclusion.** (1) `[exact]` The ladder at `L = 8` has `dim(Gauss) = 49`, matching PR #7911's `Lucas(8) + 2`, and splits into `3` components of sizes `47, 1, 1`.
(2) `[1e-9]` On the `47`-state one, `E_0 = -4.8309586723` -- PR #7911's value to the digit -- with internal gap `0.9726557606` and `<P_f> = 0.6038698340`. The exact
`L = 8` density is `-0.6038698340 lambda L`; PR #7911's `-0.6035607` is its `L -> infinity` limit, a different number, and it is the `L = 8` value a sampler on this
geometry has to return. (3) `[1e-9]` The exact canonical energies are `-4.5151826280, -4.8053520382, -4.8305435458, -4.8309585028` on the ladder component and
`-8.6891572261, -9.0239679296, -9.0267206703, -9.0267209135` on the `864`-state torus component, at `beta = 2, 4, 8, 16`. (4) `[witness, seed 20260903]` The compiled
sampler **validates on the ladder**: `0.17, 0.28, 0.33, 1.12` sigma from those values, with `<P_f> = 0.604067` at `beta = 16`. (5) `[witness, seed 20260903]` The same
engine, parameters and seed **do not validate on the 2x2x2 torus**: `E(beta = 8) = -8.118460(6703)` against `-9.0267206703`, a deviation of `135.5` sigma, and the
diagonal weights `C = 1, 4, 8` give `-8.103150(10723)`, `-8.122688(17783)`, `-8.070141(26243)`, agreeing with each other and with `C = 2` to `1.8` sigma while every one
is far from the exact value. (6) `[witness]` In every run `closure_err = 0` and `illegal = 0`, so `G_v` holds exactly and the walk stays inside its component, and the
imaginary-time embedding is exact: `G_E(0) = 0.250000`, which is `E_e^2 = 1/4` to the digit.

**Proof.** Items 1 to 3 build each Gauss sector by column transfer (ladder) or slab sweep (torus), take components of the flip graph, assemble `H` and diagonalise the
component densely, then form `E(beta) = tr(H e^{-beta H})/tr(e^{-beta H})` from the full spectrum. Items 4 to 6 compile the embedded C source with the ambient C
compiler at `-O2`, write the geometry files from the runner's own indexing, run the engine at seed `20260903` with `2e4` equilibration and `1e5` sampling sweeps in
`40` bins (`4e4` for the `C` scan), and compare the bin mean and its standard error to items 2 and 3. `[1e-9]` for items 2 and 3; items 4 to 6 are witnesses, reproduced
exactly from the declared seed.

**Reading, not theorem.** The sampler is right where it is cheap to check and wrong where it is expensive to check, on the same code at the same seed. A ladder validation is necessary and not sufficient; the smallest three-dimensional exact answer is what catches the difference.

## Theorem 4 -- what a correct three-dimensional sampler needs

**Conclusion.** (1) `[exact]` An unguided six-face block proposal -- pick six of the `N_p` faces and switch all six from diagonal to off-diagonal -- lands on a cube for
only `N_s` of the `C(N_p, 6)` six-subsets, at the pair update's weight ratio `(lambda/C)^6`. At `C = 2` that is `9.3e-07` on the 2x2x2 torus and `1.6e-11` at `4^3`. The
six-face block therefore has to be built as a **cluster**, or replaced by a **worm / directed-loop** update that propagates a Gauss-law defect through the operator
string; either changes per-face flip parity at a usable rate. (2) `[witness, measured here]` **Compute is not the obstacle.** One core, `4^3` torus at `beta = 16`,
`C = 2`: `8e3` sweeps at string length `M = 10871` run at `0.30` ms per sweep, so `2e5` sweeps cost about `59` s, with `closure_err = 0` and `illegal = 0`. Deciding the
phase needs `L >= 8`-`16` so that `k` runs over several values below the zone boundary, and `beta ~ 4L`-`8L` so that `beta Delta >~ 5` at the smallest non-zero `k`;
that is days of core time, not years. (3) `[1e-9]` Any **winding-conserving** sampler reads a sector-internal gap. At 2x2x2 that is `2.2257853859` against the
full-sector `1.6276099336`, a difference of `36.8` per cent, so which of the two a number is has to travel with the number. (4) `[exact]` The `4^3` rows of the source
computation are recorded as a **restricted-sub-ensemble baseline** and no phase is read off them; where this update can be checked against an exact answer it is
`10.1` per cent short in `|E|`.

**Proof.** Item 1 evaluates `(lambda/C)^6 N_s / C(N_p, 6)` at `L = 2` and `L = 4` in exact integer arithmetic. Item 2 times a short run of the compiled engine and reports the rate and the engine's own invariants; the size and temperature requirements are standard resolution conditions restated, not fitted. Item 3 is Theorem 1 item 5 restated as an instruction. Item 4 compares the `[witness]` torus energy to the exact one.

**Reading, not theorem.** The thing standing between this model and an answer in three dimensions is an update, not a machine. A face-pair update is cheap and wrong
there; a loop or cluster update is a day or two of work and would be right; and once one exists, the sizes that would settle the question cost days of one core, not
years. What must travel with any number it produces is which gap it is.

## Corollary -- what this note settles, and what it leaves open

Within the setting declared above, on the two named finite geometries:

1. **The smallest three-dimensional Gauss sector is not one ergodic component under plaquette flips but 937**, and the physical first excitation lives in a winding
   sector other than the ground state's. Sector-internal and full-sector gaps therefore differ -- by `36.8` per cent at 2x2x2 -- and any claim about a gap in this model
   has to say which one it is quoting. That bookkeeping is new relative to PR #7911, which reported the full-sector `Delta_1` without a sampler in view.
2. **The natural operator-pair update conserves a plaquette parity that is trivial on a ladder and dominant in three dimensions**, which is exactly why it validates on
   one and does not on the other. Rank `0` against rank `10`: an exact obstruction of the update, not a bug in its implementation, and detectable in advance on any new
   geometry by the same cycle-space rank.
3. **A correct three-dimensional sampler needs a loop or cluster update, and the compute to decide the phase is modest once it exists.** The unguided block proposal is
   `1.6e-11` at `4^3`; a `4^3` sweep at `beta = 16` costs `0.30` ms. The missing ingredient is named and priced, and it is an algorithm.
4. **The three-dimensional photon question remains undetermined**, now with its tooling requirement stated exactly. Nothing here says the pure link sector in three
   dimensions is gapped, and nothing here says it is gapless. PR #7911 left the question open for want of a tool; this note leaves it open for want of one update inside
   that tool, and says which update.

**Reading, not theorem (this register).** The sampling method that works on the ring fails on the smallest cube for a reason that can be proved: its update never
changes a certain parity, and on a ring nothing needs that parity changed while on a cube almost everything does. The cube's allowed configurations also fall into
hundreds of separate families, and the cheapest excitation sits in a different family from the ground state. So the question of light in three dimensions is still open,
and what it needs is a better update, not more computer time.

## Where this note disagrees with its own source computation

The scratch computation this note lands from is recomputed here, and three of its readings are corrected or sharpened rather than carried:

1. **The odd-cycle count is not an invariant.** The source reports `2246` of `2593` odd-parity fundamental cycles on the 2x2x2 torus. That number is a property of the
   spanning tree it used: the runner's canonical depth-first tree gives `2159` and its breadth-first tree `1573`, and the source's own breadth-first pass gave `1563`.
   All of these are correct counts of different bases of the same cycle space. **The invariant is the rank of the plaquette-parity map, `10`**, which every tree agrees
   on and which is what actually states the obstruction; the ladder's `0 of 58` *is* invariant, because rank `0` means no basis can contain an odd cycle. Theorem 2
   states the rank first and the counts second, and the corollary rests on the rank.
2. **The `4^3` cost.** The source records `~100` s per `2e5` sweeps at `beta = 16`; measured here on one core the same run costs about `59` s. Same order, same
   conclusion -- compute is not the obstacle -- and the row is labelled a measured wall-clock rate, which is hardware-dependent by nature.
3. **The `C`-scan run length is not recorded** in the source logs, so this note declares its own (`2e4` equilibration, `4e4` sampling sweeps at seed `20260903`) and quotes the values that follow, rather than three numbers whose parameters are unknown. The substance -- mutual agreement across `C`, and a large common deviation from the exact value -- reproduces.

Carried forward unchanged from the source, and worth restating: the engine embedded here is the **post-fix** version of the source's SSE, after a defect in which the
configuration was propagated with the *new* operator type following an accepted pair switch rather than the old one. Its symptom was `closure_err > 0` and
`illegal > 0`; those two invariants are checked every sweep of every run reported above and are `0` throughout, which is what makes the 2x2x2 failure a statement about
the update rather than about its coding.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The link role, the pure-gauge law and the background conventions are declared objects, and no coefficient is derived:
  `lambda` is supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears.
- **No phase claim is made for three dimensions**, in either direction. Whether the pure link sector is gapped, gapless, Coulomb or ordered in three dimensions is not
  decided here; the `4^3` numbers of the source computation are a restricted-sub-ensemble baseline and nothing is read off them. No continuum limit is taken, no matter
  appears, and no claim is made that this `U(1)` is electromagnetism.

## Interfaces named for other lanes, not moved here

- **The loop update.** A worm or directed-loop update that propagates a Gauss-law defect through the operator string, or a genuine cube cluster, is what changes
  per-face flip parity at a usable rate. It is not written here, and nothing here says what it would find.
- **Larger tori.** `4^3` and above are outside exact reach, so the parity rank of Theorem 2 is the pre-flight test available before a sampler is trusted on a new geometry. Computing it needs the configuration graph, itself exact-diagonalisation-sized; a cheap proxy for it is not addressed here.
- **The winding-sector bookkeeping.** Which winding sectors a physical answer should average over, and whether a sector-internal gap or a full-sector one is the object
  of interest for a photon, is a modelling question this note does not settle -- it only shows the two differ and insists the distinction be carried.
- **Larger link algebras.** Spin-1 or larger lifts the coordination-parity condition, makes the electric term non-trivial, and changes both the sector and the update.

## Remaining live routes

1. Implement the loop or cluster update and rerun the 2x2x2 validation against Theorem 3 item 3.
2. The parity rank on the `2x2xL` tube and on `4^3`, as far as the configuration graph can be built.
3. Which gap a photon question wants, sector-internal or full-sector, and how to sample across winding sectors if it wants the latter.
4. What the coupled matter hop of PR #7893 does to the sector decomposition of Theorem 1.

## Executable claim block

```text
setting: 2x2x2 periodic torus (24 links, 8 vertices at z_v = 6, 24 faces, rho_v = 0) and PR #7911's height-1 cylinder ladder at L = 8 (24 links, 16 vertices at z_v = 3, 8 faces, 2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i); ONE DESIGNED spin-1/2 link role per edge; no matter; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md and used as no premise
law: E_e = Z^L_e/2, U_e = sigma^+_e, G_v = (div E)_v - rho_v, P_f = W_f + W_f^dag, H = -lambda sum_f P_f with lambda supplied and set to 1; electric term a c-number by E_e^2 = I/4
census: dim(Gauss) = 9600 at 2x2x2 and 49 at the ladder, both confirming PR #7911; every state re-derived against G_v = 0, max residual 0
ice: e(v,x) = (-1)^{v_y+v_z}, e(v,y) = (-1)^{v_z+v_x}, e(v,z) = (-1)^{v_x+v_y} has G_v = 0 on any even L^3 torus with exactly half the faces applicable: 12/24, 96/192, 324/648 at L = 2, 4, 6
components: 9600 splits under single plaquette flips into 937 components, multiset 864 x 1, 464 x 6, 252 x 12, 136 x 8, 36 x 6, 6 x 144, 1 x 760; the ladder's 49 into 3 of sizes 47, 1, 1
placement: the global ground state E_0 = -9.0267209135 lies in the 864-state component (ground-vector weight 1); the full-sector Delta_1 = 1.6276099336 carries weight 1.1e-29 there; the component's internal gap is 2.2257853859, larger by 36.8 per cent
obstruction: the same-plaquette operator-pair switch changes every face's flip count by 0 or +-2, so only even-parity closed walks are sampled; the six faces of a unit cube XOR to zero at all 8 cubes of the 2x2x2 torus, so odd-parity closed walks exist and one is exhibited
cycles: 47 nodes / 104 edges / 58 cycles on the ladder and 864 / 3456 / 2593 on the torus; odd counts 0 and 2159 under the canonical depth-first tree, 0 and 1573 under the breadth-first one -- TREE-DEPENDENT; rank of the plaquette-parity map = 0 on the ladder and 10 on the torus -- INVARIANT, index-1024 subgroup in three dimensions
exact_thermal: E(beta) = -4.5151826280, -4.8053520382, -4.8305435458, -4.8309585028 on the 47-state ladder component and -8.6891572261, -9.0239679296, -9.0267206703, -9.0267209135 on the 864-state torus component, at beta = 2, 4, 8, 16
ladder_ed: E_0 = -4.8309586723 = PR #7911's L = 8 value; internal gap 0.9726557606; <P_f> = 0.6038698340; exact L = 8 density -0.6038698340 lambda L, PR #7911's -0.6035607 being the L -> infinity value
witness_ladder: [witness, seed 20260903] C = 2, 2e4 equilibration, 1e5 sampling sweeps, 40 bins: 0.17, 0.28, 0.33, 1.12 sigma from the exact values; <P_f> = 0.604067 at beta = 16
witness_torus: [witness, seed 20260903] same engine and parameters: E(beta = 8) = -8.118460(6703) against -9.0267206703, i.e. 135.5 sigma; C = 1, 4, 8 give -8.103150(10723), -8.122688(17783), -8.070141(26243), mutually consistent to 1.8 sigma and all far from exact
witness_invariants: closure_err = 0, illegal = 0 and G_E(0) = 0.250000 in every run
tooling: unguided six-face block proposal accepts at (lambda/C)^6 N_s / C(N_p, 6) = 9.3e-07 at 2x2x2 and 1.6e-11 at 4^3, so a worm / directed-loop or a genuine cube cluster is required; 4^3 at beta = 16 runs 0.30 ms per sweep at M = 10871, about 59 s per 2e5 sweeps on one core; deciding the phase needs L >= 8-16 and beta ~ 4L-8L
not_claimed: no phase claim for three dimensions in either direction; the 4^3 rows of the source computation are a restricted-sub-ensemble baseline, 10.1 per cent short in |E| where checkable, and nothing is read off them
declared_departures: the source's 2246 of 2593 odd fundamental cycles is spanning-tree dependent (2159 / 1573 here) and is replaced as the load-bearing statement by the tree-independent rank 10; the 4^3 rate is 59 s per 2e5 sweeps here against the source's ~100 s; the C-scan run length is declared here because the source's is not recorded
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=21 FAIL=0 with a C compiler present; PASS=16 FAIL=0 without one, the five [witness] rows reporting SKIP with the reason
```

## Proof boundary

Everything is proved on **two named finite geometries** -- the fully periodic 2x2x2 torus and PR #7911's height-1 cylinder ladder at `L = 8`. Nothing is claimed for `Z^3`, for `4^3` or any larger torus, or for any other background convention.

The **link role is designed**: one further two-state site per edge, assigned by a design rule and derived from no axiom. The **law is declared**: `H = -lambda sum_f P_f`
with `lambda` supplied. The **background conventions are declared** and are PR #7911's. Nothing in this note is derived from any axiom; the axioms are quoted to fix
what "readable" means and to say why the carrier is a link qubit, and for nothing else.

**The sampler rows are witnesses, not theorems.** Group `D` and item `E2` are labelled `[witness]`: one compiled engine at one declared seed (`20260903`) with declared run lengths, reproducing exactly on a rerun and nothing beyond that. The engine's C source is embedded in the runner and compiled at run time, so the row is self-contained; where no C compiler is available the five `[witness]` rows report `SKIP` with the reason and the exact rows still close at `FAIL=0`. The ladder validation is not evidence that the engine is correct in general -- Theorem 2 is precisely the statement that it is not -- and the torus failure is evidence about the update, established by `closure_err = 0` and `illegal = 0` throughout.

**The odd-cycle counts are tree-dependent** and are reported as such; the load-bearing statement of Theorem 2 is the rank of the plaquette-parity map, which no tree
choice can change.

**No phase claim is made for three dimensions.** Whether the pure link sector is gapped, gapless, Coulomb or ordered in three dimensions is not decided here and no
reading is offered in either direction. No continuum limit is taken, and no claim is made that this `U(1)` is electromagnetism.

## Review record

An honest auditor should come away with: one declared pure-gauge law on one designed spin-1/2 link role per edge, on two named finite geometries, whose smallest
three-dimensional Gauss sector is counted exactly at `9600` and shown to decompose under plaquette flips into `937` components with a fully listed size multiset -- the
ground state in the largest, the first excitation not in it at all, and the two gaps differing by `36.8` per cent. The natural operator-pair update of a stochastic
series expansion for this law conserves the parity of the flip count at every face; the rank of that parity map on the cycle space is `0` on the ladder, where the
restriction is empty, and `10` on the 2x2x2 torus, where the reachable closed walks are an index-1024 subgroup. A compiled sampler at a declared seed exhibits exactly
that: sub-sigma agreement on the ladder at four temperatures, `135.5` sigma disagreement on the torus, stable under the diagonal weight and with its own invariants
closing. The costs: the link role, the law and the background conventions are declared, not derived; `lambda` is supplied; the sampler rows are witnesses at one seed
and are labelled so; the odd-cycle counts depend on the spanning tree and the invariant rank is what carries the argument; the `4^3` wall-clock rate is
hardware-dependent; and **no phase claim is made for three dimensions in either direction** -- what is delivered is the sector bookkeeping, the exact obstruction, and
the price of the update that would settle it.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the four context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `FAIL=0`, runtime under the declared `150` seconds, and passing pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
