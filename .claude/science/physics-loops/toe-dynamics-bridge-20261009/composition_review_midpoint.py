#!/usr/bin/env python3
"""Independent closed-form check of the author's midpoint interpolation test.

Grid character orthogonality removes cross modes. The midpoint average of a
cell phase is a finite geometric sum, not a numerical cell integration:
  average exp(i k y_mid) = sin(k ell/2)/(s sin(k ell/(2s))).
This verifies interpretation of a finite control, not a continuum theorem by
sampling. Uses no repository imports.
"""
from math import pi, prod, sin
from pathlib import Path
import re

ell = 2*pi/3
modes = ((1, 0, 0), (0, 1, -1), (-1, 1, 0))
weights = (1, 2, 1/9)
assert len({tuple(k % 3 for k in row) for row in modes}) == len(modes)


def phase_average(k, subdivisions=None):
    if k == 0:
        return 1.0
    theta = k*ell/2
    return sin(theta)/(theta if subdivisions is None else
                       subdivisions*sin(theta/subdivisions))


def error_integral(subdivisions=None):
    return sum(w*2*(1-prod(phase_average(k, subdivisions) for k in row))
               for row, w in zip(modes, weights))


limit = error_integral()
previous_error = None
print(f'Exact continuum phase integral (float evaluation): {limit:.15g}')
for subdivisions in (12, 24, 48):
    midpoint = error_integral(subdivisions)
    difference = limit-midpoint
    ratio = '' if previous_error is None else f'; previous/error={previous_error/difference:.9g}'
    print(f'Finite geometric-sum midpoint s={subdivisions}: {midpoint:.15g}; error={difference:.12g}{ratio}')
    assert 0 < difference < 1.37/subdivisions**2
    previous_error = difference

directory = Path(__file__).resolve().parent
author_log = (directory/'composition_review_author_runner.log').read_text()
match = re.search(r'midpoint integral=([0-9.]+), exact-phase formula=([0-9.]+)', author_log)
assert match is not None
reported_midpoint, reported_phase = map(float, match.groups())
assert abs(reported_midpoint-error_integral(12)) <= 5e-9
assert abs(reported_phase-limit) <= 5e-9
assert limit-error_integral(12) < 0.01
print('Author direct-space midpoint result matches the independent finite phase sum to printed precision.')
print('This finite float comparison is not a rigorous enclosure; the analytic interpolation proof is separate.')
