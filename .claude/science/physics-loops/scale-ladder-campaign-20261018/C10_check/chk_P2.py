# own simple forward-difference point (L=5): phi=(0,1,0,0,0), pi=(1,2,0,0,0), u+=u-=0; Pi+- on shell
import sympy as sp, importlib.util, sys
sys.argv=['x']
exec(open('chk_P.py').read().split("d1, d2 = sp.symbols")[0])
L=5; M=make(L,{1:1,0:-1})
vals={s:0 for s in list(M["u"])+list(M["v"])}
vals.update({M["f"][x]:[0,1,0,0,0][x] for x in range(L)}); vals.update({M["p"][x]:[1,2,0,0,0][x] for x in range(L)})
av=[sp.sympify(t).subs(vals) for t in M["a"]]; bv=[sp.sympify(t).subs(vals) for t in M["b"]]
vals.update({M["Pi"][x]:-av[x]**2/4 for x in range(L)}); vals.update({M["Pv"][x]:bv[x]**2/4 for x in range(L)})
H=[M["Cp"][x]-M["Cm"][x] for x in range(L)]
hb=M["pb"](H[0],H[1]).subs(vals)
on=all(c.subs(vals)==0 for c in M["Cp"]+M["Cm"])
print(f"[{'PASS' if (on and hb!=0) else 'FAIL'}] P-point L=5 forward own point phi=(0,1,0,0,0), pi=(1,2,0,0,0), u=0: on Sigma={on}, {{H_0,H_1}} = {hb}")
