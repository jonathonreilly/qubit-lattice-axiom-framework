"""T03 Test 1: the cost horn on the Heisenberg 2x2x2 cube (8 qubits, exact diagonalisation).

Pre-registered in PREREGISTRATION.md.  J = 1, H = J sum_<xy> sigma_x . sigma_y (sigma Pauli).
Sharp lock of site x: antipodal menu along z, Kraus K_a = P_a, a = up/down, Phi*(A) = sum_a P_a A P_a.
"""
import itertools, math, random, sys
import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=150)
J = 1.0
NS = 8
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def op(single, site):
    mats = [I2] * NS
    mats[site] = single
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


SX = [op(X, i) for i in range(NS)]
SY = [op(Y, i) for i in range(NS)]
SZ = [op(Z, i) for i in range(NS)]
bonds = [(a, a ^ b) for a in range(NS) for b in (1, 2, 4) if a < (a ^ b)]
assert len(bonds) == 12


def bond(a, b):
    return J * (SX[a] @ SX[b] + SY[a] @ SY[b] + SZ[a] @ SZ[b])


Hb = {e: bond(*e) for e in bonds}
H = sum(Hb.values())
w, V = np.linalg.eigh(H)
E0 = w[0]
gap = w[1] - w[0]
g = V[:, 0]
print(f"E0 = {E0:.9f} J, gap = {gap:.9f} J, ground degenerate? {abs(w[1]-w[0])<1e-9}")

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"[PASS] {name} {detail}")
    else:
        FAIL += 1
        print(f"[FAIL] {name} {detail}")


x = 0
Pup = [(np.eye(2**NS) + SZ[s]) / 2 for s in range(NS)]
Pdn = [(np.eye(2**NS) - SZ[s]) / 2 for s in range(NS)]
hx = sum(Hb[e] for e in bonds if x in e)

# ---------------------------------------------------------------- 1a
rho = np.outer(g, g.conj())
# (i) state update (Kraus), Hamiltonian unchanged
rho_up = Pup[x] @ rho @ Pup[x] + Pdn[x] @ rho @ Pdn[x]
cost_update = np.trace(rho_up @ H).real - np.trace(rho @ H).real
# (ii) route-two algebra refinement: state untouched, H -> block-diagonal part
H_ref = Pup[x] @ H @ Pup[x] + Pdn[x] @ H @ Pdn[x]
cost_refine = (g.conj() @ H_ref @ g).real - (g.conj() @ H @ g).real
# (iii) adiabatic cut of the site's bonds (H without the bonds at x, new ground state)
H_cut = H - hx
E_cut = np.linalg.eigvalsh(H_cut)[0]
cost_cut = E_cut - E0
# (iv) classical (diagonal-in-lock-basis) bonds: Ising zz bonds, state = its own ground manifold member
Hz = sum(J * SZ[a] @ SZ[b] for (a, b) in bonds)
wz, Vz = np.linalg.eigh(Hz)
gz = Vz[:, 0]
rz = np.outer(gz, gz.conj())
rz_up = Pup[x] @ rz @ Pup[x] + Pdn[x] @ rz @ Pdn[x]
cost_classical = np.trace(rz_up @ Hz).real - np.trace(rz @ Hz).real
print(f"1a update = {cost_update:.9f}  refinement = {cost_refine:.9f}  adiabatic cut = {cost_cut:.9f}  classical bonds = {cost_classical:.2e}")
check("1a T3 value reproduced (3.213393 J)", abs(cost_update - 3.213393) < 2e-6)
check("1a refinement == update (no escape)", abs(cost_update - cost_refine) < 1e-10)
check("1a refinement is NOT < 10% of update", cost_refine > 0.1 * cost_update)
check("1a adiabatic cut costs at least as much as the sudden update", cost_cut >= cost_update - 1e-9, f"({cost_cut:.4f} >= {cost_update:.4f})")
check("1a classical (diagonal) bonds: cost exactly 0", abs(cost_classical) < 1e-10)
# rank-one check: T2 floor
p_up = (g.conj() @ Pup[x] @ g).real
floor = gap * (2 * p_up * (1 - p_up))
check("1a T2 floor (gap * sum_a (p_a - p_a^2)) holds", cost_update >= floor - 1e-9, f"({cost_update:.4f} >= {floor:.4f})")

# ---------------------------------------------------------------- 1b, 1c
Ediag = np.real(np.sum(np.abs(g) ** 2 * np.real(np.diag(H))))
total_theory = Ediag - E0
print(f"diag-ensemble energy = {Ediag:.9f} = E0/3 ? {abs(Ediag-E0/3)<1e-9};  total classicalisation cost (2/3)|E0| = {total_theory:.9f}")

