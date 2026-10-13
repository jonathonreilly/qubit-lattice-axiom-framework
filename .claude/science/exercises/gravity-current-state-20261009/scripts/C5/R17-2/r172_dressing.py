"""C5 R17-2: (A) Lemma W's generator W is the linearized-ADM Dirac dressing plus the comoving TT cloud;
(B) T3's equations say {W, H0} = -H_int weakly, so e^{-W} maps the (beta) H to H0 + constraint-prop. terms;
(C) kernel of the weak boost operator L at omega != 0, omega = 0, and |omega| -> |q| (Jacobi lemma input);
(D) boost factorisation K_b^sing = delta_b * Xi_K (b-independent).
Uses R16-12's solver verbatim (r1612_lib.py = r1612_degree3.py up to its main block; sublum_copy.py = R14-1 sublum.py).
Conventions as R16-12: W = -i sum (E.Xi_E + h.Xi_h) f, {h,E} = 1, s_ij = q_i q_j - |q|^2 delta_ij, f-dot = -i omega f."""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r1612_lib as L

out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
rng = np.random.default_rng(17200)
KS = [np.array([2.0, 0.3, 0.2]), np.array([2.6, 0.1, -0.4]), np.array([1.6, 1.6, 0.0]), np.array([2.3, -1.9, 0.7])]
I3 = np.eye(3)

def mat(cvec, bas):
    return sum(cvec[i] * bas[i] for i in range(6))

pr("C5 R17-2 r172_dressing.py; m =", L.M)
pr("\n(A) dressing identity. For each defect mode and random qhat (|q| = 1e-3), Xi = Phi_c/delta_c from R16-12's T3 solve.")
pr("    A1 Hamiltonian: {C_s^(1)[N], W} = i N s.Xi_E f  ->  need s.Xi_E = -i eps  (so the bracket is N eps f = T00[N])")
pr("    A2 momentum:    {C_j^(1)[xi], W} = -2 xi.(q.Xi_h) f -> need q.Xi_h = P/2 = eps v/2 (bracket = P^m[xi], sign as A1)")
pr("    A3 TT cloud: the GR comoving field of the W1 stress at frequency omega=q.v solves hdot=2E, Edot=-(q^2/2)h - sigma0 f:")
pr("       h_TT = 2 sigma0_TT f/(omega^2-q^2), E_TT = -i omega sigma0_TT f/(omega^2-q^2). Dressing shifts: dh = -i Xi_E f, dE = +i Xi_h f.")
pr("       Report ratios dh_T/h^GR_T, dh_TT/h^GR_TT, dE_TT/E^GR_TT (GR Newtonian h^GR_T: s.h = eps f -> coeff on (I-qq) = -eps/(2q^2)).")
for law in ("S(1.4)", "G(1.4)"):
    for k in KS:
        eps, v, P, Delta = L.matter(law, k)
        cs = [c for c in range(3) if abs(Delta[c, c]) > 1e-8]
        if not cs:
            continue
        mA1 = mA2 = 0.0; rat = []
        for _ in range(100):
            qh = rng.normal(size=3); qh /= np.linalg.norm(qh); q = 1e-3 * qh
            for c in cs:
                Bt, At, res, om, dl, bT, Km, Gm, bas = L.solve_translation(q, eps, v, Delta, c)
                if abs(dl) < 1e-12:
                    continue
                XE, Xh = Bt / dl, At / dl
                s = L.smat(q)
                mA1 = max(mA1, abs(np.sum(s * XE) - (-1j * eps)) / eps)
                mA2 = max(mA2, np.linalg.norm(Xh @ q - 0.5 * P) / np.linalg.norm(P))
                # A3 ratios
                Pp = I3 - np.outer(qh, qh)
                coefT = np.sum(XE * Pp) / 2.0              # coefficient of Xi_E on (I - qq)
                dhT = -1j * coefT; hGR_T = -eps / (2 * (q @ q))
                sig = 0.5 * eps * np.outer(v, v); sc = L.comps(sig, bas)
                XEc, Xhc = L.comps(XE, bas), L.comps(Xh, bas)
                q2 = q @ q
                for i in L.TT_IDX:
                    if abs(sc[i]) < 1e-9:
                        continue
                    hGR = 2 * sc[i] / (om ** 2 - q2); EGR = -1j * om * sc[i] / (om ** 2 - q2)
                    rat.append((dhT / hGR_T, (-1j * XEc[i]) / hGR, (1j * Xhc[i]) / EGR))
        rat = np.array(rat)
        pr(f"  {law} k={np.round(k,2)} |v|={np.linalg.norm(v):.4f}: A1 max rel err {mA1:.1e}; A2 max rel err {mA2:.1e};"
           f" A3 ratios (Newton, h_TT, E_TT): max|r+1| = {np.max(np.abs(rat+1)):.1e} over {len(rat)} samples")

