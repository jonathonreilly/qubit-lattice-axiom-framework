# AC_phi_lambda K1 Staggered K-Blindness: Real Non-Projective Lift

**Date:** 2026-07-02
**Type:** no_go
**Audit boundary:** the independent audit lane owns all verdicts. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_k1_staggered_k_blindness_real_lift_2026_07_02.py`](../scripts/acphilambda_k1_staggered_k_blindness_real_lift_2026_07_02.py) (`TOTAL: PASS=79 FAIL=0`; measured local close, N = 4 and N = 6 constructive checks)

## Claim

T9-1 proves a constructive real compensation for the `K1` staggered representative on the even torus. A diagonal sign frame `W` is obtained by edge-ratio propagation over a nearest-neighbor spanning tree, every off-tree edge closes, and the compensated rotation `Rt = W R` satisfies `Rt H_K1 Rt^T = H_K1` and `Rt^3 = I`. Thus the compensated `C3[111]` lift on the one-component staggered surface is real and non-projective: its projective class is trivial, with the same trivial conclusion for `K0`.

T9-2 transfers the real order-3 blindness theorem from PR #4831 to this retained staggered surface and establishes that the one-component staggered surface, in both retained kinetic classes, is conjugate-sector blind: for real functions `f`, `Tr(f(H) Rt) = Tr(f(H) Rt^2)` on `K1`, and `Tr(f(H_K0) R) = Tr(f(H_K0) R^2)` on `K0`.

T9-3 is the carrier-localization consequence. The one-component staggered sign-frame surface cannot supply the K-breaking registered content required off-locus. The surviving carriers are the flux/holonomy dial and genuinely two-component per-site `C^2` structure; the projective seed irreducibly needs the two-component structure. This is not a terminal no-go: it removes the one-component staggered candidate while leaving the named flux and two-component paths open.

## Frame And Retained Inputs

The sole markdown dependency is [`docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md). Its ledger scope is quoted exactly:

claim_scope (retained_bounded): "On the adjacency-licensed Q-conserving nearest-neighbor bilinear surface over per-site C^2, imposing translation and proper-cubic covariance up to local U(1) frame gives exactly two gauge/scale classes K0 and K1; the K1 branch has the stated site-local absorbing frame uniqueness, and K0 shows the flux(-1) selector is not forced."

The true text pins in that file are `Kawamoto-Smit` and `η⁰`. The present note uses only the retained two-class surface and the displayed representative below.

Campaign context, not dependency: PR #4783 `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`; PR #4789 `ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01`; PR #4798 `ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02`; PR #4803 `ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02`; PR #4831 `ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02`.

On `Z_N^3` with even `N`, the `K1` representative is

```text
eta_1(x) = 1
eta_2(x) = (-1)^(x1)
eta_3(x) = (-1)^(x1+x2)

H_K1 = sum_{x,mu} eta_mu(x) (|x><x+mu| + |x+mu><x|)
```

The `K0` representative is the same nearest-neighbor adjacency with all hoppings `+1`. The rotation is `R = C3[111]`, acting by `(x1,x2,x3) -> (x3,x1,x2)`.

## Constructive Real Frame And Trivial Projective Class (T9-1)

The computation uses the finite torus graph itself.

The vertex set is `Z_N^3`.

The edge set is the undirected nearest-neighbor support of `H_K1`.

The source edge weight is the displayed staggered sign.

The rotated target edge weight is read from `R H_K1 R^T`.

No continuum limit or symbolic lattice simplification is used in the solve.

For each nearest-neighbor edge `(i,j)`, compare `H_K1` with `R H_K1 R^T`. The support is the same, and every nonzero edge ratio

```text
H_ij / (R H_K1 R^T)_ij
```

is `+1` or `-1`. The diagonal sign equation is therefore `w_i w_j = ratio`. Starting with `w_root = +1`, breadth-first propagation over a spanning tree assigns all signs. Every off-tree edge is then checked against the same equation, so cycle consistency is computed rather than assumed.

At `N = 4`, the runner checks 192 edge constraints, 63 tree edges, and 129 off-tree closures. The covariance residual is exactly zero, `Rt^3` is exactly `I`, and the cube diagonal is all `+1`.

