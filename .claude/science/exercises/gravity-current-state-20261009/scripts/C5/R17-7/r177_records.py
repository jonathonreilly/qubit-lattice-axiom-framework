"""R17-7, the record/permanence test (AX:79-83) of (S): C = E0[H] ("the law's lowest state weighs nothing").
Setting (supplied, counted once from R17-3 / the record-map note): real symmetric KS hopping M on an even L^3 torus,
H = M + m Gamma, half-filled sea; many-body H normal-ordered at the trace zero; W1 pinching = dephasing in the
occupation (record) basis.  Reading R-proj (stated before the run, NOT axiom content): a record at site x locks the
occupation of x, i.e. it acts on the physical state as the dephasing D_x.  Reading R-label: records are labels that do
not change the physical state's energy (then nothing below applies).
Checks:
 R1  Lemma X (elementary): for H = H_diag + H_off in the record basis, a pinched state keeps <H_diag>; for the ground
     state the recorded excess <H>_pinch - E0 = -<H_off>_0 >= 0 (variational), = 0 iff the ground state is diagonal.
     Computed per site for the KS sea (ED at L = 8, Bloch at L = 257) against the trace zero and against E0.
 R2  One record (dephase one site) in the sea: Delta E_1 = -2 sum_y M_xy <c_x^dag c_y>_0 (exact for Gaussian states).
 R3  Sizes with the scale bridge a = l_P (OPEN, AX:189-190; RECALLED inputs).
 R4  Lemma M under (S): permanent records with fixed excess eps_rec > 0 give a3 rho_rec non-decreasing (w_eff <= 0).
     Toy: constant formation rate per physical volume, Gamma*eps, in a LCDM background: w_eff(z).
Subtraction rule: excess is measured from E0 (the (S) zero); the trace zero is printed only for comparison.
"""
import numpy as np, itertools
from scipy.integrate import solve_ivp

def ks(L):
    idx = lambda x, y, z: ((x % L)*L + (y % L))*L + (z % L)
    V = L**3
    M = np.zeros((V, V)); G = np.zeros(V)
    for x, y, z in itertools.product(range(L), repeat=3):
        i = idx(x, y, z); G[i] = (-1)**(x + y + z)
        for a, (dx, dy, dz) in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
            eta = [1, (-1)**x, (-1)**(x + y)][a]
            j = idx(x + dx, y + dy, z + dz)
            M[i, j] += eta; M[j, i] += eta
    return M, G

print("R1/R2. KS sea, ED at L = 8 (per site, lattice units, energy unit hbar c / a):")
M, G = ks(8)
N = M.shape[0]
for m in [0.0, 0.3, 1.0, 2.0]:
    H = M + m*np.diag(G)
    w, U = np.linalg.eigh(H)
    occ = w < -1e-12
    nz = np.sum(np.abs(w) < 1e-12)
    P = U[:, occ] @ U[:, occ].T                       # <c_j^dag c_i> = P_ij (real)
    if nz:                                            # m = 0 has exact zero modes at L = 8: fill half of them
        Z = U[:, np.abs(w) < 1e-12]; P = P + 0.5*Z @ Z.T   # mixed half-filling of the zero modes (energy unaffected)
    E0 = np.sum(w[occ])/N                             # trace zero: Tr H = 0
    Ediag = np.sum(m*G*(np.diag(P) - 0.5))/N          # pinched (all sites recorded): keeps the diagonal part
    Eoff = np.sum(M*P)/N                              # <H_off>_0 per site
    exc = Ediag - E0
    # one record at site 0: dephase site 0 -> lose the expectation of every bond touching 0
    dE1 = -2*np.sum(M[0, :]*P[0, :])
    print("   m=%.1f: E0/N = %+.6f ; pinched <H>/N = %+.6f ; excess over E0 = %+.6f ; -<H_off>_0/N = %+.6f ; "
          "one-record cost Delta E_1 = %+.6f%s" % (m, E0, Ediag, exc, -Eoff, dE1, "  (zero modes: half-filled mixture)" if nz else ""))

def bz(L, m):
    k = 2*np.pi*np.arange(L)/L
    c2 = 4*np.cos(k)**2
    S = c2[:, None, None] + c2[None, :, None] + c2[None, None, :]
    E = np.sqrt(m**2 + S)
    with np.errstate(divide='ignore', invalid='ignore'):
        inv = np.where(E > 0, 1/E, 0.0)
    return E.mean(), inv.mean()
print("R1 (Bloch, L = 257): excess over E0 per site = (1/2)<|eps|> - (m^2/2)<1/|eps|> = <sum 4cos^2 k/(2|eps|)> (kinetic share):")
exc_bz = {}
for m in [0.0, 0.3, 1.0, 2.0]:
    e, ci = bz(257, m)
    exc_bz[m] = 0.5*e - 0.5*m**2*ci
    print("   m=%.1f: E0/N = %+.6f ; pinched = %+.6f ; excess = %+.6f" % (m, -0.5*e, -0.5*m**2*ci, exc_bz[m]))

MP = 1.22089e19                                   # GeV (RECALLED)
rhoL = 0.685*0.674**2*8.0992e-47                  # GeV^4 (RECALLED Planck 2018)
print("R3. Sizes with a = l_P (OPEN bridge; RECALLED inputs):")
print("   fully recorded vacuum, (S) weight = %.3f M_P^4 = %.2e GeV^4 = %.2e rho_Lambda per staggered field (m -> 0)"
      % (exc_bz[0.0], exc_bz[0.0]*MP**4, exc_bz[0.0]*MP**4/rhoL))
print("   one record in the vacuum: Delta E_1 ~ 2.4 hbar c/a = %.2e GeV per record (energy injected; generic, not (S)-specific)" % (2.4*MP))
print("   records-as-dark-energy (if rho_rec = n_rec eps_rec = rho_Lambda with eps_rec = 2.4 M_P): n_rec = %.2e GeV^3 = %.2e per m^3"
      % (rhoL/(2.4*MP), rhoL/(2.4*MP)/(1.97327e-16)**3))

print("R4. Permanent-record component under (S), constant formation rate per physical volume, LCDM background (Om = 0.31):")
Om, Ol = 0.31, 0.69
def Hof(a): return np.sqrt(Om*a**-3 + Ol)
def rhs(lna, y):                 # d rho/d ln a = Q/H - 3 rho, Q = 1 (units)
    a = np.exp(lna); return [1.0/Hof(a) - 3*y[0]]
s = solve_ivp(rhs, (np.log(1e-3), np.log(4.0)), [0.0], dense_output=True, rtol=1e-10, atol=1e-14)
for z in [3.0, 1.0, 0.5, 0.0, -0.5, -0.75]:
    lna = np.log(1/(1+z)); r = s.sol(lna)[0]; a = np.exp(lna)
    w = -1 - (1/Hof(a) - 3*r)/(3*r)
    print("   z = %+.2f: w_eff = %+.4f  (a^3 rho non-decreasing => w <= 0; here w <= -1: phantom-like, never crosses)" % (z, w))
