# No-Go Discipline Checklist

**Claim under test:** the current fitted diagonal-mass/`xi_u,xi_d` route
cannot be promoted as a first-principles physical completion. This is not a
claim that all quark-CP constructions fail.

## N1 — Alternative route enumeration

| Attack route | What it attempts | Result on this cycle's exact surface | Evidence | Marker |
|---|---|---|---|---|
| Substitute diagonal labels for singular masses | Defend the old mass checks as an equivalent readout | The exact Frobenius identity rules out equality of the two spectra whenever an off-diagonal entry is nonzero. | [obstruction runner, parts 1 and 3](../../../../scripts/frontier_quark_cp_carrier_spectrum_basis_obstruction.py) | ATTEMPTED |
| Recover a physical fit at the printed point despite the spectrum inequality | Argue that the two ratios could still coincide accidentally | Exact characteristic-polynomial sign brackets isolate all three eigenvalues and give disjoint rational ratio intervals excluding the two imported comparators. | [obstruction runner, part 3](../../../../scripts/frontier_quark_cp_carrier_spectrum_basis_obstruction.py) | ATTEMPTED |
| Treat a shared weak-basis change as changing the physics | Defend `xi_s` as invariant because CKM data would move with it | Exact similarity algebra and the rational control show spectra, determinants, and the full CKM product are unchanged. | [target theorem 2](../../../../docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md) and runner parts 1, 2, 4 | ATTEMPTED |
| Restrict the shared orbit to the real-tree triangle family | Argue that the orbit destroys the real `1-2`, `2-3` tree conditions | A common real `1-3` rotation keeps both tree edges real while changing the `1-3` coordinate. | [obstruction runner, parts 1 and 4](../../../../scripts/frontier_quark_cp_carrier_spectrum_basis_obstruction.py) | ATTEMPTED |
| Use the determinant-phase condition as the missing selector | Fix the carrier phase by `arg det(M_u M_d)=0` | The symbolic determinant formula is real for every carrier imaginary part; only a discrete sign product is tested. | [target theorem 3](../../../../docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md) and runner parts 1, 4 | ATTEMPTED |
| Treat the fixed Schur-NNI slice as a sufficient physical basis convention | Argue that an isolated coordinate solution inside the slice defeats the no-go | The convention can define coordinates and may make the optimizer isolated, so the source explicitly concedes that point; it cannot turn those coordinates into weak-basis-invariant observables or derive the physical readout. | [target theorem 2 boundary](../../../../docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md) and N7 below | ATTEMPTED |
| Analytically invert the imported target map | Replace numerical fitting by closed-form coordinate reconstruction | Algebraic inversion would still consume observational targets and return coordinates on the same selected slice; it does not change either premise class. | [assumption/import audit](ASSUMPTIONS_AND_IMPORTS.md) | ATTEMPTED |

Seven distinct attacks have durable evidence. A future derived joint-basis
selector, invariant replacement for `xi_s`, corrected singular-spectrum fit,
or non-Hermitian construction is an explicitly open route outside the no-go;
none is mislabelled as attempted or ruled out here.

## N2 — Wall independence

For a future positive completion the collapsed walls are:

- **W-spectrum:** use a physical singular-spectrum mass readout;
- **W-basis:** derive a joint weak-basis/texture selector or use invariant
  carrier data;
- **W-carrier-readout:** derive the carrier normalization and physical readout
  attached to the selected representative;
- **W-target:** derive the mass and CKM/J target surface without observations
  as proof inputs;
- **W-theta:** only if a physical strong-CP claim is retained, derive its
  determinant/anomaly/readout bridge.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| W-spectrum / W-basis | no | no | yes |
| W-spectrum / W-carrier-readout | no | no | yes |
| W-spectrum / W-target | no | no | yes |
| W-spectrum / W-theta | no | no | yes |
| W-basis / W-carrier-readout | no | no | yes |
| W-basis / W-target | no | no | yes |
| W-basis / W-theta | no | no | yes |
| W-carrier-readout / W-target | no | no | yes |
| W-carrier-readout / W-theta | no | no | yes |
| W-target / W-theta | no | no | yes |

Hermitian determinant reality is not counted as a separate wall; it is an
exact consequence of the route ansatz. Basis selection and carrier readout are
kept separate: choosing a representative does not derive its physical
normalization/readout, and deriving a readout functional does not select a
representative. The no-go proof itself uses the spectrum and orbit identities;
this wall table governs only the positive reopening path.

## N3 — Hidden-wall scan

The prescribed phrase scan over the target note and runner found no hits for
“we assume”, “by construction”, “as is standard”, “the framework provides”,
“bridge context”, “background”, “naturally”, “obviously”, “standard QFT”,
“registered”, or “canonical”.

Manual classifications:

- Hermiticity and real tree edges are explicit route-domain hypotheses.
- Positive diagonal labels are explicit for the singular-spectrum theorem and
  hold at the historical witness.
- Physical masses as singular values and simultaneous weak-basis covariance
  are the definitions tested by the runner, not hidden framework premises.
- Observation/atlas constants are explicitly non-load-bearing replay data.
- The conclusion does not quantify over non-Hermitian matrices, other support
  graphs, or future basis selectors.

No hidden wall was promoted during this scan.

## N4 — Residual matching

