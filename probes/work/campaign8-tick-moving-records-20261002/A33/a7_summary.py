"""A33 a7: tally a classification file.  usage: python3 a7_summary.py p2a_class_r2.txt"""
import sys, ast, re, collections
rows = []
for line in open(sys.argv[1]):
    m = re.match(r"(\d+) ti=(\d) sol=(\{.*?\}) mob4=(\{.*?\}) mob6=(\{.*?\}) mob8=(\{.*?\}) cert=(\S+) CB=(\d+) SB=(\d+) k=\((\d+),(\d+),(\d+)\)", line)
    n, ti, sol, m4, m6, m8, cert, CB, SB, k4, k6, k8 = m.groups()
    rows.append(dict(n=int(n), ti=int(ti), sol=ast.literal_eval(sol), m4=ast.literal_eval(m4),
                     m6=ast.literal_eval(m6), m8=ast.literal_eval(m8), cert=cert, CB=int(CB), SB=int(SB),
                     k=(int(k4), int(k6), int(k8))))
tab = collections.Counter()
for r in rows:
    pure = "impure(cert)" if r["cert"] != "-" else ("pure-looking" if r["CB"] == r["SB"] else "undetermined")
    mob = "mobile(L4,6,8)" if any(r["m8"].values()) else ("L4-only" if any(r["m4"].values()) else "immobile(L4)")
    tab[(pure, mob)] += 1
print(f"{sys.argv[1]}: {len(rows)} candidates")
for k, v in sorted(tab.items()):
    print(f"   {k[0]:>13} | {k[1]:>15} : {v}")
pure_rows = [r for r in rows if r["cert"] == "-" and r["CB"] == r["SB"]]
print("   pure-looking: translation-invariant among them:", sum(r["ti"] for r in pure_rows))
print("   pure-looking k(L) values (L=4,6,8):", sorted(collections.Counter(r["k"] for r in pure_rows).items())[:12])
mob_pure = [r["n"] for r in pure_rows if any(r["m8"].values())]
print("   pure-looking AND mobile single defect on L=8:", mob_pure)
