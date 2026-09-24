"""Read-only released-source correspondence; never imports or runs author code."""
from pathlib import Path
from decimal import Decimal, localcontext
import datetime, hashlib, json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
AUTHOR = BASE / 'observation-unit-bridge-personal'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, value):
    path = HERE / name
    assert not path.exists(), f'Preserve existing evidence: {path}'
    path.write_text(json.dumps(value, indent=2) + '\n')

pre_seal = json.loads((HERE / 'PRE_SEAL.json').read_text())
assert sha(HERE / 'PRE_SEAL.json') == '6e08c4d893c9f40eabdb0b296c37bf1b850d48b88a2ec5dd10e2f939e866dce3'
for member in pre_seal['members']:
    path = HERE / member['path']
    assert sha(path) == member['sha256']
    assert path.stat().st_size == member['bytes']
author_seal = json.loads((AUTHOR / 'AUTHOR_SEAL.json').read_text())
for member in author_seal['members']:
    path = AUTHOR / member['path']
    assert sha(path) == member['sha256']
    assert path.stat().st_size == member['bytes']
assert sha(AUTHOR / 'OBSERVATION_RESPONSE_AND_CLOCK_SCOPE_ROOT.md') == '91fd6c3df5063dcbbbc999bd1e3a4817b286ae6ce8448156550cb957fd2d709b'

names = [x['path'] for x in author_seal['members']] + ['AUTHOR_SEAL.json', 'ROOT_METADATA_QUALIFICATION.md']
pins = []
for name in names:
    src = AUTHOR / name
    dst = HERE / 'post_sources' / name
    dst.parent.mkdir(exist_ok=True)
    assert not dst.exists()
    dst.write_bytes(src.read_bytes())
    pins.append({'origin':str(src), 'snapshot':str(dst.relative_to(HERE)), 'sha256':sha(src), 'bytes':src.stat().st_size})

receipt = json.loads((AUTHOR / 'EXECUTION.json').read_text())
root_result = json.loads((AUTHOR / 'UNIT_CONVERSIONS.json').read_text())
assert receipt['code_sha256'] == sha(AUTHOR / 'unit_conversions.py') == root_result['source_sha256']
assert receipt['result_sha256'] == sha(AUTHOR / 'UNIT_CONVERSIONS.json')
assert receipt['exit_code'] == 0 and receipt['stderr_bytes'] == 0
assert (AUTHOR / 'CONTROL.stderr').read_bytes() == b''
assert (AUTHOR / 'CONTROL.stdout').read_bytes() == (AUTHOR / 'UNIT_CONVERSIONS.json').read_bytes()
own_result = json.loads((HERE / 'CONTROL_RESULTS.json').read_text())
own_rows = [r for r in own_result['SI_rows'] if Decimal(r['A4']) < Decimal('0.34')]
assert len(own_rows) == len(root_result['rows']) == 2
comparisons = []
with localcontext() as context:
    context.prec = 85
    for ours, theirs in zip(own_rows, root_result['rows']):
        assert Decimal(ours['E_QG_GeV']) == Decimal(theirs['E_QG2_lower_GeV'])
        for our_key, root_key in [('tau_upper_s_for_A4','necessary_tau_upper_seconds'), ('a_upper_m_for_A4','orientation_independent_necessary_a_upper_m')]:
            relative = abs(Decimal(ours[our_key]) / Decimal(theirs[root_key]) - 1)
            assert relative < Decimal('1e-53')
            comparisons.append({'benchmark':theirs['benchmark'], 'quantity':root_key, 'independent_PRE_value':ours[our_key], 'root_value':theirs[root_key], 'relative_difference':str(relative), 'difference_explanation':'Stored 55-digit Decimal PRE computation compared with stored 70-digit mpmath author arithmetic; no rerun.'})

declared = json.loads((AUTHOR / 'SOURCE_PINS.json').read_text())
allowed = {x['sha256'] for x in json.loads((HERE / 'SOURCE_PINS.json').read_text())['sources']}
origin_checks = []
for source in declared['files']:
    if source['sha256'] in allowed:
        assert sha(Path(source['path'])) == source['sha256']
        origin_checks.append({'path':source['path'], 'sha256':source['sha256'], 'status':'Permitted shared parent origin verified; premise reused from PRE.'})
    else:
        origin_checks.append({'path':source['path'], 'sha256':source['sha256'], 'status':'Declaration read only. Excluded prepared-matter packet not opened or origin-hash verified; permitted published parent supplies the needed premise.'})
write('POST_SOURCE_PINS.json', {'phase':'released-source POST, not blind discovery', 'sources':pins, 'author_declared_parents':origin_checks, 'unchanged_PRE_sha256':sha(HERE/'PRE.md'), 'unchanged_PRE_seal_sha256':sha(HERE/'PRE_SEAL.json')})
write('POST_VERIFICATION_REPORT.json', {'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'unchanged_PRE_members':len(pre_seal['members']), 'author_seal_members_verified':len(author_seal['members']), 'released_snapshots':len(pins), 'author_controls_executed':0, 'scientific_control_rows_read':2, 'all_author_stdout_equals_result':True, 'empty_author_stderr':True, 'metadata_qualification':'started_utc is a receipt/completion timestamp, not the exact start. Supplemental qualification pinned separately.', 'stored_SI_comparisons':comparisons, 'primary_sources_retrieved_again':0, 'other_active_packets_read':False, 'publication_or_audit_mutation':False})
print(json.dumps({'preserved_PRE_members':len(pre_seal['members']), 'verified_author_members':len(author_seal['members']), 'snapshots':len(pins), 'stored_arithmetic_comparisons':len(comparisons), 'author_executions':0}, indent=2))
