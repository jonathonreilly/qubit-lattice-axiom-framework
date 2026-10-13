"""Summarise Wilson-Dirac results: explicit-isometry BZ averages (upper bounds), quadrature check, lower bounds,
and threshold extrapolations (suggested)."""
import re, glob, numpy as np
thp = 3.779e-124; thr = 3.209e-63
def avg(f):
    for line in open(f):
        mm = re.search(r'BZ average dE\(R=(\d+)\) = ([0-9.e+-]+)', line)
        if mm: return int(mm.group(1)), float(mm.group(2))
for m in ('0', '1'):
    rows = sorted(avg(f) for f in glob.glob('r1913_dirac_m%s_R*.out' % m) if '_ng' not in f)
    print('Wilson-Dirac m=%s explicit isometry (8x8 graded GL grid): ' % m + '  '.join('R=%d:%.4e' % rv for rv in rows))
    for (r1, v1), (r2, v2) in zip(rows[1:], rows[2:]):
        print('   local exponent %d-%d: %.2f ; ratio %.1f' % (r1, r2, -np.log(v2 / v1) / np.log(r2 / r1), v1 / v2))
    for f in glob.glob('r1913_dirac_m%s_R*_ng12.out' % m):
        R, v = avg(f); v8 = dict(rows)[R]
        print('   quadrature check R=%d: 12x12 grid %.4e vs 8x8 %.4e (rel diff %.2f%%)' % (R, v, v8, 100 * (v8 - v) / v))
    if m == '0':
        R, v = rows[-1]; C = v * R ** 5
        print('   central (suggested, R^-5 from R=%d, C=%.3e): persistent R ~ %.2e a ; registered tau=R: R ~ %.2e a' % (R, C, (C / thp) ** 0.2, (C / thr) ** (1 / 6)))
    else:
        (ra, va), (rb, vb) = rows[-2], rows[-1]; rate = np.log(va / vb) / (rb - ra)
        print('   central (suggested, exponential rate %.2f per site from R=%d,%d): persistent R ~ %.0f a ; registered tau=R: R ~ %.0f a' % (rate, ra, rb, rb + np.log(vb / thp) / rate, rb + np.log(vb * rb / thr) / rate))
lb = dict((int(a), float(b)) for a, b in re.findall(r'R=(\d+)\s+LB=([0-9.e+-]+)', open('r1913_dirac_lb_big_m0.out').read()))
R0 = 256; C7 = lb[R0] * R0 ** 7
print('Dirac m=0 lower bound: LB(512) = %.3e > persistent thr %.2e and > registered thr/512 = %.2e -> required R > 512 a (proved inequality, numerically evaluated)' % (lb[512], thp, thr / 512))
print('   suggested extrapolation LB ~ %.2e R^-7 (local exponent -> 7): persistent R > %.2e a ; registered tau=R: R > %.2e a ; tau=1: R > %.2e a' % (C7, (C7 / thp) ** (1 / 7), (C7 / thr) ** (1 / 8), (C7 / thr) ** (1 / 7)))
lb1 = dict((int(a), float(b)) for a, b in re.findall(r'R=(\d+)\s+LB=([0-9.e+-]+)', open('r1913_dirac_lb_m1.out').read()))
print('Dirac m=1 lower bound: LB(16) = %.3e -> required R > 16 a (proved inequality, numerically evaluated); LB(32,64) are at the k-sum roundoff floor' % lb1[16])
