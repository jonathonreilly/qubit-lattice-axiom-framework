"""Conditional driven-circuit and reserved resonator comparison; no circuit-parameter refit."""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.linalg import eigh
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import least_squares, minimize_scalar
from driven_squid_independent_2026_09_27 import independent_cavity

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = [
    'scripts/driven_squid_independent_2026_09_27.py',
    'data/driven_squid_resonator_2026_09_27/inputs.json',
    'data/driven_squid_resonator_2026_09_27/measurements.json',
    'data/driven_squid_resonator_2026_09_27/provenance.json',
]
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/driven_squid_resonator_2026_09_27'


def system(c, flux, EL, N=40, L=24, K=7):
    n = np.arange(-N, N + 1)
    EC, J, asymmetry = c['params']
    left, right = J * (1 + asymmetry), J * (1 - asymmetry)
    t1 = -(left + right * np.exp(-2j * np.pi * flux)) / 2
    t2 = (left**2 + right**2 * np.exp(-4j * np.pi * flux)) / (8 * EL)
    H = np.diag(4 * EC * (n - c['ng'])**2).astype(complex)
    for order, coefficient in ((1, t1), (2, t2)):
        H += np.diag(np.full(len(n) - order, coefficient), order)
        H += np.diag(np.full(len(n) - order, coefficient.conjugate()), -order)
    ev, U = eigh(H, subset_by_index=[0, L - 1])
    ev -= ev[0]
    Q = U.conj().T @ (n[:, None] * U)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    charge = np.kron(Q, np.eye(K))
    X = np.kron(np.eye(L), a + a.T)
    P = np.kron(np.eye(L), 1j * (a.T - a))
    coupled = np.diag((ev[:, None] + c['Omega_GHz'] * np.arange(K)).ravel())
    coupled = coupled + c['G_GHz'] * charge @ P
    energies, V = eigh(coupled)
    labels = [int(np.argmax(abs(V[index])**2)) for index in (0, 1, K)]
    weights = [float(abs(V[index, label])**2) for index, label in zip((0, 1, K), labels)]
    if len(set(labels)) != 3:
        raise ValueError('Ground, cavity and device labels collided')
    return energies, V.conj().T @ charge @ V, V.conj().T @ X @ V, labels, weights


def cavity(c, flux, EL):
    E, _, _, labels, weights = system(c, flux, EL)
    return float(E[labels[1]] - E[labels[0]] - c['Omega_GHz']), min(weights[:2])


def extract(raw, shape):
    y = np.array(raw['frequency_offset_MHz']) / 1000
    rows = []
    for column in raw['columns']:
        v = np.array(column['signal'])
        guess = y[np.argmin(gaussian_filter1d(v, 1))]
        def residual(p):
            b, amplitude, center, width, slope = p
            q = (y - center) / width
            peak = 1 / (1 + q*q) if shape == 'lorentzian' else np.exp(-q*q / 2)
            return b - amplitude * peak + slope * (y - center) - v
        fit = least_squares(residual, [max(v), np.ptp(v), guess, .00008, 0],
            bounds=([-10, 0, min(y), .000005, -1e5], [10, 10, max(y), .001, 1e5]),
            x_scale='jac', max_nfev=300)
        if not fit.success or np.any(fit.active_mask):
            raise ValueError('Center extraction failed or reached a bound')
        rows.append(dict(column=column['column'], flux=column['flux'],
            center_GHz=float(fit.x[2]), width_GHz=float(fit.x[3])))
    return rows


def floquet(snapshot, inputs, mutation):
    EL = inputs['EL_GHz']
    E, _, X, labels, _ = system(snapshot, inputs['rabi_flux'], EL, 32, 14, 7)
    matrix = abs(X[labels[0], labels[2]])
    D = 10**(inputs['spectroscopy_dB'] / 20) / (inputs['pi_amplitude'] * inputs['pulse_ns'] * matrix)
    E, Q, _, labels, _ = system(snapshot, inputs['drive_flux'], EL, 32, 14, 7)
    ground, excited = labels[0], labels[2]
    base = E[excited] - E[ground]
    checks = []
    for levels, sidebands in ((40, 4), (70, 6)):
        energies = E[:levels] - E[ground]
        charge = Q[:levels, :levels]
        m = np.arange(-sidebands, sidebands + 1)
        T = np.diag(np.ones(2 * sidebands), 1)
        ig, ie = sidebands * levels + ground, (sidebands - 1) * levels + excited
        def gap(w):
            F = 2 * snapshot['G_GHz'] * D * w / (snapshot['Omega_GHz']**2 - w*w)
            if mutation == 'drive':
                F *= .5
            H = np.diag((energies[None, :] + m[:, None] * w).ravel()).astype(complex)
            H += np.kron(1j * (T - T.T), F * charge / 2)
            ev, V = eigh(H)
            projections = abs(V[ig])**2 + abs(V[ie])**2
            pair = np.sort(np.argsort(projections)[-2:])
            return ev[pair[1]] - ev[pair[0]]
        opt = minimize_scalar(gap, bounds=(base - .035, base + .035), method='bounded', options={'xatol': 1e-10})
        if not opt.success:
            raise ValueError('Local avoided-gap minimization failed')
        checks.append(dict(levels=levels, sidebands=sidebands, shift_MHz=float((opt.x - base) * 1000), gap_GHz=float(opt.fun)))
    # Independent continuous-time monodromy result, shared physical inputs;
    # this is a regression anchor, not an observed target or a new proof.
    if abs(checks[-1]['shift_MHz'] - 6.181682972797198) > .00002:
        raise ValueError('Displaced result disagrees with independent monodromy anchor')
    return dict(drive_GHz=float(D), rabi_matrix=float(matrix), checks=checks)


