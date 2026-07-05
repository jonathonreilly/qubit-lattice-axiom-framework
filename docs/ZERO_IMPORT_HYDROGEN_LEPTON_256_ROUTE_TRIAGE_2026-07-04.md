# Zero-Import Hydrogen: Lepton `1/256` Route Triage

**Date:** 2026-07-04
**Type:** partial-narrowing support note
**Claim type:** meta / route triage
**Status:** support-only. This note does not promote any retained claim, does
not derive hydrogen, and does not derive a charged-lepton mass.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_route_triage.py`

## Scope

The zero-import hydrogen goal reduces the absolute spectrum to the Hartree
scale

```text
E_H = m_e alpha(0)^2.
```

The atomic lane already has a coupling-relative hydrogen harness. The first
short route to an absolute result is therefore not another hydrogen solver; it
is a retained electron mass. On the current Lane 6 surface, the charged-lepton
scale has been sharpened to

```text
y_scale = g_2 * (1/sqrt(2)) * S_l
S_l     = 1/256
```

up to the already separated Koide/readout shape gates. This note attacks only
the scale-suppression target `S_l`. It does not address the low-energy
`alpha(0)` running gate.

## Route Triage

### Route A: `M_2(C)^tensor4` exponent route

The cleanest charged-lepton-facing handle is still

```text
dim_C(M_2(C)) = 4
dim_C(M_2(C)^tensor4) = 4^4 = 256.
```

This route matches the lepton-scale probe's own notation
`S_l = 1/(dim_C M_2(C))^4`. Its strength is that the base `4` is framework
native and the integer `256` has low look-elsewhere cost near the empirical
divisor. Its unresolved content is precise: the exponent `4` is still an
explicit bounded parameter, not a derived charged-lepton-sector selector.

**Next repair target:** derive why the charged-lepton scalar block receives
four `M_2(C)` factors without using a naive four-dimensional taste count. A
useful attempt must survive the `Z^3` / `d = 3+1` correction and must explain
the observed `256.08` divisor either as a controlled correction to `256` or as
a directly derived non-integer divisor.

**Follow-up A1 firewall:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md`
sharpens this route after the OS0 geometry repair. D17-prime supplies the
charged-lepton scalar singlet and `1/sqrt(2)` normalization; OS0 supplies four
regulator slots. The current missing theorem is the carrier attachment that
puts one `M_2(C)` factor per OS0 slot on the charged-lepton scalar coefficient.
An ordinary direct-product unit normalization over `2 * 256` components gives
`(1/sqrt(2))*(1/16)`, so the tensor lift must also remain compatible with the
A2 reciprocal/density readout.

**Follow-up A1 full-cell source-carrier support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md`
proves the finite positive half of the carrier theorem. If the charged-lepton
scalar source is a full OS0-cell linear source over the four local qubit-slot
algebras, then the source-carrier coordinate space is `M_2(C)^tensor4` with
`256` matrix-unit coordinates. This narrows A1 to deriving charged-lepton
full-cell source locality and sector specificity; slot-additive, diagonal,
scalar/tracial, and D17-only source shapes do not give the `256` carrier.

**Follow-up A1 D17/full-cell separability support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md`
proves the finite compatibility half of T3. If the full-cell carrier is
supplied as a scalar source multiplier on the stated D17 charged-lepton block,
then D17's `1/sqrt(2)` normalization separates from the `256` source weights:
the separated coefficient is `(1/sqrt(2))*(1/256)`, while direct product unit
normalization would still give `(1/sqrt(2))*(1/16)`. This does not derive the
physical source attachment or A2 readout.

**Follow-up A1 source-coupled attachment support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md`
proves the source-derivative half of that attachment route. If the
source-coupled local-action convention is adopted for a lepton-specific full
OS0-cell scalar source, the local action term
`S_lep[J] = h * B_lep * sum_c j_c O_c` gives
`dS_lep/dj_c = h * B_lep * O_c`, so the `256` full-cell source directions
attach as scalar multipliers on the fixed D17 block. This narrows A1 but does
not derive the source-coupled convention, lepton full-cell locality, A2 readout,
or `S_l`.

**Follow-up A2 discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md`
sharpens the readout side. Since `M_2(C)^tensor4 ~= M_16(C)`, projection/Born
trace on a rank-one Hilbert event gives `1/16`, while algebra-basis
coefficient density over the `16^2 = 256` matrix-unit coordinates gives
`1/256`. The latter matches `S_l`, but still requires a charged-lepton
source-measure theorem.

**Follow-up A2 source-norm discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md`
tests the source/action transfer routes. It shows that the needed class is
L1 algebra-coordinate density: `(1/4)^4 = 1/256`. L2 / Hilbert-Schmidt /
Fisher-unit normalization over the same four slots gives `(1/2)^4 = 1/16`,
so the existing RN-cocycle source-unit lane cannot close `S_l` without an
additional L1 density theorem.

**Follow-up A2 source-action simplex transfer discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md`
tests the top/RN/Fisher source-action precedent against the lepton target. It
shows that direct transfer of the primitive source-unit theorem to 256
uniform channels gives `1/sqrt(256)=1/16`, while a linear action simplex
average gives `1/256`. Therefore the next A2 theorem must select
charged-lepton linear action coefficient density, not merely primitive source
amplitude.

