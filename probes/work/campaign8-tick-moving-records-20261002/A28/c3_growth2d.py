"""A28 c3: 2D classical toy of GATED formation with Option R record steps (supplied toy).

Sites: recorded (rec) or empty; empty sites may carry an 'excitation' bit (exc), a classical
stand-in for non-quiet possibilities.  Records are walls for excitations (A27 Step 1a).
One tick (A27 open edge 1: one joint instrument per empty site, PRE-tick pattern):
  each empty site with nrec>=1 recorded neighbours draws: form (prob f), claim one recorded
  neighbour (prob c_m*nrec/4, SW-blind W=1, neighbour chosen uniformly), or nothing.
  Gate closed (nrec=0): nothing (except variant V0, the ungated control, which may form).
  CL: a record claimed by several sites picks one uniformly; SW swap moves the claimant's
  content (exc bit) to the vacated site.  Formations lock (consume) the site's excitation.
  Then excitations hop (prob D_E, random direction, exclusion, records are walls).
Variants (f at a gate-open empty site; e = excitation bit; enclosed = nrec==4):
  V0 ungated sea   : f = eps everywhere (A4 F-spont control)
  V1 gated sea     : f = eps                      (open enclosure: p0 = eps)
  V2 gated sea, blind enclosure: f = eps if nrec<4 else 0   (p0 = 0)
  V3 gated quiet   : f = p_e * e                  (vanishes on quiet possibilities)
  V4 gated quiet + edge floor: f = p_e*e + eps*[nrec<4]
  V5 gated quiet + supply: V3 plus excitations injected at random empty sites (rate s)
Preparations: disc (radius 8, fully recorded, centre) or sparse (density 0.003).
Usage: python3 c3_growth2d.py VARIANT PREP [T]
"""
import signal, sys
import numpy as np
signal.alarm(55)

var = sys.argv[1]; prep = sys.argv[2]
T = int(sys.argv[3]) if len(sys.argv) > 3 else 3000
L = 128; c_m = 0.4; eps = 0.01; p_e = 0.5; u_E = 0.05; D_E = 0.8; s_sup = 2e-4
rng = np.random.default_rng(20261003)
X, Y = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
dist = np.sqrt((X - L // 2) ** 2 + (Y - L // 2) ** 2)
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if prep == 'disc':
    rec = dist <= 8.0
else:
    rec = rng.random((L, L)) < 0.003
exc = (~rec) & (rng.random((L, L)) < (u_E if var in ('V3', 'V4', 'V5') else 0.0))
n_rec0 = int(rec.sum()); n_exc0 = int(exc.sum())


def shift(a, d):
    return np.roll(a, shift=(-d[0], -d[1]), axis=(0, 1))  # value at x+d


ever_event = np.zeros((L, L), dtype=np.int64) - 1  # last tick with a record event
hist = []
form_acc = move_acc = 0
ev_map = np.zeros((L, L), dtype=np.int64)
for t in range(1, T + 1):
    nb = [shift(rec, d) for d in DIRS]
    nrec = sum(b.astype(np.int8) for b in nb)
    empty = ~rec
    gate = empty & (nrec >= 1)
    if var == 'V0':
        f = np.where(empty, eps, 0.0)
    elif var == 'V1':
        f = np.where(gate, eps, 0.0)
    elif var == 'V2':
        f = np.where(gate & (nrec < 4), eps, 0.0)
    elif var in ('V3', 'V5'):
        f = np.where(gate & exc, p_e, 0.0)
    elif var == 'V4':
        f = np.where(gate, p_e * exc + eps * (nrec < 4), 0.0)
    pc = np.where(gate, c_m * nrec / 4.0, 0.0)
    u = rng.random((L, L))
    form = u < f
    claim = (~form) & (u < f + pc)
    # claimants pick one recorded neighbour uniformly
    ci = np.flatnonzero(claim)
    if ci.size:
        cx, cy = np.unravel_index(ci, (L, L))
        has = np.stack([b.reshape(-1)[ci] for b in nb], axis=1)  # (n,4)
        k = (rng.random(ci.size) * has.sum(1)).astype(int)
        cs = np.cumsum(has, axis=1)
        dsel = np.argmax(cs > k[:, None], axis=1)
        dx = np.array([d[0] for d in DIRS])[dsel]; dy = np.array([d[1] for d in DIRS])[dsel]
        tx = (cx + dx) % L; ty = (cy + dy) % L
        tgt = tx * L + ty
        key = rng.random(ci.size)
        order = np.lexsort((key, tgt))
        _, first = np.unique(tgt[order], return_index=True)
        win = order[first]
        wc, wt = ci[win], tgt[win]
        recf = rec.reshape(-1); excf = exc.reshape(-1)
        recf[wt] = False; recf[wc] = True
        excf[wt] = excf[wc]; excf[wc] = False
        nmove = wc.size
        ev_map.reshape(-1)[wc] += 1
        ever_event.reshape(-1)[wc] = t
    else:
        nmove = 0
    # formations (sites that drew 'form' were empty, never claimants or vacated sites)
    rec |= form
    exc &= ~form
    nform = int(form.sum())
    ev_map[form] += 1
    ever_event[form] = t
    form_acc += nform; move_acc += nmove
    # excitation hop (possibility change surrogate): records are walls, exclusion
    ei = np.flatnonzero(exc & (rng.random((L, L)) < D_E))
    if ei.size:
        ex_, ey_ = np.unravel_index(ei, (L, L))
        dsel = rng.integers(0, 4, ei.size)
        dx = np.array([d[0] for d in DIRS])[dsel]; dy = np.array([d[1] for d in DIRS])[dsel]
        tt = ((ex_ + dx) % L) * L + (ey_ + dy) % L
        ok = (~rec.reshape(-1)[tt]) & (~exc.reshape(-1)[tt])
        ei, tt = ei[ok], tt[ok]
        key = rng.random(ei.size)
        order = np.lexsort((key, tt))
        _, first = np.unique(tt[order], return_index=True)
        w = order[first]
        excf = exc.reshape(-1)
        excf[ei[w]] = False; excf[tt[w]] = True
    if var == 'V5':
        exc |= (~rec) & (rng.random((L, L)) < s_sup)
    if t % (T // 10) == 0:
        rr = dist[rec]
        Rf = np.percentile(rr, 99) if rr.size else 0.0
        Rin = max(6.0, 0.5 * Rf)
        inner = dist <= Rin
        h_in = 1.0 - rec[inner].mean()
        win_t = T // 10
        ev_in = ev_map[inner].sum() / (inner.sum() * win_t)
        ev_all = ev_map.sum() / (L * L * win_t)
        recent = (ever_event > t - 200).mean()
        hist.append((t, int(rec.sum()), Rf, h_in, ev_in, ev_all, form_acc / win_t, move_acc / win_t, int(exc.sum()), recent))
        ev_map[:] = 0; form_acc = move_acc = 0

print(f'{var} {prep}: L={L} T={T} c_m={c_m} eps={eps} p_e={p_e} u_E={u_E} D_E={D_E}; records0={n_rec0} exc0={n_exc0}')
print('    t   N_rec  R_front  h_inner  ev/site/tick(inner)  ev/site/tick(all)  form/tick  move/tick  N_exc  frac sites w/ event in last 200')
for row in hist:
    t, n, Rf, h, ei_, ea, fo, mo, ne, rc = row
    print(f'{t:5d} {n:7d} {Rf:7.1f} {h:8.4f} {ei_:12.3e} {ea:18.3e} {fo:10.2f} {mo:9.2f} {ne:6d} {rc:8.4f}')
