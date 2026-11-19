D4 event set, one fermion mode per event: what multiplicity there is, and why it does not carry the one-family 16
(bounded theorem note draft, 2026-10-26; runner d4_event_one_mode_per_event_sixteen_content_taste_cosets_and_triality_2026_10_26, 10/10, about 1 s)

Claim scope. These are exact finite statements about the CL-1 cube hop algebra, one-component W(F4)-invariant kernels on D4,
the coset structure of D4, the Kogut-Susskind construction on Z^4, the D4 zoom fixed-point kernel at the half-period momenta,
and anomaly sums. The note does not derive the 16, and it does not decide whether a staggered D4 spin cell exists.

0. What the cube actually carried (correction to the premise). The 16 was never carried by the cube's multiplicity.
   - [T, 1a/1b] On one 2x2x2 cube the anticommuting hops (face phases -1) generate M2 + M2 (dim 8). Their commutant also has
     dim 8. So 8 = (R = +-1) x (copy s = +-1) x 2, where the 2 is the register's spin doublet, and the cube's one-body
     symmetry is at most U(2) x U(2). Its only rotation-blind part is the copy sign s.
   - The copy mass gaps s = -1, which leaves one light Dirac field per species.
   - The register itself records the internal content as supplied: "Handedness bit and 16 supplied" and "(g) no clause maps
     species, colours or families to role-assigned matter sites".
   - The copy sign did two jobs, both bookkeeping and neither internal content:
     - it chose the light copy versus the mirror copy (the mirror term acts on the e^(4 pi i/3) turn copy);
     - it set where the slab's mirror lands, together with the turn charge used by the family-class and N_f = 0 mod 3
       arguments.
   - The zoom-1 register reading (2x2x2 cell = one (4,2) of SU(4) x SU(2)) was already flagged rotation-blind-versus-spin
     incompatible.

1. One mode per D4 event. [T, check 2]
   - -1 is in W(F4). So every translation-invariant, W(F4)-invariant one-component kernel has an even symbol, f(p) = f(-p),
     with no term linear in p and no spin-1/2 light mode.
   - The D4 zoom-fixed-point runners (PRs #10098, #10099) in fact carry FOUR supplied spinor components per event (gamma
     matrices). That is a departure from one mode per event that the register does not yet list.
   - Counts [T, 3a]:
     - the Z^4 hypercube has 16 corners, of which 8 are D4 events;
     - |D4/2D4| = 16, with W(F4) orbits 1 + 12 + 3 (norms 0, 2, 4). The 3 are the triality frames, which form the radical
       of the mod-2 form;
     - |D4/2D4*| = 4, with orbits 1 + 3. This is the index-4 sqrt2-zoom cell, the smallest W(F4)-invariant cell that could
       hold one 4-component spinor. Whether a nearest-neighbour phase pattern realises spin on it is OPEN.
   - Kogut-Susskind [T, check 4]:
     - the staggered 16 (16 zero modes on 4^4, i.e. 4 spin x 4 taste) lives on Z^4, which is D4 plus ONE hole class;
     - on the events alone only D^2 survives, and it is a scalar Laplacian on 2e_mu hops (root-hop weight 0);
     - only 384 of the 1152 W(F4) elements keep Z^4, so the staggered 16 breaks triality and the W(F4) protection.
   - #9821's Dirac-Kahler 16 sums the soft modes over all simplex degrees (1, 4, 6, 4, 1). One mode per event is the
     0-cochain only.

2. Is there a non-doubler internal label?
   - [T, 3b] The 16 classes of D4/2D4 are exactly Fourier dual to the 16 half-period momenta pi D4* mod 2pi D4*. Every coset
     label of a translation sublattice is therefore a taste (doubler) label, not an internal one.
   - [F, 3c] The zoom fixed-point kernel is light only at p = 0 (|D*|/|p| = 0.93). At all 15 other classes it sits at
     |D*| = 1/alpha = 2, gapped. The zoom removes the multiplicity, and this agrees with d4-zoom-chirality 2a.
   - [T, 5] Rotations permute the labels, and the W(F4) image is non-abelian (perm commutant dim 12). The commutant of the
     Standard Model group on the 16 is abelian (U(1)^6). So no identification of coset labels with the 16 is W(F4)-covariant
     with rotations acting by permutation.
   - [T, 6] Triality classes as families fail on two counts:
     - an S3-invariant mass matrix has a degenerate pair (a + 2b, a - b, a - b), which measured masses exclude;
     - fixing the classes restricts W(F4) to W(D4) (192 elements), which has 3 quartic invariants against 1, so dim-6
       anisotropy returns.

3. Anomalies [T, 7].
   - The one-family 16 cancels every sum (Y^3, Y-grav, SU3^2 Y, SU2^2 Y, SU3^3, even doublets, 16 = 0 mod 16).
   - Read as one 4 of SU(4), the taste-4 is anomalous (A = 1). Only (4,2,1) + (4b,1,2) cancels.
   - 15 Weyl (no nu^c) is 15 mod 16.
   - The Dirac-Kahler 16 components give 4 Weyl after chiral projection, not 16.

VERDICT: LOST (and not previously carried).
- The D4 zoom law gives one light chiral Weyl per supplied field. It needs spinor components (4 per event, supplied, or the
  OPEN sqrt2-cell spin route).
- The internal 16 must be supplied, as it was on the cube.
- The copy sign's role passes to the slab wall label, but only for handedness. Its turn-charge role is gone on D4: the mirror
  has the light turn spectrum (d4-zoom-chirality 3b). The family-count argument via the copy-sector turn charge therefore
  has to be rebuilt.

Proposed CL text (candidate, not adopted): "Matter content. Each matter species is one field of the D4 matter law. The
species and their link charges are supplied. Only content whose light chiral currents are anomaly-free in every link factor
and mod 16 occurs."

Smuggling gate:
(1) no fitted number;
(2) it does not name the 16 or any group, but the content is SUPPLIED and so is listed as a supplied item, not a
    derivation;
(3) prediction it was not built for: mod-16 freedom (needed for symmetric far-wall gapping) requires a neutral singlet
    nu^c in every family. UNTESTED against direct measurement;
(4) bent clause: CL-1's copy-sign clause, which is deleted on D4.
Also flag: the 4 spinor components per event bend one-qubit-per-site (owner-level, alongside the image-tower question).
