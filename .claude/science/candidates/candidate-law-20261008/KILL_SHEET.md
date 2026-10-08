# Kill sheet for Candidate 1 (pre-registered 2026-10-08)

**Status: written before any test runs.** The pass and fail lines below are fixed now, before any results. A changed criterion must be dated and justified here, and must never be changed after its test is seen.

**Rule for recording a FAIL.** Three things are needed:
1. the computation;
2. the supervisor's own check of it;
3. one referee: codex sol preferred, or same-family Sonnet labelled as such.

The outcome then goes into `RESULTS` in `decision_matrix.py`, keyed by the settings the diagnosis blames. The next survivor in the ranking becomes Candidate 2.

**Order.** Tests run cheapest-decisive first, not in K order.

| # | Test | Cost | Decides |
|---|---|---|---|
| G0 | One-qubit fermion gate | minutes | room fork (P), not Candidate 1 |
| K7a | Hypercubic symmetry of every sector | hours, mostly algebra | one cone |
| K3a | Lattice momentum books with interactions | hours to days | graviton mass on a fixed grid |
| K2a | Taste and anomaly assignment | hours, counting | chirality route exists |
| K4 | Beables in 3D | hours | quantum rules |
| K1 | Coulomb phase of the gauge sector | about an hour from the literature, days for Monte Carlo | light |
| K3b, K3c, K2b, K6 | see below | days or more | — |

## G0. Can one qubit per site host fermions locally?

This is the room fork, not Candidate 1. The idea comes from the matter sweep.
- **Model.**
  - One corner v, its 6 edge qubits and 6 far corners: 13 qubits.
  - Hops are t_δ = σ⁺_{v+2δ} X_{edge δ} σ⁻_v + h.c.
  - Local phase tables in Z_4 on the 24 turns, with the group law holding up to the central sign of the binary octahedral group.
- **Observable.**
  - The Levin–Wen T-junction exchange sign (main's BKSF runner, `FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_...2026-09-02.md`).
  - KS flux −1 on every coarse square.
- **PASS:** some table is covariant under all 24 turns and gives −1 on every T-junction.
- **FAIL:** only +1 (bosons). Record K2 = 0 for room P under both turn settings. With one qubit per site, fermions then need corner records (A52) or a non-local string.

## K7. One cone: do photon, matter and graviton keep one speed?

The data bar is GW170817 (|c_g − c|/c < ~1e-15), plus Lorentz tests for matter against light.

**K7a (symmetry).**
- **Method.** Write each sector's Euclidean lattice action: compact U(1), staggered fermions, the A25 spin-2 field and the A26 coupling. Check invariance under the hypercubic group W(B4) with a_t = a_s.
- **Why it decides.** If every sector is hypercubic, a dimension-4 speed difference is forbidden by symmetry. This is the anisotropic-lattice lesson: on isotropic hypercubic lattices the anisotropies need no tuning.
- **PASS:** every sector, including gravity, has a hypercubic Euclidean form with exact lattice gauge invariance.
- **FAIL → K7b.** Expected suspect: A25 is an ADM (space + time) split, so its 4D form must be built, for example as a staggered spin-2 field on Z⁴ roles.

**K7b (one loop, only if K7a fails).**
- **Method.** Compute the one-loop speed split between the non-hypercubic sector and the others. The continuous-time comparison value is v_ψ − v_φ ≈ 0.026 g² (viability map, CHECKED).
- **PASS:** the split is zero, or below 1e-15 without tuning.
- **FAIL:** a generic O(g²) split, so equal speeds need tuning. Record K7 = 0 for (motion, gravity) = (Q, X).

## K3. Gravity on a fixed grid

**K3a: graviton mass from the interacting sea.** This is the crux of "fixed-lattice gravity unnatural".
- **Method.**
  - The coupling −½ h_ij T^ij keeps the linearized gauge invariance (𝒱D = 0) only if the lattice stress obeys exact local momentum conservation, Dᵀ T = 0.
  - Test whether any local lattice stress of Candidate 1's interacting matter and light satisfies it.
  - If none does, compute the size of the induced graviton mass-type terms at one loop.
- **Start from:**
  - the books blocks 137, 141, 143 (exact books need records that never scatter);
  - probe 6 (the sea feels shape at −0.178 / −0.109 per cell).
- **PASS:** an exactly conserved local stress exists for the interacting theory, so the mass terms are forbidden.
- **FAIL:** none exists and the induced terms are Planck-sized. Record K3 = 0 for (gravity X, room O). If the diagnosis blames the fixed grid itself, record it for X on every room.

**K3b: nonlinear closure.** The constraint algebra closes beyond second order (T66, {G,C} no-go).
- **PASS:** a lattice completion closes.
- **FAIL:** the T66 no-go extends.

**K3c: equivalence and bending.** Bound pairs fall like single bodies to 1e-15, and light bends ×2 (A26, T68, T72).
- **PASS:** both hold.
- **FAIL:** an O(binding) violation survives.

**If K3 fails for X, G and I on every room**, the casualty is outside the matrix: the fixed grid (the Lattice axiom). That is a finding to bring to the owner, not a setting to flip.

## K2. One-handed matter

**K2a: assignment.**
- **Question.** Can Candidate 1's staggered tastes, which are vector-like, be arranged per generation as Spin(10) 16 ⊕ mirror 16̄? It must have a local multi-fermion interaction that respects the lattice symmetries and could gap the mirror 16̄ symmetrically (the Wang–Wen 2018 / Eichten–Preskill route; 16 Weyl fermions are anomaly-free including Z16).
- **PASS:** an explicit assignment plus a local interaction.
- **FAIL:** the taste count or symmetry forbids it.
- **Start from:** `SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_...2026-09-14.md` (in it a mirror partner survives).

**K2b: dynamics.** Evidence that the mirror sector gaps with no symmetry breaking. Literature: Butt–Catterall–Hasenfratz, SU(4) 4D staggered symmetric mass generation. Expensive; run after K7 and K3a.

## K4. Quantum rules

- **Method.** Bell/Vink discrete-time beables on Candidate 1's matter, on a small 3D lattice.
- **PASS, all three:**
  - equivariance holds to round-off;
  - CHSH reaches 2.83 within error from the records alone;
  - one record-click per single-particle detector.
- **FAIL:** any of these fails.
- **Start from:** the 09-27 beables note, which has these on 1D rings.

## K5. Record-sector data

With beables, this passes by construction once K4 passes: there are no new effects. No-signalling is checked at the Born level.

## K1. Light

- **Method.**
  - Compact U(1) in 4D has a massless photon phase at weak coupling. This is a theorem for the Villain form (Fröhlich–Spencer 1982); Guth 1980 and numerics cover the Wilson form.
  - Physical α gives g² = 4πα ≈ 0.09, so β = 1/g² ≈ 11, deep in that phase.
  - Check that Candidate 1's gauge sector, with dynamical staggered fermions and the background charge, maps onto that class at this β.
- **PASS:** the mapping holds, or a small Monte Carlo shows a Coulomb potential.
- **FAIL:** confinement at physical α.

## K6. Numbers (last)

- **PASS:** three light generations with a mass hierarchy come out of the content, with no supplied labels.
- **FAIL:** they do not.
- **Starting point:** the hw=1 triplet is a label algebra, not a symmetry (e69519ec7a), and 4D staggered fermions give 4 tastes.
