---
claim_id: lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_bounded_theorem_note_2026-10-21
claim_type: open_gate
claim_scope: "Finite square-root branch tracking, endpoint derivative and quadratic-kernel diagnostics on supplied Kuhn and coned D4 carriers; source/action sign comparisons are conditional, and full nonlinear action reality, continuum EH matching and the null limit remain open."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_2026_10_21.py
---

# Lorentzian Regge endpoint diagnostics and conditional sign comparisons

Claim type: open_gate. The historical filename and claim identifier are retained for recovery, not theorem status.
Primary runner: `scripts/lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This packet tests supplied carriers and metric/source conventions. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) select neither those carriers, a continuum Einstein-Hilbert action, a source action nor a geometry-phase sign. No candidate-law identifier supplies the absent physical bridges.

## Finite continuation and endpoint checks

For g=diag(1,1,1,alpha exp(i phi)), alpha=.6, the fourth index is the supplied tick coordinate. The runner tracks the nearest square-root branches of hinge/dual/simplex determinants over 600 equally spaced phi values from 0 to pi. It computes area and dihedral-angle derivatives only at the endpoint, not absolute dihedral angles, absolute deficit branches or a full nonlinear action. Endpoint simplex square roots are +i times their magnitudes. Endpoint Schlaefli relative residuals are approximately 3.0e-16 (Kuhn: 15 edge and 50 hinge classes) and 3.7e-16 (coned D4: 72 edge and 208 hinge classes). No whole-path Schlaefli verification is claimed.

Causal hinge type is determined by the induced two-dimensional metric: negative determinant means timelike; a positive definite induced metric means spacelike. Degenerate hinges are excluded from these endpoint fixtures. Tick components alone do not decide causal type. The explicit Kuhn triangle with vertices 0,(1,0,0,1),(1,1,0,1) has Gram [[.4,.4],[.4,1.4]], determinant .4>0 and real area sqrt(.4)/2 despite tick components. An integer-scaled Gram control preserves this counterexample.

At the endpoint, timelike areas are +i|A|, while spacelike areas are positive real. Central-difference comparisons of the endpoint derivatives with real rotation/rapidity formulas have maximum relative errors about 5.0e-8 and 5.6e-7 for the timelike wedges; the sampled spacelike derivative signs are reported by wedge type. These derivative checks do not determine absolute deficit branches or prove a full real nonlinear S_L. S_L below denotes the proposed continued action divided by i, whose candidate quadratic kernel is tested.

## Sampled quadratic comparisons

For four seeded perturbation/momentum pairs per carrier, two scales .04 and .02 give Richardson ratios of the continued quadratic kernel against the supplied EH/2 comparator near 1.00000, with sampled imaginary-to-magnitude fractions below 2e-13. The acceptance thresholds are 2e-3 on the extrapolated ratio and 1e-9 on that fraction. Opposite continuation directions agree after division by +/-i at one additional sampled momentum per carrier, to about 2.4e-16. Flipping the spacelike-hinge contribution gives comparator ratios about -1.243 and -3.362 for those fixtures. The Euclidean Kuhn check is likewise a single sampled Richardson ratio.

At alpha=1.7,.99,.999, one further fixed perturbation/momentum pair yields ratios near 1.00000 (threshold 3e-3). The output preserves increasing individual hinge coefficients. These three values do not establish the alpha->1 limit; alpha=1 has degenerate hinges and is outside the calculation. Neither these tests nor the parent Euclidean diagnostics establish continuum equality or a full real action.

## Conditional source/action sign comparison

Supply P=-S and S_total=-sigma*kappa*S_L-E integral d tau, with E,kappa>0, the squared-length metric reading, and proper-time coordinate t'=sqrt(alpha)t. Numerics use E=kappa=1. The source expansion supplies J_tt=E/sqrt(alpha); the static response uses the displayed pseudoinverse equation. These are conditions, not framework-axiom consequences.

For three directions at |k|=.02 and sigma=-1, h_00 k^2 is near +E/kappa, and gamma=P_ij h_ij/(2h_00) is near 1. For sigma=+1 the static response reverses sign; gamma stays unchanged because both its numerator and denominator reverse. The runner checks this invariance directly and prints both sign results. Four sampled TT quadratic values at omega/(sqrt(alpha)k)=0,.5,1,1.5 show the sign change and near-null value under the same action convention. This diagnoses a quadratic kinetic sign; it does not calculate binary-pulsar decay or test-body light bending. Interpreting positive h_00 as attractive additionally uses the supplied metric/geodesic reading. Comparing to attractive gravity favors sigma=-1 only within those choices, rather than deriving a bare sign from the axioms. No global physical exclusion of the opposite sign is asserted.

For coned D4, sigma=-1, the 20^3-torus response is fitted to a lattice Green function plus a constant over 4<=r<=8. The fitted coefficient G=0.03942 is compared with 1/(8*pi)=0.03979, with relative residual .047. This is a finite fit with supplied source normalization, torus and radii. It is not a measured physical Newton constant.

If one additionally assumes continuum S_L matches EH/2 with lattice spacing a, coefficient matching gives -sigma*kappa/(2*a^2)=1/(16*pi*G). For sigma=-1 this yields G=a^2/(8*pi*kappa). Continuum matching, metric/source coupling and positive kappa are explicit extra conditions; the finite ratios do not discharge them.

## Reproduction and unresolved obligations

Run `python3 scripts/lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_2026_10_21.py` under its 120-second aggregate cap. RNG seeds 11 and 3, all original sample order, numerical formulas and diagnostic thresholds remain unchanged. The new gamma comparison uses rtol=atol=1e-10; the causal fixture uses exact integer Gram entries. Endpoint square-root/Schlaefli tolerances are 1e-9, area-component tolerances 1e-12, rotation-derivative relative tolerance 1e-6 and rapidity-sign tolerance 1e-3. Static/gamma comparator tolerance is 3e-3; near-null TT tolerance is 1e-3 times the zero-frequency magnitude. Static pseudoinverse cutoffs are 1e-8 (directions) and 1e-7 (torus); fit tolerances are 3% and .05 residual. The declared D4 helper is a contextual combinatorics pin and is not imported or executed.

Open obligations: whole-path/absolute-angle branch control, full nonlinear action construction/reality, continuum matching and null-limit behavior, and physical source/geodesic identification. No empirical value, Planck identification, nonlinear field equation or adopted law is established. Original three files, assertions and output remain recoverable at Git head 10c46a28d0fcf2b4ee7de924703aa030246e0e27; the repair preserves diagnostics and counterexamples while narrowing their interpretation.
