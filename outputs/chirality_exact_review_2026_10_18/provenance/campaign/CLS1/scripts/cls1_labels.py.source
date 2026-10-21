"""CLS-1 step 1: (i) BCC label classification by brute force; symmetry audit of the class-S perturbations
(cubic covariance, Theta parity); real-space vs folded implementation cross-check (L = 4, 6)."""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from cls1_core import *
def P(*a): print(*a); sys.stdout.flush()
rng = np.random.default_rng(20261015)

P("=== (i) BCC labels, brute force ===")
corners = list(itertools.product((0, 1), repeat=3))
# residual translations: n in Z^3 (scan mod 4) with exp(i K.n) = 1 for all three K
res = [n for n in itertools.product(range(4), repeat=3)
       if all(abs(np.exp(1j * np.dot(K, n)) - 1) < 1e-12 for K in KS)]
res_mod2 = sorted(set(tuple(x % 2 for x in n) for n in res))
P(f"residual translations (mod 4 scan): {len(res)} of 64; residues mod 2: {res_mod2}  -> BCC (n_x=n_y=n_z mod 2)")
assert res_mod2 == [(0, 0, 0), (1, 1, 1)]
labels = {}
for v in corners:
    Q = PI * np.array(v)
    lab = tuple(int(round(np.real(np.exp(1j * np.dot(Q, n))))) for n in res)
    chi = int(round(np.prod(np.cos(Q))))                    # node chirality = det of velocity matrix diag(cos Q_a)
    V = np.array([[np.real(np.trace(SIG[a] @ (walker(Q + 1e-6 * np.eye(3)[b]) - walker(Q - 1e-6 * np.eye(3)[b])) / 2e-6) / 2)
                   for b in range(3)] for a in range(3)])
    chi_num = int(np.sign(np.linalg.det(V)))
    assert chi == chi_num
    labels.setdefault(lab, []).append((v, chi))
for lab, lst in labels.items():
    chis = [c for _, c in lst]
    par = 'even' if int(round(np.prod(np.cos(PI*np.array(lst[0][0])))))*0 + (-1)**sum(lst[0][0]) == 1 else 'odd '
    P(f"label {par} (character of T_(1,1,1) = {(-1)**sum(lst[0][0]):+d}): corners "
      + ", ".join(f"{v}(hw{sum(v)},{'R' if c>0 else 'L'})" for v, c in lst)
      + f"  | chiralities {sorted(set(chis))}  index (sum chi) = {sum(chis):+d} per Spin(10) component")
P(f"number of BCC label sectors = {len(labels)}; every sector single-chirality: {all(len(set(c for _, c in l))==1 for l in labels.values())}")
P("T_d = translation by (1,1,1) is in BCC; its character on corner v is (-1)^hw(v) = node chirality (checked):",
  all(int(round(np.real(np.exp(1j*np.dot(PI*np.array(v),(1,1,1)))))) == int(round(np.prod(np.cos(PI*np.array(v))))) for v in corners))
# exact-unit-translation control: 8 distinct labels
lab_unit = set(tuple(int(round(np.real(np.exp(1j*np.dot(PI*np.array(v), e))))) for e in np.eye(3, dtype=int)) for v in corners)
P(f"control (exact unit translations): {len(lab_unit)} distinct labels (X2-L1)")
# which corner pairs does each K connect
P("corner pairs connected by each K (hopping psi_c^dag psi_c' S_K and Yukawa psi_c psi_c' H0 S_K carry the same charge):")
for m, K in enumerate(KS):
    prs = sorted(set(tuple(sorted((v, tuple(int(round(((PI*np.array(v)+K)/PI)[a]))%2 for a in range(3))))) for v in corners))
    P(f"  K_{'xyz'[m]}={tuple(int(x/PI) for x in K)}pi: " + "; ".join(f"{a}(hw{sum(a)})<->{b}(hw{sum(b)})" for a, b in prs))

P("\n=== symmetry audit of class-S perturbations (folded Bloch form) ===")
ROT = rotations(); assert len(ROT) == 24
def perm_of(R):
    return [gindex(R @ G) for G in GS]
def cubic_defect(Hfun, nk=6):
    worst = 0.0
    for _ in range(nk):
        k = rng.uniform(-PI, PI, 3)
        H0 = Hfun(k)
        n = H0.shape[0] // 2
        for R in ROT:
            u = spin_lift(R)
            pm = perm_of(R)
            HR = Hfun(R @ k)
            # build permutation+spin operator on folded space (blocks of 2 per component)
            nb = n // 1
            Uop = np.zeros_like(H0)
            nblk = H0.shape[0] // 2
            for b in range(nblk):
                grp, i = divmod(b, 4)           # grp 0 = psi, 1 = chi
                tb = grp * 4 + pm[i]
                Uop[2*tb:2*tb+2, 2*b:2*b+2] = u
            worst = max(worst, np.abs(Uop @ H0 @ Uop.conj().T - HR).max())
    return worst
def theta_defect(Hfun, nk=6):
    worst = 0.0
    for _ in range(nk):
        k = rng.uniform(-PI, PI, 3)
        H = Hfun(k); Hm = Hfun(-k)
        n = H.shape[0]
        M = np.diag([1.0] * 8 + [-1.0] * (n - 8)) if n > 8 else np.eye(8)
        worst = max(worst, np.abs(Hm + M @ H @ M).max())
    return worst
