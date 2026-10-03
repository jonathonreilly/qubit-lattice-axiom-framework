"""A44 map: where on the (J,K,D) sphere the projected parton states beat the competitors.
Inputs: VMC per-sweep samples (vmc_*.npy), LSWT/classical rows (lswt_rows.npy, LT column halved: the
lswt.py kernel lacked the 1/2 of the symmetrised Fourier form).  Parton family = VMC vectors at the
largest L available for each distinct state, plus the inversion images (e_J, e_K, -e_D)."""
import glob, numpy as np, signal
signal.alarm(60)
D = __file__.rsplit('/', 1)[0]
def vec(f):
    S = np.load(f); return S[:, :3].real.mean(0)
fam = {}
for f in sorted(glob.glob(D + "/vmc_*.npy")):
    tag = f.rsplit('/', 1)[1][4:-4]
    fam[tag] = vec(f)
for k, v in fam.items():
    print(f"  VMC {k:12s}: e = ({v[0]:+.4f}, {v[1]:+.4f}, {v[2]:+.4f})")
sold = fam.get("8_sold90", fam.get("6_sold90"))
s = -1.5 * (sold[0] - sold[1])          # Klein: e_J = -s/3, e_K = s/3
print(f"  Klein-dual pi-flux bond energy from the L=8 soldered state: s = {s:+.4f}")
family = []   # largest L per distinct state of the (t, lam) family: L=8 soldered and t-only, L=6 mixed
for k in ("8_sold90", "8_sold0", "6_sold15", "6_sold40", "6_sold51", "6_sold62.5"):
    v = fam[k]; family.append((k, v)); family.append((k + "*", v * np.array([1, 1, -1])))
tonly = fam["8_sold0"]
pi = np.array([s, s / 3, 0.])
R = np.load(D + "/lswt_rows.npy")
print("\n beta  phi |   J      K      D   | E_sold  E_parton(best, state) E_t-only E_pi-flux | E_cl   E_LSWT | sold<cl par<cl par<LSWT sold lowest-variational")
win = []
for be, ph, J, K, Dd, Ecl_named, Elsw, Eg, lt2 in R:
    n = np.array([J, K, Dd]); Ecl = min(Ecl_named, Eg)
    Es = n @ sold; Et = n @ tonly; Ep = n @ pi
    kb, vb = min(family, key=lambda kv: n @ kv[1]); Eb = n @ vb
    var_min = min(Es, Eb, Et, Ep, Ecl)
    flags = (Es < Ecl - 1e-9, Eb < Ecl - 1e-9, (not np.isnan(Elsw)) and Eb < Elsw, abs(Es - var_min) < 1e-12)
    if flags[0]: win.append(ph if be == 0 else None)
    print(f" {be:4.0f} {ph:6.1f} | {J:+.3f} {K:+.3f} {Dd:+.3f} | {Es:+.4f} {Eb:+.4f} ({kb:9s}) {Et:+.4f} {Ep:+.4f} | {Ecl:+.4f} {Elsw:+.4f} | "
          + "  ".join('Y' if f else '.' for f in flags))
# analytic window on the D=0 circle: soldered beats the best classical state
ph = np.radians(np.arange(0, 360, 0.05)); J, K = np.cos(ph), np.sin(ph)
Es = (K - J) * s / 3
Ecl = np.minimum.reduce([-J - K / 3, J + K / 3, (J - K) / 3])   # Neel / uniform / compass-staggered
inw = Es < Ecl
if inw.any():
    print(f"\n D=0 circle: soldered (s={s:+.4f}) below the best named product state for phi in "
          f"[{np.degrees(ph[inw]).min():.2f}, {np.degrees(ph[inw]).max():.2f}] deg; max margin {np.max(Ecl - Es):.4f} per bond")
else:
    print("\n D=0 circle: soldered never below the best named product state")
for sv in (-1.0, -1.01, -1.03, -1.0889):
    Es2 = (K - J) * sv / 3; w = Es2 < Ecl
    print(f"   if s = {sv:+.4f}: window " + (f"[{np.degrees(ph[w]).min():.2f}, {np.degrees(ph[w]).max():.2f}] deg, margin {np.max(Ecl - Es2):.4f}" if w.any() else "empty"))
