---
claim_id: fermion_compact_u1_links_staggered_gauss_law_maxwell_germ_join
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3 carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}, and with ONE FURTHER DESIGNED ROLE per coarse edge -- a COMPACT U(1) link role carrying E_e |m> = m |m> with m integer, U_e |m> = |m + 1>, [E_e, U_e] = U_e, truncated to |m| <= S with S = 1 and S = 2, declared as a design element of exactly the same kind as the period-(4,2,2) superlattice role pattern of PR #7834 and derived from no axiom -- for the ONE DECLARED law H^g = -t sum_<ij> eta_ij (T_ij C_e + K_ij S_e)/2 with C_e = U_e + U_e^dag and S_e = -i(U_e - U_e^dag), plus H_E = (g^2/2) sum_e E_e^2 and H_B = -(1/g^2) sum_f cos_f with cos_f = (W_f + W_f^dag)/2, whose coefficients t and g are supplied and are fixed by nothing quoted here, and on the named finite blocks only -- the single coarse 2x2x1 plaquette, the open 2x2x2 cube, the open 3x3x3 block, the 2x2x3 block, and the periodic rings of L = 4 and L = 8 corners: (T1) writing a_i^dag a_j = (T_ij - i K_ij)/2, the minimally coupled hop a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i equals (T_ij C_e + K_ij S_e)/2 exactly, Hermitian, with 16 Pauli-monomial entries at S = 1 and 32 at S = 2, on all 140 bond checks -- every bond of the plaquette, the cube and the open 3x3x3 block at S = 1 and S = 2 -- while the opposite-sign partner +i(U_e - U_e^dag) fails on every one of them and is a_i^dag U_ij^dag a_j + h.c.; at spin 1/2 this reduces to PR #7893's landed (T_ij X^L_ij + K_ij Y^L_ij)/2 since U = (X^L + i Y^L)/2 gives C = X^L and S = Y^L; the partner relations [n_i, T] = -iK, [n_i, K] = +iT, [n_j, T] = +iK, [n_j, K] = -iT and [n_w, T] = [n_w, K] = 0 off the bond hold on all 12 cube bonds and all 96 off-bond corner-bond pairs; truncation is exact for [E_e, U_e] = U_e and [E_e, U_e^dag] = -U_e^dag and breaks exactly two things, U_e^dag U_e = I - P_{+S} with U_e U_e^dag = I - P_{-S} and [C_e, S_e] = 2i (P_{+S} - P_{-S}) != 0; and [G_v, H^g] = 0 with G_v = (div E)_v - rho_v at every corner of every coordination z_v = 2, 3, 4, 5, 6 -- 1570 corner-bond pairs over the three blocks -- in both rho conventions and at S = 1 and S = 2. (T2) With integer-valued E_e, 2 (div E)_v is EVEN at every corner of every coordination, while 2 rho^{sea}_v = 2 n_v - 1 is odd and 2 rho^{stag}_v = 2 n_v - (1 - eps_v) is even, so G_v = 0 is unsolvable for rho^{sea} and solvable for rho^{stag} independently of z_v: the coordination-parity condition PR #7893 declared is absent and what replaces it is a coordination-independent selection of the staggered background half-charge. By exact census, computed by dynamic programming and cross-checked by complete enumeration, the Gauss sector is 0 and 26 at S = 1 and 0 and 50 at S = 2 on the plaquette, 0 and 102304 at S = 1 and 0 and 1477920 at S = 2 on the cube, and 0 and 234 on the L = 8 ring; exactly 2240 of the 4096 cube fermion record patterns admit a link configuration and they are precisely the half-filled N = 4 sector, all of it, in eight multiplicity classes of sizes 128, 192, 416, 768, 128, 192, 384, 32 identical at S = 1 and S = 2; dim(Gauss and code) = 13 and 25 on the plaquette; the same census run on PR #7893's spin-1/2 link returns 14400 in the SEA convention and 0 in the staggered one on the cube and 0 and 14 on the plaquette; and rho^{sea} = rho^{stag} - eps_v/2, so the two conventions are one law in shifted variables exactly when a fixed background link field c_e with (div c)_v = -eps_v/2 exists, which it does with c_e in {-1/2, 0, +1/2} on the balanced plaquette, cube and 2x2x3 block and does not on the open 3x3x3 block, whose 14 and 13 corners give sum_v (-eps_v) = -1 while any divergence sums to zero. (T3) E_e^2 has spectrum {0, 1} at S = 1 and {0, 1, 4} at S = 2, so H_E is a genuine operator and not the c-number it is at spin 1/2 where E_e^2 = I/4; [P_f, G_v] = 0 on all 52 face-corner pairs -- 48 on the cube and 4 on the plaquette -- at S = 1 and S = 2, with nnz(P_f) = 32 and 512; the assembled H^g + H_E + H_B applied to every Gauss basis state of the plaquette with destinations computed in the full space produces 0 out-of-sector amplitudes and maximum leaked amplitude 0.0e+00 at both S; and H_B is, up to an additive constant, the one-plaquette Wilson potential V(theta) = (1/g^2)(1 - cos theta), even, 2 pi-periodic, C^infinity, with V(0) = V'(0) = 0 and V''(0) = 1/g^2 > 0, the positive isotropic quadratic germ the open PR #7884 states for its quadratic basin. (T4) [numerical] On the plaquette in the staggered convention, the only admissible one, at Gauss dimensions 26 and 50: E_0 at g^2 = 1, 2, 4 without and with H_B is -2.152012, -2.491848, -1.807851, -1.889263, -1.352280, -1.364473 at S = 1 and -2.153357, -2.573395, -1.807956, -1.899006, -1.352283, -1.365185 at S = 2 to 1e-9; without H_B the gap and <cos_f> vanish at every g^2 and both S, and with H_B the gaps are 0.395359, 0.110635, 0.017047 and 0.411731, 0.114075, 0.017220 with <cos_f> = 0.418515, 0.210243, 0.063343 and 0.541713, 0.244706, 0.068693; <E_e^2> at S = 1 is 0.205293, 0.145868, 0.089108 without H_B and 0.289139, 0.168525, 0.091811 with it to 1e-6; and <rho_v> = +0.180762247, -0.180762247, -0.180762247, +0.180762247 at g^2 = 4 with H_B at S = 2, so the coupled sea is NOT locally neutral -- the block's C_4 symmetry fixes the pattern +a, -a, -a, +a and hence the vanishing total, not the value a, whose maximum is 0.426, 0.305, 0.181 at g^2 = 1, 2, 4 at S = 1 -- with <N> = 2 at half filling and Hermiticity residual 0.0e+00. (T5) The superfast ring encoding realises only even total fermion number at L = 4, 6 and 8 while half filling needs N = L/2, so L = 0 mod 4 is required and L = 6 has an empty Gauss sector. [exact] With static charges +1 and -1 at separation d and no fermion, V(d) = (g^2/2) d exactly in rational arithmetic for d = 0..4 at g^2 = 1 and g^2 = 4 on the L = 8 ring at S = 1. [numerical] With the fermion hop at t = 1 and half filling the string breaks: at g^2 = 4 the potential is 2.271563, 2.383425, 4.295402, 2.819090 against the unbroken 2, 4, 6, 8 and is not monotone, at Gauss dimensions 234, 150, 160, 132, 150 and <N> = 4 at every separation; at d = 4 and g^2 = 4 the flux localises on the sources with sum_e |<E_e>| = 1.603 against 4 for an unbroken string, dying to 0.0094 three links away, and the screening charge shows as a hole <n> = 0.181 at the +1 source and a fermion <n> = 0.981 at the -1 source; the L = 4 ring gives V = 0.762517, 0.594051 at g^2 = 1 and 2.271118, 2.169659 at g^2 = 4, saturated there too. The link role and the link dynamics are designed, not derived; an integer flux record needs log2(2S+1) bits and so needs a collective role of several physical sites, which this note does not settle; t and g are supplied data; every numerical item is at S = 1 or S = 2 and is not the untruncated theory; no gapless transverse mode of the link sector is shown, computed, or suggested, and no photon appears anywhere in this note; no continuum limit is taken; no claim is made that this U(1) is electromagnetism. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/fermion_compact_u1_links_staggered_gauss_law_join_check_2026_09_03.py
---

