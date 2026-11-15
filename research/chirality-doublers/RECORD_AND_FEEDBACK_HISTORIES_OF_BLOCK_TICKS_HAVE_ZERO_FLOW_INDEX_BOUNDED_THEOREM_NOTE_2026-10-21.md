---
claim_id: record_and_feedback_histories_of_block_ticks_have_zero_flow_index_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For supplied finite-range block ticks and frames on Z and Z^3, every history chosen by records, conditional odds, c-number link feedback or an adversary has flow 0 (additivity and zero flow of each block layer and frame; W3 = 0 for periodic histories), so the record, following and response laws, as the source notes state the candidate laws register (not the current register text), give no net chirality in the sense of this flow (for non-periodic histories that identification is a definition, and the magnetic flow identity linking it to W3 is checked numerically only); a supplied conditioning variant keeps only an index-0 coherent part, and c-number feedback breaks the following law's Born tracking in a finite diagnostic. Conditional on cited, unverified inputs: the averaging bound (integrality of the index, GNVW and Avron-Seiler-Simon) and the register-bypass statement (Stinespring uniqueness). No matter content, chiral mechanism or adopted fix is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: research/chirality-doublers/record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.py
---

# Record and feedback histories of block ticks have zero flow index

Claim type: bounded_theorem.
Primary runner: `research/chirality-doublers/record_and_feedback_histories_of_block_ticks_have_zero_flow_index_2026_10_21.py`.
Location (2026-11-14): moved from `docs/` to `research/chirality-doublers/` with its runner, following the second hold's finding R8 and the SETTINGS row "Research sections" (mathematics on a supplied model in which no framework axiom enters). The move changes no statement. The frontmatter labels, such as `bounded_theorem`, are the source's working labels and grant nothing here; see the [section README](README.md).

