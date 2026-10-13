"""R17-11 (b): linear order about FRW with dust, a TILTED lattice slicing, the E-sector and a grid vacuum with enthalpy W (sympy).

Gauge: synchronous-comoving for dust (as R15-1 Lemma S / R14-5 sec. 4.5):
   ds^2 = -dt^2 + a^2[(1 + eps h1 c) dx^2 + (1 + eps h2 c)(dy^2 + dz^2)],  c = cos(kx), s = sin(kx).
   Dust at rest, rho_m (1 + eps delta c), with delta' = -(h1' + 2 h2')/2 (dust conservation; imposed by h2 := -delta - h1/2).
Lattice time T = t + eps xi(t) c (R15-1: T = t + xi). Site frame n = unit normal of T = const; lattice lapse N = (-dT.dT)^(-1/2).
Fields of lattice time:  lam(T), g'(T)  (expanded to O(eps));  background lam' = -g' theta_n = -3 H g'  (Lemma C / generalized Lemma V).
Vacuum (site frame):  T_v = V n n + (W - V) h,  V constant,  W(t,x) = W0(t) + eps W1(t) c  ARBITRARY (enthalpy may vary).
E-sector: E = lam(T) n n + pE h with
   (d-i)       pE = g'(T)/N - lam(T) - W           (generalized Lemma V, r1711_lemmaV_general.out G1)
   (no-exch)   pE = g'(T)/N - lam(T)               (E conserved alone, vacuum not absorbed: Bianchi FAILS by Q; contrast only)
kappa = 1.

Checks:
  L1  all 10 components: E + T_v - [-(lam(T) + V) g + (g'(T)/N) h]  = 0 identically  (d-i), to O(eps).
      -> at g' = 0, lam const: E + T_v = -(lam + V) g: no xi, no W, no n in ANY component (momentum constraint included).
  L2  the 00 trace-reversed equation at O(eps):  delta'' + 2H delta' - (1/2) rho delta = (1/2)[(3 g'' + 6 H g') xi + 3 g' xi']
      for (d-i)  (R15-1 Lemma S kernel with g -> g'), and NO W0, W1 term.
  L3  contrast (no-exch): the W terms that (d-i) cancels: background -3 a''/a gets +3W0/2-type pressure terms; O(eps) gets W1 terms.
  L4  exchange current momentum leg at O(eps): Q_x = d_x W + W0 d_x ln N  (N = lattice lapse) = eps (W1 ... ) -- Planckian W0 x lapse gradient,
      which (d-i) hands to E.  Lemma S jump: Delta delta' = F D/(D - 3 g'/2) -> F at g' = 0 for every W (closed form).
"""
import sympy as sp

t, x, y, z, k, eps = sp.symbols('t x y z k epsilon', real=True)
a = sp.Function('a')(t); rho = sp.Function('rho_m')(t)
h1 = sp.Function('h1')(t); delta = sp.Function('delta')(t); xi = sp.Function('xi')(t)
lamf = sp.Function('lam'); gpf = sp.Function('gp')
W0 = sp.Function('W0')(t); W1 = sp.Function('W1')(t)
V = sp.symbols('V', real=True)
X = [t, x, y, z]
c = sp.cos(k*x); s = sp.sin(k*x)
h2 = -delta - h1/2          # so that h1 + 2 h2 = -2 delta (dust conservation in synchronous gauge)

g = sp.diag(-1, a**2*(1 + eps*h1*c), a**2*(1 + eps*h2*c), a**2*(1 + eps*h2*c))
gi = sp.simplify(g.inv())

def lin(e):
    """keep O(1) + O(eps)."""
    e = sp.expand(e)
    return sp.expand(e.subs(eps, 0) + eps*sp.diff(e, eps).subs(eps, 0))

# Ricci tensor (lower) to O(eps)
def christ(gm, gmi):
    return [[[lin(sp.Rational(1, 2)*sum(gmi[a_, d]*(sp.diff(gm[d, b], X[cc]) + sp.diff(gm[d, cc], X[b]) - sp.diff(gm[b, cc], X[d]))
                                       for d in range(4))) for cc in range(4)] for b in range(4)] for a_ in range(4)]
Gm = christ(g, gi)
def ricci(mu, nu):
    r_ = 0
    for a_ in range(4):
        r_ += sp.diff(Gm[a_][mu][nu], X[a_]) - sp.diff(Gm[a_][mu][a_], X[nu])
        for b in range(4):
            r_ += Gm[a_][a_][b]*Gm[b][mu][nu] - Gm[a_][nu][b]*Gm[b][mu][a_]
    return lin(r_)

# lattice slicing
T = t + eps*xi*c
dT = sp.Matrix([sp.diff(T, v) for v in X])
norm2 = lin(-(dT.T*gi*dT)[0, 0])
Nlat = lin(1/sp.sqrt(norm2))
n_low = sp.Matrix([lin(-Nlat*dT[i]) for i in range(4)])
n_up = (gi*n_low).applyfunc(lin)
h_low = (g + n_low*n_low.T).applyfunc(lin)
print("lattice lapse N =", sp.simplify(Nlat), "  (R15-1: delta N = -xi')")

# fields of lattice time, expanded; background relation lam' = -3 H g'
H = sp.diff(a, t)/a
lamT = lamf(t) + eps*xi*c*(-3*H*gpf(t))
gpT = gpf(t) + eps*xi*c*sp.diff(gpf(t), t)
Wtx = W0 + eps*W1*c

