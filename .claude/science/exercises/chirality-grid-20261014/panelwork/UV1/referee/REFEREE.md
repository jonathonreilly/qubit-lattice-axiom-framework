# UV-1 independent referee record

## VERDICT: CONFIRMED WITH CORRECTIONS

The worker's **literal fixed reading, OPEN for both arms, is correct**.  The
finite-coupling torus computation required by the fixed PERSISTS criterion was
not done at depth `t0 >= 3`, and the post-registered `beta_g = infinity`
calculation was explicitly classified in advance as a comparator that could
not itself set the fixed reading.  The comparator, continuity argument, and
open-time depth-2 result are nevertheless scientifically meaningful and, with
the qualifications below, support a stronger *non-classifier* conclusion:
the normalized RP violation has a very small lattice-scale tail and is not
compactly confined to the first few slices.  What is not established is a
beta-independent physical-channel amplitude, a quantitative finite `beta_0`,
or a continuum/set-B no-go theorem.

This review used the fixed text, registrations, saved outputs, source code,
and two targeted computations.  It did not rerun the expensive full Stage B
or a finite-beta deep torus integral.

## 1. Literal fixed reading

### Finding

**OPEN is the only correct literal reading for each arm.**

The fixed setup requires positive finite gauge coupling and torus witnesses at
depths 1--4.  Its PERSISTS branch is specifically “a quadrature-converged
negative eigenvalue at `t0 >= 3` for some `beta_g`”; UV-ONLY requires
PSD-at-power beyond some `t* <= 3` at every `beta_g`; everything else is OPEN
(`TESTS.md:64-67`).  The amendment leaves those readings unchanged, applies
them separately to the triangle and hard arms, and makes the triangle arm the
headline (`TESTS.md:125-131`).

The main preregistration is even more explicit: the fixed reading uses torus
data, the finite-beta torus was not convergence-checked at `t0 >= 2`, and the
open proxy cannot assign PERSISTS or UV-ONLY (`PREREG.md:58-73,
120-124`).  The later `beta_g = infinity` item was registered as a comparator
that “cannot by itself give a FIXED reading” (`PREREG.md:168-185`), and the
exponentially-small-but-nonzero interpretation was also kept separate from the
fixed classifier (`PREREG.md:206-210`).

Consequently:

- the finite-beta torus `t0 = 1` negatives do not reach the required depth;
- the finite-beta open `t0 = 2` negatives have the wrong geometry and depth;
- the torus `beta_g = infinity`, `t0 = 3,4` negatives have the right geometry
  and depth but not a registered finite coupling and were predeclared
  comparator-only;
- the continuity lemma proves existence, not a directly
  quadrature-converged finite-beta cell under the fixed wording.

The report's conclusion at `REPORT.md:3,35-38` is therefore correct.  One
wording correction is needed at `REPORT.md:54`: the decisive reason for OPEN
is not merely that `beta_0` was not computed; it is that no finite-beta torus
kernel at `t0 >= 3` was quadrature-converged and the comparator was registered
as non-classifying.

The continuity result does, if accepted, exclude the mathematical content of
UV-ONLY: a negative limit kernel at fixed `t0 = 3` or 4 implies a negative
finite-beta kernel for all sufficiently large beta.  But that does not turn
the saved evidence into the fixed PERSISTS datum.  This is a case where the
literal three-way classifier returns OPEN while the supplementary mathematics
leans decisively away from UV-ONLY.

## 2. The `beta_g = infinity` comparator

### 2.1 It is a legitimate limit, with one normalization correction

For W-matched entries the bulk plaquette factors belonging to the fixed
positive-half witnesses factor as a positive diagonal congruence.  They cancel
from the normalized kernel, just as registered at `PREREG.md:38-41`.  In the
remaining buffer/crossing integral, both profiles have value one at zero and a
unique gauge-action maximum there.  Their normalized plaquette measures
therefore concentrate at zero.  The correct weak limit is

```
delta_0(buffer and crossing plaquettes) x Haar(residual Polyakov holonomy),
```

not a delta measure in every gauge variable.  The residual Polyakov angle is
action-free and must remain integrated.  The worker does exactly this: it
extends each witness flatly through the buffer, fixes the first crossing-plane
gauge freedom, and integrates the remaining torus holonomy (`scripts/uv1_inf.py:14-34`).
This matches the registered formula (`PREREG.md:168-175`).

