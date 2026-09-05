---
claim_id: fermion_u1_quantum_links_gauss_law_support_condition
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3 carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}, and with ONE FURTHER DESIGNED ROLE per coarse edge -- a spin-1/2 link site carrying E_e = Z^L_e/2 and U_e = (X^L_e + i Y^L_e)/2, declared as a design element of exactly the same kind as the period-(4,2,2) superlattice role pattern of PR #7834 and derived from no axiom -- for the ONE DECLARED coupled law H^g = -t sum_<ij> eta_ij (T_ij X^L_ij + K_ij Y^L_ij)/2 with the supplied optional terms lambda sum_f P_f and (g^2/2) sum_e E_e^2 whose coefficients t, lambda and g are supplied and are fixed by nothing quoted here, and on the named finite blocks only -- the open 2x2x2 cube, the open 3x3x3 block, and the single coarse 2x2x1 plaquette: (T1) writing a_i^dag a_j = (T_ij - i K_ij)/2, the gauge-invariant hop a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i equals (T_ij X^L_ij + K_ij Y^L_ij)/2 exactly, Hermitian and exactly four Pauli monomials, on all 66 bonds of the cube and the open 3x3x3 block, with K_ij = -(1/2) A_ij (I - B_i B_j) Hermitian, K_ji = -K_ij, exactly two Pauli monomials on the same site support as T_ij (5 on the cube, 6, 8 or 10 on the open 3x3x3 block), K_ij = -i [T_ij, n_i], {T_ij, K_ij} = 0, [T_ij, K_ij] = -2i (n_i - n_j) = i (B_i - B_j), and J_ij of PR #7892 = -eta_ij t K_ij on every bond -- one factor of t and the sign minus, not eta (t/2) K_ij. (T2) With rho_v^{sea} = n_v - 1/2 or rho_v^{stag} = n_v - (1 - eps_v)/2 and (div E)_v = sum_{e at v} s_{v,e} E_e, every G_v = (div E)_v - rho_v is a pure Z operator, record-diagonal on the 2 z_v records at one corner -- six on the cube, three fermion edge records and three link records, and twelve at the interior corner of the 3x3x3 block -- with [G_v, G_w] = 0 for all 64 + 729 corner pairs, [G_v, H^g] = 0 at every corner, and sum_v G_v = -sum_v rho_v, which in the sea convention reads sum_v G_v = -Q; 2 (div E)_v sums z_v terms +-1 and so carries the parity of z_v, while 2 rho^{sea} is odd and 2 rho^{stag} is even, so spin-1/2 links admit rho^{sea} only at odd z_v and rho^{stag} only at even z_v; by exact enumeration the cube (z = 3) has 14400 joint record patterns of 2^24 in the sea convention and 0 in the staggered one, while the plaquette (z = 2) has 0 and 14; exactly 2240 of the 4096 cube fermion record patterns admit at least one link pattern and they are precisely the half-filled N = 4 sector, with link-pattern multiplicities 192 x 4, 1024 x 6, 768 x 7, 192 x 8 and 64 x 9; and since every nontrivial face-loop product carries X and so has zero diagonal, dim(Gauss and code) = 14400/2^5 = 450 on the cube and 14/2^1 = 7 on the plaquette; and G_v = 0, being a linear relation among the corner's 2 z_v records, is implemented by site-level forcing in ANY formation order -- on the cube in the sea convention and the plaquette in the staggered one, every occurring assignment of all but one of a corner's records leaves exactly one admissible value for the last (1248 conditioning events), no occurring record set leaves an absent record with an empty admissible set (11432 cases) and both values are open with no record of the corner present, forcing first appears with 2 of the cube's 6 corner records and 1 of the plaquette's 4, and each of the (2 z_v)! formation orders (720 and 24) reproduces the G_v = 0 set exactly, so the restriction on joint record patterns is a consequence of those site-level zeros and not a further primitive. (T3) With J^g_ij = -(t eta_ij/2)(K_ij X^L_ij - T_ij Y^L_ij) = (1/2)(J_ij X^L_ij + eta_ij t T_ij Y^L_ij), Hermitian on every bond: dn_v/dt = i[H^g, n_v] = -sum_w J^g_vw at every corner, dE_e/dt = i[H^g, E_e] = -J^g_e on every one of the 66 links, and d(div E)_v/dt = dn_v/dt at every corner; reversing a bond must reverse the link orientation too, X^L_e J^g_ji X^L_e = -J^g_ij, while J^g_ji = -J^g_ij alone fails on all 66 bonds; and E_e^2 = I/4 identically, so (g^2/2) sum_e E_e^2 is a c-number at spin 1/2. (T4) P_f = W_f + W_f^dag, the oriented four-link ring exchange around a coarse face, is Hermitian with exactly eight Pauli monomials on exactly the four link records of that face and no fermion record, [P_f, G_v] = 0 for all 48 face-corner pairs on the cube and 4 on the plaquette in both rho conventions, [P_f, S_f] = 0 and [P_f, prod_{e in f} Z^L_e] = 0, while [P_f, H^g] != 0 with 64 nonzero Pauli monomials on the cube face at (0,0,0). (T5) [numerical] On the 256-dimensional plaquette the Gauss sector has dimension 14 in the admissible staggered convention, 0 in the sea convention, and 7 intersected with the fermion code, where E_0 = -2.449489742783 = -sqrt 6 at lambda = 0 and -2.323404276086 at lambda = 1 with <P_f> = 1/6 and 0.094209746012, and max |<rho_v>| = 0.5833333333 and 0.6456532164, so that ground state is locally charged; on the cube the sea-convention Gauss sector is 14400 states of 2^24 on which H^g is sparse with 79872 nonzeros, its ground state lies in the code space at <S_f> = +1 with E_0 = -5.466823694822 at lambda = 0 and -6.980814328073 at lambda = 1, both at <N> = 4 = |V|/2, and <n_v> = 1/2, <rho_v> = 0 and <E_e> = 0 hold to 1e-13 at every one of the 8 corners and every one of the 12 links at both couplings. The link role and the link dynamics are designed, not derived; t, lambda and g are supplied data; the two rho conventions differ and that tension is carried here as an open item, not resolved; no gapless transverse mode of the link sector is shown, computed, or suggested, and no continuum limit is taken; no claim is made that this U(1) is electromagnetism. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/fermion_u1_quantum_links_gauss_law_support_condition_check_2026_09_03.py
---

