---
claim_id: emergent_internal_symmetry_protects_nothing_the_lattice_group_does_not_gauge_flow_kills_8_of_11_cone_couplings_only_logarithmically_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "One-loop flow, exact commutants and finite group-theory checks. (P) The 13 cubic-covariant k-linear cone
  couplings on the half-link 5 = E + T1 (times spin), coupled to one flavour-blind U(1) gauge field with a Lorentz cone:
  10 are irrelevant with the common rate -8/3 (alpha/2 pi), 3 are exactly marginal, and none is relevant. Of the 11
  that break colour/weak, 8 flow to zero and 3 are redundant spin-flavour frame rotations; the latter are the same
  physics as relevant on-site spin-flavour terms, which break the group to U(1). With time reversal the numbers are
  9 couplings, 6 irrelevant breaking, 1 redundant. The irrelevant ones shrink only by a power of a coupling ratio
  (at most ~2e-2 for an IR-free U(1)). (C) For the CL-1 tick (flat edges, mu = 0, no copy mass) the light content is
  2 Dirac copies. The exact lattice group (O_h, the (1,1,1) glide x sublattice sign, T, PH) allows only the universal
  cone at dimension <= 4, so U(2)_L x U(2)_R is robustly emergent. Without T or the glide it is not. With the copy
  mass on one tiling, a Dirac mass of each copy is allowed. (S) An emergent Spin(10) of free Weyl modes is always
  part of an emergent U(16). Spin(10) is the largest anomaly-free mass-forbidding group on 16 among the subgroups
  checked, but the same selector at 32 picks SU(2) x SO(16). Supplied model, finite diagnostic, no physical
  identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/emergent_internal_symmetry_cone_rg_cl1_taste_and_spin10_selection_2026_10_22.py
---

# Emergent internal symmetry: the lattice group protects; flow only cleans up, logarithmically

Runner: runner.py (24 PASS / 0 FAIL, 14.6 s, about 110 MB peak). Tested through scripts/runner_cache.execute_runner
under a unique filename (status ok, stdout 3847 characters). Seeded with 20261022.

Inputs:
- spin10-breaking: E5, and "covariance never protects a non-abelian frame of one-mode sites".
- why-five-modes: N = 5 given a full Spin(2N).
- time-complex-structure: S5, the 11 tuned cone couplings. This is the coordinator's priority question.
- Register CL-1 text: bands, copy mass, copy sign s.
- Open PRs #9884 ("the block tick has no exact copy SU(2), only a sublattice axial remnant") and #10016 ("the cube's
  tastes are two doublets, and no symmetry protects a family"). Both are consistent with C below: C refines them at
  the level of operator dimension and does not contradict them.
- No note on main treats emergent symmetry as a protection mechanism. The search was git grep for "emergent symmetr",
  "taste symmetry" and "emanant", plus open PRs.

## Organising principle (rederived, standard)

At a free (Gaussian) fixed point of n Weyl modes, the kinetic term has U(n) symmetry.
- Pauli-Gursey pairings are included. Number-conserving symmetries alone give a product of unitary groups.
- An internal group G is emergent in the infrared only if every relevant operator (dimension 3: masses, node
  shifts) and every marginal operator (dimension 4: k-linear cone matrices, gauge couplings) that breaks G is either:
  - forbidden by the exact lattice group Gamma, or
  - driven to zero by the flow.
- Irrelevant breaking (dimension >= 5) is suppressed by (E/Lambda)^(d-4) and is harmless.

So the robust emergent algebra is the commutant of all Gamma-allowed operators of dimension <= 4, adjusted for any
marginal operator the flow kills. Sections C and P compute these two pieces.

## P. The 11 colour/weak cone couplings under gauge flow (priority)

Setting:
- 5 flavours (E + T1) times spin, with the 24 cubic rotations acting through SU(2) lifts. This is the
  time-complex-structure construction, rebuilt.
- The cone is H(k) = sum_b k_b V_b.
- One U(1) gauge field couples minimally to all 5 with unit charge. This is U(1)_X, the one-body mode number. The
  photon cone is held Lorentz.
- The flow is the one-loop log-divergent self-energy, computed on an S^3 quadrature: dV_b/dl = (alpha/2pi) B_b[V],
  where l = ln(Lambda/mu). Ward identities fix the vertex as dK/dp.

