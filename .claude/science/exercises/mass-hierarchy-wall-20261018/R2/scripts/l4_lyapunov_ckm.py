"""R2 / L4: CKM from a shared random chain (Anderson / theory-space variant).
M_u = A_Q B_u, M_d = A_Q B_d with A_Q a product of L_Q i.i.d. complex Ginibre steps and
B_u, B_d independent products of L_u, L_d steps.  Report median |Vus|, |Vcb|, |Vub| and the ratio."""
import numpy as np
rng = np.random.default_rng(5)
gin = lambda: (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2)
def prod(n):
    P = np.eye(3, dtype=complex)
    for _ in range(n):
        P = gin() @ P
    return P
for (LQ, Lu, Ld) in [(4, 8, 4), (8, 8, 4), (12, 4, 2), (16, 2, 2)]:
    out = []
    for _ in range(1500):
        A = prod(LQ); Mu = A @ prod(Lu); Md = A @ prod(Ld)
        Uu = np.linalg.svd(Mu)[0]; Ud = np.linalg.svd(Md)[0]
        V = np.abs(Uu.conj().T @ Ud)
        sd = np.linalg.svd(Md, compute_uv=False)
        out.append((V[1, 2], V[0, 1], V[0, 2], sd[1] / sd[0], sd[2] / sd[1]))
    o = np.median(np.array(out), axis=0)
    r = np.median(np.array(out)[:, 1] / np.array(out)[:, 0])
    print(f"L_Q={LQ:2d} L_u={Lu} L_d={Ld}: median |Vus|={o[0]:.3f} |Vcb|={o[1]:.3f} |Vub|={o[2]:.4f}  median Vcb/Vus={r:.2f}  m_s/m_b={o[3]:.3f} m_d/m_s={o[4]:.3f}")
print("observed: |Vus|=0.225 |Vcb|=0.041 |Vub|=0.0037 Vcb/Vus=0.18; m_s/m_b~0.019 m_d/m_s~0.053")
