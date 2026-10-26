import time,sympy as sp
src=open('check.py').read()
a=src.index("def chain_matrices"); b=src.index("# P6")
pre='import sympy as sp\nPASS=FAIL=0\ndef chk(n,c,note=""):\n    print("PASS" if c else "FAIL",n)\n'
t=time.time()
exec(pre+src[a:b].replace("Nn = 4","Nn = 3"))
print('time',time.time()-t)
