"""QMC-1b gates (i) and (ii-a) (deterministic; PREREG section 4).
 (i)    W = 0: engine G(tau, k) vs analytic free G at every k and tau (f2 L4, fG L4, fG L6); light corners = 1/2.
 (ii-a) fG 2D L4, beta = 1, W = 4: phase of det(1 + M) on random prior-scale fields; T2 B T2^-1 = B; slice spectrum
        closed under conjugation.  Also: filter symbols equal their analytic formulas at every lattice momentum."""
import sys, os, time, resource
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice, AFQMC
KAP10 = {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}
t0 = time.time(); fm = FlavourModel("spin10"); allok = True
an = {"f2": lambda k: (1 + np.cos(k[0]) * np.cos(k[1])) / 2, "fG": lambda k: (2 - np.cos(k[0]) - np.cos(k[1])) / 4,
      "g1": lambda k: (1 - np.cos(k[0])) / 2, "f1": lambda k: (1 + np.cos(k[0])) / 2}
for dims, filt in (((4, 4), "f2"), ((4, 4), "fG"), ((6, 6), "fG"), ((3,), "g1"), ((3,), "f1")):
    lat = Lattice(dims, filt)
    d = max(abs(lat.fk[i] - an[filt](k)) for i, k in enumerate(lat.kvecs))
    mir, lig = lat.corners()
    print(f"filter {filt} L={dims}: rho = {lat.rho}; max |f(k) - analytic| = {d:.1e}; f at mirrors "
          f"{[round(an[filt](k), 3) for k in mir]}, at light {[round(an[filt](k), 3) for k in lig]}", flush=True)
    allok &= d < 1e-14
for dims, filt in (((4, 4), "f2"), ((4, 4), "fG"), ((6, 6), "fG")):
    lat = Lattice(dims, filt)
    sim = AFQMC(fm, KAP10, lat, W=0.0, beta=4.0, dtau=0.05, n_s=8, seed=3)
    worst, lw = [0.0], [0.0]
    mir, lig = lat.corners()
    def meas(n, G, Gt, s):
        tau = n * s.n_s * s.dtau
        N, D = s.N, s.D
        Gt4 = Gt.reshape(N, D, N, D)
        for ik, k in enumerate(lat.kvecs):
            v = np.exp(1j * lat.coords @ k) / np.sqrt(N)
            Gk = np.einsum("x,xiyj,y->ij", v.conj(), Gt4, v)
            ev, V = np.linalg.eigh(s.Kk[ik])
            ex = (V * (np.exp(-tau * ev) / (1 + np.exp(-s.beta * ev)))[None, :]) @ V.conj().T
            worst[0] = max(worst[0], np.abs(Gk - ex).max())
            if any(np.allclose(k, np.array(q)) for q in lig):
                lw[0] = max(lw[0], np.abs(Gk - 0.5 * np.eye(D)).max())
    sim.sweep(measure=meas, update=False)
    p = worst[0] <= 1e-10 and lw[0] <= 1e-8
    allok &= p
    print(f"gate(i) {filt} L={dims}: max |G_engine(tau,k) - G_free(tau,k)| = {worst[0]:.2e}; light-corner dev "
          f"{lw[0]:.1e}; wrap-vs-fresh {sim.maxdev:.1e}; PASS {p}", flush=True)
lat = Lattice((4, 4), "fG")
sim = AFQMC(fm, KAP10, lat, W=4.0, beta=1.0, dtau=0.1, n_s=2, seed=5)
phs = []
for trial in range(2):
    sim.phi = sim.rng.normal(size=sim.phi.shape)
    for l in range(sim.Lt):
        for x in range(sim.N):
            sim.core[l, x], sim.icore[l, x] = sim.vertex_core(l, sim.phi[l, x])
    lwt = sim.log_weight(); ph = abs(np.angle(np.exp(1j * lwt.imag))); phs.append(ph)
    B = sim.apply_B(0, np.eye(sim.Nd, dtype=complex))
    ev = np.linalg.eigvals(B)
    dev = max(np.min(np.abs(ev - z)) for z in ev.conj()) / np.abs(ev).max()
    Th = np.kron(np.eye(sim.N), fm.T2())
    comm = np.abs(Th @ B.conj() @ np.linalg.inv(Th) - B).max() / np.abs(B).max()
    print(f"gate(ii-a) fG L4 trial {trial}: log|w| = {lwt.real:.3f}, |phase| = {ph:.2e}; conj-closed spectrum dev "
          f"{dev:.1e}; ||T2 B T2^-1 - B||/||B|| = {comm:.1e}", flush=True)
    allok &= ph <= 1e-8 and comm <= 1e-12
print(f"GATES (i)+(ii-a) {'PASS' if allok else 'FAIL'}; total {time.time() - t0:.0f}s, peak RSS "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
