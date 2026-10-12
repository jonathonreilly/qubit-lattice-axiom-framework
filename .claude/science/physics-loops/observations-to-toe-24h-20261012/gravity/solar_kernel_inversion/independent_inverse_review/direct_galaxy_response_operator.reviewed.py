#!/usr/bin/env python3
"""Full disk response columns for a frozen monotone inverse family."""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path
import time

import numpy as np
from scipy.special import eval_legendre, roots_legendre

PACK = Path(__file__).resolve().parents[2]
FIELD_PATH = PACK / 'agents/galaxy_response/qumond_disk/direct_qumond_disk.py'
spec = importlib.util.spec_from_file_location('direct_field', FIELD_PATH)
field = importlib.util.module_from_spec(spec)
spec.loader.exec_module(field)
RUNTIME = field.RUNTIME
OUT = RUNTIME / 'gravity/response_inverse'
KNOTS = np.power(10., -13 + np.arange(21) / 4)
SOLVER_HASH = '701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00'
PROTOCOL_HASH = '16ff2920797c5d5fb027a920f623b44983953b022931ef442194f6ac8b2a90ce'


def guard():
    field.guard()
    assert field.sha(FIELD_PATH) == SOLVER_HASH
    assert field.sha(Path(__file__).with_name('FROZEN_DIRECT_INVERSE_PROTOCOL.md')) == PROTOCOL_HASH


def ramp(acceleration, lo, hi):
    a = np.asarray(acceleration)
    value = np.ones_like(a)
    positive = a > 0
    value[positive] = np.clip(np.log(hi / a[positive]) / np.log(hi / lo), 0, 1)
    return value


def geometry(fun, scored, rmin, rmax, nr, nc, lmax):
    guard()
    radius = np.unique(np.r_[np.geomspace(rmin, rmax, nr), scored])
    x, weight = roots_legendre(nc)
    cosine, weight = (x + 1) / 2, weight / 2
    sine = np.sqrt(1 - cosine ** 2)
    ur, uz = fun(radius[:, None] * sine, radius[:, None] * cosine)
    mr, mz = fun(scored, np.zeros_like(scored))
    return {'radius': radius, 'cosine': cosine, 'angular_weights': weight,
            'ur': ur, 'uz': uz, 'mr': mr, 'mz': mz, 'R': scored,
            'lmax': np.array(lmax), 'nr': np.array(nr), 'nc': np.array(nc)}


class LinearProjection:
    def __init__(self, geometry_data):
        self.g = geometry_data
        c, w = self.g['cosine'], self.g['angular_weights']
        sine = np.sqrt(1 - c ** 2)
        modes = np.arange(2, int(self.g['lmax']) + 1, 2, dtype=float)
        p = np.stack([eval_legendre(int(ell), c) for ell in modes], axis=1)
        dp = np.stack([ell * (eval_legendre(int(ell - 1), c) - c * eval_legendre(int(ell), c))
                       / (1 - c * c) for ell in modes], axis=1)
        self.radial_weights = w[:, None] * p * (2 * modes + 1)
        self.polar_weights = -w[:, None] * sine[:, None] * dp * (2 * modes + 1) / (modes * (modes + 1))
        self.modes = modes
        self.mid_factor = modes * (modes + 1) / (2 * modes + 1) * np.array([
            eval_legendre(int(ell), 0.) for ell in modes])
        self.ur_spherical = self.g['ur'] * sine + self.g['uz'] * c
        self.ut_spherical = self.g['ur'] * c - self.g['uz'] * sine
        self.norm_SI = np.hypot(self.g['ur'], self.g['uz']) * field.ACC
        self.mid_norm_SI = np.hypot(self.g['mr'], self.g['mz']) * field.ACC
        self.index = np.searchsorted(self.g['radius'], self.g['R'])
        assert np.array_equal(self.g['radius'][self.index], self.g['R'])

    def project(self, factor, mid_factor):
        guard()
        aa = (factor * self.ur_spherical) @ self.radial_weights
        bb = (factor * self.ut_spherical) @ self.polar_weights
        inside, outside = field.one_sided_convolutions(
            np.log(self.g['radius']), aa + (self.modes + 1) * bb, aa - self.modes * bb, self.modes)
        correction = ((inside[self.index] + outside[self.index]) * self.mid_factor).sum(axis=1)
        return mid_factor * self.g['mr'] - correction

    def column(self, lo, hi):
        return self.project(ramp(self.norm_SI, lo, hi), ramp(self.mid_norm_SI, lo, hi))

    def combined(self, weights):
        value, mid_value = np.ones_like(self.norm_SI), np.ones_like(self.mid_norm_SI)
        for weight, lo, hi in zip(weights, KNOTS[:-1], KNOTS[1:]):
            value += weight * ramp(self.norm_SI, lo, hi)
            mid_value += weight * ramp(self.mid_norm_SI, lo, hi)
        return self.project(value, mid_value)


