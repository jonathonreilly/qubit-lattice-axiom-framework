"""Summarise d2_scan1d_N1024.out: per (band, c, mode) over converged runs (SC res < 1e-9, E > 0 on zone
bottom so the E^2 fit is meaningful): range of small-delta exponent p, max kink ratio, and the minimum
SLAC-fit deviation per window relative to the bare band's.
Filter: SC converged (res < 1e-9), E(0) > 0 (E positive on the whole zone, so the E^2 fit with the
bare energy zero is meaningful), all fit errors < 1."""
import re, sys, collections
rows = [l for l in open(sys.argv[1]) if l.startswith(('TB', 'KG'))]
grp = collections.defaultdict(list)
for l in rows:
    f = [x.strip() for x in l.split('|')]
    head = f[0].split(); band, c, a, g2, mode = head[0], head[1], head[2], head[3], head[4]
    E0, Epi = map(float, f[1].split()); Z0, Zpi = map(float, f[2].split())
    ps = list(map(float, f[4].split())); kink = float(f[5])
    devs = [tuple(map(float, re.match(r'([\d.]+)\[([\d.]+)\]', x).groups())) for x in f[6].split()[:3]]
    conv = True
    if mode == 'SC':
        m = re.search(r'res=([\d.e+-]+)', l); conv = float(m.group(1)) < 1e-9
    grp[(band, c, mode)].append(dict(a=a, g2=g2, E0=E0, Zpi=Zpi, p=ps, kink=kink, devs=devs, conv=conv))
print("band c mode | n_conv/n | p(smallest d) range | max kink ratio | min SLAC dev/bw per window (bare) [case]")
for key, L in grp.items():
    C = [r for r in L if r['conv'] and r['E0'] > 0 - 10]
    ok = [r for r in L if r['conv'] and r['E0'] > 0 and max(d[0] for d in r['devs']) < 1]
    if not ok: print(key, 'no converged'); continue
    p0 = [r['p'][0] for r in ok]; k = [r['kink'] for r in ok]
    mins = []
    for wi in range(3):
        best = min(ok, key=lambda r: r['devs'][wi][0])
        mins.append(f"{best['devs'][wi][0]:.4f}({best['devs'][wi][1]:.4f})[{best['a']},{best['g2']}]")
    print(f"{key[0]} {key[1]} {key[2]} | {len(ok)}/{len(L)} | {min(p0):.3f}..{max(p0):.3f} | {max(k):.4f} | " + " ".join(mins))