At `N = 6`, the runner checks 648 edge constraints, 215 tree edges, and 433 off-tree closures. The covariance residual is exactly zero, `Rt^3` is exactly `I`, and the cube diagonal is all `+1`.

The `K0` branch is trivial: `W = I`, `H_K0` commutes with `R`, `Rt = R`, and `R^3 = I`.

The gauge-class point is equally finite. Any Hermitian-covariance frame `W'` must satisfy `w'_i conj(w'_j) = +-1` on every nearest-neighbor edge because the edge ratios are real. Hence relative phases are `+-1`, so `W' = exp(i alpha)` times a sign field. The cube scales as the signed representative's cube multiplied by `exp(3 i alpha)`. The cube phase is a global convention, and a representative with cube exactly `+I` exists. The projective class of the `C3[111]` lift on the one-component staggered surface is trivial.

The runner also checks the failure modes of the construction. Removing one target edge triggers the support-mismatch branch, while trying to gauge-match `H_K1` to `H_K0` triggers the cycle-inconsistency branch. A fixed-seed random sign-gauge instance is solved as a positive control.

The failure checks matter because the construction is not a declaration that any two sign systems are gauge equivalent.

If support changes, the edge-ratio equation is not even formed.

If support agrees but a plaquette product disagrees, the spanning-tree propagation reaches a contradictory assigned sign.

Those two failures are both exercised by the runner.

The successful `K1` case is therefore a computed equivalence of the rotated representative, not a hidden assumption about staggered signs.

## Blindness Transfer (T9-2)

The compensated `K1` lift is real orthogonal, commutes exactly with `H_K1`, and has order three. The PR #4831 theorem therefore applies verbatim: for every real function `f`, `Tr(f(H_K1) Rt) = Tr(f(H_K1) Rt^2)`. The same theorem applies to `K0` with the bare rotation.

The dense heat checks use the full finite matrix at `N = 4`.

The heat operator is built by Hermitian diagonalization.

The two rotation-sector traces are evaluated with separately constructed `Rt` and `Rt^2` witnesses.

The equality gate is `1e-9`.

The exact commutator check is separate from the heat trace check.

Dense heat-kernel instances at `N = 4` give the following numerical gates:

| branch | t | check |
|---|---:|---|
| `K1` | 0.3 | `|Tr(exp(-t H_K1) Rt) - Tr(exp(-t H_K1) Rt^2)| < 1e-9` |
| `K1` | 1.0 | `|Tr(exp(-t H_K1) Rt) - Tr(exp(-t H_K1) Rt^2)| < 1e-9` |
| `K0` | 0.3 | `|Tr(exp(-t H_K0) R) - Tr(exp(-t H_K0) R^2)| < 1e-9` |
| `K0` | 1.0 | `|Tr(exp(-t H_K0) R) - Tr(exp(-t H_K0) R^2)| < 1e-9` |

The runner constructs the `R^2` compensation separately and verifies `Rt^2` equals that compensated lift. It also verifies `Rt^2 R^{-2}` is diagonal with entries `+-1`.

A discriminator inserts one complex phase on a single `K1` edge and keeps the original real compensated lift. The resulting heat-trace difference is larger than `1e-3`, showing that the blindness being used here is a property of the real staggered class, not an artifact of the trace test.

That discriminator is deliberately outside the real sign-frame class.

It does not assert a flux construction.

It only verifies that the trace test can fail when the real-class hypotheses are broken.

Thus the positive blindness instances are not protected by a vacuous equality test.

## Carrier Localization (T9-3)

The one-component staggered surface, in both retained kinetic classes and with the full `U(1)` frame freedom allowed by the retained scope, cannot source the K-breaking registered content that off-locus selection requires. Its rotation lift is real and non-projective up to global convention, and its equivariant traces are conjugate-blind.

The surviving named carriers are the flux/holonomy dial, in holonomy coordinates, and genuinely two-component per-site `C^2` structure where the projective spin lift from PR #4831 can act. The projective seed irreducibly needs the two-component structure: it cannot be manufactured from one-component staggered sign frames.

The honest boundary is the one-component staggered surface with nearest-neighbor sign frames. This note does not assess two-component constructions, flux insertions, or non-nearest-neighbor structure.

The localization is a carrier statement.

It is not a value statement.