**Follow-up A2 source-action simplex uniformity support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md`
proves the finite positive theorem behind that route. If the charged-lepton
source action is a simplex-normalized linear coefficient over the supplied
`M_2(C)^tensor4` coordinates and is invariant under independent local
coordinate relabelings of those four slots, transitivity forces a single
coefficient and normalization gives `1/256`. This conditionally settles A2.4
after the source-action, norm, and physical-frame selectors are supplied.

**Follow-up A2 basis-selector discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md`
tests whether the L1 matrix-unit density is canonical under the full matrix
algebra. It shows that in `M_16(C)` a fixed matrix-unit coordinate average can
give `1/256`, but a unitarily conjugate flat projection has the same invariant
trace/HS data while the same fixed-basis average becomes `1/16`. Therefore A2
also needs a basis/source-frame selector, or an invariant determinant/volume
theorem that bypasses fixed coordinates.

**Follow-up A2 restricted tensor-frame support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md`
proves the positive finite-set half of A2.4: if a physical charged-lepton
tensor-product matrix-unit source frame and L1 density semantics are supplied,
then the uniform `1/256` coordinate density is invariant under slot
permutations, independent local coordinate relabelings, and arbitrary
coordinate bijections. This does not select the frame, choose L1 semantics, or
identify the density with `S_l`; it prevents spending another cycle on
coordinate-uniformity once those selectors are supplied.

**Follow-up A2 source-slot frame selector support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md`
narrows A2.3. If the charged-lepton scalar source family is supplied as
independent full-cell matrix-unit source controls
`J(j) = sum_c j_c O_c`, then the source controls themselves select the
tensor-product matrix-unit frame relative to that source map. Full `U(16)`
conjugations change the source-control family rather than merely relabeling
it. This conditionally handles the frame-selector problem after the
slot-resolved source family is supplied, but it does not derive that source
family, L1/simplex semantics, or `S_l`.

**Follow-up A2 source-strength additivity selector support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md`
narrows A2.2. If the supplied source controls are nonnegative linear
action-strength coordinates and source strength is finitely additive under
disjoint source-control coarse graining with total strength `mu(C) = 1`, then
tensor-frame transitivity gives `mu({c}) = 1/256`. This conditionally selects
the L1/simplex normalization class and keeps the L2/RN/Fisher source-unit class
at `1/sqrt(256) = 1/16`; it does not derive additive source-strength semantics,
the charged-lepton source bridge, or `S_l`.

**Follow-up A2 source-control linearity support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md`
narrows the source/action semantics beneath the additivity selector. If the
source-coupled local-action convention and the slot-resolved lepton full-cell
source family are supplied, then disjoint source controls add linearly:
`J(j_A + j_B) = J(j_A) + J(j_B)` and
`S_src[j_A + j_B] = S_src[j_A] + S_src[j_B]`. This supports the algebraic
control-additivity subpiece while leaving nonnegative source-strength
semantics, total normalization `mu(C) = 1`, relabeling symmetry, and `S_l`
open.

**Follow-up A2 source-strength normalization gauge firewall:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md`
sharpens the scale residual beneath the source-strength selector. Even after
source-control linearity, the source term
`S_src[j] = h * B_lep * J(j)` is invariant under
`(h, j) -> (h/lambda, lambda j)`, so vector-space additivity does not fix the
total-strength section `mu(C) = 1`. This splits the old source-strength wall
into positivity, total-strength normalization, and the identity that `S_l`
reads normalized source weight rather than source amplitude or coupling.

**Follow-up A2 projective-simplex section support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md`
records the positive convention/reframe path exposed by that firewall. If
charged-lepton source strength is a nonzero nonnegative projective source ray
`[j]`, then the L1 section
`sigma([j])_c = j_c / sum_d j_d` is invariant under source-control rescaling
and has `mu(C) = 1`; for the uniform 256-coordinate ray it gives
`sigma([1])_c = 1/256`. This conditionally moves the total-strength section
from "new number" to "gauge section," while leaving positivity, physical
projective semantics, uniform-ray selection, the `S_l` identity, and precision
open.

**Follow-up A2 source positive-cone discriminator support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md`
narrows the positivity subgate under that projective-source route. If
charged-lepton source strength is a real monotone finitely additive measure
over disjoint source-control blocks, singleton strengths are nonnegative.
Signed or complex source probes remain valid response probes, but they are not
normalized source-strength weights. This collapses positivity into the
source-strength semantic target; it does not derive projective semantics,
uniformity, `S_l`, A3 precision, or the electron branch.

**Follow-up A2 source-coupling gauge quotient projectivization support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md`
narrows the projectivization subgate. For a nonzero nonnegative source-control
vector, the raw pair `(h,j)` modulo positive rescaling decomposes into an
invariant overall front `H = h * sum_c j_c` and an invariant normalized
source-shape coordinate `sigma([j])_c`. The uniform ray gives `1/256`, while
nonuniform positive rays remain nonuniform. This supports the
front/source-shape quotient but does not derive the physical source-probe
readout rule, uniformity, `S_l`, A3 precision, or the electron branch.