pr("\n(B) T3 equations = dressing equations: {W, H0} = -i[E.(-i om Xi_E + G Xi_h) + h.(-i om Xi_h - K Xi_E)] f.")
pr("    Claim: E-part has only L components (qq, vL) and h-part equals -sigma0 f up to T component (transverse trace).")
pr("    => e^{-W}: H = H0 + h.sigma0 f  ->  H0 + {E_L, h_T}-proportional terms (weakly H0). Show components:")
for law in ("S(1.4)", "G(1.4)"):
    k = KS[1]; eps, v, P, Delta = L.matter(law, k)
    c = int(np.argmax(np.abs(np.diag(Delta))))
    worst_nonconstraint = 0.0; worst_constraint = 0.0
    for _ in range(200):
        qh = rng.normal(size=3); qh /= np.linalg.norm(qh); q = 1.0 * qh
        Bt, At, res, om, dl, bT, Km, Gm, bas = L.solve_translation(q, eps, v, Delta, c)
        XEc, Xhc = L.comps(Bt / dl, bas), L.comps(At / dl, bas)
        sc = L.comps(0.5 * eps * np.outer(v, v), bas)
        Ecoef = -1j * (-1j * om * XEc + Gm @ Xhc)
        hcoef = -1j * (-1j * om * Xhc - Km @ XEc) + sc        # should vanish except T component
        nonc = max(np.max(np.abs(Ecoef[[3, 4, 5]])), np.max(np.abs(hcoef[[0, 1, 2, 4, 5]])))
        cons = max(np.max(np.abs(Ecoef[[0, 1, 2]])), abs(hcoef[3]))
        worst_nonconstraint = max(worst_nonconstraint, nonc / max(np.max(np.abs(sc)), 1e-300))
        worst_constraint = max(worst_constraint, cons / max(np.max(np.abs(sc)), 1e-300))
    pr(f"  {law} k={k} c={c}: max non-constraint residual of {{W,H0}}+h.sigma0 f: {worst_nonconstraint:.1e};"
       f" max constraint-proportional (E_L, h_T) part: {worst_constraint:.2e} (nonzero: the weak residual)")
pr("  Constraint-proportional coefficients near qhat.v -> 0 (|q| = 1), G(1.4) k=(2.6,0.1,-0.4):")
eps, v, P, Delta = L.matter("G(1.4)", KS[1]); c = 0
vh = v / np.linalg.norm(v); w = Delta[c] - vh * (vh @ Delta[c]); w /= np.linalg.norm(w)
for dth in (1e-1, 1e-2, 1e-3, 1e-4):
    qh = np.cos(dth) * w + np.sin(dth) * vh; q = qh
    Bt, At, res, om, dl, bT, Km, Gm, bas = L.solve_translation(q, eps, v, Delta, c)
    XEc, Xhc = L.comps(Bt / dl, bas), L.comps(At / dl, bas)
    Ecoef = -1j * (-1j * om * XEc + Gm @ Xhc); sc = L.comps(0.5 * eps * np.outer(v, v), bas)
    hcoef = -1j * (-1j * om * Xhc - Km @ XEc) + sc
    pr(f"    qhat.v = {om:.1e}: |E_L coeff| = {np.max(np.abs(Ecoef[[0,1,2]])):.3e}, |h_T coeff| = {abs(hcoef[3]):.3e}"
       f"  (Xi_T = {abs(XEc[3]):.3e}, bounded: Xi is regular in qhat; the weak residual is bounded too)")

