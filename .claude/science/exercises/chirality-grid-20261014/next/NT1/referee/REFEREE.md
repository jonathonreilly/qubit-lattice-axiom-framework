# NT-1 independent referee record

## VERDICT: NOT CONFIRMED

The negative matrices are real and have been independently reproduced.  The
failure is at the preceding measure-legitimacy gate: the code constructs a
gauge-restoring phase on the finite open strip by applying a cumulative inverse
divergence to the anomaly.  It does not construct or verify the local current,
lattice-symmetry properties, and global integrability required of a Lüscher
chiral measure.  Indeed the same prescription gauge-restores an anomalous
single Weyl fermion.  Thus the computation establishes non-positivity of a
specific numerically gauge-restored finite-strip weight, and very robustly of
its modulus, but it does not establish `CHI-RP-FAIL` for a legitimate local,
anomaly-free chiral overlap measure as fixed in `TESTS.md:30-33`.

This is not a numerical rejection.  Conditional on accepting the worker's
finite-strip phase prescription as the intended measure, the RP failure is
confirmed with a margin far larger than any observed numerical error.

## Materials and independent work

I read `TESTS.md`, `PREREG.md`, `REPORT.md`, all `scripts/nt1_*.py`, the saved
outputs and kernels, and the K2c report and verdict.  I also checked the
construction against:

- M. Lüscher, *Abelian chiral gauge theories on the lattice with exact gauge
  invariance*, NPB 549 (1999) 295,
  <https://arxiv.org/abs/hep-lat/9811032>;
- D. Kadoh and Y. Kikukawa, *A simple construction of fermion measure term in
  U(1) chiral lattice gauge theories with exact gauge invariance*,
  <https://arxiv.org/abs/0709.3656>.

The latter states the relevant reconstruction conditions particularly clearly:
smoothness, locality, gauge invariance, integrability, lattice symmetries, and
separate treatment of Wilson-line degrees of freedom for global integrability.

I wrote two independent check programs.  `referee_independent_modulus.py`
imports none of the worker's modules, rebuilds the Wilson operator explicitly,
uses the polar formula

\[
D_{\rm ov}=1+X(X^\dagger X)^{-1/2},
\]

rather than `sign(H_W)`, and evaluates the full modulus kernel from
\(|\det D_1|^2|\det D_2|^{1/2}\).  `referee_measure_checks.py` probes the
worker's phase prescription under small, large, and identity-winding gauge
transformations.  Every run used `capped.sh`, two BLAS/OpenMP threads, and one
process at a time.  Peak RSS was 115 MB
(`referee_independent_lt20.out:35`).

## 1. Is this a legitimate gauge-invariant chiral measure?

### Weyl construction and conventions: correct

The overlap and projector conventions are internally consistent.

- With \(D=1+\gamma_5 S\),
  \(\widehat\gamma_5=\gamma_5(1-D)=-S\).  Therefore
  \(\widehat P_-=(1+S)/2\), so a left Weyl field occupies the positive
  spectral subspace of \(H_W\); a right Weyl field occupies the negative
  subspace.  This is exactly what `scripts/nt1_lib.py:97-100,112-125` does.
- For \(S V=+V\), \(D V=(1+\gamma_5)V=2P_+V\), and for \(SV=-V\),
  \(DV=2P_-V\).  Thus the fixed barred rows selected at
  `scripts/nt1_lib.py:100,126-128` are correct.
- Omitting the constant factor \(2^n\) per Weyl determinant in the stored
  logarithm affects only the global normalization, which cancels from the
  normalized RP kernel.  The worker's factorization gate is correspondingly
  correct (`scripts/gates_Lt12_1401.out:3`).
- The charge/chirality content at `scripts/nt1_lib.py:88-89` is genuinely
  chiral, and \(4(1)^2-(2)^2=0\) is the correct two-dimensional perturbative
  U(1) gauge-anomaly cancellation condition.

The polar/SVD step at `scripts/nt1_lib.py:123-125` is also a valid discrete
parallel transport: it chooses the new basis so that its overlap with the old
basis is positive Hermitian.  This supplies a sound straight-ray basis phase
as long as the ray remains in the gapped component.

### Gauge invariance: convergent numerical Ward identity, not an exact finite-run result

The code's current has the advertised divergence.  It defines
\(K(s)=\sum_{r\le s}\sum_x\mathcal A(x,r)\) and assigns \(K(s)/2\) to each
time link (`scripts/nt1_lib.py:75-85`).  An independent random test gives
`max|div k - anomaly| = 5.27e-16`
(`referee_measure_checks.out:25`).

