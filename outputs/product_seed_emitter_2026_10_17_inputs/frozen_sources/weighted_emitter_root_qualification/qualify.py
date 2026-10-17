"""Bind a separately reviewed weighted refinement to its qualified premises."""
from pathlib import Path
import datetime as dt
import hashlib
import json

ROOT=Path(__file__).resolve().parent
N=ROOT.parent
A=N/'weighted_emitter_escape_candidate'
R=N/'weighted_emitter_escape_review'
def pin(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(p,row):
    got=pin(p)
    assert got['bytes']==row['bytes'] and got['sha256']==row['sha256'],p
    return got
checked=[]
for base,name in [(A,'FREEZE.json'),(R,'FILE_MANIFEST.json')]:
    for row in json.loads((base/name).read_text())['files']:
        checked.append(verify(base/row['path'],row))
pairs=[]
for row in json.loads((R/'SOURCE_PINS.json').read_text())['files']:
    pairs.append({'source':verify(Path(row['source']),row),'snapshot':verify(R/row['snapshot'],row)})
assert pin(A/'CANDIDATE.md')['sha256']=='a2e96d2947b1e0deef2417d4673ddc8afd54f7382236aee6913ba6cae98e32b5'
assert pin(R/'REPORT.md')['sha256']=='cb309d98863a09a0db9b47b559a4e7a3a6f55d314b78dfd5379b57a089504028'
installed=json.loads((N/'emitter_installed_root_review/ACCEPTANCE.json').read_text())
assert installed['candidate']['sha256']=='4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee'
verify(Path(installed['candidate']['path']),installed['candidate'])
receipt=json.loads((R/'runs/attempt_1/EXECUTION.json').read_text())
assert receipt['exit_code']==0 and not receipt['timed_out']
for field in ['source_at_launch','source_after_execution','input_manifest_at_launch','wrapper','stdout','stderr','result']:
    verify(Path(receipt[field]['path']),receipt[field])
verify(R/'runs/attempt_1/executed_source.py',receipt['source_at_launch'])
result=json.loads((R/'runs/attempt_1/RESULT.json').read_text())
assert result['derived_bounds']['complete_at_T']['exact']=='2057560027/540000000000'
record={
    'qualified_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
    'disposition':'Accepted for conditional provisional mathematical reuse with the separately qualified installed source; no canonical publication or retained audit.',
    'source':pin(A/'CANDIDATE.md'), 'author_freeze':pin(A/'FREEZE.json'),
    'author_execution':pin(A/'EXECUTION.json'),
    'review':pin(R/'REPORT.md'), 'independent_checker':pin(R/'check_weighted_escape.py'),
    'independent_result':pin(R/'runs/attempt_1/RESULT.json'),
    'independent_execution':pin(R/'runs/attempt_1/EXECUTION.json'),
    'installed_acceptance':pin(N/'emitter_installed_root_review/ACCEPTANCE.json'),
    'installed_qualification':pin(N/'emitter_installed_root_review/QUALIFICATION.md'),
    'dependency_resolution':'The weighted report deliberately did not presume the installed review outcome. Root now binds its exact unchanged interface to the separately read and qualified installed theorem; the historical report and candidate are not rewritten.',
    'root_coverage':'Complete author argument/code/actual scalar evidence and complete independent report, checker, launcher, result, resource plan and receipt read. No truncated response was counted as complete.',
    'load_bearing_checks':['Monotone substitution with explicit Jacobian and whole-line I2/I3 antiderivatives; Cauchy-Schwarz I1.',
        'Cutoff slopes and all quotient derivatives; weighted unit-phase integral without a separate derivative supremum.',
        'Non-Hermitian1+7 full block inverse compared to a direct inverse, retaining all complementary coordinates.',
        'Coefficientwise positive polynomial bounds for y/y-prime, complete clock-plus-emitter C/C-prime and all three weighted moments.',
        'Within-parity square sum, positive-real outgoing normalization, literal old aging and finite-distance bound.'],
    'qualified_bounds':{'A0':'3/kappa','B0':'23/kappa','D':'3/kappa^2','onset':'10^36',
        'complete_infinite_at_onset':'2057560027/540000000000 <0.004; remainder decreases for all later times',
        'clock_sites':'5*10^37','finite_horizon':'2*10^36',
        'finite_complete':'2597560027/540000000000 <0.005 on [10^36,2*10^36]'},
    'unchanged_contract':'Same Hamiltonian, product seed, common f/rho/beta, zeta, physical nu+2kappa and full old aging; all emitter/source/clock/old outputs and passive references retained.',
    'actual_independent_execution':{'runs':1,'exit_code':0,'wall_seconds':receipt['elapsed_seconds'],'cpu_cap_seconds':45,'wall_cap_seconds':60,'largest_matrix_and_inverse_dimension':8},
    'limits':['Root authored the refinement; an independently written same-model source-exposed review assessed it. Prior local-emitter/generic exposure is disclosed.',
              'Installed optical, physical Schur, common seed overlap and reflection evidence are qualified dependencies, not re-proved by the weighted checker.',
              'No numerical quadrature, resonance grid, installed physical inverse replay, large-clock allocation or time evolution.',
              'Enormous sufficient mathematical costs; no empirical lifetime, practical apparatus, native preparation/phase supply, reset/reuse or accuracy family.',
              'Calibration and structural ladder-box extensions are not composed here; canonical wrapper/execution/publication/audit are separate.'],
    'verified_artifacts':checked,'verified_source_pairs':pairs,
    'editable_prompt_files_changed':[],'physical_axioms_changed':False}
assert not (ROOT/'ACCEPTANCE.json').exists()
(ROOT/'ACCEPTANCE.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'QUALIFICATION.md').write_text('''# Weighted escape source qualification

The weighted refinement is accepted for conditional provisional reuse with
the separately qualified installed-emitter theorem. [ACCEPTANCE.json](ACCEPTANCE.json)
records exact source identities, complete root reading and the resolved dependency.
The review's historical provisional labels remain unchanged: its conditional
interface is now matched to the same installed source that passed a separate
review and root qualification.

Keeping denominator factors together inside integration by parts yields
A0=3/kappa, B0=23/kappa and D=3/kappa^2. For the unchanged supplied apparatus,
the complete isometry error is below 0.004 for every t>=10^36. A clock with
5*10^37 sites gives error below 0.005 only through 2*10^36. This improves the
sufficient onset and size; it changes no Hamiltonian, prepared seed, output
waveform, physical scalar, fixed target phase or literal old aging.

Root read the complete separate report, checker, launcher, actual output and
receipt. One independent exact run exited zero in 10.88888437487185 seconds,
with maximum matrix and inverse dimension 8. Symbolic denominator integrals,
a non-Hermitian inverse with all seven complementary coordinates, coefficientwise
product bounds and complete normalization budgets were checked. No author code
was imported, no narrow-resonance quadrature or dynamics was used, and no huge
clock was allocated. Same-model source exposure and the reviewer's prior local
emitter/generic work limit independence; root authored the new refinement.

All installed physical assumptions remain: exact original ladder and positive
local structure, a coherent complex loop phase, an excited product seed, clean
clock/source vacuum and an infinite blank tail for permanence. These enormous
sufficient costs do not establish native implementation, practical feasibility,
reset/reuse, a calibration-independent waveform or arbitrary accuracy. Calibration
and structural coefficient-box proposals are separate. Canonical integration,
execution, regular publication and independent retained audit remain distinct
steps. No editable prompt, physical axiom, source theorem or audit verdict changed.
''')
print(json.dumps({'disposition':record['disposition'],'verified_artifacts':len(checked),'verified_source_pairs':len(pairs),'acceptance':pin(ROOT/'ACCEPTANCE.json'),'qualification':pin(ROOT/'QUALIFICATION.md')}))
