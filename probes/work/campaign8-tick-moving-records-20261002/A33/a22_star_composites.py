"""A33 a22: composites of the translation-invariant star vacuum (S_x = s for all x).
Predicted (algebra in the report): the charge support V(I) is the four body-diagonal lines through
(1,1,1), so a dipole {0, d} with d a face diagonal moves only along the perpendicular face diagonal
(lineon), and the 8-defect composite Q = (1+z^(1,0,1))(1+z^(1,1,0))(1+z^(0,1,1)) moves only in the
plane perpendicular to (1,1,1) (planon). Checks:
  (a) torus L=8: composite moves by v (pattern s + translate(s, v) in the syndrome span) for all v;
  (b) explicit Z^3 movers in a box (exact); (c) exact loop phase of the planon around the
      parallelogram spanned by u = (1,-1,0), w = (0,1,-1), for vacuum sign s = +1 and s = -1.
"""
import signal, sys, time, itertools
signal.alarm(55)
from p2lib import Torus, Elim, LBITS, pat_str, pauli_exact, P, translate, BITS2L
from p2_tests import syndrome_span

t0 = time.time()
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
star = {}
for a in range(3):
    for sg in (1, -1):
        star[tuple(sg * E3[a][i] for i in range(3))] = a + 1
add = lambda p, q: tuple(x + y for x, y in zip(p, q))
neg = lambda p: tuple(-x for x in p)

L = 8
T = Torus(L)
gens = [T.bits(T.wrapped(translate(star, x))) for x in T.sites]
Esp = syndrome_span(T, gens)


def pat_bits(points):
    v = 0
    for p in points:
        v ^= 1 << T.idx(p)
    return v


def moves(points):
    base = pat_bits(points)
    out = []
    for v in T.sites:
        if v == (0, 0, 0):
            continue
        tgt = base ^ pat_bits([add(p, v) for p in points])
        if tgt and Esp.reduce(tgt)[0] == 0:
            out.append(tuple(((c + 3) % L) - 3 for c in v))
    return sorted(out, key=lambda v: (sum(map(abs, v)), v))


dip = [(0, 0, 0), (1, -1, 0)]
dip_ax = [(0, 0, 0), (1, 0, 0)]
Q = []
for bits in itertools.product((0, 1), repeat=3):
    p = (0, 0, 0)
    for b_, d in zip(bits, [(1, 0, 1), (1, 1, 0), (0, 1, 1)]):
        if b_:
            p = add(p, d)
    Q.append(p)
for name, pts in [("face-diagonal dipole {0,(1,-1,0)}", dip), ("axis dipole {0,(1,0,0)}", dip_ax), ("8-defect composite Q", Q)]:
    mv = moves(pts)
    print(f"L=8 {name}: {len(mv)} moves; shortest {mv[:6]}   ({time.time()-t0:.1f}s)", flush=True)


def z3_mover(points, v, margin=2):
    """Pauli on a box with syndrome exactly points + (points+v) (as a set mod 2), on Z^3."""
    tgt = set()
    for p in points + [add(p, v) for p in points]:
        tgt ^= {p}
    allp = list(tgt) or points
    lo = [min(p[i] for p in points + [add(p, v) for p in points]) - margin for i in range(3)]
    hi = [max(p[i] for p in points + [add(p, v) for p in points]) + margin for i in range(3)]
    B = list(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))
    pos = {y: k for k, y in enumerate(B)}
    xs = {add(y, d) for y in B for d in itertools.product((-1, 0, 1), repeat=3)}
    if not tgt <= xs:
        return None
    Eq = Elim()
    for x in xs:
        g = translate(star, x)
        row = 0
        for z, l in g.items():
            if z in pos:
                bx, bz = LBITS[l]
                k = pos[z]
                if bz: row |= 1 << (2 * k)
                if bx: row |= 1 << (2 * k + 1)
        rhs = int(x in tgt)
        if row == 0:
            if rhs: return None
            continue
        v_, c_ = Eq.reduce(row, rhs)
        if v_ == 0:
            if c_: return None
            continue
        Eq.rows[v_.bit_length() - 1] = (v_, c_)
    sol = 0
    for h in sorted(Eq.rows):
        v_, c_ = Eq.rows[h]
        if c_ ^ (bin((v_ ^ (1 << h)) & sol).count("1") & 1):
            sol |= 1 << h
    out = {}
    for k, y in enumerate(B):
        a_, b_ = (sol >> (2 * k)) & 1, (sol >> (2 * k + 1)) & 1
        if a_ or b_:
            out[y] = BITS2L[(a_, b_)]
    return out


for v in [(1, 1, 0), (1, -1, 0), (0, 0, 1)]:
    m = z3_mover(dip, v)
    print(f"Z3 mover for the face-diagonal dipole by {v}: {'|supp| ' + str(len(m)) if m is not None else 'none in box'}")
u, w = (1, -1, 0), (0, 1, -1)
Tu, Tw = z3_mover(Q, u), z3_mover(Q, w)
print(f"Z3 movers for Q: by u={u}: {'|supp| ' + str(len(Tu)) if Tu is not None else 'none'}; by w={w}: {'|supp| ' + str(len(Tw)) if Tw is not None else 'none'};"
      f" by (1,0,0): {'found' if z3_mover(Q, (1, 0, 0)) is not None else 'none in box'}")
if Tu is not None and Tw is not None:
    W = pauli_exact(Tw) * pauli_exact(translate(Tu, w)) * pauli_exact(translate(Tw, u)) * pauli_exact(Tu)
    # decompose W into stars near the loop
    pts = Q + [add(p, u) for p in Q] + [add(p, w) for p in Q] + [add(add(p, u), w) for p in Q]
    lo = [min(p[i] for p in pts) - 4 for i in range(3)]; hi = [max(p[i] for p in pts) + 4 for i in range(3)]
    cents = list(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))
    sites = sorted({add(c, d) for c in cents for d in star} | set(W.s))
    pos = {y: k for k, y in enumerate(sites)}
    def vec(pd):
        v_ = 0
        for y, l in pd.items():
            bx, bz = LBITS[l]; v_ |= (bx << (2 * pos[y])) | (bz << (2 * pos[y] + 1))
        return v_
    Eg = Elim()
    for i, c in enumerate(cents):
        Eg.add(vec(translate(star, c)), 1 << i)
    wl = {y: {(1, 0): 1, (1, 1): 2, (0, 1): 3}[b] for y, b in W.s.items()}
    r_, cmb = Eg.reduce(vec(wl), 0)
    assert r_ == 0
    A = [cents[i] for i in range(len(cents)) if (cmb >> i) & 1]
    prod = P()
    for c in A:
        prod = prod * pauli_exact(translate(star, c))
    cP = W * prod
    assert not cP.s
    c = [1, 1j, -1, -1j][cP.k % 4]
    inside = sum(1 for c_ in A if c_ in set(Q))
    for s in (1, -1):
        phi = c * (s ** len(A)) * ((-1) ** inside)
        print(f"planon Q loop (u then w then -u then -w): W = {c} * product of {len(A)} stars "
              f"({inside} of them at Q's own defects); vacuum sign s={s}: loop phase {phi}")
print(f"({time.time()-t0:.1f}s)")
