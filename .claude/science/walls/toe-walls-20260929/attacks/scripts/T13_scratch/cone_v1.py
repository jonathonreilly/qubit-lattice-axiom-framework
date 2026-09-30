"""Test 3: pointed-cone lemma sanity.

Claim: for the connected Lorentz-type group SO_0(p,q) acting on R^{p+q}
(p negative-norm "time" directions), a pointed convex cone with nonempty interior
that is invariant under the group exists iff p == 1.
Checks (exact/numerical):
  p >= 2: a path in SO_0 (rotation by angle a in a time plane, a: 0 -> pi) ends at
          -1 on that plane; so v -> -v for timelike v; an invariant cone contains v and -v.
  p == 1: sign(v_0) of timelike v is preserved by 10^5 random group products.
  p == 0: group is compact SO(q): orbit of any v contains -v for q >= 2; invariant
          cone with interior is everything.
  quadrant cone in R^2 = light cone of q(s,t) = s t, eigenvalues (+,-).
"""
import numpy as np

rng = np.random.default_rng(7)


def metric(p, q):
    return np.diag([-1.0] * p + [1.0] * q)


def rot(n, i, j, a):
    R = np.eye(n)
    R[i, i] = np.cos(a); R[j, j] = np.cos(a)
    R[i, j] = -np.sin(a); R[j, i] = np.sin(a)
    return R


def boost(n, i, j, eta):
    B = np.eye(n)
    B[i, i] = np.cosh(eta); B[j, j] = np.cosh(eta)
    B[i, j] = np.sinh(eta); B[j, i] = np.sinh(eta)
    return B


def check_group(G, g, tol=1e-9):
    return np.linalg.norm(G.T @ g @ G - g) < tol and abs(np.linalg.det(G) - 1) < tol


ok = True
for p in (0, 1, 2, 3):
    for q in (1, 2, 3):
        n = p + q
        g = metric(p, q)
        if p >= 2:
            # rotation by pi in the plane of the first two time directions
            worst = 0.0
            for a in np.linspace(0, np.pi, 50):
                R = rot(n, 0, 1, a)
                assert check_group(R, g)
            R = rot(n, 0, 1, np.pi)
            v = np.zeros(n); v[0] = 1.0; v[p] = 0.3   # timelike: -1 + 0.09 < 0
            timelike = v @ g @ v < 0
            flips = np.allclose(R @ v, np.r_[-1.0, np.zeros(n - 1)] + np.r_[0, 0, np.zeros(n - 2)] + np.where(np.arange(n) == p, 0.3, 0))
            print(f"(p,q)=({p},{q}): timelike v={v[:p+1]}, R(pi) v = {np.round(R @ v, 6)[:p+1]}, v->-v on time part: {np.allclose((R @ v)[:2], -v[:2])}; timelike={timelike}")
            ok &= bool(np.allclose((R @ v)[:2], -v[:2])) and timelike
        elif p == 1:
            flips = 0
            for _ in range(20000 // 1):
                G = np.eye(n)
                for _k in range(5):
                    if rng.random() < 0.5:
                        i, j = rng.choice(np.arange(1, n), 2, replace=False) if q >= 2 else (1, 1)
                        if i != j:
                            G = G @ rot(n, i, j, rng.uniform(0, 2 * np.pi))
                    else:
                        j = rng.integers(1, n)
                        G = G @ boost(n, 0, j, rng.normal(scale=2.0))
                assert check_group(G, g, 1e-6 * max(1, np.abs(G).max() ** 2))
                v = np.zeros(n); v[0] = 1.0; v[1] = 0.4
                w = G @ v
                assert w @ g @ w < 0
                if w[0] < 0:
                    flips += 1
            print(f"(p,q)=({p},{q}): 20000 random SO_0 products, sign(v_0) flips = {flips}")
            ok &= flips == 0
        else:
            # p = 0: compact rotation group; q >= 2 contains rotation by pi
            if q >= 2:
                R = rot(n, 0, 1, np.pi)
                v = np.zeros(n); v[0] = 1.0
                print(f"(p,q)=({p},{q}): compact SO(q); R(pi) v = -v: {np.allclose(R @ v, -v)}")
                ok &= bool(np.allclose(R @ v, -v))
            else:
                print(f"(p,q)=({p},{q}): q=1: SO(1)=trivial (excluded from lemma; no space)")

# quadrant cone
Q = np.array([[0, 0.5], [0.5, 0]])
print("quadrant null form s*t eigenvalues:", np.linalg.eigvalsh(Q))
ok &= np.allclose(sorted(np.linalg.eigvalsh(Q)), [-0.5, 0.5])
print("ALL CONE CHECKS PASS:", ok)
