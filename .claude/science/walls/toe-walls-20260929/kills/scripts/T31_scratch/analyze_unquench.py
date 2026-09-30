import json, glob, math
Mpl = 1.2209e19; ab = 1/(4*math.pi); fac = (7/8)**0.25
def v_of(P): return Mpl*fac*(ab/P**0.25)**16
Pq = None; rows = []
for fn in sorted(glob.glob("res_Ns*_s*.json")):
    if fn.endswith("_s11.json") or fn.endswith("_s21.json"):
        continue  # debugging / timing runs, not in runs.txt
    r = json.load(open(fn)); rows.append(r)
q = [r for r in rows if r["Ns"] == 0][0]
Pq, Eq = q["P_mean"], q["P_err_jack10"]
print(f"quenched L=4 beta=6: P={Pq:.5f} +/- {Eq:.5f}  ({q['ntraj']} traj, tau_int={q['tau_int']:.1f}, acc={q['acc']:.2f})   [repo smoke 0.59601 +/- 0.00078]")
print(f"licensed P=0.5934 -> v = {v_of(0.5934):.3f} GeV  (obs 246.22: {100*(v_of(0.5934)/246.22-1):+.3f}%)")
print("\nNs (tastes)  m     P_dyn(L=4)       dP=P_dyn-Pq     tau  acc   |dH|  ntraj   v with P=0.5934+dP (GeV)   vs 246.22")
out = []
for r in sorted(rows, key=lambda r: (r["Ns"], r["m"])):
    if r["Ns"] == 0: continue
    dP = r["P_mean"] - Pq; err = math.hypot(r["P_err_jack10"], Eq)
    P_est = 0.5934 + dP
    v = v_of(P_est)
    print(f"{r['Ns']} ({4*r['Ns']:2d})     {r['m']:<5} {r['P_mean']:.5f}+/-{r['P_err_jack10']:.5f}  {dP:+.4f}+/-{err:.4f}  {r['tau_int']:4.1f}  {r['acc']:.2f}  {r['mean_abs_dH']:.2f}  {r['ntraj']:4d}   {v:8.1f}                {100*(v/246.22-1):+.1f}%")
    out.append(dict(Ns=r["Ns"], tastes=4*r["Ns"], m=r["m"], P=r["P_mean"], P_err=r["P_err_jack10"], dP=dP, dP_err=err, v_GeV=v, tau=r["tau_int"], acc=r["acc"], ntraj=r["ntraj"]))
json.dump(dict(Pq=Pq, Pq_err=Eq, rows=out), open("unquench_summary.json", "w"), indent=1)
