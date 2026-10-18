#!/usr/bin/env python3
"""B6 (finite-spin EM response lane, #7966/W37): exact sparse ED of the supplied ring model on
2x2x2, 2x2x3, 2x2x4 tori.  Delivers
  (P3) winding-sector ground energies E(W) for x-flux (W,0,0) and z-flux (0,0,W) sectors,
       min over ALL flip components of the sector (frozen singletons have E = 0), and the
       Gaussian-comparator coefficient U_W = 2 A_a [E(W)-E(0)] / (L_a W^2);
  (P2) the full plaquette-source Hessian of the vacuum component projected on real Fourier
       source vectors at every lattice momentum: chi_L (q = 0, per orientation) and K_T(q).
PASS/FAIL lines check internal consistency against constants fixed elsewhere (landed notes /
the scale-ladder probe), exact identities, gauge invariance, translation block structure and
finite differences.  Exploratory; no claim.  Model, source convention and sectors are supplied.
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ringlib import *

T0 = time.time()
RES = []
OUT = {}
VS = [1.0, 0.9, 0.5, 0.0, -1.0]


def check(label, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def translate_codes(T, codes, a):
    """Image of each state under the unit translation along axis a (link permutation)."""
    perm = np.zeros(T.nl, np.int64)
    for v in T.verts:
        w = T.add(v, a)
        for b in range(3):
            perm[T.link(v, b)] = T.link(w, b)
    out = np.zeros_like(codes)
    for l in range(T.nl):
        out |= ((codes >> l) & 1) << perm[l]
    return out


def sector_ground(T, W, Vs):
    codes = sector_states(T, W)
    if len(codes) == 0:
        return None
    inv, sizes, nf = split_components(T, codes)
    best = {V: (np.inf, -1) for V in Vs}
    order = np.argsort(sizes)[::-1]
    for ci in order:
        if sizes[ci] == 1:
            e = float(nf[np.flatnonzero(inv == ci)[0]])  # V * N_f, N_f = 0 for frozen
            for V in Vs:
                if V * e < best[V][0] - 1e-12:
                    best[V] = (V * e, 1)
            continue
        comp = Component(T, codes[inv == ci])
        for V in Vs:
            E0 = comp.ground(V)[0]
            if E0 < best[V][0] - 1e-12:
                best[V] = (E0, int(sizes[ci]))
    return dict(n_states=int(len(codes)), n_comp=int(len(sizes)), largest=int(sizes.max()),
                E={V: best[V][0] for V in Vs}, comp_of_min={V: best[V][1] for V in Vs})


def momenta(T):
    Lx, Ly, Lz = T.dims
    qs = []
    for kx in range(Lx // 2 + 1):
        for ky in range(Ly // 2 + 1):
            for kz in range(Lz // 2 + 1):
                qs.append((2 * np.pi * kx / Lx, 2 * np.pi * ky / Ly, 2 * np.pi * kz / Lz))
    return qs


def run_size(dims):
    T = Torus(dims)
    tag = "x".join(map(str, dims))
    res = dict(dims=dims)
    t = time.time()
    # ---------------- vacuum component -------------------------------------------------
    codes = sector_states(T, (0, 0, 0))
    inv, sizes, nf = split_components(T, codes)
    big = int(np.argmax(sizes))
    vac = Component(T, codes[inv == big])
    res["vac_sector_states"], res["vac_component"], res["vac_ncomp"] = int(len(codes)), vac.n, int(len(sizes))
    print(f"--- {tag}: zero-winding sector {len(codes)} states, {len(sizes)} components, vacuum component {vac.n}", flush=True)
    tr_ok = True
    for a in range(3):
        img = np.sort(translate_codes(T, vac.codes, a))
        tr_ok &= bool(np.array_equal(img, vac.codes))
    check(f"{tag}: vacuum component is mapped onto itself by the three unit translations", tr_ok)
    # ---------------- source directions ------------------------------------------------
    qs = momenta(T)
    labels, C = [], []
    for q in qs:
        for o in range(3):
            for k, v in enumerate(fourier_dirs(T, q, o)):
                labels.append((q, o, k))
                C.append(v)
    rng = np.random.default_rng(7)
    ngauge = 3
    for _ in range(ngauge):
        g = T.d1 @ rng.normal(size=T.nl)
        C.append(g / np.linalg.norm(g))
    eps = (-1.0) ** T.proot.sum(1) if all(L % 2 == 0 for L in dims) else None
    if eps is not None:
        st = np.where(T.pori == 0, eps, 0.0)
        C.append(st / np.linalg.norm(st))
    C = np.array(C)
    res["V"] = {}
    for V in VS:
        tv = time.time()
        gr = vac.ground(V)
        R, info = vac.hessian(V, C, ground=gr)
        nlab = len(labels)
        Rg = R[nlab:nlab + ngauge]
        gauge_res = float(np.abs(Rg).max())
        # momentum blocks
        blocks, offblock = {}, 0.0
        for i, (qi, oi, ki) in enumerate(labels):
            for j, (qj, oj, kj) in enumerate(labels):
                if qi != qj:
                    offblock = max(offblock, abs(R[i, j]))
        rows = []
        for q in qs:
            idx = [i for i, l in enumerate(labels) if l[0] == q]
            ev = np.linalg.eigvalsh(R[np.ix_(idx, idx)])
            rows.append(dict(q_over_pi=[round(x / np.pi, 6) for x in q], n=len(idx), ev=ev.tolist()))
        chi = [R[i, i] for i, l in enumerate(labels) if l[0] == (0.0, 0.0, 0.0)]
        rec = dict(E0=info["E0"], gap=info["gap"], cg_its=info["cg_its"], cg_res=float(info["cg_res"]),
                   chi_orient=chi, blocks=rows, gauge_res=gauge_res, offblock=offblock)
        if eps is not None:
            rec["chi_stag_xy"] = float(R[-1, -1])
        res["V"][V] = rec
        print(f"  V={V:+.2f} E0={info['E0']:.9f} gap={info['gap']:.6f} cg_its={info['cg_its']} res={info['cg_res']:.1e} "
              f"|R.exact|={gauge_res:.1e} |R(q,q')|={offblock:.1e} chi(o=0,1,2)={np.round(chi, 9).tolist()} ({time.time()-tv:.0f}s)", flush=True)
        for r in rows:
            print(f"     q/pi={r['q_over_pi']} eig={np.round(r['ev'], 9).tolist()}", flush=True)
    # ---------------- winding sectors --------------------------------------------------
    res["sectors"] = {}
    for a in (0, 2):
        for Wm in range(0, int(T.wsize[a]) + 1, 2):
            W = [0, 0, 0]
            W[a] = Wm
            tw = time.time()
            sg = sector_ground(T, tuple(W), VS)
            if sg is None:
                continue
            res["sectors"][str(tuple(W))] = sg
            print(f"  sector W={tuple(W)} states={sg['n_states']} comps={sg['n_comp']} largest={sg['largest']} "
                  + " ".join(f"E({V:+.1f})={sg['E'][V]:.9f}[c{sg['comp_of_min'][V]}]" for V in VS) + f" ({time.time()-tw:.0f}s)", flush=True)
    res["time"] = time.time() - t
    return T, vac, res


# ======================================================================================
print("B6 exact ED of the supplied ring model; J = 1; V list", VS, flush=True)

# (0) Gauss-state counts vs landed exhaustive enumeration (zero-winding note 2026-10-01).
for dims, tot_exp, zero_exp in [((2, 2, 2), 9600, 880), ((2, 2, 4), 23063296, 1552024)]:
    T = Torus(dims)
    mw = int(T.wsize.max())
    h = dfs_count_sectors(T.nl, T.nv, T.tail, T.head, np.full(T.nv, 6, np.int64), T.wmask, T.wsize, mw)
    z = int(h[mw // 2, mw // 2, mw // 2])
    check(f"{'x'.join(map(str, dims))}: Gauss states {tot_exp}, zero-winding {zero_exp} (landed note, independent enumerator)",
          int(h.sum()) == tot_exp and z == zero_exp, f"got {int(h.sum())}, {z}")
    OUT[f"gauss_{dims}"] = dict(total=int(h.sum()), zero=z, nsectors=int((h > 0).sum()))

for dims in [(2, 2, 2), (2, 2, 3), (2, 2, 4)]:
    T, vac, res = run_size(dims)
    OUT["x".join(map(str, dims))] = res
    tag = "x".join(map(str, dims))
    allV = res["V"].values()
    check(f"{tag}: Hessian annihilates exact 2-forms (gauge) at every V", max(r["gauge_res"] for r in allV) < 1e-9,
          f"max {max(r['gauge_res'] for r in allV):.1e}")
    check(f"{tag}: Hessian is block diagonal in lattice momentum (translation invariance) at every V",
          max(r["offblock"] for r in allV) < 1e-9, f"max {max(r['offblock'] for r in allV):.1e}")
    rk_ok = all(abs(sg["E"][1.0]) < 1e-10 for sg in res["sectors"].values())
    check(f"{tag}: at RK (V=J) every computed winding sector has ground energy 0 (graph Laplacian)", rk_ok)
    # rank-one co-exact structure at q != 0
    rank_ok = True
    for r in allV:
        for b in r["blocks"]:
            if any(abs(x) > 1e-12 for x in b["q_over_pi"]):
                ev = np.array(b["ev"])
                nnz = int((np.abs(ev) > 1e-8).sum())
                ncos = b["n"] // 3
                rank_ok &= (nnz == ncos) and np.allclose(ev[ev > 1e-8], ev[ev > 1e-8][0], atol=1e-9)
    check(f"{tag}: at every q != 0 the 3-orientation block has exactly one nonzero (co-exact) value per real Fourier pair", rank_ok)
    if dims == (2, 2, 2):
        r1 = res["V"][1.0]
        check("2x2x2 V=1: uniform Cartesian chi_2 = 0.285050028242 (source note / probe)", abs(r1["chi_orient"][0] - 0.285050028242) < 1e-11,
              f"{r1['chi_orient'][0]:.12f}")
        check("2x2x2 V=1: occupation-sign (staggered xy) curvature = 0.105121402155 (source note / probe)",
              abs(r1["chi_stag_xy"] - 0.105121402155) < 1e-11, f"{r1['chi_stag_xy']:.12f}")
        ok = True
        for V, r in res["V"].items():
            KQ = max(b["ev"][-1] for b in r["blocks"] if b["q_over_pi"] == [1.0, 1.0, 1.0])
            ok &= abs(r["chi_stag_xy"] - KQ / 3) < 1e-10
        check("2x2x2: occupation-sign curvature = K_T(pi,pi,pi)/3 at every V (probe identity)", ok)
        r0 = res["sectors"]
        ok = (abs(r0["(0, 0, 0)"]["E"][0.0] + 9.026721) < 5e-7 and abs(r0["(2, 0, 0)"]["E"][0.0] + 7.399111) < 5e-7
              and abs(r0["(4, 0, 0)"]["E"][0.0] + 4 * np.sqrt(2)) < 1e-9)
        check("2x2x2 V=0: sector ground energies -9.026721, -7.399111, -4 sqrt2 (landed electric-coupling note, Diagnostic 1)", ok,
              f"{r0['(0, 0, 0)']['E'][0.0]:.9f} {r0['(2, 0, 0)']['E'][0.0]:.9f} {r0['(4, 0, 0)']['E'][0.0]:.9f}")
        check("2x2x2: W=(4,0,0) sector has 56 states = frozen seed + 55 others (landed note, Diagnostic 1)",
              r0["(4, 0, 0)"]["n_states"] == 56, f"{r0['(4, 0, 0)']['n_states']} states, min in component of size {r0['(4, 0, 0)']['comp_of_min'][0.0]}")
    if dims == (2, 2, 4):
        check("2x2x4: vacuum component has 1551976 states (landed note)", vac.n == 1551976, f"{vac.n}")
        # finite-difference check of K_T at the smallest momentum along z, V = 0.5
        V = 0.5
        q = (0.0, 0.0, np.pi / 2)
        dirs = [v for o in range(3) for v in fourier_dirs(T, q, o)]
        Cq = np.array(dirs)
        gr = vac.ground(V)
        Rq, info = vac.hessian(V, Cq, ground=gr)
        w, U = np.linalg.eigh(Rq)
        c = Cq.T @ U[:, -1]
        th = [0.02, 0.01]
        Ep = {h: vac.energy_with_source(V, h * c) for h in th}
        Em = {h: vac.energy_with_source(V, -h * c) for h in th}
        fd = {h: (Ep[h] + Em[h] - 2 * gr[0]) / h ** 2 for h in th}
        rich = (4 * fd[0.01] - fd[0.02]) / 3
        check("2x2x4 V=0.5: Richardson finite difference of E0(theta c) along the co-exact q=(0,0,pi/2) mode matches K_T",
              abs(rich - w[-1]) < 2e-5 * abs(w[-1]), f"FD {rich:.8f} vs linear response {w[-1]:.8f}")
        OUT["fd_check"] = dict(V=V, fd=fd, rich=rich, KT=float(w[-1]))

for k in ("2x2x2", "2x2x3", "2x2x4"):
    low = [(W, sg["E"][V] - OUT[k]["V"][V]["E0"]) for W, sg in OUT[k]["sectors"].items() for V in VS if V < 1 and sg["E"][V] < OUT[k]["V"][V]["E0"] - 1e-9]
    print(f"INFO {k}: winding sectors below the zero-winding vacuum component for some V<1: {low if low else 'none'}", flush=True)


def _conv(o):
    if isinstance(o, dict):
        return {str(k): _conv(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_conv(v) for v in o]
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    return o


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "b6_exact_ed_results.json"), "w") as f:
    json.dump(_conv(OUT), f, indent=1)
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES) - sum(RES)}  ({time.time() - T0:.0f}s)", flush=True)
sys.exit(0 if all(RES) else 1)
