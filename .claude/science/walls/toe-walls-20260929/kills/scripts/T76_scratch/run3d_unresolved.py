import re, sys, time
import gadget_dfs as g
rules=[]
for line in open("gadget_3d.txt"):
    m=re.match(r"3 A= (\d+) NOGADGET",line)
    if m: rules.append(tuple(int(c) for c in m.group(1)))
print(len(rules),"3D rules with 0 in A and no gadget at <=18 sites")
res={}
for A in rules:
    found=None; status=[]
    for sh in [(3,3,3),(2,3,4),(3,3,4),(2,4,4),(3,4,4)]:
        t0=time.time()
        good,lv,cp=g.find(sh,A,cap=150000)
        status.append((sh,len(good),lv,cp))
        if len(good)>=2: found=sh; break
    res[A]=(found,status[-1])
    print("A=","".join(map(str,A)),"GADGET" if found else "none",found if found else status, flush=True)
