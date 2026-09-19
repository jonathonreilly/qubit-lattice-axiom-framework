#!/usr/bin/env python3
"""J:note falsifiers for U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03 (on main).

Falsifiers implemented: "a layer fails to commute with any displayed Gauss generator"; "the palindromic tick is not reversible or
Gauss-preserving"; "its flow and simple-energy errors fail the cubic ladder"; "the Floquet generator is not Hermitian, conserved, or
Gauss-preserving"; "its deviation, BCH residual, or correlated entries fail their stated refinement orders"; "either removal control
retains the correlated effect".

Independent construction for any planar complex of square faces with spin-one quantum links (E|m> = m|m>, U|m> = |m+1>, U|1> = 0),
one charged particle on the two ends of a designated hop link, H_E = (g^2/2) sum E^2, H_hop = -t (U_hop (x) |head><tail| + h.c.),
H_B = -(kappa/2) sum_f (P_f + P_f^dag), Gauss G_v = sum_in E - sum_out E - n_v, A = H_E + H_hop, B = H_B,
U_S(h) = exp(-ihA/2) exp(-ihB) exp(-ihA/2), Floquet H_F = (i/h) log U_S (complex Schur form, principal branch).
  - the note's single face (3^4 x 2 = 162, all sectors);
  - beyond it: a two-face strip (7 links, 3^7 x 2 = 4374 states; the hop on the SHARED link, so the charge sits between two
    circulating faces): layer-Gauss commutators on the full space (sparse), the Floquet analysis on the union of the invariant sectors
    reachable from every state with at most one nonzero link;
checked at h = 0.2, 0.1, 0.05: Hermiticity, [H_F, U_S] = 0, Gauss invariance, U_S^dag U_S = I and time reversal U_S(h) U_S(-h) = I,
flow error ||U_S - exp(-ih(A+B))|| (cubic), simple-energy error ||U_S^dag (A+B) U_S - (A+B)|| (cubic), deviation ||H_F - (A+B)||
(quadratic), BCH residual ||H_F - A - B - (h^2/24)([A,[A,B]] + 2[B,[A,B]])|| (quartic), and the correlated entries of H_F - (A+B)
(matter moved AND a non-hop link changed; quadratic), which must vanish when t = 0 or kappa = 0.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.linalg import schur
from scipy.sparse import lil_matrix, diags

G2, T, KAPPA = 1.3, 0.8, 0.9


class Model:
    def __init__(self, n_links, faces, hop, tail, head, n_vertices, links_ends, g2=G2, t=T, kappa=KAPPA):
        self.nl = n_links
        self.states = list(itertools.product((-1, 0, 1), repeat=n_links))
        self.basis = [(s, m) for s in self.states for m in (0, 1)]      # m = 0: charge at tail, 1: at head
        self.idx = {b: i for i, b in enumerate(self.basis)}
        self.faces, self.hop, self.tail, self.head = faces, hop, tail, head
        self.nv, self.ends = n_vertices, links_ends
        self.g2, self.t, self.kappa = g2, t, kappa

    def ops(self):
        n = len(self.basis)
        HE = lil_matrix((n, n))
        Hhop = lil_matrix((n, n))
        HB = lil_matrix((n, n))
        for i, (s, m) in enumerate(self.basis):
            HE[i, i] = self.g2 / 2 * sum(x * x for x in s)
            if m == 0 and s[self.hop] < 1:                     # U_hop (x) |head><tail|
                s2 = list(s)
                s2[self.hop] += 1
                j = self.idx[(tuple(s2), 1)]
                Hhop[j, i] += -self.t
                Hhop[i, j] += -self.t
            for face in self.faces:                              # P = prod U (along) U^dag (against)
                s2 = list(s)
                ok = True
                for link, sign in face:
                    s2[link] += sign
                    if abs(s2[link]) > 1:
                        ok = False
                        break
                if ok:
                    j = self.idx[(tuple(s2), m)]
                    HB[j, i] += -self.kappa / 2
                    HB[i, j] += -self.kappa / 2
        gauss = []
        for v in range(self.nv):
            Gv = np.zeros(n)
            for i, (s, m) in enumerate(self.basis):
                val = 0
                for link, (a, b) in enumerate(self.ends):
                    if b == v:
                        val += s[link]
                    if a == v:
                        val -= s[link]
                val -= (1 if (m == 0 and v == self.tail) or (m == 1 and v == self.head) else 0)
                Gv[i] = val
            gauss.append(Gv)
        return (HE + Hhop).tocsr(), HB.tocsr(), gauss

    def sector(self, A, B, starts):
        adj = (abs(A) + abs(B)).tocsc()
        seen, stack = set(starts), list(starts)
        while stack:
            i = stack.pop()
            for j in adj.indices[adj.indptr[i]:adj.indptr[i + 1]]:
                if j not in seen:
                    seen.add(int(j))
                    stack.append(int(j))
        return sorted(seen)


def herm_exp(H, h):
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * h * w)) @ V.conj().T


def floquet(A, B, h):
    U = herm_exp(A, h / 2) @ herm_exp(B, h) @ herm_exp(A, h / 2)
    Tm, Z = schur(U, output="complex")
    phases = np.angle(np.diag(Tm))
    HF = (Z * (-phases / h)) @ Z.conj().T
    return U, HF


def correlated_mask(model, keep, hop):
    basis = [model.basis[i] for i in keep]
    n = len(basis)
    M = np.zeros((n, n), bool)
    for a, (s, m) in enumerate(basis):
        for b, (s2, m2) in enumerate(basis):
            if m != m2 and any(s[l] != s2[l] for l in range(model.nl) if l != hop):
                M[a, b] = True
    return M


def analyse(name, model, restrict, hs=(0.2, 0.1, 0.05)):
    As, Bs, gauss_full = model.ops()
    gauss_layers = max(abs(diags(g) @ X - X @ diags(g)).max() for g in gauss_full for X in (As, Bs))   # full space, sparse
    if restrict:
        starts = [model.idx[b] for b in model.basis if sum(1 for x in b[0] if x != 0) <= 1]
        keep = model.sector(As, Bs, starts)
    else:
        keep = list(range(len(model.basis)))
    A, B = As[keep][:, keep].toarray(), Bs[keep][:, keep].toarray()
    gauss = [g[keep] for g in gauss_full]
    mask = correlated_mask(model, keep, model.hop)
    rows = []
    for h in hs:
        U, HF = floquet(A, B, h)
        comm = A @ B - B @ A
        bch = A + B + h * h / 24 * (A @ comm - comm @ A + 2 * (B @ comm - comm @ B))
        dev = HF - (A + B)
        Uex = herm_exp(A + B, h)
        Um, _ = floquet(A, B, -h)
        rows.append({
            "h": h,
            "herm": np.abs(HF - HF.conj().T).max(),
            "conserved": np.abs(HF @ U - U @ HF).max(),
            "gaussF": max(np.abs(np.diag(g) @ HF - HF @ np.diag(g)).max() for g in gauss),
            "unitary": np.abs(U.conj().T @ U - np.eye(len(keep))).max(),
            "reverse": np.abs(U @ Um - np.eye(len(keep))).max(),
            "flow": np.abs(U - Uex).max(),
            "energy": np.abs(U.conj().T @ (A + B) @ U - (A + B)).max(),
            "dev": np.abs(dev).max(),
            "bch": np.abs(HF - bch).max(),
            "corr": np.abs(dev[mask]).max() if mask.any() else 0.0,
        })
    ratio = lambda key: [rows[i][key] / rows[i + 1][key] for i in range(len(rows) - 1)]
    out = {"dim": len(keep), "gauss_layers": gauss_layers, "rows": rows, "flow_ratio": ratio("flow"), "energy_ratio": ratio("energy"),
           "dev_ratio": ratio("dev"), "bch_ratio": ratio("bch"), "corr_ratio": ratio("corr")}
    # removal controls at h = 0.1
    for label, kw in (("t=0", {"t": 0.0}), ("kappa=0", {"kappa": 0.0})):
        m2 = Model(model.nl, model.faces, model.hop, model.tail, model.head, model.nv, model.ends, **{**{"g2": G2, "t": T, "kappa": KAPPA}, **kw})
        A2s, B2s, _ = m2.ops()
        A2, B2 = A2s[keep][:, keep].toarray(), B2s[keep][:, keep].toarray()
        _, HF2 = floquet(A2, B2, 0.1)
        out[label] = np.abs((HF2 - A2 - B2)[mask]).max() if mask.any() else 0.0
    return out


def main():
    # single face: e0: 0->1, e1: 1->2, e2: 3->2, e3: 0->3; P = U0 U1 U2^dag U3^dag; hop on e0 (tail 0, head 1)
    face = Model(4, [[(0, 1), (1, 1), (2, -1), (3, -1)]], hop=0, tail=0, head=1, n_vertices=4, links_ends=[(0, 1), (1, 2), (3, 2), (0, 3)])
    # strip: vertices (x, y) -> 3y + x; links 0: h(0,0) 0->1, 1: h(1,0) 1->2, 2: h(0,1) 3->4, 3: h(1,1) 4->5, 4: v0 0->3, 5: v1 1->4,
    # 6: v2 2->5; faces: [h00, v1, h01^dag, v0^dag], [h10, v2, h11^dag, v1^dag]; hop on the shared v1 (tail 1, head 4)
    strip = Model(7, [[(0, 1), (5, 1), (2, -1), (4, -1)], [(1, 1), (6, 1), (3, -1), (5, -1)]], hop=5, tail=1, head=4, n_vertices=6,
                  links_ends=[(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)])
    fails = []
    for name, mdl, restrict in (("single face (full 162-dim block)", face, False), ("two-face strip, hop on the shared link (sectors reachable from all states with at most one nonzero link)", strip, True)):
        r = analyse(name, mdl, restrict)
        last = r["rows"][-1]
        print(f"{name}: dim {r['dim']}; layer-Gauss commutators {r['gauss_layers']:.1e}; at h = 0.05: Hermitian {last['herm']:.1e}, "
              f"[H_F,U_S] {last['conserved']:.1e}, Gauss {last['gaussF']:.1e}, unitary {last['unitary']:.1e}, reversal {last['reverse']:.1e}; "
              f"refinement ratios per halving of h: flow {[round(x, 2) for x in r['flow_ratio']]}, simple energy "
              f"{[round(x, 2) for x in r['energy_ratio']]}, deviation {[round(x, 2) for x in r['dev_ratio']]}, BCH residual "
              f"{[round(x, 2) for x in r['bch_ratio']]}, correlated entries {[round(x, 2) for x in r['corr_ratio']]} (size at h = 0.05: "
              f"{last['corr']:.2e}); removal controls: t = 0 -> {r['t=0']:.1e}, kappa = 0 -> {r['kappa=0']:.1e}")
        checks = (r["gauss_layers"] < 1e-12 and last["herm"] < 1e-9 and last["conserved"] < 1e-9 and last["gaussF"] < 1e-9
                  and last["unitary"] < 1e-10 and last["reverse"] < 1e-10 and all(6 < x < 10 for x in r["flow_ratio"])
                  and all(6 < x < 10 for x in r["energy_ratio"]) and all(3 < x < 5 for x in r["dev_ratio"])
                  and all(12 < x < 20 for x in r["bch_ratio"]) and all(3 < x < 5 for x in r["corr_ratio"]) and last["corr"] > 1e-8
                  and r["t=0"] < 1e-12 and r["kappa=0"] < 1e-12)
        if not checks:
            fails.append(name)
    if fails:
        print(f"HIT: a refinement order or invariance fails on: {fails}")
    print(f"SUMMARY: with an independent construction the note's single face reproduces every listed property, and beyond it the "
          f"two-face strip with the charge on the shared link behaves the same way: layers commute with all Gauss generators, the "
          f"palindromic tick is unitary, reversible and Gauss-preserving, flow and simple-energy errors are cubic, the Floquet generator is "
          f"Hermitian, conserved and Gauss-preserving with quadratic deviation, quartic BCH residual and quadratic correlated charge-face "
          f"entries that vanish when t = 0 or kappa = 0 ({not fails})")


if __name__ == "__main__":
    main()