Results:
- P1 (exact). The cubic-covariant cone space is 13-dimensional. 2 of its directions are colour/weak-blind and 11
  break colour/weak, as found in time-complex-structure S5.
- P2 (sanity). A single Weyl fermion with speed c flows to c = 1. The rates are +0.884 at c = 0.6 and -1.207 at
  c = 1.4, identical in the gauges xi = 0, 1, 3. This is Nielsen-Chadha emergent Lorentz invariance, and it validates
  the signs and the gauge independence.
- P3, P4 (theorem-grade numerics). The linearised flow at the blind cone V* = sigma x 1 has:
  - eigenvalue -8/3 ten times (irrelevant), and 0 three times;
  - no relevant direction.
  - The blind speeds c_E and c_T are in the -8/3 space, so both flow to the photon cone.
  - The 3 zero modes are exactly the redundant directions i[S, V*]. Here S runs over the 5-dimensional space of
    cubic-invariant on-site Hermitians on (E+T1) x spin; the 2 spin-blind ones give 0. They are field redefinitions
    psi -> exp(iS) psi that rotate spin into flavour. They are exactly marginal under any flavour-blind dynamics,
    because the gauge sector cannot see a field redefinition.
- P5. So the answer to the coordinator's question is: 8 of the 11 flow to zero (irrelevant), 3 are exactly marginal
  (redundant), and 0 are relevant.
- P6 (nonlinear). Starting from a generic covariant cone at 35% deformation, the band-speed spread falls
  0.114 -> 0.007 -> 4e-4 -> 2e-5 over flow time (alpha/2pi) l = 3. Every species ends on the photon cone, 5-fold
  degenerate.
- P7. With time reversal (1 x i sigma_y) K:
  - there are 9 cone couplings: 2 blind and 7 breaking;
  - of the 7 breaking ones, 6 are irrelevant and 1 is redundant;
  - there are 4 covariant on-site terms: 2 blind and 2 spin-flavour.
- P8, P9 (the catch).
  - A redundant cone direction is removable only by rotating the on-site term. exp(iS) maps the blind 2+3 on-site
    term into the spin-flavour on-site terms (checked: i[S, M0] lies in the covariant on-site space and is nonzero).
  - So "marginal misalignment" and "relevant spin-flavour on-site term" are one coupling seen in two frames.
  - Any generic covariant on-site term, with or without time reversal, leaves internal commutant 1, even with the blind
    cone (13 -> 1). It is relevant (dimension 3), so no flow removes it.
- P10 (rate).
  - The irrelevant directions decay as delta proportional to alpha^p, with p = (8/3)(1/2pi)/b.
  - For an IR-free U(1), b = N_W/(3 pi), which gives p = 4/N_W.
  - Even from alpha_UV = 1 down to 1/137, delta_IR/delta_UV is at least 0.02 (N_W = 5), 0.29 (N_W = 16) or 0.66
    (N_W = 48).
  - At fixed alpha = 1/137 over 44 e-folds (cell to GeV), the factor is 0.87.
  - Measured colour exactness and species-dependent cone bounds (<~1e-15 or tighter; Kostelecky-Russell tables,
    cited) need about 15 more orders.
  - This is the known Collins-Perez-Sudarsky-Urrutia-Vucetich fine-tuning problem (cited), now computed for this
    multiplet.

Verdict on the priority question: the 11 couplings are not truly relevant, and most are irrelevant under gauge flow.
But:
(a) the restoration is logarithmic, a fixed small power of a coupling ratio, so it misses measurement by >~13 orders
    unless the cell starts within ~1e-13 of blind. That is tuning.
(b) 3 of the 11 (1 with time reversal) are exactly marginal, and they are equivalent to relevant on-site terms that the
    flow cannot touch.
So the SM group on the half-link 5 is NOT emergent without tuning under U(1)_X-type dynamics.

What could change this (UNTESTED):
- a strongly coupled infrared sector, where the exponent is O(1) per e-fold rather than O(alpha). The only candidate
  is the colour sector itself, which is circular;
- a lattice symmetry that maps the 3 spin-flavour on-site terms to minus themselves. P7 shows time reversal removes
  only one of them.

## C. CL-1's emergent taste/copy symmetry