# The fermion on compact `U(1)` links: the integer flux selects the staggered Gauss law, and joins the Maxwell germ

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/fermion_compact_u1_links_staggered_gauss_law_join_check_2026_09_03.py`](../scripts/fermion_compact_u1_links_staggered_gauss_law_join_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/fermion_compact_u1_links_staggered_gauss_law_join_check_2026_09_03.txt`](../logs/runner-cache/fermion_compact_u1_links_staggered_gauss_law_join_check_2026_09_03.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

PR #7893 coupled the coarse-lattice emergent fermion's `U(1)` to one designed spin-1/2 link role per coarse edge, and left two things on its face: an electric term that was a c-number at that link size, and a
coordination-parity condition that made the charge convention depend on how many neighbours a corner has, declared as an open tension. Its own interface named the way out -- a larger link algebra. A sister
lane, open at PR #7884, was already carrying the compact `U(1)` connection the other half of the picture needs, with charged sources explicitly outside its claim. The question here is the join: does the
fermion's charge couple to a compact `U(1)` link exactly, what is Gauss's law once it does, and what does putting the two halves together give. The answer is that the coupling is exact at every coordination,
that the integer flux removes the parity condition and selects the staggered background half-charge everywhere instead, and that the resulting magnetic term sits at the centre of the sister lane's quadratic
basin. No photon is shown here.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems about one declared law on the coarse-lattice emergent fermion carrying one designed COMPACT U(1) link role per coarse edge: the gauge-invariant minimal coupling and what truncation preserves and breaks, the parity statement that makes the staggered convention the admissible one at every coordination, the exact Gauss-sector census by two independent methods, the electric and magnetic terms with the Wilson germ, and the ring's static potential. The symplectic Pauli statements are exact Gaussian-rational arithmetic on F2 supports with Z4 phases tensored with exact integer link matrices; the census statements are exact integer arithmetic by dynamic programming cross-checked by complete enumeration; the tagged numerical items are floating-point at the stated tolerance."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the design question this note does not decide: an integer flux record needs a collective role of several physical sites per coarse edge, and whether the staggered background half-charge is a registered pattern or supplied data is not settled here."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `C` and item `E2` are exact -- Gaussian-rational coefficients on symplectic Pauli
monomials (`F2` supports, `Z4` phases) tensored with exact integer link matrices, and exact integer record arithmetic, with no floating-point step anywhere -- and the items tagged `[numerical]` are
floating-point cross-checks at the stated tolerance.

1. `T1` (`A`). The minimally coupled hop on a compact `U(1)` link, what truncation costs, and gauge invariance at every coordination. `T2` (`B`). The integer flux selects the staggered convention everywhere,
   with the exact census and the background field that relates the two conventions on balanced blocks. `T3` (`C`). The electric term is dynamical, the Wilson term respects Gauss's law, and its germ is the
   sister lane's. `T4` (`D`). The plaquette in its Gauss sector. `T5` (`E`). The ring: exact linear confinement, and string breaking when the fermion is present.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the compact `U(1)` rotor with truncated integer flux, the Wilson plaquette term and the
Kogut-Susskind Hamiltonian presentation are standard methodology; every object is redeclared here and every statement recomputed by the runner. No observational value, no fitted number and no framework
premise enters any proof. Non-load-bearing pointers, no grade and no dependency weight:

- `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7893): the spin-1/2 link role, the coupled hop `(T_ij X^L_ij + K_ij
  Y^L_ij)/2`, the coordination-parity condition declared as an open tension, and the refereed reading of "support condition" used below. Its named interface -- a larger link algebra -- is what this note takes
  up.
- `COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7884): the compact `U(1)` carrier and its quadratic-basin statement, quoted in Theorem 3. An open
  sister-lane pointer, carrying no authority and no grade here.
