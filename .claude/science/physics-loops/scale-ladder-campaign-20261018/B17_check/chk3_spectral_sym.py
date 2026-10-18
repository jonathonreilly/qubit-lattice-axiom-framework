"""B17 check, claim 2/3 side facts: spectral symmetries of the eight-node step that explain the second node set at -pi/2,
and the absence of a quasi-energy gap away from the node quasi-energies (relevant to a local Floquet Hamiltonian i log W)."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B17_check')
import steplib
d = steplib.build(); Ws = lambda k: np.sqrt(2) * d['Ws'](k)
rng = np.random.default_rng(3); ks = rng.uniform(-np.pi, np.pi, size=(200, 3))
srt = lambda e: np.sort(np.mod(e, 2 * np.pi))
def same(a, b): 
    a, b = srt(a), srt(b); return np.max(np.abs(np.exp(1j*a) - np.exp(1j*b))) < 1e-8
sh = all(same(np.angle(np.linalg.eigvals(Ws(k))), np.angle(np.linalg.eigvals(Ws(k))) + np.pi) for k in ks)
cj = all(same(np.angle(np.linalg.eigvals(Ws(k))), -np.angle(np.linalg.eigvals(Ws(k)))) for k in ks)
cjm = all(same(np.angle(np.linalg.eigvals(Ws(k))), -np.angle(np.linalg.eigvals(Ws(-k)))) for k in ks)
Q = np.pi * np.ones(3)
shQ = all(same(np.angle(np.linalg.eigvals(Ws(k + Q))), np.angle(np.linalg.eigvals(Ws(k))) + np.pi) for k in ks)
print("spec W(k) = spec(-W(k)) [theta -> theta+pi] at 200 random k:", sh)
print("spec W(k+pi(1,1,1)) = spec(-W(k)):", shQ)
print("spec W(k) = conj spec W(k) [theta -> -theta]:", cj, "; spec W(k) = conj spec W(-k):", cjm)
for n in (20, 32):
    grid = [np.array(t) * 2 * np.pi / n - np.pi + 0.037 for t in itertools.product(range(n), repeat=3)]
    ph = np.concatenate([np.angle(np.linalg.eigvals(Ws(g))) for g in grid])
    hist, edges = np.histogram(ph, bins=720, range=(-np.pi, np.pi))
    emp = edges[:-1][hist == 0]
    far = [e for e in emp if min(abs(e - np.pi / 2), abs(e + np.pi / 2)) > 0.1]
    print(f"{n}^3 grid: {len(emp)} of 720 half-degree bins empty, all within {np.max(np.minimum(abs(emp-np.pi/2),abs(emp+np.pi/2))) if len(emp) else 0:.3f} rad of +-pi/2; empty bins farther than 0.1 rad: {len(far)}")
