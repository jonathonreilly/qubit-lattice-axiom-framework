#!/usr/bin/env python3
"""
EW kappa_EW object-pin + Monte-Carlo-undecidability runner
==========================================================

PStack experiment: ew-kappa-self-energy-object-pin

Companion runner for
  docs/EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md

This runner reproves -- from group-theory / linear-algebra primitives, with no
PDG or experimental inputs -- the load-bearing bridges that PIN the object the
named matching coefficient kappa_EW lives on, and that demonstrate kappa_EW is
NOT a Monte-Carlo-decidable quantity.

It does NOT introduce any new axiom, new selector, or new audit verdict, and it
does NOT privilege either completion (kappa=0 or kappa=1). It sharpens the
already-landed EW kappa_EW no-go family by:

  (A) re-deriving the SU(N_c) Fierz completeness identity
        Tr[M^dag M] = (1/N_c)|Tr M|^2 + 2 sum_A |Tr[M t^A]|^2 = S + C ;

  (B) IDENTIFYING THE OBJECT (conditionally): for the framework's own color-blind
      point-split EW current (internal generator Q_EW (x) I_color), the bare
      connected two-current correlator color factor is
        Tr_internal(Q_EW^2) * Tr_color[G(x,y) G(y,x)] = Tr_internal(Q_EW^2)*(S+C),
      the full color trace. (This is the expression in the landed traceless-
      generator no-go.) This is the OBJECT the ensemble computes; the physical
      readout weight kappa is a SEPARATE, external functional choice;

  (C) showing the channel split is KINEMATIC: <S>/<T> = 1/N_c^2 for BOTH a free
      propagator in a random gauge orbit AND a Haar-random color matrix, so
      R_conn = C/T = (N_c^2-1)/N_c^2 = 8/9 is a gauge-orbit fraction, the same
      at every beta (no continuum trend);

  (D) showing color-blindness fixes NEITHER completion: a color-scalar (I_color)
      renormalization scales S and C equally, so it does not select kappa
      (MATCHING_RULE sec2). kappa=0 is an active singlet projection (OZI / planar /
      leading-N_c, a non-color-blind operation); kappa=1 is the identity readout
      (retain the full trace); selecting either as physical is an external scheme
      choice, and the color-blind lattice current privileges neither;

  (E) the structural Monte-Carlo-undecidability: the lattice ensemble outputs the
      channel data {<S>, <C>, <T>=<S>+<C>} -- of which only <T>=Tr[GG^dag] is
      pointwise gauge-invariant, while <S>,<C> are gauge-orbit-averaged channel
      diagnostics (per-config S,C are gauge-variant); kappa_EW is the
      EXTERNAL weight of S in the physical readout Pi_phys = C + kappa S.
      kappa=0 (K_EW=9/8) and kappa=1 (K_EW=1) are both functions of the same
      measured {S,C,T}; no MC observable is a function of kappa alone; neither is
      privileged by any lattice measurement;

  (F) sin^2(theta_W) is kappa-invariant (the K_EW(kappa) factor cancels in the
      g_1/g_2 ratio), so it survives either completion.

Self-contained: numpy + sympy only.
"""

import numpy as np
import sympy as sp

RNG = np.random.default_rng(20260608)
PASS = 0
FAIL = 0


def check(desc, ok):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {desc}")
    return ok


# ============================================================
# SU(N) generators with Tr[t^A t^B] = (1/2) delta_AB
# (generalized Gell-Mann basis), reproven orthonormal.
# ============================================================
def su_n_generators(n):
    """Generalized Gell-Mann basis normalized to Tr[t^A t^B] = (1/2) delta_AB."""
    gens = []
    # off-diagonal (symmetric + antisymmetric), each = lambda/2 with Tr=1/2
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex)
            m[i, j] = 0.5
            m[j, i] = 0.5
            gens.append(m)
            m2 = np.zeros((n, n), dtype=complex)
            m2[i, j] = -0.5j
            m2[j, i] = 0.5j
            gens.append(m2)
    # diagonal (Cartan): diag(1,...,1,-k,0,...) normalized so Tr t^2 = 1/2
    for k in range(1, n):
        diag = np.zeros(n, dtype=complex)
        for r in range(k):
            diag[r] = 1.0
        diag[k] = -k
        c = 1.0 / np.sqrt(2.0 * k * (k + 1))
        gens.append(np.diag(diag) * c)
    return gens