nbrs = {s: [t for (a, b) in bonds for t in ((b,) if a == s else (a,) if b == s else ())] for s in range(NS)}
Hdiag = np.real(np.diag(H))


def sequential_total(order):
    """Exact mean of E(final) - E0 for locking sites in `order`, common z basis, Born branches.
    Also returns dict k -> (sum of cost*prob, sum of prob) with k = # already locked neighbours."""
    stats = {}
    def rec(psi, prob, depth, locked, Ecur):
        if depth == NS:
            return prob * (psi.conj() @ H @ psi).real
        s = order[depth]
        tot = 0.0
        k = sum(1 for t in nbrs[s] if t in locked)
        for P in (Pup[s], Pdn[s]):
            phi = P @ psi
            pr = float(np.vdot(phi, phi).real)
            if pr < 1e-14:
                continue
            phi = phi / math.sqrt(pr)
            Enew = (phi.conj() @ H @ phi).real
            tot += rec(phi, prob * pr, depth + 1, locked | {s}, Enew)
            # per-step cost, averaged later
            st = stats.setdefault(k, [0.0, 0.0])
            st[0] += prob * pr * (Enew - Ecur)
            st[1] += prob * pr
        return tot
    Efin = rec(g.astype(complex), 1.0, 0, frozenset(), E0)
    return Efin - E0, stats


random.seed(7)
orders = [list(range(NS))] + [random.sample(range(NS), NS) for _ in range(5)]
totals = []
agg = {}
for od in orders:
    t, st = sequential_total(od)
    totals.append(t)
    for k, (c, p) in st.items():
        a = agg.setdefault(k, [0.0, 0.0])
        a[0] += c
        a[1] += p
print("1b total mean cost per order:", np.array(totals))
check("1b every order gives (2/3)|E0| (order independent)", max(abs(np.array(totals) - total_theory)) < 1e-8)
check("1b no order gives < 90% of the others", min(totals) > 0.9 * max(totals))
print("1c mean cost of the next lock given k already-locked neighbours (averaged over orders and Born branches):")
prev = None
mono = True
for k in sorted(agg):
    c = agg[k][0] / agg[k][1]
    print(f"   k = {k}:  mean cost {c:.6f} J   (weight {agg[k][1]:.1f})")
    if prev is not None and c > prev + 1e-9:
        mono = False
    prev = c
check("1c cost per lock is non-increasing in the number of already-locked neighbours", mono)
# neighbours of a corner site: 3.  Site with all neighbours locked should cost less than the isolated first lock.
c0 = agg[0][0] / agg[0][1]
ckmax = agg[max(agg)][0] / agg[max(agg)][1]
check("1c a lock with all neighbours locked costs < 15% of a first lock", ckmax < 0.15 * c0, f"({ckmax:.4f} vs {c0:.4f})")

# ---------------------------------------------------------------- 1d
def phi_dephase(r):
    return Pup[x] @ r @ Pup[x] + Pdn[x] @ r @ Pdn[x]


def entropy(r):
    ev = np.linalg.eigvalsh((r + r.conj().T) / 2)
    ev = ev[ev > 1e-15]
    return float(-(ev * np.log(ev)).sum())


def gibbs(beta):
    e = np.exp(-beta * (w - w[0]))
    return (V * e) @ V.conj().T / e.sum()


d = 2**NS
Hoff = H - (Pup[x] @ H @ Pup[x] + Pdn[x] @ H @ Pdn[x])
slope = float(np.trace(Hoff @ Hoff).real / d)
print("1d Gibbs states of the cube, lock at site 0 along z:")
neg = False
bound_ok = True
rows = []
for beta in (0.0, 0.05, 0.2, 1.0, 5.0, 20.0):
    r = gibbs(beta)
    c = (np.trace(phi_dephase(r) @ H) - np.trace(r @ H)).real
    dS = entropy(phi_dephase(r)) - entropy(r)
    lb = (dS / beta) if beta > 0 else 0.0
    if c < -1e-10:
        neg = True
    if beta > 0 and c < lb - 1e-9:
        bound_ok = False
    rows.append((beta, c, lb))
    print(f"   beta = {beta:5.2f}: cost = {c:.6f} J,  T*dS lower bound = {lb:.6f},  small-beta slope prediction = {slope*beta:.6f}")
check("1d cost >= 0 for every Gibbs state (passivity)", not neg)
check("1d cost >= T*dS for every Gibbs state", bound_ok)
check("1d small-beta law cost ~ beta*||H-Phi*(H)||^2/dim (beta=0.05, 5%)", abs(rows[1][1] - slope * 0.05) < 0.05 * slope * 0.05 + 1e-6)
check("1d beta -> infinity reproduces the ground-state cost", abs(rows[-1][1] - cost_update) < 5e-3)
check("1d infinite temperature costs exactly 0", abs(rows[0][1]) < 1e-12)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
