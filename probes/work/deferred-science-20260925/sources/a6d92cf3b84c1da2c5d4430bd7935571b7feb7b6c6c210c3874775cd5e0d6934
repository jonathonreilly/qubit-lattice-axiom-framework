"""One-time publication correspondence; no scientific execution or source edits."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import datetime, hashlib, importlib.util, json, math, sys

E = Path(__file__).resolve().parent
R = E / 'native-ground-publication'
b = json.loads((E/'NATIVE_GROUND_PUBLICATION_WORKING_SOURCES.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
out = R/b['output_directory']
sources = {
    'pair_NATIVE_PAIR_RESULTS.json': E/'native-one-pair-spectrum-personal/NATIVE_PAIR_RESULTS.json',
    'pair_LOCAL_ROW_CERTIFICATE.json': E/'native-one-pair-spectrum-personal/LOCAL_ROW_CERTIFICATE.json',
    'pair_ROW_POLYNOMIAL_CERTIFICATE.json': E/'native-one-pair-spectrum-personal/ROW_POLYNOMIAL_CERTIFICATE.json',
    'filling_GROUND_FILLING_CERTIFICATES.json': E/'native-ground-filling-personal/GROUND_FILLING_CERTIFICATES.json',
    'activity_PRIMITIVE_RATE_ENERGY_RESULTS.json': E/'ground-formation-incompatibility-personal/PRIMITIVE_RATE_ENERGY_RESULTS.json',
}
differences, counts = [], Counter()

def compare(a, c, path):
    assert type(a) is type(c), path
    if isinstance(a, dict):
        assert list(a) == list(c), path
        for k in a: compare(a[k], c[k], path+'/'+k)
    elif isinstance(a, list):
        assert len(a) == len(c), path
        for i, (x, y) in enumerate(zip(a, c)): compare(x, y, path+'/'+str(i))
    else:
        counts[type(a).__name__] += 1
        if a != c: differences.append({'path': path, 'original': a, 'fresh': c})

for name, original in sources.items():
    compare(json.loads(original.read_text()), json.loads((out/name).read_text()), name)
metadata = {
    'pair_NATIVE_PAIR_RESULTS.json/elapsed_seconds',
    'pair_LOCAL_ROW_CERTIFICATE.json/elapsed_seconds',
    'pair_ROW_POLYNOMIAL_CERTIFICATE.json/prior_row_certificate_sha256',
    'filling_GROUND_FILLING_CERTIFICATES.json/elapsed_seconds',
    'activity_PRIMITIVE_RATE_ENERGY_RESULTS.json/elapsed_seconds',
}
floating = {
    'pair_NATIVE_PAIR_RESULTS.json/quotients/2/floating_top_delta_eigenvalue',
    'pair_NATIVE_PAIR_RESULTS.json/quotients/2/floating_eigen_residual',
}
actual = {v['path'] for v in differences}
assert actual == metadata | floating
try:
    assert actual == metadata
except AssertionError:
    failure = {
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Read-only replay and preservation of the prior unsaved comparison failure, not a scientific rerun.',
        'failed_assumption': 'Only four elapsed times and the fresh local-certificate content hash would differ.',
        'error': 'AssertionError: actual difference paths include two floating eigensolver diagnostics.',
        'all_differences': differences,
        'consequence': 'The first comparison did not verify or freeze the publication. Sources and scientific outputs were left unchanged.',
    }
    p = E/'NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT01_FAILURE.json'
    assert not p.exists()
    p.write_text(json.dumps(failure, indent=2)+'\n')
else:
    raise AssertionError('Expected historical comparison failure was not reproduced.')

pair = json.loads((out/'pair_NATIVE_PAIR_RESULTS.json').read_text())
certificates = []
for q in pair['quotients']:
    rows = [dict(row) for row in q['delta_Q_rows']]
    v, weights, shift = q['positive_integer_test_vector'], q['orbit_weights'], q['nonnegative_shift']
    assert all(isinstance(x, int) and x > 0 for x in v)
    ratios = []
    for i, row in enumerate(rows):
        assert row.get(i, 0)+shift > 0
        for j, value in row.items():
            assert i == j or value >= 0
            assert weights[i]*value == weights[j]*rows[j].get(i, 0)
        ratios.append(Fraction(sum(value*v[j] for j, value in row.items()), v[i]))
    low, high = min(ratios), max(ratios)
    expected = q['exact_delta_Q_Perron_interval']
    assert low == Fraction(expected['lower']['numerator'], expected['lower']['denominator'])
    assert high == Fraction(expected['upper']['numerator'], expected['upper']['denominator'])
    gap = q['proposed_ground_gap_g2_tau_interval']
    assert -high/4 == Fraction(gap['lower']['numerator'], gap['lower']['denominator'])
    assert -low/4 == Fraction(gap['upper']['numerator'], gap['upper']['denominator'])
    assert float(low)-1e-8 <= q['floating_top_delta_eigenvalue'] <= float(high)+1e-8
    assert q['floating_eigen_residual'] < 1e-10
    certificates.append({'side':q['side'], 'rows':len(rows), 'entries':sum(map(len,rows)),
                         'integer_matrix_and_rational_certificate_unchanged':True})
drift = [v for v in differences if v['path'] in floating]
for v in drift:
    v['absolute_difference'] = abs(v['fresh']-v['original'])
    assert v['absolute_difference'] < 2e-12
assert abs(drift[0]['fresh']-drift[0]['original']) <= math.ulp(drift[0]['original'])
poly = json.loads((out/'pair_ROW_POLYNOMIAL_CERTIFICATE.json').read_text())
assert poly['prior_row_certificate_sha256'] == sha(out/'pair_LOCAL_ROW_CERTIFICATE.json')
for item in b['origins']:
    assert sha(Path(item['origin'])) == sha(R/item['publication']) == item['sha256']
for item in b['source_notes']:
    assert sha(Path(item['origin'])) == item['sha256']

result_rel = b['output_directory']+'/NATIVE_GROUND_PUBLIC_RESULTS.json'
result = json.loads((R/result_rel).read_text())
assert result['source_sha256'] == sha(R/b['runner'])
assert result['all_assertions_passed'] is True and len(result['stages']) == 5
for stage in result['stages']:
    p = Path(stage['program']); stem = p.parent.name+'_'+p.stem
    stdout, stderr = out/(stem+'.stdout.txt'), out/(stem+'.stderr.txt')
    assert sha(R/p) == stage['source_sha256']
    assert stage['exit_code'] == stage['stderr_bytes'] == stderr.stat().st_size == 0
    assert sha(stdout) == stage['stdout_sha256']
    assert stdout.stat().st_size == stage['stdout_bytes']
assert {Path(x['path']).name for x in result['complete_scientific_artifacts']} == set(sources)
for artifact in result['complete_scientific_artifacts']:
    p = R/artifact['path']
    assert sha(p) == artifact['sha256'] and p.stat().st_size == artifact['bytes']

spec = importlib.util.spec_from_file_location('native_pub_runner_cache', R/'scripts/runner_cache.py')
cache_module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cache_module; spec.loader.exec_module(cache_module)
assert cache_module.cache_identity_status(b['runner']) == 'fresh'
assert cache_module.cache_status(b['runner']) == 'ok'
cache = cache_module.cache_path_for(b['runner'])
fingerprint = cache_module.declared_input_fingerprint(b['runner'])
execution = json.loads((E/'NATIVE_GROUND_PUBLICATION_CACHE_EXECUTION.json').read_text())
assert execution['exit_code'] == 0 and execution['stderr'] == ''
assert execution['stdout'] == (R/result_rel).read_text()+'TOTAL_PASS: 5\n'

record = {
    'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_identity':b['origins'], 'all_payload_leaf_counts':dict(counts),
    'all_differences':differences, 'floating_diagnostics_review':drift,
    'diagnostic_interpretation':'The two eigensolver diagnostics differ at roundoff scale. Every integer matrix entry, positive integer test vector, exact rational interval and other scientific leaf is identical. The rational intervals are verified directly here without rerunning an eigensolver. No stronger diagnosis of the numerical backend is claimed.',
    'exact_certificates':certificates,
    'full_artifacts_bytes':sum((out/n).stat().st_size for n in sources),
    'input_fingerprint_sha256':fingerprint,
    'elapsed_sec':execution['elapsed_sec'],
    'failed_assumption_preserved':'NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT01_FAILURE.json',
    'limits':'Fresh exact-source reuse and full correspondence, not another independent derivation or an observed fit.',
}
verification = E/'NATIVE_GROUND_PRIMARY_ROOT_VERIFICATION.json'; assert not verification.exists()
verification.write_text(json.dumps(record,indent=2)+'\n')
files = [b['note'], b['runner'], *b['parent_paths'], *b['runtime'], str(cache.relative_to(R))]
files += [str(p.relative_to(R)) for p in sorted(out.iterdir()) if p.is_file()]
frozen = {**b, 'result':result_rel, 'cache':str(cache.relative_to(R)),
          'files_sha256':{p:sha(R/p) for p in files}, 'frozen_utc':record['at'], 'generation':1}
p = E/'NATIVE_GROUND_PUBLICATION_FROZEN_SOURCES.json'; assert not p.exists()
p.write_text(json.dumps(frozen,indent=2)+'\n')
print(json.dumps({'leaf_counts':dict(counts),'differences':differences,
                  'certificates':certificates,'frozen_files':len(files),
                  'fingerprint':fingerprint,'root_verification_sha256':sha(verification),
                  'frozen_sha256':sha(p)},indent=2))
