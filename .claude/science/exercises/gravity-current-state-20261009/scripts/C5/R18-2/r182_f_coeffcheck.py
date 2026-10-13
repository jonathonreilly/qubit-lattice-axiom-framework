"""R18-2 (f): is the RECALLED Buttazzo comparator diagnostic of the two-loop transcription?
Swap in the alternative two-loop coefficients found in the repo runner scripts/frontier_higgs_mass_full_3loop.py:236-279
(converted to SM-normalized gY) and compare lam(M_P) with the comparator -0.0143 at (173.34, 125.15, 0.1184)."""
import numpy as np
import smrge
from smrge import run, MP, K

orig = smrge.beta_sm


def beta_repo(y, loops=2):
    out = orig(y, 1)
    gY, g2, g3, yt, L = y[:5]
    g1sq = 5 / 3 * gY**2
    a, b, c, t2 = gY**2, g2**2, g3**2, yt**2
    K2 = K**2
    bgY = K2 * gY**3 * (199 / 18 * a + 4.5 * b + 44 / 3 * c - 17 / 6 * t2)
    bg2 = K2 * g2**3 * (1.5 * a + 35 / 6 * b + 12 * c - 1.5 * t2)
    bg3 = K2 * g3**3 * (11 / 6 * a + 4.5 * b - 26 * c - 2 * t2)
    byt = K2 * yt * (-12 * t2**2 + t2 * (36 * c + 225 / 16 * b + 131 / 80 * g1sq) + 1187 / 216 * g1sq**2 - 23 / 4 * b**2
                     - 108 * c**2 + 19 / 15 * g1sq * c + 9 / 4 * b * c + 6 * L**2 - 6 * L * t2)
    blam = K2 * (-312 * L**3 - 144 * L**2 * t2 - 3 * L * t2**2 + 30 * t2**3 + 80 * L * t2 * c + 22.5 * L * t2 * b
                 + 85 / 6 * L * t2 * a - 32 * t2**2 * c - 4.5 * t2**2 * b + 8.5 * t2**2 * a + 36 * L**2 * (3 * b + a)
                 - 73 / 8 * L * b**2 + 39 / 4 * L * b * a + 629 / 24 * L * a**2 + 305 / 16 * b**3 - 289 / 48 * b**2 * a
                 - 559 / 48 * b * a**2 - 379 / 48 * a**3 - 8 / 5 * a * t2**2)
    return [out[0] + bgY, out[1] + bg2, out[2] + bg3, out[3] + byt, out[4] + blam]


for lab, fn in [("mine (R18-2 transcription)", orig), ("repo runner variant", beta_repo)]:
    smrge.beta_sm = fn
    T, Y = run(173.34, 125.15, 0.1184, mu_max=MP * 1.01, npts=800)
    lmp = np.interp(np.log(MP), T, Y[4])
    print("%-28s lam(M_P) = %+.5f ; comparator (RECALLED) = -0.0143 ; diff = %+.5f ; yt(M_P) = %.4f" % (lab, lmp, lmp + 0.0143, np.interp(np.log(MP), T, Y[3])))
smrge.beta_sm = orig