cases = {
    "walker only": lambda k: h_psi(k),
    "P-a density (eps=0.3)": lambda k: h_psi(k, eps_a=0.3),
    "P-b spin density (eps=0.3)": lambda k: h_psi(k, eps_b=0.3),
    "P-c modulated walker hop (eta=0.3)": lambda k: h_psi(k, eta=0.3),
    "model A, Delta=1, kappa=0": lambda k: H_modelA(k, 1.0),
    "model A, Delta=1, P-d kappa=0.3": lambda k: H_modelA(k, 1.0, 0.3),
}
for name, Hf in cases.items():
    P(f"  {name:40s} cubic-covariance defect {cubic_defect(Hf):.2e}   Theta defect |h(-k)+M h(k) M| {theta_defect(Hf):.2e}"
      f"  -> {'Theta-even (allowed)' if theta_defect(Hf) < 1e-12 else 'Theta-odd (forbidden by Theta)'}")

P("\n=== real-space vs folded cross-check (model A + P-a + P-b + P-c + P-d), and real-space Theta check ===")
def realspace_H(L, Delta, kappa, eps_a, eps_b, eta, amps=(1, 1, 1)):
    N = L ** 3
    idx = lambda x: ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
    Hpp = np.zeros((2 * N, 2 * N), complex); Bcp = np.zeros((2 * N, 2 * N), complex)
    for x in itertools.product(range(L), repeat=3):
        i = idx(x); xa = np.array(x)
        cK = [np.cos(np.dot(K, xa)) for K in KS]
        onsite = sum(amps[m] * cK[m] * (eps_a * s0 + eps_b * SIG[m]) for m in range(3))
        Hpp[2*i:2*i+2, 2*i:2*i+2] += onsite
        for b in range(3):
            y = xa.copy(); y[b] += 1; j = idx(y)
            A = (1 + eta * amps[b] * cK[b]) * 1j * SIG[b] / 2       # walker + P-c on b-bonds (K_b.b = 0 so cK[b] bond-symmetric)
            Hpp[2*j:2*j+2, 2*i:2*i+2] += A
            Hpp[2*i:2*i+2, 2*j:2*j+2] += A.conj().T
        # filter: psi_S(x) = 1/2 psi(x) - 1/4 sum_b [psi(x+b)+psi(x-b)] + kappa sum_K amp cos(K.x) psi(x)
        Bcp[2*i:2*i+2, 2*i:2*i+2] += Delta * (0.5 + kappa * sum(amps[m] * cK[m] for m in range(3))) * s0
        for b in range(3):
            for sgn in (1, -1):
                y = xa.copy(); y[b] += sgn; j = idx(y)
                Bcp[2*i:2*i+2, 2*j:2*j+2] += Delta * (-0.25) * s0
    Z = np.zeros_like(Hpp)
    return np.block([[Hpp, Bcp.conj().T], [Bcp, Z]]), idx
pars = dict(Delta=0.8, kappa=0.21, eps_a=0.13, eps_b=0.07, eta=0.17, amps=(1.0, 0.7, 0.4))
for L in (4, 6):
    Hrs, idx = realspace_H(L, **pars)
    erw = np.linalg.eigvalsh(Hrs)
    # folded: reduced momenta = torus momenta modulo {G}
    reps = []
    for n in itertools.product(range(L), repeat=3):
        k = 2 * PI * np.array(n) / L
        if not any(gindex(k - r) >= 0 for r in reps):
            reps.append(k)
    ef = np.sort(np.concatenate([np.linalg.eigvalsh(H_modelA(k, pars['Delta'], pars['kappa'], eps_a=pars['eps_a'],
                 eps_b=pars['eps_b'], eta=pars['eta'], amps=pars['amps'])) for k in reps]))
    P(f"  L={L}: {len(reps)} reduced momenta, dim {Hrs.shape[0]}; max |spectrum(real) - spectrum(folded)| = {np.abs(np.sort(erw) - ef).max():.2e}")
    # Theta in real space: U h U = -h, U = (inversion x->-x) x diag(+1 psi, -1 chi); check per term family
    N = L ** 3
    Pm = np.zeros((N, N))
    for x in itertools.product(range(L), repeat=3):
        Pm[idx(tuple(-np.array(x))), idx(x)] = 1
    U = np.kron(np.diag([1., -1.]), np.kron(Pm, np.eye(2)))
    for lab, pp in [("walker+partner (kappa=0)", dict(Delta=0.8, kappa=0, eps_a=0, eps_b=0, eta=0)),
                    ("+P-c eta", dict(Delta=0.8, kappa=0, eps_a=0, eps_b=0, eta=0.17)),
                    ("+P-d kappa", dict(Delta=0.8, kappa=0.21, eps_a=0, eps_b=0, eta=0)),
                    ("+P-a eps_a", dict(Delta=0.8, kappa=0, eps_a=0.13, eps_b=0, eta=0)),
                    ("+P-b eps_b", dict(Delta=0.8, kappa=0, eps_a=0, eps_b=0.07, eta=0))]:
        Hx, _ = realspace_H(L, amps=(1.0, 0.7, 0.4), **pp)
        P(f"     real-space Theta defect |U h U + h| for {lab:26s}: {np.abs(U @ Hx @ U + Hx).max():.2e}")
    if L == 6: break
