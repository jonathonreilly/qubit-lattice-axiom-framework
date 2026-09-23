"""Freeze this reconstruction before any candidate-source exposure."""
from pathlib import Path
import datetime,hashlib,json

HERE=Path(__file__).resolve().parent
def ident(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

destination=HERE/'PRE_COMPARISON_SEAL.json'
assert not destination.exists(),'Never overwrite the PRE seal.'
sources=json.loads((HERE/'SOURCE_IDENTITIES.json').read_text())
for recorded in sources['science_sources']:
    current=ident(Path(recorded['path']))
    assert current==recorded,(current,recorded)
prepared=json.loads(Path(sources['science_sources'][0]['path']).read_text())
for recorded in prepared['independent_artifacts']:
    assert ident(Path(recorded['path']))['sha256']==recorded['sha256']
receipts=[]
for stem in ('consequence','adjoint_reference','source'):
    receipt=json.loads((HERE/(stem+'_RECEIPT.json')).read_text())
    assert receipt['exit_code']==0
    assert ident(Path(receipt['command'][1]))['sha256']==receipt['script_sha256']
    for stream in ('stdout','stderr'):
        assert ident(HERE/(stem+'.'+stream))['sha256']==receipt[stream+'_sha256']
    receipts.append({'stem':stem,'exit_code':receipt['exit_code'],'elapsed_seconds':receipt['elapsed_seconds']})
artifacts=[ident(p) for p in sorted(HERE.iterdir()) if p.is_file()]
seal={
    'phase':'PRE_COMPARISON',
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scientific_status':'Source-bound independent consequence theorem; comparison pending. Not a formal retained/audit verdict.',
    'candidate_seal_hash_supplied_by_coordinator_only':'e8a1ea634f3355f883da749124af2ab5f5fbaba3ea7270d972dd279d3ded6046',
    'candidate_source_exposure':'None. actual_first_output_author and all excluded unprepared/tail/planning sources remain unopened.',
    'result_scope':'Restarted actual output: time-smeared N6 local limit and pointwise integrated N8 local limit. Original all-A-plus zero-field state: exact target first clock 16 kappa, pointwise compact-time-uniform finite-window density limits, local trace (1+exp(-16 kappa t))/2, no trace-norm convergent subsequence at fixed t>0, total number bounds without an asserted complementary or total number limit; deterministic microscopic transfer.',
    'decisive_obligations':['Exact finite-spin loss bound R_S<=4 and resolved/coherent loss equality','Adjoint prepared theorem by signed-Hamiltonian core proof','Positive trace-class commutant lies in physical point spectrum','Exact zero-field first-sector clock and outputs','Finite-range jumps preserve finite-window observable scope','Convolution upgrades local time-weak convergence to fixed-time local convergence','Trace deficit versus global number probabilities kept distinct'],
    'science_sources':sources['science_sources'],
    'prepared_artifacts_authenticated':len(prepared['independent_artifacts']),
    'procedure_source_record':sources['procedures'],
    'origin_main_revision':sources['origin_main'],
    'execution_receipts':receipts,
    'independent_artifacts':artifacts,
    'preservation':'All listed PRE bytes are immutable; later comparison and corrections must be separate files.',
    'authority_limits':'No Git mutation, publication, audit verdict, external message, onward delegation, broader no-go packet completeness, or candidate comparison is claimed.'
}
destination.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'seal':ident(destination),'science_sources':len(sources['science_sources']),'artifacts':len(artifacts),'all_receipts_exit_zero':True},indent=2))
