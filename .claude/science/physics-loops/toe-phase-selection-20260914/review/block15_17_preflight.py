"""Author mechanical evidence readiness, not an audit verdict."""
import hashlib,json,re,sys
from pathlib import Path
root=Path('/Users/jonreilly/Documents/Codex/toe-coupled-defect-convexity-20260915')
sys.path[:0]=[str(root/'scripts'),str(root/'docs/audit/scripts')]
import runner_cache,forensic_evidence_readiness,no_go_discipline_gate
specs=[
(17,'FREE_CUBIC_MAGNETIC_LOCAL_FILLINGS_AND_POSITIVE_ELECTRIC_CURRENT_CONVEX_EXTENSION_BOUNDED_THEOREM_NOTE_2026-09-15.md','free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_2026_09_15.py',16,4),
(15,'CARRIER_PRESERVING_CLOSED_INTEGER_CHARGE_GAS_CONVEXIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md','carrier_preserving_closed_integer_charge_gas_convexification_2026_09_15.py',16,6),
(16,'FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-09-15.md','finite_clock_exact_coupled_electric_magnetic_defect_representation_2026_09_15.py',13,2)]
for block,n,r,count,families in specs:
 note='docs/'+n;runner='scripts/'+r
 cache,header,body=runner_cache.load_cache(runner);stdout=body.split('----- stdout -----',1)[1].split('----- stderr -----',1)[0];m={}
 no_go_discipline_gate.set_packet_evidence(m,path=note,role='source',text=(root/note).read_text())
 no_go_discipline_gate.set_packet_evidence(m,path=runner,role='runner_stdout',text=stdout,invocation_bound_rendered_text=True)
 issue=forensic_evidence_readiness._runner_source_issue(runner,root);n5=forensic_evidence_readiness.live_manifest_readiness_issue(m)
 assert issue is None and n5 is None,(issue,n5)
 assert runner_cache.cache_status(runner)=='fresh' and header['status']=='ok'
 prefix=body.split('----- stdout -----',1)[0];budget=int(re.search(r'^timeout_sec: (\d+)$',prefix,re.M).group(1));elapsed=float(re.search(r'^elapsed_sec: ([\d.]+)$',prefix,re.M).group(1));assert budget==180
 faults=json.loads(Path(__file__).with_name(f'BLOCK{block}_MUTATIONS.json').read_text());sha=hashlib.sha256((root/runner).read_bytes()).hexdigest()
 assert faults['runner_sha256']==sha and len(faults['faults'])==count and all(f['detected'] for f in faults['faults'])
 record=dict(note=note,note_sha256=hashlib.sha256((root/note).read_bytes()).hexdigest(),runner=runner,runner_sha256=sha,cache_status='fresh',elapsed_sec=elapsed,declared_timeout_sec=budget,runner_source_issue=issue,n5_live_readiness_issue=n5,detected_mutations=count,qualification='Personal fault challenges and mechanical source/cache/N5 readiness; independent review and formal audit pending.')
 Path(__file__).with_name(f'BLOCK{block}_PREFLIGHT.json').write_text(json.dumps(record,indent=2)+'\n')
 data=json.JSONDecoder().raw_decode(stdout[stdout.index('{'):])[0];assert len(data)==families
 Path(__file__).parents[1].joinpath(f'BLOCK{block}_CHECKS.json').write_text(json.dumps(dict(runner_sha256=sha,finite_families=data,qualification=record['qualification']),indent=2)+'\n')
 print(json.dumps(record,indent=2))
