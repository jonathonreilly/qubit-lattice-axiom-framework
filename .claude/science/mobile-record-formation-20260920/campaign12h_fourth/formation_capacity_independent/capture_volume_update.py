from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
D = HERE.parent
items = [
    ('compensated_volume_independent/FINAL_SEAL.json', 'ad9aa6598563aabe3db38e0ae4bb421aef602782aa9c718daf479056402f8c89', 'whole-file authentication, metadata and selected relevant entries read; no claim to rerun or recursively authenticate the whole prior packet'),
    ('compensated_volume_independent/COMPARISON.md', '61411fbea5f5c9566de48080464dbd2f5439d6c5054a903ca159144121a426a0', 'complete argument read for source-comparison closure'),
    ('compensated_volume_independent/F1_CLARIFICATION_ACK.json', '4e4234926f9b0ec8781af90d9ddec63a0553af3a2fce48dedb8b948384a40ee1', 'complete acknowledgment read'),
    ('compensated_volume_author/ROOT_TIME_TOPOLOGY_CLARIFICATION.md', '256c6243b7f0c4d7208dd8b2ced8971b9f843bb8a9a715e36be05ce10e932fdd', 'complete clarification read; no norm-C0 restoration by representation change'),
]
entries = []
for rel, expected, scope in items:
    p = D / rel
    b = p.read_bytes()
    digest = hashlib.sha256(b).hexdigest()
    assert digest == expected, (p, digest, expected)
    entries.append(dict(path=str(p), bytes=len(b), sha256=digest, role=scope))
seal = json.loads((D/items[0][0]).read_text())
bound = {x['path']: x for key in ('sources','artifacts') for x in seal[key]}
for entry in entries[1:]:
    assert bound[entry['path']]['sha256'] == entry['sha256']
    assert bound[entry['path']]['bytes'] == entry['bytes']
result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
    authorization='Parent explicitly authorized this volume-only source update before capacity PRE.',
    sources=entries, previous_source_binding_preserved=True,
    disposition='Pending volume source comparison closed; read original note with the exact F1 clarification.',
    mathematical_change_to_capacity_reconstruction=False,
    formation_capacity_author_read=False,
    no_new_independent_volume_proof_or_runner_replay_claim=True)
(HERE/'SOURCE_UPDATE_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(authenticated_update_sources=len(entries), pending_volume_comparison_closed=True,
                     capacity_author_still_unread=True),indent=2))
