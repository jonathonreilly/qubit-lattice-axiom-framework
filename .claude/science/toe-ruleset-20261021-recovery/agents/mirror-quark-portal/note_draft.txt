---
claim_id: mirror_quark_portal_is_a_shared_hypercharge_bare_mass_that_keeps_theta_tree_zero_and_lets_mirror_quarks_decay_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Exact group theory and supplied-model mass-matrix toys for the question: in the face-swap (BCS) shape, can a P_slab-symmetric light-mirror quark portal let mirror quarks decay while keeping theta_tree = 0 and the light J free? Exact: with separate U(1)_Y x U(1)'_Y no product of H, H' neutralises any light-mirror quark bilinear; the invariant I = (Q + triality/3) mod 1 is 1/3 on mirror quarks and 0 on everything else, so with Q, Q' separately exact the lightest mirror-quark hadron is stable whatever fields are added; with ONE shared hypercharge register (SU(2) wall-local, SU(3) and U(1)_Y shared) u'L-bar uR and d'L-bar dR are gauge-invariant bare masses C, qL-bar q'R starts at dim-5 (H H'^dag), u'L-bar dR and d'L-bar uR are forbidden to all orders in H, H'; the mass matrix is block lower-triangular, so det(M_u M_d) > 0 for every Yukawa, every C (Hermitian or not) and every VEV phase (max 1.6e-13); no bi-doublet VEV keeps W_L - W' unmixed and M_W^2 = g^2 v^2/4; the wall-overlap mass is (1-m)^Ls times the inter-wall Wilson line. Finite: light J median 2.1e-2; dim-5 B leak linear in C and v'-independent, theta < 1e-10 needs C <~ 0.04 GeV (worst direction) to 0.9 GeV (median); a condensed bi-doublet leaks 3e-4; tree Z FCNC zero to 5e-16. Estimates (supplied numbers): tau(u') < 1 s needs C >~ 2e-5 to 6e-4 GeV over v' in [1e8, 1e11] GeV, so a window exists; slab-native C = (1-m)^Ls x cutoff needs Ls ~ 46-58 at 1-m = 0.4. Not covered: loop leaks (quoted from literature as supplied), the CL-1 cell slab, a Monte Carlo of the ordered-U(1)/confined-SU(2) bulk, a derivation of C, v' or the share set."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - face_swap_parity_gives_a_tree_level_zero_theta_only_with_wall_local_electroweak_registers_and_shared_colour_bounded_theorem_note_2026-10-24
  - wall_local_electroweak_registers_are_realisable_on_a_confining_layer_bulk_but_chosen_and_leave_stable_fractional_charges_bounded_theorem_note_2026-10-24
runner: scripts/mirror_quark_portal_is_a_shared_hypercharge_bare_mass_that_keeps_theta_tree_zero_and_lets_mirror_quarks_decay_2026_10_24.py
---

# The mirror-quark portal is a shared-hypercharge bare mass: theta_tree stays zero and mirror quarks decay

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=13 FAIL=0, 0.32 s, 61 MB peak, 2.9 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (mirror_quark_portal_test_run.py in the scratchpad, removed after the run).
Axioms and register unchanged; no rule adopted. Criteria were written before any code ran (criteria_pre_run.txt).

Pre-set mismatches (recorded, not tuned away):
- P6 predicted C_max ~ 40 GeV. That was an arithmetic slip (1e-10 x y_u^2 x Lambda = 0.037 GeV). Measured: the
  worst-direction bound is 0.037 GeV and the median bound is 0.89 GeV. P6's "within a factor 3 of the estimate" FAILED
  (ratio 24): the random flavour projection onto the up direction softens the median. The window survives with the
  worst-case bound, so the verdict does not depend on this.
- The first contrast for an unsuppressed B (v'/v = 30, O(1) entries) gave median theta 0.10, below the pre-set 0.3,
  because D ~ 30 suppresses it. It was replaced by the realistic case (hierarchical Yukawas, bi-doublet VEV 1 GeV),
  which gives 3e-4. Both are recorded; the conclusion (B must stay ~0) is unchanged.
- P9 said uR and u'L share charges, so there is no FCNC. True, but the mass-basis right-handed mixing is with u'R (an
  SU(2)' doublet). Its Z coupling equals uR's at leading order because both have T3' + Y = 2/3, and the difference
  enters only through Z-Z' mixing. The null result holds for that reason.
- Two code bugs in the first run (the Z eigenvalue index used in rho and FCNC) were fixed. They were not physics.

Repo first. A git grep of origin/main for "universal seesaw" and "Babu-Mohapatra" found nothing. This note builds on
face-swap-parity (BCS shape, det > 0, v' window [1e8, 1e11] GeV, Delta N_eff) and wall-local-electroweak (confining
bulk; D3: no light-mirror bilinear, stable charge-1/3 hadrons; C1: two maximal shareable sets; A2: ordering thresholds;
D2: Ls <~ 5 tension). Literature cited as supplied: Babu-Mohapatra 1990 (left-right parity with vector-like singlet
quarks); Barr-Chang-Senjanovic 1991; later radiative analyses of the minimal parity solution (Hall-Harigaya and
others), whose loop numbers are not rederived here.

## A. Which portals exist (step 1)

Gauge group: SU(3)_c x SU(2)_L x U(1)_Y x SU(2)' x U(1)'_Y. Light fields: qL, uR, dR. Mirror fields: q'R, u'L, d'L.
Scalars: H and H'.
- A1 [T]. Every left-right cross bilinear carries (Y, Y') off Z/2:
  - qL-bar q'R: (-1/6, 1/6)
  - u'L-bar uR: (2/3, -2/3)
  - u'L-bar dR: (-1/3, -2/3)
  - d'L-bar uR: (2/3, 1/3)
  - d'L-bar dR: (-1/3, 1/3)
  H and H' products carry Y, Y' in Z/2, so no dressing at any dimension neutralises these. This reproduces wall-local
  D3.
- A3 [T]. Stronger: I = (Q + triality/3) mod 1 is additive and exactly conserved. It is 0 on every light field and on
  mirror leptons, and 1/3 on mirror quarks, when Q = T3 + Y and Q' = T3' + Y' are separately exact. Final states built
  from known fields have I = 0. So the lightest I != 0 state is absolutely stable whatever portal field is added
  (a bi-doublet with no VEV, a coloured mediator, anything), unless that field brings a lighter fractional charge,
  which is then stable itself.
  - Hence: mirror-quark decay REQUIRES that Y - Y' is broken or absent.
  - Only Q + Q' (the P_slab-symmetric combination) may stay exact. On it, I = 0 for all fields.
- Two equivalent ways to get there:
  - (i) a singlet s with charges (q, -q) that condenses. The minimal choice is q = 1/3: d'L-bar dR s is renormalizable
    and u'L-bar uR s^2 is dim-5. Its VEV w breaks Y x Y' to the diagonal.
  - (ii) at w ~ cutoff, its low-energy limit: ONE shared hypercharge register.
- A2 [T]. With shared Y (SU(2) per wall, SU(3) and U(1)_Y shared):
  - u'L-bar uR and d'L-bar dR are neutral singlets, i.e. bare masses C (dimension 3), the analogue of eR/e'L for
    leptons;
  - qL-bar q'R is a (2,2) with Y = 0 and needs H H'^dag (dim-5): B ~ c v v'/Lambda;
  - u'L-bar dR and d'L-bar uR carry Y = -1/+1, but an SU(2) x SU(2)' singlet built from one doublet each has Y = 0, so
    they are forbidden to all orders in H, H'.
  - The renormalizable mass matrix is block lower-triangular, M = [[A, 0], [C, D]], with A = Y h* and D = Y^dag h'
    (the face-swap P relation). This is the Babu-Mohapatra structure: q'R plays SU(2)_R doublet, and (u'L, uR) are the
    vector-like singlet pair.
- [S] Is it already in our construction? Yes, as a structure. P_slab maps the near zero mode of each 5D field onto the
  far zero mode with the same charges (face-swap A3-A4). So the slab's wall-overlap (residual) mass pairs uR (near) with
  u'L (far) and qL with q'R, for every component.
  - E1 [T]: on the layer chain this overlap is exactly (1-m)^Ls times the inverse inter-wall Wilson line. The C entry
    is m_res <Phi_Y^k>, where k = 6|Y| is the hop power at elementary charge 1/6. The B entry is m_res <Phi_2 Phi_Y>.
  - The bi-doublet-like composite is therefore present: it is the SU(2) inter-wall Wilson line.
  - E2 [F]: X1 as stated (all EW inter-wall links disordered) gives <Phi_Y> = <Phi_2> = 0, so C = B = 0. That is
    exactly wall-local D3's stable fractional charges.
  - An ordered U(1) link (the adopted Links clause's flat register for that factor) with a disordered SU(2) link gives
    C != 0 and B = 0.
  - What must be SUPPLIED: the share set {SU(3), U(1)_Y} (U(1) Coulomb in the bulk, SU(2) confining). This is a THIRD
    choice beyond wall-local C1's {SU3} and {SU2}. It is not vector-like per wall, but it is anomaly-free per wall
    (each 16 is anomaly-free under its own SU(2) with the shared U(1) and SU(3); 4 doublets per SU(2)).

## B. theta_tree and J (step 2)

- B1 [T]. det M = det A det D for block-triangular M, independent of C. So det(M_u M_d) =
  |det Y_u det Y_d|^2 |h h'|^6 > 0 for every Y, every C (Hermitian as P_slab gives, OR generic, e.g. a spontaneous
  P phase in w) and every VEV phase. Max |theta_tree| = 1.6e-13 over 300 samples, v'/v in [1e1, 1e4]. The bare theta
  stays 0, since colour is the shared P-even register (face-swap A5).
- B3 [F]. The light J is free: median |J| = 2.1e-2 for O(1) random Yukawas. Light masses equal the singular values of
  Y times v to 8e-10 when C << y v'.
- C1 [F]. The dim-5 B leak is theta = arg det(1 - D^-1 C A^-1 B), about |c| C/(y_u^2 Lambda) in the worst direction.
  - It is linear in C and v'-independent: medians 1.5e-10 (C = 1 GeV), 1.1e-9 (C = 10 GeV), and 1.5e-9 at v' = 1e11.
  - theta < 1e-10 needs C <~ 0.04 GeV (worst direction) to 0.9 GeV (median), for |c| = 1 and Lambda = 2.4e18
    (supplied). In the slab, c is likely further suppressed by m_res (not computed).
- C1b [F]. A condensed bi-doublet (B = 1 GeV, i.e. an ordered SU(2) inter-wall link) leaks a median theta of 3e-4.
  It is excluded, so the SU(2) link must stay disordered.
- Loops [supplied]: the literature reports the minimal parity model's radiative theta as finite and small (leading at
  two loops). That is not rederived here, and face-swap C4's commutator-type leak still applies.

## C. Lifetime (step 3) [E, supplied numbers]

- The lightest mirror quark is u', with m_u' = m_u v'/v = 880 GeV at v' = 1e8 GeV.
- It mixes with uR at angle theta_R ~ C/(y_u v'), which gives couplings ~ C/v' to u h, u Z_L and d W_L (Goldstone
  equivalence). So Gamma ~ (C/v')^2 m_u'/(16 pi), and tau < 1 s needs C >~ 2e-5 GeV (v' = 1e8), 6e-5 (1e9),
  2e-4 (1e10), 6e-4 (1e11).
- C2: the window [C_min, C_max] is non-empty at every v' in face-swap's window, even with the worst-case
  C_max = 0.04 GeV. The window is about three decades wide.
- Mirror leptons decay the same way, through the bare eR/e'L mass. Leptons do not enter theta, so that mass is
  unconstrained here.
- Consequences:
  - no stable fractional charge (I = 0 for all fields);
  - no mirror-electron overclosure;
  - the supplied low T_RH of wall-local D4 is no longer needed.
  - There is ONE photon, so face-swap's gamma' share of Delta N_eff disappears. The rest of Delta N_eff (the singlet
    neutrinos) was not computed.

## D. Electroweak breaking and FCNC (step 4)

- D1 [T]. With no bi-doublet VEV, the W_L - W' mass matrix is exactly diagonal and M_W^2 = g^2 v^2/4. There is one
  massless photon, and rho - 1 = 1.0e-5 and 1.0e-7 at v'/v = 1e2 and 1e3 (it scales as (v/v')^2; at v' >= 1e8 GeV it
  is <~ 1e-11). H' is an SU(2)_L singlet, so it does NOT break our SU(2). The face-swap B4 problem does not return.
  - A bi-doublet VEV of 0.3 v gives W_L - W' mixing 0.04: the problem DOES return if the SU(2) link orders.
- D2 [F]. Tree-level Z FCNC among light quarks is 4.5e-16 (numerical zero) at v'/v = 1e4:
  - uR and u'L share all charges;
  - the u'R admixture has the same leading Z coupling (T3' + Y = Q);
  - the residual comes through Z-Z' mixing times theta_R^2.
- [E] Z' (SU(2)') flavour changing is ~ theta_Ri theta_Rj / v'^2. At v' = 1e8 and C = 0.9 GeV it is <~ 1e-26 GeV^-2,
  far below the supplied K-Kbar bound (~1e-16 GeV^-2). The W_R - W_L box bound (few TeV) is irrelevant at v' >= 1e8.

## E. Slab-native size of C [E]

- E3. If C is the bare overlap (1-m)^Ls x cutoff with 1-m = 0.4, landing in the window needs Ls ~ 46-58.
  - That collides with wall-local D2: flat colour needs Ls <~ 5 for a 5D bulk value ~3 (supplied).
  - At Ls = 5, C ~ 1e16 GeV, which puts the light quarks in the universal-seesaw regime m ~ y^2 v v'/C. The top then
    needs v' ~ C, outside the v' window: EXCLUDED.
- So either 1-m <~ 4e-4 at Ls = 5, or C is suppressed further by <Phi_Y^k> (u^k with k = 4 for u, 2 for d), or Ls is
  large. Each of these is SUPPLIED, and C is not derived.

## Verdict

FIXES, with supplied ingredients.
- A P_slab-symmetric light-mirror quark portal exists, and the ONLY kind that lets mirror quarks decay is one that
  removes Y - Y' as an exact charge (A3).
- Sharing the hypercharge register (or condensing a (q, -q) singlet) gives:
  - a renormalizable portal C (the existing wall-overlap mass dressed by an ordered U(1) Wilson line);
  - a block-triangular mass matrix: theta_tree = 0 exactly, for every C;
  - J free;
  - tau(u') < 1 s for C >~ 1e-4 GeV;
  - no EW-breaking problem and no tree FCNC.
- The theory becomes the Babu-Mohapatra left-right parity model with the mirror as the vector-like and SU(2)_R
  partners.
- Supplied:
  - Y1: the share set {SU(3), U(1)_Y}, i.e. per-factor bulk strengths with U(1) Coulomb and SU(2) confining. This is
    a third option alongside wall-local C1's two maxima, still a CHOICE, and a smuggling risk until a share rule is
    derived;
  - Y2: C in [~1e-4, ~0.04-0.9] GeV (the slab-native size needs Ls ~ 50 or a small 1-m, in tension with flat colour);
  - Y3: v' (as before);
  - Y4: no large dim-5 B coefficient beyond |c| ~ 1.
- FAILS if X1 is kept exactly as stated (all EW factors wall-local). Then no portal of any kind can remove the stable
  charge-1/3 hadrons (A3, exact).
- Simplification gained: only SU(2) needs a confining bulk. U(1) keeps the adopted flat register, and the low T_RH is
  no longer needed.
- Walls move. Next steps:
  - Monte Carlo of a bulk with U(1) ordered and SU(2) disordered;
  - a share rule that picks {SU3, U1} (for example "non-abelian factors under which the wall is chiral are
    wall-local"; untested and post hoc);
  - derive C from m_res <Phi_Y^k>.

## Gate (for "share U(1)_Y, keep SU(2) wall-local")

1. Measured numbers: none chosen to pass. C and v' are supplied windows set by bounds (FITTED-type).
2. Named structure: the share set is picked so that it works, which is a smuggling RISK. A principled rule is not yet
   derived.
3. Predictions it was not built for:
   - vector-like mirror quarks with mass ratios equal to the SM ratios (m_q' = m_q v'/v);
   - one photon (no gamma' in N_eff);
   - no fractional charges.
   All UNTESTED (out of reach at v' >= 1e8).
4. Bends: the Links clause (per-factor bulk strength, as in wall-local) and the Lattice axiom (physical layers, owner
   decision 5).

## Smuggling review

- Supplied:
  - the BCS/LR field content and the share set;
  - C, v', Lambda = 2.4e18, |c| <= 1;
  - PDG quark masses (no running), 246 GeV, g and g1 toy values;
  - the 1 s BBN bound and the K-Kbar bound;
  - 1-m = 0.4 and the Ls tension numbers;
  - literature loop results.
- Forced:
  - the A1/A2 operator enumeration;
  - the stability invariant (A3);
  - block-triangular det > 0 (B1);
  - W_L - W' non-mixing without a bi-doublet (D1);
  - the overlap = Wilson-line identity (E1).
- No measured number was chosen to pass anything.
