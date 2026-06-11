import time, numpy as np
from scipy.linalg import expm
import importlib.util
spec = importlib.util.spec_from_file_location("draft", "/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py")
# we can't import (it runs at module level). Re-define minimal copies by exec of function defs only.
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
# cut off at the "# ===" Part 1 banner so only defs+constants run
head = src.split("# ===========================================================================\nprint")[0]
ns = {}
exec(head, ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]

t=time.time(); env3=ns["build"](3); print("build L=3", round(time.time()-t,2),"s  DIM",env3["DIM"])
t=time.time(); most3,rows3,sv3=ns["scan"](env3,4242,11,5); print("scan L=3 depth11", round(time.time()-t,2),"s")
g3,Th3,w3=rows3[9]
print("L=3 4242 d9: global %.3f  p2/p3/p4 %.3f/%.3f/%.3f  null %.3f"%(g3,
   ns["prefix"](Th3,w3,2),ns["prefix"](Th3,w3,3),ns["prefix"](Th3,w3,4),ns["null_p95"](Th3,w3,3)))
