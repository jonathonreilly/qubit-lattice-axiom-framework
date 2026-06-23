# Summary

Block151 proposes the Route-2 same-source selector primitive isolated by
Block150, with a required five-reviewer physicist panel certificate.

This is not an audit verdict. No audit worker was run and no audit verdict was
applied. The branch does not edit the primitive registry and does not claim
the primitive is accepted.

## Trace

```yaml
trace_class: upstream_support
reachability_to_target: supports
artifact_role: frontier_probe
actual_current_surface_status: open
```

## Primitive

The candidate primitive supplies one physical Route-2 source/readout surface:
finite `Omega_R`, positive normalized `P_0`, normalized `P_h << P_0`,
physical `J_CR`, same-source physical variables `X,Y`, raw moment
`E_0[XY]=1`, cubic one-axis one-point magnitude `E_0[X]=E_0[Y]=s/3`,
connected-subtraction typing, source/readout unit identification `mu=1`, and
orientation datum `sigma_TE=-1` applied after `kappa=0`.

If externally accepted, this supplies the Block150 missing primitive and gives
the endpoint-independent path to `kappa=0`.

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.py | tee outputs/frontier_quark_route2_same_source_selector_primitive_proposal_2026_06_23.txt
TOTAL: PASS=95, FAIL=0

Adjacent guards passed:
Block150 82/0; Block149 79/0; Block148 79/0; Block147 113/0.

Hygiene passed:
STATE.yaml YAML parse; git diff --check; ASCII scan; overclaim scan.
```

## Panel

```text
Physicist A: PASS
Physicist B: PASS
Physicist C: PASS
Physicist D: PASS
Physicist E: PASS
objections: 0
```

## PR Identity

```text
pending
```