**Follow-up A2 source-shape readout selector discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md`
narrows the readout-selector subgate. Under gauge invariance, front
independence, normalized-shape, and uniform-ray criteria, the current named
source-chain candidates select `sigma([j])_c = (h*j_c)/H`; raw `h`, raw
`j_c`, `h*j_c`, `H`, projection trace `1/16`, and RN/Fisher amplitude `1/16`
fail at least one criterion. This supports the source-shape selector inside
the source-probe interface but does not derive the physical `S_l` convention,
uniformity, A3 precision, or the electron branch.

**Follow-up A2 projective tensor-frame uniform-ray support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md`
settles the finite uniformity theorem after projective source semantics and
physical tensor-frame invariance are supplied. If a nonzero nonnegative
projective source ray is invariant under a finite transitive tensor-frame
relabeling group, then every finite-order positive scale character is trivial,
so projective invariance becomes ordinary invariance and transitivity forces a
uniform ray. The L1 section then gives `sigma([j])_c = 1/256`. This still
leaves the physical invariance bridge, `S_l` identity, and precision open.

**Follow-up A2 projective tensor-frame invariance bridge support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md`
narrows that physical invariance bridge. For the slot-resolved source family
`J(j) = sum_{c in C} j_c O_c`, each tensor-frame relabeling `g` induces a
source-family preserving relabeling `rho_g` satisfying
`rho_g J(j) = J(rho_g j)`. If the charged-lepton projective source-ray
assignment is natural under those source-family relabelings, then W5b follows:
`[j] = [rho_g j]` for every tensor-frame relabeling. Combined with the finite
transitive tensor-frame projective invariance theorem, this yields
`sigma([j])_c = 1/256`. This still leaves the physical license for
source-family naturality, `S_l` identity, and precision open.

**Follow-up A2 source-naturality label-free license support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md`
narrows that physical license. If the charged-lepton scalar source interface
is label-free, meaning its source controls carry no physical coordinate tag
beyond the supplied tensor-frame source family `J(j) = sum_c j_c O_c`, then
source-family naturality follows as source-coordinate isomorphism invariance.
The finite tensor-frame action is transitive, so the prior uniform-ray theorem
returns `sigma([j])_c = 1/256`. This still leaves the derivation or
ratification of the label-free source interface, the `S_l` readout convention,
and precision open.

