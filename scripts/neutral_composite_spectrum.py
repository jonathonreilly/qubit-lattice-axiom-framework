#!/usr/bin/env python3
"""Reproduce the scoped neutral-composite milestone from explicit development inputs."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACK = '.claude/science/physics-loops/neutral-composite-24h-20261018'
PROBES = [
    'exact_no_flat_transition', 'rational_spectral_enclosure',
    'finite_range_mode', 'finite_range_verify', 'filter_atom_control',
    'resolvent_limit', 'parity_control',
]
AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = ['data/collective_corner_response/candidate.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/exact_no_flat_transition.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/rational_spectral_enclosure.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_mode.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_verify.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/filter_atom_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/resolvent_limit.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/probes/parity_control.py']

def main():
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1')
    results = {}
    for name in PROBES:
        path = ROOT / PACK / 'probes' / f'{name}.py'
        proc = subprocess.run([sys.executable, str(path)], cwd=ROOT, env=env,
                              capture_output=True, text=True, timeout=120)
        if proc.returncode:
            raise RuntimeError(f'{name}: {proc.stdout}\n{proc.stderr}')
        result = path.with_suffix('.json')
        results[name] = json.loads(result.read_text())
        print(f'reproduced {name}; result_sha256={hashlib.sha256(result.read_bytes()).hexdigest()}')
    output = ROOT / 'outputs/neutral_composite_spectrum/result.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    packet = {
        'scope': 'Supplied quadratic Hamiltonian; fixed Q neutral spectrum; no empirical validation or physical scalar identification.',
        'empirical_data_used': False,
        'scientific_status': 'partial-narrowing with explicit remaining routes',
        'negative_packet_status': 'five-family submission minimum not established; no blanket no-go approval',
        'source_hashes': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        'results': results,
    }
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + '\n')
    print('per_element: exact decimal rational hopping entries and Hermitian pair identities checked')
    print('per_site: checked and not executed — no independent native one-qubit-site dynamics reconstructed in this runner')
    print('per_mode: exact fixed-Q characteristic polynomials and neutral spectral bounds checked')
    print('per_block: finite-range coarse-block bilinear coefficients and independent momentum norms checked')
    print('lattice_wide: analytic infinite-volume implication is proved in source under L2 domain assumptions; numerical grids remain finite')
    print('physical scalar derived: false; canonical matter coupling derived: false')

if __name__ == '__main__':
    main()
