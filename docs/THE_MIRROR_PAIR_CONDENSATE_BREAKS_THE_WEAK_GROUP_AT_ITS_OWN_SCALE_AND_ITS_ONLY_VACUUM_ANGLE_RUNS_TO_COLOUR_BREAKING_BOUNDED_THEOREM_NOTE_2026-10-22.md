---
claim_id: the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the candidate laws' mirror family (one mirror 16 per family under the Spin(10) pair square, the SM group embedded in Spin(10)) and the supplied one-quartic SU(4) toy: (A) the toy quartic c1c2c3c4 is exactly the vector-channel pair square of a Spin(6) spinor, and the Spin(10) pair square is the Spin(10) member of the same family. The toy's SU(4) -> Sp(4) is SO(6) -> SO(5), and the Spin(10) analogue is SO(10) -> SO(9) with vacuum manifold S^9 (9 Goldstones). The spinless toy pair (antisymmetric) corresponds to the spin-singlet Weyl pair (symmetric). (B) The 10's colour-singlet part is a B-L = 0, Y = +-1/2 bidoublet, so a mirror pair condensate there breaks SU(2)_L x U(1)_Y and keeps the Z4 of B-L. No weight of the 45 is a colour-singlet doublet, so a Spin(10)-symmetric mirror sector has no pseudo-Goldstone doublet in any channel. In u(16N) every colour-singlet doublet generator has |B-L| = 2; B-L-neutral ones mix light with mirror. (C) On S^9 the W-mass sum is sin^2(theta)/2 and the colour-breaking sum is (4/3) cos^2(theta) exactly, so the only vacuum angle runs from EW breaking to colour breaking: unbroken colour forces v = f. The gauge-loop potential is exactly linear in sin^2(theta). (D) An SU(4)/Sp(4) coset on SM-charged modes with a neutral EW-safe end and a Y = 1/2 pseudo-Goldstone needs the content (2)_0 + (1)_+1/2 + (1)_-1/2, which is in no 16; with spin-1/2 modes it needs a further two-valued antisymmetric index (8 Weyl modes per cell). Every embedding of the toy SU(4) in the mirror 16 has its EW-safe end breaking colour or charge. The estimates against measurement (a condensed mirror is excluded by gg -> h, S and LEP; the new-content candidate needs xi <= 0.05) are separate. The unification of the chirality and weak-scale walls through the mirror condensate is not established; it is excluded in the stated content."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - transmutation_removes_the_weak_scale_tuning_but_only_colour_binds_a_doublet_pair_and_no_rule_vacuum_has_a_misalignment_angle_bounded_theorem_note_2026-10-22
  - the_cube_filtered_quartic_toy_is_sign_free_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
runner: scripts/the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_2026_10_22.py
---

# The mirror pair condensate breaks the weak group at its own scale, and its only vacuum angle runs to colour breaking

