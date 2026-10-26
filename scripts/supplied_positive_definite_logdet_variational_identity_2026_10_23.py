#!/usr/bin/env python3
"""Finite controls for the supplied positive-cone identity; no selector inference."""
from pathlib import Path
import json
import numpy as np

AUDIT_INPUT_PATHS = ('docs/SUPPLIED_POSITIVE_DEFINITE_LOGDET_VARIATIONAL_IDENTITY_NOTE_2026-10-23.md',)
TOL = 1e-12


def positive(a):
    a = np.asarray(a, dtype=complex)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or not a.shape[0]:
        raise ValueError('nonempty square matrix required')
    if not np.isfinite(a).all() or not np.allclose(a, a.conj().T, atol=1e-10, rtol=0):
        raise ValueError('finite Hermitian matrix required')
    if np.min(np.linalg.eigvalsh(a)) <= 0:
        raise ValueError('positive definite matrix required')
    return a


def logdet(a):
    return float(np.sum(np.log(np.linalg.eigvalsh(positive(a)))))


def objective(y, k):
    y = positive(y)
    k = np.asarray(k, dtype=complex)
    if k.shape != y.shape:
        raise ValueError('shape mismatch')
    a = positive(np.eye(len(y)) + k)
    return logdet(a) - float(np.trace(k @ y).real)


def value(y):
    y = positive(y)
    return float(np.trace(y).real) - logdet(y) - len(y)


def main():
    text = (Path(__file__).resolve().parents[1] / AUDIT_INPUT_PATHS[0]).read_text()
    checks = {'scope_document': 'Y is held fixed' in text and 'no physical generator' in text}
    fixtures = [np.array([[2.]]), np.diag([.5, 2., 3.]),
                np.array([[2., .3+.4j], [.3-.4j, 1.5]])]
    errors = []
    for i, y in enumerate(fixtures):
        k = np.linalg.inv(y) - np.eye(len(y))
        error = abs(objective(y, k) - value(y)); errors.append(error)
        checks[f'optimizer_{i}'] = error < TOL
        a = np.diag(np.arange(1, len(y)+1, dtype=float)) + .25*np.eye(len(y))
        w, u = np.linalg.eigh(y)
        root = (u * np.sqrt(w)) @ u.conj().T
        z = root @ a @ root
        gap = value(y) - objective(y, a-np.eye(len(y)))
        checks[f'gap_{i}'] = abs(gap-value(z)) < TOL and gap > TOL
    checks['noncommuting_fixture'] = np.linalg.norm(fixtures[-1] @ np.diag([1.25,2.25])-np.diag([1.25,2.25]) @ fixtures[-1]) > .1
    seed = np.array([[2., .2j],[-.2j, 1.]])
    effective = fixtures[-1]
    w,u = np.linalg.eigh(seed); invroot = (u / np.sqrt(w)) @ u.conj().T
    y = invroot @ effective @ invroot
    product = np.linalg.solve(seed,effective)
    corollary = float(np.trace(product).real) - np.linalg.slogdet(product)[1] - 2
    checks['seed_corollary'] = abs(value(y)-corollary) < TOL
    bad = [np.diag([0.,1.]), np.diag([-1.,-1.]), np.array([[1.,1.],[0.,1.]])]
    for i,a in enumerate(bad):
        try:
            positive(a)
        except ValueError:
            checks[f'reject_Y_{i}'] = True
        else:
            checks[f'reject_Y_{i}'] = False
    try:
        objective(np.eye(2), -np.eye(2))
    except ValueError:
        checks['reject_infeasible_K'] = True
    else:
        checks['reject_infeasible_K'] = False
    checks['positive_det_not_positive'] = np.linalg.det(bad[1]) > 0 and np.linalg.eigvalsh(bad[1]).max() < 0
    t = np.array([1., 2., 4., 8.])
    checks['null_route_control'] = bool(np.all(np.diff(np.log(t)) > 0))
    checks['negative_route_control'] = bool(np.all(np.diff(np.log(t)+t-1) > 0))
    print(json.dumps({'checks':{k:bool(v) for k,v in checks.items()}, 'max_optimizer_error':max(errors),
                      'scope':'supplied matrices only; proof in note; boundary samples not asymptotic proof'}, indent=2))
    failed = sum(not v for v in checks.values())
    print(f'PASS={len(checks)-failed} FAIL={failed}')
    return int(bool(failed))

if __name__ == '__main__':
    raise SystemExit(main())
