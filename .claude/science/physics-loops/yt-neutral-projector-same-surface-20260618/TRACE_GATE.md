# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25
target_blocker_text: "missing_bridge_theorem: add or cite a retained same-surface carrier theorem identifying the qubit P_- source ray with the neutral EW Higgs doublet ray, then re-audit the bounded support claim."
source_of_blocker_text: audit_ledger
reachability_to_target: closes_source_side_blocker
artifact_role: theorem_and_runner_certificate
next_trace_action: "Reviewer should inspect the source-side theorem and runner, then independent audit can decide whether the audited_conditional row moves."
```

## Why The Trace Is Direct

The current conditional verdict says the local projector algebra and EW doublet neutrality check out, but the bridge lacks authority that the qubit readout `P_-` carrier and the EW Higgs lower ray are the same physical carrier surface.

This branch supplies that missing authority in the narrowest possible form: on the retained one-Higgs EW carrier, the neutral ray is the zero-eigenvalue spectral projector of

```text
Q_H = T_3 + Y_H = diag(1,0).
```

That spectral projector is

```text
P_neut = 1_0(Q_H) = I - Q_H = P_-.
```

Therefore the identification is not a discretionary basis label. It is a spectral-projector identity on the same two-dimensional EW carrier.

## Boundary

This trace gate reaches only the same-surface carrier blocker. It does not reach full `Y_T` closure, top coefficient authority, top transfer-response measurement, scalar normalization, physical-scale `g_2`, or observed mass values.
