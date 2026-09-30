"""SM gauge RGEs (2-loop gauge, 1-loop y_t) in GUT normalisation g1^2 = (5/3) g'^2. Same-family check code (Sonnet 5.5)."""
import numpy as np
from scipy.integrate import solve_ivp

PI = np.pi
MZ = 91.1876
MPL = 1.2209e19
V = 246.28
AEM_INV_MZ = 127.951
S2W_MZ = 0.23122
AS_MZ = 0.1179
YT_MZ = 0.98          # MS-bar y_t at M_Z (1-loop-run from m_t(m_t)=163); effect on gauge running is 2-loop and tiny

B1 = np.array([41/10, -19/6, -7.0])
BB = np.array([[199/50, 27/10, 44/5],
               [9/10, 35/6, 12.0],
               [11/10, 9/2, -26.0]])
DT = np.array([17/10, 3/2, 2.0])

def rhs(t, y, loops):
    g = y[:3]; yt = y[3]
    k = 1/(16*PI**2)
    dg = np.empty(3)
    for i in range(3):
        two = 0.0
        if loops >= 2:
            two = k*(sum(BB[i, j]*g[j]**2 for j in range(3)) - DT[i]*yt**2)
        dg[i] = k*g[i]**3*(B1[i] + two)
    dyt = k*yt*(4.5*yt**2 - 17/20*g[0]**2 - 9/4*g[1]**2 - 8*g[2]**2)
    return np.array([*dg, dyt])

def run(y0, mu0, mu1, loops=2):
    sol = solve_ivp(rhs, [np.log(mu0), np.log(mu1)], y0, args=(loops,), rtol=1e-10, atol=1e-12, method='DOP853')
    return sol.y[:, -1]

def mz_inputs():
    a = 1/AEM_INV_MZ
    e2 = 4*PI*a
    g2 = np.sqrt(e2/S2W_MZ)                # g2^2 = e^2/s^2
    gp2 = e2/(1-S2W_MZ)                    # g'^2 = e^2/c^2
    g1 = np.sqrt(5/3*gp2)
    g3 = np.sqrt(4*PI*AS_MZ)
    return np.array([g1, g2, g3, YT_MZ])

def observables(y):
    """from (g1,g2,g3,yt) return dict: g'^2, g2^2, g3^2, sin^2, 1/alpha_em"""
    g1, g2, g3, _ = y
    gp2 = 3/5*g1**2
    g22 = g2**2
    e2 = g22*gp2/(g22+gp2)
    return dict(gp2=gp2, g22=g22, g32=g3**2, s2=gp2/(g22+gp2), aem_inv=4*PI/e2)

def up_from_mz(mu, loops=2):
    return run(mz_inputs(), MZ, mu, loops)

def down_from_mpl(gp2, g22, up_mpl, mu=MZ, loops=2):
    """start at M_Pl with candidate (g'^2, g2^2); g3 and y_t taken from the SM upward run"""
    y0 = np.array([np.sqrt(5/3*gp2), np.sqrt(g22), up_mpl[2], up_mpl[3]])
    return run(y0, MPL, mu, loops)
