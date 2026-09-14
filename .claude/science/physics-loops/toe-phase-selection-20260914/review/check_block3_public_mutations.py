#!/usr/bin/env python3
"""Bounded source challenges. Supply the exact restored public runner path."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    original = args.source.read_text()
    changes = [
        ('inverse_response_reciprocal',
         'predicted = -u @ (response_multiplier(gap) * ve) @ u.conj().T',
         'predicted = -u @ (ve / response_multiplier(gap)) @ u.conj().T'),
        ('inverse_kernel_factor',
         'kernel = -np.log(-np.expm1(-2 * np.pi * tau)) / (2 * np.pi)',
         'kernel = -np.log(-np.expm1(-2 * np.pi * tau)) / (4 * np.pi)'),
        ('gaussian_B_factor',
         'aa, bb = fg / bt, bs * lam * (1 + r / 4) * fg',
         'aa, bb = fg / bt, bs * lam * fg'),
        ('vacuum_scalar', 'np.exp(-omega * (n + .5))', 'np.exp(-omega * n)'),
        ('curl_orientation', '((step(x, j), i), -1)', '((step(x, j), i), 1)'),
        ('fourier_matrix_orientation',
         'symbol = lam*np.eye(3)-d[:, None]*d[None, :].conj()',
         'symbol = lam*np.eye(3)-d[:, None].conj()*d[None, :]'),
        ('overstrong_locality_rate',
         'bound_a = qmax**(degree+1)/bt',
         'bound_a = qmax**(2*degree+2)/bt'),
        ('charge_time_normalization',
         'expected = float(rho @ delta_inverse @ rho / (2*bt))',
         'expected = float(bt * rho @ delta_inverse @ rho / 2)'),
        ('green_heat_clock',
         'np.prod(ive(np.asarray(x), 2*t))',
         'np.prod(ive(np.asarray(x), t))'),
    ]
    out = Path(__file__).resolve().parent / 'block3_mutations'
    out.mkdir(exist_ok=True)
    rows = []
    with tempfile.TemporaryDirectory(prefix='toe-gaussian-log-mutations-') as directory:
        for label, old, new in changes:
            assert original.count(old) == 1, (label, original.count(old))
            changed = original.replace(old, new, 1)
            path = Path(directory)/(label+'.py')
            path.write_text(changed)
            result = subprocess.run([sys.executable, str(path)], capture_output=True,
                                    text=True, timeout=120)
            for suffix, content in (('py', changed), ('stdout', result.stdout),
                                    ('stderr', result.stderr)):
                (out/(label+'.'+suffix+'.gz')).write_bytes(
                    gzip.compress(content.encode(), mtime=0))
            row = dict(mutation=label, old=old, new=new, returncode=result.returncode,
                       caught_by_assertion=result.returncode != 0 and
                       'AssertionError' in result.stderr,
                       stderr_tail=result.stderr.splitlines()[-5:],
                       mutant_sha256=hashlib.sha256(changed.encode()).hexdigest())
            rows.append(row)
    evidence = dict(primary_source=str(args.source.resolve()),
                    primary_sha256=hashlib.sha256(original.encode()).hexdigest(),
                    mutations=rows,
                    all_caught=all(row['caught_by_assertion'] for row in rows))
    (out/'SUMMARY.json').write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(evidence, indent=2))
    assert evidence['all_caught']


if __name__ == '__main__':
    main()
