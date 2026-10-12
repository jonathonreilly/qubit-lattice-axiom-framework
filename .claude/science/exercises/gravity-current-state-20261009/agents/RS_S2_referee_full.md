# Lane RS probe S2 — independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

The momentum-only bounded FAIL is confirmed for the stated staggered-QED Born class, but only for perturbatively analytic charges whose local or exponentially quasi-local density gives a regular analytic one-particle symbol and whose required taste slope is genuinely universal, b_j times the identity. The worker overstates three auxiliary points: the light-cone inequality is a same-sign-band statement, invertibility plus a trace does not classify traceless matrix charges, and the photon “open neighbourhood/no regularity” chaining proof is false as written. The Z2 extension remains conditional and is not part of the confirmed FAIL. This is a momentum verdict only, as required by `TESTS.md:914-918`.

## Findings

### 1. Light-cone inequality — correct for equal-sign bands, false for opposite signs

Let Q = k − k′ + πn modulo 2π, with each n_i in {0,1}. Then sin(k_i − Q_i) = (−1)^n_i sin(k′_i). The vectors a = (sin k,m) and b = (sin(k−Q),m) therefore have norms ε(k) and ε(k′). The reverse triangle inequality and

```text
|sin k_i − sin(k_i−Q_i)| = 2 |cos(k_i−Q_i/2) sin(Q_i/2)|
```

give |ε(k)−ε(k′)| ≤ ||a−b|| ≤ ω(Q). This is exact for every taste shift, for m = 0 and m > 0, and for both positive-to-positive and negative-to-negative bands (`S2_report.md:29-34`; `s2_core.py:13-17`; `S2_referee_checks.py:14-31`). Equality is confined to exceptional/forward sets of measure zero on the regular d = 2,3 shell.

It is false for opposite signs: at Q = 0 and k = k′, |(+ε)−(−ε)| = 2ε > 0. Explicit massive and massless examples are in `S2_referee_checks.out:5-6`. Thus “no same-band transverse exchange pole” is correct, while O(e) band-changing pair poles remain, consistent with the independently confirmed K3a resonances (`K_K3a_referee.md:9`).

### 2. Born reduction — correct as a necessary regular-shell condition, with an O(e) qualification

On a degenerate free two-electron shell, the matrix element of [H0,Q2] vanishes. Solving the nonresonant part of [H0,Q1] = −[V,Q0] leaves the second-order condition

```text
(P̃3⊗1 + 1⊗P̃4) T = T (P̃1⊗1 + 1⊗P̃2),
```

with the direct-minus-exchange Coulomb and transverse Born terms implemented at `s2_core.py:72-103`. This is the same necessary asymptotic obstruction—not an equivalence to a local conserved charge—identified by the L2 referee (`RN_L2_referee_full.md:33-60`), and the worker scopes it that way at `S2_report.md:48-52`.

The claim that all Q1 denominators do not vanish is too broad (`S2_report.md:43-45`). Equal-sign electron-emission denominators do not vanish, and pair intermediate states reached from the two-electron sector cost energy; globally, however, the K3a photon↔pair resonances exist. There the O(e) equation imposes the extra compatibility condition P_E[V,Q0]P_E = 0. A smooth local perturbative charge has no freely resonance-supported homogeneous Q1 kernel that can cancel the regular two-electron Born condition. The O(e) equations therefore add constraints; they cannot restore a slope removed by Møller scattering.

### 3. Trace lemma — exact trace consequence, not a full matrix collapse

For Møller scattering, all one-particle spaces have dimension n_+, and

```text
Tr(P3⊗1 + 1⊗P4) = n_+ (tr P3 + tr P4).
```

Similarity through invertible T therefore gives exactly f1 + f2 = f3 + f4 for f = tr(P)/n_+. For Compton scattering, with dimensions n_+ and n_γ = d−1, the trace is n_γ tr(P) + n_+ tr(g), so the normalized equation is f + γ̃ = f′ + γ̃′ with γ̃ = tr(g)/n_γ. The factors were independently checked at `S2_referee_checks.py:50-62` and `S2_referee_checks.out:13-15`.

