"""Synthetic physical-action control of CSS reduction; not an audit verdict.

The physical oracle enumerates Cartesian edges independently of the reducer's
geometry function. Only x is periodic in the 12-qubit test, avoiding the
length-two periodic multigraph convention. Both positive and mutated reduced
operators are compared through the full physical-space isometry.
"""
import itertools
import json
import numpy as np
from native_mode_compass_sector_basis import basis, dense_terms, isometry

AUDIT_TIMEOUT_SEC = 60


def main():
    shape = (3, 2, 2)
    sites = list(itertools.product(*(range(n) for n in shape)))
    index = {p: i for i, p in enumerate(sites)}
    physical_bonds = []
    for p, i in index.items():
        for axis, length in enumerate(shape):
            if p[axis] + 1 < length or axis == 0:
                q = list(p)
                q[axis] = (q[axis] + 1) % length
                physical_bonds.append((i, index[tuple(q)], axis))
    reports = []
    for zsign, xsign in [([0, 0], [0, 0]), ([1, 0], [0, 1])]:
        data = basis(shape, zsign=zsign, xsign=xsign)
        assert data['sites'] == sites
        terms = list(data['terms'])
        for p, i in index.items():
            if p[0] == shape[0] - 1:
                j = index[(0, p[1], p[2])]
                mask = (1 << i) | (1 << j)
                terms.append(data['reduce_term'](mask, 0, -1))
        U = isometry(data)
        rows = np.arange(1 << data['n'])
        HU = np.zeros_like(U)
        for i, j, axis in physical_bonds:
            mask = (1 << i) | (1 << j)
            parity = ((rows >> i) ^ (rows >> j)) & 1
            if axis == 0:
                target, amplitude = rows ^ mask, -np.ones(len(rows))
            elif axis == 1:
                target, amplitude = rows ^ mask, np.where(parity, -1., 1.)
            else:
                target, amplitude = rows, np.where(parity, 1., -1.)
            HU[target] += amplitude[:, None] * U

        def defect(candidate):
            reduced = dense_terms(candidate, data['dimension'])
            return float(np.max(np.abs(HU - U @ reduced)))

        isometry_error = float(np.max(np.abs(U.T @ U - np.eye(data['dimension']))))
        native_error = defect(terms)
        # Flip one actual YY coefficient, keeping every other matrix entry input.
        yy_index = next(k for k, (_, _, axis) in enumerate(data['bonds']) if axis == 1)
        bad_yy = list(terms)
        flip, phase, coefficient = bad_yy[yy_index]
        bad_yy[yy_index] = (flip, phase, -coefficient)
        bad_yy_error = defect(bad_yy)
        # The final term is one of the newly appended periodic x bonds.
        missing_wrap_error = defect(terms[:-1])
        assert isometry_error < 1e-13
        assert native_error < 1e-13
        assert bad_yy_error > 1e-3
        assert missing_wrap_error > 1e-3
        reports.append(dict(zsign=zsign, xsign=xsign,
                            dimension=data['dimension'],
                            isometry_error=isometry_error,
                            native_intertwining_error=native_error,
                            mutated_single_YY_sign_error=bad_yy_error,
                            omitted_single_wrap_error=missing_wrap_error))
    print(json.dumps(dict(inputs='pure synthetic', shape=shape,
                          periodic_axes=[0], physical_bonds=len(physical_bonds),
                          checks=reports,
                          scope='Physical-action implementation check, not a spectrum, finite-size, or audit verdict.'), indent=2))


if __name__ == '__main__':
    main()
