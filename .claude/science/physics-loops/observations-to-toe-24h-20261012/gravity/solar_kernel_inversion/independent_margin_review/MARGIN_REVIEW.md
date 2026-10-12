# Independent narrow margin, readout, and scalar-symbol review

Reviewed 2026-10-12 by the delegated implementation checker. Parent remains the
scientific author. No material mathematical or implementation error was found
in the five pinned subjects. This is a focused source and synthetic check,
not a formal audit or a claim that the real margin candidate has passed its
field tests. No author file was edited, real galaxy field evaluated, empirical
fit rerun, or parent-owned process inspected or interrupted.

## Exact scope and provenance

The full assigned sources were read. SHA-256 identities are:

| Subject | SHA-256 |
|---|---|
| FOLLOWUP_MARGIN_PROTOCOL.md | `75d11669ced2b3ab386cf43fc186414b54b37bd32021127147a8fa3e3908c622` |
| direct_margin_candidate.py | `9529f3859d62ba03148e02e642cc614f4b80d1e34600272faf81ed2f84aac0e2` |
| direct_validate_margin.py | `66431cd233c846dbf41e52816b35e3d2ee231b706d61ead1571ba12bfd580031` |
| direct_inverse_results.py | `7eb0db61c3ecaed47d4d904a04924fed1800422358debfb5d81d0c6546da023c` |
| DIRECT_SINGLE_SCALAR_CONES.md | `3e136dca278ff8a29eaff760cc6c22fdcb1d3b064aa6ceaa5fbd57eb4cac4e67` |

These sources and the previously reviewed operator, fit, basis, field solver,
inverse protocol, and original field validator remained byte-identical at the
end of both check scripts. Their exact original paths, snapshots and hashes
are in runtime `independent_margin_review/snapshot_manifest_v1.json`.

The preserved freeze receipt has SHA
`c2c6a9669d38b52107f35e865dc3dbe973d68448f0b3f0d14e0ef37af33a4833`.
Its recorded time, 20:11:06.004520 UTC, precedes the candidate receipt time by
42.613303 seconds. Candidate SHA is
`ffa93f9ad0f8a412020eb756bbc996c07caa1b55a4269cbfee865aa7af591ebc`.
The original six-fit receipt remains
`6b0528745ba0e3ebdc081678821355e54d0d41d8e787cf0e904099942926bcb1`.
The recorded ordering is consistent with the stated freeze; these ordinary
JSON timestamps are not cryptographic evidence of wall-clock ordering.

The fixed Newtonian external acceleration equals the original D combined-case
value exactly: E = 1.4915242022774435e-10 m/s². The candidate, freeze and original
fits have matching protocol and parent identities. All three operator receipt
hashes match across the candidate, original fits and current receipt files:

| Galaxy | Operator receipt SHA-256 |
|---|---|
| NGC2976 | `6f4015c5cc8c35f37fbb7c6fcffa69a8d409025cc9a73733f394ad105873beff` |
| UGC07577 | `49dce344ef0b102ba8c1c6c9c61387ec933d5287a37bccd18c929b95478dc81d` |
| KK98-251 | `f3b1ea13a65b1bdc2788e070ef3bba3737acd146c1db4b2ecfe1ef6df2d8b29a` |

No campaign target velocities were opened in this review. The already exposed
three galaxies and solar/external bounds retain fitting-input roles. E is a
condition inherited from the prior sampled optimization, not a newly optimized
parameter or an independent measurement of Newtonian E.

## Tightened constraints

Write F_i = g_N,i + K_i w and A_i = V_i²/R_i. Independently dividing the two
galaxy inequalities by positive A_i gives

    (K_i/A_i) w + z <= H_i/A_i - g_N,i/A_i,
   -(K_i/A_i) w + z <= g_N,i/A_i - L_i/A_i.

