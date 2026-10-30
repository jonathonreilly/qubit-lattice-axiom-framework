---
claim_id: the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free-field Floquet ticks with the (111) turn T3 as a symmetry on the turn axis; FREEZE (W_F = (-2, 1, 1)) rebuilt inline. (A1) In each turn sector the net eigenphase flow through every quasi-energy equals the det winding W_a, so W_a != 0 puts a BULK Bloch eigenstate at every quasi-energy (pi included) on the axis loop; checked for FREEZE and turn-symmetric deformations. (A2) Every interval filling has flow W at both cuts; intersection lemma: a band filling with no occupied-empty touching on the axis forces W = 0. (A3) An anomalous Floquet (RLBL) tick has gapped bulk at 0 and pi and zero det winding on every loop, walls F_0 = F_pi = +-1. (A4) On a slab, per wall F_0 - F_pi = C (band invariant of the bulk bands between 0 and pi); total pi flow = W_slab is forced but its wall is not: a sector-resolved class-A toy with a static-type domain-wall bulk (C = f(2,+), W = 0) and a W-carrying far termination layer has near wall (f(2,+), 0) and far wall (f(1,-), W_F). (B1) U0 O U0^-1 = (-1)^(n_pi) O, so any periodic drive resolves only the parity of the number of pi legs; tick-alternating terms cancel exactly on 0-0 and pi-pi terms. (B2) Separating pi-pi from 0-0 needs an S-odd term, which gives the light sector the reflected interaction; reduced two-flavour Spin(6) site: unique ground state for one sign, 2-fold for the reflected sign. (C) N_f = 0 mod 3 unchanged under the supplied anomaly-family-count index form. Not covered: the repaired slab built on FREEZE's 8-mode cell, the far-wall SMG of mirror + pi pair, interacting wall dynamics, gauge fields, the low-energy recheck of a W = 0 bulk."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_bounded_theorem_note_2026-10-24
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - the tick-winding-origin note (2026-10-24, campaign files)
  - the spin10-two-flavour note (2026-10-24, campaign files)
  - the smg-strong-coupling note (2026-10-24, campaign files)
runner: scripts/the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_2026_10_24.py
---

# The family-class winding forces bulk pi states, but a slab can put all its pi flow on the far wall, while no tick-alternating term separates pi-pi from 0-0

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] reading.
Runner: runner.py, TOTAL: PASS=7 FAIL=0, 2.7 s, 81 MB peak, about 4.0 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/pi_repair_test_run.py). Axioms unchanged. No rule adopted. No CL edit.
Criteria were written before any code ran (criteria_pre_run.txt). Every criterion came out as predicted.

The first run had three code-level failures, and each was fixed without changing any claim:
- A4: the wall-flow counter missed crossings on the k-loop seam, because the crossing fell exactly on a grid point. The
  fix was a grid offset.
- A4: tau = 0.8 let the trivial-mass strip's bulk band cross pi. The fix was tau = 0.5, which gives a bandwidth below pi.
- B1: the sign convention for the alternating drive was wrong (H_eff = -O_odd for the order (+, -)).

Question (repair of the SUSPENDED family-class tick):
- (A) Is a light pi node forced by W != 0 in the bulk, or only on slab walls?
- (B) If bulk pi copies are forced, can they be gapped symmetrically, for example by a tick-alternating interaction?
- (C) Verdict.

Repo first. A git grep of origin/main (docs, scripts) for "anomalous floquet", "rudner" and "pi copy" found nothing. This
note builds on and narrows:
- pi-sector-stability: S, the zero vacuum polarization, and repair routes (a) and (b);
- floquet-pi-slab: the sum rule F_0 = F_pi = W, P3 (the termination is chosen), and the alternating F/F^+ bulk;
- tick-winding-origin: T forces a zero W component, and W is additive;
- spin10-two-flavour: the Spin(12) Casimir and the reduced Spin(6) analogue;
- smg-strong-coupling: one 16 per site has no unique low-degree singlet.

## A. Bulk tick versus slab walls

