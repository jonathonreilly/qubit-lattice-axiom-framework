# Primary-literature applicability ledger

Requested during this bounded review. These are independent source reads,
not an exhaustive literature survey or a priority claim. No external theorem
is silently added to the premises of FC1–FC20. The owned filename replaces
the skill's generic literature/import filenames because the coordinator
explicitly restricted this review's writable paths. Download identities and
failed retrievals are preserved in the `review_residual_full_colour_literature_download*.json`
files; the source manifest records exact PDF page coverage.
The complete PDF snapshots are local-only inputs and must not be staged or
republished; no license for that use has been verified. The commit-ready
evidence is this original analysis, source metadata and hashes.

| Reviewed block | Primary source and exact item | Hypotheses, applicability and import class |
|---|---|---|
| Neutral finite coefficient, FC1; finite-part consumer FC17 | Adams–Lee, [Structure of logarithmically divergent one-loop lattice Feynman integrals](https://arxiv.org/abs/0709.0781), §II, Eqs. (7)–(15), main decomposition (1), and p.13 | Smooth scaled numerator/denominator, finite homogeneous continuum limits, nonnegative denominator, continuum ellipticity, doubler-free zero-external denominator, and infrared finiteness. The logarithm and continuum momentum dependence are universal while a finite polynomial can depend on the lattice action. This does not imply a neutral finite coefficient is zero and supplies no n-uniform bound on our finite parts. **Background context; theorem not imported.** |
| Actual lattice Ward structure and one-loop matching, FC10–FC17 | Lüscher–Weisz, [Background field technique and renormalization in lattice gauge theory](https://arxiv.org/abs/hep-lat/9504006), §6 Eqs. (6.5)–(6.12), (6.18), (6.24)–(6.25); §7(a)–(e), §8 Eq. (8.1) | Wilson lattice theory, formal perturbative renormalization, BRS/background-gauge/shift symmetries, continuum limit at nonexceptional external momenta. The lattice BRS and shift relations underpin matching after finite renormalizations. Our soft-kernel determinant, periodic constant-mode prescription and depth dependence are extra data. The paper does not identify our finite-volume Taylor regulator with a nonlinear stabilizer integral. **Background context; not a replacement for FC14–FC16.** |
| Gauge-profile change in FC9 and the charged predecessor | Iguri–Mazzitelli, [Gauge-fixing independence of test fields in Yang–Mills theories](https://arxiv.org/abs/hep-th/0107095), Eqs. (13)–(14), (25)–(29) | BRST-exact gauge fixing and invariant quantum measure yield an equation-of-motion identity; classical fields add another term. Gauge independence does not follow off shell merely from naming a Nielsen identity. FC9 instead has the exact neutral row `H_W d=0`; the charged source explicitly retains its nonzero row. **Non-derivation analogy; no new analytic estimate imported.** |
| Harmonic/gauge completion FC3–FC9 and possible uniform linear producer | Dimock, [Covariant Axial Gauge](https://arxiv.org/abs/1410.2798), Proposition 5/Eqs. (75)–(84), Proposition 6/Eqs. (86)–(88), Proposition 7/Eq. (140) | Abelian gauge field, hard block constraint, covariant axial gauge; Prop.6 assumes `QA=0`, `tau A=0` and gives a lower bound independent of N,k, depending on L. Prop.5 identifies the gauge projection on `Delta ker Q`; Prop.7 relates the fluctuation covariance to a constrained Green operator. The paper works chiefly in d=3 and discusses dimension extension; it does not supply the root-evaluation/soft-S4′ dictionary or our periodic harmonic normalization. **Literature theorem candidate, not invoked as a premise.** |
| Curvature-controlled interpolation and FC19 | Dimock, [Multiscale block averaging for QED in d=3](https://arxiv.org/abs/1712.10029), §3.1 Eqs. (189)–(204), §3.7 Eqs. (284)–(303), Theorem 1/Eq. (327) | Nested small-field regions, hard multiscale averaging, earlier boundary data in axial gauge, sufficiently large M, weights satisfying `p_j'/p_j <= L^abs(j-j')`. Theorem1 gives a local gauge representative bounded by coarse curvatures with d=3 scale factors, constant depending only on L. Eqs. (291)–(303) give Green/minimizer random-walk bounds. These are concrete techniques for a uniform producer, but FC19 asks for d=4 weighted row **and column** bounds for a finite-kappa soft stationary chain. **Literature theorem candidate; missing normalization/domain/comparison proof is explicit.** |
| Alternative covariance infrastructure for FC19 and later flow | Brydges–Guadagni–Mitter, [Finite range Decomposition of Gaussian Processes](https://arxiv.org/abs/math-ph/0303013), Theorem 1.1 and Theorem 5.5/Eqs. (5.10)–(5.11) | Scalar resolvent on Z^d, d>=3, nonnegative mass, sufficiently large dyadic L. Positive finite-range pieces have rescaled Fourier/Sobolev bounds uniform in scale. Our L is odd and our gauge/soft-chain inverse is a different operator. Even at the free point, replacing its covariance by this decomposition needs an exact comparison or a changed construction. **Non-derivation analogy/possible tool, not an imported FC19 proof.** |
| Nonabelian uniform background RG and nonlinear small-field flow | Bałaban, [RG approach I](https://doi.org/10.1007/BF01215223); [background propagators](https://doi.org/10.1007/BF01240355); [variational/background fields](https://doi.org/10.1007/BF01229381) | Publisher metadata/abstract and bibliography were located; direct full-paper attempts returned access HTML or errors. The first abstract expressly restricts the construction to the four-dimensional small-field approximation. **Bibliographic lead only. No theorem numbers, detailed hypotheses or imported closure are claimed from unread text.** |

Each row uses its source only for the stated comparison or candidate tool;
none provides derivation closure for FC19, the full nonlinear flow, continuum
OS existence, or the physical Hamiltonian gap in the supplied construction.

## A concrete dictionary to pursue, derived from the actual contour definitions

This is an independently checked dictionary already present in
[FLOW §89](../FLOW.md), in its RFL11-fix S11-7 paragraph; it is not new
science or an imported Dimock theorem. In the present unit's integrated-link convention define
`Q_str a(X,mu)=L^-4 sum_y integral_(y->y+L e_mu) a` and
`alpha_X(a)=(24 L^4)^-1 sum_(sigma,y) integral_(X->y along sigma) a`.
The two endpoint paths in each adopted contour telescope on averaging:

`Q_S4prime a = Q_str a - d_c alpha(a)`.

Thus `d_c Q_S4prime = d_c Q_str`. On a scalar gradient,
`alpha(d lambda)=blockavg(lambda)-ev(lambda)`, which gives precisely
`Q_S4prime d=d_c ev`. This identity holds with the stated winding convention
because the two endpoint path families are translates of the same family.
Dimock's Eq. (189) uses an additional division by the coarse edge length:
in d=3 his `L^-4` is volume averaging `L^-3` times `L^-1`; the present d=4
integrated-link `L^-4` is volume averaging alone. Equal printed exponents
must therefore **not** be treated as equal normalization conventions.

This yields a useful first bridge for curvature estimates without replacing
the nonlinear averaging map. It is insufficient by itself: the soft penalty
depends on the whole mismatch, the minimizer's gauge choice must be tracked,
and its finite-kappa Hessian is not the hard constrained minimizer. A viable
next result would prove a gauge-compatible resolvent comparison, then transfer
the published derivative/locality estimates into the actual `r_j`, `z_j,T`
and `f_0` row/column norms. The necessary strict factor `theta<1/L` must be
proved after every rescaling and level sum. This is a constructive candidate,
not a claim that such a comparison has been completed or that other routes
are exhausted.

FC2/FC18 themselves are a Taylor expansion and stationary substitution for
the supplied normalized density. The literature above supplies neither those
model-specific quartic coefficients nor license to discard their neutral
parts. Those formulas are independently derived and directly tested in this
review. FC20 is the elementary anchored product estimate under FC19; no
external result is needed to turn that explicitly conditional implication
into a proof.
