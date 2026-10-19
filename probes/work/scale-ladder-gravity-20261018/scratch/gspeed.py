"""E3': how fast does a record's pull reach far sites? A record forms at the centre at tick 0 and from then on drains
the pace field (source -q). Two tick rules for the pace deficit d:
  first-order (relax once per tick):  d(t+1) = d(t) + D * lap d(t) + q*delta
  lean-away-in-time (second-order):   d(t+1) = 2 d(t) - d(t-1) + s * lap d(t) + s*q*delta
Report d at distance r along an axis versus tick, normalised by its late static value."""
import numpy as np
L = 112; c = L//2
def lap(u): return (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2) - 6*u)
src = np.zeros((L, L, L)); src[c, c, c] = 1.0
probes = (10, 20)
def run(kind, T, s=0.25, D=1/6, damp=0.0):
    d0 = np.zeros((L, L, L)); d1 = d0.copy(); hist = {r: [] for r in probes}
    for t in range(T):
        if kind == 'first':
            d1 = d1 + D*lap(d1) + src*0.01
        else:
            d2 = (2 - damp)*d1 - (1 - damp)*d0 + s*lap(d1) + s*src*0.01; d0, d1 = d1, d2
        for r in probes: hist[r].append(d1[c + r, c, c])
    return hist
static = {r: 0.01/(4*np.pi*r) for r in probes}           # continuum static profile for the drain (lap d = -q delta)
for kind, T, extra in (('first', 400, {}), ('second', 120, {'s': 0.25}), ('second', 120, {'s': 0.25, 'damp': 0.05})):
    h = run(kind, T, **extra); lab = kind + (f" s={extra.get('s')}" if extra else '') + (f" damped {extra['damp']}" if 'damp' in extra else '')
    for r in probes:
        v = np.array(h[r]) / static[r]
        first_tick = int(np.argmax(np.abs(v) > 0.05)) if np.any(np.abs(v) > 0.05) else -1
        print(f"{lab:26s} r={r:2d}: reaches 5% of static at tick {first_tick:3d} (light-cone r/c = {r/0.5:.0f} for c=0.5); value/static at ticks 10,20,40,80,{T-1}: " +
              " ".join(f"{v[min(t, T-1)]:+.3f}" for t in (10, 20, 40, 80, T-1)))