def run(mutation='none'):
    provenance = json.loads((DATA / 'provenance.json').read_text())
    for name, digest in provenance['packaged_inputs'].items():
        if hashlib.sha256((DATA / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Pinned scientific input drift')
    inputs = json.loads((DATA / 'inputs.json').read_text())
    raw = json.loads((DATA / 'measurements.json').read_text())
    if mutation == 'units':
        raw['frequency_offset_MHz'] = (np.array(raw['frequency_offset_MHz']) * 1000).tolist()
    reserved = {r['column'] for r in raw['columns']}
    calibration = set(inputs['calibration_columns'])
    if mutation == 'split':
        calibration.add(50)
    if reserved & calibration or reserved != set(range(10, 400, 20)):
        raise ValueError('Calibration and evaluation column split is invalid')
    observations = extract(raw, 'lorentzian')
    alternative = extract(raw, 'gaussian')
    shape_change = max(abs(a['center_GHz'] - b['center_GHz']) * 1e6 for a, b in zip(observations, alternative))
    if not all(-.0002 <= x['center_GHz'] <= .00088 for x in observations):
        raise ValueError('Measured centers outside published frequency-offset axis')
    nominal, aligned, independent_checks = [], [], []
    # Each snapshot is propagated; no selection by evaluation residual.
    for group, snapshots in ((nominal, inputs['driven_snapshots']), (aligned, inputs['alignment_snapshots'])):
        for original in snapshots:
            c = dict(original)
            if mutation == 'coupling':
                c['G_GHz'] *= 1.1
            points = []
            for obs in observations:
                shift, weight = cavity(c, obs['flux'] + c.get('flux_offset', 0), inputs['EL_GHz'])
                if group is aligned and obs['column'] == 250:
                    independent = independent_cavity(c, obs['flux'] + c['flux_offset'], inputs['EL_GHz'])
                    if mutation == 'independent':
                        independent += .000001
                    difference_Hz = (shift - independent) * 1e9
                    if abs(difference_Hz) > 1:
                        raise ValueError('Direct-basis independent comparison failed')
                    independent_checks.append(dict(ng=c['ng'], start_delta=c['start_delta'], difference_Hz=float(difference_Hz)))
                residual = (shift + c['offset_GHz'] - obs['center_GHz']) * 1e6
                points.append(dict(column=obs['column'], residual_kHz=float(residual), label_weight=weight))
            group.append(dict(ng=c['ng'], start_delta=c.get('start_delta'), flux_offset=c.get('flux_offset', 0),
                rms_kHz=float(np.sqrt(np.mean([p['residual_kHz']**2 for p in points]))), points=points))
    # Independent direct charge-photon diagonalization checked these four values.
    anchors = {(0, 50):108.148909, (0,250):114.806630, (.5,50):108.518610, (.5,250):120.440751}
    for row in nominal:
        for point in row['points']:
            key = (row['ng'], point['column'])
            if key in anchors and abs(point['residual_kHz'] - anchors[key]) > .001:
                raise ValueError('Cavity prediction differs from independent numerical anchor')
    result = dict(scope='Supplied imported-model snapshots; retrospective measured-column separation; no refit, confidence interval, native TOE claim or dissipative line-center prediction.',
        observations=observations, shape_center_max_change_kHz=shape_change,
        nominal=nominal, alignment_controls=aligned, independent_alignment_checks=independent_checks,
        driven=floquet(inputs['drive_reference'], inputs, mutation),
        input_reads='Scientific inputs: inputs.json and measurements.json. Integrity input: provenance.json and hashes of those scientific inputs. Independent numerical anchors are explicit regression references in source.')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutation', choices=['none', 'drive', 'coupling', 'split', 'units', 'independent'], default='none')
    args = parser.parse_args()
    print(json.dumps(run(args.mutation), indent=2))
