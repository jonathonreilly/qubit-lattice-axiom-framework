"""GUIDE for row 1085: the top eigenvectors of P_0 M P_0 (n = 2) with layer-swap parity, centre parity (exact at beta_T = 0)
and l_i - l_0. Uses tplaq.py. Usage: NEIG=8 python3 sectors.py A D betaT"""
import os, sys
os.environ.setdefault('NEIG', '8')
import tplaq
A, D, bT = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
S = tplaq.setup(A, D)
for bM in (2.0, 3.0, 4.0, 6.0, 8.0, 8.5, 10.0, 12.0, 16.0):
    o = tplaq.run(S, 2, bM, bT)
    print(f"bM {bM} bT {bT}  l0 {o['l'][0]:.6f}")
    for i in range(1, int(os.environ['NEIG'])):
        print(f"   i {i} lam_i/lam_0 {o['lam'][i]/o['lam'][0]:.6f} swap {o['parity'][i]:+.2f} centre {o['cpar'][i]:+.3f} l_i-l_0 {o['l'][i]-o['l'][0]:+.6f}")
