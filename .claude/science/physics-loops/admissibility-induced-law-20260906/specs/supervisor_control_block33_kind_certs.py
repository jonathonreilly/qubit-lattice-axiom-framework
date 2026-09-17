"""Exact rational super-solutions for the kind-typed count (unrestricted and R1-restricted).
Variables: G[e][k], e in D,U,F (R is derived), k in P,A,S with G[U][S] = 0 -> 8 unknowns.  A super-solution: a nonnegative
rational vector dominating its image under the map; then the least fixed point is below it and the count converges with
R <= image of the super-solution at the root."""
import sys, os, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block33_restricted_count as rc
KEYS = [(e, k) for e in "DUF" for k in "PAS" if not (e == "U" and k == "S")]
def image(G, xP, xA, eS, yF, variant, root=False):
    """G: dict (e,k)->value (Fractions or floats); returns the image dict (and the root value if root)."""
    Dsum = sum(G[("D", k)] for k in "PAS"); Fsum = sum(G[("F", k)] for k in "PAS")
    UP, UA = xP * G[("U", "P")], xA * G[("U", "A")]
    out = {}
    ents = "DUF" + ("R" if root else "")
    for e in ents:
        nup = 2 if e == "D" else 3; nfork = 5 if e == "F" else 6
        for k in "PAS":
            if e == "U" and k == "S": continue
            own = 1 if k == "S" else (3 * (xP if k == "P" else xA) * Dsum if e != "U" else 1)
            if k in "PA" and variant == "R1":
                up = (1 + UA) ** nup + nup * UP * (1 + UA) ** (nup - 1)
            else:
                up = (1 + UP + UA) ** nup
            fk = (1 + yF * Fsum) ** nfork
            out[(e, k)] = (eS if k == "S" else 1) * own * up * fk
    return out
def certificate(p, q, r, c, variant, t):
    d1, d2, d3 = rc.devs(p, q, r); e1, e2 = d1, max(d2, d3)
    xP, xA, eS, yF = Fr(t), e2 / Fr(t) ** c, e1, 1 / Fr(t) ** 3
    xf = {k: float(v) for k, v in dict(xP=xP, xA=xA, eS=eS, yF=yF).items()}
    G = {key: 0.0 for key in KEYS}
    for it in range(20000):
        Gn = image(G, xf["xP"], xf["xA"], xf["eS"], xf["yF"], variant)
        if max(Gn.values()) > 1e9: return None
        if max(abs(Gn[k] - G[k]) for k in KEYS) < 1e-15: G = Gn; break
        G = Gn
    v = np.array([G[k] for k in KEYS]); h = 1e-7; J = np.zeros((len(KEYS), len(KEYS)))
    def f(vec):
        GG = {k: vec[i] for i, k in enumerate(KEYS)}; im = image(GG, xf["xP"], xf["xA"], xf["eS"], xf["yF"], variant)
        return np.array([im[k] for k in KEYS])
    for j in range(len(KEYS)):
        e = np.zeros(len(KEYS)); e[j] = h * max(1.0, abs(v[j])); J[:, j] = (f(v + e) - f(v - e)) / (2 * e[j])
    w, V = np.linalg.eig(J); kk = np.argmax(w.real); vec = np.abs(V[:, kk].real); vec /= vec.max()
    for dl in (1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1):
        cand = v + dl * vec * np.maximum(1.0, np.abs(v))
        Gq = {k: Fr(round(cand[i] * 10**14), 10**14) for i, k in enumerate(KEYS)}
        im = image(Gq, xP, xA, eS, yF, variant, root=True)
        if all(Gq[k] >= im[k] for k in KEYS):
            Rq = im[("R", "P")] + im[("R", "A")] + im[("R", "S")]
            return dict(t=Fr(t), rho=w.real[kk], G=Gq, R=Rq, bound=e1 * Rq)
    return None
if __name__ == "__main__":
    for (p, q, r, c, variant) in ((4165, 1, 2, 2, "none"), (453, 1, 2, 1, "none"), (2921, 1, 2, 2, "R1"), (1464, 1, 1, 2, "R1"), (5842, 2, 4, 2, "R1"), (4380, 1, 3, 2, "R1"), (407, 1, 2, 1, "R1"), (209, 1, 1, 1, "R1"), (813, 2, 4, 1, "R1"), (608, 1, 3, 1, "R1")):
        best = None
        for tn in range(60, 160, 2):
            cert = certificate(p, q, r, c, variant, Fr(tn, 1000))
            if cert and (best is None or cert["bound"] < best["bound"]): best = cert
        if best is None: print(f"({p},{q},{r}) c={c} {variant}: no certificate on the grid"); continue
        print(f"({p},{q},{r}) c={c} {variant}: t={best['t']} rho={best['rho']:.4f} eps1*R={float(best['bound']):.3e} R={float(best['R']):.4f}")
        print("   G =", {f"{e}{k}": str(v) for (e, k), v in best["G"].items()})
