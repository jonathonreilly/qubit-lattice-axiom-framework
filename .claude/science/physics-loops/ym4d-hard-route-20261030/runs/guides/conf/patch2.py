import sys
p=sys.argv[1]
s=open(p).read()
a="""This is antiscreening. At weak coupling kappa = (1/4) g^2(2L)/g^2(L) > 1/4 by
asymptotic freedom (the vacuum is a colour paramagnet: Nielsen 1981, Hughes
1981)."""
b="""This is antiscreening. ARGUED: at weak coupling z_e grows like a positive
power of g^2(L) (Luscher's small-volume value is g^(2/3)), so 4 kappa exceeds
1 by an amount of order g^2(L), by asymptotic freedom (the vacuum is a colour
paramagnet: Nielsen 1981, Hughes 1981). The exact power is not needed here."""
assert s.count(a)==1
s=s.replace(a,b)
open(p,'w').write(s)
print("ok")