Thus `K_infinity` is the entrywise limit of the **diagonally normalized**
finite-beta kernels for both arms.  It is not generally the nonzero limit of
the raw kernel entries: raw entries centered on nonflat deep witnesses can
vanish exponentially with beta.  This distinction does not weaken the RP
conclusion because positive diagonal congruence preserves inertia at every
finite beta, but it does limit the physical interpretation of “beta
independent.”

The field is flat only in the buffer and at the crossing planes.  The saved
deep witnesses themselves have nonzero bulk plaquettes (for example the
`t0 = 4` pool reports maximum 0.5363 at
`scripts/INF_torus_Lt20_t04.out:17`).  Hence `REPORT.md:28` should not say the
violation is present “even for a flat field” without adding “near the
reflection planes.”

### 2.2 The `t0 = 3,4` negatives are real

The saved primary runs already have large *absolute* sign margins:

- `Lt = 20, t0 = 3`: absolute `lambda_min = -2.2081e-7`, relative
  `-1.4156e-8`, `E = 3.2e-13`
  (`scripts/INF_torus_Lt20_t03.out:17-19`);
- `Lt = 20, t0 = 4`: absolute `lambda_min = -1.5080e-9`, relative
  `-9.4590e-11`, `E = 3.8e-13`
  (`scripts/INF_torus_Lt20_t04.out:17-19`);
- `Lt = 16, t0 = 3`: absolute `lambda_min = -1.5316e-8`, relative
  `-9.8204e-10`, `E = 3.3e-13`
  (`scripts/INF_torus_Lt16_t03.out:17-19`).

It is important not to compare the quoted *relative* eigenvalues directly to
the *absolute* `E`.  On the `Lt = 20, t0 = 4` cell the absolute negative is
about 4,000 times `E`; the relative error scale is approximately
`E/lambda_max = 2.4e-14`.  The kernel is close to rank one and therefore
ill-conditioned as a positive matrix candidate, but the negative eigenvalue
is not close to the numerical backward-error or quadrature scales.

Independent longer searches gave the same sign with larger magnitude:
`-6.6334e-8` at `Lt = 16, t0 = 3`, `-7.1195e-7` at `Lt = 20, t0 = 3`, and
`-3.5822e-9` at `Lt = 20, t0 = 4`
(`scripts/INF2_torus_Lt16_t03.out:24-27`,
`scripts/INF2_torus_Lt20_t03.out:24-27`,
`scripts/INF2_torus_Lt20_t04.out:24-27`).  The worker's explicit-link polar
builder also reproduced the `Lt = 16, t0 = 3` and `Lt = 20, t0 = 4` cells
(`scripts/VINF_Lt16_t03.out:7-8`, `scripts/VINF_Lt20_t04.out:7-8`).

I independently rebuilt the most delicate `Lt = 20, t0 = 4`, 16-witness
kernel from explicit links, importing none of the UV-1 operator builders and
using `X (X^dagger X)^(-1/2)` for the overlap (`referee_checks.py:30-170`).
The result was

```
nw = 12: lambda_min = -1.507970267691e-9
nw = 24: lambda_min = -1.507973749028e-9
nw = 48: lambda_min = -1.507973163092e-9
```

with maximum entry changes `1.07e-14` and `7.20e-15`, eigenpair residuals
below `1.7e-15`, exactly flat crossing plaquettes to `4.4e-16`, and minimum
sampled `|eig H_W| = 0.779726158` on a 64-point scan of the full residual
holonomy circle for every pool pair (`referee_inf_t04.out:7-14`).  This closes
the conditioning concern at the requested scale.  The repeated NumPy
`slogdet` warnings are undesirable, but all retained entries were finite and
the sign and value are stable under two operator constructions and increased
Polyakov resolution.

The registered `E` remains an a-posteriori convergence estimate, not a
rigorous analytic error bound (`PREREG.md:92-95`; the same limitation was
identified in the K2c precedent at `K2c_REFEREE_VERDICT.md:24`).  “Quadrature-
converged” is the correct description.

### 2.3 Witness legitimacy

