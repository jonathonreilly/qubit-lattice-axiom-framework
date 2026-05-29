# Bounded-to-Retained Re-audit Queue (2026-05-29)

**Purpose:** rank high-leverage `retained_bounded` rows that look eligible
for claim-type / scope re-audit as `positive_theorem` without adding any new
framework axiom. This is the next-tier successor to the 2026-05-22 promotion
queue and the 2026-05-23 bounded-to-retained queue, whose targets have largely
already converted to `retained` and are no longer in scope here.

**Operating rule:** this queue does not retag the ledger. It only identifies
rows that should be opened for direct review. The reviewer/audit lane owns any
claim-type change. Nothing in this file is an audit verdict, and it must not
be cited as proof that any row is `retained`.

**How the bucket is decided (ground truth):**
`docs/audit/scripts/compute_effective_status.py` maps
`claim_type: bounded_theorem -> retained_bounded` and
`claim_type: positive_theorem -> retained`. A conversion is therefore the
audit lane re-typing `bounded_theorem -> positive_theorem` on a fresh
re-audit, applied only through `docs/audit/scripts/apply_audit.py` in the
audit lane. This manifest does not perform that re-typing.

**Baseline:** current `origin/main` at `96d90f5ed`. Counts read directly from
`docs/audit/data/audit_ledger.json` (`effective_status == "retained_bounded"`).

**Selection rule:** prefer already-audited clean `bounded_theorem` rows with
large downstream reach where the safe positive scope is exact local algebra,
finite representation theory, a closed-form identity, existence-uniqueness, an
onset coefficient, or operator realization. Longer descendant chains are ranked
first. Rows whose bounded status protects a still-open physical closure are only
listed with a narrowed safe scope, or held back in the explicit non-automatic
section.

## Triage Summary

595 rows are `retained_bounded` on the baseline ledger. Excluding the five
rows in flight in a separate review packet leaves a triaged pool of 590, sorted
into three classes by `claim_scope` (and, for the ranked entries, by opening the
note):

| Class | Count | Meaning |
|---|---:|---|
| SPURIOUS bound (exact core, conservatively typed) | ~172 | Load-bearing content is exact local algebra / finite representation theory / a closed-form identity / existence-uniqueness / an onset coefficient / an operator realization. Bounded→positive candidate. |
| REMOVABLE bound (restricted-but-extendable) | ~16 | Exact on a finite block / enumerated range / minimal config / conditional on a named premise; derivation work could extend it. Candidate, but tag the extension as the open piece. |
| GENUINE bound (leave alone) | ~402 | Bounded interval, support-only quantitative match, finite-box coefficient support, blocker/obstruction, or conditional on an admitted input (P1 / AC_phi_lambda / S / theta). Converting these would overclaim. |

These class counts are a heuristic triage and are deliberately conservative
toward GENUINE: over-converting a bounded row is the dangerous error, so any row
whose scope carries an admitted-input, support-only, finite-box, or
conditional-premise signal is left in GENUINE. The precise per-row class is
reviewer-owned; only the ranked entries below were confirmed by opening the
note.

## Highest-Impact Queue

