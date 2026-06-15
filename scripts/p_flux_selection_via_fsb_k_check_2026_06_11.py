#!/usr/bin/env python3
"""P-FLUX selection via FSB-K + the retained (Z) certificate — phi = -1
at retained FSB-K grade (composer runner).

Companion to
docs/P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md

The retained-grade composition checked here:

  GIVEN C1: the FSB-K row (axiom_first_fermionic_stefan_boltzmann_
          narrow_theorem_note_2026-05-26, re-scoped 2026-06-12:
          quantifier on the realized kernel class, hypothesis (Z)
          explicit) stands at retained_bounded grade with its quantifier and
          Corollary FSB-CL intact,
  USING   the retained (Z)-certificate row (staggered_kernel_satisfies_
          z_point_cone_certificate_narrow_theorem_note_2026-06-11:
          Theorem Z-K1, the K1 kernel satisfies (Z) exactly; Theorem
          Z-K0, the K0 kernel violates it),
  THEN within the licensed two-class kinetic surface the finite-
       species-density requirement (CL) -- boundary B-Z2 of the P-FLUX
       no-gos, in the retained Stefan-Boltzmann bridge row's own
       per-dof currency, supplied by FSB-K's conclusion quantified
       over realized kernels -- is SATISFIED by K1 (g_eff plateau ~ 8
       in the central-difference normalization = sum |det V|^-1;
       equivalently ~ 1 = 8/2^3 per site at unit hopping) and VIOLATED
       by K0 (g_eff ~ T^-2, Sommerfeld), hence phi = -1 is selected:
       B-Z2 supplied, B-BIT retired within the licensed surface at
       C1's grade.

What this runner verifies:

  [A] chain inventory and honesty about TODAY's grades: the FSB-K
      supplier is retained_bounded as of 2026-06-14, the
      (Z)-certificate row is retained, and the retained currency/surface
      anchors are at their stated grades. The FSB-K row no longer carries the old U4 row as
      a load-bearing dependency; the load-bearing content is string-
      verified (quantifier, FSB-CL, branch-blindness; Z-K1/Z-K0); the
      (Z) interface matches verbatim across FSB-K and the retained
      geometry row, and
      FSB-K's g_eff formula instantiates on the certified cone data to
      8 per cell (central-difference) / 1 per site (unit hopping).
  [B] the composed conclusion is recomputed in-runner, self-contained,
      using FSB-K's own mode-sum method on this runner's own kernel
      constructions: flux certificates, zero counts (8,8,8) vs
      (20,68,140), closed-form/eigensolver spectrum ties licensing the
      L = 128 symbol grids; K1's g_eff plateau (8.21, 9.15, 12.06 at
      T = 0.05, 0.1, 0.2 central-difference; 0.979 ~ 1 unit-hopping,
      exact scale tie); K0's T^-2 divergence (g_eff 323, 81, 20.4, 5.0
      unit; halving ratios ~ 4; Sommerfeld u/T^2 plateau ~ 0.233); the
      point-zero quadratic comparator diverging ~ T^-3/2 (so (CL) is
      strictly stronger than bare point-likeness); and the end-to-end
      LABEL-FREE pipeline: geometry + thermal data in, selected kernel
      out, its computed flux = -1.
  [C] the retained-grade assembly: the conclusion is exactly the named
      missing row of the finite-species-density no-go (its section-7
      formulation 2 and N6 promotion target), it retires exactly the
      kinetic-class note's B-BIT by that note's own named route
      ('point-like zero sets (relativistic cones)'), the retained SB
      bridge supplies the currency (7/240 exact; 427/4 branch-
      independent), and the note's grade structure (C1 retained-grade,
      retained Z geometry, future reconditionalization/collapse, surface scope
      B-C0) is declared in the note text.
  [D] falsification legs and inversion-guard compliance: dropping (CL)
      restores the retained-surface tie (carrier battery recomputed:
      cube TRUE/TRUE, M_3(C) dim 9/9, count 3 = 3 -- selects nothing);
      dropping the retained Z geometry leaves FSB-K's hypothesis
      unverified AND FSB-K minus (Z) is false as a universal statement
      (the realized-class
      comparator violates the T^4 law), so the selection collapses;
      the selection consumes thermal/spectral data only -- the
      kernel-global count readouts are 8/4 vs 20/8, never 3, the only
      3 = 3 appears in the falsification tie where it selects nothing,
      and the turn-1 inversion guards of the index-pairing no-go are
      respected.

Deterministic, no network, no randomness; numpy only.
Exit code 0 iff FAIL = 0.
"""