# The fermion's `U(1)` coupled to quantum links: Gauss's law as a support condition among records

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/fermion_u1_quantum_links_gauss_law_support_condition_check_2026_09_03.py`](../scripts/fermion_u1_quantum_links_gauss_law_support_condition_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/fermion_u1_quantum_links_gauss_law_support_condition_check_2026_09_03.txt`](../logs/runner-cache/fermion_u1_quantum_links_gauss_law_support_condition_check_2026_09_03.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

PR #7892 gave the coarse-lattice emergent fermion a charge and a conserved bond current, and left one question open on its face: nothing in the declared law couples
to that `U(1)`. The question here is whether something can, inside the framework's readable algebra, and what Gauss's law is once it does. The answer needs one more
designed role -- a second site per coarse edge -- declared as designed, in exactly the sense PR #7834's role pattern is. What comes back is that the coupling is
exact, and that Gauss's law is a linear relation among the records at one corner, implemented by site-level forcing in any formation order: with the corner's other
records present, the value that would unbalance it carries zero odds where the last one forms. Which joint patterns occur is the consequence, not a further law.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems about one declared coupled law on the coarse-lattice emergent fermion carrying one designed spin-1/2 link role per coarse edge: the gauge-invariant hop and its two-monomial partner K_ij, Gauss's law as a record-diagonal corner relation with its exact joint record-pattern census and its coordination-parity condition, the coupled Ampere and continuity relations, and the four-link ring exchange. The symplectic Pauli statements are exact Gaussian-rational arithmetic on F2 supports with Z4 phases; the census statements are exact integer arithmetic over all 2^24 cube and 2^8 plaquette record patterns; the site-level forcing statements are exact enumeration over one corner's 2^(2 z_v) record assignments in every formation order; the tagged numerical items are floating-point cross-checks at the stated tolerance."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the design question this note does not decide: which link size the framework wants, given that spin-1/2 links carry a coordination-parity condition the bulk coarse lattice and the cube answer differently."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`F`. Groups `A`, `B`, `C`, `D` and `F` are exact --
Gaussian-rational coefficients on symplectic Pauli monomials, `F2` supports and `Z4` phases, complete sweeps, and integer record arithmetic, with no floating-point
step anywhere -- and the items tagged `[numerical]` in group `E` are floating-point cross-checks at the stated tolerance.

1. `T1` (`A`). The gauge-invariant hop, and `K_ij` as the two-monomial partner the encoding already contains.
2. `T2` (`B`, `F`). Gauss's law as a record-diagonal corner relation, its exact census, the coordination-parity condition on spin-1/2 links, and its implementation by
   site-level forcing in any formation order.
3. `T3` (`C`). Ampere, coupled continuity, and what bond reversal does to a link.
4. `T4` (`D`). The four-link ring exchange, and what it does and does not commute with.
5. `T5` (`E`). The coupled sea on the plaquette and on the cube's Gauss sector.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the quantum-link (gauge-magnet) presentation
with finite-dimensional link algebras, the ring-exchange plaquette term and the Pauling ice estimate are standard methodology; every object is redeclared here and
every statement recomputed by the runner. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, no grade and
no dependency weight:

- `CHARGE_CONJUGATION_AND_THE_CONSERVED_U1_CURRENT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7892): the charge `Q = -(1/2) sum_v B_v` and
  the bond current `J_ij = eta_ij (t/2) A_ij (I - B_i B_j)`. Its closing interface -- nothing couples to this `U(1)` -- is the question answered here.
- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the period-`(4,2,2)` superlattice
  role pattern and the coarse sublattice `2Z^3`. The link role declared here is a design element of exactly that kind.
- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): the staggered kinetic form and the KS signs.
- `THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7885) and
  `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7879): the vacuum
  coefficient and the half-filled sea at `<n_v> = 1/2`.
- `RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858): record formation on the vacuum and its parity cosets.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting", including the Admissibility reading note used to say what a support condition is.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has
algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" -- the law
supplies the odds. Reading note (3) fixes the vocabulary used below: "The distribution is a probability measure on the local possibility domain;
'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability." **Record**: "Records form", "a record locks
exactly one admissible local possibility", "records are permanent", "Only records are readable", and "A readout value is determined by record content alone."