The lemma does not collapse a matrix charge to its trace: traceless intertwiners remain logically possible. It suffices only to exclude a slope proportional to the identity. Also, a real-analytic determinant nonzero somewhere is nonzero almost everywhere only on each connected analytic component where it is not identically zero. The worker did not establish all components (`S2_report.md:58-60`), so the random minima 6.5e−5 and 4.9e−6 are evidence, not a global theorem.

I found exact-energy, nonzero-total-momentum shells whose T matrices are well conditioned in every stated d,m, with singular-value ratios 0.20–0.69 (`S2_referee_checks.py:90-108`; `S2_referee_checks.out:20-23`). This supplies a robust open invertible patch. For analytic local or exponentially quasi-local symbols, the standard local collision-invariant argument gives f = a + b·k + cε on that patch; analytic continuation and period π force b = 0. This does not prove the worker’s larger claim for arbitrary merely C1 symbols on untested shell components.

### 4. Staggered dispersion and tastes — identity exact; massless Spohn scope corrected

The identity ε_stag(k) = ½ω_KG(2k;2m) is exact (`S2_report.md:64-68`; `S2_referee_checks.out:7-12`). The map q = 2k is a bijection from the reduced period-π torus to the ordinary period-2π torus, sends momentum conservation modulo π to conservation modulo 2π, and preserves the collision energy equation up to the common factor ½. Taste corners become the internal n_+-fold degeneracy at the same reduced momentum; they do not create extra scalar invariants.

The worker is too pessimistic about m = 0 (`S2_report.md:70-71,164`). Spohn’s hypothesis allows a codimension-at-least-one nonsmooth set. Massless lattice KG has isolated zeros, and its Hessian determinant is not identically zero: at q = (π,…,π), Hess(ω) = −I/(2√d), with nonzero determinants recorded at `S2_referee_checks.out:9,12`. Thus, if the scalar collision equation holds almost everywhere, Spohn gives aω + c for m = 0 too. The open-patch analytic argument in Finding 3 is enough for the fixed local/exponentially quasi-local class without assuming global shell connectivity.

If the required slope is b_j times the identity, its trace slope is n_+b_j; zero averaged slope forces b_j = 0. A traceless slope such as diag(b,−b,…) could survive the trace lemma even if all eigenvalues have equal magnitude. It is not taste-universal in the fixed PASS sense, which requires the same momentum action on every taste (`TESTS.md:914-916`). The finite matrix runs find no such survivor at their tested massive ranges, but do not prove its absence at arbitrary range or m = 0.

### 5. Compton and the photon slope — trace step correct; chaining proof overstated

Given invertible T_C, the normalized Compton trace equation is correct. With f = a + cε, energy conservation makes h(p) = γ̃(p)−cω(p) constant on each Compton-connected component (`S2_report.md:82-88`; `s2_compton_lib.py:4-22`). What is not proved is the asserted connectivity.

“Forward-near Compton reaches an open set around every p” is false for m > 0. Along a soft axial photon, an infinitesimal outward radial endpoint would require an electron velocity component equal to the photon velocity. At m = 0.5 and p_x = 0.05, sup|v_e,x| = 0.6180 while v_γ,x = 0.99969 (`S2_referee_checks.py:135-145`; `S2_referee_checks.out:26`). A full neighbourhood is therefore not reachable, and the stronger “no regularity needed” claim is unsupported.

The numerical conclusion is strong: the supplied massive Compton null spaces reproduce, and fresh m = 0 runs—missing from the worker packet—give zero joint and photon-only nullity with smallest singular values 0.14–0.34 (`S2_referee_checks.out:24-25`). For analytic photon symbols, a mixed-species local collision-invariant theorem or an explicit Compton-graph proof would repair the argument. Until then, “photon slope forced to zero for any polarization matrix with no regularity” is checked/conditional, not proved. This does not undo the fixed QED FAIL because Møller already forbids the required taste-universal fermion slope.

### 6. Numerics — reproduced and robust for finite matrices, not an all-range proof

I reran every supplied scalar, matrix, joint-matrix, Ward, resonance, and 1D control at the recorded sizes. All outputs reproduce, including the 2,000-parameter 3D r = 2 matrix run. Fresh-seed Møller tests retain zero scalar nullity with smallest singular values 0.55–0.61 (`S2_referee_checks.out:16-19`); fresh-seed matrix runs retain two represented survivors and slopes below 2.2e−11 (`S2_referee_checks.out:27-29`). The free-momentum, permutation-only, one-dimensional, and Ward controls behave as reported (`s2_control1d.out:1-9`; `s2_ward.out:1-12`).

