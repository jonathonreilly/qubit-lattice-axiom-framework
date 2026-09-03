---
claim_id: shifting_position_records_exact_diffusion_uniform_attractor
claim_type: bounded_theorem
claim_scope: "On two declared lattices -- (a) the 2x2x2 cube graph (8 corners, 12 edge sites, 6 faces) with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, inside the N = 2 record sector of dimension 896 = 28 corner pairs x 32; and (b) the coarse L^3 torus carrying one-particle hopping with Kogut-Susskind staggered (pi-flux) link signs, unit amplitude, unit spacing and coordination 6, at L = 32 with L = 16 as a finite-size control and L = 6 for two records -- under SIX STIPULATED tick models declared here in full and derived from nothing: M0 no record, the state running freely; M1 a frozen record whose gap generator is the post-record Hamiltonian of PR #7876; M2 a shifting record, the corner occupation registered again by Lueders conditioning every tick of length tau, the record moving to wherever it is registered; M3 M2 with formation probability p per tick; M4 two records with an added bond ENERGY COST g sum_bonds n n; M5 the M2 tick written at record level as rho -> mask(U(tau) rho U(tau)^dag) on the cube's 896-dimensional sector. (T1) [exact] Over all 4096 record patterns x 12 edge sites (49152 cases, 0 violations) a hop along the shared edge site e is exactly y -> y XOR e: it complements n_v and n_w alone, the edge-record weight |y| moves by exactly +-1 and never by 0 (24576 up, 24576 down), and the corner-record count sum_v n_v is conserved exactly when one endpoint is occupied and moves by +-2 otherwise -- so 'the pattern's support shifts' is exact at the corner level and only under exclusion, while at the physical sites a shift is a VALUE change at one edge site. (T2) [numerical, 1e-12] M0 on L = 32 has sigma^2(t) = 0.0592, 0.3453, 1.0890, 2.1365, 5.8574, 12.0704, 32.2419, 125.5190 at t = 0.1 to 10 with sigma/t falling 2.4332 -> 1.1204, ballistic and carrying no diffusion constant (L = 16 agrees to 1.7e-8 for tau <= 1); M1's H_R annihilates the recorded site identically, giving sigma^2 = 0 and leakage 0 at t = 0.5, 1, 5, 20, 100 -- the frozen rule is degenerate. (T3) [exact + numerical] M2's one-tick kernel p_tau(r) = |<v + r| e^{-i tau H} |v>|^2 is translation covariant to 1.5e-31 and even to 3.3e-24, so the registered trajectory is an i.i.d. mean-zero walk and sigma^2(n tau) = n m_2(tau) exactly (FFT convolution, max 2.0e-12 over 17 (tau, n) pairs, n <= 50); D(tau) = m_2(tau)/(6 tau) = 0.0987, 0.2302, 0.3630, 0.3860, 0.3561, 0.3479, 0.4881, 0.6706, 1.0747 at tau = 0.1, 0.25, 0.5, 0.7, 1, 1.2, 2, 3, 5; the Zeno limit is m_2 = 6 tau^2 - 8 tau^4 + O(tau^6) with 6 = the coordination number exactly and 8 extrapolated (7.99984 at tau = 0.005), so D = tau - (4/3) tau^3 + ...; the Drude limit is m_2/tau^2 -> c_2 = 1.2437(10) so D -> 0.2073 tau; between them D carries a shoulder, a local max 0.3860 at tau = 0.7 and a local min 0.3474 at tau = 1.15. (T4) [exact + numerical] With formation probability p the age since the last registration carries P_n(a) = (1-p)^a p for a < n and (1-p)^n at a = n, exactly as Fractions, and sigma^2(n tau) = E[V_n] + sum_a P_n(a) m_2(a tau) matches brute-force enumeration of all 2^n formation histories to 7.7e-13 at n <= 12; D_inf = 0.3630, 0.9942, 4.0735, 3.9700, 16.1936 at (tau, p) = (0.5, 1), (0.5, 0.2), (0.5, 0.05), (1, 0.1), (2, 0.05) against the closed form c_2 tau (2-p)/(6p) = 0.1036, 0.9328, 4.0421, 3.9385, 16.1685; the controlling scale is the mean free time tau/p, three pairs sharing tau/p = 10 agreeing within 8.3% while their p tau spans a factor 16. (T5) [numerical, 1e-6] Under M4 on the 6^3 torus the 23220 two-particle configurations reduce by translation covariance to an EXACT 111-class relative-coordinate chain, and at tau = 0.5 a pair held together by an ENERGY COST comes apart at every g: P(adjacent) over ticks 1 to 40 runs 0.3092 -> 0.0279 (g = 0), 0.4588 -> 0.0279 (4), 0.7368 -> 0.0279 (8), 0.9285 -> 0.0766 (16), 0.9783 -> 0.4235 (32) toward the uniform reference 0.0279, with tick-40 mean corner distance 4.5209, 4.5209, 4.5208, 4.3187, 3.0338 against the uniform 4.5209; the centre of mass carries D_CoM/D_1 = 0.4910 at g = 0 against the independent-record value 1/2, and the cube's 896-dimensional sector agrees (tau = 0.5, g = 32: P(d = 1) = 0.9880, 0.9762, 0.9423, 0.8905, 0.6726 at ticks 1, 2, 5, 10, 40, toward 0.4286). NOTHING is claimed about a pair held by a SUPPORT CONDITION of the law -- exact zero odds for a configuration in which a record loses a neighbour it needs -- which is a different mechanism, outside this family and untested here. (T6) [numerical, 1e-15] M5's tick map agrees with explicit record-tree enumeration (312 branches after tick 1, 5824 after tick 2) to L1 = 6.0e-16; from the ground state the forbidden-pair mass after ticks 1, 2, 5, 8 is 0.2655, 0.3430, 0.4161, 0.4267 at tau = 0.5, 0.3101, 0.3638, 0.4228, 0.4280 at tau = 1 and 0.2148, 0.3065, 0.4016, 0.4223 at tau = 2; the maximally mixed sector state I/896 is an EXACT fixed point (5.6e-18) whose odds are uniform on the 28 corner pairs with forbidden mass exactly 12/28; convergence is geometric with per-tick L1 ratios 0.5294, 0.4560, 0.6156; and the L1 distance to the pre-record Born diagonal is exactly twice the forbidden mass at every tick. This note declares tick models and computes with them; nothing is derived from any axiom, no formation clause is supplied, no axiom is amended, no status is set, and no claim is made about what the framework's tick is."
upstream_dependencies: []
runner: scripts/shifting_position_records_exact_diffusion_law_check_2026_09_03.py
---

