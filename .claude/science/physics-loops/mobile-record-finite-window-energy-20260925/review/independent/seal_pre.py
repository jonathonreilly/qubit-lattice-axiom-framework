"""Create the immutable blind PRE content seal, refusing an existing seal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    destination = HERE/'PRE_SEAL.json'
    assert not destination.exists(), 'Do not replace a sealed PRE.'
    pins = load(HERE/'SOURCE_PINS.json')
    evidence = load(HERE/'EVIDENCE_VERIFICATION.json')
    scientific = load(HERE/'CONTROL_ATTEMPT_01_EXECUTION.json')
    checked = load(HERE/'EVIDENCE_VERIFICATION_EXECUTION.json')
    assert evidence['source_origin_count'] == len(pins['sources']) == 13
    assert evidence['PRE_sha256'] == sha(HERE/'PRE.md')
    assert scientific['exit_code'] == checked['exit_code'] == 0
    assert sha(HERE/'primitive_energy_control.py') == scientific['source_sha256']
    assert sha(HERE/'CONTROL_ATTEMPT_01_STDOUT.json') == scientific['stdout_sha256']
    assert sha(HERE/'CONTROL_ATTEMPT_01_STDERR.txt') == scientific['stderr_sha256']
    assert sha(HERE/'verify_evidence.py') == checked['source_sha256'] == evidence['verifier_sha256']
    assert sha(HERE/'EVIDENCE_VERIFICATION.json') == checked['stdout_sha256']
    assert sha(HERE/'EVIDENCE_VERIFICATION_STDERR.txt') == checked['stderr_sha256']
    for source in pins['sources']:
        frozen = HERE/source['frozen']
        assert sha(frozen) == source['sha256'] and frozen.stat().st_size == source['bytes']
        if source['type'] == 'filesystem':
            assert sha(Path(source['origin'])) == source['sha256']
        elif source['role'] == 'scientific parent':
            assert sha(Path(source['repository'])/source['path']) == source['sha256']
    excluded = {'PRE_SEAL.json','PRE_SEAL_EXECUTION.json','PRE_SEAL_STDERR.txt'}
    names = sorted(str(p.relative_to(HERE)) for p in HERE.rglob('*')
                   if p.is_file() and str(p.relative_to(HERE)) not in excluded)
    assert len(names) == 25, names
    members = [{'path':name,'bytes':(HERE/name).stat().st_size,'sha256':sha(HERE/name)} for name in names]
    seal = {'sealed_utc':datetime.now(timezone.utc).isoformat(),
        'signed_by':'Codex independent checker /root/rotor_upper_tail_check',
        'scope':'Blind bounded PRE: full microscopic spectral energy laws for fixed positive-probability finite-bin records, separately proved stopped birth instrument, ordered birth-output limit, and independent exact small-graph moment counterexample.',
        'report':'PRE.md','scientific_source_revision':pins['scientific_revision'],
        'scientific_parent_count':3,'source_origin_count':13,
        'author_sources_read':[],'author_or_parent_scientific_programs_imported_or_executed':[],
        'own_scientific_controls':[{'source':'primitive_energy_control.py','execution':'CONTROL_ATTEMPT_01_EXECUTION.json',
                                    'output':'CONTROL_ATTEMPT_01_STDOUT.json','exit_code':0}],
        'limitations':['Fixed graph and fixed positive event probability; no uniform shrinking-window or growing-volume theorem.',
                       'Weak energy-law convergence does not imply general moment or support-edge convergence.',
                       'Physical counterexample is a disconnected twelve-dimensional graph, not a cube computation.',
                       'Abstract moving-atom/lower-edge examples are not physical rotor simulations.',
                       'No physical calibration, heat, source, audit or native-law-selection conclusion.'],
        'process_failure_record':'INDEPENDENCE_AND_FAILURE_RECORD.json',
        'member_count':len(members),'members':members,
        'next_step':'Stop before author disclosure. A later released-source comparison must preserve this PRE and use a separately sealed POST.'}
    with destination.open('x') as f:
        json.dump(seal,f,indent=2)
        f.write('\n')
    for name in names:
        (HERE/name).chmod(0o444)
    destination.chmod(0o444)
    for member in load(destination)['members']:
        assert sha(HERE/member['path']) == member['sha256']
    print(json.dumps({'status':'sealed and all 25 members verified','PRE_sha256':sha(HERE/'PRE.md'),
        'PRE_SEAL_sha256':sha(destination),'SOURCE_PINS_sha256':sha(HERE/'SOURCE_PINS.json'),
        'control_source_sha256':sha(HERE/'primitive_energy_control.py'),
        'control_result_sha256':sha(HERE/'CONTROL_ATTEMPT_01_STDOUT.json'),
        'member_count':25,'source_origin_count':13},indent=2))


if __name__ == '__main__':
    main()
