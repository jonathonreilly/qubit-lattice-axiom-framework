#!/usr/bin/env python3
"""Bind the completed read-only mathematical review; no science is rerun."""
import hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
assert Path.cwd()==ROOT
L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C=L/'checks'
SCI='0ea4e56c4c00da4e70863eb274cbee987b7bd917'
METH='ca2bc7ddf64790da96cd43d42017d000fbfe4808'
FINAL='2eee991e4e4546aa3ed10ad0ffe40d840c5347a002d623aac47b2fc515fd7769'
def sha(data):return hashlib.sha256(data).hexdigest()
def blob(rev,path):return subprocess.check_output(['git','show',rev+':'+str(path)])
def fileinfo(path):
 data=Path(path).read_bytes()
 return {'path':str(path),'bytes':len(data),'lines':len(data.splitlines()),'sha256':sha(data)}
def readinfo(path,rev=None,ranges=None,description=''):
 data=blob(rev,path) if rev else Path(path).read_bytes()
 lines=data.splitlines(keepends=True)
 if ranges is None:ranges=[[1,len(lines)]]
 for a,b in ranges:assert 1<=a<=b<=len(lines),(path,a,b,len(lines))
 covered=[]
 for a,b in ranges:
  value=b''.join(lines[a-1:b]);covered.append({'first_line':a,'last_line':b,'sha256':sha(value),'bytes':len(value)})
 return {'path':str(path),'revision':rev or 'working_tree','sha256':sha(data),'total_lines':len(lines),'coverage_kind':'complete' if ranges==[[1,len(lines)]] else 'partial','read_ranges':covered,'description':description}
method_paths=[
 'AGENTS.md','docs/ai_methodology/SCIENCE_WORKFLOW.md',
 'docs/ai_methodology/skills/review-loop/SKILL.md',
 'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
 'docs/ai_methodology/skills/review-loop/references/REVIEW_SETUP.md',
 'docs/ai_methodology/skills/review-loop/references/REVIEW_UNITS.md',
 'docs/ai_methodology/skills/review-loop/references/SCIENCE_LENSES.md',
 'docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md',
 'docs/ai_methodology/skills/review-loop/references/AUDIT_COMPATIBILITY.md',
 'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
 'docs/audit/data/axiom_premise_nodes.json',
]
coverage=[readinfo(p,METH,description='Current-main governing context; complete content read.') for p in method_paths]
coverage.append(readinfo('/Users/jonBridger/.codex/skills/review-loop/SKILL.md',description='Installed entry read; current-main instructions supersede if different.'))
for name in ['SOURCE_LOCAL_RETURN_ASTRA.md','checks/source_return_exact.py','checks/source_return_results.json','checks/source_return_receipt.json']:
 coverage.append(readinfo(L/name,SCI,description='Original frozen review unit or author check evidence; completely read.'))
partials={
 'PROOF.md':[[1410,1456],[2790,2850],[2990,3125],[3270,3465],[5450,5873]],
 'STEP55.md':[[241,390],[419,543],[656,697]],
 'CODEX_REVIEW_STEP.md':[[1,215]],
 'CODEX_REVIEW_SRC2.md':[[22,39],[108,125]],
 'CODEX_REVIEW_B2.md':[[116,160]],
 'SRC2_55.md':[[389,430],[650,663],[687,701]],
 'B2_55.md':[[335,354]],
 'RECOVERY_CLUSTER_ASTRA.md':[[1,276],[344,368]],
}
for name,ranges in partials.items():coverage.append(readinfo(L/name,SCI,ranges,'Affected context ranges read completely; no whole-file coverage claimed.'))
coverage.append(readinfo(L/'SOURCE_LOCAL_RETURN_ASTRA.md',description='Complete original source, full 855-line f7af9a3a corrected source, then complete final two-line dimension-label diff; reconstructed complete final coverage.'))
coverage.append(readinfo(L/'REVIEW_RECOVERY_CLUSTER_ASTRA.md',description='Complete final sibling review read; exact source and receipt hashes independently verified.'))
coverage_payload={'science_revision':SCI,'methodology_revision':METH,'records':coverage,'recovery_notes':['Initially truncated reads were recovered in explicit complete chunks.','Size-only inventories and search hits do not count as full source reads.','Final generic source is not claimed fully reread by this reviewer; its independent frozen sibling review supplies that dependency.']}
coverage_path=C/'review_source_return_coverage.json'
coverage_path.write_text(json.dumps(coverage_payload,indent=2,ensure_ascii=False)+'\n')
syntax=[]
for p in sorted(C.glob('review_source_return_*.py')):
 compile(p.read_text(),str(p),'exec')
 syntax.append({'path':str(p),'sha256':sha(p.read_bytes()),'compiled':True})