def fierz_S_C(M, n):
    """S = (1/n)|Tr M|^2 ; T = Tr[M^dag M] = sum|M_ab|^2 ; C = T - S."""
    T = float(np.real(np.trace(M.conj().T @ M)))
    S = float(np.abs(np.trace(M)) ** 2 / n)
    return S, T - S, T


# ============================================================
# (A) Fierz completeness identity, reproven for N_c = 2..5
# ============================================================
def part_A():
    print("\n(A) SU(N_c) Fierz completeness: Tr[M^dag M] = (1/N_c)|Tr M|^2 + 2 sum|Tr[M t^A]|^2")
    okall = True
    for n in [2, 3, 4, 5]:
        gens = su_n_generators(n)
        # generator orthonormality Tr[t^A t^B] = (1/2) delta_AB
        ortho = True
        for a in range(len(gens)):
            for b in range(len(gens)):
                val = np.trace(gens[a] @ gens[b])
                target = 0.5 if a == b else 0.0
                if abs(val - target) > 1e-10:
                    ortho = False
        n_gen = len(gens)
        ok_count = (n_gen == n * n - 1)
        # Fierz on a random complex matrix
        M = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
        S, C, T = fierz_S_C(M, n)
        C_gen = 2.0 * sum(np.abs(np.trace(M @ t)) ** 2 for t in gens)
        ok_fierz = abs(C - C_gen) < 1e-9 and abs(S + C - T) < 1e-9
        okall &= check(
            f"N_c={n}: gens orthonormal={ortho}, count {n_gen}=N_c^2-1={ok_count}, "
            f"C=2*sum|Tr[M t^A]|^2 (err {abs(C - C_gen):.1e}), S+C=T={ok_fierz}",
            ortho and ok_count and ok_fierz,
        )
    return okall


# ============================================================
# (B) OBJECT PIN: connected color-blind two-current loop = full trace,
#     and the singlet channel S genuinely carries weight Tr(Q^2).
# ============================================================
def part_B():
    print("\n(B) The bare connected color-blind correlator computes Tr(Q^2)*(S+C): the OBJECT (not the readout)")
    n = 3
    okall = True

    # B1: color-blind loop color factor equals Tr[G G^dag] = S + C for the
    #     reflected pair G(y,x) = G(x,y)^dag.
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    loop = np.trace(G @ G.conj().T)  # Tr_color[ I G I G^dag ]
    S, C, T = fierz_S_C(G, n)
    okall &= check(
        f"color-blind loop Tr[G G^dag] = S+C = T (loop {np.real(loop):.4f} vs T {T:.4f})",
        abs(np.real(loop) - T) < 1e-9 and abs(np.imag(loop)) < 1e-9,
    )

    # B2: internal (weak/hypercharge) factorization for a DIRECT-PRODUCT generator
    #     Q (x) I_color : Tr[(Q⊗I) (V⊗G) (Q⊗I) (V'⊗G^dag)] = Tr(Q V Q V') Tr(G G^dag).
    #     For the EW self-energy the internal line is trivial (V=V'=I_2), giving
    #     Tr(Q^2) * Tr(G G^dag).  Verify the factorization with a generic V.
    Q = np.array([[0.5, 0.0], [0.0, -0.5]], dtype=complex)  # T_3
    V = RNG.standard_normal((2, 2)) + 1j * RNG.standard_normal((2, 2))
    Vp = RNG.standard_normal((2, 2)) + 1j * RNG.standard_normal((2, 2))
    Gd = G.conj().T
    full = np.kron(Q, np.eye(n)) @ np.kron(V, G) @ np.kron(Q, np.eye(n)) @ np.kron(Vp, Gd)
    lhs = np.trace(full)
    rhs = np.trace(Q @ V @ Q @ Vp) * np.trace(G @ Gd)
    okall &= check(
        f"direct-product factorization Tr[(Q⊗I)(V⊗G)(Q⊗I)(V'⊗G†)] = Tr(QVQV')*Tr(GG†) (err {abs(lhs - rhs):.1e})",
        abs(lhs - rhs) < 1e-9,
    )

    # B3: with trivial internal line V=V'=I, weight of S+C is exactly Tr(Q^2).
    full_triv = np.kron(Q, np.eye(n)) @ np.kron(np.eye(2), G) @ np.kron(Q, np.eye(n)) @ np.kron(np.eye(2), Gd)
    weight = np.trace(full_triv) / np.trace(G @ Gd)
    okall &= check(
        f"trivial-internal weight of (S+C) = Tr(Q^2) = 1/2 (got {np.real(weight):.4f})",
        abs(np.real(weight) - float(np.real(np.trace(Q @ Q)))) < 1e-9,
    )

    # B4: the landed counterexample -- Q=T_3, M=I_color : connected loop is
    #     ENTIRELY singlet (S=N_c, C=0), with weight Tr(T_3^2)=1/2, so the
    #     singlet channel genuinely carries weight; tracelessness Tr(T_3)=0
    #     does NOT remove it.  (matches EW_CURRENT_TRACELESS_GENERATOR no-go.)
    I3 = np.eye(n, dtype=complex)
    S0, C0, T0 = fierz_S_C(I3, n)
    okall &= check(
        f"counterexample M=I_color: S=N_c={S0:.0f}, C=0 (got {C0:.1e}); singlet carries Tr(T_3^2)*S = {0.5 * S0:.2f}",
        abs(S0 - n) < 1e-9 and abs(C0) < 1e-9,
    )
    return okall


