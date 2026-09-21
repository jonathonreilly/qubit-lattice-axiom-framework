#!/usr/bin/env python3
"""Seal current review outputs after checking all authenticated source identities."""
from pathlib import Path
import datetime
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parents[2]
sha = lambda b: hashlib.sha256(b).hexdigest()

def identity(path):
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': sha(raw)}

results = json.loads((HERE/'ASSEMBLY_RESULTS.json').read_text())
assert results['all_checks_passed'] is True
sources = []
for relative, item in results['source_identities'].items():
    source = identity(ROOT/relative)
    assert source['sha256'] == item['sha256'] and source['bytes'] == item['bytes'], relative
    sources.append(source)
procedures = []
for path, expected in [
 (ROOT/'AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
 (ROOT/'docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
 (Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455')]:
    item = identity(path); assert item['sha256'] == expected
    procedures.append(item)
pr_receipts = json.loads((HERE/'SUPPLIER_PR_RECEIPTS.json').read_text())
for item, expected in zip(pr_receipts, ['c26b0171974c456f68dd92a4c8661ade1cc5ddbd','4ae52ade2299b4dfaff388971f423aa8f6ddf64a']):
    assert item['returncode'] == 0
    record = item['record']
    assert record['state'] == 'OPEN' and record['isDraft'] is True and record['headRefOid'] == expected
    raw = (HERE/f'PR_{item["number"]}.stdout').read_text()
    assert json.loads(raw) == record
    assert not (HERE/f'PR_{item["number"]}.stderr').read_text()
assert not (HERE/'CHECK.stderr').read_text()
assert not (HERE/'VERIFY_EVIDENCE.stderr').read_text()
artifacts = [identity(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name != 'FINAL_SEAL.json']
seal = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope': 'Post-source publication assembly/provenance review, reusing exact previously sealed mathematical evidence; no audit verdict.',
 'source_identities': sources, 'procedure_dependencies': procedures, 'artifact_identities': artifacts,
 'baseline_commit': 'c26b0171974c456f68dd92a4c8661ade1cc5ddbd',
 'concurrent_source_identity_recheck_passed': True,
 'scientific_suite_executions_during_review': 0,
 'no_actionable_assembly_findings': True,
 'source_or_git_mutations': []}
(HERE/'FINAL_SEAL.json').write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n')
print(json.dumps({'sources': len(sources), 'procedures':len(procedures), 'artifacts':len(artifacts),
 'report_sha256':sha((HERE/'REPORT.md').read_bytes()), 'seal_sha256':sha((HERE/'FINAL_SEAL.json').read_bytes())},indent=2))