- C1. At mu = 0, flat edges and no copy mass, the tick has one node at k = 0.
  - It has 8 components and an isotropic Clifford cone with v = 2 sin(eps)/sqrt3 per site momentum, which equals
    sin(eps)/sqrt3 per block, matching the register.
  - Its chirality is 4/4, which means 2 Dirac copies, i.e. 2 L + 2 R Weyl.
  - The zone-corner partner sits at quasi-energy 2 eps (gapped).
- C2 (exact). The tick's lattice group contains:
  - all 48 O_h elements about the even-cube centre, with gauge phases;
  - the (1,1,1) glide times the sublattice sign. Its intertwiner is eps_x V(k)^dag T, with
    V = e^{-i eps R_o/2} e^{i eps R_e/2}, and it is exact on the Floquet step.
- C2b. At leading order the tick is eps(R_e - R_o), which is gauge-equivalent to the Kogut-Susskind Hamiltonian (pi
  flux), so single-site shifts are exact there. The full tick breaks them at relative order eps^2 (3.9e-3 -> 1.6e-2
  when eps doubles).
- C3. The free cone has number-conserving commutant u(2)+u(2) and 4 complex Pauli-Gursey pairings, so the free
  fixed-point group is U(4) on 4 Weyl.
- C4 (exact). Robust commutant, meaning the commutant of every Gamma-allowed operator of dimension <= 4:

  | Lattice group | Commutant |
  |---|---|
  | O_h | 1 |
  | + glide | 2 |
  | + T | 8 |
  | + PH | 8 |

  So U(2)_L x U(2)_R of the two copies is robustly emergent iff the glide x sublattice and time reversal are exact.
  Then the only allowed dimension-<=4 terms are the universal cone (plus the chemical potential before PH). The
  breaking starts at dimension >= 5: the symmetric-frame k^2 terms of the tick already break it (commutant -> 1 at
  finite k).
  - This is the staggered-taste mechanism, but carried by the glide and T, not by single-site shifts, which CL-1
    breaks.
- C5. The copy mass s = i R1 R2 R3 R satisfies s^2 = 1, commutes with the cone and is odd under C4, so it is exactly
  the relevant operator that breaks the copy U(2).
  - Its own symmetry group is T_h, T.C4 and PH.C4. Under that group, without the glide, there are 2 relevant terms,
    and they include a Dirac mass for EACH copy. So the light copy's masslessness is not protected once the copy mass
    sits on one tiling (as the polar split puts it).
  - With the glide, the commutant is U(1)^4.
  - This rederives the register's "additive-mass and chirality problems are one" in operator-dimension form.
- C6. The free tick's spectrum is 4-fold degenerate at every k. This is a spectral, not an algebraic, copy degeneracy,
  consistent with PR #9884.

## S. Can the emergent group be Spin(10) or SU(5) on 16 Weyl modes?

- S1 (Burnside, exact). so(10) on the 16 generates all of gl(16).
  - So any free fixed point with an emergent Spin(10) on an irreducible 16 has emergent U(16).
  - SU(5) on 10 + 5b + 1 likewise implies U(10) x U(5) x U(1).
  - So at a free fixed point emergence never stops at Spin(10). The GUT structure can enter only through marginal
    interactions, i.e. gauge fields or Yukawas, which are the sibling emergent-gauge-composite lane.
- S2 (exact). A number-conserving lattice is vector-like (Nielsen-Ninomiya), so U(1)_N acts as Theta: +1 on (4,2,1)
  and -1 on (4b,1,2).
  - Theta is not in so(10), and its commutant there is Pati-Salam (21).
  - So the Spin(10) generators outside PS are Pauli-Gursey (number-violating). They can only be emergent, and an exact
    on-site SU(2)_L is excluded by Nielsen-Ninomiya per charge sector.
- S3. The selector is "the largest subgroup of the emergent U(16) that is anomaly-free (cubic, Witten) and forbids
  every Majorana mass (no symmetric invariant)". Results:
  - SO(16): fails, because it is real.
  - Sp(16): fails on the Witten anomaly. Its minimal SU(2) acts as one doublet; this index is coded in the runner,
    not computed there.
  - SU(2) x SU(8), SU(4) x SU(4) and S(U8 x U8): fail on the cubic anomaly.
  - Spin(10) (45): passes.
  - Principal SU(2) with j = 15/2 (3): passes. The old Witten index is even; the new SU(2) anomaly is cited (WWW).
  - SU(2) x SO(8) (31): passes.
  So, on the checked list, the largest is Spin(10). This is not a full subgroup classification.
