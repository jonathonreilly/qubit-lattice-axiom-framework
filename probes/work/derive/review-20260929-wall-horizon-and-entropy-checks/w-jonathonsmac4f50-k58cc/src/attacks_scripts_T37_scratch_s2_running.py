"""S2: sector-blind bare r + SM one-loop running. Does the sector spread close anywhere in [m_t, M_Pl]?"""
from common import *
from scipy.integrate import solve_ivp
g = load_runner(); PARS, _RG = g["PARS"], g["_RG"]
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
MU0 = 162.5; V = 246.22
up = np.array([PARS['mu']*R.factor(2.0,MU0), PARS['mc']*R.factor(PARS['mc'],MU0), PARS['mt']*R.factor(PARS['mt'],MU0)])
dn = np.array([PARS['md']*R.factor(2.0,MU0), PARS['ms']*R.factor(2.0,MU0), PARS['mb']*R.factor(PARS['mb'],MU0)])
alpha = 1/127.9
Mp = M_LEP_POLE/1000.0
en = Mp*(1-(alpha/np.pi)*(1+0.75*np.log((MU0)**2/Mp**2)))   # GeV, MSbar at m_t
y0 = np.concatenate([np.sqrt(2)*up/V, np.sqrt(2)*dn/V, np.sqrt(2)*en/V, [0.4626, 0.6483, 1.1666]])
b = np.array([41/10, -19/6, -7.0]); p16 = 16*np.pi**2
def f(t, y):
    yu, yd, ye, gg = y[0:3], y[3:6], y[6:9], y[9:12]
    T = (3*yu**2 + 3*yd**2 + ye**2).sum()
    Gu = 17/20*gg[0]**2 + 9/4*gg[1]**2 + 8*gg[2]**2
    Gd = 1/4*gg[0]**2 + 9/4*gg[1]**2 + 8*gg[2]**2
    Ge = 9/4*gg[0]**2 + 9/4*gg[1]**2
    dyu = yu*(1.5*(yu**2 - yd**2) + T - Gu)/p16      # CKM = 1 pairing (u_i,d_i)
    dyd = yd*(1.5*(yd**2 - yu**2) + T - Gd)/p16
    dye = ye*(1.5*ye**2 + T - Ge)/p16
    dg = b*gg**3/p16
    return np.concatenate([dyu, dyd, dye, dg])
t0, t1 = np.log(MU0), np.log(1.22e19)
ts = np.linspace(t0, t1, 400)
sol = solve_ivp(f, (t0, t1), y0, t_eval=ts, rtol=1e-10, atol=1e-14, method="DOP853")
Y = sol.y
rr = np.array([[rf(Y[0:3,i]), rf(Y[3:6,i]), rf(Y[6:9,i])] for i in range(len(ts))])   # masses ∝ y, degree-0
spread = rr.max(1) - rr.min(1)
print("mu[GeV]      r_up     r_down   r_lep   spread   y_t   g3")
for mu in (162.5, 1e3, 1e4, 1e6, 1e9, 1e12, 2e16, 1.22e19):
    i = np.argmin(abs(ts-np.log(mu)))
    print("%9.3g  %8.5f %8.5f %8.5f %8.5f  %.3f  %.3f" % (np.exp(ts[i]), rr[i,0], rr[i,1], rr[i,2], spread[i], Y[2,i], Y[11,i]))
i = np.argmin(spread)
print("min spread %.5f at mu=%.3g GeV (IR spread %.5f)" % (spread[i], np.exp(ts[i]), spread[0]))
print("max drift of r_up: %.5f, r_down: %.5f, r_lep: %.5f (over the whole run)" % (np.ptp(rr[:,0]), np.ptp(rr[:,1]), np.ptp(rr[:,2])))
# also: GUT-scale masses for the Georgi-Jarlskog test (S4b): save
i = np.argmin(abs(ts-np.log(2e16)))
np.save("gut_masses.npy", np.array([Y[0:3,i], Y[3:6,i], Y[6:9,i]])*V/np.sqrt(2))
print("SM 1-loop GUT-scale (2e16) masses [GeV]:\n up", Y[0:3,i]*V/np.sqrt(2), "\n dn", Y[3:6,i]*V/np.sqrt(2), "\n lep", Y[6:9,i]*V/np.sqrt(2))
# sensitivity: what would the top-Yukawa-driven change of r_up need to be? r_up if m_t/m_c were reduced by factor s
