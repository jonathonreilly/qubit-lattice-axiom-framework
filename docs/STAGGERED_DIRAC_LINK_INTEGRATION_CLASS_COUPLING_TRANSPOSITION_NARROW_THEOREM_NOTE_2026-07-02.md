---
claim_id: staggered_dirac_link_integration_class_coupling_transposition_narrow_theorem_note_2026-07-02
claim_type: bounded_theorem
claim_scope: "On finite U(1)-link lattice patches (open patches and the 2x2 torus) with Q-conserving nearest-neighbor matter hopping in a fixed kinetic phase class (K0 or K1): the per-edge Haar substitution w_e = t_e u_e makes the link-integrated theory with matter phase system t and plaquette coupling beta exactly equal to the trivial-phase theory with per-plaquette couplings beta*Phi_P(t). Consequences proved here: at beta = 0 every gauge-invariant polynomial observable of the hopping kernel takes identical values on K0 and K1; at first order in beta the directed plaquette-loop observable registers Phi_P linearly with derived coefficient 1/2; fixed-background probes register the flux directly; on the torus, zero-flux wrap twists of t wash out of all link-integrated observables. The link measure is consumed as the standard Haar/uniform measure exactly as on the landed interacting-RP surface; no measure-forcing claim is made; no selection of K1 over K0 is claimed; no Tier-A status movement is proposed."
upstream_dependencies:
  - staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10
  - staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07
  - interacting_rp_full_algebra_fixed_a_gauge_invariant_four_fermion_bounded_note_2026-06-05
  - minimal_axioms
runner: scripts/staggered_dirac_link_integration_class_coupling_transposition_check_2026_07_02.py
---

# Staggered-Dirac Link Integration Class-Coupling Transposition

**Date:** 2026-07-02
**Type:** bounded_theorem
**Primary runner:** [`scripts/staggered_dirac_link_integration_class_coupling_transposition_check_2026_07_02.py`](../scripts/staggered_dirac_link_integration_class_coupling_transposition_check_2026_07_02.py)

## 1. Setting and licensed surface

The licensed kinetic input is the D-kin two-class surface from the
[kinetic-class note](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md):
K0 has plaquette flux `Phi_P = +1` and representative `t == 1`;
K1 has plaquette flux `Phi_P = -1` and representative Kawamoto-Smit
eta phases.  That note reduces P-KIN to the B-BIT choice between these
two flux classes, while P-SD is the site-local absorbing-frame theorem
on the K1 branch.

