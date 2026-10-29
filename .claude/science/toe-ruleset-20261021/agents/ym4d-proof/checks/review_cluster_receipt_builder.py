#!/usr/bin/env python3
"""Bind this review's actual frozen reads and evidence; no science/status authority."""
from pathlib import Path
import hashlib,json,subprocess,datetime,platform
R=Path.cwd()
L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
SCI='962f97c259d8c241df632a07e27f498f4ad33b09'
METH='ca2bc7ddf64790da96cd43d42017d000fbfe4808'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args])
def source(rev,path,ranges,role):
    data=git('show',rev+':'+path)
    return dict(revision=rev,path=path,git_blob=git('rev-parse',rev+':'+path).decode().strip(),
        bytes=len(data),sha256=sha(data),line_count=len(data.splitlines()),
        read_coverage=ranges,role=role)
reads=[]
for name in ['RECOVERY_CLUSTER_ASTRA.md','checks/recovery_cluster_exact.py','checks/recovery_cluster_results.json',
             'checks/recovery_cluster_receipt.json','recovery_20261029/continuations.json']:
    reads.append(source(SCI,str(L/name),'complete','Frozen reviewed unit and exact source/evidence provenance; criteria embedded in note'))
context={
 'STEP55.md':[[243,277],[312,376],[470,543],[656,697]],
 'CODEX_REVIEW_STEP.md':[[108,215]],
 'PROOF.md':[[5660,5845]],
 'BFT34_55.md':[[98,131],[229,307]],
 'SRC2_55.md':[[389,430],[633,748]],
 'B2_55.md':[[273,292],[323,357],[426,435]],
 'CODEX_REVIEW_B2.md':[[116,160]],
 'CODEX_REVIEW_SRC2.md':[[22,53],[108,125]],
 'LINEAR_PACKAGE.md':[[290,329]],
}
for name,ranges in context.items():
    reads.append(source(SCI,str(L/name),ranges,
        'Necessary original premises/arguments for source-coverage ledger; not blanket certification of these files'))
methods=['AGENTS.md','docs/ai_methodology/SCIENCE_WORKFLOW.md',
 'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
 'docs/ai_methodology/skills/review-loop/SKILL.md',
 'docs/ai_methodology/skills/review-loop/references/REVIEW_SETUP.md',
 'docs/ai_methodology/skills/review-loop/references/REVIEW_UNITS.md',
 'docs/ai_methodology/skills/review-loop/references/SCIENCE_LENSES.md',
 'docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md',
 'docs/ai_methodology/skills/review-loop/references/AUDIT_COMPATIBILITY.md',
 'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',
 'docs/ai_methodology/skills/no-go-discipline/SKILL.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
 'docs/audit/data/axiom_premise_nodes.json']
for name in methods:
    reads.append(source(METH,name,'complete','Methodology/authority boundary; not a physics premise for the generic theorem'))
original=git('show',SCI+':'+str(L/'RECOVERY_CLUSTER_ASTRA.md'))
corrected=(L/'RECOVERY_CLUSTER_ASTRA.md').read_bytes()
needle=b'neighborhood of D (or the bounds hold on all compact subdomains). Define'
replacement=b'neighborhood of D (or the bounds hold on all compact subdomains). Fix\n**\xce\xb2\xe2\x89\xa50** for the support norms and operator lemma below. Define'
assert original.count(needle)==1
assert corrected==original.replace(needle,replacement)
assert sha(corrected)=='9c9264bd4d92b60798e48ccd2eb0ff230e221c3ffd2107c0f6443ec86de563cf'
manifest={'frozen_science_revision':SCI,'methodology_revision':METH,'reads':reads,
 'science_read_policy':'Git object reads only, except exact coordinator beta-domain correction explicitly requested and confirmed',
 'excluded_evolving_source':'SOURCE_LOCAL_RETURN_ASTRA.md was not read or used',
 'corrected_source':{'path':str(L/'RECOVERY_CLUSTER_ASTRA.md'),'bytes':len(corrected),'sha256':sha(corrected),
    'coverage':'Complete original source plus exhaustive exact-byte comparison proving the only change is beta >= 0',
    'finding_id':'Cluster-domain-1','same_reviewer_fix_confirmation':True},
 'fix_provenance':{'path':str(L/'checks/full_proof_cluster_fix.json'),
    'sha256':sha((L/'checks/full_proof_cluster_fix.json').read_bytes()),
    'role':'Coordinator-authored repair record read as provenance; source bytes independently compared'},
 'coverage_note':'Read coverage is an honest reviewer record, not a machine proof that semantic reading occurred.'}