The pools are W-matched at both interfaces and have flat buffers by
construction (`scripts/INF_torus_Lt20_t04.out:17`; the matching code is at
`scripts/uv1_inf.py:65-70,107-110`).  W is a gauge-invariant spatial holonomy;
matching it selects gauge-orbit centers and makes zero buffer flux feasible.
It is not an extra constraint inserted into the measure.  The determinant and
the integrated kernel are gauge invariant.  Point configurations are
distributional probes, but the kernel is continuous on the gap-protected
admissible neighborhood, so a strictly negative finite matrix can be replaced
by sufficiently narrow smooth gauge-invariant bump functions supported on the
same deep links.  This is exactly the legitimacy argument already accepted in
the K2c independent precedent (`K2c_REFEREE_VERDICT.md:3`).

Accordingly the witnesses are W-matched, gauge invariant after smoothing, and
supported at the registered depths (`PREREG.md:43-56`).

## 3. Continuity to finite beta

### Finding

**The lemma is correct for each fixed finite witness pool, after replacing
“the flat point” by “the flat buffer/crossing locus times the Polyakov
circle” and making the diagonal normalization explicit.**

For a fixed W-matched pair, let `p` denote all independent buffer/crossing
plaquette variables and `w` the residual Polyakov holonomy.  After the
separable positive bulk factors are removed, normalize the gauge weight to a
probability measure.  For both arms,

```
mu_beta(dp,dw) -> delta_0(dp) dw/(2 pi).
```

The support is compact.  On a neighborhood of the limiting locus, the Wilson
kernel has a nonzero spectral gap, so the overlap sign function and
`det D_ov(p,w)` are continuous.  The independent dense scan found a minimum
gap 0.7797 for the most delicate pool (`referee_inf_t04.out:13`).  Boundedness
is automatic in finite dimension.  Thus every normalized kernel entry
converges to the comparator entry.

The diagonal limits are strictly positive.  For massive vector-like overlap,
write the massive operator as `a + b V`, with `V` unitary and gamma5-Hermitian,
`a = 1 + m/2`, and `b = 1 - m/2`.  Complex eigenvalues of `V` pair by
conjugation, while the real `V = +/-1` factors are `2` and `m`; for
`0 < m < 2` their determinant product is positive.  The diagonal normalizers
therefore remain nonzero.

Entrywise convergence of a fixed finite Hermitian matrix implies operator-norm
convergence.  Weyl continuity then gives, for
`lambda_min(K_infinity) < 0`, a finite `beta_0` such that the corresponding
normalized finite-beta kernel is non-PSD for every `beta > beta_0`.  The Haar
Polyakov degree is integrated on both sides of this limit; it is not silently
frozen.

What the lemma does **not** provide is a useful numerical `beta_0`, a finite-
beta quadrature certificate, or a bound uniform in depth, volume, or witness
family.  Given the `t0 = 4` eigenvalue is only `1.5e-9` absolute, the required
`beta_0` could be very large.  It also says nothing directly about fixed
physical depth `t0 m_S`, where `t0` grows with beta.

## 4. Stage B, open time at `t0 = 2`

### Finding

**The fixed code and quadrature construction are correct, and the depth-2
negative meets the registered operational threshold.  It is not a rigorous
analytic certification and it does not set the fixed torus reading.**

The original bug is real and was caught before a kernel was used: the killed
run showed a `6.0e-2` operator mismatch
(`scripts/Bsel_d2_open_KILLED_bugfound.out:7-8`).  The corrected code removes
both positive- and negative-side buffer x-link hops at their zero-angle
values, then restores their node angles (`scripts/uv1_lib.py:131-148`).  Its
V-B0 comparison now agrees with the direct builder exactly at the matrix level
and to `3.6e-15` in log determinant, with every explicit plaquette orientation
checked (`scripts/Bsel_d2_open.out:13-16`; validation code at
`scripts/uv1_d2.py:37-55`).

The nested rule is also structurally correct.  Its residual-flux recursion
uses signs `(-1,-1,+1,+1)`, splits each outer variable wherever the remaining
box/triangle convolution changes polynomial piece, and applies the final
two-plaquette crossing constraint (`scripts/uv1_lib.py:92-110`).  The phrase
“exact-kink quadrature” should mean that the domains and kinks are represented
exactly; the determinant integral on each analytic piece is still a numerical
Gauss approximation.