**Follow-up A2 `S_l` readout identity bridge support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md`
narrows the W6 identity. The lepton-scale probe writes
`y_scale = g_2 * (1/sqrt(2)) * S_l`, while the source chain supplies the same
front factors with normalized source multiplier `sigma([j])_c`. If `S_l` is
ratified as the normalized singleton source-strength multiplier of the
charged-lepton scalar source, then `S_l = sigma([j])_c`. Combined with the
prior uniform-ray chain, this gives exact `S_l = 1/256`. This still leaves
the physical license for the `S_l` source-readout convention and the precision
correction open.

**Follow-up A2 source-probe interface compression support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md`
compresses the source/action convention, label-free naturality, projective
source-strength semantics, and `S_l` readout identity into one auditable
target: the normalized label-free charged-lepton full-cell source-probe
interface. If that interface is derived or ratified, the prior source-chain
notes compose to exact `S_l = 1/256`. This does not derive the interface,
does not place A3 precision, and does not derive the electron branch.

	**Follow-up A2 source-probe ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
		tests the compressed target for minimality. The full F/L/P/R interface closes
		the exact source-side scaffold conditionally, while every one-clause-removed
		target fails: no F loses the 256 full-cell source family, no L allows a tagged
		nonuniform ray, no P leaves raw source gauge ambiguity, and no R leaves `S_l`
		unbound. This still does not ratify F/L/P/R.

		**Follow-up A2 source-probe interface ratification decision packet:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md`
		packages the exact owner/audit contract for the normalized label-free
		charged-lepton full-cell source-probe interface: CLAUSE_TEXT_LOCK,
		CHARGED_LEPTON_SCOPE_LOCK, NO_NEW_PRIMITIVE_OR_AXIOM,
		NO_EMPIRICAL_COMPARATOR_INPUT, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE.
		If accepted, this gives source-side `S_l = 1/256` conditionally; it does
		not ratify F/L/P/R, A3 precision, the electron branch, or hydrogen.

		**Follow-up A2 F-clause source/action assembly discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md`
	decomposes F into F1 source-coupled local-action convention, F2
	charged-lepton sector specificity, F3 full OS0-cell tensor source locality,
	and F4 scalar-multiplier attachment. With all F1-F4 supplied, the source
	family has `S_lep[j] = h * B_lep * sum_{c in C} j_c O_c` and
	`dS_lep/dj_c = h * B_lep * O_c`; every one-input-removed F target fails.
	This still does not ratify F, L/P/R, `S_l`, A3 precision, or the electron
	branch.

	**Follow-up A2 F1 source-coupled local-action ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
	narrows F1 specifically. A local linear source term
	`S[j] = S_0 + sum_c j_c A_c` gives the finite derivative
	`dS/dj_c = A_c`, but F1 still requires the adopted or retained
	source-insertion convention that lets this derivative count as a physical
	local source insertion. This supports the F1 ratification target
	conditionally; it does not ratify F1, F, `S_l`, A3 precision, or the
	electron branch.

	**Follow-up A2 F2 charged-lepton source-block selector discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md`
	narrows F2 specifically. D17 supplies the bounded charged-lepton scalar
	block `B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R` with
	`Z_lep^2 = 2`, but F2 still requires explicit charged-lepton sector
	restriction and source-block attachment. This supports the F2 selector
	conditionally; it does not ratify F2, F, `S_l`, A3 precision, or the
	electron branch.

	**Follow-up A2 F3 full-cell tensor source-locality ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
	narrows F3 specifically. OS0 supplies the four-slot geometry and the
	full-cell carrier support proves `M_2(C)^tensor4` with `256` matrix-unit
	coordinates after a full-cell source is supplied, but F3 still requires the
	physical charged-lepton source-locality license, full tensor independence,
	and ratification. This supports the F3 ratification target conditionally; it
	does not ratify F3, F, `S_l`, A3 precision, or the electron branch.

		**Follow-up A2 F4 scalar-multiplier attachment ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
		narrows F4 specifically. D17 supplies the charged-lepton scalar block and
		F3 supplies the full-cell source target, but F4 still requires scalar
		multiplication, D17 block preservation instead of `512` product weights, and
		ratification. This supports the F4 ratification target conditionally; it
		does not ratify F4, F, `S_l`, A3 precision, or the electron branch.

		**Follow-up A2 L label-free source-coordinate ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
		narrows L specifically. The target needs a supplied source interface,
		tensor-frame relabeling, label-free license, tag exclusion, and
		ratification before tensor-frame source relabelings can count as
		label-free coordinate isomorphisms. A coordinate-tagged nonuniform ray
		gives singleton weight `1/112`, so the no-tag convention remains
		load-bearing. This supports the L ratification target conditionally; it
		does not ratify L, F/L/P/R, `S_l`, A3 precision, or the electron branch.

		**Follow-up A2 P positive projective source-strength ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
		narrows P specifically. The target needs a source-strength object,
		positive nonzero domain, source-scale gauge, projective L1 section,
		source-shape selector, and ratification before `sigma([j])_c` can count
		as the physical positive projective source-shape coordinate. The
			one-input-removed witnesses reject raw `h`, raw `j_c`, `h*j_c`, `H`, and
			`1/16` alternatives. This supports the P ratification target
			conditionally; it does not ratify P, F/L/P/R, `S_l`, A3 precision, or the
			electron branch.

			**Follow-up A2 R `S_l` readout identity ratification target discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
			narrows R specifically. The target needs scale-symbol context, source
			coefficient context, common nonzero front, normalized singleton candidate,
			source-readout license, and ratification before `S_l` can count as the
			physical normalized singleton source-strength multiplier. The
			one-input-removed witnesses reject symbol-only, coefficient-only,
			mismatched-front, raw source-shape, lattice `y_0`, A3/threshold, and
			empirical comparator routes. This supports the R ratification target
			conditionally; it does not ratify R, F/L/P/R, A3 precision, or the
			electron branch.

			**Follow-up A2 source-coordinate unfixed-choice label-free support:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md`
			attacks the label-free coordinate-tag subclause using the now-closed `#4952`
	Qualification clarification proposal or an equivalent retained rule. If a law
may not depend on an unfixed choice absent admission, then a nonuniform
law-level source-coordinate selector requires an admitted coordinate tag. This
supports the label-free clause only under that retained-rule condition; it does
not derive the source/action interface, projective source strength, `S_l`, A3
precision, or the electron branch.

### Route B: lattice `g_2^2 / 64` route

The strongest shortcut-looking handle is the lattice-scale result

```text
g_2^2 |_lattice = 1/4
y_0_lattice = g_2^2 |_lattice / 64 = 1/256.
```

This is real progress on the old `G_WEAK` framing: the lattice weak coupling
piece is retained-grade algebra inside the cited convention. But it is not yet
a charged-lepton scale derivation. The `/64` factor is an identified
leptogenesis convention, and `y_0` has not been identified with the
charged-lepton suppression `S_l`.

**Next repair target:** either derive the `/64` normalization from the
charged-lepton scalar operator itself, or prove a retained bridge
`S_l = y_0_lattice` for the charged-lepton block. Without that bridge, this
route is a candidate splice, not a closure.

**Follow-up firewall:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md`
sharpens this route further: the `/64` splice hits `S_l = 1/256` only when
the suppression slot uses lattice `g_2^2 = 1/4` while the front factor uses
`g_2(v)`. If both slots use weak-scale `g_2(v)`, the suppression is about
`68%` too large.

**Follow-up A3 firewall:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md`
pins the precision residual common to Routes A and B. Exact `256` is not the
repo comparator divisor `256.082435...`; a future route must either derive a
downstream correction `C_A3 = 0.999678091...` after exact `1/256`, or derive
the noninteger divisor directly.

