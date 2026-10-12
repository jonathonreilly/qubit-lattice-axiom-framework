# I1 check 2: band sum rule for the boost anomaly, the face-touching partner, and the tower.
# Sum rule (proved): for any finite-N periodic C^2 fibre h(k) on T^d,
#   sum_a  int_T Hess(u_a) dk = int_T Hess(tr h^2 / 2) dk = 0   (u_a = E_a^2/2, labels irrelevant)
# so the band-and-zone average of the C3 anomaly (Hess u - beta I)/beta is exactly -I for every N.
import numpy as np
rng = np.random.default_rng(11)
print("(a) d=2 random finite-range N-band fibres: band-and-zone average of Hess(u)  [closure needs beta*I]")
L = 96
k = np.linspace(-np.pi, np.pi, L+1)[:-1]; KX, KY = np.meshgrid(k, k, indexing='ij'); dk = k[1]-k[0]
for N in (1, 2, 4, 8):
    terms = {}
    for rx in range(-2, 3):
        for ry in range(-2, 3):
            if (rx, ry) < (0, 0) or (rx, ry) in terms: continue
            M = rng.normal(size=(N,N)) + 1j*rng.normal(size=(N,N))
            terms[(rx, ry)] = M; terms[(-rx, -ry)] = M.conj().T
    terms[(0,0)] = terms[(0,0)] + terms[(0,0)].conj().T
    H = sum(M[None,None]*np.exp(1j*(rx*KX+ry*KY))[...,None,None] for (rx,ry), M in terms.items())
    E = np.linalg.eigvalsh(H); U = E**2/2                     # energy-sorted bands (with crossings)
    Uxx = (np.roll(U,-1,0)-2*U+np.roll(U,1,0))/dk**2
    Uyy = (np.roll(U,-1,1)-2*U+np.roll(U,1,1))/dk**2
    Uxy = (np.roll(np.roll(U,-1,0),-1,1)-np.roll(np.roll(U,-1,0),1,1)-np.roll(np.roll(U,1,0),-1,1)+np.roll(np.roll(U,1,0),1,1))/(4*dk**2)
    tot = np.array([[Uxx.sum(), Uxy.sum()],[Uxy.sum(), Uyy.sum()]])*dk*dk
    print("   N=%d  sum_a int Hess u_a = [[%.1e, %.1e],[%.1e, %.1e]]   (=> mean anomaly = -beta*I exactly)" % (N, tot[0,0], tot[0,1], tot[1,0], tot[1,1]))

print("\n(b) C1-type two-band face-touching construction (1D, beta=m=1):")
print("    lower band = exact SLAC E0=sqrt(1+k^2) on the zone; partner = tower band 1, sqrt(1+(2pi-rho(k))^2),")
print("    capped smoothly near k=0 (rho = |k| outside |k|<w).  Analytic branch B (partner) on the zone:")
kk = np.linspace(-np.pi, np.pi, 200001); h = kk[1]-kk[0]
for w in (1.0, 0.3, 0.1, 0.03):
    rho = np.where(np.abs(kk) >= w, np.abs(kk), (kk**2/w + w)/2)
    E1 = np.sqrt(1 + (2*np.pi - rho)**2); uB = E1**2/2
    upp = np.gradient(np.gradient(uB, h), h)
    integral = np.gradient(uB, h)[-1] - np.gradient(uB, h)[0]
    E0 = np.sqrt(1+kk**2)
    print("    w=%.2f: int(u_B'') = %.5f (pred -2pi=%.5f); mean anomaly (u_B''-1) = %.4f; min u_B'' = %.1f; partner >= lower: %s"
          % (w, integral, -2*np.pi, integral/(2*np.pi) - 1, upp[5:-5].min(), bool((E1 >= E0-1e-12).all())))
print("    -> the partner carries a fixed anomaly -2 (zone mean), independent of the cap; it sits at E ~ sqrt(1+4pi^2) = %.3f" % np.sqrt(1+4*np.pi**2))

print("\n(c) truncated tower with N analytic branches glued into one 2*pi*N-periodic branch U(kappa) (1D):")
print("    paraboloid U = (1+kappa^2)/2 on |kappa| < pi*N - w, smooth turn at the top; total anomaly int(U''-1):")
for N in (1, 3, 9, 27):
    Lk = np.pi*N; x = np.linspace(-Lk, Lk, 400001); hx = x[1]-x[0]; w = 0.5
    # C^1 cap: replace kappa^2 near +-pi N by its reflection-smoothed version (periodic in 2piN)
    s = Lk - np.abs(x)                       # distance to the top
    q = np.where(s >= w, x**2, (Lk - (s**2/w + w)/2)**2)
    U = (1+q)/2
    dU = np.gradient(U, hx)
    total = (dU[-1] - dU[0]) - 2*Lk          # int U'' - int 1 ; periodic => int U'' over a period = 0
    Etop = np.sqrt(1 + (Lk)**2)
    print("    N=%3d: int(U''-1) = %9.4f  (pred -2piN = %9.4f), located at E ~ %.1f" % (N, total, -2*np.pi*N, Etop))