mp=L/'checks/review_cluster_source_manifest.json'
mp.write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
evidence=[]
for path in [L/'REVIEW_RECOVERY_CLUSTER_ASTRA.md']+sorted((L/'checks').glob('review_cluster_*')):
    if path.name=='review_cluster_receipt.json' or not path.is_file():continue
    data=path.read_bytes()
    evidence.append(dict(path=str(path),bytes=len(data),sha256=sha(data)))
ind=json.loads((L/'checks/review_cluster_01_out.json').read_text())
author=json.loads((L/'checks/review_cluster_author_controls_out.json').read_text())
receipt={'schema_version':1,'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Scoped independent mathematical source review only; no audit or whole-PR/landing PASS',
 'reviewer_context':'/root/review_cluster','requested_configuration':{'model':'gpt-6-astra','reasoning_effort':'max','fork_turns':'none'},
 'configuration_evidence':'Parent dispatch/task brief; no separate runtime identity attestation',
 'independence':'Same-family/fresh-context; independent derivation and implementation; no authorship of reviewed theorem',
 'frozen_science_revision':SCI,'frozen_science_tree':git('rev-parse',SCI+'^{tree}').decode().strip(),
 'methodology_revision':METH,'original_note_sha256':sha(original),
 'confirmed_corrected_note_sha256':sha(corrected),
 'source_manifest_path':str(mp),'source_manifest_sha256':sha(mp.read_bytes()),
 'final_disposition':'Generic theorem and stated sufficient regimes supported after beta-domain correction; actual Yang--Mills inputs and full T_OS remain unestablished by this unit',
 'findings':[{'id':'Cluster-domain-1','original':'Missing beta >= 0 domain','disposition':'Corrected by coordinator; confirmed in same reviewer context','original_counterexample_preserved':True}],
 'independent_checks':{'script':str(L/'checks/review_cluster_01.py'),'sha256':sha((L/'checks/review_cluster_01.py').read_bytes()),
   'named_checks':len(ind['checks']),'all_checks_pass':ind['all_checks_pass'],
   'named_controls':len(ind['controls']),'all_mutations_detected':ind['all_mutations_detected'],
   'python':ind['python'],'sympy':ind['sympy'],'stdout_sha256':sha((L/'checks/review_cluster_01_out.json').read_bytes()),
   'stderr_sha256':sha((L/'checks/review_cluster_01_err.txt').read_bytes()),'observed_exit_code':0},
 'author_reproduction':{'exact_stdout_replay':author['exact_author_replay'],'observed_replay_exit_code':author['runs'][0]['exit_code'],
   'all_six_mutations_detected':author['all_six_author_mutations_detected'],
   'negative_controls':'Six mutant exit-code-1 runs and all outputs retained; no unexpected failure'},
 'operations':{'git_mutations':0,'commits':0,'pushes':0,'PR_calls':0,'full_pipeline_runs':0,'audit_worker_runs':0,
   'source_fix_author':'coordinator','same_context_fix_confirmations':1},
 'unperformed_gates':'Whole-PR source disposition/current-main preservation/combined pipeline/strict lint/changed-evidence/landing are coordinator scope',
 'report':{'path':str(L/'REVIEW_RECOVERY_CLUSTER_ASTRA.md'),'sha256':sha((L/'REVIEW_RECOVERY_CLUSTER_ASTRA.md').read_bytes())},
 'artifacts':evidence}
p=L/'checks/review_cluster_receipt.json';p.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps({'report_sha256':receipt['report']['sha256'],'receipt_sha256':sha(p.read_bytes()),
 'source_manifest_sha256':sha(mp.read_bytes()),'corrected_note_sha256':sha(corrected),
 'artifact_count':len(evidence),'read_source_count':len(reads)},indent=2))
