"""R19-11 (a): quadrature check of the Dirac linear coefficients at the m->0+ root law: slope over [0, 1e-4] at GL(6,16) vs GL(4,10).
Axial rows from smud_lib.dirac (dfam + xiud); face rows from dface (off-axis)."""
import re
def rd(fn):
    D = {}
    for l in open(fn):
        m = re.match(r'm=(\S+)', l)
        if not m: continue
        ax, off = l.split('| off:')
        d = {k: float(v) for k, v in re.findall(r'(\w+) ([+-]\d\.\d+e[+-]\d+)', ax)}
        d.update({'off_' + k: float(v) for k, v in re.findall(r'(\w+) ([+-]\d\.\d+e[+-]\d+)', off)})
        D[float(m.group(1))] = d
    return D
A = rd('mscan_d_root0_GL6_16.out'); B = rd('mscan_d_root0_dense_GL4_10.out')
for k in ['T2g', 'Eg', 'muE', 'muT2', 'off_face1', 'off_face2']:
    s6 = (A[1e-4][k] - A[0][k])/1e-4; s4 = (B[1e-4][k] - B[0][k])/1e-4
    print('%-9s slope[0,1e-4] GL(6,16) %+.6e  GL(4,10) %+.6e  rel diff %.1e | m=0: GL(6,16) %+.10e GL(4,10) %+.10e' % (k, s6, s4, abs(s6 - s4)/abs(s4), A[0][k], B[0][k]))
