"""R2-6 numbers at a = l_P (repo convention a^-1 = M_P, non-reduced, 1.22089e19 GeV).

Inputs from memory unless marked: MICROSCOPE SUEP test masses (Pt/Rh ~0.4015 kg,
Ti alloy ~0.3009 kg); |eta| bound ~1e-15 (PRL 129, 121102: (-1.5 +- 2.3 +- 1.5)e-15,
checked by search); LLR |Delta(mG/mI)| ~ 1e-13 (as in O2); Earth 5.972e24 kg,
Moon 7.342e22 kg; nucleon 0.939 GeV; Fermi momentum 0.25 GeV; LHAASO
E_QG,1 > 10 E_Pl, E_QG,2 > 6e-8 E_Pl (packet: C4_B1_report.md:233-236, O1 referee).
"""
import mpmath as mp

mp.mp.dps = 40
MP_GeV = mp.mpf('1.22089e19')
MP_kg = mp.mpf('2.17643e-8')
a = 1 / MP_GeV  # GeV^-1
mN, kF = mp.mpf('0.939'), mp.mpf('0.25')
GeV_per_kg = MP_GeV / MP_kg


def fac_left(x):   # aM/sinh(aM): response of P(+)q
    return x / mp.sinh(x)


def fac_right(x):  # aM coth(aM): response of q(+)P
    return x / mp.tanh(x)


def eta(f1, f2):
    return 2 * abs(f1 - f2) / (f1 + f2)


print("== (b) dispersion: Snyder free one-particle mass shell is exactly Lorentz invariant ==")
print("  dimension-5 coefficient = 0, dimension-6 coefficient = 0 (any a): LHAASO E_QG,1 > 10 E_Pl and")
print("  E_QG,2 > 6e-8 E_Pl both pass with infinite margin at tree level (velocity = p/E, r26_composition C7).")
print()
print("== (c) mapping A: a body of mass M kicked as ONE Snyder particle with scale a ==")
bodies = [("25 kDa molecule", mp.mpf('25e3') * mp.mpf('1.66054e-27')),
          ("16 microgram crystal", mp.mpf('16e-9')),
          ("MICROSCOPE Ti (~0.3009 kg)", mp.mpf('0.3009')),
          ("MICROSCOPE Pt (~0.4015 kg)", mp.mpf('0.4015')),
          ("Moon", mp.mpf('7.342e22')),
          ("Earth", mp.mpf('5.972e24'))]
xs = {}
for name, Mkg in bodies:
    x = Mkg / MP_kg
    xs[name] = x
    fl, fr = fac_left(x), fac_right(x)
    print(f"  {name:28s} aM = {mp.nstr(x, 5):>12s}   left factor aM/sinh(aM) = {mp.nstr(fl, 5):>12s}   right factor aM coth(aM) = {mp.nstr(fr, 5)}")
xT, xP = xs["MICROSCOPE Ti (~0.3009 kg)"], xs["MICROSCOPE Pt (~0.4015 kg)"]
xE, xM = xs["Earth"], xs["Moon"]
print(f"  MICROSCOPE eta (right) = {mp.nstr(eta(fac_right(xT), fac_right(xP)), 5)}  vs bound ~1e-15")
print(f"  MICROSCOPE left: both factors < 1e{int(mp.floor(mp.log10(fac_left(xT))))}: the masses would not fall at all")
print(f"  LLR eta (right) = {mp.nstr(eta(fac_right(xE), fac_right(xM)), 5)}  vs bound ~1e-13; left: neither body falls")
# threshold mass for eta < 1e-15 under mapping A (small aM: eta ~ |x1^2 - x2^2|/6 (left) or /3 (right))
for lab, den in [("left", 6), ("right", 3)]:
    xmax = mp.sqrt(den * mp.mpf('1e-15') / (1 - (xT / xP)**2))
    print(f"  mapping A ({lab}): eta(Ti,Pt-ratio bodies) < 1e-15 needs M_Pt < {mp.nstr(xmax, 3)} M_P = {mp.nstr(xmax * MP_kg, 3)} kg")
print()
print("== (c) mapping B: each constituent (granularity mu) kicked separately, total never (+)-composed ==")
for lab, mu in [("electron", mp.mpf('0.000511')), ("nucleon", mN), ("Ti-48 nucleus", 47.9 * mp.mpf('0.9315')),
                ("Pt-195 nucleus", 195.1 * mp.mpf('0.9315'))]:
    print(f"  {lab:15s} (a mu)^2/6 = {mp.nstr((a * mu)**2 / 6, 4)}")
d_nuc = ((a * 195.1 * mp.mpf('0.9315'))**2 - (a * 47.9 * mp.mpf('0.9315'))**2) / 6
print(f"  nucleus-granularity Ti vs Pt: eta_B ~ {mp.nstr(d_nuc, 3)}; nucleon granularity: eta_B <~ {mp.nstr((a*mN)**2/6, 3)}")
print(f"  effective composite scale needed: M_P,eff >= M / sqrt(6e-15) = {mp.nstr(1/mp.sqrt(6e-15), 3)} x M")
print()
print("== (c) per-constituent (+)-total of a body with Fermi motion (C5 fit, perturbative regime aM<~1) ==")
C = mp.mpf('0.12')
for Nlab, N in [("1e12", mp.mpf('1e12')), ("1e16", mp.mpf('1e16')), ("1e18", mp.mpf('1e18'))]:
    v = C * a**2 * mN * kF * N**mp.mpf(1.5)
    print(f"  N = {Nlab}: aM = {mp.nstr(a * N * mN, 3)}, spurious velocity ~ {mp.nstr(v, 3)} c")
Nstar = (mp.mpf('1e-15') / (C * a**2 * mN * kF))**(mp.mpf(2) / 3)
print(f"  spurious velocity reaches 1e-15 c at N ~ {mp.nstr(Nstar, 3)} nucleons ({mp.nstr(Nstar * mp.mpf('1.6726e-27'), 3)} kg)")
print(f"  aM = 1 (non-perturbative) at N = {mp.nstr(MP_GeV / mN, 3)} nucleons ({mp.nstr(MP_kg, 3)} kg)")
print()
print("== (d) tree-level size of the Lemma W defect: O((a E)^2) relative, E = collision energy scale incl. mass")
print("   (C6: |k1+k2-k3-k4| = 0.729 a^2 in units m = 1 with spatial momenta ~0.5 m) ==")
for lab, k in [("nucleon ~0.94 GeV", mN), ("1 TeV", mp.mpf('1e3')), ("1e11 GeV", mp.mpf('1e11'))]:
    print(f"  {lab:18s}: (a E)^2 = {mp.nstr((a * k)**2, 3)}")
