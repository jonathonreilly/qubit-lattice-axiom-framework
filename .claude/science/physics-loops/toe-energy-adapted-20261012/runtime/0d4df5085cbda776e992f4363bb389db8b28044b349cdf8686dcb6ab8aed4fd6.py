#!/usr/bin/env python3
"""Deterministic verification of complete stored author evidence; no science rerun."""
from pathlib import Path
import datetime, difflib, hashlib, json

ROOT=Path(__file__).resolve().parent
S=ROOT.parent
SNAP=ROOT/'author_snapshot'
E=SNAP/'energy_adapted_refinement'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def mapped(p):return SNAP/Path(p).relative_to(S)

fm=E/'final_manifest.json'
assert sha(fm)=='a9287eb6b86016905a2e11e3e751beaee91238e5e079ca1938bdbe3425540466'
final=json.loads(fm.read_text())
for p,h in final['files'].items():assert sha(mapped(p))==h,(p,h)
assert len(final['files'])==69
original=(E/'frozen/ENERGY_ADAPTED_REFINEMENT_PROBE.md').read_bytes()
note=(SNAP/'ENERGY_ADAPTED_REFINEMENT_PROBE.md').read_bytes()
assert note.startswith(original)
diff=''.join(difflib.unified_diff(original.decode().splitlines(True),note.decode().splitlines(True),fromfile='frozen/ENERGY_ADAPTED_REFINEMENT_PROBE.md',tofile='../ENERGY_ADAPTED_REFINEMENT_PROBE.md'))
assert diff==(E/'FINAL_APPENDIX.diff').read_text()
man=E/'execution_manifest.json';manifest=json.loads(man.read_text());pin=sha(man)
assert pin=='de6d88613c3c5a362d3d80a9122b9e68dc64fee82a03c6ad52a513d010732ce1'
for p,h in manifest['files'].items():
    source=mapped(p)
    if Path(p)==S/'ENERGY_ADAPTED_REFINEMENT_PROBE.md':source=E/'frozen/ENERGY_ADAPTED_REFINEMENT_PROBE.md'
    assert sha(source)==h,p
rows=[];diagnostics=[];receipts=[];jobs=[];boolean_only=[]
for job in ('baseline','drop_jacobian','reverse_cell_phase'):
    for layer in ('inner','outer'):
        f=E/'runs'/f'{job}_{layer}.receipt.json';r=json.loads(f.read_text())
        assert r['source_before']==manifest['files']==r['source_after']
        assert r['source_unchanged'] and not r['timeout']
        assert r['actual_manifest_sha256']==pin==r['expected_manifest_sha256']
        for kind in ('stdout','stderr'):assert sha(mapped(r[kind]))==r[kind+'_sha256']
        assert mapped(r['stderr']).read_bytes()==b''
        receipts.append({'job':job,'layer':layer,'sha256':sha(f),'returncode':r['returncode'],'timeout':r['timeout'],'elapsed_seconds':r['elapsed_seconds']})
    raw=E/'runs'/f'{job}_inner.stdout.txt'; own=[];extra=[];n5=[];summary=[]
    for lineno,line in enumerate(raw.read_text().splitlines(),1):
        if not line.startswith('{'):
            n5.append(line);continue
        val=json.loads(line);item={'job':job,'raw_path':str(S/'energy_adapted_refinement/runs'/raw.name),'raw_line':lineno,**val}
        if 'name' in val:
            if 'value' in val and 'tolerance' in val:assert val['passed']==(val['value']<val['tolerance']),item
            elif 'value' in val and 'threshold' in val:assert val['passed']==(val['value']>val['threshold']),item
            elif 'norm_error' in val and 'threshold' in val:assert val['passed']==(val['norm_error']<val['threshold']),item
            else:boolean_only.append({'job':job,'name':val['name'],'passed':val['passed']})
            own.append(item);rows.append(item)
        elif 'diagnostic' in val:diagnostics.append(item);extra.append(item)
        elif val.get('summary'):summary.append(val)
        else:raise AssertionError(item)
    assert len(own)==len({x['name'] for x in own})==238
    assert len(summary)==1 and len(n5)==5
    sm=summary[0];assert sm['total']==238 and sm['failed']==sum(not x['passed'] for x in own) and sm['passed']==sum(x['passed'] for x in own)
    for r in receipts[-2:]:assert r['returncode']==int(sm['failed']>0)
    jobs.append({'job':job,'summary':sm,'false_names':[x['name'] for x in own if not x['passed']],'surviving_names':[x['name'] for x in own if x['passed']],'diagnostics':extra,'N5_lines':n5})
assert rows==json.loads((E/'row_inventory.json').read_text())
assert diagnostics==json.loads((E/'diagnostic_inventory.json').read_text())
assert len(rows)==714 and len(diagnostics)==30 and len(receipts)==6
base=(E/'candidate.py').read_text()
assert (E/'variants/drop_jacobian.py').read_text()==base.replace('JACOBIAN_POWER = .5','JACOBIAN_POWER = 0.')
assert (E/'variants/reverse_cell_phase.py').read_text()==base.replace('CELL_PHASE_SIGN = +1','CELL_PHASE_SIGN = -1')
repro=json.loads((E/'reproduction_manifest.json').read_text())
assert sha(E/'reproduction_manifest.json')=='3fbcd8c8c808d8932f9d1e6ac084639a7800edad6b84021d42c5090999905907'
for p,h in repro['files'].items():assert sha(mapped(p))==h,p
parents=json.loads((E/'source_inventory.json').read_text())['parents_and_brief']
for entry in parents:assert sha(mapped(entry['copy']))==entry['sha256']
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'final_files_verified':69,'execution_inputs_verified':len(manifest['files']),'complete_rows_verified':len(rows),'complete_diagnostics_verified':len(diagnostics),'complete_receipts_verified':len(receipts),'frozen_core_exact_prefix':True,'appendix_diff_exact':True,'literal_variants_exact':True,'numeric_predicates_recomputed_from_stored_values':len(rows)-len(boolean_only),'boolean_only_recorded_rows':boolean_only,'jobs':jobs,'receipts':receipts,'scientific_reruns':0,'limits':['Stored numeric predicates are consistency checks, not independent mathematical derivations.','No author helper was executed. All author evidence was opened after the separate independent evidence seal.','The author nested recorder has separately sessioned children; outer kill alone is not whole-descendant cleanup. Original completed executions are unaffected.']}
(ROOT/'AUTHOR_RECONCILIATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['utc','final_files_verified','execution_inputs_verified','complete_rows_verified','complete_diagnostics_verified','complete_receipts_verified','numeric_predicates_recomputed_from_stored_values','scientific_reruns']}))
for j in jobs:print(json.dumps({'job':j['job'],'summary':j['summary'],'false_names':j['false_names'],'diagnostics':j['diagnostics']}))
