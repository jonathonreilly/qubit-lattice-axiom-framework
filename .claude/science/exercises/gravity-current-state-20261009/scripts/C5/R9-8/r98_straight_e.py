"""R9-8: electron speed for BQ-W with STRAIGHT-LINE Wilson lines (Terning/Mandelstam path), photon momentum q taken in the
fundamental domain (-pi,pi]^3 (sharp, alias-free band-limited interpolation of A: exactly gauge invariant, but the
photon-matter coupling then has power-law tails -- outside the l1 class; the smooth-alias l1 version is not run).
  vertex  V_j(p,k) = delta_j/Dhat_j(q),  delta_j = q_j int_0^1 ds d_j h_W(k + s q)       (sum_j delta_j = h_W(p)-h_W(k) exactly)
  seagull S_jj(p;q,-q) = (q_j^2/d_j^2) int_0^1 (1-u) [d_j^2 h_W(p+u q) + d_j^2 h_W(p-u q)] du   (full 3-vector q)
For separable h (F = 1) both reduce identically to R8-5's BQ rules.  Photon side: r98_paths.py ('straight').
Feynman gauge, Clifford closed forms exactly as r98_frame_qed.fermion."""
import numpy as np, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r98_frame_qed import LawW, comps_norm, dot4, kgrid1, U, photon
from r98_paths import run as photon_paths

def dj(law, k, j, hs=1e-3):
    def at(s):
        kk = list(k); kk[j] = kk[j] + s; return law.hW(*kk)
    a, b, c, d = at(2 * hs), at(hs), at(-hs), at(-2 * hs)
    return tuple((-a[i] + 8 * b[i] - 8 * c[i] + d[i]) / (12 * hs) for i in range(4))

def djj(law, k, j, hs=2e-3):
    def at(s):
        kk = list(k); kk[j] = kk[j] + s; return law.hW(*kk)
    a, b, c, d, e = at(2 * hs), at(hs), at(0.0), at(-hs), at(-2 * hs)
    return tuple((-a[i] + 16 * b[i] - 30 * c[i] + 16 * d[i] - e[i]) / (12 * hs ** 2) for i in range(4))

def fermion_straight(law, N, lam, hp=(1e-3, 2e-3), chunk=8, ng=12):
    q1 = kgrid1(N); QY, QZ = np.meshgrid(q1, q1, indexing="ij")
    gs, gw = np.polynomial.legendre.leggauss(ng); s01 = 0.5 * (gs + 1); w01 = 0.5 * gw
    uw01 = w01 * (1 - s01)
    A_id = 0.0; tadd = 0.0
    sun = {p: 0.0 for p in [s * h for h in hp for s in (+1, -1)]}
    for i0 in range(0, N, chunk):
        qx = q1[i0:i0 + chunk][:, None, None] + 0 * QY[None]; qy = QY[None] + 0 * qx; qz = QZ[None] + 0 * qx
        q = (qx, qy, qz)
        d2 = tuple(law.d(qq) ** 2 for qq in q)
        Om = np.sqrt(d2[0] + d2[1] + d2[2] + lam ** 2)
        # tadpole: (1/2) sum_j < d/dp_x [S_jj(p;q)]_{alpha_x} / (2 Om) > at p = 0
        h1 = hp[0]; tsum = 0.0
        for j in range(3):
            val = {}
            for sg in (+1, -1):
                acc = 0.0
                for u, w in zip(s01, uw01):
                    for su in (+1, -1):
                        kk = (sg * h1 + su * u * qx, su * u * qy, su * u * qz)
                        acc = acc + w * djj(law, kk, j)[0]
                val[sg] = acc * q[j] ** 2 / d2[j]
            tsum = tsum + (val[1] - val[-1]) / (2 * h1) / (2 * Om)
        tadd += 0.5 * np.sum(tsum)
        for p in list(sun.keys()) + [0.0]:
            k = (p - qx, -qy, -qz)
            n, E = comps_norm(law.hW(*k))
            db = []
            for j in range(3):
                acc = [0.0] * 4
                for s, w in zip(s01, w01):
                    g = dj(law, (k[0] + s * qx, k[1] + s * qy, k[2] + s * qz), j)
                    for c in range(4): acc[c] = acc[c] + w * g[c]
                db.append(tuple(q[j] * acc[c] for c in range(4)))
            if p == 0.0:
                s2 = sum(dot4(db[j], db[j]) / d2[j] for j in range(3))
                A_id += np.sum((s2 - 1) / (2 * Om * (Om + E) ** 2)); continue
            comp = -n[0]
            for j in range(3):
                comp = comp + (2 * dot4(db[j], n) * db[j][0] - dot4(db[j], db[j]) * n[0]) / d2[j]
            sun[p] += np.sum(-comp / (2 * Om * (Om + E)))
    V = N ** 3; A_id /= V; tadd /= V
    for p in sun: sun[p] /= V
    h1, h2 = hp
    sund = (4 * (sun[h1] - sun[-h1]) / (2 * h1) - (sun[h2] - sun[-h2]) / (2 * h2)) / 3
    B = sund + tadd
    return dict(A_id=A_id, B=B, tad=tadd, dce=B - A_id)

if __name__ == "__main__":
    t0 = time.time()
    b1, b2, r, c1, c2 = [float(x) for x in sys.argv[1:6]]; N = int(sys.argv[6]); m = float(sys.argv[7]); lam = float(sys.argv[8])
    E1, E2 = float(sys.argv[9]), float(sys.argv[10]); ng = int(sys.argv[11]) if len(sys.argv) > 11 else 12
    if E1 < 0: E1 = E2 = None
    law = LawW(b1, b2, r, c1, c2, m, E1, E2)
    fe = fermion_straight(law, N, lam, ng=ng)
    PE, PMst, PMsl = photon_paths(law, N)
    dcg = (PMsl - PE) / 2
    print(f"straight b=({b1},{b2}) c=({c1},{c2}) E=({E1},{E2}) N={N} m={m} ng={ng} | dc_g*U={U*dcg:+.4f} | A*U={U*fe['A_id']:+.4f}"
          f" B*U={U*fe['B']:+.4f} [tad {U*fe['tad']:+.4f}] dc_e*U={U*fe['dce']:+.4f} | DELTA={U*(fe['dce']-dcg):+.4f} ({time.time()-t0:.0f}s)", flush=True)