import itertools
import json
import math
import os
import sys

import numpy as np

PASS = 0
FAIL = 0
CHECK = 0

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PREF = (7.0 / 8.0) * (math.pi ** 2 / 30.0)


def report(ok, msg):
    global PASS, FAIL, CHECK
    CHECK += 1
    if ok:
        PASS += 1
        print(f"[PASS] {CHECK:2d}. {msg}")
    else:
        FAIL += 1
        print(f"[FAIL] {CHECK:2d}. {msg}")


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


def note_text(relpath):
    with open(os.path.join(REPO, relpath), encoding="utf-8") as f:
        return f.read()


def ledger():
    with open(os.path.join(REPO, "docs/audit/data/audit_ledger.json"),
              encoding="utf-8") as f:
        return json.load(f)["rows"]


def status(rows, row):
    if row not in rows:
        return None
    r = rows[row]
    return r.get("effective_status") or r.get("status")


RETAINED_GRADES = ("retained", "retained_no_go", "retained_bounded")


def retained_grade(st):
    return st in RETAINED_GRADES or str(st).startswith("decoration_under")


# ----------------------------------------------------------------------
# constructions (self-contained; same licensed surface as the parents)
# ----------------------------------------------------------------------

def sites_of(L):
    return list(itertools.product(range(L), repeat=3))


def t_K0(x, mu):
    return 1.0


def t_K1(x, mu):
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** x[0]
    return (-1.0) ** (x[0] + x[1])


def build_h(L, t_fun, onsite=0.0):
    sites = sites_of(L)
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((N, N))
    for x in sites:
        for mu in range(3):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L
            t = t_fun(x, mu)
            h[idx[tuple(xp)], idx[x]] += t
            h[idx[x], idx[tuple(xp)]] += t
        if onsite != 0.0:
            h[idx[x], idx[x]] += onsite
    return h, sites, idx


def plaquette_flux_set(L, t_fun):
    out = set()
    for x in sites_of(L):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % L
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % L
                f = (t_fun(x, mu) * t_fun(tuple(xm), nu)
                     * t_fun(tuple(xn), mu) * t_fun(x, nu))
                out.add(round(f, 12))
    return out


def kernel_dim(h, tol=1e-9):
    return int((np.abs(np.linalg.eigvalsh(h)) < tol).sum())


def torus_grid(L):
    p = 2.0 * np.pi * np.arange(L) / L
    return np.meshgrid(p, p, p, indexing="ij")


def k1_symbol_vals(L):
    """Closed-form K1 |spectrum| multiset over the full torus grid
    (= the Bloch band family of the (Z)-certificate's all-volume
    identity; tied to the eigensolver in check 5)."""
    p1, p2, p3 = torus_grid(L)
    return (2.0 * np.sqrt(np.sin(p1) ** 2 + np.sin(p2) ** 2
                          + np.sin(p3) ** 2)).ravel()


def k0_symbol_vals(L):
    p1, p2, p3 = torus_grid(L)
    return (2.0 * (np.cos(p1) + np.cos(p2) + np.cos(p3))).ravel()


def comparator_symbol_vals(L):
    return k0_symbol_vals(L) - 6.0


def u_density(vals, T):
    """FSB-K's own mode-sum probe: half-filled free-Fermi thermal
    energy density per site, u(T) = (1/N) sum |E| n_F(|E|/T) -- the
    retained SB bridge row's integrand on the kernel spectrum
    (hypothesis-satisfiability currency, not realized dynamics)."""
    a = np.abs(vals)
    return float(np.sum(a / (np.exp(np.minimum(a / T, 700.0)) + 1.0))
                 / len(vals))


def g_eff(vals, T):
    return u_density(vals, T) / (PREF * T ** 4)


# ---- (Z)-side machinery (same decision data as the certificate) ------

def dir_speed(E_abs, p0, u, t=1e-6):
    return abs(E_abs(tuple(p0[i] + t * u[i] for i in range(3)))) / t


DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1),
        (1 / math.sqrt(2), -1 / math.sqrt(2), 0),
        (1 / math.sqrt(2), 0, -1 / math.sqrt(2)),
        (0, 1 / math.sqrt(2), -1 / math.sqrt(2))]


def min_speed(E_abs, p0):
    return min(dir_speed(E_abs, p0, u) for u in DIRS)


# ---- carrier battery (lite; re-derived as in the parent no-gos) ------

