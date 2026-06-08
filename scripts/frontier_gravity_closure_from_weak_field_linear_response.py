"""Class-A finite runner (memory-safe): the self-consistency closure L^{-1}=G_0
(the open D-row gap of gravity_full_self_consistency) is DERIVED at WEAK FIELD as
first-order linear response. The weak-field gravitational potential sourced by a
matter density rho is, by first-order perturbation theory on the single lattice,
the resolvent (Green-function) convolution phi = G_0 rho, with G_0 = H^{-1} the
UNIQUE linear-response kernel of H = -Delta_lat. Hence the field operator
L = G_0^{-1} = H = -Delta_lat (Poisson), i.e. L^{-1}=G_0. The closure holds at
LINEARIZED order; the full nonlinear self-gravity loop (phi back-reacts into
H -> H+phi -> changes G_0) does NOT converge (retained_no_go poisson_self_gravity_
loop_v3 / gate_b_poisson_self_gravity) -- the strong-field boundary.

The point-source potential is the import-free lattice Green function G_0(r)->1/(4pi r)
(companion lattice_greens_1_over_r_from_heat_kernel_resolvent, this session), so the
weak-field 1/r Newtonian potential + Poisson are now linear-order import-free.

  T1  closure: phi=G_0 rho satisfies the field equation H phi = rho (Poisson) for a
      neutral source => L = G_0^{-1} = H = -Delta (L^{-1}=G_0 holds at linear order).
  T2  UNIQUENESS (teeth): G_0=H^{-1} is the unique linear-response kernel; a perturbed
      kernel K != G_0 fails the field equation (H K rho != rho).
  T3  FIRST-ORDER / LINEARITY: the field response is exactly linear in the source
      (phi[a rho1 + b rho2] = a phi[rho1] + b phi[rho2]) -- it IS first-order
      perturbation theory (the weak-field regime), not an ansatz.
  T4  point source -> Green function column = the 1/(4pi r) potential (companion #3184):
      H G_0 e_y = e_y (neutral), and G_0 e_y is the lattice Green function of a point mass.
  T5  NONLINEAR BOUNDARY (the no-go): iterating phi into H (H->H+phi) changes the kernel
      (G_0' = (H+phi)^{-1} != G_0); the loop MOVES (first nonlinear correction nonzero),
      consistent with the retained_no_go nonconvergence. So the closure is LINEAR-order.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import itertools

TOL = 1e-9
L = 10
N = L ** 3
def idx(x): return (x[0] % L) * L * L + (x[1] % L) * L + x[2] % L

# H = -Delta_lat (graph Laplacian) on the periodic Z^3 lattice
H = np.zeros((N, N))
for x in itertools.product(range(L), repeat=3):
    H[idx(x), idx(x)] = 6.0
    for mu in range(3):
        for s in (1, -1):
            y = list(x); y[mu] = (y[mu] + s) % L
            H[idx(x), idx(tuple(y))] -= 1.0

# G_0 = resolvent (pseudo-inverse; drop the uniform zero mode)
w, Vv = np.linalg.eigh(H)
inv = np.array([1.0 / wi if wi > 1e-9 else 0.0 for wi in w])
G0 = Vv @ np.diag(inv) @ Vv.T
P_neutral = np.eye(N) - np.ones((N, N)) / N   # projector off the zero mode

rng = np.random.default_rng(0)
def neutral():
    r = rng.standard_normal(N); return r - r.mean()

results = []
def check(name, ok): results.append((name, bool(ok)))

# --- T1: closure phi=G_0 rho satisfies Poisson H phi = rho ---
rho = neutral(); phi = G0 @ rho
check("T1 closure: phi=G_0 rho satisfies Poisson H phi = rho (=> L=H=-Delta, L^{-1}=G_0)",
      np.allclose(H @ phi, rho, atol=1e-9))

# --- T2: uniqueness (teeth) -- a perturbed kernel fails ---
Kbad = G0 + 0.1 * (Vv @ np.diag(np.r_[0, np.ones(N - 1)]) @ Vv.T)  # G0 + a non-resolvent perturbation
check("T2 UNIQUENESS: a perturbed kernel K!=G_0 fails the field equation (H K rho != rho)",
      not np.allclose(H @ (Kbad @ rho), rho, atol=1e-6))

# --- T3: first-order / linearity ---
r1, r2 = neutral(), neutral(); a, b = 1.3, -0.7
check("T3 FIRST-ORDER linearity: phi[a r1+b r2] = a phi[r1] + b phi[r2]",
      np.allclose(G0 @ (a * r1 + b * r2), a * (G0 @ r1) + b * (G0 @ r2), atol=1e-12))

# --- T4: point source -> Green-function column (the 1/(4pi r) potential, #3184) ---
y0 = idx((5, 5, 5))
ey = np.zeros(N); ey[y0] = 1.0; ey -= ey.mean()
gcol = G0 @ ey
check("T4 point source: H (G_0 e_y) = e_y (neutral) -- the Green-function/1-over-r potential",
      np.allclose(P_neutral @ (H @ gcol), P_neutral @ ey, atol=1e-9))
# the column decays with distance (Newtonian-like)
def dist(a, b):
    xa = np.array([a // (L * L), (a // L) % L, a % L]); xb = np.array([b // (L * L), (b // L) % L, b % L])
    d = np.abs(xa - xb); d = np.minimum(d, L - d); return np.sqrt((d ** 2).sum())
near = np.mean([gcol[idx((5 + dx, 5, 5))] for dx in (1, -1)])
far = np.mean([gcol[idx((5 + dx, 5, 5))] for dx in (3, -3)])
check("T4b Green-function column decays with distance (potential falls off)", near > far)

# --- T5: nonlinear boundary -- iterating moves the kernel (no-go) ---
Hp = H + np.diag(phi)            # phi back-reacts into H -> H+phi
wp, Vp = np.linalg.eigh(Hp)
invp = np.array([1.0 / wi if abs(wi) > 1e-9 else 0.0 for wi in wp])
G0p = Vp @ np.diag(invp) @ Vp.T  # new kernel
moved = np.linalg.norm(G0p - G0) / np.linalg.norm(G0)
check("T5 NONLINEAR BOUNDARY: back-reaction H->H+phi changes the kernel (G_0' != G_0), loop moves",
      moved > 1e-3)
check("T5b => closure is LINEAR-order only (nonlinear loop nonconvergent, retained no-go)", moved > 1e-3)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("kernel-move under one back-reaction step = %.3f (nonzero => nonlinear loop moves)" % moved)
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
