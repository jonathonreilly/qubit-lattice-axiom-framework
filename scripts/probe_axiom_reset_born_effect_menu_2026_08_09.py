"""Probe: does the drafted Observables/Actuality pair actually close the Born form?

The reset proposal claims:
  (i)  M_2(C) with a projection-only menu is the one case where an additivity
       axiom cannot force the Born rule, because Gleason's theorem fails in
       dimension two;
  (ii) in dimension three the same additivity DOES force the trace form;
  (iii) in dimension two, stating additivity over the full effect menu
       (Busch's theorem) forces it after all.

If (i) fails the diagnosis is wrong. If (iii) fails, the reset does not buy
Born and the readout/Born lane stays open.

Solution-space dimensions are computed from null spaces, never assumed.
"""

import numpy as np

RESULTS = []
rng = np.random.default_rng(20260809)

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def random_unit(n, dim=3):
    v = rng.normal(size=(n, dim))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


# ---------------------------------------------------------------------------
# (i) dimension two, projection menu: Gleason fails
# ---------------------------------------------------------------------------

def probe_qubit_projection_menu():
    c = 0.4

    def f(n):                      # candidate frame function on qubit projections
        return 0.5 + c * n[..., 2] ** 3

    N = random_unit(4000)
    frame_defect = float(np.abs(f(N) + f(-N) - 1.0).max())
    check("candidate is a valid frame function on every qubit basis",
          frame_defect < 1e-12,
          f"max |f(n) + f(-n) - 1| = {frame_defect:.2e} over {len(N)} bases")

    vals = f(N)
    check("candidate takes legitimate probability values",
          vals.min() >= -1e-12 and vals.max() <= 1 + 1e-12,
          f"range [{vals.min():.4f}, {vals.max():.4f}]")

    # Born form on a qubit is affine in the Bloch vector: (1 + r.n)/2.
    design = np.column_stack([np.ones(len(N)), N])
    coef, *_ = np.linalg.lstsq(design, vals, rcond=None)
    resid = float(np.abs(vals - design @ coef).max())
    check("(i) Gleason FAILS in dimension two: a non-Born frame function exists",
          resid > 1e-3,
          f"best affine (Born) fit leaves max residual {resid:.4f}; "
          f"f(n) = 1/2 + {c}*n_z^3 is additive on every basis yet is not a trace form")


# ---------------------------------------------------------------------------
# (ii) dimension three, projection menu: Gleason holds
# ---------------------------------------------------------------------------

def even_monomials(max_deg=6):
    out = []
    for i in range(max_deg + 1):
        for j in range(max_deg + 1 - i):
            for k in range(max_deg + 1 - i - j):
                if (i + j + k) % 2 == 0 and (i + j + k) <= max_deg:
                    out.append((i, j, k))
    return out


def monomial_values(pts, mons):
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    return np.column_stack([x ** i * y ** j * z ** k for (i, j, k) in mons])


def probe_qutrit_projection_menu():
    mons = even_monomials(6)

    # orthonormal triples in R^3
    triples = []
    for _ in range(1500):
        Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        triples.append(Q.T)
    T = np.array(triples)

    rows = [monomial_values(t, mons).sum(axis=0) for t in T]
    A = np.array(rows)

    # homogeneous frame condition sum_i f(n_i) = 0
    _, s, Vt = np.linalg.svd(A)
    null_coefs = Vt[np.sum(s > 1e-8):]

    # dimension AS FUNCTIONS (the monomial basis is redundant on the sphere)
    sample = random_unit(4000)
    M = monomial_values(sample, mons)
    null_funcs = M @ null_coefs.T
    dim_null = int(np.linalg.matrix_rank(null_funcs, tol=1e-7))

    # the traceless quadratics: exactly the ell = 2 sector
    quad = np.column_stack([
        sample[:, 0] ** 2 - sample[:, 1] ** 2,
        sample[:, 0] ** 2 - sample[:, 2] ** 2,
        sample[:, 0] * sample[:, 1],
        sample[:, 0] * sample[:, 2],
        sample[:, 1] * sample[:, 2],
    ])
    dim_quad = int(np.linalg.matrix_rank(quad, tol=1e-7))
    joint = int(np.linalg.matrix_rank(np.column_stack([null_funcs, quad]), tol=1e-7))

    check("(ii) Gleason HOLDS in dimension three: only trace forms survive",
          dim_null == 5 and dim_quad == 5 and joint == 5,
          f"solution space searched over even harmonics up to degree 6 "
          f"(function-space rank {int(np.linalg.matrix_rank(M, tol=1e-7))}); "
          f"null space dim = {dim_null}, traceless-quadratic dim = {dim_quad}, "
          f"joint span = {joint} -> the solutions are exactly the ell=2 sector, "
          f"i.e. f(n) = n^T rho n")