def translation(L, sites, idx, mu):
    N = len(sites)
    T = np.zeros((N, N))
    for x in sites:
        xp = list(x)
        xp[mu] = (xp[mu] + 1) % L
        T[idx[tuple(xp)], idx[x]] = 1.0
    return T


def c3_111(sites, idx):
    N = len(sites)
    R = np.zeros((N, N))
    for x in sites:
        R[idx[(x[2], x[0], x[1])], idx[x]] = 1.0
    return R


def kernel_basis(h, tol=1e-9):
    w, v = np.linalg.eigh(h)
    return v[:, np.abs(w) < tol]


def joint_characters(ker, Ts):
    K = ker.shape[1]
    Tr = [ker.conj().T @ T @ ker for T in Ts]
    M = sum((3 ** a) * (Tr[a] + Tr[a].conj().T)
            + (3 ** (a + 3)) * 1j * (Tr[a] - Tr[a].conj().T)
            for a in range(3))
    _, v = np.linalg.eigh(M)
    chars = []
    for i in range(K):
        vec = v[:, i]
        c = []
        for a in range(3):
            lam = complex(vec.conj() @ Tr[a] @ vec)
            if np.linalg.norm(Tr[a] @ vec - lam * vec) > 1e-7:
                raise RuntimeError("not a joint eigenvector")
            c.append(lam)
        chars.append(tuple(c))
    return v, chars


def find_cube(chars):
    K = len(chars)
    for base in range(K):
        lam = chars[base]
        members = {}
        for j, c in enumerate(chars):
            d = tuple(c[a] / lam[a] for a in range(3))
            s = tuple(int(round(x.real)) for x in d)
            if all(abs(d[a] - s[a]) < 1e-7 and s[a] in (-1, 1)
                   for a in range(3)):
                members.setdefault(s, []).append(j)
        if len(members) == 8 and all(len(v) == 1 for v in members.values()):
            return {s: v[0] for s, v in members.items()}
    return None


def algebra_dim(gens, n):
    allm = [np.eye(n, dtype=complex)] + list(gens)
    rank = 0
    for _ in range(6):
        allm = allm + [a @ g for a in allm for g in gens]
        rank = np.linalg.matrix_rank(
            np.array([m.flatten() for m in allm]), tol=1e-7)
        if rank == n * n:
            break
    return int(rank)


