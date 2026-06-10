#!/usr/bin/env python3
"""Final confirmations:
 1. Does the draft's OWN initial state (seed 20260610, its psi0) have full-rank cross
    blocks (explaining why its runner never hits nan)?
 2. WHY are the Fermi-sea cross blocks rank-deficient -- is it a structural/symmetry zero
    (real Slater => the site0->site1 coherence block degenerate)?
 3. Is the positive-spread claim robust on states that DO have full-rank blocks (so the
    only defect is the degeneracy, not the spread)?
 4. Is the draft's polar() guarded anywhere? (re-read the exact line.)
"""
from __future__ import annotations
import numpy as np
from scipy.linalg import expm
from numpy.linalg import svd, matrix_rank

L, NM = 3, 9
SZ = np.array([[1, 0], [0, -1]], float); SM = np.array([[0, 1], [0, 0]], float); I2 = np.eye(2)
def ann(j, n):
    mats = [SZ]*j + [SM] + [I2]*(n-j-1)
    out = np.array([[1.0]])
    for m in mats: out = np.kron(out, m)
    return out
A = [ann(j, NM) for j in range(NM)]; AD = [a.T for a in A]
NDAGN = [[(AD[i] @ A[j]).astype(complex) for j in range(NM)] for i in range(NM)]
hmat = np.zeros((NM, NM))
for x in range(L):
    for c in range(3):
        a_, b_ = 3*x+c, 3*((x+1)%L)+c
        hmat[a_, b_] = hmat[b_, a_] = -1.0
H = sum(hmat[i, j]*NDAGN[i][j] for i in range(NM) for j in range(NM))
U_step = expm(-1j*H*0.35)
def Gof(psi):
    return np.array([[psi.conj() @ NDAGN[i][j] @ psi for j in range(NM)] for i in range(NM)])
def cross(psi): return Gof(psi)[0:3, 3:6]

# ---- reproduce the DRAFT's exact psi0 (seed 20260610, its construction) ----
rng = np.random.default_rng(20260610)
Kpart = 5
PSI = np.linalg.qr(rng.normal(size=(NM, Kpart)) + 1j*rng.normal(size=(NM, Kpart)))[0]
vac = np.zeros(2**NM)
vac[int(np.argmin(np.diag(sum(AD[m] @ A[m] for m in range(NM)).real)))] = 1.0
psi0 = vac.astype(complex)
for k in range(Kpart):
    psi0 = sum(PSI[m, k]*AD[m].astype(complex) for m in range(NM)) @ psi0
psi0 /= np.linalg.norm(psi0)

def KB_pair(eps):
    Nop = sum(AD[c] @ A[c] for c in range(3))
    w, V = np.linalg.eigh(Nop)
    Nt = (w-w.mean())/max(abs(w-w.mean()))
    Kp = (V @ np.diag(np.sqrt((1+eps*Nt)/2)) @ V.T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1-eps*Nt)/2)) @ V.T).astype(complex)
    return Kp, Km
KB = KB_pair(0.6)

print("=== 1. Draft's own psi0: cross-block rank along its depth-5 tree ===")
branches = [(1.0, psi0)]
mins = []; ranks = []
for n in range(5):
    new = []
    for (wt, ps) in branches:
        ps_f = U_step @ ps
        for Kop in KB:
            phi = Kop @ ps_f
            p = float(np.real(phi.conj() @ phi))
            if p < 1e-14: continue
            phi = phi/np.sqrt(p)
            s = svd(cross(phi), compute_uv=False)
            mins.append(s.min()); ranks.append(matrix_rank(cross(phi), tol=1e-9))
            new.append((wt*p, phi))
    branches = new
print(f"  draft psi0: min cross-block sv = {min(mins):.4e}, min rank = {min(ranks)} (full=3) "
      f"-> {'FULL RANK (never hits the degeneracy)' if min(ranks)==3 else 'DEGENERATE'}")
print(f"  Is draft psi0 a real vector? max|Im(psi0)| = {np.max(np.abs(psi0.imag)):.3e} "
      f"(complex => generic, avoids the real-Slater degeneracy)")

print("\n=== 2. Fermi sea is REAL => structural zero in the site0->site1 coherence block ===")
ew, evec = np.linalg.eigh(hmat)
def fermi_sea(nfill):
    vac2 = np.zeros(2**NM, complex)
    vac2[int(np.argmin(np.diag(sum(AD[m] @ A[m] for m in range(NM)).real)))] = 1.0
    psi = vac2
    for k in range(nfill): psi = sum(evec[m, k]*AD[m].astype(complex) for m in range(NM)) @ psi
    return psi/np.linalg.norm(psi)
for nf in [1, 2, 5]:
    psi = fermi_sea(nf)
    cb = cross(psi)
    s = svd(cb, compute_uv=False)
    print(f"  fermi_sea({nf}): cross-block singular values = {s}, "
          f"max|Im(psi)|={np.max(np.abs(psi.imag)):.2e}")

print("\n=== 3. Positive spread on a FULL-RANK near-sea-ish state (isolate degeneracy) ===")
# fermi_sea3 and fermi_sea4 had FULL rank cross blocks. Confirm spread there is well-defined
# and positive with scipy polar (the only honest polar there).
from scipy.linalg import polar as sp_polar
def polar_scipy(M):
    U, _ = sp_polar(M, side='right'); return U
def tree_inc(psi0, polar):
    branches = [(1.0, psi0, [])]
    for n in range(5):
        new = []
        for (wt, ps, hist) in branches:
            ps_f = U_step @ ps
            for Kop in KB:
                phi = Kop @ ps_f
                p = float(np.real(phi.conj() @ phi))
                if p < 1e-14: continue
                phi = phi/np.sqrt(p)
                new.append((wt*p, phi, hist+[polar(cross(phi))]))
        branches = new
    incs = [(wt, h[-1] @ h[-2].conj().T) for (wt, _, h) in branches]
    Z = sum(wt for wt, _ in incs)
    Em = sum(wt*d for wt, d in incs)/Z
    var = float(sum(wt*np.linalg.norm(d-Em)**2 for wt, d in incs)/Z)
    return var, Em
for nf in [3, 4]:
    v, Em = tree_inc(fermi_sea(nf), polar_scipy)
    print(f"  fermi_sea({nf}) [FULL RANK]: spread = {v:.5f} (well-defined, positive)")

print("\n=== 4. The draft polar line (verbatim from the runner) ===")
print("    def polar_u(M):")
print("        w, V = np.linalg.eigh(M.conj().T @ M)")
print("        return M @ V @ np.diag(w ** -0.5) @ V.conj().T   # <-- w**-0.5, NO guard")
print("  -> on a zero eigenvalue this is 0**-0.5 = inf; the note's increment, spread,")
print("     covariance ALL inherit this on rank-deficient branches (the Fermi sea).")
