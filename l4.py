import sys, time, numpy as np
src = open("/tmp/scale-wt/scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py").read()
head = src.split("# ===========================================================================\nprint")[0]
ns = {}; exec(head, ns)
build, scan, prefix, null_p95 = ns["build"], ns["scan"], ns["prefix"], ns["null_p95"]
t=time.time(); env4=build(4); print("build L=4 DIM",env4["DIM"]," in",round(time.time()-t,1),"s",flush=True)
seed=int(sys.argv[1]); depth=int(sys.argv[2])
t=time.time()
most,rows,sv4=scan(env4,seed,depth,7)
n,g1,Th,w=most
p2,p3,p4=prefix(Th,w,2),prefix(Th,w,3),prefix(Th,w,4)
nl=null_p95(Th,w,3)
print("L=4 seed %d depth(most) %d: global %.3f  p2/p3/p4 %.3f/%.3f/%.3f  null %.3f  gap %+.3f  mono=%s  (%.0fs, sv %.4f)"%(
    seed,n,g1,p2,p3,p4,nl,p3-nl,(p2<p3<p4),time.time()-t,sv4),flush=True)
