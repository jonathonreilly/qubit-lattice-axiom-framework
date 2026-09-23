from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
D = HERE.parent
ROOT = D.parents[3]
SCIENCE = [
    ('local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md', '42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4', 'finite target, full read'),
    ('local_compensation_locality_author/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md', '5539bbe3171ba21933aa42c4cc191b787029e5f5c9220dc8c3ee255e4906f582', 'local pair form and jump support, full read'),
    ('compensated_volume_author/AUTHOR_SEAL.json', '5da6ab8a81e7f6442a3c63ece190e9119b3c2cdd00c9960465bc01cc963d1f7f', 'provisional volume seal, full read'),
    ('compensated_volume_independent/PRE_COMPARISON_SEAL.json', '6e8bae143d8ee1e0c77c57461c8025143b660709ff89e42c5c072a38d2164d0f', 'provisional volume PRE, full read'),
    ('compensated_volume_author/LOCAL_VOLUME_DYNAMICS_WITH_COMMUTING_ELECTRIC_TERMS.md', 'a0c1389773766c47b41300329cf6b945a8f5e584c2c46853fe34064a9c331bd6', 'bound provisional volume theorem, full read for needed hypotheses'),
    ('compensated_volume_independent/REPORT.md', '9dee691689889316acea057aa0180c59776315b7fa9499f0c52bccc9f0e6101b', 'bound provisional volume report, full read for needed hypotheses'),
]
INSTRUCTIONS = [
    ('AGENTS.md', '9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
    ('docs/ai_methodology/SCIENCE_WORKFLOW.md', 'd74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
]

def bind(path, expected, role):
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == expected, (path, digest, expected)
    return dict(path=str(path), bytes=len(raw), sha256=digest, role=role)

entries = [bind(D / p, h, role) for p, h, role in SCIENCE]
instructions = [bind(ROOT / p, h, 'unchanged instructions, previously read; no new workflow loop') for p, h in INSTRUCTIONS]
result = dict(created_utc=datetime.now(timezone.utc).isoformat(), sources=entries,
              instructions=instructions, external_literature_used=False,
              forbidden_author_or_frontier_read=False,
              provisional_dependency='Volume source comparison not closed in this packet.')
(HERE / 'SOURCE_BINDINGS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(dict(science_sources=len(entries), instruction_sources=len(instructions),
                     all_exact_sha256_bindings_match=True, root=str(ROOT)), indent=2))
