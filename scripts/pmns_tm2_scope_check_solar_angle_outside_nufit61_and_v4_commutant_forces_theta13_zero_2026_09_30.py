#!/usr/bin/env python3
"""Class-A scope check for the PMNS TM2 notes (supports the 2026-09-30 corrigenda).

The TM2 notes (trimaximal column from the recorded C3-singlet sector; magic residual and
V4 = <S, P23>; site-basis K/CPT predicate; theta13 / sqrt2 note) present the TM2 pattern
"one trimaximal column W = (1,1,1)/sqrt3 + mu-tau residual + free theta13" as a derived
structure.  This check computes, with numpy only and fixed seeds, what that construction
actually gives:

  (A) Solar angle.  With the trimaximal column as the second PMNS column and U_e = I, the
      sum rule is s12^2 = 1/(3 c13^2) >= 1/3.  The repo-quoted NuFIT-6.1 3-sigma rectangle
      (docs/PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08.md:28,
      scripts/audit_companion_pmns_dcp_nufit6_comparator_refresh_exact.py) is
      s12^2 in [0.2893, 0.3295], s13^2 in [0.02064, 0.02420].  TM2 is outside it for every
      s13^2, and a trimaximal (1/3,1/3,1/3) column is outside it at every mass position.
  (B) V4 = <S, P23>.  The Hermitian commutant of V4 is 3-dimensional, spanned by the
      projectors onto W, xi = (2,-1,-1)/sqrt6, eta = (0,1,-1)/sqrt2.  Every V4-invariant M
      with a non-degenerate spectrum has electron row |U_ej|^2 = {0, 1/3, 2/3}: theta13 = 0
      (tribimaximal), not "free".  The runner
      scripts/pmns_tm2_magic_residual_dynamical_generator_runner.py checks the trimaximal
      column and equal mu,tau rows for such an M but never |U_e3|^2; reproduced here.
  (C) What would keep theta13 free is not a unitary P23 commutation but an antiunitary
      mu-tau reflection P23 M* P23 = M with [M,S] = 0.  It gives s23^2 = 1/2, |sin delta| = 1
      with theta13 free, but the solar angle stays at the TM2 value (outside the rectangle).
      This is a "what would be needed" computation, not a framework derivation.
  (D) The runner's "theta13 proxy" is the minimum over all nine |U|^2; its witness has that
      minimum in the tau row; its electron row is far from the band.
  (E) theta13 note: PMNS = R12(theta_e)^T (xi, W, eta) gives s13^2 = sin^2(theta_e)/2 exactly,
      but the second column is no longer trimaximal and s12^2 is 0.20 (or 0.48).

Nothing here derives a PMNS angle, adopts TM1, or sets an audit status.
"""

from __future__ import annotations

import math

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ---- repo-quoted NuFIT-6.1 3-sigma rectangle (normal ordering) ----
# docs/PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08.md:28
S12_LO, S12_HI = 0.2893, 0.3295
S13_LO, S13_HI = 0.02064, 0.02420          # union of the no-SK and with-SK ranges
S13_OBS = 0.02220                          # central value used by the theta13 runner

# ---- carrier objects on the hw=1 triplet ----
W = np.ones(3) / math.sqrt(3)
XI = np.array([2.0, -1.0, -1.0]) / math.sqrt(6)
ETA = np.array([0.0, 1.0, -1.0]) / math.sqrt(2)
I3 = np.eye(3)
PW = np.outer(W, W)
S = 2 * PW - I3                                            # magic reflection
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], float)   # graph-first mu-tau swap
R_SP = S @ P23                                             # the third involution of V4
DBL = np.column_stack([XI, ETA])                           # real doublet basis


def observables(U):
    """(s12^2, s13^2, s23^2, sin delta) for a unitary with rows (e,mu,tau), columns (nu1,nu2,nu3)."""
    a = np.abs(U) ** 2
    s13 = a[0, 2]
    c13 = 1.0 - s13
    s12 = a[0, 1] / c13
    s23 = a[1, 2] / c13
    jarl = (U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])).imag
    den = math.sqrt(max(s12 * (1 - s12) * s23 * (1 - s23), 0.0)) * c13 * math.sqrt(max(s13, 0.0))
    sind = jarl / den if den > 1e-14 else float("nan")
    return s12, s13, s23, sind


