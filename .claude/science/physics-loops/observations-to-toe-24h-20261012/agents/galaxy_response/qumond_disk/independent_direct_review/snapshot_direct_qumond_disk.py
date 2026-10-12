#!/usr/bin/env python3
"""Direct-author fixed-source QUMOND projection; no observed-velocity fitting."""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.constants import parsec
from scipy.integrate import quad
from scipy.special import eval_legendre, i0e, i1e, j0, j1, roots_legendre, erfcx

RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
DATA = RUNTIME / 'galaxy_response'
G = 4.30091e-6
ACC = 1e6 / (1000 * parsec)
A0_SI = 7.658058668049826e-11
STELLAR_U = 0.5605122519882025


def guard():
    if time.time() >= json.loads((RUNTIME / 'DEADLINE.json').read_text())['packaging_epoch']:
        raise RuntimeError('Discovery window ended under the original campaign clock')
    if any((RUNTIME / name).exists() for name in
           ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json')):
        raise RuntimeError('Campaign stop marker present')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def nu(y):
    if np.any(np.asarray(y) <= 0):
        raise ValueError('This evaluation requires a nonzero Newtonian field')
    return 1 / (-np.expm1(-np.sqrt(y)))


def vertical(k, z, h):
    """Upper-half-space exponential vertical convolution and its derivative."""
    k = np.asarray(k)[None, :]
    z = np.asarray(z)[:, None]
    if h == 0:
        value = np.exp(-z * k)
        return value, value
    t, u = k * h, z / h
    d = t - 1
    e = np.exp(-u)
    difference = np.exp(-t * u) - e
    near = np.abs(d * u) < .5
    # Compute the cancellation-sensitive difference only on its safe domain.
    du = np.broadcast_to(-d * u, difference.shape)
    ee = np.broadcast_to(e, difference.shape)
    difference[near] = ee[near] * np.expm1(du[near])
    denominator = np.broadcast_to(-d * (1 + t), difference.shape)
    exact = np.broadcast_to(np.abs(d) < 1e-12, difference.shape)
    v = np.divide(difference, denominator, out=np.zeros_like(difference), where=~exact)
    v[exact] = np.broadcast_to(u * e / 2, difference.shape)[exact]
    return v + e / (1 + t), v


class RingField:
    """Two positive ring mixtures: a gas sheet and exponential-height stars."""
    def __init__(self, radii, sigma, gas, stars, height, hankel=1024, g=G):
        x, w = roots_legendre(hankel)
        self.k = (x + 1) * 4 / sigma
        self.weights = w * 4 / sigma
        self.radii = np.asarray(radii)
        self.sigma = sigma
        self.gas = np.asarray(gas)
        self.stars = np.asarray(stars)
        self.height = height
        self.g = g
        transform = j0(np.outer(self.k, radii))
        common = self.k * self.weights * np.exp(-.5 * (self.k * sigma) ** 2)
        self.gas_kernel = common * (transform @ gas)
        self.star_kernel = common * (transform @ stars)

    def gas_trace(self, radius):
        r = np.asarray(radius)[:, None]
        a = self.radii[None, :]
        surface = np.exp(-.5 * ((r - a) / self.sigma) ** 2)
        surface *= i0e(r * a / self.sigma ** 2) / (2 * np.pi * self.sigma ** 2)
        return 2 * np.pi * self.g * (surface @ self.gas)

    def __call__(self, radius, z):
        shape = np.broadcast_shapes(np.shape(radius), np.shape(z))
        radius = np.broadcast_to(radius, shape).ravel()
        z = np.broadcast_to(z, shape).ravel()
        if np.any(z < 0):
            raise ValueError('Upper-half-space field only')
        ur = np.empty_like(radius)
        uz = np.empty_like(radius)
        for begin in range(0, len(radius), 128):
            guard()
            end = begin + 128
            rr, zz = radius[begin:end], z[begin:end]
            kr = np.outer(rr, self.k)
            jrad, jvert = j1(kr), j0(kr)
            zg, vg = vertical(self.k, zz, 0.)
            zs, vs = vertical(self.k, zz, self.height)
            ur[begin:end] = self.g * np.sum(jrad * (zg * self.gas_kernel + zs * self.star_kernel), axis=1)
            uz[begin:end] = self.g * np.sum(jvert * (vg * self.gas_kernel + vs * self.star_kernel), axis=1)
        at_sheet = z == 0
        if np.any(at_sheet):
            uz[at_sheet] = self.gas_trace(radius[at_sheet])
        return ur.reshape(shape), uz.reshape(shape)


def one_sided_convolutions(log_radius, values_inside, values_outside, modes):
    """Exact cell integrals of the piecewise-linear coefficients in log r."""
    s = np.zeros_like(values_inside)
    t = np.zeros_like(values_outside)

    def coefficients(rate, delta):
        x = rate * delta
        decay = np.exp(-x)
        a = -np.expm1(-x) / rate
        # Integral_0^delta y exp(-rate*y) dy, with a small-x expansion.
        b = (-np.expm1(-x) - x * decay) / rate ** 2
        small = np.abs(x) < 1e-3
        xx = x[small]
        b[small] = delta ** 2 * (.5 - xx/3 + xx**2/8 - xx**3/30 + xx**4/144)
        return decay, a, b / delta

    for i, delta in enumerate(np.diff(log_radius), start=1):
        decay, a, b = coefficients(modes + 2, delta)
        s[i] = decay * s[i-1] + b * values_inside[i-1] + (a-b) * values_inside[i]
    for i in range(len(log_radius)-2, -1, -1):
        delta = log_radius[i+1] - log_radius[i]
        decay, a, b = coefficients(modes - 1, delta)
        t[i] = decay * t[i+1] + (a-b) * values_outside[i] + b * values_outside[i+1]
    return s, t


def project(field, scored, rmin, rmax, a0, nr=384, nc=64, lmax=32, newtonian=False):
    guard()
    radii = np.unique(np.r_[np.geomspace(rmin, rmax, nr), scored])
    x, w = roots_legendre(nc)
    c, w = (x+1)/2, w/2
    sine = np.sqrt(1-c*c)
    rr, zz = radii[:, None]*sine, radii[:, None]*c
    ur, uz = field(rr, zz)
    factor = np.ones_like(ur) if newtonian else nu(np.hypot(ur, uz)/a0)
    ar = factor * (ur * sine + uz * c)
    atheta = factor * (ur * c - uz * sine)
    modes = np.arange(2, lmax+1, 2, dtype=float)
    p = np.stack([eval_legendre(int(l), c) for l in modes], axis=1)
    dp = np.stack([l*(eval_legendre(int(l-1), c)-c*eval_legendre(int(l), c))/(1-c*c)
                   for l in modes], axis=1)
    dtheta = -sine[:, None] * dp
    aa = ar @ (w[:, None] * p * (2*modes+1))
    bb = atheta @ (w[:, None] * dtheta * (2*modes+1)/(modes*(modes+1)))
    s, t = one_sided_convolutions(np.log(radii), aa+(modes+1)*bb, aa-modes*bb, modes)
    at = np.searchsorted(radii, scored)
    correction_modes = ((s[at]+t[at]) * modes*(modes+1)/(2*modes+1)
                        * np.array([eval_legendre(int(l), 0) for l in modes]))
    mr, mz = field(scored, np.zeros_like(scored))
    local_norm = mr if newtonian else nu(np.hypot(mr, mz)/a0)*mr
    algebraic = mr if newtonian else np.where(mr > 0, nu(np.abs(mr)/a0)*mr, np.nan)
    full = local_norm - correction_modes.sum(axis=1)
    return {'R': scored, 'newtonian': mr, 'sheet_vertical': mz, 'algebraic': algebraic,
            'local_norm': local_norm, 'full': full, 'correction_modes': correction_modes,
            'coefficient_radii': radii, 'a_modes': aa, 'b_modes': bb,
            'metadata': {'nr': nr, 'actual_nr': len(radii), 'nc': nc, 'lmax': lmax,
                         'rmin': rmin, 'rmax': rmax, 'newtonian': newtonian}}


def controls():
    checks = {}
    gauss = RingField([0.], 1., [1.], [0.], .2, hankel=2048, g=1.)
    r = np.array([.2, .5, 1., 2., 5.])
    value, vertical_value = gauss(r, np.zeros_like(r))
    z = r*r/4
    expected = np.sqrt(np.pi/2)*r/2*(i0e(z)-i1e(z))
    checks['gaussian_midplane'] = float(np.max(np.abs(value/expected-1)))
    _, axial = gauss(np.zeros_like(r), r)
    axial_expected = 1 - np.sqrt(np.pi/2)*r*erfcx(r/np.sqrt(2))
    checks['gaussian_axis'] = float(np.max(np.abs(axial/axial_expected-1)))
    errors = []
    for k in [.2, 1., 1+1e-9, 3.]:
        for z in [0., .3, 2., 10.]:
            zh, vh = vertical(np.array([k]), np.array([z]), 1.)
            density = lambda v: np.exp(-abs(v))/2
            zz = sum(quad(lambda v: density(v)*np.exp(-k*abs(z-v)), a, b,
                          epsabs=1e-13, epsrel=1e-12)[0]
                     for a, b in [(-np.inf, 0), (0, z), (z, np.inf)])
            vv = sum(quad(lambda v: density(v)*np.exp(-k*abs(z-v))*np.sign(z-v), a, b,
                          epsabs=1e-13, epsrel=1e-12)[0]
                     for a, b in [(-np.inf, 0), (0, z), (z, np.inf)])
            errors.extend([abs(float(zh[0, 0])-zz), abs(float(vh[0, 0])-vv)])
    checks['vertical_convolution_absolute'] = float(max(errors))

    def plummer(r, z):
        denom = (r*r+z*z+1)**1.5
        return r/denom, z/denom
    test = np.geomspace(.2, 10, 25)
    sph = project(plummer, test, .002, 300, .2, nr=384, nc=64, lmax=32)
    checks['spherical_projection_relative'] = float(np.max(np.abs(sph['full']/sph['algebraic']-1)))

    def kuzmin(r, z):
        denom = (r*r+(z+1)**2)**1.5
        return r/denom, (z+1)/denom
    kuzmin_rows = []
    for nr, nc, lmax in [(384, 64, 32), (768, 128, 64)]:
        k = project(kuzmin, test, .001, 800, .2, nr=nr, nc=nc, lmax=lmax)
        exact = nu(1/(.2*(test*test+1))) * test/(test*test+1)**1.5
        err = float(np.max(np.abs(k['full']/exact-1)))
        kuzmin_rows.append({'nr': nr, 'nc': nc, 'lmax': lmax, 'max_relative': err})
    checks['kuzmin_projection_relative'] = kuzmin_rows[-1]['max_relative']
    # A single non-spherical gradient mode tests the radial convolutions alone.
    radius = np.geomspace(1e-5, 1e4, 2500)
    modes = np.array([2., 4., 8.])
    f = radius[:, None]**modes/(1+radius[:, None])**(2*modes+1)
    aa = f*(modes/radius[:, None]-(2*modes+1)/(1+radius[:, None]))
    bb = f/radius[:, None]
    s, t = one_sided_convolutions(np.log(radius), aa+(modes+1)*bb, aa-modes*bb, modes)
    checks['gradient_radial_cancellation_normalized'] = float(np.max(np.abs(s+t))/np.max(np.abs(bb)))
    passed = (checks['gaussian_midplane'] < 5e-7 and checks['gaussian_axis'] < 5e-7
              and checks['vertical_convolution_absolute'] < 5e-7
              and checks['spherical_projection_relative'] < 1e-9
              and checks['kuzmin_projection_relative'] < .003
              and checks['gradient_radial_cancellation_normalized'] < 5e-4)
    return {'checks': checks, 'kuzmin_refinement': kuzmin_rows, 'passed': bool(passed)}


def galaxy(name, args):
    report = json.loads((DATA/'baryonic_reconstruction_64.json').read_text())
    row = next(x for x in report['rows'] if x['name'] == name)
    with np.load(DATA/'baryonic_forward_64.npz') as raw:
        radii = raw[name+'_R'][raw[name+'_score_mask']]
        field = RingField(raw[name+'_A'], row['sigma'], raw[name+'_gas_masses'],
                          STELLAR_U*raw[name+'_disk_masses'], row['h'], args.hankel)
        reference = (raw[name+'_gas'][0]+STELLAR_U*raw[name+'_disk'][0])[raw[name+'_score_mask']]/radii
    rmax_source = max(row['meta'].get('RHI', 0), float(np.max(radii)))
    # Preserve the protocol's boundary scale Rmax, not the HI metadata radius.
    rmax_source = float(np.max(radii))
    values = project(field, radii, row['sigma']/args.inner, args.outer*rmax_source,
                     A0_SI/ACC, nr=args.nr, nc=args.nc, lmax=args.lmax, newtonian=args.newtonian)
    result = {'name': name, 'source_row': row, 'U': STELLAR_U, 'a0_SI': A0_SI,
              'hankel': args.hankel, 'source_npz_sha256': sha(DATA/'baryonic_forward_64.npz'),
              'newtonian_midplane_relative_error': float(np.max(np.abs(values['newtonian']/reference-1))),
              'full_over_algebraic': (values['full']/values['algebraic']).tolist(),
              'full_over_local_norm': (values['full']/values['local_norm']).tolist(),
              'projection': {k: v.tolist() if isinstance(v, np.ndarray) else v for k, v in values.items()},
              'target_usage': 'No observed velocities read or fitted by this calculation'}
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--controls', action='store_true')
    parser.add_argument('--name')
    parser.add_argument('--nr', type=int, default=384)
    parser.add_argument('--nc', type=int, default=64)
    parser.add_argument('--lmax', type=int, default=32)
    parser.add_argument('--hankel', type=int, default=1024)
    parser.add_argument('--inner', type=float, default=16.)
    parser.add_argument('--outer', type=float, default=8.)
    parser.add_argument('--newtonian', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    guard()
    if args.output.exists():
        raise RuntimeError('Refusing to overwrite a scientific execution receipt')
    started = time.time()
    result = controls() if args.controls else galaxy(args.name, args)
    result.update(source_sha256=sha(__file__), at=dt.datetime.now(dt.timezone.utc).isoformat(),
                  elapsed_seconds=time.time()-started, author='this user chat, direct calculation')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    summary = {k: v for k, v in result.items() if k not in ('projection', 'source_row')}
    print(json.dumps(summary, indent=2))
    if args.controls and not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