This, together with the scalar phase correction at
`scripts/nt1_lib.py:129-131`, explains why the local gauge Ward identity is
recovered in the continuum path-integration limit.  The sign `s_k=-1` is a
convention consequence and is correctly selected by the Ward-identity test;
the opposite sign is plainly wrong (`scripts/gates_Lt12_1401.out:8-12`).

But “exactly gauge invariant (to 1e-7–1e-8)” is contradictory wording.  The
implemented determinant is only numerically invariant at finite transport
resolution.  The production pools give residuals from `1.57e-8` to `1.13e-7`
(`scripts/T1_Lt12_wgsearch4401.out:2`,
`scripts/T1_Lt20_wsearch1420.out:2`).  My spot check shows convergence with
transport order: for a small random transformation the phase residual falls
to `2.48e-12` at R32, while a unit-size random transformation gives
`4.78e-8`; identity-winding transformations still leave `4.14e-7` to
`9.78e-7` at R32 (`referee_measure_checks.out:19-24`).  These results strongly
support the infinitesimal/connected Ward identity, but they do not turn the
finite arrays into an exactly invariant measure or prove invariance around all
compact-field loops.

### The blocking issue: this is not the Lüscher local-current construction

Lüscher's reconstruction is not obtained by choosing any current whose
divergence equals the anomaly.  The current must be a smooth, gauge-invariant,
**local** axial-vector functional with the required lattice symmetries; its
connection must satisfy local and global integrability.  On a finite periodic
lattice, Wilson-line/toron degrees of freedom require separate treatment.

The worker instead uses the one-dimensional cumulative sum
`np.cumsum(As.sum(2), axis=1)` (`scripts/nt1_lib.py:78`) on an open strip.
This is an inverse-divergence prescription tied to an end of the strip.  No
uniform locality bound, axial-vector/lattice-symmetry proof, or global
integrability proof is supplied.  The registered locality diagnostic did not
close that gap: the anomaly-free 11112 response grows on the far side of the
mid-strip insertion up to `-2.25e-3`
(`scripts/D1p_Lt12.out:2-4`), and the report calls the test inconclusive
(`REPORT.md:71-74`).  Most decisively, the same construction makes the
anomalous L1 determinant gauge invariant to comparable accuracy
(`scripts/gates_Lt12_1401.out:10-12`; `REPORT.md:71-72`).  That is exactly what
a nonlocal finite-volume inverse of the divergence can do, and exactly the
distinction anomaly cancellation is supposed to control in the Lüscher
construction.

The scalar correction is an exact one-form on the chosen real-potential chart,
so the worker's *local curvature* statement is reasonable there.  It is not a
proof of the reconstruction theorem's global integrability on compact link
field space, and Lüscher's periodic finite-volume theorem does not directly
cover this `Lx=2`, open-time geometry.  Consequently the phase is best
described as a **numerically gauge-restored chart prescription**, not as an
established Lüscher measure.

**Item-1 finding:** projector/determinant algebra PASS; numerical connected
gauge invariance PASS-at-resolution; legitimate local/global Lüscher measure
NOT ESTABLISHED.  This is the verdict-controlling defect.

## 2. Hermiticity, the reflection lemma, and the F3/F4 sign

For a reflection-invariant boundary integration, gluing obeys
\(\theta J(a,b,\phi)=J(b,a,-\phi)\).  Hence

\[
\rho(\theta U)=c\,\overline{\rho(U)}
\quad\Longrightarrow\quad
K(b,a)=c\,\overline{K(a,b)}.
\]

A global rephasing makes \(c=1\).  The converse is valid when “for all
witnesses” means a separating class of gauge-invariant bump functions (so the
integrand is determined almost everywhere); it is not implied merely by
Hermiticity on one finite pool.  With that qualification, the worker's lemma
at `REPORT.md:76-84` is correct.

The code does not fill the chiral kernel by Hermitian conjugation: it evaluates
all ordered pairs (`scripts/nt1_lib.py:163-169`,
`scripts/nt1_kernel.py:39-45`).  The stored full-kernel Hermiticity defects are
`3.2e-14` to `8.3e-14` on the two main Lt=12 pools
(`scripts/T1_Lt12_wsearch1401.out:8`,
`scripts/T1_Lt12_wgsearch4401.out:8`) and `6.9e-14` at Lt=20
(`scripts/T1_Lt20_wsearch1420.out:8`).  Thus Hermiticity of the computed
kernels is not an imposed artifact.

The F3 correction is sound.  Removing the constant reflection phase leaves a
twofold sign.  Positivity of the vacuum normalization/diagonal selects the sign
used at `scripts/nt1_kernel.py:79-87`.  A global phase other than the
reflection-fixing choices would destroy Hermiticity; the remaining minus sign
would make every positive diagonal negative.  It cannot make the matrix PSD.
Equivalently, the present matrices have a large positive eigenvalue near
`k=19` or `20` as well as a negative eigenvalue, so multiplying by `-1` remains
indefinite.  The earlier sign bug therefore cannot explain away the final
negative.

