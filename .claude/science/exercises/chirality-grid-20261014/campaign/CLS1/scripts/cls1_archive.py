"""CLS-1 archive: label table, loop coefficients (N=48, m=0.1), merged with the light/theta archives."""
import numpy as np, itertools, re, sys
sys.path.insert(0, '.')
from cls1_core import *
lab = np.array([[*v, (-1) ** sum(v), int(round(np.prod(np.cos(PI * np.array(v)))))] for v in itertools.product((0, 1), repeat=3)])
loop = []
for line in open('loop2.out'):
    m = re.search(r"y0=([-+0-9.]+) y1=([0-9.]+).*\|off coeffs\| \[([^\]]*)\]", line)
    if m: loop.append([float(m.group(1)), float(m.group(2))] + [float(x) for x in m.group(3).split()])
A = dict(np.load('cls1_light_archive.npz')); B = dict(np.load('cls1_theta_archive.npz'))
np.savez('cls1_archive.npz', labels_v_bccchar_chirality=lab, loop_offdiag_coeffs_y0_y1_c1_c2_c3=np.array(loop), **A, **B)
print("saved cls1_archive.npz with", ['labels_v_bccchar_chirality', 'loop_offdiag_coeffs_y0_y1_c1_c2_c3'] + list(A) + list(B))
print(np.array(loop))
