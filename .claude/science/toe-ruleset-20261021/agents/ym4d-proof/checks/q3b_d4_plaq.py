"""q3b: q3's level-0 plaquette sources (B), (C) in d = 4, k = 1, 2. Criteria: checks/q3b_criteria.md (written first).
The Chain class is read verbatim from checks/q3_src_decay.py (the part before 'def fmt')."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import time, resource
import numpy as np

AUDIT_TIMEOUT_SEC = 600
t0 = time.time()
src_text = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "q3_src_decay.py")).read()
ns = {}
exec(src_text.split("\ndef fmt")[0], ns)
Chain, L = ns["Chain"], ns["L"]


def plaq_source4(ch, kind):
    d, k = ch.d, ch.k; n = L ** k
    src = np.zeros(ch.nrows)
    ro, nr = ch.rowblocks[("p", 0, 1)]
    N = ch.Nf(0); psh = [N[a] - (1 if a in (0, 1) else 0) for a in range(d)]
    idx = np.indices(psh).reshape(d, -1).T.astype(float)
    cen = idx.copy(); cen[:, 0] += 0.5; cen[:, 1] += 0.5
    Xs = np.array([n / 2, n / 2, (n - 1) / 2, (n - 1) / 2])
    y = cen - Xs
    Y = y[:, 2] ** 2 + y[:, 3] ** 2 - y[:, 0] ** 2 - y[:, 1] ** 2
    if kind == "B4":
        vals = np.sign(Y) * L ** (-2 * k); sigma = 1.0
    else:
        vals = Y / n ** 2 * L ** (-2 * k); sigma = np.max(np.abs(vals)) * L ** (2 * k)
    src[ro:ro + nr] = vals
    return src, sigma


res = {}; allconv = True
for k in (1, 2):
    ch = Chain(4, k)
    print(f"=== d=4 k={k} nfree={ch.nfree} rows={ch.nrows}  (t={time.time() - t0:.1f}s)", flush=True)
    for kind in ("B4", "C4"):
        s, sig = plaq_source4(ch, kind)
        r = ch.solve(s); allconv &= r["conv"]
        for key in ("Nall", "N0", "ctr"):
            r[key] /= sig
        res[(kind, k)] = r
        print(f"  {kind} (sigma={sig:.4f}): conv={r['conv']} relgrad={r['g']:.1e} it={r['it']} Nall={r['Nall']:.4f} "
              f"N0={r['N0']:.4f} Rctr={r['ctr']:.4f} E={r['E']:.4e}\n      curv*L^2(k-i) (unnormalised): " +
              " ".join(f"{v:.3f}" for v in r["pc"]) + " | res: " + " ".join(f"{v:.3f}" for v in r["pr"]), flush=True)
    del ch
RB = res[("B4", 2)]["ctr"] >= 1.10 * res[("B4", 1)]["ctr"] and res[("B4", 2)]["ctr"] - res[("B4", 1)]["ctr"] >= 0.05
RC = res[("C4", 2)]["N0"] <= 1.10 * res[("C4", 1)]["N0"] + 0.05
print("SUMMARY B4 Rctr " + " ".join(f"{res[('B4', k)]['ctr']:.4f}" for k in (1, 2)) + " N0 " +
      " ".join(f"{res[('B4', k)]['N0']:.4f}" for k in (1, 2)) + " | C4 N0 " +
      " ".join(f"{res[('C4', k)]['N0']:.4f}" for k in (1, 2)) + " Rctr " +
      " ".join(f"{res[('C4', k)]['ctr']:.4f}" for k in (1, 2)))
print(f"R1 {'PASS' if allconv else 'FAIL'}  RB {'PASS' if RB else 'FAIL'}  RC {'PASS' if RC else 'FAIL'}")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"OVERALL: {'PASS' if (allconv and RB and RC) else 'FAIL'}   (wall {time.time() - t0:.1f} s, peak RSS {rss:.0f} MB)")
