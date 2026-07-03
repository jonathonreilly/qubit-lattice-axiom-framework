# Beta=6 SU(3) Wilson Single-Plaquette Closure Research Map - Note

**Status:** research map / planning note - this note records the
retained-vs-open state, the consolidated blocked-route ledger, and the ranked
closure-route analysis for the beta=6 SU(3) Wilson single-plaquette
closure lane. It is **not** a closure, promotion, retirement, or new
theorem of any kind. It introduces no value, no new authority, and no new
vocabulary.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome for any cited claim_id; all statuses
quoted below are read-offs from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on the dates stated.
**Date:** 2026-05-29
**Type:** meta (research-map / planning content only; this is not a
theorem, no-go, audit verdict, or claim-retagging surface)
**Script:** none (no new computation; two load-bearing constants were
independently recomputed for self-consistency — see Section 7).

## 0. Scope and what this note is for

The thermodynamic SU(3) Wilson single-plaquette expectation at the framework
point beta=6,

```
<P>(beta=6, L->infinity) ~= 0.5934   (canonical lattice-QCD comparator),
<P> := <(1/N_c) Re Tr U_p>,  N_c = 3,
```

is the single most-cited open quantitative gate in the framework: it feeds
`u_0 = <P>^(1/4)` (the 1/4 exponent is itself a retained_bounded theorem,
`u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17`), then
`alpha_s(v) = alpha_bare/u_0^2` (vertex power n_link=2 retained,
`alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`),
then `alpha_s(M_Z) ~= 0.1181`, and via the same `alpha_LM` it touches the
v / y_t / m_t / m_H chain. The number is currently obtained **only** as an
admitted comparison/reuse number (`plaquette_self_consistency_note`,
withdrew value-closure language 2026-05-25) and reproducibly via a numerical
Monte-Carlo finite-size-scaling extrapolation
(`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`,
P_inf = 0.59400 +/- 0.00037). Neither is an analytic from-primitives
derivation.

This is a multi-session research problem. The purpose of this note is to map
the open-route surface and identify the most useful next calculation,
**not** to claim closure. Five candidate analytic/structural routes were
generated and put through a review pruning pass (Section 5). **Zero routes
currently qualify as a closure-ready derivation.** Section 4 records the most
informative blocked route worth further testing and the concrete obstruction
that blocks it today; Section 6 states the one concrete next step worth
attempting.

## 1. Retained-vs-open state (ledger read-off, 2026-05-29)

All statuses below are read directly from
`docs/audit/data/audit_ledger.json` (`rows[<claim_id>]['effective_status']`)
on 2026-05-29; the ledger carried 2509 rows on this worktree. **Several rows
that prior synthesis notes recorded with older statuses have since moved**
(Section 2); the table below is the live read-off.

### 1a. Retained (operator realization, existence/uniqueness, structure)