- `A_HIERARCHY_OF_NEIGHBOURHOOD_CONDITIONS_GLUED_BREAKABLE_AND_FREE_RECORD_GROUPS_UNDER_SHIFTING_TICKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7899): the glued, breakable and free levels of a
  neighbourhood condition; Theorem 5 exhibits the breakable level on a ring.
- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the period-`(4,2,2)` superlattice role pattern and the coarse sublattice
  `2Z^3`; the link role declared here is a design element of exactly that kind.
- `CHARGE_CONJUGATION_AND_THE_CONSERVED_U1_CURRENT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7892): the charge and the bond current the link couples to, and
  `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting", with the Admissibility reading note used to say what a support condition is.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations
about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed
nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies
with, the nearest-neighbor conditions" -- the law supplies the odds. Reading note (3) fixes the vocabulary used below: "The distribution is a probability measure on the local possibility domain;
'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability." **Record**: "Records form", "a record locks exactly one admissible local possibility",
"records are permanent", "Only records are readable", and "A readout value is determined by record content alone."

The lattice is physical. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, and replaces PR #7893's spin-1/2 link role by a compact `U(1)`
one. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras, with no graded clause anywhere.

A **support condition** in this note means what reading note (3) licenses and what PR #7893's refereed reading fixes: a zero of the law-level odds at the site where a record forms, putting the value it
excludes outside the support of the distribution the law supplies there. `G_v = 0` is a linear relation among the records at one corner, and a linear relation is implemented by site-level forcing in **any**
formation order -- whenever all but one of its records are present, the last record's odds for the violating value are zero. The restriction on joint record patterns counted in Theorem 2 is the
**consequence** of those site-level zeros, not a further primitive, and no formation site, rate, or process word states it.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field on it, the superfast encoding, the designed
compact `U(1)` link role with its `E_e` and `U_e`, and the declared `H^g`, `H_E` and `H_B` with their supplied coefficients. `P1` (`A`) is the coupling and its gauge invariance, `P2` (`B`) the parity
statement and the census, `P3` (`C`) the electric and magnetic terms, `P4` (`D`) the plaquette Gauss sector and `P5` (`E`) the ring; `P1` and `P2` use `P0`, `P3` uses `P1`, and `P4` and `P5` use `P2` and
`P3`. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **KS sign** of the coarse bond `(v, v + e_a)`
is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, fermion code sites on the coarse edges, direction order
`-x < -y < -z < +x < +y < +z`. The **link role** is one further role per coarse edge, declared exactly as PR #7834's superlattice role pattern is declared: assigned by design, derived from nothing.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_v  = the product of the Z's at corner v = I - 2 n_v,   S_f = the ordered product of the four A's around a coarse face
n_v  = (I - B_v)/2,   eps_v = (-1)^{v_1+v_2+v_3},   T_ij = (i/2) A_ij (B_i - B_j),   K_ij = -(1/2) A_ij (I - B_i B_j)
E_e |m> = m |m>, m integer, truncated to |m| <= S ;  U_e |m> = |m+1>  (U_e |S> = 0) ;   [E_e, U_e] = U_e   EXACTLY
C_e = U_e + U_e^dag        S_e = -i (U_e - U_e^dag)        both Hermitian        W_f = the oriented four-link loop product
bond (v, e_a) is oriented i = v -> j = v + e_a ;   s_{v,e} = +1 if e leaves v, -1 if e enters v
H^g = -t sum_<ij> eta_ij (T_ij C_e + K_ij S_e)/2      H_E = (g^2/2) sum_e E_e^2      H_B = -(1/g^2) sum_f cos_f
cos_f = (W_f + W_f^dag)/2 = P_f/2                     THE DECLARED LAW, with t and g SUPPLIED
(div E)_v = sum_{e at v} s_{v,e} E_e,  rho_v^{sea} = n_v - 1/2,  rho_v^{stag} = n_v - (1 - eps_v)/2,  G_v = (div E)_v - rho_v
```

The **coordination** `z_v` is the number of coarse edges at `v`: `2` on the plaquette and the ring, `3` on the open cube, `3` to `6` on the open `3x3x3` block, `6` in the bulk. A **record pattern** is one
assignment of a value to every record site. `t` and `g` are **supplied**. Untruncated, every Gauss sector counted below is infinite; the finite window is what makes any of these numbers a number.

## Theorem 1 -- the coupling is exact, at every coordination