# Shifting position records: the exact diffusion law, and the uniform attractor

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/shifting_position_records_exact_diffusion_law_check_2026_09_03.py`](../scripts/shifting_position_records_exact_diffusion_law_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/shifting_position_records_exact_diffusion_law_check_2026_09_03.txt`](../logs/runner-cache/shifting_position_records_exact_diffusion_law_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

The owner asked, on 2026-09-03: "what if records can move (a fixed record can shift to an adjacent site, groups of records can move together if the lattice supports
it)". `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7876) stipulates a tick in which a formed record's value is
**frozen** and the gap generator drops the hops on the recorded sites. This note writes the owner's proposal down as a family of tick models on the same cube and on a
coarse torus, and computes what each one does. The short answer: a record that shifts each tick registers an exact random walk with a computable diffusion constant, and
the sharp pattern the resting state carried does not survive it.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-object theorems -- the 49152-case mapping census on the cube, the age decomposition of the renewal law in Fraction arithmetic against brute-force enumeration, the exact coordination coefficient of the Zeno limit, and the exact reduction of 23220 two-particle configurations to a 111-class relative chain -- together with deterministic double-precision evaluations of exactly specified quantities on the L = 32, L = 16 and L = 6 tori and on the cube's 896-dimensional sector, tagged [numerical] at stated thresholds. There is no sampling, no seed and no random number anywhere in the runner."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained note, and route to its owner the two wording questions it raises and does not decide: whether value-permanence at the physical sites survives a shift (T1), and whether a support-conditioned law -- not the energy cost tested in T5 -- is the intended mechanism for groups that move together."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`: `T1` (`A`) what a shift is; `T2` (`B`) unrecorded and frozen; `T3`
(`C`) the diffusion law; `T4` (`D`) the renewal law; `T5` (`E`) group motion under an energy cost; `T6` (`F`) the uniform attractor. Group `A`, the `Fraction` arithmetic
of `D1` and the coordination coefficient of `C4` are **exact**: integer, `F2` and `Fraction` arithmetic with no floating point in the statement. Every other line is a
**deterministic double-precision evaluation** of an exactly specified quantity at the threshold printed in its tag: the propagator `exp(-i t H)` is transcendental, so no
rational value exists to compare against, but there is **no sampling, no seed and no random number anywhere in this runner**. No line is a witness.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Jordan-Wigner transform, Slater determinants, Lueders conditioning, the
Kogut-Susskind staggered link signs, the geometric distribution and renewal-reward accounting are standard methodology; every object is redeclared here and the runner
recomputes every statement. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no
weight: `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7876 -- the same cube, encoding and sector, whose frozen-record
convention is `M1` here and whose corollary names the relaxation principle this note's `T6` bears on), `RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858 -- record formation and the `E = -4` ground state used as the starting state of `T6`), the sea note (open PR #7879), and `MINIMAL_AXIOMS_2026-06-29.md`, from which the axiom text in "Setting" is quoted verbatim. This note cites no grade of any of these and consumes no ledger row.

## Setting

The framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site." "No site is privileged." **Qubit / Site Possibility**: "Each site has a domain of local
possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each
site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (2), interpretive and
non-governing: "the distribution concerns which possibility a forming record locks, conditional on formation at that site; **it does not supply the formation site,
probability, or rate.**" Reading note (3) adds that the distribution is a probability measure on the local possibility domain **whose support is what "admissible"
denotes**, and that "Record locks a supported realization." That support clause is the hinge of the scope caveat in `T5`.

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are
permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

The owner's proposal, quoted as the question this note answers on declared models and does not settle for the framework: **"what if records can move (a fixed record can
shift to an adjacent site, groups of records can move together if the lattice supports it)"**.

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded or signed
clause is used anywhere. The **record ontology** is used as declared: a record at a site registers a value there; it does not report one the site already had. Reading
note (2) says the axioms supply no formation site, probability or rate, and this note **stipulates** six tick models rather than deriving any.

