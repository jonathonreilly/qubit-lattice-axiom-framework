from pathlib import Path
import json,hashlib,subprocess,ast,difflib
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';P=R/'review-loop-efficiency-proposal-v1'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:{'path':str(p),'sha256':h(p)};git=lambda *a:subprocess.check_output(['git','-C',str(W),*a])
f=json.loads((R/'review-loop-efficiency-author-source-freeze-v1.json').read_text());base=f['base'];head=f['commit'];tree=f['tree']
assert git('rev-parse','HEAD').decode().strip()==head
assert git('rev-parse','origin/main').decode().strip()==base
assert git('rev-parse','HEAD^{tree}').decode().strip()==tree
assert not git('status','--porcelain')
assert git('rev-parse',head+'^').decode().strip()==base
assert set(git('diff','--name-only','--no-renames',base,head).decode().splitlines())=={x['path'] for x in f['paths']}
for x in f['paths']:
 assert h(W/x['path'])==x['sha256']
 assert hashlib.sha256(git('show',head+':'+x['path'])).hexdigest()==x['sha256']
 assert hashlib.sha256(git('show',base+':'+x['path'])).hexdigest()==x['before_sha256']
 assert (W/x['path']).read_bytes()==(P/'references'/Path(x['path']).name).read_bytes()
old=json.loads((R/'review-loop-efficiency-current-main-source-check-v1.json').read_text())
for x in old['files']:
 suffix=Path(x['path']).relative_to('/Users/jonBridger/.codex/skills/review-loop')
 assert hashlib.sha256(git('show',base+':docs/ai_methodology/skills/review-loop/'+str(suffix))).hexdigest()==x['sha256']
for x in json.loads((R/'review-loop-efficiency-review-v1.json').read_text())['references']:assert h(Path(x['path']))==x['sha256']
draft=json.loads((R/'review-loop-efficiency-author-unit-draft-v1.json').read_text())
for rows in draft['inputs'].values():
 for x in rows: assert h(W/x['path'])==x['sha256']
a=R/'enroll_process_receipt_v1.py';prior=R/'enroll_drain_receipt_v2.py';ast.parse(a.read_text())
delta=''.join(difflib.unified_diff(prior.read_text().splitlines(True),a.read_text().splitlines(True),fromfile=str(prior),tofile=str(a)))
(R/'review-loop-efficiency-process-adapter-reviewed-v1.diff').write_text(delta)
rationales={
 'REVIEW_UNITS.md':'Methodology for complete source recovery, frozen capture provenance and same-session/current-main validation. It asserts no scientific theorem, empirical result or retained status.',
 'OPERATIONS.md':'Archival naming preparation for the existing tracked-docs basename invariant. Operational storage guidance only, with no active scientific proof or claim adopted.',
 'FIXES_AND_REPORTING.md':'Review execution and evidence IO guidance, including rerunnable output, raw-result preservation and once-only limits. It makes no scientific conclusion.',
 'UNIT_RECEIPT.md':'Mechanical record category and checker-schema clarification. It does not certify science or confer audit standing.'}
