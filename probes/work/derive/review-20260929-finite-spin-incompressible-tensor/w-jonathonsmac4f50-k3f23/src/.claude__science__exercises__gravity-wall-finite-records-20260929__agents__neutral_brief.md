# Neutral brief: the gravity wall

Repository root: /Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790 (branch of PR #9363; main is origin/main). Paths below are relative to it.

### Precise version

- **Target.** A local (finite-range, analytic-symbol), stable
  (positive-semidefinite) harmonic model on the supplied tensor complex
  (vector stencil G, scalar stencil S, six slots per cell). The slots are
  finite, meaning finite-dimensional local Hilbert spaces, and the scalar
  (time) rule is exact. Its low-energy spectrum must be Einstein's linear
  spectrum: two pure-TT modes with ω ∝ |q| in every direction, and no other
  gapless mode.
- **Status.** Excluded, whatever the residual symmetry (probes 10–21; bounded
  theorems, unaudited):
  - exact transverse rules give ω = O(q²);
  - both TT polarisations linear in every direction force a linear mode
    with helicity ±1 weight on a dense set of directions.
- **What does not count as closure:** approximate Lorentz invariance with
  unequal partner speeds; a gapped tensor; ω ∝ q^n with n > 1; a spectrum
  with extra gapless modes.
- **Positive comparator.** The same complex with non-compact canonical pairs
  (continuous, unbounded h and π) gives exactly Einstein's linear spectrum
  (2026-09-24, unaudited).
- **The sharpest one-line form.** Einstein's linear graviton, in the
  comparator, is built from canonical pairs [h, π] = i. No finite-dimensional
  site can carry an exact canonical pair (the landed 2026-05-02 no-go, by
  trace). Every finite approximation tried so far breaks one of the
  graviton's two properties: speed or purity.
- **Progress would be:**
  - a finite-slot or one-qubit-per-site model, beyond harmonic order or in a
    strongly correlated phase, with Einstein's linear spectrum;
  - or a reformulation in which gravity does not need a lattice graviton
    mode;
  - or a proof that the wall is equivalent to one named premise (the price).
- **Leaned on:**
  - the supplied tensor complex and its two rules;
  - the harmonic comparators;
  - Einstein's linear spectrum as the target;
  - the landed CCR no-go;
  - the June induced-gravity lane;
  - panel strategy.

### What the axioms say / what we supplied / what was proved

| What the axioms say | What we supplied | What was proved |
| --- | --- | --- |
| Z³ with nearest-neighbour adjacency, translations and cubic rotations; no site privileged | a tensor carrier on Z³ with six slots per cell, and the stencils G and S | ω ∝ k² or k³ with exact rules (09-14) |
| one site's possibilities have algebraic presentation M₂(C) | finite slots of spin S, or qubit slots (not one qubit per site) | no exact canonical pair on M₂(C) (05-02) |
| one nearest-neighbour admissibility rule fixes each site's odds | exact local balance laws (Gauss laws) as the reading of that rule | finite slots with an exact additive law: the moves' low moments vanish (probes 10, 15, 17) |
| records form, one per site, permanent; only records are read | harmonic (small-wave) models with stable quadratic forms; local terms | light-like TT brings a light-like ±1 mode, any symmetry (probes 20, 21) |
| Admissibility is not a dynamics axiom; there is no time metric | a Hamiltonian, a time rule, a DeWitt kinetic term, Einstein's spectrum as the target | both rules soft: gapped (probe 18) |
| — | continuous canonical pairs (the comparator) | continuous pairs: Einstein's linear spectrum (09-24) |
| — | a metric degree of freedom (June lane) | given one, the matter induces G ~ a² (06-17) |
| — | tick rates and lengths per site (source-link clause C1, blocks 53–62) | the lapse algebra closes at linear order only at β = −α (112) |

**Reading.** Every entry in the middle column is supplied. The axioms say
nothing about gravity, dynamics or a metric. So the wall presses on the
supplied tensor-complex reading. It says that reading, built from finite
parts, cannot produce Einstein's linear graviton. It does not say the axioms
cannot. The middle column is also where the routes are.


## The ledger

"LB" marks whether the row is load-bearing: yes, or no (the wall survives
without it).

| ID | Kind | Assumption, in plain words | Where the wall uses it | What if wrong? | Already tested? | Cheapest test | Owner decision? | LB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | axiom | The grid is fixed: Z³, with fixed neighbours | AX:35; every probe's lattice | A dynamical grid : the metric could be the connection pattern, with no fixed background | no | none known | yes | yes |
| A2 | axiom | Each site's possibilities have algebraic presentation M₂(C), which is finite | AX:44; CCR:54–60 | Continuous per-site variables : the comparator (C24) works | the comparator, yes | — | yes | yes |
| A3 | axiom | One nearest-neighbour admissibility rule fixes each site's odds; it is not a dynamics axiom | AX:51, 114 | If it could supply dynamics with a metric, the rule itself might carry gravity | no | derive a Hamiltonian from the rule (open gate) | — | no: the wall is about the supplied dynamics |
| A4 | axiom | Records: one per site, permanent, the only readable things | AX:67 | Gravity from records' collective statistics (entanglement, counts) instead of from a wave field | probe 19 (formation counts), probe 7 | — | — | no: records do not enter the harmonic proofs |
| S1 | supplied model | Gravity is carried by a symmetric tensor on the lattice, a lattice metric h_ij and its momentum, with the stencils G and S | P21:96; P10:90 | Gravity need not be a local tensor field at all: an equation of state (Jacobson), entanglement geometry, or an induced effective metric | the June lane induced the action but posited the metric | Is the lattice's entanglement first law local?  | yes | yes |
| S2 | supplied model | Slots are finite: finite-dimensional local spaces | P21:96; P17 | Continuous slots give Einstein (C24); large spin S approaches them | probe 14 (S ≥ 2), large S (panel 3) | — | yes | yes |
| S3 | supplied model | The time (scalar) rule is exact | P21:96; P20:84 | If soft, everything is gapped (P18 D) | probe 18 | — | — | yes |
| S4 | method | Harmonic level: small waves around a state with a stable quadratic form | P20:84; P21:96 | Strongly correlated phases, which emergent photons need (quantum spin ice's linear photon from spin-½), might give linear gravitons | exact sum rules (P10) hold in every state: they need χ = O(q²) (incompressibility) | Does any finite-slot state have an incompressible TT channel? P11: only composites, with partners | yes | yes |
| S5 | method | Locality: finite range and analytic symbols | P20:84 | Non-local terms could stiffen TT alone: X(0) = m² P_TT(q̂) is non-analytic | panel 4 (canonical lens) named it | — | — | yes |
| S6 | method | On-site (q-independent) stiffness breaks the momentum rule | P20:84 (D) | Derivative or two-field breaking could avoid the TT-plane argument | not tested (P20 N7) | classify q-dependent breaking terms | — | partly |
| S7 | supplied model | Translation invariance and cubic symmetry of the model | P20; P21 | A crystalline or disordered record background might change the mode counting | no | — | — | partly |
| S8 | target | "Gravity works" means Einstein's linear spectrum: two TT modes at light speed and nothing else gapless | P21:1–40 | Weaker requirement: gravity needs only universal coupling to energy, and wave speed and polarisations within observational bounds. Partners might be allowed if they decouple or are slow enough | no | Do helicity ±1 partners couple to conserved static sources?  | yes: changes whether the broken branch is dead | yes |
| S9 | supplied model | One of the two storage assignments (momentum or metric diagonal) | P17 | Mixed storages keep only part of the rules (P17: 15/3/1 counts) | P17 | — | — | no |
| S10 | reading | The Hamiltonian formulation, with a separate time; a fixed foliation | every probe | A covariant, spacetime-lattice formulation (a Z⁴ event lattice) might change the counting | no (the formation 3+1 lead exists) | — | — | partly |
| S11 | reading | The qubit site is the fundamental carrier of gravity's variables | S1–S2 | Gravity's variables could be collective: many sites per metric component (coarse-grained record densities) | P11 and P16 (composite of photon fields) | — | — | partly |
| S12 | supplied model | Continuous comparator is the only positive reference | C24 | Other positive references: Gu–Wen, Xu, CDT, LQG semiclassical limits | literature only | — | — | no |