def order_columns(V):
    """TM2 ordering: nu2 = the trimaximal column W; nu1 = the other column with larger electron content."""
    tri = [j for j in range(3) if np.allclose(np.abs(V[:, j]) ** 2, 1 / 3, atol=1e-8)]
    assert len(tri) == 1, tri
    others = sorted((j for j in range(3) if j != tri[0]), key=lambda j: -abs(V[0, j]) ** 2)
    return V[:, [others[0], tri[0], others[1]]]


# Hermitian basis (9 real dimensions) and commutant machinery
BASIS = []
for i in range(3):
    E = np.zeros((3, 3), complex)
    E[i, i] = 1
    BASIS.append(E)
for i in range(3):
    for j in range(i + 1, 3):
        E = np.zeros((3, 3), complex)
        E[i, j] = E[j, i] = 1
        BASIS.append(E)
        E = np.zeros((3, 3), complex)
        E[i, j] = 1j
        E[j, i] = -1j
        BASIS.append(E)


def _vec(X):
    return np.concatenate([X.real.ravel(), X.imag.ravel()])


def commutant_basis(gens):
    """Real basis (as Hermitian matrices) of {M Hermitian : [M, g] = 0 for g in gens}."""
    cols = [np.concatenate([_vec(g @ B - B @ g) for g in gens]) for B in BASIS]
    A = np.array(cols).T
    _, s, vt = np.linalg.svd(A)
    rank = int((s > 1e-10).sum())
    return [sum(c * B for c, B in zip(v, BASIS)) for v in vt[rank:]]


def group_closure(gens):
    G = [I3.astype(complex)]
    changed = True
    while changed:
        changed = False
        for g in list(G):
            for h in gens:
                gh = g @ h
                if not any(np.allclose(gh, x) for x in G):
                    G.append(gh)
                    changed = True
    return G


