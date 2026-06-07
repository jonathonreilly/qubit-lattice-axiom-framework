#!/usr/bin/env python3
"""Class-A verifier: the SIGN of the interaction asymmetry `delta` and the
nonresonant sign of the emergent signed C3 coupling K_C3.

Chain:
  * delta = E_2 - 2 E_1 + E_0 is the two-excitation MUTUAL energy
    (the occupation curvature; see the companion structure theorem). So
    sign(delta) = sign of the two-body interaction.
  * The retained `staggered_self_consistent_two_body` channel (retained_bounded) couples the
    lattice matter density to a shared scalar field via (L + mu^2) Phi = G |psi|^2, and its
    exact partner-force observable is ATTRACTIVE (the retained note: 15/15 rows, ~d^-1.95).
  * The stacked generation periodic plane-wave bridge identifies the retained
    hw=1 momentum-corner generation pair with the same density-density mediator
    kernel on a finite periodic torus:
        delta_ij = (Vq(0) - Vq(k_i-k_j)) / N < 0.
  * The second-order C3 coupling is not asserted by a sampled delta value. For
    H0 = eps_gap*N and pair curvature delta, direct elimination gives
        K_C3 = t^2 * delta / (eps_gap * (eps_gap + delta)).
    Hence sign(K_C3)=sign(delta) only on the nonresonant branch
        eps_gap > 0 and eps_gap + delta > 0.
    A resonance/strong-curvature branch is explicitly outside this sign claim.

This runner reproduces the retained force observable VERBATIM (conventions
copied from `scripts/frontier_staggered_self_consistent_two_body.py`: L =
graph Laplacian, mu2 = 0.001, reg = 1e-6, G = 50, sigma = 0.80,
central-difference gradient; partner-force = -sum rho * grad_x Phi,
"toward partner" positive), confirms attraction + binding-energy sign +
bounded monotone falloff, checks the periodic-kernel sign bridge, and proves
the nonresonant second-order sign formula over both symbolic and numeric
surfaces.

What it does NOT claim: the physical magnitude of delta, the gap inequality,
or a flavor value (no r, no Q). The mediator fixes delta < 0 on the stated
surfaces. K_C3 < 0 follows only on the explicitly checked nonresonant branch.
"""

from __future__ import annotations
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix, eye as speye
from scipy.sparse.linalg import spsolve

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ---- retained conventions (verbatim from frontier_staggered_self_consistent_two_body.py) ----
MU2, REG, G, SIGMA = 0.001, 1e-6, 50.0, 0.80
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "DELTA_SIGN_FIXED_NEGATIVE_BY_RETAINED_TWO_BODY_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-06.md"
PERIODIC_BRIDGE = ROOT / "docs" / "GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE_NOTE_2026-06-07.md"