| claim_id | effective_status | what it gives |
|---|---|---|
| `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | retained | Exact one-clock realization Z=Tr[T^Lt]; plaquette source = multiplication by J=(chi_{1,0}+chi_{0,1})/6; exact six-neighbour SU(3) dominant-weight recurrence; spectrum(J) in [-1/2,1]. Names the open piece as transfer-state identification at beta=6. |
| `gauge_vacuum_plaquette_reduction_existence_theorem_note` | retained | Existence + uniqueness + analyticity + strict monotonicity of the implicit reduction law beta_eff,L(beta)=P_1plaq^{-1}(P_L(beta)); bijection [0,inf)->[0,1); onset beta_eff=beta+beta^5/26244+O(beta^6). |
| `plaquette_self_consistency_note` | retained_bounded | Finite Wilson <P> is a unique bounded observable of Z_L(beta); 0.5934 is an admitted comparison/reuse number, value-closure language withdrawn 2026-05-25. |
| `plaquette_observable_uniqueness_bounded_note_2026-05-25` | retained_bounded | Affine identity <P>=1+(1/N_plaq) d ln Z/d beta; structural uniqueness of the observable, numeric-value half explicitly excluded. |
| `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | retained_bounded | SINGLE-LINK normalized Wilson coefficients rho_{p,q}(6) on box 0<=p,q<=4 by two independent integrators (agree 4e-15). NOT the multi-link environment coefficients. |
| `u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17` | retained_bounded | Derives the 1/4 exponent in u_0=<P>^(1/4) from the four-link loop count; does NOT derive <P>. |
| `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10` | retained | alpha_s(v)=alpha_bare/u_0^2 (n_link=2); consumes a <P> value, does not produce one. |
| `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | retained_bounded | T_src(6)=exp((beta/2)J) D_beta exp((beta/2)J) with D_beta central/diagonal. |
| `gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10` | retained | Temporal-gauge linkwise factorization; four-marked-link compression D_beta^loc chi=a^4 chi. (Proven in temporal gauge only — see Section 5, Route 4.) |
| `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | retained | Diagonal central operator R chi=rho chi EQUALS normalized convolution C_{Z/Z00} on the finite character basis. |
| `gauge_vacuum_plaquette_local_environment_factorization_theorem_note` | retained_bounded | Bounded finite NMAX=4, MODE_MAX=80, beta=6 packet (positivity/self-adjointness/conjugation-symmetry). Does NOT close the full beta=6 solve. |
| `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | retained_bounded | Finite-box diagonal character-measure formalism, rho_{0,0}=1. |
| `gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note` | retained_bounded | Finite tensor-transfer packet. |
| `gauge_vacuum_plaquette_residual_environment_identification_theorem_note` | retained_bounded | Names the residual environment operator C_{Z_6^env} after the local marked-link factor is stripped; the object whose rho_{p,q}(6) is missing. |
| `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | retained_bounded | Two REFERENCE Perron solves with rho supplied as input: rho=1 -> P_loc(6)=0.4524, rho=delta -> P_triv(6)=0.4225. Houses the Theorem-3 underdetermination statement. |
| `plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05` | retained_bounded | The only in-repo route reaching the target: P_inf=0.59400 +/- 0.00037 (1/L^4 fit, L in {3,4,5,6,8}); numerical, not analytic, comparator-only. |
| `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | retained | Exact first nonlinear coefficient: P_full(beta)=P_1plaq(beta)+beta^5/472392+O(beta^6); the order-5 survivors are four closed cube shells (4/18^5). |
| `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | retained | Exact BBGKY source-derivative identity d/dbeta = sum_r d/dJ_r. |
| `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | retained | SU(3) fusion/adjoint-generator/Casimir primitives. |
| `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | retained | 4-fold Haar projector P^G_{(1,1)^4} on C^4096, rank-8 exact link-integration primitive. |
| `su3_fusion_engine_pr1_theorem_note_2026-05-03` | retained_bounded | Fusion multiplicities N^nu_{lam,mu} on box {0<=p,q<=4}. |
| `su3_cube_perron_solve_combined_theorem_note_2026-05-03` | retained_bounded | L_s=2 PBC cube encoder, bipartite 6:6 adjacency, trivial-sector P=0.4225 recovery; Schur 0-parameter cube value P=0.4291. |
| `su3_low_rank_irrep_picard_fuchs_odes_note_2026-05-05` | retained_bounded | Order-3 PF ODE catalog for 7 low-rank irreps + exact c_{p,q}(6). |
| `plaquette_v1_picard_fuchs_ode_note_2026-05-05` | retained_bounded | Origin V=1 PF ODE; exact <P>_{V=1}(6)=0.422531739650. |
| `plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_theorem_note_2026-05-17` | retained_bounded | Exact-rational closure of the (r=2,d=12) rank-exclusion cell; r<=2 empty kernel. |
| `su3_wilson_closed_form_fanout_theorem_note_2026-05-04` | retained_bounded | Bounded record of four closed-form beta=6 values: M1=0.4225, M2=0.3333, M4=0.8740, M5=0.9259. |
| `gauge_vacuum_plaquette_compressed_rim_evaluation_theorem_note_2026-04-17` | retained_bounded | Compressed Peter-Weyl evaluation law Z_6^env(W)=<K(W),v_6>: once v_6 is known the marked-W dependence is automatic. |