**Follow-up A3 placement discriminator:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md`
splits that correction into named placement classes. The same product can be
written with `C_A3` in the source readout, the weak front factor, the
Koide/electron readout factor, or a direct noninteger divisor, but those
placements have different dependency responsibilities. A future A3 theorem
must license one placement instead of laundering a fitted correction into the
exact `1/256` source scaffold.

**Follow-up A3 precision-placement decision packet:** `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md`
packages that placement problem as a nine-input owner/audit handoff:
A3_PLACEMENT_TEXT_LOCK, EXACT_SOURCE_SCAFFOLD_STATUS, ONE_PLACEMENT_SELECTED,
PLACEMENT_THEOREM_RETAINED, NO_SOURCE_DOUBLE_COUNT,
NO_EMPIRICAL_COMPARATOR_INPUT, NO_NEW_PRIMITIVE_OR_AXIOM,
OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If accepted,
`A3_PRECISION_PLACEMENT_RETAINED` follows conditionally, but the packet does
not derive `C_A3`, `m_e`, `alpha(0)`, or hydrogen.

**Follow-up K4 scale-assembly decision packet:** `ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md`
packages the absolute charged-lepton scale handoff after source-side exact
`S_l` and A3 placement. Its ten inputs are K4_SCALE_TEXT_LOCK,
CHARGED_LEPTON_SCOPE_LOCK, WEAK_FRONT_BASE_RETAINED,
EXACT_SOURCE_SINGLETON_RETAINED, A3_PRECISION_PLACEMENT_RETAINED,
NO_SOURCE_A3_DOUBLE_COUNT, NO_COMPARATOR_PROOF_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If
accepted, `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED` follows conditionally, but
that is K4 scale support only; it does not derive `m_e`, `alpha(0)`, or
hydrogen.

### Route C: C-iso anisotropy-ratio route

The C-iso orbit can display `256` as a ratio:

```text
beta_tau / beta_sigma = xi^2.
```

For example, `xi = 16` gives `256`, while `xi = 1/16` gives `1/256`. That is
not a charged-lepton selector. The C-iso theorem proves that the anisotropy
degree of freedom routes into the Wilson coefficient doublet while the
bare-coupling conclusion is invariant along the orbit. The approved
kinetic-isotropy primitive supplies only `c_t = c_s` as OS0 kinetic-form
isotropy; it does not supply an anisotropy selector or a lepton-sector
weight.

**Next repair target if pursued:** supply a physical selector for `xi` and a
separate bridge from the resulting action-coefficient ratio to `S_l`. This is
not the shortest zero-import hydrogen lane.

### Route D: Koide / supertrace shape route

The Koide, supertrace, equivariant-index, and holomorphic leads remain relevant
to the charged-lepton shape and readout problem. They do not by themselves set
the absolute scale suppression `S_l`.

The Koide native zero-section `#5007` impact discriminator
(`ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md`)
keeps this route live as a parallel electron-readout target. It records
`KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE` as useful route-algebra
context, but it does not derive zero-source readout, the real-primitive Brannen
endpoint, the based determinant-line readout, the physical electron species
bridge, or the absolute charged-lepton scale.

The Koide native zero-section bridge ratification decision packet
(`ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md`)
packages the Z1/Z2/Z3 bridge as the next owner/audit handoff:
BRIDGE_TEXT_LOCK, ZERO_SOURCE_READOUT_RETAINED,
REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED,
BASED_DETERMINANT_LINE_READOUT_RETAINED, NO_COMPARATOR_PROOF_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If
accepted, `NATIVE_ZERO_SECTION_BRIDGE_RETAINED` follows conditionally, but
physical electron species, absolute scale, `alpha(0)`, and hydrogen remain
downstream.

The physical electron species-bridge ratification decision packet
(`ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md`)
packages the K3 species bridge as a separate owner/audit handoff:
K3_SPECIES_BRIDGE_TEXT_LOCK, C3_GRADE_SCOPE_LOCK,
MINIMUM_DECOMPOSITION_RETAINED, RATIFICATION_CLASS_BOUNDARY_RETAINED,
PR4929_OWNER_ADOPTION, NO_ABOVE_C3_CONTENT_INPUT, NO_COMPARATOR_PROOF_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If
accepted, `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED` follows conditionally,
but K1/K2 readout, Z1-Z3 native bridge, absolute scale, `alpha(0)`, and
hydrogen remain downstream.

The absolute charged-lepton scale ratification decision packet
(`ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md`)
packages the K4 scale assembly separately: K4_SCALE_TEXT_LOCK,
CHARGED_LEPTON_SCOPE_LOCK, WEAK_FRONT_BASE_RETAINED,
EXACT_SOURCE_SINGLETON_RETAINED, A3_PRECISION_PLACEMENT_RETAINED,
NO_SOURCE_A3_DOUBLE_COUNT, NO_COMPARATOR_PROOF_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If
accepted, `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED` follows conditionally, but
it does not close K1/K2 readout, the native bridge, the physical species
bridge, `alpha(0)`, or hydrogen.

The Tier-A owner-retirement `#4991` impact discriminator
(`ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md`)
keeps this route from overclaiming the open governance work. If adopted,
#4991 would move old `AC_phi_lambda` occupancy and R-eta atoms to
owner-governed premise standing, but it still does not derive `S_l`,
`rho_e(delta)`, `m_e`, `alpha(0)`, or hydrogen.