rows=[dict(original_path=x['path'],original_sha256=x['sha256'],disposition='accepted unchanged from independently reviewed proposal',recovery='Exact constituent source in Git '+head+':'+x['path']+'; prechange bytes retained in Git '+base+':'+x['path'],final_path=x['path'],final_sha256=x['sha256']) for x in f['paths']]
report={
 'schema_version':1,'unit_id':f['unit_id'],'verdict':'FINAL_SOURCE_CONFIRMED_FOR_ENROLLMENT',
 'reviewer':{'session':'/root/review_efficiency_methodology','same_session':True,'role':'independent MethodologySkillReviewer'},
 'source':{'base':base,'commit':head,'tree':tree,'paths':[{'path':x['path'],'sha256':x['sha256']} for x in f['paths']]},
 'reviewed_current_main':base,
 'current_main_preservation':{'confirmed':True,'exact_parent':True,'complete_delta_exactly_four_reviewed_paths':True,'all_other_current_main_bytes_preserved':True,'all_15_methodology_baseline_files_unchanged_since_early_review':True,'semantic_confirmation':'Actual intervening main adds PR8032 source/archive/evidence and a companion runner map entry in both graph and packet APIs. Inspected both API deltas: each is one matching helper mapping, with parser/checker/output contracts unchanged. No interaction invalidates these process instructions or earlier isolated controls. Current-main science remains byte-preserved because the complete candidate delta is exactly the four accepted documentation edits.'},
 'constituents':[{'id':f['unit_id'],'head':head,'delta_base':base}],
 'original_dispositions':rows,
 'non_science_notes':[{'path':x['path'],'rationale':rationales[Path(x['path']).name],'sha256':x['sha256']} for x in f['paths']],
 'findings':[],
 'applicable_lenses':{'MethodologySkillReviewer':'PASS','RepoGovernanceReviewer':'PASS','CodeRunnerReviewer':'PASS for external identity-only adapter; no repository code changed'},
 'adapter_review':{'status':'ACCEPTED_FOR_THIS_PROCESS_ONLY_ENROLLMENT','source':ref(a),'prior_adapter':ref(prior),'diff':ref(R/'review-loop-efficiency-process-adapter-reviewed-v1.diff'),'conclusions':['Removes numeric-PR parsing and commit creation; uses existing exact committed source with empty PR list.','Requires empty science notes and supporting proofs, complete process disposition paths, matching full base-relative changed paths and exact committed tree.','Preserves record/preflight/source/input/evidence hash and clean-checkout requirements. Requires preflight cache_checked but executes no cache, runner, pipeline or audit.','Does not infer independent verdict: coordinator must use this final reviewed source and its valid final canonical preflight. Existing evidence is not restamped.'],'limitations':'Review is of this exact adapter for this four-file process unit. It is not a general source-preservation or reviewer-authenticity verifier; ordinary integration gates still apply.'},
 'controls_reused':{'unchanged_earlier_independent_controls':True,'science_executions':0,'cache_executions':0,'pipeline_executions':0,'source_edits':0,'new_controls':'Read-only Git object/delta/hash/clean-state comparisons and adapter AST parsing only.'},
 'references':[ref(R/x) for x in ['review-loop-efficiency-review-v1.json','review-loop-efficiency-review-v1.md','review-loop-efficiency-author-source-freeze-v1.json','review-loop-efficiency-independent-controls-v1.json','review-loop-efficiency-supplemental-controls-v1.json','review-loop-efficiency-author-unit-draft-v1.json','review-loop-efficiency-author-main-input-check-v1.json']],
 'boundary':'Final source confirmation permits enrollment of this exact commit/tree on actual reviewed main. Combined integration validation and landing remain required; no audit verdict or prospective approval of moved main.'}
q=R/'review-loop-efficiency-final-review-v1.json'
with q.open('x') as out:json.dump(report,out,indent=2);out.write('\n')
md=f'''# Review-loop efficiency final source confirmation

**Final source confirmed for enrollment; no material findings.** Original independent reviewer `/root/review_efficiency_methodology`, same session.

Commit `{head}`, tree `{tree}`, reviewed current main/base `{base}`. The complete Git delta contains exactly the four accepted reference updates with identical proposal hashes. All other current-main bytes are preserved. All 15 methodology baseline files still match the earlier review.

The intervening main change adds PR8032 material and two matching one-entry helper mappings; these preserve the checker/IO contracts used by the guidance. Earlier isolated controls remain valid and were not rerun. Four explicit non-science rationales and complete canonical original/final dispositions are in the JSON report. Prechange source remains recoverable from the exact Git base. All author-draft bound inputs match the actual checkout.

The process-only enrollment adapter is accepted for this unit: it keeps record/source/input/evidence checks, requires no science notes or supporting proofs and full process dispositions, preserves the existing exact commit, and fabricates no PR number. It executes no science or gate and makes no independent-review judgment. Its coordinator must bind the final canonical preflight and this report.

No source edits, science, cache or pipeline execution occurred. Combined integration validation and landing remain pending. This confirmation covers this actual main state, not future advances.
'''
with (R/'review-loop-efficiency-final-review-v1.md').open('x') as out:out.write(md)
print(json.dumps({'report':ref(q),'summary':ref(R/'review-loop-efficiency-final-review-v1.md')}))
