"""Seal the blind homogeneous charged-ring reconstruction and allowed sources."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':sha256(data).hexdigest()}


def verify(rows):
    for row in rows:assert identity(row['path'])==row,row['path']


boundary=json.loads((HERE/'SOURCE_READ_BOUNDARY.json').read_text())
sources=boundary['dependencies'];verify(sources)
controls=[]
for script,prefix in [('finite_sector_check.py','FINITE_SECTOR'),
                      ('algebra_bulk_check.py','ALGEBRA_BULK'),
                      ('weighted_sector_check.py','WEIGHTED_SECTOR')]:
    result=json.loads((HERE/(prefix+'_RESULTS.json')).read_text())
    receipt=json.loads((HERE/(prefix+'_CHECK_RECEIPT.json')).read_text())
    assert result['status']=='PASS' and receipt['exit_code']==0
    assert identity(HERE/script)['sha256']==result['source_sha256']
    verify([receipt['runner'],receipt['stdout'],receipt['stderr']])
    assert (HERE/(prefix+'_CHECK.stderr')).read_bytes()==b''
    assert (HERE/(prefix+'_CHECK.stdout')).read_bytes()==(HERE/(prefix+'_RESULTS.json')).read_bytes()
    controls.append({'runner':identity(HERE/script),'result':identity(HERE/(prefix+'_RESULTS.json'))})
weighted=json.loads((HERE/'WEIGHTED_SECTOR_RESULTS.json').read_text())
assert weighted['reused_own_helper_sha256']==identity(HERE/'finite_sector_check.py')['sha256']
artifacts=[identity(p) for p in sorted(HERE.rglob('*')) if p.is_file()
           and '__pycache__' not in p.parts
           and p.name not in ('PRE_COMPARISON_SEAL.json','CHECKPOINT.md')]
out={'created_utc':datetime.now(timezone.utc).isoformat(),
     'status':'Blind bounded independent reconstruction complete before author-source comparison; no publication or formal audit status.',
     'sources':sources,'artifacts':artifacts,
     'counts':{'sources':len(sources),'artifacts':len(artifacts),'total':len(sources)+len(artifacts)},
     'principal_results':[
       'One-hop denominator alpha=2d-1; two disjoint outward-hop denominator 2alpha-w, w=0,1,2.',
       'Second order gives K sum E^2 plus scalar on the physical neutral code, K=t^2/(alpha V0 S(S+1)).',
       'Fourth order is the complete folded diagonal in report Eq9 plus charge-swapping plaquettes with J=2t^4/[V0^3 alpha^2(alpha-1)]. Opposite-charge orientations add to the same transition.',
       'The full space has nonzero first-order B-resonant hops, independently witnessed in a neutral half-filled physical 6x6 state. Use a velocity O(t), not the old O(V0 epsilon^2) estimate without extra proof.',
       'A finite local Gauss/count-preserving dressing through m=3d+6, epsilon^2 S(S+1)=J alpha(alpha-1)/(2K), and beta=beta0 epsilon^(3d) gives the stated fixed-time uniform local charged rotor/matter comparison under bounded per-link fourth electric moments.'
     ],
     'local_error':'C_X,T ||O_X|| [epsilon+(1+log(S(S+1)))^d/(S(S+1))], with fixed d,K,J,beta0 and uniform moment bound; arbitrary charge/field correlations allowed.',
     'independent_controls':controls,
     'limits':[
       'Conditional dressed preparation; no bare-quench theorem or automatically selected checkerboard state.',
       'Charged rotor/matter target, not a pure-field rotor for arbitrary neutral content.',
       'Positive finite-S births vanish in the limit; no fixed-beta dynamics, growing times, completion, or thermodynamic phase claim.',
       'Small exact square controls have a frozen cubic outside environment; no full-torus quantum diagonalization or production simulation was performed.',
       'The dimension-independent local Lindblad proof is reused only at its previously verified identity; the changed commuting-penalty support, resonances and charged rotor domain steps are reconstructed in this report.'
     ],
     'failures':'No failed execution. Three scientific scripts passed on first runs; the invalid old-velocity shortcut is preserved as an analytic and exact physical countercontrol.',
     'read_boundary':'No new author homogeneous, charged-potential, result, seal, campaign checkpoint or registry opened. No new external theorem lookup.',
     'mutable_exclusion':'CHECKPOINT.md is an unsealed recovery aid.'}
target=HERE/'PRE_COMPARISON_SEAL.json';assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
sealed=json.loads(target.read_text());verify(sealed['sources']+sealed['artifacts'])
print(json.dumps({'report':identity(HERE/'REPORT.md'),'pre_seal':identity(target),
                  'counts':sealed['counts'],'all_bindings_verified':True},indent=2))
