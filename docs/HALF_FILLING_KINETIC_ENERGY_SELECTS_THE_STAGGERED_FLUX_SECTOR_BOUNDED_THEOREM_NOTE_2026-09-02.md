---
claim_id: half_filling_kinetic_energy_selects_staggered_flux_sector
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with free nearest-neighbour hopping sum_ij eta_ij c_i^dag c_j and no other term, the flux sector of a face being the eigenvalue of that face's stabilizer S_f and E_N the sum of the N lowest one-particle levels, on the named finite blocks and tori only: (T1) the open 2x2x2 coarse cube has exactly 32 consistent flux sectors of the 64 face assignments -- six faces with one F2 relation, so an even number of -1 faces -- confirmed by enumerating all 2^12 link-sign fields, which realise exactly those 32 holonomy patterns with the one-particle spectrum constant on each; the all-(+1) sector has E_N = 0, -3, -4, -5, -6, -5, -4, -3, 0 and the all-(-1) sector E_N = -N sqrt3 for N <= 4 with its mirror, both exact over the integers; at N = 4 the all-(-1) sector is the unique minimiser of all 32, by 0.456067 to the next distinct value and by 4 sqrt3 - 6 to the plain sector, while the unique minimiser is the plain sector at N = 1, 7, the two-flux class at N = 2, 6 and the four-flux class at N = 3, 5, and all 32 tie at N = 0 and 8. (T2) On the coarse tori 4^3, 4x4x6, 6^3 and 8^3 and the open blocks 3^3 and 4^3, sign(E_N(-) - E_N(+)) is + below N*, - on the whole of [N*, V - N*] and + above -- one contiguous window, the difference symmetric under N -> V - N -- with N* = 23, 30, 71, 171, 10, 22 respectively; at L = 4 the spectra are fixed exactly by integer minimal-polynomial and power-trace witnesses, E_32(-) - E_32(+) = 36 - 24 sqrt2 - 8 sqrt3 < 0, E_16(-) - E_16(+) = 48 - 24 sqrt2 - 8 sqrt3 > 0, and the first sign change is at N* = 23 where the difference is 46 - 24 sqrt2 - 8 sqrt3. (T3) The S_f fix no torus Wilson line, so each sector is a family of eight link-sign fields; minimised over the eight twists the half-filling energies are -78.383672 against -67.882251 on 4^3, -116.809009 against -99.882251 on 4x4x6 and -258.857540 against -218.564065 on 6^3, and the all-(-1) sector at its worst twist still beats the all-(+1) sector at its best, by 3.92, 10.15 and 36.58; the twisted Bloch formulas +-sqrt(6 + 2 sum_a cos q_a) and 2 sum_a cos q_a reproduce all 48 twisted real-space spectra of those tori at 1e-9. (T4) The 4^3 coarse torus is bipartite with every degree 6, so for ANY link-sign field on it the integer matrix M has tr M^2 = 2|E| = 6V = 384 and D M D = -M for the colour involution D, hence a spectrum symmetric about 0; the V/2 lowest squared levels therefore sum to 3V = 192 and Cauchy-Schwarz gives E_{V/2} >= -sqrt((V/2)(3V)) = -V sqrt(3/2) = -32 sqrt6 = -78.383672, with equality exactly when every |lambda| = sqrt6; the all-(-1) sector at its optimal twist satisfies M^2 = 6 I exactly as a 64x64 integer identity, its spectrum is +-sqrt6 with multiplicity 32 each, and it attains the bound, so it is a global minimiser at half filling over all 2^192 link-sign fields on that torus; on 4x4x6, 6^3 and 8^3 the same bound is -117.5755, -264.5449 and -627.0694 and the all-(-1) sector misses it by 0.766, 5.687 and 15.26. (T5) At half filling on 4^3 and 4x4x6, 2000 random link-sign fields per torus as drawn and a 500-field subsample with each field minimised over its own eight twists give 0 of 2500 fields beating the all-(-1) sector on either torus; the structured sectors with flux only on the xy, xz or yz plaquettes, xy flux on alternating x planes, and flux on the xz and yz plaquettes together are consistent and all strictly above it, while flux on the even-parity faces, xz+yz on alternating planes and a single-face flip off the all-(-1) sector are inconsistent; greedy single-link descent from 24 random restarts per torus never beats the all-(-1) field at its optimal twist and on 4^3 returns exactly that field; that field is a strict local minimum, every single-link flip raising E_{V/2} by at least 0.426844 on 4^3 and 0.365352 on 4x4x6. (T6) From the exact Bloch formulas the per-site half-filling energies converge to e(+) = -1.00241973 and e(-) = -1.19380112, a difference of -0.19138139 |t| per coarse site, while at quarter filling the difference is +0.07909 at L = 96; the crossing filling n* = N*/V settles to 0.339659 with the window ending at the mirror 1 - n* = 0.660341. T3 and T5 are search results, not theorems. Nothing here is derived from any axiom, no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py
---

