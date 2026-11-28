# GUIDE run for library/gap-vargeom-opus.md Step 6, criterion C3 (row 960). Refutes or guides only; proves nothing.
# Lattice free massive scalar. Large box B+ = (b+1, c, c), small box B = (b, c, c).
# Best overlap^2 between the large-box vacuum Omega_L and any state of the form
#   psi = Omega_s(rho(phi')) x chi(phi'_inserted | phi'_kept)   (chi any normalised conditional state),
# which by Cauchy-Schwarz in the inserted variables equals <Omega_s o rho, M>^2 with M(x) = ||Omega_L(x, .)||_2.
# For Gaussians: overlap^2 = sqrt(det Wf det WM) / det((Wf + WM)/2), WM = (1/2) [ ((2 W_L)^-1)_kept ]^-1.
# Also: k inserted planes at once (doubling b -> 2b keeps every second plane) for small c.
import sys, resource
import numpy as np

LIMIT = 2 * 1024**3


def rss_check():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > LIMIT:
        print("RSS above 2 GB, stopping")
        sys.exit(3)


def lap_K(sides, m):
    # K = -Laplacian + m^2 on the periodic box, sites indexed lexicographically
    n1, n2, n3 = sides
    N = n1 * n2 * n3
    idx = np.arange(N).reshape(n1, n2, n3)
    K = np.zeros((N, N))
    K[np.arange(N), np.arange(N)] = 6 + m * m
    for ax in range(3):
        nb = np.roll(idx, -1, axis=ax).ravel()
        K[idx.ravel(), nb] -= 1
        K[nb, idx.ravel()] -= 1
    return K


def W_of(K):
    w, V = np.linalg.eigh(K)
    return (V * np.sqrt(w + w * w / 4)) @ V.T


def overlap2(b, c, m, inserted_planes):
    # large box: (b + len(inserted), c, c); small: (b, c, c); inserted_planes: sorted plane indices of the large box to drop
    hL = b + len(inserted_planes)
    KL = lap_K((hL, c, c), m)
    Ks = lap_K((b, c, c), m)
    WL = W_of(KL)
    Ws = W_of(Ks)
    keep_planes = [p for p in range(hL) if p not in set(inserted_planes)]
    assert len(keep_planes) == b
    idxL = np.arange(hL * c * c).reshape(hL, c, c)
    kept = idxL[keep_planes].ravel()  # kept sites of B+, in the order of the planes of B
    SigL = np.linalg.inv(2 * WL)
    WM = 0.5 * np.linalg.inv(SigL[np.ix_(kept, kept)])
    Wf = Ws  # kept sites ordered as the sites of B (plane j of B <-> keep_planes[j])
    s1 = np.linalg.slogdet(Wf)[1]
    s2 = np.linalg.slogdet(WM)[1]
    s3 = np.linalg.slogdet(0.5 * (Wf + WM))[1]
    rss_check()
    return 0.5 * (s1 + s2) - s3  # log overlap^2


def main():
    print("== C3a: one inserted plane (plane 1 of B+). columns: m b c  -log(overlap^2)  per transverse site")
    fails = 0
    for m in (1.0, 0.5, 0.25):
        for c in (2, 3, 4, 5, 6, 7, 8):
            for b in (c, 2 * c):
                if b < 3:
                    continue
                if (b + 1) * c * c > 1200:
                    continue
                lo = overlap2(b, c, m, [1])
                print("%5.2f %3d %2d   %.5f   %.5f" % (m, b, c, -lo, -lo / (c * c)))
                if c >= 4 and m * c >= 1 and -lo < 0.017:
                    fails += 1
                sys.stdout.flush()
    print("C3 OVL reading:", "FAILS (%d)" % fails if fails else "not refuted (every lift below 0.983 where tested)")

    print("== C3b: doubling b -> 2b by inserting b planes (keep every second plane). columns: m b c -log(overlap^2) per site of B")
    for m in (1.0, 0.5, 0.25):
        for c in (2, 3, 4):
            for b in (3, 4, 5, 6):
                if 2 * b * c * c > 1200:
                    continue
                ins = [2 * j + 1 for j in range(b)]
                lo = overlap2(b, c, m, ins)
                print("%5.2f %3d %2d   %.4f   %.5f" % (m, b, c, -lo, -lo / (b * c * c)))
                sys.stdout.flush()


if __name__ == "__main__":
    main()
