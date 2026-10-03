"""A33 a21: the Wyckoff-subspace class W(r2<=R2, dim<=2) (R2 from env A33_R2, default 2; r_inf must be 1) -- period-2 covariant stabilizer groups whose
checks at each role site span a subspace U_role (dim 0, 1 or 2) of the exactly invariant shapes
(site group O for V, C; D4 for E, F) in the ball |d|^2 <= 2. Several checks per site are allowed, so
the stabilizer module need not be free (local relations allowed): this is where Theorem C does not
apply. P2-A is the special case dim U = 1 everywhere (already done; skipped here).
stage 1 (count): all mutually commuting choices with dV + dC + 3dE + 3dF >= 8 and some dim = 2.
  writes w_combos.pkl
stage 2 (start end): rank on L=8 (k8 = N - rank), exact impurity certificate (3^3 / 4^3 boxes),
  single-check-flip mobility per check type on L = 8 then 12; appends to w_stage2.txt
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, quad_ok, sign_ok_role, ROLES, role_of, shape_at, functional
from p2lib import combo, pcomm, translate, Torus, Elim, popc
from p2_tests import syndrome_span, mobile_moves, rank_k
from a9_inspect_lib import certificate

import os
R2 = int(os.environ.get("A33_R2", "2"))
S = Space(R2)
assert S.rinf == 1
stage = int(sys.argv[1])
t0 = time.time()


def shape(r, c):
    return combo(S.basis[r], [(c >> i) & 1 for i in range(S.dim[r])])


if stage == 1:
    cons = S.bilinear_constraints()
    valid = {r: [c for c in range(1, 1 << S.dim[r]) if quad_ok(c, list(cons.get((r, r), ()))) and sign_ok_role(S, r, c)]
             for r in ROLES}
    print("valid shapes per role:", {r: len(v) for r, v in valid.items()})

    def pair_ok(r1, c1, r2, c2):
        """all images of shape c1 (role r1) commute with all images of c2 (role r2), incl. same site."""
        for B in cons.get((r1, r2), ()):
            if popc(functional(c1, B) & c2) & 1:
                return False
        for B in cons.get((r2, r1), ()):
            if popc(functional(c2, B) & c1) & 1:
                return False
        if r1 == r2:   # same site, same role: the two shapes must commute
            if pcomm(shape(r1, c1), shape(r2, c2)):
                return False
        return True

    # subspaces of dim <= 2 per role: basis tuples (a,) or (a, b) with a < b, a^b valid, all commuting
    subs = {}
    for r in ROLES:
        vs = set(valid[r])
        out = [()]
        out += [(a,) for a in valid[r]]
        seen = set()
        for a, b in itertools.combinations(valid[r], 2):
            sp = frozenset((a, b, a ^ b))
            if sp in seen or (a ^ b) not in vs:
                continue
            if pair_ok(r, a, r, b):
                seen.add(sp)
                out.append((a, b))
        subs[r] = out
    print("subspaces (dim<=2) per role:", {r: len(v) for r, v in subs.items()}, f"({time.time()-t0:.1f}s)", flush=True)

    def compat(r1, U1, r2, U2):
        return all(pair_ok(r1, a, r2, b) for a in U1 for b in U2)

    combos = []
    for UV in subs["V"]:
        for UC in subs["C"]:
            if not compat("V", UV, "C", UC):
                continue
            Es = [UE for UE in subs["E"] if compat("V", UV, "E", UE) and compat("C", UC, "E", UE)]
            Fs = [UF for UF in subs["F"] if compat("V", UV, "F", UF) and compat("C", UC, "F", UF)]
            for UE in Es:
                for UF in Fs:
                    dims = (len(UV), len(UC), len(UE), len(UF))
                    if max(dims) < 2 or dims[0] + dims[1] + 3 * dims[2] + 3 * dims[3] < 8:
                        continue
                    if compat("E", UE, "F", UF):
                        combos.append({"V": UV, "C": UC, "E": UE, "F": UF})
    pickle.dump(combos, open(f"w_combos_r{R2}.pkl", "wb"))
    from collections import Counter
    print(f"commuting combos with some dim 2 and >= 8 checks per cell: {len(combos)}; by dims:",
          sorted(Counter((len(c['V']), len(c['C']), len(c['E']), len(c['F'])) for c in combos).items()),
          f"({time.time()-t0:.1f}s)")
    sys.exit()

a, b = int(sys.argv[2]), int(sys.argv[3])
combos = pickle.load(open(f"w_combos_r{R2}.pkl", "rb"))


def gen_list(cb, L):
    """list of (site, check-type label, pattern) for all checks on the L-torus."""
    out = []
    for x in itertools.product(range(L), repeat=3):
        r, ax = role_of(x)
        for j, c in enumerate(cb[r]):
            _, p = shape_at(shape(r, c), r, ax, x)
            out.append((x, (r, j), p))
    return out


REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
lines = []
for n in range(a, min(b, len(combos))):
    cb = combos[n]
    rec = {}
    T = Torus(8)
    gl = gen_list(cb, 8)
    gens = [T.bits(T.wrapped(p)) for _, _, p in gl]
    rk = Elim()
    for g in gens:
        rk.add(g[0] | (g[1] << T.N))
    k8 = T.N - len(rk)
    # impurity certificate: generators of all types (box commutant with every check)
    sh_multi = cb
    cert = "-"
    # build a pseudo-shape dict usable by a9_inspect_lib.certificate: it needs one shape per role;
    # emulate several checks per role by testing each box against all of them
    from a9_inspect_lib import commutant as _comm
    import a9_inspect_lib as AL
    for side in (3, 4):
        B = [tuple(2 + d[i] for i in range(3)) for d in itertools.product(range(side), repeat=3)]
        pats = None
        # commutant with all checks = intersection over check indices j of the commutant with the j-th shapes
        rows_pats = []
        Bset = set(B); pos = {y: k for k, y in enumerate(B)}
        E = Elim()
        for x in {tuple(p + d for p, d in zip(y, dd)) for y in B for dd in itertools.product(range(-1, 2), repeat=3)}:
            r, ax = role_of(x)
            for c in cb[r]:
                _, p = shape_at(shape(r, c), r, ax, x)
                row = 0
                for z, l in p.items():
                    if z in pos:
                        kk = pos[z]
                        bx, bz = {1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
                        if bz: row |= 1 << (2 * kk)
                        if bx: row |= 1 << (2 * kk + 1)
                if row:
                    E.add(row)
        nB = 2 * len(B)
        R = {h: v for h, (v, _) in E.rows.items()}
        hs = sorted(R, reverse=True)
        for h in hs:
            for h2 in hs:
                if h2 != h and (R[h2] >> h) & 1:
                    R[h2] ^= R[h]
        vecs = []
        for f in range(nB):
            if f in R: continue
            v = 1 << f
            for h, row in R.items():
                if (row >> f) & 1: v |= 1 << h
            vecs.append(v)
        xm = sum(1 << (2 * k) for k in range(len(B))); zm = xm << 1
        found = False
        for i in range(len(vecs)):
            for j in range(i + 1, len(vecs)):
                t = popc(((vecs[i] & xm) << 1) & (vecs[j] & zm)) + popc(((vecs[j] & xm) << 1) & (vecs[i] & zm))
                if t & 1:
                    found = True; break
            if found: break
        if found:
            cert = f"{side}^3"; break
    mob = "-"
    if cert == "-":
        mobs = {}
        for L in (8, 12):
            T = Torus(L)
            gl = gen_list(cb, L)
            gens = [T.bits(T.wrapped(p)) for _, _, p in gl]
            Esp = syndrome_span(T, gens)
            # single flipped check of each type at the representative site: index in gl
            idx = {}
            for gi, (x, typ, _) in enumerate(gl):
                if x == REP[typ[0]]:
                    idx[typ] = gi
            mobs[L] = {}
            for typ, gi in idx.items():
                cnt = 0
                for gj, (y, typ2, _) in enumerate(gl):
                    if gj != gi and Esp.reduce((1 << gi) | (1 << gj))[0] == 0:
                        cnt += 1
                mobs[L][typ] = cnt
            if not any(mobs[L].values()):
                break
        mob = mobs[max(mobs)]
        mob = f"L={max(mobs)} {mob}"
    lines.append(f"{n} dims={tuple(len(cb[r]) for r in 'VCEF')} cb={cb} k8={k8} cert={cert} mob={mob}")
    if time.time() - t0 > 48:
        lines.append(f"# stopped after {n}")
        break
with open(f"w_stage2_r{R2}.txt", "a") as fh:
    fh.write("\n".join(lines) + "\n")
print(f"stage 2 [{a},{b}): {len(lines)} lines   ({time.time()-t0:.1f}s)")