**Conclusion.** (1) Writing `a_i^dag a_j = (T_ij - i K_ij)/2`, the minimally coupled hop is exact: `a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i = (T_ij C_e + K_ij S_e)/2`, Hermitian, with `16` Pauli-monomial
entries at `S = 1` and `32` at `S = 2`, on all `140` bond checks -- every bond of the plaquette, the cube and the open `3x3x3` block at both truncations. (2) The opposite-sign partner `+i(U_e - U_e^dag)` is
that hop on none of them: it is `a_i^dag U_ij^dag a_j + h.c.`, which carries flux the other way along the bond. (3) At spin `1/2` the same identity is PR #7893's landed form, since `U = (X^L + i Y^L)/2` gives
`C = X^L` and `S = Y^L`. (4) The partner relations `[n_i, T] = -iK`, `[n_i, K] = +iT`, `[n_j, T] = +iK`, `[n_j, K] = -iT` hold on all `12` cube bonds, and `[n_w, T] = [n_w, K] = 0` at every corner `w` off the
bond (`96` pairs). (5) Truncation is **exact** for `[E_e, U_e] = U_e` and `[E_e, U_e^dag] = -U_e^dag`, and breaks **exactly two** things: `U_e^dag U_e = I - P_{+S}` with `U_e U_e^dag = I - P_{-S}`, and `[C_e,
S_e] = 2i (P_{+S} - P_{-S}) != 0`. (6) Hence `[G_v, H^g] = 0` at **every corner of every coordination `z_v = 2, 3, 4, 5, 6`** -- `1570` corner-bond pairs over the three blocks -- in both `rho` conventions and
at both `S`.

**Proof.** Item 1 builds `a_i^dag a_j` and `a_j^dag a_i` from `T` and `K`, multiplies by the exact integer link matrices, and compares key by key in the hybrid algebra: a `(2S+1) x (2S+1)` matrix of exact
Gaussian-rational Pauli sums. Item 2 is the same comparison returning a nonzero residual. Items 3 to 5 are matrix identities on the link factor. Item 6 follows from items 4 and 5 with `[E_e, C_e] = i S_e` and
`[E_e, S_e] = -i C_e`, and is then checked outright on all `1570` pairs. All exact, complete over the three blocks.

**Reading, not theorem.** Giving each edge a record that counts whole units of flux rather than a half changes nothing about whether the charge couples to it: the coupled hop is the same two pieces the
encoding already contains, one paired with the cosine of the link and one with its sine. The window on the count costs exactly two things, and neither is used here.

## Theorem 2 -- the integer flux selects the staggered convention, everywhere

**Conclusion.** (1) With integer-valued `E_e`, `2 (div E)_v = 2 sum_e s_{v,e} m_e` is **even at every corner of every coordination**, while `2 rho^{sea} = 2 n_v - 1` is odd and `2 rho^{stag} = 2 n_v - (1 -
eps_v)` is even. So `G_v = 0` is unsolvable for `rho^{sea}` and solvable for `rho^{stag}`, and `z_v` has dropped out of the statement entirely. (2) The exact census, by dynamic programming and cross-checked
by complete enumeration -- the whole link space on the plaquette and the ring, the whole `3^12` space and the cycle space on the cube -- is `0` and `26` at `S = 1` and `0` and `50` at `S = 2` on the
plaquette, `0` and `102304` at `S = 1` and `0` and `1477920` at `S = 2` on the cube, and `0` and `234` on the `L = 8` ring. (3) Exactly `2240` of the `4096` cube fermion record patterns admit a link
configuration, and they are **precisely the half-filled `N = 4` sector, all of it**, at both `S`, in eight multiplicity classes of sizes `128, 192, 416, 768, 128, 192, 384, 32` **identical at both
truncations**: raising `S` re-weights the charge sectors and does not re-partition them. `dim(Gauss and code) = 13` and `25` on the plaquette. (4) The same census run on PR #7893's spin-1/2 link returns
`14400` in the **sea** convention and `0` in the staggered one on the cube, and `0` and `14` on the plaquette. (5) `rho^{sea} = rho^{stag} - eps_v/2`, so the two conventions are one law in shifted variables
exactly when a fixed background link field `c_e` with `(div c)_v = -eps_v/2` exists. It does on every **balanced** block, with `c_e in {-1/2, 0, +1/2}` -- the plaquette (`2/2` corners), the cube (`4/4`), the
`2x2x3` block (`6/6`) -- and it does **not** on the open `3x3x3` block, whose `14` and `13` corners give `sum_v (-eps_v) = -1` while any divergence sums to zero.

**Proof.** Item 1 is a parity count. Item 2 is exact integer arithmetic by two independent algorithms agreeing on every entry: a link-by-link dynamic program over prescribed divergences, and complete
enumeration -- of the whole link space where that is small, and of the cycle space on the cube, where the spanning tree's values are determined by the divergence and only the five chords are free, so the cube
is **counted** and never diagonalised. Item 3 reads the same counts per fermion record pattern, `sum_v rho^{stag}_v = N - 4` forcing `N = 4` and the census showing it sufficient. Item 4 is the same dynamic
program at `2E = +-1`; item 5 is an integer spanning-tree solve. All exact.

**Reading, not theorem.** With whole units of flux the balance at a corner no longer notices how many neighbours the corner has -- the cube, the plaquette and the bulk stop contradicting each other about the
charge convention. The price is fixed and it is not the one this lane expected: the convention that survives is the one with a background half-charge alternating from corner to corner, and the convention that
made the sea neutral at each corner separately is no longer available anywhere. On a block with equal numbers of the two kinds of corner the difference between the two is one fixed half-unit of background
flux on the links; on a block without that balance it is not even that.

## Theorem 3 -- the electric term is dynamical, and the magnetic term is the sister lane's germ

