"""R18-10 s5: R18-1's pre-registered pinch diagnostic (s5b rho/xi^2, imported unchanged) plus S_gamma/q^2 and
S_gamma/q^4 at the smallest axis q (mean over the 3 axis copies, bin errors) and the Identity-V residual."""
import numpy as np, pickle, sys, os
sys.argv_saved = sys.argv; sys.argv = [sys.argv[0], "/dev/null"]
import importlib.util
spec = importlib.util.spec_from_file_location("s5b", os.path.join(os.path.dirname(os.path.abspath(__file__)), "s5b_pinch_table.py"))
src = open(spec.origin).read().split("files = sys.argv")[0]   # take only the definitions (comp, rho) from R18-1's s5b
ns = {}; exec(src, ns); rho = ns['rho']
sys.argv = sys.argv_saved
def sgam(res, m):
    kl = res['klist']; Gb = res['Gb']; L = res['L']; Mb = res['Mb']
    ii = [i for i, (n, mm, v) in enumerate(kl) if n == "axis" and mm == m]
    q2 = 4*np.sin(np.pi*m/L)**2
    arr = Gb[:, ii].mean(1)
    # Identity V residual: S_gamma(k e_j) = (q2/4) * sum of the three row-j slot diagonal entries
    res_v = 0.0
    for i in ii:
        j = int(np.argmax(np.abs(kl[i][2]))); sl = {0: [0, 3, 5], 1: [1, 3, 4], 2: [2, 4, 5]}[j]
        idv = (q2/4)*np.array([sum(np.real(Mb[b, i][s, s]) for s in sl) for b in range(Mb.shape[0])])
        res_v = max(res_v, abs(Gb[:, i].mean() - idv.mean()))
    return q2, arr.mean()/q2, arr.std()/np.sqrt(len(arr))/q2, arr.mean()/q2**2, res_v
rows = []
for f in sys.argv[1:]:
    res = pickle.load(open(f, "rb")); L = res['L']
    a = rho(res, 1); b = rho(res, 2); s = sgam(res, 1)
    rows.append((res['bU'], L, os.path.basename(f), res['Eb'].mean(), res['Eb'].std()/np.sqrt(len(res['Eb'])), a, b, s))
rows.sort(key=lambda r: (r[0], r[1], r[2]))
print("%-5s %-3s %-26s %-17s | rho(q1)          xi^2(q1)          | xi^2(q2)          | Sg/q^2(q1)       Sg/q^4  | S_T(q1) | xi/L  | idV-res" % ("bU", "L", "run", "E/edge"))
for bU, L, f, E, dE, a, b, s in rows:
    print("%-5.2f %-3d %-26s %.5f+-%.5f | %.4f+-%.4f  %7.3f+-%6.3f | %7.3f+-%6.3f | %.4f+-%.4f  %7.3f | %.3f   | %.3f | %.0e" %
          (bU, L, f, E, dE, a[1], a[2], a[3], a[4], b[3], b[4], s[1], s[2], s[3], a[5], np.sqrt(max(a[3], 0))/L, s[4]))
