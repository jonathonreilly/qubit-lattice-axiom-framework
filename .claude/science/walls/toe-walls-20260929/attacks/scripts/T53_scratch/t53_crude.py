"""T53: CRUDE distance of each surviving (J<0) sheet from the repo-quoted NuFIT-6.1 best fit.
Yardstick (flagged crude; NOT a likelihood): 1 sigma proxy = repo-quoted asymmetric errors for dCP
(207 +23/-20 noSK ; 212 +26/-36 SK, docs/PMNS_DCP_FORECAST_STANDING_DEGRADES...:37-46) and one third of the
repo-quoted 3sigma half-range on each side for s23^2 (0.470; 3s [0.432,0.587] noSK, [0.435,0.584] SK)."""
import math, json
sheets = {'(g+,210) forecast sheet': dict(d=(258.985, 269.606), s=(0.5330, 0.5453)),
          '(g-,201) partner sheet': dict(d=(270.394, 281.015), s=(0.4547, 0.4670))}
cols = {'noSK': dict(dbest=207., dlo=20., dhi=23., sbest=0.470, s3=(0.432, 0.587)),
        'SK':   dict(dbest=212., dlo=36., dhi=26., sbest=0.470, s3=(0.435, 0.584))}
out = {}
for name, sh in sheets.items():
    for cn, c in cols.items():
        def zd(x): return (x - c['dbest']) / c['dhi'] if x >= c['dbest'] else (c['dbest'] - x) / c['dlo']
        def zs(x):
            up = (c['s3'][1] - c['sbest']) / 3; lo = (c['sbest'] - c['s3'][0]) / 3
            return (x - c['sbest']) / up if x >= c['sbest'] else (c['sbest'] - x) / lo
        zdr = sorted([zd(sh['d'][0]), zd(sh['d'][1])]); zsr = sorted([zs(sh['s'][0]), zs(sh['s'][1])])
        comb = (math.hypot(zdr[0], zsr[0]), math.hypot(zdr[1], zsr[1]))
        out[f'{name} | {cn}'] = dict(z_dCP=[round(v, 2) for v in zdr], z_s23=[round(v, 2) for v in zsr], z_quadrature=[round(v, 2) for v in comb])
        print('%-26s %-5s z(dCP)=%s z(s23^2)=%s quadrature=%s' % (name, cn, [round(v, 2) for v in zdr], [round(v, 2) for v in zsr], [round(v, 2) for v in comb]))
json.dump(out, open('crude_result.json', 'w'), indent=1)
