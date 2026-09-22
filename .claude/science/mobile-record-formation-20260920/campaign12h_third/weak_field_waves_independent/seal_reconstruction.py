"""Bind only this blind reconstruction and its pinned allowed dependencies."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

HERE=Path(__file__).resolve().parent


def row(path):
    path=Path(path).resolve();data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}


def verify(rows):
    for r in rows:
        assert row(r['path'])==r,r['path']


boundary=json.loads((HERE/'SOURCE_READ_BOUNDARY.json').read_text())
sources=boundary['allowed_pinned_sources'];verify(sources)
prior=HERE.parent/'large_spin_rotor_independent'/'FINAL_SEAL.json'
assert row(prior)['sha256']=='7620bb6ff3b16ec319f12ad0d588d45a56f0fd084ed192b59e8c86d0f9ac30d4'
old=json.loads(prior.read_text());verify(old['sources']+old['artifacts'])
verify([old['pre_comparison_seal'],old['author_seal']])
controls=[]
for prefix,script in [('INCIDENCE','incidence_check.py'),
                      ('COMPACT_PACKET','compact_packet_check.py'),
                      ('COUPLING_PATH','coupling_path_check.py')]:
    result=json.loads((HERE/(prefix+'_RESULTS.json')).read_text())
    receipt=json.loads((HERE/(prefix+'_CHECK_RECEIPT.json')).read_text())
    assert result['status']=='PASS' and receipt['exit_code']==0
    assert result['source_sha256']==row(HERE/script)['sha256']==receipt['runner_sha256']
    assert (HERE/(prefix+'_CHECK.stderr')).read_bytes()==b''
    assert (HERE/(prefix+'_CHECK.stdout')).read_bytes()==(HERE/(prefix+'_RESULTS.json')).read_bytes()
    controls.append({'prefix':prefix,'runner':row(HERE/script),'result':row(HERE/(prefix+'_RESULTS.json'))})
artifacts=[row(p) for p in sorted(HERE.rglob('*')) if p.is_file()
           and p.name not in ('CHECKPOINT.md','PRE_COMPARISON_SEAL.json')
           and '__pycache__' not in p.parts]
out={'created_utc':datetime.now(timezone.utc).isoformat(),
     'status':'Blind independent reconstruction complete before any new author weak-field access; no publication or formal audit status.',
     'sources':sources,'artifacts':artifacts,
     'counts':{'sources':len(sources),'artifacts':len(artifacts),'total':len(sources)+len(artifacts)},
     'reused_final_packet_authenticated':{'listed_bindings':len(old['sources'])+len(old['artifacts']),'additional_top_level_seals':2,'seal':row(prior)},
     'result':'A compact cutoff packet in the zero global electric-flux sector approximates the transverse harmonic state with the explicit residual (13) and O(h) fixed-time norm bound (15), at fixed finite box and fixed omega0=sqrt(KJ), h=sqrt(K/J)->0.',
     'dispersion':'omega(k)=2 sqrt(KJ) sqrt(4 sum_i sin^2(k_i/2)), two transverse polarizations at each nonzero mode.',
     'countercontrols':['Gauss alone leaves three physical harmonic directions; an additional global electric-flux sector is selected explicitly.',
                        'At fixed K=1,J=h^-2, the one-square first gap is 4/h-1+O(h); a fixed-time prepared relative phase differs from the uncorrected harmonic one.'],
     'independent_controls':controls,
     'proof_scope':'Finite box, prescribed small-angle quantum packet, fixed wave/time normalization. Subsequent fixed finite-mode continuum and record-to-rotor compositions use explicitly ordered limits.',
     'unresolved_extensions':['No uniform-in-volume weak-packet error or unrestricted joint h,N,S schedule established.',
                              'No thermodynamic phase, record-selected vacuum, all continuum observables, native implementation or full QFT theorem.'],
     'failures':'All three independent runners passed on their first execution; no failed helper or scientific attempt in this packet.',
     'source_boundary':'New author weak-field/energy/content/static-source/ramp/transport source, code, result, seal, campaign checkpoint and registry remain unopened.',
     'mutable_exclusion':'CHECKPOINT.md is an unsealed recovery aid.'}
path=HERE/'PRE_COMPARISON_SEAL.json'
assert not path.exists(),'Do not overwrite an existing PRE seal.'
path.write_text(json.dumps(out,indent=2)+'\n')
check=json.loads(path.read_text());verify(check['sources']+check['artifacts'])
print(json.dumps({'pre_seal':row(path),'report':row(HERE/'REPORT.md'),
                  'counts':check['counts'],'all_bindings_verified':True},indent=2))