Thus changing both former relaxed-t coefficients from -1 to +1 is correct.
For B_j(E) equal to the ramp evaluated at physical SI E, the external rows are

     B(E) w + [(g_max-g_min)/(2E)] z <= g_max/E - 1,
    -B(E) w + [(g_max-g_min)/(2E)] z <= 1 - g_min/E.

The solar row is (q/Qmax) w + z <= 1. All rows are dimensionless: the galaxy
force and A share field units; g and E are both SI acceleration; q and Qmax
have units s^-2. The positive coefficients and nonnegative weights imply
Q2 >= 0, so the negative edge of the symmetric solar box is inactive.

The implementation at candidate lines 28–38 reproduces these signs and
scalings. The reliance on the last three constraint rows is correct for the
pinned fit helper: external upper, external lower, solar upper. The cap and
the exact D rows are unchanged. Those D rows encode, on ramp interval j,

    min D = 1 + sum_(k>j) w_k - w_j/log(A_(j+1)/A_j) >= 0.

The minimization objective -z, bounds 0 <= z <= 1, secondary objective sum w,
and added secondary row -z <= -z_max + 1e-8 are correct. The scaled primal
residual is checked against 1e-7. The heterogeneous normalization of z is
explicit in the frozen protocol and supports a numerical interior margin,
not a confidence level. There is no external-field rescan in this script.

The real receipt has z_max = 0.0367710320697293 and secondary z =
0.0367710220697293. Independent response arithmetic reproduces total weight
1.5742642362621637, minimum D slack 0.23367903944320956,
E N(E) = 2.0613858267822293e-10 m/s², and external margin
0.19183070869446633. The solar margin arithmetic matches the preserved Q2;
its quadrature was independently checked in the earlier inverse review and
was not reintegrated here. These statements concern the LP candidate receipt,
not its direct-field rectangle margins.

## Direct validation and downstream rectangle allowance

The follow-up validator checks the candidate author source, protocol and
parent identity, fixed E, each source operator receipt, weight shape,
nonnegativity, cap, and D slacks before projections. It requires completed
base/refined/boundary cache files and receipts before calling geometry loaders.
The loaders' cache-identity checks and the previously reviewed boundary
extension remain responsible for cache content. Weight bytes are compared
after all three projections for each galaxy; no fit is performed here.

It applies the same finite gates: positive finite matrix/base/refined/boundary
forces, base/matrix change <= 0.003, refined/base <= 0.005, and boundary/base
<= 0.003. It separately computes the original untightened box margins for
every force and requires all three actual force methods to lie inside all
galaxy boxes. It recomputes external E N(E) and solar q(E)·w at the same E and
weights. Consequently a numerical pass alone cannot pass the candidate.
The D check tolerance is slightly stricter than the LP feasibility tolerance;
that can conservatively reject a near-boundary receipt, not falsely accept it.

For a fixed actual force F_i, the minimum required rectangle relaxation is

    t_required = max_i max(0, (F_i-H_i)/A_i, (L_i-F_i)/A_i).

`direct_inverse_results.py` lines 42–64 implement this expression separately
for matrix, base, refined and boundary forces. It records the original primary
and secondary LP t separately. The maximum direct requirement excludes the
matrix method intentionally, while the matrix result remains reported.
The velocity logarithm is exactly 0.5 log10(F_i/A_i), since the same radius
enters F_i and A_i. Per-galaxy RMS values are aggregated with equal galaxy
weight, not equal pooled-row weight. Nonpositive forces have no real positive
circular-speed log score; the script preserves a null score and a finite
rectangle allowance. Small positive t is not rounded to zero.

## Single-scalar principal symbol

