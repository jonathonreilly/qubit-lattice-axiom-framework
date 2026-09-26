#!/usr/bin/env python3
"""Rebuild original N<=128 statistics directly from all stored Fourier histories.

This script does not read saved PER_HISTORY, original result cells or by-axis
comparison values. No author observable function is imported.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import math
import numpy as np

OUT = Path(__file__).resolve().parent
SCREEN = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/dimer_routed_dynamic_screen')
TIMES = [0., 7/16, 7/8, 21/16, 7/4]
METRICS = ['propagation_residual', 'transverse_autocovariance', 'signed_cross_covariance', 'longitudinal_autocovariance']


def ident(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def verified(row):
    assert ident(Path(row['path'])) == row, row['path']
    return row


def aggregate(data):
    x = np.asarray(data, dtype=float)
    flat = x.reshape(len(x), -1)
    means, ses = [], []
    for column in flat.T:
        mu = math.fsum(map(float, column)) / len(column)
        variance_of_mean = math.fsum((float(v) - mu) ** 2 for v in column) / (len(column) * (len(column) - 1))
        means.append(mu); ses.append(math.sqrt(variance_of_mean))
    shape = x.shape[1:]
    return {'mean': np.asarray(means).reshape(shape).tolist(),
            'standard_error': np.asarray(ses).reshape(shape).tolist()}


def observables(fields):
    result = np.empty((5, 3, 4))
    for mode in range(3):
        n = np.eye(3)[mode]
        e0, b0 = fields[0, mode, :3], fields[0, mode, 3:]
        ep, bp = n * e0[mode], n * b0[mode]
        de, db = 1j * np.cross(n, b0), -1j * np.cross(n, e0)
        for time_index, time in enumerate(TIMES):
            e, b = fields[time_index, mode, :3], fields[time_index, mode, 3:]
            angle = 4 * math.pi * time / 7
            prediction_e = ep + math.cos(angle) * (e0 - ep) + math.sin(angle) * de
            prediction_b = bp + math.cos(angle) * (b0 - bp) + math.sin(angle) * db
            residual = (np.vdot(e - prediction_e, e - prediction_e).real + np.vdot(b - prediction_b, b - prediction_b).real) / 6
            transverse = (np.vdot(e0 - ep, e).real + np.vdot(b0 - bp, b).real) / 4
            cross = (np.vdot(de, e).real + np.vdot(db, b).real) / 4
            longitudinal = (np.conj(e0[mode]) * e[mode] + np.conj(b0[mode]) * b[mode]).real / 2
            result[time_index, mode] = [residual, transverse, cross, longitudinal]
    return result


def main():
    manifest_path, summary_path, dispatch_path = [SCREEN / x for x in ['MANIFEST.json', 'SUMMARY.json', 'DISPATCH.json']]
    manifest = json.loads(manifest_path.read_text())
    # Assert the original size boundary before opening even one history.
    assert len(manifest['jobs']) == 960
    assert set(j['N'] for j in manifest['jobs']) == {16, 32, 64, 128}
    assert len({j['seed'] for j in manifest['jobs']}) == 960
    summary = json.loads(summary_path.read_text()); dispatch = json.loads(dispatch_path.read_text())
    assert summary['statuses'] == {'complete_verified_receipt': 960}
    assert summary['manifest'] == dispatch['manifest'] == ident(manifest_path)
    assert summary['dispatch'] == ident(dispatch_path)
    bindings = [ident(manifest_path), ident(summary_path), ident(dispatch_path)]
    bindings += [verified(manifest['binary']), verified(dispatch['wrapper'])]
    for row in dispatch['source_snapshots']:
        bindings.append(verified(row['snapshot']))
        assert row['snapshot']['sha256'] == row['original']['sha256']
        assert row['snapshot']['bytes'] == row['original']['bytes']
    for row in manifest['geometry']:
        bindings.append(verified(row['file']))
    completed = {(r['N'], r['kind'], r['replicate']): r for r in summary['rows']}
    assert len(completed) == 960
    cells, histories, payload_bindings, receipt_bindings = {}, [], [], []
    for job in sorted(manifest['jobs'], key=lambda j: (j['N'], j['kind'], j['replicate'])):
        key = (job['N'], job['kind'], job['replicate'])
        row = completed[key]
        assert row['seed'] == job['seed'] and row['status'] == 'complete_verified_receipt'
        receipt_bindings.append(verified(row['receipt']))
        receipt = json.loads(Path(row['receipt']['path']).read_text())
        assert receipt['job'] == job and receipt['returncode'] == 0
        assert receipt['status'] == 'complete_verified_receipt'
        assert {v['path'] for v in receipt['outputs']} == {job['output'] + x for x in ['', '.state', '.stdout', '.stderr']}
        # Byte authentication of all original output payloads, without decoding
        # endpoint .state files or claiming any trajectory replay.
        payload_bindings += [verified(v) for v in receipt['outputs']]
        raw = json.loads(Path(job['output']).read_text())
        assert raw['N'] == job['N'] and raw['seed'] == job['seed'] and raw['mode'] == 'production'
        k = job['N'] ** 3 // 2
        assert raw['pairs'] == k and raw['channels'] == 5 * k
        assert raw['minimum_nontrivial_cycle'] >= job['N'] // 2
        assert raw['key_permutation_verified'] and raw['counts_verified']
        assert len(raw['color_counts']) == 14 and sum(raw['color_counts']) == k
        assert raw['gamma'] == 1 and raw['k0'] == 1.1
        assert 0 <= raw['color_changes'] <= raw['accepted'] <= raw['attempts']
        assert [x['t'] for x in raw['snapshots']] == TIMES
        encoded = np.asarray([x['fields'] for x in raw['snapshots']], dtype=float)
        assert encoded.shape == (5, 3, 6, 2) and np.isfinite(encoded).all()
        field = encoded[..., 0] + 1j * encoded[..., 1]
        field[..., :3] *= math.sqrt(7); field[..., 3:] *= math.sqrt(7) / 2
        values = observables(field)
        assert np.max(values[0, :, 0]) < 1e-25
        data = {'N': key[0], 'kind': key[1], 'replicate': key[2], 'seed': job['seed'],
                'by_time_mode_metric': values.tolist()}
        for name in ['attempts', 'accepted', 'color_changes', 'wall_seconds']:
            data[name] = raw[name]
        histories.append(data)
        cells.setdefault(key[:2], []).append((data, np.abs(field) ** 2))
    results = []
    for (N, kind), rows in sorted(cells.items()):
        count = {16: 256, 32: 128, 64: 64, 128: 32}[N]
        assert len(rows) == count and [r['replicate'] for r, _ in rows] == list(range(1, count + 1))
        x = np.asarray([r['by_time_mode_metric'] for r, _ in rows])
        # Each within-history mean is computed before any between-history SE.
        av = np.asarray([[[math.fsum(x[h, t, :, j]) / 3 for j in range(4)] for t in range(5)] for h in range(count)])
        cell = {'N': N, 'kind': kind, 'histories': count, 'times': TIMES, 'metrics': METRICS,
                'by_mode': aggregate(x), 'mode_average': aggregate(av),
                'normalized_component_variances': aggregate([v for _, v in rows])}
        for name in ['attempts', 'accepted', 'color_changes', 'wall_seconds']:
            cell[name] = aggregate([r[name] for r, _ in rows])
        results.append(cell)
        print('reconstructed', N, kind, count, 'whole histories', flush=True)
    auth = {'created_utc': datetime.now(timezone.utc).isoformat(), 'sources': bindings,
            'history_receipts': receipt_bindings, 'history_payloads': payload_bindings,
            'authenticated_payload_bytes': sum(r['bytes'] for r in payload_bindings),
            'states_decoded': False, 'trajectory_replay': False,
            'N256_observable_access': False}
    (OUT / 'RAW_HISTORY_AUTHENTICATION.json').write_text(json.dumps(auth, indent=2) + '\n')
    (OUT / 'REBUILT_PER_HISTORY.json').write_text(json.dumps({'times': TIMES, 'metrics': METRICS, 'rows': histories}, indent=2) + '\n')
    (OUT / 'REBUILT_AGGREGATES.json').write_text(json.dumps({'cells': results, 'scope': 'Independent raw-history component formulas and compensated whole-history mean/SE sums. Bootstrap comparison is a separate later step.'}, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'histories': len(histories), 'cells': len(results),
                      'authenticated_payloads': len(payload_bindings), 'payload_bytes': auth['authenticated_payload_bytes']}))


if __name__ == '__main__':
    main()
