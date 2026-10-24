---
claim_id: the_spin10_gapping_channel_carries_the_higgs_doublets_but_as_the_electroweak_higgs_it_forces_zero_quark_mixing_and_an_unsplit_heavy_ten_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "For the forced far-wall gapping term -(g/2) sum_a {B_a, B_a^+} with B_a = psi_1^T C Gamma^a psi_2 on the 16 (spin10-two-flavour) and the SM embedding Y = (1/3) sum_colour h - (1/2) sum_weak h: (A) exact: the channel is the 10, = (1,2)_{+1/2} + (1,2)_{-1/2} + (3,1)_{-1/3} + (3bar,1)_{+1/3}; its colour-singlet part carries exactly the Higgs quantum numbers, the neutral components pair (u,u^c)+(nu,nu^c) and (d,d^c)+(e,e^c) with one Clebsch (all nonzero entries of modulus 1); the Spin(10) commutant on the 10 is one-dimensional, so the term gives doublets and triplets the same mass and the same coupling matrix, and the triplets carry qq and q^c l^c couplings. (B) exact: as the Yukawa source, one symmetric family coupling Y gives M_u = M_nu = Y v_u, M_d = M_e^T = Y v_d, hence |V_CKM| = 1; family-local channels (each family's mirror its own 10) give diagonal M_u, M_d and a permutation |V_CKM|. (C) exact: the unique ground state has <B_a> = 0; the 10 level sits at 10 g (fermion 13 g, lowest excitation the charge-4 singlet at 4 g); reduced Spin(6) diagonalisation agrees. Estimates against supplied measurements (separate): |V_us| = 0.2250(7) excludes the rule 'electroweak Higgs = the gapping channel' at 336 sigma, independent of the matching scale; m_s/m_mu = 0.22, m_d/m_e = 2.4 and (m_s/m_b)/(m_c/m_t) = 6.8 also fail, only m_b/m_tau = 0.59 is near 1; a triplet degenerate with a weak-scale doublet is excluded by p -> e+ pi0 (M_T > 2e10 GeV). Not covered: the electroweak scale (not produced: open), additional forced channels (126, 120), the interacting slab, light-mirror coupling of the channel."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_spin10_pair_square_on_two_sixteens_is_a_spin12_casimir_with_a_unique_singlet_ground_state_and_gap_four_g_but_a_frozen_far_region_still_moves_the_mirror_bounded_theorem_note_2026-10-23
runner: scripts/the_spin10_gapping_channel_carries_the_higgs_doublets_but_as_the_electroweak_higgs_it_forces_zero_quark_mixing_and_an_unsplit_heavy_ten_2026_10_23.py
---

# The Spin(10) gapping channel carries the Higgs doublets, but as the electroweak Higgs it forces zero quark mixing and an unsplit heavy 10

Claim type: bounded_theorem. Exact statements are labelled [T], finite diagnostics [F], estimates against measurement [E].
Runner: runner.py, TOTAL: PASS=13 FAIL=0, 0.1 s, 3.5 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was run under a unique filename (scratch/higgs_gapping_channel_test_run.py). Axioms unchanged. No rule adopted.

## Question

spin10-two-flavour showed that the fewest-change Spin(10)-invariant far-wall term on the two spin components of the 16 is
the 10-channel pair square, with a unique symmetric ground state and gap 4 g. The 10 is the Higgs representation of SO(10)
unification. Is the electroweak Higgs this channel (B_a, or its Hubbard-Stratonovich boson phi_a), with Yukawa 16.16.10,
so that the rules predict the Higgs without adding one by hand?

Rule under test (H10, not adopted): "The electroweak Higgs is the 10-channel of the forced far-wall gapping term; Yukawa
couplings are the 16.16.10 couplings of that channel."

## Repo first (earlier Higgs results)

- higgs-from-structure: every colour-singlet doublet in 16 x 16 has B-L = 0 and Y = +-1/2 and sits in the 10; no
  structure of the laws gives a light B-L = 0 doublet; the tested rule failed the gate.
- mirror-condensate-ew (register, "Mirror condensate as the Higgs"): a mirror condensate in the 10's colour-singlet part
  breaks SU(2) x U(1) but on S^9 the only vacuum angle runs from EW to colour breaking, so v = f, and a condensed mirror is
  excluded (S, gg -> h, LEP). The mirror must be in the SYMMETRIC phase.
