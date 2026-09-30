#!/usr/bin/env python3
"""T28 Tests B and C (see PREREG.md).

B: Where does the 09-02 note's member g'=1 of H_g = g'^2 H_E + g'^-2 H_B sit on the Euclidean beta axis
   under the standard weak-coupling Kogut-Susskind dictionary?  (H_E = -Laplacian in half-trace metric,
   H_B = sum_p (1 - Re Tr U_p / N).)
C: Staggered-fermion induced plaquette coefficient: check tr D^4 has -8 Re Tr U_p per plaquette.
"""
import numpy as np, itertools
from scipy.linalg import expm

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ---------------- Test B ----------------
P("=== Test B: operator-family member g'=1 versus Euclidean beta (weak-coupling dictionary) ===")
# Gell-Mann-type generator with Tr(T_a T_b) = delta/2 : T_3
def su_n_T3(N):
    t = np.zeros((N, N), complex)
    t[0, 0] = 0.5; t[1, 1] = -0.5
    return t
for N in (2, 3, 4):
    T = su_n_T3(N)
    assert abs(np.trace(T @ T) - 0.5) < 1e-14
    # H_B small-x coefficient:  1 - Re Tr exp(i x T)/N  ->  x^2/(4N)
    x = 1e-3
    hb = 1 - np.real(np.trace(expm(1j * x * T))) / N
    P(f"N={N}: (1 - ReTr U/N)/x^2 at x=1e-3 = {hb/x**2:.8f}   expected 1/(4N) = {1/(4*N):.8f}")
P("Harmonic limit: H = e*sum p^2 + (m/(4N)) sum (curl x)^2  =>  omega^2 = 4 e (m/(4N)) k^2  =>  c^2 = e*m/N.")
P("So the light-cone condition is e*m = N, not e*m = 1 (the 09-02 note's 'coefficient product = 1' is a normalisation of the operators, not c=1).")
P("Kogut-Susskind: H = (g^2/2) sum E^2 + (1/g^2) sum_p Tr(2 - U_p - U_p^dag) = (g^2/2) H_E + (2N/g^2) H_B  (H_B with 1/N).")
for N in (2, 3):
    g2 = np.sqrt(4 * N)     # solve (g^2/2)/(2N/g^2) = g^4/(4N) = 1  -> equal coefficients
    P(f"N={N}: e*m = (g^2/2)(2N/g^2) = {N} = N  -> c=1 for every g (KS).  Equal-coefficient point: g^4 = 4N -> g^2 = {g2:.5f}, beta = 2N/g^2 = {2*N/g2:.5f} = sqrt(N) = {np.sqrt(N):.5f}")
P("Member g'=1 of the note's family (e = g'^2, m = g'^-2 up to a common clock factor) <-> KS g^4 = 4N.  => beta_eq = sqrt(N) (1.73 for SU(3)), not 2N (6).")
P("READING B: FAIL for 'g=1 of H_g is the beta=6 point'; the equal-coefficient point is a normalisation artefact (factor 2, factor N).")

# ---------------- Test C ----------------
P("\n=== Test C: staggered hopping tr D^4 on 4^4 periodic lattice, SU(2) links ===")
L = 4
dims = (L, L, L, L)
sites = list(itertools.product(range(L), repeat=4))
idx = {s: i for i, s in enumerate(sites)}
Nc = 2
rng = np.random.default_rng(12345)

def rand_su2():
    a = rng.normal(size=4); a /= np.linalg.norm(a)
    return np.array([[a[0] + 1j * a[3], a[2] + 1j * a[1]], [-a[2] + 1j * a[1], a[0] - 1j * a[3]]])

def shift(s, mu, d):
    t = list(s); t[mu] = (t[mu] + d) % L; return tuple(t)

def eta(s, mu):
    return (-1) ** sum(s[:mu])

def build(links):
    n = len(sites) * Nc
    D = np.zeros((n, n), complex)
    for s in sites:
        i = idx[s]
        for mu in range(4):
            j = idx[shift(s, mu, 1)]
            D[i*Nc:(i+1)*Nc, j*Nc:(j+1)*Nc] += eta(s, mu) * links[(s, mu)]
            k = idx[shift(s, mu, -1)]
            D[i*Nc:(i+1)*Nc, k*Nc:(k+1)*Nc] -= eta(s, mu) * links[(shift(s, mu, -1), mu)].conj().T
    return D

def plaq_sum(links):
    tot = 0.0
    for s in sites:
        for mu in range(4):
            for nu in range(mu + 1, 4):
                Up = links[(s, mu)] @ links[(shift(s, mu, 1), nu)] @ links[(shift(s, nu, 1), mu)].conj().T @ links[(s, nu)].conj().T
                tot += np.real(np.trace(Up))
    return tot

def poly_sum(links):
    tot = 0.0
    for s0 in sites:
        for mu in range(4):
            M = np.eye(Nc, dtype=complex); pos = s0
            for _ in range(L):
                M = M @ links[(pos, mu)]; pos = shift(pos, mu, 1)
            tot += np.real(np.trace(M))
    return tot

xs, ys, zs = [], [], []
for trial in range(10):
    if trial == 0:
        links = {(s, mu): np.eye(Nc, dtype=complex) for s in sites for mu in range(4)}
    else:
        links = {(s, mu): rand_su2() for s in sites for mu in range(4)}
    D = build(links)
    D2 = D @ D
    t4 = np.real(np.trace(D2 @ D2))
    xs.append(plaq_sum(links)); zs.append(poly_sum(links)); ys.append(t4)
xs, ys, zs = np.array(xs), np.array(ys), np.array(zs)
A = np.vstack([xs, zs, np.ones_like(xs)]).T
coef, res, *_ = np.linalg.lstsq(A, ys, rcond=None)
P(f"fit tr D^4 = a * sum_p Re Tr U_p + c * sum_lines Re Tr(Polyakov) + b :  a = {coef[0]:.9f} (expected -8),  c = {coef[1]:.5f},  b = {coef[2]:.4f},  max residual = {np.max(np.abs(A@coef-ys)):.2e}")
# implied coupling
P("ln det(1 + kappa D) contains  -(kappa^4/4) tr D^4  =  +2 kappa^4 sum_p Re Tr U_p ;  with rooting N_f/4 per 4-taste det:")
P("   exp[(beta_ind/N) Re Tr U_p]  with  beta_ind = N * N_f * kappa^4 / 2 ,  kappa = 1/(2m):  beta_ind = N N_f /(32 m^4)")
for Nc_, nf in ((3, 1), (3, 6)):
    m4 = Nc_ * nf / (32 * 6.0)
    m = m4 ** 0.25
    P(f"   N={Nc_}, N_f={nf}: beta_ind = 6 needs m = {m:.4f} (kappa = {1/(2*m):.3f}); hopping expansion needs kappa < ~1/8 (m > ~4).")
for m in (4.0, 8.0):
    P(f"   at m = {m}: beta_ind(N=3,N_f=1) = {3/(32*m**4):.3e}")

open("testBC_output.txt", "w").write("\n".join(out) + "\n")
