"""T03 kill check: mean energy input of a white-noise collapse (CSL-type) on a free-fermion lattice.

Pre-registered in PREREGISTRATION_kill.md (K1, K2).

Model: 1D ring of N sites, two modes per site, walker H(k) = -t sin k sigma_x + m sigma_z (t = 1, antiperiodic
boundaries).  Vacuum = all negative-energy states filled.  Collapse Lindbladian (mean dynamics of CSL-type noise):
    d rho/dt = gamma * sum_x ( L_x rho L_x - 1/2 {L_x^2, rho} ),   L_x = sum_z g_x(z) n_z  (Hermitian, one-body)
For Hermitian one-body L the map O_M = c^dag M c obeys [L,[L,O_M]] = O_{[A,[A,M]]}, so the one-body matrix closes:
    d Gamma/dt = -i[h,Gamma] - (gamma/2) sum_x [A_x,[A_x,Gamma]],  E = Tr(h Gamma),
    dE/dt|_diss = -(gamma/2) sum_x Tr([A_x,[A_x,h]] Gamma).
Checks:
  0. independent many-body check (4 sites, 8 modes, exact Lindblad on the 256-dim Fock space) of the one-body formula.
  1. K1: site-occupation coupling A_x = G_x (x) 1: rate and its rho^-3 scaling; bond-energy formula.
  2. K2: band-projected coupling A_x = P+ G_x P+ - P- G_x P-: vacuum rate ~ 0; one upper-band particle at k0 heats at
     (1/2) eps''(k0) * sum_x g'(x)^2   (nonrelativistic GRW/CSL value).
"""
import itertools
import numpy as np

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}", flush=True)


