from pathlib import Path
import hashlib, json, math
from datetime import datetime, timezone

S=Path(__file__).resolve().parent; E=S/'energy_adapted_refinement_review'
O=S/'energy_adapted_independent_root_verification_v2'; O.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
anchors={'NEUTRAL_PLAN.md':'e29710e00305f62af46997423cfb86b18f56e81281ecb6f2536adcbca7804ca1','FROZEN_EXECUTION_MANIFEST.json':'6c8dbba4bb292220c18212681ddeed7fbf13220ba97e2b2c9d573633e82dd1a2','INDEPENDENT_EVIDENCE.seal.json':'02471e96867ced1abac3cdc464c7e690e51aa542ff35fc6328084d7bf63ae5d3'}
for p,h in anchors.items(): assert sha(E/p)==h,p
manifest=json.loads((E/'FROZEN_EXECUTION_MANIFEST.json').read_text())
seal=json.loads((E/'INDEPENDENT_EVIDENCE.seal.json').read_text())
for m in [manifest,seal]:
    for row in m['files']:
        p=E/row['path']; assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],row
assert not seal['author_protocol_opened'] and not seal['author_helper_opened'] and not seal['author_results_opened']
mh=anchors['FROZEN_EXECUTION_MANIFEST.json']
expected_snap={'manifest_sha256':mh,'files':[{'path':r['path'],'sha256':r['sha256']} for r in manifest['files']]}
snapmap={r['path']:r['sha256'] for r in manifest['files']}
def near(x,y): assert math.isclose(x,y,rel_tol=3e-12,abs_tol=3e-14),(x,y)
def predicate(r):
    n=r['gate'];v=r['values']
    if n=='literal_spin_energy_boost_current':return max(v[k] for k in ['energy','bulk_boost','current'])<2e-12 and v['retained_endpoint_mismatch']>.1
    if n.startswith('actual_') and n.endswith('_intertwining'):return v['residual']<2e-11
    if n=='full_measure_isometry':
        near(v['residual'],abs(v['transported_norm2']-v['coefficient_norm2']));return v['residual']<2e-10
    if n=='actual_covariance_integral':
        near(v['residual'],abs(complex(*v['input'])-complex(*v['output'])));return v['residual']<2e-9
    if n=='direct_cell_alias_normalization':return v['residual']<3e-11
    if n in ['weak_gaussian_cell_limit','weak_haar_cell_limit']:
        samples=v['samples']
        for x in samples: near(x['error'],math.sqrt(max(0,x['image_norm2']+x['full_target_norm2']-2*x['cross_real'])))
        es=[x['error'] for x in samples]
        return es[-1]<.1 and es[-1]<.4*es[0] if n=='weak_gaussian_cell_limit' else es[-1]<.8*es[0]
    if n=='boost_differential_transport':
        es=v['residuals'];near(v['first_final_ratio'],es[0]/max(es[-1],1e-30));return es[-1]<2e-6 and (v['first_final_ratio']>=10 or max(es)<1e-11)
    if n=='coarse_boost_domain_singularity':
        amps=v['amplitudes'];eps=v['epsilons']
        for i,slope in enumerate(v['log_slopes']):near(slope,(math.log(amps[i+1])-math.log(amps[i]))/(math.log(eps[i+1])-math.log(eps[i])))
        return max(abs(s+.25) for s in v['log_slopes'])<.02
    if n=='even_boost_band_escape':
        assert v['support_group_parameter']==-v['pullback_characteristic_duration']
        return min(v['finals'])>v['coarse_cutoff_in_fine_q']+.01 and max(v['finals'])<math.pi/.4
    if n in ['even_spatial_projection_witness','even_actual_current_projection_witness']:return v['distance']>1e-5 and v['zero_parameter_distance']<2e-7
    raise AssertionError(n)