It is not an occurrence statement.

It is not a claim that holonomy coordinates are unavailable.

It is not a claim that a two-component carrier will succeed.

It says the retained one-component staggered surface cannot carry the required projective seed.

## What This Moves

| Surface | Movement |
|---|---|
| one-component `K1` staggered candidate | removed from the K-breaking source space by real non-projective lift plus trace blindness |
| one-component `K0` adjacency candidate | removed by the same real order-3 blindness transfer |
| carrier requirement | sharpened to two-component-or-flux: projective `C^2` seed or flux/holonomy dial |

## What Does Not Move

No value is selected. No two-component computation is performed here. Chirality and K-reality questions are untouched. Occurrence and realized-state selection are untouched.

The named walls are not edited. `W_cycle_holonomy_value`, `W_defect_identity_unit`, and `W_defect_readout_selection` retain their prior boundaries.

The off-locus requirement from PR #4789 is not recomputed here.

The heat-trace face from PR #4803 is not changed here.

The scalar carrier result from PR #4831 is used as a theorem, not rewritten.

The pointer-labeling context from PR #4798 is not imported as a proof dependency.

The defect-identity-unit obstruction from PR #4783 is not altered.

## Audit Consequence If Retained

If independent review retains the computation, the source-side consequence is narrow: one-component staggered kinetic candidates, including both retained classes, are unavailable as K-breaking carriers. A downstream use may cite the constructive real lift, the trivial projective class, and the conjugate-sector blindness transfer. It may not cite this note for a value, for a two-component construction, or for an occurrence statement.

The permitted citation payload is finite:

constructive sign frame;

exact covariance;

exact order-three lift;

trivial projective class up to global phase;

conjugate-sector trace blindness;

one-component carrier removal.

## Non-Claims

This note does not create an axiom, primitive, wall, registry row, or ledger edit.

It does not prove that the flux/holonomy dial is realized in the needed sector.

It does not compute the two-component per-site `C^2` carrier.

It does not assert any terminal obstruction to `AC_phi_lambda`; it localizes the carrier requirement.

It does not change the retained Dirac-row theorem or the earlier scalar blindness theorem.

## No-Go Discipline Gate

**Gate result:** PASS bounded; not a terminal no-go.

N1: Routes are separated. The one-component staggered route is ruled out here in both retained kinetic classes. The flux-holonomy route remains the mapped wall. The two-component projective route remains open as the named seed for the next computation. The occurrence lane remains open separately. Owner primitive governance is not touched.

N2: Wall inventory is unchanged; no additional W-name is introduced.

N3: Hidden-wall scan. `compensating frame` is constructed, not assumed. `spanning tree` is an algorithmic device, not a physical premise. `projective class` is computed trivial, not asserted. `two-component carrier` is the retained row's `C^2` surface, not a derived realization claim.

N4: Residual matching is against PR #4831, PR #4789, PR #4803, and the linked Dirac row. The result extends the scalar real-order blindness logic onto the retained one-component staggered surface and leaves off-locus K-breaking to flux or two-component structure.

N5: Proven content is the constructive sign frame, exact covariance, exact cube, `R^2` compensation agreement, and heat-trace blindness at the stated dense instances. The symbolic content is the one-edge relative-phase forcing and global cube scaling.

N6: Live paths remain shaped. The immediate next computation is the two-component equivariant carrier calculation with the projective spin seed. A separate flux-holonomy calculation remains available in holonomy coordinates. Occurrence remains a separate lane.

N7: Steelman: the trivial cocycle was expected because `H_K1` is real. Reply: expected or not, the calculation upgrades the wave-8 scalar result to the retained staggered surface and forces the projective seed onto `C^2`. Concession: no value is selected.

N8: Echo check. Blindness extensions recur across scalar, heat-trace, and staggered surfaces. The lesson is to name what a surface cannot see before assigning carrier load to it.

## Verification

Local command:

```bash
python3 scripts/acphilambda_k1_staggered_k_blindness_real_lift_2026_07_02.py
```

Measured close: `TOTAL: PASS=79 FAIL=0`, with constructive checks at `N = 4` and `N = 6`, dense heat traces at `N = 4`, numeric gates `1e-9`, fixed seed `20260702`, and both rejector branches exercised.
