from pathlib import Path
import json
r=Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';live=json.load(open(r/'drain8154-author-live.json'))
for n,d in live.items():
 p=w/d['note'];s=p.read_text();s=s.replace('**Status:**','**Type:** bounded_theorem\n\n**Status:**',1);block='''## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Quantitative mathematical bounds for explicitly supplied sphere static models; no physical channel classification."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Original independent affected-source confirmation and bounded finite evidence capture; retained-grade audit remains separate."
conditional_surface_status: "'''+d['scope'].replace('"',"'")+'''"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

''';s=s.replace('## Premises and declared objects',block+'## Premises and declared objects',1);s=s.replace('  - minimal_axioms_2026-06-29','  - minimal_axioms');p.write_text(s)
