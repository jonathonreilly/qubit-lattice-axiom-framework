# Route-2 Eta-Floor HF Boundary: No Spectral Floor Object in the Live Chain

**Type:** bounded_theorem (implementation-boundary result)
**Claim scope:** This source note checks the live Route-2 eta-floor chain named
by the finite-difference provenance note and asks whether the current code
exposes the spectral object required for a Hellmann-Feynman endpoint derivative:
`eta_floor(q) = lambda_min(A(phi(q)))` with a simple floor eigenpair. It does
not compute or claim exact-slope endpoint ratios.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:** [scripts/quark_route2_eta_floor_hf_boundary_check.py](../scripts/quark_route2_eta_floor_hf_boundary_check.py)
**Runner cache:** [logs/runner-cache/quark_route2_eta_floor_hf_boundary_check.txt](../logs/runner-cache/quark_route2_eta_floor_hf_boundary_check.txt)

## Result

The requested Hellmann-Feynman replacement cannot be performed on the live
implementation because the live object named `eta_floor[1]` is not an
eigenvalue. The runner traces the chain:

- `scripts/frontier_tensor_support_center_excess_law.py` calls
  `two.tensor_metrics(phi_from_q(q))[0]`;
- `scripts/frontier_tensor_boundary_drive_two_channel.py` returns
  `blk.eta_floor[1]`;
- `scripts/frontier_tensor_universal_kernel.py` sets
  `eta_floor = np.array([0.0, base.e_spatial_tf], dtype=float)`;
- `scripts/frontier_tensorial_einstein_regge_completion.py` defines
  `e_spatial_tf` as the maximum absolute entry of the trace-free spatial
  Einstein tensor over the fixed shell-adjacent probe points.

So the live eta-floor endpoint is a nonspectral max-entry envelope:

```text
eta_floor[1] = max_probe,max_i,j |G_ij^TF(phi)|
```

not a `lambda_min(A(phi))` object. The runner also confirms that no
`eig`/`eigh`/`eigvalsh` call participates in the eta-floor assembly path. The
only `eigvalsh` occurrence in `scripts/frontier_tensor_universal_kernel.py` is
the later diagnostic of `K_univ`, outside `family_block` and not used to create
`eta_floor`.

The linear map part of the requested program is true: `q -> phi` is linear on
the endpoint and bright-channel directions. That is not sufficient for the
Hellmann-Feynman derivative, because the current chain has no assembled
operator `A(phi)`, no floor eigenvalue, and no floor eigenvector `psi`.

## Endpoint Observations

The runner evaluates the two endpoint backgrounds:

```text
q=e0:        eta_floor[1] = 7.007177027199343e-05
q=s/sqrt(6): eta_floor[1] = 4.608047364021197e-05
```

At both endpoints, `eta_floor[0]` is zero and `eta_floor[1]` equals
`ProbeResult.e_spatial_tf` from the tensor-completion probe. The active
nonspectral max-entry envelope is not tied at these two backgrounds; the
active max gaps are positive. This is reported only to identify the implemented
envelope. It is not a spectral simplicity gap and does not supply an
eigenvector residual.

## Consequence for the Exact-Slope Request

No exact-slope `t_balance` is emitted by this row. The requested number would
require an operator family `A(phi)`, a simple `lambda_min`, and an eigenvector
`psi`; those objects are absent from the live eta-floor chain. Printing
Hellmann-Feynman endpoint slopes from this implementation would fabricate the
load-bearing eigen-objects.

The finite-difference provenance note remains correct about provenance and
step-stability as an in-flight pointer: `.claude/tmp/refs/T_BALANCE_FD_NOTE.md`.
This row does not supersede those finite-difference values with step-free
values; it identifies the implementation boundary that blocks that specific
supersession route. Named open targets are now:

- define or locate the intended spectral operator `A(phi)` whose simple floor
  eigenvalue should replace the current max-entry eta-floor object;
- alternatively derive a direct analytic/envelope derivative for the actual
  nonspectral max-entry observable;
- only after one of those is supplied, recompute endpoint slopes and revisit
  the `|b_T/a_T| - 1` near-miss without finite differences.

## No-Go Discipline Gate

This is a narrow negative result: the closed claim is only that the requested
Hellmann-Feynman derivative is not available from the current implemented
eta-floor object.

**N1 alternative routes.**

| Route tested against the narrow claim | Status |
| --- | --- |
| Trace `support_center_excess_law.eta_floor` | ATTEMPTED; it delegates to `tensor_metrics(phi_from_q(q))[0]`. |
| Trace `boundary_drive_two_channel.tensor_metrics` | ATTEMPTED; it returns `blk.eta_floor[1]`. |
| Trace `universal_kernel.family_block` | ATTEMPTED; it stores `[0.0, base.e_spatial_tf]`. |
| Trace `tensorial_einstein_regge_completion` | ATTEMPTED; `e_spatial_tf` is a max absolute trace-free Einstein tensor entry. |
| Search spectral calls on the eta-floor path | ATTEMPTED; no eigensolver call participates in the eta-floor assembly. |
| Dynamic endpoint evaluation | ATTEMPTED; `eta_floor[1]` equals `e_spatial_tf` at both endpoint backgrounds. |

**N2 wall independence.** There is one collapsed wall: the live eta-floor object
is not a spectral floor eigenvalue and exposes no eigenpair. The static trace,
spectral-call scan, and endpoint evaluation are witnesses of that same wall,
not independent admissions.

**N3 hidden-wall scan.** The words "floor" and "eta" in the existing code are
names, not spectral structure. The runner checks the implementation path rather
than assuming the name supplies an operator.

**N4 residual matching.** The residual here is exactly the requested
Hellmann-Feynman derivative for the live eta-floor chain. The in-flight
finite-difference note is cited only as a plain-text provenance pointer and is
not used as a witness that a spectral object exists.

**N5 rhetoric audit.** The note does not say that no exact derivative exists
for any reformulation. It says the current implemented chain lacks the
Hellmann-Feynman prerequisites.

**N6 partial-closure scan.** Two partial-closure paths remain open: add or
identify the intended spectral operator `A(phi)`, or derive a direct derivative
for the actual nonspectral max-entry envelope.

**N7 steelman.** A reviewer could argue that the phrase `eta_floor` refers to
a conceptual spectral construction omitted from these helper modules. That
would be a valid route if a module or note supplies `A(phi)` and its floor
eigenpair. This row only checks the live code path used by the finite-difference
endpoint ratios.

**N8 cross-cycle echo.** Prior route-boundary notes in this repo avoid turning
a failed method into a global obstruction. This note follows that pattern: it
records a failed Hellmann-Feynman route for the current implementation and
leaves the spectral-operator and nonspectral-envelope derivative routes open.

**Gate status:** PASS for the narrowed implementation-boundary result; FAIL for
any broader reading that says every step-free derivative route is blocked.

## Reproduction

```bash
python3 scripts/quark_route2_eta_floor_hf_boundary_check.py
```

Expected final line: `TOTAL: PASS=12, FAIL=0`.