pr("\n(C) kernel of the weak boost operator L(X,Y) = (-i om X + G Y on T,TT ; -i om Y - K X on qq,vL,TT), unknowns X(6),Y(6)")
def Lop(q, om):
    qh = q / np.linalg.norm(q); bas = L.basis(qh)
    Gm = np.array([[np.sum(bi * L.Gop(bj)) for bj in bas] for bi in bas])
    Km = np.array([[np.sum(bi * L.Kop(bj, q)) for bj in bas] for bi in bas])
    rows = []
    for i in L.T_IDX + L.TT_IDX:
        r = np.zeros(12, complex); r[i] += -1j * om; r[6:] += Gm[i]; rows.append(r)
    for i in L.L_IDX + L.TT_IDX:
        r = np.zeros(12, complex); r[6 + i] += -1j * om; r[:6] += -Km[i]; rows.append(r)
    return np.array(rows)
names = ["X_qq", "X_vL1", "X_vL2", "X_T", "X_TT1", "X_TT2", "Y_qq", "Y_vL1", "Y_vL2", "Y_T", "Y_TT1", "Y_TT2"]
qh = rng.normal(size=3); qh /= np.linalg.norm(qh); q = qh
for om in (0.37, 1e-6, 0.0, 0.999999, 1.0):
    A = Lop(q, om); u, sv, vt = np.linalg.svd(A)
    tol = 1e-9 * sv[0]; rank = int(np.sum(sv > tol)); ns = vt[rank:].conj().T
    # which components appear in the null space
    weight = np.sum(np.abs(ns) ** 2, axis=1)
    comp = [names[i] for i in range(12) if weight[i] > 1e-12]
    pr(f"  omega = {om:<9}: rank {rank}, null dim {12-rank}; null directions involve: {comp}; smallest kept sv {sv[rank-1]:.1e}")
pr("  (X_qq, X_vL multiply E_L, Y_T multiplies h_T: constraint-proportional = weakly zero.)")

pr("\n(D) boost factorisation: the forced helicity-0 boost pieces (X_T, Y_qq) / delta_b are b-independent")
for law in ("S(1.4)", "G(1.4)"):
    k = KS[3] if law == "G(1.4)" else KS[2]; eps, v, P, Delta = L.matter(law, k)
    bs = [b for b in range(3) if abs(Delta[b, b]) > 1e-8]
    if len(bs) < 2:
        pr(f"  {law} k={k}: fewer than two defect directions ({bs}); skipped"); continue
    qh = rng.normal(size=3); qh /= np.linalg.norm(qh); q = qh
    vals = []
    for b in bs:
        Bt, At, res, om, dl, bT, Km, Gm, bas = L.solve_translation(q, eps, v, Delta, b)
        XT = 2j * bT / om; YQ = bT
        vals.append((XT / dl, YQ / dl))
    vals = np.array(vals)
    pr(f"  {law} k={k}: defect directions b = {bs}; spread of X_T/delta_b {np.ptp(np.abs(vals[:,0])):.1e},"
       f" of Y_qq/delta_b {np.ptp(np.abs(vals[:,1])):.1e}; X_T/delta_b vs -eps/(|q|^2 omega): "
       f"{abs(vals[0,0] - (-eps/((q@q)*om)))/abs(vals[0,0]):.1e}")

with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")
