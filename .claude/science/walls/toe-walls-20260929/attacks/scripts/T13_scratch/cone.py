"""Test 3 (revised): invariant pointed cones under SO_0(p,q).

Lemma: for n = p+q >= 2, a closed pointed convex cone with nonempty interior that is
invariant under SO_0(p,q) exists iff min(p,q) == 1.
Proof structure checked here:
 (i)  min == 1: the cone {Q < 0 on the minority axis side} is invariant: 20000 random
      group products never flip the sign of the minority-axis coordinate of a vector
      inside the cone (the vector stays inside).
 (ii) min != 1: any invariant cone with interior contains some w with Q(w) != 0 (Q = 0 is
      a null set).  We construct, for BOTH signs of Q(w), an SO_0 element (a path of
      rotations from the identity, so connected to 1) that maps w to -w.
      Q(w) < 0 needs p >= 2 (rotation by pi in a time plane) or, for p = 0, none exist.
      Q(w) > 0 needs q >= 2 (rotation by pi in a space plane).
      If min(p,q) >= 2 both exist -> not pointed.  If min == 0 (definite), one sign
      is absent and the other has a rotation by pi (n >= 2).
"""
import numpy as np

rng = np.random.default_rng(11)


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


def in_group(G, g, tol):
    return np.linalg.norm(G.T @ g @ G - g) < tol and abs(np.linalg.det(G) - 1) < tol


def random_element(p, q, k=6):
    n = p + q
    G = np.eye(n)
    for _ in range(k):
        i, j = rng.choice(n, 2, replace=False)
        same = (i < p) == (j < p)
        G = G @ (rot(n, i, j, rng.uniform(0, 2 * np.pi)) if same else boost(n, i, j, rng.normal(scale=1.5)))
    return G


results = {}
for p in range(0, 5):
    for q in range(0, 5):
        n = p + q
        if n < 2:
            continue
        g = metric(p, q)
        mn = min(p, q)
        if mn == 1:
            # minority axis: index 0 if p == 1 (time), index p if q == 1 (space-like minority)
            axis = 0 if p == 1 else p
            sgn_form = -1.0 if p == 1 else 1.0   # sign of Q on the axis direction
            # cone: Q has the axis-sign and axis coordinate > 0.  test invariance
            flips = 0
            trials = 4000
            for _ in range(trials):
                G = random_element(p, q)
                if not in_group(G, g, 1e-6 * max(1.0, np.abs(G).max() ** 2)):
                    continue
                u = np.zeros(n); u[axis] = 1.0
                # a vector inside the cone: mostly axis, small others
                v = u + 0.3 * rng.normal(size=n) * (np.arange(n) != axis) / np.sqrt(n)
                if (v @ g @ v) * sgn_form <= 0:
                    continue
                w = G @ v
                assert (w @ g @ w) * sgn_form > 0
                if w[axis] <= 0:
                    flips += 1
            results[(p, q)] = ("exists", flips)
        else:
            has_neg = p >= 2   # a time-plane rotation by pi exists (Q<0 vectors reversible)
            has_pos = q >= 2
            need_neg = p >= 1  # negative-norm vectors exist
            need_pos = q >= 1
            ok_neg = (not need_neg) or has_neg
            ok_pos = (not need_pos) or has_pos
            # explicit witnesses
            wit = []
            if need_neg and has_neg:
                R = rot(n, 0, 1, np.pi); w = np.zeros(n); w[0] = 1.0
                assert in_group(R, g, 1e-9) and np.allclose(R @ w, -w) and (w @ g @ w) < 0
                wit.append("Q<0 reversible")
            if need_pos and has_pos:
                R = rot(n, p, p + 1, np.pi); w = np.zeros(n); w[p] = 1.0
                assert in_group(R, g, 1e-9) and np.allclose(R @ w, -w) and (w @ g @ w) > 0
                wit.append("Q>0 reversible")
            results[(p, q)] = ("none" if (ok_neg and ok_pos) else "??", wit)

expected = lambda p, q: "exists" if min(p, q) == 1 else "none"
allok = True
for (p, q), (verdict, info) in sorted(results.items()):
    good = verdict == expected(p, q) and (verdict != "exists" or info == 0)
    allok &= good
    print(f"(p,q)=({p},{q}) n={p+q}: invariant pointed cone {verdict:6s}  {info}   {'OK' if good else 'MISMATCH'}")
print("quadrant null form s*t eigenvalues:", np.linalg.eigvalsh(np.array([[0, 0.5], [0.5, 0]])), "(signature (1,1))")
print("ALL PASS:", allok)
