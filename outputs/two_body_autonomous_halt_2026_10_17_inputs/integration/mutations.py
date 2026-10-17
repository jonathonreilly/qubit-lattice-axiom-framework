"""Execute scoped scientific mutations outside the checkout; retain streams."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

N = Path(__file__).resolve().parents[1]
W = N.parent/'correlation_worktree'
D = N/'two_body_integration/mutations'
D.mkdir(exist_ok=True)
primary = W/'scripts/two_body_autonomous_halt_2026_10_17.py'
base = primary.read_text()
cases = [
 ('target_conjugation', 'w=(F(-7,25),F(24,25))', 'w=(F(-7,25),F(-24,25))', 'assert central_bound<central_contract'),
 ('common_phase_sign', 'zeta_approx=cneg(cmul(cpow(zi,4),alpha))', 'zeta_approx=cmul(cpow(zi,4),alpha)', 'assert cmul(r0_abs,zeta_approx)==cmul(cpow(zi,2),alpha)'),
 ('closed_root_underbound', 'kappa=F(1,7)', 'kappa=F(1,100)', 'assert 2+g/J>kappa+1/kappa'),
 ('interval_overextension', 'width=F(1,1000)', 'width=F(1,20)', 'assert min(source_gap,old_gap)>g'),
 ('localized_columns_orthogonal', 'Dpacket=F(88000)', 'Dpacket=F(62004)', 'assert Dj<62004 and 2*Dj*Dj<Dpacket*Dpacket'),
 ('finite_ready_support', 'N=22*10**12', 'N=2*10**12', 'assert d>=max(F(1),2*J*T,16*(F1+F0)**2/(3*eta_p**2))'),
 ('finite_observation_horizon', 'M=9*10**14', 'M=8*10**14', 'assert dM>rho*Tobs*F(6,5)+9'),
]
env = os.environ.copy()
env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
env['PYTHONPATH'] = str(W/'scripts')
records = []
def pin(raw): return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
for name, old, new, expected in cases:
    assert base.count(old) == 1, (name, base.count(old))
    folder = D/name
    folder.mkdir(exist_ok=False)
    source = base.replace(old, new, 1).replace(
        'REPO = Path(__file__).resolve().parents[1]', 'REPO = Path('+repr(str(W))+')', 1)
    for output_name in ['two_body_autonomous_halt_2026_10_17.json',
                        'two_body_autonomous_halt_2026_10_17_point_witnesses.json']:
        source = source.replace("REPO/'outputs/"+output_name+"'",
                                'Path('+repr(str(folder/output_name))+')')
    script = folder/'mutated.py'
    script.write_text(source)
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock = time.monotonic()
    proc = subprocess.run([sys.executable, str(script)], cwd=W, env=env,
                          capture_output=True, timeout=30)
    elapsed = time.monotonic()-clock
    (folder/'stdout').write_bytes(proc.stdout)
    (folder/'stderr').write_bytes(proc.stderr)
    rejected = (proc.returncode == 1 and b'AssertionError' in proc.stderr
                and expected.encode() in proc.stderr)
    row = {'name': name, 'started_utc': start, 'elapsed_seconds': elapsed,
           'exit_code': proc.returncode, 'wall_cap_seconds': 30,
           'source': pin(script.read_bytes()), 'old': old, 'new': new,
           'expected_scientific_assertion': expected,
           'scientific_assertion_rejected': rejected,
           'stdout': pin(proc.stdout), 'stderr': pin(proc.stderr)}
    (folder/'EXECUTION.json').write_text(json.dumps(row,indent=2)+'\n')
    records.append(row)
    assert rejected, name
record = {'base_primary': pin(primary.read_bytes()),
          'scope': 'Mutations alter one scientific relation in copied primary code. Input files and cache authority are unchanged. Each rejection must identify the planned mathematical assertion; no checksum rejection counts.',
          'cases': records}
(D/'RESULTS.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'cases': len(records), 'all_expected_scientific_rejections': True,
                  'elapsed_seconds': sum(r['elapsed_seconds'] for r in records)}))