**Conclusion.** (1) `E_e^2` has spectrum `{0, 1}` at `S = 1` and `{0, 1, 4}` at `S = 2`, so `H_E = (g^2/2) sum_e E_e^2` is a genuine operator -- contrast spin `1/2`, where `E_e^2 = I/4` identically and the
electric term supplies no dynamics. (2) `[P_f, G_v] = 0` on all `52` face-corner pairs -- `48` on the cube and `4` on the plaquette -- at both `S`, with `nnz(P_f) = 32` and `512`; `rho_v` is fermion-only, so
`[P_f, rho_v] = 0` outright and the content is `[P_f, (div E)_v] = 0`. (3) The **assembled** `H^g + H_E + H_B`, applied to every Gauss basis state of the plaquette with destinations computed in the full
space, produces `0` out-of-sector amplitudes and maximum leaked amplitude `0.0e+00` at both `S`; the individual `T C` and `K S` terms do leave the sector and cancel exactly. (4) `H_B = -(1/g^2) sum_f cos_f`
is, up to an additive constant, the one-plaquette Wilson potential `V(theta) = (1/g^2)(1 - cos theta)`: even, `2 pi`-periodic, `C^infinity`, with `V(0) = V'(0) = 0` and `V''(0) = 1/g^2 > 0`.

**Proof.** Items 1 and 2 are exact integer and complex matrix arithmetic on the `(2S+1)^4` face-link space, over every face of both blocks and every corner of each face; item 3 applies the assembled operator
state by state and looks up every destination; item 4 is the exact Maclaurin coefficients of `(1 - cos theta)/g^2`. All exact.

The open sister-lane note PR #7884 supplies, verbatim, an isotropic one-plaquette action `S_V[ell] = sum_(x,mu<nu) V(bar_theta_mu_nu(x))` with `V` even, `2 pi`-periodic, `C^4` near the flat point, normalised
by "`V(0)=0, V''(0)=kappa>0`", and concludes that "every smooth principal-branch refinement family has the same leading continuum physics", including "exactly two local transverse spatial modes after Gauss
reduction". Its declared boundary, quoted: *"This is a supplied-action theorem. It does not establish that the framework's Admissibility law realizes a compact connection, an action in this basin, or a
physical electromagnetic dictionary. Charged sources, coupling normalization, Record readout, interacting quantum electrodynamics, nonsmooth sectors, and general multi-plaquette actions are outside the
claim."* Item 4 says only that the magnetic term written here is a member of that class, with `kappa = 1/g^2` -- a plain-text pointer carrying no authority. Three things it does not do, and this note says all
three. PR #7884 is a Euclidean four-dimensional supplied-action statement about a classical limit; this is a `3+1` Hamiltonian with a truncated quantum link. Its two transverse modes are a flat-background
Hessian count, and **nothing here computes a photon at the quantum level**. And it excludes charged sources, which is exactly what this note supplies -- the complement of its boundary, not a crossing of it.

The object assembled here -- one fermionic mode per corner of a bipartite lattice with the staggered background charge, a compact `U(1)` rotor per link with integer flux, the coupled hop, the electric term,
the plaquette term, and `div E = rho` as a commuting constraint -- is the Kogut-Susskind Hamiltonian lattice gauge theory of compact `U(1)` with staggered fermions. That is said plainly as an identification
of the algebra, cited as nothing and used as no authority: every object is redeclared here and every statement recomputed. **The "designed" status is unchanged by it** -- the link role, the coupling, `H_E`,
`H_B`, `t`, `g` and the staggered convention are all designed and derived from no axiom.

**Reading, not theorem.** At the smaller link size the cost of the flux was the same number whatever the flux was, so it did nothing. With whole units it is a real energy, and it is what holds a string
together. The plaquette energy is the one whose small-angle behaviour the sister lane's open note takes as its condition; the two lanes now touch, and where they touch is one number.

## Theorem 4 -- the plaquette in its Gauss sector

**Conclusion.** `[numerical]` In the staggered convention -- the only admissible one, `rho^{sea}` having Gauss dimension `0` -- at dimensions `26` and `50`: (1) `E_0` at `g^2 = 1, 2, 4` without and with `H_B`
is `-2.152012, -2.491848, -1.807851, -1.889263, -1.352280, -1.364473` at `S = 1` and `-2.153357, -2.573395, -1.807956, -1.899006, -1.352283, -1.365185` at `S = 2`, to `1e-9`. (2) Without `H_B` the gap and
`<cos_f>` vanish at every `g^2` and both `S`; with `H_B` the gaps are `0.395359, 0.110635, 0.017047` and `0.411731, 0.114075, 0.017220` and `<cos_f> = 0.418515, 0.210243, 0.063343` and `0.541713, 0.244706,
0.068693` -- the magnetic term is what lifts the degeneracy and puts flux on the face. (3) `<E_e^2>` at `S = 1` is `0.205293, 0.145868, 0.089108` without `H_B` and `0.289139, 0.168525, 0.091811` with it, to
`1e-6`: the flux window is barely used, and the `S = 1` to `S = 2` shift in `E_0` is `3.27%` at `g^2 = 1` with `H_B`, so **no `g^2 = 1` number with `H_B` is converged in `S`**. (4) `<rho_v> = +0.180762247,
-0.180762247, -0.180762247, +0.180762247` at `g^2 = 4` with `H_B` at `S = 2`: the coupled sea is **not** locally neutral. The block's `C_4` symmetry fixes the pattern `+a, -a, -a, +a` and hence the vanishing
**total**, not the value `a`, whose maximum is `0.426, 0.305, 0.181` at `g^2 = 1, 2, 4` at `S = 1` and falls to zero only in the strong-coupling limit. `<N> = 2` at half filling and the Hermiticity residual
is `0.0e+00`. (5) The single face stabilizer splits the sector exactly in half, `26 = 13 + 13` and `50 = 25 + 25`, so `dim(Gauss and code) = 13` and `25`.