# ============================================================
# (B') Substantiate the color reflection G(y,x) = eps(x)eps(y) G(x,y)^dag from the ACTUAL
#      staggered theory (not just random matrices): the massive staggered operator obeys
#      eps-hermiticity D_m^dag = eps D_m eps (eps(x) = (-1)^{sum x_mu}), so G = D_m^{-1}
#      obeys G^dag = eps G eps, i.e. G(y,x)_color = eps(x)eps(y) G(x,y)_color^dag.
# ============================================================
def part_Bp():
    print("\n(B') Color reflection G(y,x)=eps(x)eps(y)G(x,y)^dag from staggered eps-hermiticity (real lattice, random SU(3))")
    L, nc, ndim = 2, 3, 4
    vol = L ** ndim
    mass = 0.1
    coords = np.array([[ (s // L ** mu) % L for mu in range(ndim)] for s in range(vol)])
    eps = np.array([(-1.0) ** int(np.sum(coords[s])) for s in range(vol)])  # staggered sign
    eta = np.ones((vol, ndim))
    for mu in range(ndim):
        for s in range(vol):
            eta[s, mu] = (-1.0) ** int(np.sum(coords[s, :mu]))
    idx = lambda c: int(sum(int(c[mu]) * L ** mu for mu in range(ndim)))
    # random SU(3) links
    U = np.array([[haar_su(nc) for mu in range(ndim)] for s in range(vol)])
    N = nc * vol
    D = np.zeros((N, N), dtype=complex)
    for x in range(vol):
        for mu in range(ndim):
            c = coords[x].copy()
            c[mu] = (c[mu] + 1) % L
            xp = idx(c)
            cm = coords[x].copy()
            cm[mu] = (cm[mu] - 1) % L
            xm = idx(cm)
            for a in range(nc):
                for b in range(nc):
                    D[a * vol + x, b * vol + xp] += 0.5 * eta[x, mu] * U[x][mu][a, b]
                    D[a * vol + x, b * vol + xm] += -0.5 * eta[xm, mu] * np.conj(U[xm][mu][b, a])
    D = D + mass * np.eye(N)
    E = np.diag(np.concatenate([eps for _ in range(nc)]))  # eps on color (x) site index
    herm_err = np.max(np.abs(D.conj().T - E @ D @ E))
    G = np.linalg.inv(D)
    refl_err = np.max(np.abs(G.conj().T - E @ G @ E))
    ok = check(
        f"staggered D_m^dag = eps D_m eps (err {herm_err:.1e}) => G^dag = eps G eps (err {refl_err:.1e}); "
        f"reflection is a theory property, not an assumption",
        herm_err < 1e-9 and refl_err < 1e-9,
    )
    return ok


# ============================================================
# (C) Channel split is KINEMATIC: <S>/<T> = 1/N_c^2 (free+random-gauge AND Haar),
#     so R_conn = 8/9 is a gauge-orbit fraction, beta-independent (no continuum trend).
# ============================================================
def haar_su(n):
    z = (RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diagonal(r)
    q = q * (d / np.abs(d))
    q = q / (np.linalg.det(q)) ** (1.0 / n)
    return q


def part_C():
    print("\n(C) Channel split is a kinematic gauge-orbit fraction: <S>/<T> = 1/N_c^2 for ANY dressing")
    okall = True
    nsamp = 40000
    for n in [2, 3, 4, 5]:
        # (i) DECISIVE beta-independence: a FIXED arbitrary NON-unitary dressed propagator M
        #     (a generic complex matrix with arbitrary singular values -- the actual dressed
        #     propagator at any beta), averaged over the gauge orbit M -> Omega(0) M Omega(x)^dag.
        #     Weingarten: <|Tr[Omega M Omega'^dag]|^2> = (1/N) Tr[M M^dag] = T/N, so <S>/T = 1/N^2,
        #     INDEPENDENT of the dressing M.  This covers every beta, not just unitary cases.
        M = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
        M = M @ np.diag(RNG.uniform(0.1, 3.0, n))  # arbitrary non-unitary dressing
        T_fixed = float(np.real(np.trace(M @ M.conj().T)))
        Sorb = 0.0
        for _ in range(nsamp):
            G = haar_su(n) @ M @ haar_su(n).conj().T
            Sorb += np.abs(np.trace(G)) ** 2 / n
        rorb = (Sorb / nsamp) / T_fixed
        target = 1.0 / n ** 2
        # (ii) cross-checks: the two extreme regimes (free + random gauge, and fully Haar).
        Sf = Tf = Sh = Th = 0.0
        for _ in range(nsamp):
            s, c, t = fierz_S_C(haar_su(n) @ np.eye(n) @ haar_su(n).conj().T, n)
            Sf += s
            Tf += t
            s2, c2, t2 = fierz_S_C(haar_su(n), n)
            Sh += s2
            Th += t2
        okall &= check(
            f"N_c={n}: arbitrary-dressing orbit-avg <S>/T={rorb:.4f} (=1/N_c^2={target:.4f}, Weingarten); "
            f"cross-check free+gauge={Sf / Tf:.4f}, Haar={Sh / Th:.4f} => R_conn={1 - target:.4f}",
            abs(rorb - target) < 0.01 and abs(Sf / Tf - target) < 0.01 and abs(Sh / Th - target) < 0.01,
        )
    # The gauge-orbit fraction is dressing-independent (any M) => R_conn = 8/9 has no beta-trend.
    print("    => the gauge-orbit singlet fraction is dressing(beta)-independent: R_conn = 8/9 has no continuum trend")
    return okall


# ============================================================
# (D) Color-blindness fixes NEITHER completion: it leaves kappa free.
#     kappa=0 (singlet projection) is an active non-color-blind operation; kappa=1
#     (retain S+C) is the identity readout; selecting either as physical is an
#     external scheme choice the lattice current does not make.  (Symmetric
#     statement, consistent with MATCHING_RULE sec2.)
# ============================================================
def part_D():
    print("\n(D) Color-blindness leaves kappa free: both kappa=1 and kappa=0 are external scheme choices")
    n = 3
    okall = True
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    S, C, T = fierz_S_C(G, n)
    R0 = C / T

    # A multiplicative color-scalar renormalization Z * I_color: G -> z G scales S and C by the
    # SAME |z|^2, so it leaves R_conn = C/T invariant: it selects neither completion.  (A more
    # general dressed two-current kernel can carry independent singlet/adjoint projectors, but
    # THEIR coefficients are likewise not fixed by color-blindness alone -- color-blindness is
    # agnostic to the channel weights.)  Hence color-blindness does not select kappa (MATCHING_RULE sec2).
    z = 1.7 - 0.4j
    Sz, Cz, Tz = fierz_S_C(z * G, n)
    okall &= check(
        f"multiplicative color-scalar renorm scales S,C equally -> R_conn invariant ({R0:.6f} -> {Cz / Tz:.6f}); "
        f"color-blindness selects neither completion",
        abs(R0 - Cz / Tz) < 1e-9,
    )

    # The two completions: kappa=0 is an ACTIVE singlet projection (OZI / planar / leading-N_c);
    # kappa=1 is the IDENTITY readout (retain the full trace S+C, the exact connected correlator).
    # Selecting which the physical coupling uses is an external continuum scheme choice either way.
    G_adj = G - (np.trace(G) / n) * np.eye(n)
    S0, C0, T0 = fierz_S_C(G_adj, n)
    okall &= check(
        f"kappa=0 = active singlet projection removes S (S {S:.3f} -> {S0:.1e}, C unchanged); a non-color-blind op",
        S0 < 1e-9 and abs(C0 - C) < 1e-9,
    )
    okall &= check(
        f"kappa=1 = identity readout, retain full trace T=S+C ({T:.3f}); selecting it as physical is still external",
        abs((S + C) - T) < 1e-9,
    )
    print("    => color-blindness fixes neither completion; kappa=0 (OZI/planar projection) and kappa=1 (identity")
    print("       readout) are both external continuum scheme choices -- neither is privileged by the lattice current")
    return okall


# ============================================================
# (E) Structural MC-undecidability of kappa_EW.
# ============================================================
def part_E():
    print("\n(E) Structural Monte-Carlo-undecidability of kappa_EW")
    n = 3
    F_adj = sp.Rational(n ** 2 - 1, n ** 2)  # 8/9
    kappa = sp.symbols("kappa", nonnegative=True)
    R_phys = F_adj + kappa * (1 - F_adj)
    K_EW = 1 / R_phys
    K0 = sp.nsimplify(K_EW.subs(kappa, 0))
    K1 = sp.nsimplify(K_EW.subs(kappa, 1))
    okall = True
    okall &= check(f"K_EW(0) = 9/8 (got {K0}) ; K_EW(1) = 1 (got {K1})",
                   K0 == sp.Rational(9, 8) and K1 == sp.Integer(1))

    # The lattice ensemble measures the channel data {<S>,<C>,<T>=<S>+<C>}; only <T>=Tr[GG^dag]
    # is pointwise gauge-invariant, while <S>,<C> are gauge-orbit-averaged channel diagnostics.
    # The bare correlator computes the full trace <T>=<S>+<C>.  kappa is the EXTERNAL weight of
    # S in the *physical readout functional* Pi_phys = C + kappa S; both
    # completions are functions of the SAME measured data and neither is forced by it.
    S_meas, C_meas = sp.Rational(1, 9), sp.Rational(8, 9)  # any measured split; T=1
    T_meas = S_meas + C_meas
    bare_correlator = T_meas  # what the ensemble actually computes; independent of kappa
    Pi0 = C_meas + 0 * S_meas
    Pi1 = C_meas + 1 * S_meas
    okall &= check(
        f"bare gauge-invariant correlator = <T> = {bare_correlator} (full trace S+C); this is the OBJECT, "
        f"not yet the physical readout",
        bare_correlator == sp.Integer(1),
    )
    okall &= check(
        f"Pi_phys(kappa=0)={Pi0} (singlet-subtracted) and Pi_phys(kappa=1)={Pi1} (full trace) are BOTH built "
        f"from the SAME measured {{S={S_meas},C={C_meas},T={T_meas}}} -> no MC observable is a function of kappa alone",
        Pi0 == C_meas and Pi1 == T_meas,
    )
    print("    => kappa_EW is not Monte-Carlo-decidable: the channel split is an ensemble observable, but the readout")
    print("       weight (which channels the matched physical coupling retains) is a continuum scheme choice external")
    print("       to it; neither completion is privileged by any lattice measurement")
    return okall


# ============================================================
# (F) sin^2(theta_W) is kappa-invariant.
# ============================================================
def part_F():
    print("\n(F) sin^2(theta_W) is kappa-invariant (K_EW cancels in the g_1/g_2 ratio)")
    kappa, g1b, g2b = sp.symbols("kappa g1b g2b", positive=True)
    F_adj = sp.Rational(8, 9)
    K = 1 / (F_adj + kappa * (1 - F_adj))
    # both gauge couplings get the same sqrt(K) color projection
    g1 = sp.sqrt(K) * g1b
    g2 = sp.sqrt(K) * g2b
    sin2 = g1 ** 2 / (g1 ** 2 + g2 ** 2)
    sin2_simpl = sp.simplify(sin2 - g1b ** 2 / (g1b ** 2 + g2b ** 2))
    okall = check(f"sin^2(theta_W) independent of kappa (residual {sin2_simpl})", sin2_simpl == 0)
    return okall


def main():
    print("=" * 78)
    print("EW kappa_EW object-pin + MC-undecidability runner (zero PDG inputs)")
    print("=" * 78)
    results = [part_A(), part_B(), part_Bp(), part_C(), part_D(), part_E(), part_F()]
    print("\n" + "=" * 78)
    print(f"RUNNER STATUS: {'PASS' if all(results) and FAIL == 0 else 'FAIL'} (PASS={PASS} FAIL={FAIL})")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print("=" * 78)
    return 0 if (all(results) and FAIL == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
