"""Pack all run summaries (jsonl) and saved S(k) arrays into scripts/lock1_archive.npz; list peak locations."""
import json, glob, collections, numpy as np
recs, Sk = [], {}
for f in sorted(glob.glob("runs/*.jsonl")):
    recs += [l.strip() for l in open(f)]
for f in sorted(glob.glob("runs/*_Sk.npz")):
    d = np.load(f)
    Sk.update({k: d[k] for k in d.files})
np.savez_compressed("scripts/lock1_archive.npz", summaries=np.array(recs), **Sk)
cnt = collections.Counter()
for l in recs:
    r = json.loads(l)
    if r["Smax_over_V"] > 0.002:
        L = r["L"]; k = tuple(sorted(min(c, L - c) for c in r["kmax"]))
        cls = "corner(pi,pi,pi)" if k == (L//2,)*3 else ("smallest-k" if k == (0, 0, 1) else f"other {k} L={L} g={r['g']} rho={r['rho']} start={r['start']} SQ/V={r['SQ_over_V']:.4f}")
        cnt[cls] += 1
print(len(recs), "runs archived;", len(Sk), "S(k) arrays")
for k, v in cnt.items(): print(v, k)
