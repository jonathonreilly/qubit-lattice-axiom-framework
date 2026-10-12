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

## K3a′ (added 2026-10-08, after K3a; a new test, K3a's own line is unchanged)

**Why it was added.** K3a found that interacting lattice QED has no exactly conserved finite-range stress. The best range-R stress leaves a vertex defect of 13% at R ≤ 3 and 3.5% at R ≤ 4. Crystal momentum has a 1/r kernel (probe 6), so the defect may fall as a power of R and never reach zero. The question that matters for data is whether a *quasi-local* stress, wide but still microscopic, is good enough.

**The data bar.**
- Gravitational waves bound the graviton mass at m_g ≲ 1.3e-23 eV (LIGO–Virgo GWTC-3), which is about 1e-51 M_P.
- The induced mass² coefficient per cell, about e²·defect², must therefore be below about 1e-104.
- With e² = 4πα, the defect must be below about 1e-51.

**Method.**
- Extend K3a's best-range-R fit to R = 5, 6, 7 and more, as far as the budget allows.
- Fit the defect against R with exponential and power-law forms, and report both, with fit quality.
- Extrapolate the R at which the defect reaches 1e-51.

**PASS:** the extrapolated range is at most 1e15 sites (about 1e-20 m, a factor 1e5 below the proton radius), with a fit that is stable over at least three consecutive R values.

**FAIL:** the defect plateaus, or the extrapolated range exceeds 1e15 sites.

**INCONCLUSIVE:** the fit is not stable over three R values.

## G0c (added 2026-10-08, after G0 and G0b): face-qubit bosonization

**Why it was added.**
- G0 and G0b exclude, within the classes tested, fermions built as corner occupation qubits with edge links. Both verdicts were refereed (CONFIRMED WITH CORRECTIONS).
- The referee identified Chen–Kapustin's exact 3D bosonization (arXiv:1807.07081) as genuinely outside that architecture:
  - qubits on faces, carrying a 2-form Z₂ gauge field;
  - fermion parity as cube flux;
  - face-supported X·Z-dressed hops;
  - a modified edge Gauss law.
- It depends on a spin structure and on a cubic-lattice framing (the ∪₁ convention). Whether the 24 turns are a symmetry needs its own calculation.
- On the doubled cell, face-role sites are exactly "one qubit per site with a pattern".

**Question.** Can all 24 proper turns about a cube centre (and about a vertex) be implemented on the Chen–Kapustin model as locality-preserving maps (finite-depth local unitaries, times gauge transformations, times a change of framing that is itself a local unitary) that preserve:
1. the bosonized Hamiltonian algebra, up to the gauge constraints;
2. the fermionic statistics of the cube excitations?

**PASS:** an explicit, locality-preserving implementation of all 24 turns, checked on a finite periodic lattice, preserving the dressed-hop algebra in the constrained sector.

**FAIL:** some turn maps the framing to an inequivalent one, meaning no finite-depth local circuit plus gauge transformation relates them, or the hop algebra cannot be preserved.

**INCONCLUSIVE:** the implementation needs a non-local or non-finite-depth map that is not excluded.

## K3a″ (added 2026-10-08, after K3a and K3a′, both refereed INCONCLUSIVE): direct calculation of the interacting shear response

