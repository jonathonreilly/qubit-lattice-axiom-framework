"""R18-10 s7: channel structure factors along axis, face and body directions at the smallest |k| (m = 1), using R18-1's
analyze.channels unchanged: S_V/S_TT, S_S/S_TT and S_gamma/q^2. White noise: S_V/S_TT = 4/3 on the axis (R18-1 report section 4).
A Coulomb pinch needs S_V -> 0 along EVERY direction; a planar (subsystem) artefact suppresses only the axis lines."""
import numpy as np, pickle, sys, os
from analyze import channels
print("%-26s %-5s %-3s | %-34s | %-34s | %-34s" % ("run", "bU", "L", "axis: V/TT  S/TT  Sg/q2", "face: V/TT  S/TT  Sg/q2", "body: V/TT  S/TT  Sg/q2"))
for f in sys.argv[1:]:
    res = pickle.load(open(f, "rb")); tab = channels(res); out = []
    for name in ["axis", "face", "body"]:
        q2, d = tab[(name, 1)]
        out.append("%6.3f %6.3f %6.3f" % (d['V'][0]/d['TT'][0], d['S'][0]/d['TT'][0], d['gam'][0]/q2))
    print("%-26s %-5.2f %-3d | %-34s | %-34s | %-34s" % (os.path.basename(f), res['bU'], res['L'], out[0], out[1], out[2]))