**Proof.** The Gauss sector is built explicitly by exact integer arithmetic and diagonalised densely at dimensions `26` and `50`. The full plaquette space at `S = 2` is `16 x 625 = 10 000` and is never
formed. `[numerical, 1e-9]` for items 1, 2, 4 and 5 and `[numerical, 1e-6]` for item 3.

**Reading, not theorem.** The corner condition pins a nonzero flux on a corner with two neighbours, and the background half-charge is what it is pinned to, so the charge at a corner is not zero even though
the charges of the four corners cancel. Which of those two facts a symmetry argument gives is exactly the pattern, not the size.

## Theorem 5 -- the ring: an exact string, and a broken one

**Conclusion.** (1) `[exact]` The superfast ring encoding realises **only even** total fermion number at `L = 4, 6, 8`, while half filling needs `N = L/2`, so `L = 0 mod 4` is required and `L = 6` has an
empty Gauss sector. (2) `[exact]` With static charges `+1` and `-1` at separation `d` and no fermion, `V(d) = (g^2/2) d` **exactly** in rational arithmetic for `d = 0..4` at `g^2 = 1` and `g^2 = 4` on the `L
= 8` ring at `S = 1`; `S = 1` already suffices, the minimiser using only `E in {0, 1}`. (3) `[numerical]` With the fermion hop at `t = 1` and half filling the string **breaks**: at `g^2 = 4` the potential is
`2.271563, 2.383425, 4.295402, 2.819090` against the unbroken `2, 4, 6, 8`, and it is not monotone -- `V(4) < V(3)` at `g^2 = 1` too. Gauss dimensions `234, 150, 160, 132, 150` and `<N> = 4` exactly at every
separation: the screening happens inside the half-filled sea. (4) `[numerical]` At `d = 4` and `g^2 = 4` the flux does not span the separation but localises on the sources, `sum_e |<E_e>| = 1.603` against `4`
for an unbroken string, dying to `0.0094` three links away, and the screening charge shows as a **hole** `<n> = 0.181` at the `+1` source and a **fermion** `<n> = 0.981` at the `-1` source. (5) `[numerical]`
The `L = 4` ring gives `V = 0.762517, 0.594051` at `g^2 = 1` and `2.271118, 2.169659` at `g^2 = 4` -- saturated there too, so the breaking is not an `L = 8` artefact, though the values are finite-size
numbers.

**Proof.** The ring carries a hand-rolled superfast encoding verified against the same relations as Theorem 1 item 4. Item 1 counts the encoded total over all `2^L` fermion record patterns; item 2 minimises
`(g^2/2) sum_e E_e^2` over the rational solutions of the corner condition with sources; items 3 to 5 build the Gauss sector explicitly and diagonalise it densely at dimension at most `234`. `[numerical,
1e-9]` for items 3 and 5, `[numerical, 1e-4]` for item 4's profiles.

**Reading, not theorem.** Two fixed opposite charges on a ring with no matter between them are held by a string whose energy grows exactly in step with the distance. Put the matter back and the string does
not hold: past a short separation it is cheaper to make a pair out of the sea, and what the ground state then shows is flux clinging to the two charges, a hole at one and a fermion at the other. This is PR
#7899's breakable level, reached from a glued corner condition plus matter, on a finite ring.

## Corollary -- what the join gives, and what it costs

Within the setting declared above, and on the finite blocks named:
1. **The full lattice-gauge structure exists at the supplied-carrier level.** The coupling is exact and gauge-invariant at every coordination from `2` to `6`, the electric term is dynamical rather than a
   constant, and the Wilson plaquette term commutes with Gauss's law. Charge, Gauss's law, an electric energy and a magnetic energy are all present at once, and the magnetic term is a member of the class the
   sister lane's open note (PR #7884) states its quadratic-basin conclusion for, with `V''(0) = 1/g^2 > 0`. That is a pointer to where the two lanes touch, nothing more.
2. **The convention tension of PR #7893 is resolved in one direction, and it is not the direction this lane expected.** The premise carried into this computation was that the integer flux would make the
   neutral-sea convention and the bulk convention coincide. **That premise was wrong.** The coordination-parity *condition* is genuinely absent -- `z_v` has dropped out -- but what replaces it is a
   coordination-independent selection of the **staggered** background half-charge, and `rho^{sea} = n_v - 1/2` has a Gauss sector of dimension exactly zero on every block tested, at every coordination and
   every `S`. On balanced blocks the two conventions differ by an explicit fixed `+-1/2` background link field; on the open `3x3x3` block no such field exists. The conventions do **not** coincide.
3. **Static charges confine, and the string breaks when the matter is there.** The exact `(g^2/2) d` of Theorem 5 item 2 is the glued behaviour; Theorem 5 items 3 to 5 are PR #7899's breakable level derived
   from that constraint plus matter, on a finite ring, with the screening charge visible corner by corner.
4. **What it still lacks.** No photon is shown at the quantum level -- no gapless transverse mode is computed or suggested here, and the sister lane's two transverse modes are a classical flat-background
   count in a supplied Euclidean action. The link record is **multi-valued**: it needs `log2(2S+1)` bits, `1.585` at `S = 1` and `2.322` at `S = 2`, unbounded untruncated. One physical site cannot carry it,
   since `M_2(C)` per site is fixed, so the link role must be a **collective role of several physical sites** -- a role over a small block of sites, of exactly the kind PR #7834's superlattice role pattern
   already uses. This note declares that and settles none of it. And nothing here is derived from any axiom: the link role, the coupling, both energy terms, the staggered background charge, `t` and `g` are
   all supplied.