def walker_h(N, t=1.0, m=0.0):
    """One-body matrix on modes index = 2*x + s.  Antiperiodic ring."""
    h = np.zeros((2 * N, 2 * N), complex)
    sx = np.array([[0, 1], [1, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    for x in range(N):
        y = (x + 1) % N
        sign = -1.0 if y == 0 else 1.0     # antiperiodic
        # (t/2i) (psi_{x+1}^dag sx psi_x - psi_x^dag sx psi_{x+1})
        blk = sign * (t / 2j) * sx
        h[2 * y:2 * y + 2, 2 * x:2 * x + 2] += blk
        h[2 * x:2 * x + 2, 2 * y:2 * y + 2] += blk.conj().T
        h[2 * x:2 * x + 2, 2 * x:2 * x + 2] += m * sz
    assert np.allclose(h, h.conj().T)
    return h


def kernel(N, x, rho):
    d = np.array([min((z - x) % N, (x - z) % N) for z in range(N)], float)
    return np.exp(-d ** 2 / (2 * rho ** 2)) / (np.sqrt(2 * np.pi) * rho)     # normalised, sum ~ 1


def G_op(N, x, rho):
    return np.kron(np.diag(kernel(N, x, rho)), np.eye(2))


def dcomm(A, h):
    return A @ A @ h - 2 * A @ h @ A + h @ A @ A


def rate(N, h, Gamma, ops):
    return -0.5 * sum(np.trace(dcomm(A, h) @ Gamma) for A in ops).real


# ------------------------------------------------------------------ 0. many-body cross-check
def jw_ops(nm):
    I = np.eye(2); Zm = np.diag([1., -1.]); a = np.array([[0, 1], [0, 0]], float)
    ops = []
    for j in range(nm):
        mats = [Zm] * j + [a] + [I] * (nm - j - 1)
        o = mats[0]
        for mm in mats[1:]:
            o = np.kron(o, mm)
        ops.append(o)
    return ops


def many_body_check():
    N, rho = 4, 0.9
    nm = 2 * N
    h = walker_h(N, 1.0, 0.3)
    c = jw_ops(nm)
    H = sum(h[i, j] * c[i].T @ c[j] for i in range(nm) for j in range(nm))
    ncount = [c[i].T @ c[i] for i in range(nm)]
    w, V = np.linalg.eigh(h)
    occ = V[:, w < 0]
    Gamma = occ @ occ.conj().T
    # many-body vacuum: Slater determinant of occ
    dimF = 2 ** nm
    # build via applying creation operators to Fock vacuum
    vac = np.zeros(dimF, complex); vac[0] = 1.0
    psi = vac
    for k in range(occ.shape[1]):
        cd = sum(occ[i, k] * c[i].T for i in range(nm))
        psi = cd @ psi
    psi /= np.linalg.norm(psi)
    Em = (psi.conj() @ H @ psi).real
    E1 = np.trace(h @ Gamma).real
    check("0a Slater determinant energy matches Tr(h Gamma)", abs(Em - E1) < 1e-9, f"({Em:.8f} vs {E1:.8f})")
    rho0 = np.outer(psi, psi.conj())
    dE = 0.0
    for x in range(N):
        g = kernel(N, x, rho)
        L = sum(g[z] * (ncount[2 * z] + ncount[2 * z + 1]) for z in range(N))
        Lrho = L @ rho0 @ L - 0.5 * (L @ L @ rho0 + rho0 @ L @ L)
        dE += np.trace(H @ Lrho).real
    ops = [G_op(N, x, rho) for x in range(N)]
    dE1 = -0.5 * sum(np.trace(dcomm(A, h) @ Gamma) for A in ops).real
    check("0b many-body Lindblad dE/dt (gamma=1) equals the one-body double-commutator formula",
          abs(dE - dE1) < 1e-9 * max(1, abs(dE)), f"({dE:.8f} vs {dE1:.8f})")
    check("0c the collapse heats the vacuum (dE/dt > 0)", dE > 1e-6)


many_body_check()

# ------------------------------------------------------------------ 1. site-occupation coupling: vacuum heating
N = 160
t = 1.0
print(f"\n1D ring N={N}, t=1, massless walker sea (half filled).  Rate is dE/dt per unit gamma, normalised kernel.")
h0 = walker_h(N, t, 0.0)
w, V = np.linalg.eigh(h0)
occ = V[:, w < 0]
Gam0 = occ @ occ.conj().T
E0 = np.trace(h0 @ Gam0).real
print(f"vacuum energy per site = {E0 / N:.6f}  (analytic -2/pi = {-2 / np.pi:.6f}: two modes per site)")
check("1a vacuum energy per site is -2t/pi", abs(E0 / N + 2 / np.pi) < 1e-3)

rows = []
for rho in (2.0, 3.0, 4.0, 6.0, 8.0):
    ops = [G_op(N, x, rho) for x in range(N)]
    R = rate(N, h0, Gam0, ops)
    # bond-energy prediction: (1/2) * sum_bonds |<h_b>| * sum_x (g_x(b1) - g_x(b2))^2
    hb_total = -E0                                  # sum of |bond energies| (all of H is hopping when m=0)
    dsum = 0.0
    g = kernel(N, 0, rho)
    dsum = sum((g[z] - g[(z + 1) % N]) ** 2 for z in range(N)) * N   # x runs over N sites; translation invariant
    pred = 0.5 * (hb_total / N) * dsum
    rows.append((rho, R, pred))
    print(f"   rho = {rho:4.1f}: rate = {R:.6e}   bond-energy formula = {pred:.6e}   rate*rho^3 = {R * rho ** 3:.5f}")
check("1b rate matches the bond-energy formula (1/2) sum_b |<h_b>| sum_x (dg)^2 within 25 % at every rho",
      all(abs(R / p - 1) < 0.25 for _, R, p in rows), "(bond expectations are uniform on a translation-invariant sea; hop is not diagonal in bond, formula is leading order in 1/rho)")
rr = [R * rho ** 3 for rho, R, _ in rows if rho >= 4]
check("1c rate * rho^3 constant to 5 % for rho >= 4 (1D: integral g'^2 ~ rho^-3)", max(rr) / min(rr) < 1.05, f"({rr})")
check("1d heating is non-zero and does not vanish for a vacuum", all(R > 1e-6 for _, R, _ in rows))

# ------------------------------------------------------------------ 2. band-projected coupling
print("\nBand-projected (excitation-number) coupling on the same sea")
Pm = occ @ occ.conj().T
Pp = np.eye(2 * N) - Pm
rho = 4.0
opsP = [Pp @ G_op(N, x, rho) @ Pp - Pm @ G_op(N, x, rho) @ Pm for x in range(N)]
Rvac_proj = rate(N, h0, Gam0, opsP)
Rvac_site = rate(N, h0, Gam0, [G_op(N, x, rho) for x in range(N)])
print(f"   vacuum: site coupling {Rvac_site:.6e}   band-projected {Rvac_proj:.3e}")
check("2a filled-band vacuum: projected coupling heats < 1e-10 of the site coupling", abs(Rvac_proj) < 1e-10 * Rvac_site)

# massive walker, one upper-band particle near k=0; scan mass and kernel width
def particle_vs_vacuum(m, rho):
    hm = walker_h(N, t, m)
    wm, Vm = np.linalg.eigh(hm)
    occm = Vm[:, wm < 0]
    Pm2 = occm @ occm.conj().T
    Pp2 = np.eye(2 * N) - Pm2
    k_idx = np.where(wm > 0)[0][0]
    k0 = np.pi / N
    psi_p = Vm[:, k_idx:k_idx + 1]
    Gam_p = Pm2 + psi_p @ psi_p.conj().T
    Gs = [G_op(N, x, rho) for x in range(N)]
    opsP2 = [Pp2 @ G @ Pp2 - Pm2 @ G @ Pm2 for G in Gs]
    Rvac_proj2 = rate(N, hm, Pm2, opsP2)
    R_particle = rate(N, hm, Gam_p, opsP2) - Rvac_proj2
    Rvac_site2 = rate(N, hm, Pm2, Gs)
    g = kernel(N, 0, rho)
    gp2 = sum(((g[(z + 1) % N] - g[(z - 1) % N]) / 2) ** 2 for z in range(N))     # sum over centres at fixed z (no factor N)
    eps = lambda k: np.sqrt(t * t * np.sin(k) ** 2 + m * m)
    dk = 1e-4
    eps2 = (eps(k0 + dk) - 2 * eps(k0) + eps(k0 - dk)) / dk ** 2
    return Rvac_proj2, R_particle, 0.5 * eps2 * gp2, Rvac_site2 / N


print("\nmass and width scan: projected vacuum rate, one-particle rate vs NR prediction, site-coupled vacuum rate per site")
ok_vac = True
ratios = {}
for m in (0.5, 1.0, 2.0):
    for rho in (6.0, 10.0):
        rv, rp, pr, rs = particle_vs_vacuum(m, rho)
        ratios[(m, rho)] = rp / pr
        ok_vac &= abs(rv) < 1e-12
        print(f"   m={m:3.1f} rho={rho:4.1f}: proj vacuum {rv: .2e}  particle {rp:.4e}  NR pred {pr:.4e}  ratio {rp / pr:.3f}   site-coupled vacuum per site {rs:.4e}")
check("2b projected coupling: filled-band vacuum heating is zero to 1e-12 for every mass and width", ok_vac)
check("2c one upper-band particle heats at the NR value (1/2) eps'' * integral g'^2 within 10 % once rho >= 10 (q << m)",
      all(abs(ratios[(m, 10.0)] - 1) < 0.10 for m in (0.5, 1.0, 2.0)), f"({[round(ratios[(m,10.0)],3) for m in (0.5,1.0,2.0)]})")
vs = [particle_vs_vacuum(m, 10.0)[3] for m in (0.5, 1.0, 2.0)]
pp = [particle_vs_vacuum(m, 10.0)[1] * m for m in (0.5, 1.0, 2.0)]
print(f"   site-coupled vacuum per site for m=0.5,1,2: {vs};  particle rate x m: {pp}")
check("2d the particle bill scales as 1/m (rate*m constant within 10 %) while the site-coupled vacuum bill per site does not fall with m the same way",
      max(pp) / min(pp) < 1.10 and max(vs) / min(vs) < 3.0)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