The full saved kernel gives, in the primary arm, relative negatives
`-3.3521e-6` through `-3.3801e-6` for beta 0 through 8, with absolute
eigenvalues about `-2.0e-5` and `E = 2.8e-7` through `6.3e-7`.  Every cell
satisfies `lambda_min < -10 E`; both secondary-arm cells and controls behave as
reported (`scripts/Bsel_d2_open.out:22-29,34-53,55-63`).  This is precisely the
registered criterion at `PREREG.md:92-94,131-145`.

I additionally checked the primary beta-8 negative direction rather than a
random third-level pair.  A 2-by-2 principal subkernel is already negative:

```
n = 2: lambda_min = -8.415227449821e-6
n = 3: lambda_min = -8.421559419436e-6
n = 4: lambda_min = -8.423311774475e-6
```

The `n = 3 -> 4` maximum entry change is `1.752e-9`, over 4,800 times smaller
than the negative eigenvalue.  The base support volume is exactly
`(88/5) delta^5 = 1.368576` at `n = 3,4`, and the overlap gap stays above
0.811 (`referee_stageb_stream.out:8-16`).  The streaming implementation and
node selection are recorded at `referee_checks.py:173-304`.  This directly
addresses the possibility that the worker's six sampled third-level pairs
missed the negative direction.

Stage B remains an open-time proxy and reaches only `t0 = 2`; by registration
it cannot assign PERSISTS (`PREREG.md:66-73,131-139`).

## 5. “Lattice-scale, beta-independent decay” and OS reconstruction

### Finding

**A lattice-scale tail is strongly suggested; a beta-independent decay law is
not established.  Exact RP fails in the finite proxy wherever any one of the
finite-beta negative witnesses exists, but the result is not a general set-B
or continuum reconstruction theorem.**

The evidence for locality is coherent:

- the finite-beta torus `t0 = 1` relative negative changes by less than about
  two percent between beta 0 and 8 (`scripts/A12h_d1_torus.out:41-49`, with
  comparable results in the other saved Stage-A pools);
- the same open witness family loses a factor about 57 from depth 1 to depth 2
  while remaining negative at every beta (`scripts/Bsel_d2_open.out:55-63`);
- the `Lt = 20` infinity-comparator searches remain negative through depth 4
  and fall steeply (`scripts/INF_torus_Lt20_t01.out:17-19`,
  `scripts/INF_torus_Lt20_t02.out:17-19`,
  `scripts/INF_torus_Lt20_t03.out:17-19`,
  `scripts/INF_torus_Lt20_t04.out:17-19`);
- the free overlap block norm has a lattice decay rate about 0.81 per spacing
  (`scripts/LOC_free_overlap.out:1-13`).

But the claimed `0.2--0.4`-spacing decay length is obtained by comparing
separately optimized pools at different depths, not by following one fixed
witness family or bounding the full negative part of the kernel.  Finite-beta
deep torus data do not exist, so beta independence of the *depth exponent*
was not measured.  Only the amplitudes at `t0 = 1` (torus) and `t0 = 2`
(open) were tested over beta 0--8.  The report itself partly acknowledges that
the per-slice rates are indicative (`REPORT.md:106-115`), but the stronger
plain-language claims at `REPORT.md:29-31` should be downgraded to
“suggested.”  “Never exactly zero at finite depth” is proved only for the
specific depths/pools reached via the comparator and continuity, not for every
finite depth.

The normalization qualification also matters: the beta-infinity persistence
is persistence of the normalized conditional Gram kernel.  It permits
beta-dependent rescaling of increasingly rare nonflat witness sectors, which
is legitimate for the exact RP axiom but is not a demonstration of an
unsuppressed typical or physical-channel effect.  The proposed
`exp(-kappa t0)` suppression at fixed physical `t0 m_S` is plausible only if a
uniform-in-volume/depth locality estimate is proved; the present finite tori
do not supply that estimate.  The qinfo panelist's original diagnostic was
explicitly about dependence on `t0 m_S`, beta, and a physical channel
(`qinfo_statement.md:276-281`), so the fixed UV-1 classifier and the physical
continuum question should not be conflated.

