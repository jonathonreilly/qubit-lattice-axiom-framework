import numpy as np
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
head = src.split("# ===========================================================================\nprint")[0]
ns = {}; exec(head, ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]
env3=build(3)
# seed 99 d7 event
most,rows,sv=scan(env3,99,11,5)
g,Th,w=rows[7]
p3=prefix(Th,w,3)
print("L=3 seed99 d7: prefix-3 = %.3f ; null p95 over varied null-seeds & draw counts:"%p3)
for nd in (300,1000):
  for ns_ in (7777, 1, 2, 12345):
    nl=null_p95(Th,w,3,n_draws=nd,seed=ns_)
    print("   draws=%4d null-seed=%5d -> p95 %.3f  gap %+.3f"%(nd,ns_,nl,p3-nl))
