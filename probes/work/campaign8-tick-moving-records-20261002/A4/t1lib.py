"""Supplied toy T1: moving records with crowd-tilted odds on a periodic grid (any dimension).

One tick = move phase, then formation phase.

Move phase (I2, I3 as supplied toy rules):
  * every record at x draws one option from {stay} + {each empty neighbour y}
    with odds  w(y) = exp(g * S_y),  S_y = records around y other than the mover,
               w(stay) = exp(g * S_x), S_x = records around x (x itself not counted);
    occupied neighbours get odds 0;
  * several records drawing the same empty y: one wins, chosen with probability
    proportional to its normalised choice probability (relative odds); losers stay;
  * destinations must be empty at the start of the tick (no chains), so each site
    receives at most one record and each record moves at most one site.
Formation phase: on the post-move configuration, each empty site forms at most one
record, with odds set by the chosen formation rule.

Everything is vectorised numpy; periodic boundaries via np.roll.
"""
import numpy as np


def directions(d):
    return [(ax, s) for ax in range(d) for s in (+1, -1)]


def neighbour_count(occ):
    n = np.zeros(occ.shape, dtype=np.int16)
    for ax in range(occ.ndim):
        n += np.roll(occ, 1, axis=ax)
        n += np.roll(occ, -1, axis=ax)
    return n


def at_dest(a, ax, s):
    """value of array a at x + s*e_ax, indexed by x."""
    return np.roll(a, -s, axis=ax)


def to_dest(a, ax, s):
    """move a value defined at origin x to index y = x + s*e_ax."""
    return np.roll(a, s, axis=ax)


def move_phase(occ, g, rng, expg=None):
    """Return (new_occ, moved_out, arrived, wins) for one T1 move phase.

    moved_out[x] : a record left x this tick
    arrived[y]   : a record arrived at y this tick
    wins[i][y]   : the arrival at y came through direction i (origin y - s e_ax)
    """
    d = occ.ndim
    z = 2 * d
    if expg is None:
        expg = np.exp(g * np.arange(z + 1))
    nrec = neighbour_count(occ)
    empty = ~occ
    dirs = directions(d)
    w_stay = expg[nrec]
    ws = []
    for ax, s in dirs:
        dest_ok = occ & at_dest(empty, ax, s)
        sy = np.clip(at_dest(nrec, ax, s) - 1, 0, z)  # exclude the mover
        ws.append(np.where(dest_ok, expg[sy], 0.0))
    Z = w_stay + np.sum(ws, axis=0)
    probs = [w / Z for w in ws]
    u = rng.random(occ.shape)
    cum = np.zeros(occ.shape)
    claims = []
    for i, (ax, s) in enumerate(dirs):
        chose = occ & (u >= cum) & (u < cum + probs[i])
        cum = cum + probs[i]
        claims.append(to_dest(np.where(chose, probs[i], 0.0), ax, s))
    T = np.sum(claims, axis=0)
    v = rng.random(occ.shape) * T
    cum = np.zeros(occ.shape)
    new = occ.copy()
    moved_out = np.zeros(occ.shape, dtype=bool)
    arrived = np.zeros(occ.shape, dtype=bool)
    wins = []
    for i, (ax, s) in enumerate(dirs):
        win = (claims[i] > 0) & (v >= cum) & (v < cum + claims[i])
        cum = cum + claims[i]
        origin = at_dest(win, ax, s)  # origin x of an arrival at y = x + s e_ax: origin[x] = win[x + s e_ax]
        new[origin] = False
        moved_out |= origin
        arrived |= win
        wins.append(win)
    new[arrived] = True
    return new, moved_out, arrived, wins


def stir_counts(occ_shape, arrived, wins, d):
    """stirA[x]: arrivals at neighbours of x; stirB[x]: same, excluding an arrival that came from x."""
    stirA = np.zeros(occ_shape, dtype=np.int16)
    stirB = np.zeros(occ_shape, dtype=np.int16)
    for i, (ax, s) in enumerate(directions(d)):
        # neighbour y = x + s e_ax ; arrival at y from x means it came through direction (ax, s)
        stirA += at_dest(arrived, ax, s)
        stirB += at_dest(arrived & ~wins[i], ax, s)
    return stirA, stirB


def formation_phase(occ, rule, rng, params, stir=None):
    d = occ.ndim
    z = 2 * d
    empty = ~occ
    u = rng.random(occ.shape)
    p = params.get("p", 0.05)
    if rule == "none":
        return np.zeros(occ.shape, dtype=bool)
    nrec = neighbour_count(occ)
    if rule == "spont":
        odds = np.full(occ.shape, p)
    elif rule == "contact":
        odds = np.where(nrec >= 1, p, 0.0)
    elif rule == "crowdtrig":
        odds = np.where(nrec >= params.get("mtrig", z - 1), p, 0.0)
    elif rule == "kempty":
        k = params.get("k", 1)
        odds = np.where((z - nrec) >= k, p, 0.0)
    elif rule == "crowd_soft":
        odds = p * np.exp(-params.get("beta", 1.0) * nrec)
    elif rule == "crowd_hard":
        odds = p * ((z - nrec) / z) ** params.get("m", 1)
    elif rule in ("stirA", "stirB"):
        sA, sB = stir
        cnt = sA if rule == "stirA" else sB
        odds = 1.0 - (1.0 - p) ** cnt
    else:
        raise ValueError(rule)
    return empty & (u < odds)


def tick(occ, g, rule, rng, params, moves=True, expg=None):
    d = occ.ndim
    if moves:
        occ, moved_out, arrived, wins = move_phase(occ, g, rng, expg)
        stir = stir_counts(occ.shape, arrived, wins, d) if rule in ("stirA", "stirB") else None
    else:
        moved_out = np.zeros(occ.shape, dtype=bool)
        stir = (np.zeros(occ.shape, np.int16),) * 2
    form = formation_phase(occ, rule, rng, params, stir)
    occ = occ | form
    return occ, moved_out, form