- ax6-higgs: the SU(4)/Sp(4) light-Higgs content (2)_0 + (1)_+-1/2 is in no structure of the laws; supplying it inserts
  observed structure and fails the gate (register owner decision 3: 8 new Weyl modes per cell).
- higgs-5mode, rung-higgs: earlier site/rung routes (scratch; not re-derived here).
So the earlier campaign's Higgs routes failed for two reasons: the light doublet had to be inserted (gate failure), or
the forced 10 condensate gives v = f with colour on the same vacuum manifold (measurement failure). This note tests the
remaining identification, the gapping channel itself as the Higgs and as the Yukawa source, which none of those tested.

## Pass criteria

Written before any run: criteria_pre_run.txt. One correction after the first run: the oscillator weights were defined
with the opposite sign (h = n - 1/2 gives the 16bar on even states); the fix h = 1/2 - n made A2/A3 pass as predicted.
The criteria themselves are unchanged.

## A. Quantum numbers (exact)

- A1 [T]. Each complex pair direction (C b_k^+, C b_k) pairs 16 weights with w1 + w2 = +-e_k, each once: the channel is
  the 10 (the pair matrices from the explicit oscillator 16).
- A2 [T]. With Y = (1/3) sum_colour h - (1/2) sum_weak h the 16 is Q(6) + u^c(3) + d^c(3) + L(2) + e^c + nu^c with
  standard hypercharges, and the 10 = (1,2)_{+1/2} + (1,2)_{-1/2} + (3,1)_{-1/3} + (3bar,1)_{+1/3}.
- A3 [T]. The colour-singlet doublets carry exactly the measured Higgs quantum numbers. The neutral component with pair
  hypercharge -1/2 pairs (u,u^c) and (nu,nu^c) (the H_u slot); the one with +1/2 pairs (d,d^c) and (e,e^c) (H_d). Every
  nonzero entry has modulus 1: one Clebsch, so M_u = M_nu and M_d = M_e^T.
  This is a genuine structural success: the forced gapping channel contains the Higgs doublet's quantum numbers, which
  were not put in.
- A4 [T]. Schur: the Spin(10) commutant on the 10 is one-dimensional. The forced term (Spin(10)-invariant) gives the
  doublets and the triplets the same mass and the same coupling matrix. Nothing in the term splits them.
- A5 [T]. The triplet directions pair qq (QQ), q l (QL), u^c e^c and u^c d^c: baryon-number-violating couplings fixed by
  the doublet Yukawas.
- What else in the rules could split doublet from triplet: only the Spin(10)-breaking parts (the SM gauge links if the
  links are SM-valued). They split the 10 radiatively by ~ alpha/(4 pi) (relative), not by the >= 1e8 needed (C3). Not
  computed beyond this estimate. The doublet-triplet problem is inherited, not solved.

## B. Yukawa relations (exact) and the measurement test

- B1 [T]. The 10 sits in the symmetric part of 16 x 16 (C Gamma^a symmetric, Lorentz epsilon antisymmetric, so the family
  matrix Y is symmetric). One coupling: M_u = M_nu = Y v_u, M_d = M_e^T = Y v_d. M_u and M_d are proportional, so their left
  singular vectors coincide and |V_CKM| = 1 (200 seeded complex Y, error 8e-15). Ratios m_u/m_d = m_c/m_s = m_t/m_b =
  |v_u/v_d| for every family; m_d = m_e, m_s = m_mu, m_b = m_tau. A real 10 also forces v_u = v_d (m_t = m_b); a complex
  10 (the channel is complex: B carries J = -1) allows tan beta.
- B2 [T]. If each family's mirror carries its own gapping 10 (the term acts within one family's 32 modes), every channel
  couples ii only: M_u and M_d are both diagonal for ANY VEVs, |V_CKM| is a permutation. Still no mixing.
- B3 [F] (contrast, escape, not forced): two independent symmetric couplings (a 10 plus a second channel, e.g. the 126)
  give generic mixing (median |V_us| 0.29).
- B4 [E]. Measured |V_us| = 0.2250(7) (PDG 2024, supplied) against the predicted 0: excluded at 336 sigma. V_us runs
  very little, so this holds at any matching scale (near-wall or far-wall).
- B5 [E]. Supplied SM running values at 2e16 GeV (Xing-Zhang-Zhou 2008): m_b/m_tau = 0.59 (near 1, within 50%; the
  rough success, closer in supersymmetric running per literature, not computed); m_s/m_mu = 0.22 and m_d/m_e = 2.4
  (predicted 1); m_c/m_t = 3.2e-3 vs m_s/m_b = 2.2e-2 (predicted equal; off by 6.8).

