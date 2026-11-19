D4 event, one mode per event: no single Weyl node protected by a rotations-only subgroup of W(F4) on the 16-event cell
(spinor-class and chirality-trace obstructions); a protected Dirac block stays rep-allowed for order-96 nonsymmorphic flux realisations

Date: 2026-10-26
Claim type: bounded_theorem (exact group / cohomology / representation facts; finite diagnostics on seeded subgroup samples and
general invariant kernels)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. Seeded, 9/9, about 12 s, 150 MB, output 2.3 k characters.
  Tested under a unique filename (scratchpad copy d4_chiral_rotations_only_test.py); out.txt is that run.
Pre-registration: criteria_pre_run.txt, written before any code. Labels: [T] exact; [F] finite diagnostic; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Sources used: d4-spin-taste-16 (#10105: the rotations-only window, sampler, H^1 code), d4-spin-cell (#10104: cells, no eta
phases), d4-interacting-check (#10095: W(F4) protection, RP failure on root slicing), d4-zoom-chirality (#10099: slab Weyl with
4 supplied components per event). Nothing contradicted; this closes #10105's open window for single Weyl nodes.

Scope. One complex mode per event; coarse translations 2D4; point group G a protected rotations-only subgroup of W(F4)
(quartic invariant 1 and spinor cubic covariant 2, the #10105 criterion); any affine realisation x -> Ax + tau_A; any U(1) phases
on modes (commuting magnetic translations on the 16-cell); psi and psibar may carry DIFFERENT monomial actions; any kernel range.
"Single Weyl" = 2-dim light psi space W, 2-dim light psibar space W', linear term with L^dag L = p^2 1.

1. Groups [F, C2]. 16 protected rotations-only groups, orders 96, 192, 288, 576 (576 = W(F4)+). All contain -1. [T, C4] Each
   fixes only P = 0 of the cell zone (since -1 is in G, fixed momenta lie in (1/4)D4*; only 0 survives). So every other
   momentum has an UNPROTECTED little group: any node away from P = 0 (in particular every doubler) can carry dim-6 LIV.
2. Lemma [T]. An isotropic equivariant L: V x W -> W' (W, W' 2-dim) makes p -> L_0^-1 L(p) a quaternion algebra; left/right
   multiplication by U(2) preserves it only up to a real sign, so W = (right spinor) x (phase) projectively. Hence the cocycle
   of the Bloch module must equal the spinor class omega (omega_L = omega_R, since omega_L omega_R = class of V = 1).
3. Spinor class [T, C3]. For all 16 protected groups, z = (-1,-1) lies in [Ghat, Ghat] (Ghat = Spin(4) preimage): omega is
   NONTRIVIAL. (Contrast: all 29 sampled unprotected rotations-only groups, orders 48-96, have omega trivial. Protection and a
   nontrivial spinor class go together in the sample.)
4. Genuine realisations [T, C4]. H^1(G, D4/2D4) = 0 for 288 and 576: every realisation fixes an event class, which forces a
   trivial cocycle for ANY phases. With 2 and 3: no single Weyl node, any range, any twist. For 96/192 the same holds for every
   realisation that fixes a class.
5. Spin-class realisations [T, C6]. For 96 and 192, H^1 = 1 or 2: nonsymmorphic realisations without a fixed class exist, every
   orbit stabiliser has trivial spinor restriction, so U(1) phases CAN put the 16 modes in the spinor class (modules induced from
   stabiliser characters with z -> -1). Then the chirality-trace identity kills the Weyl: kernel minus cokernel of ANY equivariant
   D0 equals [M_psi] - [M_psibar] in the representation ring, and a single Weyl needs this to be (S+ - S-)alpha, whose trace on
   the lift (1,-1) of -1 is 4 alpha. The lift has trace exactly 8 (absolute value) on EVERY such 16-mode module (288
   realisations x all phase choices), so the difference is 0. No Weyl, tuned or forced.
6. Finite check [F, C5]. General invariant kernel (145 hops, |d|^2 <= 6), 187 (group, realisation, psibar character) cases at
   P = 0: forced light blocks have dims 0, 1, 4, 5, 6, 10, 12 (never 2); 1-dim blocks have L = 0 (1e-16); 144 larger blocks have
   L = 0, the rest are singular in some direction. (A psibar character twist forces zero modes, but never Weyl ones.)
7. Dirac allowance [T, C7]. Some order-96 spin-class realisations contain S+alpha and S-alpha together: a Dirac light block at
   P = 0 is rep-allowed with one mode per event (not built; its mass is not forbidden, so it needs tuning or a GW structure).
8. Nielsen-Ninomiya [T, C8]. Local chirality = degree in pi_3(GL). Rotations preserve it, so G cannot cancel it inside an
   orbit; a plain reflection flips it; the OS map Theta (reflection + psi <-> psibar + conjugation, i.e. reflection + dagger)
   PRESERVES it. Control: 16 nodes of sum sigma_mu sin p_mu, chiralities +-1, sum 0.
9. Time [T, C9]. Reflection positivity does NOT need an improper symmetry of the action. It needs invariance under the
   ANTILINEAR Theta, whose geometric part is a reflection but which is chirality-preserving and so compatible with a
   rotations-only G. What is lost is only the linear reflection, which would force vector-like content. Unitary real-time step:
   the stabiliser of the time root in G is the proper cube group (24; 48 with time reversal). It has 2 transverse quartic
   invariants, so a real-time slice step has no dim-6 protection of its own; the protection lives only in the 4D weight
   (positivity on a root slice is still failing, #10095/#10096).

VERDICT (pre-registered rule): NO-GO in the exact scope. On the 16-event cell, one mode per event, there is no single Weyl node
at any momentum with a protected rotations-only little group: for any range, phases, nonsymmorphic realisation or psi/psibar
twist. For orders 288/576 this is complete; for 96/192 it rests on the seeded sample. The only protected momentum is P = 0. There,
genuine modules fail the spinor class (3, 4) and spin-class modules fail the chirality trace (5). So question (3) (removing
opposite-chirality doublers) does not arise: no protected chiral node exists to keep.

Plain statement for the owner: on the D4 route, one qubit per event cannot by itself give a protected Weyl fermion on the
16-event cell, even with a chiral (rotations-only) lattice symmetry. The Qubit axiom survives only through (a) a protected Dirac
block at P = 0 in an order-96 nonsymmorphic flux realisation, made chiral by a GW/overlap or slab structure (open, not built);
(b) larger cells (64-event 4D4*); or (c) the slab route with 4 components per event (#10099), which bends the axiom.

Open (walls move): build the order-96 Dirac block kernel and check isotropy, dim-6 and the GW index; non-commuting magnetic
translations (cells > 16); 4D4*; Weyl plus spectator light modes (excluded here only by the 2-dim definition); the full subgroup
list (the sample is 2-generated).

Proposed CL text: none. The negative result gives no rule. The lead is (a) above, UNTESTED.

Smuggling review. Forced/exact: lifts, commutator subgroups, H^1, fixed momenta, chirality-trace identity, NN degree, root
stabiliser and its invariants. Supplied: sampler seed and size (3000 two-generated subgroups), shells |d|^2 <= 6, the U(1) phase
class (commuting magnetic translations), tolerances 1e-8/1e-9. Fitted: none.
Deviations from pre-registration: P5 "anisotropy > 1e-3" was met as "singular or L = 0" (the blocks are not invertible at all).
Not pre-registered: the spin-class (nonsymmorphic + phase) branch and its trace identity (C6), and the Dirac allowance (C7).
The first C5 normalisation (by |dD|) was wrong where dD = 0; it was replaced by |D0| before the recorded run.
