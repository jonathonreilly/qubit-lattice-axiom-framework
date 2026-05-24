# Staggered Fermion + Parity-Coupled Gravity — Complete Card

**Status:** bounded - bounded or caveated result note (audited_conditional;
2026-05-02 fresh-context audit)
**Date:** 2026-04-11 (parity coupling rewrite); 2026-05-10 conditional-hypotheses
bookkeeping repair
**Coupling:** `H_diag = (m + Phi) * epsilon(x)` — scalar 1x1 in spin-taste
**Reference:** Zache et al. (Quantum 2020), Dempsey et al. (arXiv:2501.10862)

## Claim Boundary (audit response)

This card is a **conditional finite-harness numerical/card result for the
registered parity-coupled runner outputs, not an audited-clean bounded
theorem/card**. The 2026-05-02 fresh-context audit
(`fresh-staggered-fermion-card-auditor`, codex-fresh, fresh_context, class B)
landed `audited_conditional` because attraction and force-direction closure
require **importing** the screened-Poisson bridge `(L + mu^2) Phi = G rho`
together with fixed `G > 0`, free `mu`, positive source `rho = |psi|^2`,
static lattice, and selected graph families. The runner verifies finite-card
consequences under those premises; it does not derive them.

This 2026-05-10 repair makes the conditional hypotheses explicit at the head
of the note (rather than only restating them under "What is still assumed"
near the tail), restates the load-bearing claim as a conditional bounded
card, and originally pointed the staggered-Dirac structure at its `A_min`
anchor in [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
(A3) so that the card no longer reads as deriving Dirac structure from
inside itself. The 2026-05-24 repair (see "2026-05-24 audit-conditional
repair" below) replaces the meta-only `MINIMAL_AXIOMS` anchor with citations
to the retained staggered-Dirac substep chain and acknowledges the retained
H2 narrow theorem. Numeric content of the card is unchanged.

## Conditional Hypotheses (admitted_context_inputs)

The bounded card claim closes **only under** the following admitted/imported
premises. Each is an external input on the harness side, not derived inside
this note from `A_min`:

- **(H1) Screened-Poisson bridge.** The gravitational potential `Phi` is
  determined by `(L + mu^2) Phi = G * rho` with `L` the graph Laplacian on
  the chosen family, `mu^2 > 0` a fixed screening mass, and `G > 0` a fixed
  positive coupling. This equation is **not derived** from the framework and
  is treated as a harness import on the same footing as standard
  Newton-style screened gravity.
- **(H2) Positive source.** The matter source is `rho = |psi|^2 >= 0` so
  that `Phi >= 0` follows mathematically from positivity of the resolvent
  `(L + mu^2)^{-1}` against a non-negative source. The forward chain
  `rho >= 0 ==> Phi >= 0` is derived as a retained Class-A theorem in
  [`STAGGERED_FERMION_CARD_H2_POSITIVE_SOURCE_PHI_POSITIVITY_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_FERMION_CARD_H2_POSITIVE_SOURCE_PHI_POSITIVITY_NARROW_THEOREM_NOTE_2026-05-17.md)
  (Stieltjes / non-singular M-matrix). The H2 admission as stated in this
  card is therefore conditional on H1 only; the resolvent-positivity half
  is no longer a fresh import.
- **(H3) Free positive coupling `G`.** `G` is a free positive parameter of
  the harness; the reported strengths `G in {8.0, 50.0, ...}` are operating
  points, not predicted couplings.
- **(H4) Free screening mass `mu`.** `mu^2 > 0` is a free parameter; the
  reported `mu^2 = 0.22` is an operating point.
- **(H5) Static lattice.** The graph (sites and edges) is fixed in time;
  there is no dynamical metric or graph evolution alongside `psi`.
- **(H6) Enumerated graph families.** Closure is reported only on the
  registered families (1D `n=61`, 3D `n in {9, 11, 13}`, `random_geo s10`,
  `growing n=48`, `layered_cycle 8x8`, `causal_dag 10x6`, `causal_dag 8x8`,
  and the explicit cycle/wave/portability variants below). The card does
  not claim universality across arbitrary graphs.
- **(H7) Eigensolve / family-coverage gate.** The 3D card runs energy
  projections at `n=9`; at `n in {11, 13}` only `4/6` families are tested
  because `N_sites > 1000` (frozen `n=9` eigensolve gate).
- **(H8) Sign convention for `Phi`.** Positive-definite `(L + mu^2)` and
  positive `rho` give `Phi >= 0`. Inverting `Phi -> -Phi` inverts the
  measured force; the sign-test column below documents that this inversion
  has been exercised on the canonical cubic card.
- **(H9) Staggered-Dirac structure cited from retained substep chain.**
  The Kogut–Susskind staggered Hamiltonian (the staggering phases
  `eta_mu(x)`, `epsilon(x)`, and the diagonal mass term used in `H_diag`)
  is the same staggered-Dirac structure carried by the retained
  staggered-Dirac substep chain:
  [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  (substep 1, Grassmann forcing),
  [`STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md)
  (substep 2, Kähler–Dirac equivalence),
  [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  (substep 3, BZ-corner Hamming orbit),
  [`STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  (substep 3, species reduction bridge), and
  [`STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md)
  (substep 4, AC-λ simultaneous diagonalization bridge). This card cites
  the retained substep chain as the staggered-Dirac authority but does not
  itself derive or ratify it; the legacy `A_min` / A3 surface label has
  been superseded by the substep chain. The earlier
  [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md) anchor is
  retained only as historical context (meta, superseded).

The bounded claim of this card is therefore: **conditional on (H1)–(H9),
the registered parity-coupled runner outputs reproduce the score surface
tabulated below on the enumerated finite cards**. Promotion to an
unconditional bounded theorem requires either ratifying (H1)–(H9) inside
the note or retaining a separate derivation that closes them.

## Coupling Structure

The gravitational potential enters the staggered Hamiltonian through the
SAME parity factor epsilon(x) as the mass term, because both are scalar
(1x1 in spin-taste) couplings to psi-bar-psi in the continuum:

```
H_diag = (m + Phi(x)) * epsilon(x)
```

This is NOT the same as the identity coupling `m*epsilon + Phi` used in
earlier versions. Under parity coupling:
- Phi > 0 WIDENS the mass gap (slows propagation) -> repulsion
- Phi < 0 NARROWS the mass gap (speeds propagation) -> attraction
- The sign of gravity is a PREDICTION of the Dirac structure

The screened Poisson equation (L + mu^2)Phi = G*rho with positive-definite
operator and positive source rho = |psi|^2 always gives Phi >= 0. Under
self-gravity, the sign chain is:

1. |psi|^2 >= 0 -> Phi >= 0 (mathematical, not a choice)
2. (m + Phi)*epsilon modulates the mass gap (from Dirac structure)
3. Gap modulation creates velocity gradient -> force toward high-density regions
4. Force direction is TOWARD (attraction) as a dynamical prediction

Verified: inverting Phi -> -Phi inverts the force (AWAY). The old identity
coupling gave TOWARD regardless of Phi sign (tautological).

## 1. Canonical 17-Card (frontier_staggered_17card.py)

Operating point: mass=0.3, g=50.0, S=5e-4, dt=0.15

### 1D (n=61): 17/17

| Row | Test | Value | Status |
|-----|------|-------|--------|
| C1 | Sorkin Born |I3|/P | 1.28e-15 | PASS |
| C2 | TV distance | 0.92 | PASS |
| C3 | Zero-source force | 0.00 | PASS |
| C4 | F proportional to M | R^2=0.917 | PASS |
| C5 | Force TOWARD | +5.75e-5 | PASS |
| C6 | Decoherence | 0.230->0.177 | PASS |
| C7 | Mutual information | 0.165 | PASS |
| C8 | Purity CV | 0.011 | PASS |
| C9 | Force stable across N | all TOWARD | PASS |
| C10 | Distance (force) | 5/5 TW | PASS |
| C11 | KG dispersion | R^2=0.997 | PASS |
| C12 | Gauge (persistent current) | J=2.14e-3 | PASS |
| C13 | Force achromaticity | CV=0.000 | PASS |
| C14 | Equivalence (a=F/m) | CV=0.000 | PASS |
| C15 | Force vs depth | all TOWARD | PASS |
| C16 | Multi-observable | 1/2 | PASS |
| C17 | State families (6/6) | all TOWARD | PASS |
| | **Norm** | **5.55e-16** | |

### 3D Convergence

| Row | n=9 (729) | n=11 (1331) | n=13 (2197) |
|-----|-----------|-------------|-------------|
| C1 Sorkin | 2.62e-15 | 2.75e-15 | 3.11e-15 |
| C4 F~M | R^2=1.000 | R^2=1.000 | R^2=0.999 |
| C5 Force | +1.29e-3 TW | +5.44e-4 TW | +3.18e-4 TW |
| C6 Decoh | 0.754->0.164 | 0.699->0.068 | 0.657->0.085 |
| C12 Gauge | 3D torus 3.69e-3 | 3D torus 2.27e-3 | 3D torus 1.49e-3 |
| C17 families | 6/6 (incl anti) | 4/4 | 4/4 |
| **Score** | **17/17** | **17/17** | **17/17** |

## 2. Cycle-Bearing Graph Battery (frontier_staggered_cycle_battery.py)

DT=0.12, MASS=0.3, G=8.0, mu2=0.22, N_ITER=15

| Row | random_geo (36) | growing (48) | layered_cycle (24) |
|-----|-----------------|--------------|---------------------|
| B1 Zero-source | F=0, Phi=0 PASS | F=0, Phi=0 PASS | F=0, Phi=0 PASS |
| B2 Linearity | R^2=0.991 PASS | R^2=0.9999 PASS | R^2=0.991 PASS |
| B3 Additivity | res=2e-16 PASS | res=2e-16 PASS | res=2e-16 PASS |
| B4 Force | +1.87e-2 TW PASS | +3.42e-3 TW PASS | +5.83e-2 TW PASS |
| B5 Iter stab | 15/15 TW PASS | 15/15 TW PASS | 15/15 TW PASS |
| B6 Norm | 7e-16 PASS | 1e-16 PASS | 2e-16 PASS |
| B7 Families | 3/3 TW PASS | 3/3 TW PASS | 3/3 TW PASS |
| B8 Gauge | sin R^2=1.00 PASS | sin R^2=0.95 PASS | sin R^2=0.97 PASS |
| B9 G_eff | 58.7 | 129.6 | 29.2 |
| **Score** | **9/9** | **9/9** | **9/9** |

B2 was previously marginal on layered_cycle; the current runner reports `R^2=0.991249 PASS`,
lifting layered_cycle to 9/9. Parity coupling still introduces mild nonlinearity
in force-vs-source because (m+Phi)*epsilon couples mass and field multiplicatively.

## 3. Self-Gravity Probe (frontier_staggered_self_gravity.py)

G_SELF=50.0, mu2=0.22, N_ITER=20. No external source.

| Row | random_geo (36) | growing (48) | layered_cycle (24) |
|-----|-----------------|--------------|---------------------|
| S1 Force sign | 20/20 TW PASS | 20/20 TW PASS | 20/20 TW PASS |
| S2 Contraction | **w=0.629** PASS | **w=0.598** PASS | **w=0.436** PASS |
| S3 Norm | 2e-16 PASS | 4e-16 PASS | 4e-16 PASS |
| S4 Stability | 0 flips PASS | 0 flips PASS | 0 flips PASS |
| S5 Families | 3/3 TW PASS | 3/3 TW PASS | 3/3 TW PASS |
| **Score** | **5/5** | **5/5** | **5/5** |

**Contraction is the biggest improvement.** Under the old identity coupling,
the wavepacket EXPANDED (w=1.68). Under parity coupling, it CONTRACTS to
w=0.44-0.63 — gravity now works as expected.

## 4. Retarded/Hybrid Family Closure (frontier_two_field_retarded_family_closure.py)

Retarded field: d^2 Phi/dt^2 = -c^2(L+mu^2)Phi - gamma*dPhi/dt + beta*source
Memory: dm/dt = (rho - m)/tau_mem

| Row | random_geo (36) | growing (48) | layered (24) | causal_dag (36) |
|-----|-----------------|--------------|--------------|-----------------|
| R1 Zero-src | PASS | PASS | PASS | PASS |
| R2 Linearity | R^2=1.000 | R^2=1.000 | R^2=1.000 | R^2=1.000 |
| R3 Additivity | PASS | PASS | PASS | PASS |
| R4 Force | +2.98 TW | +1.07 TW | +4.06 TW | +3.55 TW |
| R5 Iter stab | 30/30 TW | 25/30 TW FAIL | 30/30 TW | 30/30 TW |
| R6 Norm | 2e-16 | 2e-16 | 7e-16 | 1e-16 |
| R7 Closure | 3/3 TW | 3/3 TW | 3/3 TW | 3/3 TW |
| R8 Gauge | sin R^2=1.00 | sin R^2=0.95 | sin R^2=0.97 | no cycle, SKIP |
| R9 G_eff | 0.4 | 0.4 | 0.4 | 0.7 |
| **Score** | **9/9** | **8/9** | **9/9** | **8/9** |

G_eff = 0.4-0.7 across all families. Source-scale gap closed.

## 5. Iterative Endogenous Closure (frontier_staggered_iterative_closure.py)

20-iteration backreaction loop with G=8.0.

| Family | Force | Norm | Phi settled | Families |
|--------|-------|------|-------------|----------|
| random_geo (36) | 20/20 TW, CV=0.12 | 3e-16 | dphi=0.012 | 3/3 TW |
| growing (48) | 20/20 TW, CV=0.93 | 2e-16 | dphi=0.011 | 3/3 TW |

## 6. Two-Field Wave (frontier_two_field_wave.py, rerun-corrected)

Wave-equation Phi + staggered psi, parity coupling.

| Family | Force | Norm | Phi bounded | Families |
|--------|-------|------|-------------|----------|
| random_geo (36) | 30/30 TW | 4e-16 | max=0.27 | 2/3 TW |
| growing (48) | 30/30 TW | 2e-16 | max=0.16 | 3/3 TW |
| layered (24) | 30/30 TW | 2e-16 | max=0.34 | 2/3 TW |

Hard scores after the clean-family rerun: random geometric `4/5`, growing
`5/5`, layered `4/5`.

## 7. Graph Portability (frontier_staggered_graph_portability.py)

| Family | Born | Norm | Force | F~M | Achrom | Equiv | Robust | Gauge |
|--------|------|------|-------|-----|--------|-------|--------|-------|
| random_geo (36) | 6e-16 | 4e-16 | +3.6e-3 TW | R^2=1.0 | CV=0 | CV=0 | 3/3 | 5.1e-3 |
| growing (48) | 5e-16 | 1e-15 | +3.6e-3 TW | R^2=1.0 | CV=0 | CV=0 | 3/3 | 9.1e-3 |
| layered_dag (36) | 6e-16 | 0 | +3.8e-3 TW | R^2=1.0 | CV=0 | CV=0 | 3/3 | N/A |
| **Score** | **8/8** | **8/8** | **8/8** |

## 8. Critical Exponents (frontier_critical_exponents.py)

| Family | n | G_crit | beta | R^2 | Status |
|--------|---|--------|------|-----|--------|
| random_geo s10 | 100 | 2.0 | 0.73 | 0.97 | fit |
| growing n64 | 64 | 14.0 | 0.37 | 0.95 | fit |
| layered_cycle 8x8 | 64 | 5.0 | 0.33 | 0.92 | fit |
| random_geo s8 | 64 | 1.0 | - | - | degenerate |
| causal_dag 10x6 | 55 | 1.0 | - | - | degenerate |
| causal_dag 8x8 | 57 | 1.0 | - | - | degenerate |

beta ranges 0.33-0.73 (NOT mean-field 0.5) — topology-dependent.

## Complete Score Summary

| Harness | Scores | Total rows |
|---------|--------|-----------|
| 17-card 1D | 17/17 | 17 |
| 17-card 3D n=9 | 17/17 | 17 |
| 17-card 3D n=11 | 17/17 | 17 |
| 17-card 3D n=13 | 17/17 | 17 |
| Cycle battery | 9+9+8 = 26/27 | 27 |
| Self-gravity | 5+5+5 = 15/15 | 15 |
| Retarded closure | 9+8+9+8 = 34/36 | 36 |
| Iterative closure | PASS on 2 families | ~10 |
| Two-field wave | 4+5+4 = 13/15 | 15 |
| Graph portability | 8+8+8 = 24/24 | 24 |
| **TOTAL** | **~183/190** | |

## What Changed: Identity -> Parity Coupling

Old (all scripts before 2026-04-11):
```python
H.setdiag(mass * parity - mass * phi)    # identity coupling
```

New (all scripts after parity rewrite):
```python
H.setdiag((mass + phi) * parity)         # parity (scalar 1x1) coupling
```

### Key improvements under parity coupling

| Metric | Identity (old) | Parity (new) | Why |
|--------|---------------|--------------|-----|
| Self-gravity width | 1.68 (EXPAND) | 0.44-0.63 (CONTRACT) | Gap modulation creates attraction |
| Sign selection (exact lattice) | TOWARD under both +/- Phi | TOWARD for Phi>0, AWAY for Phi<0 | Direct well/hill test is sign-selective |
| Physical mechanism | Uniform energy shift | Mass-gap modulation | Correct Dirac coupling |
| Force direction (exact lattice) | Tautological (prescribed) | Sign-sensitive (well/hill split) | Only on canonical cubic card so far |

### What is verified by the runner (conditional on H1–H9)

The items below are runner-verified consequences of the parity-coupled
staggered-Dirac structure **once (H1)–(H9) are admitted**. They are not
unconditional derivations from `A_min`.

1. **Dirac dispersion** E^2 = m^2 + sin^2(k) — from the staggering phases
   eta_mu(x) once the staggered-Dirac realization (H9) is admitted
2. **Born rule** I3 at machine zero — from CN linearity on the registered
   finite card
3. **Force direction on exact lattice** — well/hill sign test splits cleanly
   under parity coupling on the canonical cubic card (conditional on the
   imported `Phi >= 0` chain (H1)+(H2) plus sign convention (H8); not a
   direction-from-axioms derivation)
4. **Achromatic force** CV=0.000 — F = -<dV/dz> has no k-dependence on the
   registered card
5. **Equivalence** a = F/m mass-independent — CV=0.000 on the registered card
6. **Gauge invariance** persistent current J(A) — from the parity-coupled
   Hamiltonian structure on the registered finite card
7. **Self-gravity contraction** w_f/w_0 < 1 — from iterated backreaction
   under the imported screened-Poisson bridge (H1) with fixed `G`, `mu`
8. **Norm conservation** ~1e-15 — from CN unitarity

NOTE: "Force direction" applies only to the exact-lattice canonical card and
is conditional on the imported sign chain (H1)+(H2)+(H8). On irregular graph
families, the retained shell/edge-radial proxies are structural
interacting-field results but do not yet constitute a clean directional-gravity
claim. One frozen graph-native directional observable is still needed for
irregular-graph sign closure.

### What is admitted (and currently not derived)

These restate (H1)–(H9) in the legacy "what is still assumed" position so
that downstream readers cross-checking the original tail catch the same set:

1. **Screened Poisson equation** (L + mu^2)Phi = G*rho — admitted as (H1);
   not derived from the framework
2. **Coupling constant G** — admitted as (H3); free positive parameter
3. **Screening mass mu** — admitted as (H4); free parameter
4. **Static lattice** — admitted as (H5); graph is fixed, not dynamically grown
5. **The specific graph families** — admitted as (H6); bipartite structure is
   required by the staggering, but which graph is not predicted
6. **Staggered-Dirac structure** — admitted as (H9); cited from the
   retained staggered-Dirac substep chain (substeps 1–4 as listed in
   (H9) above), not derived inside this card. The earlier
   `MINIMAL_AXIOMS_2026-04-11.md` A3 anchor is superseded by the substep
   chain.

## Caveats

1. **B2 linearity marginal on layered_cycle** (R^2=0.985) — parity coupling
   introduces mild nonlinearity because (m+Phi)*epsilon couples multiplicatively.

2. **R5 growing family** — 25/30 TOWARD (5 AWAY iterations). Growing graphs
   have less regular structure; the retarded field oscillates more.

3. **Critical exponents** — 3 of 6 configurations are degenerate (G_crit at
   floor). Finite-size scouts, not definitive universality evidence.

4. **Shell force proxy** — on irregular graphs, the shell-averaged force is a
   radial proxy (shell size enters the observable). The 17-card lattice force
   F = -<dV/dx> is the cleanest observable. On graphs, require both shell and
   edge-radial measures to agree before claiming direction.

5. **Emergent geometry** — force direction is mixed/measurement-dependent on
   grown graphs. Not included in this card until it passes a two-metric gate
   across seeds and sizes.

## 2026-05-24 audit-conditional repair: cite retained substep chain + H2 narrow theorem

Per the 2026-05-22 `audited_conditional` verdict, this card's only cited
authority for the staggered-Dirac anchor was the superseded meta note
[`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md) (claim_type
`meta`), and the H2 admission did not acknowledge the retained Class-A
positivity theorem landed 2026-05-17. This repair re-anchors both
citations against retained authorities. It does NOT promote the card; the
audit posture remains conditional on the still-unresolved imports
(`H1, H3, H4, H5, H6, H7, H8`) and continues to await independent re-audit.

### Concrete edits

1. **(H2) — Positive source.** Updated to cite the retained Class-A
   theorem
   [`STAGGERED_FERMION_CARD_H2_POSITIVE_SOURCE_PHI_POSITIVITY_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_FERMION_CARD_H2_POSITIVE_SOURCE_PHI_POSITIVITY_NARROW_THEOREM_NOTE_2026-05-17.md)
   (`retained`, `positive_theorem`). That note proves the forward chain
   `rho >= 0 ==> Phi >= 0` from standard linear algebra (Stieltjes /
   non-singular M-matrix). The H2 admission in this card now reads as
   conditional on H1 only; the resolvent-positivity half is no longer a
   fresh import.

2. **(H9) — Staggered-Dirac structure.** Re-anchored from the superseded
   meta `MINIMAL_AXIOMS_2026-04-11.md` (A3) to the retained
   staggered-Dirac substep chain:
   - [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md) (`retained_bounded`)
   - [`STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md) (`retained_bounded`)
   - [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md) (`retained`)
   - [`STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md) (`retained_bounded`)
   - [`STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md) (`retained`)

   The card cites the retained substep chain as the staggered-Dirac
   authority; H9 itself remains admitted (this card does not derive the
   staggered-Dirac structure).

### What this repair does NOT do

- Does **not** derive H1 (the screened-Poisson bridge equation
  `(L + mu^2 I) Phi = G rho`). H1 remains the missing physics bridge from
  the framework surface to a graph-Laplacian screened-Poisson equation
  and continues as an imported harness premise.
- Does **not** prove the force-direction (sign-flip) half of H8.
- Does **not** discharge H3, H4, H5, H6, or H7. Those remain
  operating-point admissions.
- Does **not** modify any numeric content of the card or any runner.
- Does **not** introduce new mathematics; the H2 theorem and substep
  chain were already retained before this repair.
- Does **not** set a new audit verdict. Re-audit is required for the
  effective_status to update.

### Remaining admitted bundle after this repair

After this repair the admitted bundle reads as: `{H1, H3, H4, H5, H6,
H7, H8, H9}` with H9 now anchored at the retained substep chain rather
than the superseded meta surface, and H2 represented by a retained
Class-A theorem covering the forward positivity chain (H2 antecedent
plus H1-shape resolvent positivity). Promotion to retained closure still
requires retaining the screened-Poisson bridge H1 itself (or splitting
the card scope explicitly to exclude H1-dependent rows), plus closing
H8's sign-flip half.
