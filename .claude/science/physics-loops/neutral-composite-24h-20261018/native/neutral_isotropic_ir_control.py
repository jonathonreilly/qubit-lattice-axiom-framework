import mpmath as m,json
m.mp.dps=60
rows=[]
for k in [m.mpf('.8'),m.mpf('.4'),m.mpf('.2'),m.mpf('.1')]:
 F=lambda q:4*m.pi*(m.sin(q*k)-q*k*m.cos(q*k))/q**3
 integral=4*m.pi*k**3/3+F(2)-2*F(m.sqrt(2))
 density=2*integral/(2*m.pi)**3;lead=k**7/(105*m.pi**2)
 rows.append(dict(kappa=float(k),norm2_over_J2N=float(density),leading=float(lead),ratio=float(density/lead)))
assert abs(rows[-1]['ratio']-1)<.002
print(json.dumps(dict(rows=rows,scope='Continuum Fourier integral of exact initial spin-pair form factor, not an invariant mode spectrum'),indent=2))
