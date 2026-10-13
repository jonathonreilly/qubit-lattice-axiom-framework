"""R19-7 s10: audit of the 'main pole' diagnostic. ed.diagnose falls back to the lowest pole (any weight) when no pole
carries >= 10% of S (np.argmax of an all-False mask returns 0). Flag, per channel, entries with main < low (certain fallback)
and entries where main differs from the long-time decay rate r20 by > 10% (possible fallback or multi-pole spread)."""
import re, glob
files = ["s2_scan_cube2.out", "s2_scan_tilt3.out", "s2_scan_tilt4_partA.out"] + sorted(glob.glob("s2_scan_tilt4_b*.out"))
for f in files:
    nT2 = 0; badT2 = []; fall = {}
    cur = None
    for line in open(f):
        m = re.match(r"bU=([\d.]+) v=([-\d.]+)", line)
        if m: cur = (float(m.group(1)), float(m.group(2))); continue
        m = re.match(r"\s+(\w+)\s+m=\s*(-?\d+) k=\S+ \| (.*)", line)
        if not m: continue
        for part in m.group(3).split(" | "):
            ch = part.split(":")[0].strip()
            if "main=" not in part: continue
            mn = float(re.search(r"main=([-\d.e+]+)", part).group(1)); lo = float(re.search(r"low=([-\d.e+]+)", part).group(1))
            r20 = float(re.search(r"r20=([-\d.e+na]+)", part).group(1))
            if mn < lo - 1e-9: fall.setdefault(ch, []).append((cur, m.group(1), int(m.group(2))))
            if ch == "TT2" and m.group(1) == "axis":
                nT2 += 1
                if abs(mn - r20) > 0.1*max(abs(r20), 1e-12): badT2.append((cur, int(m.group(2)), mn, r20))
    print(f, "| axis TT2 entries", nT2, "| TT2 axis main vs r20 >10%%: %d %s" % (len(badT2), badT2[:6]))
    print("   certain fallbacks (main < low) by channel:", {k: len(v) for k, v in fall.items()}, " TT2 cases:", fall.get("TT2", [])[:5])