The finite-matrix nullities are stable, but the gap description needs correction. The d = 2,r = 4 relative gap is about 6e−6, only 6e3 (3.8 decades) above the 1e−9 relative threshold; the fresh joint gap is 4.0e−4, about 5.6 decades above threshold (`S2_referee_checks.out:27,29`). These gaps are ample for the sampled finite null spaces, especially with fresh seeds, but are not order-one relative gaps and cannot support r→∞ or exponential-tail extrapolation by themselves. The random row sketches at `s2_matrix.py:46-49` and `s2_matrix_compton.py:42-63` are probability-one numerical devices, not exact certificates.

There is also a locality caveat in the joint photon ansatz: it parametrizes the number-basis symbol g = E_perp^T M(p) E_perp by trigonometric M (`s2_matrix_compton.py:26-37`). As written, this contains photon number but not the local Maxwell-energy one-photon symbol ω(p) times the identity. Its two survivors therefore do not classify every canonically local quadratic photon charge. The trace argument is broader and is the relevant route for a universal photon slope.

### 7. Z2 reduction — not confirmed

The report itself makes this conclusion conditional on generic invertibility and excludes confined/nonperturbative regimes (`S2_report.md:147-152`). A gapped deconfined gauge sector can generate exponentially local effective interactions after it is integrated out, but the gauge constraints, topological sectors, leading two-body amplitude, and its rank still require derivation. No Z2 amplitude or null space was run. The correct statement is conditional: if a controlled deconfined reduction produces a nonzero generically invertible two-fermion T on a suitable open collision patch, the same trace/dispersion obstruction applies. No bounded Z2 FAIL is established.

### 8. Fixed-reading verdict and remaining loopholes

The fixed FAIL asks only about momentum and is bounded to the interaction class (`TESTS.md:914-918`). For noncompact staggered QED at Born order, the required taste-universal slope is excluded: the regular-shell Born condition is necessary; a well-conditioned open Møller patch exists for every stated d,m; its trace gives the scalar collision equation; and analytic locality plus the exact KG map removes the odd trace slope. Pair channels add constraints. The momentum-only QED FAIL is therefore not rendered INCONCLUSIVE by the missing global component check.

Remaining open routes are: merely C1 but nonanalytic symbols beyond the local/exponentially quasi-local class; power-law-tailed or otherwise nonlocal momentum; nonanalytic-in-e, strong-coupling and infrared-dressed constructions; traceless taste/polarization slopes, which do not meet strict taste universality; a rigorous all-component photon-connectivity theorem; and the uncomputed Z2, compact-confining, or other nonperturbative gauge regimes. The result also does not classify charges whose leading one-particle action vanishes or prove a stress/first-class gravitational completion, neither of which is needed for this fixed FAIL.

## Strongest correct statement

For d = 2,3, m = 0,0.5, and noncompact staggered QED in Coulomb gauge through the regular O(e²) Born sector, any conserved charge analytic in e whose local or exponentially quasi-local density has a regular leading one-fermion symbol and a taste-universal momentum slope b_j times the identity must have b_j = 0: the exact same-sign staggered/Yee light-cone inequality removes normal transverse poles, the on-shell commutator gives the necessary Møller intertwiner, a robust open set has invertible T, its correctly normalized trace is a scalar staggered collision invariant, and the exact q = 2k lattice-KG identification plus analytic periodicity removes its odd slope (for m = 0, Spohn’s allowed-singular-set hypotheses also apply once an almost-everywhere collision equation is available). The reproduced finite-basis calculations strongly support zero polarization-averaged photon slope as well, including fresh massless Compton runs, but the worker’s no-regularity Compton-connectivity proof is incomplete; traceless equal-magnitude taste slopes are not excluded analytically but are not taste-universal; and no Z2, strong-coupling, nonanalytic, power-law-tail, or nonperturbative gauge no-go is established. Thus the FIXED reading is a bounded **FAIL for the specified QED momentum question**, with these corrections, not a broader no-go.
