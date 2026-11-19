---
claim_id: the_adopted_link_rule_puts_one_gauge_field_on_both_slab_walls_so_a_separate_mirror_world_needs_a_new_link_rule_and_a_supplied_temperature_asymmetry_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free-field slab checks and supplied-number estimates for the owner question 'why must the far-wall mirror be removed?'. Exact: (i) for a Gaussian (Coulomb-phase) U(1) on Ls layers with inter-layer plaquettes, the layer operator is a weighted path Laplacian whose only null vector is constant for every positive layer and inter-layer coupling, so the one massless mode couples both walls with the same 4D charge (sum beta_s)^(-1/2); a bulk gauge mass leaves no massless mode; separate wall photons need zero inter-layer coupling. (ii) For a 3+1+1 Wilson domain-wall slab (m = 0.6, Ls = 16), the layer phases that commute with the slab update at generic momenta form exactly the uniform phase (commutant dimension 1), so under the Links clause (registers valued in the update's symmetries, Gauss's law per block) one gauge factor acts on both walls with equal charge and opposite chirality: vector-like. (iii) The far-half charge fails to commute with the update by exactly the middle-bond hop (norm 1, cutoff scale); between wall Weyls the violation is |1 - m|^Ls (slope -0.916 = ln 0.4). Estimates (supplied numbers): a full SM mirror at T'/T = 1 gives Delta N_eff = 6.14 (allowance ~0.3; ~36 sigma); T'/T < 0.47 is needed; symmetric baryogenesis gives Omega'_b/Omega_b = 1, not 5.36; mirror hydrogen has sigma/m ~5e7 cm^2/g. Not covered: non-perturbative bulk confinement (Dvali-Shifman), interactions, the family-class tick's own slab, any new link rule's computation."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - the_fewest_change_symmetric_far_wall_term_is_forced_and_gaps_the_3450_mirror_in_a_wall_mode_chain_while_the_flux_pump_separates_anomalous_content_bounded_theorem_note_2026-10-23
  - the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_bounded_theorem_note_2026-10-22
runner: scripts/the_adopted_link_rule_puts_one_gauge_field_on_both_slab_walls_so_a_separate_mirror_world_needs_a_new_link_rule_and_a_supplied_temperature_asymmetry_2026_10_24.py
---

# The adopted link rule puts one gauge field on both slab walls, so a separate mirror world needs a new link rule and a supplied temperature asymmetry

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate against supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=19 FAIL=0, 0.07 s, 47 MB peak, 2.5 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (mirror_world_test_run.py, removed after the run). Axioms unchanged. No rule adopted.
Criteria were written before any code ran (criteria_pre_run.txt). Every prediction there matched. One runner line (A2h)
first failed because it read hybridised k != 0 states. It was fixed to use the chirality-localised k = 0 wall modes. The
fix changed which states were read, not the claim.

## Question (owner, 2026-10-24)

Measurement only requires that the far-wall mirror not feel OUR gauge forces at low energy: V-A weak currents, the Z
width (N_nu = 2.984), and no extra light charged states. Option (b) is a mirror world (Kobzarev-Okun-Pomeranchuk; Foot;
Berezhiani; cited as supplied). The mirror keeps its own copies of the gauge fields, couples to us by gravity (the edge
registers sit on the coarsest block and are shared), and could be dark matter. Can the rules hold it, and is it allowed?

Repo first. A git grep of origin/main (docs, scripts) for "mirror world", "Dvali-Shifman" and "Berezhiani" found
nothing. The nearest open PR is #9980 (gk-smoothed-layers). This note builds on:
- chiral-tick-form: one Weyl per wall, mirror overlap |1 - m|^Ls, layer-sign charge not conserved;
- floquet-pi-slab and the family-class tick: the mirror sits in the other turn copy on the far wall;
- far-wall-smg: the gapping route;
- mirror-dark-matter: the tick's one-body commutant is trivial, so an exact separate mirror number would leave the
  light sector vector-like;
- gk-smoothed-layers / gk-nogo-check: a far end reading a different field gets a forced photon mass, and every
  excitation rule fills both ends equally.

## A. Can gauge fields localise to each wall separately? (Q1)