## The stipulated tick models, declared in full

Six models, all declared here, none derived. Each fixes what happens to a registered position between one tick and the next. A lane proposing a different tick inherits
the obligations of `T3`-`T6` and none of these choices.

1. **`M0` unrecorded.** No record forms; the state runs under `H` for a time `t`. The reference against which every other model is read.
2. **`M1` frozen.** One record is registered at a corner `v` and never moves. The gap generator is `H_R` = the hop terms on the sites carrying no record -- exactly the
   convention of PR #7876 -- which at the coarse level deletes the six hops at `v`.
3. **`M2` shifting.** Every tick of length `tau` the corner occupation is registered again by Lueders conditioning, and the record moves to whatever corner is registered.
   This is the owner's proposal read as a tick: **the record shifts, each tick, with the odds the law gives**.
4. **`M3` shifting with formation probability `p`.** As `M2`, but a tick registers with probability `p` and otherwise lets the state run on. `p = 1` recovers `M2`;
   `p -> 0` recovers `M0`.
5. **`M4` group motion under an energy cost.** Two records under `H = -sum_bonds eta (c^dag c + h.c.) + g sum_bonds n n`, both registered every tick as in `M2`, with `g`
   the energy cost of parting. This is a **cost**, not a **support condition**: the law's odds stay strictly positive on every separated configuration.
6. **`M5` record level.** The `M2` tick written on the cube's `896`-dimensional sector as `rho -> mask(U(tau) rho U(tau)^dag)`, `mask` = Lueders conditioning on the `28`
   corner patterns, cross-checked against explicit enumeration of the whole record tree.

`tau -> 0` (records shifting faster than the state can run) and `tau -> infinity` (a free flight between shifts) are the two boundary regimes, and `T3` computes both.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P6`.

`P0` (declared here): the cube, the coarse torus, the encoding, the parity dictionary, and the six tick models above. `P1` (`A`): what a shift is. `P2` (`B`): `M0` and
`M1`. `P3` (`C`): the diffusion law. `P4` (`D`): the renewal law. `P5` (`E`): group motion under a cost. `P6` (`F`): the attractor.

## Definitions

The **cube** is the `2x2x2` cube graph, corner `s = 4a + 2b + c`, `8` corners, `12` edge sites, `6` faces, one qubit per edge site, with

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
H    = sum over edges of the encoded hop T_e = (i/2) A_ij (B_i - B_j),          star(v) = the edges incident to v.
```

A **record** at an edge site registers a `Z`-value there, so a **finished set of records** is a vector `y` in `F2^12`; the **parity dictionary** is
`n_v(y) = (1 - B_v)/2 = |y intersect star(v)| mod 2`, and the **record number** is `N = sum_v n_v`. The **`N = 2` record sector** is the span of the `896` patterns of
record number `2`, `28` corner pairs times `32`; no object above `896 x 896` is formed anywhere in the runner. The **odds** over the dictionary are the `28` numbers a
sector state carries on those corner pairs. The **pre-record state** of `T6` is the `E = -4` Slater ground state of the encoded hopping, whose odds are `1/16` on `16`
corner pairs and exactly `0` on the other `12`: the **forbidden pairs**, the pairs sharing an `x`-face.

The **coarse torus** is `Z_L^3` with nearest-neighbour hopping of unit amplitude and unit spacing, coordination `6`, and Kogut-Susskind staggered (pi-flux) link signs
`eta(v, 1) = 1`, `eta(v, 2) = (-1)^{v_x}`, `eta(v, 3) = (-1)^{v_x + v_y}`. `m_2(tau)` is the second moment of the one-tick kernel `p_tau(r) = |<v + r| e^{-i tau H}
|v>|^2`, `D(tau) = m_2(tau)/(6 tau)`, and `D_1` is the one-record value of `D` on the same torus. On the `6^3` torus a **relative class** is an unordered pair of
positions modulo translation and inversion; there are `111` of them.

