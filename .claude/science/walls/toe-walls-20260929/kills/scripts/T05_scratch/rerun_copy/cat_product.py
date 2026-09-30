"""Exact arm C: F - (mean predictive prob) vs F - (mean marginal prob), n qubits, z-menu, outcome '0'.
Sequential predictive p_t(0|x_<t) from the joint Born law; exact enumeration (no sampling)."""
import numpy as np
rng = np.random.default_rng(7)

def analyse(P, n, tag):
    P = P.reshape((2,) * n)
    xs = np.array(np.meshgrid(*[[0, 1]] * n, indexing="ij")).reshape(n, -1).T  # (2^n, n)
    flat = P.reshape(-1)
    # marginals over prefixes
    pred = np.zeros((flat.size, n))
    for t in range(n):
        # P(prefix of length t+1 with x_t=0) / P(prefix length t)
        axes_rest = tuple(range(t + 1, n))
        num_all = P.sum(axis=axes_rest) if axes_rest else P            # shape (2,)*(t+1)
        den_all = num_all.sum(axis=t)                                    # shape (2,)*t
        for i, x in enumerate(xs):
            pre = tuple(x[:t])
            den = den_all[pre] if t > 0 else 1.0
            num = num_all[pre + (0,)]
            pred[i, t] = num / den if den > 0 else 0.5
    F = (xs == 0).mean(axis=1)
    mean_pred = pred.mean(axis=1)
    marg = np.array([P.sum(axis=tuple(j for j in range(n) if j != t))[0] for t in range(n)])
    mean_marg = marg.mean()
    D1 = F - mean_pred
    D2 = F - mean_marg
    v1 = float((flat * (D1 - (flat * D1).sum()) ** 2).sum())
    v2 = float((flat * (D2 - (flat * D2).sum()) ** 2).sum())
    print(f"{tag:34s} n={n:2d}  mean odds={mean_marg:.4f}  Var(F-mean marginal)={v2:.5f}  Var(F-mean predictive)={v1:.6f}  bound 1/(4n)={1/(4*n):.5f}  ok={v1 <= 1/(4*n)+1e-12}")
    return v1, v2

allok = True
for n in (8, 12):
    a, b = np.sqrt(2 / 3), np.sqrt(1 / 3)
    # product
    psi = np.array([1.0])
    for _ in range(n):
        psi = np.kron(psi, np.array([a, b]))
    v1, _ = analyse(psi ** 2, n, "product (2/3,1/3)"); allok &= v1 <= 1 / (4 * n) + 1e-12
    # cat
    psi = np.zeros(2 ** n); psi[0] = a; psi[-1] = b
    v1, _ = analyse(psi ** 2, n, "cat sqrt(2/3)|0..0>+sqrt(1/3)|1..1>"); allok &= v1 <= 1 / (4 * n) + 1e-12
    # equal-weight GHZ
    psi = np.zeros(2 ** n); psi[0] = psi[-1] = 1 / np.sqrt(2)
    v1, _ = analyse(psi ** 2, n, "GHZ 1/2,1/2"); allok &= v1 <= 1 / (4 * n) + 1e-12
for k in range(4):
    n = 6
    psi = rng.normal(size=2 ** n) + 1j * rng.normal(size=2 ** n); psi /= np.linalg.norm(psi)
    v1, _ = analyse(np.abs(psi) ** 2, n, f"random 6-qubit state #{k}"); allok &= v1 <= 1 / (4 * n) + 1e-12
print("\nARM C:", "PASS (bound Var(F - mean predictive) <= 1/(4n) holds in every case)" if allok else "FAIL")
