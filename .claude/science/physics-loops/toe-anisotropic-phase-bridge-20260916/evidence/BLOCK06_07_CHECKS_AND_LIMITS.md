# Personal checks for blocks06-07

These are author checks of scoped formulas, not independent scientific
review, a phase computation, or retained-status evidence.

## Raw-curl source comparison

`block06_raw_curl_counterexample.py`, SHA256
`165e47cec92cdc7228c8df483aebacce99e3c329817672fbe5fc04a7d44ed80c`,
passed its first run. Its paired ATTEMPT1 stdout records all nonzero
edge angles, four raw curls and exact rational coefficients; stderr is
empty. The actual nine-vertex, twelve-edge square has raw curl2pi on one
face while its compact plaquette energy is zero. At m=1/10 its action is
3/5 and the source's claimed bound is(83/200)pi^2, approximately4.095886.
The failure of that inequality is certified with rational arithmetic and
pi>3. No conclusion about the source's final theorem is tested.

## Positive mixture comparison

The pre-metadata `block07_positive_mixture_check.py` has SHA256
`771a38fcb8977d0b6d6743341cc6ea9949ff18b571a7728a95b9ca4e731787d0`.
Its ATTEMPT2 run passed in5.336seconds and stderr is empty. It contains
four distinct finite challenges:

- A radial finite-volume heat equation with centrifugal killing checks
  the Hartman-Watson Bessel transform at a=1,3,12 and nu=1/2,1,2.
  The observation radius is exactly1. At the final resolution1024 the
  largest absolute discrepancy is5.665e-5. This checks a discretized
  heat kernel through a different method from the Bessel formula. It is
  not a rigorous finite-difference error certificate or a proof by grid.
- On the actual six-face, twelve-edge cube, all64 assignments of a
  two-point variance law are summed, at prior bad probabilities.01,.2,.5.
  Every specified bad subset satisfies the product bound, and two
  nontrivial loop characters satisfy the mixture and dilution bounds.
  The tested law is a two-point law, not a numerical integration of the
  Hartman-Watson density. The Fourier current sum runs from-80 to80;
  omitted terms are bounded by a geometric tail starting at exp(-1536)
  from the minimum variance. No statistical sampling is used.
- Circle convolutions at m=4,16,64,256 compare direct FFT convolution
  of von Mises densities with Bessel coefficients and the image-sum
  Villain density. At m=256, uniform errors to Villain are.001094,
  .002191,.003468 for variances.2,.8,2. The FFT/Bessel discrepancy is
  at most3.411e-13. These checks do not replace the uniform Fourier
  domination proof in the note.
- At100-digit working precision, the small-Laplace-parameter cusp is
  checked against K_0(a)/I_0(a) for a=.7,3,10. At lambda=10^-48 the
  relative discrepancy is at most1.184e-17. The infinite-mean statement
  itself follows analytically from the transform and monotone convergence.

The cube includes a direction-of-tilt control. Replacing the correct
partition weight Z by1/Z raises a selected bad probability above its
prior: at prior.2 it becomes.257152, whereas the correct tilt gives
.129381. Dropping or inverting this weight is therefore detectable.
This is a named control, not a formal mutation-suite receipt.

The explicit conservative weak-region bounds are epsilon(50)=.004930,
epsilon(100)=6.076e-6, epsilon(200)=9.230e-12 and
epsilon(400)=2.130e-23. These are evaluations of the analytic bound,
not measured defect probabilities. At a=10 the bound is only1.

## Actual failure and repair

ATTEMPT1 failed the radial check at a=1,nu=1/2,resolution256:
heat ratio.740847952299944 versus Bessel ratio.7406209303345246,
absolute error.00022702196541946051 exceeded the declared8e-5 criterion.
The failed source is preserved as
`block07_positive_mixture_check.ATTEMPT1.py`, SHA256
`99744cc5c25f6462075d123021c8861561b2639bd07205798cbbf74219d75020`.
Its traceback and empty stdout are preserved. Later groups were not run
in that failed attempt.

The separate resolution diagnostic has SHA256
`60a278fc6022ed312a177c3db736b811a2fb30548982bdc843b52c9f35f777e6`
and imports that exact preserved source. It found errors.000915284,
.000455259,.000227022,.000113358,.000056641 at resolutions64,128,
256,512,1024 for the failing parameter pair. The first-order behavior
is consistent with the non-smooth radial derivative r^(1/2) at the origin;
integer orders show second-order behavior in this diagnostic. ATTEMPT2
extends the resolution sequence to1024 and keeps the original8e-5 final
criterion. No assertion threshold was relaxed.

Reproduction: run the named program with python3 from the checkout root,
redirecting stdout and stderr to a new attempt pair. NumPy, SciPy and
mpmath are required for block07; block06 uses only the standard library.

## Final metadata-only refresh

The preceding attempt receipts remain historical evidence. Timeout declarations
were added before packaging, and the mixture docstring was made descriptive.
The complete previous sources are preserved as BEFORE_TIMEOUT_METADATA files.
The mathematical formulas and criteria were unchanged in this refresh.

Current `block06_raw_curl_counterexample.py` has SHA256`823a8a7e989aba461b3522cbd09fc9ae6c30f37fabc57d85a666fced4997f115`;
its `block06_raw_curl_counterexample.FINAL.stdout.json` records a successful rerun with empty stderr.

Current `block07_positive_mixture_check.py` has SHA256`f11c894ca38aac8de32d4b05c5a7998354ac0286f3f9d629a3b2aca7984f512e`;
its `block07_positive_mixture_check.FINAL.stdout.json` records a successful rerun with empty stderr.