def build(pE):
    E = (lamT*n_low*n_low.T + pE*h_low).applyfunc(lin)
    Tv = (V*n_low*n_low.T + (Wtx - V)*h_low).applyfunc(lin)
    u_low = sp.Matrix([-1, 0, 0, 0])
    Tm = (rho*(1 + eps*delta*c)*u_low*u_low.T).applyfunc(lin)
    return E, Tv, Tm

pE_di = lin(gpT/Nlat - lamT - Wtx)
pE_nx = lin(gpT/Nlat - lamT)

# ---------- L1 --------------------------------------------------------------------
E, Tv, Tm = build(pE_di)
target = (-(lamT + V)*g + (gpT/Nlat)*h_low).applyfunc(lin)
res = (E + Tv - target).applyfunc(lambda e: sp.simplify(lin(e)))
print("L1 (d-i): max over 16 components of |E + T_v - [-(lam(T)+V) g + (g'(T)/N) h]| at O(eps):",
      "all zero" if res == sp.zeros(4, 4) else res)
at_g0 = (E + Tv).applyfunc(lambda e: sp.simplify(lin(e).subs(gpf(t), 0).doit()))
print("L1 (d-i), g' = 0:  E + T_v + (lam + V) g  =",
      "zero in all components" if (at_g0 + ((lamf(t) + V)*g).applyfunc(lin)).applyfunc(sp.simplify) == sp.zeros(4, 4) else "NONZERO")
print("     -> xi, W0, W1 and the site frame n absent from every component (incl. the 0x momentum constraint).")

# ---------- L2/L3: 00 trace-reversed equation ---------------------------------------
R00 = ricci(0, 0)
def rhs00(E, Tv, Tm):
    S = (E + Tv + Tm)
    trS = lin(sum(gi[m_, n_]*S[m_, n_] for m_ in range(4) for n_ in range(4)))
    return lin(S[0, 0] - sp.Rational(1, 2)*trS*g[0, 0])

def analyse(label, pE):
    E, Tv, Tm = build(pE)
    eq = lin(R00 - rhs00(E, Tv, Tm))
    bg = sp.simplify(eq.subs(eps, 0))
    first = sp.simplify(sp.diff(eq, eps).subs(eps, 0)/c)
    # background: solve for a''
    add = sp.solve(sp.Eq(bg, 0), sp.diff(a, t, 2))[0]
    first = sp.simplify(first.subs(sp.diff(a, t, 2), add))
    print(f"{label} background 00 eq:  a''/a =", sp.simplify(add/a))
    # normalise: coefficient of delta'' is +1 or -1
    coef = sp.simplify(sp.diff(first, sp.diff(delta, t, 2)))
    first = sp.expand(sp.simplify(first/coef))
    return first

f_di = analyse("(d-i)  ", pE_di)
expected = sp.diff(delta, t, 2) + 2*H*sp.diff(delta, t) - rho*delta/2 \
    - sp.Rational(1, 2)*((3*sp.diff(gpf(t), t) + 6*H*gpf(t))*xi + 3*gpf(t)*sp.diff(xi, t))
print("L2 (d-i): [O(eps) 00 eq] - [delta'' + 2H delta' - rho delta/2 - (1/2)((3g'' + 6Hg') xi + 3 g' xi')] =",
      sp.simplify(f_di - sp.expand(expected)))
print("L2 (d-i): W0 / W1 dependence of the O(eps) equation:",
      sp.simplify(sp.diff(f_di, W0)), sp.simplify(sp.diff(f_di, W1)))
print("L2 (d-i): xi dependence at g' = 0:", sp.simplify(f_di.subs(gpf(t), 0).doit().diff(xi)),
      sp.simplify(f_di.subs(gpf(t), 0).doit().diff(sp.diff(xi, t))))

f_nx = analyse("(no-exch)", pE_nx)
print("L3 (no-exch) contrast: W-dependent part of the O(eps) equation:",
      sp.simplify(f_nx - f_di))

# ---------- L4: exchange current momentum leg ------------------------------------------
lnN = lin(sp.log(Nlat))
Qx = lin(sp.diff(Wtx, x) + Wtx*sp.diff(lnN, x))
print("L4 Q_x (momentum leg of Q = div(W h)) at O(eps):", sp.simplify(Qx))
print("L4 Q_t-leg (energy) background: W0 * theta_n = 3 H W0 (r1711_lemmaV_general G2).")
D, gp_, F = sp.symbols('D g_p F', real=True)
jump = F*D/(D - sp.Rational(3, 2)*gp_)
print("L4 Lemma S jump (R15-1, kernel unchanged by W per L2):", jump, "-> at g' = 0:", jump.subs(gp_, 0))

# ---------- L3b: momentum constraint (0x) contrast ---------------------------------------
for label, pE in (("(d-i)", pE_di), ("(no-exch)", pE_nx)):
    E, Tv, Tm = build(pE)
    S0x = sp.simplify(lin((E + Tv)[0, 1]))
    print(f"L3b {label}: (E + T_v)_0x at O(eps) =", S0x,
          " (source of the 0x momentum constraint beyond dust)")
print("     -> without exchange the lattice tilt xi carries a Planckian momentum density -W0 k xi sin(kx) (frame visible);"
      " with (d-i) only the g' (R15-1) term remains, zero under (S).")
