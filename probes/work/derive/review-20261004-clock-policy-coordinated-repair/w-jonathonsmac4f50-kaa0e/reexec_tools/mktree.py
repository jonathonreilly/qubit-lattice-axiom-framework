import subprocess, os, sys
M="/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt"; O="3e1a2dd2531590dabf85bee8db56175ba9b96e90"
dest=sys.argv[1]
ls=subprocess.run(["git","-C",M,"ls-tree","-r",O],capture_output=True).stdout.decode().strip().split("\n")
ent={}
for l in ls:
    meta,p=l.split("\t",1); mode,typ,sha=meta.split(); ent[p]=(mode,sha)
inputs=set(open("inputs.txt").read().split("\n"))
want=[p for p in ent if p.startswith("scripts/") or p.startswith("docs/audit/") or p in inputs]
missing=[p for p in inputs if p not in ent]; print("missing inputs",len(missing),missing[:5])
inp="".join(ent[p][1]+"\n" for p in want).encode()
out=subprocess.run(["git","-C",M,"cat-file","--batch"],input=inp,capture_output=True).stdout
i=0; n_files=0; tot=0
for p in want:
    j=out.index(b"\n",i); n=int(out[i:j].split()[2]); body=out[j+1:j+1+n]; i=j+1+n+1
    if ent[p][0]=="120000": continue
    fp=os.path.join(dest,p); os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,"wb").write(body); n_files+=1; tot+=n
print(n_files,tot)