## Theorem 1 -- what a shift is, exactly

**Conclusion.** `[exact]` On the cube, over all `4096` record patterns and all `12` edge sites (`49152` cases): a hop along the shared edge site `e = (vw)` is exactly the
map `y -> y XOR e`. It complements `n_v` and `n_w` and leaves the other `6` corners untouched (`0` violations). The **edge-record weight** `|y|` changes by exactly `+-1`
in every case -- `24576` up, `24576` down -- and **never by `0`** (`0` violations). The **corner-record count** `sum_v n_v` is conserved exactly when one endpoint is
occupied (`24576` cases, `0` violations) and changes by `+-2` otherwise (`24576` cases, `0` violations).

**Proof.** Exhaustive enumeration in `F2` over the `4096 x 12` pairs, with the dictionary evaluated by popcount. No floating point.

**Reading, not theorem.** Two different sentences are both true and they are not the same sentence. At the corner level the picture the proposal draws is exact: a record
at one corner and none at its neighbour becomes a record at the neighbour and none at the first, with the count preserved -- and this holds precisely under exclusion,
one endpoint occupied. At the physical sites nothing moves at all: the record sitting on the shared edge site changes its **value**.

## Theorem 2 -- unrecorded is ballistic, frozen is pinned

**Conclusion.** `[numerical, 1e-12]` On the `L = 32` pi-flux torus, `M0` carries `sigma^2(t) = 0.0592, 0.3453, 1.0890, 2.1365, 5.8574, 12.0704, 32.2419, 125.5190` at
`t = 0.1, 0.25, 0.5, 1, 2, 3, 5, 10`, with `sigma(t)/t` falling `2.4332 -> 1.1204`: the unrecorded walk spreads **ballistically** and carries no diffusion constant at
all. The `L = 16` torus agrees with `L = 32` to `1.4e-17, 4.1e-13, 1.7e-08` at `tau = 0.1, 0.5, 1.0`, so every one-particle row below is torus-independent for `tau <= 1`.
`[numerical, 1e-15]` `M1` is degenerate: `H_R` deletes the `6` bonds at the recorded corner, `H_R e_v = 0` **identically**, and `sigma^2(t) = 0` with leakage `0` at
`t = 0.5, 1, 5, 20, 100`.

**Proof.** Deterministic evaluation of `exp(-i t H)` applied to one basis vector by Krylov exponentiation on the sparse hopping matrix, with the second moment taken
against minimal-image displacements; the wrap mass is reported and is below `5e-5` at every tabulated `t <= 5`. `M1`'s row is a one-line consequence of dropping every
bond at the site, checked to be exactly zero rather than small.

**Reading, not theorem.** The two obvious models are both extremes. With no record the position never settles anywhere; with a frozen record it never moves at all. Neither
is matter that moves, and something between them is what the proposal asks for.

## Theorem 3 -- the exact diffusion law of a shifting record

**Conclusion.** `[numerical]` The one-tick kernel `p_tau(r) = |<v + r| e^{-i tau H} |v>|^2` is **translation covariant** to `1.5e-31` and **even** to `3.3e-24` at
`tau = 0.5`, with `|E[r]| <= 2.6e-13`. Hence the registered trajectory is an i.i.d. mean-zero walk, and `sigma^2(n tau) = n m_2(tau)` exactly: the `n`-fold FFT
convolution of the tick kernel reproduces it to `2.0e-12` over the `17` `(tau, n)` pairs with `tau <= 2`, `n <= 50` whose torus wrap mass stays below `1e-14`. The law is
`D(tau) = m_2(tau)/(6 tau) = 0.0987, 0.2302, 0.3630, 0.3860, 0.3561, 0.3479, 0.4881, 0.6706, 1.0747` at `tau = 0.1, 0.25, 0.5, 0.7, 1, 1.2, 2, 3, 5`. Its two limits:
`[exact + numerical]` **Zeno**, `m_2(tau) = z tau^2 - a tau^4 + O(tau^6)` with `z = sum_w |H_wv|^2 |w - v|^2 = 6` **exactly**, the coordination number, and `a -> 8`
(`7.99984` at `tau = 0.005`), so `D(tau) = tau - (4/3) tau^3 + ...`; `[numerical, 1e-3]` **Drude**, `m_2/tau^2 -> c_2 = 1.2437(10)` on `tau in [3, 6]`, so
`D(tau) -> 0.2073 tau`. Between them `D` carries a **shoulder**: a local maximum `0.3860` at `tau = 0.7` and a local minimum `0.3474` at `tau = 1.15`.

**Proof.** Covariance and evenness are entrywise comparisons of two exactly computed kernels reindexed by minimal-image displacement. Independence of increments follows
from the model itself -- each registration restores a delta at the registered corner -- so the second moments add, and the FFT convolution is an independent check of that
addition rather than a derivation of it. `z = 6` is a finite sum of squared unit amplitudes times squared unit displacements, evaluated as an integer; the Drude coefficient is a three-parameter least-squares fit on four exactly computed `m_2` values, and the shoulder is read off a scan of `D`.

