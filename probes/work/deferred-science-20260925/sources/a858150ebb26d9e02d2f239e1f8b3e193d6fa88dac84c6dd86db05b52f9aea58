"""Bindings and complete retained-row summaries only; no scientific rerun."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import difflib

HERE=Path(__file__).resolve().parent


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def load(name):return json.loads((HERE/name).read_text())


sources=load('SOURCE_PINS_INITIAL.json')
for row in sources['sources']:
    assert sha(Path(row['origin']))==row['sha256']==sha(HERE/row['snapshot'])
    assert (HERE/row['snapshot']).stat().st_size==row['bytes']

data=load('CONTROL_RESULTS.json');cert=load('COVARIANCE_CERTIFICATE.json')
for prefix,script,result,stdout,stderr in [
    ('CONTROL','two_detector_controls.py','CONTROL_RESULTS.json','CONTROL_STDOUT.log','CONTROL_STDERR.log'),
    ('CERTIFICATE','covariance_certificate.py','COVARIANCE_CERTIFICATE.json','CERTIFICATE_STDOUT.log','CERTIFICATE_STDERR.log')]:
    receipt=load(prefix+'_EXECUTION.json')
    assert receipt['exit_code']==0 and receipt['stderr_bytes']==0
    assert (HERE/stderr).read_bytes()==b''
    assert sha(HERE/script)==receipt['code_sha256']==load(result)['source_sha256']
    assert sha(HERE/result)==sha(HERE/stdout)==receipt['stdout_sha256']
first=HERE/'attempt01_direct_subtraction_failure'
preserved=json.loads((first/'PRESERVATION.json').read_text())
for name,expected in preserved['files'].items():assert sha(first/name)==expected
first_run=json.loads((first/'CONTROL_EXECUTION.json').read_text())
assert first_run['exit_code']==1
assert sha(first/'two_detector_controls.py')==first_run['code_sha256']
assert sha(first/'CONTROL_STDOUT.log')==first_run['stdout_sha256']
assert len((first/'CONTROL_STDERR.log').read_bytes())==first_run['stderr_bytes']
diagnosis=load('DIRECT_SUBTRACTION_DIAGNOSTIC.json')
assert diagnosis['own_source_sha256']==sha(first/'two_detector_controls.py')

primitive=data['primitive'];leading=[];finite=[];covs=[]
assert len(primitive['rows'])==8
assert all(r['exact_Gauss_and_product_effect'] and r['joint_Laurent_terms']==9 for r in primitive['rows'])
for geometry in data['reference']:
    leading+=geometry['leading_rows'];finite+=geometry['finite_g_rows']
    covs.append({k:geometry[k] for k in ['L','separation','v','c','normalized_covariance']})
assert len(leading)==12 and len(finite)==48
assert len([r for r in finite if not r['direct_ratio_assertion_applicable']])==12
assert all(r['scaled_numerator_error']<2e-13 and r['scaled_denominator_error']<2e-13 for r in finite)
assert all(r['independent_vacuum_subtracted']<0 for r in leading if r['packet']=='opposed_covariance')
assert len(cert['rows'])==2
for row in cert['rows']:
    assert len(row['exact_group_rows'])==42
    assert sum(x['momenta'] for x in row['exact_group_rows'])==1727
    lo=Fraction(row['covariance_lower_outward_decimal']);hi=Fraction(row['covariance_upper_outward_decimal'])
    assert lo<hi
    assert hi<0 if row['separation_axis']==0 else lo>0
    assert Fraction(row['normalized_abs_covariance_upper_outward_decimal'])<Fraction(2,3)

diff=''.join(difflib.unified_diff((first/'two_detector_controls.py').read_text().splitlines(keepends=True),(HERE/'two_detector_controls.py').read_text().splitlines(keepends=True),fromfile='first_failed_control',tofile='repaired_conditioning_control'))
(HERE/'CONTROL_REPAIR_DIFF.txt').write_text(diff)
report={'verified_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(Path(__file__)),
        'source_origins_and_snapshots_verified':len(sources['sources']),
        'new_scientific_reruns_by_this_verifier':0,
        'own_main_control_runs':2,'own_exact_covariance_certificate_runs':1,'own_inline_diagnosis_runs':1,
        'failed_main_run_preserved':True,'author_or_parent_control_runs':0,
        'primitive_rows':len(primitive['rows']),'leading_rows':len(leading),'finite_g_rows':len(finite),
        'rational_certificate_geometries':len(cert['rows']),'rational_groups_total':84,
        'covariance_floating_rows':covs,
        'maximum_reference_quadrature_error':max(r['quadrature_error'] for r in finite),
        'maximum_quadrature_order_change':max(r['quadrature_order_change'] for r in finite),
        'maximum_scaled_subtraction_numerator_error':max(r['scaled_numerator_error'] for r in finite),
        'maximum_scaled_subtraction_denominator_error':max(r['scaled_denominator_error'] for r in finite),
        'ill_conditioned_direct_ratio_rows_reported_without_precision_assertion':12,
        'maximum_recorded_direct_ratio_error':max(r['direct_subtraction_error'] for r in finite),
        'largest_conditioning_scale':max(r['direct_subtraction_condition_scale'] for r in finite),
        'complete_results_stdout_identity':True,'current_stderr_empty':True,
        'verification_limits':'Exact primitive algebra and explicit rational finite-sum covariance enclosures; Gaussian quadrature is floating corroboration. Full time theorem is analytic; no actual full-generator simulation, empirical fit or author review.'}
text=json.dumps(report,indent=2)+'\n'
(HERE/'VERIFICATION_REPORT.json').write_text(text);print(text,end='')
