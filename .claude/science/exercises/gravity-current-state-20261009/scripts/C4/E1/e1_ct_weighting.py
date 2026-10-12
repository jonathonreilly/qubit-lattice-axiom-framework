"""Check: in Anber-Donoghue's one-loop speed beta functions (arXiv:1102.0789, as
extracted), (a) the C_T-weighted mean speed is RG-invariant to first order in the
speed difference, (b) each sector's speed relaxes at a rate proportional to 1/C_T,
(c) the QED relaxation rate equals the DGLAP n=2 singlet eigenvalue lambda+=8
(units alpha/4pi) and KLP's Q^-3. Free-field C_T ratios (4D): real scalar 1,
Dirac fermion 6, Maxwell field 12 (Osborn-Petkou; comparator)."""
import sympy as sp
g,e,eta,c=sp.symbols('g e eta c',positive=True)
pi=sp.pi
# Yukawa: real scalar (b) + Dirac fermion (f)
cb,cf=sp.symbols('c_b c_f',positive=True)
beta_cb = g**2*(cb**2-cf**2)/(8*pi**2*cb*cf**3)
beta_cf = g**2*(cf-cb)/(6*pi**2*cb*(cf+cb)**2)
def lin(expr):
    return sp.simplify(sp.series(expr.subs({cb:1+eta,cf:1}),eta,0,2).removeO())
Yb,Yf=lin(beta_cb),lin(beta_cf)
print("Yukawa: beta(c_b) ~",Yb," beta(c_f) ~",Yf)
print("  rate ratio boson/fermion =",sp.simplify(Yb/(-Yf)),"(C_T ratio Dirac/real scalar = 6)")
print("  C_T-weighted sum 1*beta_b + 6*beta_f =",sp.simplify(Yb+6*Yf))
print("  relative-speed rate d(eta)/dlnmu / eta =",sp.simplify((Yb-Yf)/eta))
# QED: photon (g) + Dirac fermion (f)
cg=sp.symbols('c_g',positive=True)
beta_cg = 4*e**2/(3*(4*pi)**2)*(cg**2-cf**2)/(cf*cg)
beta_cf2= 8*e**2/(3*(4*pi)**2)*(cf-cg)*(4*cf**2+3*cf*cg+cg**2)/(cg*(cf+cg)**2)
Qg=sp.simplify(sp.series(beta_cg.subs({cg:1+eta,cf:1}),eta,0,2).removeO())
Qf=sp.simplify(sp.series(beta_cf2.subs({cg:1+eta,cf:1}),eta,0,2).removeO())
print("QED: beta(c_g) ~",Qg," beta(c_f) ~",Qf)
print("  rate ratio fermion/photon =",sp.simplify(-Qf/Qg),"(C_T ratio Maxwell/Dirac = 2)")
print("  C_T-weighted sum 12*beta_g + 6*beta_f =",sp.simplify(12*Qg+6*Qf))
rate=sp.simplify((Qg-Qf)/eta)
alpha=sp.symbols('alpha',positive=True)
print("  relative rate =",rate," = (alpha/4pi) *",sp.simplify(rate.subs(e,sp.sqrt(4*pi*alpha))/(alpha/(4*pi))),
      " (DGLAP lambda+ for QED, 1 flavour = 8; with |beta0|=4/3 -> exponent 3 = KLP Q^-3)")