**Reading, not theorem.** This is the quantitative content of the proposal. Let a record shift each tick with the odds the law gives and the recorded path is a random
walk whose spread grows at a rate the lattice fixes. Tick very fast and the record barely moves -- `D` falls off linearly with the tick, the Zeno end. Tick slowly and it
flies between shifts -- `D` grows linearly with the tick, the Drude end. The classical, diffusive regime is the middle, and the crossover is not a free parameter.

## Theorem 4 -- the renewal law, and what sets the crossover

**Conclusion.** `[exact]` Under `M3` the age `a` since the last registration carries `P_n(a) = (1-p)^a p` for `a < n` and `(1-p)^n` at `a = n`, summing to `1` exactly as
`Fraction`s at every `n <= 12`; and the decomposition `sigma^2(n tau) = E[V_n] + sum_a P_n(a) m_2(a tau)`, with `E[V_n]` the accumulated variance of completed segments,
matches **brute-force enumeration of all `2^n` formation histories** to `7.7e-13`. `[numerical, 1e-6]` The asymptotic constant
`D_inf = (p/(6 tau)) sum_k p (1-p)^{k-1} m_2(k tau)` equals `0.3630, 0.9942, 4.0735, 3.9700, 16.1936` at `(tau, p) = (0.5, 1), (0.5, 0.2), (0.5, 0.05), (1, 0.1),
(2, 0.05)`, against the ballistic closed form `c_2 tau (2 - p)/(6 p) = 0.1036, 0.9328, 4.0421, 3.9385, 16.1685`. The controlling scale is the **mean free time** `tau/p`,
not the product `p tau`: the three pairs `(0.5, 0.05)`, `(1, 0.1)`, `(2, 0.2)` share `tau/p = 10` and give `D_inf` within `8.3%` of one another, while their `p tau`
spans a factor `16`.

**Proof.** The age recursion is a two-line induction whose weights are exact `Fraction`s; the enumeration sums, over all `2^n` binary formation histories with exact
rational weights, the second moments of the independent segments, and is compared entry by entry with the recursion. The closed form is the `m_2(s) -> c_2 s^2`
substitution into the renewal sum, evaluated as a geometric series; the tabulated `D_inf` uses exact `m_2` for `k tau <= 6` and that ballistic tail beyond.

**Reading, not theorem.** Records need not form every tick, and how often they do is what decides whether the world looks classical. Registrations far apart in time leave
long ballistic flights between them and a large diffusion constant; registrations close together give a small one. The single number that governs it is the average time
between shifts, and the same number appears whether one changes the tick length or the formation probability.

## Theorem 5 -- a pair held by an energy cost does not shift rigidly

**Conclusion.** `[numerical, 1e-6]` Under `M4` on the `6^3` torus the `23220` two-particle configurations reduce by translation covariance to an **exact** `111`-class
relative-coordinate chain, every row of whose one-tick kernel sums to `1` (max deviation `3.6e-13`). At `tau = 0.5` a pair held together by an **energy cost** comes apart
at every `g`: `P(adjacent)` over ticks `1` to `40` runs `0.3092 -> 0.0279` at `g = 0`, `0.4588 -> 0.0279` at `4`, `0.7368 -> 0.0279` at `8`, `0.9285 -> 0.0766` at `16`,
`0.9783 -> 0.4235` at `32`, toward the uniform-over-configurations reference `0.0279` in every case; the tick-`40` mean corner distance is `4.5209, 4.5209, 4.5208,
4.3187, 3.0338` against the uniform `4.5209`. `g = 4` sits inside the two-particle continuum (half band `sqrt(12) = 3.4641`). The centre of mass carries
`D_CoM/D_1 = 0.4910` at `g = 0`, against the independent-record value `1/2`. The cube's `896`-dimensional sector agrees: at `tau = 0.5`, `g = 32`, two records started
adjacent carry `P(d = 1) = 0.9880, 0.9762, 0.9423, 0.8905, 0.6726` at ticks `1, 2, 5, 10, 40`, running to the uniform-on-`28` value `0.4286`.

**Scope.** This is a statement about the **energy-cost family `g sum_bonds n n` alone**. A **support condition** of the law -- exact zero odds for a configuration in
which a record loses a neighbour it needs, in the sense of Admissibility reading note (3), where "admissible" denotes the support of the distribution -- is a **different
mechanism**, outside this family. Such a condition confines a group exactly, because the shift that parts them carries odds `0` and is never registered, and **nothing
here tests it or bears on it**. It is named as an interface below.