# ---------------------------------------------------------------------------
# (iii) dimension two, effect menu: Busch closes it
# ---------------------------------------------------------------------------

def effect_monomials(max_deg=3):
    out = []
    for i in range(max_deg + 1):
        for j in range(max_deg + 1 - i):
            for k in range(max_deg + 1 - i - j):
                for l in range(max_deg + 1 - i - j - k):
                    out.append((i, j, k, l))
    return out


def eval_effect_monomials(params, mons):
    a, bx, by, bz = params.T
    return np.column_stack([a ** i * bx ** j * by ** k * bz ** l
                            for (i, j, k, l) in mons])


def sample_effect_pair():
    """E = (a I + b.sigma)/2 is an effect iff |b| <= a <= 2 - |b|."""
    while True:
        b1 = rng.normal(size=3) * 0.25
        b2 = rng.normal(size=3) * 0.25
        n1, n2 = np.linalg.norm(b1), np.linalg.norm(b2)
        if n1 > 1.0 or n2 > 1.0:          # |b| <= a <= 2-|b| is empty otherwise
            continue
        a1 = rng.uniform(n1, 2 - n1)
        a2 = rng.uniform(n2, 2 - n2)
        bs = b1 + b2
        ns = np.linalg.norm(bs)
        if ns <= a1 + a2 <= 2 - ns:          # the sum is also an effect
            return (np.array([a1, *b1]), np.array([a2, *b2]),
                    np.array([a1 + a2, *bs]))


def probe_qubit_effect_menu():
    mons = effect_monomials(3)
    E1, E2, ES = [], [], []
    for _ in range(1200):
        e1, e2, es = sample_effect_pair()
        E1.append(e1); E2.append(e2); ES.append(es)
    E1, E2, ES = np.array(E1), np.array(E2), np.array(ES)

    A = (eval_effect_monomials(ES, mons)
         - eval_effect_monomials(E1, mons)
         - eval_effect_monomials(E2, mons))
    _, s, Vt = np.linalg.svd(A)
    null_coefs = Vt[np.sum(s > 1e-8):]

    probe_pts = np.column_stack([rng.uniform(0.4, 1.6, 3000),
                                 rng.normal(size=(3000, 3)) * 0.2])
    Mv = eval_effect_monomials(probe_pts, mons)
    null_funcs = Mv @ null_coefs.T
    dim_null = int(np.linalg.matrix_rank(null_funcs, tol=1e-7))

    linear = probe_pts                              # a, bx, by, bz
    dim_lin = int(np.linalg.matrix_rank(linear, tol=1e-7))
    joint = int(np.linalg.matrix_rank(np.column_stack([null_funcs, linear]), tol=1e-7))

    check("(iii) Busch CLOSES dimension two: effect additivity forces the trace form",
          dim_null == 4 and dim_lin == 4 and joint == 4,
          f"searched polynomials to degree 3 in (a, b) "
          f"(basis size {len(mons)}); additive solution space dim = {dim_null}, "
          f"linear-form dim = {dim_lin}, joint span = {joint} -> only "
          f"mu(E) = Tr(rho E) survives; the n_z^3 counterexample of (i) is killed")

    # confirm the (i) counterexample really is excluded by the effect menu
    c = 0.4
    def mu_bad(p):
        a, b = p[:, 0], p[:, 1:]
        nb = np.linalg.norm(b, axis=1) + 1e-15
        return a / 2 + c * (b[:, 2] / nb) ** 3 * nb
    defect = float(np.abs(mu_bad(ES) - mu_bad(E1) - mu_bad(E2)).max())
    check("the dimension-two counterexample violates effect additivity",
          defect > 1e-3,
          f"max additivity violation = {defect:.4f} over {len(ES)} effect pairs")


def main():
    probe_qubit_projection_menu()
    probe_qutrit_projection_menu()
    probe_qubit_effect_menu()

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
