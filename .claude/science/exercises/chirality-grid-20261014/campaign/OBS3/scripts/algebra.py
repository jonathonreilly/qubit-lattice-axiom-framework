"""OBS-3 S2/S4 numbers: (1) Higgs on-site kernel vs flavon kernel (is K(c,c',a) independent of c'?);
(2) 3x3 complex Hadamard check (dephased form forces F); (3) CKM vs the circulant Latin-square pattern;
(4) bounds on column non-flatness in the up-flat class."""
import numpy as np, itertools
from obs3_core import *
P = print
np.set_printoptions(precision=5, linewidth=150)
for (m, D) in (('0.1', '0.5'), ('0.025', '0.5'), ('0.025', '0.0')):
    I, syms = load_kin(96, m, D, 'sym'); opt, cov = load_flav(96, m, D)
    P(f"(1) N=96 m0={m} Delta={D}: Higgs on-site I_00(e_x) per axis {I['x']['00']};  flavon K(x,y) (own, partner, third) {np.array(opt)}")
# (2) dephased 3x3 complex Hadamard: H = [[1,1,1],[1,a,b],[1,c,d]], |.|=1, H H^dag = 3: scan
best = 9
grid = np.exp(2j * np.pi * np.arange(360) / 360)
for a in grid:
    b = -1 - a                                       # row orthogonality to (1,1,1)
    if abs(abs(b) - 1) > 1e-9: continue
    P(f"(2) row 2 of a dephased Hadamard: a = exp(i {np.angle(a):+.4f}), b = exp(i {np.angle(b):+.4f})  (only +-2pi/3 solve 1+a+b=0 with |a|=|b|=1)")
# (3) circulant Latin-square test with PDG 2024 direct moduli (RECALLED) and the global fit
direct = np.array([[0.97367, 0.2243, 0.00382], [0.221, 0.975, 0.0411], [0.0086, 0.0415, 1.010]])
derr = np.array([[0.00032, 0.0008, 0.00020], [0.004, 0.006, 0.0012], [0.0002, 0.0009, 0.027]])
P("(3) a unitary equivalent (rephasing + row/column permutations) to a circulant has a Latin-square moduli matrix:")
P("    every row and every column holds the same multiset {|c0|,|c1|,|c2|}. Compare sorted rows/columns (direct PDG 2024 moduli):")
for lab, M, E in (('rows', direct, derr), ('cols', direct.T, derr.T)):
    srt = [sorted(zip(M[i], E[i])) for i in range(3)]
    for k, name in enumerate(('smallest', 'middle', 'largest')):
        vals = [srt[i][k] for i in range(3)]
        pulls = [abs(vals[i][0] - vals[j][0]) / np.hypot(vals[i][1], vals[j][1]) for i in range(3) for j in range(i + 1, 3)]
        P(f"    {lab} {name:8s}: " + ", ".join(f"{v[0]:.5f}({v[1]:.5f})" for v in vals) + f"   max pairwise pull {max(pulls):.1f} sigma")
AV = np.abs(INPUTS['pdg24']['V'])
P(f"    global-fit |V| (input) =\n{AV}")
# (4) up-flat: column non-flatness lower bounds  max_c ||W_d,ci|^2-1/3| >= (2/3)|A1| cos(pi/6),  |A1| >= p_max - (sum of the other two pair products)
for i, nm in enumerate(('d', 's', 'b')):
    z = AV[:, i]; prods = sorted([z[0] * z[1], z[1] * z[2], z[2] * z[0]])
    A1 = prods[2] - prods[1] - prods[0]
    P(f"(4) up-flat => |W_d,c{nm}|^2 deviation >= (2/3)(|V_u{nm}||...| pair bound {A1:.4f})(cos 30deg) = {2/3*A1*np.cos(np.pi/6):.4f}")
