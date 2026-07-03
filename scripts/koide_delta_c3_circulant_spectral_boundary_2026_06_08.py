"""Koide delta: bounded spectral boundary for a Hermitian C3 circulant.

The C3 charged-lepton Yukawa is the Hermitian circulant M = a I + b C + b-bar C^2 with
b = |b| e^{i delta}; eigenvalues lambda_k = a + 2|b| cos(delta + 2*pi*k/3) (real).

CLAIM (bounded): symmetric spectral quantities in this ansatz depend on delta through
u = cos(3 delta); det M and Tr log|M| are monotone in u; and the standard
non-monotone discriminant has its interior extremum at u=0 (delta=30deg), not at
the Brannen comparator delta=2/9. This is not a global closure result over
non-spectral, labeled, dynamical, or future readout routes.

VERIFIES (exact sympy + numpy):
  D1. M is Hermitian with real eigenvalues lambda_k = a + 2|b| cos(delta + 2*pi*k/3).
  D2. e1 = 3a and e2 = 3(a^2-|b|^2) are delta-INDEPENDENT; e3 = det M = a^3 - 3a|b|^2 + 2|b|^3 * u with
      u = cos(3 delta) -- LINEAR (hence monotonic) in u. (trig reduced via exp rewrite.)
  D3. Every symmetric function is a function of u = cos(3 delta) alone: the power sums p_n (n=1..6) satisfy
      p_n(delta) = p_n(delta') whenever cos(3 delta)=cos(3 delta') (tested on the cos3delta-stabilizer
      delta -> -delta and delta -> 2pi/3 - delta).
  D4. det M and Tr log|M| are MONOTONIC in u (d/du sign-definite on the physical cone) -> their
      delta-gradient = sin(3 delta) * (sign-definite) vanishes ONLY at sin(3 delta)=0 (u=+/-1).
  D5. At the stationary points delta = k*60deg the spectrum is DEGENERATE; the comparator delta = 2/9 rad is
      NON-degenerate, sits at interior u=cos(2/3)~0.786, and has sin(3*2/9)!=0 -> not stationary.
  D6. The eigenvalue SET is invariant under delta -> -delta -> masses EVEN in delta: SIGN of delta
      undetermined by the spectrum (Z2 orientation residual); |delta| in [0,pi/3] fixed by u.
  D7. Interior-boundary check: u_target=cos(2/3) is strictly interior to [-1,1]; det and Tr log have
      NO interior critical point in u (monotonic), so no framework-native canonical functional is stationary
      there.
  D8. Discriminant boundary: the squared-Vandermonde discriminant has its interior
      critical point at u=0 (delta=30deg), amplitude-independently.

No PDG value or fitted mass is used.
"""
from __future__ import annotations
import sympy as sp
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def main() -> int:
    print("KOIDE delta: C3 circulant spectral boundary")
    print("=" * 64)
    a, c, d = sp.symbols('a c delta', real=True, positive=True)  # c = |b|
    two_pi_3 = 2 * sp.pi / 3
    lam = [a + 2 * c * sp.cos(d + k * two_pi_3) for k in range(3)]

    # D1: Hermitian circulant, real eigenvalues
    av, cv, dv = 1.7, 1.7/np.sqrt(2), 0.3
    C = np.array([[0,1,0],[0,0,1],[1,0,0]], complex)
    bcomp = cv*np.exp(1j*dv)
    M = av*np.eye(3) + bcomp*C + np.conj(bcomp)*(C@C)
    herm = np.allclose(M, M.conj().T)
    eig_num = np.sort(np.linalg.eigvalsh(M))
    lam_num = np.sort([float(l.subs({a:av, c:cv, d:dv})) for l in lam])
    check("D1: M = aI + bC + b-bar C^2 Hermitian, eigenvalues a + 2|b|cos(delta + 2pi k/3) (real)",
          herm and np.allclose(eig_num, lam_num),
          f"Hermitian={herm}; eig(M)={np.round(eig_num,6)} == lam={np.round(lam_num,6)}")

    # D2: e1, e2 delta-independent; e3 = a^3 - 3a c^2 + 2 c^3 cos(3 delta) (linear in u=cos3delta).
    # e3 via the exact circulant-determinant identity det circ(a,b,b-bar) = a^3 + b^3 + b-bar^3 - 3 a |b|^2.
    e1 = sp.expand(sp.simplify(sum(lam)))
    e2 = sp.simplify(sum(lam[i]*lam[j] for i in range(3) for j in range(i+1, 3)))
    bsym = c*sp.exp(sp.I*d)
    e3_circ = sp.simplify(a**3 + bsym**3 + sp.conjugate(bsym)**3 - 3*a*(bsym*sp.conjugate(bsym)))
    e1_t, e2_t = 3*a, 3*a**2 - 3*c**2
    e3_t = a**3 - 3*a*c**2 + 2*c**3*sp.cos(3*d)
    ok_e1 = sp.simplify(e1 - e1_t) == 0
    ok_e2 = sp.simplify(e2 - e2_t) == 0
    ok_e3 = sp.simplify(e3_circ.rewrite(sp.cos) - e3_t) == 0
    # numeric grid cross-check that the eigenvalue PRODUCT equals the closed form (independent of the identity)
    grid_ok = True
    for dd in np.linspace(0, 2*np.pi, 41):
        prod = np.prod([av + 2*cv*np.cos(dd + k*2*np.pi/3) for k in range(3)])
        closed = av**3 - 3*av*cv**2 + 2*cv**3*np.cos(3*dd)
        grid_ok = grid_ok and abs(prod - closed) < 1e-9
    check("D2: e1=3a, e2=3(a^2-|b|^2) delta-INDEPENDENT; e3=det M = a^3-3a|b|^2 + 2|b|^3 cos(3 delta) "
          "(circulant-det identity) -- LINEAR (monotonic) in u=cos(3 delta); eigenvalue-product grid-checked",
          ok_e1 and ok_e2 and ok_e3 and grid_ok,
          f"e1={e1}, e2={sp.factor(e2)}, e3(circ)={e3_circ}; product==closed on 41-pt grid: {grid_ok}")

    # D3: every symmetric function is a function of u=cos(3 delta) alone -> p_n invariant on the
    # cos3delta-stabilizer (delta -> -delta and delta -> 2pi/3 - delta)
    def pn_num(delta, n):
        return float(sum((av + 2*cv*np.cos(delta + k*2*np.pi/3))**n for k in range(3)))
    all_u = True
    detail3 = []
    test_deltas = [0.21, 0.5, 0.83]
    for n in range(1, 7):
        ok_n = True
        for d0 in test_deltas:
            # transforms preserving cos(3 delta): d -> -d, d -> 2pi/3 - d
            same = (abs(pn_num(d0, n) - pn_num(-d0, n)) < 1e-9 and
                    abs(pn_num(d0, n) - pn_num(2*np.pi/3 - d0, n)) < 1e-9)
            ok_n = ok_n and same
        all_u = all_u and ok_n
        detail3.append(f"p{n}:{'u-only' if ok_n else 'FAIL'}")
    check("D3: power sums p_n (n=1..6) are functions of u=cos(3 delta) ALONE (invariant under the "
          "cos3delta-stabilizer delta->-delta, delta->2pi/3-delta) -> so is every symmetric function (Newton)",
          all_u, "; ".join(detail3))

    # D4: det and Tr log|M| MONOTONIC in u -> stationary in delta only at sin(3 delta)=0
    u = sp.symbols('u', real=True)
    detM_u = a**3 - 3*a*c**2 + 2*c**3*u          # det as function of u
    d_det_du = sp.diff(detM_u, u)                 # = 2 c^3 > 0 (constant sign)
    trlog_u = sp.log(detM_u)                      # Tr log|M| = log det (on the positive cone)
    d_trlog_du = sp.simplify(sp.diff(trlog_u, u)) # = 2c^3 / det > 0 on the cone
    det_mono = (d_det_du == 2*c**3)               # strictly positive constant
    # Tr log derivative positive on physical cone (det>0): check sign at sample
    trlog_pos = float(d_trlog_du.subs({a:av, c:cv, u:np.cos(2/3)})) > 0
    # and the delta-gradient is sin(3 delta) * (-3) * F'(u): vanishes iff sin(3 delta)=0 (F'!=0)
    f_dtrlog_ddelta = sp.lambdify((a,c,d), sp.diff(sum(sp.log(l) for l in lam), d), 'numpy')
    grad_0 = abs(float(f_dtrlog_ddelta(av,cv,1e-9)))
    grad_29 = abs(float(f_dtrlog_ddelta(av,cv,2/9)))
    check("D4: det M (d/du = 2|b|^3 > 0) and Tr log|M| (d/du = 2|b|^3/det > 0) are MONOTONIC in u "
          "-> delta-gradient = -3 sin(3 delta) F'(u) vanishes ONLY at sin(3 delta)=0 (degenerate boundary)",
          det_mono and trlog_pos and grad_0 < 1e-6 and grad_29 > 1e-6,
          f"d(det)/du={d_det_du}; d(Trlog)/du>0:{trlog_pos}; |d(Trlog)/ddelta| at 0={grad_0:.2e}, at 2/9={grad_29:.3f}")

    # D5: stationary points degenerate; 2/9 comparator is nondegenerate, interior u, sin3delta != 0
    def spectrum(delta):
        return np.sort([av + 2*cv*np.cos(delta + k*2*np.pi/3) for k in range(3)])
    def min_gap(s):
        return min(abs(s[i]-s[j]) for i in range(3) for j in range(i+1,3))
    deg0, deg60 = min_gap(spectrum(0.0)) < 1e-9, min_gap(spectrum(np.pi/3)) < 1e-9
    nondeg29 = min_gap(spectrum(2/9)) > 1e-3
    u_phys = np.cos(3*2/9); interior = -1 < u_phys < 1
    check("D5: stationary delta=0,60deg are DEGENERATE; comparator delta=2/9 is NON-degenerate, interior "
          "u=cos(2/3)~0.786, sin(3*2/9)!=0 -> not a spectral-stationary point",
          deg0 and deg60 and nondeg29 and interior and abs(np.sin(3*2/9)) > 1e-3,
          f"gaps: 0={min_gap(spectrum(0.0)):.1e}, 60={min_gap(spectrum(np.pi/3)):.1e}, 2/9={min_gap(spectrum(2/9)):.4f}; "
          f"u_phys={u_phys:.4f} interior={interior}; sin(3*2/9)={np.sin(3*2/9):.4f}")

    # D6: even in delta
    check("D6: eigenvalue SET invariant under delta -> -delta (relabel k -> -k) -> masses EVEN in delta: "
          "SIGN of delta undetermined by spectrum (Z2 orientation residual); |delta| fixed by u",
          np.allclose(spectrum(0.41), spectrum(-0.41)),
          f"spectrum(+0.41)==spectrum(-0.41): {np.allclose(spectrum(0.41), spectrum(-0.41))}")

    # D7: interior-boundary check
    check("D7: u_target=cos(2/3)~0.786 is strictly interior to [-1,1]; det and Tr log have NO interior "
          "critical point in u (monotonic), so these canonical spectral functionals do not select delta=2/9",
          (-1 < u_phys < 1) and (d_det_du != 0),
          f"u_phys={u_phys:.5f} in (-1,1); canonical functionals monotonic (d(det)/du={d_det_du}!=0) -> no interior extremum")

    # D8: the squared-Vandermonde discriminant has its interior extremum at u=0
    # (delta=30deg), amplitude-independent -- not at the 2/9 comparator.
    # D = e1^2 e2^2 - 4 e2^3 - 4 e1^3 e3 + 18 e1 e2 e3 - 27 e3^2, with e3 affine in u -> D quadratic in u.
    uu = sp.symbols('u', real=True)
    e1u, e2u, e3u = 3*a, 3*a**2 - 3*c**2, a**3 - 3*a*c**2 + 2*c**3*uu
    Dexpr = e1u**2*e2u**2 - 4*e2u**3 - 4*e1u**3*e3u + 18*e1u*e2u*e3u - 27*e3u**2
    dD_du = sp.diff(Dexpr, uu)
    u_star = sp.solve(dD_du, uu)
    d2D = sp.diff(Dexpr, uu, 2)
    is_max = sp.simplify(d2D) == -54*(2*c**3)**2 / (2*c**3) ** 0  # d2D/du2 = -54*(2c^3)^2 < 0 -> concave (max)
    # cross-check: argmax of D over delta in [0, pi/3] is 30deg for several amplitudes
    def disc_of_delta(delta, cval):
        s = [av + 2*cval*np.cos(delta + k*2*np.pi/3) for k in range(3)]
        return ((s[0]-s[1])*(s[1]-s[2])*(s[2]-s[0]))**2
    argmax_ok = True
    for cval in [0.1*av, 0.5*av, av/np.sqrt(2), 0.9*av, 1.5*av]:
        grid = np.linspace(1e-4, np.pi/3 - 1e-4, 20001)
        dmax = grid[int(np.argmax([disc_of_delta(x, cval) for x in grid]))]
        argmax_ok = argmax_ok and abs(dmax - np.pi/6) < 1e-3
    u_star_zero = (len(u_star) == 1 and sp.simplify(u_star[0]) == 0)
    check("D8: the squared-Vandermonde discriminant has its interior critical point at u*=0 "
          "(delta=30deg), amplitude-INDEPENDENT, a concave MAX; not the comparator u=cos(2/3)~0.786.",
          u_star_zero and bool(sp.simplify(d2D + 54*(2*c**3)**2) == 0) and argmax_ok,
          f"u* solving dD/du=0 -> {u_star} (=0); d2D/du2={sp.simplify(d2D)} (<0, max); argmax_delta==30deg for all amplitudes: {argmax_ok}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: symmetric spectral quantities of the Hermitian C3 circulant collapse to u=cos(3 delta).\n"
        "The canonical spectral examples det and Tr log are monotone in u and are stationary only at the\n"
        "degenerate delta=k*60deg boundary; the discriminant extremizes at delta=30deg. The runner supports\n"
        "this bounded spectral boundary only. It does not close non-spectral, labeled, dynamical, or future\n"
        "readout routes to the Koide phase."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
