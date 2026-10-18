"""NT-3 validation V1-V3 (PREREG.md 'Validation')."""
import numpy as np, itertools, sys
import scipy.sparse as sp, scipy.sparse.linalg as sla
from ed_core import Model, ring, lowest
from analyze import analyze, summarize
from filters import ring_fvals, NORM1D

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

P("filter norms (sqrt<f^2>):", {k: round(v, 6) for k, v in NORM1D.items()})

# ---------- V1: on-site control, light included ----------
for L in (3, 4, 5):
    m = Model(ring(L), ring_fvals("C0", L), include_light=True)
    r = analyze(m, near_light=(1, L - 1)); r["Vs"] = L
    summarize(r, f"V1 C0 L={L}", P)
    ok = abs(r["E0"] + L) < 1e-9 and r["D"] == 1 and abs(r["gap"] - 1) < 1e-9
    P(f"V1 L={L}: E0=-L, D=1, gap=1 -> {'PASS' if ok else 'FAIL'};  expected chi6/site=12, S6(q=0)=3")

# ---------- V2: F_star with light mode included, L = 4 ----------
L = 4
mA = Model(ring(L), ring_fvals("F_star", L), include_light=False)
mB = Model(ring(L), ring_fvals("F_star", L), include_light=True)
rA = analyze(mA, near_light=(1, 3), want_chi=False); rA["Vs"] = L
rB = analyze(mB, near_light=(1, 3), want_chi=False); rB["Vs"] = L
zero_rows = [(r[1], r[2]) for r in rB["table"] if abs(r[0]) < 1e-8]
P(f"V2 L=4: E0 mirror-only = {rA['E0']:.12f}, E0 with light = {rB['E0']:.12f}")
P(f"V2 zero-gap rows with light (expect (0,0,0,0) lvl1, (1,0,0,0), (1,1,0,0), (1,1,1,0) at K0 = 0): {zero_rows}")
P(f"V2 first nonzero gap: mirror-only {rA['gap']:.10f}, with light {rB['gap']:.10f}")
okV2 = abs(rA["E0"] - rB["E0"]) < 1e-10 and abs(rA["gap"] - rB["gap"]) < 1e-9 and len(zero_rows) == 4
P("V2:", "PASS" if okV2 else "FAIL")

# ---------- V3: independent real-space Jordan-Wigner builder ----------
def jw_ops(nm):
    I = sp.identity(2, format="csr"); Z = sp.diags([1.0, -1.0]).tocsr()
    a = sp.csr_matrix(np.array([[0.0, 1.0], [0.0, 0.0]]))  # annihilates |1> -> |0> (basis |0>,|1>)
    ops = []
    for p in range(nm):
        mats = [Z] * p + [a] + [I] * (nm - p - 1)
        o = mats[0]
        for mm in mats[1:]:
            o = sp.kron(o, mm, format="csr")
        ops.append(o)
    return ops

def realspace_H(L, name):
    fv = ring_fvals(name, L)
    phi = np.array([sum(fv[m] * np.cos(2 * np.pi * m * r / L) for m in range(L)) / L for r in range(L)])
    nm = 4 * L
    c = jw_ops(nm)                       # mode (a, x) -> a*L + x
    cS = [[sum(phi[(x - y) % L] * c[a * L + y] for y in range(L) if abs(phi[(x - y) % L]) > 1e-14)
           for x in range(L)] for a in range(4)]
    H = None
    for x in range(L):
        t = cS[0][x] @ cS[1][x] @ cS[2][x] @ cS[3][x]
        t = -(t + t.T.conj())
        H = t if H is None else H + t
    return H.tocsr()

def momentum_full_H(L, name):
    m = Model(ring(L), ring_fvals(name, L), include_light=True)
    basis = np.arange(1 << (4 * L), dtype=np.int64)
    return m.build_H(basis)

for L, name in ((3, "F_star"), (3, "F_hi"), (3, "F_lo"), (4, "F_star")):
    Hr = realspace_H(L, name); Hm = momentum_full_H(L, name)
    if Hr.shape[0] <= 4096:
        er = np.linalg.eigvalsh(Hr.toarray()); em = np.linalg.eigvalsh(Hm.toarray())
        diff = np.abs(er - em).max()
        P(f"V3 {name} L={L}: full spectra (dim {Hr.shape[0]}) max |diff| = {diff:.2e}; E0 = {er[0]:.10f} vs {em[0]:.10f}")
    else:
        er = np.sort(sla.eigsh(Hr, k=8, which="SA", tol=1e-12)[0]); em = np.sort(sla.eigsh(Hm, k=8, which="SA", tol=1e-12)[0])
        diff = np.abs(er - em).max()
        P(f"V3 {name} L={L}: lowest 8 (dim {Hr.shape[0]}) max |diff| = {diff:.2e}; real {np.round(er,8).tolist()} mom {np.round(em,8).tolist()}")
    P("V3:", "PASS" if diff < 1e-9 else "FAIL")

open(__file__.replace(".py", ".out"), "w").write("\n".join(out) + "\n")