def controls():
    guard()
    checks = []
    scored = np.geomspace(.2, 10, 25)
    for kind in ['sphere', 'kuzmin']:
        def source(r, z):
            zz = z if kind == 'sphere' else z + 1
            denom = (r * r + z * z + 1) ** 1.5 if kind == 'sphere' else (r * r + zz * zz) ** 1.5
            return 1e4 * r / denom, 1e4 * zz / denom
        projection = LinearProjection(geometry(source, scored, .001, 800, 768, 128, 64))
        # The complete N=1+b fields avoid relative division by a zero column.
        for index in [0, 4, 8, 12, 16, 19]:
            weights = np.zeros(20)
            weights[index] = 1
            actual = projection.combined(weights)
            expected = projection.g['mr'] * (1 + ramp(projection.mid_norm_SI, KNOTS[index], KNOTS[index + 1]))
            error = float(np.max(np.abs(actual / expected - 1)))
            checks.append({'source': kind, 'basis': index, 'relative_error': error,
                           'limit': 1e-9 if kind == 'sphere' else .003})
    return {'passed': all(row['relative_error'] <= row['limit'] for row in checks), 'checks': checks}


def source_receipt(name):
    prefix = 'direct' if name in ['NGC2976', 'UGC07577', 'KK98-251'] else 'expanded'
    return field.DATA / 'qumond_disk' / f'{prefix}_{name}_boundary_v4.json'


def galaxy_geometry(name, tag='base', refine=False):
    guard()
    receipt = source_receipt(name)
    previous = json.loads(receipt.read_text())
    assert previous['source_sha256'] == SOLVER_HASH
    assert previous['source_npz_sha256'] == field.sha(field.DATA / 'baryonic_forward_64.npz')
    meta = previous['projection']['metadata']
    row = previous['source_row']
    settings = {'nr': meta['nr'] * (2 if refine else 1),
                'nc': meta['nc'] * (2 if refine else 1),
                'lmax': meta['lmax'] * (2 if refine else 1),
                'hankel': previous['hankel'], 'rmin': meta['rmin'], 'rmax': meta['rmax']}
    cache = OUT / f'newtonian_field_{name}_{tag}.npz'
    metadata = OUT / f'newtonian_field_{name}_{tag}.json'
    identity = {'name': name, 'solver_sha256': SOLVER_HASH, 'source_receipt_sha256': field.sha(receipt),
                'source_npz_sha256': previous['source_npz_sha256'], 'U': previous['U'], 'settings': settings}
    if cache.exists():
        assert metadata.exists()
        saved = json.loads(metadata.read_text())
        assert saved['identity'] == identity and saved['cache_sha256'] == field.sha(cache)
        with np.load(cache) as archive:
            return {key: archive[key] for key in archive.files}, previous, identity
    with np.load(field.DATA / 'baryonic_forward_64.npz') as raw:
        mask = raw[name + '_score_mask']
        scored = raw[name + '_R'][mask]
        assert np.array_equal(scored, previous['projection']['R'])
        source = field.RingField(raw[name + '_A'], row['sigma'], raw[name + '_gas_masses'],
                                 previous['U'] * raw[name + '_disk_masses'], row['h'], settings['hankel'])
        data = geometry(source, scored, settings['rmin'], settings['rmax'],
                        settings['nr'], settings['nc'], settings['lmax'])
    OUT.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(cache, **data)
    metadata.write_text(json.dumps({'at': dt.datetime.now(dt.timezone.utc).isoformat(),
                                    'identity': identity, 'cache_sha256': field.sha(cache)}, indent=2) + '\n')
    return data, previous, identity


def build_operator(name):
    guard()
    geo, previous, identity = galaxy_geometry(name)
    projection = LinearProjection(geo)
    columns = np.stack([projection.column(lo, hi) for lo, hi in zip(KNOTS[:-1], KNOTS[1:])], axis=1)
    newton_projected = projection.project(1., 1.)
    old_nu = projection.project(field.nu(projection.norm_SI / field.A0_SI),
                                 field.nu(projection.mid_norm_SI / field.A0_SI))
    weights = .03 + (np.arange(20) + 1) / 400
    direct = projection.combined(weights)
    linear = newton_projected + columns @ weights
    checks = {
        'newtonian_projection_relative': float(np.max(np.abs(newton_projected / geo['mr'] - 1))),
        'prior_full_response_relative': float(np.max(np.abs(old_nu / previous['projection']['full'] - 1))),
        'synthetic_superposition_relative': float(np.max(np.abs(direct / linear - 1))),
    }
    assert checks['newtonian_projection_relative'] <= .003
    assert checks['prior_full_response_relative'] <= 1e-10
    assert checks['synthetic_superposition_relative'] <= 1e-11
    return {'name': name, 'R_kpc': geo['R'].tolist(), 'g_N': geo['mr'].tolist(), 'K': columns.tolist(),
            'knots_SI': KNOTS.tolist(), 'units': '(km/s)^2/kpc', 'identity': identity, 'checks': checks,
            'limits': 'Source-pinned baseline grid and synthetic controls. Individual columns not interval certified; final fitted responses require direct refined validation.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--controls', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    guard()
    assert not args.output.exists(), 'Do not overwrite scientific execution receipts'
    source_hash = field.sha(__file__)
    started = time.time()
    result = controls() if args.controls else build_operator(args.name)
    assert field.sha(__file__) == source_hash
    result.update(at=dt.datetime.now(dt.timezone.utc).isoformat(), source_sha256=source_hash,
                  solver_sha256=SOLVER_HASH, protocol_sha256=PROTOCOL_HASH,
                  elapsed_seconds=time.time() - started, observed_velocities_read=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['K', 'g_N', 'R_kpc', 'knots_SI', 'identity']}, indent=2))
    if args.controls and not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
