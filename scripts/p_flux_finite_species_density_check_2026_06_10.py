#!/usr/bin/env python3
"""P-FLUX finite-species-density supplier hunt on the enumerated
determinant/Matsubara, thermal, and isotropy surfaces — no retained
supplier within scope (runner).

Companion to
docs/P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md

Question.  The landed point-zero-set no-go
(P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10;
all shared facts re-derived here) sharpened the live escape
for the one-bit residual P-FLUX (phi = -1 vs phi = +1) to ONE clause —
boundary B-Z2: a future retained-grade "the massless species density is
finite" / "ker = carrier" / point-like-zero-set requirement.  This
runner hunts the supplier in the nearby candidate family that consumes
FULL spectral density rather than carrier slices — the
determinant/Matsubara/heat-kernel family — plus the emergent-isotropy/
Lorentz rows and the thermal/entropy rows, and computes, on both
licensed kinetic classes (K0 = uniform flux +1 scalar tight-binding;
K1 = uniform flux -1 Kawamoto-Smit class), exactly WHICH
determinant-currency and thermal-currency objects degenerate on the
extensive-zero-set branch and how.

Outcome computed here:

  1. NO RETAINED SUPPLIER: every current row in the enumerated
     determinant/Matsubara/heat-kernel candidate set is staggered-scoped
     (Matsubara decomposition family: fixed Z^4 APBC L_s=2 mean-field
     staggered block, gapped on its own surface so its normalization
     clause never meets a zero mode), hypothesis-conditional
     (det positivity: m > 0; Jacobi derivative: "invertible on an open
     neighborhood"), matrix-agnostic (Berezin: "for any complex
     matrix M" — an identity, not a finiteness requirement), supplied
     (flavor heat-kernel path), or off the realized matter-kernel
     sector (Higgs taste carrier; thermal-circle zeta ladders).  The
     retained-pending real-diagonal candidate is hypothesis-conditional
     ("For invertible real antisymmetric D") and is not treated as
     retained-grade.  The
     thermal g* inventory row is currently unaudited; the axiom-first
     fermionic SB, Greens, and GL(F) discriminator rows are now
     retained_bounded but still scoped/conditional rather than suppliers
     of B-Z2 for the realized matter kernel; the retained
     Lorentz/isotropy rows are descriptive of BOTH given carriers
     (staggered sin^2 and bosonic graph-Laplacian), normative of
     neither.  No retained third-law/vacuum-entropy row exists.
  2. THE DEGENERACY CERTIFICATES (the new computed content, making the
     missing supplier maximally concrete in retained currency):
     (a) det vanishing ORDER at m -> 0: ord_m det(D_E + m I) = N_0(L)
         — bounded (8,8,8) on the K1-class Euclidean operator vs
         extensive (20,56,68) on the K0-class one (L = 4,6,8); the
         retained det-positivity row proves det > 0 for m > 0 on BOTH
         (its mechanism is branch-neutral) and is silent at m = 0
         where the branches separate.
     (b) the naive zeta route is CLOSED: the per-volume IR limit
         (1/V) log det(h^2 + m^2) - (2 N_0 / V) log m^2 ... exists and
         is m-independent on BOTH branches, and the divergence
         coefficient 2 N_0 / V -> 0 on BOTH — "log-det divergence per
         volume" does NOT separate; only the ORDER does.
     (c) the retained free-energy-density normalization clause
         (ln|det(D+m)| - ln|det(D)|) fails branch-neutrally on the
         licensed PBC surface at 4|L (det = 0 on both) and is
         L-dependent under APBC (K0 kernel 0,0,96 at L=4,8,12; K1
         kernel empty at all three) — convention-graded, consumed by
         no retained row at any volume quantifier.
     (d) the object that ACTUALLY bites, in the retained
         Stefan-Boltzmann row's own per-dof currency: g_eff(T) :=
         u(T) / [(7/8)(pi^2/30) T^4] has a FINITE T -> 0 plateau
         (~ 1 = 8 species / v^3) on K1 and DIVERGES like T^-2 on K0
         (Fermi-surface T^2 law, Sommerfeld plateau u/T^2 ~ 0.233);
         the point-zero comparator diverges like T^-3/2 — so the
         thermal clause is strictly STRONGER than point-like zero set
         (it also forces conical dispersion).
     (e) near-zero-set isotropy: K1 cone speeds are direction-
         independent (= 2); K0's zero surface carries an EXACT flat
         direction (tangent speed 0, normal speed 2*sqrt(3)) — a real
         separator consumed by no retained row.
  3. The zero-point-entropy route is honestly killed: N_0 ln2 / V -> 0
     on BOTH branches (no "nonvanishing T -> 0 entropy density" exists
     even on K0), and no third-law row exists at any grade.
  4. Falsification: the candidate clause CL ("g_eff(T) bounded as
     T -> 0", B-Z2 in retained-SB currency) selects EXACTLY K1 among
     {K0, K1, comparator} as a SINGLE clause; dropping it restores the
     retained-surface PASS/PASS tie; the turn-1 inversion guards are
     respected (nothing forced from matched-3=3).

Sections:
  [A] exact branch construction, zero-set geometry, closed-form
      spectrum licenses, comparator
  [B] route A: the determinant/Matsubara family — supplier sweep and
      degeneracy certificates
  [C] routes B/C: thermal (Stefan-Boltzmann currency) and isotropy
      certificates; entropy kill
  [D] falsification legs and inversion-guard compliance

Deterministic, no network, no randomness, numpy only.
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


# ----------------------------------------------------------------------
# constructions (re-derived on the retained single-mode surface;
# conceptually parallel to the two parent P-FLUX no-go runners; their
# shared facts are re-derived here rather than imported)
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


def build_h(L, t_fun, onsite=0.0, apbc=False):
    sites = sites_of(L)
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((N, N), complex)
    for x in sites:
        for mu in range(3):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L
            wrap = (x[mu] + 1 == L)
            t = t_fun(x, mu) * (-1.0 if (apbc and wrap) else 1.0)
            h[idx[tuple(xp)], idx[x]] += t
            h[idx[x], idx[tuple(xp)]] += np.conj(t)
        if onsite != 0.0:
            h[idx[x], idx[x]] += onsite
    return h, sites, idx


def build_euclid(L, t_fun):
    """Euclidean central-difference operator
    D = sum_mu t_mu(x) (S_mu - S_mu^T)/2 — real antisymmetric; for
    t = eta (Kawamoto-Smit phases) this is the staggered M_KS of the
    retained det-positivity row at U = 1; for t = 1 it is the K0-class
    analog with the same construction."""
    sites = sites_of(L)
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    D = np.zeros((N, N))
    for x in sites:
        for mu in range(3):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L
            t = t_fun(x, mu)
            D[idx[tuple(xp)], idx[x]] += 0.5 * t
            D[idx[x], idx[tuple(xp)]] -= 0.5 * t
    return D, sites, idx


def plaquette_fluxes(L, sites, t_fun):
    fluxes = []
    for x in sites:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % L
                xm = tuple(xm)
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % L
                xn = tuple(xn)
                f = (t_fun(x, mu) * t_fun(xm, nu)
                     * np.conj(t_fun(xn, mu)) * np.conj(t_fun(x, nu)))
                fluxes.append(complex(f))
    return fluxes


def kernel_dim(h, tol=1e-9):
    return int((np.abs(np.linalg.eigvalsh(h)) < tol).sum())


def k0_symbol_vals(L):
    k = 2 * np.pi * np.arange(L) / L
    c = np.cos(k)
    return (2 * (c[:, None, None] + c[None, :, None]
                 + c[None, None, :])).ravel()


def k1_symbol_vals(L):
    """Closed-form K1 spectrum multiset (certified against the
    eigensolver in check 4): +-2 sqrt(sum_mu sin^2 q_mu) with
    q_mu = 2 pi n_mu / L, n_mu = 0..L/2-1, multiplicity 4 each sign."""
    k = 2 * np.pi * np.arange(L // 2) / L
    s2 = np.sin(k) ** 2
    e = 2 * np.sqrt(s2[:, None, None] + s2[None, :, None]
                    + s2[None, None, :])
    e = e.ravel()
    return np.concatenate([np.repeat(e, 4), np.repeat(-e, 4)])


def comparator_symbol_vals(L):
    return k0_symbol_vals(L) - 6.0


def u_density(vals, T):
    """Thermal energy density per site at temperature T for the
    half-filled free Fermi sector: u(T) = (1/V) sum_E |E| f_FD(|E|/T)
    — the Stefan-Boltzmann row's integrand evaluated on the realized
    spectrum (a hypothesis-satisfiability probe, not a realized-
    dynamics claim)."""
    a = np.abs(vals)
    return float(np.sum(a / (np.exp(np.minimum(a / T, 700.0)) + 1.0))
                 / len(vals))


def logdet_h2(vals, m):
    return float(np.log(vals ** 2 + m ** 2).sum())


def leibniz_det(M):
    """Berezin readout Z_F = int exp(-chibar M chi) evaluated by the
    Grassmann (Leibniz) expansion — the explicit permutation sum the
    Berezin rules produce."""
    n = M.shape[0]
    tot = 0.0 + 0j
    for perm in itertools.permutations(range(n)):
        seen = [False] * n
        par = 0
        for i in range(n):
            if not seen[i]:
                j = i
                cl = 0
                while not seen[j]:
                    seen[j] = True
                    j = perm[j]
                    cl += 1
                par += cl - 1
        prod = 1.0 + 0j
        for i in range(n):
            prod *= M[i, perm[i]]
        tot += ((-1) ** par) * prod
    return tot


# --- carrier battery (lite port of the parent no-go machinery) -------

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


def commutant_dim(ops):
    n = ops[0].shape[0]
    rows = [np.kron(np.eye(n), A) - np.kron(A.T, np.eye(n)) for A in ops]
    C = np.vstack(rows)
    return int(n * n - np.linalg.matrix_rank(C, tol=1e-8))


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
    K = ker.shape[1]
    out["ker_dim"] = K
    if K == 0:
        return out
    vecs, chars = joint_characters(ker, Ts)
    cube = find_cube(chars)
    out["cube"] = cube is not None
    if cube is None:
        return out
    out["extra_dim"] = K - 8
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


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("[A] branch construction, zero-set geometry, closed-form")
    print("    spectrum licenses, comparator")
    print("=" * 72)

    Ls = (4, 8, 12)
    H0 = {L: build_h(L, t_K0)[0] for L in Ls}
    S4 = sites_of(4)
    H1 = {L: build_h(L, t_K1)[0] for L in Ls}

    f0 = plaquette_fluxes(4, S4, t_K0)
    f1 = plaquette_fluxes(4, S4, t_K1)
    report(np.allclose(H0[4], H0[4].conj().T)
           and np.allclose(H1[4], H1[4].conj().T)
           and all(abs(f - 1) < 1e-12 for f in f0)
           and all(abs(f + 1) < 1e-12 for f in f1),
           "[A] both branches Hermitian; frame-invariant uniform flux "
           "K0 phi=+1, K1 phi=-1 (licensed two-class surface, "
           "re-derived)")

    z0 = {L: kernel_dim(H0[L]) for L in Ls}
    z1 = {L: kernel_dim(H1[L]) for L in Ls}
    sym0 = {L: int((np.abs(k0_symbol_vals(L)) < 1e-9).sum()) for L in Ls}
    report((z0[4], z0[8], z0[12]) == (20, 68, 140)
           and (z1[4], z1[8], z1[12]) == (8, 8, 8)
           and all(sym0[L] == z0[L] for L in Ls),
           f"[A] zero-mode counts: K0 (L=4,8,12) = "
           f"({z0[4]},{z0[8]},{z0[12]}) = lattice trace of the codim-1 "
           f"surface sum_mu cos p_mu = 0; K1 = ({z1[4]},{z1[8]},{z1[12]})")

    expo = math.log(z0[12] / z0[8]) / math.log(12 / 8)
    report(expo > 1.5 and z1[4] == z1[12],
           f"[A] K0 growth exponent {expo:.2f} (extensive, "
           f"surface-like); K1 count L-independent = 8 (point-like)")

    ok_cf = True
    for L in (4, 8):
        w = np.sort(np.linalg.eigvalsh(H1[L]))
        ok_cf &= np.allclose(w, np.sort(k1_symbol_vals(L)), atol=1e-9)
        w0 = np.sort(np.linalg.eigvalsh(H0[L]))
        ok_cf &= np.allclose(w0, np.sort(k0_symbol_vals(L)), atol=1e-9)
    report(ok_cf,
           "[A] closed-form spectra certified against the eigensolver "
           "at L=4,8 (K0: 2 sum cos p; K1: +-2 sqrt(sum sin^2 q), "
           "mult 4) — licenses the large-L symbol-grid evaluations "
           "below")

    HP = {L: build_h(L, t_K0, onsite=-6.0)[0] for L in Ls}
    zp = {L: kernel_dim(HP[L]) for L in Ls}
    report((zp[4], zp[8], zp[12]) == (1, 1, 1),
           f"[A] comparator (scalar NN + on-site -6, declared OFF the "
           f"two-class surface): point-like zero set ({zp[4]},{zp[8]},"
           f"{zp[12]}), quadratic band — used below to separate "
           f"'point-like zero set' from 'finite g_eff'")

    print()
    print("=" * 72)
    print("[B] route A: the determinant/Matsubara family — supplier")
    print("    sweep and degeneracy certificates")
    print("=" * 72)

    rows = ledger()
    fam = {
        "hierarchy_matsubara_decomposition_note": "retained_bounded",
        "staggered_only_det_positivity_case_a_note_2026-05-17": "retained",
        "staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05":
            "retained",
        "spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10":
            "retained_bounded",
        "flavor_logdet_factor_4b_jacobi_derivative_narrow_theorem_note_"
        "2026-06-04": "retained",
        "real_diagonal_source_det_positivity_and_log_readout_lemma_note_"
        "2026-06-08": "retained_pending_chain",
        "higgs_mean_field_determinant_apbc_taste_bridge_note_2026-06-06":
            "retained",
        "flavor_supplied_heat_kernel_arrow_r_half_stability_bounded_note_"
        "2026-06-04": "retained_bounded",
        "hierarchy_seven_eighths_twisted_thermal_zeta_period_quotient_"
        "narrow_theorem_note_2026-05-26": "retained",
    }
    ok_fam = all(status(rows, r) == s for r, s in fam.items())
    dec1 = status(rows, "hierarchy_matsubara_determinant_narrow_theorem_"
                        "note_2026-05-02")
    dec2 = status(rows, "hierarchy_matsubara_free_energy_density_narrow_"
                        "theorem_note_2026-05-16")
    status_expect = {
        "hierarchy_matsubara_determinant_ratio_narrow_theorem_note_2026-05-10": "unaudited",
        "hierarchy_matsubara_quartic_coefficient_ratio_narrow_theorem_note_2026-05-10": "unaudited",
        "emergent_gauge_heat_kernel_clt_attractor_conditional_on_bi_invariant_dynamics_narrow_theorem_note_2026-06-08": "unaudited",
        "hierarchy_heat_kernel_d4_compression_bounded_theorem_note_2026-05-10": "unaudited",
        "lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07": "retained_bounded",
        "staggered_dirac_substep1_statistics_gl_f_conditional_discriminator_bounded_theorem_note_2026-06-10": "retained_bounded",
    }
    ok_related = all(status(rows, r) == s for r, s in status_expect.items())
    report(ok_fam and ok_related
           and str(dec1).startswith("decoration_under")
           and str(dec2).startswith("decoration_under"),
           "[B] ledger sweep of the determinant/Matsubara/heat-kernel "
           "candidate set: expected statuses match the note "
           "(retained-grade rows plus one retained-pending "
           "real-diagonal candidate; decomposition parent retained_"
           "bounded with the determinant + free-energy decorations "
           "under it); the "
           "ratio/quartic and heat-kernel-CLT/d4 rows are unaudited, while "
           "the Greens and GL(F)-Berezin discriminator rows are retained_bounded "
           "but remain scope/condition limited and do not supply B-Z2")

    det_txt = note_text("docs/HIERARCHY_MATSUBARA_DETERMINANT_NARROW_"
                        "THEOREM_NOTE_2026-05-02.md")
    fed_txt = note_text("docs/HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_"
                        "NARROW_THEOREM_NOTE_2026-05-16.md")
    own_gap = all(min(3 + math.sin((2 * n + 1) * math.pi / Lt) ** 2
                      for n in range(Lt)) >= 3.0 - 1e-12
                  for Lt in (2, 3, 4, 6, 8))
    report("minimal spatial APBC block" in det_txt
           and "staggered Dirac" in det_txt
           and "ln|det(D + m)| - ln|det(D)|" in fed_txt
           and own_gap,
           "[B] textual + algebraic: the Matsubara family is scoped to "
           "the 'minimal spatial APBC block' of the 'staggered Dirac' "
           "operator (staggered-grounded => circular as a selector, "
           "same class as RP), and on its own surface "
           "min_omega (3 + sin^2 omega) = 3 > 0 — its normalization "
           "clause ln|det(D + m)| - ln|det(D)| NEVER meets a zero mode "
           "and is silent off its block")

    pbc6_0 = kernel_dim(build_h(6, t_K0)[0])
    pbc6_1 = kernel_dim(build_h(6, t_K1)[0])
    report(z0[4] > 0 and z1[4] > 0 and z0[12] > 0 and z1[12] > 0
           and pbc6_0 == 24 and pbc6_1 == 0,
           f"[B] the Delta-f clause det(D) != 0 on the licensed PBC "
           f"surface: FAILS on BOTH branches at 4|L (kernels "
           f"{z0[4]}/{z1[4]} at L=4, {z0[12]}/{z1[12]} at L=12); at "
           f"L=6 it holds on K1 only (kernels {pbc6_0}/{pbc6_1}) — "
           f"L-graded wrap-convention data, quantified over volumes by "
           f"NO retained row")

    ap0 = {L: kernel_dim(build_h(L, t_K0, apbc=True)[0]) for L in Ls}
    ap1 = {L: kernel_dim(build_h(L, t_K1, apbc=True)[0]) for L in Ls}
    apw0 = {L: int((np.abs(np.linalg.eigvalsh(
        build_h(L, t_K0, apbc=True)[0])) < 0.5).sum()) for L in (8, 12)}
    apw1 = {L: int((np.abs(np.linalg.eigvalsh(
        build_h(L, t_K1, apbc=True)[0])) < 0.5).sum()) for L in (8, 12)}
    report((ap0[4], ap0[8], ap0[12]) == (0, 0, 96)
           and (ap1[4], ap1[8], ap1[12]) == (0, 0, 0)
           and (apw0[8], apw0[12]) == (48, 144)
           and (apw1[8], apw1[12]) == (0, 0),
           f"[B] under APBC (the retained family's own convention): K0 "
           f"kernel ({ap0[4]},{ap0[8]},{ap0[12]}) at L=4,8,12 — "
           f"resonance re-entry at L=12 — K1 kernel "
           f"({ap1[4]},{ap1[8]},{ap1[12]}); near-zero density persists "
           f"only on K0 (|E|<0.5 counts: K0 {apw0[8]},{apw0[12]} vs K1 "
           f"{apw1[8]},{apw1[12]} at L=8,12): real det-currency "
           f"separators, consumed by NO retained row")

    ok_mech = True
    ordE = {}
    for L in (4, 6, 8):
        for nm, tf in (("K1E", t_K1), ("K0E", t_K0)):
            D, sites, _ = build_euclid(L, tf)
            eps = np.diag([(-1.0) ** sum(x) for x in sites])
            ok_mech &= np.allclose(D, -D.T)
            ok_mech &= np.allclose(eps @ D @ eps, -D, atol=1e-12)
            lam = np.linalg.eigvalsh(1j * D)
            ld = {m: float(np.log(m ** 2 + lam ** 2).sum()) / 2.0
                  for m in (1e-3, 1e-5)}
            ordE[(nm, L)] = ((ld[1e-3] - ld[1e-5])
                             / (math.log(1e-3) - math.log(1e-5)))
            # det(D + mI) = prod_k (m - i lam_k); the +-lam pairing
            # (verified) makes it m^{N_0} prod_{lam>0} (m^2 + lam^2) > 0
            # for m > 0 — the Case-A conclusion, eigenvalue-exact
            ok_mech &= np.allclose(np.sort(lam), -np.sort(lam)[::-1],
                                   atol=1e-9)
    report(ok_mech,
           "[B] det-positivity mechanism is branch-neutral: BOTH "
           "Euclidean central-difference operators are real "
           "antisymmetric with {eps, D} = 0 and +-lambda paired "
           "spectra (the Case-A hypotheses and mechanism), so "
           "det(D + m I) = m^N_0 prod(m^2 + lambda^2) > 0 for every "
           "m > 0 on both — the retained m > 0 conclusion cannot "
           "separate")

    o1 = tuple(round(ordE[("K1E", L)]) for L in (4, 6, 8))
    o0 = tuple(round(ordE[("K0E", L)]) for L in (4, 6, 8))
    ok_ord = (o1 == (8, 8, 8) and o0 == (20, 56, 68)
              and all(abs(ordE[k] - round(ordE[k])) < 0.05 for k in ordE))
    report(ok_ord,
           f"[B] THE determinant-currency degeneracy (computed): "
           f"ord_m det(D_E + m I) as m -> 0 equals N_0(L): K1-class "
           f"{o1} (bounded), K0-class {o0} (extensive) at L=4,6,8 — "
           f"the retained det-positivity text ('m > 0', 'arbitrary "
           f"SU(3) gauge background') is SILENT at m = 0, exactly "
           f"where the branches separate")

    ok_zeta = True
    reg_print = {}
    for L in (12, 24, 48):
        for nm, vals in (("K0", k0_symbol_vals(L)),
                         ("K1", k1_symbol_vals(L))):
            V = L ** 3
            n0 = int((np.abs(vals) < 1e-12).sum())
            regs = {}
            for m in (1e-6, 1e-8):
                regs[m] = ((logdet_h2(vals, m) - 2 * n0 * math.log(m))
                           / V)
            ok_zeta &= abs(regs[1e-6] - regs[1e-8]) < 1e-4
            reg_print[(nm, L)] = (n0, regs[1e-8])
    co0 = [2 * reg_print[("K0", L)][0] / L ** 3 for L in (12, 24, 48)]
    co1 = [2 * reg_print[("K1", L)][0] / L ** 3 for L in (12, 24, 48)]
    ok_zeta &= co0[0] > co0[1] > co0[2] and co1[0] > co1[1] > co1[2]
    report(ok_zeta,
           f"[B] the naive zeta route is CLOSED (honesty leg): the "
           f"per-volume IR limit of (1/V) log det(h^2+m^2) minus the "
           f"zero-mode term exists on BOTH branches (m-independent at "
           f"1e-6 vs 1e-8; e.g. L=48: K0 "
           f"{reg_print[('K0', 48)][1]:.4f}, K1 "
           f"{reg_print[('K1', 48)][1]:.4f}), and the divergence "
           f"coefficient 2 N_0/V -> 0 on BOTH (K0: "
           f"{co0[0]:.3f},{co0[1]:.3f},{co0[2]:.3f}; K1: "
           f"{co1[0]:.4f},{co1[1]:.4f},{co1[2]:.4f} at L=12,24,48) — "
           f"per-volume log-det divergence does NOT separate; only the "
           f"ORDER of vanishing does")

    ber_txt = note_text("docs/SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_"
                        "THEOREM_NOTE_2026-05-10.md")
    jac_txt = note_text("docs/FLAVOR_LOGDET_FACTOR_4B_JACOBI_DERIVATIVE_"
                        "NARROW_THEOREM_NOTE_2026-06-04.md")
    rds_txt = note_text("docs/REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_"
                        "READOUT_LEMMA_NOTE_2026-06-08.md")
    hk_txt = note_text("docs/FLAVOR_SUPPLIED_HEAT_KERNEL_ARROW_R_HALF_"
                       "STABILITY_BOUNDED_NOTE_2026-06-04.md")
    hg_txt = note_text("docs/HIGGS_MEAN_FIELD_DETERMINANT_APBC_TASTE_"
                       "BRIDGE_NOTE_2026-06-06.md")
    h0_2 = build_h(2, t_K0)[0]
    h1_2 = build_h(2, t_K1)[0]
    ring = np.zeros((4, 4))
    for i in range(4):
        ring[(i + 1) % 4, i] += 1.0
        ring[i, (i + 1) % 4] += 1.0
    ok_ber = (abs(leibniz_det(h0_2) - np.linalg.det(h0_2)) < 1e-6
              and abs(leibniz_det(h1_2) - np.linalg.det(h1_2)) < 1e-6
              and abs(leibniz_det(ring)) < 1e-12
              and abs(np.linalg.det(ring)) < 1e-12)
    report("for any complex matrix" in ber_txt
           and "invertible on an open neighborhood" in jac_txt
           and "For invertible real antisymmetric" in rds_txt
           and "supplied heat-kernel/blocking path" in hk_txt
           and "dim H_taste = 16" in hg_txt
           and ok_ber,
           "[B] remaining family quantifiers (textual): Berezin holds "
           "'for any complex matrix' (an identity, verified here by "
           "Leibniz expansion on both L=2 branch blocks AND on a "
           "singular K0-class ring where det = 0 — no finiteness "
           "clause); Jacobi assumes 'invertible on an open "
           "neighborhood'; real-diagonal L2 'For invertible real "
           "antisymmetric D'; the flavor heat-kernel path is "
           "'supplied'; the Higgs bridge lives on the fixed 16-dim "
           "taste carrier — none binds the realized matter kernel's "
           "zero set")
    residual("the determinant-currency separators computed here "
             "(vanishing order bounded-vs-extensive; APBC "
             "invertibility/near-zero density) are real but consumed "
             "by no retained row; stating a retained requirement on "
             "any of them is exactly B-Z2, still open (boundary B-F1)")

    print()
    print("=" * 72)
    print("[C] routes B/C: thermal (Stefan-Boltzmann currency) and")
    print("    isotropy certificates; entropy kill")
    print("=" * 72)

    sb_txt = note_text("docs/GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_"
                       "BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md")
    st_sb = status(rows, "gstar_thermal_seven_eighths_stefan_boltzmann_"
                         "bridge_narrow_theorem_note_2026-06-06")
    st_inv = status(rows, "g_star_sm_content_at_leptogenesis_from_supplied_"
                          "thermal_inventory_bounded_theorem_note_2026-05-28")
    st_ax = status(rows, "axiom_first_fermionic_stefan_boltzmann_narrow_"
                         "theorem_note_2026-05-26")
    gstar = 28 + (7.0 / 8.0) * 90
    report(st_sb == "retained_bounded" and st_inv == "unaudited"
           and st_ax == "retained_bounded"
           and "relativistic, effectively massless thermal degree of "
               "freedom" in sb_txt
           and "It does not derive the Standard Model particle inventory"
               in sb_txt
           and abs(gstar - 427.0 / 4.0) < 1e-12,
           "[C] the retained SB row binds 'a relativistic, effectively "
           "massless thermal degree of freedom' and 'does not derive "
           "the Standard Model particle inventory'; the supplied-inventory "
           "row is currently unaudited; the axiom-first fermionic SB row is "
           "retained_bounded but does not derive the realized matter-kernel "
           "inventory; the g* arithmetic 28 + (7/8)*90 = 427/4 is "
           "branch-independent — no retained row applies the T^4 form "
           "to the REALIZED matter kernel")

    L = 128
    T_ladder = (0.05, 0.1, 0.2, 0.4)
    vals = {"K0": k0_symbol_vals(L), "K1": k1_symbol_vals(L),
            "comp": comparator_symbol_vals(L)}
    pref = (7.0 / 8.0) * (math.pi ** 2 / 30.0)
    geff = {(nm, T): u_density(v, T) / (pref * T ** 4)
            for nm, v in vals.items() for T in T_ladder}
    u64 = u_density(k1_symbol_vals(64), 0.2)
    conv = abs(u64 - u_density(vals["K1"], 0.2)) / u_density(vals["K1"], 0.2)
    r0a = geff[("K0", 0.05)] / geff[("K0", 0.1)]
    r0b = geff[("K0", 0.1)] / geff[("K0", 0.2)]
    r1 = geff[("K1", 0.05)] / geff[("K1", 0.1)]
    rca = geff[("comp", 0.05)] / geff[("comp", 0.1)]
    rcb = geff[("comp", 0.1)] / geff[("comp", 0.2)]
    report(conv < 0.01
           and 3.8 < r0a < 4.2 and 3.8 < r0b < 4.2
           and 0.85 < r1 < 1.05
           and abs(geff[("K1", 0.05)] - 1.0) < 0.05
           and 2.5 < rca < 2.95 and 2.5 < rcb < 2.95,
           f"[C] WHICH retained-currency object bites (computed, L=128 "
           f"symbol grid, T=0.05..0.4): g_eff(T) := u(T)/[(7/8)"
           f"(pi^2/30) T^4] — K1 has a FINITE plateau "
           f"{geff[('K1', 0.05)]:.3f} ~ 1 = 8 species / v^3 "
           f"(T-halving ratio {r1:.2f}); K0 DIVERGES like T^-2 "
           f"(g_eff {geff[('K0', 0.05)]:.0f}, {geff[('K0', 0.1)]:.0f}, "
           f"{geff[('K0', 0.2)]:.1f}, {geff[('K0', 0.4)]:.1f}; ratios "
           f"{r0a:.2f}, {r0b:.2f}); the point-zero comparator diverges "
           f"like T^-1.5 (ratios {rca:.2f}, {rcb:.2f}) — finite g_eff "
           f"is 'finite massless species density' in the retained SB "
           f"row's own per-dof currency")

    u_T2 = [u_density(vals["K0"], T) / T ** 2 for T in T_ladder]
    report(max(u_T2) / min(u_T2) < 1.05,
           f"[C] K0's massless sector is a Fermi surface in the "
           f"thermal currency: u(T)/T^2 plateaus at "
           f"{u_T2[0]:.3f},{u_T2[1]:.3f},{u_T2[2]:.3f},{u_T2[3]:.3f} "
           f"(Sommerfeld T^2 law; the T^4 Stefan-Boltzmann form fails "
           f"structurally, not numerically)")

    s_ent0 = [z0[L0] * math.log(2) / L0 ** 3 for L0 in Ls]
    s_ent1 = [z1[L0] * math.log(2) / L0 ** 3 for L0 in Ls]
    no_third_law = not any("third_law" in k for k in rows)
    st_rr = status(rows, "record_reset_sink_entropy_ledger_2026-06-05")
    report(s_ent0[0] > s_ent0[1] > s_ent0[2]
           and s_ent1[0] > s_ent1[1] > s_ent1[2]
           and no_third_law and st_rr == "unaudited",
           f"[C] route C honestly killed BOTH ways: the zero-point "
           f"entropy density N_0 ln2 / V -> 0 on BOTH branches (K0: "
           f"{s_ent0[0]:.3f},{s_ent0[1]:.3f},{s_ent0[2]:.3f}; K1: "
           f"{s_ent1[0]:.4f},{s_ent1[1]:.4f},{s_ent1[2]:.4f} at "
           f"L=4,8,12) — no 'nonvanishing T->0 entropy density' exists "
           f"even on K0 — and no third-law/vacuum-entropy row exists "
           f"at any grade (record-reset entropy ledger unaudited)")

    el_txt = note_text("docs/EMERGENT_LORENTZ_INVARIANCE_NOTE.md")
    lv_txt = note_text("docs/LORENTZ_VIOLATION_DERIVED_NOTE.md")
    fp_txt = note_text("docs/LORENTZ_VIOLATION_ANGULAR_FINGERPRINT_AC_PHI_"
                       "LAMBDA_INDEPENDENCE_BOUNDED_NOTE_2026-06-08.md")
    st_el = status(rows, "emergent_lorentz_invariance_note")
    st_lv = status(rows, "lorentz_violation_derived_note")
    st_fp = status(rows, "lorentz_violation_angular_fingerprint_ac_phi_"
                         "lambda_independence_bounded_note_2026-06-08")
    st_ep = status(rows, "emergent_poincare_free_sector_from_kinetic_"
                         "isotropy_primitive_bounded_theorem_note_"
                         "2026-06-09")
    report(st_el == "retained_bounded" and st_lv == "retained_bounded"
           and st_fp == "retained_bounded" and st_ep == "unaudited"
           and "the free cubic" in el_txt and "staggered lattice" in el_txt
           and "sin^2(p_i a / 2)" in lv_txt
           and "graph-Laplacian carrier gives coefficient" in fp_txt
           and "the angular fingerprint is independent of the" in fp_txt,
           "[C] route B circularity check (textual): the retained "
           "isotropy core is derived ON 'the free cubic ... staggered "
           "lattice' (NOT independently of the Dirac form => circular "
           "as a selector, same class as RP); the retained LV package "
           "ALSO carries the K0-class bosonic graph-Laplacian "
           "dispersion sin^2(p_i a / 2) as a legitimate carrier with "
           "the same angular fingerprint — descriptive of both "
           "carriers, normative of neither; the kinetic-isotropy-"
           "primitive Poincare row is unaudited")

    p = 1e-2
    c_stag = (p ** 2 - math.sin(p) ** 2) / p ** 4
    c_bose = (p ** 2 - 2 * (1 - math.cos(p))) / p ** 4
    report(abs(c_stag - 1.0 / 3.0) < 1e-4 and abs(c_bose - 1.0 / 12.0) < 1e-4,
           f"[C] the retained Lorentz content ties (computed): BOTH "
           f"carriers are isotropic at leading order near p=0 with "
           f"quartic coefficients 1/3 (staggered, {c_stag:.5f}) and "
           f"1/12 (graph-Laplacian, {c_bose:.5f}) — the retained rows' "
           f"actual statements hold on both branches' home dispersions "
           f"and require nothing of the realized zero set")

    def Ek1(pv):
        return 2 * math.sqrt(sum(math.sin(x) ** 2 for x in pv))

    def Ek0(pv):
        return 2 * sum(math.cos(x) for x in pv)

    s = 1e-5
    dirs = [(1, 0, 0), (1 / math.sqrt(2), 1 / math.sqrt(2), 0),
            (1 / math.sqrt(3),) * 3,
            (2 / math.sqrt(5), 1 / math.sqrt(5), 0)]
    sp1 = [Ek1([s * u for u in d]) / s for d in dirs]
    p0 = (math.pi / 2,) * 3
    nrm = (1 / math.sqrt(3),) * 3
    tan = (1 / math.sqrt(2), -1 / math.sqrt(2), 0)

    def dspeed(d):
        pp = [p0[i] + s * d[i] for i in range(3)]
        pm = [p0[i] - s * d[i] for i in range(3)]
        return (Ek0(pp) - Ek0(pm)) / (2 * s)

    report(max(sp1) - min(sp1) < 1e-8 and abs(sp1[0] - 2.0) < 1e-8
           and abs(abs(dspeed(nrm)) - 2 * math.sqrt(3)) < 1e-6
           and abs(dspeed(tan)) < 1e-9,
           f"[C] near-zero-set isotropy separator (computed): K1's "
           f"cone speed is direction-independent (= {sp1[0]:.6f} along "
           f"axis/face/body/skew directions); K0's zero surface at "
           f"(pi/2,pi/2,pi/2) has normal speed {abs(dspeed(nrm)):.4f} "
           f"= 2 sqrt(3) and EXACTLY flat tangent directions (speed "
           f"{abs(dspeed(tan)):.1e}) — real separator, consumed by NO "
           f"retained row")
    residual("the thermal objects above are hypothesis-satisfiability "
             "probes in the retained SB row's own integrand, not "
             "realized-dynamics or equilibrium claims (boundary B-F3)")

    print()
    print("=" * 72)
    print("[D] falsification legs and inversion-guard compliance")
    print("=" * 72)

    # CL (bounded g_eff): plateau test — the T-halving ratio of g_eff
    # stays below 1.5 (a bounded function has ratio -> 1; T^-2 gives 4,
    # T^-1.5 gives ~2.8)
    cl = {nm: geff[(nm, 0.05)] / geff[(nm, 0.1)] < 1.5
          for nm in ("K0", "K1", "comp")}
    report(cl["K1"] and not cl["K0"] and not cl["comp"],
           "[D] falsification leg 1 (non-vacuity): the candidate "
           "clause CL = 'g_eff(T) bounded as T -> 0' (B-Z2 in retained "
           "SB currency) selects EXACTLY K1 among {K0, K1, comparator} "
           "as a SINGLE clause (the comparator passes point-like zero "
           "set but fails CL: CL = point-like zero set AND conical "
           "dispersion) — it would force phi = -1 immediately IF any "
           "retained row stated it of the realized matter kernel")

    h0_4, s4b, i4b = build_h(4, t_K0)
    h1_4, _, _ = build_h(4, t_K1)
    d0 = carrier_data(h0_4, 4, s4b, i4b)
    d1 = carrier_data(h1_4, 4, s4b, i4b)
    tie = (d1.get("cube") and d1.get("carrier_count") == 3
           and d1.get("carrier_alg_dim") == 9
           and d0.get("cube") and d0.get("carrier_count") == 3
           and d0.get("carrier_alg_dim") == 9)
    report(bool(tie),
           "[D] falsification leg 2 (remove the non-retained clause): "
           "the retained-surface battery alone ties PASS/PASS — det "
           "positivity at m > 0 (check 10), the Berezin identity "
           "(check 13), the supplied-inventory g* arithmetic (check "
           "14), and the carrier package (both embedded carriers: "
           "M_3(C) dim 9, count 3, re-computed here) — the ENTIRE "
           "selection lives in the unsupplied clause CL")

    report(d1.get("kernel_char_count") == 8
           and d1.get("kernel_c3_orbit_count") == 4
           and d0.get("kernel_char_count") == 20
           and d0.get("kernel_c3_orbit_count") == 8
           and d1.get("carrier_count") == d0.get("carrier_count") == 3,
           "[D] turn-1 inversion-guard compliance (computed): nothing "
           "is forced from the matched 3 = 3 — the kernel-global count "
           "readouts are 8/4 (K1) and 20/8 (K0), never 3; the only "
           "reading yielding 3 (carrier + hw=1) TIES; and the "
           "discriminating certificates (vanishing order, g_eff, "
           "tangent flatness) consume only spectra — no count, "
           "carrier, or species-label input anywhere in their chain")
    residual("CL is NOT retained and is not granted here; it is B-Z2 "
             "restated in the retained SB row's per-dof currency, and "
             "on this surface (given the parent carrier certificates) "
             "it is strictly stronger than the bare point-like-zero-"
             "set clause (boundary B-F2)")
    residual("finite volumes/grids: eigensolver L in {2,4,6,8,12}, "
             "symbol grids L in {12,24,48,64,128} licensed by check 4; "
             "wrap-convention (PBC/APBC, L mod 4) data recorded as "
             "convention-graded, not analyzed exhaustively (boundary "
             "B-F4)")
    residual("the supplier sweep covers the enumerated determinant/"
             "Matsubara/heat-kernel, thermal/g*/entropy, and "
             "isotropy/Lorentz "
             "families enumerated in the note's section 4; "
             "exhaustiveness over all retained rows is not claimed "
             "(boundary B-F5)")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: B-Z2 ('the massless species density is finite') "
              "has NO retained supplier on the determinant/Matsubara,")
        print("         thermal, or isotropy surfaces within the stated "
              "scope. Every enumerated retained-grade det-family")
        print("         candidate is staggered-scoped, hypothesis-")
        print("         conditional (m > 0 / invertibility), "
              "matrix-agnostic, supplied, or off-sector; the naive")
        print("         per-volume zeta divergence is closed (finite on "
              "BOTH branches). The objects that DO degenerate on K0")
        print("         are computed and named in retained currency: det "
              "vanishing order extensive (20,56,68) vs bounded (8,8,8);")
        print("         g_eff(T) divergent ~T^-2 vs finite plateau ~1; "
              "exact flat tangent directions vs isotropic cones.")
        print("         phi = -1 remains underived; B-Z2 is sharpened to "
              "one maximally concrete missing row: a future retained-grade")
        print("         statement binding the REALIZED matter kernel with "
              "bounded g_eff (equivalently bounded det-vanishing")
        print("         order per volume; equivalently ker = carrier with "
              "conical dispersion). Any of these, at retained grade,")
        print("         selects phi = -1 immediately given the "
              "certificates above.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
