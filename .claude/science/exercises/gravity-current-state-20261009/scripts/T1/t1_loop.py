"""T1 common one-loop machinery (Euclidean, continuous time, translation-invariant spatial regulators).

Theory: L = psibar (i g0 q0 + i g.S(q) + M(q)) psi + 1/2 phi (q0^2 + w2(q)) phi + g phi psibar psi,
4-component Dirac psi, Hermitian Euclidean gammas.  Optional Collins-type factors multiply the
free propagators: G -> fF(q) G, D -> fB(q) D.

Gamma_F(p) = i g0 p0 (1+A) + i g.p (1+B) + mass terms;   delta c_psi = B - A      (O(g^2), g=1)
Gamma_B(p) = p0^2 (1+a) + p^2 (1+b) + mass;              delta c_phi = (b - a)/2
Delta = 16 pi^2 (dc_psi - dc_phi).

Closed forms after the q0 integral (derived in the T1 report; checked against direct q0 quadrature
in selftest_q0()):
  J0(E,E',p0) = int dq0/2pi 1/((q0^2+E^2)((q0+p0)^2+E'^2)) = (E+E')/(2EE'((E+E')^2+p0^2))
  J2 = int q0(q0+p0)/(..)(..) = 1/2[1/(2E)+1/(2E') - (p0^2+E^2+E'^2) J0]
  I1 = int q0/((q0^2+E^2)((p0-q0)^2+w^2)) = p0/(2w((E+w)^2+p0^2))
  A = int_q fF fB / (2 w (E+w)^2)
  B = -int_q fF S_x d_x[fB/(2 E w (E+w))]   (derivative acts on the boson line only)
  a = 1/2 int_q fF^2 S^2/E^5
  b = 1/2 d^2/dp_x^2 Pi(0,p),  Pi(0,p) = 4 int_q fF fF' (M M' - S.S' - E E')/(2 E E' (E+E'))
All integrals are int d^3q/(2pi)^3 (supplied as weights).
"""
import numpy as np


def selftest_q0():
    from scipy.integrate import quad
    rng = np.random.default_rng(1)
    worst = 0.0
    for _ in range(20):
        E, Ep, w, p0 = rng.uniform(0.2, 2.0, 4)
        J0n = quad(lambda x: 1 / ((x * x + E * E) * ((x + p0) ** 2 + Ep * Ep)), -np.inf, np.inf)[0] / (2 * np.pi)
        J0c = (E + Ep) / (2 * E * Ep * ((E + Ep) ** 2 + p0 * p0))
        J2n = quad(lambda x: x * (x + p0) / ((x * x + E * E) * ((x + p0) ** 2 + Ep * Ep)), -np.inf, np.inf)[0] / (2 * np.pi)
        J2c = 0.5 * (1 / (2 * E) + 1 / (2 * Ep) - (p0 * p0 + E * E + Ep * Ep) * J0c)
        I1n = quad(lambda x: x / ((x * x + E * E) * ((p0 - x) ** 2 + w * w)), -np.inf, np.inf)[0] / (2 * np.pi)
        I1c = p0 / (2 * w * ((E + w) ** 2 + p0 * p0))
        worst = max(worst, abs(J0n - J0c) / J0c, abs(J2n - J2c) / abs(J2c), abs(I1n - I1c) / abs(I1c))
    return worst


def coeffs(wt, F, B, h=1e-3, mt=0.0):
    """wt: quadrature weights for int d^3q/(2pi)^3.
    F: dict with fermion arrays S (3,...), M, dS (3,...) = d_x S_b, d2S (3,...) = d_x^2 S_b, dM, d2M,
       fF, dfF, d2fF  (Collins factor and its x-derivatives; 1,0,0 if absent).
    mt: optional twisted IR mass (term -i g5 mt in the fermion action): E^2 = S^2 + M^2 + mt^2,
        tr[G G'] mass part M M' -> M M' - mt^2,  a -> 1/2 int (S^2+mt^2)/E^5.  A, B unchanged in form.
    B: dict with boson arrays w2, dw2 (= d_x w2), fB, dfB.
    Returns dict of A, B, a, b, dc_psi, dc_phi, Delta (g = 1)."""
    S, M = F["S"], F["M"]
    S2 = (S * S).sum(0)
    E = np.sqrt(S2 + M * M + mt * mt)
    w = np.sqrt(B["w2"])
    dw = B["dw2"] / (2 * w)
    fF, fB = F["fF"], B["fB"]
    # fermion self-energy pieces
    A_int = fF * fB / (2 * w * (E + w) ** 2)
    hB = 1.0 / (2 * E * w * (E + w))
    dhB_dw = -(E + 2 * w) / (2 * E * w * w * (E + w) ** 2)
    Bf_int = -fF * S[0] * (B["dfB"] * hB + fB * dhB_dw * dw)
    # boson self-energy pieces
    a_int = 0.5 * fF * fF * (S2 + mt * mt) / E ** 5

    def Pi_int(Mp, Sp, fFp):
        Ep = np.sqrt((Sp * Sp).sum(0) + Mp * Mp + mt * mt)
        return 4 * fF * fFp * (M * Mp - mt * mt - (S * Sp).sum(0) - E * Ep) / (2 * E * Ep * (E + Ep))

    P0 = Pi_int(M, S, fF)
    Pp = Pi_int(M + h * F["dM"] + 0.5 * h * h * F["d2M"], S + h * F["dS"] + 0.5 * h * h * F["d2S"],
                fF + h * F["dfF"] + 0.5 * h * h * F["d2fF"])
    Pm = Pi_int(M - h * F["dM"] + 0.5 * h * h * F["d2M"], S - h * F["dS"] + 0.5 * h * h * F["d2S"],
                fF - h * F["dfF"] + 0.5 * h * h * F["d2fF"])
    b_int = 0.5 * (Pp + Pm - 2 * P0) / (h * h)
    out = dict(A=(wt * A_int).sum(), B=(wt * Bf_int).sum(), a=(wt * a_int).sum(), b=(wt * b_int).sum())
    out["dc_psi"] = out["B"] - out["A"]
    out["dc_phi"] = 0.5 * (out["b"] - out["a"])
    out["Delta"] = 16 * np.pi ** 2 * (out["dc_psi"] - out["dc_phi"])
    # integrands of the two speed shifts, for region decomposition
    out["_ipsi"] = wt * (Bf_int - A_int)
    out["_iphi"] = wt * 0.5 * (b_int - a_int)
    return out


if __name__ == "__main__":
    print("q0 closed forms vs quadrature, worst rel err:", selftest_q0())
