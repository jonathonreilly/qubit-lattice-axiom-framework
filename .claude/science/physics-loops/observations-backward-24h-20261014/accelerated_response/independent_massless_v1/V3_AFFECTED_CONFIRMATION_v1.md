# Affected confirmation: v2 to v3 clock/force note

Reviewer `/root/inertial_response_check`. Root remains scientific author. This
is an affected mathematical source check, not a formal audit. The completed v2
comparison report and identity remain unchanged. I read the complete v2-to-v3
delta and checked its interaction with the already reviewed joint operator and
adjoint regularity. No new adjoint implementation or numerical count experiment
was read or rerun; those remain the separate checker's scope.

| Input | SHA-256 |
| --- | --- |
| `JOINT_CLOCK_FORCE_WORKING_v2.md` | `7ac81b681804460dfb277b4e2fa369b69ed138b68f833d103a9e547f81de7f7c` |
| `JOINT_CLOCK_FORCE_WORKING_v3.md` | `c90af86ca2008d4d31e857bf4f7b6a7fe5b73b7ad0c307f65ac08eb3bff62605` |
| Prior v2 comparison report | `a72bba3e9364fafdb7f09f6a237c52b6013e2502595e2c19ace2e115c773d0a4` |
| Prior v2 comparison identity | `fd9fb89d9da92218e8111d49b9ca9d908c91faa9976c8032c7ae56f3a58c4770` |

No unresolved mathematical discrepancy was found in the new L2 premise or the
constant-response contrast. The change neither selects an absolute background
nor extends the result beyond the supplied massless linear observation model.

## Distributed-readout regularity

On a finite interval, bounded reference evolution coefficients and L2
distributed forcing give a bounded adjoint that is H1 between the finitely many
endpoint atoms. Position and clock atoms have no velocity-state component, so
the velocity-adjoint component remains continuous across them. Its derivative
is L2 globally. Thus the pre-existing argument that the force weight is H1 is
valid under the newly explicit L2 premise, subject to the already stated smooth
or bounded-multiplier reference assumptions. The final zero trace and full
initial-state cancellation supply the other compact-extension trace. Clock
adjoint jumps remain compatible with the direct coefficient being L2. The new
premise is sufficient and is not a claim that arbitrary distributions have this
regularity. No endpoint-velocity atom or point-field observation has been added.

## Constant response and the quotient domain

For any specified observation row i, the already checked linear response is

    L_i(h) = sum_A integral [c_i,A h + W_i,A . a_h] ds.

For an added spatially and temporally constant k, the force a_k vanishes.
Therefore the response increment is exactly

    L_i(h+k)-L_i(h) = k sum_A integral c_i,A ds = k b0_i.

This uses the direct coefficient, including its sign; it cannot be recovered by
summing separate direct-field and force norms. A linear contrast t has increment
`k b0^T t`, so insensitivity to every constant is equivalent to `b0^T t=0`.
The column b0 is computed from the supplied observation's adjoint. It is not a
new freely chosen field-state selector. Since c is L2 with finite support, its
integral exists. After full initial-state cancellation, the force traces also
have the zero endpoint values needed for the energy theorem.

It follows that an admissible contrast satisfying the initial-state, instrument
and b0 constraints has the same value on every anchored Sobolev representative
plus a constant. The original massless Gram therefore gives its continuous
functional on the energy space modulo those constants. This statement is about
removing first-order constant perturbations for a specified linear measurement
model. It does not determine the background value A_b, the coupling, external
reference dynamics or any environmental/energy supplier. It does not license
arbitrary nonlinear constant changes while holding the linearized model fixed.
The note explicitly retains these limitations.

Using the actual column span of [N,X,b0] is correct even if columns are
dependent. A useful nonzero contrast exists only if its orthogonal nullspace is
nontrivial; appending b0 can remove a direction and information. If the mapping
or response columns are uncertain, exact mathematical annihilation does not
make that uncertainty vanish. These requirements are explicitly stated in v3.

## Numerical example and preserved scope

The added paragraph reporting a synthetic 22-count, 14-initial-component,
two-instrument-column example, a seven-to-six floating nullspace change and
constant response of order 3.4e-8 was read as an attributed numerical example.
I have not independently checked its underlying adjoint implementation,
rank thresholds or numerical outputs. That implementation is another checker's
assigned scope. The paragraph does distinguish a floating experiment from an
exact-rank certificate or real calibration. The mathematical cancellation above
does not depend on those numerical values. A nonzero residual, however small,
is insufficient for a universal energy-only inequality if arbitrary constants
remain admitted; the note's warning is mathematically correct.

The rest of the delta is version text, section renumbering and equation label
8 to 8b. No joint Gram, sign, normalization or massive claim changed. Previously
frozen independent derivations and controls are reused only for their unchanged
massless scope; no broad suite was rerun. The exact source diff is retained as
`V3_AFFECTED_DIFF_v1.patch`. All reviewer writes remain inside this independent
directory; no author source, index, branch, lock or publication was changed.
