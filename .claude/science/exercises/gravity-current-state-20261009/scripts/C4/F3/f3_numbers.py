# F3 arithmetic: Pospelov-Shang bound, healthy window, hierarchy sizes, dimensional transmutation
import math
MPl = 1.221e19   # non-reduced Planck mass, GeV (repo convention, a^-1 = M_Pl)
MPr = 2.435e18   # reduced
print("== (1a) PS bound, F2 form dc = (M*/M)^2/(16 pi^2) ==")
bounds = {"GW-like 1e-15":1e-15, "gamma decay 2.7e-19":2.7e-19, "PS text 1e-20":1e-20, "GZK p/gamma 4e-23":4e-23}
for name,b in bounds.items():
    for lab,M in (("nonred",MPl),("red",MPr)):
        Ms = M*math.sqrt(16*math.pi**2*b)
        print(f"  {name:22s} {lab:6s} M* < {Ms:.3e} GeV  L=M_Pl/M* > {MPl/Ms:.3e}")
print("== (1b) PS eq.55 (healthy, vector cured): dc ~ (M*^2/(12 pi^2 M^2)) * ln(Luv^2/M*^2), Luv = M_Pl (grid) ==")
for name,b in bounds.items():
    for lab,M in (("nonred",MPl),("red",MPr)):
        # solve x = M*/M : x^2 * 2 ln(MPl/(x M)) /(12 pi^2) = b
        lo,hi=1e-30,1.0
        for _ in range(200):
            x=math.sqrt(lo*hi)
            f=x*x*2*math.log(MPl/(x*M))/(12*math.pi**2)-b
            if f>0: hi=x
            else: lo=x
        Ms=x*M
        print(f"  {name:22s} {lab:6s} M* < {Ms:.3e} GeV  log factor 2ln(M_Pl/M*)={2*math.log(MPl/Ms):.1f}  L > {MPl/Ms:.3e}")
print("  PS uncured vector term Luv^2/(24 pi^2 M^2) with Luv = M (grid = Planck):", 1/(24*math.pi**2), "(nonred,red equal if Luv=M)")
print("  ... with Luv = M_Pl nonred and M reduced:", (MPl/MPr)**2/(24*math.pi**2))
print("== (1c) healthy-Horava window: M* < M_SC ~ sqrt(alpha) c_S^{-1/2} M (GSS eq.15, reduced M) ==")
def cS2(a,g,b=0.0): return (2-a)*(g+b)/(a*(1-b)*(2+3*g+b))
for a,g in ((8e-7,0.01),(1e-9,0.01),(1e-12,0.01),(1e-15,0.01),(1e-18,0.01)):
    c2=cS2(a,g); Msc=math.sqrt(a)*c2**(-0.25)*MPr
    print(f"  alpha={a:.0e} gamma={g}: c_S={math.sqrt(c2):.3e}  M_SC={Msc:.3e} GeV")
# alpha needed for M_SC > M* = 1e10, 2e9: M_SC ~ alpha^{3/4} gamma^{-1/4} sqrt(2)^{...}; solve numerically
for Ms in (1.5e10,2e9):
    lo,hi=1e-40,1.0
    for _ in range(300):
        a=math.sqrt(lo*hi); Msc=math.sqrt(a)*cS2(a,0.01)**(-0.25)*MPr
        if Msc>Ms: hi=a
        else: lo=a
    print(f"  M*={Ms:.1e}: need alpha > {a:.2e} (gamma=0.01) for M* < M_SC; window to 8e-7 weak-PPN")
print("== (2) hierarchy sizes on one grid (a^-1 = M_Pl nonred) ==")
for Ms in (1.5e10,2e9):
    L=MPl/Ms
    print(f"  M*={Ms:.1e}: L={L:.3e}, z=3 coefficient (M_Pl/M*)^4={L**4:.3e} lattice units, (M*/M_Pl)^2 = G_Lif = {1/L**2:.3e}")
    kmax=(math.pi*Ms**2*MPl)**(1/3)
    print(f"    Z^4 tick (omega<=pi/a): z=3 regime fits only to k_max=(pi M*^2/a)^(1/3)={kmax:.3e} GeV = {kmax/MPl:.2e}/a")
    Lnat=math.sqrt(4*math.pi*MPl*Ms)
    print(f"    continuous-time gravity: z=1 coeff natural only if gravity cutoff < sqrt(4pi M M*)={Lnat:.3e} GeV; at cutoff M_Pl the loop/tree ratio ~ (M_Pl/that)^4={(MPl/Lnat)**4:.2e}")
    Nsp=16*math.pi**2*L**2
    print(f"    species needed for O(1) induced LV in graviton at M*: N ~ 16pi^2 (M/M*)^2 = {Nsp:.2e}")
print("== (2b) dimensional transmutation: Lambda_h/M_Pl = exp(-2pi/(b0 alpha)) (1-loop); 2-loop SU(N) ==")
target=1e-9
for name,b0,b1 in (("SU(2) YM",22/3,136/3),("SU(3) YM",11,102),("SU(3)+6 flavours (QCD-like)",7,26),("SU(5) YM",55/3,3400/3*0+ (34/3)*25)):
    a1=2*math.pi/(b0*math.log(1/target))
    # 2-loop: Lambda = mu exp(-1/(2 b0' g2)) (b0' g2)^(-b1'/(2 b0'^2)) with b0'=b0/(16pi^2), b1'=b1/(16pi^2)^2, g2=4pi alpha
    B0=b0/(16*math.pi**2); B1=b1/(16*math.pi**2)**2
    lo,hi=1e-4,10.0
    for _ in range(200):
        g2=math.sqrt(lo*hi)
        r=math.exp(-1/(2*B0*g2))*(B0*g2)**(-B1/(2*B0**2))
        if r>target: hi=g2
        else: lo=g2
    print(f"  {name:28s} b0={b0:.3f}: 1-loop alpha_h={a1:.4f} (1/alpha={1/a1:.1f}); 2-loop alpha_h={g2/(4*math.pi):.4f}")
# sensitivity: dln(Lambda)/dln(alpha) = 2pi/(b0 alpha) = ln(1/target)
print(f"  sensitivity d ln Lambda / d ln alpha = ln(1e9) = {math.log(1e9):.1f} (no fine tuning: a 5% change in alpha moves Lambda by e^{0.05*math.log(1e9):.2f})")
print("== (2c) spontaneous khronon from a DT sector: alpha,beta ~ (Lambda_h/M)^2 ==")
for Lh in (1e9,1.5e10,1e11):
    print(f"  Lambda_h={Lh:.1e}: (Lambda_h/M_Pl)^2={(Lh/MPl)**2:.2e}; PS percolation (.../16pi^2)={(Lh/MPl)**2/(16*math.pi**2):.2e}")