### 1b. The exact open beta=6 residual

The single un-derived analytic step is uniformly identified across the lane:

> **Open object:** the boundary character measure / class-sector amplitude
> vector of the unmarked 3D spatial Wilson environment at beta=6 —
> equivalently `rho_{p,q}^env(6)` (the eigenvalue sequence of the residual
> environment convolution), equivalently the Perron eigenvector of the
> positive transfer operator `T_src(6)` on the source-cyclic SU(3)
> class-function subspace, equivalently the exact class-sector matrix
> elements of the one-slab Wilson/Haar bulk kernel `K_6^env` and the
> full-slice rim lift `B_6(W)`.

Producing this vector analytically yields `P(6)` (target 0.5934), `beta_eff(6)`,
`u_0`, and the whole alpha_s chain. Everything upstream of this single
evaluation is retained; only the analytic evaluation of the multi-link
spatial-environment Perron data remains open.

The reduction of the seam **to** this evaluation is now itself only a
**purely formal linear-algebra lemma**, not a physical reduction (Section 2):
the audit of `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17`
narrowed it (2026-05-28) to an abstract `(S, eta, K)` statement and listed
**four required-but-unsupplied retained authorities** for the physical
identification — full Wilson/Haar one-slab kernel; full-slice rim-lift; exact
kernel/rim compression; exact compressed rim-evaluation. The physical
beta=6 application is explicitly out of scope of that note's load-bearing
claim.

## 2. Status corrections vs. prior synthesis (memory-staleness flags)

Per the standing operational rule "verify ledger before citing memory," the
following four rows have moved since the 2026-05-10 / 2026-05-17 synthesis
inputs and are recorded here so future cycles cite the live status:

