"""Reproduce one frozen original job under fresh INNER/OUTER record names.

This post-execution convenience driver is not itself an original science run.
It uses the recovery manifest, with the original note's immutable frozen copy.
"""
import argparse
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST_SHA = '3fbcd8c8c808d8932f9d1e6ac084639a7800edad6b84021d42c5090999905907'
CANDIDATES = {
    'baseline': ROOT / 'candidate.py',
    'drop_jacobian': ROOT / 'variants/drop_jacobian.py',
    'reverse_cell_phase': ROOT / 'variants/reverse_cell_phase.py',
}
p = argparse.ArgumentParser()
p.add_argument('job', choices=CANDIDATES)
p.add_argument('--label', required=True)
a = p.parse_args()
if not re.fullmatch(r'[A-Za-z0-9_-]+', a.label):
    p.error('label must contain only letters, digits, underscore and hyphen')
base = ROOT / 'reproductions' / a.label
base.mkdir(parents=True, exist_ok=True)
recorder = [sys.executable, str(ROOT / 'record_process.py')]
anchor = ['--manifest', str(ROOT / 'reproduction_manifest.json'),
          '--manifest-sha', MANIFEST_SHA]
inner = recorder + ['--record', str(base / (a.job + '_inner')),
                    '--timeout', '60'] + anchor + ['--', sys.executable,
                    str(ROOT / 'check_controls.py'), '--candidate',
                    str(CANDIDATES[a.job])]
outer = recorder + ['--record', str(base / (a.job + '_outer')),
                    '--timeout', '70'] + anchor + ['--'] + inner
sys.exit(subprocess.run(outer, cwd=ROOT).returncode)
