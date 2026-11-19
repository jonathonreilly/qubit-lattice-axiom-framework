D4 spin x taste on the 16-event cell: no W(F4)-symmetric (or parity-containing protected) realisation for one mode per
event; only a rotations-only (chiral) window stays open, and there the KS shift mechanism is excluded

Date: 2026-10-26
Claim type: bounded_theorem (exact group / F2 / representation facts; finite diagnostics on a seeded subgroup sample and
supplied free kernels)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. Seeded, 11/11, about 9 s, output 2.1 k characters.
  Tested under a unique filename (scratchpad copy d4_spin_taste_16_test.py); out.txt is that run.
Pre-registration: criteria_pre_run.txt, written before any code. Labels: [T] exact; [F] finite diagnostic; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Sources used: d4-spin-cell (#10104: cells, no eta phases, untasted Frobenius obstruction, quartic counts),
d4-sixteen-content (#10103: orbits 1+12+3, cosets = tastes), d4-zoom-fixed-point-fermion (#10098), d4-interacting-check
(tensor-count protection). git grep origin/main: no D4/W(F4) staggered, spin-taste or Adams note (main's staggered work is
Z^3). Nothing contradicted; this closes #10104's OPEN item "16-event spin x taste with long hops" for W(F4).

Set-up. Every 2D4-periodic kernel (any range, any U(1) phases) is a 16x16 matrix D(P) in the cell basis; fine
translations, rotations and phases act P-independently up to scalars. "Spin x taste" = D(P0+p) = (gamma.p) x 1_T + O(p^2)
on all 16 modes. Then every symmetry acts as U(g) = S(A) x T(g) (S = Pin lift; the leading term forces this).

1. No KS-type taste Clifford with W(F4) [T, C2]. W(F4)-invariant subspaces of D4/2D4: 0, R (frame classes), all; of the
   character group: 0, R^0 (= annihilator of R), all. Invariant alternating forms: 0 and b = x.y mod 2, rank 2. A Pauli
   (shift + character) internal group acts irreducibly on a 4-dim taste space iff its F2^8 image is 4-dim nondegenerate;
   the three possible shapes (graph over F2^4, R + R^0, all characters) are all degenerate.
2. Frobenius-orbit no-go [T, C3-C4]. H^1(W(F4), F2^4) = H^1(W(F4), F2^4/R) = 0, so ANY symmetry group mapping onto W(F4)
   (with any shifts or phases) has an event class x whose stabiliser G_x maps onto W(F4). Then C^16|G_x = lambda + M3 + M12
   (classes 1 + 3 + 12), and lambda in S x T forces T|G_x = S* lambda, so C^16|G_x = End(S) lambda, whose W(F4)
   constituents have dims 1, 1, 4, 4, 6. No subset makes 3. Hence no spin x taste on the 16-event cell with W(F4), at any
   kernel range, any phases, any internal symmetry. With #10104's untasted argument (light S x T' needs dim T' >= 4), there
   is no light spin content of any taste multiplicity. The same holds for both index-2 subgroups that contain reflections.
   Nodes away from P = 0 have stabilisers of order <= 384 (quartic count >= 2: unprotected per species).
3. Control [T, C5]. KS on Z^4: B4 classes 1+4+6+4+1 = End(S) dims (Dirac-Kahler), partition passes, KS form invariant,
   quartic count 2, cubic count 2: spin x taste exists, unprotected. The orbit pattern is the whole difference.
4. Subgroups [F, C6]. Seeded sample (3000 two-generated subgroups, plus det+): 19 protected groups (quartic 1, cubic = O(4)/
   SO(4) value), orders 96-1152. Every one containing an improper element fails the partition. Every rotations-only one
   (96, 192, 288, 576) passes, with S = two Weyl halves (reducible), so the Frobenius step no longer fixes T. That is the
   window.
5. KS mechanism closed in the window [T, C7; F, C8]. A graph-type taste Clifford makes every symmetry a Clifford element
   (monomial U normalises the character Paulis and the shifts), so Ad S(A) is a signed Pauli permutation on Sigma-perp:
   |tr S(A)|^2 <= #fixed classes of A. W(F4) violates this (52 elements); all 12 (protected group, nondegenerate form)
   candidates violate it (8 elements with |tr S|^2 = 9 > 1). NN root hops with those dressings: no Clifford sign pattern.
6. Taste lifting [F, C9; supplied]. KS + Adams flavoured mass r(1 - prod cos 1 x xi5): 8 light modes (2 tastes x 4 spin),
   light p^4 coefficient anisotropic (axis -0.083, body +0.167 at r = 1; free KS -1/3, -1/12). The zoom fixed point on one
   mode per event gaps the 15 corners but has no spin (#10103). Hoelbling-type one-taste terms: not built; argument: they
   fix a rank-1 taste projector, i.e. (T|G_x = S*) a spinor line, which shrinks the symmetry further.
7. Count [T, C10]. Taste carries the spinor rotation (T|G_x = S* lambda; KS: 16 = End(S)). Taste is a doubler label locked
   to rotations, not an internal label. SU(4) Pati-Salam reading: FLAGGED only (and a single taste-4 is anomalous, #10103).

VERDICT (pre-registered rule): PARTIAL.
- NO-GO (exact): W(F4), and every protected group containing an improper element (index-2 exact, others sampled).
- Open window: rotations-only protected groups (96-576), with non-Pauli internal symmetry or none. Taste-dependent terms
  (e.g. p_a gamma_b x Sigma_ab) must then be excluded by rotations alone. Not shown either way; no kernel built.

Proposed CL text (UNTESTED, not adopted): "Matter's 16-event cell carries no improper symmetry: the event weight is
invariant under a rotations-only subgroup of W(F4) with a single quartic invariant, plus the coarse translations."
Gate: (1) no fitted number, PASS; (2) names no observed structure, PASS (chirality of the lattice is a rule on neighbours);
(3) prediction not built for: lattice-level parity violation with Weyl halves of different normalisation; UNTESTED, and the
rule is not yet shown to give spin at all; (4) bends: the D4 law's full W(F4) (protection would rest on a subgroup).
Gate: incomplete (3). Report as a lead, not a rule.

Plain statement for the owner: with one qubit per event, full W(F4) symmetry cannot produce spin-1/2 on the 16-event cell
in any form, tasted or not. The Qubit axiom can be kept only if the lattice symmetry is rotations-only (chiral), or if a
larger cell (64 events) works. Neither is shown yet. Otherwise the D4 matter law needs four modes per event (#10104).

Open (walls move): the chiral window (explicit kernel; taste-dependent dim-4 count); the 64-event cell 4D4*, where
stabilisers are smaller and S may restrict reducibly; the 2-generation sample is not every subgroup.

Smuggling review. Forced/exact: forms, subspaces, H^1, End(S) dims, orbit partition, KS control, Clifford character bound.
Supplied: the Adams term and r = 1, subgroup sampler seed and size, NN hop set in C8, tolerances 1e-8/1e-9. Fitted: none.
Deviations from pre-registration: Q2 also gave the improper/proper split (not foreseen); the Adams term was first coded as
r(1 - gamma5 x xi5) (wrong: light modes then disperse as p^2/2r) and replaced by the flavoured mass 1 x xi5 before the
recorded run.
