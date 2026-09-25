"""Build one clean, explicitly stacked publication from immutable root sources."""
from pathlib import Path
import hashlib, json, re, subprocess

E = Path(__file__).resolve().parent
R = E/'microscopic-energy-budget-publication'
BASE = 'd3dfdff92b6eb9e422da3691d13af4c249b7c4e9'
BRANCH = 'codex/mobile-record-microscopic-ground-energy-budget-20260925'
PACKET = '.claude/science/physics-loops/mobile-record-microscopic-energy-budget-20260925'
NOTE = 'docs/MICROSCOPIC_GROUND_ENERGY_AND_FORMATION_BUDGET_BOUNDED_THEOREM_NOTE_2026-09-25.md'
RUNNER = 'scripts/microscopic_ground_energy_and_formation_budget_2026_09_25.py'
OUT = 'outputs/microscopic_energy_budget_20260925'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *a: subprocess.check_output(['git', *a], cwd=R, text=True).strip()
assert git('rev-parse', 'HEAD') == BASE
assert git('branch', '--show-current') == BRANCH
assert git('status', '--porcelain') == ''
parents = ['docs/'+s+'_BOUNDED_THEOREM_NOTE_2026-09-24.md' for s in [
    'BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET',
    'LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT',
    'LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS',
    'FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES',
]] + ['docs/NATIVE_GROUND_ENERGY_AND_ORIGINAL_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-25.md']
units = [
    ('microscopic', 'microscopic-ground-stationarity-personal', 'FULL_MICROSCOPIC_ENERGY_AND_FORMATION_ROOT.md', '7e03d6e1b644dd841cf5d7cc35863a884db8f40cf092d276cd0b90cfa7a0deeb'),
    ('budget', 'native-ground-energy-budget-personal', 'NATIVE_GROUND_RESIDENCE_AND_ENERGY_BUDGET_ROOT.md', '8b5ae458dd48672764ed9a79d35affcb945473ac330a9afbeb23af4d7411204d'),
]
sections, source_notes, replacements = [], [], []
for key, directory, filename, expected in units:
    d = E/directory
    seal = json.loads((d/'AUTHOR_SEAL.json').read_text())
    rows = seal.get('members', seal.get('files'))
    if isinstance(rows, dict):
        rows = [{'path': k, 'sha256': v if isinstance(v, str) else v['sha256']} for k, v in rows.items()]
    for row in rows:
        assert sha(d/row['path']) == row['sha256']
    assert sha(d/filename) == expected
    text = (d/filename).read_text()
    if key == 'microscopic':
        old = 'Personal root conditional theorem candidate, 25 September 2026. Unreviewed\nuntil a separate reconstruction is sealed. The primary agent personally'
        new = 'Personally derived conditional theorem, 25 September 2026. Separate scoped\nPRE and POST are complete; no retained audit status. The primary agent personally'
        changes = [(old, new)]
    else:
        changes = [(
            'Personally derived conditional candidate, 25 September 2026. This composes\nthe sealed but not yet independently checked root37 microscopic theorem',
            'Personally derived conditional consequence, 25 September 2026. This composes\nthe separately checked root37 microscopic theorem in Part I'), (
            'This is an analytic composition. No new numerical experiment or independent\nconfirmation is claimed.',
            'This is an analytic composition. No new numerical experiment is claimed.\nIts separate scoped PRE and POST are described in the publication overview.')]
    for old, new in changes:
        assert text.count(old) == 1
        text = text.replace(old, new)
        replacements.append({'unit': key, 'old': old, 'new': new})
    text = re.sub(r'^(#{1,6}) ', lambda m: '#'*(len(m[1])+2)+' ', text, flags=re.M)
    sections.append(text)
    source_notes.append({'unit': key, 'origin': str(d/filename), 'sha256': expected})