Verdict: the rule "electroweak Higgs = the gapping channel, with its 16.16.10 coupling as the Yukawa source" is FALSIFIED
cleanly by measured quark mixing, and by the second- and first-family mass relations. This is the result.

## C. Scale (exact) and the electroweak scale (open)

- C1 [T]. From F = 144 - 2S(S+1) - C2_10 - J^2 (spin10-two-flavour): the 10 composite B^+|GS> is at 10 g, all ten
  components degenerate; the fermion at 13 g; the lowest excitation is the charge-4 Spin(10) singlet at 4 g. The unique
  ground state is a J eigenstate and B carries J = -1, so <B_a> = 0 exactly: the forced term breaks no electroweak symmetry.
  The 10 is HEAVY (gap scale g), not near-wall light.
- C2 [F]. Reduced Spin(6) site (2^8, full diagonalisation): unique ground state (gap 4 g), max |<B>| 3e-32, all six
  B_a^+|GS> at one energy (6 g). (The Spin(6) case has antisymmetric M, a different type; it is a Schur illustration only.)
- C3 [E]. With triplet couplings fixed by B1 (first-family y_u y_d ~ 1.8e-11), p -> e+ pi0 (tau > 2.4e34 yr, alpha_H =
  0.012 GeV^3, D + F = 1.27) needs M_T > 2e10 GeV. Degenerate with a weak-scale doublet, the triplet is excluded by > 1e8.
- The electroweak scale is not produced. The purpose of the term (a symmetric gapped mirror) REQUIRES <B> = 0; the
  Higgs role requires <B_doublet> != 0 with <B_triplet> = 0. Condensing the channel is the mirror-condensate route (v = f,
  colour on the same S^9, excluded). v/(10 g) at a cell scale of 1e16-1e19 GeV is 1e-14 to 1e-17: the hierarchy is open.
- Coupling to the light family: the term acts on the far (mirror) wall. A phi coupling to the light 16 needs either the
  same term on the near wall (which would gap the light family symmetrically: excluded, the light fermions are seen) or
  bulk-suppressed transmission. Not computed; it would only rescale Y, so B1/B2 stand.

## Rule wording and gate

H10 (tested, NOT adopted): "The electroweak Higgs is the 10-channel of the forced far-wall gapping term; Yukawas are its
16.16.10 couplings."
1. Measured numbers chosen: none (g, Y free): PASS.
2. Observed structure inserted by name: none beyond the register's 16 / Spin(10) and the forced channel. The SM embedding
   of Y is used to READ the channel, not to build it: PASS.
3. Predictions it was not built for: the Higgs quantum numbers (A3, success), |V_CKM| = 1 and the per-family mass
   equalities (B1/B2), doublet-triplet degeneracy (A4), <B> = 0 (C1). Tested: FALSIFIED by measurement (B4, B5, C3).
4. Axiom bent: none beyond those of the gapping term itself (spin10-two-flavour: none if the 32 modes are a cell).
Gate result: non-smuggling PASS; against measurement FAIL. Reported as a failure, not adopted.

What a replacement rule would need (proposals only, untested): a second forced Yukawa channel with a different family
matrix (10 + 126 is the minimal SO(10) structure known to fit masses and mixing; the 126 pair square is also
Spin(10)-invariant but is not the fewest-change term), a family-off-diagonal gapping channel, and a doublet-triplet
splitting mechanism plus a weak-scale source, none of which the present rules force.

## Smuggling review

Supplied: the 16 with one orbital per weight; the 10-channel form (forced upstream); the SM embedding used to read
quantum numbers; GUT-scale running masses, |V_us|, proton-lifetime bound, hadronic matrix element (estimates only).
Forced: the 10 content and its Higgs-doublet quantum numbers; the single Clebsch; Schur degeneracy; |V_CKM| = 1 (single
and family-local); <B> = 0; the 10 g level.
Not shown: the electroweak scale; a doublet-triplet splitter; extra channels; the slab and the light-wall coupling.

Literature (cited, not computed): Georgi-Jarlskog 1979 (m_s/m_mu factor 3); Babu-Mohapatra 1993 (10 + 126 Yukawa);
Xing-Zhang-Zhou 2008 (running masses); PDG 2024; Super-Kamiokande 2020; Aoki et al. (alpha_H); You-He-Xu-Vishwanath 2018.