Exact Osterwalder-Schrader reconstruction of a given finite-lattice measure
requires RP for all positive-half test functions.  Therefore the finite-beta
torus `t0 = 1` witnesses already rule out exact OS reconstruction for the
specific 2D overlap measures and couplings tested; one need not show failure
at every depth.  Conversely, the data do not prove `REPORT.md:120`'s broad
phrase “fails at every depth,” nor do they rule out an emergent/approximate
coarse-grained transfer matrix or a reflection-positive continuum limit.  And
because the calculation is 2D U(1), `Lx = 2`, vector-like overlap at
`M = 1, m = 0.05`, it cannot by itself establish a no-go for the complete set-B
matter construction.

## Corrections required

1. Keep **OPEN for both arms**, but ground it in the absence of a directly
   convergence-checked finite-beta torus cell at `t0 >= 3`, not merely in the
   absence of a numerical `beta_0`.
2. Describe `K_infinity` as the limit of the **diagonally normalized** kernels,
   with `delta_0` in the buffer/crossing plaquettes and Haar integration over
   the remaining Polyakov holonomy.
3. Replace “present even for a flat field” by “present when the field is flat
   in the buffer and across the reflection planes”; the deep witness fields
   are not flat.
4. Retain the `t0 = 3,4` negatives as quadrature-converged.  Their absolute
   signs are secure despite the small relative numbers; do not call the
   a-posteriori `E` a rigorous certificate.
5. Describe Stage B as kink-exact in its domain decomposition and numerical in
   its analytic-piece integration.  The corrected code and sign pass the
   registered operational test.
6. Downgrade the numerical decay length and beta-independent depth law to
   suggestive.  Do not say nonzero at every finite depth.
7. Scope the OS conclusion to exact RP of the stated finite 2D proxy.  Approximate
   coarse-grained and continuum reconstruction remain open.

## Strongest correct statement

For the finite two-dimensional `Lx = 2` U(1) proxy with link reflection,
`M = 1`, `m = 0.05`, and W-matched gauge-invariant positive-half witnesses,
the vector-like overlap measure has quadrature-converged negative normalized
RP kernels at finite `beta_g = 1,4,8` on the tested tori at `t0 = 1`, and on
the open-time depth-2 proxy for both the positive-type triangle and hard arms;
on `Lt = 20` the common normalized `beta_g -> infinity` torus comparator is
independently negative at `t0 = 3` and 4, with the `t0 = 4` sign stable at
`-1.508e-9` absolute under an explicit-link rebuild and 12--48 Polyakov nodes.
Because the normalized buffer measures converge to flat plaquettes while the
residual Polyakov holonomy remains Haar-integrated, continuity implies
non-PSD finite-beta kernels at those fixed depths for all sufficiently large
beta.  Thus an exact compact-depth “UV-ONLY” cutoff is excluded in substance,
and the evidence favors an exponentially small lattice-scale tail; however,
under the fixed preregistered evidentiary wording both arms remain **OPEN**
because no finite-beta torus kernel at `t0 >= 3` was directly
quadrature-converged, and no beta-independent physical-depth law, useful
`beta_0`, continuum limit, or full set-B no-go has been established.

## Computational and protocol record

- Independent `beta_g = infinity`, `Lt = 20, t0 = 4` rebuild command:
  `zsh capped.sh referee_inf_t04.out python3 referee_checks.py inf scripts/pool_UV1_inf_torus_Lt20_t04_seed9004.npz --nws 12,24,48 --gap-grid 64`.
  Peak RSS was 34,224 KB (`referee_inf_t04.out:15`).
- The retained Stage-B spot command used a referee-local hard 300,000-KB
  watchdog and streaming node evaluation.  Peak RSS was 212,592 KB
  (`referee_stageb_stream.out:17`).
- Protocol incident: an initial non-streamed Stage-B spot run peaked at 342,672
  KB (`referee_stageb.out:17`), exceeding the requested 0.3-GB ceiling.  It is
  not relied upon.  A first hard-cap retry was then killed at 304,448 KB before
  producing its `n = 4` result (`referee_stageb_under300.out:13-14`).  The
  streaming rerun supersedes both and stayed under the cap.  All referee runs
  used two BLAS/OpenMP threads and ran one at a time.