| claim_id | prior synthesis status | live status (2026-05-29) | consequence for the lane |
|---|---|---|---|
| `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | audited_conditional | **ledger read-off: retained_bounded effective status** — but only as a purely formal abstract `(S,eta,K)` linear-algebra lemma; physical beta=6 identification explicitly out of scope (needs 4 unsupplied authorities) | The "seam is reduced to matrix-element evaluation" framing holds only abstractly; the physical reduction is itself unsupplied. The open residual is deeper than "just evaluate." |
| `gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17` | audited_conditional | **audited_renaming** — audit flags the identity rho=kappa/a^4 as a definition/packaging of the stripped residual eigenvalue sequence, NOT an independent derivation of the environment boundary class function | The "(T1') identity" that one surviving-route candidate leaned on is audit-flagged as circular packaging (relevant to Route 4 below). |
| `gauge_vacuum_plaquette_beta6_scalar_value_insufficiency_note_2026-04-17` | unaudited (no_go) | **audited_conditional (no_go)** — bounded formal warning: one scalar sample insufficient to recover the N-dimensional retained coefficient vector | Strengthens (does not weaken) the open-target framing: scalar reuse cannot replace the vector evaluation. |
| `su3_wigner_l3_treewidth_infeasible_2026-05-04` | unaudited | **audited_conditional** | The treewidth-29 infeasibility result is now audited; the foreclosure of exact L_s>=3 contraction is on firmer footing. |
| `su3_wigner_l3_cube_haar_mc_negative_result_2026-05-04` | audited_conditional | **ledger read-off: retained_bounded effective status** | The naive-Haar-MC sign-problem foreclosure is now retained_bounded. |

Unaudited author-tier consumers/supports (cite as unaudited, not as
retained): `alpha_s_derived_note`, `complete_prediction_chain_2026_04_15`,
`plaquette_v1_picard_fuchs_ode_all_order_proof_note_2026-05-09`,
`bridge_gap_hk_plaquette_closed_form_note_2026-05-06`,
`exact_tier_ewitness_bounded_note_2026-05-07_ewitness`,
`spatial_slab_transfer_operator_positivity_and_delta_x_real_note_2026-05-19`,
`su3_cube_full_rho_perron_2026-05-04`, `su3_z3_apbc_variant_probe_2026-05-04`,
`su3_bridge_clean_tube_k12_support_2026-05-04`,
`plaquette_bootstrap_framework_integration_note_2026-05-03`.

## 3. Consolidated blocked-route ledger

This is the consolidated catalog of blocked or superseded routes so the lane
does not reuse them as closure candidates without new source input. **20
distinct blocked routes**, each grounded in a repo note. The no-go / bounded
notes that establish each boundary are cited; statuses are the live 2026-05-29
read-off.

### 3a. Closed-form / single-frame routes (all far-miss; `su3_wilson_closed_form_fanout_theorem_note_2026-05-04`, retained_bounded)

1. **M1 single-plaquette Haar character expansion = 0.4225.** Misses all
   inter-plaquette correlation; identical to the V=1 value and P_triv.
2. **M2 leading strong-coupling beta/(2N^2) = 0.3333.** Strict leading order;
   undershoots in the crossover.
3. **M4 Drouffe-Itzykson mean-field self-consistency (z=6) = 0.8740.**
   beta_eff jumps to ~31.5 (deep weak coupling); overshoots. This is the
   only blocked "mean-field self-consistency" frame.
4. **M5 weak-coupling 1-loop 1-4/54 = 0.9259.** Not yet asymptotic at beta=6;
   overshoots.

### 3b. V=1 Picard-Fuchs (finite-window support, wrong observable)

5. **V=1 single-plaquette Picard-Fuchs ODE / Frobenius (Lee-Yang) zero
   localization.** Runner-backed finite-window support (exact checks through
   the verified Taylor window, finite-grid lower-order exclusion, indicial
   roots {-4,-3,0}, and conditional Bostan-Salvy-Schost arithmetic if an
   external all-degree R=3,D=2 bridge is supplied), but not standalone
   all-degree Picard-Fuchs closure. In any case it yields only the
   single-plaquette-in-isolation value 0.4225. Explicitly does NOT close the
   thermodynamic limit, multi-plaquette generalization, or higher-irrep
   extension. Notes: `plaquette_v1_picard_fuchs_ode_note_2026-05-05`
   (retained_bounded); finite-window boundary companion unaudited.

### 3c. Finite L_s=2 cube (cannot host the correlation length)

6. **L_s=2 APBC cube full-rho Perron with d^(-16) factor = 0.4291**
   (`su3_cube_full_rho_perron_2026-05-04`, unaudited). APBC == PBC under the
   all-forward convention; d^(-16) Haar pairing over-suppresses large rho.
7. **L_s=2 Z3 center-twist APBC phase variants** (`su3_z3_apbc_variant_probe_2026-05-04`,
   unaudited). Uniform Z3 twists cancel globally (symmetric & cocycle stay
   0.4291; one-direction toy moves AWAY to 0.4192).
8. **L_s=2 Schur 0-parameter cube = 0.4291** (`su3_cube_perron_solve_combined_theorem_note_2026-05-03`,
   retained_bounded). A specific finite-volume number, not the thermodynamic
   limit; L_s=2 PBC cannot host xi > 2a at the crossover.

### 3d. K-tube independent-product candidate and target-fit exponents

9. **rho=(c/c_00)^12 clean K-tube candidate = 0.5888**
   (`su3_bridge_clean_tube_k12_support_2026-05-04`, unaudited). Closest
   near-miss (0.78% = 15x eps_witness) but does not close; residual correction
   NOT derived from primitives.
10. **Target-fit exponent closures "12+2/pi" / "(N^2-1)/(4pi)" for the 0.78%
    gap** (`su3_bridge_pr525_flaw_fix_note_2026-05-05`, retained_bounded;
    `su3_bridge_clean_tube_k12_support_2026-05-04` Sec 4.1). The 2/pi correction
    is not a universal beta-family law; it imports an unproved correction term
    with no source-sector derivation. Preserved as review context, rejected as
    source authority. (Note: PR-525's "451% spread" refutation of the 1-loop
    interpretation was itself a methodological error — wrong denominator — so
    the 1-loop interpretation is neither foreclosed nor derived.)

### 3e. Exact L_s>=3 contraction / sampling (computationally foreclosed)

11. **L_s=3 PBC cube naive Haar Monte-Carlo**
    (`su3_wigner_l3_cube_haar_mc_negative_result_2026-05-04`, retained_bounded).
    Sign-problem-like: product of 81 mean-zero plaquette characters drives the
    integrand to ~1e-100; needs ~1e200 samples; gives P=0.108 (noise).
12. **Importance-sampled (standard Wilson) lattice Monte-Carlo at L_s=3**
    (same note, Sec 3). Would import 0.5934 as the answer — violates the
    forbidden-import policy; methodological foreclosure, not a derivation.
13. **Exact L_s=3 tensor-network contraction by naive node-elimination**
    (`su3_wigner_l3_treewidth_infeasible_2026-05-04`, audited_conditional).
    Link-adjacency graph (81 nodes, 324 edges, 8-regular) has treewidth >=29
    -> worst intermediate 8^30 ~ 1e27 entries ~ 1e19 GB, ~20 orders over a
    4 GB budget; bond-dim 2 already 16 GB; greedy fails at 65 TB.

### 3f. Transfer-operator / source-sector underdetermination (retained no-gos)

14. **Fix rho_{p,q}(6) from c_lambda(6) + SU(3) intertwiners + a 1-parameter
    rho-family ansatz** (`gauge_vacuum_plaquette_tensor_transfer_perron_solve_note`
    Theorem 3, retained_bounded). Decay, one-plaquette-env, and tube-power
    families each give a different P(6); combined Perron spread >= 0.1937,
    straddling 0.5934 with nothing canonically selecting it. The residual is
    "genuinely 3D-geometric." (Scope clarification 2026-05-04: this does NOT
    rule out 0-parameter derivations — but the L_s=2 Schur 0-parameter case
    gives 0.4291, demonstrating 0-parameter does not imply correct.)
15. **Re-derive P(6) / beta_eff(6) from the existing factorized source-sector
    transfer / Perron-Jacobi stack**
    (`gauge_vacuum_plaquette_perron_jacobi_underdetermination_note`,
    retained_no_go; `gauge_vacuum_plaquette_framework_point_underdetermination_note`,
    retained_no_go). The source-operator stack does not force the beta-6 Perron
    moments / Jacobi coefficients after the local marked-link factor is fixed;
    the finite jet + analyticity + monotonicity do not force beta_eff(6).
16. **Observable bridge <P>_full = R_O(beta_eff) from the current Wilson
    primitive packet** (`gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03`,
    retained_no_go). BRIDGE only PINS the missing nonperturbative number;
    escape requires a NEW independently-audited primitive.
17. **Spatial-environment transfer underdetermination**
    (`gauge_vacuum_plaquette_spatial_environment_transfer_underdetermination_note_2026-04-17`,
    retained_no_go). The spatial-environment transfer is underdetermined
    without the actual Wilson dynamics.
18. **Constant-lift closed-form guess beta_eff^can ~= 9.3295**
    (`gauge_vacuum_plaquette_constant_lift_obstruction_note`, retained_no_go).
    The closeness of 9.329531846653 to the implicit
    beta_eff^can = P_1plaq^{-1}(0.5934) = 9.32617 is a support coincidence, not
    a theorem.

### 3g. Scalar reuse and finite-order truncation

19. **Reuse a fixed scalar P(6) to recover the class-sector vector v_6 /
    rho_{p,q}(6)** (`gauge_vacuum_plaquette_beta6_scalar_value_insufficiency_note_2026-04-17`,
    audited_conditional no_go). Two distinct positive normalized 3-weight
    vectors share L(v)=1 but differ in M(v) and induce different boundary
    class functions; one scalar is one constraint, not the vector.
20. **Close the lane from a FINITE-ORDER truncation of the connected
    hierarchy** (`gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note`,
    retained_no_go). log Z_L is non-polynomial; no finite-order truncation
    closes the thermodynamic value.

## 4. Closure-ready routes after review pruning

**Closure-ready routes: 0.** All five candidate routes (Section 5) were judged
not closure-ready. There is therefore no route to rank as the next closure
attempt. This section records the **most informative blocked route** and the
**common obstruction**.

### 4a. Common obstruction

Every route that needs the genuine multi-plaquette (thermodynamic, beta=6)
content collides with one of two recorded foreclosures:

- **Computational foreclosure of the exact spatial-environment data.** Any exact
  evaluation of the unmarked 3D spatial Wilson environment at L_s>=3 is the
  treewidth-29-infeasible SU(3) tensor contraction (8^30 intermediate,
  `su3_wigner_l3_treewidth_infeasible_2026-05-04`), and naive Haar-MC is
  sign-problem-bound (`su3_wigner_l3_cube_haar_mc_negative_result_2026-05-04`).
  The connected-coefficient frontier is separate: current source notes now
  carry exact `d_5..d_9` data, with per-cluster link integrals handled by
  small invariant-projector contractions and shape-collapse/cube-sector
  certificates. That coefficient work sharpens the resummation route, but it
  does not evaluate the missing spatial-environment Perron data.
- **Algebraic underdetermination by local data.** Local character +
  intertwiner data + any 1-parameter rho-family do not select rho_{p,q}(6)
  (Theorem-3, `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note`); the
  finite jet + analyticity + monotonicity do not force beta_eff(6)
  (`gauge_vacuum_plaquette_framework_point_underdetermination_note`).

In one sentence: **the single missing object is uniformly `rho_{p,q}(6)`
(the boundary character measure / Perron eigenvector of the unmarked 3D
spatial Wilson environment), which is proven not determined by local
character + intertwiner data and proven infeasible to compute by exact
contraction at L_s>=3.** No current route supplies new dynamical input that
escapes both foreclosures.

### 4b. Most informative blocked route

Ranked by (tractability x likelihood-of-progress) among the blocked routes,
the most informative one is **Route 1: conformally-mapped / d-log-Pade resummation
of the connected-shell plaquette series**, for three reasons:

- It is the only route rated `long-shot` (not `infeasible`) that is **not**
  also `already_blocked` (Route 5 is also `long-shot` but is
  `already_blocked: true` and rests on a cost-arithmetic error).
- Its review finding explicitly isolates a **viable sub-kernel**:
  beta-plane d-log Pade on a complex-conjugate-pair singularity converges to
  1e-3 by ~[10/10] in a controlled proxy (complex-pair branch point at
  |beta_c| ~= 5.7, amplitude tuned to the physical Delta(6) ~ 0.171). The
  method is sound **if** the inputs and singularity structure cooperate.
- Its blocking obstructions are sharply named and separable from the method:
  (i) the old coefficient-engine shortfall is no longer the blocker because
  exact source notes reach `d_9`; (ii) the Borel-Leroy half is a category error
  for a finite-radius series and must be replaced by direct beta-plane analytic
  continuation; (iii) the complex-pair / d-log-Pade premise is not established
  by the now-known coefficients: the single-pair sign prediction fails at
  `d_8`, and the activated `[1/1]` d-log-Pade from `d_5..d_8` predicts the
  correct `d_9` sign but the wrong magnitude and a spurious real pole.

The other four are less actionable: Route 2 (finite-volume holonomic
continuation) is `infeasible` on three independent walls (data 10^36-10^72 supports;
certification bound R <= 3^81 ~ 10^232; order explosion). Route 3
(collective-field large-N saddle) is `infeasible` — the leading saddle lands
on blocked values (flat-density -> 0.4225; self-consistent ->
Drouffe-Itzykson 0.8740) and the core is the unsolved d>2 master field.
Route 4 (transverse-slab kappa self-consistency) is `infeasible` and
`already_blocked` - its dimensional collapse rests on an invalid axis-swap
of the temporal-gauge factorization, and its re-target via the rho=kappa/a^4
identity is circular (that identity is now `audited_renaming` =
definition/packaging, Section 2). Route 5 (nested-transfer-matrix slab) is
`long-shot` but `already_blocked` - the slab Hilbert dimension is
8^(2 L_perp^2) (8^32 at L_perp=4, the same order as the 8^30 wall), so the
advertised (8^L_perp)^2 cost is an arithmetic error, and beta=6 has
xi ~ 2-3 so reachable L_perp <= xi never enters the asymptotic regime.

## 5. The five routes and their review findings (preserved record)

Preserved so the lane does not regenerate them without new source input. Each
row: route, lens, review fields (`closure_ready` / `already_blocked` /
`feasibility`), and the one-line blocking obstruction.

| # | Route (one line) | closure_ready | already_blocked | feasibility | Blocking obstruction (one line) |
|---|---|---|---|---|---|
| 1 | Conformally-mapped Borel-Pade / d-log-Pade resummation of the connected-shell (linked-cluster) plaquette series | false | false | long-shot | The blocker is not a missing coefficient engine: exact source notes now reach `d_9` (`d_5=1/472392`, `d_6=7/5668704`, `d_7=5/17006112`, `d_8=5/272097792`, `d_9=-2035/264479053824`). Per-cluster SU(3) link integrals stay small on this frontier; the treewidth-29 wall bites the `rho_{p,q}(6)` spatial-environment contraction object, not these coefficient checks. Borel-Leroy remains a category error for a finite-radius series. The surviving beta-plane d-log-Pade kernel is only an open diagnostic: the single-complex-pair prediction fails at `d_8`, while the activated `[1/1]` from `d_5..d_8` gets the `d_9` sign but not the magnitude and returns a spurious real pole. |
| 2 | Finite-volume holonomic (Picard-Fuchs) continuation of L_s>=3 Z(beta) from strong coupling to beta=6, then 1/L^4 FSS | false | false | infeasible | Strong-coupling Taylor data for finite-volume Z_L at depth 40-80 needs ~10^36-10^72 connected supports (repo has computed exactly one nontrivial coefficient, beta^5); no a-priori D-finite (R,D) bound (closure bound R <= 3^81 ~ 10^232), so the ODE is a fit, not a certificate. |
| 3 | Collective-field (Jevicki-Sakita) large-N_c saddle of the spatial-environment kernel, 1/N_c^2 fluctuation at N_c=3 | false | false | infeasible | Leading saddle lands on blocked values (flat strong-phase density -> rho=delta -> 0.4225; self-consistent -> Drouffe-Itzykson -> 0.8740); the coupled-resolvent core is the unsolved d>2 SU(N) master field; 1/N^2 continuation has wrong analytic structure across a large-N bulk transition. |
| 4 | Transverse-slab self-consistent Perron closure for the source-sector eigenvalue sequence kappa_{p,q}(6) | false | true | infeasible | Dimensional collapse rests on an invalid axis-swap of the temporal-gauge linkwise factorization (proven only in temporal gauge; in-slab spatial plaquettes couple the crossing links). The rho=kappa/a^4 re-target is circular (now audited_renaming = packaging). Correct kernel is the treewidth-29-foreclosed 3D contraction. |
| 5 | Nested-transfer-matrix transverse-slab Perron solve at isotropic Wilson beta=6 | false | true | long-shot | Cost arithmetic wrong: slab Hilbert dim is 8^(2 L_perp^2) (8^32 at L_perp=4, same order as the 8^30 treewidth wall), not (8^L_perp)^2. The "a_{p,q} not heat-kernel" claim contradicts the cited slab note. beta=6 has xi ~ 2-3, so reachable L_perp <= xi never reaches the asymptotic exp(-Delta_x L_perp) regime. |

## 6. Most useful bounded next step and named obstruction

Because no route is closure-ready, there is no closure attempt to rank. The
previously recommended runnable increment - compute exact coefficients beyond
`d_5` - has now been completed and extended through `d_9`. That source work is
valuable because it falsifies several cheap resummation stories, but it is no
longer the lane's next open step.

### 6a. Completed increment and updated next step

Current exact connected coefficients for
`Delta(beta) = P(beta) - P_1plaq(beta)` are:

```text
d_5 = 1/472392
d_6 = 7/5668704
d_7 = 5/17006112
d_8 = 5/272097792
d_9 = -2035/264479053824
```

The coefficient frontier gives three useful negative diagnostics without
claiming `P(6)`:

- the geometric/tadpole single-ratio story fails because
  `d_7/d_6 = 5/21 != d_6/d_5 = 7/12`;
- the constant-amplitude single complex-pair story fails because it predicts a
  sign change at `d_8`, while exact `d_8` is positive;
- the first activated `[1/1]` d-log-Pade from `d_5..d_8` predicts a negative
  `d_9` but misses the magnitude and localizes a spurious real pole.

The updated useful next step is therefore not "get coefficients past `d_5`."
It is either (i) organize the connected series by a non-fitted analytic
graphical/closed-form rule that survives the exact `d_5..d_9` checks, or
(ii) attack the actual spatial-environment Perron data with a rank-aware
contractor or new analytic compression. Either path must still keep the
thermodynamic beta=6 value out of scope until the missing environment data are
supplied.

### 6b. Named obstruction after the coefficient frontier

**Spatial-environment data plus analytic-class control.** Exact connected
coefficients are now available through `d_9`, so the old "no data beyond `d_5`"
obstruction is retired. The remaining obstruction has two parts. First, the
source-sector value still needs the unmarked 3D spatial-environment Perron data
`rho_{p,q}(6)`, whose direct exact contraction is the treewidth-29 object.
Second, resumming the connected series into a beta=6 value would require an
analytic-class theorem strong enough to justify the continuation; the exact
`d_5..d_9` evidence currently breaks the simplest single-ratio and
single-complex-pair stories instead of supporting them. A genuine closure would
still require either a non-fitted analytic organization of the connected
coefficients or a rank-aware contractor that defeats the spatial-environment
wall, plus an independent analytic-continuation premise strong enough for the
chosen resummation.

## 7. Self-consistency check of the two load-bearing constants

To keep the note's quantitative anchors independent of memory, the two
load-bearing constants were recomputed here (mpmath, 50 dps) by rebuilding
J(beta) = int_{SU(3)} exp((beta/3) Re Tr U) dU from the order-3 recurrence
6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2},
a_0=1, a_1=0, a_2=1/36:

- `P_1plaq(6) = J'(6)/J(6) = 0.4225317396` (matches the retained V=1
  single-plaquette value and M1/P_triv).
