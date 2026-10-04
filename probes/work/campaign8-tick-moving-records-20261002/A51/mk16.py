"""A51 mk16: map the |d|^2 <= 4 four-spin rules (B4_r4) found at 6^3 and 8^3 into A49's 23-operator basis for the 16-site
exact forward test (A49 fwd16).  O_(001) = 3(-J1 + (2/sqrt3) K1), O_(011) = 3 sqrt2 (-J2 + (2/sqrt3) Kn2), O_(002) = 3 J3,
O_(111) = sqrt12 J4 (A49 normalized operators); four-spin terms identical.  Checks the map on the 6^3 parton expectations."""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
names = ["J1", "K1", "D1", "J2", "Kn2", "Kd2", "D2", "J3", "K3", "D3", "J4", "Kd4", "D4", "T0", "T2", "C0", "Dm0", "Dm1", "Y0", "Y1", "Y2", "P0", "P1"]
out = {}
for L in (6, 8):
    R = np.load(f"rules51_{L}.npz"); ks = [tuple(k) for k in R["ks"]]; v = R["B4_r4"]; nc = len(ks)
    c = np.zeros(23); g = lambda k: v[ks.index(k)]
    c[0] = -3 * g((0, 0, 1)); c[1] = 2 * np.sqrt(3) * g((0, 0, 1))
    c[3] = -3 * np.sqrt(2) * g((0, 1, 1)); c[4] = 2 * np.sqrt(6) * g((0, 1, 1))
    c[7] = 3 * g((0, 0, 2)); c[10] = np.sqrt(12) * g((1, 1, 1)); c[13:21] = v[nc:nc + 8]
    out[f"L{L}_B4r4_inv"] = c
    print(f"L={L} B4_r4 -> A49 basis: " + " ".join(f"{nm}:{x:+.3f}" for nm, x in zip(names, c) if abs(x) > 1e-9))
# map check: A49 6^3 parton <J1>,<K1> = +0.3366, -0.5831 -> O_(001)/site = 3(-0.3366 + 1.1547*(-0.5831))
print(f"map check: 3(-0.3366 + (2/sqrt3)(-0.5831)) = {3*(-0.3366 + 2/np.sqrt(3)*(-0.5831)):+.4f} (A51 6^3 <O_001>/site -3.037)")
np.savez("rules16.npz", **out)
