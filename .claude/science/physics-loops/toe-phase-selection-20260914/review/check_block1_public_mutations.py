#!/usr/bin/env python3
"""Execute seven source mutations on separate copies of the public runner."""
from concurrent.futures import ThreadPoolExecutor
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

SOURCE = Path('/Users/jonreilly/Documents/Codex/toe-clock-penalty-support-20260914/scripts/finite_clock_local_probability_and_charge_projection_2026_09_14.py')
OUT = Path(__file__).resolve().parent/'block1_mutations'


def main():
    original = SOURCE.read_text()
    digest = hashlib.sha256(original.encode()).hexdigest()
    changes = [
        ('cell_orientation', 'sign = (-1)**position', 'sign = 1'),
        ('projected_double_hop', 'for jump in (-2, -1, 1, 2):', 'for jump in (-1, 1):'),
        ('penalty_limit_generator', '= expm(-total_time*H0)', '= expm(-0.5*total_time*H0)'),
        ('probability_energy_sign', 'return float(-2*C*tau+2*r*log_k)', 'return float(2*C*tau+2*r*log_k)'),
        ('electric_support_geometry',
         'electric_supports.append(set().union(*(face_supports[p]\n                                               for p in np.flatnonzero(F[:, l]))))',
         'electric_supports.append({l})'),
        ('gauge_orbit_normalization', 'orbit_size = 3**(len(levels[0])-1)', 'orbit_size = 3**len(levels[0])'),
        ('counterexample_potential', 'H2 = 2*np.eye(3)-B+np.diag([0., 100., 100.])',
         'H2 = 2*np.eye(3)-B+np.diag([0., 0., 0.])'),
    ]
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='toe-clock-mutations-') as directory:
        prepared = []
        for label, old, new in changes:
            assert original.count(old) == 1, (label, original.count(old))
            changed = original.replace(old, new, 1)
            path = Path(directory)/(label+'.py')
            path.write_text(changed)
            prepared.append((label, old, new, path, changed))

        def run(entry):
            label, old, new, path, changed = entry
            result = subprocess.run([sys.executable, str(path)], capture_output=True,
                                    text=True, timeout=120)
            for suffix, text in (('py', changed), ('stdout', result.stdout), ('stderr', result.stderr)):
                (OUT/(label+'.'+suffix+'.gz')).write_bytes(gzip.compress(text.encode(), mtime=0))
            row = {'mutation': label, 'old': old, 'new': new, 'returncode': result.returncode,
                   'caught_by_assertion': result.returncode != 0 and 'AssertionError' in result.stderr,
                   'stderr_tail': result.stderr.splitlines()[-5:],
                   'mutant_sha256': hashlib.sha256(changed.encode()).hexdigest()}
            return row

        with ThreadPoolExecutor(max_workers=3) as pool:
            rows = list(pool.map(run, prepared))
    evidence = {'primary_source': str(SOURCE), 'primary_sha256': digest,
                'mutations': rows, 'all_caught': all(row['caught_by_assertion'] for row in rows)}
    (OUT/'SUMMARY.json').write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(evidence, indent=2))
    assert evidence['all_caught']


if __name__ == '__main__':
    main()