I independently varied the stated action, rather than using the timelike
sound-speed formula. With signature (-,+,+,+), X = eta^ab p_a p_b > 0,
g = sqrt(X), H'(X) = mu(g), the principal current is J^a = mu(g) p^a. Therefore

    dJ^a/dp_b = mu eta^ab + [mu'(g)/g] p^a p^b.

The action variation gives div J = 4 pi G rho with the stated source sign.
For a static gradient along x, Z = diag(-mu, mu+g mu', mu, mu).
The quadratic Lagrangian has positive time coefficient mu/(8 pi G), and
positive spatial-gradient energy when mu+g mu' > 0.

On a smooth strict-D interval, differentiating g = A N(A) and mu = 1/N gives

    dA/dg = 1/D,
    mu' = -N'/(N²D),
    mu + g mu' = 1/D.

Thus omega² = (N/D) k_parallel² + k_perp² in units where the assumed metric
light speed is one. The document's radial and transverse speed ratios are
correct for this spacelike background. In a ramp, D = N-c_j; N/(N-c_j)
increases toward the high-acceleration edge. Its upper one-sided supremum is
N_hi/(N_hi-c_j), provided the denominator is positive. Constant tails have
ratio one. At knots these are one-sided coefficients; strict D is essential
for the smooth inverse being used.

The match to QUMOND is restricted to the spherical flux relation with the
usual boundary condition. The disk and solar operators cannot be transferred
to this different scalar equation. Comparison to a matter light cone also
assumes the stated metric is the physical matter metric; that coupling is an
additional premise. The source correctly declines to infer a global causal
paradox, ghost, observational exclusion, or healthy full completion from this
local wider cone. Its cited distinction agrees with the scope described by
[Babichev, Mukhanov and Vikman](https://arxiv.org/abs/0708.0561); the calculation
above is checked directly rather than inferred from that citation.

## Independent controls and disposition

`check_margin_synthetic.py` executes the pinned subjects on synthetic data,
with all observational row readers replaced before any main call and an
explicit trap on actual RingField construction. Expectations are derived
independently. All controls passed:

- A one-row analytic LP returned z = 0.2 and the expected secondary weight;
  a retained zero-error row forced z = 0; an impossible row retained status 2.
  Direct physical inequality residuals and the assembled normalized rows
  agree to 2.23e-16. An external-scan trap was never triggered.
- Unequal synthetic galaxy row counts reproduced base/refined/boundary
  allowances 0.2/0.225/0.1 despite LP primary t = 0. Equal-galaxy log scores
  agree with independent scalar-loop calculations. Negative-force null scores,
  failed/absent candidates, and a 1.0000889e-12 violation were retained.
- Eight validator scenarios behaved as intended. Only the compatible case
  passed. Tight boxes failed despite numerical convergence; numerical failure
  failed despite rectangle compatibility; negative forces and external/solar
  failures failed. Missing caches were rejected before geometry calls. A
  deliberate weight mutation was detected. All 54 completed projection calls
  across the other six cases received the original weight bytes.
- A separately defined one-ramp scalar response was inverted numerically.
  Finite differences of its four-current at ten axial/rotated spacelike
  backgrounds agreed with Z to at most 1.67e-10. The radial and transverse
  eigenvalues, determinant sign, two constant tails, and upper-knot limiting
  ratio 2 were checked independently of author helpers.

The completed synthetic run used approximately 83.2 MB peak RSS and 0.078
seconds after imports, with numerical thread counts set to one. The initial
reviewer harness had a length-one-array scalar-conversion error; its source,
completed fixture, and failure note are preserved. Correcting that reviewer
line produced the passing run and did not change an author source.

Evidence is in runtime `synthetic_checks_v1.json`, `provenance_checks_v1.json`,
the fixture receipts, and `margin_review_receipt_v1.json`, all under
`gravity/response_inverse/independent_margin_review`. No full-sphere theorem
or classification validation is claimed. The actual parent-owned field
validation, out-of-fit development objects, source/circular-speed readout
uncertainties, and any healthy dynamical completion remain outside this
disposition. The protocol's original deadline and stop markers were checked;
campaign ownership and scheduling were not changed.