results=json.loads((E/'INDEPENDENT_RESULTS.json').read_text()); verified=[]
for job in results:
    n=job['attempt']; D=E/'runs'/n
    receipts={}
    for layer,bound in [('INNER',40),('OUTER',50)]:
        r=json.loads((D/f'{layer}.receipt.json').read_text())
        assert r==job[layer.lower()+'_receipt']
        assert not r['timeout'] and r['sources_unchanged'] and r['timeout_seconds']==bound and r['elapsed_seconds']<bound
        assert r['source_manifest_sha256']==mh
        assert manifest['created_utc']<r['started_utc']<r['finished_utc']<seal['sealed_utc']
        for kind in ['stdout','stderr']:assert sha(D/f'{layer}.{kind}')==r[kind+'_sha256']
        assert (D/f'{layer}.stderr').read_bytes()==b''
        for when in ['before','after']:assert json.loads((D/f'{layer}.sources.{when}.json').read_text())==expected_snap
        receipts[layer]=r
    assert receipts['OUTER']['started_utc']<receipts['INNER']['started_utc']<receipts['INNER']['finished_utc']<receipts['OUTER']['finished_utc']
    assert json.loads((D/'OUTER.stdout').read_text())==receipts['INNER']
    raw=[json.loads(line) for line in (D/'INNER.stdout').read_text().splitlines()]
    assert raw==job['all_results']
    gates=raw[:-1];sm=raw[-1]['summary'];assert len(gates)==15 and len({r['gate'] for r in gates})==15
    for r in gates:assert predicate(r) is r['passed'],(n,r)
    fails=[r['gate'] for r in gates if not r['passed']];survive=[r['gate'] for r in gates if r['passed']]
    assert sm=={'variant':n,'pass':len(survive),'fail':len(fails),'failed_gates':fails,'surviving_gates':survive}
    code=1 if fails else 0
    assert receipts['INNER']['exit_code']==receipts['OUTER']['exit_code']==code
    cpath='candidate_formula.py' if n=='baseline' else f'variants/{n}/candidate_formula.py'
    assert receipts['INNER']['candidate_sha256']==snapmap[cpath]
    verified.append({'job':n,'gates':len(gates),'failures':fails,'survivors':survive,'inner_seconds':receipts['INNER']['elapsed_seconds'],'outer_seconds':receipts['OUTER']['elapsed_seconds']})
integrity=json.loads((E/'integrity_controls/receipts.json').read_text())
for r in integrity:
    D=E/'integrity_controls'/r['name']
    assert r['exit_code']==3 and r['elapsed_seconds']<r['timeout_seconds']==5 and r['trusted_manifest_sha256']==mh
    for k in ['stdout','stderr']:assert sha(D/('guard.'+k))==r[k+'_sha256']
    assert (D/'guard.stderr').read_bytes()==b''
    out=json.loads((D/'guard.stdout').read_text());assert out['guard']=='rejected'
    if r['name']=='self_rebound_manifest':assert out['reason'].startswith('MANIFEST_PIN_MISMATCH')
    else:assert out['reason'].startswith('SOURCE_PIN_MISMATCH')
assert len(verified)==6 and sum(x['gates'] for x in verified)==90 and len(integrity)==3
(O/'verified_runs.json').write_text(json.dumps(verified,indent=2)+'\n')
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'complete_original_independent_evidence_checked','anchors':anchors,'sealed_files':len(seal['files']),'original_scientific_runs':6,'complete_inner_outer_receipts':12,'gates_recomputed_from_raw_values':90,'integrity_controls':3,'science_rerun':False,'manual_coverage':'Full 218-line independent proof, 74-line spec and all 346 scientific/recording helper lines; baseline values and every changed mutant value read completely, unchanged rows mechanically matched. Initial oversized pretty-JSON print was truncated and is not counted as verification. Literal five source diffs read.','limits':['Same selected model family in a fresh neutral-plan context; target formula and necessary parents exposed.','Selective finite quadrature, finite differences and spin matrices are diagnostics, not universal proofs.','Original author outer timeout alone does not guarantee killing its independently sessioned science child; all original jobs completed, with separate inner timeout and complete records.','This independent outer wrapper attempts killing the separately recorded child group too; not an atomic race-free security guarantee.'],'pending':['Final fresh review report/manifest integration']}
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