- A1 [T]/[F]. Bulk theorem.
  - In turn sector a, U_a(kappa) is a unitary loop. The net upward crossing count of ANY fixed quasi-energy eps equals the
    winding of det U_a, which is W_a.
  - So W_a != 0 forces a bulk Bloch eigenstate at every eps, including pi, on the axis loop. This is the bulk tick's own
    spectrum, not a slab effect.
  - FREEZE: the flow is (-2, 1, 1) at eps = 0.37, 1.1, 1.77, 2.6 and pi. Two random turn-symmetric deformations give the
    same.
  - Every family-class tick has all components of W nonzero, so no family-class BULK tick is gapped at pi or anywhere else
    on the axis.
- A2 [T]. Fillings.
  - An interval filling (a, b) has flow W at both cuts. A light cut at 0 therefore always brings a second gapless cut. Its
    quasi-energy is a convention (pi in the standard vacuum), but its existence is forced.
  - Intersection lemma for band fillings with no occupied-empty touching on the axis (touchings across turn sectors are
    protected crossings, i.e. 3D nodes).
    - Occupied and empty curves are disjoint closed sets on the torus (kappa, theta). So every pair has zero algebraic
      intersection: N_o,a m_b - N_e,b n_a = 0.
    - All occupied and empty slopes are then equal. Since sum_a W_a = 0, the common slope is 0 and W = 0.
    - An exhaustive check over 676 disjoint configurations agrees.
  - Hence ANY bulk vacuum of a W != 0 tick has occupied-empty touchings beyond the single light cut. This answers (A) for a
    bulk world: forced.
- A3 [F]. Anomalous Floquet contrast.
  - The RLBL tick (4 full-transfer steps around a plaquette, plus an on-site step 0.8) has a bulk gap at 0 (0.80) and at
    pi, and det winding 0 on every loop.
  - Its strip walls carry F_0 = F_pi = (-1, +1).
  - So anomalous Floquet phases have gapped bulks only because their det windings vanish. Their invariant lives in the
    micromotion, not in W, and it cannot gap a W != 0 bulk.
  - It IS the structure of a slab whose bulk period has W = 0. That is floquet-pi-slab's F/F^+ bulk, whose net W sits in
    the unpaired layer, i.e. the termination.