**Next repair target:** keep this route parallel to Route A/B, not instead of
them. Hydrogen needs both the shape/readout and the scale.

### Route E: realized-state or empirical divisor route

The realized-state primitive permits pointwise evaluation at a supplied
law-admissible realized state. It does not supply the state, a state-selection
rule, a weighting rule, or a mass value. Likewise, the empirical relation
`a_lepton^2 ~= m_W / 256` is an open gate and cannot be used as a zero-import
derivation input.

**Next repair target:** do not route zero-import hydrogen through realized
state data unless the goal is explicitly downgraded from retained derivation
to registered-data evaluation.

## Lane Decision

The nearest lane is **Lane 6, charged leptons**, specifically the lepton-scale
`1/256` suppression gate.

The immediate work should split into two concrete attacks:

1. **Primary:** derive the charged-lepton `M_2(C)` exponent/selector. This is
   the route most directly aligned with `S_l = 1/(dim_C M_2(C))^4`.
   The full-cell source-carrier support theorem narrows this to a physical
   source-locality target: prove that the charged-lepton scalar source is a
   full OS0-cell source over the four qubit-slot algebras, not merely a
   slot-additive, diagonal, scalar/tracial, or D17-only source. The
   F3 full-cell tensor source-locality discriminator narrows this to a
   ratifiable target: OS0 geometry, physical source family, full tensor
   locality, independent matrix-unit controls, and retained adoption. The
   D17/full-cell separability support theorem then shows the D17 block
   normalization is compatible with such a supplied carrier, and the
   source-coupled attachment support theorem shows how action derivatives
   attach the carrier once the source-coupled convention and lepton-specific
   full-cell source are supplied. Neither theorem derives those source-side
   inputs.
2. **Secondary:** retire the `/64` convention import by deriving it inside the
   charged-lepton scalar block, or prove a retained bridge
   `S_l = y_0_lattice`.
3. **A2 readout follow-up:** prove the source-measure theorem selecting
   algebra-basis coefficient density instead of projection/Born trace, and
   specifically the L1 algebra-coordinate density class instead of the
   L2/Fisher source-unit class. The source-action simplex transfer
   discriminator shows that the top/RN primitive source-unit precedent gives
   `1/16` on 256 channels; the `1/256` lane needs linear action coefficient
   density. The simplex uniformity support theorem then proves that local
   coordinate relabeling symmetry plus simplex normalization forces `1/256`,
   once the physical source frame is supplied. The latest refinement adds a basis/source-frame
   selector: fixed matrix-unit coordinates give `1/256`, but full inner-automorphism
   covariance returns the tracial/projection `1/16` class. The restricted
   tensor-frame support note then conditionally settles the coefficient
   uniformity sub-wall once the physical frame and L1 source semantics are
   supplied. The source-slot frame selector support note then narrows the
   frame-selector wall: a slot-resolved matrix-unit source family selects its
   own tensor frame, but the charged-lepton full-cell source family itself
   remains to be derived. The source-strength additivity selector support note
   then conditionally supplies the L1/simplex norm selector: finite additivity
   of nonnegative action-strength controls plus total strength one gives
   `mu({c}) = 1/256`, while the L2/RN/Fisher source-unit class remains
   `1/16`. The source-control linearity support note then reduces the source
   semantics one step further: source-coupled local action gives algebraic
   additivity of disjoint source controls once the convention and slot-resolved
   source family are supplied, but it does not supply positivity or total
   normalization. The source-strength normalization gauge firewall then
   isolates the next residual: `S_src[j] = h * B_lep * J(j)` is invariant under
   `(h, j) -> (h/lambda, lambda j)`, so the total-strength section
   `mu(C) = 1` and the identity that `S_l` reads normalized source weight must
   be supplied separately. The projective-simplex section support note then
   supplies the convention/reframe path for that section: if source strength is
   the positive projective ray `[j]`, the L1 representative
   `sigma([j])_c = j_c / sum_d j_d` has total strength one and gives `1/256`
   on the uniform 256-coordinate ray. The remaining live gates are positivity,
   physical projective semantics, uniform-ray selection, `S_l` identity, and
   precision. The source positive-cone discriminator support note then
   narrows the positivity subgate: real monotone finite-additive
   source-strength semantics forces singleton nonnegativity, while signed or
   complex probes are response probes rather than normalized source-strength
   weights. The source-coupling gauge quotient projectivization support note
   then supplies the finite front/source-shape decomposition: `(h,j)` modulo
   positive rescaling gives invariant `H = h * sum_c j_c` and invariant
   normalized `sigma([j])_c`. The source-shape readout selector discriminator
   then narrows the candidate readout subgate: under the source-shape criteria
   Q1-Q4, `sigma([j])_c = (h*j_c)/H` is selected among the current named
   candidates. The remaining live gate is the source-strength semantic bridge
   itself, plus physical source-probe readout, uniformity, `S_l`, and
   precision. The
   projective tensor-frame uniform-ray support note then
   conditionally handles the finite uniformity step: finite transitive
   tensor-frame projective invariance forces the source ray to be uniform, so
   the projective-simplex section returns `1/256`. The live residue is the
   physical bridge that the charged-lepton source ray has that tensor-frame
   invariance. The projective tensor-frame invariance bridge support note then
   reduces that residue to source-family naturality for
   `rho_g J(j) = J(rho_g j)`: if the charged-lepton source ray assignment is
   natural under source-family preserving tensor-frame relabelings, W5b follows
   and the prior uniform-ray theorem returns `sigma([j])_c = 1/256`. The live
   residue is now the physical license for source-family naturality, plus
   `S_l` identity and precision. The source naturality label-free license
   support note then narrows that residue: if the charged-lepton scalar source
   interface is label-free, with no physical coordinate tag beyond
   `J(j) = sum_c j_c O_c`, source-family naturality follows as
   source-coordinate isomorphism invariance and the prior theorem returns
   `sigma([j])_c = 1/256`. The live residue is now the derivation or
   ratification of the label-free source interface, plus `S_l` identity and
   precision. The `S_l` readout identity bridge support
   note then reduces W6 to a source-readout convention: if `S_l` is the
   normalized singleton source-strength multiplier in the charged-lepton scale
   factorization `y_scale = g_2 * (1/sqrt(2)) * S_l`, then
   `S_l = sigma([j])_c`, and the prior chain gives exact `1/256`. The live
   residue is now the label-free source-interface license, the
   physical license for that `S_l` readout convention, and precision. The
   source-probe interface compression support note then collapses those
   source-side licenses into one target: derive or ratify the normalized
   label-free charged-lepton full-cell source-probe interface. If supplied,
   the source chain gives exact `S_l = 1/256`, while A3 precision and the
   Koide/electron branch remain live. The source-probe ratification target
	   discriminator then proves all four F/L/P/R clauses are necessary among the
	   tested targets: removing F, L, P, or R breaks source-side closure. The
	   L label-free source-coordinate ratification target discriminator then
	   narrows L itself: source interface, tensor-frame relabeling, label-free
	   license, tag exclusion, and ratification are all required, and a
	   coordinate-tagged nonuniform ray gives `1/112`. The P positive
	   projective source-strength ratification target discriminator then narrows
		   P itself: source-strength object, positive nonzero domain, source-scale
		   gauge, projective L1 section, source-shape selector, and ratification are
		   all required, and the rejected no-P witnesses are raw `h`, raw `j_c`,
		   `h*j_c`, `H`, and the `1/16` alternatives. The R `S_l` readout identity
		   ratification target discriminator then narrows R itself: scale-symbol
		   context, source coefficient context, common nonzero front, normalized
		   singleton candidate, source-readout license, and ratification are all
		   required, and the rejected no-R witnesses are symbol-only,
		   coefficient-only, mismatched-front, raw source-shape, lattice `y_0`,
		   A3/threshold, and empirical comparator routes. The
		   source-coordinate unfixed-choice
		   support note then narrows the label-free subclause conditional on the
   now-closed `#4952` proposal or equivalent retained rule: a law-level
   nonuniform source-coordinate selector needs an admitted tag.
