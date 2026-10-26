D4 event, one mode per event: an order-96 nonsymmorphic flux realisation carries an explicit protected Dirac block at P = 0 and a
doubler-free overlap with an ultralocal orbit-sign chirality; but order 96 allows anisotropic gauge kinetic terms (dim 4), and the
smooth-background index is not yet established

Date: 2026-10-26
Claim type: bounded_theorem (exact representation/character facts; finite diagnostics on one seeded kernel and small backgrounds)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. Seeded, 10/10, 19 s, peak 0.9 GB, output 3.3 k characters.
  Tested under a unique filename (scratchpad d4_order96_dirac_overlap_test.py); out.txt is that run.
Pre-registration: criteria_pre_run.txt (written before code). Labels: [T] exact; [F] finite; [S] reading. Axioms unchanged.
No CL edit. Nothing adopted. Sources: d4-chiral-rotations-only (C7 lead, group/realisation code reused), d4-spin-taste-16,
d4-zoom-chirality (overlap/flux code pattern), d4-interacting-check (tensor-count method). Nothing contradicted.

1. Realisation [F census, T explicit; C1-C2]. Of the 8 sampled order-96 protected rotations-only groups, exactly 2 host a Dirac
   block; in every case the 16 events split into orbits 4 + 12, with S+alpha on one orbit and S-alpha on the other. Explicit
   16x16 monomial matrices for Ghat (order 192, nonsymmorphic tau, no fixed class, U(1) phases from stabiliser characters) form a
   representation (error 1e-13) with U(z) = -1. Module is multiplicity-free: irreps 2,2,2,2,2,6.
2. Chirality is FORCED and ultralocal [T]. A site-diagonal G-invariant grading is constant on orbits, so Gamma = eps = +1 on the
   12-orbit, -1 on the 4-orbit is the unique one with the Dirac signs. Tr eps = 8 per cell is harmless: the overlap index is
   (Tr eps - Tr sign H)/2 (checked: Tr Gamma_hat = 2 index - Tr eps exactly, C9). Correction to the pre-registration: Tr Gamma = 0
   is not needed.
3. Light-block counts [T, C3]. Hom_G(Sym^k V x S_D, S_D) = SO(4) value 2 for k = 0..3: the velocity is isotropic and there is
   no dim-6 term. Excess first appears at k = 4, and only in the S- block (3 quartics, vs 1 for S+): the quartic is NOT exactly
   (p^2)^2 for that chirality. There is off-diagonal excess at k = 5. The physical pole first sees LIV at relative order p^4
   (dim 8).
4. Kernel [F, C4-C5]. D_W = A + sum R^dag R. A is anti-Hermitian and eps-odd; R is eps-even, hops |d|^2 <= 4, and tuned linearly
   so that R(0) = 0 on S_D. D_W is G-invariant (1e-13) and eps-hermitian. It has exactly 4 null vectors at P = 0 (= S_D to 2e-14),
   and it is invertible elsewhere (Re<v,Dv> = <v,Wv>; min sv 0.21 at distance > 0.8 from P = 0). Light |det D_eff|^(1/4)/|p| has
   velocity 0.50 and anisotropy ~ eps^4 (slope 3.99): dim 6 = 0.
5. Overlap [F, C6-C7]. Built on an UNTUNED W, with light masses 4e-4 to 2e-3 below m0. GW holds to 2e-16; there are exactly 4
   zero modes at P = 0 with no tuning, and none elsewhere (min sv 0.074 = 0.9 x 2m0). It is G-equivariant (8e-15), so the
   protection survives. The light branch is isotropic, anisotropy slope 3.85. Weak point: W's far-zone floor is only ~0.08 of the
   heavy P = 0 mass (for every seeded R tried). This forces m0 = 0.041, which is small. Not optimised.
6. Backgrounds [F, C8-C9]. 2048-event Z^4 box, constant fluxes. H is Hermitian to 4e-16. Index = +Q for Q = 0, 1, 2, but
   Q = -1 gives 0: the index theorem is NOT established. The likely reason (not shown) is that flux shifts of the heavy/far
   modes are of order m0, given the small m0 and the 8^4 box. Q = 1: P_hat is a projector (6e-15); Gamma_hat decays (0.6 per
   unit, slow).
7. Interacting protection [T, C10]. G full-tensor counts at ranks 2/4/6 are 1/8/96, vs O(4) 1/3/15 and SO(4) 1/4/25. Symmetric
   counts are 1/1/2: scalar and fermion self-energies are isotropic through dim 6, and J6 appears at dim 8, as for W(F4). But
   <L2,L2> = 4 vs SO(4) 2: a G-invariant gauge kinetic term F_{mu nu} F_{rho sigma} T can be anisotropic at DIMENSION 4. So
   loops (e.g. vacuum polarisation from this fermion) are allowed to make the photon speed direction-dependent. <S2,S2> = 4 vs 2
   as well (anisotropic symmetric-tensor structures, e.g. graviton-type). (The pre-registered O(4) target "1/3" is the wrong
   comparator for a rotations-only group, since epsilon is invariant; even so, G exceeds SO(4).)

VERDICT (pre-registered rule): PARTIAL. WORKS for the free fermion: an explicit one-mode-per-event G-invariant kernel whose only
light content is one Dirac block; an ultralocal forced chirality; and a doubler-free GW overlap whose zero modes need no tuning,
with dim 6 = 0. FAILS the protection requirement for gauge fields (dim-4 anisotropy allowed in F F). The smooth-field index is
not established (Q = -1). So the 4-mode register is not yet shown to be unnecessary.

Plain statement for the owner: one qubit per event CAN carry a massless Dirac fermion, with exact lattice chiral symmetry, on
the D4 cell if the cell is a "flux" cell with 96 rotations. Spin and chirality come from how 16 events split into a 4-cluster
and a 12-cluster (composite, not atomic). But 96 rotations are too few to keep light isotropic once the fermion couples to a
gauge field, and the index test is incomplete.

Open (walls move): order-192 realisations (H^1 = 1-2, Dirac blocks not seen in the parent census; recheck); larger cells
(4D4*); a stronger Wilson floor (larger m0) and a larger box for the index; whether the gauge field's own lattice symmetry
(the W(F4)-symmetric link sector) can stay larger than the fermion's G.

Proposed CL text: none (gate failure on interacting protection). Lead, UNTESTED: "matter's 16-event cell carries the order-96
nonsymmorphic flux realisation; chirality = event-orbit sign".
Gate: (1) no fitted number, PASS. (2) no observed structure named, PASS. (3) Prediction not built for: dim-4 photon anisotropy
is allowed unless the gauge sector has larger symmetry. This conflicts with measured photon isotropy (better than 1e-17), so as
it stands it is a FAILED prediction. (4) Bends the D4 law's full W(F4) on matter.

Smuggling review. Forced: orbits, multiplicity-free decomposition, eps (unique), character counts, index formula. Supplied:
group choice (first hosting group in the seeded sample), cocycle, lambda/alpha choice (the U(1) flux pattern), random seeded
kernel coefficients, the A and R scales, m0 = half the far Wilson floor, box size 8, fluxes. Fitted: none.
Deviations from pre-registration: Tr Gamma = 0 dropped (wrong requirement, item 2). Q5 failed at Q = -1 and is recorded, not
passed. The R hop range was raised to |d|^2 <= 4, because |d|^2 <= 2 forced an extra null pair. Overlap isotropy was measured at
eps 0.02-0.005, inside the analytic radius ~m0/v. Kernel selection is best-of-6 seeded draws by Wilson floor.
