# Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "A volume-independent sector-energy inequality A_cons >= e_neutral I-c N is needed to turn the conditional quadratic ground-state defect-density estimate into an estimate for the actual supplied clock Hamiltonian."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Independently review the proposed uniform bound; address neutral-phase stiffness separately."
```

The exact missing premise appears as A_cons >= e_neutral I - c N in the
prior campaign's BLOCK1_SECTOR_PROOF_SEARCH.md at18ff8d43faa1c4078b7af27bdb93038f2a9c4de1.
The proposed proof supplies c=max(0,3t rho(exp(-4mu))-9K/4),
rho(h)=(h+sqrt(h²+8))/2. It then supplies a bound independent of volume:
<N>/E <=48v²/(lambda-c-12v)², v=2t exp(-mu), lambda>c+12v.
The theorem does not select a phase, native law or physical parameters.
Author proposal status is bounded-support; independent review is pending.
