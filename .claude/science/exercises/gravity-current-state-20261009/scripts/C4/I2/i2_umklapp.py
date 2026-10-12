"""Lane RI / probe I2 (iii): interband scattering at the truncation edge, contact interaction.  Units a = 1, c = 1.

(A) Folded fine lattice (N-site cells of a fine NN Klein-Gordon lattice, d = 2), contact interaction on fine sites
    (lambda phi^4).  Tower momentum K = k + 2 pi n is conserved mod 2 pi N (the fine reciprocal lattice); a
    'tower umklapp' is a collision with K1 + K2 - K3 - K4 = 2 pi N G != 0.  On-shell 2 -> 2 weight split
    into normal / umklapp, binned in the incoming total energy E (units of the fine bandwidth E_max ~ 2 sqrt(2) N).
    Also the thermal umklapp fraction Gamma_U / Gamma at temperature T (Boltzmann incoming pairs).
(B) Vacuum-loop (zone-averaged) umklapp fraction of a contact vertex: fraction of momentum-conserving
    4-tuples that need a fine reciprocal vector; flat measure and basketball weight 1/(w1 w2 w3 w4); d = 1, 2, 3.
(C) Generic N-band cells without an internal Z_N (fine-translation) label: perturb the N-site cell by random
    on-site energies of relative size delta; the contact vertex on cell sites then couples LOW tower bands with
    a coarse reciprocal vector mismatch (tower umklapp at energies ~ pi/a, far below the truncation edge).
"""
import numpy as np
out = []
def P(s=""):
    print(s, flush=True); out.append(s)
rng = np.random.default_rng(7)
m = 1.0

def w_fine(K, N):  # K array (..., d)
    return np.sqrt(m**2 + np.sum(4 * N**2 * np.sin(K / (2 * N))**2, axis=-1))

# ---------------------------------------------------------------- (A)
P("=== (A) on-shell 2->2 umklapp fraction vs incoming energy, folded fine lattice d = 2 ===")
def reduce(K, N):
    return (K + np.pi * N) % (2 * np.pi * N) - np.pi * N
def onshell_split(N, npairs=3000, G3=96, eta=0.02):
    Emax = w_fine(np.array([np.pi * N, np.pi * N]), N)
    g = (np.arange(G3) + 0.5) / G3 * 2 * np.pi * N - np.pi * N
    K3 = np.stack(np.meshgrid(g, g, indexing='ij'), -1).reshape(-1, 2)
    w3 = w_fine(K3, N)
    K1 = rng.uniform(-np.pi * N, np.pi * N, (npairs, 2)); K2 = rng.uniform(-np.pi * N, np.pi * N, (npairs, 2))
    Ein = w_fine(K1, N) + w_fine(K2, N)
    res = []
    for i in range(npairs):
        Ptot = K1[i] + K2[i]
        K4raw = Ptot[None, :] - K3
        K4 = reduce(K4raw, N)
        um = np.any(np.abs(K4raw - K4) > 1e-9, axis=1)
        mism = Ein[i] - w3 - w_fine(K4, N)
        wt = np.exp(-0.5 * (mism / (eta * Emax))**2)
        res.append((Ein[i] / Emax, wt[~um].sum(), wt[um].sum()))
    return np.array(res), Emax
bins = np.linspace(0, 2, 11)
for N in (4, 8, 16):
    r, Emax = onshell_split(N)
    line = []
    for b0, b1 in zip(bins[:-1], bins[1:]):
        s = (r[:, 0] >= b0) & (r[:, 0] < b1)
        if s.sum() < 5:
            line.append("   -  "); continue
        line.append(f"{r[s, 2].sum() / (r[s, 1].sum() + r[s, 2].sum()):.3f} ")
    P(f"N={N:2d} (E_max={Emax:6.1f}): umklapp fraction in E_in/E_max bins of 0.2: " + " ".join(line))
P("-> the curves coincide in E/E_max (E_max ~ 2 sqrt(2) N): tower umklapp switches on at a fixed fraction of the")
P("   truncation-edge energy and is O(1) above it, for every N.")

