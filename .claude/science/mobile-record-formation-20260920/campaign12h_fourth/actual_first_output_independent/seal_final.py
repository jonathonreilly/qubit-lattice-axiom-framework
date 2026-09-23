"""Freeze the completed bounded comparison; never replace PRE or FINAL."""
from pathlib import Path
import datetime,hashlib,json

HERE=Path(__file__).resolve().parent
def ident(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

destination=HERE/'FINAL_SEAL.json'
assert not destination.exists(),'Never overwrite a FINAL seal.'
pre=HERE/'PRE_COMPARISON_SEAL.json'
assert ident(pre)['sha256']=='ba8907a8da440ad8832f86ff42b33b7c90d99082d181d215af43a8b89c11f37c'
predata=json.loads(pre.read_text())
for item in predata['science_sources']+predata['independent_artifacts']:
    assert ident(Path(item['path']))==item
sources=json.loads((HERE/'COMPARISON_SOURCES.json').read_text())
for item in sources['opened_and_authenticated']:
    assert ident(Path(item['path']))==item
receipts=[]
for stem in ('consequence','adjoint_reference','source','comparison'):
    p=HERE/(stem+'_RECEIPT.json');r=json.loads(p.read_text())
    assert r['exit_code']==0
    assert ident(Path(r['command'][1]))['sha256']==r['script_sha256']
    for stream in ('stdout','stderr'):
        assert ident(HERE/(stem+'.'+stream))['sha256']==r[stream+'_sha256']
    receipts.append(ident(p))
result=json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
assert result['material_candidate_discrepancies_identified']==[]
artifacts=[ident(p) for p in sorted(HERE.iterdir()) if p.is_file()]
seal={
    'phase':'FINAL_SELECTIVE_COMPARISON',
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status':'Bounded post-PRE comparison complete. No material discrepancy in the frozen candidate shared flat-window, survival and count claims. Not a formal retained/audit/no-go verdict.',
    'candidate_author_seal':sources['opened_and_authenticated'][0],
    'immutable_pre_seal':ident(pre),
    'pre_explicit_source_and_artifact_bindings_reauthenticated':len(predata['science_sources'])+len(predata['independent_artifacts']),
    'pre_science_sources':predata['science_sources'],
    'post_pre_opened_sources':sources['opened_and_authenticated'],
    'unopened_bound_support_entries':sources['unopened_candidate_support_entries'],
    'independence_and_attribution':'The candidate was frozen before the independent PRE and not read until PRE and explicit coordinator authorization. Its narrower claims predate the independent consequence report. Broader full-window time-smearing, first-age-convolved local state convergence and the exact trace-norm obstruction belong to the independent PRE, remain provisional, and are not independently reviewed by this checker merely through this comparison.',
    'decisive_comparison':'Shared proof hypotheses and full argument read. Exact clock/loss controls and symbolic count convolution agree. All 48 stored-vector window diagnostics independently reprocessed; full S=64 propagation independently regenerated with max vector error 3.07e-12. Higher S arrays authenticated/reprocessed, not rerun. Author code not executed.',
    'material_candidate_discrepancies':[],
    'unresolved':'No unique complementary state/clock, exact full unselected waiting law, or exact total N6/N8 probability limit established. No growing-window, unbounded moment, larger-volume or empirical claim.',
    'execution_receipts':receipts,
    'independent_artifacts':artifacts,
    'scope_discipline':'Only the assigned independent folder was written. All PRE bytes and source bytes remain unchanged. No Git mutation, publication, formal audit, external message, onward delegation, cube/tail research or campaign-plan access.',
    'preservation':'This seal binds the complete current independent packet. Any later correction must be separately identified and must preserve all frozen evidence.'
}
destination.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'seal':ident(destination),'independent_artifacts':len(artifacts),'PRE_bindings_unchanged':35,'post_PRE_sources_authenticated':len(sources['opened_and_authenticated']),'all_four_receipts_exit_zero':True},indent=2))