- `beta_eff^can = P_1plaq^{-1}(0.5934) = 9.32617` (matches the implicit value
  in `gauge_vacuum_plaquette_constant_lift_obstruction_note`; confirms the
  constant-lift guess 9.3295 is a coincidence, not the value).

These reproductions are internal arithmetic checks only; they introduce no new
authority and set no audit outcome.

## 8. Key files

- `docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_SCIENCE_ONLY_NOTE_2026-04-17.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_BETA6_SCALAR_VALUE_INSUFFICIENCY_NOTE_2026-04-17.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_PERRON_JACOBI_UNDERDETERMINATION_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`
- `docs/SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md`
- `docs/SU3_WIGNER_L3_TREEWIDTH_INFEASIBLE_2026-05-04.md`
- `docs/SU3_WIGNER_L3_CUBE_HAAR_MC_NEGATIVE_RESULT_2026-05-04.md`
- `docs/SU3_BRIDGE_CLEAN_TUBE_K12_SUPPORT_2026-05-04.md`
- `docs/SU3_CUBE_FULL_RHO_PERRON_2026-05-04.md`
- `docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`
- `docs/PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`
- `docs/U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md`
- `docs/PLAQUETTE_OBSERVABLE_UNIQUENESS_BOUNDED_NOTE_2026-05-25.md`
- `docs/GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md`
- `docs/GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md`
- `docs/ALPHA_S_DERIVED_NOTE.md`

This note supersedes, on the four status rows flagged in Section 2, the
status table of `PLAQUETTE_ALPHA_S_CHAIN_AUDIT_MAP_SYNTHESIS_META_NOTE_2026-05-10.md`.
It is a research map only and asserts no closure.