**Why it was added.** Extrapolating a defect over 16 decades cannot decide K3 (referee). The direct quantity is the graviton mass-type term itself, measured as the vacuum's energy response to a uniform traceless shear at q = 0.
- **Why that quantity.** A constant h_ij is a coordinate rescaling. Linearized gauge invariance then allows only a density (trace) response, and forbids any transverse-traceless (TT) second derivative. A nonzero TT shear coefficient is therefore a graviton mass term (probe 6's "the sea feels shape").

**Method.**
- Take Candidate 1's matter and light: staggered fermions plus compact/Yee U(1).
- Couple them to a constant h_ij by a stated local rule. Choose it so that the **free** vacuum is exactly shear-blind (probe 6: possible by design).
- Compute the vacuum-energy TT shear coefficient c₂ at **O(e²)** by second-order perturbation theory. The intermediate states are a fermion pair plus a photon, so this is a finite lattice integral over two momenta.
- Converge it in L (or use the infinite-volume integral). Report c₂ in lattice units for at least two coupling rules: the strictly linear one, and one natural alternative such as the exponential vielbein.
- Check whether any choice inside a stated local family makes c₂ vanish, and if one does, whether a symmetry protects that choice.

**PASS:** c₂ = 0 at O(e²), within numerical precision of 1e-10 in lattice units, for a local coupling rule protected by a symmetry. No tuned bare graviton-mass counterterm is needed.

**FAIL:** c₂ ≠ 0, at least 1e-6 in lattice units, for every rule in the stated family. Then the only fix is a bare graviton-mass counterterm tuned to about 1e-100 of its natural size (LIGO: m_g ≲ 1e-51 M_P). That is a **naturalness kill**, like the cosmological-constant problem, not a logical inconsistency. It is recorded as such.

**INCONCLUSIVE:** c₂ is not converged, or the result depends on the coupling family in a way not covered here.

## W1 and W2 (added 2026-10-08, after K3a″; tests of gravity option W before a Candidate 2 is written)

**Why they were added.** The W prior-art sweep (Sonnet, `TEST_LOG.md`) found two things:
- W in its explicit form, with dynamical edge lengths entering the matter weights, is essentially K3a″'s vielbein model. It escapes only if the cutoff and measure follow the strain, and a Brillouin zone fixed by adjacency suggests they cannot.
- W in its position-blind form reduces to K3a.

**W1: interacting vacuum Hessian under uniform edge-length deformation**
- **The complex.** The cubic (Kuhn/Coxeter) Regge complex with 15 edge classes in 4D, or 7 in 3D. Use 3D if the Hamiltonian form is used.
- **The weights.** Staggered fermions plus compact U(1), with every weight a function of the edge lengths, fixed by one no-free-parameter rule: DEC Hodge stars, with hops ∝ 1/ℓ and photon weights ∝ ℓ_dual/ℓ. Universal coupling, x_γ = x_f.
- **The observable.** The vacuum-energy Hessian per cell under uniform edge-length deformation, at O(e⁰) and at O(e²). Decompose it into the constant-metric directions (trace, E_g, T_2g), the vertex-displacement directions, and the non-metric directions.
- **The control.** K3a″'s no-grid (proper-momentum) run.

**W1 verdict lines:**
- **PASS:** the TT (E_g and T_2g) second derivatives vanish, to 1e-10 or better, at both orders, with no tuned counterterm.
- **FAIL:** any nonzero TT term at O(e²) with universal coupling. **A FAIL kills explicit W.**
- **INCONCLUSIVE:** not converged.

**W2: the vacuum Regge graviton count**
- **The question.** On the hypercubic Regge complex, with no matter, resolve the open 5-versus-7 null-space count of `docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_*_2026-09-03.md`. The method:
  - classify every exact zero mode of the second variation at generic momentum (gauge vertex displacements, physical TT, spurious);
  - check whether the flat spurious direction is lifted at cubic order.

**W2 verdict lines:**
- **PASS:** after gauge, exactly 2 physical massless polarizations, and every spurious direction is massive or lifted.
- **FAIL:** an extra massless non-gauge mode survives.

## FR: gravity when records freeze sites (added 2026-10-09; owner request: "test gravity with records freezing sites")

**The setting (the axioms read literally).** A record locks its site's possibility for good, so that site has no live qubit. The live qubits, which carry the shared possibilities, evolve on the remaining sites. A frozen site still counts as a neighbour condition: it is a fixed state that live neighbours feel. Matter is a cluster of N frozen sites. This follows the owner's thought that records are mass; it is a test setting only.

**Prior art these tests build on (they are not re-derived):**
- **Block 117.** A walker on unrecorded sites freezes when records fill a sublattice.
- **Block 193 v3.** Missing records do not stretch the walk: periodic patterns give axis speed 1 or 0, and random vacancies at first order act as local scatterers with damping.
- **Campaign 8 A6–A18.** A gas of wandering records swallowed by clumps gives 1/r clock slowing, but:
  - half of Einstein's next-order term;
  - half the light bending;
  - no waves;
  - a moving body's field survives only as a wake.
- **Blocks 190/191.** The free sea resists shear, which gaps the member.

**FR1: the static field of a frozen cluster.** This is the cheapest and most decisive test, so it runs first.

*Method.* Use two live-vacuum classes, which between them cover the obvious long-range mechanisms:
- **(a) A gapless free-fermion sea.** Staggered hopping on live sites. Frozen sites are blocked, or carry a fixed occupation that acts as a local potential. Run both readings.
- **(b) An ordered qubit magnet with Goldstone modes.** XY and Heisenberg, ferro and antiferro, in linear spin-wave theory, plus exact checks where small. Frozen sites are spins locked along, or across, the order direction.

For a cluster of N frozen sites, compute two things, then fit the tail over at least a decade in r and check that it scales with N:
- the static perturbation δ(r) of the live vacuum at distance r;
- the energy shift, i.e. the clock-rate shift, of a live test excitation at r.

*Lines:*
- **PASS (Newton-like):** δ ∝ N/r over at least a decade, with the same coefficient within 10% for every live species tested in that vacuum (universality).
- **FAIL:** the tail falls faster than 1/r, the strength does not scale with N, or species coefficients differ by more than 10%.
- **INCONCLUSIVE:** no clean asymptotic regime.

*The Goldstone case.* A locked spin transverse to the order is a local field on a gapless mode, so a 1/r tilt is possible. If that happens, report what kind of field it is (scalar or vector). Campaign 8 found a one-number (scalar) field bends light half or not at all.

**FR2 (only if FR1 passes): light bending and universality.**
- **Method.** Send live wave packets past the cluster and compute their deflection against the Newtonian deflection from FR1's potential.
- **PASS:** a ratio of 2 ± 0.1 for every species.
- **FAIL:** anything else.

**FR3: gravitational waves.**
- **Permanent, immobile records** (the literal axiom). The frozen pattern can change only by adding records, so it cannot oscillate and carries no wave. That contradicts the observed gravitational waves (ARGUED).
- **Moving records** (the owner's 09-20 reading).
  - **Method.** Find the record pattern's collective modes.
  - **PASS:** two transverse-traceless modes at light speed.
  - **FAIL:** only longitudinal, scalar or vector modes, or none.
  - **Prior art.** Campaign 8 found that records as locked possibilities carry no momentum, so they spread and do not ripple. Only a supplied clause, "content = direction of travel", gives sound, which is a longitudinal mode.
