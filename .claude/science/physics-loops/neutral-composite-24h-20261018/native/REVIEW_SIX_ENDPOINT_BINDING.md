# Final focused six-endpoint binding review

Disposition: PASS. No material source fix found. This is a K1 relative-height binding certificate in the supplied boundary sector, not a full-H particle, finite-droplet or ground-state theorem. No shared files edited; no audit or landing performed.

## Breakup bound covers the necessary channels

The new four-column input correctly covers the entire even-multiplicity height sector, not only its flat-connected component. Four even multiplicities mean either all equal or a 2+2 split, giving six full rays plus flat. The seven-state core includes all separation-one swaps. Independent tails beyond it have |t(k)|<=2 and are eliminated exactly at energy -5; no finite-height tail truncation enters the lower bound. The negative tail correction (-5+sqrt(25-4|t|²))/2 is correct.

The interval implementation adds 19/4 to the core diagonal, i.e. certifies M-1/4 I, and uses interval pi, exponentials and square roots. Strict positive interval pivot lower endpoints are checked before division. Explicit real/imaginary conjugation is correct, and conversion to float occurs only after certification for display. Hermiticity follows from the symbolic native graph; the LDL calculation does not need to infer it from rounded values. The independent report includes successful replay of all 15 induced subsets times 257 momenta. Its displayed minimum pivot is not an eigenvalue bound, and neither source treats it as one.

The derivative estimates |t'|<=1, |s'|<=4/3 and ||Hcore'||<=sqrt(6) justify the looser norm bound 8. The maximum grid distance pi/256 leaves a positive margin 1/4-8pi/256. Thus the all-momentum, all-component four-column lower bound -5 supplies exactly the input needed for separated six-column channels. The proof does not generalize it to arbitrary four-column footprints or odd multiplicities.

Global height-multiplicity parity forces separated groups to have even size and even internal multiplicities. Escape therefore has a 2+4 or finer 2+2+2 split. Uniform internal momentum bounds survive the total six-column momentum constraint. The discrete IMS partition on sorted gaps and finite label refinements has bounded edge differences O(1/R), hence bounded-degree form error O(R^-2), including signed hoppings. Large-gap support removes cross-cluster edges exactly. Its interior is finite after common-height quotient. This proves essential spectrum bounded below by -7; equality or channel accessibility is not asserted.

## Exact trial and binding inference

The stored integer trial is explicitly matched to the generated 1459-state order before computing its quadratic form. The model's temporary float sparse entries are exact small integers and are asserted integral before conversion; arithmetic in the numerator and norm uses Python integers. The exact identities are qTq=9999999925139683, qTHq=-71308060208219532 and 10qTHq+71qTq=-3080607397277827<0. Zero extension supplies a valid infinite-component trial irrespective of paths that might leave the cutoff before returning. Its quotient below -7.1, combined with the essential lower bound -7, proves at least one discrete eigenvalue below -7.1. No uniqueness or exact eigenvalue is claimed, and finite-box eigenvalue extrapolation is not doing the proof's work.

## Original-source projection

The physical center for six walls changes by +/-1/3 on pair moves, so the bounded-degree fiber operator is norm analytic locally in momentum. A finite isolated eigencluster below the certified threshold continues with a finite-rank norm-continuous projection. This does not require a nondegenerate eigenvector or a separately proved nonflat dispersion.

The upper-interface distance-two readout has the correct coefficient -4cos(p/2)exp(ip/2) times exp(ipR)D_p, with D_p the sum of six endpoint phases. Uniform bound ||D_p||<=6 and strong convergence to 6I imply norm convergence after the finite-rank source projection. Combining with P(p)->P(0) gives the stated cluster map limit -24P(0), hence a nonzero map at sufficiently small finite momentum. It does not claim a nonzero element between every pair of chosen eigenvectors or a nonzero-frequency transition if the branch were flat.

The source is explicitly unnormalized and restricted to the upper interface. The lower interface of a finite interval contributes separately, giving total zero-momentum excess -48 for six intervals of length at least two. This fixes the otherwise material factor-two ambiguity. At p=0 the projection is constant and has no internal inelastic transition. No vacuum-creation amplitude or observational detector is inferred.

## Scope and evidence

The canonical note consistently identifies the infinite ordered-column/same-orientation boundary sector, uniform exterior, total momentum-zero starting component, and physical first-order energy 12Jz+Jz lambda times the coefficient eigenvalue. Higher orders, paired endpoints, full-H stability, preparation and empirical identifications remain separate. Independent lower-bound, IMS and readout checks were reused, and the actual certifying scripts were inspected. Root reports the successful 5.5023-second source-bound replay; no redundant full interval replay was necessary for this final integration pass.

## Source hashes

- `docs/NATIVE_SIX_ENDPOINT_BINDING_NOTE_2026-10-18.md`: `ca84a4277a8296e76207b85412bd933e1bf7c1049283561fb7d13ea0c48f846f`
- `scripts/native_six_endpoint_binding.py`: `53bb7f1989262b5503257dd21fb66b879144b4a1d4b2d982f92ec09367d1b69d`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_ENDPOINT_BINDING_PROOF.md`: `9bca83bd9986010a752d3d8424c4fdba7bf91a0a50d37ff45c5546328f99331b`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FOUR_ENDPOINT_LOWER_BOUND.md`: `40cd30dd23899f0b8cd7b180431e5b43f8ff3f1ab1a0d8f6ddc69514be37203c`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SIX_ENDPOINT_THRESHOLD.md`: `1bff94644353a0d991b3ae58bb5b09450a4bce4c2b311f725f478428f12e0545`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SIX_READOUT.md`: `8b9bc8ebecee69a5a1b220845f1bd203f9eafa2bc6b5a6ef04a525b865170cd4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_interval_certificate.py`: `911842594553f103f086748cd63708378d2977527f871fd735a07a685e00dac5`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_endpoint_cluster_model.py`: `26ec0511a0ae95baab6112fd1fa5c29c3d6d5d4c0590cbc65c52b33adaf8efb0`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/six_endpoint_integer_trial.json`: `eaf4ad107d22e0c6da9bd1f294667f5766f022e93abb9c61ba60164949e65c6d`
- `outputs/native_six_endpoint_binding/result.json`: `5d7ea4c32f714c97713770a5274473649ee13cf00241713c13c4761440d30a04`
