#!/usr/bin/env python3
"""Actual bounded source faults for block24; no independent review claim."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import tempfile

PACK = Path(__file__).resolve().parent
SOURCE = PACK/'block24_smoothing_check.py'
FAULTS = [
 ('fold_image_sign', 'kprime = k - D @ ell', 'kprime = k + D @ ell', 'check_chain_and_folding'),
 ('completion_drift_sign', 'r = theta - beta * M.inv() * D.T * Fs', 'r = theta + beta * M.inv() * D.T * Fs', 'check_completion_and_bundle'),
 ('haar_determinant_factor', '* theta_fourier/np.sqrt(np.linalg.det(A))', '* theta_fourier*np.sqrt(np.linalg.det(A))', 'check_poisson_density'),
 ('filtered_noise_scale', 'K = 1/(1+noise_var)', 'K = 1/(1+2*noise_var)', 'check_one_plaquette_law'),
 ('electric_theta_exponent', 'mp.exp(-g*g*j*j/34)*mp.cos(g*j*z)', 'mp.exp(-g*g*j*j/32)*mp.cos(g*j*z)', 'check_one_plaquette_law'),
 ('density_partition_factor', 'mp.sqrt(2*mp.pi*K)/denominator', 'mp.sqrt(2*mp.pi*K)*denominator', 'check_one_plaquette_law'),
 ('integer_strip_orientation', 'sign = 1 if axis < direction else -1', 'sign = 1', 'check_fillings_and_gauge'),
 ('gauge_projection_dropped', 'divergence = N*(G.T @ candidate)', 'divergence = np.zeros(G.shape[1], dtype=int)', 'check_fillings_and_gauge'),
 ('carrier_filling_extension', 'off_carrier = flux_numer.astype(float)/7 + .013*(B.T @ cube)', 'off_carrier = flux_numer.astype(float)/7', 'check_fillings_and_gauge'),
 ('massive_covariance_subtraction', 'Cscaled = invA/64-np.eye(len(cc[1]))/128', 'Cscaled = invA/64-np.eye(len(cc[1]))/64', 'check_massive_geometry'),
 ('cubic_orientation_parity', 'orientation *= (-1)**inversions', 'orientation *= 1', 'check_cubic_filling_average'),
 ('overlapping_current_components', 'if any(supports[i] & supports[j] for i, j in itertools.combinations(active, 2)):\n            continue', 'if False:\n            continue', 'check_polymer_positivity_and_response'),
 ('gaussian_response_covariance', "hessian = mean2+np.einsum('a,ai,aj->ij', tilted, centered, centered)", 'hessian = mean2', 'check_polymer_positivity_and_response'),
 ('third_response_cumulant', "+np.einsum('a,ai,aj,ak->ijk', tilted, centered, centered, centered))", "+0*np.einsum('a,ai,aj,ak->ijk', tilted, centered, centered, centered))", 'check_polymer_positivity_and_response'),
 ('source_filter_removed', 'K = np.linalg.inv(np.eye(6)+tau*D @ D.conj().T)', 'K = np.eye(6, dtype=complex)', 'check_macroscopic_sources'),
]


def main():
    body = SOURCE.read_text()
    records = []
    with tempfile.TemporaryDirectory(prefix='toe-block24-faults-') as temp:
        for name, old, new, family in FAULTS:
            assert body.count(old) == 1, (name, body.count(old))
            mutant = body.replace(old, new, 1)
            path = Path(temp)/f'{name}.py'
            path.write_text(mutant)
            invocation = "import runpy; n=runpy.run_path("+repr(str(path))+"); n["+repr(family)+"]()"
            result = subprocess.run([sys.executable, '-c', invocation], text=True,
                                    capture_output=True, timeout=60)
            record = {'fault': name, 'check': family, 'exit_code': result.returncode,
                      'stdout': result.stdout, 'stderr': result.stderr,
                      'original': old, 'replacement': new,
                      'mutated_sha256': hashlib.sha256(mutant.encode()).hexdigest(),
                      'caught': result.returncode != 0 and 'AssertionError' in result.stderr}
            records.append(record)
            print(json.dumps(record), flush=True)
    receipt = {'at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'source': SOURCE.name, 'source_sha256': hashlib.sha256(body.encode()).hexdigest(),
               'faults': records, 'all_caught': all(r['caught'] for r in records),
               'interpretation': 'Actual source mutations caught by finite author falsifiers; not independent review or a general proof.'}
    (PACK/'BLOCK24_MUTATION_CHECKS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    assert receipt['all_caught']


if __name__ == '__main__':
    main()