The lattice is physical. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, and adds one further
designed role. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras, with no graded clause anywhere.

A **support condition** in this note means what reading note (3) licenses: a zero of the law-level odds at the site where a record forms, putting the value it
excludes outside the support of the distribution the law supplies there. It is no further dynamical clause, and no formation site, rate, or process word states it.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field
on it, the superfast encoding with its face stabilizers, the designed link role with its `E_e` and `U_e`, and the coupled law `H^g` with its supplied coefficients.
`P1` (`A`) is the gauge-invariant hop and `K_ij`; `P2` (`B`) Gauss's law, its census and the coordination-parity condition; `P3` (`C`) Ampere and continuity; `P4`
(`D`) the ring exchange; `P5` (`E`) the coupled sea; `P6` (`F`) the site-level forcing that implements `P2`. `P2` uses `P0` only; `P3` uses `P1`'s `K_ij`; `P4` uses
`P0`; `P5` and `P6` use `P2`. The strongest supported scope is precisely `P0`-`P6`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **KS
sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. The **encoding** is the Bravyi-Kitaev superfast
encoding on the coarse lattice, fermion code sites on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`. The **link role** is one further two-state site
per coarse edge, declared exactly as PR #7834's role pattern is declared: assigned by design, derived from nothing.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_v  = the product of the Z's at corner v = I - 2 n_v,   S_f = the ordered product of the four A's around a coarse face f
n_v  = (I - B_v)/2,   eps_v = (-1)^{v_1+v_2+v_3},   T_ij = (i/2) A_ij (B_i - B_j),   K_ij = -(1/2) A_ij (I - B_i B_j)
E_e  = (1/2) Z^L_e   (eigenvalues +-1/2),    U_e = (X^L_e + i Y^L_e)/2,    U_e^dag U_e + U_e U_e^dag = I
bond (v, e_a) is oriented i = v -> j = v + e_a;   s_{v,e} = +1 if e leaves v, -1 if e enters v
H^g = -t sum_<ij> eta_ij (T_ij X^L_ij + K_ij Y^L_ij)/2   +  lambda sum_f P_f  +  (g^2/2) sum_e E_e^2      THE DECLARED LAW
J^g_ij = -(t eta_ij / 2) (K_ij X^L_ij - T_ij Y^L_ij)                                       THE COUPLED BOND CURRENT
(div E)_v = sum_{e at v} s_{v,e} E_e,  rho_v^{sea} = n_v - 1/2,  rho_v^{stag} = n_v - (1 - eps_v)/2,  G_v = (div E)_v - rho_v
W_f = the oriented loop product of U (forward steps) and U^dag (backward steps) around a coarse face;  P_f = W_f + W_f^dag
```

The **coordination** `z_v` is the number of coarse edges at `v`: `3` on the open cube, `2` on the plaquette, `3` to `6` on the open `3x3x3` block, `6` in the bulk. A
**record pattern** is one assignment of a value to every record site; the record basis is the joint eigenbasis of the `Z`'s. An operator is **record-diagonal** when
it is diagonal in that basis, so that its value is fixed by record content alone. `t`, `lambda` and `g` are **supplied**.

