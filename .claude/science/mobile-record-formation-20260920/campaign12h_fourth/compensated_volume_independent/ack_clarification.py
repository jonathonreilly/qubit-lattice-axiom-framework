"""Bind the separately supplied F1 topology clarification; no science rerun."""
from pathlib import Path
import datetime
import hashlib
import json

base = Path(__file__).resolve().parent
author = base.parent/'compensated_volume_author'
expected = {
    'AUTHOR_SEAL.json': '5da6ab8a81e7f6442a3c63ece190e9119b3c2cdd00c9960465bc01cc963d1f7f',
    'LOCAL_VOLUME_DYNAMICS_WITH_COMMUTING_ELECTRIC_TERMS.md':
        'a0c1389773766c47b41300329cf6b945a8f5e584c2c46853fe34064a9c331bd6',
    'ROOT_TIME_TOPOLOGY_CLARIFICATION.md':
        '256c6243b7f0c4d7208dd8b2ced8971b9f843bb8a9a715e36be05ce10e932fdd',
    'local_support_and_birth_check.py':
        '95bbec165a6fac41874567c2285c52e848c1fcb7fe1fb84d9316bae7177a9e42',
    'LOCAL_SUPPORT_BIRTH_RESULTS.json':
        '2c279d3b2e4525c53a5cae7a54ed285d428621a661f698449e040ebe9d2ec915',
}
bindings = []
for name, sha in expected.items():
    p = author/name
    content = p.read_bytes()
    actual = hashlib.sha256(content).hexdigest()
    assert actual == sha, (name, actual)
    bindings.append({'path': str(p), 'bytes': len(content), 'sha256': actual})
text = (author/'ROOT_TIME_TOPOLOGY_CLARIFICATION.md').read_text()
assert 'no such algebra is constructed' in text
assert 'does not restore operator-norm time continuity on the same full local algebra' in text
result = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'finding': 'F1: the original Section 5 representation alternative could wrongly suggest restoration of norm time continuity.',
    'disposition': 'Resolved by the separately supplied clarification, read together with the frozen note.',
    'reason': 'It explicitly reserves norm continuity for a separately constructed and checked invariant regular algebra, and distinguishes strong/weak statewise continuity in locally normal representations.',
    'original_author_note_and_seal_unchanged': True,
    'author_scientific_runner_and_results_unchanged': True,
    'PRE_artifacts_modified': False,
    'mathematical_replay_for_clarification': False,
    'bindings': bindings,
}
target = base/'F1_CLARIFICATION_ACK.json'
if target.exists():
    raise FileExistsError(target)
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'finding': 'F1', 'resolved': True, 'bindings_verified': len(bindings),
                  'acknowledgment': str(target)}, indent=2))
