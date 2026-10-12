"""K1: basis-free size of the generated non-gauge-invariant kinetic space.
Rank (mod EH) of the family {fermion c_K(m), m = 0.1..0.5} U {photon c_K}, and of the masses {cMnet}.
Singular values reported in the O(4)-orthonormal metric of the quotient (EH projected out by least squares).  Usage: python span_check.py
"""
import numpy as np, json, glob
EH = np.array([1, -2, 2, -1, 0, 0, 0, 0, 0]) / 4.0
vecs = []; mvecs = []; labels = []
for f in sorted(glob.glob("loop_fermion_m*.json")):
    d = json.load(open(f)); L = str(max(int(k) for k in d if k.isdigit()))
    vecs.append(np.array(d[L]["cK"]) / 4); mvecs.append(np.array(d[L]["cMnet"]) / 4); labels.append(f)
dp = json.load(open("loop_photon.json")); Lp = str(max(int(k) for k in dp))
vecs.append(np.array(dp[Lp]["cK"])); mvecs.append(np.array(dp[Lp]["cM"])); labels.append("photon")
V = np.array(vecs)
P = np.eye(9) - np.outer(EH, EH) / (EH @ EH)       # remove EH component
s = np.linalg.svd(V @ P, compute_uv=False)
print("family:", labels)
print("kinetic (mod EH) singular values:", " ".join(f"{x:.2e}" for x in s))
print("fermion-only (mod EH):", " ".join(f"{x:.2e}" for x in np.linalg.svd(V[:-1] @ P, compute_uv=False)))
print("masses singular values:", " ".join(f"{x:.2e}" for x in np.linalg.svd(np.array(mvecs), compute_uv=False)))
