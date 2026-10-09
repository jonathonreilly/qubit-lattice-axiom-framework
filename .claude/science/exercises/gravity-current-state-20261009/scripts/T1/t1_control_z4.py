"""T1 control: Euclidean hypercubic Z^4 (time on the lattice, a_t = a_s), Wilson fermion (r=1) + nn scalar,
Yukawa g phi psibar psi, twisted IR mass m on the fermion, mass m on the scalar.
Extract the O(p_mu) coefficient of i gamma_mu in Gamma_F and the O(p_mu^2) coefficient of Gamma_B
for mu = 0 (time) and mu = 1 (space) by symmetric finite differences; hypercubic symmetry forbids a split.
"""
import numpy as np
L, m, r, h = 32, 0.3, 1.0, 1e-3
q1 = 2 * np.pi * np.fft.fftfreq(L)
Q = np.meshgrid(q1, q1, q1, q1, indexing="ij")

def fermion_parts(Qs):
    s = [np.sin(x) for x in Qs]
    W = r * sum(1 - np.cos(x) for x in Qs)
    den = sum(x * x for x in s) + W * W + m * m
    return s, W, den

def Dbos(Qs):
    return 1.0 / (sum(4 * np.sin(x / 2) ** 2 for x in Qs) + m * m)

s, W, den = fermion_parts(Q)
res = {}
for mu in (0, 1):
    # fermion: Z_mu = 1 + d/dp_mu [ (1/L^4) sum_q s_mu(q)/den(q) D(p - q) ] at p = 0
    def sig(pm):
        Qp = [pm * h - Q[i] if i == mu else -Q[i] for i in range(4)]
        return (s[mu] / den * Dbos(Qp)).mean()
    Zf = (sig(+1) - sig(-1)) / (2 * h)
    # boson: Pi(p) = 4 (1/L^4) sum_q [W W' - m^2 - s.s'] / (den den'),  coefficient of p_mu^2 = 1/2 d^2 Pi
    def Pi(pm):
        Qp = [Q[i] + pm * h if i == mu else Q[i] for i in range(4)]
        sp, Wp, denp = fermion_parts(Qp)
        return 4 * ((W * Wp - m * m - sum(a * b for a, b in zip(s, sp))) / (den * denp)).mean()
    Zb = 0.5 * (Pi(+1) + Pi(-1) - 2 * Pi(0)) / h ** 2
    res[mu] = (Zf, Zb)
    print(f"mu={mu}: fermion dZ_mu = {Zf:+.12f}   boson dZ_mu = {Zb:+.12f}")
k = 16 * np.pi ** 2
dpsi = res[1][0] - res[0][0]; dphi = 0.5 * (res[1][1] - res[0][1])
print(f"Z^4 hypercubic control: 16pi^2 dc_psi = {k*dpsi:+.3e}, 16pi^2 dc_phi = {k*dphi:+.3e}, Delta = {k*(dpsi-dphi):+.3e}")
