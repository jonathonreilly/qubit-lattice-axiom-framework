# Primitive kinetic photon test: bounded source comparison

This is a focused mathematical comparison, not a formal audit or empirical test. The pre-author proof and all 15 files bound by `INDEPENDENT_FREEZE_v1.json` remain unchanged. That freeze has SHA256 `c0169b30739ddccc8c086ee3be618a4f6680f156a02495b9a5e1ec9e1f2c13f6`.

**The operator calculation agrees. The old full-ray physical witness had a real domain failure, and its numerical noise interpretation needed qualification. The supplied v3 repair and angular addendum resolve those two issues within this bounded check.**

## Correspondence and surviving mutation

The author multiplies the strong kinetic equation by minus lambda; my pre-author proof uses plus lambda. All final kernels consequently differ by one global sign. The commutator N=-KZ, radial divergence 2/r, time derivative of a*cY, and the ordered primitive pullback agree. In conformal coordinates the author's measure is correctly a*r^2*deta*dr, not r^2*deta*dr. The formal abstract domain requires a>0, r>0, K=C'+hC nonzero, sufficient coefficient regularity, and compact boundary traces. Final lambda derivatives have order at most seven; the polynomial windows vanish through derivative order seven and have C7 zero extensions.

For arbitrary probes the exact residual correction is
`M_first-M_eliminated=integral(wJ*rE-b*rN)dmu`.
Those probes do not satisfy the physical equations and the author labels them accordingly.

The physical harmonic Z=-4r^2/eta has Delta_2 Z=0, so reversing the wZ sign has zero integrated effect. For the separately declared Z0=eta^3*r^3 probe, Delta_2 Z0=6eta^3*r. I independently obtain the old-window wrong-minus-right moment
`-103843867/263793576254208000`, which is nonzero. Thus the added probe challenges a sign that the physical fixture cannot. The supplied probe note preserves that distinction. I checked the mathematical reason; the historical mutation execution receipt itself was outside the supplied comparison set.

## Domain failure and correction

The original eta[-2,-1], r[1,2] source rectangle includes eta=-3/2,r=7/4,u=1/4. Its ray eta_ray=u-s crosses zero at s=1/4. Polynomial continuations of P and the photon primitives do not extend the singular background through that crossing. The old local operator moments remain valid algebraic calculations, but they were not a valid complete physical ray witness.

The correction fixes eta[-4,-3], r[1,2]. Every complete ray lies within eta_ray[-4,-1], with a regular open enlargement available. The v2-to-v3 runner delta changes the window, corresponding exact integration limits, error-example coordinates, and four domain controls; the action, mode, candidate, and primitive formulas are unchanged. The exact source delta is preserved losslessly inside `POST_EXPOSURE_SOURCE_BINDINGS_v3.json`.

A separate beta-integral calculation gives Ckin(Utrue)=0, Ckin(0)=3P and the corrected wrong-candidate moment
`827093/50599790841600 = 1.634577902879423747345137e-8`.
This matches all three v3 author moment entries. The calculation is independent of the author's Laurent integration implementation.

## Error interpretation

The abstract full-measure triangle inequality is correct. The numerical two-dimensional L1 budgets apply to errors in the recovered normalized-Y20 harmonic coefficients. They do not directly bound arbitrary full-sky pixel errors of the same numerical size. I independently verify
`integral|Y20|dOmega=4sqrt(15pi)/9=3.050970776212563...`.
The angular addendum states this distinction correctly.

The v3 source budgets give the unit-template coefficient radius m/[2(Npsi+Nz)] approximately 2.772445809344887e-37. For a common pointwise full-sky envelope, divide this conservative radius by the angular factor, giving approximately 9.087093953704027e-38. These are source-bound monomial-triangle budgets: I checked their implementation and radius arithmetic but did not independently recompute every high-order weight norm. Guaranteed rejection for every perturbed record requires a strict epsilon<radius; the factor two covers both the displacement from the nominal moment and the candidate's error allowance. All radii scale by the absolute common signal amplitude. No instrument precision or usable conditioning is established.

## Executed scope and remaining obligations

The frozen pre-author stage has 61 exact controls on an independently chosen nonphysical operator fixture. Post-exposure checks add 57 generic algebra/angular/domain/trace controls in 0.72 seconds and 12 corrected-moment/source-arithmetic checks in 0.31 seconds. Both owned subprocesses used a 120-second cap and disabled bytecode; complete stdout/stderr and source pins are preserved. There were no owned failed or timed-out subprocesses, and no retries. Both implementations use SymPy; no author helper was imported or executed by these checks. I read the complete supplied notes, runners and results. Per instruction, I did not replay either unchanged author aggregate; reported author totals 73/0 and 77/0 are inspected source results.

This check does not re-establish every original action/pressure/scalar equation of the inherited noncanonical fixture. The full-ray geometric repair is verified conditional on that stipulated local fixture. The test remains necessary rather than sufficient for an action solution; finite moments do not establish rank or uniqueness. Background/geometry, repeated reception-time coverage, Born and observer conventions, harmonic extraction and mask/error calibration remain supplied assumptions. Positive candidate primitive gains may be pulled back as H/g after taking adjoints, but are not inferred by this test.

Next obligation: retain both the ray-domain correction and coefficient-envelope contract in any integrated claim, keep the old failed ray interpretation visible, and supply physical observation/background/error inputs before an empirical use.

## Exact author source identities

| File | SHA256 |
|---|---|
| KINETIC_PRIMITIVE_PHOTON_DERIVATION_v1.md | 1979979683f09637d1fe66240af81a52bbfa99aa2815eec9d7f768a0b6361c68 |
| KINETIC_PRIMITIVE_OPERATOR_PROBES_v1.md | 689289b78aa523162b9337d9395155f47616d37ddc4e7cfa25c6f8f04b62b5b9 |
| check_kinetic_primitive_photon_v2.py | aeaff17b7fedd682c2b633301b4e28ad7fe5e9a3f3d9edd3f6c5c5cdb74763ab |
| KINETIC_PRIMITIVE_PHOTON_CONTROLS_v2.json | b5a7fec2f246701d2be20f06abe042c2e4c5ef46ade7066774e5ef7a2bc5d7f1 |
| check_kinetic_primitive_photon_v3.py | 91a61402aa8ab2b94c7d5ee424aba66ecf1cb0d85c08274f6444a4fc9254b063 |
| KINETIC_PRIMITIVE_PHOTON_CONTROLS_v3.json | fc0ddaa78b802ab6753099f2c2cfcb8841153d6b24152033c340fe32560450c3 |
| KINETIC_PRIMITIVE_ANGULAR_ERROR_CONTRACT_v1.md | 7fecf447b1c9a51395dfe243d640edfb94709347983306c4c21e98201cfafea4 |
| KINETIC_PRIMITIVE_RAY_DOMAIN_CORRECTION_v1.md | d16da374f6b5dc545c3548595351fe539a4d8ad0b3d24d21abfcd2673b5e451a |

Exact source snapshots, byte counts, read bindings, closure check and all owned evidence are bound by `POST_EXPOSURE_MANIFEST_v1.json`. No canonical milestone source, Git state, external application or unrelated artifact was changed.
