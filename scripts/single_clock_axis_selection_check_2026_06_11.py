"""Single-clock axis selection: W-transport audit of every retained candidate
axis-selecting structure (companion runner of
SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md).

Context: the 2026-06-11 re-scope of
AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md
demoted evolution-axis selection from theorem to declared premise (B-AXIS),
because the staggered surface is exactly invariant under the conjugated
exchange W = P_{tau<->1} . diag((-1)^{x_tau x_1}). This runner asks the
follow-up question hostilely: does ANY retained structure break the
tau<->x_1 exchange, so that the axis could be derived rather than declared?

Blocks (tags: [A] exact algebraic fact, [B] cross-note textual/one-hop
import check, [C] first-principles compute on explicit small lattices,
[D] falsification / discipline leg):

  [S]       baseline exchange certificate (recomputed, with the
            no-sign-field falsifier).
  [RT-RP]   W-transport of the RP/OS reconstruction data: the conjugated
            temporal reflection IS a signed x_1 reflection; the
            one-particle OS kernel about x_1 is exactly unitarily
            equivalent to the temporal one (identical Hermitian spectra,
            identical positivity status). This computes the failure of
            the "only the temporal axis has a GNS/positivity structure"
            escape: the spatial construction is obtained for free by
            conjugation.
  [RT-REC]  W-transport of the record/durability structure: the Record
            axiom and the retained record rows are axis-blind by their
            own text (no time metric, no forced formation, supplied
            clock); durability (= operator-order monotonicity of the
            registered-record counter) is unitary-transport invariant
            (computed); the registration-cone slice package (CAP-K
            shape) maps exactly onto the x_1-axis package.
  [RT-ANOM] W-transport of the anomaly/chirality structure: the
            staggered chirality grading eps(x) and the chiral
            anticommutation are exactly W-invariant; the anomaly
            consumer's own text says it constrains the COUNT d_t, not
            the axis label.
  [PIN]     the sharpened pin: computed minimal axis-selecting inputs.
            Antiperiodic-tau/periodic-space BCs break W exactly (and a
            relabeling-invariant kernel-dimension discriminator shows no
            lattice exchange of any kind survives); symmetric BCs
            restore the exchange symmetry, so the selecting datum is the
            per-axis Z_2 BC asymmetry, not the BC itself; asymmetric
            extents L_tau != L_1 also discriminate (regulator-level).
  [D]       composition discipline: scope-boundary N2/N4/N5 consumed
            verbatim; the companion fixed note's declared B-AXIS and its
            named candidate suppliers; this note's no-contradiction
            wording guards.

Deterministic, no RNG in any load-bearing leg, runtime well under 5 min.
TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import os

import numpy as np

PASS = 0
FAIL = 0


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}][{tag}] {label}" + (f"  -- {detail}" if detail else ""))


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord=2))


# ---------------------------------------------------------------------
# staggered surface: antisymmetrized KS hop matrix, time-first phases
# eta_0 = 1, eta_mu(x) = (-1)^(x_0+...+x_{mu-1}); per-axis BC flags
# ---------------------------------------------------------------------


def build_surface(Ls, mass: float = 0.3, apbc=()):
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)

    def eta(mu, x):
        return (-1) ** sum(x[:mu])

    M = np.zeros((N, N))
    sectors = []
    for mu in range(4):
        Mmu = np.zeros((N, N))
        for x in sites:
            y = list(x)
            y[mu] = (y[mu] + 1) % Ls[mu]
            bc = -1.0 if (mu in apbc and x[mu] == Ls[mu] - 1) else 1.0
            Mmu[idx[x], idx[tuple(y)]] += bc * eta(mu, x)
            Mmu[idx[tuple(y)], idx[x]] -= bc * eta(mu, x)
        sectors.append(Mmu)
        M += Mmu
    M += mass * np.eye(N)
    return M, sectors, sites, idx


def exchange_W(Ls, sites, idx):
    N = len(sites)
    P = np.zeros((N, N))
    S = np.zeros((N, N))
    for x in sites:
        P[idx[(x[1], x[0], x[2], x[3])], idx[x]] = 1.0
        S[idx[x], idx[x]] = (-1.0) ** (x[0] * x[1])
    return P @ S, P


def read_doc(name: str) -> str:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", name)
    return open(path, encoding="utf-8").read()


# ---------------------------------------------------------------------
# [S] baseline exchange certificate
# ---------------------------------------------------------------------


def block_S(M, W, P, N, mass):
    print()
    print("-" * 72)
    print("[S] BASELINE: the exact tau<->x_1 exchange certificate (recomputed)")
    print("-" * 72)
    record("C", "W = P_{tau<->1} diag((-1)^{x_tau x_1}) is orthogonal",
           opnorm(W @ W.T - np.eye(N)) < 1e-14, f"N = {N} sites, mass = {mass}")
    inv = opnorm(W @ M @ W.T - M)
    record("C", "exact surface invariance: ||W M_KS W^T - M_KS|| = 0 (periodic BCs)",
           inv < 1e-13, f"resid = {inv:.2e}")
    naive = opnorm(P @ M @ P.T - M)
    record("D", "falsifier: plain axis swap WITHOUT the sign field fails",
           naive > 1.0, f"resid = {naive:.4f} >> 0 (the certificate is non-trivial)")


# ---------------------------------------------------------------------
# [RT-RP] transport of the RP/OS reconstruction data
# ---------------------------------------------------------------------


def block_RT_RP(M, W, Ls, sites, idx, N):
    print()
    print("-" * 72)
    print("[RT-RP] ROUTE A1: does the OS/GNS construction anchor the axis? (computed: NO)")
    print("-" * 72)

    # temporal site reflection theta_tau : t -> L_t - 1 - t
    Th_tau = np.zeros((N, N))
    R1 = np.zeros((N, N))
    for x in sites:
        Th_tau[idx[(Ls[0] - 1 - x[0], x[1], x[2], x[3])], idx[x]] = 1.0
        R1[idx[(x[0], Ls[1] - 1 - x[1], x[2], x[3])], idx[x]] = 1.0

    # the conjugated reflection is a SIGNED x_1 reflection: same permutation
    # support as R1, orthogonal involution
    Th1p = W @ Th_tau @ W.T
    invol = opnorm(Th1p @ Th1p - np.eye(N))
    support = opnorm(np.abs(Th1p) - R1)
    record("C", "W theta_tau W^T is an orthogonal involution supported EXACTLY on the "
           "x_1 site reflection x_1 -> L-1-x_1 (a signed spatial reflection)",
           invol < 1e-14 and support < 1e-14,
           f"involution resid = {invol:.1e}, |support - R_1| = {support:.1e}")

    C = np.linalg.inv(M)
    cinv = opnorm(W @ C @ W.T - C)
    record("C", "the covariance (one-particle Euclidean kernel) is W-invariant: "
           "W M^{-1} W^T = M^{-1}", cinv < 1e-12, f"resid = {cinv:.2e}")

    # one-particle OS kernels: G_a[x,y] = (Theta_a C)[x,y] on the positive half
    half_tau = [idx[s] for s in sites if s[0] >= Ls[0] // 2]
    half_1 = [idx[s] for s in sites if s[1] >= Ls[1] // 2]
    G_tau = (Th_tau @ C)[np.ix_(half_tau, half_tau)]
    G_1p = (Th1p @ C)[np.ix_(half_1, half_1)]
    Wr = W[np.ix_(half_tau, half_1)]
    orth = opnorm(Wr @ Wr.T - np.eye(len(half_tau)))
    trans = opnorm(Wr @ G_1p @ Wr.T - G_tau)
    record("C", "the x_1-axis OS kernel is EXACTLY unitarily equivalent to the "
           "temporal one: W_r G_1 W_r^T = G_tau (W_r = W restricted to halves, orthogonal)",
           orth < 1e-14 and trans < 1e-12,
           f"||W_r W_r^T - I|| = {orth:.1e}, transport resid = {trans:.2e}")

    ht = np.sort(np.linalg.eigvalsh(0.5 * (G_tau + G_tau.T)))
    h1 = np.sort(np.linalg.eigvalsh(0.5 * (G_1p + G_1p.T)))
    spec = float(np.max(np.abs(ht - h1)))
    record("C", "identical Hermitian spectra and identical minimum eigenvalue: "
           "WHATEVER positivity status the tau construction has, the x_1 construction "
           "has identically — the 'no spatial GNS structure' escape is FALSE",
           spec < 1e-12 and abs(ht[0] - h1[0]) < 1e-12,
           f"max |spec diff| = {spec:.1e}, min eig (both) = {ht[0]:.6f}")


# ---------------------------------------------------------------------
# [RT-REC] transport of the record/durability structure
# ---------------------------------------------------------------------


def block_RT_REC(sec, W, Ls, sites, idx):
    print()
    print("-" * 72)
    print("[RT-REC] ROUTE A2: does record durability anchor the axis? (textual + computed: NO)")
    print("-" * 72)

    ax = read_doc("MINIMAL_AXIOMS_2026-06-05.md")
    record("B", "Record axiom is axis-blind by its own text: a record supplies no "
           "'time metric' (verbatim in the exclusion list)",
           "time metric" in ax and "Durable means fixed once registered" in ax,
           "MINIMAL_AXIOMS_2026-06-05.md")

    rf = read_doc("RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md")
    record("B", "record formation is not forced (retained_no_go): 'at least one record "
           "exists' is NOT an axiom consequence, so no axis can be derived from it "
           "unconditionally",
           "does **not** hold unconditionally" in rf, "record-formation no-go quoted")

    cr = read_doc("POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md")
    record("B", "the clock map is supplied, never derived from records (retained_no_go): "
           "'Without the supplied `tau`, the same record history supports many "
           "inequivalent rates' — the event ORDER carries no lattice-axis label",
           "Without the supplied `tau`, the same record history supports many"
           " inequivalent\nrates." in cr.replace("\r", ""),
           "clock/rate interface quoted")

    cap = read_doc("OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md")
    record("B", "the CAP-K registration cone is axis-CONDITIONAL, not axis-selecting: "
           "its dynamics clause (REG-dyn) consumes the framework H and its window "
           "(REG-tau) consumes a supplied clock — both downstream of B-AXIS, so "
           "citing it for axis selection would be circular",
           "(REG-dyn)" in cap and "(REG-tau)" in cap
           and "generated by `H + V_k`" in cap
           and "supplied clock window `tau`" in cap
           and "not derived from record counts" in cap,
           "CAP-K note clauses present")

    # durability = operator-order monotonicity; unitary transport preserves it
    # (A <= B  <=>  U A U^dag <= U B U^dag). Computed toy: a registered-record
    # counter N_0 <= N_1 <= N_2 <= N_3 on a 3-qubit register, conjugated by a
    # deterministic unitary (matrix exponential of a fixed Hermitian), stays
    # monotone with the SAME increments spectrum.
    e = np.zeros((8,)); proj = []
    for j in range(4):
        v = np.zeros((8, 1)); v[j, 0] = 1.0
        proj.append(v @ v.T)
    Ns = [sum(proj[:k], np.zeros((8, 8))) for k in range(5)]
    mono = all(np.linalg.eigvalsh(Ns[k + 1] - Ns[k]).min() > -1e-14 for k in range(4))
    K = np.zeros((8, 8))
    for a in range(8):
        for b in range(8):
            K[a, b] = np.sin(1.0 + 0.37 * a * b)  # fixed, deterministic
    K = 0.5 * (K + K.T)
    w, V = np.linalg.eigh(K)
    U = V @ np.diag(np.exp(1j * w)) @ V.conj().T
    Ns_t = [U @ Nk @ U.conj().T for Nk in Ns]
    mono_t = all(np.linalg.eigvalsh(Ns_t[k + 1] - Ns_t[k]).min() > -1e-12 for k in range(4))
    incr = max(
        float(np.max(np.abs(
            np.sort(np.linalg.eigvalsh(Ns_t[k + 1] - Ns_t[k]))
            - np.sort(np.linalg.eigvalsh(Ns[k + 1] - Ns[k])))))
        for k in range(4))
    record("A", "durability ('fixed once registered, never un-registered') is "
           "operator-order monotonicity of the record counter, and operator order is "
           "unitary-transport invariant: the conjugated counter is monotone with the "
           "same increment spectra — durability CANNOT distinguish W-related axes",
           mono and mono_t and incr < 1e-12,
           f"monotone before/after = {mono}/{mono_t}, max increment-spec diff = {incr:.1e}")

    # registration-cone slice package: choosing axis a as evolution leaves the
    # in-slice hop operator D^(a); W maps the axis-1 package exactly onto the
    # axis-tau package (same generator, same cone, same registration capacity)
    N = len(sites)
    sl_t0 = [idx[s] for s in sites if s[0] == 0]
    sl_x0 = [idx[s] for s in sites if s[1] == 0]
    D_tau = (sec[1] + sec[2] + sec[3])[np.ix_(sl_t0, sl_t0)]
    D_1 = (sec[0] + sec[2] + sec[3])[np.ix_(sl_x0, sl_x0)]
    Wsl = W[np.ix_(sl_t0, sl_x0)]
    orth = opnorm(Wsl @ Wsl.T - np.eye(len(sl_t0)))
    trans = opnorm(Wsl @ D_1 @ Wsl.T - D_tau)
    st = np.sort(np.abs(np.linalg.eigvals(D_tau)))
    s1 = np.sort(np.abs(np.linalg.eigvals(D_1)))
    record("C", "the slice/registration-cone package transports exactly: W maps the "
           "x_1-as-evolution in-slice hop operator onto the tau-as-evolution one "
           "(W_sl D^(1) W_sl^T = D^(tau), identical spectra) — every cone constant, "
           "LR velocity, and CAP-K capacity built on the slice dynamics is equal",
           orth < 1e-14 and trans < 1e-13
           and float(np.max(np.abs(st - s1))) < 1e-12,
           f"slice dim = {len(sl_t0)}, transport resid = {trans:.1e}, "
           f"max |spec diff| = {float(np.max(np.abs(st - s1))):.1e}")


# ---------------------------------------------------------------------
# [RT-ANOM] transport of the anomaly/chirality structure
# ---------------------------------------------------------------------


def block_RT_ANOM(M, sec, W, sites, mass, N):
    print()
    print("-" * 72)
    print("[RT-ANOM] ROUTE B: does the anomaly/chirality chain pick the axis? (NO: count, not label)")
    print("-" * 72)

    E = np.diag([(-1.0) ** sum(x) for x in sites])
    A = M - mass * np.eye(N)
    et = opnorm(W @ E @ W.T - E)
    ac = opnorm(A @ E + E @ A)
    record("C", "the staggered chirality grading eps(x) = (-1)^{sum x_mu} is exactly "
           "W-invariant and the chiral anticommutation {D_hop, eps} = 0 is preserved: "
           "the chirality structure is axis-label-blind",
           et < 1e-14 and ac < 1e-13, f"||W E W^T - E|| = {et:.1e}, ||{{A,E}}|| = {ac:.1e}")

    an = read_doc("ANOMALY_FORCES_TIME_THEOREM.md")
    fixed = read_doc("AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md")
    record("B", "the anomaly consumer constrains the COUNT d_t, 'not\n   which axis is "
           "temporal' (its own non-circularity section), and the fixed note's "
           "B-AXIS 'references no anomaly content' — route B supplies no axis label "
           "by both notes' own text",
           "not\n   which axis is temporal" in an.replace("\r", "")
           and "references no anomaly" in fixed,
           "both texts quoted")


# ---------------------------------------------------------------------
# [PIN] the sharpened pin: computed minimal axis-selecting inputs
# ---------------------------------------------------------------------


def block_PIN(Ls, mass, W):
    print()
    print("-" * 72)
    print("[PIN] THE SHARPENED PIN: what WOULD break the exchange (computed witnesses)")
    print("-" * 72)

    M_ap, _, _, _ = build_surface(Ls, mass, apbc=(0,))
    r_ap = opnorm(W @ M_ap @ W.T - M_ap)
    record("C", "antiperiodic-tau / periodic-space BCs break the exchange EXACTLY: "
           "||W M_ap W^T - M_ap|| > 0 — one per-axis Z_2 BC datum suffices to select "
           "the axis on this surface",
           r_ap > 1.0, f"resid = {r_ap:.6f} (= 2*sqrt(2) on this block)")

    M_both, _, _, _ = build_surface(Ls, mass, apbc=(0, 1))
    r_both = opnorm(W @ M_both @ W.T - M_both)
    record("C", "falsification leg: antiperiodic in BOTH tau and x_1 RESTORES the exact "
           "exchange symmetry — the axis-selecting datum is the BC ASYMMETRY between "
           "the axes, not the antiperiodic wrap itself",
           r_both < 1e-13, f"resid = {r_both:.1e}")

    _, sec_ap, _, _ = build_surface(Ls, 0.0, apbc=(0,))
    kt = int(np.sum(np.abs(np.linalg.eigvals(sec_ap[0])) < 1e-9))
    k1 = int(np.sum(np.abs(np.linalg.eigvals(sec_ap[1])) < 1e-9))
    record("C", "relabeling-invariant discriminator: with antiperiodic-tau the temporal "
           "hop sector has TRIVIAL kernel while the periodic x_1 sector has a nonzero "
           "kernel — no exchange map of any kind (signed, conjugated, or otherwise) "
           "can identify the two sectors once the BC datum is supplied",
           kt == 0 and k1 > 0, f"dim ker: temporal(apbc) = {kt}, x_1(pbc) = {k1}")

    _, sec_ext, _, _ = build_surface((6, 4, 2, 2), 0.0)
    st = np.sort(np.abs(np.linalg.eigvals(sec_ext[0])))
    s1 = np.sort(np.abs(np.linalg.eigvals(sec_ext[1])))
    gap = abs(float(st.max()) - float(s1.max()))
    record("C", "asymmetric extents L_tau != L_1 also discriminate (sector spectral "
           "radii differ) — but extents are finite-block regulator data, declared, "
           "not framework axioms; recorded as the weaker regulator-level datum",
           gap > 0.1, f"max|spec|: temporal = {float(st.max()):.4f}, "
           f"x_1 = {float(s1.max()):.4f} on (6,4,2,2)")

    fixed = read_doc("AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md")
    record("D", "the pin addresses ONLY the axis-label clause of B-AXIS.2 (= N4): "
           "B-AXIS.1 (the supplied 2a_tau, = N2) and B-AXIS.3 (no commuting factor "
           "clock, = N5) remain declared premises exactly per the scope boundary; the "
           "fixed note's candidate-supplier sentence names the BC route this pin "
           "sharpens",
           "(B-AXIS.1)" in fixed and "(B-AXIS.3)" in fixed
           and "antiperiodic temporal BC" in fixed,
           "B-AXIS clauses + candidate-supplier sentence present")


# ---------------------------------------------------------------------
# [D] composition / no-contradiction discipline
# ---------------------------------------------------------------------


def block_D():
    print()
    print("-" * 72)
    print("[D] COMPOSITION DISCIPLINE (scope boundary consumed, not contradicted)")
    print("-" * 72)

    sb = read_doc("SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md")
    record("D", "scope-boundary clauses consumed verbatim: N2 (time step), N4 "
           "(axis/transfer uniqueness), N5 (commuting factors), and 'Stone uniqueness "
           "is transfer-relative and tau-relative'",
           "uniqueness of the reflection-positive axis or transfer construction" in sb
           and "exclusion of independent commuting transfer factors" in sb
           and "the physical time step / block spacing `tau`" in sb
           and "Stone uniqueness is transfer-relative and tau-relative." in sb,
           "N2/N4/N5 + repair line present")

    note = read_doc("SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md")
    record("D", "this note is a narrow no-go that does NOT claim the axis is derived: "
           "honest-outcome strings present, forbidden closure strings absent",
           "narrow no-go" in note and "B-AXIS" in note
           and "the axis is hereby derived" not in note
           and "B-AXIS is retired" not in note
           and "axis selection is derived from the Record axiom" not in note,
           "wording guards hold")

    record("D", "no-go is consistent with the boost-faith and cubic-anisotropy "
           "boundaries: no boost action is derived (no Lorentz content consumed), and "
           "no SO(4) wording is used (the c_t = c_s primitive makes the surface MORE "
           "exchange-symmetric, which this note's direction respects)",
           "matter-attachment" in read_doc(
               "QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md")
           and "c_t = c_s" in read_doc("SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md"),
           "one-hop boundary texts present")


# ---------------------------------------------------------------------
# main
# ---------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("SINGLE-CLOCK AXIS SELECTION: W-TRANSPORT AUDIT (2026-06-11)")
    print("=" * 72)
    print()
    print("Question: does any retained structure (record/durability, OS/GNS,")
    print("registration cone, anomaly/chirality) break the tau<->x_1 exchange")
    print("W = P_{tau<->1} diag((-1)^{x_tau x_1}), so the evolution axis could be")
    print("derived instead of declared (B-AXIS)?  Answer computed below: NO —")
    print("every candidate transports exactly; the sharpened pin is one per-axis")
    print("Z_2 datum (BC asymmetry) or an equivalent registration-direction bridge.")

    Ls = (4, 4, 2, 2)
    mass = 0.3
    M, sec, sites, idx = build_surface(Ls, mass)
    N = len(sites)
    W, P = exchange_W(Ls, sites, idx)
    print(f"\n  surface: block {Ls}, N = {N} sites, mass = {mass}, periodic BCs")

    block_S(M, W, P, N, mass)
    block_RT_RP(M, W, Ls, sites, idx, N)
    block_RT_REC(sec, W, Ls, sites, idx)
    block_RT_ANOM(M, sec, W, sites, mass, N)
    block_PIN(Ls, mass, W)
    block_D()

    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
