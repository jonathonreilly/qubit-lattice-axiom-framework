import sys, os, json, subprocess, time, pickle, resource
tree, outjson, cap = os.path.abspath(sys.argv[1]), sys.argv[2], int(sys.argv[3])
lst = json.load(open("runlist.json"))
res = {}
if os.path.exists(outjson): res = json.load(open(outjson))
for r in lst:
    if r in res: continue
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, "-u", os.path.join(tree, r)], cwd=tree, capture_output=True,
                           env={**os.environ, "PYTHONPATH": os.path.join(tree, "scripts")}, timeout=cap)
        out = p.stdout.decode("utf-8","replace") + p.stderr.decode("utf-8","replace"); rc = p.returncode; st = "ok" if rc == 0 else "nonzero_exit"
    except subprocess.TimeoutExpired as e:
        out = ""; rc = None; st = "timeout"
    res[r] = dict(status=st, rc=rc, elapsed=round(time.time() - t0, 2), stdout=out[-20000:], maxrss=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    json.dump(res, open(outjson, "w"))
print("done", len(res))
