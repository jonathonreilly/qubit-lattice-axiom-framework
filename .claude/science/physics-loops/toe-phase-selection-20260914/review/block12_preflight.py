"""Mechanical source/cache preflight only, not an audit verdict."""
import hashlib
import json
import re
import sys
from pathlib import Path

root=Path('/Users/jonreilly/Documents/Codex/toe-direct-clock-wilson-20260914')
sys.path[:0]=[str(root/'scripts'),str(root/'docs/audit/scripts')]
import runner_cache
import forensic_evidence_readiness
import no_go_discipline_gate

note='docs/FINITE_CLOCK_LOGARITHMIC_MAXWELL_SCALING_AND_GLOBAL_DEFECT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-14.md'
runner='scripts/finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py'
cache,header,body=runner_cache.load_cache(runner);manifest={}
stdout=body.split('----- stdout -----',1)[1].split('----- stderr -----',1)[0]
no_go_discipline_gate.set_packet_evidence(manifest,path=note,role='source',text=(root/note).read_text())
no_go_discipline_gate.set_packet_evidence(manifest,path=runner,role='runner_stdout',text=stdout,invocation_bound_rendered_text=True)
source_issue=forensic_evidence_readiness._runner_source_issue(runner,root)
n5=forensic_evidence_readiness.live_manifest_readiness_issue(manifest)
assert source_issue is None and n5 is None
assert runner_cache.cache_status(runner)=='fresh' and header['status']=='ok'
head=body.split('----- stdout -----',1)[0]
timeout=int(re.search(r'^timeout_sec: (\d+)$',head,re.M).group(1));assert timeout==180
elapsed=float(re.search(r'^elapsed_sec: ([\d.]+)$',head,re.M).group(1))
fault=json.loads(Path(__file__).with_name('BLOCK12_MUTATIONS.json').read_text())
sha=hashlib.sha256((root/runner).read_bytes()).hexdigest()
assert fault['runner_sha256']==sha and len(fault['faults'])==25
record=dict(note=note,note_sha256=hashlib.sha256((root/note).read_bytes()).hexdigest(),runner=runner,runner_sha256=sha,cache_status='fresh',declared_timeout_sec=timeout,elapsed_sec=elapsed,runner_source_issue=source_issue,n5_live_readiness_issue=n5,detected_mutations=25,qualification='Mechanical source/cache/N5 readiness and personal fault challenges only. Independent proof review and formal audit pending.')
Path(__file__).with_name('BLOCK12_PREFLIGHT.json').write_text(json.dumps(record,indent=2)+'\n')
data=json.JSONDecoder().raw_decode(stdout[stdout.index('{'):])[0]
assert len(data)==7
Path(__file__).parents[1].joinpath('BLOCK12_CHECKS.json').write_text(json.dumps(dict(runner_sha256=sha,finite_families=data,qualification=record['qualification']),indent=2)+'\n')
print(json.dumps(record,indent=2))