A1 [T]. Toy U(1) on a layered slab, Gaussian (Coulomb phase). Take the k -> 0 mass operator over layers, with
arbitrary positive layer couplings beta_s and inter-layer plaquettes bp_s. It is a weighted path Laplacian.
- Its null space is one-dimensional and constant. Checked: max |A_s/A_0 - 1| = 1.8e-14 for random couplings.
- So the massless photon has a FLAT profile. Both walls couple with the identical 4D charge (sum beta_s)^(-1/2),
  0.3147 in the run. This is gauge universality, and it holds however strongly coupled the bulk layers are.
- A Higgs-phase bulk (mass on the interior layers, walls massless) leaves NO massless mode. The lowest mass^2 is
  0.58, and still 9.9e-3 at bp = 1e-2: the wall photons pick up masses through the bulk.
- Each wall has its own massless photon only at bp = 0, i.e. with no inter-layer plaquettes (Ls zero modes).

A2 [T/F]. The 3+1+1 Wilson domain-wall slab (layer = extra spatial direction, m = 0.6, Ls = 16) has:
- one 2-component Weyl per wall at k = 0 with opposite Gamma = i alpha_4 beta (near -1, far +1);
- amplitude ratio 0.400000 = |1 - m| per layer;
- next state at 0.614.
The real phases c_s on layers that commute with the slab Hamiltonian at three random momenta form a space of
dimension EXACTLY 1, the uniform phase (smallest nonzero singular value 0.679). [T] This is because each inter-layer
hop T = beta/2 - i alpha_4/2 is nonzero and ties c_s = c_(s+1).

A3 [T], the reading of the adopted rules. The Links clause makes registers "valued in the update's symmetries of matter
modes", one register per factor on each face of the factor's role blocks, with Gauss's law in every B_f-block.
- By A2, the only layer symmetry is the uniform one. So every gauge factor acts on BOTH walls with the same charge.
- The two walls carry opposite chirality, so sum Gamma q^3 = 0: the slab is vector-like under every register.
- On the floquet slab the layers are a role-block coordinate. There they all lie inside one B_f-block, and hops inside a
  block are undressed. The one face register then dresses near and far modes alike: the same conclusion, directly.
- A far-only register would violate Gauss's law. ||[H, Q_far]|| = ||T|| = 1.0000 is a cutoff-scale violation carried
  by bulk modes. Between the two wall Weyls it is |1 - m|^Ls (5.5e-4, 1.4e-5, 3.6e-7 at Ls = 8, 12, 16; slope -0.916 =
  ln 0.4). So a "mirror charge" is conserved only approximately at low energy. That makes it no symmetry under the
  clause's exact-commutation wording, and Gauss's law forbids gauging it.

Answer to Q1. Under the adopted rules the gauge fields cannot localise to each wall. One register couples both walls, so
the mirror carries OUR charges with the opposite hand. The measured V-A structure and the Z width then require the
mirror to be gapped (SMG, far-wall-smg) or decoupled by some other mechanism. That is why "remove the mirror" is forced
within the present rules. It is not forced by measurement alone: the owner is right that measurement needs only
low-energy decoupling.

The exits, which need NEW rules (not adopted, not tested here):
- (X1) Dvali-Shifman (Dvali-Shifman 1997, cited as supplied). A bulk in a CONFINING phase with Coulomb-phase walls
  localises a separate massless gauge field on each wall. A1e is its strong-coupling caricature: inter-layer plaquette
  stiffness goes to 0, giving one photon per wall.
  - It needs a physical extra dimension carrying its own registers (owner decision 5; bends the Lattice axiom).
  - It needs a bulk group that confines while the wall group stays deconfined. DS break a larger bulk group on the wall,
    and that group is supplied by name, which is a gate risk.
  - Bulk charged modes then still connect the walls at the confinement scale.
  - Not computable here. It is non-perturbative and lies outside any Gaussian toy.
- (X2) A projected-symmetry link rule: registers valued in symmetries of the low-quasi-energy (wall-mode) block of the
  update. By A2h it violates Gauss's law at |1 - m|^Ls on wall modes and at O(1) on bulk modes, so it fails the
  clause's Gauss's law unless the bulk modes are themselves excluded.

## B. If a separate mirror world existed: observable consequences (Q2) [E, supplied numbers]