**Proof.** The relative-class chain is exact: translation covariance of the one-tick kernel (`T3`) makes the relative class a Markov chain, and one propagated column per
class fills its transition row; row stochasticity is checked. The centre-of-mass step variance is a class function accumulated along the same chain, and the cube row is the `M5` map of `T6` with the diagonal `g` term added.

**Reading, not theorem.** Two records that started side by side and were held together only by a **cost** wander apart, however large the cost: raising `g` slows the
parting but never stops it, because the walk that separates them is transient. Whether a **condition** that forbids their parting outright makes them move as one is a
different question, and it is not asked here.

## Theorem 6 -- the uniform attractor

**Conclusion.** `[numerical, 1e-15]` `M5`'s tick map `rho -> mask(U(tau) rho U(tau)^dag)` on the `896`-dimensional sector agrees with **explicit record-tree
enumeration** -- `312` branches after tick `1`, `5824` after tick `2` -- to `L1 = 2.6e-16` and `6.0e-16`. `[numerical, 1e-9]` From the ground state the forbidden-pair
mass after ticks `1, 2, 5, 8` is `0.2655, 0.3430, 0.4161, 0.4267` at `tau = 0.5`; `0.3101, 0.3638, 0.4228, 0.4280` at `tau = 1`; `0.2148, 0.3065, 0.4016, 0.4223` at
`tau = 2`. `[numerical, 1e-15]` The maximally mixed sector state `I/896` is an **exact fixed point**: `max |map(I/896) - I/896| = 5.6e-18, 6.3e-18, 4.8e-18` at
`tau = 0.5, 1, 2`, its odds are uniform on the `28` corner pairs to `6.6e-16`, and its forbidden mass is exactly `12/28`. `[numerical, 1e-3]` Convergence is **geometric**,
the per-tick `L1` ratio to uniform-on-`28` settling at `0.5294, 0.4560, 0.6156`. `[numerical, 1e-12]` The `L1` distance from the record odds to the pre-record Born
diagonal is **exactly twice** the forbidden mass at all `24` tabulated ticks (max residual `1.9e-15`), because no allowed pair ever exceeds its Born value `1/16`.

**Proof.** The tick map is a masking of a conjugation, so its branches are exactly the record tree's; the tree is enumerated in full, with no sampling, and compared entry
by entry at ticks `1` and `2`. The fixed-point statement is the residual of one application of the map to `I/896`, and the `L1` identity is arithmetic on the `28` odds given the checked inequality `q_k <= 1/16` on the allowed pairs.

**Reading, not theorem.** Whatever sharp pattern the resting state carried, shifting records wash it out. Within a few ticks the odds are flat over every corner pair the
law allows, and the pairs the resting state never registered are registered at the same rate as the rest. The flat state is not merely reached; it is fixed exactly.

## Corollary -- what this says about the owner's proposal

Within the setting declared above, on the two named lattices, and for the stipulated tick models alone:

1. **Shifting position records give matter that moves, with a quantitative divide.** `T3` supplies the law, `T4` the crossover. The classical, diffusive picture holds for
   times long against the mean free time `tau/p` and the quantum, ballistic picture for times short against it, so **registration density is the dial** between them, and
   it is not free: `D` is fixed once `tau` and `p` are.
2. **The exclusion clause of the proposal is free; the permanence clause is not.** By `T1` "records move together with the pattern" is exactly corner-record count
   conservation, which holds precisely when one endpoint is occupied -- exclusion. But at the **physical sites** a shift is a **value change at one edge site**, and the
   edge-record weight changes by `+-1` at every shift. The proposal therefore requires either a weakened value-permanence -- "a record's value may be complemented by a
   neighbouring shift" -- or records relocated from the physical sites to the coarse cells, where the corner-level statement is the exact one. Which of the two the owner
   intends is a wording question this note does not decide.
3. **Groups held by an energy cost do not shift rigidly.** `T5` shows the pair comes apart at every `g`, with the centre of mass diffusing at half the single-record rate.
   This says nothing about groups held by a **support condition** of the law, which is a different mechanism and is named as an interface below.
4. **The fermionic sign is not supplied by shifting records.** The registered trajectory of `T3` is a classical Markov chain on the lattice; every sign in it enters
   through the imported pre-record propagator, and the exclusion of `T1` is satisfied equally by hard-core bosons. Shifting records give motion, not statistics.
5. **The sharp record patterns are not preserved.** By `T6` the attractor of the shifting tick is the uniform state, exactly, and the selection-rule zeros are lost
   geometrically. So the relaxation or state-selection principle that PR #7876's corollary names as an interface is **still required**: shifting records do not supply it,
   and on this model they make the need sharper, not weaker.

## Reading, not theorem -- the whole thing in plain words