Claim type: bounded_theorem.
Primary runner: `scripts/the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Two of its walls look like one:

- Chirality. The mirror family must be gapped by the cube-filtered pair square, a four-fermion term rather than a gauge binder. In the [toy QMC note](THE_CUBE_FILTERED_QUARTIC_TOY_IS_SIGN_FREE_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md) the one-quartic SU(4) toy forms a charge-2 pair condensate at strong coupling, breaking SU(4) to an Sp(4)-type subgroup, not a symmetric gap.
- Weak scale. The [weak-scale note](TRANSMUTATION_REMOVES_THE_WEAK_SCALE_TUNING_BUT_ONLY_COLOUR_BINDS_A_DOUBLET_PAIR_AND_NO_RULE_VACUUM_HAS_A_MISALIGNMENT_ANGLE_BOUNDED_THEOREM_NOTE_2026-10-22.md) finds that no gauge binder in the content condenses a Y = 1/2 doublet pair. It also finds that a narrow 125 GeV scalar needs an SU(4)/Sp(4)-type coset with a misalignment angle, v = f sin theta.

The quartic is the kind of non-gauge binder the weak-scale note says is missing. This note tests whether the mirror's pair condensate is the electroweak breaker, with heavy mirrors at f and a light pseudo-Goldstone doublet at v. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Statement

A. The toy and Spin(10) are one family.

1. Exact. Take a chiral spinor of Spin(2k) and its vector-channel pairing psi^T C Gamma_a psi. For k = 3 (4 x 4 -> 6) the pairing is antisymmetric. For k = 5 (16 x 16 -> 10) it is symmetric. For k = 3, sum_a M_a(ij) M_a(kl) = lambda eps_ijkl, so the toy quartic is c1c2c3c4 = (1/(24 lambda)) sum_a (c M_a c)^2. The toy's quartic is therefore the Spin(6) pair square, and the register's Spin(10) pair square is the Spin(10) member of the same construction. The toy's spinless pair is antisymmetric. The Spin(10) Weyl pair is a Lorentz scalar, symmetric internally, and the Lorentz eps supplies the antisymmetry. So the spinless toy corresponds to the spin-singlet channel.
2. Exact. The toy's breaking SU(4) -> Sp(4) is SO(6) -> SO(5), with a real 6-vector condensate whose phase is locked by the charge-4 term. The vacuum manifold is S^5, with 5 Goldstones. The Spin(10) analogue is SO(10) -> SO(9), with vacuum S^9 and 9 Goldstones.

B. Charges.

1. Exact. The 10 = (1,2,2) + (6,1,1). Its colour-singlet part is a Y = +-1/2 bidoublet with B-L = 0, which is one real (2,2), i.e. one complex Higgs-type doublet. The (6,1,1) carries B-L = -+2/3 and Y = -+1/3. A mirror pair condensate in the (1,2,2) therefore does carry SU(2)_L x U(1)_Y. It breaks SU(2)_L x SU(2)_R to the diagonal (custodial) subgroup and keeps the Z4 of B-L. This answers question (i): yes.
2. Exact. A colour singlet has zero colour weight. No weight of the 45 has zero colour weight and T3L = +-1/2. So the adjoint of Spin(10), and of Spin(10) times any family group, holds no colour-singlet doublet. Whatever the condensate channel (10, 120, 126 or any mixture), a Spin(10)-symmetric mirror sector has no pseudo-Goldstone Higgs doublet.
3. Exact. In u(16N), the symmetry algebra of N free Weyl 16s, the colour-zero doublet generators all have B-L = +-2 (Y = +-1/2 or +-3/2). B-L-neutral doublet generators appear only in 16 x 16, that is, in generators rotating the light family into the mirror. A mirror-only quartic breaks those generators at order g. A B-L-neutral pseudo-Goldstone doublet from mirror-only dynamics therefore needs either a vacuum of |B-L| = 2 (breaking the Z4 of B-L) or light-mirror mixing.

C. The pair-square vacuum and its angle.

1. Exact. On the 10 the colour Casimir is 4/3 and the SU(2)_L Casimir is 3/4. Y^2 is 1/4 on the (1,2,2) and 1/9 on the (6,1,1). The commutant of colour in so(10) has dimension 7, namely SU(2)_L x SU(2)_R x U(1)_B-L. So no SU(4) acting on mirror modes commutes with colour.
2. Exact. S^9 has 9 Goldstones at every point. At the (1,2,2) end colour is unbroken, SU(2)_L x U(1)_Y -> U(1)_em with 3 eaten modes, and 6 real colour-triplet directions remain. No point of S^9 is fixed by the SM group.
3. Exact. Write n = cos(theta) t + sin(theta) h with unit t in the (6,1,1) and unit h in the (1,2,2). Then sum_(a=1,2) |T_a n|^2 = sin^2(theta)/2, so v = f sin(theta), and sum_A |T_A n|^2 over colour = (4/3) cos^2(theta). The only misalignment angle on S^9 runs from EW breaking to colour breaking. Unbroken colour forces theta = pi/2 exactly, so v = f. This answers question (ii): no.
4. Exact, then estimate. The gauge-loop potential, a positive coefficient times sum_G g_G^2 sum_A |T_A n|^2, equals A_t + (A_h - A_t) sin^2(theta) exactly, with A_h = (3/4) g2^2 + (1/4) g'^2 and A_t = (4/3) g3^2 + (1/9) g'^2. Being linear in sin^2(theta), it has no interior minimum. With unified couplings (0.900 < 1.400), at m_Z (0.351 < 1.990) and at 1 TeV (0.340 < 1.513) it picks the (1,2,2) end: the vacuum alignment drives the mirror condensate to break the weak group at its own scale.

D. The toy's coset on SM-charged modes.

1. Exact (weak-scale C3 rederived on the toy coset). Take 4 = (2)_0 + (1)_+1/2 + (1)_-1/2. The Sp(4) stabiliser has dimension 10, so there are 5 Goldstones: one Y = 1/2 doublet and one singlet. The theta = 0 end keeps SU(2)_L x U(1)_Y, Q is kept at every theta, and m_W^2(theta)/m_W^2(pi/2) = sin^2(theta).
2. Exact. Take 4 = (2)_yD + (1)_y1 + (1)_y2. Every full-rank Sp(4)-type vacuum contains eps_L, of charge 2 yD, and s1 s2, of charge y1 + y2. The pseudo-Goldstone doublet has Y = yD + y_i. A neutral EW-safe end with a Y = 1/2 pseudo-Goldstone therefore forces (2)_0 + (1)_+-1/2. The doublets of the 16 and 16bar have Y = +-1/6 and +-1/2 only, so this content is new. For the mirror's own leptonic four (L', L'^c) the theta = 0 end is charged, with |Q| = 1 and B-L = -+2.
3. Exact. Spin-1/2 Weyl modes pair symmetrically in flavour (A1), giving the 10 of SU(4). The EW-invariant vacua then have rank at most 2: the (2)_0 stays massless because SU(2)_L has no symmetric singlet. Four modes also hold a single Weyl doublet, which carries the Witten anomaly. The toy's antisymmetric 6 on spinful modes therefore needs a further two-valued antisymmetric index, which gives 8 Weyl modes per cell.
4. Exact (the map asked for). The toy SU(4) = Spin(6) can be embedded in the mirror 16 in three ways. (a) As SU(4)_PS on (4,2,1), the toy 6 is the (6,1,1), which breaks colour. (b) As a Spin(6) on the bidoublet plus two colour directions, it contains colour generators (C1). (c) As the leptonic U(4) of (L', L'^c) inside u(16), its EW-safe end is charged (D2). No embedding gives a neutral EW-safe end.

## Estimates against measurement

These are estimates, not theorems. Inputs: S = -0.05 +- 0.07, kappa_V = 1.035 +- 0.031, mu_ggF about 1.0 +- 0.1, and the LEP heavy charged-lepton bound of 100.8 GeV. The literature values are approximate.

| scenario | what follows | measured comparison |
|---|---|---|
| condensed mirror, v = f (C3, C4) | Spin(10) makes all mirror members degenerate, so T = 0; S = 4/(6 pi) per mirror family | S = 0.212 (3.7 sigma, one family), 0.637 (9.8 sigma, three) |
| same | mirror quarks get their masses from v, so they do not decouple in gg -> h | sigma(gg -> h)/SM = 8.6 (one family), 46 (three) vs about 1.0 |
| same | Pagels-Stokar fixes the constituent mass from v | m* = 89 GeV (one family), 51 GeV (three) with the cell cutoff, below the LEP 100.8 GeV; with a log of order one, 774 or 447 GeV (chiral, still excluded by gg -> h and S) |
| same | scalar | radial mode at about 2 m*; no narrow SM-like 125 GeV state with these couplings |
| same | 6 colour-triplet pseudo-Goldstones (Y = -+1/3, B-L = +-2/3) | colour-loop mass about 0.5 TeV, pair-produced by QCD (bounds not compared) |
| mirror in the symmetric phase (SMG) | its masses do not come from v, so it decouples: no gg -> h shift and S of order (v/M_mirror)^2 | consistent with present data if M_mirror is above the vector-like quark bounds (about 1.5 TeV) |
| new-content candidate (D2-D3 content with the toy quartic) | xi = sin^2(theta) <= 0.051 from kappa_V = cos(theta) | f >= 1.09 TeV; IR dS about 0.013, dT about -0.037 |
| same, the scale | f/M is set by the rung carrying the quartic (n about 51 with order-one coefficient, unfixed) or by near-critical coupling | mean field needs (g - g_c)/g_c of about 2e-31 at the cell; the toy's broken-phase boundary (between g/t = 4 and infinity at T = 1/8) gives no window |

Measured reality decides between the two walls: Higgs data require the mirror family to be in the symmetric phase, which is the phase toy-qmc did not find at strong coupling. If the Spin(10) mirror pairs the way the toy does, it breaks the weak group at the mirror scale with v = f. That is excluded by m_W itself if the mirror is heavy, and by gg -> h, S and LEP if it is light. The two walls are not one. They pull in opposite directions: the chirality route needs the symmetric phase, and electroweak breaking needs a broken phase in a different sector.

## Candidate law text (tested, not adopted)

> "One quartic, two sectors. The cube-filtered pair square (the vector-channel square of a Spin(2k) spinor) acts on the mirror 16 (k = 5) in its symmetric phase and on a further electroweak four per cell (k = 3: (2)_0 + (1)_+1/2 + (1)_-1/2, carried twice by a two-valued antisymmetric index) in its pair-condensed phase; the weak doublet is the latter's pseudo-Goldstone, its angle the stationary point of the response law's total phase with the top's Yukawa-type term."

Smuggling check.
- Forced given the content: the coset SU(4)/Sp(4), the doublet's quantum numbers, v = f sin(theta), T = 0 at tree level (custodial Sp(4)), and the absence of any colour or charge breaking.
- Supplied: the new content (8 Weyl modes per cell, not in CL-1's one 16 per family), which needs the owner. Also supplied: the two-valued index (perhaps the tick's two copies; untested); placing the two sectors on opposite sides of the pair transition; the top's coupling to the condensate; the angle theta, which is not computed; and the rung or near-critical coupling that sets f.
- What it does: it unifies the interaction form, replacing weak-scale's supplied Sp(2) link factor and its failed count reading with the register's own quartic. It also turns the 1e-34 tuning into xi of about 0.05 times an unfixed f.
- What it does not do: generate v/M.
- Sign problem: the toy's det^4 sign-freedom (four identical flavours) is not established for the index structure.

## Notes used or contradicted

- weak-scale (draft): C1 (v = f for psi chi bilinears), C2 (10 -> 9 Goldstones, colour triplet plus 3 eaten) and C3 (the SU(4)/Sp(4) contrast) are rederived here. Here C3 adds the exact angle on S^9 and its colour-breaking end, B2 to B3 add the 45 and u(16N) theorems, and D2 to D3 fix the content a neutral SU(4)/Sp(4) needs. Its candidate (Sp(2) link plus four modes) is consistent with D3, which also says why four modes need the two-valued index.
- toy-qmc (draft): its SU(4) x Z4 -> Sp(4)-type breaking is identified as SO(6) -> SO(5) (A1 to A2). The direction within the 6, which it does not measure, is degenerate in the toy. The breaking does not transfer to an EW-safe vacuum on the mirror (D4).
- composite-band-3d (draft): not contradicted. Its no-atomic-limit and gapped-face-composite results bear on whether the symmetric phase exists, which this note shows is the phase measurement requires.
- Register line on the pair-square channel ("its one channel a Y = 1/2 doublet plus a colour triplet") and on "a mirror-family composite needs chiral mirrors near v (S = 0.21, 3.7 sigma)": both are rederived (B1, the E table).
- PR #9910 (unique gapped Spin(10)-symmetric ground state of one mirror cell): consistent. The single-cell phase is the symmetric one that measurement requires.
- main: VACUUM_CRITICAL_STABILITY_NOTE (a pseudo-Goldstone Higgs needs f >> Lambda_EW): consistent. B2 shows Spin(10) cannot supply it.

## Boundary

The theorems are exact representation theory and linear algebra on the stated content. The gauge-loop sign is the standard vacuum-alignment sign and is supplied. The estimates use measured inputs, leading-log Pagels-Stokar and one-loop formulas. The following are not computed:
- the Spin(10) mirror's actual phase;
- the condensation channel beyond the mean-field 10;
- theta in the candidate;
- any 3D lattice dynamics.

Nothing here excludes an electroweak sector built from new content, or a mirror that is symmetric at intermediate coupling.
