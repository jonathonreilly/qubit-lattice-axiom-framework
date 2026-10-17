"""Record source qualification after full root reading; no scientific rerun."""
from pathlib import Path
import datetime as dt
import hashlib
import json

ROOT = Path(__file__).resolve().parent
N = ROOT.parent
A = N / 'emitter_installed_certificate'
R = N / 'emitter_installed_review'

def pin(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def verify(p, row):
    got = pin(p)
    assert got['bytes'] == row['bytes'] and got['sha256'] == row['sha256'], p
    return got

checked = []
for base, manifest in [(A, 'FREEZE.json'), (R, 'FILE_MANIFEST.json')]:
    for row in json.loads((base / manifest).read_text())['files']:
        checked.append(verify(base / row['path'], row))
source_pairs = []
for row in json.loads((R / 'SOURCE_PINS.json').read_text())['files']:
    original = verify(Path(row['original_path']), row)
    snapshot = verify(R / row['snapshot_path'], row)
    source_pairs.append({'original': original, 'snapshot': snapshot})
assert pin(A/'CANDIDATE.md')['sha256'] == '4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee'
assert pin(R/'REPORT.md')['sha256'] == 'cf9f05affa0155ff4069549490f61971d1d136b9f1e37a5d566c45b0f8d9590f'
execution = json.loads((R/'EXECUTION.json').read_text())
assert execution['exit_code'] == 0 and not execution['timed_out']
assert pin(R/'check_installed.py')['sha256'] == execution['script_sha256']
assert pin(R/'attempt_01/check_installed.py')['sha256'] == execution['script_sha256']
assert (R/'RESULTS.json').read_bytes() == (R/'attempt_01/stdout.json').read_bytes()
assert pin(R/'RESULTS.json')['sha256'] == execution['stdout_sha256']
assert pin(R/'attempt_01/stderr.txt')['sha256'] == execution['stderr_sha256']

record = {
    'qualified_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
    'disposition': 'Accepted for conditional provisional mathematical reuse; publication and independent retained audit remain separate.',
    'candidate': pin(A/'CANDIDATE.md'),
    'author_program': pin(A/'certify_installed_emitter.py'),
    'author_output': pin(A/'CERTIFICATE.json'),
    'author_execution': pin(A/'run01_execution.json'),
    'root_source_read': pin(ROOT/'SOURCE_READ.json'),
    'review': pin(R/'REPORT.md'),
    'independent_program': pin(R/'check_installed.py'),
    'independent_output': pin(R/'RESULTS.json'),
    'independent_execution': pin(R/'EXECUTION.json'),
    'independent_freeze': pin(R/'FREEZE.json'),
    'full_read_scope': ['Complete frozen candidate, all formulas and assumptions',
                        'Complete author program, result and actual execution record',
                        'Complete new independent report, checker, launcher, result, caps and receipt',
                        'Exact prior qualified packet and interval source identities reused'],
    'coverage_note': 'Truncated combined reads were completed by explicit report lines135-370 and complete checker/result reads; no omitted argument was treated as verified.',
    'decisive_checks': [
        'Retarded gluing, noncommuting XTY order and augmented physical-coordinate Schur complement reconstructed from an independent14-dimensional outgoing graph.',
        'Analytic uniform Schur imaginary bound, closed-coordinate inverse and point-spectrum argument separately checked with all internal directions retained.',
        'Reference spectral mass and Jacobian, one common normalized envelope, full2-by-2 seed overlap and same-energy old aging independently assessed.',
        'Common phase and all returns, complete localized derivatives, finite escape time and finite-horizon polynomial distance retained.',
        'Wrong matrix order, lower sign, density without velocity and diagonal-only overlap yield explicit nonzero discriminators.'
    ],
    'accepted_conditional_bounds': {
        'product_seed_isometry': '<0.003',
        'common_reflection': '<0.000714',
        'infinite_complete_isometry': '<0.004 for every t>=10^72',
        'finite_complete_isometry': '<0.005 for 10^72<=t<=2*10^72, M=5*10^73',
        'complete_comparator': 'zeta exp[-i(nu+2*kappa)t] beta_t tensor iota exp(-itK)W, with emitter empty and all outputs/reference retained',
    },
    'premises_and_limits': [
        'Original exact ladder, positive two-body forms, loop geometry and coherent complex phase are supplied.',
        'Initial excited emitter and blank clock/source product vacuum are supplied; no extended incoming-packet preparation is needed in this theorem.',
        'Earlier stationary and interval certificates remain inherited, including fixed central residual; no accuracy family follows.',
        'Old-site added cap2 does not bound source or contact loads, and old edge norm3 remains separate.',
        'Same-model source-exposed review; reviewer authored prior stationary ladder and reviewed prior generic proof. The new emitter proof and independent graph were separately derived.',
        'No author-code replay in review, no large clock allocation, no resonance quadrature, momentum-grid proof, time evolution, native hardware, reset/reuse or retained audit.',
        'Weighted escape and calibration extensions are separate proposals; this acceptance does not qualify them.'
    ],
    'actual_independent_execution': {'attempts': 1, 'wall_seconds': execution['wall_seconds'], 'largest_matrix_dimension': 14, 'cpu_cap_seconds': 45, 'wall_cap_seconds': 60},
    'verified_artifacts': checked,
    'verified_source_pairs': source_pairs,
    'editable_prompt_files_changed': [],
    'physical_axioms_changed': False,
}
assert not (ROOT/'ACCEPTANCE.json').exists()
(ROOT/'ACCEPTANCE.json').write_text(json.dumps(record, indent=2)+'\n')
(ROOT/'QUALIFICATION.md').write_text('''# Installed emitter source qualification

The frozen installed-emitter proof is accepted for conditional provisional
mathematical reuse. Its source identity, exact evidence, complete read coverage
and limits are recorded in [ACCEPTANCE.json](ACCEPTANCE.json). This is distinct
from a publication wrapper, canonical execution, PR or independent retained audit.

The complete source and separately written review support a supplied excited
product seed evolving into one common outgoing clock profile and the fixed old
operation. The infinite-apparatus complete isometry error is below0.004 for
every t>=10^72. The stated finite apparatus gives below0.005 only through
2*10^72, with5*10^73 clock sites. Both comparisons preserve the empty emitter,
source, all clock output, arbitrary passive references, scalar nu+2*kappa and
literal old aging from seed time. The exact inverse includes all internal
emitter directions and coherent returns. Point spectrum is included in the
seed-overlap error; it is not discarded or counted twice.

The reviewer independently assembled a noncommuting two-channel outgoing
graph, checked its direct14-dimensional solution, and reconstructed conservative
rational ceilings for the physical interval argument. One bounded run exited0
in0.8808858329430223 seconds. The toy graph distinguishes conventions; it is
not an interval simulation. The analytic mass, Schur, overlap and integration
arguments remain load-bearing. No blanket proof-assistant claim is made.

Prior ladder point/interval evidence is reused by exact identity. The reviewer
authored the earlier stationary ladder, so that evidence is not independently
recertified by this review. Same-model source exposure and shared premises limit
independence. Full report, code, launcher, output and receipt were read by the
root; omitted parts of truncated tool responses were subsequently read explicitly.

Exact local block structure, original ladder coefficients, coherent loop phase,
an excited qubit and a clean blank clock/source are supplied resources. Source
and contact loads exceed the old-only cap. These enormous sufficient costs do
not establish practical feasibility, native preparation, a fixed nominal waveform
under calibration error, reset/reuse, Record identification or empirical physics.
Weighted escape and calibration extensions remain separately reviewable work.
No source theorem, editable prompt, physical axiom, main branch or audit verdict
was changed by this qualification.
''')
print(json.dumps({'status': record['disposition'], 'verified_artifacts': len(checked), 'source_pairs': len(source_pairs), 'acceptance': pin(ROOT/'ACCEPTANCE.json'), 'qualification': pin(ROOT/'QUALIFICATION.md')}))
