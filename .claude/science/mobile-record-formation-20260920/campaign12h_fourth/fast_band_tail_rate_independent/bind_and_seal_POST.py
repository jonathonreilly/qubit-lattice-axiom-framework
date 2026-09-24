#!/usr/bin/env python3
"""Read-only authentication and owned-directory POST sealing; no science replay."""
from pathlib import Path
import hashlib,json,datetime,shutil
HERE=Path(__file__).resolve().parent;D=HERE.parent;RAW=D.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
PRE='84f629be9deb702e119a333fc8ae85d940586f4493ebd86405a0a215f61600d7'
assert not (HERE/'FINAL_SEAL.json').exists(),'Do not overwrite a frozen final seal'
assert sha(HERE/'PRE_SEAL.json')==PRE
pre=json.loads((HERE/'PRE_SEAL.json').read_text());assert len(pre['files'])==27
for row in pre['files']:
 p=HERE/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
releases=[
 ('fast_band_tail_rate_author/ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND.md','a8cbb5fa4f71f4fde6644a1242ef1741799c701c2ce8835b5da42b46c5075745','released analytic rate proof, read in full'),
 ('fast_band_tail_rate_author/AUTHOR_SEAL.json','3a8305a55aaef7feb91ab07499b3c2c70059d1f3b7bf9a66d84fe5863f2082a4','released rate-author seal, read in full'),
 ('fast_band_tail_independent/POST_COMPARISON.md','bf40d648eedecf994ad8668cbb9c647f36323940c03b43674f99061c06f2ef75','completed full-fiber comparison report, read in full; complete source audit reused'),
 ('fast_band_tail_independent/FINAL_SEAL.json','f3922528290f8f2f8d72e0b5cd230ab9586b1400d6b2cd8e90e7d55ae36c5fff','completed full-fiber comparison seal identity/scope'),
]
rows=[]
for alias,digest,role in releases:
 p=D/alias;assert sha(p)==digest,(alias,sha(p));dest=HERE/'post_sources'/alias;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 rows.append({'source_alias':alias,'snapshot':str(dest.relative_to(HERE)),'sha256':digest,'bytes':dest.stat().st_size,'role':role})
author=json.loads((HERE/rows[1]['snapshot']).read_text())
for artifact in author['artifacts']:
 p=HERE/'post_sources/fast_band_tail_rate_author'/artifact['path'];assert sha(p)==artifact['sha256'] and p.stat().st_size==artifact['bytes']
prior=json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
by_alias={row['source_alias']:row for row in prior['sources']}
reused=[]
prefix='.claude/science/mobile-record-formation-20260920/campaign12h_fourth/'
for row in author['sources']:
 assert row['path'].startswith(prefix)
 alias=row['path'][len(prefix):];bound=by_alias[alias];assert bound['sha256']==row['sha256']
 assert sha(HERE/bound['snapshot'])==row['sha256']
 # Also authenticate the released current source bytes without changing them.
 assert sha(RAW/row['path'])==row['sha256']
 reused.append({'source_alias':alias,'PRE_snapshot':bound['snapshot'],'sha256':row['sha256']})
manifest={'stage':'bounded POST analytic source comparison','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_seal_sha256':PRE,'PRE_files_authenticated_unchanged':27,'released_sources':rows,'root_bound_dependencies_reused_from_PRE':reused,'verification_scope':'Authenticate this PRE, the complete one-note rate-author packet, all four root-bound source identities, and the newly released predecessor comparison report/seal. Does not repeat all68 predecessor evidence bindings.','portability':'Relative scientific aliases plus exact hashes are authoritative. Public projection omissions of historical instructions require explicit provenance omissions.'}
(HERE/'POST_SOURCE_BINDINGS.json').write_text(json.dumps(manifest,indent=2)+'\n')
receipt={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_files_authenticated_unchanged':27,'root_rate_artifacts_authenticated':len(author['artifacts']),'root_rate_dependencies_authenticated':len(reused),'new_release_snapshots_authenticated':len(rows),'source_binding_sha256':sha(HERE/'POST_SOURCE_BINDINGS.json'),'scientific_activity':'Full analytic comparison of algebraic simplicity, complete derivative cancellation, quadratic eigenvalue bound, bounded projection and physical five-ball integral. No new numerics or author replay.','mathematical_corrections_required':[],'unresolved_execution_failures':[]}
(HERE/'POST_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
files=[]
for p in sorted(HERE.rglob('*')):
 if p.is_file():
  assert not p.is_symlink() and '__pycache__' not in p.parts
  files.append({'path':str(p.relative_to(HERE)),'bytes':p.stat().st_size,'sha256':sha(p)})
seal={'stage':'complete bounded POST source comparison','sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_seal_sha256':PRE,'PRE_files_authenticated_unchanged':27,'root_rate_note_sha256':releases[0][1],'root_rate_author_seal_sha256':releases[1][1],'completed_tail_comparison_report_sha256':releases[2][1],'completed_tail_comparison_seal_sha256':releases[3][1],'report':'POST_COMPARISON.md','report_sha256':sha(HERE/'POST_COMPARISON.md'),'status':'POST_STATUS.md','scope_supported':['For the three stipulated zero-field actual first-mark rotor curves and fixed delta,kappa>0, f_i(tau)>=c_i(1+tau)^(-5/2) with c_i>0.','No eventual upper bound A exp(-a tau) exists for these fixed limiting curves, with finite A,a>0.','The root full-complex-eigenvalue derivative/Taylor route is valid from the identically zero dark block.','The distinct immutable PRE dissipative-form and weaker Duhamel routes remain separately attributed.','The preceding full physical tail theorem is reused within its completed scoped comparison, not re-audited.'],'excluded':['Sharp asymptotic, matching upper rate, optimal exponent/constants or complete exceptional-set classification.','Arbitrary-input/universal-physics no-go, change of original marks or tau-dependent replacement input.','Fixed-positive-physical-time microscopic result, finite-spin infinite-time result, exchanged limits, heat/bath/reservoir/selection conclusion.','Formal audit or retained status, publication/landing approval, editable-prompt or platform-instruction change.'],'mathematical_corrections_required':[],'scientific_discrepancies':[],'new_scientific_numerical_executions':0,'unresolved_execution_failures':[],'retained_history':'PRE has no failed executions. Completed dependencies retain their documented failed historical executions and auxiliary floating comparison; these were not relabeled as successes.','files':files}
(HERE/'FINAL_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
for row in files:
 p=HERE/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
print(json.dumps({'final_seal_sha256':sha(HERE/'FINAL_SEAL.json'),'report_sha256':seal['report_sha256'],'bound_files':len(files),'PRE_files_unchanged':27,'new_sources':len(rows),'reused_root_source_identities':len(reused),'mathematical_corrections_required':[]},indent=2))
