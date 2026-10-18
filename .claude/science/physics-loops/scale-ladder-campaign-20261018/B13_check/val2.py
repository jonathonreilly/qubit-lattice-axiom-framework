"""2^3 validation of chk.py: forward-walking slope and twisted mixed energies vs exact (own BFS ED)."""
import os, sys, time, json
os.environ.setdefault("NUMBA_NUM_THREADS", "2")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import chk
lat = chk.Lat((2, 2, 2)); s0 = chk.simple_ice(lat)
S, nf, mv = chk.component(lat, s0)
c = lat.harm(0)
Cm = np.array([lat.harm(0), lat.harm(1), lat.harm(2)])
out = {}
for V in (0.0, -0.5):
    Ee = lambda b: np.linalg.eigvals(chk.H_twist(len(S), nf, mv, V, b, c, imag=True)).real.min()
    E0 = Ee(0.0)
    ex = {eta: Ee(eta) for eta in (1.0, 2.0)}
    t0 = time.time()
    r = chk.run(lat, s0, V, N=2000, dt=0.1, ttherm=20, nblocks=40, block_t=20, ctw=c, eta=0.0, Cm=Cm, seed=7)
    tau = r["tau"]; sel = tau >= 8
    m2 = r["M2"].mean(0)
    slopes = [np.polyfit(tau[sel], m2[sel, s], 1)[0] for s in range(3)]
    jk = []
    for b in range(r["M2"].shape[0]):
        mm = np.delete(r["M2"], b, 0).mean(0)
        jk.append(np.mean([np.polyfit(tau[sel], mm[sel, s], 1)[0] for s in range(3)]))
    jk = np.array(jk); err = np.sqrt((len(jk) - 1) * jk.var())
    Em = np.nanmean(r["EM"])
    hd = (S[:, None, :] != 0)
    # exact chi by Hermitian FD
    Eh = lambda b: np.linalg.eigvalsh(chk.H_twist(len(S), nf, mv, V, b, c, imag=False))[0]
    chi_ex = (Eh(1e-3) + Eh(-1e-3) - 2 * Eh(0.0)) / 1e-6
    print(f"V={V}: exact E0={E0:.5f} chi={chi_ex:.5f} | DMC Emix={Em:.5f} FW chi={np.mean(slopes):.4f}+-{err:.4f} {np.round(slopes,4)} ({time.time()-t0:.0f}s)", flush=True)
    for eta in (1.0, 2.0):
        r2 = chk.run(lat, s0, V, N=2000, dt=0.1, ttherm=20, nblocks=40, block_t=10, ctw=c, eta=eta, Cm=Cm[:0], seed=9)
        e = r2["EM"][~np.isnan(r2["EM"])]
        bl = e.reshape(20, -1).mean(1)
        print(f"   eta={eta}: exact E(i eta)={ex[eta]:.5f} DMC={bl.mean():.5f}+-{bl.std(ddof=1)/np.sqrt(20):.5f}  growth={r2['ET'] - r2['LM'].mean()/0.1:.5f}", flush=True)