4. **Precision follow-up:** derive the `256.08` correction after exact `256`,
   or derive the noninteger divisor directly without using the empirical
   open-gate values as proof inputs. The A3 placement discriminator now
   requires the theorem to declare whether `C_A3` belongs to source readout,
   front-factor/threshold matching, Koide/electron readout, or a direct
   noninteger-divisor theorem. The A3 precision-placement decision packet then
   packages that as the one-placement/no-double-count owner/audit contract.

Lane 2 becomes active again after `m_e` improves: `alpha(0)` still needs the
QED-running firewall retired through charged-lepton, heavy-quark, and hadronic
vacuum-polarization thresholds. The atomic hydrogen harness is the final
substitution and verification surface, not the first bottleneck.

## No-Go Discipline Gate

This section applies the no-go discipline to prevent a broad negative claim.
The checked broad claim would be: "the existing `256` handles cannot close the
charged-lepton suppression." That broad no-go is **not** shipped. The result is
demoted to this narrower claim: the currently documented handles do not by
themselves close `S_l`; they sharpen the next attack targets.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| `M_2(C)^tensor4` | Use `4^4 = 256` as the charged-lepton suppression. | ATTEMPTED. It gives the right integer, but `d=4` is an explicit bounded parameter in `M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md`. |
| `16^2` taste/hierarchy | Use `256 = 16^2` from the naive taste count. | RULED OUT BY PRIOR for this purpose by the `d = 3+1` survival test and the regulator-dependence boundary cited in `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md`. |
| lattice `g_2^2/64` | Substitute retained `g_2^2 |_lattice = 1/4` into the cycle-12 `y_0 = g_weak^2/64` convention. | ATTEMPTED. It gives `1/256`, but the `/64` convention and the `y_0 -> S_l` charged-lepton bridge remain unclosed. |
| projection/Born trace | Read `M_2(C)^tensor4 ~= M_16(C)` through a rank-one projection event. | ATTEMPTED. It gives `1/16`, so it sharpens the A2 readout wall rather than closing `S_l`. |
| C-iso ratio | Read `1/256` from `beta_tau/beta_sigma = xi^2` at `xi = 1/16`. | ATTEMPTED. The cited theorem makes this a convention-orbit ratio for action coefficients, not a lepton-sector selector. |
| Koide/supertrace | Use the shape/readout route to derive the electron mass. | RULED OUT AS COMPLETE SCALE ROUTE by current Lane 6 notes: it attacks shape/readout, while `S_l` remains the scale gate. |
| realized-state data | Let the realized state supply the lepton weights. | RULED OUT AS ZERO-IMPORT ROUTE by `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`: the primitive supplies evaluation only, no state content or selector. |
| empirical `m_W/256` | Use the observed relation directly. | RULED OUT AS ZERO-IMPORT ROUTE because it is the open comparator gate, not a derivation input. |