syntax_path=C/'review_source_return_syntax.json'
syntax_path.write_text(json.dumps({'method':'Python compile(source, filename, exec); no bytecode files, no science execution','checks':syntax,'all_passed':all(r['compiled'] for r in syntax)},indent=2)+'\n')
assert sha((L/'SOURCE_LOCAL_RETURN_ASTRA.md').read_bytes())==FINAL
expected={
 'RECOVERY_CLUSTER_ASTRA.md':'9c9264bd4d92b60798e48ccd2eb0ff230e221c3ffd2107c0f6443ec86de563cf',
 'REVIEW_RECOVERY_CLUSTER_ASTRA.md':'f3b3c8baed4e53cf4f3213342b97e51587576b59be4fb8d61fc3cbb3565dc2a0',
 'checks/review_cluster_receipt.json':'5f6dc6642e0b28db9a7ca71cab9852aa70deb3ba9c3a7a57224d5b5bd497e3d4',
}
for name,digest in expected.items():assert sha((L/name).read_bytes())==digest
out02=json.loads((C/'review_source_return_02_out.json').read_text())
out03=json.loads((C/'review_source_return_03_out.json').read_text())
mutants=json.loads((C/'review_source_return_author_controls_out.json').read_text())
assert out02['all_passed'] and len(out02['checks'])==28 and len(out02['controls'])==16
assert out03['all_passed'] and len(out03['checks'])==4
assert len(mutants['records'])==6
assert sum(x['all_passed'] is True for x in mutants['records'])==3
assert sum(x['exit_code']==1 for x in mutants['records'])==3
assert (C/'review_source_return_01_err.txt').stat().st_size>0
assert (C/'review_source_return_02_err.txt').stat().st_size==0
assert (C/'review_source_return_03_err.txt').stat().st_size==0
report=L/'REVIEW_SOURCE_LOCAL_RETURN_ASTRA.md'
receipt=C/'review_source_return_receipt.json'
now=datetime.now(timezone.utc)
start=datetime.fromisoformat('2026-10-29T12:35:53.989453+00:00')
evidence=[fileinfo(p) for p in sorted(C.glob('review_source_return_*')) if p.is_file() and p!=receipt]
record={
 'frozen_at_utc':now.isoformat(),
 'review_contract_recorded_at_utc':start.isoformat(),
 'elapsed_wall_seconds_since_contract':(now-start).total_seconds(),
 'unit':'PR #10114 / SOURCE_LOCAL_RETURN_ASTRA.md §§1–4',
 'requested_model_effort':'Astra/max; coordinator-provided task selection, not independently attested runtime metadata',
 'independence':'same-family fresh reviewer context, separate from author; not a cross-family audit',
 'science_baseline':SCI,'methodology_revision':METH,
 'original_source_sha256':'7da909685242b9c9f13e597a641e337d5928f5905211392b154e8f3649bda1ca',
 'intermediate_full_read_source_sha256':'f7af9a3ab9db86a939dbc313367f4d50145007a821d09b62aa67b358eb8adbfc',
 'final_source':fileinfo(L/'SOURCE_LOCAL_RETURN_ASTRA.md'),
 'report':fileinfo(report),'coverage':fileinfo(coverage_path),
 'generic_dependency':[fileinfo(L/name) for name in expected],
 'review_iterations':{'initial':1,'paired_scope_precision_fix_confirmations':2,'dimension_label_fix_confirmation':1},
 'findings':{'source_findings':5,'source_findings_fixed':5,'source_findings_skipped':0,'author_checker_sensitivity_observations':3,'reviewer_execution_failure_preserved':1},
 'successful_independent_checks':{'attempt_02_predicates':28,'attempt_02_controls':16,'attempt_03_incidence_predicates_including_omission_control':4},
 'author_mutations':{'total':6,'rejected':3,'survived':['missing_collar','common_logdet_half','missing_marked_right'],'source_unchanged':True},
 'syntax':fileinfo(syntax_path),
 'evidence':evidence,
 'disposition':'PASS WITH BOUNDED CLAIMS for this source unit only, on its explicit finite-volume level-zero domains.',
 'not_certified':['whole PR','audit PASS','normalized complex face/history return bound','all-coarse-field coverage','arbitrary holes/holonomies outside the specified domain','higher-level induction','E_cb equals E_NA','full Euclidean SU(N) existence on R4','OS0–OS3','physical Yang–Mills mass gap'],
 'operations':{'reviewer_git_mutations':0,'reviewer_commits':0,'pr_operations':0,'full_pipelines':0,'integration_retries':0,'audit_authority_edits':0,'autonomous_daemons':0},
 'combined_gates_and_landing':'Coordinator responsibility; no unit claim of completed combined gates or landed SHA.',
 'skipped_checks':['Unchanged author baseline already exactly reproduced by coordinator, not rerun for bookkeeping.','No full 4D nonabelian Hessian numerical construction.','No full continuum or physical mass-gap verification.','No full historical PROOF.md or generic source re-review beyond recorded ranges and frozen sibling dependency.'],
 'freeze_note':'Receipt omits its own hash; supplied separately to coordinator. All failed checks and surviving mutants retained.'
}
receipt.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'source_sha256':FINAL,'report':fileinfo(report),'receipt':fileinfo(receipt),'coverage':fileinfo(coverage_path),'evidence_files':len(evidence),'elapsed_wall_seconds_since_contract':record['elapsed_wall_seconds_since_contract']},indent=2))