**Item-2 finding:** CONFIRMED, with the stated converse qualification.

## 3. Negative eigenvalues, quadrature, and witnesses

### Saved kernels

Reloading the four `*_Zchi.npy` files and diagonalizing their Hermitian parts
gave:

| Pool | `lambda_min` | `lambda_max` | full Hermiticity defect |
|---|---:|---:|---:|
| Lt12 wsearch 1401 | `-1.078276817573e-2` | `2.000805066234e1` | `3.24e-14` |
| Lt12 wgsearch 4401 | `-5.309135956307e-3` | `2.000349932381e1` | `8.31e-14` |
| Lt12 NT-1 search 7401, k=19 | `-9.628784546277e-3` | `1.900752650938e1` | `4.67e-14` |
| Lt20 wsearch 1420 | `-1.143452079483e-2` | `2.001072744515e1` | `6.92e-14` |

These reproduce `REPORT.md:99-107`.

### Independent full-kernel rebuilds

The independent polar-overlap/modulus implementation reproduced every pool I
ran:

| Pool / quadrature | independent `lambda_min` | max matrix difference from saved real Hermitian part | peak RSS |
|---|---:|---:|---:|
| Lt12 1401, n=16 | `-1.078276817573e-2` | `1.60e-14` | 49 MB |
| Lt12 1401, n=32 | `-1.078276817572e-2` | `1.95e-14` | 85 MB |
| Lt12 4401, n=16 | `-5.309135956307e-3` | `1.98e-14` | 61 MB |
| Lt12 7401 k=19, n=16 | `-9.628784546289e-3` | `3.20e-14` | 53 MB |
| Lt20 1420, n=16 | `-1.143452079481e-2` | `3.33e-14` | 115 MB |

Evidence: `referee_independent_modulus.out:28-35`,
`referee_independent_modulus_n32.out:28-35`,
`referee_independent_wg.out:28-35`,
`referee_independent_t2.out:27-34`, and
`referee_independent_lt20.out:28-35`.  The direct gap minima also reproduce the
worker's admissibility gates, including `0.1320` for the retained k=19 search
pool (`referee_independent_t2.out:27`).

This is a stronger numerical check than recomputing a few entries: it rebuilds
the complete real kernel by an independent overlap formula.  It also shows
that the hard-support one-dimensional Gauss-Legendre quadrature is converged
far beyond what is needed for the sign.

### Error estimate

The reported
\(E=k\max(q,q_3,q_{PT},h)+10^{-13}\) is conservative if the maximum really
bounds every entry, by the standard `k * max-entry-error` spectral-norm bound.
But `q3` and `qPT` are measured on only 24 off-diagonal entries
(`scripts/nt1_kernel.py:69-75,90-95`), so `E` is not a rigorous remainder
bound.  “Certified negative” should remain “quadrature-converged negative,” as
the K2c referee already required.

For this result the limitation is harmless numerically.  The full independent
modulus matrices are stable from n=16 to n=32 at about `1e-14`; the path error
only produces imaginary components of `4.5e-8` to `1.37e-7`
(`scripts/T1_Lt12_wsearch1401.out:8-10`,
`scripts/T2_kernel_Lt12_7401_k19.out:8-10`).  These scales are orders of
magnitude below the `5.3e-3` to `1.14e-2` negatives.

### W matching and gauge-invariant witnesses

All four retained pools have exactly matched boundary spatial Wilson angle in
the stored floating-point data.  The independent outputs record
`Wmatch=0.000e+00` and bulk-plaquette margins below 0.55
(`referee_independent_modulus.out:1`,
`referee_independent_wg.out:1`, `referee_independent_t2.out:1`,
`referee_independent_lt20.out:1`).  Fixing the Wilson angle chooses centers of
gauge orbits; the kernel still integrates the crossing gauge degree of freedom.
As in K2c, continuity and the nonzero gap/margin let the point-orbit matrix be
approximated by smooth gauge-invariant bump witnesses without changing the
sign.  Thus the witnesses meet the fixed W-matched, gauge-invariant condition.

**Item-3 finding:** numerical negativity CONFIRMED; `E` is an empirical
convergence estimate rather than a rigorous error bar; witnesses are properly
W-matched and can be realized gauge-invariantly.

## 4. “Chiral = modulus,” factorization, and what is new beyond K2c

At index zero,

\[
|\det M_L(e)|=|\det M_R(e)|=|\det D(e)|^{1/2}
\]

