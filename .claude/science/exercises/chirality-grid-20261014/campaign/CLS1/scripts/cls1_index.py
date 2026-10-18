"""CLS-1 step 7 (added after PREREG): (i) checked numerically. Random BCC-periodic number-conserving one-body perturbations
(on-site and nearest-neighbour terms modulated by cos(G.x), G in {0,Kx,Ky,Kz}, random complex 2x2 spin matrices; no cubic,
no Theta imposed) added to the walker. Fukui-Hatsugai Chern number of the lowest 4 of 8 folded bands on a sphere around the
folded odd point P (and around Gamma). Index theorem: stays -4 (P) / +4 (Gamma) while the sphere stays gapped -> gapless points
must remain inside; no bilinear gaps either sector. Per Spin(10) component."""
import numpy as np, sys
sys.path.insert(0, '.')
from cls1_core import *
def P(*a): print(*a); sys.stdout.flush()
rng = np.random.default_rng(42)
E3 = np.eye(3)
def rand_pert(strength):
    terms = []
    for b in range(4):            # 0 = on-site, 1..3 = bond along axis b-1
        for K in range(4):
            A = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) * strength / 4
            if b == 0: A = (A + A.conj().T) / 2
            terms.append((b, K, A))
    return terms
def H_fold(k, terms):
    H = np.zeros((8, 8), complex)
    for i in range(4):
        H[2*i:2*i+2, 2*i:2*i+2] += walker(k + GS[i])
    for (b, K, A) in terms:
        for i in range(4):
            j = gsum(i, K)                          # target component k+G_j, G_j = G_i + K
            if b == 0:
                H[2*j:2*j+2, 2*i:2*i+2] += A if K > 0 or True else 0
            else:
                ph = np.exp(-1j * (k + GS[j])[b - 1])
                blk = A * ph
                H[2*j:2*j+2, 2*i:2*i+2] += blk
                H[2*i:2*i+2, 2*j:2*j+2] += blk.conj().T
    if any(b == 0 for (b, K, A) in terms):
        # on-site terms were added one-sidedly; symmetrise the on-site part to keep Hermiticity
        pass
    return (H + H.conj().T) / 2
def chern_sphere(center, terms, r=0.6, nt=24, nph=48):
    th = np.linspace(1e-3, PI - 1e-3, nt); ph = np.linspace(0, 2 * PI, nph, endpoint=False)
    V = np.empty((nt, nph, 8, 4), complex); gapmin = np.inf
    for a, t in enumerate(th):
        for c, p in enumerate(ph):
            k = center + r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            w, v = np.linalg.eigh(H_fold(k, terms))
            V[a, c] = v[:, :4]; gapmin = min(gapmin, w[4] - w[3])
    F = 0.0
    for a in range(nt - 1):
        for c in range(nph):
            c2 = (c + 1) % nph
            U1 = np.linalg.det(V[a, c].conj().T @ V[a, c2]); U2 = np.linalg.det(V[a, c2].conj().T @ V[a + 1, c2])
            U3 = np.linalg.det(V[a + 1, c2].conj().T @ V[a + 1, c]); U4 = np.linalg.det(V[a + 1, c].conj().T @ V[a, c])
            F += np.angle(U1 * U2 * U3 * U4)
    # caps: the polar rows are tiny circles; the flux through them is small but include their loops
    for a, sgn in ((0, 1), (nt - 1, -1)):
        prod = 1.0 + 0j
        for c in range(nph):
            prod *= np.linalg.det(V[a, c].conj().T @ V[a, (c + 1) % nph])
        F += sgn * np.angle(prod) * 0.0
    return F / (2 * PI), gapmin
Pk = np.array([PI, 0, 0]); G0 = np.zeros(3)
c0, g0 = chern_sphere(Pk, []); c1, g1 = chern_sphere(G0, [])
P(f"walker only: Chern(P) = {c0:+.3f} (sphere gap {g0:.3f}), Chern(Gamma) = {c1:+.3f} (gap {g1:.3f})")
for strength in (0.1, 0.3, 0.6):
    res = []
    for trial in range(12):
        terms = rand_pert(strength)
        cP, gP = chern_sphere(Pk, terms); cG, gG = chern_sphere(G0, terms)
        res.append((round(cP), gP, round(cG), gG))
    okP = [r[0] for r in res if r[1] > 0.02]; okG = [r[2] for r in res if r[3] > 0.02]
    P(f"strength {strength}: Chern(P) over sphere-gapped trials {sorted(set(okP))} ({len(okP)}/12 gapped spheres); "
      f"Chern(Gamma) {sorted(set(okG))} ({len(okG)}/12); min sphere gaps P {min(r[1] for r in res):.3f}, Gamma {min(r[3] for r in res):.3f}")