# Half filling selects the staggered flux sector

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py`](../scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt`](../logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

A separate construction puts one fermionic mode on each vertex of the coarse lattice `2Z^3` and shows that transport of one encoded excitation around a coarse face
equals that face's stabilizer `S_f`, so the framework's staggered kinetic sign field is the sector in which every `S_f` is `-1` and the plain field is the sector in
which every one is `+1`. That construction states its own limit: the law as written attaches no coefficient to any face term, so the sector is a free choice under
the law. This note refines that statement. The law's hopping term *is* supplied, and it is not indifferent: on the finite clusters named below the hopping energy of
a filled Fermi sea distinguishes the two sectors, strictly, and which one it prefers depends on how much matter is present.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems on the flux-sector dependence of the free coarse-lattice hopping energy: exhaustive enumeration on the open 2x2x2 cube, exact surd spectra on the 4^3 torus, and an integer Cauchy-Schwarz certificate making the staggered sector a global half-filling minimiser there. The sampling, structured-sector and descent items are declared search results, not theorems, and the thermodynamic items are converged quadrature."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: what fixes the coarse-lattice matter density."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`. Group `A`, the `L = 4` content of `B` and the whole of `D` are
exact -- exhaustive enumeration, `sympy` surds, integer matrix arithmetic at zero tolerance, `F2`/`Z4` symplectic bit arithmetic -- and the items tagged
`[numerical]` are floating-point statements at the stated tolerance. Groups `C` and `E` are search results and are labelled as such wherever they appear.

1. `T1` (`A`). The exhaustive `2x2x2` cube: 32 consistent sectors, their `E_N` ladders, and the filling-dependent minimiser.
2. `T2` (`B`). The two uniform sectors on four tori and two open blocks: one contiguous `pi`-flux window `[N*, V - N*]`, with exact surds at `L = 4`.
3. `T3` (`C`). The Wilson-line caveat: the `S_f` fix no torus Wilson line, and the ordering survives every twist.
4. `T4` (`D`). The Cauchy-Schwarz certificate: on the `4^3` torus the staggered sector at its optimal twist is a global half-filling minimiser over all link-sign
   fields, and the gap by which the bound is missed elsewhere.
5. `T5` (`E`). Random, structured and greedily optimised sectors, all at half filling. Search results.
6. `T6` (`F`). The thermodynamic per-site difference and the crossing filling, from the exact Bloch formulas.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering and the tight-binding dispersion are standard
methodology; every object is redeclared here and the runner recomputes every statement. Lieb's flux-phase theorem is named only as background -- it fixes the
optimal flux of half-filled bipartite *planar* lattices, is not proved for the cubic lattice, and nothing below uses it or claims a cubic analogue. No observational
value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): face transport equals `S_f`, and the sentence
  quoted below. Pointer only; the encoding, the sign fields and the face stabilizers are redeclared here and recomputed by this runner.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`: the kinetic-form clause quoted below.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". This note cites none of their grades and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has
algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**:
"Records form", "a record locks exactly one admissible local possibility", "records are permanent", "Only records are readable."

The landed kinetic clause whose sign field is under test reads, verbatim:

> **Kinetic-form clause.** Within the declared kinetic class (the naive-Dirac kinetic form on nearest-neighbor `Z^3` links, made
> compatible with the matter-statistics clause by site-local spin diagonalization), the kinetic operator is the staggered operator
> `D = (1/2) Σ_{x,μ} η_μ(x) (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})` with the Kawamoto-Smit phases `η_1 = 1, η_2(x) = (−1)^{x_1},
> η_3(x) = (−1)^{x_1+x_2}`, unique as a local Z2 gauge class.

and the sentence this note refines, from the face-transport note, reads:

> So the two sectors are a free choice under the law as written; a face term `-J sum_f S_f` with negative `J` would select the staggered
> sector, and no such term is supplied by anything quoted here.

Everything below reads those sign fields on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, with free nearest-neighbour hopping and nothing else.
Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the two uniform
sign fields on it, the superfast encoding, the face stabilizers, the flux sectors and the filling functional `E_N`. `P1` (`A`) is the exhaustive `2x2x2` cube; `P2`
(`B`) the uniform sectors on the named tori and blocks and the shape of the difference; `P3` (`C`) the Wilson-line freedom; `P4` (`D`) the Cauchy-Schwarz bound and
its equality case; `P5` (`E`) the searches; `P6` (`F`) the thermodynamic limit. `P4` uses nothing from `P3` but its numbers; `P5` and `P6` use nothing from each
other. The strongest supported scope is precisely `P0`-`P6`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The
**KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`, the clause's phases read in coarse
coordinates; the **plain sign** is `+1` on every bond. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, code qubits on the coarse
edges, direction order `-x < -y < -z < +x < +y < +z`, with

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_i  = product of the Z's on the edges incident to i,   S_f = the ordered product of the four A's around a coarse face f
```

A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` consistent with the `F2` relations among them; a sector is realised as a link-sign field `eta` by
spanning-tree gauge fixing followed by fundamental-cycle transport, and the plaquette holonomy of that field reproduces the sector face by face. The **hopping
matrix** is `M_ij = eta_ij` on nearest-neighbour coarse bonds and `0` elsewhere; `E_N` is the sum of its `N` lowest eigenvalues, the ground-state kinetic energy of
`N` spinless fermions, and the **filling** is `n = N/V`. On a torus the three **Wilson lines** -- the products of `eta` around the three non-contractible loops --
are gauge-invariant data that no `S_f` fixes; a **twist** flips the signs on one cut plane and changes one Wilson line without changing any face.

## Theorem 1 -- the exhaustive 2x2x2 cube

**Conclusion.** On the open `2x2x2` coarse cube, 8 sites, 12 links, 6 faces with one `F2` relation:

1. Exactly `32` of the `64` face assignments are consistent flux sectors -- those with an even number of `-1` faces -- and enumerating all `2^12` link-sign fields
   gives exactly those `32` holonomy patterns, with the one-particle spectrum constant on each pattern.
2. `E_N` of the all-`(+1)` sector is `0, -3, -4, -5, -6, -5, -4, -3, 0` and of the all-`(-1)` sector is `-N sqrt3` for `N <= 4` with its mirror, both exact.
3. At half filling `N = 4` the all-`(-1)` sector is the **unique** minimiser of all `32`, by `0.456067` to the next distinct value and by `4 sqrt3 - 6` to the plain
   sector. The unique minimiser is the plain sector at `N = 1, 7`, the two-flux class at `N = 2, 6` and the four-flux class at `N = 3, 5`; all `32` tie at `N = 0`
   and `N = 8`.

**Proof.** Item 1 solves the `F2` relations among the six face generators, realises each consistent assignment as a sign field and checks its holonomy face by face,
then enumerates the `4096` sign fields directly, `[numerical, 1e-12]` for the constancy of the spectrum within a pattern and exact for the pattern count. Item 2
diagonalises the two exact integer `8x8` matrices in `sympy` and sums the surds. Item 3 compares the `32` exact ladders entry by entry, with the tie counts
`32, 1, 3, 12, 1, 12, 3, 1, 32` and the minimiser's flux count `all, 0, 2, 4, 6, 4, 2, 0, all` printed by the runner.

**Reading, not theorem.** Eight sites and a choice of sign on each of six squares. With no particles, or with all eight sites full, every choice costs the same.
With one particle the plain arrangement is cheapest; with four -- one particle for every two sites -- the arrangement with a minus on every square is cheapest, and
by a clear margin. In between, other arrangements win. The cheapest sign pattern is a function of how many particles there are.

## Theorem 2 -- the uniform sectors on tori and open blocks

**Conclusion.** For the two uniform sectors on the coarse tori `4^3`, `4x4x6`, `6^3` and `8^3` and the open blocks `3^3` and `4^3`:

1. `sign(E_N(-) - E_N(+))` over `N = 1..V-1` is `+` below `N*`, `-` on the whole of `[N*, V - N*]` and `+` above: one contiguous window, and the difference is
   symmetric under `N -> V - N`. The values are `N* = 23, 30, 71, 171, 10, 22` in that order.
2. At `L = 4` both spectra are fixed exactly by an integer minimal-polynomial witness and integer power traces: `0 x20, +-2 x15, +-4 x6, +-6 x1` for the plain
   sector and `0 x8, +-2 x12, +-2sqrt2 x12, +-2sqrt3 x4` for the staggered one. Hence `E_32(-) - E_32(+) = 36 - 24 sqrt2 - 8 sqrt3 < 0` at half filling,
   `E_16(-) - E_16(+) = 48 - 24 sqrt2 - 8 sqrt3 > 0` at quarter filling, and the first sign change is at `N* = 23`, where the difference is
   `46 - 24 sqrt2 - 8 sqrt3`.
3. Where the sector is small enough to be formed from the `S_f` directly, the field read off the all-`(-1)` sector has holonomy `-1` on every plaquette and the same
   one-particle spectrum as the KS field, so the two labels name the same object here.

**Proof.** Item 2 evaluates the claimed minimal polynomial at the exact integer matrix, which vanishes over `Z`, and checks `tr M^k` for `k = 1..8` against the
claimed multiset, which fixes the multiplicities; the ladders and their difference are then exact sums of surds. Item 1 is `[numerical, 1e-9]` away from `L = 4`,
with `E_N = E_{V-N}` from the symmetry of a bipartite spectrum; item 3 likewise, and the `8^3` torus is evaluated from the Bloch formula, not a matrix.

**Reading, not theorem.** The same picture holds on every block tested. Below about a third filling the plain arrangement is cheaper, above about two thirds it
is cheaper again, and in the whole band between the two the minus-on-every-square arrangement is. The band is a single stretch, symmetric about half filling.

## Theorem 3 -- the Wilson-line caveat

**Conclusion.** The face stabilizers fix none of the three torus Wilson lines, so each sector is a family of eight link-sign fields, related by twists that change no
face. Minimising each uniform sector over its eight twists gives `E_{V/2} = -78.383672` against `-67.882251` on `4^3`, `-116.809009` against `-99.882251` on
`4x4x6` and `-258.857540` against `-218.564065` on `6^3`. The staggered sector at its **worst** twist still beats the plain sector at its best, by `3.92`, `10.15`
and `36.58` respectively. The twisted Bloch formulas `+-sqrt(6 + 2 sum_a cos q_a)` and `2 sum_a cos q_a`, with a half-integer momentum shift on each twisted axis,
reproduce all 48 twisted real-space spectra of those three tori.

**Proof.** Both statements are `[numerical, 1e-9]`: the eight twisted fields are built explicitly per sector, diagonalised, and compared, and the Bloch spectra are
compared eigenvalue by eigenvalue against the real-space ones.

**Reading, not theorem.** A sign on each link is not the whole story on a ring: besides the sign around every small square there is a sign around each way through
the box, and the squares do not fix those. This is a real freedom, and it moves the numbers. It does not move the comparison: the worst way of running the
minus-on-every-square field around the box is still cheaper than the best way of running the plain one.

## Theorem 4 -- the Cauchy-Schwarz certificate on the 4^3 torus

**Conclusion.**

1. The `4^3` coarse torus is bipartite, coloured by `(-1)^{v_1+v_2+v_3}`, with every degree `6`. So for **any** link-sign field on it the integer hopping matrix
   satisfies `tr M^2 = 2|E| = 6V = 384` and `D M D = -M` for the colour involution `D`, hence has a spectrum symmetric about `0`.
2. The `V/2` lowest levels are therefore the negatives of the `V/2` highest, their squares sum to `(1/2) tr M^2 = 3V = 192`, and Cauchy-Schwarz gives
   `E_{V/2} = -sum |lambda| >= -sqrt((V/2)(3V)) = -V sqrt(3/2) = -32 sqrt6 = -78.383672`, with **equality exactly when every `|lambda| = sqrt6`**.
3. The all-`(-1)` sector at its optimal twist satisfies `M^2 = 6 I` exactly, as a `64x64` integer matrix identity, so its spectrum is `+-sqrt6` with multiplicity
   `32` each and its half-filling energy attains the bound. It is therefore a **global minimiser at half filling over all `2^192` link-sign fields on that torus**.
4. The same bound reads `-117.5755` on `4x4x6`, `-264.5449` on `6^3` and `-627.0694` on `8^3`, and there the all-`(-1)` sector misses it by `0.766`, `5.687` and
   `15.26`: its spectrum `+-sqrt(6 + 2 sum_a cos q_a)` is not flat on those tori. Global minimality is a theorem on `4^3` and a search result elsewhere.

**Proof.** Items 1 and 3 are zero-tolerance integer matrix identities, item 1 on 52 fields including both uniform ones and item 3 on the single field named. Item
2 applies Cauchy-Schwarz to the `V/2` numbers `|lambda|`, whose sum of squares item 1 pins. Item 4 evaluates the bound and the exact Bloch energies, `[1e-9]`.

**Reading, not theorem.** Two facts about the box fix a floor no arrangement of signs can go below: every site has six neighbours, so the levels have a fixed total
spread, and the box is two-colourable, so they come in plus-minus pairs. Spreading a fixed total spread over a fixed number of levels is cheapest when every level
has the same size. On the smallest box the minus-on-every-square field, run the right way around the box, does exactly that: every level is the same size. So it is
not merely better than everything tried -- it is as good as anything could be.

## Theorem 5 -- the searches

**Conclusion.** At half filling on the tori `4^3` and `4x4x6`, all `[numerical, 1e-9]` and all **search results, not theorems**:

1. `2000` random link-sign fields per torus, each realising a consistent sector as drawn, and a `500`-field subsample with each field minimised over its own eight
   twists: `0` of `2500` beats the all-`(-1)` sector on either torus.
2. The structured sectors with flux only on the `xy`, `xz` or `yz` plaquettes, `xy` flux on alternating `x` planes, and flux on the `xz` and `yz` plaquettes
   together are consistent and all strictly above the all-`(-1)` sector. Flux on the even-parity faces, `xz+yz` on alternating planes, and a single-face flip off
   the all-`(-1)` sector are **inconsistent**: every face lies in two cube relations, so no sector differs from another in one face alone.
3. Greedy single-link descent from `24` random restarts per torus never beats the all-`(-1)` field at its optimal twist. On `4^3` its best equals that field
   exactly, `3` of `24` restarts reaching it. On `4x4x6` its best stays above, at `-116.134` against `-116.809`.
4. That field is a strict local minimum: every one of the `192` and `288` single-link flips raises `E_{V/2}`, by at least `0.426844` and `0.365352`.

**Proof.** Direct evaluation of `E_{V/2}` for each field, with the consistency of a structured assignment decided by the `F2` relations among the `S_f` before any
diagonalisation. The negative statements are statements about the samples drawn and the descent runs made, at the seeds the runner fixes, and are not claims about
the whole space.

**Reading, not theorem.** Two thousand random arrangements, five patterned ones, and a descent free to change any single link: nothing beats the
minus-on-every-square arrangement, and on the smallest box the descent walks straight back to it. Away from that box this is evidence, not proof.

## Theorem 6 -- the thermodynamic limit and the crossing filling

**Conclusion.** From the exact Bloch formulas -- `E = +- sqrt(6 + 2 sum_a cos q_a)` for the all-`(-1)` sector, fourfold, and `2 sum_a cos q_a` for the all-`(+1)`
one -- evaluated at `L = 4, 8, 16, 32, 64, 96` and by converged Brillouin-zone quadrature:

1. At half filling `e(+) = -1.00241973` and `e(-) = -1.19380112`, a difference of `-0.19138139 |t|` per coarse site in favour of the staggered sector.
2. At quarter filling the difference is `+0.07909` per coarse site at `L = 96`, in favour of the plain sector.
3. The crossing filling `n* = N*/V` settles to `0.339659` along the sequence `0.3594, 0.3287, 0.3340, 0.3380, 0.3411, 0.3398, 0.3394, 0.3397, 0.3396, 0.3397` at
   `L = 4, 6, 8, 12, 16, 24, 32, 48, 64, 96`, and the window ends at the mirror `1 - n* = 0.660341`.

**Proof.** Item 1 is `[numerical]` at converged quadrature: the reduced-grid Brillouin-zone integrals at `M = 600, 1200, 2400` agree to `1e-8` in `e(-)` and settle
to the digits quoted in `e(+)`. Items 2 and 3 are `[numerical, 1e-9]` on the `L = 96` Bloch grid, `n*` read off it by linear interpolation of the difference.

**Reading, not theorem.** In a large box the two arrangements differ by a fixed amount per site, not a vanishing one. Fill a third of the sites or fewer and the
plain arrangement is cheaper; fill more, up to two thirds, and the other is cheaper, by about a fifth of a hopping unit per site at half filling.

## Corollary -- what this says about the framework's kinetic form

Within the setting declared above, and on the finite blocks and tori named:

1. The law's own hopping term selects the framework's staggered kinetic form at half filling. No face term is supplied, and none is needed: the term already in the
   law does the selecting, uniquely on the `2x2x2` cube, provably against all link-sign fields on the `4^3` torus, and by a fixed amount per site in the limit.
2. The selection is a property of the **matter density**. Below `n* ~ 0.3397` and above `1 - n*` the plain sector is cheaper; between them the staggered sector is.
   At `N = 0` -- the record vacuum, no matter present -- every sector ties exactly, and at `N = V` they tie again.
3. So the question "which sector" is answered by "how much matter", and the filling is a supplied datum, not something this note derives. What the face-transport
   note calls a free choice under the law as written is free only until a matter density is named; once one is, the hopping term already in the law fixes the sector.
4. The `-J sum_f S_f` term that note describes is not needed for the half-filled case and is not supplied here. Nothing below the level of the hopping term is
   added, and no coefficient, coupling, rate or unit appears anywhere in this note.

**Reading, not theorem.** With no matter present, the sign on the squares costs nothing either way. Put in enough matter, about a third of the sites or more, and
the arrangement with a minus on every square is the cheapest by a fixed amount per site. That arrangement is the framework's staggered kinetic form: it is not
chosen by the law's wording; it is chosen by the matter's own energy.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign fields and the filling are declared objects, and the theorems are about them.
- No update rule, formation site, formation rate, coupling, mass, absolute unit or dynamical clause appears. The filling is supplied, never derived.
- No claim is made that a Lieb-type flux-phase theorem holds on the cubic lattice. The certificate of Theorem 4 is a Cauchy-Schwarz bound on one named torus.

## Interfaces named for other lanes, not moved here

- **The filling as a supplied datum.** Every statement here is conditional on `N`. Which filling the coarse lattice actually carries is a science question a lane
  owning the matter density must answer; nothing here narrows it, and Corollary item 3 states exactly what such a lane would have to supply.
- **Interacting terms.** Only free nearest-neighbour hopping is compared. A four-fermion term, or any interaction, could order the sectors differently, and no such
  term is examined.
- **Global minimality beyond `4^3`.** Theorem 4 is a theorem on the `4^3` torus and on the `2x2x2` cube only. On `4x4x6`, `6^3` and `8^3` the bound is missed and
  the statement is the search result of Theorem 5. A lane wanting global minimality there must supply a different certificate.
- **The Wilson-line convention.** Theorem 3 makes the twist explicit; which twist a physical setting selects is not decided here.
- **The many-body energetics.** Only the one-particle ladder `E_N` is used, the ground state of the free problem; what an interacting ground state prefers is
  untouched.

## Remaining live routes

1. Larger blocks and other geometries. The four tori and two open blocks named are what is proved; nothing is claimed beyond them.
2. Other fillings on the cube. Theorem 1 names a minimiser for each `N` on the `2x2x2` cube; the corresponding statement on larger clusters is not made.
3. Finite temperature. Everything here is a ground-state energy at fixed particle number, and `N = 0` and `N = V` tie exactly across all sectors.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one mode per coarse vertex, BK superfast encoding on it, free nearest-neighbour hopping only; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
objects: KS eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}; plain +1; S_f the face stabilizer; flux sector = consistent choice of S_f eigenvalues; E_N = sum of the N lowest levels of M_ij = eta_ij
cube_2x2x2: 32 of 64 face assignments consistent (flux counts 0, 2, 4, 6), confirmed by all 2^12 link fields giving exactly 32 holonomy patterns; E_N(+1) = 0, -3, -4, -5, -6, -5, -4, -3, 0; E_N(-1) = -N sqrt3 for N <= 4 and mirror
cube_minimisers: N = 4 unique all-(-1), margin 0.456067 to the next distinct value and 4 sqrt3 - 6 to plain; ties 32, 1, 3, 12, 1, 12, 3, 1, 32 and minimiser flux counts all, 0, 2, 4, 6, 4, 2, 0, all
uniform_window: tori 4^3, 4x4x6, 6^3, 8^3 and open blocks 3^3, 4^3; sign(E_N(-) - E_N(+)) is + below N*, - on [N*, V - N*], + above, symmetric under N -> V - N; N* = 23, 30, 71, 171, 10, 22
exact_L4: E_32(-) - E_32(+) = 36 - 24 sqrt2 - 8 sqrt3; E_16(-) - E_16(+) = 48 - 24 sqrt2 - 8 sqrt3 > 0; first sign change N* = 23 at 46 - 24 sqrt2 - 8 sqrt3
wilson: S_f fix no torus Wilson line; twist-minimised E_{V/2} = -78.383672 vs -67.882251 (4^3), -116.809009 vs -99.882251 (4x4x6), -258.857540 vs -218.564065 (6^3); staggered at its worst twist beats plain at its best by 3.92, 10.15, 36.58
certificate: 4^3 bipartite, all degrees 6, so tr M^2 = 6V = 384 and D M D = -M for any link field; E_{V/2} >= -V sqrt(3/2) = -32 sqrt6 = -78.383672, equality iff every |lambda| = sqrt6; all-(-1) at its optimal twist has M^2 = 6 I exactly, spectrum +-sqrt6 x32 each, attains the bound: global minimiser over all 2^192 fields
certificate_gaps: bound -117.5755, -264.5449, -627.0694 on 4x4x6, 6^3, 8^3, missed by 0.766, 5.687, 15.26
searches: 2000 random fields per torus plus a 500-field Wilson-minimised subsample, 0 of 2500 beating all-(-1) on 4^3 or 4x4x6; five structured sectors consistent and all above; even-parity faces, alternating xz+yz and any one-face flip inconsistent; 24 greedy restarts per torus never beat it and on 4^3 return it; strict local minimum, smallest single-flip rise 0.426844 and 0.365352
thermodynamic: e(+) = -1.00241973, e(-) = -1.19380112 at half filling, difference -0.19138139 |t| per coarse site; +0.07909 at quarter filling at L = 96; n* -> 0.339659, mirror 0.660341
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=19 FAIL=0
```

## Proof boundary

The content is **free nearest-neighbour hopping only**, on **finite** clusters, at a **supplied** filling. No interaction, mass, coupling, rate, temperature or
absolute unit appears, and no dynamical clause is proposed. Nothing here is derived from the four axioms.

Global minimality over all link-sign fields is a **theorem on exactly two clusters**: the open `2x2x2` cube, by exhaustion of all `2^12` fields, and the `4^3`
coarse torus, by the Cauchy-Schwarz certificate whose equality case the all-`(-1)` sector meets. On `4x4x6`, `6^3` and `8^3` the bound is missed by the stated gaps
and the corresponding statement is a **search result** -- a statement about the samples drawn and the descent runs made at the runner's fixed seeds, not about the
whole space. Theorem 3 and Theorem 5 are search results throughout and are labelled so wherever they are used.

No Lieb-type flux-phase theorem is claimed for the cubic lattice. Lieb's theorem is planar; it is named as background only and no step below invokes it.

The three torus **Wilson lines** are gauge-invariant data that no face stabilizer fixes, so "the sector" alone does not name a link-sign field on a torus. Every
torus comparison here is either at the stated twist or minimised over all eight, and Theorem 3 records both. Theorem 5's `4x4x6` descent result is that the best
restart stays *above* the all-`(-1)` field, not that it reaches it; only the `4^3` descent returns that field exactly.

The identification of the all-`(-1)` sector with the staggered kinetic form is up to a **site relabelling**, and is verified spectrally here only on the clusters
small enough for the sector to be formed directly from the `S_f`; on the larger tori the KS field is used and its holonomy is `-1` on every face by construction.

## Review record

An honest auditor should come away with: one exhaustive finite-cluster theorem naming the staggered sector as the unique half-filling minimiser on the `2x2x2`
cube; one exact-surd statement of where the two uniform sectors cross on four tori and two open blocks, with a single contiguous window symmetric about half
filling; one genuine certificate -- a Cauchy-Schwarz bound whose equality case the staggered sector meets exactly on the `4^3` torus, making it a global minimiser
there over all `2^192` link-sign fields; a clearly labelled band of search results away from that torus; and one honest limit, that the whole statement is
conditional on a filling this note does not derive.

The three things most likely to be over-read are flagged in the proof boundary: global minimality holds as a theorem on two clusters only; the `4x4x6` descent does
not reach the staggered field, it merely fails to beat it; and no cubic-lattice flux-phase theorem is claimed. This note is self-contained:
`upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the three context notes in "Imports and authority" are
plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=19 FAIL=0`, runtime under the
declared `120` seconds, stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence
gates; independent audit remains a separate lane.
