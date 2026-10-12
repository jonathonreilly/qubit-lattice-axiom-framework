"""Independent checks for campaign C4 / lane RW / probe W3.

This does not reuse the worker's root classifier.  For the general scalar
symbol it loads the worker's saved symbolic matrix, integrates out the two
auxiliary variables by a Schur complement, reconstructs the quadratic
eigenvalue problem, and scans a much denser momentum grid.  The tensor,
vector, and ultraviolet static formulas are derived independently from the
listed h-local operators.
"""

from pathlib import Path
import pickle

import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# 1. Hand algebra for the anomaly and the h-local mass obstruction.
#
# sigma = B-E_dot has delta sigma = -epsilon.  Therefore
# delta F/a = -grad(epsilon_dot).grad(E) - grad(Phi).grad(chi)
#             + grad(sigma).grad(epsilon)
#           = grad(B).grad(epsilon) - grad(chi).grad(Phi) + divergence.
# Expanding I=F[Phi+pi_dot,B-pi+zeta_dot,E+zeta] similarly gives
# I-F=L_WZ+divergence.
#
# For the five mass invariants, variation of m1(grad B)^2 simultaneously
# gives -2m1 grad(B).grad(epsilon) and +2m1 grad(B).grad(chi_dot).  Matching
# the first requires m1=-a/2, while absence of the second requires m1=0.
# Independently, m4 Phi(-6 Psi+2 lap E) must have m4=a/2 to match
# +a Phi lap(chi), but absence of Psi epsilon_dot requires m4=0.
a, m1, m4 = sp.symbols("a m1 m4", nonzero=True)
mass_solution = sp.solve(
    [-2 * m1 - a, 2 * m1, 2 * m4 - a, -6 * m4],
    [m1, m4],
    dict=True,
)

print("[1] delta F/a = grad(B).grad(eps) - grad(chi).grad(Phi) modulo a divergence")
print("[1] I-F = L_WZ modulo a divergence")
print("[1] local-mass matching solution:", mass_solution)


# ---------------------------------------------------------------------------
# 2-3. Closed forms for the khronometric and exactly repaired subclasses.
lam, k, A, xi, eta = sp.symbols("lambda k A xi eta", positive=True)
a_free = sp.symbols("a_free", real=True)
K_worker = (
    3 * (1 - 3 * lam) / 2
    - (1 - 3 * lam) ** 2 * k**2 / (2 * ((1 - lam) * k**2 - a_free))
)
K_factored = (1 - 3 * lam) * (2 * k**2 - 3 * a_free) / (
    2 * ((1 - lam) * k**2 - a_free)
)
assert sp.simplify(K_worker - K_factored) == 0

# Physical sign a=-A and g4=0.
omega2_unrepaired = sp.factor(
    2 * xi * k**2 * (A - (lam - 1) * k**2)
    / ((3 * A + 2 * k**2) * (3 * lam - 1))
)
K_physical = sp.factor(K_factored.subs(a_free, -A))
V_repaired = (
    xi * k**2 * (1 - 2 * xi / eta)
    - 6 * xi * A / eta
    - 9 * A**2 / (2 * eta * k**2)
)

print("[2] K_Psi(a=-A) =", K_physical)
print("[2] omega^2(c4=0,g4=0,a=-A) =", omega2_unrepaired)
print("[3] repaired potential coefficient =", V_repaired)
print("[3] E cancellation coefficient is a+2*m4; hence m4=-a/2")
print("[3] k_*^2=A/(lambda-1)=2*mu^2/(lambda-1)")
print("[3] lambda_eff=lambda-2*mu^2/k^2")


# ---------------------------------------------------------------------------
# 4. Independent scalar-pole reconstruction from the saved exact symbol.
root = Path(__file__).resolve().parent
with (root / "scripts" / "w3_c2_symbol.pkl").open("rb") as fh:
    M = pickle.load(fh)
with (root / "scripts" / "w3_c2_hits.pkl").open("rb") as fh:
    hits_by_decade = pickle.load(fh)
hits = [pv for p in hits_by_decade for pv in hits_by_decade[p]]

w_sym, k_sym = sp.symbols("omega k", positive=True)
lam_sym, eta_sym, a_sym = sp.symbols("lam eta a", real=True)
ms_sym = sp.symbols("m0:5", real=True)
cs_sym = sp.symbols("c0:13", real=True)
pars = (lam_sym, eta_sym, a_sym) + ms_sym + cs_sym
Mfun = sp.lambdify((w_sym, k_sym, *pars), M, "numpy")


def reduced_coefficients(kv, pv):
    """Return K,L,V in D(w)=K*w^2+L*w+V after eliminating Phi,s."""

    def schur(ww):
        mat = np.asarray(Mfun(ww, kv, *pv), dtype=complex)
        cc = mat[:2, :2]
        cd = mat[:2, 2:]
        return mat[2:, 2:] - mat[2:, :2] @ np.linalg.solve(cc, cd)

    v = schur(0.0)
    plus = schur(1.0)
    minus = schur(-1.0)
    return (plus + minus) / 2 - v, (plus - minus) / 2, v


