#!/usr/bin/env python3
"""Standard-library exact verifier; no optimizer or fit-code imports."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

def check(directory):
    results = []
    for cp in sorted(directory.glob('*_certificate.json')):
        c = json.loads(cp.read_text())
        mp = directory / (c['name'] + '_matrix.json')
        assert hashlib.sha256(mp.read_bytes()).hexdigest() == c['matrix_sha256']
        m = json.loads(mp.read_text())
        a = [[F(float.fromhex(v)) for v in row] for row in m['A_hex']]
        b = [F(float.fromhex(v)) for v in m['b_hex']]
        y = [F(int(n), int(d)) for n, d in c['y_rational']]
        assert m['objective'] == [0] * 20 + [1]
        assert len(a) == len(b) == len(y)
        assert all(len(row) == 21 for row in a)
        assert all(v <= 0 for v in y)
        cap = F(c['weight_cap'])
        assert cap == 100
        assert any(row == [F(1)] * 20 + [F(0)] and bi == cap for row, bi in zip(a, b))
        sums = [sum(row[j] * yi for row, yi in zip(a, y)) for j in range(21)]
        assert sums[-1] <= 1
        deficit = max([F(0)] + sums[:-1])
        lower = sum(bi * yi for bi, yi in zip(b, y)) - cap * deficit
        assert deficit == F(*map(int, c['weight_deficit_rational']))
        assert 1 - sums[-1] == F(*map(int, c['time_residual_rational']))
        assert lower == F(*map(int, c['lower_bound_rational']))
        assert 0 < F(c['lower_bound_decimal_downward']) <= lower
        results.append({'name': c['name'], 'lower_bound': c['lower_bound_decimal_downward'],
                        'exact_arithmetic_pass': True})
    assert len(results) == 6
    return results

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('directory', type=Path)
    print(json.dumps(check(p.parse_args().directory), indent=2))
