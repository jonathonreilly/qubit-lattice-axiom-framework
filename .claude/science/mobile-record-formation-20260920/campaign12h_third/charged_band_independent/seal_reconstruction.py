"""Freeze the independent reconstruction before author band-source access."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
HERE=Path(__file__).resolve().parent
OUT=HERE/'PRE_COMPARISON_SEAL.json';assert not OUT.exists()
def row(p):
    p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r,p=None):
    a=row(p or r['path']);assert a['bytes']==r['bytes'] and a['sha256']==r['sha256'],(r,a)
boundary=json.loads((HERE/'SOURCE_READ_BOUNDARY.json').read_text())
expected={
 'homogeneous_charged_independent/REPORT.md':'88bef2c7814bacb3864eee220e245365b3207c9d8f189298f8e8ddf1e13a3582',
 'homogeneous_charged_independent/COMPARISON.md':'689a0d3bc19054fc5d7f4c95a7d3cf7796a405ccf0f84ec61458e95a9750ddb5',
 'homogeneous_charged_independent/FINAL_SEAL.json':'fdcb0aea3a020ad2c71793dcd50e028e694c26a7c1cd12db590a20ffa9d18c05',
 'weak_field_waves_independent/REPORT.md':'97e03699969206594235e727487ef55ab77d0cb201abff5870dc7ac52fe64a93',
 'weak_field_waves_independent/COMPARISON.md':'4e0d398024ad892c8e5d878cf0e97bcd10b90a2c9e6135f3b5ede793680d3314',
 'weak_field_waves_independent/FINAL_SEAL.json':'381c1a07ff18dbca2019e51eaa086707ac0b11d4d7a1c642e5435b3aeaa0b610',
 'HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS.md':'8598d411c9837c4a97ac217de3058803386e83875ea62d0f707f6b9e32fd9b59'}
for r in boundary['sources']:
    verify(r);assert r['sha256']==expected[str(Path(r['path']).relative_to(HERE.parent))]
for prefix in ['BAND_ALGEBRA_REPAIRED_CHECK','TORUS_RESPONSE_MODULAR_CHECK']:
    rec=json.loads((HERE/(prefix+'_RECEIPT.json')).read_text());assert rec['exit_code']==0
    for field in ['runner','stdout','stderr']:verify(rec[field])
    assert Path(rec['stderr']['path']).read_bytes()==b''
assert (HERE/'BAND_ALGEBRA_RESULTS.json').read_bytes()==(HERE/'BAND_ALGEBRA_REPAIRED_CHECK.stdout').read_bytes()
assert (HERE/'TORUS_RESPONSE_RESULTS.json').read_bytes()==(HERE/'TORUS_RESPONSE_MODULAR_CHECK.stdout').read_bytes()
failed=[]
for prefix,sub,exitcode in [('BAND_ALGEBRA_CHECK','sympy_numpy_scalar',1),('TORUS_RESPONSE_CHECK','dense_exact_rank',-2)]:
    receipt=json.loads((HERE/(prefix+'_RECEIPT.json')).read_text());assert receipt['exit_code']==exitcode
    for field in ['stdout','stderr']:verify(receipt[field])
    old=HERE/'failed_attempts'/sub/Path(receipt['runner']['path']).name
    verify(receipt['runner'],old)
    failed.append({'receipt':row(HERE/(prefix+'_RECEIPT.json')),'archived_source':row(old),
                   'diagnosis':row(HERE/'failed_attempts'/sub/'DIAGNOSIS.md'),'exit_code':exitcode})
old=(HERE/'failed_attempts/sympy_numpy_scalar/band_algebra_check.py').read_text()
new=(HERE/'band_algebra_check.py').read_text()
assert old.replace('np.exp(-1j*t*q[a]*ch[e])','np.exp(-1j*t*q[a]*float(ch[e]))')==new
files=sorted(p for p in HERE.rglob('*') if p.is_file() and p.name not in ['CHECKPOINT.md','PRE_COMPARISON_SEAL.json'] and '__pycache__' not in p.parts)
artifacts=[row(p) for p in files]
data={'created_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Blind bounded reconstruction complete before new author charged-band access; no publication or formal audit status.',
 'sources':boundary['sources'],'artifacts':artifacts,
 'counts':{'sources':len(boundary['sources']),'artifacts':len(artifacts),'total':len(boundary['sources'])+len(artifacts)},
 'main_result':'Relaxed quadratic coefficient Q=p_equal C^T C+p_opposite T^T Pi_cycle T; Hessian 2Q. Gauge kernel exactly range D^T; harmonic stiffness 4 p_opposite(d-1).',
 'prepared_limit':'Fixed-box compact physical chart packet follows -Delta+x^T Q_U x with sufficient O(sqrt(h)) finite-time norm error for K=omega0 h,J=omega0/h.',
 'directional_control':'lambda_T(k)=4[p_opposite(d-1)-sin^2(k/2)/(n-1)]; frequencies 2 omega0 sqrt(lambda_T).',
 'exact_controls':['Six-dimensional complete neutral matter resolvent: direct 15, relaxation 9, exact relaxed coefficient 6.',
 'Allowed 6x6 torus rational gauge identities and modular rank37 with matching exact kernel; harmonic 36/17 and axis 35/17,33/17,32/17.',
 'Allowed 6x6x6 integer incidence identities and numerical harmonic/axis residuals.'],
 'failures_preserved':failed,
 'limits':['No uniform-volume matter-band gap or packet constants.','No thermodynamic phase or light-like continuum theorem.',
 'No new author band, finite-rate formation, registry or checkpoint accessed.','No full neutral many-body diagonalization on either cubic torus.'],
 'read_boundary':boundary['read_boundary'],'mutable_exclusion':'CHECKPOINT.md is an unsealed recovery aid.'}
OUT.write_text(json.dumps(data,indent=2)+'\n')
for r in data['sources']+data['artifacts']:verify(r)
print(json.dumps({'PRE':row(OUT),'REPORT':row(HERE/'REPORT.md'),'counts':data['counts'],'all_bindings_verified':True},indent=2))
