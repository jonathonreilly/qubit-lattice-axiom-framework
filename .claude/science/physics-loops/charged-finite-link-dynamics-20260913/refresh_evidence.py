from pathlib import Path
import sys,gzip,json,hashlib,re,py_compile
root=Path(__file__).resolve().parents[4];sys.path.insert(0,str(root/'scripts'));sys.path.insert(0,str(root/'docs/audit/scripts'))
import runner_cache,forensic_evidence_readiness as ready
p=Path(__file__).resolve().parent;runner='scripts/charged_finite_link_local_dynamics_and_phase_bridge_2026_09_13.py';note='docs/CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md'
result,cache=runner_cache.execute_and_write_cache(runner,timeout_sec=90)
(p/'CANONICAL_EXECUTION.json').write_text(json.dumps(result,indent=2)+'\n');assert result['status']=='ok' and result['exit_code']==0 and cache is not None
(p/'canonical_runner_cache.txt.gz').write_bytes(gzip.compress(cache.read_bytes(),mtime=0))
row=dict(claim_id='charged_finite_link_local_dynamics_and_phase_bridge_bounded_theorem_note_2026-09-13',claim_type='bounded_theorem',runner_path=runner,note_path=note)
info=dict(note_sha256=hashlib.sha256((root/note).read_bytes()).hexdigest(),runner_sha256=hashlib.sha256((root/runner).read_bytes()).hexdigest(),runner_source_issue=ready._runner_source_issue(runner,root),cached_row_readiness_issue=ready.cached_row_readiness_issue(row,{},repo_root=root),cache_status=runner_cache.cache_status(runner))
(p/'SOURCE_READINESS.json').write_text(json.dumps(info,indent=2)+'\n');print(json.dumps(info));assert info['runner_source_issue'] is None and info['cached_row_readiness_issue'] is None
py_compile.compile(str(root/runner),doraise=True)
prose=re.sub(r'```.*?```','',(root/note).read_text(),flags=re.S);links=re.findall(r'\]\(([^)]+)\)',prose);local=[v for v in links if not re.match(r'https?://',v)];assert all((root/note).parent.joinpath(v.split('#')[0]).exists() for v in local)
(p/'FOCUSED_VALIDATION.json').write_text(json.dumps(dict(primary_compile='passed',relative_source_links=local,all_relative_source_links_exist=True,full_integrated_pipeline='pending',strict_integrated_lint='pending',independent_review='pending',formal_audit='pending'),indent=2)+'\n')
review=p/'AUTHOR_REVIEW.md';s=review.read_text();s=re.sub(r'Final note SHA256: [a-f0-9]+\.',f"Final note SHA256: {info['note_sha256']}.",s);s=re.sub(r'canonical runtime [0-9.]+ seconds',f"canonical runtime {result['elapsed_sec']} seconds",s);review.write_text(s)
