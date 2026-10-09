"""S2 (supervisor, E1'-b): overlap volume of two link 'needles' I(y,x), I(y',x) in M^{1,3}, vs transverse offset b.
Units l = 1 (rho = 1). x = origin. y at distance r along -e1, time -(r+delta); y' at distance r' along direction rotated by theta
toward e2, time -(r'+delta'). delta chosen so rho*V = m0 (V = pi tau^4/24, tau^2 = (r+delta)^2 - r^2).
Monte Carlo: sample uniformly in the apex piece of I(y,x) with |v| < vcut (light-cone coords along e1),
estimate the fraction inside I(y',x); overlap = (piece volume) * fraction. Also full-needle check at small b.
Prediction (supervisor): overlap ~ min(V, C (l/b)^4 l^4) with b = D*theta.
"""
import numpy as np
rng = np.random.default_rng(1)

def delta_for(r, m0):
    tau2 = np.sqrt(24*m0/np.pi)       # rho V = m0 -> tau^4 = 24 m0/pi
    return -r + np.sqrt(r*r + tau2)   # (r+delta)^2 - r^2 = tau2

def in_interval(z, ybot):
    # z: (n,4) [t,x1,x2,x3]; returns ybot < z (future timelike) and z < origin
    dt = z[:,0] - ybot[0]
    dx = z[:,1:] - ybot[1:]
    c1 = (dt > 0) & (dt*dt > (dx*dx).sum(1))
    c2 = (z[:,0] < 0) & (z[:,0]**2 > (z[:,1:]**2).sum(1))
    return c1 & c2

def sample_piece(r, delta, vcut, n):
    # light-cone coords along e1 pointing toward y: y spatial at -r e1.  define s = -x1 (distance toward y).
    # u = -t - s ... use: t = -(a+b)/2, s = (a-b)/2 ... simpler: sample t,s directly in bounding box then reject.
    # points of I(y,x) near apex: s in (0, vcut/2), t in (-(s+delta), -s), transverse |zeta|^2 < t^2 - s^2
    s = rng.uniform(0, vcut/2, n)
    t = -s - rng.uniform(0, delta, n)            # t in (-(s+delta), -s)
    rmax = np.sqrt(np.maximum(t*t - s*s, 0))
    # sample transverse uniformly in disk of radius Rb = max possible, then reject
    Rb = np.sqrt((vcut/2+delta)**2 - (vcut/2)**2)
    ang = rng.uniform(0, 2*np.pi, n); rad = Rb*np.sqrt(rng.uniform(0,1,n))
    z2, z3 = rad*np.cos(ang), rad*np.sin(ang)
    z = np.stack([t, -s, z2, z3], 1)
    box_vol = (vcut/2)*delta*np.pi*Rb**2
    return z, box_vol

def overlap(r, rp, m0, theta, vcut, n=2_000_000):
    d = delta_for(r, m0); dp = delta_for(rp, m0)
    y  = np.array([-(r+d), -r, 0.0, 0.0])
    yp = np.array([-(rp+dp), -rp*np.cos(theta), -rp*np.sin(theta), 0.0])
    z, box = sample_piece(r, d, vcut, n)
    iny = in_interval(z, y)
    inboth = iny & in_interval(z, yp)
    Vpiece = box*iny.mean()
    Vov = box*inboth.mean()
    return Vpiece, Vov, inboth.sum()

r = rp = 1000.0; m0 = 1.0
V = 1.0  # rho V = m0 = 1
print("needle at r = 1000 l, rho V = 1 (V = 1 l^4); delta =", delta_for(r, m0))
print(" b=r*theta   vcut     V_piece(|v|<vcut)   overlap     hits   overlap*b^4")
for b in [0.25, 0.5, 1, 2, 4, 8, 16, 32]:
    theta = b/r
    d = delta_for(r, m0)
    vstar = 4*(2*np.sqrt(d))**2/theta**2      # supervisor's bound on overlap depth |v|
    vcut = min(2*r, 2.5*vstar)
    Vp, Vo, hits = overlap(r, rp, m0, theta, vcut)
    print(f" {b:7.2f}  {vcut:9.2f}  {Vp:12.5f}  {Vo:12.4e}  {hits:7d}  {Vo*b**4:10.4f}")
