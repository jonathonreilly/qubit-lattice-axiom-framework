"""T127 - THE SIGN OF INDUCED GRAVITY, FROM THE FRAMEWORK'S OWN FIBRE.

T126 verified G = 12 pi tau_0 to 0.03% -- but for ONE SCALAR.  The framework's
matter field is not a scalar: it is the Kahler-Dirac field, Gamma_a = eps_a +
iota_a on the exterior algebra, whose fibre is an irreducible Cl(d,d) module of
rank 2^d = 16 in d=4 (spin (x) flavour).  Sakharov's induced 1/G is a SUM OVER
THE FIELD CONTENT with signs, and the sign is what decides whether the induced
gravity is attractive.  In this framework the content is NOT free -- it is fixed
by the Clifford structure -- so the framework predicts the sign.

Two facts do the work, and both have a sign that must be got right:
  (1) D^2 = the Hodge Laplacian on the FULL exterior algebra, so the heat trace
      is the sum over all form degrees, NOT 16 copies of the scalar one.  The
      Weitzenbock curvature terms differ per degree and do not cancel.
  (2) statistics: a boson contributes W = +(1/2) logdet, a fermion
      W = -logdet(D) = -(1/2) logdet(D^2).  Opposite overall sign.
Both must be applied, and getting either wrong flips the answer, so each is
checked separately below rather than asserted together.

On S^2 the full Hodge spectrum is exactly known:
   Delta_0: l(l+1), mult 2l+1 (l>=0);  Delta_2 = Delta_0 by Hodge duality;
   Delta_1: l(l+1), mult 2(2l+1) (l>=1), b_1 = 0.
   =>  K_form(tau) = 2 K_0 + 2(K_0 - 1) = 4 K_0 - 2.
Rank check: 4 = 2^2.  Constant term: 4(chi/6) - 2 = 4/3 - 2 = -2/3, i.e.
a_1 = -(1/3) int R, against +(1/6) int R for a single scalar: OPPOSITE SIGN and
twice the size.  That is fact (1) in d=2, and it is checked numerically below
rather than trusted."""
import numpy as np, itertools
def K0_sph(s,LMAX=4000):
    l=np.arange(LMAX+1.0); return float(np.sum((2*l+1)*np.exp(-s*l*(l+1))))
def K0_tor(s,W=14):
    t=0.0
    for w in itertools.product(range(-W,W+1),repeat=2): t+=np.exp(-(w[0]**2+w[1]**2)/(4.0*s))
    return t/(4*np.pi*s)
Kform_sph=lambda s: 4*K0_sph(s)-2.0          # full exterior algebra on S^2
Kform_tor=lambda s: 4*K0_tor(s)              # flat: 4 identical copies

print("T127  the sign of induced gravity from the Kahler-Dirac fibre")
print()
print("(1) CHECK fact (1) numerically in 2D: constant term of the full form trace")
print(f"    {'tau':>8} {'K_form - 4 Area/(4 pi tau)':>28} {'one scalar: K_0 - A/(4pi t)':>30}")
for s in (0.02,0.01,0.005,0.002):
    print(f"    {s:8.4f} {Kform_sph(s)-4*4*np.pi/(4*np.pi*s):28.6f} {K0_sph(s)-4*np.pi/(4*np.pi*s):30.6f}")
print(f"    predicted:            -2/3 = {-2/3:.6f}                     chi/6 = {1/3:.6f}")
print(f"    ratio  a_1(form)/a_1(scalar) = {(-2/3)/(1/3):.4f}   -> opposite sign, twice the size")
print()
print("(2) the same in 4D by the product structure, Lambda*(S^2 x T^2) = Lambda* (x) Lambda*")
VOL=4*np.pi
K4=lambda s: Kform_sph(s)*Kform_tor(s)
print(f"    {'tau':>8} {'[(4 pi t)^2 K4 - 16 Vol]/t':>28} {'one scalar (T126 route)':>26}")
for s in (0.01,0.005,0.002,0.001):
    a=((4*np.pi*s)**2*K4(s)-16*VOL)/s
    b=((4*np.pi*s)**2*(K0_sph(s)*K0_tor(s))-VOL)/s
    print(f"    {s:8.4f} {a:28.6f} {b:26.6f}")
print(f"    predicted a_1(form)  = -(4/3) int R = {-(4/3)*8*np.pi:.6f}")
print(f"    predicted a_1(scalar)= +(1/6) int R = {(1/6)*8*np.pi:.6f}")
print(f"    ratio = {-(4/3)/(1/6):.1f}")
print()
print("(3) THE INDUCED 1/G, with statistics applied explicitly.")
print("    scalar boson :  W = -(1/2) int (ds/s)[K - free],  matched to -(1/16 pi G) int R")
print("    KD fermion   :  W = +(1/2) int (ds/s)[K - free]   (opposite overall sign)")
def tauI(tau0,m2,Kfun,rank,sign,NQ=3000,SMAX=60.0):
    ss=np.exp(np.linspace(np.log(tau0),np.log(SMAX),NQ))
    f=np.array([(Kfun(s)-rank*VOL/(4*np.pi*s)**2)*np.exp(-s*m2)/s for s in ss])
    tr=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
    return tau0*sign*0.5*tr(f,ss)
print(f"    {'m^2':>7} {'scalar boson':>16} {'KD fermion (16)':>18} {'ratio':>9}")
for m2 in (0.2,0.1,0.05):
    a=-tauI(0.001,m2,lambda s:K0_sph(s)*K0_tor(s),1,+1.0)   # boson: -(1/2)
    b=+tauI(0.001,m2,K4,16,+1.0)                            # fermion: +(1/2)
    print(f"    {m2:7.3f} {a:16.7f} {b:18.7f} {b/a:9.3f}")
print()
print("    Positive ratio = the Kahler-Dirac fibre induces gravity with the SAME sign")
print("    as an ordinary scalar, i.e. ATTRACTIVE, and 8x stronger per field.")
print("    Negative ratio = wrong-sign (ghost) induced gravity, a real problem for")
print("    the framework and a genuine prediction either way.")
