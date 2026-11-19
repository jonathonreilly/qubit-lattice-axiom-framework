---
claim_id: face_swap_parity_gives_a_tree_level_zero_theta_only_with_wall_local_electroweak_registers_and_shared_colour_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free-field slab checks and supplied-model mass-matrix toys for R1, the question 'does an exact slab face swap solve strong CP'. Exact on the working Wilson domain-wall slab (m = 0.6, Ls = 16): P_slab = layer reversal x 3D inversion x beta commutes with the slab update, maps the near Weyl onto the far Weyl with Gamma flipped and the same charges, and acts on the one flat link register as ordinary parity (A_i -> -A_i), so the theta carrier sum E.B is P_slab-odd. Exact: the overlap kernel is P-covariant, but Luscher's chiral projector maps to the opposite one (gamma5_hat -> -gamma5_hat); a far-wall-only term is not invariant. Toys (3 families, supplied): with one gauge field (adopted Links clause) P_slab-symmetric masses give generic O(1) theta_tree (median 0.81) once h != h'; a supplied Z2 gives theta_tree = 0, but the mirror Higgs then breaks our SU(2)xU(1) (v'/v <= 3.4, N_nu = 6, excluded); heavy vector-like masses leave no light chiral state. In the Barr-Chang-Senjanovic shape (separate electroweak registers per wall, shared colour, supplied) det(M_u M_d) > 0 exactly for every Y, v'/v in [1e2, 1e10] and VEV phase, with median light |J| 2.7e-2. SMG mirror: kappa = N_f, Z4 anomaly-free, theta_bar not tied to arg det Y. Estimates: P-even dim-6 (H'H' - HH) G Gdual and misaligned Yukawas bound v' < ~1e11 GeV; mirror-quark bound v' >~ 1e8 GeV; Delta N_eff 0.19-0.64. Not covered: the CL-1 cell slab itself (Wilson kernel used), the FREEZE slab, interacting SMG, a derivation of v', loops beyond the dressing proxy, a Gauss-law-consistent wall-local register rule."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_adopted_link_rule_puts_one_gauge_field_on_both_slab_walls_so_a_separate_mirror_world_needs_a_new_link_rule_and_a_supplied_temperature_asymmetry_bounded_theorem_note_2026-10-24
  - copy_sign_odd_vacua_give_a_tree_level_nelson_barr_block_only_if_the_light_doublet_mirror_pairing_is_absent_which_the_copy_sign_does_not_forbid_bounded_theorem_note_2026-10-24
runner: scripts/face_swap_parity_gives_a_tree_level_zero_theta_only_with_wall_local_electroweak_registers_and_shared_colour_2026_10_24.py
---

# Face-swap parity gives a tree-level zero theta only with wall-local electroweak registers and shared colour

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=23 FAIL=0, 0.07 s, 37 MB peak, 3.5 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (face_swap_parity_test_run.py in the scratchpad, removed after the run). Axioms unchanged.
No rule adopted. Criteria were written before any code ran (criteria_pre_run.txt). One mismatch: pre-set P7 said that
P-covariant dressings at split scales keep theta = 0. That holds for Hermitian dressings (C3). Non-Hermitian products
at split scales give a small nonzero theta (C4: 4e-9 at dressing 0.05 vs 0.04). This is recorded, not tuned away.

Repo first. A git grep of origin/main for Barr-Chang, Babu-Mohapatra, "mirror parity" and "parity solution" found no
note (one unrelated script). This note builds on:
- mirror-world: one flat register reaches both walls;
- copy-sign-nelson-barr: G slot; the SMG vertex phase enters theta-bar;
- wizards/w2-algebra: approach 2, the kappa question;
- the register's strong-CP entry: theta_bar = -arg det(M_u M_d) once theta_gauge = 0.

## A. What P_slab is, and whether the adopted clauses keep it

A1-A2 [T]. On the working slab (layer = extra spatial direction), P_slab = (layer reversal s -> Ls-1-s) x (3D inversion
k -> -k) x beta. It is an EXACT symmetry: the residual is 0. beta commutes with beta and anticommutes with all four alpha
matrices, including the layer hop. In the 4 spatial directions of the slab it is a full inversion, which is a proper
rotation, and that is why it is automatic.

A3-A4 [T]. On fermions, P_slab maps the near Weyl (Gamma = -1) onto the far Weyl (Gamma = +1) with overlap 1 - O(1e-9).
- So it maps the light 16 to the mirror: same gauge charges, opposite hand (the CP conjugate of a left-handed 16bar).
- On gauge fields, it acts on the ONE flat register (mirror-world A1/A3) as ordinary parity: A_0 even, A_i -> -A_i.
  A constant link background is a symmetry only with A -> -A.
- It does NOT exchange two gauge groups. The adopted rules have only one.

A5 [T]. sum E.B goes to -sum E.B (spectral check, exact). A P_slab-symmetric rule set therefore forbids the bare theta.

Which adopted clauses keep P_slab:
- Tick-form slab (chiral-tick-form, Wilson kernel): YES (A2).
- Links clause: YES, as ordinary parity on the single register (A3).
- History-level weighting (overlap + Luscher projector): NO. D is P-covariant, but gamma5_hat -> -gamma5_hat (A6, exact),
  so the selection of left-handed Weyls with no mirror is explicitly P-odd. In that reading there is no mirror to swap.
- Far-wall gapping term (far-wall-smg candidate, Cayley form): NO, explicitly (A7, bilinear proxy). A P_slab-exact rule
  set would put the same vertex on the near wall and gap the light 16 too.
- CL-1 cell slab in the one-copy window: both walls sit in turn copy q = 2 (anomaly-family-count). A unitary P that
  commutes with the turn is consistent with that. The cell slab was NOT rebuilt here; inversion is kept by CL-1's tick
  with the copy mass (register). [S]
- FREEZE odd-layer slab: q_light = 2 but q_mirror = 1. A turn-commuting unitary cannot map one onto the other, so the
  swap there must be antiunitary (CP-like, w -> w^2). [S, algebra only]

## B. Toy with one gauge field (the adopted Links clause)

The light fields are q_L, u_R, d_R. The mirror fields are q'_R, u'_L, d'_L, with the SAME charges. H and H' are both
doublets of OUR SU(2). P_slab forces M(h, h') = sigma M(h', h)^dag sigma, so the mirror block is the P image of the light
block (Y' = Y^dag in psi_L-bar M psi_R form, which is Y* in the all-left-handed convention).

Gauge invariance allows three extra kinds of term:
- cross Yukawas (q_L H' u_R);
- a Hermitian doublet mass q_L-bar B q'_R;
- Hermitian singlet masses C.

Results:
- B2 [F]. det M(h,h') = conj det M(h',h), so it is real only at h = h'. With spontaneous breaking h != h', the median
  |theta_tree| is 0.81. NO cancellation.
- B3 [T]. A supplied Z2 that removes the cross and mixing terms gives theta_tree = 0 exactly. But the mirror masses then
  equal the light masses times v'/v.
- B4 [E]. H' breaks OUR electroweak group, so v^2 + v'^2 = (246 GeV)^2. With perturbative y_t this gives v'/v <= 3.4,
  so m_u' <= 7 MeV, with right-handed-doublet mirror neutrinos: N_nu = 6 vs 2.984 +- 0.008 (377 sigma). EXCLUDED.
- B5 [F]. Making the mirror heavy through B and C pairs mirror WITH light: in 100 samples, no light chiral state is left.
  Under one gauge field the mirror can only be removed by SMG (D) or by pairing it with the light 16 (vector-like).

## C. BCS shape (supplied: separate electroweak registers per wall, shared colour)

With SU(2) x U(1) per wall and SU(3) shared (Barr-Chang-Senjanovic 1991; cf. Babu-Mohapatra 1990, Hall-Harigaya, cited
as supplied), gauge invariance alone forbids every light-mirror bilinear. Then:
- M_u = diag(Y_u h*, Y_u^dag h'), M_d = diag(Y_d h, Y_d^dag h'*);
- C1 [T]: det(M_u M_d) = |det Y_u det Y_d|^2 |h h'|^6 > 0. So theta_tree = 0 (not pi) for every Y and every v, v' and
  VEV phase (max 2.7e-15 over v'/v in [1e2, 1e10]);
- the bare theta is 0 by A5, because colour is the shared, P_slab-even register;
- C2 [F]: the light J is untouched (median |J| 2.7e-2 for O(1) random Yukawas). The CKM phase lives in Y freely.
- C3 [T]: Hermitian dressings keep theta = 0 even with split light and mirror scales.
- C4 [F]: non-Hermitian products at split scales give theta ~ 4e-9 at dressing 0.05 vs 0.04. This sits beyond first order
  and scales with the commutator invariant det[H_u, H_d] (8.8e-5 here). It is the SM-like small leak; the published
  higher-loop estimates are supplied, not rederived.

## D. The adopted SMG mirror (one gauge field)

theta_bar = theta - arg det(Y_u Y_d) - kappa arg(lambda_4).
- D1 [T]. Per 16, the sum of 2T(colour) over Weyls is 4. The charge-4 vertex therefore gives |kappa| = N_f = 3. This
  answers w2's question.
- D2 [T]. The kept Z4 shifts theta by 2 pi N_f, so it is QCD-anomaly-free. theta_bar is continuous in arg lambda_4: it
  is not quantised to pi/2.
- D3 [F]. P_slab maps lambda_4 to a NEAR-wall vertex (which must have zero strength, i.e. spontaneous breaking), never to
  Y. So arg lambda_4 and arg det Y are unrelated, and theta_bar is generically O(1).
- So with an SMG mirror, P_slab removes only the bare theta. The w2 hope ('theta-bar cancels pairwise') FAILS.

## E. Quality and scales [E, supplied numbers]

- E1. (H'^dag H' - H^dag H) G Gdual / Lambda^2 is P-EVEN, so exact P_slab allows it: theta ~ v'^2/Lambda^2, which needs
  v' < 2.4e13 GeV at Lambda = 2.4e18 GeV (lattice-cutoff = Planck, supplied).
- E2. A misaligned dim-6 Yukawa is enhanced by 1/y_u (median ratio 6.2e4), giving v' < ~1e11 GeV.
- E3. Mirror quarks are coloured and stable against mixing, with m_u' = m_u v'/v >~ 1.5 TeV (supplied). That needs
  v' >~ 1e8 GeV, so the window is [1e8, 1e11] GeV. v' is SUPPLIED: no rule fixes it (R2's slab depth could be tried).
- E4. After colour decoupling, the light mirror relics are gamma' + 3 nu': Delta N_eff = 4.14 x^4 with
  x = 0.47-0.63, i.e. Delta N_eff = 0.19-0.64. This is marginal against ~0.3. It is the one prediction this route was not
  built for: Delta N_eff >= ~0.2 if nu' is light, testable at CMB-S4.

## F. What it implies for the rules [S]

- The mirror must be HEAVY through its OWN electroweak breaking (v' >> v), not through SMG.
- That needs a mirror electroweak group distinct from ours. The adopted Links clause (one register per factor, flat
  across layers, Gauss's law) forbids this (mirror-world A3).
- Required new rule (UNTESTED): "factors under which a wall's content is chiral get wall-local registers, while factors
  that are vector-like on each wall span the slab".
  - On a 16, colour is vector-like per wall (2 triplets + 2 antitriplets) and SU(2) x U(1) is chiral, so the rule
    produces the BCS split without naming a group.
  - It must repair Gauss's law (far-half charge leaks at O(1) through bulk modes, mirror-world A2g): bulk modes must
    carry no electroweak charge, or the bulk must confine them (Dvali-Shifman-type, owner decision 5).
- Anomaly: each wall's 16 is anomaly-free under its own electroweak group, and SU(3)^3 and SU(3)^2 U(1) cancel per wall.
  No conflict.
- The chirality wall changes character. There is no symmetric mass generation. The slab becomes vector-like under colour
  only, each wall is chiral under its own electroweak group, and the mirror gets an ordinary Higgs mass.
- The far-wall-smg program would become unnecessary for this route. It also conflicts with it: the SMG term breaks
  P_slab explicitly (A7).
- The history-level Luscher selection must give way to the tick-form slab, since it breaks P_slab (A6).

## Verdict

- Within the adopted rules: FAILS. One register means P_slab maps G to itself, and the mirror is removable only by SMG
  (no cancellation, |kappa| = 3) or by pairing with light matter (vector-like). The Z2 version is excluded by N_nu = 6.
- With a new rule: NEEDS X.
  - X1: wall-local electroweak registers with shared colour, plus the Gauss-law repair.
  - X2: a supplied P-breaking scale v' in [1e8, 1e11] GeV.
  - X3: the explicit breakers removed (Luscher projector, far-wall SMG term).
  - X4: no larger cutoff-scale P-even G Gdual coefficient.
- With X1-X4: theta_tree = 0 exactly with J free, and the leak sits beyond first order.
- Walls move: X1 is a candidate link rule to test next (with R4, the confining bulk).

## Gate (for the X1 candidate)

1. It chooses no measured number. v' is supplied, not fitted, and the window comes from bounds.
2. It names no group: chirality per wall is a property of the content.
3. Prediction: Delta N_eff >= ~0.2 and coloured mirror relics. UNTESTED.
4. It bends the Links clause (not an axiom). A physical bulk that confines bends the Lattice axiom (owner decision 5).

## Smuggling review

- Supplied:
  - the Wilson slab (m, Ls);
  - the BCS gauge split in toy C (this is the X1 content, not derived);
  - random O(1) Yukawas;
  - the quark Yukawas, 246 GeV, y_t perturbativity, N_nu, Lambda = 2.4e18, the 1.5 TeV bound, g* values and the N_eff
    allowance;
  - the literature mechanisms (BCS, Babu-Mohapatra, Hall-Harigaya, Dvali-Shifman, Ellis-Gaillard-type loop smallness).
- Forced:
  - P_slab's exact form and action (A1-A4);
  - theta's P-oddness (A5);
  - the explicit breaking by the Luscher projector and the SMG term (A6-A7);
  - the P relation and its failure at h != h' (B);
  - det > 0 in the BCS shape (C1);
  - |kappa| = N_f and the anomaly-free Z4 (D).
- No measured number was chosen to pass anything.
