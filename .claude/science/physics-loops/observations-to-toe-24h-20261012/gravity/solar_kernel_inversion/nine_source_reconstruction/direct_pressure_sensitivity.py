#!/usr/bin/env python3
"""Post-result sensitivity of exact finite LP certificates to pressure readout."""
from fractions import Fraction as F
import datetime as dt
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = ROOT / 'gravity/response_inverse/nine_source'
CERT = OUT / 'finite_lp_certificates_v1'
SOURCE = ROOT / 'galaxy_response/baryonic_forward_64.npz'
TARGET = ROOT / 'galaxy_response/sealed_targets.npz'

def ratio(v):
    return [str(v.numerator), str(v.denominator)]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    dest = OUT / 'PRESSURE_SENSITIVITY_v1.json'
    assert not dest.exists()
    frozen = json.loads((OUT / 'FREEZE.json').read_text())['identities']
    assert sha(SOURCE) == frozen['source_data']
    assert sha(TARGET) == frozen['target_data']
    results = []
    with np.load(SOURCE) as source, np.load(TARGET) as target:
        for family in ['M', 'D']:
            cp = CERT / f'{family}_galaxies_only_certificate.json'
            mp = CERT / f'{family}_galaxies_only_matrix.json'
            c, m = json.loads(cp.read_text()), json.loads(mp.read_text())
            assert sha(mp) == c['matrix_sha256']
            lower = F(*map(int, c['lower_bound_rational']))
            terms = []
            for label, rat in zip(m['row_labels'], c['y_rational']):
                y = F(*map(int, rat))
                if not y or 'source' not in label:
                    continue
                name, i = label['source'], label['scored_bin']
                mask = source[name + '_score_mask']
                radius = source[name + '_R'][mask]
                velocity = target[name + '_v'][mask]
                acceleration = velocity * velocity / radius
                # Keep the actual frozen numeric normalization: p/(R*A).
                scale = F(float(radius[i])) * F(float(acceleration[i]))
                sign = 1 if label['kind'].startswith('upper') else -1
                coefficient = sign * y / scale
                terms.append({**label, 'velocity_km_s': float(velocity[i]),
                              'coefficient_rational': ratio(coefficient),
                              'coefficient_approximate': float(coefficient)})
            relieving = [x for x in terms if x['source'] == 'UGC07577'
                         and F(*map(int, x['coefficient_rational'])) < 0]
            total = -sum(F(*map(int, x['coefficient_rational'])) for x in relieving)
            necessary_max_p = lower / total
            result = {'family': family, 'certificate_sha256': sha(cp), 'terms': terms,
                      'lower_bound_rational': ratio(lower),
                      'scenario': 'Only UGC07577 pressure shifts allowed; all other source bounds and matrix fixed.',
                      'necessary_max_pressure_km2_s2_rational': ratio(necessary_max_p),
                      'necessary_max_pressure_km2_s2_approximate': float(necessary_max_p),
                      'illustrative_slope_if_sigma_8_km_s': float(necessary_max_p / 64),
                      'necessary_not_sufficient': True}
            if len(relieving) == 1:
                v = relieving[0]['velocity_km_s']
                result.update(R_kpc=relieving[0]['R_kpc'],
                              central_speed_illustration_km_s=float(np.sqrt(v*v+float(necessary_max_p))),
                              central_speed_increase_illustration_km_s=float(np.sqrt(v*v+float(necessary_max_p))-v))
            results.append(result)
    data = {'at': dt.datetime.now(dt.timezone.utc).isoformat(),
            'source_sha256': sha(Path(__file__)), 'source_data_sha256': sha(SOURCE),
            'target_data_sha256': sha(TARGET),
            'definition': 'p_i=v_c^2-v_phi^2; both squared-speed rectangle endpoints shift by p_i. The original normalization A_i is held fixed.',
            'identity': 't >= original_exact_lower_bound + sum_i coefficient_i * p_i',
            'limits': 'Necessary finite-matrix sensitivity, not a new fit, pressure measurement, physical field exclusion, or proof of sufficiency. sigma=8 is an illustrative source-model assumption, not a local dispersion measurement.',
            'results': results}
    dest.write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