The [Kawamoto-Smit phase-class theorem](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
is the home of the P-KIN-bounded premise this note informs.  The
gauged edge variable and the det-weighted Haar-averaged gauged
staggered surface are consumed from the
[interacting-RP note](INTERACTING_RP_FULL_ALGEBRA_FIXED_A_GAUGE_INVARIANT_FOUR_FERMION_BOUNDED_NOTE_2026-06-05.md).
The named framework axioms are the
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

On an oriented nearest-neighbor edge `e`, the matter phase is `t_e`,
the dynamical link is `u_e`, and the combined hopping entry is
`w_e = t_e u_e`.  The one-particle Hermitian hopping matrix is
`H[w] = sum_e (w_e |head(e)><tail(e)| + h.c.)`.  The gauge-invariant
polynomial observables used here include `tr(H^2)`, `tr(H^4)`,
`tr(H^6)`, `det(m I + H)`, and the directed plaquette-loop observable
`W_P`, the product of the four directed `H` entries around `P`.

The link measure is CONSUMED as the standard Haar/uniform measure
exactly as on the landed interacting-RP surface; no measure-forcing
claim is made.  The landed note
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md`
records that bare gauge-covariance is measure-blind; this note stays
on the consumed-measure side of that line.

## 2. Class-Coupling Transposition

Class-coupling transposition theorem. For each edge set the substitution w_e = t_e u_e. Translation invariance of the per-edge Haar (and per-edge Z_K uniform) measure gives, exactly and at every beta: Z[t, beta] = Z[1, {beta_P}] with beta_P = beta * Phi_P(t), together with equality of all gauge-invariant matter correlators under the same replacement.

The proof is the one-line change of variables `u_e -> conj(t_e) w_e`
edge by edge.  The matter kernel becomes phase-free, `H[t u] = H[w]`.
The plaquette action transforms as
`beta sum_P Re u_P = beta sum_P Re(conj(Phi_P(t)) w_P)`, hence for
the real K0/K1 fluxes `Phi_P = +/-1` it is the phase-free action with
per-plaquette coupling `beta_P = beta * Phi_P(t)`.

The same statement is exact on every per-edge `Z_K` grid used by the
runner whenever all `t_e` lie in `Z_K`; the map is then a permutation
of the finite grid, not an approximation.  The runner uses `K = 4, 8,
16` legs as exact finite instances and a K-refinement stability check.

## 3. Bare-Point Blindness

Bare-point blindness corollary. At beta = 0 the link-integrated surface is exactly K0/K1-blind: the bare integrated point cannot source the kinetic-class selector bit.

At `beta = 0`, the action term disappears.  The per-edge substitution
therefore sends every gauge-invariant polynomial observable of the
hopping kernel to the same phase-free integral, independent of the
K0/K1 phase system.  Berezin-integrated multi-fermion correlators on
the licensed finite surface are finite polynomials in the hopping
entries, so the same substitution argument covers them.

This is a scoped negative only: the bare integrated point is blind, not
the plaquette-weighted theory, fixed-background probes, or channels
outside this U(1) polynomial-hopping surface.  The N1-N8 mini-gate in
section 7 records that scope.

## 4. Coupling-Sign Registration

Coupling-sign location corollary. Under link integration the kinetic-class bit is neither erased nor selected: it transposes into the sign of the effective plaquette coupling.

For the single plaquette, `W_P = Phi_P(t) u_P`.  With weight
`exp(beta Re u_P)`, the derivative at the bare point is
`d <Re W_P> / d beta |_{0} = Phi_P(t) <(Re u_P)^2> = Phi_P(t)/2`,
using the one-link moment identity `int u^m conj(u)^n = delta_mn`.
Thus K0 registers `+1/2` and K1 registers `-1/2`: the bit re-enters by
sign at first order.

The fixed-background control is separate and intentionally not
integrated.  At `u == 1`, each plaquette orientation contributes the
loop word and its conjugate as `2 Re Phi_P`; over four starting sites
and two orientations on the single-plaquette patch, the loop term in
`tr(H^4)` is `8 Re Phi_P`.  The runner computes the full integer:
`tr(H^4)_K0 = 32`, `tr(H^4)_K1 = 16`, hence K0 minus K1 is exactly
`16`, with identical backtracking terms cancelling from the difference.
The runner also checks `W_P = +1` for K0 and `W_P = -1` for K1 at the
same fixed background.

The one-link moment table and the `1/N` meson-dimer weight in
`HIERARCHY_DELTA0_S1_EXACT_ONE_LINK_STRONG_COUPLING_PROBE_NOTE_2026-06-11.md`
are context for the same carrier mechanism; that note is a
hierarchy-lane elimination probe.  This note's carrier corollary is
the U(1) instance on the kinetic-class surface.

## 5. Wrap washout

On the `2x2` torus, set `lambda_e = i` on every `+x` edge and
`lambda_e = 1` elsewhere.  This changes the x-wrap holonomy by
`i^2 = -1`, but every plaquette has zero added flux.  Class-coupling transposition is
per-edge and does not need simple connectivity, so all link-integrated
gauge-invariant observables are unchanged at every `beta`.

The runner verifies this with a beta-zero observable battery and with
`Z` at `beta = 0.5`.  The fixed-background diagnostic still sees the
wrap data: on the implemented torus, `tr(H^2)` at `u == 1` is `32`
untwisted and `16` with the twist.

## 6. What this does and does not do

This does NOT select K1 over K0.  B-BIT is untouched.  The selection
question relocates: under link integration the bit lives exactly in
the sign of the effective plaquette coupling.  The next path this
opens is the selector search on the plaquette-coupling sign channel,
matching the dynamical/spectral selector shape named in the linked
kinetic-class note's section 7, and on fixed-background probes,
including `the in-flight kinetic-branch selection chain (PRs #4797-#4810)`.

The opened paths named here are: (i) gauge-sector positivity/spectral
discrimination of the coupling sign; and (ii) the SU(N) baryon-charge
channel outside this note's U(1) surface.

## 7. N1-N8 mini-gate for the blindness corollary

| Gate | Scope check |
|---|---|
| N1 | Alternative routes: ATTEMPTED beta-zero integrated polynomial route is closed by the substitution identity here; ATTEMPTED plaquette-weighted channel remains live and is located by the first-order coefficient; ATTEMPTED fixed-background probes remain live; UNTESTED SU(N) baryon channel is open; UNTESTED non-polynomial or unlicensed observables are outside this surface; RULED OUT measure-selection is out of scope because Haar/uniform measure is consumed. |
| N2 | No independent wall set is claimed; the scoped closure is the measure-level substitution identity on the licensed polynomial surface. |
| N3 | No hidden wall: the identity is the one-line per-edge change of variables. |
| N4 | Residual matches the kinetic-class selector bit: K0/K1 selection remains exactly open and unchanged. |
| N5 | Rhetoric is scoped to "the bare integrated point cannot source the selector"; no global selector statement is made. |
| N6 | Partial closure path is positive: the coupling-sign registration leg shows where the bit reappears. |
| N7 | Steelman: an observable class outside polynomials in the hoppings could evade this surface; none is licensed here. |
| N8 | Echo: consistent with the linked kinetic-class note's recorded fact that the staggered-grounded RP surface does not separate K0 from K1. |

## 8. Boundaries

| ID | Boundary |
|---|---|
| U(1) link scope | U(1) links only.  U(N) determinant-charge grading admits the same substitution argument; SU(N) baryon channels with charge `0 mod N` are outside this scope and named as an opened path, not a result. |
| Q-conserving matter scope | Q-conserving nearest-neighbor matter bilinears only; pairing is excluded by the same declaration as the kinetic-class note's B-S1. |
| order scope | Class-coupling transposition is exact at every `beta`; the registration coefficient is the first-order term, with higher orders open. |
| measure scope | Haar/uniform link measure is consumed, not derived. |
| topology scope | Class-coupling transposition needs no simple-connectivity because it is per-edge.  Wrap data of `t` washes out on the torus; the kinetic-class simply-connected flux classification is cited, not extended. |
| polynomial-observable scope | One-particle kernel observables plus finite Berezin polynomiality are covered; no interacting-measure positivity claim is added beyond the interacting-RP surface consumed above. |

## 9. Runner contract

Runner: `scripts/staggered_dirac_link_integration_class_coupling_transposition_check_2026_07_02.py`.

| Gate | Count | Contract |
|---|---:|---|
| flux registration | 1 | S1 flux registration: K0 `+1`, K1 `-1`. |
| one-link moment and measure-discriminator checks | 6 | Z8 one-link moments plus von-Mises and uniform-measure discriminators. |
| degree/carrier checks | 4 | Single-hop annihilation and paired carrier degree identities for K0/K1. |
| transposition checks | 9 | Transposition identity on S1, S2, and S3, including observables. |
| beta-zero blindness checks | 7 | `beta = 0` K0/K1 blindness for polynomial observables. |
| fixed-background discriminator checks | 2 | Fixed-background discriminator: exact `tr(H^4)` difference and `W_P` sign. |
| first-order registration checks | 4 | First-order registration sign, antisymmetry, FD convergence ratio, coefficient `1/2`. |
| torus wrap checks | 3 | Torus wrap washout under integration and fixed-background distinction. |
| refinement checks | 2 | K-refinement stability and K16 transposition. |

Acceptance line: `TOTAL: PASS=38 FAIL=0`.
