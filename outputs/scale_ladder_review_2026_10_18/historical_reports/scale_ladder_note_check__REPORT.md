# Independent check: scale-ladder cross-rung note (2026-10-18)

Provenance: fresh-context agent of the same model family (Claude Opus 5.5), not an independent
human reviewer. No repo files outside this directory were edited; the runner was not rerun.
Scripts: common.py (own translation-invariant gauge via GF(2) with translation rows), item1_shifts.py,
lift2O.py (2O lift by BFS from C4z, C3[111] generators on the full 768-dim space), item2_item4_rep.py,
item2_random.py, item3_isotropy.py, item4_gap.py, item4_extra.py, item5_answer_check.py; logs *.log.

## Item 1 -- CONFIRMED
s_R derived from gauge signs: sigma_R(q)sigma_R(q+e_i) is constant per (R,i); M_R T_t M_R^-1 = chi_R(t) T_{Rt}
verified as operator identity; s_R = R a mod 2. All 8 shift classes occur (identity and two C3 have s=0).
Bloch cross-check M_R B(k) = B(Rk+pi s_R)U holds. Fixed set {k*, -k*}; with s_R=0: {Gamma, (pi,pi,pi)}.
Same affine action on grids pi/4, pi/6, pi/12 gives the same two points (aside: the shift data is L-independent).

## Item 2 -- CONFIRMED
Own BFS lift: exactly 2 of 4 generator-sign choices are homomorphisms (they differ by A2); central element = -I on
the full space. Class invariants on k* block without any lift: (twisted C2axis)^2 = (C2edge)^2 = (C4)^4 = -I.
Global-lift decomposition at k* and -k*: E1/2+E5/2+2G3/2 each (content A2-symmetric, so lift ambiguity harmless).
Random rot+translation-symmetric H, every range, strengths 1e-2..1e3, seed 777, no H0: all levels even at +-k*;
Gamma shows 1-fold levels. Break attempts: bare (ungauged) permutation symmetry -> all 1-fold at k* (the class
requires the gauge-dressed PSG operators); C3[111] subgroup only -> 1-fold. Rotations + even translations only:
folded levels still even (statement extends).

## Item 3 -- CONFIRMED
Own X (seeds 5, 99), 409 directions (Fibonacci + axes), six parameter points incl. t2 in {0.1..0.5}, X in {0.02..0.3}:
anisotropy ratio per halving 3.96-4.12 at q=0.08, 4.0000+-0.0003 at q<=0.02, for both k* doublets. v is linear in
X strength (0.0714 at 0.05, 0.2855 at 0.2, seed 5); quoted v=0.110 and 2.60e-4 are specific to the runner's X.

## Item 4 -- CONFIRMED WITH CORRECTIONS
PSG: I R I^-1 R^-1 = A2(R) exactly, I^2 = -1. Inversion maps E1/2(k*) -> E5/2(-k*) with weight 1.000, G3/2->G3/2.
Commutant of {rotations, inversion} on the folded 24-space: dimension 12, all irreps 4-dim (multiplicity 2 each),
random commutant elements [4x6]; rotations alone give 2- and 4-fold. So "every level a multiple of 4 at any
strength" is an exact Schur statement in this class. Real-space strength-3 random backgrounds: all 4-fold.
A2 gap/eps: relative change between halvings 2e-6..2e-9 (runner's 4e-3 is a tolerance, not a measurement).
Corrections: (a) quartet splitting is necessary, not sufficient, for a Dirac mass: the inversion-broken control
splits quartets into pinned Weyl doublets with no mass; rotations alone already forbid a gap at k*. Drop
"(a Dirac mass)" as gloss of "splitting". (b) The sampled A2 term is not inversion-symmetric (even/odd norm ratio 2.0);
its inversion-even part alone splits every quartet, its inversion-odd part only 2 of 6. Say so. (c) Control: the
2-fold eigenvectors mix valleys (k*-weight 0.10-0.93), so "the two valleys separate in energy" should read
"inversion partners split". (d) "4-fold" -> "multiplicity divisible by 4".

## Item 5 -- CONFIRMED (math); interpretation overclaims
Reynolds on explicit bases: B4: sym rank-2 1, general rank-2 (gamma_mu k_nu) 1, quadratic forms in F_mu nu 1,
sym rank-4 2 (so LV first at k^4, dimension 6). O_h x T: 2, 2, 2, 4. So the common-speed conclusion does extend to
Dirac and gauge-invariant spin-1 kinetic terms -- conditional on: B4 acting on spinors through its double cover;
exact gauge redundancy for spin-1 (without it 3 forms, per gravity probe) and linearised diffeo for spin-2
(only "locus-closed" in repo); exactly isotropic step a_t = a_s (anisotropic lattices need per-species tuning);
no spontaneous breaking. Doublers: a symmetric 4D fermion step brings temporal doublers; Wilson-in-time removal
keeps RP and B4 but breaks the chiral (w1-odd) protection, re-introducing additive mass tuning. Reflection
positivity of the corner model is untested: it is a 3D Hamiltonian model with pi-flux and a projective spin
realization; a 4D version is a different model and its v (~0.1, set by X) would have to become 1.
"only if time is on the same footing" is too strong (sufficient, not necessary; Chadha-Nielsen flow is the cited
alternative). "One speed then serves the electron, the photon and the graviton" is physical identification in
answer text.

## Lane table vs REPORT.md
Maxwell: "kernel unique" not in report. Formation: report says "largely explained", caveat heavy-tailed codings
omitted; strong-coupling phase difference omitted. Handedness: CME probe is a two-band toy model with unresolved sign,
not the corner model. Readout: "menu abundance" listed as not helped, report says reframed. Electron row's C20
in-progress claim has no report behind it.

## Citations
All checked from memory as correct: Wen PRB 65 165113; LSM AnnPhys 16 407; Oshikawa PRL 84 1535; Hastings PRB 69
104431; 't Hooft NATO B59 135; Wilson-Kogut PhysRep 12 75; Chadha-Nielsen NPB 217 125; Collins et al PRL 93 191301;
Vidal PRL 99 220405; Swingle PRD 86 065007; ADH JHEP04(2015)163; Zurek NatPhys 5 181; Osterwalder-Seiler AnnPhys 110
440; NN NPB 185 20; Gleason JMM 6 885; Davies CMP 39 91; van den Berg-Steif AnnProb 27 1501 (least certain).
Wording: Collins et al. corrections are unsuppressed by the cutoff (order coupling), not "order one".