**Reading, not theorem (this register).** Give each link a whole number of flux units instead of a half, and the charge couples to it exactly, at every corner, however many neighbours the corner has. The
price is fixed: with whole units the balance at each corner must include a background half-charge that alternates from corner to corner, and the alternative that made the vacuum locally neutral is no longer
available anywhere. With that settled, the electric energy is real, the plaquette energy is the one whose small-angle limit the sister lane showed gives Maxwell's equations, and two fixed charges on a ring
are held by a string whose energy grows with distance until the matter breaks it by making a pair. What is still not shown is light itself.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign field, **the link role**, the coupled law and both energy terms are declared objects, and no coefficient is derived: `t`
  and `g` are supplied, and no update rule, formation site, formation rate, or absolute unit appears.
- No continuum limit is taken, no second species appears, and **no photon** and no gapless transverse mode of the link sector is shown, computed, or suggested. PR #7884 is cited as an open sister-lane pointer
  with no grade and no dependency weight: nothing in its claim is used as a premise here, and nothing here is claimed for it.

## Interfaces named for other lanes, not moved here

- **The photon at the quantum level.** Whether this link sector carries a gapless transverse mode is not decided here; PR #7893's estimate of the smallest plausible test -- a `4^3` coarse torus, whose
  pure-link Gauss sector is about `10^25` states -- is unchanged by the larger link, which only enlarges it.
- **The collective link role.** An integer flux record needs several physical sites per coarse edge, and writing that role -- how many sites, which pattern, which classes -- is a design question for the lane
  that owns the role rule. **Larger blocks**: the plaquette, the cube, the open `3x3x3` block, the `2x2x3` block and the rings of `4` and `8` corners are what is treated. **The fine lattice**: the link role
  is declared on the coarse edge, and writing it as a rule on `Z^3`, the way PR #7834 does, is not done here.
- **The staggered background.** Whether the alternating background half-charge is a registered pattern of the framework or supplied data is not settled here. It is supplied in this note.

## Remaining live routes

