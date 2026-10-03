"""A33 a14: tally r4_resolve.txt: per candidate, roles still mobile on L=6,8,16 and explicit Z^3 movers."""
import re, collections, ast
cat = collections.Counter(); ex = collections.defaultdict(list)
for line in open("r4_resolve.txt"):
    if not line[0].isdigit():
        continue
    n = int(line.split()[0])
    parts = line.split(" sol=")[1].split("} ", 1)[1].split(" | ")
    sig = []
    for p in parts:
        r, st = p.split(":", 1)
        if st.startswith("imm"):
            continue
        L16 = int(re.search(r"L16:(\d+)", st).group(1))
        mov = ast.literal_eval(re.search(r"Z3movers(\[.*?\])", st).group(1))
        dirs = set()
        for v in mov:
            nz = tuple(i for i in range(3) if v[i])
            dirs.add(nz)
        sig.append(f"{r}(L16={L16}, Z3 movers {'NONE' if not mov else sorted(dirs)})")
    key = "; ".join(sig) if sig else "all roles immobile on some torus"
    cat[key] += 1; ex[key].append(n)
for k, v in sorted(cat.items(), key=lambda t: -t[1]):
    print(f"{v:4d}  {k}   e.g. #{ex[k][:3]}")