runtime = PACKET+'/runtime/primitive_spin_energy_controls.py'
source = E/'microscopic-ground-stationarity-personal/primitive_spin_energy_controls.py'
assert sha(source) == '7dbb936adc22aec2fe5321cba6b6498e354b5cf609c92b6f518bcf6dca2a2c14'
(R/runtime).parent.mkdir(parents=True)
(R/runtime).write_bytes(source.read_bytes())
claims = [Path(p).stem.lower() for p in parents]
header = '''---
claim_id: microscopic_ground_energy_and_formation_budget_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Conditional fixed-volume full microscopic energy/activity transfer and ground-input energy budget for the supplied compensated formation model; no selected physical vacuum, calibrated heating prediction or reservoir construction."
upstream_dependencies:
'''+''.join('  - '+c+'\n' for c in claims)+'runner: '+RUNNER+'\n---\n\n'
header += '''**Type:** bounded_theorem
**Status:** conditional mathematics with selective independent checks; no retained audit status.

# Microscopic ground energy and the original formation budget

In the supplied compensated model, an energetic ground state cannot remain
a quiet vacuum under the same original formation dynamics. The common-law
energy/activity constraint transfers to the full finite-spin Hamiltonian
under an actual-energy cap. At fixed finite cubic volume and sufficiently
small fixed K/delta, followed by increasing spin resource, every ground-input
density must acquire mean excitation energy 2 delta n by a preparation-dependent
first hitting time whose limsup is at most 5/(16 kappa). These are conditional
statements about that Hamiltonian and instrument. No physical vacuum or
observed heating rate is identified.

The two complete root arguments follow. Part I is the new microscopic transfer;
Part II composes it with exact number balance. The common-law filling trial
and energy/activity inequality imported in Part I are supplied by the native
ground-energy parent in this branch's base. Their separately checked arguments
remain conditional, with no audit promotion. This publication is stacked on
that open review branch rather than silently treating its result as main.

The root personally derived both arguments. Each has a sealed blind PRE and
a released-source POST. Part I's checker reconstructed the microscopic form
comparison, actual-energy control, high/low coherence estimate and spectral
infima. Part II's checker reconstructed the residence and energy-accounting
composition with Part I explicitly imported; it did not independently reprove
Part I. The final released-source publication comparison is a correspondence
review, not an additional blind derivation. Complete exposure histories and
original status wording are preserved in the evidence packet.

The finite-spin correction is an anticommutator, whose sign does not establish
operator order. The comparison controls forms on bounded gated-electric-energy
states; it does not control all occupied-link flux or prove global operator
convergence. A vanishing high-cluster population can retain finite mean energy.
The proof uses a one-sided energy comparison and keeps high/low coherences.
These distinctions are load-bearing, not optional numerical approximations.

Part II bounds total time spent in a low-energy region, including returns.
Its hitting time depends on the prepared ground density. It does not assert
a common laboratory readout time, positive initial power, monotone energy,
temperature, an individual quantum trajectory's energy, or a photon lifetime.
An implementation conserving an additive endpoint energy must account for
the system's gain; a separate interaction-energy or work contribution changes
that ledger. For an unbounded reservoir, the mean-energy statement presupposes
well-defined finite means (or the corresponding nonnegative excitation forms).
The ground-environment example presupposes an attained normal ground state
and actual conservation of the total energy observable; a formal commutator
on an unspecified domain alone is insufficient.

PRE-only stronger conclusions, extra controls and counterexamples retain their
independent provenance. They are not silently folded into the root claims.
In particular, the noncompact flux and rare-high-tail examples constrain
stronger microscopic interpretations, and the independent budget PRE's
time-average and late-time improvements are separate results in its report.

'''
footer = '''
## Verification and physical boundary

The primary runner freshly reuses the exact root microscopic-control source
in a temporary directory and preserves its complete stdout, stderr and JSON
artifact. The exact S=1 coefficient controls and floating cycle diagnostics
test the transfer mechanism. They do not numerically prove the small-K/delta
cubic inequality or the analytic residence theorem. The initial floating
equality failure, its narrow recorded repair, all earlier evidence and the
separate checker scopes remain available. Fresh source reuse creates no new
independence; floating diagnostics are not certified interval enclosures.

Limits are fixed graph, fixed positive K,delta,kappa with small K/delta selected
under the common-law parent, then increasing spin resource. The remainder is
uniform on each fixed actual-energy cap. No numerical resource threshold,
uniform volume limit or physical scale calibration is asserted. All original
matter states, formation signs and spin-boundary paths remain in the law.

The implication for the observation bridge is specific: a proposed persistent
energetic vacuum needs a justified preparation, state-selection mechanism and
energy supply or accounting. Those are not supplied by naming the ground
state. Driven or constrained preparations and other justified implementations
remain open. These statements do not compare a predicted number with data,
exclude the whole framework, add an axiom, construct a reservoir or complete
a theory of everything.

## Imports

'''+''.join('- ['+c+']('+Path(p).name+'): conditional parent within its stated scope.\n' for c,p in zip(claims,parents))+f'''
## Reproduction and evidence

Run `python3 {RUNNER}` from the repository root. Complete fresh results are
under `{OUT}/`. Original arguments, failed attempts, independent reports,
source bindings and final correspondence are in [the evidence directory](../{PACKET}/).
'''
body = header+'\n## Part I — transfer to the full microscopic law\n\n'+sections[0]+'\n## Part II — residence and actual energy supply\n\n'+sections[1]+footer
(R/NOTE).write_text(body)
inputs = [NOTE, *parents, runtime]
wrapper = '''#!/usr/bin/env python3
"""Fresh exact-source microscopic controls; residence proof is analytic."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = '''+repr(tuple(inputs))+'''
OUTPUT_DIRECTORY = '''+repr(OUT)+'''
RUNTIME = '''+repr(runtime)+'''
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter()
    sha=lambda raw:hashlib.sha256(raw).hexdigest()
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='microscopic-energy-budget-') as tmp:
        source=Path(tmp)/Path(RUNTIME).name;source.write_bytes((root/RUNTIME).read_bytes())
        r=subprocess.run([sys.executable,str(source)],cwd=tmp,capture_output=True,env=env)
        for stream,data in [('stdout',r.stdout),('stderr',r.stderr)]:
            (out/('microscopic_control.'+stream+'.txt')).write_bytes(data)
        if r.returncode or r.stderr:raise RuntimeError(r.stderr.decode())
        artifact=Path(tmp)/'SPIN_ENERGY_CONTROL_RESULTS.json'
        data=artifact.read_bytes();json.loads(data)
        assert data==r.stdout
        (out/artifact.name).write_bytes(data)
    result={'scope':'Fresh reuse of exact root cycle controls for the microscopic transfer; no numerical cubic residence theorem or new independent check.',
      'source_sha256':sha(Path(__file__).read_bytes()),'runtime_source_sha256':sha((root/RUNTIME).read_bytes()),
      'elapsed_seconds':time.perf_counter()-tick,'exit_code':r.returncode,'stderr_bytes':len(r.stderr),
      'stdout_bytes':len(r.stdout),'stdout_sha256':sha(r.stdout),
      'complete_scientific_artifact':{'path':OUTPUT_DIRECTORY+'/'+artifact.name,'sha256':sha(data),'bytes':len(data)},
      'all_assertions_passed':True}
    text=json.dumps(result,indent=2,allow_nan=False)+'\\n'
    (out/'MICROSCOPIC_ENERGY_BUDGET_PUBLIC_RESULTS.json').write_text(text)
    print(text,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
'''
(R/RUNNER).write_text(wrapper)
config = {'base_revision':BASE,'base_branch':'codex/mobile-record-native-ground-energy-and-formation-20260925','branch':BRANCH,'packet':PACKET,'note':NOTE,'runner':RUNNER,'output_directory':OUT,'parent_paths':parents,'runtime':[runtime],'source_notes':source_notes,'presentation_replacements':replacements,'origins':[{'origin':str(source),'publication':runtime,'sha256':sha(source),'adaptation':'None; exact sealed source.'}]}
(E/'MICROSCOPIC_ENERGY_BUDGET_PUBLICATION_WORKING_SOURCES.json').write_text(json.dumps(config,indent=2)+'\n')
print(json.dumps({'note_sha256':sha(R/NOTE),'note_bytes':(R/NOTE).stat().st_size,'runner_sha256':sha(R/RUNNER),'runtime_sha256':sha(R/runtime)},indent=2))
