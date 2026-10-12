"""R4-1 (D): same machinery as (C) on the M=160 data; adds kernels F flat at x=0.
R4-1 (C): LRL shell weights whose ensemble mean is box + O(a^2 box^2 ln), and their per-realization deviation.
Operator (retarded, per realization):  (B phi)(x) = c phi(x) + sum_{m} f_m sum_{v in gL7 future, v^2=-m} phi(x - v).
Mean symbol at spacelike k (K = |k|):  Bbar(K) = c + sum_m g_m F_m(K),  g_m = C_m f_m,  F_m = 2 pi sqrt(m) K1(K sqrt m)/K
  = c + 2pi[ S0/K^2 + (1/2) sum g m (ln(K sqrt m/2)+gamma-1/2) + (K^2/16) sum g m^2 (ln(K sqrt m/2)+gamma-5/4) ] + O(K^4 ln K)
Conditions: S0 = sum g = 0, S1 = sum g m = 0, S2 = sum g m^2 = 0;  c = -(pi/2) sum g m ln m;  (pi/16) sum g m^2 ln m = -1.
Then Bbar(K) = -K^2 + O(K^4 ln K) = symbol of box (signature -+++).
Test function: phi = exp(-|y|_E^2/(2 l^2)) centred at the evaluation point; box phi(0) = -2/l^2.
"""
import numpy as np, sys, glob
from scipy.special import k1
fn = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob('r41_B_M96_seed7_eta1.0.npz'))[0]
d = np.load(fn); S = d['S']; I = d['I']; ells = d['ells']; C = d['C']; M = S.shape[2]
mvals = np.arange(1, M+1).astype(float)
Cm = C[1:M+1]
print(f"file {fn}: frames={S.shape[0]}, ells={ells.tolist()}, M={M}")

def finish(g):
    """given g on m=1..M satisfying S0=S1=S2=0 (up to scale): normalize, return f, c, g"""
    g = np.asarray(g, float)
    nrm = (np.pi/16)*np.sum(g*mvals**2*np.log(mvals))
    g = -g/nrm
    c = -(np.pi/2)*np.sum(g*mvals*np.log(mvals))
    return g/np.where(Cm > 0, Cm, np.inf), c, g

def divided_diff(shells):
    g = np.zeros(M)
    for i, mi in enumerate(shells):
        g[mi-1] = 1.0/np.prod([mi - mj for j, mj in enumerate(shells) if j != i])
    return finish(g)

def minnorm_f(shells):
    # minimize sum f^2 subject to sum C f m^k = 0 (k=0,1,2) and sum C f m^2 ln m = -16/pi
    idx = np.array(shells) - 1
    A = np.stack([Cm[idx]*mvals[idx]**k for k in range(3)] + [Cm[idx]*mvals[idx]**2*np.log(mvals[idx])])
    b = np.array([0, 0, 0, -16/np.pi])
    fs = A.T @ np.linalg.solve(A @ A.T, b)
    g = np.zeros(M); g[idx] = Cm[idx]*fs
    return finish(g)

def smooth_family(L, smooth_in='f', mmax=M, deg=3):
    # f_m (or g_m) = exp(-m/L^2) * poly_deg(m/L^2), poly fixed by S0=S1=S2=0 (+normalization): min-norm in poly coefficients
    x = mvals[:mmax]/L**2; base = np.exp(-x)
    cols = np.stack([base*x**j for j in range(deg+1)], 1)           # M x (deg+1)
    if smooth_in == 'f':
        G = cols*Cm[:mmax, None]
    else:
        G = cols
    A = np.stack([G.T @ mvals[:mmax]**k for k in range(3)] + [G.T @ (mvals[:mmax]**2*np.log(mvals[:mmax]))])
    b = np.array([0, 0, 0, -16/np.pi])
    coef = np.linalg.lstsq(A, b, rcond=None)[0]
    g = np.zeros(M); g[:mmax] = G @ coef
    return finish(g)

def mean_symbol(g, c, K):
    return c + np.sum(g[None, :]*2*np.pi*np.sqrt(mvals)[None, :]*k1(K[:, None]*np.sqrt(mvals)[None, :])/K[:, None], 1)

def report(name, f, c, g):
    S0 = g.sum(); S1 = (g*mvals).sum(); S2 = (g*mvals**2).sum()
    Kt = np.array([0.003, 0.01, 0.03, 0.1, 0.3])
    sym = mean_symbol(g, c, Kt)/(-Kt**2)
    print(f"\n== {name}:  shells used {int((np.abs(g) > 0).sum())}, max m {int(mvals[np.abs(g) > 0].max())},  c = {c:+.4f}, "
          f"sum|f| = {np.abs(f).sum():.3e}   moments S0,S1,S2 = {S0:.1e},{S1:.1e},{S2:.1e}")
    print("   mean symbol / (-K^2) at K = " + ", ".join(f"{k}:{s:.6f}" for k, s in zip(Kt, sym)))
    print("    l     mean B.phi/(box phi)   per-realization: rms rel dev   sd rel dev   max|rel dev|")
    out = []
    for j, l in enumerate(ells):
        box = -2.0/l**2
        bbar = c + np.sum(g*I[j])
        Bg = c + S[:, j, :] @ f
        rel = (Bg - bbar)/abs(box)
        out.append((l, bbar/box, np.sqrt(np.mean(rel**2)), rel.std(), np.abs(rel).max()))
        print(f"  {l:5.1f}   {bbar/box:12.6f}            {out[-1][2]:12.4e}   {out[-1][3]:10.3e}   {out[-1][4]:10.3e}")
    o = np.array(out)
    big = o[:, 0] >= 6
    if big.sum() >= 3:
        sl = np.polyfit(np.log(o[big, 0]), np.log(o[big, 2]), 1)[0]
        print(f"   fitted slope d ln(rms rel dev)/d ln l over l >= 6: {sl:+.2f}")
    return o


def flat_family(L, mmax=M, deg=3, smooth_in='f'):
    x = mvals[:mmax]/L**2; base = np.exp(-x - 1.0/x)
    cols = np.stack([base*x**j for j in range(deg+1)], 1)
    G = cols*Cm[:mmax, None] if smooth_in == 'f' else cols
    A = np.stack([G.T @ mvals[:mmax]**k for k in range(3)] + [G.T @ (mvals[:mmax]**2*np.log(mvals[:mmax]))])
    b = np.array([0, 0, 0, -16/np.pi])
    coef = np.linalg.lstsq(A, b, rcond=None)[0]
    g = np.zeros(M); g[:mmax] = G @ coef
    return finish(g)
res = {}
for L in (2.0, 3.0, 4.0):
    res[f"exp-cubic L={L}"] = report(f"F(x) = e^(-x) cubic(x), x = m/L^2, L = {L} (F(0) != 0)", *smooth_family(L, 'f'))
for L in (1.5, 2.0, 2.5, 3.0, 3.5, 4.0):
    res[f"flat L={L}"] = report(f"F(x) = e^(-x-1/x) cubic(x), x = m/L^2, L = {L} (F flat at 0)", *flat_family(L))
res["divdiff 1234"] = report("minimal 4-shell [1,2,3,4]", *divided_diff([1, 2, 3, 4]))
np.save('r41_D_results.npy', res, allow_pickle=True)
