# Independent narrow far-field and plateau review

Reviewed 2026-10-12. No mathematical or numerical error was found in the pinned
derivation or the actual two-candidate arithmetic. One wording ambiguity was
identified and then resolved in the separately preserved V2 note, as checked
below. This review checks the stated static
point-source problem and computation; it does not evaluate an actual binary,
new galaxy field, target velocity, fitted response, or observational likelihood.
Parent remains the scientific author. No author source or active process was
modified, and this is not a formal audit.

## Exact subjects

| Subject | SHA-256 |
|---|---|
| DIRECT_FAR_FIELD_PREDICTION.md | `6cd3131b2fe517d160ccfa8e7b3d128c58c001da1d1cf00182ec17c96b85a9e3` |
| direct_far_field_check.py | `9718702e6921ddc7cd27cd853fe6083e5831d568b0533bb6a98545d31c6b117d` |
| FAR_FIELD_PREDICTION_v1.json | `620bab786ad252acb8f84b88f568b43d35abdd71d6fa63b76a8194e18ea44d53` |
| Original six-fit receipt | `6b0528745ba0e3ebdc081678821355e54d0d41d8e787cf0e904099942926bcb1` |
| Separate margin candidate | `ffa93f9ad0f8a412020eb756bbc996c07caa1b55a4269cbfee865aa7af591ebc` |

The complete note and checker were read. The actual result's source, note,
fits and margin hashes match these bytes. The operator, fit helper, response
basis, field solver and inverse protocol are the previously reviewed pinned
dependencies; their identities are recorded in `snapshot_manifest_v1.json`.
All actual input arrays remain unopened in this review. Only candidate and
result JSON receipts were used for the response arithmetic.

