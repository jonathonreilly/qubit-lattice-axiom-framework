#!/usr/bin/env python3
"""Narrow remaining provenance and display checks; no statistical rerun."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

OUT = Path(__file__).resolve().parent
RAW = OUT.parent


def ident(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def verify(r):
    assert ident(Path(r['path'])) == r
    return r


def main():
    auth = json.loads((RAW / 'dimer_routed_dynamic_results/AUTHENTICATION.json').read_text())
    own = json.loads((OUT / 'REBUILT_PER_HISTORY.json').read_text())
    histories = {(r['N'], r['kind'], r['replicate']): r for r in own['rows']}
    for row in auth['history_receipts']:
        verify(row['receipt'])
        receipt = json.loads(Path(row['receipt']['path']).read_text())
        job = receipt['job']; key = row['N'], row['kind'], row['replicate']
        assert key == (job['N'], job['kind'], job['replicate'])
        assert job['seed'] == histories[key]['seed']
    receipt_path = RAW / 'dimer_routed_finite_wavelength_comparison/RECEIPT.json'
    receipt = json.loads(receipt_path.read_text())
    for r in [receipt['source']] + receipt['inputs'] + receipt['outputs']:
        verify(r)
    comparison = json.loads((RAW / 'dimer_routed_finite_wavelength_comparison/RESULTS.json').read_text())
    row = next(r for r in comparison['by_axis'] if r['N'] == 64 and r['axis'] == 0)
    mean = row['observed_mean'][3][0]; se = row['observed_standard_error'][3][0]
    assert row['times'][3] == 21/16
    assert mean < 2.3 < mean + se < 2.4
    source = RAW / 'compare_dimer_routed_finite_wavelength.py'
    assert source.read_text().splitlines()[71].strip() == "ax.set_ylim((-.08,2.3) if panel==0 else (-.15,1.18))"
    finding = {'id': 'F1', 'type': 'minor display correction', 'status': 'open at final review seal',
               'source': ident(source), 'line': 72,
               'description': 'Fixed upper y-limit clips the top of one displayed one-standard-error bar.',
               'cell': {'N': 64, 'kind': 'winding', 'axis': 0, 'time': 21/16,
                        'metric': 'propagation_residual', 'mean': mean, 'standard_error': se,
                        'upper_endpoint': mean + se, 'display_limit': 2.3},
               'narrow_correction': 'Raise only the error-panel upper limit above 2.308821018867613, for example to 2.4. Retain all numerical estimates, comparisons and scope labels.',
               'scientific_values_affected': False,
               'parent_response': 'Parent acknowledged and will preserve old sources/plots before a separate narrow correction acknowledgment.'}
    (OUT / 'FINDINGS.json').write_text(json.dumps([finding], indent=2) + '\n')
    result = {'created_utc': datetime.now(timezone.utc).isoformat(), 'author_receipt_key_mappings_checked': len(histories),
              'plot_receipt': ident(receipt_path), 'plot_bound_files': [receipt['source']] + receipt['inputs'] + receipt['outputs'],
              'visual_check': 'PNG viewed after exact numeric clipping detection; displays benchmark and post-outcome scope labels. PDF bytes authenticated, not separately rendered.',
              'protocol': ident(RAW / 'DIMER_ROUTED_DYNAMIC_SCREEN_PROTOCOL.md'), 'findings': [finding]}
    (OUT / 'FINAL_EVIDENCE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'receipt_key_mappings': len(histories), 'finding': 'F1: one clipped uncertainty-bar cap; numerical values correct'}))


if __name__ == '__main__':
    main()
