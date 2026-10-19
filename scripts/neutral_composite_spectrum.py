#!/usr/bin/env python3
"""Reproduce the scoped neutral-composite milestone from explicit development inputs."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACK = 'outputs/neutral_composite_review_2026_10_18/helpers'
PROBES = [
    'exact_no_flat_transition', 'rational_spectral_enclosure',
    'finite_range_mode', 'finite_range_verify', 'filter_atom_control',
    'resolvent_limit', 'parity_control',
]
AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = ['data/collective_corner_response/candidate.json', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/exact_no_flat_transition.py', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/filter_atom_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/finite_range_mode.py', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/finite_range_verify.py', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/parity_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/rational_spectral_enclosure.py', 'outputs/neutral_composite_review_2026_10_18/helpers/probes/resolvent_limit.py', 'outputs/neutral_composite_review_2026_10_18/proofs/NEUTRAL_FEATURE_DERIVATION.md', 'outputs/neutral_composite_review_2026_10_18/proofs/SCOPED_SPECTRAL_CERTIFICATE.md', 'outputs/neutral_composite_review_2026_10_18/proofs/HIGHER_NEUTRAL_COMPOSITES.md', 'outputs/neutral_composite_review_2026_10_18/proofs/INDEPENDENT_POLAR_MATH.md']

def main():
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1')
    results = {}
    for name in PROBES:
        path = ROOT / PACK / 'probes' / f'{name}.py'
        proc = subprocess.run([sys.executable, str(path)], cwd=ROOT, env=env,
                              timeout=120)
        if proc.returncode:
            raise RuntimeError(f'{name}: child exit {proc.returncode}; output is in the parent execution capture')
        result = path.with_suffix('.json')
        results[name] = json.loads(result.read_text())
        print(f'reproduced {name}; result_sha256={hashlib.sha256(result.read_bytes()).hexdigest()}')
    output = ROOT / 'outputs/neutral_composite_spectrum/result.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    packet = {
        'scope': 'Supplied quadratic Hamiltonian; fixed Q neutral spectrum; no empirical validation or physical scalar identification.',
        'empirical_data_used': False,
        'scientific_status': 'constructive calculations and finite controls; negative theorems deferred',
        'negative_packet_status': 'five-family submission minimum not established; no blanket no-go approval',
        'source_hashes': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        'results': results,
    }
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + '\n')
    print('per_element: exact decimal rational hopping entries and Hermitian pair identities checked')
    print('per_site: checked and not executed — no independent native one-qubit-site dynamics reconstructed in this runner')
    print('per_mode: exact fixed-Q characteristic polynomials and neutral spectral bounds checked')
    print('per_block: finite-range coarse-block bilinear coefficients and independent momentum norms checked')
    print('lattice_wide: numerical grids remain finite; infinite-volume negative continuation deferred with incomplete N1 packet')
    print('physical scalar derived: false; canonical matter coupling derived: false')

if __name__ == '__main__':
    main()