Let a record slide to a neighbouring corner each tick with the odds the law gives, and a particle's recorded path becomes a random walk whose spread grows with time at a
computable rate: very fast ticks pin it, slow ticks let it fly between them, and the average time between shifts is the single number that says which. Two records that
started side by side and were held together only by a cost wander apart, however large the cost; whether a condition that forbids their parting outright makes them move
as one is a different question, not asked here. And whatever sharp pattern the resting state carried, sliding records wash it out to a flat one within a few ticks.

## Interfaces named for other lanes, not settled here

- **The wording of the Record axiom.** `T1` shows a shift is a value change at one physical site while the corner-level pattern moves. Whether "records are permanent"
  survives that, and in which of the two readings of corollary item 2, is the owner's call and is not made here.
- **Support-conditioned shifts.** A law whose support excludes configurations in which a record loses a neighbour it needs confines a group exactly, by a mechanism
  entirely different from the energy cost of `T5`: the parting shift carries odds `0` and is never registered. That mechanism is **under test in a separate lane** and
  nothing here tests it, supports it or excludes it.
- **The relaxation or state-selection principle.** Named by PR #7876 and sharpened by `T6`. Untouched here.
- **Interactions beyond the declared family.** Only the on-bond `g sum n n` term is used. Longer-range terms, three-body terms, and any dynamical constraint are outside
  this note.
- **Larger tori and larger clusters.** `L = 32` one-particle, `L = 6` two-particle, and the `2x2x2` cube. The thermodynamic limit, other record-number sectors and the
  three-record case are outside this note.

## Remaining live routes

1. Whether the shoulder in `D(tau)` -- max at `tau = 0.7`, min at `tau = 1.15` -- has a structural origin in the pi-flux band or is an artefact of this particular sign
   convention. The Zeno and Drude ends are both understood; the crossover is not.
2. Whether the `a -> 8` coefficient of the Zeno expansion is exactly `8` on this lattice, as the extrapolation strongly suggests but does not prove, and whether it has a closed form in the coordination number and the plaquette flux.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions.

```text
setting: (a) qubits on the 12 EDGE sites of the 2x2x2 cube graph, ordinary composition, superfast encoding, dictionary n_v = (1 - B_v)/2, N = 2 sector 896 = 28 corner pairs x 32; (b) the coarse L^3 torus, one-particle hopping, KS staggered (pi-flux) signs, unit amplitude and spacing, coordination 6, L = 32 (L = 16 control), L = 6 for two records; axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading notes (2) and (3)
tick_models: STIPULATED, six declared -- M0 no record; M1 frozen (PR #7876's H_R); M2 shifting (Lueders on the corner occupation every tick tau, the record moving to where it registers); M3 M2 with formation probability p; M4 two records plus a bond ENERGY COST g sum n n; M5 the M2 tick at record level, rho -> mask(U rho U^dag). None derived; no formation site, probability or rate is taken from any axiom
T1_what_a_shift_is [exact]: over 4096 patterns x 12 edge sites (49152 cases) a hop along e is y -> y XOR e; it complements n_v and n_w alone (0 violations); |y| moves by exactly +-1, never 0, 24576 up and 24576 down (0 violations); sum_v n_v is conserved iff one endpoint is occupied (24576 cases) and moves by +-2 otherwise (24576 cases), 0 violations
T2_unrecorded_and_frozen [numerical, 1e-12]: M0 on L = 32 gives sigma^2 = 0.0592, 0.3453, 1.0890, 2.1365, 5.8574, 12.0704, 32.2419, 125.5190 at t = 0.1..10 with sigma/t 2.4332 -> 1.1204 (ballistic, no diffusion constant); L = 16 agrees to 1.4e-17, 4.1e-13, 1.7e-08 at tau = 0.1, 0.5, 1; M1 has H_R e_v = 0 identically, sigma^2 = 0 and leakage 0 at t = 0.5, 1, 5, 20, 100
T3_diffusion_law [exact + numerical]: the one-tick kernel is translation covariant to 1.5e-31 and even to 3.3e-24 at tau = 0.5, |E[r]| <= 2.6e-13, so sigma^2(n tau) = n m_2(tau) (FFT convolution, max 2.0e-12 over 17 (tau, n) pairs, n <= 50); D(tau) = 0.0987, 0.2302, 0.3630, 0.3860, 0.3561, 0.3479, 0.4881, 0.6706, 1.0747 at tau = 0.1, 0.25, 0.5, 0.7, 1, 1.2, 2, 3, 5; Zeno m_2 = 6 tau^2 - 8 tau^4 + O(tau^6), 6 = coordination exact, 8 extrapolated (7.99984 at tau = 0.005), D = tau - (4/3) tau^3 + ...; Drude c_2 = 1.2437(10), D -> 0.2073 tau; shoulder max 0.3860 at tau = 0.7, min 0.3474 at tau = 1.15
T4_renewal [exact + numerical]: P_n(a) = (1-p)^a p (a < n), (1-p)^n (a = n), exact Fractions summing to 1 for n <= 12; sigma^2(n tau) = E[V_n] + sum_a P_n(a) m_2(a tau) matches enumeration of all 2^n histories to 7.7e-13; D_inf = 0.3630, 0.9942, 4.0735, 3.9700, 16.1936 at (tau, p) = (0.5, 1), (0.5, 0.2), (0.5, 0.05), (1, 0.1), (2, 0.05) against c_2 tau (2-p)/(6p) = 0.1036, 0.9328, 4.0421, 3.9385, 16.1685; three pairs at tau/p = 10 agree within 8.3% while p tau spans 16x
T5_cost_bound_group [numerical, 1e-6]: 23220 two-particle configurations on the 6^3 torus reduce EXACTLY to a 111-class relative chain, rows summing to 1 (3.6e-13); at tau = 0.5, P(adjacent) over ticks 1..40 runs 0.3092 -> 0.0279 (g = 0), 0.4588 -> 0.0279 (4), 0.7368 -> 0.0279 (8), 0.9285 -> 0.0766 (16), 0.9783 -> 0.4235 (32) toward the uniform 0.0279; tick-40 mean distance 4.5209, 4.5209, 4.5208, 4.3187, 3.0338 against 4.5209; g = 4 inside the continuum (half band sqrt(12)); D_CoM/D_1 = 0.4910 at g = 0 against 1/2; cube sector at tau = 0.5, g = 32 gives P(d = 1) = 0.9880, 0.9762, 0.9423, 0.8905, 0.6726 at ticks 1, 2, 5, 10, 40 toward 0.4286. SCOPE: the energy-cost family only; a SUPPORT condition of the law is a different mechanism and is untested here
T6_uniform_attractor [numerical, 1e-15]: the tick map agrees with explicit record trees (312 branches after tick 1, 5824 after tick 2) to L1 = 2.6e-16 and 6.0e-16; forbidden mass at ticks 1, 2, 5, 8 is 0.2655, 0.3430, 0.4161, 0.4267 (tau = 0.5), 0.3101, 0.3638, 0.4228, 0.4280 (1), 0.2148, 0.3065, 0.4016, 0.4223 (2); I/896 is an EXACT fixed point (5.6e-18, 6.3e-18, 4.8e-18), odds uniform on 28 to 6.6e-16, forbidden mass exactly 12/28; per-tick L1 ratios 0.5294, 0.4560, 0.6156; L1 to the pre-record Born diagonal = 2 x forbidden mass at all 24 ticks (residual 1.9e-15)
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=23 FAIL=0
```