def scalar_tags(kv, pv):
    Kmat, Lmat, Vmat = reduced_coefficients(kv, pv)
    # det(V+wL+w^2K), ascending in w.
    mul = np.polynomial.polynomial.polymul
    poly = np.polynomial.polynomial.polysub(
        mul([Vmat[0, 0], Lmat[0, 0], Kmat[0, 0]],
            [Vmat[1, 1], Lmat[1, 1], Kmat[1, 1]]),
        mul([Vmat[0, 1], Lmat[0, 1], Kmat[0, 1]],
            [Vmat[1, 0], Lmat[1, 0], Kmat[1, 0]]),
    )
    scale = max(abs(poly[0]), abs(poly[2]), abs(poly[4]), 1e-300)
    if max(abs(poly[1]), abs(poly[3])) > 1e-6 * scale:
        return ["odd-determinant"]
    roots_w2 = np.roots([poly[4] / scale, poly[2] / scale, poly[0] / scale])
    tags = []
    for root_w2 in roots_w2:
        if abs(root_w2.imag) > 1e-6 * max(1.0, abs(root_w2)):
            tags.append("complex")
            continue
        W = root_w2.real
        if W <= 0:
            tags.append("tachyon")
            continue
        ww = np.sqrt(W)
        dyn = Vmat + ww * Lmat + W * Kmat
        vec = np.linalg.svd(dyn)[2][-1].conj()
        energy = ww * np.real(vec.conj() @ (2 * ww * Kmat + Lmat) @ vec)
        tags.append("healthy" if energy > 0 else "ghost")
    return tags


ks = np.logspace(-6, 6, 2401)
scalar_dense = []
first_scalar_failure = {}
for number, pv in enumerate(hits, start=1):
    ok = True
    for kval in ks:
        tags = scalar_tags(kval, pv)
        if len(tags) != 2 or tags != ["healthy", "healthy"]:
            ok = False
            first_scalar_failure[number] = (float(kval), tags)
            break
    if ok:
        scalar_dense.append(number)

print("[4] worker grid hits:", len(hits))
print("[4] scalar hits surviving dense k grid:", scalar_dense)
print("[4] coarse-grid false positives (first failure):", first_scalar_failure)


# ---------------------------------------------------------------------------
# Independently derived tensor and transverse-vector sectors for k along x.
# For h_yz=T:
#   omega_T^2=[(1-8c0)k^2-8m2]/(1+8c4).
# For h_0y=S and h_xy=H, eliminating S gives
#   SS=4m1+(1+4c6)k^2,
#   K_V=(1+8c4)-(1+2c8)^2 k^2/SS,
#   V_V=8m2+4(2c0+c2)k^2, omega_V^2=-V_V/K_V.
def tensor_vector_healthy_dense(pv):
    m = np.asarray(pv[3:8], dtype=float)
    c = np.asarray(pv[8:], dtype=float)
    kt = 1 + 8 * c[4]
    omega_t2 = ((1 - 8 * c[0]) * ks**2 - 8 * m[2]) / kt
    tensor_ok = kt > 0 and np.all(omega_t2 > 0)

    ss = 4 * m[1] + (1 + 4 * c[6]) * ks**2
    kv = (1 + 8 * c[4]) - (1 + 2 * c[8]) ** 2 * ks**2 / ss
    vv = 8 * m[2] + 4 * (2 * c[0] + c[2]) * ks**2
    omega_v2 = -vv / kv
    vector_ok = (
        np.all(np.isfinite(omega_v2))
        and np.all(np.abs(ss) > 1e-12)
        and np.all(kv > 0)
        and np.all(omega_v2 > 0)
    )
    return tensor_ok, vector_ok


full_dense = []
for number in scalar_dense:
    tensor_ok, vector_ok = tensor_vector_healthy_dense(hits[number - 1])
    if tensor_ok and vector_ok:
        full_dense.append(number)
print("[4] dense-grid scalar+tensor+vector survivors:", full_dense)


# Independent ultraviolet static Hessian for q=(Phi,Psi,e=k^2 E).
def static_uv(pv):
    eta_value = pv[1]
    c = np.asarray(pv[8:], dtype=float)
    H = np.zeros((3, 3))

    def square(coef, vec):
        H[:] += 2 * coef * np.outer(vec, vec)

    def product(coef, left, right):
        H[:] += coef * (np.outer(left, right) + np.outer(right, left))

    phi = np.array([1.0, 0.0, 0.0])
    psi = np.array([0.0, 1.0, 0.0])
    evar = np.array([0.0, 0.0, 1.0])
    hxx = -2 * (psi + evar)
    hyy = -2 * psi
    trace = -2 * (3 * psi + evar)

    square(eta_value / 2, phi)
    square(1, psi)
    product(-2, phi, psi)
    square(c[0], hxx)
    square(c[0], hyy)
    square(c[0], hyy)
    square(c[1], trace)
    square(c[2], hxx)
    product(-c[3], hxx, trace)
    product(c[10], phi, trace)
    product(c[11], phi, hxx)
    square(c[12], phi)

    q = np.linalg.solve(H, np.array([-1.0, 0.0, 0.0]))
    gamma = q[1] / q[0]
    geff_over_gr = q[0] / 0.5
    ct2 = (1 - 8 * c[0]) / (1 + 8 * c[4])
    return ct2, gamma, geff_over_gr


print("[4] UV observables for dense full-sector survivors:")
for number in full_dense:
    ct2, gamma, geff = static_uv(hits[number - 1])
    print(
        f"    hit {number}: cT2={ct2:+.6f}, gamma={gamma:+.6f}, "
        f"G_eff/G_GR={geff:+.6f}"
    )