## Theorem 1 -- the gauge-invariant hop, and the partner the encoding already contains

**Conclusion.** (1) Writing `a_i^dag a_j = (T_ij - i K_ij)/2`, the minimally coupled hop is exact: `a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i = (T_ij X^L_ij + K_ij
Y^L_ij)/2`, Hermitian, exactly four Pauli monomials, on all `66` bonds of the `2x2x2` cube and the open `3x3x3` block. (2) `K_ij = -(1/2) A_ij (I - B_i B_j)` is
Hermitian with `K_ji = -K_ij` and is **exactly two Pauli monomials**, on the same site support as `T_ij` -- `5` sites on the cube, `6`, `8` or `10` on the open
`3x3x3` block. (3) `K_ij = -i [T_ij, n_i]`, so given the hop `K` is fixed by the fermion algebra and is not a further choice. (4) `{T_ij, K_ij} = 0` and `[T_ij,
K_ij] = -2i (n_i - n_j) = i (B_i - B_j)`: `T`, `K` and `n_i - n_j` close an `su(2)` on every bond. (5) `J_ij` of PR #7892 `= -eta_ij t K_ij` on every bond -- one
factor of `t`, sign **minus**, and not `eta_ij (t/2) K_ij`.

**Proof.** Item 1 builds `a_i^dag a_j` and `a_j^dag a_i` from `T` and `K`, multiplies by the raising and lowering monomials of the link site, and compares key by key
against the four-monomial right-hand side. Items 2 to 5 are `F2` support arithmetic with `Z4` phases on Gaussian-rational coefficients: monomial counts, supports,
commutators and anticommutators compared to zero exactly. All exact, complete over both blocks.

**Reading, not theorem.** The hop already came in two pieces, one even and one odd under exchanging the two corners. Giving each edge its own record supplies what the
odd piece needs -- something that can change when the particle passes -- and the pairing is forced, not fitted: that odd piece is the current PR #7892 already named.

## Theorem 2 -- Gauss's law is a support condition among records

**Conclusion.** (1) Every `G_v = (div E)_v - rho_v` is a **pure `Z` operator**, record-diagonal on the `2 z_v` records at one corner: six on the cube -- three fermion
edge records and three link records -- and twelve at the interior corner of the `3x3x3` block. Explicitly at the cube corner `(0,0,0)`, `G_v^{sea} = (1/2)(Z_{f0}
Z_{f1} Z_{f2} + Z_{L0} + Z_{L1} + Z_{L2})`, four monomials. (2) `[G_v, G_w] = 0` for all `64 + 729` corner pairs and `[G_v, H^g] = 0` at every corner, in both `rho`
conventions; and `sum_v G_v = -sum_v rho_v`, which in the sea convention reads `sum_v G_v = -Q`. (3) **The coordination-parity condition.** `2 (div E)_v` is a sum of
`z_v` terms `+-1` and so carries the parity of `z_v`, while `2 rho^{sea} = 2 n_v - 1` is odd and `2 rho^{stag} = 2 n_v - (1 - eps_v)` is even: with spin-1/2 links
`G_v = 0` is solvable at `v` only for `rho^{sea}` at odd `z_v`, and only for `rho^{stag}` at even `z_v`. By exact census the cube (`z = 3`) has `14400` joint record
patterns of `2^24` in the sea convention and `0` in the staggered one; the plaquette (`z = 2`) has `0` and `14`. (4) On the cube, exactly `2240` of the `4096`
fermion record patterns admit at least one link pattern, and they are **precisely the half-filled `N = 4` sector, all of it**; the link-pattern multiplicities are
`192 x 4`, `1024 x 6`, `768 x 7`, `192 x 8`, `64 x 9`, summing to `14400`. (5) Every nontrivial face-loop product carries `X` and so has zero diagonal, hence
`dim(Gauss and code) = 14400/2^5 = 450` on the cube and `14/2^1 = 7` on the plaquette.

**Proof.** Item 1 is monomial arithmetic: `n_v` is a corner parity of fermion edge records, `E_e` is one link record, and the sum of pure `Z` terms is pure `Z`.
Item 2 is symplectic-form arithmetic against the four-monomial hop on every bond, plus a term-by-term cancellation of each link's two incidences in the sum. Item 3
is the handshake parity of `z_v` terms `+-1` against the parity of `2 rho_v`, confirmed by complete vectorised integer enumeration of all `2^24` and `2^8` joint
record patterns. Item 4 is the same enumeration read per fermion pattern; the restriction to `N = |V|/2` is already forced by item 2's `sum_v G_v = -Q`, and the
census shows it is also sufficient. Item 5 is `F2` support arithmetic over the `2^5` and `2^1` face-loop products. All exact.

