# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: s3_route2_readout_endpoint_triple
target_blocker_text: "The unresolved Route-2 endpoint triple still needs the E-channel readout ratio, equivalently q_E/q_T=9/4 or rho_E=21/4, from a current-surface source/readout primitive."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "Use the characterized primitive as the next hard target: derive q_X proportional to w_X^-2 from a named same-domain nonlinear source/readout construction, or prove a larger-class no-go."
```

If the inverse-square primitive is supplied, the endpoint chain is exact:

```text
w_E=1/3, w_T=1/2
q_E/q_T=(w_T/w_E)^2=9/4
q_E=15/8
rho_E=21/4
c_TE=-8/9
```

The current surface still lacks the rule that maps the shell weights to the
inverse-square covariance primitive. This block supports the target by
pinning the missing primitive exactly.
