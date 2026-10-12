"""R9-8 checks: (1) telescoping Ward identity sum_j dbar_j(p,k) = h_W(p) - h_W(k) for the rotated (non-separable) symbol;
(2) h_W has the same spectrum E(k) as h; (3) F->1 limit of the rotation code equals h; (4) h_W = E beta where F = 0;
(5) forward interband current outside the INV support vanishes; (6) radial/tangential forward-current ratios in the shell."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r98_frame_qed import LawW, dbar, comps_norm, dh, dot4
rng = np.random.default_rng(1)
law = LawW(2.0, 3.0, 1.0, 2.0, 3.0, 0.2, 1.0, 1.8)
K = rng.uniform(-np.pi, np.pi, (3, 20000)); px = 0.37
db, hk = dbar(law, px, K[0], K[1], K[2])
hp = law.hW(np.array(px), np.array(0.0), np.array(0.0))
res = max(np.max(np.abs(sum(db[j][c] for j in range(3)) - (hp[c] - hk[c]))) for c in range(4))
print(f"(1) telescoping WT residual max = {res:.2e}")
h0 = LawW(2.0, 3.0, 1.0, 2.0, 3.0, 0.2).hW(K[0], K[1], K[2]); hw = law.hW(K[0], K[1], K[2])
print(f"(2) |E_W - E| max = {np.max(np.abs(np.sqrt(dot4(hw,hw)) - np.sqrt(dot4(h0,h0)))):.2e}")
lawbig = LawW(2.0, 3.0, 1.0, 2.0, 3.0, 0.2, 100.0, 200.0); hb = lawbig.hW(K[0], K[1], K[2])
print(f"(3) F=1 via rotation code vs h: max diff = {max(np.max(np.abs(hb[c]-h0[c])) for c in range(4)):.2e}")
E = np.sqrt(dot4(h0, h0)); out = E >= 1.8
print(f"(4) where F=0 ({out.sum()} pts): max |alpha comps of h_W| = {max(np.max(np.abs(hw[c][out])) for c in range(3)):.2e}")
# (5) forward interband current |x|^2 - (x.n)^2 for x = d_y h_W, outside support
n, EW = comps_norm(hw); x = dh(law, K[0], K[1], K[2], 1)
inter = dot4(x, x) - dot4(x, n) ** 2
print(f"(5) forward interband |d_y h_W|_perp^2 where F=0: max = {np.max(inter[out]):.2e}; inside plateau (E<=1): vs BQ max diff "
      f"{np.max(np.abs(inter[E<=1.0] - (lambda x0,n0: dot4(x0,x0)-dot4(x0,n0)**2)(dh(LawW(2.0,3.0,1.0,2.0,3.0,0.2),K[0],K[1],K[2],1), comps_norm(h0)[0])[E<=1.0])):.2e}")
# (6) in the shell, ratio of forward interband current to BQ's, radial vs tangential direction (k along x-axis, current along x vs y)
kk = np.linspace(0.3, 1.95, 12)
lawQ = LawW(2.0, 3.0, 1.0, 2.0, 3.0, 0.2)
def inter_perp(L, kx, axis):
    h = L.hW(kx, 0 * kx, 0 * kx); n, _ = comps_norm(h); x = dh(L, kx, 0 * kx, 0 * kx, axis)
    return np.sqrt(np.maximum(dot4(x, x) - dot4(x, n) ** 2, 0))
rad = inter_perp(law, kk, 0) / inter_perp(lawQ, kk, 0); tan = inter_perp(law, kk, 1) / inter_perp(lawQ, kk, 1)
Ek = np.sqrt(0.04 + kk ** 2)
print("(6)  k     E     F(E)   radial ratio  tangential ratio")
for a, b, c, d in zip(kk, Ek, law.F(Ek), zip(rad, tan)):
    print(f"   {a:5.2f} {b:5.3f} {c:6.3f}   {d[0]:9.4f}    {d[1]:9.4f}")
