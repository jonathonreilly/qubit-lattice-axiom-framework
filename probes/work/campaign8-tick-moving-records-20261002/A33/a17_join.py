"""A33 a17: join r4_resolve.txt (Z^3 mobility) with r4_recert.txt (6^3/7^3 impurity certificates, k(16)/N)."""
import re, ast, collections
mob = {}
for line in open("r4_resolve.txt"):
    if not line[0].isdigit():
        continue
    n = int(line.split()[0])
    parts = line.split(" sol=")[1].split("} ", 1)[1].split(" | ")
    kinds = []
    for p in parts:
        r, st = p.split(":", 1)
        if st.startswith("imm"):
            continue
        movers = ast.literal_eval(re.search(r"Z3movers(\[.*?\])", st).group(1))
        if not movers:
            kinds.append(f"{r}:no-Z3-mover")
            continue
        span = set()
        for v in movers:
            span.add(tuple(1 if c else 0 for c in v))
        # rank of the mover vectors
        import numpy as np
        rk = np.linalg.matrix_rank(np.array(movers, dtype=float))
        kinds.append(f"{r}:rank{rk}")
    mob[n] = tuple(sorted(kinds)) if kinds else ("all-immobile-on-a-torus",)
rec = {}
for line in open("r4_recert.txt"):
    if not line[0].isdigit():
        continue
    n = int(line.split()[0])
    cert = re.search(r"cert=(\S+)", line).group(1)
    kn = float(re.search(r"k16/N=([0-9.]+)", line).group(1))
    rec[n] = (cert, kn)
tab = collections.Counter(); ex = collections.defaultdict(list); kmax = collections.defaultdict(float)
for n, kinds in mob.items():
    cert, kn = rec[n]
    pur = "IMPURE(6/7^3 cert)" if cert != "-" else "no cert"
    tab[(kinds, pur)] += 1; ex[(kinds, pur)].append(n); kmax[(kinds, pur)] = max(kmax[(kinds, pur)], kn)
for k, v in sorted(tab.items(), key=lambda t: (t[0][1], -t[1])):
    print(f"{v:4d}  {k[1]:>18}  {' '.join(k[0]):<40} max k16/N={kmax[k]:.3f}  e.g. #{ex[k][:3]}")
