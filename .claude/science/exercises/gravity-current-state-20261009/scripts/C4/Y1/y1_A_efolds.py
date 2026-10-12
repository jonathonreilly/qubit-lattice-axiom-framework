# Y1: e-folds n_var = c*sqrt(eps)*tau/l_k, tau = sqrt(2 D s + s^2), eps=(l_P/l_k)^4
import math
lP=1.616255e-35; Gpc=3.0857e25; c_light=2.998e8
lk=7.9e-20
eps=(lP/lk)**4; se=math.sqrt(eps)
print(f"l_k={lk:.2e} m  eps={eps:.3e}  sqrt(eps)={se:.3e}  sqrt(eps)/l_k={se/lk:.3e} /m")
consts={'c_low op0 (proved)':0.628,'c_low op2 (proved)':0.712,'k_h op0 (derived)':2.735,'k_h op2 (derived)':3.254}
for name,c in consts.items():
    g=c*se/lk
    print(f"{name}: var rate gamma={g:.3e}/m  2/gamma={2/g:.3e} m")
cases=[('atom size',1e-10),('optical thermal coherence (~1 um)',1e-6),
('optical line, 10 ns lifetime (3 m)',3.0),('radio continuum, 100 MHz band (3 m)',3.0),
('radio, 1 MHz channel (300 m)',300.0),('maser line, ~1 km',1e3),('maser/1 kHz channel (3e5 m) = FRB 1 ms',3e5),
('1 s emission',c_light*1),('lensed SN, ~100 d',c_light*8.64e6),('quasar monitoring 20 yr',c_light*20*3.156e7),
('quasar lifetime 1e7 yr',c_light*1e7*3.156e7)]
for D in (1,3,5):
    DD=D*Gpc
    print(f"\n=== D = {D} Gpc (flat-space proper-time formula) ===")
    print(f"{'source extent':45s} {'s (m)':>9s} {'tau (m)':>9s} {'n_var c_low':>12s} {'n_var k_h':>12s}  (op0; sd = n_var/2)")
    for nm,s in cases:
        tau=math.sqrt(2*DD*s+s*s)
        print(f"{nm:45s} {s:9.2e} {tau:9.2e} {0.628*se*tau/lk:12.3e} {2.735*se*tau/lk:12.3e}")
    for name,c in (('c_low op0',0.628),('k_h op0',2.735)):
        g=c*se/lk
        s1=1/(2*DD*g*g); s2=4/(2*DD*g*g)
        print(f"  threshold s for n_var=1 ({name}): {s1:.3e} m = {s1/c_light:.2e} s ; for n_sd=1 (n_var=2): {s2:.3e} m = {s2/c_light:.2e} s")
# cross-covariance end-rung suppression (RL3b Lemma D): ratio ~ z/|Delta| in l_k units = gamma*lk^2/r
print("\nDisplaced-end suppression z/|Delta| = gamma*l_k^2/r (c=k_h op0):")
g=2.735*se/lk
for r in (1e-15,1e-10,1e-6,1.0):
    print(f"  r={r:.0e} m: {g*lk*lk/r:.2e}")
# geometric shared proper time: y,y' at transverse r, x at proper time tau from each; tau_x = max over common future
print("\nGeometric shared proper time tau_x = sqrt(tau^2+r^2/4)-r/2 (exact, rest frame of x-midpoint):")
for tau,r in ((7.9e12,1e-10),(7.9e12,1e12),(7.9e12,1e13)):
    tx=math.sqrt(tau**2+r**2/4)-r/2
    print(f"  tau={tau:.1e} r={r:.0e}: tau_x={tx:.4e}, tau-tau_x={tau-tx:.3e}")
# observational: lensed quasar ages and detector band suppression heuristics
for nm,om in (('optical 600 nm',2*math.pi*c_light/600e-9),('radio 5 GHz',2*math.pi*5e9),('radio 22 GHz maser',2*math.pi*22e9)):
    x=lk*om/c_light
    print(f"band parameter l_k*omega/c for {nm}: {x:.2e}  ln = {math.log(x):.1f}")