### Reading of "support condition", refereed

A referee objected that item 1 is claimed at the wrong level, and the objection stands. The Admissibility axiom supplies, for each site, a probability distribution
over that site's possibilities given its neighbours' conditions, and reading note (3) reads "admissible" as that distribution's support. A normalised conditional
cannot assign zero odds to its own conditioning event, so a joint constraint on a whole neighbourhood's records is not, by itself, a support condition at any one
site: nothing forbids a neighbourhood's configuration from a single site.

`G_v = 0` is instead a **linear relation among the corner's `2 z_v` records** -- `sum_e s_{v,e} E_e = rho_v` -- and a linear relation is implemented by site-level
support conditions in **any** formation order: whenever all but one of its records are present, the last record's odds for the violating value are zero, a support
condition at that site of the axiom's kind. PR #7858 exhibits this for the corner parities: a coset, odds `1/2` or forced, forcing by cocircuits, order-independent.

So "support condition among records" means that site-level forcing, and the restriction on the joint domain -- only balanced corner configurations occur -- is its
**consequence**, not a further primitive. Group `F` checks this on the cube (sea) and the plaquette (staggered): every occurring assignment of all but one of a
corner's records forces the last, `1248` cases (`F1`); no occurring record set leaves an absent record with no admissible value, `11432` cases, and with none present
both values are open (`F2`); each of the `(2 z_v)!` orders, `720` and `24`, reproduces the `G_v = 0` set exactly (`F3`). Forcing is not confined to the all-but-one
case -- it first appears at `2` of the cube's `6` records and `1` of the plaquette's `4` -- but each is still a zero of the odds at one site, never a joint veto.

**Reading, not theorem.** At each corner the law says one thing about the records there: the flux records on the edges meeting at that corner, counted with the
direction they point, must balance the matter record there, one record at a time. On the cube that single condition already picks out the half-filled patterns and no
others, the same population the vacuum work reached from the energy side.

## Theorem 3 -- Ampere, coupled continuity, and what reversing a bond does

**Conclusion.** With `J^g_ij = -(t eta_ij/2)(K_ij X^L_ij - T_ij Y^L_ij)`, Hermitian on every bond: (1) `dn_v/dt = i[H^g, n_v] = -sum_w J^g_vw` at every corner of both
blocks. (2) `dE_e/dt = i[H^g, E_e] = -J^g_e` on every one of the `66` links, `e` oriented tail to head. (3) `d(div E)_v/dt = dn_v/dt` at every corner. (4)
`J^g_ij = (1/2)(J_ij X^L_ij + eta_ij t T_ij Y^L_ij)`: the `X^L` part of the coupled current **is** the uncoupled current of PR #7892. (5) Reversing a bond must
reverse the link orientation with it -- `X^L_e J^g_ji X^L_e = -J^g_ij` -- while `J^g_ji = -J^g_ij` alone fails on all `66` bonds. (6) `E_e^2 = I/4` identically, so
`(g^2/2) sum_e E_e^2` is a c-number: at spin `1/2` the electric term supplies no dynamics at all.

**Proof.** Items 1 to 4 expand `i[H^g, .]` as Pauli sums with Gaussian-rational coefficients and compare key by key against the stated right-hand sides, on every
corner and every link of both blocks. Item 5 conjugates by the link monomial and compares; the failure of the bare relation is the same comparison returning a
nonzero residual on each bond. Item 6 is one monomial squared. All exact. Item 3 is Theorem 2 item 2 written as a rate.

**Reading, not theorem.** The record on a link answers to exactly one thing: the current through its own edge. The two halves of the corner condition change together,
so a satisfying pattern keeps satisfying it. One caution: a link record points one way along its edge, so reading the bond backwards reads the link backwards too.

## Theorem 4 -- the ring exchange, and what it leaves alone

**Conclusion.** `P_f = W_f + W_f^dag`, the oriented four-link ring exchange around a coarse face, is (1) Hermitian with **exactly eight Pauli monomials** on exactly
the **four link records** of that face and no fermion record; (2) `[P_f, G_v] = 0` for all `48` face-corner pairs on the cube and `4` on the plaquette, in both `rho`
conventions; (3) `[P_f, S_f] = 0` and `[P_f, prod_{e in f} Z^L_e] = 0`, so the fermion code is untouched and the `Z2` remnant of the face flux is a record-diagonal
constant of the ring exchange; and (4) `[P_f, H^g] != 0` -- on the cube face at `(0,0,0)` the commutator carries `64` nonzero Pauli monomials.

