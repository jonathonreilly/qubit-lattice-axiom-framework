---
claim_id: staggered_dirac_coupling_sign_channel_registration_narrow_theorem_note_2026-07-03
claim_type: bounded_theorem
claim_scope: "On finite U(1)-link lattice patches (open patches; 2D tori with L1*L2 even; 3D tori with at most one odd side, where stated) with Q-conserving nearest-neighbor matter weights in a fixed kinetic phase class: the Kawamoto-Smit eta relabeling u_e -> eta_e u_e maps (t, beta) to (t*eta, -beta) exactly, so the flux-class label and the coupling sign are jointly frame data and the relabeling-orbit invariant is the per-plaquette effective coupling beta_P = beta * Phi_P(t); pure-gauge coupling-sign blindness holds whenever a flux-(-1) Z2 1-cochain exists (GF(2) criterion), and on 2D tori the converse is also proved (blind iff #P is even; every odd-#P torus registers the sign); the plaquette first moment I_1(beta_P)/I_0(beta_P) is odd and registers sign(beta_P) exactly for beta_P != 0; and on the frozen backgrounds selected by beta_P -> +/-infinity the one-particle zero set is extensive-surface type at flux +1 versus eight isolated conical points at flux -1, so the B-BIT is registration-equivalent to the frozen-background zero-set type named by the kinetic-class note's dynamical/spectral selector shape. The link measure is consumed as the standard Haar/uniform measure; no measure-forcing claim is made; no selection of K1 over K0 is claimed; no derivation of the coupling sign is claimed; no Tier-A status movement is proposed."
upstream_dependencies:
  - staggered_dirac_link_integration_class_coupling_transposition_narrow_theorem_note_2026-07-02
  - staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10
  - staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07
  - minimal_axioms
runner: scripts/staggered_dirac_coupling_sign_channel_registration_check_2026_07_03.py
---

# Staggered-Dirac Coupling-Sign Channel Registration

**Date:** 2026-07-03
**Type:** bounded_theorem
**Primary runner:** [`scripts/staggered_dirac_coupling_sign_channel_registration_check_2026_07_03.py`](../scripts/staggered_dirac_coupling_sign_channel_registration_check_2026_07_03.py)

## 1. Setting and licensed surface

