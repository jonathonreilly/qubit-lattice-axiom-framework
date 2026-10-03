"""A46 vmc_ring: dual-frame VMC of the projected pi-flux singlet (m = 0; the Klein image of the soldered
state) and the AF family (pi-flux + staggered field m), measuring e_J' = <s.s>, e_K' = <s^a s^a> per
bond, ring = <P + P^-1> per face, and the staggered moment.  Usage: vmc_ring.py CLUSTER NSWEEP m1,m2,..
CLUSTER = L (cube, APBC in the soldered frame) or fcc16 (validation against ed16_ring.py)."""
import sys, signal, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a46lib import *
cname, nsw = sys.argv[1], int(sys.argv[2]); ms = [float(v) for v in sys.argv[3].split(",")]
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]) if cname == "fcc16" else cube(int(cname))
plaq = plaquettes(cl); budget = 265. / len(ms)
print(f"cluster {cname}: N={cl.N}, faces {len(plaq)}; m values {ms}; budget/state {budget:.0f}s", flush=True)
for m in ms:
    Phi, gap = mf_dual(cl, 0., 1., m=m)
    S, info = vmc_dual(cl, Phi, nsw, max(40, nsw // 10), 4600 + int(100 * m), budget * 0.9, plaq=plaq, conserve=True)
    out = []
    for k, nm in enumerate(["e_J'", "e_K'", "ring", "m_stag"]):
        mu, er = binerr(S[:, k].real); n = len(S)
        out.append(f"{nm} = {mu:+.5f} +- {er:.5f} (halves {S[:n//2, k].real.mean():+.4f}/{S[n//2:, k].real.mean():+.4f})")
    print(f"m={m}: MF gap {gap:.3f}; sweeps {len(S)} in {info['secs']:.0f}s; exch acc {info['acc'][2]}/{info['acc'][3]}; drift {info['drift']:.1e}; |Im ring| {abs(S[:, 2].imag.mean()):.1e}")
    for o in out: print("   " + o, flush=True)
    np.save(f"vmcr_{cname}_m{m}.npy", S)