- A4 [T]/[F]. Slab walls.
  - [T] For a slab bulk gapped at 0 and pi, each wall has F_0 - F_pi = C, the band invariant of the bulk bands between 0
    and pi on that side (sector resolved). The walls sum to W_slab at every eps.
  - So the total pi flow W_slab != 0 is forced (floquet-pi-slab B3), but WHICH wall carries it is set by C.
  - floquet-pi-slab's bulk has C = 0, which gives F_0 = F_pi on each wall. That is why its near wall holds the light q 2
    at both (0, 0) and (R, pi): the near-wall pi copy.
  - [F] Sector-resolved class-A toy. Per turn sector there is a QWZ strip (U = exp(-0.5 i H)) with C_a = f(2,+) =
    (-1, 1, 0). Its far termination carries a W_a chiral shift layer coupled at g = 0.3.
    - Near wall: (F_0, F_pi) = ((-1, 1, 0), (0, 0, 0)), i.e. the light q 2 at 0 only, with NO near-wall pi copy.
    - Far wall: F_0 = (-1, 0, 1) = f(1,-), the mirror q 1 in the other copy, and F_pi = W_F = (-2, 1, 1).
    - The slab's det winding is (-2, 1, 1).
  - [S] On the full cell this would be a static-type domain-wall bulk (W = 0, gap at pi, as in CL-1's tick) with one FREEZE
    layer at the far termination. At 0 the far wall then has: the static mirror q 2 (-), plus FREEZE's q 2 (+) and q 1 (-).
    The q 2 pair has zero net flow and is removable, leaving the mirror q 1. At pi it has FREEZE's (q 2, +) and (q 1, -).
    Not built on the 8-mode cell.

## B. Gapping pi copies in a bulk world

- B1 [T]/[F]. Under the tick, a term with n_pi pi-legs obeys U0 O U0^-1 = (-1)^(n_pi) O.
  - So a drive of any period resolves only n_pi mod 2. The harmonics are multiples of 2 pi / n, and a pi-pi term carries
    total quasi-energy 0 mod 2 pi, exactly like a 0-0 term.
  - Constant terms give H_eff = O_even. Tick-alternating terms give H_eff = -O_odd. The errors are 1.5e-3 at g = 0.01.
  - Splittings: a 0-0 mass, a pi-pi mass and a 2+2 quartic each give 0.60 when constant and 0 (exact) when alternating.
    A 0-pi mixing term gives 0 when constant and 0.60 when alternating.
  - Answer: a tick-alternating interaction does NOT couple only pi-pi pairs. It cancels exactly on them, and on 0-0 terms.
    Allowed or not (it would make CL-1's tick period-2), it does not do the job.
- B2 [T]/[F]. Separating pi-pi from 0-0 needs an S-odd term (S exchanges the sectors).
  - In S-mapped frames an S-odd term gives the light sector the reflected interaction -O.
  - Reduced two-flavour Spin(6) site (2^8 states), with the term -(g/2) sum {B_a, B_a^+}:
    - the gapping sign has a unique half-filled ground state (gap 2.00 g in this runner's normalisation, which differs
      from spin10-two-flavour's);
    - the reflected sign has a 2-fold ground state.
  - So the light 16s would carry a cutoff-scale strongly coupled term. A reflected sign with a unique gapped state would
    gap the light, which is worse.
  - No S-odd route is shown benign.

## C. Verdict

There are two readings.

Bulk-world reading (the light Weyls are FREEZE's bulk nodes): NOT REPAIRABLE by free terms (A1, A2) or by
tick-alternating interactions (B1). The S-odd route is not shown (B2).

Slab-world reading (the world is the near wall; this is the adopted clause's own setting): REPAIRABLE for the light wall at
the level of flows (A4). The rule costs are:
1. The family-class winding moves off the bulk tick into the far termination layer. The bulk tick becomes W = 0 (a
   static-type domain-wall circuit, gapped at pi). The clause would read: "the slab's far termination layer has all three
   turn-graded winding components nonzero; the bulk tick has W = 0".
   - floquet-pi-slab already found that the termination fixes the far copy (P3 FAIL). So this is no new choice in kind,
     but it is still a choice.
2. The far wall must gap, by SMG, the mirror at 0 plus the pi pair (q 2, +), (q 1, -). That is 3 x 16 = 48 Weyls per
   family (0 mod 16), with no turn-symmetric bilinear (the charge difference is 1). Not shown.
3. Rechecks are needed because the bulk is now W = 0 and T-symmetric (tick-winding-origin lemma): the 96-element kept group
   and the low-energy, CP and lapse results were derived for a FREEZE bulk.

Also: N_f = 0 mod 3 is unchanged (C1, under the supplied anomaly-family-count index form). The near wall has 1 light node
per family instead of 2, and both are units mod 3. The near wall has no pi states, so the S complement map of
pi-sector-stability has no near-wall instance. The vacuum polarization test (A2 probe of pi-sector-stability) on the
near wall is not run.

So the family-class mod-3 count is not lost. The suspension is narrowed: "family-class bulk tick" is excluded, and
"family-class far termination" is open, pending far-wall SMG and the rechecks.

## Gate (for the candidate termination clause, not adopted)

1. No measured number is chosen.
2. No observed structure is named. It is a layer and update condition, but the termination placement is chosen.
3. Prediction not built for: the near wall is pi-free, so vacuum polarization and N_nu = N_f come back. The far wall holds
   3 x 16 heavy states per family. UNTESTED on the full cell.
4. It bends no axiom.

Result: NOT YET PASSED (untested). It is not adopted.

## Smuggling review

Supplied:
- FREEZE as the representative;
- the class-A sector toy (QWZ strip plus a chiral shift layer as a stand-in for the FREEZE layer);
- the RLBL model;
- the Spin(6) reduction and its normalisation;
- the anomaly-family-count index form;
- the choice of termination.

Forced:
- the bulk spectral flow at every quasi-energy;
- the two-cut and intersection lemmas;
- the per-wall F_0 - F_pi = C;
- total pi flow = W_slab;
- n_pi-parity resolution under any drive;
- the S-odd sign reflection.