For an external consistency check, I read the primary
[QUMOND paper, section V and V.1, equations 57–60](https://arxiv.org/html/0911.5464v2#S5.SS1).
Its monopole flux and leading quadrupolar potential agree with the note.
Section V also treats the Newtonian and physical external boundary fields
as separate inputs absent an additional relation from the parent system.
The following derivation and tests were performed independently of the paper
and the author's helper functions.

## Independent flux and Poisson derivation

Put a = GM, c = cos(theta), s = a/r², and U = E e_z + s r_hat. For r > 0,
div U = 0. At a smooth external point E,

    |U| = E + s c + O(s²),
    N(|U|)U = N_e E e_z + N_e s r_hat + E N'_e s c e_z + O(s²).

The first term is uniform, and the second has zero ordinary divergence away
from the point source. Since d_z(c/r²) = (1-3c²)/r³,

    Delta psi = a E N'_e (1-3c²)/r³ + O(r^-5)
              = -2 a N_e K P2(c)/r³ + O(r^-5),
    K = E N'_e/N_e.

This is only a far-region expansion; it is not valid through the nonlinear
central region. Instead, the source equation and Gauss theorem directly give
the surface-flux identity. The uniform physical potential has zero net flux.
The normalized flux of N(|U|)U through a sphere is

    (1/2) integral_-1^1 N(sqrt(E²+s²+2Es c)) [1+(E/s)c] dc.

The leading limit is N_e + E N'_e/3 = N_e(1+K/3). This independently fixes
the monopole coefficient to -a N_e(1+K/3)/r. The angular Poisson identity
Delta(P2/r) = -6 P2/r³ fixes the particular term to +a N_e K P2/(3r).
Adding the two terms gives exactly

    psi = -(a N_e/r)[1+(K/2)sin²(theta)] + o(r^-1).

The signs and factors 1/3 and 1/2 are therefore correct. Strict differential
positivity D = N + A N' > 0 implies 1+K = D(E)/N_e > 0 for positive N_e.
This is a static constitutive statement, with no kinetic-health conclusion.

## Plateau support and extraction

For the frozen nonnegative log-ramp basis, each open knot interval has
derivative -w_j/[A log(A_(j+1)/A_j)]. It is constant exactly when w_j = 0.
Adjacent zero cells join continuously, and a run reaching the first or last
cell also joins the constant low or high tail. The checker uses exact zero,
not a threshold; its left/right merging and 0/infinity tail endpoints are
correct for the supplied E, which lies strictly inside a knot cell.

I independently recovered the interval by examining all active derivative
intervals and taking the nearest active boundaries below and above E. This
uses a different extraction algorithm. It reproduces both complete plateaus,
not merely the single cell containing E. Both share A_low = 1e-10 m/s².
Their upper endpoints are 1.7782794100389228e-9 and
5.623413251903491e-9 m/s², respectively.

For delta = min(E-A_low, A_high-E) > 0, the reverse triangle inequality is

    abs(|U|-E) <= |s r_hat| = GM/r².

Thus every angle at every r > sqrt(GM/delta) is inside the same plateau.
Outside that sphere, div[N_e U] = N_e div U = 0. The effective extra source
has no support there. Its flux is exactly 4 pi GM N_e, because the uniform
E cos(theta) part integrates to zero. Hence the total effective monopole mass
is N_e M, and the effective extra mass is (N_e-1)M. The high-acceleration
response tends to one, so the point baryonic source retains its usual mass
coefficient at the origin.

The exterior internal potential is harmonic. Its decaying multipoles can
still be nonzero. For example P2(c)/r³ is harmonic outside the origin and has
zero net spherical flux, while changing the force and its angular dependence.
This separately demonstrates why the correct total flux and compact support
do not imply an exactly central force or a specified relative error at the
support radius. The author states that limitation accurately.

## Independently recomputed numbers

Both candidates use E = 1.4915242022774435e-10 m/s² and have K(E) = 0 exactly.
At this E, all nonzero ramps below the plateau are zero and those above it
are one. Consequently N_e can also be read as one plus the sum of the
high-side active weights, independently of ramp interpolation.

| Candidate | N(E), also asymptotic acceleration ratio | sqrt(N(E)), speed scale |
|---|---:|---:|
| Original D joint | 1.3409101890174848 | 1.157976765318495 |
| Interior D joint | 1.3820666293142616 | 1.175613299224818 |

For both, delta = 4.915242022774435e-11 m/s². With the supplied
GM_sun = 1.32712440018e20 m³/s² and 1 AU = 149597870700 m, the support bound is
10983.934931297521 AU. Its units are length, and for a different stipulated
point mass it scales as sqrt(M/M_sun). The speed multiplier follows from the
leading test-particle circular relation v² = GM N_e/r relative to a
high-acceleration calibration where N = 1. It is an asymptotic scale, not a
finite-separation binary prediction or an orbital distribution.

## Controls, wording qualification and limits

`check_far_field_independent.py` passed the following lightweight controls:

- Symbolic differentiation of the stated potential reproduces the P2 source
  and flux exactly. A separate surface expansion of N(|U|)U gives
  N_e + E N'_e/3 without using that potential.
- A synthetic smooth nonconstant response with K = -0.1875 gives surface
  flux coefficients 1.4996666667, 1.4999966667 and 1.4999999667 as the internal
  to external field ratio decreases from 0.1 to 0.01 to 0.001, approaching
  the independently predicted 1.5. The pointwise source remainder scales
  as r^-5 under successive radius doublings.
- At 65-digit precision, an independent scalar ramp evaluator and adaptive
  opposite-hemisphere quadrature reproduce each frozen plateau's N_e flux at
  radius factors 1.000001, 1.001, 2, 10 and 100. The support inequalities
  hold explicitly at both angular extrema. The computed flux differences
  vanish at that working precision; this is numerical agreement, not a
  replacement for the triangle/Gauss proof.
- The response on the opposite axis at 0.99 times the bound already differs
  from N_e in both actual candidates, so the check does not silently assume
  constancy inside the stated support radius.
- The pinned author checker was run on synthetic merged-middle, low-tail,
  high-tail, all-zero, single-cell and tiny-nonzero-neighbor fixtures. Its
  plateau endpoints match the independent active-interval construction.
  A nonconstant cell is rejected. A weight of 1e-300 is correctly treated
  as nonzero when locating the interval.

The successful check used approximately 122.8 MB peak RSS and 1.525 seconds,
with numerical threads limited to one. Actual source-field construction and
all array loads were trapped during the checker fixtures. Runtime evidence
is preserved in `independent_checks_v1.json` and the fixtures under
`gravity/response_inverse/independent_far_field_review`.

The original pinned note says, “No binary orbital statistic, stellar mass
estimate or velocity datum was used to choose these predictions.” Read
literally, the unqualified velocity clause is too broad: the response weights
were fitted to galaxy velocities. The surrounding note clearly identifies
the responses as fitted, and no new binary data enter this computation. A
narrow clarification such as “No additional binary measurements were used to
choose this consequence” would remove the ambiguity. This is a wording
qualification, not a failure of the derivation or arithmetic. It was sent to
the parent; no author file was changed by this reviewer.

The parent subsequently supplied the complete `DIRECT_FAR_FIELD_PREDICTION_V2.md`,
SHA `e2874ee4d0f29821d3deb1b25393f4c3513e23130f64ba45cab9c3a2aeedf767`.
I read the complete V2 and independently computed its diff. The only changes
are replacement of the broad sentence with an explicit statement that no
additional binary observation was fitted, and a footer stating that galaxy
velocities and solar/external constraints previously fitted the response.
The mathematics, numbers, support claim and limitations are unchanged. This
resolves the wording issue. The original note, checker and numerical receipt
remain byte-identical; their prior source binding remains valid. No arithmetic
rerun was needed. The exact checked diff and a separate
`wording_followup_receipt_v1.json` are preserved in the runtime review folder.

The note correctly keeps the physical external field relation g_e = E N(E)
separate from the local constant-boundary problem; that relation came from
the earlier spherical-parent premise. It also correctly requires a
finite-separation field or multipole error bound, mass calibration, external
geometry, trajectories, projection and selection/contamination modeling
before observational use. No new observation is scored here. No claim about
an exact binary force law, finite-radius accuracy, a healthy relativistic
completion, full-sphere theorem, or formal audit standing follows from this
review. Original deadline and stop markers were checked; campaign ownership
and the active six-source process were unchanged.
