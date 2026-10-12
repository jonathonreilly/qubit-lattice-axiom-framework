# C3 lane D: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

## VERDICT: NOT CONFIRMED

The worker’s `FAIL (bounded)` is not supported.

**Corrected lane verdict: INCONCLUSIVE**, with several useful exact, narrowly scoped no-gos retained. The appended adversarial check is substantially correct, but it overstates the constructions as having an exact finite-density mean and understates some remaining noise/readout qualifications.

## Findings

1. **D-T1 is valid only for a two-marked-event, fixed-fiber kernel.**  
   For an isomorphism-invariant \(F(\Pi;x,y)\in\mathrm{End}(V)\) whose internal matrices do not transform, its mean has only scalar spacetime dependence. If spin covariance is additionally imposed, the mean lies in the Lorentz-representation commutant; either way it cannot contain \(\gamma\!\cdot\!\Delta\). But the headline “any order-only rule” is false: cochain-valued outputs transform through their arguments and escape the theorem. The tilted-chain calculation reproduces such a covariant one-form mean. See [C3_D_report.md:106](<C3_D_report.md:106>) and [C3_D_report.md:418](<C3_D_report.md:418>).

2. **D-T2 proves absence of an intrinsic handedness selector, not absence of the Dirac propagator.**  
   An unoriented order cannot choose a pseudoscalar orientation or distinguish one Weyl handedness from the other. The broader statements “every order-only quantity is parity-even” and “every order-only fermion theory is vector-like” require the same trivial-fiber restriction as D-T1. A Dirac kernel is parity-covariant and contains both chiralities; it is not excluded. See [C3_D_report.md:118](<C3_D_report.md:118>).

3. **“Chirality” is textually present, but a single chiral/Weyl theory is not the registered target.**  
   The fixed reading names the **Dirac** retarded propagator and then says “one cone, chirality” [TESTS.md:538](<TESTS.md:538>). The worker strengthened this to a Weyl target in H4 [C3_D_report.md:82](<C3_D_report.md:82>). Under the fixed text, “chirality” can require the correct massless Dirac chiral-block behavior, but cannot retroactively mean a parity-violating single-Weyl theory. D-T2 therefore does not close the registered target.

4. **D-T3 is sound for finite, nonzero classical marks attached to individual events.**  
   The Palm/invariant-measure argument excludes an equivariantly selected direction, frame, nonzero spinor, finite neighbour set, and hence finite-valency intrinsic cellulation. This agrees with the original BHS theorem’s direction and finite-valency conclusions. [BHS](https://arxiv.org/abs/gr-qc/0605006)  
   It does **not** exclude infinite link collections, relational or gauge-redundant data, cochains, quantum fields, or apparatus-held frames. Class F’s link displacement also uses embedding data and is therefore link-plus-embedding, not pure abstract link data. See [C3_D_report.md:133](<C3_D_report.md:133>) and [C3_D_report.md:424](<C3_D_report.md:424>).

5. **Class E has the correct massless mean in the registered continuum-limit sense and counts as link-only bulk propagation.**  
   For smooth compactly supported \(\eta\),
   \[
   G_\rho(i\gamma\!\cdot\!\partial\eta)
   = (i\gamma\!\cdot\!\partial G_\rho)\eta
   \]
   after integration by parts. Since \(E[G_\rho]\to G_R\), its mean tends to \(S_R\eta\). “EXACT” at [C3_D_report.md:172](<C3_D_report.md:172>) should mean exact factorization through the finite-density scalar kernel—not exact equality to the continuum propagator at finite density. It counts under the literal reading because the bulk rule uses links only, although the spin frame and derivative are supplied by source/detector apparatus.

6. **The Kähler–Dirac 0-form route is a genuine order-only massless escape.**  
   \(dG_\rho\) is an order-complex 1-cochain. In the continuum limit its Clifford image is \(\gamma^\mu\partial_\mu G_R\). The codifferential is irrelevant on the scalar Green-function sector because \(\delta\phi=0\) for a 0-form; it becomes necessary for a complete intrinsic kinetic operator. Chirality projection, unlike \(\delta\), requires a Hodge-star/orientation construction. This distinction is standard in discrete Kähler–Dirac treatments. [Discrete Dirac–Kähler chirality](https://arxiv.org/abs/1411.7673)  
   Thus it counts if the lane admits cochain-valued propagators, as its wording does not exclude them. The price is external Clifford/tetrad readout and, intrinsically, taste/minimal-ideal selection. See [C3_D_report.md:205](<C3_D_report.md:205>).

7. **Neither PASS nor FAIL is presently reached.**  
   Massless noise has a viable controlled route: class E inherits the E1′-b Poincaré bound componentwise, while
   \[
   \operatorname{Var}(\phi(x_0)-\phi(x_1))
   \le(\sqrt{\operatorname{Var}\phi(x_0)}+\sqrt{\operatorname{Var}\phi(x_1)})^2
   \]
   controls the Kähler–Dirac difference, with the expected \(\lambda/\delta\) relative-noise penalty. The report, however, does not complete all constants and physical-bar hypotheses. More decisively, both massive constructions inherit lane M’s uncontrolled massive-scalar noise problem [C3_D_report.md:178](<C3_D_report.md:178>). Therefore PASS is unproved, while the surviving massless routes prevent FAIL.

The negative-claim discipline fails on unclosed alternative routes and resolution conflation: event-valued kernels were treated as if they exhausted link/cochain constructions. In particular, N1, N5, and N7 fail.

## Strongest correct statement

A Poisson causal order cannot, by itself, produce a nonzero finite spinor/frame/direction mark at each event, choose a spatial handedness, or yield \(\gamma\!\cdot\!\Delta\) as the mean of a fixed-fiber two-event matrix kernel. Nevertheless, link propagation of a scalar Green function followed by apparatus differentiation, and the order-only Kähler–Dirac cochain \(dG\), reproduce the **massless Dirac response in mean** in the continuum regime. Controlled massive coherence remains open.

For genuinely chiral event matter, the route must pay for an orientation/chiral selector and a spin/Clifford transport structure. If supplied as finite physical event frames, that sacrifices Lorentz invariance in law; if supplied relationally or as gauge/link/cochain data, it is an additional substrate primitive whose locality, noise, spin connection, and taste reduction must be proved. A parity-symmetric mixture of the two orientations is not enough—it returns a vector-like Dirac mean.

All Python files compiled; the profile moments, independent Monte Carlo summaries, and tilted-chain cochain means reproduced. No files were edited.