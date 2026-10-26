# Step 2 — load-bearing assumptions; step 3 — reduction

Abbreviations for paths:
- **P10** `docs/ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_…_2026-09-28.md`
- **P15** `docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_…_2026-09-28.md`
- **P17** `docs/AN_EXACT_ADDITIVE_GAUSS_LAW_ON_DISCRETE_SLOTS_…_2026-09-28.md`
- **P18** `docs/BREAKING_THE_MOMENTUM_RULE_…_2026-09-29.md`
- **P20** `docs/EVERY_GAUSS_LAW_COMPATIBLE_MOVE_…_2026-09-29.md`
- **P21** `docs/THE_TENSOR_COMPLEX_ON_FINITE_SLOTS_…_2026-09-29.md`
- **C24** `docs/TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_…_2026-09-24.md`
- **CCR** `docs/NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md`
- **AX** `docs/MINIMAL_AXIOMS_2026-06-29.md`

## The ledger

"LB" marks whether the row is load-bearing: yes, or no (the wall survives
without it).

| ID | Kind | Assumption, in plain words | Where the wall uses it | What if wrong? | Already tested? | Cheapest test | Owner decision? | LB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | axiom | The grid is fixed: Z³, with fixed neighbours | AX:35; every probe's lattice | A dynamical grid (option B): the metric could be the connection pattern, with no fixed background | no | none known (option B has no bounded test) | yes (B) | yes |
| A2 | axiom | Each site's possibilities have algebraic presentation M₂(C), which is finite | AX:44; CCR:54–60 | Continuous per-site variables (option A): the comparator (C24) works | the comparator, yes | — | yes (A) | yes |
| A3 | axiom | One nearest-neighbour admissibility rule fixes each site's odds; it is not a dynamics axiom | AX:51, 114 | If it could supply dynamics with a metric, the rule itself might carry gravity | no | derive a Hamiltonian from the rule (open gate) | — | no: the wall is about the supplied dynamics |
| A4 | axiom | Records: one per site, permanent, the only readable things | AX:67 | Gravity from records' collective statistics (entanglement, counts) instead of from a wave field | probe 19 (formation counts), probe 7 | — | — | no: records do not enter the harmonic proofs |
| S1 | supplied model | Gravity is carried by a symmetric tensor on the lattice, a lattice metric h_ij and its momentum, with the stencils G and S | P21:96; P10:90 | Gravity need not be a local tensor field at all: an equation of state (Jacobson), entanglement geometry, or an induced effective metric | the June lane induced the action but posited the metric | Is the lattice's entanglement first law local? (Route E) | yes: a new route | yes |
| S2 | supplied model | Slots are finite: finite-dimensional local spaces | P21:96; P17 | Continuous slots give Einstein (C24); large spin S approaches them | probe 14 (S ≥ 2), large S (panel 3) | — | yes (A) | yes |
| S3 | supplied model | The time (scalar) rule is exact | P21:96; P20:84 | If soft, everything is gapped (P18 D) | probe 18 | — | — | yes |
| S4 | method | Harmonic level: small waves around a state with a stable quadratic form | P20:84; P21:96 | Strongly correlated phases, which emergent photons need (quantum spin ice's linear photon from spin-½), might give linear gravitons | exact sum rules (P10) hold in every state: they need χ = O(q²) (incompressibility) | Does any finite-slot state have an incompressible TT channel? P11: only composites, with partners | yes: C (strongly correlated) | yes |
| S5 | method | Locality: finite range and analytic symbols | P20:84 | Non-local terms could stiffen TT alone: X(0) = m² P_TT(q̂) is non-analytic | panel 4 (canonical lens) named it | — | C | yes |
| S6 | method | On-site (q-independent) stiffness breaks the momentum rule | P20:84 (D) | Derivative or two-field breaking could avoid the TT-plane argument | not tested (P20 N7) | classify q-dependent breaking terms | — | partly |
| S7 | supplied model | Translation invariance and cubic symmetry of the model | P20; P21 | A crystalline or disordered record background might change the mode counting | no | — | — | partly |
| S8 | target | "Gravity works" means Einstein's linear spectrum: two TT modes at light speed and nothing else gapless | P21:1–40 | Weaker requirement: gravity needs only universal coupling to energy, and wave speed and polarisations within observational bounds. Partners might be allowed if they decouple or are slow enough | no | Do helicity ±1 partners couple to conserved static sources? (Route M) | yes: changes whether the broken branch is dead | yes |
| S9 | supplied model | One of the two storage assignments (momentum or metric diagonal) | P17 | Mixed storages keep only part of the rules (P17: 15/3/1 counts) | P17 | — | — | no |
| S10 | reading | The Hamiltonian formulation, with a separate time; a fixed foliation | every probe | A covariant, spacetime-lattice formulation (a Z⁴ event lattice) might change the counting | no (the formation 3+1 lead exists) | — | — | partly |
| S11 | reading | The qubit site is the fundamental carrier of gravity's variables | S1–S2 | Gravity's variables could be collective: many sites per metric component (coarse-grained record densities) | P11 and P16 (composite of photon fields) | — | C | partly |
| S12 | supplied model | Continuous comparator is the only positive reference | C24 | Other positive references: Gu–Wen, Xu, CDT, LQG semiclassical limits | literature only | — | — | no |

**Blind-check result.** See `WALL.md`, under "Blind check". The restatement
matched, and six phrasings were fixed.

## Route clusters

| Route | Assumptions challenged | Why this might open the wall | Expected artifact | Risk | First test |
| --- | --- | --- | --- | --- | --- |
| A — continuous geometry per site | A2, S2 | The comparator works, and the June lane induces the action | a candidate axiom and the second-order lapse algebra (A1) | Nonlinear closure fails on a fixed grid; "records are the grain" is lost | programme A's step A1 (specified in the map) |
| B — recorded adjacency | A1 | No fixed background, so the local spin-2 no-go does not apply | a first bounded model | No known test; the Record wording becomes circular | find a minimal dynamical-graph model with a known graviton limit |
| C — strongly correlated phase | S4, S11 | Emergent photons are linear only beyond harmonic order | a model and state with an incompressible TT channel | The exact sum rules already demand incompressibility; only composites are known | a small-system test of TT incompressibility |
| E — gravity as an equation of state of entanglement | S1 | Jacobson-type: Einstein's equation from the first law of entanglement plus an area law, with no graviton slot at all | a lattice check of the ingredients | Needs a local modular Hamiltonian and Lorentz invariance at long distances | check the entanglement first law and area law for the lattice walker's ground state |
| M — reframe the target | S8 | If the ±1 partners do not couple to conserved sources, the broken branch may be physics, not a failure | a coupling computation, then observational bounds | Partners couple through momentum flux; bounds from gravitational-wave speed and binary pulsars | a symbolic coupling test |

## Step 3 — reduction

1. **Make the requirement less wrong.** What gravity must do, observationally:
   - couple universally to energy;
   - give a 1/r potential;
   - bend light twice as much as the Newtonian estimate;
   - radiate like a two-polarisation light-speed wave, to about 10⁻¹⁵ in
     speed (GW170817), with no measurable extra polarisations.

   "Einstein's linear spectrum exactly" is stronger than any single
   observation, but the observations pin it to high precision. The
   requirement is therefore not obviously too strong. Route M tests whether
   the extra shake is visible to matter at all.
2. **Delete.** The wall survives without records (A4), without Admissibility
   (A3), without the choice of storage (S9) and without the comparator (S12).
   It needs A1, A2 or S2, S1, S3, S4, S5, and the target S8.
3. **Shrink.** The smallest object where it bites is one wavevector's
   symbol. A symmetric 3×3 tensor h and its conjugate have to support two
   linear modes of one helicity. On finite slots, a conserved additive charge
   makes every allowed move lose its lowest moments. The kinetic term then
   starts at q², and its first moments feed helicity ±1 at least a quarter as
   much as TT (P20 B). That is a 6 × 6 linear-algebra fact about first
   moments, already built and checked (P20 A, B, H2). The irreducible core
   is two facts:
   - a finite site has no exact canonical pair (CCR);
   - an exact conserved local charge on bounded variables forces the moves'
     moments to vanish (P10, P15, P17).
4. **Split.** Two bits:
   - a representation bit: finite versus continuous local variables;
   - a target bit: must the extra modes be absent, or only invisible?

   Routes A, B and C attack the first bit; route M attacks the second. Route
   E dissolves both by not using a lattice graviton mode.
5. **Price it.** Within the tested class (harmonic, local, stable, time rule
   exact, the supplied complex), Einstein's linear spectrum holds if and only
   if each slot carries an exact canonical pair:
   - "if": C24;
   - "only if": no finite site carries one (CCR), and every finite
     approximation fails (probes 10–21).

   That is the exact price inside the supplied reading: an infinite local
   dimension. Outside that reading, S1 and S4, the price is unknown.