## Proof boundary

Every statement above is proved on **declared finite objects**: the `2x2x2` cube graph and its `896`-dimensional `N = 2` record sector, and the `L = 32`, `L = 16` and
`L = 6` pi-flux tori. Nothing is claimed for the thermodynamic limit, for other record-number sectors, for other lattices or flux conventions, or for any law family
other than the ones in "Definitions" and "The stipulated tick models". The coarse law is **designed**, not derived: the staggered sign convention is one pi-flux gauge
among many and no minimality or uniqueness is claimed for it, and the parity dictionary is one readout map among many.

**The six tick models are stipulated in full and derived from nothing.** Reading note (2) is explicit that the axioms supply no formation site, probability or rate, and
this note supplies none either: it declares six models and computes with them, so every statement here is about **those** models. **Nothing here says what the
framework's tick is**, and nothing forecloses any tick. In particular `T5` is a statement about a two-record law whose parting configurations carry **strictly positive**
odds; a law whose **support** excludes them is a different object, untested here, and `T5` says nothing about it.

The `[exact]` lines -- group `A`, the `Fraction` age law of `T4`, and the coordination coefficient `z = 6` of `T3` -- carry no floating point. Every other line is a
**deterministic double-precision evaluation** of an exactly specified quantity at the threshold printed in its tag: the propagator is transcendental, so no exact rational
value exists to compare against, but there is **no sampling, no seed and no random number anywhere in the runner**, and no line is a witness. Torus wrap mass is reported
wherever it could matter and every tabulated row is inside a regime where it is negligible. No absolute unit appears anywhere, no axiom text is amended, extended,
reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

An honest auditor should come away with six declared tick models and their consequences, not a claim about what the framework's tick is; one exact census, one exact
combinatorial identity and one exact integer coefficient, with everything else a deterministic unsampled double-precision evaluation on named finite objects; no Monte
Carlo anywhere; the stipulation declared as stipulated in the front matter, the setting, its own section, the claim block and the proof boundary alike; the scope of `T5`
stated three times over, in the theorem, the corollary and the proof boundary, as a statement about an energy cost and not about a support condition; and a corollary
written as an answer to a proposal with two open wording questions handed back to its owner, not as a foreclosure of it.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority"
pointers are plain text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=23 FAIL=0`, runtime under the declared `150`
seconds, stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a
separate lane.
