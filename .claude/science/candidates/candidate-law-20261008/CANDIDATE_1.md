# Candidate 1: the whole law on one page (test settings, 2026-10-08)

**Status: a test setting, not adopted.** Nothing here enters the axiom memo. Every piece reuses an existing repo construction, cited below. All of those are unaudited and same-family.

**Settings (code Q L O B X):**
- **Q, hypercubic tick:** time is a lattice direction, with the same step as space.
- **L, local frames:** turns act up to a site-local U(1) frame. This is main's kinetic-class reading.
- **O, continuous fields:** each site carries continuous variables plus fermion modes.
- **B, records are Bell-type beables:** the fermion occupations.
- **X, gravity is an explicit linear spin-2 field.**

**Why this one.** It is rank 1 on physics alone and rank 3 once axiom fit is included (see `DECISION_MATRIX.md`). It is also the only top-ranked combination whose every sector already has a working construction, so it is the only one that can be written down completely today.

Its main job is to test the walls that do not depend on what a site holds:
- chirality;
- one cone;
- nonlinear gravity on a fixed grid;
- generations.

If it dies on one of those, qubits would not have saved it. If it survives, the next question is a separate one: can qubits produce these fields? Quantum link models are the known kind of bridge.

## 1. Grid and roles

- **Grid.** The sites are the points of Z³. Time steps by τ.
- **Roles.** Each site has a role from its position mod 2 relative to one of 8 translates t:
  - vertex: no odd coordinate;
  - edge: one odd coordinate;
  - face: two odd coordinates;
  - cube: three odd coordinates.
- **The translate is chosen by the state, not the law.** t is a conserved state label, as in A25 F6. The law itself is covariant under every translation and turn, so no site is privileged by the law.
- **Turns.** They act with the Kawamoto–Smit sign field, and translations act projectively. This is main's `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`, under which all 24 turns survive.

## 2. What each role holds

| Role | Matter | Light | Gravity |
|---|---|---|---|
| vertex | one fermion mode ψ_v | (Gauss-law site) | h_ii, π_ii (i = 1..3) |
| edge | — | U(1) rotor θ_e with integer E_e | — |
| face | — | (flux is the plaquette of θ) | h_ij, π_ij (i<j) |
| cube | — | — | — (spare) |

Non-abelian links are deferred: the first kill round runs with U(1) only. On qubits, SU(2) needs 2 and SU(3) needs 3 qubits per link (main `DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS_...`).

## 3. The law

**The step.** The real-time step is U_τ = e^{−iτH}, with H = −(1/a) log T. Here T is the transfer matrix of a 4D lattice action that is hypercubic with a_t = a_s. The hypercubic form is the Q setting, and K7 tests whether it holds in every sector.

The Kogut–Susskind forms below are the leading terms of −(1/a) log T and become exact as a_t → 0.

**Correction after K7a (2026-10-08), see `TEST_LOG.md`.**
- **Gravity has no positive transfer matrix.** The conformal mode makes Q indefinite, so −(1/a) log T cannot define gravity. The real-time law is the reversible leapfrog itself, built from each sector's hypercubic Euclidean action. The hypercubic setting is a symmetry of those actions, not a transfer-matrix construction.
- **The tick.** Hypercubic means a_t = 2 fine edges. A25's leapfrog is unstable at that step, so the stable real-time scheme at a_t = a_s is still owed.
- **Matter in the hypercubic form** is 4D staggered fermions (4 tastes, two-step transfer matrix), not the 3D H_ψ below. In that form K2a found no lattice-symmetry mirror selector.

The H_ψ below is the continuous-time (H) variant's matter.

H = H_E + H_B + H_ψ + H_g + H_int, with:
- **Light.** This is Kogut–Susskind compact U(1):
  - H_E = (g²/2) Σ_e E_e²
  - H_B = −(1/g²) Σ_f cos θ_f
- **Matter.** These are staggered fermions on the coarse lattice 2Z³ + t, hopping through the edge between:
  - H_ψ = ½ Σ_{v,μ} η_μ(v) (i ψ_v† e^{iθ_{v,μ}} ψ_{v+2μ} + h.c.) + m Σ_v ε(v) ψ_v†ψ_v
  - Sources: main `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` and `EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_...2026-09-03.md`.
- **Gravity.** This is A25's "Yee for spin-2" (`ai/probes` campaign 8 A25):
  - H_g = π:π − ½(tr π)² + ¼ h:inc(h)
  - It gives two tensor polarizations at one speed, no doubler, exact linearized constraints, and GR's kinetic weights (A23).
- **Coupling.** This is the stress coupling of A26, with H_int = −½ Σ h_ij T^ij. T is the lattice stress of matter and light. A23 D17 needs it to be conserved.

**Constraints.**
- **Gauss law:** G_v = Σ_μ (E_{v,μ} − E_{v−2μ,μ}) − (ψ_v†ψ_v − (1 − ε(v))/2) = 0, with a staggered background charge.
- **Gravity:** the linearized momentum and Hamiltonian rows (A25 S3).

**Tree-level speeds are set equal.**
- photon c (Yee/KS);
- matter c (the kinetic-isotropy primitive);
- graviton c (A25, with α = K/4 as in blocks 134–146).

K7 tests whether interactions keep them equal.

## 4. Records

- **What a record is.** The record configuration is n_v ∈ {0,1}, the fermion occupations at vertex sites. One record per site is Pauli exclusion.
- **How records move.** They jump between steps with Bell/Vink discrete-beable probabilities, set by the wave and U_τ (Bell 1986; Vink 1993).
- **Born statistics.** If records start Born-distributed, they stay Born-distributed (equivariance).
- **Readout.** Only records are read. Photons and gravitons carry no records and are read only through matter.
- **Count.** The record count is fixed: the filled sea holds records, and holes are antimatter.

## 5. Where it strains the axioms (stated, not hidden)

| Axiom sentence | Strain |
|---|---|
| Qubit: "M_2(C)" per site | **Set aside for this test**: continuous fields plus a fermion mode. The qubit question becomes the substrate bridge. |
| Record: "Records form", "records are permanent" | Beables exist and move. The count is conserved, not rising. Formation is a sea record leaving a hole. |
| Admissibility: nearest-neighbour conditions | The jump odds depend on the joint wave, which is nonlocal. That is the price of CHSH 2.83 (T08), and matches the owner's joint-phases point (10-04). |
| "A state is a configuration of records" | The wave is a second ingredient, as in every candidate with B. |
| Lattice: "No site is privileged" | Met. The law is covariant, and the role translate lives in the state. |
