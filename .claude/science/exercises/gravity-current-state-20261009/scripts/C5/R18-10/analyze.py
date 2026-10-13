"""R18-1 analysis of run_mc.py output: channel structure factors, Identity-V check, pinch ratio, xi_eff."""
import numpy as np, pickle, sys
from mc import channel_pols, cvec
def channels(res):
    K = res['K']; Mb = res['Mb']; Gb = res['Gb']; out = {}
    for ik, (name, m, v) in enumerate(res['klist']):
        k = K[ik]; pols = channel_pols(np.array(v, float))
        q2 = float((4*np.sin(k/2)**2).sum())
        vals = {}
        for ch, lst in pols.items():
            vb = np.mean([[np.real(cvec(e) @ Mb[b, ik] @ cvec(e)) for e in lst] for b in range(Mb.shape[0])], axis=1)
            vals[ch] = vb
        vals['gam'] = Gb[:, ik]
        if name == "axis":   # Identity V: S_gamma(k e_j) = (q^2/4)(M_jj + M_ij,ij + M_kj,kj) for the slots containing j
            j = int(np.argmax(np.abs(v))); sl = {0: [0, 3, 5], 1: [1, 3, 4], 2: [2, 4, 5]}[j]
            idv = (q2/4)*np.array([sum(np.real(Mb[b, ik][s, s]) for s in sl) for b in range(Mb.shape[0])])
            vals['idV'] = idv
        out.setdefault((name, m), []).append((q2, vals))
    tab = {}
    for key, lst in out.items():
        q2 = np.mean([x[0] for x in lst]); d = {}
        for ch in lst[0][1]:
            arr = np.mean([x[1][ch] for x in lst], axis=0)   # per-bin average over cubic copies
            d[ch] = (arr.mean(), arr.std()/np.sqrt(len(arr)))
        rb = np.mean([x[1]['V'] for x in lst], 0)/np.mean([x[1]['TT'] for x in lst], 0)
        d['r'] = (rb.mean(), rb.std()/np.sqrt(len(rb)))
        tab[key] = (q2, d)
    return tab
def report(path, show=True):
    res = pickle.load(open(path, "rb")); tab = channels(res); L = res['L']
    lines = ["L=%d bU=%.2f init=%s acc=%.4f E/edge=%.5f+-%.5f (equil trace %s)" % (L, res['bU'], res['init'], res['acc'],
             res['Eb'].mean(), res['Eb'].std()/np.sqrt(len(res['Eb'])), np.round(res['Etr'][[0, len(res['Etr'])//2, -1]], 5))]
    for name in ["axis", "face", "body"]:
        for m in range(1, L//2 + 1):
            if (name, m) not in tab: continue
            q2, d = tab[(name, m)]
            s = "  %-4s m=%d q2=%.4f TT=%.4f V=%.4f(%.4f) S=%.4f Tr=%.4f gam/q2=%.4f r=V/TT=%.4f(%.4f)" % (
                name, m, q2, d['TT'][0], d['V'][0], d['V'][1], d['S'][0], d['T'][0], d['gam'][0]/q2, d['r'][0], d['r'][1])
            if 'idV' in d: s += " idV:|gam-(q2/4)sum|=%.1e" % abs(d['gam'][0] - d['idV'][0])
            lines.append(s)
    if show: print("\n".join(lines))
    return res, tab
if __name__ == "__main__":
    for p in sys.argv[1:]: report(p)
