"""parse s2_scan text outputs into dict[(bU, v)] -> {'gap': g, ('axis', m, ch): (S, main), ...}"""
import re
def parse(files):
    D = {}; cur = None
    for f in files:
        for line in open(f):
            m = re.match(r"bU=([\d.]+) v=([-\d.]+) E0=\S+ gaps\(w1..w3-w0\)=\[\s*([\d.e+-]+)", line)
            if m:
                cur = (float(m.group(1)), float(m.group(2))); D[cur] = {"gap": float(m.group(3))}; continue
            m = re.match(r"\s+(\w+)\s+m=\s*(-?\d+) k=\S+ \| (.*)", line)
            if m and cur is not None:
                nm, mm = m.group(1), int(m.group(2))
                for part in m.group(3).split(" | "):
                    ch = part.split(":")[0].strip()
                    if "S=0" == part.split(":")[1].strip(): D[cur][(nm, mm, ch)] = (0.0, None); continue
                    S = float(re.search(r"S=([\d.e+-]+)", part).group(1)); mn = float(re.search(r"main=([-\d.e+]+)", part).group(1))
                    D[cur][(nm, mm, ch)] = (S, mn)
    return D