up to the field-independent powers of two.  Four left charge-1 determinants
and one right charge-2 determinant therefore give

\[
|\rho_{11112}|=C\,|\det D(1)|^2|\det D(2)|^{1/2}.
\]

The code implements those multiplicities at `scripts/nt1_lib.py:88-89,126-130`.
The direct check finds a constant residual to `7.1e-14`
(`scripts/modcheck_Lt12.out:1`), and my independent full-kernel rebuilds verify
the factorization at matrix level to `3.3e-14` or better.  The factorization is
therefore correct.

The stronger claim needs narrowing.  On these W-matched configurations the
phase is constant only within transport error; it is not a general property of
chiral measures.  In fact the same phase constancy occurs for the anomalous
single-Weyl L1 and for isolated L2/R2 factors
(`scripts/P1_phase_Lt12.out:1-4`).  Therefore the phase collapse is a property
of this very restricted `Lx=2`, open-time, W-matched configuration family
(possibly of an even narrower symmetry within it), not evidence about generic
11112 configurations.  The present data do not isolate which of those
restrictions is decisive.

The test is not numerically vacuous: it establishes that the distinct positive
functional \(|\det D_1|^2|\det D_2|^{1/2}\) is itself non-RP on these witnesses,
with a negative about 4.4--4.7 times the K2c massive vector-overlap negative.
That is the precise new result beyond K2c.  But it is vacuous as a probe of the
chiral **phase**, of anomaly cancellation, or of the Lüscher current: all of
those data drop out on the tested family.  Nor does modulus non-positivity prove
that every allowed local measure-term/counterterm phase is non-RP.

**Item-4 finding:** factorization CONFIRMED; generic “chiral = modulus” and a
chirality-specific mechanism NOT CONFIRMED.

## 5. Is fixed `CHI-RP-FAIL` met?

Numerically, yes: every tested matrix is Hermitian within transport/roundoff,
the negatives are quadrature-converged and far below `-10E`, and the witnesses
are W-matched and gauge-invariant.  If the fixed criterion is read as accepting
any finite-strip gauge-restored phase prescription, the appropriate reading
would be `CHI-RP-FAIL`.

Under the stated scientific setup, no.  `TESTS.md:30` asks whether RP fails for
a genuinely chiral, anomaly-free overlap **measure**, with a Lüscher-type or 2D
abelian construction.  The required locality/global-integrability part of that
construction was neither proved nor tested successfully, and the prescription
does not distinguish the anomaly-free multiplet from anomalous L1.  The setup
gate therefore fails before the eigenvalue reading is applied.  My strict
reading is **OPEN / NOT CONFIRMED**, specifically: “a legitimate local
gauge-invariant chiral measure was not built in the evidence supplied.”

Scope is in any case limited to 2D compact U(1), `Lx=2`, open time,
`Lt=12,20`, overlap mass parameter `M=1`, `beta_g=0`, hard plaquette support
`delta=0.6`, link reflection, and one phase/current prescription.  No torus,
`Lx>=4`, continuum/infinite-volume limit, nonabelian theory, 4D theory, or
local-counterterm scan was performed.  Algebraic anomaly cancellation of the
charge list is true, but its role in producing a local measure was not tested.

**Item-5 finding:** the numerical inequality in `CHI-RP-FAIL` is met, but the
measure-legitimacy premise is not; the fixed reading is therefore NOT
CONFIRMED (OPEN at the measure-construction gate).

## Strongest correct statement

On the finite two-dimensional `Lx=2` open-time U(1) lattices tested, with hard plaquette support and W-matched gauge-invariant orbit witnesses, the worker's specific numerically gauge-restored 11112 overlap prescription yields a Hermitian RP kernel whose phase is constant within transport error and whose kernel consequently equals that of the positive modulus `|det D(1)|^2 |det D(2)|^(1/2)`; independent polar-overlap rebuilds reproduce quadrature-converged negative eigenvalues from `-5.309e-3` to `-1.143e-2` on all four pools.  This extends K2c by showing robust non-RP of that fractional-power overlap modulus for 11112 multiplicities, but it does not yet show RP failure of a legitimate local anomaly-free chiral measure, because the cumulative open-strip current has not been shown to satisfy Lüscher locality, lattice-symmetry, and global-integrability requirements and the tested sector is insensitive to both the chiral phase and anomaly cancellation.

## Files created for this review

- `REFEREE.md` (this record)
- `referee_independent_modulus.py`
- `referee_measure_checks.py`
- `referee_independent_modulus.out`
- `referee_independent_modulus_n32.out`
- `referee_independent_wg.out`
- `referee_independent_t2.out`
- `referee_independent_lt20.out`
- `referee_measure_checks.out`

No `REFEREE_VERDICT.md` was created.