def main() -> int:
    print("=" * 76)
    print("PMNS TM2 SCOPE CHECK: solar angle vs NuFIT-6.1, and V4 commutant => theta13 = 0")
    print("=" * 76)

    # ------------------------------------------------------------------ (A)
    print("\n(A) TM2 solar angle s12^2 = 1/(3 c13^2) against the repo-quoted NuFIT-6.1 rectangle")
    s12_at_obs = 1.0 / (3.0 * (1.0 - S13_OBS))
    check("TM2 at s13^2 = 0.0222 gives s12^2 = 0.3409, above the 3-sigma top 0.3295",
          s12_at_obs > S12_HI, f"s12^2={s12_at_obs:.5f}, range=[{S12_LO},{S12_HI}]")
    s12_lo_edge = 1.0 / (3.0 * (1.0 - S13_LO))
    s12_hi_edge = 1.0 / (3.0 * (1.0 - S13_HI))
    check("across the whole quoted s13^2 range TM2 gives s12^2 in [0.3404, 0.3416], all outside",
          s12_lo_edge > S12_HI and s12_hi_edge > S12_HI,
          f"[{s12_lo_edge:.5f},{s12_hi_edge:.5f}]")
    grid = np.linspace(0.0, 0.6, 600001)
    check("for EVERY s13^2 in [0,0.6] the TM2 sum rule gives s12^2 >= 1/3 > 0.3295",
          float((1.0 / (3.0 * (1.0 - grid))).min()) >= 1 / 3 - 1e-15 and 1 / 3 > S12_HI,
          "minimum 1/3 at s13^2 = 0")
    ue1 = ((1 - S12_HI) * (1 - S13_HI), (1 - S12_LO) * (1 - S13_LO))
    ue2 = (S12_LO * (1 - S13_HI), S12_HI * (1 - S13_LO))
    ue3 = (S13_LO, S13_HI)
    third = 1.0 / 3.0
    check("a trimaximal electron-row entry 1/3 lies outside the image of the rectangle at every "
          "mass position (nu1, nu2, nu3)",
          not (ue1[0] <= third <= ue1[1]) and not (ue2[0] <= third <= ue2[1])
          and not (ue3[0] <= third <= ue3[1]),
          f"|Ue1|^2 in [{ue1[0]:.4f},{ue1[1]:.4f}], |Ue2|^2 in [{ue2[0]:.4f},{ue2[1]:.4f}], "
          f"|Ue3|^2 in [{ue3[0]:.5f},{ue3[1]:.5f}]")

    # ------------------------------------------------------------------ (B)
    print("\n(B) V4 = <S, P23>: commutant, electron row, theta13")
    V4 = group_closure([S.astype(complex), P23.astype(complex)])
    check("<S,P23> is the Klein four-group (order 4, abelian, involutions)",
          len(V4) == 4 and all(np.allclose(g @ g, I3) for g in V4)
          and all(np.allclose(a @ b, b @ a) for a in V4 for b in V4))
    cS = commutant_basis([S])
    cP = commutant_basis([P23])
    cV = commutant_basis([S, P23])
    check("Hermitian commutant of S alone has real dimension 5 (1 + 2x2 block)", len(cS) == 5, f"dim={len(cS)}")
    check("Hermitian commutant of P23 alone has real dimension 5", len(cP) == 5, f"dim={len(cP)}")
    check("Hermitian commutant of V4 has real dimension 3", len(cV) == 3, f"dim={len(cV)}")
    proj = [np.outer(x, x.conj()) for x in (W, XI, ETA)]
    stacked = np.vstack([np.array([_vec(M) for M in cV]), np.array([_vec(P) for P in proj])])
    check("that commutant is exactly span{P_W, P_xi, P_eta}",
          np.linalg.matrix_rank(stacked, tol=1e-9) == 3
          and all(np.allclose(P @ S, S @ P) and np.allclose(P @ P23, P23 @ P) for P in proj))

    rng = np.random.default_rng(20260930)
    rows = set()
    ordered_obs = []
    n_used = 0
    for _ in range(3000):
        M = sum(rng.normal() * X for X in cV)
        w, V = np.linalg.eigh(M)
        if np.min(np.diff(w)) < 1e-6:
            continue
        n_used += 1
        rows.add(tuple(np.round(np.sort(np.abs(V[0]) ** 2), 8)))
        ordered_obs.append(observables(order_columns(V)))
    check("every non-degenerate V4-invariant M has electron row |U_ej|^2 = {0, 1/3, 2/3}",
          rows == {(0.0, round(1 / 3, 8), round(2 / 3, 8))}, f"{n_used} samples, patterns={sorted(tuple(float(x) for x in r) for r in rows)}")
    obs = np.array(ordered_obs)
    check("hence the TM2 ordering gives s13^2 = 0, s12^2 = 1/3, s23^2 = 1/2 (tribimaximal), never 0.022",
          np.allclose(obs[:, 1], 0, atol=1e-10) and np.allclose(obs[:, 0], 1 / 3, atol=1e-9)
          and np.allclose(obs[:, 2], 0.5, atol=1e-9),
          f"max s13^2={obs[:, 1].max():.2e}")

    # the runner's own construction (scripts/pmns_tm2_magic_residual_dynamical_generator_runner.py, part D)
    rr = np.random.default_rng(7)
    A = rr.standard_normal((3, 3))
    A = A + A.T
    M = A.copy()
    for g in V4:
        M = (M + g.real @ M @ g.real.T) / 2.0
    M = (M + M.T) / 2.0
    en, Un = np.linalg.eigh(M)
    Pm = np.abs(Un) ** 2
    check("the runner's own V4-symmetrised M_nu (seed 7): trimaximal column and equal mu,tau rows, "
          "but electron row (0,1/3,2/3)",
          any(np.allclose(Pm[:, j], 1 / 3) for j in range(3)) and np.allclose(Pm[1], Pm[2])
          and np.allclose(np.sort(Pm[0]), [0, 1 / 3, 2 / 3], atol=1e-9),
          f"electron row={np.round(np.sort(Pm[0]), 6).tolist()}")

    # degenerate doublet block: commutes with V4 but fixes no mixing angle
    Md = 0.7 * PW + 1.3 * (I3 - PW)
    phi = math.radians(20.0)
    v_a = math.cos(phi) * XI + math.sin(phi) * ETA
    v_b = -math.sin(phi) * XI + math.cos(phi) * ETA
    ev = np.sort(np.linalg.eigvalsh(Md))
    check("a V4-invariant M with a degenerate doublet block has a repeated eigenvalue (two equal masses) "
          "and every rotated doublet basis is an eigenbasis: theta13 is then not fixed by M",
          np.allclose(Md @ S, S @ Md) and np.allclose(Md @ P23, P23 @ Md)
          and np.isclose(ev[1], ev[2]) and np.allclose(Md @ v_a, 1.3 * v_a) and np.allclose(Md @ v_b, 1.3 * v_b),
          f"eigenvalues={np.round(ev, 3).tolist()}, |U_e3|^2 = (2/3) sin^2(phi) for any phi")

    # record dephasing plus the third flip S.P23 gives the same V4
    rs = np.random.default_rng(5)
    A = rs.normal(size=(3, 3)) + 1j * rs.normal(size=(3, 3))
    A = A + A.conj().T
    Mr = (A + R_SP @ A @ R_SP.conj().T) / 2                 # generic Hermitian M with [M, S.P23] = 0
    P1 = I3 - PW
    Dm = PW @ Mr @ PW + P1 @ Mr @ P1                       # record dephasing D(M)
    w, V = np.linalg.eigh(Dm)
    check("record dephasing D applied to M commuting with S.P23 gives an operator commuting with S, S.P23 "
          "and P23 (V4)",
          np.allclose(Mr @ R_SP, R_SP @ Mr) and np.allclose(Dm @ S, S @ Dm)
          and np.allclose(Dm @ R_SP, R_SP @ Dm) and np.allclose(Dm @ P23, P23 @ Dm))
    check("its electron row is (0, 1/3, 2/3): theta13 = 0 again (the record does not supply a TM1-type pattern)",
          np.allclose(np.sort(np.abs(V[0]) ** 2), [0, 1 / 3, 2 / 3], atol=1e-9),
          f"{np.round(np.sort(np.abs(V[0]) ** 2), 6).tolist()}")

    # ------------------------------------------------------------------ (C)
    print("\n(C) what would keep theta13 free: [M,S]=0 plus an ANTIUNITARY mu-tau reflection (not supplied)")
    rc = np.random.default_rng(11)
    sel = []
    n_refl = 0
    for _ in range(20000):
        a = rc.normal()
        B = rc.normal(size=(2, 2)) + 1j * rc.normal(size=(2, 2))
        B = B + B.conj().T
        M = a * PW + DBL @ B @ DBL.conj().T
        M = (M + P23 @ M.conj() @ P23) / 2                  # impose P23 M* P23 = M
        w, V = np.linalg.eigh(M)
        if np.min(np.diff(w)) < 1e-6:
            continue
        n_refl += 1
        U = order_columns(V)
        o = observables(U)
        if 0.0207 < o[1] < 0.0242:
            sel.append(o)
    sel = np.array(sel)
    check("with the antiunitary reflection and [M,S]=0, theta13 in the data window occurs "
          "(so theta13 is free there)", len(sel) >= 100, f"{len(sel)} of {n_refl} samples")
    check("in that family s23^2 = 1/2 and |sin delta| = 1 exactly",
          np.allclose(sel[:, 2], 0.5, atol=1e-9) and np.allclose(np.abs(sel[:, 3]), 1.0, atol=1e-9))
    check("but s12^2 = 1/(3 c13^2) in [0.3404, 0.3416]: still outside the NuFIT-6.1 3-sigma range",
          np.allclose(sel[:, 0], 1 / (3 * (1 - sel[:, 1])), atol=1e-9) and sel[:, 0].min() > S12_HI,
          f"s12^2 in [{sel[:, 0].min():.5f},{sel[:, 0].max():.5f}]")

    # ------------------------------------------------------------------ (D)
    print("\n(D) the runner's 'theta13 proxy' (part E of the magic-residual runner)")
    r3 = np.random.default_rng(3)
    wit = None
    for _ in range(20000):
        a = r3.uniform(-1, 1)
        b = r3.uniform(-1, 1, 3)
        Bm = np.array([[b[0], b[2]], [b[2], b[1]]])
        Mw = a * PW + DBL @ Bm @ DBL.T
        enw, Uw = np.linalg.eigh(Mw)
        Pw = np.abs(Uw) ** 2
        if any(np.allclose(Pw[:, j], 1 / 3, atol=1e-9) for j in range(3)) and 0.015 < Pw.min() < 0.030:
            wit = Pw
            break
    check("the runner's witness is found (seed 3); its proxy value is the global minimum 0.0213",
          wit is not None and abs(wit.min() - 0.0213) < 5e-4,
          f"min={wit.min():.4f}" if wit is not None else "none")
    row_of_min = int(np.argwhere(wit == wit.min())[0][0])
    check("that minimum sits in the tau row, not the electron row",
          row_of_min == 2, f"row of minimum={row_of_min} (0=e,1=mu,2=tau)")
    check("the witness's electron-row minimum is 0.279, far outside the band 0.015-0.030 (|U_e3|^2 is not 0.0213)",
          wit[0].min() > 0.2, f"electron row={np.round(wit[0], 4).tolist()}")
    check("the witness commutes with S only: its mu and tau rows differ (no mu-tau residual)",
          not np.allclose(wit[1], wit[2]))
    # S-commuting operators CAN reach the observed s13^2 (this part of the note's claim stands)
    phi = math.asin(math.sqrt(1.5 * S13_OBS))
    v1 = math.cos(phi) * XI + math.sin(phi) * ETA
    v3 = -math.sin(phi) * XI + math.cos(phi) * ETA
    Ms = 0.0 * np.outer(v1, v1) + 1.0 * PW + 2.0 * np.outer(v3, v3)
    w, V = np.linalg.eigh(Ms)
    o = observables(order_columns(V))
    check("an S-commuting operator (no P23) reaches s13^2 = 0.0222 with the trimaximal column, "
          "and then s12^2 = 0.3409, outside the range",
          np.allclose(Ms @ S, S @ Ms) and abs(o[1] - S13_OBS) < 1e-9 and o[0] > S12_HI,
          f"s13^2={o[1]:.5f}, s12^2={o[0]:.5f}")

    # ------------------------------------------------------------------ (E)
    print("\n(E) theta13 note: PMNS = R12(theta_e)^T (xi, W, eta)")
    UTBM = np.column_stack([XI, W, ETA])

    def r12(t):
        c, sn = math.cos(t), math.sin(t)
        return np.array([[c, sn, 0], [-sn, c, 0], [0, 0, 1]])

    te = math.asin(math.sqrt(2 * S13_OBS))
    ok_exact = True
    for deg in (5.0, 9.0, 12.16, 13.04):
        t = math.radians(deg)
        ok_exact &= abs(abs((r12(t).T @ UTBM)[0, 2]) - math.sin(t) / math.sqrt(2)) < 1e-12
    check("|U_e3| = sin(theta_e)/sqrt2 holds exactly (the note's sqrt2 relation is right)", ok_exact,
          f"theta_e at s13^2=0.0222: {math.degrees(te):.2f} deg")
    U = r12(te).T @ UTBM
    s12_real = observables(U)[0]
    U2 = r12(-te).T @ UTBM
    s12_flip = observables(U2)[0]
    check("with a real theta_e the PMNS solar angle is 0.2005 (or 0.4813 for the other sign): both outside "
          "[0.2893,0.3295]; the second column is no longer trimaximal",
          not (S12_LO <= s12_real <= S12_HI) and not (S12_LO <= s12_flip <= S12_HI)
          and abs(s12_real - 0.2005) < 5e-4 and abs(s12_flip - 0.4813) < 5e-4,
          f"s12^2={s12_real:.4f} / {s12_flip:.4f}")
    target = 0.5 * (S12_LO + S12_HI)
    cosphi = (1.0 - 3.0 * target * (1.0 - S13_OBS)) / math.sin(2 * te)
    phi_needed = math.degrees(math.acos(cosphi))
    erow = math.cos(te) * UTBM[0] - math.sin(te) * np.exp(1j * math.radians(phi_needed)) * UTBM[1]
    s12_phase = abs(erow[1]) ** 2 / (1.0 - abs(erow[2]) ** 2)
    check("a second (phase) parameter of about 77 degrees would be needed to reach mid-range s12^2; the note "
          "names theta_e as the only residual",
          70.0 < phi_needed < 85.0 and abs(s12_phase - target) < 1e-9 and abs(abs(erow[2]) ** 2 - S13_OBS) < 1e-12,
          f"phi={phi_needed:.1f} deg for s12^2={target:.4f}")

    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: scope check FAILED.")
        return 1
    print("VERDICT: TM2 solar angle is outside the repo-quoted NuFIT-6.1 range at every s13^2; a "
          "V4-invariant (unitary P23) M forces theta13 = 0; the runner's theta13 proxy is not |U_e3|^2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
