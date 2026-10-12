#!/usr/bin/env python3
"""Complete the preselected six-source extension, stopping on a failed gate."""
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

from direct_qumond_disk import DATA, guard, sha

OUT = DATA / 'qumond_disk'
SOLVER = Path(__file__).with_name('direct_qumond_disk.py')
EXPECTED = '701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00'


def change(a, b):
    return float(np.max(np.abs(np.asarray(a) / np.asarray(b) - 1)))


def run(name, tag, lmax=128, nr=1536, hankel=2048, inner=16, outer=8, newtonian=False):
    guard()
    assert sha(SOLVER) == EXPECTED
    output = OUT / f'expanded_{name}_{tag}_v4.json'
    # Resume only source-pinned receipts with the exact requested settings.
    nc = 2 * lmax
    if not output.exists():
        command = [sys.executable, str(SOLVER), '--name', name,
                   '--nr', str(nr), '--nc', str(nc), '--lmax', str(lmax),
                   '--hankel', str(hankel), '--inner', str(inner), '--outer', str(outer),
                   '--output', str(output)]
        if newtonian:
            command.append('--newtonian')
        with output.with_suffix('.log').open('x') as stream:
            subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=True)
    result = json.loads(output.read_text())
    meta = result['projection']['metadata']
    assert result['source_sha256'] == EXPECTED and result['hankel'] == hankel
    assert (meta['nr'], meta['nc'], meta['lmax'], meta['newtonian']) == (nr, nc, lmax, newtonian)
    assert np.isclose(meta['rmin'], result['source_row']['sigma'] / inner, rtol=0, atol=1e-15)
    assert np.isclose(meta['rmax'], outer * max(result['projection']['R']), rtol=0, atol=1e-12)
    print(json.dumps({'at': result['at'], 'name': name, 'tag': tag,
                      'elapsed_seconds': result['elapsed_seconds']}), flush=True)
    return result


def main():
    guard()
    assert json.loads((OUT / 'DIRECT_NUMERICAL_GATES.json').read_text())['passed']
    frozen = json.loads((OUT / 'contract_and_subset_freeze.json').read_text())
    names = frozen['conditional_expansion']
    assert names == ['NGC3949', 'NGC3972', 'UGC06667', 'UGC08837', 'DDO064', 'DDO168']
    protocol = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'names': names,
                'solver_sha256': EXPECTED, 'runner_sha256': sha(__file__),
                'mode_sequence': [128, 256, 512, 1024], 'radial_points': 1536,
                'angular_points': 'twice lmax', 'stop_on_numerical_failure': True,
                'no_observed_velocities_read': True,
                'limits': 'Same fixed physical contract; numerical mode ceiling extended before any expansion field values. No target-based galaxy selection.'}
    protocol_path = OUT / 'DIRECT_EXPANSION_NUMERICS_FREEZE.json'
    if not protocol_path.exists():
        protocol_path.write_text(json.dumps(protocol, indent=2) + '\n')
    else:
        previous = json.loads(protocol_path.read_text())
        assert previous['runner_sha256'] == sha(__file__) and previous['solver_sha256'] == EXPECTED
    rows = []
    for name in names:
        newton = run(name, 'newtonian', lmax=64, nr=768, newtonian=True)
        newton_error = change(newton['projection']['full'], newton['projection']['newtonian'])
        previous = run(name, 'ell128')
        history = []
        converged = False
        for ell in [256, 512, 1024]:
            current = run(name, f'ell{ell}', lmax=ell)
            delta = change(current['projection']['full'], previous['projection']['full'])
            history.append({'lmax': ell, 'relative_change': delta})
            previous = current
            if delta <= .005:
                converged = True
                break
        final = None
        boundary_error = None
        if converged:
            final = run(name, 'boundary', lmax=ell, hankel=4096, inner=32, outer=16)
            boundary_error = change(final['projection']['full'], current['projection']['full'])
        passed = bool(converged and newton_error <= .003 and boundary_error <= .003
                      and final['newtonian_midplane_relative_error'] <= 2e-6)
        row = {'name': name, 'newtonian_projection_error': newton_error,
               'mode_refinement': history, 'boundary_hankel_grid_change': boundary_error,
               'passed': passed, 'converged_modes': ell if converged else None}
        rows.append(row)
        receipt = OUT / f'DIRECT_EXPANSION_GATE_{name}.json'
        if not receipt.exists():
            receipt.write_text(json.dumps(row, indent=2) + '\n')
        else:
            assert json.loads(receipt.read_text()) == row
        print(json.dumps(row), flush=True)
        if not passed:
            print('Expansion stopped on the first numerical failure; preserve this route and checkpoint.', flush=True)
            break
    output = OUT / 'DIRECT_EXPANSION_GATES.json'
    assert not output.exists()
    output.write_text(json.dumps({'at': dt.datetime.now(dt.timezone.utc).isoformat(),
                                  'rows': rows, 'passed': len(rows) == len(names) and all(r['passed'] for r in rows),
                                  'source_sha256': sha(__file__), 'solver_sha256': EXPECTED}, indent=2) + '\n')


if __name__ == '__main__':
    main()
