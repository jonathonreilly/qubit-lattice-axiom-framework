"""A27 check 4: time doublers under a smooth change sampled at ticks.

Records read the change only at ticks, so what matters is U(tau) = exp(-i tau H(k)).
1D: where the second species sits.
   stepped Dirac (A5):   cos w = cos m cos k   -> partner at (k, w) = (pi, pi)  [time doubler]
   smooth naive H = sin k sz + m sx, sampled  -> partner at (k, w) = (pi, 0)   [space doubler]
3D: covariant H_W = sum_a sin k_a sigma_a (A1 D21).  U(tau) has a degeneracy at quasi-energy pi
   iff |d(k)| tau = pi somewhere, i.e. iff tau*sqrt(3) >= pi (aliasing); below that the only
   touchings are H_W's eight nodes at quasi-energy 0, whose chiralities sum to zero.
Chirality via the coordinator's independent tool (toys/weyl_walk_tool.py, FHS link variables).
"""
import signal, sys, itertools
import numpy as np
signal.alarm(55)
sys.path.insert(0, "/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/toys")
from weyl_walk_tool import chirality, winding, sx, sy, sz, s0

ks = np.linspace(-np.pi, np.pi, 2001)
for m in [0.0, 0.3]:
    w_step = np.arccos(np.cos(m)*np.cos(ks))                 # stepped Dirac, upper band in [0, pi]
    gap0 = 2*w_step.min(); gappi = 2*(np.pi - w_step.max())
    k_at_pi = ks[np.argmax(w_step)]
    E = np.sqrt(np.sin(ks)**2 + m**2)                          # smooth naive lattice Dirac
    tau = 1.0
    # minima of the stroboscopic gap 2*E*tau: positions
    loc = ks[np.where(np.isclose(E, E.min(), atol=1e-9))]
    print(f"1D m={m}: stepped -> gap at w=0 {gap0:.3f} (k=0), gap at w=pi {gappi:.3f} (k={k_at_pi/np.pi:+.2f} pi); "
          f"smooth -> gap minima 2E*tau={2*E.min()*tau:.3f} at k/pi = {np.round(loc/np.pi, 3)} (both at quasi-energy 0)")

def d_of(k):
    return np.sin(k)

def U_of(tau):
    def Uf(k):
        d = d_of(k); nd = np.linalg.norm(d)
        if nd < 1e-15:
            return s0.copy()
        return np.cos(nd*tau)*s0 - 1j*np.sin(nd*tau)*(d[0]*sx + d[1]*sy + d[2]*sz)/nd
    return Uf

n = 40
grid = np.arange(n)*2*np.pi/n
dn = np.array([[[np.linalg.norm(np.sin([a, b, c])) for c in grid] for b in grid] for a in grid])
trim = [np.array(v)*np.pi for v in itertools.product([0, 1], repeat=3)]
for tau in [1.0, 2.0]:
    dist_pi = np.abs(np.pi - np.mod(dn*tau, 2*np.pi))
    frac_near = (dist_pi < 0.05).mean()
    print(f"\n3D H_W, tau={tau}: max |d| tau = {np.sqrt(3)*tau:.3f} (pi = {np.pi:.3f}); "
          f"min distance of eigenphase from pi on 40^3 grid = {dist_pi.min():.3f}; grid fraction within 0.05 of pi = {frac_near:.4f}")
    Uf = U_of(tau)
    chs = []
    for k0 in trim:
        ch, Es = chirality(Uf, k0 + 1e-9)
        chs.append(ch)
    print(f"   chiralities at the 8 TRIM (quasi-energy 0): {np.round(chs, 3)}; net {sum(chs):+.3f}")
    if tau == 1.0:
        W = winding(Uf, n=20)
        print(f"   W3 (grid 20^3) = {W.real:+.4f}")