- S3b. The same selector at 32 Weyl modes picks the pseudoreal SU(2) x SO(16) (123) over Spin(12) (66), so it is not
  a GUT selector in general. It gives Spin(10) only at exactly 16.
- S4. CL-type cells give 4 b^3 Weyl modes (zoom b, one node) or 8 b^3 (partner light), never 16. Reaching 16 needs a
  supplied factor 4 (flavours or nodes).

## R4: is emergent ("accidental") protection admissible?

Theorem-level statement:
- A relevant operator allowed by Gamma is generated with an O(1) coefficient at the cell scale by generic
  Gamma-invariant dynamics, so an emergent symmetry can never be what keeps something light.
- R4's "light only if protected" must therefore be read with Gamma, the exact lattice group: emergent symmetries
  protect nothing that Gamma does not.

An emergent G is still admissible as STRUCTURE of the light sector when:
- every G-breaking operator of dimension <= 4 is Gamma-forbidden (C4 shows this for CL-1 copies with glide and T); or
- every such operator is irrelevant under the flow. P shows "irrelevant under flow" is only logarithmic here, so it
  fails measurement unless the starting point is tuned.

Admissible pattern: Gamma forbids all relevant AND marginal breaking, and dimension-5/6 breaking is suppressed by
(E/Lambda)^(1-2), which is ~1e-17 to 1e-34 at TeV/Planck. Inadmissible: marginal breaking left to log flow.

## Against measurement

- Exact colour SU(3) and species-universal cones (bounds ~1e-15 or tighter, cited) exclude the half-link 5 with
  generic covariant couplings even after gauge flow (P10). They also exclude the redundant/relevant spin-flavour
  terms outright (P9).
- The electron's lightness (mass ~4e-22 in cell units) is not protected in CL-1 with the polar copy mass (C5). This
  agrees with the register.

## Gate (anti-smuggling)

Candidate rule ES: "internal symmetries of the light sector are the emergent symmetry of the infrared fixed point:
the commutant of all lattice-allowed operators of dimension <= 4, after gauge flow".
1. Numbers chosen: none. PASS.
2. No observed structure is named. PASS.
3. Predictions not built for:
   - CL-1 copies have exact-to-dimension-5 U(2)_L x U(2)_R iff the glide and T are exact;
   - the half-link 5 flows to U(1)_X x (free U(5) broken only by relevant spin-flavour terms);
   - the largest anomaly-free protected subgroup of U(16) is Spin(10), and that of U(32) is SU(2) x SO(16).
   None is tested against data here, beyond the failures listed.
4. Axiom bent: none. It is a reading rule for CL-1.

Result:
- As a reading rule it is ADOPTABLE.
- As a route to the SM it FAILS: it gives U(1)_X on the half-link 5 (measured exact SU(3) x SU(2) contradicts this
  unless tuned), and U(2) x U(2) or U(1)^4 copy groups on CL-1.
- The selector form "largest anomaly-free protected subgroup" FAILS gate clause 3 in substance, because it gives
  Spin(10) only at an input count of 16 that no cell supplies. It also needs a rule that some subgroup is gauged,
  which is the emergent-gauge lane.

## Smuggling review

- Supplied:
  - the (E+T1) x spin multiplet and the SU(2) lifts (from time-complex-structure);
  - one flavour-blind U(1) with a Lorentz photon cone held fixed (the photon's own flow is ignored; one-loop only);
  - Feynman-type gauges, with gauge independence checked;
  - the k-linear truncation;
  - CL-1 at mu = 0 on flat edges;
  - the static-frame representation of the glide for operators of dimension <= 4 (exact at the node, since
    H_F(0) = 0; at dimension >= 5 the Floquet frame matters);
  - the choice of maximal subgroups and the coded Sp(16) Witten index.
- Forced (exact or numerically exact): P1, P3-P5, P7-P9; C1-C5; S1, S2, S3 within the checked list; S4.
- Cited, not rederived: Nielsen-Chadha emergent Lorentz invariance (P2 reproduces the sign); the QED beta coefficient;
  Collins et al. 2004; Kostelecky-Russell bounds; Witten and Wang-Wen-Witten SU(2) anomalies; Nielsen-Ninomiya;
  Burnside's theorem.
- Not done: an interacting fixed point, a non-abelian gauge flow, a two-loop flow, and the photon cone's own flow.