| Rank | Claim id | Downstream | Current status | Proposed re-audit scope | Why this can help |
|---:|---|---:|---|---|---|
| 1 | `oh_schur_boundary_action_note` | 718 | `retained_bounded` | Exact Schur-complement DtN boundary action on the finite `R=4` shell: `Lambda_R = H_tt - H_tb H_bb^{-1} H_bt`, `E_R(f)=1/2 f^T Lambda_R f`, `grad E_R = Lambda_R f`, and `Lambda_R f - j = 0` for the microscopic trace flux. | Highest reach. The exact lattice DtN / Schur identities are finite linear algebra; the bound is the general Einstein/Regge/all-`R`/arbitrary-source theorem, which stays out of scope. |
| 2 | `dm_neutrino_weak_vector_theorem_note_2026-04-15` | 525 | `retained_bounded` | Exact finite Clifford representation theorem on `C^16`: `Y_i = P_R Gamma_i P_L` is an exact `SU(2)` weak vector under `B_a`, has spin-1 adjoint Casimir, and satisfies `Tr(Y_i^dag Y_j) = 8 delta_ij`. | The covariance and trace-orthogonality are exact representation theory; the bound is only the homogeneous overall coefficient, which stays support-only. |
| 3 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | 717 | `retained_bounded` | Exact finite cone-cap construction certificate for the explicit cubical-boundary family at `R=2,3,4`. | Exact constructive combinatorics on the enumerated range; bounded only by the arbitrary-PL-cap / `S^3` / homogeneity extension. |
| 4 | `s3_cap_uniqueness_note` | 716 | `retained_bounded` | Exact finite cone-cap construction certificate for the cubical-ball family at `R=2,3,4,5`. | Exact finite construction; bounded only by global cap uniqueness, arbitrary PL cap classification, and PL `S^3` compactification. |
| 5 | `s3_boundary_link_theorem_note` | 714 | `retained_bounded` | Exact exhaustive 256-subset octahedral certificate (`K_simp(P)` is a PL 2-disk for every connected proper `P`) plus `R=2..10` link verification. | The 256-subset enumeration is a complete finite combinatorial theorem; bounded only by the unrestricted all-`R` cubical-ball closure. |
| 6 | `s3_general_r_derivation_note` | 710 | `retained_bounded` | Exact finite boundary-link disk certificate for `R=2..10` plus finite cone-cap certificate for `R=2..5`. | Exact finite construction/verification on the enumerated ranges; bounded only by all-`R` closure, global uniqueness, and PL `S^3` identification. |
| 7 | `higgs_mechanism_note` | 483 | `retained_bounded` | Exact finite-dimensional algebra of the admitted quartic `V(r)=(1/2)m2 r^2 + (1/4)lambda r^4` on `r>=0`: global-minimum cases and radial curvature. | Radial-potential minimization is exact closed-form calculus; the bound is the scalar substrate, Coleman-Weinberg potential, and physical Higgs mass, which stay out of scope. |
| 8 | `dm_neutrino_cascade_geometry_note_2026-04-14` | 467 | `retained_bounded` | Exact `C^8` weak-axis operator realization for `Gamma_1`: `P_T1 Gamma_1 P_T1 = 0`, rank-1 `O_0` plus rank-2 `T_2` split, second-order return `diag(1,0,0)+diag(0,1,1)=I_3`. | Operator-geometry decomposition is exact finite linear algebra; the bound is the physical neutrino-Yukawa cascade interpretation. |
| 9 | `pmns_graph_axis_to_active_lane_bridge_note` | 406 | `retained_bounded` | Exact finite-dimensional algebra on `C^8=(C^2)^{otimes 3}`: residual `Z_2` axis stabilizer maps to `P_23` on the active Hermitian triplet lane, forcing `P_23 H P_23 = H`. | Stand-alone finite-dimensional bridge lemma with a full runner; the bound is active-sector assignment and value selection. |
| 10 | `pmns_graph_first_forward_cycle_residual_swap_bridge_narrow_theorem_note_2026-05-24` | 405 | `retained_bounded` | Exact finite-dimensional algebra on `V_1`: forward 3-cycle and residual `P_23` action induce the stated cycle-channel and antiunitary residual-swap identities. | Exact finite-dimensional identities; the bound is the downstream coefficient / orientation-selection law. |
| 11 | `pmns_oriented_cycle_selection_structure_note` | 402 | `retained_bounded` | The three displayed finite `3x3` identities for `C`, `I_3`, `P_23`, `A_fwd(c)`, and `S(A)=P_23 A^dagger P_23`: cyclic coefficient permutation, the `C_3` fixed locus, and the swap-conjugation fixed locus. | Already narrowed in source to raw finite matrix identities; pure exact matrix algebra. |
| 12 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | 240 | `retained_bounded` | Exact finite-Grassmann Berezin identity: `Z_F = int prod dchi-bar dchi exp(-chi-bar M chi) = det(M)` for any complex `M`, plus odd-correlator antisymmetry, under explicit anticommutation + Berezin hypotheses. | Pure finite Grassmann calculus with all hypotheses explicit; the bound is the deliberate isolation from physical Hilbert-space identification and any bosonic no-go. |
| 13 | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | 237 | `retained_bounded` | Exact algebraic bridge between two retained primitives (the `Cl(3)` faithful dim-2 readout and the Berezin determinant identity): the substep-1 Grassmann-vs-bosonic dichotomy on `H_Lambda = V^{otimes|Lambda|}`. | Finite algebraic bridge on already-retained primitives; the bound is the open staggered-Dirac realization gate. |
| 14 | `pmns_commutant_eigenoperator_selector_note` | 194 | `retained_bounded` | Exact `C_3` representation-theoretic decomposition of the corner-trace profile of a projected non-`Cl(3)` commutant generator on the `hw=1` orbit, with the one-way `Cl(3)`-span vanishing check. | Exact finite `C_3` Fourier/representation decomposition; the bound (bridge to physical PMNS observables) is explicitly outside the load-bearing chain. |
| 15 | `koide_cyclic_projector_block_democracy_note_2026-04-18` | 189 | `retained_bounded` | Exact cyclic-projector circulant algebra: `B0=I`, `B1=C+C^2`, `B2=i(C-C^2)`, the exact cyclic responses/target reconstruction, and the response-space identity `2 r0^2 = r1^2 + r2^2`. | Exact finite circulant / cyclic-projector algebra; the bound is the physical Koide-selector interpretation, which stays a candidate. |
| 16 | `su3_wigner_intertwiner_block3_theorem_note_2026-05-03` | 169 | `retained_bounded` | Exact finite combinatorial geometry of the `L_s=3` PBC cube: 27 sites, 81 directed links, 81 unique unoriented plaquettes, and the verified each-link-in-4-plaquettes incidence. | Exact finite combinatorial enumeration verified exhaustively; the bound is the broader cube-closure campaign verdict. |
| 17 | `hierarchy_matsubara_decomposition_note` | 524 | `retained_bounded` | Exact closed-form temporal Matsubara decomposition on the minimal `L_s=2` block: `|det(D+m)| = prod_omega [m^2 + u_0^2 (3 + sin^2 omega)]^4`, with the intensive free-energy and condensate decompositions. | Exact closed form on the minimal block; bounded only because restricted to `L_s=2` (general-`L_s` extension is the open piece). |
| 18 | `hierarchy_spatial_bc_and_u0_scaling_note` | 484 | `retained_bounded` | Exact minimal `L_s=2` statements: temporal-APBC determinant formulas for spatial PBC/APBC, the BC-independent zero-mass `u_0^(8 L_t)` power, the APBC-only finite intensive small-`m` coefficient limit, and local `m/u_0` homogeneity. | Each listed statement is exact on the minimal block; bounded only by larger-block generalization. |