**Proof.** Expansion of the four-factor loop product into monomials, then symplectic-form arithmetic for each commutator, over every face of both blocks and both
`rho` conventions. All exact.

**Reading, not theorem.** The link records need a term of their own to have any life, because the obvious candidate -- the cost of the flux itself -- is a constant at
this link size. The one that does it acts on the four links of a face at once: a neighbourhood term, not a nearest-neighbour one, and as designed as the link role.

## Theorem 5 -- the coupled sea

**Conclusion.** (1) On the `256`-dimensional plaquette the Gauss sector has dimension `14` in the admissible staggered convention, `0` in the sea convention, and `7`
intersected with the fermion code. (2) There `E_0 = -2.449489742783 = -sqrt 6` at `lambda = 0` and `-2.323404276086` at `lambda = 1`, with `<P_f> = 0.166666666667 =
1/6` and `0.094209746012`. (3) That plaquette ground state is **locally charged**: `max |<rho_v>| = 0.5833333333` and `0.6456532164`, the total charge vanishing only
in the sum. (4) On the cube the sea-convention Gauss sector is `14400` states of `2^24`, on which `H^g` is sparse with `79872` nonzeros and Hermitian at `0`; the
ground state lies in the code space at `<S_f> = +1`, with `E_0 = -5.466823694822` at `lambda = 0` and `-6.980814328073` at `lambda = 1`, both at `<N> = 4 = |V|/2`.
(5) There `<n_v> = 1/2`, `<rho_v> = 0` and `<E_e> = 0` to `1e-13` at every one of the `8` corners and every one of the `12` links, at both couplings: **the coupled
sea is neutral with zero mean flux**.

**Proof.** The plaquette is diagonalised densely on `256` dimensions, projected first onto the joint kernel of the four `G_v` and then onto the `+1` eigenspace of
the face stabilizer. The cube's Gauss sector is built by vectorised bit arithmetic on the `2^24` joint record patterns and carried as a sparse `14400 x 14400`
operator; `-5 sum_f S_f` places the code space lowest and Lanczos returns the ground state there. `[numerical, 1e-12]` for items 1 to 3 and `[numerical, 1e-10]` for
items 4 and 5, the neutrality residuals at `1e-13`. No dense object above `14400` rows and no dense `2^24` object is formed anywhere.

**Reading, not theorem.** With the links coupled, the half-filled sea stays exactly half filled, carries no charge at any corner, and no net flux on any link. That is
stronger than the uncoupled statement: the corner condition could have forced flux into the ground state, and on the plaquette it does exactly that.

## Corollary -- what the coupling buys, and what it costs

Within the setting declared above, and on the finite blocks named:

1. **An exactly gauge-invariant minimal coupling exists.** The emergent fermion's conserved `U(1)` couples to a designed spin-1/2 link role with no residual: the
   coupled hop is four Pauli monomials, and the partner it needs was already inside the encoding as `-i[T_ij, n_i]`.
2. **Gauss's law is implemented by site-level forcing in any formation order.** `G_v` is record-diagonal on the `2 z_v` records at one corner and `G_v = 0` is a
   linear relation among them, so a value that relation cannot rescue, given the corner records present, is a zero of the odds **at the site where that record
   forms**. The joint restriction -- on the cube, exactly the half-filled sector -- follows from those zeros and their order-independence; it is not imposed on a
   neighbourhood.
3. **What registers and what does not.** The electric flux `E_e` is a one-record value on a link site, readable; so are `n_v`, `rho_v`, `(div E)_v`, `G_v`, `Q` and
   the `Z2` face flux. The coupled hop, the current `J^g_ij`, the link raising `U_e` and the ring exchange `P_f` carry `X` in every monomial and so have no
   record-diagonal part at all: they register only through correlations among records. This is PR #7892's pattern, extended to the link sector.
4. **The cost is a coordination-parity condition.** Spin-1/2 links admit `rho^{sea}` only at odd `z_v` and `rho^{stag}` only at even `z_v`: on `2Z^3` proper (`z = 6`)
   the staggered background half-charge, on the cube (`z = 3`) the sea convention. **This note declares that tension and does not resolve it.**
5. **The coupled sea is neutral with zero mean flux** on the cube, at both values of the ring-exchange coefficient computed.

**Reading, not theorem (this register).** Give every link between two corners its own record, read as a unit of flux pointing one way or the other. Gauss's law then
says only this: at each corner, the flux records in and out must balance the matter record there. It bites one record at a time -- with the rest of a corner already
written down, the value that would unbalance it cannot be the one that forms. With that rule in place the matter's charge can flow along the links, the flux records
change exactly as the current says, and the half-filled sea is neutral with no net flux anywhere.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign field, **the link role** and the coupled law are declared objects, and no
  coefficient is derived: `t`, `lambda` and `g` are supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears.