1. The collective link role and its size, which decides whether the truncation `S` is itself a design parameter or a consequence.
2. Larger blocks, and a region carrying more than one coordination at once with the magnetic term present.
3. The string tension and the breaking scale as functions of `L` and `g^2`, which the two ring lengths here cannot separate from finite-size wobble, and the correlations of the coupled current and of the link raising, which have no record-diagonal part.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one fermionic mode per coarse vertex, BK superfast encoding, plus ONE DESIGNED COMPACT U(1) link role per coarse edge (declared, of the same kind as PR #7834's superlattice role pattern); ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md; H^g, H_E, H_B declared here with supplied t and g
blocks: plaquette 2x2x1, open cube 2x2x2, open 3x3x3, block 2x2x3, periodic rings L = 4 and L = 8; truncations S = 1 and S = 2
link: E_e |m> = m |m> integer, U_e |m> = |m+1>, [E_e, U_e] = U_e exact under truncation; C_e = U + U^dag, S_e = -i(U - U^dag)
hop: a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i = (T_ij C_e + K_ij S_e)/2 exactly, Hermitian, 16 and 32 monomial entries, on all 140 bond checks; the +i(U - U^dag) partner fails on every one and is a_i^dag U^dag a_j + h.c.; at spin 1/2 the identity is PR #7893's (T X^L + K Y^L)/2
partner_relations: [n_i,T] = -iK, [n_i,K] = +iT, [n_j,T] = +iK, [n_j,K] = -iT on all 12 cube bonds; [n_w,T] = [n_w,K] = 0 on all 96 off-bond pairs
truncation: exact for [E,U] = U and [E,U^dag] = -U^dag; breaks exactly two things, U^dag U = I - P_{+S} with U U^dag = I - P_{-S}, and [C,S] = 2i(P_{+S} - P_{-S}) != 0
gauge: [G_v, H^g] = 0 at every corner of every coordination z = 2,3,4,5,6 -- 1570 corner-bond pairs -- both rho conventions, S = 1 and 2
parity: 2 (div E)_v is EVEN at every corner when E is integer; 2 rho^sea odd, 2 rho^stag even; G_v = 0 unsolvable for rho^sea and solvable for rho^stag INDEPENDENTLY of z_v
census: plaquette 0 / 26 (S=1) and 0 / 50 (S=2); cube 0 / 102304 (S=1) and 0 / 1477920 (S=2); ring L=8 0 / 234; DP cross-checked by complete enumeration (whole link space on plaquette and ring, whole 3^12 space and the cycle space on the cube); the cube is COUNTED, never diagonalised
cube_structure: 2240 of 4096 fermion patterns admit, exactly the half-filled N = 4 sector, all of it, at both S; eight multiplicity classes of sizes 128, 192, 416, 768, 128, 192, 384, 32 identical at S = 1 (38,39,42,44,48,50,54,69) and S = 2 (616,626,642,652,672,682,702,767); dim(Gauss and code) = 13 and 25 on the plaquette
spin_half_comparison: the same census on 2E = +-1 gives cube 14400 SEA / 0 staggered and plaquette 0 sea / 14 staggered -- PR #7893's 14400 is the SEA convention
background_field: rho^sea = rho^stag - eps_v/2; c_e with (div c)_v = -eps_v/2 EXISTS with c_e in {-1/2,0,+1/2} on the balanced plaquette (2/2), cube (4/4) and 2x2x3 (6/6), and does NOT exist on the open 3x3x3 (14/13, sum_v -eps_v = -1)
electric: E_e^2 spectrum {0,1} and {0,1,4}, so H_E is not a c-number -- contrast E_e^2 = I/4 at spin 1/2
magnetic: [P_f, G_v] = 0 on all 52 face-corner pairs at both S, nnz(P_f) = 32 and 512; the assembled H^g + H_E + H_B leaves the plaquette Gauss sector with 0 out-of-sector amplitudes, max leaked 0.0e+00; H_B is the Wilson potential V = (1/g^2)(1 - cos theta), even, 2 pi-periodic, V(0) = V'(0) = 0, V''(0) = 1/g^2 > 0, a member of the class the open PR #7884 states its conclusion for
plaquette_numerics: Gauss dims 26 and 50; E_0 (g^2 = 1,2,4, without/with H_B) = -2.152012, -2.491848, -1.807851, -1.889263, -1.352280, -1.364473 at S=1 and -2.153357, -2.573395, -1.807956, -1.899006, -1.352283, -1.365185 at S=2; gaps and <cos_f> vanish without H_B; with H_B gaps 0.395359, 0.110635, 0.017047 / 0.411731, 0.114075, 0.017220 and <cos_f> 0.418515, 0.210243, 0.063343 / 0.541713, 0.244706, 0.068693; <E_e^2> at S=1 0.205293, 0.145868, 0.089108 / 0.289139, 0.168525, 0.091811; <rho_v> = +-0.180762247 at g^2 = 4 with H_B, S = 2, total 0, max |<rho_v>| = 0.426, 0.305, 0.181 at S = 1; <N> = 2; NOT locally neutral, and not zero by symmetry
ring: superfast encoding realises only even N, so L = 0 mod 4 and L = 6 is empty; V(d) = (g^2/2) d EXACTLY for d = 0..4 at g^2 = 1 and 4 with no fermion; with the hop at half filling V = 2.271563, 2.383425, 4.295402, 2.819090 at g^2 = 4 against 2,4,6,8, non-monotone, Gauss dims 234, 150, 160, 132, 150, <N> = 4; at d = 4, g^2 = 4: sum |<E_e>| = 1.603 vs 4, 0.0094 three links away, hole <n> = 0.181 at the +1 source and fermion <n> = 0.981 at the -1 source; L = 4 gives 0.762517, 0.594051 and 2.271118, 2.169659
not_shown: no photon and no gapless transverse mode at the quantum level; no continuum limit; no claim that this U(1) is electromagnetism
design_debt: the link record needs log2(2S+1) bits and so needs a COLLECTIVE ROLE of several physical sites per coarse edge; not settled here
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=28 FAIL=0
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3`, on named finite blocks: the `2x2x1` plaquette (algebra, census and numerics), the open `2x2x2` cube (algebra and census only -- it is **counted**, never
diagonalised), the open `3x3x3` block (algebra and the background-field non-existence only), the `2x2x3` block (background field only), and the periodic rings of `L = 4` and `L = 8` corners. Nothing is
claimed for `Z^3`, for a torus, or for any larger region.

The **link role is designed**, exactly as PR #7834's superlattice role pattern is designed, and derived from no axiom. The **link dynamics is declared**: `H^g`, `H_E` and `H_B` are supplied laws with supplied
`t` and `g`. `H_B` is a four-link term inside one coarse face, not a nearest-neighbour term. The link record is multi-valued and needs a collective role of several physical sites; that role is named as an
interface and written nowhere here.

**Truncation.** Every algebraic statement -- the coupling, `[G_v, H^g] = 0`, `[P_f, G_v] = 0`, the census parity -- uses only `[E_e, U_e] = U_e` and is exact at any `S`. Every **numerical** statement is at `S
= 1` or `S = 2` and is not the untruncated theory: `E_0` shifts by `3.27%` between the two at `g^2 = 1` with `H_B`. Untruncated, every Gauss sector counted here is infinite.

**The staggered convention is the one that survives.** `rho^{sea} = n_v - 1/2` has a Gauss sector of dimension exactly zero on every block tested, at every coordination and every `S`. The two conventions are
not claimed to coincide, and on unbalanced blocks no background field relates them.

**No photon.** No gapless transverse mode is shown, computed, or suggested. PR #7884's two transverse modes are a classical, Euclidean, supplied-action, flat-background Hessian count; this note's Hamiltonian
is quantum, truncated, and on blocks of at most eight corners, and its germ statement is a pointer to an open PR, not a step of any proof here. **String breaking is a finite-size observation**: `L = 4` and `L
= 8`, `S = 1`, no mass term, the plateau not claimed to equal twice any mass gap and no infinite-volume statement made. Nothing in this note is derived from any axiom; the axioms are quoted to fix what
"readable" and "admissible" mean, and for nothing else.

## Review record

An honest auditor should come away with: one declared law on named finite blocks in which PR #7893's spin-1/2 link role is replaced by a compact `U(1)` link role, and in which the minimally coupled hop is
exact and gauge-invariant at every coordination from `2` to `6`, the electric term is dynamical, the Wilson plaquette term commutes with Gauss's law, and the assembled Hamiltonian preserves the Gauss sector
with zero leaked amplitude. The load-bearing new fact is a parity count with a complete census behind it: with integer flux the coordination drops out of Gauss's law and the staggered background half-charge
is selected everywhere, so the tension PR #7893 declared is settled in that direction and **not** by the two conventions coinciding -- the premise this lane carried in was the opposite one and it was wrong.
On a ring, static charges feel exactly `(g^2/2) d` and the string breaks once the fermion is present. The costs: the link role and both energy terms are designed, not derived; the link record needs a
collective role of several physical sites that this note does not write; every numerical item is truncated; and no photon appears anywhere -- the sister lane's quadratic basin is cited as an open pointer and
used as no premise.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the context notes in "Imports and authority" are plain-text pointers
carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=28 FAIL=0`, runtime under the declared `150` seconds, and passing pipeline, strict-lint and
changed-evidence gates; independent audit remains a separate lane.