- T'/T. The rules give no temperature asymmetry.
  - The slab's excitation rules fill both ends equally (gk-smoothed-layers).
  - CL-3's de Sitter phase has no inflaton (a scalar seed needs a supplied clock), so there is no asymmetric reheating.
  - The family-class tick's near/far difference is a turn-charge label, not an energy split.
  - So T'/T = 1 is the rule-set value [S].
- N_eff. A full SM mirror at T ~ 1 MeV has g* = 10.75, giving Delta N_eff = (10.75/1.75) x^4 = 6.14 x^4.
  - At x = 1: Delta N_eff = 6.14, against an allowance of ~0.3 (~36 sigma at sigma 0.17). EXCLUDED.
  - Allowed only for x < 0.470 (Delta N_eff(0.45) = 0.25). That needs a SUPPLIED reheating asymmetry
    (Berezhiani-Dolgov-Mohapatra-type), which no rule gives.
- Abundance. Symmetric baryogenesis gives Omega'_b = Omega_b. Measurement needs Omega_c/Omega_b = 5.36. The asymmetry
  is supplied.
- Self-interaction. Mirror hydrogen has sigma/m ~ pi a0^2/m_H = 5.3e7 cm^2/g, against the cluster bound ~1 cm^2/g.
  Mirror baryons are a dissipative atomic gas, not collisionless dark matter.
  - All-DM survives only in the Foot-type picture: halos kept puffed by ordinary supernova heating through kinetic
    mixing eps ~ 1e-9. That picture is contested and it fixes eps.
  - The supplied dissipative-DM limits (dark disks, CMB/LSS) allow a mirror FRACTION of ~5%, for x <~ 0.3-0.47.
- Kinetic mixing. IF separate fields existed, wall tails give eps ~ (alpha/3 pi) |1 - m|^(2 Ls) ln(Lambda/mu) ~ 6e-15
  at Ls = 16, far below ~1e-9. That is allowed, but it is then too small for Foot's halo heating.
- Low-energy safety. With separate fields, V-A, N_nu and the charged-state bounds are untouched, because mirror states
  have zero OUR-charge up to |1 - m|^(2 Ls).

Answer to Q2:
- With all of DM, at the rule-set T'/T = 1: EXCLUDED (N_eff; abundance ratio 1, not 5.36; collisional halos).
- As a fraction <~5% with supplied x < 0.47: ALLOWED.
- As all DM with supplied x and baryon asymmetry: only in the contested dissipative-halo picture, which needs
  eps ~ 1e-9, not the rule-set ~1e-14. Disfavoured.

## C. Gate status (Q3)

The mirror world fails as a rule under the present Links clause (A3).
- A rule enabling it (X1 or X2) must bend the Links clause, plus the Lattice axiom for X1.
- It must supply T'/T and the mirror baryon asymmetry. These are fitted to N_eff and Omega_c/Omega_b, so they are
  FITTED and do not count.
- X1 also supplies a bulk group by name.
- Gate: FAIL for a mirror world as the dark matter. X1 as a pure chirality mechanism, with the mirror as a sub-5% fraction
  and T'/T supplied, is UNTESTED. Its one unbuilt prediction would be a mirror sector with eps ~ |1 - m|^(2 Ls) and
  Delta N_eff = 6.14 x^4.

## Verdict

- MIRROR-WORLD consistent with the adopted rules: NO. The Links clause plus Gauss's law give one gauge field on both
  walls, which is vector-like. Removing (gapping) the mirror is forced by the rules, not by measurement.
- Viable observationally: as a separate sector, YES as a small fraction with a supplied T'/T < 0.47. NO as all of DM at
  the rule-set T'/T = 1.
- Walls move: the open route is a confining-bulk (Dvali-Shifman-type) link rule. It needs owner decision 5 and is
  untested.

## Smuggling review

- Supplied: the Wilson slab and its m, Ls; the Gaussian U(1) toy; the cosmological numbers (g* = 10.75, Delta N_eff
  allowance 0.3, sigma 0.17, Omega_b h^2 = 0.0224, Omega_c h^2 = 0.120, cluster sigma/m ~1, 5% fraction, eps ~1e-9);
  the literature mechanisms (KOP, Foot, Berezhiani, Dvali-Shifman, BDM).
- Forced: flat zero mode (A1); uniform-phase-only commutant (A2e); vector-like charges under the Links clause (A3); the
  Gauss violation size (A2g/h).
- No measured number was chosen to pass anything.
