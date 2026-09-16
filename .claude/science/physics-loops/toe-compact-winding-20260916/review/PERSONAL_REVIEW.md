# Personal mathematical review and verification limits

This is the sole author's review, not independent acceptance. All three
current notes and three primary Python sources were read. The following
load-bearing arguments were checked analytically before packaging.

## Sparse current law

The original side4 enlarged boxes were disjoint but could be Chebyshev
adjacent. Cold review caught this after the original finite check passed.
The old note, program and successful output are preserved. Side6 blocks
with central coordinates2/3 now separate enlarged boxes by at least3;
the strengthened finite check excludes adjacency as well as overlap. Joint vertex events require at least ceil(n/4) independent
activations after conditioning on all geometry/sign variables. The full
sign environment is ergodic: the diagonal block shift mixes all24 sequences
and the iid marks simultaneously. The initial longer coordinate-by-coordinate
argument was replaced by this direct cylinder proof. The random-origin
extension is stationary and ergodic under fine translations. Reflections
act on orientations and on the uniform interior offsets, not just locations.

The diffuse filling sum separates into a product of four normalized sign
sums and conditionally independent centered Bernoulli noise. Uniform
conditional characteristic convergence supplies independence in the limit.
Pairwise orthogonality controls both the covariance and the physical-window
and smooth-test errors. The exact fourth moment independently confirms the
78rho^4 cumulant. The exponentially rare all-plus sign environment suffices
to make the real MGF diverge; it is not inferred from weak convergence.

No claim that this law violates a separately checked Hamiltonian DLR equation
is made. Its representation as that law was never supplied. Its observable
is a specified local filling, not the conserved current against a constant
edge source and not the Hamiltonian magnetic field.

## Compact cover and source calculus

The Haar factor is compensated at every trace integration. The integer
increment map is bijective; intermediate translates tile real space while
the initial fundamental cell and final winding remain. The source definition
of the bridge action is included explicitly, avoiding a hidden dependency
on PR8166. Principal flux retains its integer branch correction. Nonlinear
background derivatives retain contact terms and normalized mixture cumulants.

The free-circle Hessian can be negative near the antipode even though each
lift is convex. This is a mixture check, not a fixed-g thermodynamic no-go.
The static magnetic Ward identity uses h=Cu. Its first spectral moment
retains cos(B) inside C*, so a previously failed local Gram comparison is
not reused. Full thermal and physical Gauss-projected traces are distinct.

## Actual compact sine score

The electric Dyson expansion has nonnegative coefficients before source
phases, and absolute convergence precedes the triangle inequality. The
constant part of the Hamiltonian is kept fixed during the amplitude-phase
replacement. The second bound uses the positive coordinate-path integral,
where cos<=1 is legitimate, rather than an unjustified matrix ordering of
noncommuting exponentials. This proves the claimed actual MGF bound.

The ergodic-component issue matters: a bound known for finite zero-background
traces is not silently inherited by every component. The static curl proof
instead obtains its own weaker exponential bound directly from the local
shift identity, sufficient for the Gaussian limit. Its factor4 in the tilted
Cauchy-Schwarz remainder comes from half the cubic remainder at2t. Contact
concentration is L2, not an unsupported replacement of a random quadratic
term inside an exponential. Weighted ergodic averages and the lattice-curl
Taylor error are controlled separately. A deterministic variance and its
positivity are consequences/premises exactly as stated; nondegeneracy is
not inferred from ergodicity alone.

The result is finite-temperature, static-curl and sine-score specific. The
independent gapped rotor comparison is deliberately retained to prevent
misidentifying Gaussian fluctuations with a photon pole.

## Reproduction and finite evidence

Run from repository root:

```sh
python3 .claude/science/physics-loops/toe-compact-winding-20260916/evidence/sparse_loop_counterexample_check.py
python3 .claude/science/physics-loops/toe-compact-winding-20260916/evidence/compact_cover_source_check.py
python3 .claude/science/physics-loops/toe-compact-winding-20260916/evidence/compact_score_check.py
python3 .claude/science/physics-loops/toe-compact-winding-20260916/evidence/run_formula_faults.py
```

The sparse checker tests18432 oriented symmetry cases and exact finite-law
moments by both ordered sign monomials and conditionally independent binomial
sums. It does not sample a Hamiltonian or numerically prove ergodicity.

The cover checker compares image/Fourier kernels and three derivatives at
120-digit precision, including antipodal cancellation; it separately checks
free traces. Compact one- and two-plaquette Hamiltonians test the physical
kinetic metric, unitary source translation, inverse spectral Ward moment
and double commutator. Padded Fourier multiplication retains cutoff leakage
in the separate cosine-gradient calculation.

The score checker builds an actual2x2 oriented plaquette complex and its
three-coordinate, zero-harmonic electric sector. It compares a direct sine
source with a separately assembled amplitude/phase Hamiltonian, checks the
unphased partition domination and the exact-source Ward identity, and keeps
a nonexact source whose Ward contact does not equal its variance. It checks
the full finite-temperature Duhamel sum, not an equal-time variance.

The first Fourier cutoffs2/3 failed the predeclared maximum MGF refinement
criterion0.003: the largest change was about0.011026. The exact failing
source/stdout/stderr are preserved under initial_score_refinement_failure.
Cutoffs3/4 pass the SAME criterion, with changes about0.00280414 and
0.000003624 at the two parameter pairs. These are finite convergence checks,
not certified tail bounds. An initial diagnostic command failed only while
writing its result because an array shadowed a path variable; the corrected
diagnostic retains the actual cutoff data. No scientific threshold changed.

The independent-rotor comparator keeps a positive single-site gap while
its diffuse sum approaches the Ward Gaussian MGF. At4096 copies the two
tested differences are about2.34e-6 and6.77e-8. Those copies do not increase
the interacting lattice's volume or supply its phase.

Nine actual formula faults are rejected: loop orientation; sign environment;
fourth-moment coefficient; Haar normalization; winding cubic sign; ground
Ward factor; score phase sign; thermal time measure; and the exact-curl
premise. The last fault fails the thermal Ward assertion before reaching
unitary conjugacy. Every changed source and actual stderr is preserved.

## Independent-review priorities

Verify the conditional product-noise limit and symmetry/ergodicity of the
sparse construction, then the positive trace domination and the local Gibbs
shift application in the score theorem. The physical source and state
restrictions are part of the claim, not optional caveats. Canonical packets,
formal negative-claim submission where applicable, independent review and
integrated landing gates remain pending.
