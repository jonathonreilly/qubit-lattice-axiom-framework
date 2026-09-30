"""T46 P3: robustness of the P1/P2 readings + scale-sensitivity of the mixed-scale ratio."""
import numpy as np
from qcdrun import QCD
import t46_p2_sm_rge as P2

V_ATLAS = 0.103303816122/np.sqrt(6)
R_PRED = V_ATLAS**(6/5)
q = QCD()
MB = 4.18
print("== Scale sensitivity of the MIXED ratio m_s(mu_s)/m_b(m_b) ==")
print("   mu_s[GeV]  R_mixed    R_pred/R_mixed-1")
for mus in (1.0, 1.5, 1.8, 1.9, 2.0, 2.1, 2.2, 2.5, 3.0, 4.18):
    ms = q.mass(0.0934, 2.0, mus)
    R = ms/MB
    print(f"   {mus:7.2f}   {R:.6f}   {100*(R_PRED/R-1):+8.2f}%")
d = (np.log(q.mass(0.0934, 2.0, 2.1)) - np.log(q.mass(0.0934, 2.0, 1.9)))/np.log(2.1/1.9)
print(f" dln m_s/dln mu at 2 GeV = {d:.4f}  ->  1% in R  <->  {100*0.01/abs(d):.1f}% in mu_s")

print("\n== Exponent needed / V_cb needed on the common surface ==")
R0 = q.mass(0.0934, 2.0, 4.18)/MB
Rm = 0.018854  # nf=5 region value used in P2
for R in (R0, Rm):
    print(f" R={R:.6f}:  V_cb for exact 5/6: {R**(5/6):.5f} ({100*(R**(5/6)/V_ATLAS-1):+.1f}% vs atlas);"
          f"  R for exact 5/6 from atlas V: {R_PRED:.6f} ({100*(R_PRED/R-1):+.1f}% vs R)")

print("\n== SM-RGE robustness (p at m_t and at M_Pl) ==")
print(" case                                 p(m_t)   p(v)    p(1e10)  p(M_Pl)   R(M_Pl)/R(m_t)  V(M_Pl)/V(m_t)")
def line(label, **kw):
    mu, yt, R, V, p = P2.curve(**kw)
    i10 = np.argmin(np.abs(np.log(mu/1e10))); iv = np.argmin(np.abs(np.log(mu/246.22)))
    print(f" {label:36s} {p[0]:.4f}  {p[iv]:.4f}  {p[i10]:.4f}  {p[-1]:.4f}   {R[-1]/R[0]:.4f}        {V[-1]/V[0]:.4f}   ymax_t(MPl)={yt[-1]:.3f}")
    return p
line("baseline (1-loop, V_cb=0.0422)")
line("V_cb(low)=0.0408", Vcb0=0.0408)
line("V_cb(low)=0.0391 (exclusive-like)", Vcb0=0.0391)
line("V_cb(low)=0.0365 (needed for 5/6)", Vcb0=0.0365)
line("y_t(m_t)=0.9269", yt0=0.9269)
line("y_t(m_t)=0.9469", yt0=0.9469)
line("Yukawa non-universal term x0.8", kyuk=0.8)
line("Yukawa non-universal term x1.2", kyuk=1.2)
line("2-loop gauge", loop2=True)
line("alpha_s(MZ)=0.1170", asMZ=0.1170)
line("alpha_s(MZ)=0.1190", asMZ=0.1190)
line("m_s(2GeV)=92.6 MeV", MS2=0.0926)
line("m_s(2GeV)=94.2 MeV", MS2=0.0942)
line("m_b(m_b)=4.155", MB=4.155)
line("m_b(m_b)=4.210", MB=4.210)
line("Yukawa term x3 (extreme)", kyuk=3.0)
print("\nextreme: what Yukawa strength would 5/6 need? scan kyuk")
for k in (5, 10, 20):
    mu, yt, R, V, p = P2.curve(kyuk=k)
    print(f"  kyuk={k}: p(M_Pl)={p[-1]:.4f}")