### N2 - Wall-independence audit

The narrowed wall set is:

| wall | content |
|---|---|
| W1 | Sector-identity wall: prove the candidate quantity is the charged-lepton suppression `S_l`. |
| W2 | Count/source wall: derive the `4` exponent or the `/64` normalization. |
| W3 | Precision wall: account for `N = 256.08` versus exact `256`. |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 <-> W2 | no in either direction | independent |
| W1 <-> W3 | no in either direction | independent |
| W2 <-> W3 | no in either direction | independent |

No wall is double-counted. A derivation of `4^4` alone would not prove it is
`S_l`; a sector bridge alone would not derive the number; exact `256` alone
would not explain the `0.032%` empirical offset.

### N3 - Hidden-wall scan

The proof text was scanned for assumption-hiding language. The relevant
registered or convention words are already explicit:

| phrase class | classification |
|---|---|
| `approved primitive` / `primitive` | cited registry boundary, not a hidden selector. |
| `convention` | explicit wall for `/64` and C-iso, not used as a derivation input. |
| `bridge` | explicit W1 sector-identity wall. |
| `empirical` | comparator/open-gate role only, not a proof input. |

No hidden admission is left buried as background.

### N4 - Residual matching

| cited surface | residual it actually attacks | match to `S_l` closure? |
|---|---|---|
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | structural base and exponent status for charged-lepton `1/256` | yes |
| `M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md` | finite algebraic count `4^4 = 256` with `d=4` input | partial: count only |
| `G_WEAK_FROM_FRAMEWORK_NOTE_2026-05-03.md` | lattice `y_0 = g_2^2/64` inside a leptogenesis convention | partial: same value, different residual |
| `G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md` | C-iso orbit invariance for `g_bare` | no: not a lepton suppression residual |
| `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | pointwise realized-state evaluation boundary | no: registry guard only |

Non-matching citations are not counted as witnesses for closure.

### N5 - Rhetoric audit

The note does not claim "`256` is not structural" or "no route exists." It
uses the narrow claim "the currently documented handles do not by themselves
close charged-lepton `S_l`." Tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| integer arithmetic | yes | all three handles can display `256` or `1/256`. |
| charged-lepton sector identity | yes | no cited handle proves `S_l = candidate`. |
| count/normalization source | yes | `d=4` and `/64` remain explicit residuals. |
| all possible per-mode or future operator routes | no | not claimed closed. |

### N6 - Partial-closure path scan

The primitive registry was checked. `scale_reference_primitive` supplies units
only; `kinetic_isotropy_primitive` supplies OS0 kinetic-form isotropy only;
`realized_state_primitive` supplies pointwise evaluation only; the current
minimal axioms supply no selector, weighting rule, normalization rule, or
mass value.

There is a legitimate import-retirement path: reframe the `/64` convention as
a derivable charged-lepton scalar normalization, or prove it is the same
sector quantity as `S_l`. That would not be a new axiom if it is carried by a
retained bridge or a convention-retirement audit. This is why the artifact is
partial narrowing rather than a no-go.

### N7 - Steelman

A hostile reviewer can fairly argue: the lattice `g_2^2/64` note already
produces exactly `1/256` without PDG input, and the lepton-scale formula needs
exactly a dimensionless `1/256`. If the charged-lepton scalar normalization
and the cycle-12 `y_0` normalization are the same framework object written in
two dialects, then this note is artificially separating a bridge that should
be an audit/documentation cleanup. That is the strongest reason to pursue
Route B next instead of declaring any no-go.

### N8 - Cross-cycle echo

Similar walls have been retired before by separating structure from labels or
conventions, especially where a route first looked like a new axiom but later
became an import-retirement or convention-ratification path. The `G_WEAK`
cycle itself inverted an old obstruction by showing that a missing
phenomenological input was actually a bounded running surface plus a retained
lattice primitive. The same mechanism could apply here if `/64` is shown to
be charged-lepton scalar normalization rather than a leptogenesis-only
convention.

**Gate result:** broad no-go fails; narrowed partial-triage passes. The next
cycle should attack Route A's exponent selector or Route B's `/64` bridge.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the exponent `4`.
- No derivation of the `/64` normalization.
- No proof that `S_l = y_0_lattice`.
- No derivation of `m_e`, Koide, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_route_triage.py
```

The verifier checks the arithmetic for the three `256` handles, confirms the
primitive-registry boundary, verifies the no-go discipline section is present,
and guards the explicit non-claims.
