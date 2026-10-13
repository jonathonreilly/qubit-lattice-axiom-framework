from pathlib import Path
import importlib.util,json,sys
p=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("negative_mutant",p/"check_analytic_fluid_v1.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
rows=m.off_trajectory_controls()
out={"scope":"Negative sensitivity only; not independent positive evidence", "rows":rows,"checks":m.CHECKS,"passed":sum(c["passed"] for c in m.CHECKS),"failed":sum(not c["passed"] for c in m.CHECKS)}
(p/"RESULTS.json").write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
print(json.dumps({"passed":out["passed"],"failed":out["failed"]},sort_keys=True))
raise SystemExit(int(out["failed"]>0))
