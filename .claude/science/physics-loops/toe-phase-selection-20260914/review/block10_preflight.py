"""Mechanical author preflight, not a scientific audit verdict."""
import hashlib
import json
import re
import sys
from pathlib import Path

root=Path('/Users/jonreilly/Documents/Codex/toe-periodic-clock-phase-20260914')
sys.path[:0]=[str(root/'scripts'),str(root/'docs/audit/scripts')]
import runner_cache
import forensic_evidence_readiness
import no_go_discipline_gate

note='docs/FINITE_CLOCK_SCORE_GAUSSIAN_MAXWELL_SCALING_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-14.md'
runner='scripts/finite_clock_score_gaussian_maxwell_scaling_limit_2026_09_14.py'
cache,header,body=runner_cache.load_cache(runner);manifest={}
no_go_discipline_gate.set_packet_evidence(manifest,path=note,role='source',text=(root/note).read_text())
no_go_discipline_gate.set_packet_evidence(manifest,path=runner,role='runner_stdout',text=body.split('----- stdout -----',1)[1].split('----- stderr -----',1)[0],invocation_bound_rendered_text=True)
source_issue=forensic_evidence_readiness._runner_source_issue(runner,root)
n5=forensic_evidence_readiness.live_manifest_readiness_issue(manifest)
assert source_issue is None and n5 is None,(source_issue,n5)
assert runner_cache.cache_status(runner)=='fresh'
assert header['status']=='ok'
head=body.split('----- stdout -----',1)[0]
timeout=int(re.search(r'^timeout_sec: (\d+)$',head,re.M).group(1))
elapsed=float(re.search(r'^elapsed_sec: ([\d.]+)$',head,re.M).group(1))
assert timeout==180
old='docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md'
assert hashlib.sha256((root/old).read_bytes()).hexdigest()=='bfedf452ec4e5b4b19c7099cb4c5e7ebc69aca4198fbdfba1c8788647ddea237'
fault=json.loads(Path(__file__).with_name('BLOCK10_MUTATIONS.json').read_text())
sha=hashlib.sha256((root/runner).read_bytes()).hexdigest()
assert fault['runner_sha256']==sha and len(fault['faults'])==26
record=dict(note=note,note_sha256=hashlib.sha256((root/note).read_bytes()).hexdigest(),runner=runner,runner_sha256=sha,cache_status='fresh',declared_timeout_sec=timeout,elapsed_sec=elapsed,runner_source_issue=source_issue,n5_live_readiness_issue=n5,detected_mutations=26,upstream_source_unchanged=True,qualification='Mechanical source/cache/N5 readiness and personal fault checks only; no independent review or audit verdict.')
Path(__file__).with_name('BLOCK10_PREFLIGHT.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
