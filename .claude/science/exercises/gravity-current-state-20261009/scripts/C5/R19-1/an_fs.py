"""R19-1 analysis: per channel and direction, S, f, omega_SMA = f/S (per-bin ratio of copy-averages)."""
import numpy as np, pickle, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mc import channel_pols, cvec
def table(path):
    res = pickle.load(open(path, "rb")); out = {}
    for ik, (name, m, v) in enumerate(res['klist']):
        pols = channel_pols(np.array(v, float)); k = res['K'][ik]; q2 = float((4*np.sin(k/2)**2).sum())
        for ch in ["TT", "V", "S"]:
            for ie, e in enumerate(pols[ch]):
                c = cvec(e)
                sb = np.array([np.real(c @ res['Mb'][b, ik] @ c) for b in range(20)])
                fb = np.array([np.real(c @ res['Fb'][b, ik] @ c) for b in range(20)])
                out.setdefault((name, m, ch + str(ie + 1)), []).append((q2, sb, fb))
    rows = []
    for (name, m, ch), lst in out.items():
        q2 = np.mean([x[0] for x in lst]); sb = np.mean([x[1] for x in lst], 0); fb = np.mean([x[2] for x in lst], 0)
        w = fb/sb
        rows.append((name, m, ch, q2, sb.mean(), sb.std()/np.sqrt(20), fb.mean(), fb.std()/np.sqrt(20), fb.mean()/sb.mean(), w.std()/np.sqrt(20)))
    return res, rows
if __name__ == "__main__":
    for p in sys.argv[1:]:
        res, rows = table(p)
        print("== %s  L=%d bU=%.2f E/edge=%.5f+-%.5f (trace %s)" % (p.split('/')[-1], res['L'], res['bU'], res['Eb'].mean(), res['Eb'].std()/np.sqrt(20), np.round(res['Etr'][[0, 25, -1]], 5)))
        for r in sorted(rows, key=lambda r: (r[0], r[1], r[2])):
            print("  %-4s m=%d %-3s q2=%.4f  S=%.5f(%.5f)  f=%.5f(%.5f)  f/S=%.4f(%.4f)" % r)