The [candidate-law register](../../docs/CANDIDATE_LAWS.md) has zero premise weight. Here "the register", "the update law" and its "record, following and response laws" are those rules as the source notes state them; the current register text does not contain them, and every statement that uses them is conditional on them. Those laws break the translation invariance, the fixed tick and the state-independent update that the free-circuit winding result assumes. This note asks whether that lets the layer carry net chirality. It does not. The [minimal axioms](../../docs/MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## Statement

For a finite-range single-particle unitary V, the flow is the net probability crossing a cut from the uniform state. Every product of block layers of a fixed tiling and diagonal frames has flow 0, however each factor is chosen. Within the update, record, following and response laws of the register, every realised history is such a product, so the layer gives no net chirality in any history. Coherent chirality from extra registers needs registers that are coherent, blank and fermionic with the matter's charges, which records are not.

## Derivation

Pathwise flow. For finite-range V the flow is Tr(V^dag P V - P), P the projector on one side of the cut, a finite-rank trace. It is additive under products (cyclicity of the trace for finite-rank differences), 0 on any block-diagonal layer (each block is a finite trace) and 0 on any frame. So the flow of a product of block layers and frames is 0 whatever selects the factors: the actual configuration, the conditional odds, records or an adversary. This step does not use integrality. For periodic histories the flow equals W1 = n_R(w) - n_L(w) at every quasi-energy w. In 3D every factor is contractible, so W3 = 0 for every periodic history: net local degree 0 at each quasi-energy, and net Weyl-cone chirality 0 when the cones are nondegenerate (#9863). For non-periodic histories the note uses a magnetic flow index: thread flux N_phi through a transverse torus and take the flow along z. Block circuits give 0. For a translation-invariant walk it equals W3 N_phi; this identity is checked numerically, not proved in general.

Effective dynamics. The flow is affine in mixtures. The Born mean over the configuration process is a mixture of index-0 histories, so its flow is 0; its weights are quadratic in the state, so it is not a channel. The Born mean of the conditional odds is the one-body state, which evolves as gamma(t) = V_hist gamma(0) V_hist^dag.

Conditioning variant. The register forbids records that condition the odds. If they did, at rate kappa per half-tick with outcome-dependent index-0 feedback, the coherent part would be exactly (1 - kappa)^n times the free tick: a conditioning event leaves a configuration-diagonal state, which cannot regrow coherence beyond its light cone. Any chirality then sits in the decohered fraction. The argument does not depend on dimension.

Averages. Let K = sum_j p_j U_j with every U_j of index 0 and range at most r. If K is within delta of a unitary U of range at most r, then |ind U| <= 2n sqrt(2 delta) with n = 2rd. Conditional on the integrality of the index (the cited GNVW and Avron-Seiler-Simon results, not checked here), ind U = 0 for delta < 1/(8n^2), and a K whose determinant has a point-gap winding is at least 1/(8n^2) from every range-r unitary. Two-term mixtures never wind. This bound is derived here and has not been compared with the literature.

Register bypass (conditional on Stinespring uniqueness, cited and not checked here). If a finite-depth circuit on matter plus fresh registers induces a unitary chiral map on the matter, then by that uniqueness the register output is independent of the matter, so the registers are not records. Fermion parity and charge rule out links and records as carriers of the compensating flow.

Covariance. The following law is label-equivariant and the source and link response transform covariantly, so the whole layer is inversion covariant. Inversion-symmetric initial odds give an inversion-symmetric law of histories. Chiral initial odds change which modes are occupied, not the index.

Born tracking. If links are c-numbers that follow the actual configuration, the update depends on that configuration, and the realised odds then carry information about it. This breaks the following law's statement that the configuration is distributed as its odds. With quantised links the joint update is a fixed unitary and the statement holds exactly; that fix is not adopted here.

## Checks

The runner gives 20 PASS and 0 FAIL; the N_nu comparison below is printed as a conditional estimate and not counted (2026-11-14). These are finite diagnostics of supplied models.

- 1D free two-site tick: det U(k) is constant (max |W1| 4.3e-21), and crossings are balanced (1, 1) at every quasi-energy tested.
- Full layer on a ring of 40 sites with 2 fermion relays over 6 ticks: every realised history is a free block circuit to 1.1e-15, and every flow is 0 to 4e-16. That includes an adversary choosing bond phases to push right, which visibly moves the odds (Born mean position 39.00 against 54.05). Transport marginals are exact to 9.8e-15.
- Exact branching on a ring of 8 sites with 2 relays over 4 half-ticks: without feedback the law of the configuration equals the Born mean of the odds to 2.1e-15. With c-number feedback the total variation is 6.7e-3 at g^2 = 0.3 and 2.9e-2 at g^2 = 1, and 0.89 given the link history, over 237 histories. The layer is inversion covariant to 5.6e-17.
- Conditioning variant on a ring of 48 sites: the infinite-temperature drift is kappa/2 per half-tick, and long-range coherence is (1 - kappa)^6 times the free value (1, 0.941480, 0.531441, 0).
- 2,500 mixtures of depth-4 index-0 circuits: 145 wind, none with two terms. Every winding mixture is at least 0.871 from unitary, against the bound 0.0020.
- Register bypass: matter flow +1, register flow -1, registers left blank.
- 3D: the register's update on the 2^3 cell reproduces cos w = A S(k) - B to 9.0e-16. W3 is 4.6e-12 with random frames and 2.3e-12 over a 3-tick history with different frames, masses and steps. In a random frame field the magnetic flow winding is 6.3e-17 with crossings of w = 0 balanced at (2, 2). The quasi-local control walk gives W3 = -1, +2, 0 at m = -2, 0.5, 4.5, and windings -1, -2, +2, 0 matching W3 N_phi.

## Against measurement (conditional estimates; inputs supplied)

Oscillation visibility of at least 0.9 over 180 km, with a lattice spacing of 5 l_P supplied (a supplied value: the approved scale-reference primitive fixes units only and does not supply it), bounds a conditioning rate at kappa < 2.4e-41 per half-tick. Index 0 in every charge sector puts a light mirror partner beside each left-handed neutrino. If those partners couple to the Z as nu_L does (a supplied identification), that gives N_nu = 6 against the LEP value 2.9840 +- 0.0082, about 368 sigma away. Averaging can damp one chirality, but it removes no states, so under the same identification the count would also disagree with chiral dephasing.

## Boundary

Supplied: the 1D two-site analogue, the packets, the link reading of the response law with its current, the length response, the adversary's objective, the conditioning variant (which the register forbids), the mixture ensemble, the random frames and magnetic translations, and all measured inputs. Unverified inputs and open obligations (2026-11-14, second hold R9): integrality of the flow (GNVW; Avron-Seiler-Simon) is read only by the averaging bound, and Stinespring uniqueness only by the register bypass; both statements are conditional on them. The general magnetic flow identity is checked numerically only, not proved. For non-periodic histories, identifying chirality with the flow index is a definition supported by the controls, not a derivation. The result is negative for chirality from the record layer under the current laws. No matter content, chiral mechanism or adopted fix is established.