- No continuum limit is taken, no second species appears, and no gapless transverse mode of the link sector is shown, computed, or suggested.

## Interfaces named for other lanes, not moved here

- **Whether the link sector carries light.** Whether the ring-exchange link sector has a gapless transverse mode -- a photon -- is **not** decided here. The smallest
  test with a plausible one is the `4^3` coarse torus (`64` corners, `192` links, `z = 6`), whose pure-link Gauss sector is about `2.5^64 = 2.9 x 10^25` states by the
  Pauling ice estimate -- beyond exact diagonalisation and beyond matrix-free Lanczos. Sampling or a variational ansatz on the ice manifold is what it would cost.
- **Larger links.** Spin-1 or larger link algebras lift the coordination-parity condition of Theorem 2 item 3 and make the electric term of Theorem 3 item 6
  non-trivial. Neither is treated here, and which link size the framework wants is a design question for the lane that owns the role rule.
- **The ring-exchange coefficient.** `lambda` is supplied. What fixes it, if anything does, is not addressed.
- **The fine-lattice role assignment.** The link role is declared on the coarse edge; writing it as a rule on `Z^3`, the way PR #7834 does, is not done here.
- **The continuum.** Everything here is a lattice operator; no continuum limit is shown, and this `U(1)` is not claimed to be electromagnetism.

## Remaining live routes

