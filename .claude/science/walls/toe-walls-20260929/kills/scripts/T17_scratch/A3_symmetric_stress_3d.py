"""3D version of A2: bond, diagonal pair, L-triple, plaquette clusters with six contents (subsets N=2,3, plus plaquette N=4 sample)."""
import itertools, sys, random
import numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('A2', 'A2_symmetric_stress.py')
src = open('A2_symmetric_stress.py').read().split("worst = defaultdict")[0]
ns = {}
exec(src, ns)
CL, E3, events, dpi_of, solve_stress = ns['CLUSTERS'], ns['E3'], ns['events'], ns['dpi_of'], ns['solve_stress']
random.seed(3)
worst = defaultdict(float); count = defaultdict(int)
for name in ('bond', 'diag2d', 'ltriple', 'plaquette'):
    sites = CL[name]; n = len(sites)
    for mask in range(1, 1 << n):
        xs = [sites[i] for i in range(n) if mask >> i & 1]
        if len(xs) < 2: continue
        evs = events(xs, E3)
        if len(evs) > 60: evs = random.sample(evs, 60)      # sample for speed (N=4 plaquette has ~1000 pairs)
        for xs_, c1, c2 in evs:
            r = solve_stress(3, xs_, dpi_of(xs_, c1, c2), margin=2, symmetric=True)
            worst[name] = max(worst[name], r); count[name] += 1
for k in worst:
    print('3D six-content events', k, ': tested', count[k], 'worst symmetric-stress residual', f'{worst[k]:.2e}')
xs = [(0,0,0), (1,0,0)]
c1 = ((1,0,0), (0,1,0)); c2 = ((0,1,0), (1,0,0))
print('3D control perpendicular exchange: symmetric residual', f"{solve_stress(3, xs, dpi_of(xs, c1, c2), symmetric=True):.3f}")
