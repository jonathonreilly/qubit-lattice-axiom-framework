"""NT-1'' B2c (PREREG section 4, descriptive, different geometry): Weyl-bundle Chern numbers over the toron torus of a periodic
Lx x Lt lattice (fermions antiperiodic in both directions), zero plaquettes, torons on the wrap links (Luscher U[w], eq. 7.5).
Fukui-Hatsugai-Suzuki lattice field strength. usage: python3 nt1pp_b2c.py Lx Lt ngrid"""
import sys
import numpy as np
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
Lx, Lt, ng = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); N = 2 * Lx * Lt; n = N // 2
g5 = np.tile([1., -1.], N // 2)


def H(wx, wt):
    D = 2.0 * np.eye(N, dtype=complex)
    for t in range(Lt):
        for x in range(Lx):
            a = 2 * (t * Lx + x)
            for (g, x1, t1, u) in ((s1, (x + 1) % Lx, t, (-np.exp(1j * wx)) if x == Lx - 1 else 1.0),
                                   (s2, x, (t + 1) % Lt, (-np.exp(1j * wt)) if t == Lt - 1 else 1.0)):
                b = 2 * (t1 * Lx + x1)
                D[a:a + 2, b:b + 2] += -0.5 * (I2 - g) * u; D[b:b + 2, a:a + 2] += -0.5 * (I2 + g) * np.conj(u)
    return g5[:, None] * (D - np.eye(N))


ws = 2 * np.pi * np.arange(ng) / ng
res = {}
for e in (1, 2):
    VL = np.zeros((ng, ng, N, n), complex); VR = np.zeros((ng, ng, N, n), complex); gmin = np.inf
    for i in range(ng):
        for j in range(ng):
            w, V = np.linalg.eigh(H(e * ws[i], e * ws[j])); gmin = min(gmin, np.abs(w).min())
            assert (w > 0).sum() == n
            VL[i, j] = V[:, n:]; VR[i, j] = V[:, :n]
    for lab, V in (('L', VL), ('R', VR)):
        def link(a, b):
            d = np.linalg.det(np.conj(a.T) @ b); return d / abs(d)
        U1 = np.array([[link(V[i, j], V[(i + 1) % ng, j]) for j in range(ng)] for i in range(ng)])
        U2 = np.array([[link(V[i, j], V[i, (j + 1) % ng]) for j in range(ng)] for i in range(ng)])
        F = np.angle(U1 * np.roll(U2, -1, 0) * np.conj(np.roll(U1, -1, 1)) * np.conj(U2))
        C = F.sum() / (2 * np.pi)
        phi = np.angle(np.prod(U1, 0))          # Berry phase around the non-contractible w_x loop, as a function of w_t
        res[(lab, e)] = (C, phi, np.abs(F).max())
        print(f"charge {e} {lab}-Weyl bundle: Chern number {C:+.6f} (max |F_plaq| {np.abs(F).max():.3f}); min gap over grid {gmin:.3f}", flush=True)
C11112 = 4 * res[('L', 1)][0] + res[('R', 2)][0]; CL1 = res[('L', 1)][0]
def wind(ph): d = np.angle(np.exp(1j * (np.roll(ph, -1) - ph))); return d.sum() / (2 * np.pi)
Phi = 4 * res[('L', 1)][1] + res[('R', 2)][1]; PhiL1 = res[('L', 1)][1]
print(f"C(11112) = 4 C_L(1) + C_R(2) = {C11112:+.6f};  C(L1) = C_L(1) = {CL1:+.6f}")
print(f"winding over w_t of the Berry phase around the non-contractible w_x loop: 11112 {wind(Phi):+.4f}, L1 {wind(PhiL1):+.4f}; "
      f"11112 phase spread over w_t {np.ptp(np.unwrap(Phi)):.3f} rad")
np.savez(f"b2c_Lx{Lx}_Lt{Lt}_g{ng}.npz", phi11112=Phi, phiL1=PhiL1, C=np.array([C11112, CL1]))