1. The convention question of Corollary 4, on a region large enough to carry both parities at once, or with a larger link algebra.
2. Larger blocks. The open `2x2x2` cube, the open `3x3x3` block and the single `2x2x1` plaquette are what is proved; nothing is claimed beyond them.
3. Correlations of the coupled current and of the link raising, which Theorem 5 shows are where these objects register at all.
4. The `Z2` remnant of the face flux: readable by Theorem 4 item 3, but not a constant of `H^g`. What it does under the coupled law is not computed.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one fermionic mode per coarse vertex, BK superfast encoding, plus ONE DESIGNED spin-1/2 link role per coarse edge (declared, of the same kind as PR #7834's role pattern); ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md; H^g declared here with supplied t, lambda, g
blocks: open 2x2x2 cube (8 corners, 12 + 12 records), open 3x3x3 block (27 corners, 54 + 54 records), single 2x2x1 plaquette (4 corners, 4 + 4 records)
hop: a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i = (T_ij X^L_ij + K_ij Y^L_ij)/2 exactly, Hermitian, 4 Pauli monomials, on all 66 bonds
K: K_ij = -(1/2) A_ij (I - B_i B_j), Hermitian, K_ji = -K_ij, exactly 2 monomials, support = supp(T_ij) = 5 (cube), 6/8/10 (open 3x3x3); K_ij = -i [T_ij, n_i]
su2: {T_ij, K_ij} = 0 and [T_ij, K_ij] = -2i (n_i - n_j) = i (B_i - B_j) on every bond
current_relation: J_ij (PR #7892) = -eta_ij t K_ij on every bond -- one factor of t, sign minus, NOT eta (t/2) K_ij
gauss: G_v = (div E)_v - rho_v is pure Z on the 2 z_v records at one corner (6 on the cube, 12 at the 3x3x3 interior corner); [G_v, G_w] = 0 (64 + 729 pairs); [G_v, H^g] = 0 at every corner; sum_v G_v = -sum_v rho_v = -Q in the sea convention
parity_condition: 2 (div E)_v carries the parity of z_v; 2 rho^sea odd, 2 rho^stag even; spin-1/2 links admit rho^sea only at odd z_v and rho^stag only at even z_v
census: cube z = 3: 14400 joint record patterns of 2^24 (sea) and 0 (stag); plaquette z = 2: 0 and 14; 2240 of 4096 cube fermion patterns admissible = exactly the N = 4 sector; multiplicities 192 x 4, 1024 x 6, 768 x 7, 192 x 8, 64 x 9; dim(Gauss and code) = 450 and 7
site_forcing: G_v = 0 is a linear relation among the corner's 2 z_v records, implemented by site-level forcing in ANY formation order -- cube (sea) and plaquette (stag): every occurring assignment of all but one of a corner's records leaves exactly 1 admissible value for the last (1248 events, all forced); no occurring record set leaves an absent record with an empty admissible set (11432 cases), both values open with none present; forcing first appears at 2 of the cube's 6 corner records and 1 of the plaquette's 4; each of the (2 z_v)! orders (720, 24) reproduces the G_v = 0 set exactly, so the JOINT restriction is a consequence, not a primitive
ampere: dE_e/dt = -J^g_e on all 66 links; dn_v/dt = -sum_w J^g_vw at every corner; d(div E)_v/dt = dn_v/dt; J^g_ij = (1/2)(J_ij X^L + eta t T_ij Y^L); X^L_e J^g_ji X^L_e = -J^g_ij while J^g_ji = -J^g_ij alone fails on 66 of 66 bonds; E_e^2 = I/4 identically
ring_exchange: P_f Hermitian, 8 Pauli monomials, exactly the 4 link records of one face, no fermion record; [P_f, G_v] = 0 (48 pairs cube, 4 plaquette, both conventions); [P_f, S_f] = [P_f, prod Z^L] = 0; [P_f, H^g] != 0 with 64 nonzero monomials on the cube face at (0,0,0)
plaquette_numerics: Gauss dim 14 (stag) / 0 (sea), Gauss and code 7; E_0 = -2.449489742783 = -sqrt 6 (lambda 0) and -2.323404276086 (lambda 1); <P_f> = 1/6 and 0.094209746012; max |<rho_v>| = 0.5833333333 and 0.6456532164 -- locally charged
cube_numerics: Gauss sector 14400 of 2^24, sparse, 79872 nonzeros; ground state in the code space at <S_f> = +1; E_0 = -5.466823694822 (lambda 0) and -6.980814328073 (lambda 1); <N> = 4 = |V|/2; <n_v> = 1/2, <rho_v> = 0, <E_e> = 0 to 1e-13 at every corner and link
not_shown: no gapless transverse mode of the link sector; smallest test is the 4^3 pure-link Gauss sector at ~2.9 x 10^25 states (Pauling estimate), beyond exact diagonalisation and beyond matrix-free Lanczos
open_item: the sea and staggered conventions differ; the bulk (z = 6) admits only the staggered background half-charge while the cube (z = 3) admits only the sea convention; declared, not resolved
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=31 FAIL=0
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3`, on three named finite blocks: the open `2x2x2` cube, the open `3x3x3` block, and the single `2x2x1` plaquette.
Nothing is claimed for `Z^3`, for a torus, or for any larger region. The bulk statement of the coordination-parity condition is a parity count on `z_v = 6`, not a
computation on a bulk region.

The **link role is designed**, exactly as PR #7834's superlattice role pattern is designed: one further two-state site per coarse edge, assigned by a design rule and
derived from no axiom. The **link dynamics is declared**: `H^g`, `P_f` and `(g^2/2) sum_e E_e^2` are supplied laws with supplied `t`, `lambda` and `g`. `P_f` is a
four-link neighbourhood term inside one coarse face, not a nearest-neighbour term, and the electric term is a c-number at spin `1/2` and does nothing. Nothing in
this note is derived from any axiom; the axioms are quoted to fix what "readable" and "admissible" mean, and for nothing else.

**No photon.** No gapless transverse mode is shown, computed, or suggested. The result is not that electromagnetism appears; it is that one designed coupling exists,
exactly, with its Gauss law implemented by site-level forcing in any formation order.

**The convention tension is carried, not resolved.** The convention that makes the sea locally neutral (`rho = n_v - 1/2`) and the one spin-1/2 links admit in the
bulk (`rho = n_v - (1 - eps_v)/2`) are different; settling that needs a larger region carrying both coordination parities, or a larger link algebra.

## Review record

An honest auditor should come away with: one declared coupled law on named finite blocks, in which the emergent fermion's conserved `U(1)` acquires an exact
gauge-invariant minimal coupling to one designed spin-1/2 link role per coarse edge -- four Pauli monomials per bond, with the partner `K_ij` fixed by the fermion
algebra and equal to the landed current up to `-eta_ij t` -- and in which Gauss's law is a pure `Z` linear relation among the `2 z_v` records at a single corner,
implemented in any order by site-level forcing of the record that forms last: a support condition in the axioms' own vocabulary at the site, the joint restriction its
consequence. Its solution set on the cube is exactly the half-filled sector at `14400` patterns of `2^24`. The costs: the link role and its dynamics are designed, not
derived; spin-1/2 links carry a coordination-parity condition the bulk lattice and the cube answer differently; and whether the link sector carries light is
untouched.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the six context notes in
"Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at
`PASS=31 FAIL=0`, runtime under the declared `120` seconds, stdout under `7000` characters, and passing pipeline, strict-lint and changed-evidence gates; independent
audit remains a separate lane.