The licensed inputs are exactly these one-hop dependency edges:
[transposition note](STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md),
[kinetic-class note](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md),
[Kawamoto-Smit phase-class theorem](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
and [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

The K0/K1 surface is consumed from the kinetic-class note: K0 has
plaquette flux `+1`, K1 has plaquette flux `-1`, and the B-BIT is the
choice between those two flux classes on that surface.  The
transposition note is consumed for the identity
`beta_P = beta * Phi_P(t)`.  The link measure is CONSUMED as the
standard per-edge Haar/uniform measure exactly as there; no
measure-forcing claim is made.

Edges are oriented nearest-neighbor edges `e = (x, x + e_i)` on finite
open patches or tori in dimension `d = 2, 3`.  The matter phase is
`t_e in U(1)`, the dynamical link is `u_e in U(1)`, and the combined
hopping phase is `w_e = t_e u_e`.  The one-particle Hermitian hopping
matrix is
`H[w] = sum_e (w_e |head(e)><tail(e)| + h.c.)`.

For each oriented plaquette `P`, `u_P` and `w_P` denote the oriented
products around the unit square, and `Phi_P(t)` denotes the oriented
product of the matter phases.  The Wilson action is
`S = beta * sum_P Re u_P`, and the link-integrated quantity is
`Z[t, beta] = int Du exp(S) F(H[t u])`, with `F` any
Q-conserving gauge-invariant matter weight on the licensed surface.

The Kawamoto-Smit eta cochain used here is
`eta_1(x) = 1`, `eta_2(x) = (-1)^{x_1}`,
`eta_3(x) = (-1)^{x_1 + x_2}` in 3D, assigned to the edge
`(x, x + e_i)`.  In 2D it is
`eta_1(x) = 1`, `eta_2(x) = (-1)^{x_1}`.

The consumed eta facts are:

| ID | Fact |
|---|---|
| F1 | `eta_e in {+1, -1}` and every plaquette has `Phi_P(eta) = -1`. |
| F2 | `eta_i(x + e_i) = eta_i(x)`.  This is immediate because `eta_i` does not depend on its own coordinate `x_i`. |
| F3 | For `i != j`, `eta_i(x) * eta_j(x + e_i) = - eta_j(x) * eta_i(x + e_j)`.  The two products differ by exactly the one eta exponent whose coordinate is crossed first. |
| F4 | On an `L1 x ... x Ld` torus, eta is single-valued iff every coordinate that eta depends on has even extent; all-even `L` suffices. |

## 2. Theorem A: relabeling orbit of the (class, sign) pair

Theorem A.  The change of variables `u_e -> eta_e u_e` is a
measure-preserving bijection of the link ensemble.  Under it, exactly
and at every `beta`,

`Z[t, beta] = Z[t * eta, -beta]`.

The proof is three lines.  First, per-edge Haar measure is invariant
under multiplication by the fixed phase `eta_e`.  Second, the matter
kernel is unchanged as a function of the combined variable:
`H[t * (eta u)] = H[(t eta) u]`.  Third, each plaquette action term
maps as `Re u_P -> Phi_P(eta) Re u_P = -Re u_P`, since every eta
plaquette has flux `-1`.

The same replacement gives equality of all gauge-invariant matter
correlators.  In particular `Z[1, beta] = Z[eta, -beta]`: the K0
representative at coupling `beta` is the K1 representative at coupling
`-beta`.

Combined with the transposition theorem
`Z[t, beta] = Z[1, {beta * Phi_P(t)}]`, the relabeling-orbit invariant
is the per-plaquette signed coupling
`beta_P = beta * Phi_P(t)`.  The flux-class label and the bare sign of
`beta` are therefore jointly frame data; neither is separately
frame-invariant on this surface.  Torus validity is exactly the GF(2)
existence condition stated in Theorem B.

## 3. Theorem B: sign-blindness from the GF(2) topology condition, with the 2D converse

B1.  On any open simply connected patch, pure gauge with `F = 1` has
`Z(-beta) = Z(beta)` exactly.  Tree gauge fixing makes the plaquette
angles independent Haar variables.  The shift `theta -> theta + pi`
for every plaquette variable flips the sign of each `Re` term and
preserves Haar.

B2.  On the 2D `L1 x L2` torus, the U(1) character expansion gives

`Z(beta) = sum_{n in Z} I_n(beta)^{#P}`, with `#P = L1 * L2`.

Since `I_n(-beta) = (-1)^n I_n(beta)`, the equality
`Z(-beta) = Z(beta)` holds iff `#P` is even.  For odd `#P`, the
difference
`2 * sum_{n odd} I_n(beta)^{#P}` is positive and registers the sign.
At `beta = 1.3`, `#P = 9`, the runner recomputes the value near
`5.210e-01`.

B3.  The registration is topological.  The map `beta -> -beta` is a
link relabeling iff there is `c in C^1(lattice, GF(2))` with `dc` equal
to the all-ones 2-cochain.  Equivalently,
`rank_GF2([d]) = rank_GF2([d | all-ones])`.  For 2D tori this holds
iff `L1 * L2` is even.  For 3D tori it holds iff at most one side
length is odd, because each coordinate 2-torus `(i,j)` pairs the
all-ones 2-cochain to `L_i * L_j mod 2`.

## 4. Theorem C: the registration channel and the frozen-background zero-set dichotomy

C1.  On any open patch in pure gauge,
`<Re u_P> = I_1(beta) / I_0(beta)` for every plaquette.  This is an odd
function of `beta`, nonzero and sign-faithful for every `beta != 0`.
Theorem A maps the directed plaquette observable covariantly,
`W_P -> -W_P`.  The frame-invariant registered datum is therefore
`beta_P = beta * Phi_P(t)`: the coupling-sign channel registers
`sign(beta_P)`.  Nothing is read off a pre-record value.

C2.  As `beta_P -> +infinity`, the single-plaquette density
`exp(beta_P cos theta)` concentrates at `theta = 0`, i.e. flux `+1`.
As `beta_P -> -infinity`, it concentrates at `theta = pi`, i.e. flux
`-1`.  The Laplace width is proportional to `1 / sqrt(|beta_P|)`.

C3.  On the frozen backgrounds, the one-particle kernel on the `L^3`
torus with even `L` has two different zero-set types.

For flux `+1`, with `t = 1` and `u = 1`, the eigenvalues are exactly

`{2(cos k_1 + cos k_2 + cos k_3) : k in (2 pi / L) Z_L^3}`.

The zero set is the surface `sum_i cos k_i = 0`, and its lattice count
grows with `L`.

For flux `-1`, with `w = eta` up to gauge, write
`T_i = eta_i(x) S_i` for the signed shift in direction `i`.  By F2,
`T_i^2` has trivial phase:
`T_i^2 = S_{2 e_i}`.  For `i != j`, F3 gives
`T_i T_j + T_j T_i = 0` at every site, and the adjoint cross terms
cancel in the same way.  Thus all cross terms in `H[eta]^2` vanish and
the exact operator identity is

`H[eta]^2 = sum_i (S_{2 e_i} + S_{2 e_i}^dag + 2 I)`.

The eigenvalues of `H[eta]^2` are therefore exactly
`{4 sum_i cos^2 k_i}`.  The zero set is the eight isolated conical
points `k = (+/-pi/2, +/-pi/2, +/-pi/2)`, with
`|E| = 2 |delta k| + O(delta k^2)` isotropically.  The exact finite-L
zero count is `8` iff `4 | L`; if `L = 2 mod 4`, the spectrum is
gapped with
`min |E| = 2 min_k sqrt(sum_i cos^2 k_i) > 0`.

The kinetic-class section-7 target shape is quoted once here:
"a dynamical/spectral principle requiring point-like zero sets (relativistic cones)".
This note localizes that target shape to the coupling-sign channel; it
does not derive that preference.

Corollary.  B-BIT, i.e. `sign(beta_P)`, is registration-equivalent to
the frozen-background zero-set type: extensive surface at flux `+1`
versus eight isolated conical points at flux `-1`.  Any dynamical or
spectral preference for point-like zero sets would register
`sign(beta_P) = -1` on its surface.  No such principle is proved here,
and the selector search is transposed into this channel, not settled.

## 5. Boundaries and honest auditor read

- U(1) links only; Z_K uniform links are not treated here beyond what
  the transposition note landed.
- Q-conserving gauge-invariant matter weights only.
- Haar measure is consumed, not derived.
- The frozen-limit statements are statements about the frozen
  BACKGROUNDS as `beta_P -> +/-infinity`; the fluctuating-ensemble
  zero-set question at finite `beta_P` stays open.
- No reflection-positivity claim is made at negative coupling.  An
  RP/transfer-positivity analysis of the `beta_P < 0` ensemble is a
  named next path, not used here.
- Torus statements carry the stated parity and wrap conditions.
  Wrap-holonomy convention data remain B-H class per the kinetic-class
  note.
- Exact zero count `8` requires `4 | L`; `L = 2 mod 4` is gapped, a
  finite-size fact stated honestly.
- The point-like-zero-set preference is NOT derived from the axioms.
  The selector search is transposed into this channel, not settled.
- No selection of K1 over K0 is claimed.

## 6. What the runner checks

| Gate | Anchor |
|---|---|
| S1 | Eta cochain flux, F2/F3 identities, wrong-cochain rejector, and torus wrap well-definedness. |
| S2 | Relabeling identity with determinant matter on one plaquette and a two-plaquette strip, same-sign rejector, correlator covariance, and quadrature convergence. |
| S3 | U(1) character expansion, Bessel quadrature convergence, torus brute check, even/odd parity blindness, and odd-sector discriminator. |
| S4 | GF(2) rank obstruction for 2D and 3D tori against the stated parity laws. |
| S5 | Plaquette first moment `I_1(beta) / I_0(beta)`, independent Simpson check, oddness, sign-faithfulness, and open-patch equality. |
| S6 | Single-plaquette concentration at negative coupling and the `1 / sqrt(|beta|)` width ratio. |
| S7 | Frozen-background spectral anchors, the `H[eta]^2` operator identity, wrong-cochain rejector, zero counts, and wrong-anchor rejector. |
| S8 | Combined-flux blindness for deterministic generic link fields and its rejector. |
| S9 | Ledger pin: the Kawamoto-Smit `claim_scope` appears verbatim in this note. |

## 7. Next paths this opens

The next path this opens is one spectral preference statement on the
frozen-background dichotomy: point-like versus extensive zero sets.

The next path this opens is an RP/transfer-positivity analysis of the
negative-coupling ensemble.

The next path this opens is a finite-`beta_P` fluctuating-ensemble
zero-set statement beyond frozen limits.

The next path this opens is sector-level torus analysis where the
GF(2) obstruction is nontrivial, including odd-odd wraps.

## 8. Cited authorities (one hop, with license statements)

`staggered_dirac_link_integration_class_coupling_transposition_narrow_theorem_note_2026-07-02`
is consumed as the dependency edge for the `beta_P` transposition.  It
was not yet in the ledger at drafting time.

`staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10`
is consumed as the definition of the licensed two-class surface and
the B-BIT boundary, not as a retained authority.  Its ledger row is
unaudited at drafting time (effective_status_reason awaiting_audit).

`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` is
consumed for the eta phase-class surface.  Its ledger `claim_scope` is
"Under the declared nearest-neighbor P-KIN plus site-local unitary P-SD surface on simply connected Z^3 regions, scalarizable phase systems are exactly the Clifford -1 cocycle solutions and form one local Z2/U(1) gauge class containing the Kawamoto-Smit representative."
Its ledger effective_status is retained_bounded at drafting time.

`minimal_axioms` is consumed as the named framework axiom surface
underlying the two staggered-Dirac dependency notes; this note adds no
new axiom.

## 9. Command

Runner invocation:
`python3 scripts/staggered_dirac_coupling_sign_channel_registration_check_2026_07_03.py`.

Expected final line:
`TOTAL: PASS=39 FAIL=0`.
