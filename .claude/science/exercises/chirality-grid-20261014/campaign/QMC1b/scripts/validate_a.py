"""QMC-1 validation part A (deterministic checks; no sampling statistics):
 A1  gate (i): W = 0 engine G(tau, k) vs analytic free G, Spin(10), 1D L = 4 (f1) and 2D L = 4 (f2), all k and tau.
 A2  measurement code vs ED at W = 0 (reduced flavours, 1D L = 3, f1): <X_a X_a>, <Y_a Y_a>, kinetic energy.
 A3  Spin(10) weights on a small cluster (1D L = 4, f1, beta = 1, W = 4): phase of det(1 + M) for random fields;
     Kramers pairing of the eigenvalues of M = B(beta, 0); <Q> from Bh^a vs from the HS channels (Fierz, Wick).
"""
import sys, time, resource
import numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from x2model import FlavourModel
from afqmc import Lattice, AFQMC, Observables
import ed_exact

def P(*a):
    print(*a, flush=True)

def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20

KAP10 = {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}     # PREREG follow-up A
KAPRED = {"sing:1v": 1.0, "trip:1v": -1.0 / 3}                                   # PREREG section 4 (iii)
t0 = time.time()

# ---------------------------------------------------------------------------------------------------- A1
fm = FlavourModel("spin10")
for dims, filt in (((4,), "f1"), ((4, 4), "f2")):
    lat = Lattice(dims, filt)
    sim = AFQMC(fm, KAP10, lat, W=0.0, beta=2.0, dtau=0.1, n_s=4, seed=3)
    worst = [0.0]
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
        # off-diagonal momentum blocks must vanish: total weight check
        tot = sum(np.sum(np.abs(np.einsum("x,xiyj,y->ij", np.exp(-1j * lat.coords @ k) / np.sqrt(N), Gt4,
                                            np.exp(1j * lat.coords @ k) / np.sqrt(N))) ** 2) for k in lat.kvecs)
        worst[0] = max(worst[0], abs(tot - np.sum(np.abs(Gt) ** 2)))
    sim.sweep(measure=meas, update=False)
    P(f"A1 gate(i) Spin(10) {filt} L={dims}: max |G_engine(tau,k) - G_free(tau,k)| over all k, tau = {worst[0]:.2e} "
      f"(PASS if <= 1e-10: {worst[0] <= 1e-10}); wrap-vs-fresh {sim.maxdev:.1e}")

# ---------------------------------------------------------------------------------------------------- A2
fr = FlavourModel("reduced")
lat = Lattice((3,), "f1")
ops = ed_exact.build(fr, KAPRED, lat, W=0.0)
ed = ed_exact.thermal(ops, beta=2.0)
sim = AFQMC(fr, KAPRED, lat, W=0.0, beta=2.0, dtau=0.1, n_s=4, seed=4)
obs = Observables(sim)
got = {}
def meas2(n, G, Gt, s):
    if n == s.nst:
        got["SX"], got["SY"] = obs.structure(G)
        got["Ek"] = obs.kinetic(G).real
sim.sweep(measure=meas2, update=False)
P(f"A2 W=0 reduced 1D L=3: ED  N*S_X {np.round(ed['SX'], 10).tolist()}  N*S_Y {np.round(ed['SY'], 10).tolist()}  Ekin {ed['Ekin']:.10f}")
P(f"A2 W=0 reduced 1D L=3: QMC N*S_X {np.round(got['SX'] * lat.N, 10).tolist()}  N*S_Y {np.round(got['SY'] * lat.N, 10).tolist()}  Ekin {got['Ek']:.10f}")
d2 = max(np.abs(got["SX"] * lat.N - ed["SX"]).max(), np.abs(got["SY"] * lat.N - ed["SY"]).max(), abs(got["Ek"] - ed["Ekin"]))
P(f"A2 max deviation {d2:.2e} (PASS if <= 1e-10: {d2 <= 1e-10})")

# ---------------------------------------------------------------------------------------------------- A3
lat = Lattice((4,), "f1")
sim = AFQMC(fm, KAP10, lat, W=4.0, beta=1.0, dtau=0.1, n_s=2, seed=5)
phases, pairdev = [], []
for trial, scale in enumerate((1.0, 1.0, 2.0, 4.0)):
    sim.phi = sim.rng.normal(size=sim.phi.shape) * scale
    for l in range(sim.Lt):
        for x in range(sim.N):
            sim.core[l, x], sim.icore[l, x] = sim.vertex_core(l, sim.phi[l, x])
    lw = sim.log_weight()
    ph = abs(np.angle(np.exp(1j * lw.imag)))
    if scale == 1.0:
        phases.append(ph)
    # Kramers: the spectrum of each slice matrix B_l is closed under conjugation (well conditioned, unlike M)
    B = sim.apply_B(0, np.eye(sim.Nd, dtype=complex))
    ev = np.linalg.eigvals(B)
    dev = max(np.min(np.abs(ev - z)) for z in ev.conj()) / np.abs(ev).max()
    # Kramers degeneracy test on the slice: T2 B T2^-1 = B, T2 = (1_N x i sigma_y x 1) K
    Th = np.kron(np.eye(sim.N), fm.T2())
    comm = np.abs(Th @ B.conj() @ np.linalg.inv(Th) - B).max() / np.abs(B).max()
    P(f"A3 field scale {scale}: log|w| = {lw.real:.3f}, |phase| = {ph:.2e}; slice spectrum conj-closed deviation "
      f"{dev:.1e}; ||T2 B T2^-1 - B||/||B|| = {comm:.1e}")
P(f"A3 gate(ii) on prior-scale random fields: max |phase| = {max(phases):.2e} (<= 1e-8: {max(phases) <= 1e-8}); "
  f"scale 2 and 4 are stress tests outside the sampled regime (roundoff of the stabilised log det at log|w| ~ 1e3)")
obs = Observables(sim)
sim.build_left_stack()
G, _ = sim.green(sim.identity_udv(), sim.Lst[0])
qa, qb = obs.local_terms(G)
P(f"A3 Fierz in expectation (random-field Gaussian state): <sum Q> from Bh^a = {qa.real:.12f}{qa.imag:+.1e}j, "
  f"from HS channels = {qb.real:.12f}{qb.imag:+.1e}j, |diff| = {abs(qa - qb):.2e}")
P(f"total {time.time() - t0:.0f}s, peak RSS {rss():.0f} MB")
