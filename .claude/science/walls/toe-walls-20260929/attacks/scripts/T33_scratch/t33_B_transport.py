import numpy as np, sys
sys.path.insert(0, '.')
from rge import *
L = 38.4422   # ln(M_Pl/v) from the lane's hierarchy map (G_2_V note, X6/X7)
o1 = observables(up_from_mz(V, 2))
obs = dict(g3=np.sqrt(o1['g32']), g2=np.sqrt(o1['g22']), gY=np.sqrt(o1['gp2']))
print("observed (SM-run from M_Z, 2-loop) at v: g3=%.4f g2=%.4f g'=%.4f" % (obs['g3'], obs['g2'], obs['gY']))
u0_su3 = 0.5934**0.25
u0_su2 = {'single-plaquette 0.9761 (lane X1)': 0.976111254449673, 'weak comparator 0.988': 0.988}
b = dict(g3=-7.0, g2=-19/6, gY=41/6)   # 1-loop SM in the (sign: dg/dt = b g^3/16pi^2) convention, g' with Y/2: b_Y = 41/6
lane = dict(g3=1.0, g2=0.25, gY=0.2)
def rmap(g2bare, u0):  # CMT: alpha_v = alpha_bare/u0^2, no running
    return np.sqrt(g2bare/u0**2)
def rrun(g2bare, u0, bi):  # tadpole-improved bare at M_Pl, then 1-loop over L
    inv = (4*PI/g2bare)*u0**2 + (bi/(2*PI))*L   # 1/alpha(v) = 1/alpha(Mpl) + (b/2pi) L  with b<0 asymptotically free
    return np.sqrt(4*PI/inv) if inv > 0 else float('nan')
rows = []
print("\nfactor  rule    u0       g(v) pred   obs     err")
def show(f, rule, u0, val):
    err = (val/obs[f]-1)*100 if val == val else float('nan')
    print(f"{f:5s}  {rule:6s}  {u0:.4f}   {val:8.4f}  {obs[f]:.4f}  {err:+7.1f}%" if val == val else f"{f:5s}  {rule:6s}  {u0:.4f}   Landau pole (1/alpha(v) <= 0)")
    rows.append((f, rule, u0, val, err))
show('g3', 'R-map', u0_su3, rmap(lane['g3'], u0_su3))
show('g3', 'R-run', u0_su3, rrun(lane['g3'], u0_su3, b['g3']))
for name, u0 in u0_su2.items():
    show('g2', 'R-map', u0, rmap(lane['g2'], u0))
    show('g2', 'R-run', u0, rrun(lane['g2'], u0, b['g2']))
show('gY', 'R-map', 1.0, rmap(lane['gY'], 1.0))
show('gY', 'R-run', 1.0, rrun(lane['gY'], 1.0, b['gY']))
print("\nPASS test: exists rule with all three within 10%?")
for rule in ('R-map', 'R-run'):
    for u0name in u0_su2:
        u2 = u0_su2[u0name]
        vals = []
        for f, u0 in (('g3', u0_su3), ('g2', u2), ('gY', 1.0)):
            if rule == 'R-map': v = rmap(lane[f], u0)
            else: v = rrun(lane[f], u0, b[f])
            vals.append((v/obs[f]-1)*100 if v == v else float('nan'))
        ok = all(abs(x) <= 10 for x in vals if x == x) and all(x == x for x in vals)
        print(f"  {rule} with SU(2) u0 = {u0name}: errors g3,g2,gY = {['%+.1f%%' % x for x in vals]} -> {'PASS' if ok else 'FAIL'}")
# mixed rule as the lane actually uses
print("\nLane's actual mixed usage: g3 via R-map, g2 via R-run, gY via R-run(u0=1):")
for name, u2 in u0_su2.items():
    e = [(rmap(1.0, u0_su3)/obs['g3']-1)*100, (rrun(.25, u2, b['g2'])/obs['g2']-1)*100, (rrun(.2, 1.0, b['gY'])/obs['gY']-1)*100]
    print("   SU(2) u0 =", name, "errors (%):", ["%+.1f" % x for x in e])
# what if SU(3) is treated by R-run with the SM-required g^2 = 0.2375 (weak lattice coupling)
print("\nUniversal reading: g^2 = 1/4 for all three, R-run, tadpole u0 = 1 (no improvement):")
for f in ('g3', 'g2', 'gY'):
    v = rrun(0.25, 1.0, b[f]); print(f"   {f}: g(v) = {v:.4f} vs obs {obs[f]:.4f}  ({(v/obs[f]-1)*100:+.1f}%)")
print("   and with lane tadpoles u0=(0.878, 0.988, 1):")
for f, u0 in (('g3', u0_su3), ('g2', 0.988), ('gY', 1.0)):
    v = rrun(0.25, u0, b[f]); print(f"   {f}: g(v) = {v:.4f} vs obs {obs[f]:.4f}  ({(v/obs[f]-1)*100:+.1f}%)")
# Sensitivity of the SU(2) 'hit' to the lane's own forking choices
print("\nSU(2) hit sensitivity (g2(v) with anchor 1/4; obs %.4f):" % obs['g2'])
for u0 in (0.9761, 0.988, 1.0):
    for pw in (0, 1, 2, 4):    # tadpole power on the bare (1/alpha ~ u0^pw)
        inv = (4*PI/0.25)*u0**pw + (b['g2']/(2*PI))*L
        print(f"   u0={u0:.4f} vertex power {pw}: g2(v) = {np.sqrt(4*PI/inv):.4f} ({(np.sqrt(4*PI/inv)/obs['g2']-1)*100:+.1f}%)")
for kk, K in (('kappa_EW=0 (K=9/8)', 9/8), ('kappa_EW=1/2', 18/17), ('kappa_EW=1', 1.0)):
    inv = (4*PI/0.25)*0.988**2 + (b['g2']/(2*PI))*L
    g = np.sqrt(4*PI/inv)*np.sqrt(K)
    print(f"   x sqrt(K_EW) {kk}: g2(v) = {g:.4f} ({(g/obs['g2']-1)*100:+.1f}%)")
