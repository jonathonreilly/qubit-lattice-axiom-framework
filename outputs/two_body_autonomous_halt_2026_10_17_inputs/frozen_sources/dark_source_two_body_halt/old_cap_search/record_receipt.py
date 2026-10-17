#!/usr/bin/env python3
"""Deterministic bookkeeping and immutable-witness check for this bounded run."""
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path
import datetime, hashlib, json

ROOT=Path(__file__).resolve().parent
def read(name): return json.loads((ROOT/name).read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
before=read('ORIGINAL_SNAPSHOT.json')
unchanged=[]
for entry in before['files']:
    path=ROOT.parent/entry['path']
    current=dict(path=entry['path'],size=path.stat().st_size,sha256=sha(path))
    assert current==entry,(entry,current)
    unchanged.append(current)
current_originals={str(p.relative_to(ROOT.parent)) for p in ROOT.parent.rglob('*')
                   if p.is_file() and ROOT not in p.parents}
assert current_originals=={v['path'] for v in unchanged}

first=read('SEARCH.json');second=read('ALLOWED_SEARCH.json')
cert=read('rational_point_certificate.json');check=read('different_path_check.json')
rows=first['rows']+second['rows']
assert len(rows)==second['combined_starts']<=60
assert [r['index'] for r in rows]==list(range(len(rows)))
assert all(r.get('nfev_reported',0)<=500 for r in rows)
assert second['combined_search_seconds']<180
assert all(0<r['physical']['gA']<=1 and 0<r['physical']['gB']<=1
           and 4*r['physical']['J']<2 and r['source_gap_entire_band']>0 for r in rows)
P={k:F(v) for k,v in cert['exact_parameters'].items()}
assert 0<P['gA']<=1 and 0<P['gB']<=1 and 4*P['J']<2
assert min(P['DeltaA'],P['DeltaB'])>2+4*P['J']
assert F(cert['certified_point_isometry_error']['rational'])<F(176,10**15)
assert P['scalar_reserve']==max(F(0),-P['mu0'])+max(F(0),-P['mu1'])
assert all((ROOT/f).stat().st_size==0 for f in
           ['SEARCH.stderr','ALLOWED_SEARCH.stderr','CERTIFICATE.stderr','DIFFERENT_PATH.stderr'])
provenance=read('VERIFIER_PROVENANCE.json')
assert all(sha(ROOT.parent/f)==value for f,value in provenance['copied_originals'].items())
getcontext().prec=70
error=F(cert['certified_point_isometry_error']['rational'])
result=dict(
    recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    original_witness_status='All 36 snapshotted preexisting files byte-for-byte unchanged; no original files added or removed',
    original_files_verified=unchanged,
    source_revision='c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc',
    supplied_main_revision='5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2',
    original_sources_manifest_sha256=sha(ROOT.parent/'sources/MANIFEST.json'),
    searches=dict(
        shared_cap=dict(max_starts=60,max_nfev_per_start=500,wall_checkpoint_seconds=180,
                        checkpoint='Between completed starts; actual combined search elapsed below cap'),
        completed_starts=len(rows),combined_search_seconds=second['combined_search_seconds'],
        exception_failures=sum('failure' in r for r in rows),
        termination_reasons=dict(Counter(r.get('message',r.get('failure','missing')) for r in rows)),
        numerical_target_below_1e9=sum(r.get('numerical_target_error',1)<1e-9 for r in rows),
        optimizer_residual_calls=sum(r.get('actual_optimizer_residual_calls',0) for r in rows),
        calls_including_detail_evaluations=first['actual_residual_calls_including_detail_evaluations']+second['model_residual_calls'],
        expanded_search_box_used=False,
        variant_a_best_index=first['best']['index'],variant_b_best_index=second['best']['index']),
    certificate=dict(
        scope=cert['claim'],exact_error_upper=str(error),
        decimal_display=str(Decimal(error.numerator)/Decimal(error.denominator)),
        exact_assertion='error < 176/10**15',
        exact_parameter_map_sha256=hashlib.sha256(json.dumps(cert['exact_parameters'],sort_keys=True).encode()).hexdigest(),
        source_gap=cert['source_threshold_gap_entire_clock_band'],
        old_band_separation=cert['old_energy_band_separation'],
        loads=cert['added_incident_block_norms'],
        elapsed_seconds=cert['elapsed_seconds'],versions=cert['versions']),
    different_path=dict(
        maximum_dimension=max(v['dimension'] for v in check['rows']),
        max_difference=max(v['difference_from_certified_surface'] for v in check['rows']),
        max_linear_residual=max(v['linear_residual_infinity'] for v in check['rows']),
        max_offdiagonal=max(v['offdiagonal'] for v in check['rows']),
        elapsed_seconds=check['elapsed_seconds'],versions=check['versions'],
        independent_reviewer=False),
    environment={'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'},
    command_exit_statuses={'search.py':0,'search_allowed.py':0,'certify_old_cap.py':0,'check_old_cap.py':0},
    source_copied_verifier_adaptations=provenance,
    writes_scope=str(ROOT),
    editable_prompt_files_changed=[],shared_source_files_changed=[],
    network_calls=0,git_mutations=0,
    note='Verifier reruns only tightened positivity/error assertions and fixed-momentum wording; the exact candidate and different-path input coefficients stayed unchanged.'
)
(ROOT/'RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n')
summary=dict(original_files_verified=len(unchanged),completed_starts=len(rows),
             certified_error_display=result['certificate']['decimal_display'],
             source_gap=cert['source_threshold_gap_entire_clock_band']['upper_float'],
             unchanged_original_route_sha256=sha(ROOT.parent/'ROUTE.md'))
summary_text=json.dumps(summary,indent=2)+'\n'
(ROOT/'RECEIPT.stdout').write_text(summary_text)
manifest=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p))
          for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='FILE_MANIFEST.json']
(ROOT/'FILE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(summary_text,end='')