P("\n   thermal umklapp fraction Gamma_U/Gamma (Boltzmann incoming pairs, same on-shell weights), T in coarse units")
for N in (4, 8, 16):
    r, Emax = onshell_split(N, npairs=3000)
    row = []
    for T in (2.0, 4.0, 8.0, 16.0, 32.0):
        bw = np.exp(-(r[:, 0] * Emax) / T)
        U = np.sum(bw * r[:, 2]); Nn = np.sum(bw * r[:, 1])
        row.append(f"T={T:4.0f}: {U / (U + Nn):.2e}")
    P(f"N={N:2d}: " + "  ".join(row))
P("-> at fixed T the umklapp fraction falls like exp(-E_th/T) with E_th proportional to N; at T ~ N it is O(1).")

# ---------------------------------------------------------------- (B)
P("\n=== (B) vacuum-loop umklapp fraction of a contact vertex (zone-averaged, all bands) ===")
for d in (1, 2, 3):
    for N in (4, 16, 64):
        S = 400000
        K = rng.uniform(-np.pi * N, np.pi * N, (S, 3, d))
        K4raw = -K.sum(axis=1)
        um = np.any(np.abs(K4raw) > np.pi * N, axis=1)
        wts = 1.0 / (w_fine(K, N).prod(axis=1) * w_fine(reduce(K4raw, N), N))
        P(f"d={d} N={N:3d}: flat fraction {um.mean():.4f}   basketball-weighted fraction {wts[um].sum() / wts.sum():.4f}")
P("   exact flat values: d=1: 1/3, d=2: 5/9, d=3: 19/27 = 0.7037 (sum of three uniforms leaves the zone)")
P("-> N-independent: in loops, most of the contact-vertex phase space is tower umklapp, for every N.")

# ---------------------------------------------------------------- (C)
P("\n=== (C) N-band cells without an internal Z_N label: low-band tower umklapp from a cell-site contact vertex ===")
def cell_W(k, N, eps):
    W = np.zeros((N, N), complex)
    for j in range(N):
        W[j, j] = m**2 + 2 * N**2 * (1 + eps[j])
    for j in range(N - 1):
        W[j, j + 1] = W[j + 1, j] = -N**2
    W[N - 1, 0] += -N**2 * np.exp(1j * k); W[0, N - 1] += -N**2 * np.exp(-1j * k)
    return W
def modes(k, N, eps):
    lam, v = np.linalg.eigh(cell_W(k, N, eps))
    return lam, v
P("  process: bands (0,0) -> (1,0) at coarse momenta k1 + k2 = k3 + k4 (tower mismatch 2 pi: a LOW-energy tower umklapp)")
P("  ratio = |V_umklapp| / |V_normal (0,0)->(0,0)|, vertex V = sum_j psi1 psi2 conj(psi3 psi4) over cell sites")
for N in (4, 8, 16):
    row = []
    for delta in (0.0, 1e-3, 1e-2, 1e-1):
        rats = []
        for trial in range(20):
            eps = delta * rng.normal(size=N)
            k1, k2 = rng.uniform(-1, 1, 2); k3 = rng.uniform(-1, 1); k4 = k1 + k2 - k3
            _, v1 = modes(k1, N, eps); _, v2 = modes(k2, N, eps); _, v3 = modes(k3, N, eps); _, v4 = modes(k4, N, eps)
            # band 1 at small k: tower K = k +- 2 pi; take the lower of the two n = +-1 bands (index 1)
            Vu = np.sum(v1[:, 0] * v2[:, 0] * np.conj(v3[:, 1] * v4[:, 0]))
            Vn = np.sum(v1[:, 0] * v2[:, 0] * np.conj(v3[:, 0] * v4[:, 0]))
            rats.append(abs(Vu) / abs(Vn))
        row.append(f"delta={delta:.0e}: {np.median(rats):.2e}")
    P(f"N={N:2d}: " + "  ".join(row))
P("-> with the exact Z_N (fine translation) the low-band tower umklapp vertex vanishes (machine zero); any breaking")
P("   of it switches on tower umklapp among the LOWEST bands, linearly in the breaking.  Tower-normal contact")
P("   interactions among N bands require the internal Z_N label, i.e. the network to be a fine lattice of spacing a/N.")
open('i2_umklapp.out', 'w').write('\n'.join(out) + '\n')
