"""A33 torus tests shared by the period-2 searches.

Exactness note: if a Pauli on Z^3 moves a defect by v, its wrapped copy does the same on every
even L-torus with L larger than the generators' diameter (syndromes add linearly over lifts).
So 'immobile on such a torus' is an EXACT statement about Z^3; 'mobile on a torus' needs a
check on larger tori (or an explicit local mover) before it is claimed for Z^3.
"""
import itertools
from p2lib import Torus, Elim, syndrome_table, LBITS


def build(gen_list, L):
    """gen_list: list of (site, sign, pattern) on the L-torus (pattern in absolute coords)."""
    T = Torus(L)
    gens = []
    for x, s, p in gen_list:
        gens.append(T.bits(T.wrapped(p)))
    return T, gens


def rank_k(T, gens):
    E = Elim()
    for g in gens:
        E.add(g[0] | (g[1] << T.N))
    return len(gens) - len(E), len(E)


def syndrome_span(T, gens, track=False):
    sx, sz = syndrome_table(T, gens)
    E = Elim()
    for i, v in enumerate(sx + sz):
        E.add(v, (1 << i) if track else 0)
    return E


def mobile_moves(T, E, x0):
    """displacements v != 0 (as site tuples mod L) with delta_x0 + delta_{x0+v} in the span."""
    i0 = T.idx(x0)
    out = []
    for y in T.sites:
        j = T.idx(y)
        if j == i0:
            continue
        if E.reduce((1 << i0) | (1 << j))[0] == 0:
            out.append(tuple((a - b) % T.L for a, b in zip(y, x0)))
    return out


def creatable(E, i):
    return E.reduce(1 << i)[0] == 0


def local_logicals(T, gens, box):
    """(C_B, S_B): dim of Paulis on the box commuting with all generators, and dim of stabilizer
    elements supported in the box. C_B > S_B <=> a local logical operator inside the box."""
    bidx = [T.idx(y) for y in box]
    pos = {i: k for k, i in enumerate(bidx)}
    nb = len(bidx)
    inmask = 0
    for i in bidx:
        inmask |= 1 << i
    # C_B: commutation rows restricted to the box
    Ec = Elim()
    for xb, zb in gens:
        if not ((xb | zb) & inmask):
            continue
        row = 0
        for i in bidx:
            k = pos[i]
            if (zb >> i) & 1:
                row |= 1 << (2 * k)
            if (xb >> i) & 1:
                row |= 1 << (2 * k + 1)
        Ec.add(row)
    CB = 2 * nb - len(Ec)
    # S_B: combinations of generators with no support outside the box; outside bits placed high
    N = T.N
    Es = Elim()
    outmask = ((1 << N) - 1) ^ inmask
    for xb, zb in gens:
        ox = xb & outmask
        oz = zb & outmask
        ins = 0
        for i in bidx:
            k = pos[i]
            if (xb >> i) & 1:
                ins |= 1 << (2 * k)
            if (zb >> i) & 1:
                ins |= 1 << (2 * k + 1)
        v = (((ox << N) | oz) << (2 * nb)) | ins
        Es.add(v)
    SB = sum(1 for h in Es.rows if h < 2 * nb)
    return CB, SB


def box(c, side):
    return [tuple(c[i] + d[i] for i in range(3)) for d in itertools.product(range(side), repeat=3)]
