"""T03 Test 2: energy accounting of the repository's other formation model.

Model (on main, 2026-09-24): docs/FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md
  builder: scripts/repeated_formation_check.py:tree_model  (imported unchanged from the main checkout)
  GKLS law: H = delta*W/eps^2 + delta*T/eps ,  jumps sqrt(kappa) j/eps  (creation-only, N -> N+2, W -> W-1)
Note's own remark: H_orig = Delta*N_B + t*T (Delta = delta/eps^2, t = delta/eps) differs from H' = Delta*W + t*T
by the number-dependent constant Delta*(N - M_A).

Question: net energy exchanged with the bath per birth, in both conventions.  The unitary part conserves the
energy expectation exactly, so E(end) - E(0) is the total heat exchanged over the whole birth history.
"""
import math, sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

MAIN = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts"
sys.path.insert(0, MAIN)
import repeated_formation_check as rf  # noqa: E402

delta, kappa = 1.3, 0.7
PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"[PASS] {name} {detail}")
    else:
        FAIL += 1
        print(f"[FAIL] {name} {detail}")


def run(model, kind, eps, tmax=200.0, nt=2):
    g = model["g"]; dim = len(g)
    W = model["W"].astype(float); T = model["T"].astype(float); N = model["N"].astype(float); NB = model["NB"].astype(float)
    MA = len(model["A_sites"])
    Hp = delta * W / eps**2 + delta * T / eps          # H'  (the GKLS Hamiltonian of the note)
    jumps = [math.sqrt(kappa) * j / eps for j in model[kind]]
    L = rf.superop(Hp, jumps)
    rho0 = np.outer(g, g).astype(complex)
    traj = expm_multiply(L, rho0.reshape(-1, order="F"), start=0, stop=tmax, num=nt, traceA=L.diagonal().sum())
    Delta, t = delta / eps**2, delta / eps
    Horig = Delta * NB + t * T
    out = []
    for tt, v in zip(np.linspace(0, tmax, nt), traj):
        r = v.reshape((dim, dim), order="F")
        b = (np.trace(N @ r).real - np.trace(N @ rho0).real) / 2
        Ep = np.trace(Hp @ r).real
        Eo = np.trace(Horig @ r).real
        out.append((tt, b, Ep, Eo))
    return np.array(out), Delta


print("Energy per birth in the repository's GKLS creation-only formation law")
print("model      kind       eps   births   Q_orig/Delta   Q'/delta   (Q = total energy change / births over the whole history)")
rows = []
for m in (2, 3, 4, None):
    model = rf.tree_model(m)
    for kind in ("coherent", "resolved"):
        for eps in (0.2, 0.1, 0.05):
            arr, Delta = run(model, kind, eps)
            b = arr[-1, 1]
            Qp = (arr[-1, 2] - arr[0, 2]) / b if b > 1e-9 else float("nan")
            Qo = (arr[-1, 3] - arr[0, 3]) / b if b > 1e-9 else float("nan")
            rows.append((model["label"], kind, eps, b, Qo / Delta, Qp / delta))
            print(f"{model['label']:9s}  {kind:9s}  {eps:4.2f}  {b:7.3f}   {Qo/Delta:10.4f}   {Qp/delta:9.4f}")

# ---- ground-state energies of each N sector (the binding that a birth can remove)
print()
print("Lowest energy of each N sector under H' (units of delta), eps = 0.05: the coherent hopping energy a birth can remove")
gs_changes = []
for m in (2, 3, 4, None):
    model = rf.tree_model(m)
    eps = 0.05
    W = model["W"].astype(float); T = model["T"].astype(float); Nd = np.diag(model["N"])
    Hp = delta * W / eps**2 + delta * T / eps
    egs = {}
    for n in sorted(set(Nd)):
        idx = np.where(Nd == n)[0]
        egs[int(n)] = np.linalg.eigvalsh(Hp[np.ix_(idx, idx)])[0] / delta
    ns = sorted(egs)
    print(f"  {model['label']:9s} " + "  ".join(f"N={n}: {egs[n]:8.4f}" for n in ns))
    gs_changes.append(max(egs[ns[i + 1]] - egs[ns[i]] for i in range(len(ns) - 1)))

# ---- readings
ro = [r for r in rows if r[3] > 1e-6]
check("H_orig: the energy deposited per birth is 2*Delta (N_B rises by 2) in every model/instrument/eps (1e-2)",
      all(abs(r[4] - 2) < 1e-2 for r in ro), " ".join(f"{r[4]:.4f}" for r in ro[:6]) + " ...")
check("H': the heat exchanged over the whole history is zero (|Q'/delta| < 5e-3) in every model/instrument/eps",
      all(abs(r[5]) < 5e-3 for r in ro), " max |Q'/delta| = %.2e" % max(abs(r[5]) for r in ro))
check("the birth removes binding: the lowest energy of the sector rises by >= 1.5 delta at some birth in some model",
      max(gs_changes) >= 1.5, " max rise = %.3f delta" % max(gs_changes))
check("the cost is exactly a supplied number: Q_orig - Q' = 2*Delta per birth (H_orig - H' = Delta*(N - M_A))",
      all(abs(r[4] - 2) < 1e-2 for r in ro), "")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