## Explicit Non-Automatic Cases

These representative GENUINE-bound rows must stay `retained_bounded`. Converting
them would overclaim, so they are not in the queue above.

- `yt_ward_identity_derivation_theorem` (reach 966) is bounded on the *admitted*
  canonical `Q_L=(2,3)` surface; the `1/sqrt(6)` single-component matrix element
  is exact, but the row carries no SM Yukawa readout, and converting it would
  read as upgrading the conditional top-Yukawa chain. Leave bounded.
- `g_bare_derivation_note` (reach 932) and the rest of the `g_bare` chain are
  bounded because the `g_bare^2 = 1` conclusion is conditional on scoped Wilson
  matching, `beta = 6`, and the same-1PI bridge, none of which is itself
  retained. The `g_bare = 1` forcing claim stays conditional until those
  premises retain; do not promote any link in this chain.
- `strong_cp_theta_zero_note` (reach 903) closes `theta_eff = 0` only on the
  explicitly theta-free Wilson-plus-staggered action surface. It is conditional
  on that admitted action surface, not an unbounded strong-CP solution.
- `plaquette_self_consistency_note` (reach 776) is a bounded finite-volume
  observable existence claim with diagnostics only, not a same-surface or
  infinite-volume `0.5934` certificate. Support-only.
- `hypercharge_identification_note` (reach 647) is a bounded chain-assembly
  theorem conditional on the admitted `P1-P4` premise packet and the imported
  `Sym^2/Anti^2` ratio. It does not derive matter assignment or physical
  hypercharge; converting it would promote admitted inputs.
- `tensor_support_center_excess_law_note` (reach 620) mixes an exact seven-site
  center-excess scalar formula with a cached-runner affine-fit support claim to
  numerical tolerances. This is a mixed row: split the exact formula from the
  cached-runner support before any positive re-audit; do not promote as-is.
- `universal_gr_polarization_frame_bundle_blocker_note` (reach 516) is a blocker
  recording that the current stack gives only a frame-orbit family, not a
  canonical `Pi_curv` projector bundle. A blocker is a genuine bound by
  construction.
- `higgs_from_lattice_note` (reach 497) is explicitly bounded quantitative
  support only; promotion needs a separate Higgs authority-boundary rewrite
  (already retired in the 2026-05-23 queue for the same reason).
- `gauge_vacuum_plaquette_local_environment_factorization_theorem_note`
  (reach 184) is an intentionally finite-box coefficient packet at fixed
  `beta = 6` and explicitly disclaims the operator-level factorization bridge.
  It is finite-box support, like the retired `rho_pq6` row.

Held back from the ranked queue but not strictly GENUINE (recorded in the JSON
`retired_targets`): `wilson_bz_corner_hamming_staircase_bounded_note_2026-05-08`
(its exact identity is already lifted by an unaudited closed-form companion —
target the companion), `g_bare_rigidity_theorem_note` (exact but load-bearing in
the open `g_bare` closure), `koide_circulant_wilson_target_note_2026-04-18` (an
assembler that imports its exact identity from a narrow theorem — target the
narrow theorem), and `r_base_group_theory_derivation_theorem_note_2026-04-24`
(exact `31/9` arithmetic but conditional on the admitted `3/5` normalization).

## Review Notes

- Re-audit each row independently; do not bulk-retag. A clean retag is applied
  only through `docs/audit/scripts/apply_audit.py` in the audit lane.
- Keep stronger physical closures out of the positive scope. The proposed scope
  for each row is strictly the exact sub-statement; everything physical stays
  in the bound.
- Split mixed rows first. If a row mixes exact algebra with support-only or
  cached-numeric content (e.g. `tensor_support_center_excess_law_note`), land
  the source split as a separate review packet before requesting audit.
- The auditor's restricted packet should not include this file, prior audit
  rationales, the 2026-05-23 queue, or publication-facing retained summaries.
- Use the JSON companion at
  `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-29.json` for
  dispatcher tooling.
