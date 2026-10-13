"""R17-3 probe (a)/(c): the one record map realized on file, applied to the vacuum.
Setting (supplied, from docs/THE_RECORD_MAP_KEEPS_THE_MASS_FRACTION_..._2026-09-04.md, T1-T2):
real symmetric KS hopping M on an even periodic L^3 torus, eta = (1, (-1)^x, (-1)^(x+y)), Gamma = (-1)^(x+y+z),
H = M + m Gamma, half-filled sea (negative levels filled).  W1 pinching D(O) = diag(O) in the occupation basis.
Recorded (pinched) energy per site r_v = m eps_v (P_vv - 1/2) = -(m^2/2)[(M^2+m^2)^(-1/2)]_vv (note T2).
Checks:
 1. exact diagonalization at L = 8 and 12 against the note's printed values (counted once; reproduces the note);
 2. Bloch form [(M^2+m^2)^(-1/2)]_vv = < (m^2 + sum_a 4cos^2 k_a)^(-1/2) >_BZ, and c0 = its m -> 0 limit (L -> large);
 3. sea energy relative to the trace zero (the particle-hole-symmetric zero): E0/V = -(1/2)<sqrt(m^2 + 4 sum cos^2 k)>;
 4. physical sizes with the scale bridge a = l_P (AX:189-190; RECALLED inputs), against rho_Lambda.
Subtraction named before the run: none for r_v (pinching keeps it); for item 3 the trace (Tr H = 0) is the zero.
"""
import numpy as np, itertools

def ks(L, m):
    idx = lambda x, y, z: ((x % L)*L + (y % L))*L + (z % L)
    V = L**3
    M = np.zeros((V, V))
    G = np.zeros(V)
    for x, y, z in itertools.product(range(L), repeat=3):
        i = idx(x, y, z)
        G[i] = (-1)**(x + y + z)
        for a, (dx, dy, dz) in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
            eta = [1, (-1)**x, (-1)**(x + y)][a]
            j = idx(x + dx, y + dy, z + dz)
            M[i, j] += eta; M[j, i] += eta
    return M, G

print("1. Exact diagonalization vs the note (T2):")
for L, ms, ref in [(8, [0.3, 1.0, 2.0, 6.0], [-.021413851, -.201703228, -.648782512, -2.781026670]), (12, [1.0], [-.200917464424])]:
    M, G = ks(L, 0)
    acomm = np.abs(M @ np.diag(G) + np.diag(G) @ M).max()
    for mm, rr in zip(ms, ref):
        H = M + mm*np.diag(G)
        w, U = np.linalg.eigh(H)
        P = U[:, w < 0] @ U[:, w < 0].T
        r = mm*G*(np.diag(P) - 0.5)
        print("   L=%2d m=%.1f: r_v mean=%.12f spread=%.1e  note=%.12f  |{M,Gamma}|max=%.0e" % (L, mm, r.mean(), r.max() - r.min(), rr, acomm))

def bz(L, m):
    k = 2*np.pi*np.arange(L)/L
    c2 = 4*np.cos(k)**2
    S = c2[:, None, None] + c2[None, :, None] + c2[None, None, :]
    with np.errstate(divide='ignore'):
        inv = np.where(m**2 + S > 0, 1/np.sqrt(m**2 + S), 0.0)
    return inv.mean(), np.sqrt(m**2 + S).mean()

print("2. Bloch form (same quantities): ")
for L, mm in [(8, 1.0), (12, 1.0), (8, 0.3)]:
    ci, e = bz(L, mm)
    print("   L=%d m=%.1f: -(m^2/2)<(m^2+M^2)^-1/2> = %.12f" % (L, mm, -0.5*mm**2*ci))
# c0: odd L avoids the exact zero modes cos k = 0 ... use large even L with m small and extrapolate in m
for L in [64, 128, 256]:
    vals = []
    for mm in [1e-2, 3e-3, 1e-3]:
        ci, e = bz(L if L % 4 else L + 1, mm)   # L+1 odd: no k with all cos = 0 exactly
        vals.append(ci)
    print("   L~%d: <(m^2+M^2)^-1/2> at m = 1e-2, 3e-3, 1e-3: %.6f %.6f %.6f" % (L, *vals))
c0 = bz(257, 1e-3)[0]
print("   c0 ~= %.4f (lattice units; finite in 3D since the integrand ~ 1/|q| near the cones)" % c0)
print("   small-m law: r_v ~= -(c0/2) m^2 ; recorded vacuum energy moves with every mass threshold.")
print("3. Sea energy relative to the trace zero (chiral/particle-hole symmetric point):")
for mm in [0.0, 1e-3, 0.3, 1.0]:
    ci, e = bz(257, mm)
    print("   m=%.3g: E0/V = -(1/2)<|eps|> = %.6f per site" % (mm, -0.5*e))
# physical sizes, a = l_P (RECALLED inputs)
MP = 1.22089e19          # GeV, unreduced Planck mass = 1/l_P  (RECALLED)
rhoL = 0.685*0.674**2*8.0992e-47   # GeV^4  (Omega_L h^2 * rho_crit/h^2; RECALLED Planck 2018)
print("4. Physical sizes with a = l_P (scale bridge AX:189-190 is OPEN; inputs RECALLED):  rho_Lambda = %.3e GeV^4" % rhoL)
for name, mass in [('electron', 0.000511), ('muon', 0.10566), ('b quark', 4.18), ('W', 80.38), ('top', 172.7)]:
    d = 0.5*c0*mass**2*MP**2
    print("   %-8s: recorded-vacuum shift (c0/2) m^2 M_P^2 = %.3e GeV^4 = %.2e rho_Lambda (per staggered field)" % (name, d, d/rhoL))
ci, e = bz(257, 0.0)
print("   trace-zero sea: |E0| M_P^4 = %.3e GeV^4 = %.2e rho_Lambda (negative)" % (0.5*e*MP**4, 0.5*e*MP**4/rhoL))
