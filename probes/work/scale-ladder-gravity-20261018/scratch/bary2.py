import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
B = pickle.load(open('bary.pkl', 'rb'))
rng = np.random.default_rng(0)
for kk in [rng.standard_normal(4)*0.5, np.array([0.7, 0, 0, 0]), np.array([1.5, -0.8, 0.4, 2.0])]:
    s = np.sort(np.linalg.svd(B.Q(kk), compute_uv=False)); s /= s[-1]
    lg = np.log10(np.maximum(s, 1e-300)); gaps = np.diff(lg); i = int(np.argmax(gaps[:150]))
    print(f"k={np.round(kk,2)}: largest log-gap after index {i+1} (sv {s[i]:.1e} -> {s[i+1]:.1e}); nullity ~ {i+1}; sv 62..70:", " ".join(f"{x:.0e}" for x in s[62:70]))