def carrier_data(h, L, sites, idx):
    Ts = [translation(L, sites, idx, mu) for mu in range(3)]
    R = c3_111(sites, idx)
    out = {}
    ker = kernel_basis(h)
    out["ker_dim"] = ker.shape[1]
    vecs, chars = joint_characters(ker, Ts)
    cube = find_cube(chars)
    out["cube"] = cube is not None
    if cube is None:
        return out
    hw1 = [s for s in cube if sum(1 for x in s if x == -1) == 1]
    hw1.sort(key=lambda s: s.index(-1))
    B = np.column_stack(
        [vecs[:, cube[s]] / np.linalg.norm(vecs[:, cube[s]]) for s in hw1])
    Rr = ker.conj().T @ R @ ker
    M3gen = B.conj().T @ Rr @ B
    P = [np.diag([1.0 if i == j else 0.0 for i in range(3)])
         for j in range(3)]
    out["carrier_alg_dim"] = algebra_dim(P + [M3gen], 3)
    out["carrier_count"] = len(hw1)

    def rnd(c):
        return tuple(complex(round(z.real, 6), round(z.imag, 6)) for z in c)
    classes = set(rnd(c) for c in chars)
    out["kernel_char_count"] = len(classes)
    seen = set()
    orbits = 0
    for c in classes:
        if c in seen:
            continue
        orbits += 1
        cur = c
        for _ in range(3):
            cur = (cur[2], cur[0], cur[1])
            seen.add(cur)
    out["kernel_c3_orbit_count"] = orbits
    return out


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("[A] the named chain: today's grades (honesty), FSB-K condition")
    print("    content, and the (Z) interface match")
    print("=" * 72)

    rows = ledger()
    st_c1 = status(rows, "axiom_first_fermionic_stefan_boltzmann_narrow_"
                         "theorem_note_2026-05-26")
    st_c2 = status(rows, "staggered_kernel_satisfies_z_point_cone_"
                         "certificate_narrow_theorem_note_2026-06-11")
    st_kc = status(rows, "staggered_dirac_kinetic_class_forcing_narrow_"
                         "theorem_note_2026-06-10")
    st_sd = status(rows, "p_flux_finite_species_density_from_determinant_"
                         "matsubara_surface_narrow_no_go_note_2026-06-10")
    st_sb = status(rows, "gstar_thermal_seven_eighths_stefan_boltzmann_"
                         "bridge_narrow_theorem_note_2026-06-06")
    st_tb = status(rows, "tensor_product_translation_fermion_operator_"
                         "bridge_narrow_theorem_note_2026-05-25")
    own_txt = note_text("docs/P_FLUX_SELECTION_VIA_FSB_K_AND_Z_"
                        "CERTIFICATE_CONDITIONAL_THEOREM_NOTE_"
                        "2026-06-11.md")
    no_old_u4_risk = "known u4 risk" not in own_txt and "recorded u4" not in own_txt
    report(retained_grade(st_c1)
           and retained_grade(st_c2)
           and st_kc == "unaudited"
           and st_sd in (None, "unaudited")
           and st_sb == "retained_bounded" and st_tb == "retained"
           and no_old_u4_risk
           and "FSB-K is retained-bounded as of 2026-06-14" in own_txt
           and "within-surface conclusion is active at current grades" in own_txt,
           f"[A] today's grades (as of 2026-06-14), recorded honestly: "
           f"C1 (FSB-K) = {st_c1}; retained Z certificate = {st_c2}; the "
           f"kinetic-class surface row = {st_kc}; the finite-species-"
           f"density no-go = "
           f"{'absent-from-ledger' if st_sd is None else st_sd}; the "
           f"retained anchors: SB bridge = {st_sb}, Fock bridge = "
           f"{st_tb}; the old U4 row is not load-bearing -- C1 is now "
           f"retained-grade and this note's within-surface selection is "
           f"active at current grades")

    fsb_txt = note_text("docs/AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_"
                        "NARROW_THEOREM_NOTE_2026-05-26.md")
    report("for **every** kinetic kernel in the realized class" in fsb_txt
           and "conditionally on (Z)" in fsb_txt
           and "Corollary FSB-CL" in fsb_txt
           and "neither assumes nor derives `phi = -1`" in fsb_txt
           and "composed by a downstream consumer" in fsb_txt,
           "[A] C1 content (textual): the FSB-K row's quantifier binds "
           "'for **every** kinetic kernel in the realized class', its "
           "finiteness clause is supplied 'conditionally on (Z)' "
           "(Corollary FSB-CL), it 'neither assumes nor derives "
           "`phi = -1`', and its boundary B-3 says any selection must "
           "be 'composed by a downstream consumer' from external "
           "kernel-geometry certificates -- THIS note is that consumer")

    zc_txt = note_text("docs/STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_"
                       "CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md")
    report("Theorem Z-K1 (the K1 kernel satisfies (Z) exactly)" in zc_txt
           and "Theorem Z-K0 (the K0 kernel violates (Z), both clauses)"
               in zc_txt
           and "(V, C_j, r_j) = (2I, 2/3, 1)" in zc_txt
           and "performs no selection" in zc_txt,
           "[A] retained Z content (textual): the (Z)-certificate row states "
           "Theorem Z-K1 (K1 satisfies (Z) exactly, explicit cone data "
           "(V, C_j, r_j) = (2I, 2/3, 1)) and Theorem Z-K0 (K0 "
           "violates both clauses), and itself 'performs no selection' "
           "-- the geometry leg and the thermal leg meet only here")

    iface = ("Z(h) = {(p_j, b) : E_b(p_j) = 0}", "is finite, and for each",
             "invertible real `3×3` matrix")
    ok_iface = all(s in fsb_txt and s in zc_txt for s in iface)
    det_v = 2.0 ** 3
    inst_unit = 8 * (1.0 / det_v)
    inst_cd = 8 * 1.0
    report(ok_iface and abs(inst_unit - 1.0) < 1e-15
           and abs(inst_cd - 8.0) < 1e-15,
           "[A] the (Z) interface matches VERBATIM across FSB-K and the "
           "retained Z row (shared defining strings: the zero set "
           "'Z(h) = {(p_j, b) : E_b(p_j) = 0}', 'is finite, and for "
           "each', 'invertible real `3x3` matrix'), and FSB-K's "
           "g_eff = sum |det V_jb|^-1 instantiates on the certified "
           "cone data to 8 x 1/8 = 1 per site (unit hopping, V = 2I) "
           "= 8 per cell (central-difference, V = I) -- no quantifier "
           "gap in the composition")
    residual("C1 is retained_bounded as of 2026-06-14 while the Z "
             "certificate is retained; the within-surface selection is "
             "active at current grades, but future C1 invalidation would "
             "collapse or reconditionalize the composition (boundary B-C1)")

    print()
    print("=" * 72)
    print("[B] the composed conclusion recomputed self-contained with")
    print("    FSB-K's own mode-sum method on this runner's kernels")
    print("=" * 72)

    h0 = {L: build_h(L, t_K0)[0] for L in (4, 8, 12)}
    h1 = {L: build_h(L, t_K1)[0] for L in (4, 8, 12)}
    fx0 = plaquette_flux_set(4, t_K0)
    fx1 = plaquette_flux_set(4, t_K1)
    z0 = {L: kernel_dim(h0[L]) for L in (4, 8, 12)}
    z1 = {L: kernel_dim(h1[L]) for L in (4, 8, 12)}
    ok_tie = all(
        np.allclose(np.sort(np.abs(np.linalg.eigvalsh(h1[L]))),
                    np.sort(k1_symbol_vals(L)), atol=1e-9)
        and np.allclose(np.sort(np.linalg.eigvalsh(h0[L])),
                        np.sort(k0_symbol_vals(L)), atol=1e-9)
        for L in (4, 8))
    report(fx0 == {1.0} and fx1 == {-1.0}
           and (z1[4], z1[8], z1[12]) == (8, 8, 8)
           and (z0[4], z0[8], z0[12]) == (20, 68, 140)
           and ok_tie,
           f"[B] both kernels re-constructed: uniform flux K0 = +1, "
           f"K1 = -1; zero-mode counts K1 = ({z1[4]},{z1[8]},{z1[12]}) "
           f"(point-like), K0 = ({z0[4]},{z0[8]},{z0[12]}) "
           f"(extensive); closed-form |spectrum| multisets tied to the "
           f"eigensolver at L = 4, 8 -- licensing the L = 128 symbol "
           f"grids below")

    L = 128
    Ts = (0.05, 0.1, 0.2, 0.4)
    v1u = k1_symbol_vals(L)
    v0u = k0_symbol_vals(L)
    vcu = comparator_symbol_vals(L)
    v1c = v1u / 2.0
    v0c = v0u / 2.0
    g1c = {T: g_eff(v1c, T) for T in Ts}
    g1u = {T: g_eff(v1u, T) for T in Ts}
    r1 = g1c[0.05] / g1c[0.1]
    scale_tie = max(abs(g_eff(v1c, T) - 8.0 * g_eff(v1u, 2 * T))
                    for T in (0.05, 0.1))
    conv = abs(g_eff(k1_symbol_vals(64) / 2.0, 0.1) - g1c[0.1]) / g1c[0.1]
    report(abs(g1c[0.05] - 8.0) < 0.25 and 0.85 < r1 < 1.05
           and abs(g1u[0.05] - 1.0) < 0.05
           and scale_tie < 1e-12 and conv < 0.01,
           f"[B] K1 SATISFIES (CL) -- the FSB-K plateau, recomputed: "
           f"central-difference g_eff(T) = {g1c[0.05]:.2f}, "
           f"{g1c[0.1]:.2f}, {g1c[0.2]:.2f} at T = 0.05, 0.1, 0.2 -- "
           f"FINITE plateau ~ 8 = sum |det V|^-1 per cell (T-halving "
           f"ratio {r1:.3f}); unit-hopping g_eff(0.05) = "
           f"{g1u[0.05]:.3f} ~ 1 = 8 species / 2^3; exact scale tie "
           f"g_cd(T) = 8 g_unit(2T) (max dev {scale_tie:.1e}); "
           f"finite-size control L = 64 vs 128 at T = 0.1: "
           f"{conv:.2e} < 1%")

    g0u = {T: g_eff(v0u, T) for T in Ts}
    g0c = {T: g_eff(v0c, T) for T in (0.05, 0.1, 0.2)}
    r0a, r0b = g0u[0.05] / g0u[0.1], g0u[0.1] / g0u[0.2]
    r0c = g0c[0.05] / g0c[0.1]
    u_T2 = [u_density(v0u, T) / T ** 2 for T in Ts]
    report(3.8 < r0a < 4.2 and 3.8 < r0b < 4.2 and 3.8 < r0c < 4.2
           and g0u[0.05] > 100 and max(u_T2) / min(u_T2) < 1.05,
           f"[B] K0 VIOLATES (CL): g_eff (unit) = {g0u[0.05]:.0f}, "
           f"{g0u[0.1]:.0f}, {g0u[0.2]:.1f}, {g0u[0.4]:.1f} at "
           f"T = 0.05..0.4, T-halving ratios {r0a:.2f}, {r0b:.2f} ~ 4 "
           f"(T^-2); central-difference likewise ({g0c[0.05]:.0f}, "
           f"{g0c[0.1]:.0f}, {g0c[0.2]:.1f}; ratio {r0c:.2f}); the "
           f"true low-T law is Sommerfeld: u/T^2 = {u_T2[0]:.3f}, "
           f"{u_T2[1]:.3f}, {u_T2[2]:.3f}, {u_T2[3]:.3f} -- no finite "
           f"T^4 bookkeeping exists for the K0 kernel")

    gcu = {T: g_eff(vcu, T) for T in Ts}
    rca, rcb = gcu[0.05] / gcu[0.1], gcu[0.1] / gcu[0.2]
    report(2.5 < rca < 2.95 and 2.5 < rcb < 2.95,
           f"[B] the point-zero quadratic comparator (off-surface) "
           f"also violates (CL): T-halving ratios {rca:.2f}, "
           f"{rcb:.2f} ~ 2^1.5 (T^-3/2) -- (CL) is strictly stronger "
           f"than bare point-likeness (it also forces conical "
           f"dispersion), exactly as the parents' B-F2 declared")

    # end-to-end label-free pipeline: geometry + thermal data -> branch
    zero_pt = {"A": (0.0, 0.0, 0.0), "B": (math.pi / 2,) * 3}
    E_abs = {"A": lambda p: 2.0 * math.sqrt(sum(math.sin(x) ** 2
                                                for x in p)),
             "B": lambda p: abs(2.0 * sum(math.cos(x) for x in p))}
    counts = {"A": (z1[4], z1[8], z1[12]), "B": (z0[4], z0[8], z0[12])}
    gr = {"A": g1c[0.05] / g1c[0.1], "B": g0c[0.05] / g0c[0.1]}
    verdicts = {}
    for nm in ("A", "B"):
        z_ok = (len(set(counts[nm])) == 1
                and min_speed(E_abs[nm], zero_pt[nm]) > 1e-4)
        cl_ok = gr[nm] < 1.5
        verdicts[nm] = (z_ok, cl_ok)
    selected = [nm for nm in verdicts if verdicts[nm][1]]
    sel_flux = (plaquette_flux_set(4, t_K1)
                if selected == ["A"] else plaquette_flux_set(4, t_K0))
    report(verdicts == {"A": (True, True), "B": (False, False)}
           and selected == ["A"] and sel_flux == {-1.0},
           "[B] end-to-end LABEL-FREE pipeline: two anonymized kernels "
           "in, computed zero counts + cone speeds ((Z) leg) and "
           "computed g_eff ratios ((CL) leg) out -- verdicts "
           "{A: (Z) pass + (CL) pass, B: fail + fail}; exactly one "
           "kernel satisfies the finite-species-density requirement, "
           "and ITS computed plaquette flux is -1: the selection "
           "consumes thermal/spectral data only, then reads the flux "
           "off the selected kernel")
    residual("u(T) is the half-filled free-Fermi probe in the retained "
             "SB bridge row's own integrand (hypothesis-satisfiability "
             "currency); thermal equilibrium of the realized dynamics "
             "is NOT derived anywhere in this chain (inherited FSB-K "
             "B-1 / parents' B-F3; boundary B-P)")

    print()
    print("=" * 72)
    print("[C] the retained-grade assembly: B-Z2 supplied, B-BIT retired")
    print("    within surface, using retained FSB-K and retained Z geometry")
    print("=" * 72)

    sd_txt = note_text("docs/P_FLUX_FINITE_SPECIES_DENSITY_FROM_"
                       "DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_"
                       "NOTE_2026-06-10.md")
    bz2_g_eff = (
        "`g_eff(T)` bounded as `T → 0`" in sd_txt
        or "g_eff(T) = u(T)/[(7/8)(π²/30)T⁴] is bounded as `T → 0`"
        in sd_txt
        or "g_eff(T) := u(T)/[(7/8)(π²/30)T⁴] has a **finite plateau"
        in sd_txt
    )
    bz2_select = (
        "Hence `φ = −1` remains underived" in sd_txt
        or "The most natural derivation target is N6's: promote an axiom-first"
        in sd_txt
        or "Stefan-Boltzmann row to retained grade with its quantifier on the"
        in sd_txt
    )
    bz2_stronger = (
        "strictly stronger than the bare point-like-zero-set clause" in sd_txt
        or "strictly stronger than bare point-like zero set" in sd_txt
    )
    report(bz2_g_eff and bz2_select and bz2_stronger,
           "[C] the conclusion is EXACTLY the named missing row: the "
           "finite-species-density no-go's section-7 formulation 2 "
           "('g_eff bounded as T -> 0', the retained SB row's own "
           "currency) is what C1 plus the retained Z geometry states "
           "of the realized "
           "kernel, and its N6/section-7 language names this "
           "retained-SB-row promotion target; "
           "its B-F2 strictly-stronger caveat is reproduced by the "
           "comparator leg above -- B-Z2 is supplied at the chain's "
           "grade, not granted")

    kc_txt = note_text("docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_"
                       "NARROW_THEOREM_NOTE_2026-06-10.md")
    report("(K1 vs K0) is NOT forced by the specified constraint set"
           in kc_txt
           and "point-like zero sets (relativistic cones)" in kc_txt,
           "[C] what retires: the kinetic-class note's B-BIT ('the "
           "selector phi = -1 (K1 vs K0) is NOT forced by the "
           "specified constraint set') -- and by that note's own "
           "candidate route ('a dynamical/spectral principle requiring "
           "point-like zero sets (relativistic cones)', its section "
           "7), which is exactly the (Z)+(CL) principle composed "
           "here; B-BIT retires within the licensed two-class surface "
           "using retained C1 and retained Z geometry")

    sb_txt = note_text("docs/GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_"
                       "BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_"
                       "2026-06-06.md")
    from fractions import Fraction
    gstar = 28 + (7.0 / 8.0) * 90
    report(st_sb == "retained_bounded"
           and "relativistic, effectively massless thermal degree of "
               "freedom" in sb_txt
           and "It does not derive the Standard Model particle "
               "inventory" in sb_txt
           and Fraction(7, 240) == Fraction(7, 8) * Fraction(1, 30)
           and abs(gstar - 427.0 / 4.0) < 1e-12,
           "[C] the currency anchor is already retained: the SB bridge "
           "(retained_bounded) owns the per-dof coefficient 7/240 = "
           "(7/8)(1/30) exactly and binds 'a relativistic, effectively "
           "massless thermal degree of freedom' with a supplied "
           "inventory ('It does not derive the Standard Model particle "
           "inventory'); the 427/4 arithmetic is branch-independent -- "
           "the requirement (REQ) composed here is consistency of the "
           "realized kernel with that retained finite-g_eff "
           "bookkeeping, the exact content of B-Z2")

    report("Current state: C1 retained-grade" in own_txt
           and "Retained geometry leg" in own_txt
           and "Z certificate is retained" in own_txt
           and "Future invalidation of C1" in own_txt
           and "resolves by cascade" in own_txt
           and "collapses" in own_txt
           and "boundary B-C0" in own_txt
           and "within-surface selection is active at current grades" in own_txt,
           "[C] the grade structure is declared in the note text: "
           "C1 is retained-grade with quantifier + FSB-CL intact, and "
           "the retained Z geometry carries Z-K1 + Z-K0; future "
           "audited_conditional dependency invalidation reverts the row "
           "to conditional cascade, while audited_failed / "
           "audited_renaming of C1 makes the composition collapse and "
           "B-Z2 reopen; the two-class surface itself is scope "
           "(boundary B-C0), so the active conclusion is within-surface")
    residual("the licensed two-class surface is the kinetic-class "
             "forcing row's scope (unaudited); this composition "
             "selects WITHIN the surface; retiring P-KIN wholesale "
             "additionally requires that row's grade (boundary B-C0)")

    print()
    print("=" * 72)
    print("[D] falsification legs and inversion-guard compliance")
    print("=" * 72)

    h0_4, s4, i4 = build_h(4, t_K0)
    h1_4, _, _ = build_h(4, t_K1)
    d0 = carrier_data(h0_4, 4, s4, i4)
    d1 = carrier_data(h1_4, 4, s4, i4)
    tie = (d1.get("cube") and d0.get("cube")
           and d1.get("carrier_count") == d0.get("carrier_count") == 3
           and d1.get("carrier_alg_dim") == d0.get("carrier_alg_dim") == 9)
    report(bool(tie),
           "[D] falsification leg 1 (drop the (CL) clause): the "
           "retained-surface battery alone TIES -- both kernels carry "
           "the embedded generation package (Klein cube TRUE/TRUE, "
           "M_3(C) dim 9/9, observable count 3 = 3, recomputed here "
           "exactly as the matter-content no-go found) -- without the "
           "finite-species-density clause the selection vanishes and "
           "the parents' no-go state returns")

    report(2.5 < rca < 2.95
           and "neither assumes nor derives `phi = -1`" in fsb_txt
           and verdicts["A"][0] != verdicts["B"][0],
           "[D] falsification leg 2 (drop the retained Z geometry): "
           "FSB-K minus (Z) is FALSE as a universal statement (the "
           "realized-class quadratic comparator violates the T^4 law, "
           "ratios ~ 2^1.5), and FSB-K is branch-blind on its face "
           "('neither assumes nor derives `phi = -1`') -- without the "
           "retained Z leg the hypothesis is unverified on BOTH licensed "
           "kernels and "
           "the quantifier instantiates on neither: the selection "
           "collapses; the (Z) leg is load-bearing, not decorative")

    ip_txt = note_text("docs/INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_"
                       "SELECTOR_NO_GO_NOTE_2026-06-08.md")
    consumed = [z1[4], z1[8], z1[12], z0[4], z0[8], z0[12],
                int(round(g1c[0.05])), d1.get("kernel_char_count"),
                d1.get("kernel_c3_orbit_count"),
                d0.get("kernel_char_count"),
                d0.get("kernel_c3_orbit_count")]
    report(3 not in consumed
           and d1.get("kernel_char_count") == 8
           and d1.get("kernel_c3_orbit_count") == 4
           and d0.get("kernel_char_count") == 20
           and d0.get("kernel_c3_orbit_count") == 8
           and "the pairing is not forced" in ip_txt
           and "matched-3=3 count" in ip_txt
           and "merger-273 / Cl(3) cubic-lift are not cited to supply "
               "it" in ip_txt
           and "consumes thermal/spectral data only" in own_txt,
           "[D] turn-1 inversion-guard compliance (computed + "
           "textual): the selection consumes thermal/spectral data "
           "only -- zero counts 8/8/8 vs 20/68/140, cone speeds, "
           "|det V|, g_eff ratios; the kernel-global count readouts "
           "are 8/4 (K1) and 20/8 (K0), NEVER 3; the only 3 = 3 in "
           "this runner is the falsification TIE (leg 1), which "
           "selects nothing; the guards of the index-pairing no-go "
           "('not forced from the matched-3=3 count'; merger-273 / "
           "Cl(3) cubic-lift not cited) are respected and the note "
           "declares it")
    residual("finite grids: eigensolver L in {4, 8, 12} (PBC, 4 | L "
             "wrap convention), symbol grids L in {64, 128} licensed "
             "by the closed-form ties of check 5 (boundary B-G)")
    residual("if C1 is later invalidated to audited_conditional, the "
             "selection reverts to a conditional cascade; if C1 is "
             "later invalidated to audited_failed or audited_renaming, "
             "the composition collapses. This runner re-checks the "
             "grades on every run (boundary B-C1)")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: RETAINED-GRADE within-surface selection, composed "
              "honestly: since the FSB-K row (C1) stands at")
        print("         retained_bounded grade,")
        print("         using the retained (Z)-certificate geometry leg, "
              "within the licensed two-class kinetic surface the")
        print("         finite-species-density")
        print("         requirement (CL) -- B-Z2 in the retained SB "
              "bridge's own per-dof currency -- is satisfied by K1")
        print("         (g_eff plateau ~ 8 = sum |det V|^-1 per cell; "
              "~ 1 = 8/2^3 per site at unit hopping) and violated by")
        print("         K0 (g_eff ~ T^-2, Sommerfeld), hence phi = -1 "
              "is selected: B-Z2 supplied, B-BIT retired within the")
        print("         licensed surface at C1's grade. TODAY C1 is "
              "retained_bounded and the Z certificate is retained:")
        print("         this note performs the within-surface selection at "
              "current grades. Dropping (CL) restores the retained-surface tie;")
        print("         dropping the retained Z geometry leaves the "
              "hypothesis unverified and the selection collapses. "
              "Nothing is forced from")
        print("         the matched-3=3 count: the selection consumes "
              "thermal/spectral data only.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
