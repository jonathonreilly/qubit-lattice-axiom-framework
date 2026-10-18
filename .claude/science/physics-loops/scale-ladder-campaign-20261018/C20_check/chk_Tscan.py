"""T scan of the leading channel per sector (all 20 O_h sectors, q=0 and Q), to see where the ranking holds."""
import sys, numpy as np
sys.argv = ['x']
src = open('chk_lindhard.py').read().split('# 1) reproduce')[0]
exec(src)
for N, T in ((12, 0.03), (16, 0.05), (16, 0.07), (16, 0.1), (16, 0.15), (16, 0.2), (12, 0.3)):
    out = {}
    for lab, qv in (('0', np.zeros(3)), ('Q', Q)):
        for s in sectors: out[s + '@' + lab] = top(s, qv, N, T, 0.017)[0]
    best = sorted(out.items(), key=lambda kv: -kv[1])[:5]
    print(N, T, [(k, round(v, 4)) for k, v in best], 'A1u@0', round(out['A1u@0'], 4), 'A2u@Q', round(out['A2u@Q'], 4), flush=True)
