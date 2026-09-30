import re, time
import gadget_dfs2 as g
rules=[]
for line in open("gadget_3d.txt"):
    m=re.match(r"3 A= (\d+) NOGADGET",line)
    if m: rules.append(tuple(int(c) for c in m.group(1)))
print(len(rules),"3D rules, 0 in A, no gadget at <=18 sites", flush=True)
for A in rules:
    t0=time.time()
    good,lv,unk,cp=g.find((3,3,3),A,cap=20000)
    print("A=","".join(map(str,A)),"3x3x3: good",len(good),"leaves",lv,"unknown",unk,"capped",cp,f"{time.time()-t0:.0f}s",flush=True)