| Witness | Witness residual | Current residual | Match? | Disposition |
|---|---|---|---|---|
| Current audit verdict on `quark_cp_carrier_completion_note_2026-04-18` | fitted `xi_u,xi_d` and imported targets are not a derivation | diagonal-mass readout failure and weak-basis non-invariance of the fitted coordinates | no | task provenance and trace target only; not a proof witness |
| `QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md` | uniqueness of the off-tree `1-3` phase slot on a fixed real tree | value/readout/basis identifiability of `xi_s` | no | context only; not cited as proof |
| `QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md` | fitted carriers are non-perturbative relative to the Schur base | spectrum and weak-basis coordinate obstruction | no | dropped as witness |
| `DM_NEUTRINO_CKM_TEXTURE_TRANSFER_NO_GO_NOTE_2026-04-15.md` | universal neutrino bridge retains degenerate singular spectrum under unitary transfer | quark diagonal labels fail to equal singular spectrum | no | cross-cycle analogy only |
| `FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md` | equivariance leaves a different carrier/basepoint parameter free | quark `xi_s` changes on a weak-basis orbit | no | cross-cycle analogy only |

No prior note is used as a proof witness. The target audit blocker supplies
task provenance and explains why this route was attacked, while the new exact
identities independently prune/retype that route. Non-matching prior notes are
not markdown-linked from the source note and do not seed proof dependencies.

## N5 — Rhetoric audit

The negative statements are tested at these resolutions:

| Resolution | Tested? | Boundary |
|---|---|---|
| one Hermitian three-by-three matrix | yes | exact trace and determinant formulas |
| paired up/down matrices under a shared weak-basis change | yes | exact CKM covariance and determinant/spectrum invariance |
| historical fitted point | yes | concrete singular-ratio and coordinate-change witness |
| every Hermitian texture slice | no | not claimed |
| non-Hermitian mass matrices | no | explicitly outside scope |
| lattice/site/mode/block/global framework | no | no negative statement is made at these resolutions |
| all possible quark-CP derivations | no | explicitly denied |

The note uses “current route cannot be promoted,” not “quark CP is impossible”
or “the framework can never derive a carrier.” No rhetoric widening remains.

## N6 — Partial-closure paths

- A **basis convention** can define `xi_s` coordinates. This is a valid
  convention reframe, not a new axiom, but it caps the result at a coordinate-
  conditional/bounded surface and does not derive a physical selector.
- A **singular-spectrum objective** is a direct runner repair and remains a
  bounded numerical route until its inputs are derived.
- The existing slot-minimality companion closes only which extra edge carries
  a cycle phase on the fixed tree; it does not select the physical tree/basis
  or coefficient values.
- The approved scale-reference, kinetic-isotropy, and realized-state
  primitives were checked. None supplies a flavor basis, mass matrix, carrier
  normalization, mixing observable, or numerical target, and none is called a
  wall merely for being a primitive.
- A future retained joint-basis/texture theorem or invariant-carrier theorem
  is the explicit import-retirement/reopening path. The no-go does not call it
  a new axiom or rule it out.

No convention or existing primitive closes the source note's physical-
promotion target while leaving its claim unchanged.

## N7 — Steelman

**Hostile reviewer steelman.** The fixed Schur-NNI ansatz already declares the
diagonal labels, real tree edges, and numerical `c12/c23` coefficients; within
that six-parameter coordinate slice the optimizer may have an isolated
solution, and the common `1-3` rotation exits the slice by changing those
declared quantities. Therefore the orbit does not prove the fitted point is
non-unique inside the ansatz. Moreover, a corrected objective could use
singular values and potentially find a full physical numerical match.

**Disposition.** This is convincing against an overbroad “no fit” or “no
unique coordinate solution” claim, so neither is shipped. It does not defeat
the actual no-go: declarations defining a coordinate slice are not a
first-principles physical selector, and the old runner demonstrably did not
check singular mass ratios. The source explicitly leaves a corrected fit and
derived selector open. The claim is narrow enough to survive the steelman.

## N8 — Cross-cycle echo

- `DM_NEUTRINO_CKM_TEXTURE_TRANSFER_NO_GO_NOTE_2026-04-15.md` uses singular-
  spectrum invariance to prune a CKM-to-neutrino transfer route while leaving
  new flavor mechanisms open. It has not been retired; its route-scoping
  pattern is adopted here, not treated as quark proof.
- `FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md` records a carrier
  parameter left free by equivariance. Later work reframed related readout and
  carrier/basepoint names into one open gate rather than claiming a global
  impossibility. This mechanism supports the present convention-vs-physics
  distinction and is included in N6.
- The June 17 quark slot-minimality companion retired the slot-choice portion
  of the parent gap by narrowing to a fixed-tree theorem. It did not retire the
  coefficient, mass-readout, or basis-selector residuals. The present no-go
  therefore avoids repeating the obsolete “slot arbitrary” claim.
- The older Lane 3 fan-out showed that current-bank quark mass routes require
  new source/readout theorem content. It does not witness the current exact
  matrix obstruction and is not used as proof.

No similar wall was found to have been retired by an unconsidered mechanism.
The known retirement mechanisms—narrow theorem, convention reframe, corrected
runner, or new retained selector—are all explicit reopening paths here.

## Gate result

`PASS`: all N1-N8 checks are answered, no global no-go is asserted, nonmatching
witnesses are dropped, and the strongest steelman is absorbed by narrowing the
claim to the current physical-promotion route.