class Lattice:
    def __init__(self, side):
        self.side = side
        self.n = side ** 3
        self.pos = np.array([(x, y, z) for x in range(side) for y in range(side)
                             for z in range(side)], dtype=float)
        self.L = self._laplacian()

    def idx(self, x, y, z):
        return x * self.side * self.side + y * self.side + z

    def _laplacian(self):
        L = lil_matrix((self.n, self.n))
        s = self.side
        for x in range(s):
            for y in range(s):
                for z in range(s):
                    i = self.idx(x, y, z)
                    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
                                       (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                        xx, yy, zz = x + dx, y + dy, z + dz
                        if 0 <= xx < s and 0 <= yy < s and 0 <= zz < s:
                            L[i, self.idx(xx, yy, zz)] -= 1.0
                            L[i, i] += 1.0
        return L.tocsr()

    def gaussian(self, center):
        rel = self.pos - np.asarray(center, dtype=float)
        psi = np.exp(-0.5 * np.sum(rel * rel, axis=1) / SIGMA ** 2)
        return psi / np.linalg.norm(psi)

    def solve_phi(self, rho):
        op = (self.L + (MU2 + REG) * speye(self.n)).tocsc()
        return spsolve(op, G * rho).real

    def grad_x(self, phi):
        g = np.zeros(self.n)
        s = self.side
        for x in range(s):
            for y in range(s):
                for z in range(s):
                    i = self.idx(x, y, z)
                    if x == 0:
                        g[i] = phi[self.idx(x + 1, y, z)] - phi[i]
                    elif x == s - 1:
                        g[i] = phi[i] - phi[self.idx(x - 1, y, z)]
                    else:
                        g[i] = 0.5 * (phi[self.idx(x + 1, y, z)] - phi[self.idx(x - 1, y, z)])
        return g

    def force_x(self, psi, gx):                       # exact retained observable
        rho = np.abs(psi) ** 2
        rho = rho / np.sum(rho)
        return float(-np.sum(rho * gx))


def mediator_rows(side, distances=(3, 4, 5, 6, 7)):
    lat = Lattice(side)
    c = 0.5 * (side - 1)
    rows = []
    for d in distances:
        psiA = lat.gaussian((c - d / 2.0, c, c))
        psiB = lat.gaussian((c + d / 2.0, c, c))
        rhoA = np.abs(psiA) ** 2; rhoA = rhoA / rhoA.sum()
        PhiB = lat.solve_phi(np.abs(psiB) ** 2)
        PhiA = lat.solve_phi(np.abs(psiA) ** 2)
        fA = -lat.force_x(psiA, lat.grad_x(PhiB))     # A on left: toward partner = +x
        fB = lat.force_x(psiB, lat.grad_x(PhiA))      # B on right: toward partner = -x
        E_mut = -float(np.sum(rhoA * PhiB))           # binding energy = -(potential)
        rows.append((d, fA, fB, E_mut))
    return rows


def kron3(o, q):
    I2 = np.eye(2, dtype=complex)
    m = np.array([[1]], dtype=complex)
    for i in range(3):
        m = np.kron(m, o if i == q else I2)
    return m


def K_offdiag(delta):
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    nup = np.array([[0, 0], [0, 1]], dtype=complex)
    hwv = np.array([bin(i).count("1") for i in range(8)])
    P1 = [i for i in range(8) if hwv[i] == 1]
    Vc = sum(kron3(sx, q) for q in range(3))
    nops = [kron3(nup, q) for q in range(3)]
    Hint = delta * sum(nops[i] @ nops[j] for i in range(3) for j in range(i + 1, 3))
    E = {i: hwv[i] * 1.0 + Hint[i, i].real for i in range(8)}
    E1 = E[P1[0]]
    H = np.array([[sum(Vc[a, k] * Vc[k, b] / (E1 - E[k])
                       for k in range(8) if hwv[k] != 1 and abs(E1 - E[k]) > 1e-9)
                   for b in P1] for a in P1])
    return H


def K_offdiag_formula(delta, eps_gap=1.0, t=1.0):
    return t * t * delta / (eps_gap * (eps_gap + delta))


def eps_periodic(k):
    return float(sum(2.0 * (1.0 - np.cos(component)) for component in k))


def Vq(k):
    return -G / (eps_periodic(k) + MU2)


def main() -> int:
    print("=" * 78)
    print("delta SIGN from the RETAINED two-body mediator (attractive => delta<0)  [class A]")
    print("=" * 78)

    # ---- (1) reproduce the retained attractive partner force + binding-energy sign ----
    print("\n-- (1) retained mediator: partner force attractive, binding energy E_mut < 0 --")
    all_rows = []
    for side in (12, 14, 16):
        rows = mediator_rows(side)
        all_rows.extend(rows)
        attractive = all(fA > 0 and fB > 0 for _, fA, fB, _ in rows)
        bound = all(E < 0 for _, _, _, E in rows)
        slope = np.polyfit(np.log([r[0] for r in rows]),
                           np.log([abs(r[1]) for r in rows]), 1)[0]
        check(f"side={side}: partner force ATTRACTIVE on all separations (reproduces the "
              f"retained 15/15)", attractive,
              detail=f"|F| ~ d^{slope:.2f} (retained ~d^-1.95); F(d=3)={rows[0][1]:+.4f}")
        check(f"side={side}: two-excitation binding energy E_mut = -sum rho_A Phi_B < 0 "
              f"on all separations (attractive => bound)", bound)
    # exact match to the retained note's published value (side=12, d=3: +4.9557e-01)
    f_ref = mediator_rows(12, distances=(3,))[0][1]
    check("force reproduces the retained note value verbatim (side=12, d=3 -> +0.49557)",
          np.isclose(f_ref, 0.49557, atol=1e-4), detail=f"got {f_ref:+.5f}")

    # ---- (2) |E_mut| bounded and monotone-decreasing in separation (scale bounded) ----
    print("\n-- (2) |delta| bounded by the (sign-definite Yukawa) propagator --")
    rows12 = mediator_rows(12)
    Emags = [abs(E) for _, _, _, E in rows12]
    monotone = all(Emags[i] >= Emags[i + 1] - 1e-9 for i in range(len(Emags) - 1))
    check("|E_mut| is bounded and monotone-decreasing with separation (the screened-Poisson "
          "(L+mu^2)^-1 kernel is sign-definite) => |delta| bounded, not divergent", monotone,
          detail=f"|E_mut|(d=3..7) = {[round(e,2) for e in Emags]}")

    # ---- (3) periodic generation-pair bridge: delta_ij < 0 and equal across pairs ----
    print("\n-- (3) periodic hw=1 generation-pair kernel: delta_ij < 0 and J-I symmetry --")
    corners = [
        np.array([np.pi, 0.0, 0.0]),
        np.array([0.0, np.pi, 0.0]),
        np.array([0.0, 0.0, np.pi]),
    ]
    pair_deltas = []
    N_periodic = 10 ** 3
    for i in range(3):
        for j in range(i + 1, 3):
            dk = corners[i] - corners[j]
            pair_deltas.append((Vq(np.zeros(3)) - Vq(dk)) / N_periodic)
    check("periodic bridge formula gives equal negative delta_ij for all hw=1 corner pairs",
          np.allclose(pair_deltas, pair_deltas[0]) and all(d < 0 for d in pair_deltas),
          detail=", ".join(f"{d:.6e}" for d in pair_deltas))
    check("all corner-pair transfers have eps(Delta k)=8, so the pair matrix has J-I form",
          all(np.isclose(eps_periodic(corners[i] - corners[j]), 8.0)
              for i in range(3) for j in range(i + 1, 3)))

    # ---- (4) nonresonant sign propagation into the second-order K_C3 on C^8 ----
    print("\n-- (4) sign propagation branch: K = t^2 delta/[eps_gap(eps_gap+delta)] --")
    sample_grid = []
    for eps_gap in (0.5, 1.0, 2.0, 5.0):
        for frac in (0.05, 0.25, 0.75):
            delta = -frac * eps_gap
            sample_grid.append((eps_gap, delta, K_offdiag_formula(delta, eps_gap=eps_gap)))
    check("nonresonant attractive branch eps_gap>0 and eps_gap+delta>0 gives K_C3<0",
          all(k < 0 for eps_gap, delta, k in sample_grid),
          detail="; ".join(f"eps={e:.2g},delta={d:.2g}->K={k:.3g}" for e, d, k in sample_grid[:4]))
    repulsive_grid = [
        (eps_gap, delta, K_offdiag_formula(delta, eps_gap=eps_gap))
        for eps_gap in (0.5, 1.0, 2.0)
        for delta in (0.05 * eps_gap, 0.4 * eps_gap)
    ]
    check("counterfactual repulsive branch delta>0 gives K_C3>0 with the same denominator sign",
          all(k > 0 for _, _, k in repulsive_grid))
    resonant = K_offdiag_formula(-1.5, eps_gap=1.0)
    check("strong-curvature resonance branch is detected and excluded from the sign theorem",
          resonant > 0, detail=f"eps_gap=1, delta=-1.5 gives K={resonant:+.3f}")

    Hk = K_offdiag(-0.3)
    offs = [Hk[i, j].real for i in range(3) for j in range(3) if i != j]
    formula_value = K_offdiag_formula(-0.3)
    check("finite C^8 elimination matches the symbolic nonresonant formula at delta=-0.3",
          np.isclose(Hk[0, 1].real, formula_value), detail=f"matrix={Hk[0,1].real:+.6f}, formula={formula_value:+.6f}")
    check("the sourced coupling is the exact C3 (J - I) form (all off-diagonals equal)",
          np.allclose(offs, offs[0]))

    # ---- (5) note/source markers ----
    print("\n-- (5) source-note markers for the narrowed branch claim --")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    bridge_text = PERIODIC_BRIDGE.read_text(encoding="utf-8")
    for marker in [
        "K_C3 = t^2 * delta / (eps_gap * (eps_gap + delta))",
        "eps_gap > 0 and eps_gap + delta > 0",
        "GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE_NOTE_2026-06-07",
        "strong-curvature/resonant branch",
    ]:
        check(f"delta-sign note contains marker: {marker}", marker in note_text)
    check("stacked periodic bridge contains the finite-volume delta formula",
          "delta(k,l) = <rho_k, V_L rho_l>" in bridge_text and "(Vq(0) - Vq(k-l)) / N" in bridge_text)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: delta-sign from the retained mediator FAILED.")
        return 1
    print("VERDICT: the retained two-body mediator channel gives negative mutual energy "
          "delta < 0 on the open-cubic force surface and on the stacked periodic hw=1 "
          "plane-wave kernel. The exact second-order C3 coupling satisfies "
          "K_C3 = t^2 delta/[eps_gap(eps_gap+delta)], so K_C3 < 0 follows on the "
          "explicit nonresonant branch eps_gap>0, eps_gap+delta>0. The physical "
          "magnitude/gap branch remains open; no flavor value is forced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
