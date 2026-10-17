"""Read-only source capture and exact hash bookkeeping; no scientific calculation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import os

D=Path(__file__).resolve().parent
N=D.parent
W=N.parent/"correlation_worktree"
items=[
 ("family.md",N/"emitter_resource_family_candidate/CANDIDATE.md","9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac","Complete argument read previously; complete affected sections refreshed; controlling mathematical premise"),
 ("family_qualification.md",N/"emitter_family_root_qualification/QUALIFICATION.md","27a4008d6588fef9f0a5ac1d231d71240c12468db93d50a36ac2ee02f6ab7814","Complete current qualification read"),
 ("family_acceptance.json",N/"emitter_family_root_qualification/ACCEPTANCE.json","a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325","Exact source-status identity; no new audit"),
 ("local_emitter.md",N/"autonomous_emitter_route/ROUTE.md","f03626e591cddc3448bee72148edbee4717ae64af3a6543d4b5c184e7ef9f0a1","Complete previously reviewed argument; physical cells and packet implication refreshed; historical pending labels retained"),
 ("installed.md",N/"emitter_installed_certificate/CANDIDATE.md","4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee","Unchanged exact installed argument reused by identity; family supersedes affected kappa bounds"),
 ("generic_v2.md",N/"finite_channel_wavepacket_bridge/THEOREM_V2.md","db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3","Previously checked full packet theorem; no new claim of independent recheck"),
 ("moment.md",N/"ballistic_emitter_escape_candidate/CANDIDATE.md","31449e982b27e623491f4e9cb0c8239e2ff15ebc9605668b8e4684055c52410f","Author's earlier argument; exact moment identities also reproduced in family"),
 ("interval.md",N/"two_body_interval_bridge/CANDIDATE.md","b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45","Previously fully checked; ladder targets and local supports reused"),
 ("reflection_v2.md",N/"autonomous_reflection_candidate/CANDIDATE_V2.md","694484853b731991d97f11f5d9a3a012ff30b9badb7fe57a7c57f6fee7e2fd36","Complete body read; comparison only: supplied incoming packet and three-body boundary, not premise for gate success here"),
 ("reflection_finite.md",N/"autonomous_reflection_candidate/FINITE_READINESS_ADDENDUM.md","ce01691b49abf924d2fc610cf2dd6c71c565c0c21df6f1bc39960ecb2c546a2f","Complete body read; finite-horizon strategy prior work"),
 ("family_wrapper.md",W/"docs/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md",None,"Current wrapper scope refreshed; body reused by its exact separate pin; parent-reported W revision, no Git freshness action"),
 ("reflection_wrapper.md",W/"docs/AUTONOMOUS_BOUNDARY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-16.md",None,"Complete mathematical bodies and scope wrapper read; no publication status adjudication"),
 ("workflow.md",W/"docs/ai_methodology/SCIENCE_WORKFLOW.md",None,"Complete current local workflow read"),
 ("no_go_discipline.md",W/"docs/ai_methodology/skills/no-go-discipline/SKILL.md",None,"Complete narrow-negative scope gate read; no general no-go PASS claimed"),
 ("primitive_registry.json",W/"docs/audit/data/axiom_premise_nodes.json",None,"Complete registry read; no registered primitive classified as a missing axiom"),
 ("realized_state_primitive.md",W/"docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",None,"Complete relevant source read; supplies no chiral seed content")
]
entries=[]
for name,source,pin,coverage in items:
    data=source.read_bytes(); digest=sha256(data).hexdigest()
    if pin is not None and digest!=pin:
        raise RuntimeError(f"source pin mismatch: {source}: {digest}")
    dest=D/"inputs"/name
    with dest.open("xb") as f:
        f.write(data); f.flush(); os.fsync(f.fileno())
    entries.append({"original":str(source),"snapshot":"inputs/"+name,"sha256":digest,"bytes":len(data),"expected_parent_or_previous_pin":pin,"read_coverage":coverage})
out={"created_utc":datetime.now(timezone.utc).isoformat(),"parent_reported_worktree_revision":"0e3993770a7a2dd872018f9dd3c76c2d9a624db9","git_or_remote_revision_verification":False,"entries":entries}
with (D/"SOURCE_MANIFEST.json").open("x") as f:
    json.dump(out,f,indent=2); f.write("\n"); f.flush(); os.fsync(f.fileno())
print(json.dumps({"snapshot_count":len(entries),"all_supplied_pins_matched":True},indent=2))
