"""A33 a11: tally r4_stage3.txt (P2-A r2<=4 survivors of the one-site filter)."""
import re, collections, ast
c = collections.Counter(); mob10 = collections.Counter(); keys = collections.defaultdict(list)
for line in open("r4_stage3.txt"):
    n = int(line.split()[0])
    if "cert=3" in line:
        c["impure: 3^3-box certificate"] += 1; continue
    L = int(re.search(r"mobL=(\d+)", line).group(1))
    m = ast.literal_eval(re.search(r"mob=(\{[^}]*\})", line).group(1))
    if not any(m.values()):
        c[f"immobile on L={L} (exact on Z^3)"] += 1; continue
    cert5 = re.search(r"cert5=(\S+)", line).group(1)
    sig = tuple(sorted((r, v) for r, v in m.items() if v))
    mob10[(cert5, sig)] += 1
    keys[(cert5, sig)].append(n)
    c[f"mobile on L=6,8,10, 5^3 cert={cert5}"] += 1
for k, v in sorted(c.items()):
    print(f"  {k}: {v}")
print("  mobile-on-L10 signatures (cert5, moves per role on L=10; 24 = in-plane, 124 = all same-role sites):")
for k, v in sorted(mob10.items(), key=lambda t: -t[1]):
    print(f"     {k}: {v}   e.g. #{keys[k][:4]}")
