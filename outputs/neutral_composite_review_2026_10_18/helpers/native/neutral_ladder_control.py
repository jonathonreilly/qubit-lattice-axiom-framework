"""Synthetic harmonic and anharmonic ladder controls; not observations."""
from pathlib import Path
import numpy as np,json
omega=1.738972318271891;Z=.003524947756927933;n=np.arange(6)
a=np.diag(np.sqrt(n[1:]),1);C=np.sqrt(Z)*(a+a.T);rows=[]
for kappa in [0,.08]:
 E=omega*n+kappa*n*(n-1)/2
 for width in [.02,.05,.1,.2]:
  weights=C[:,1]**2;up=float(weights@np.exp(-((E-2*omega)/width)**2));down=float(weights@np.exp(-(E/width)**2))
  # Separate Gaussian branch amplitude filters have squared weights exp(-d²/width²).
  predicted=2*Z*np.exp(-(kappa/width)**2)+Z*np.exp(-(2*omega/width)**2)
  assert abs(up-predicted)<1e-14
  if kappa==0:assert abs(up/(2*Z)-1)<1e-12 and abs(down/Z-1)<1e-12
  rows.append(dict(kappa=kappa,width=width,upper_over_2Z=up/(2*Z),lower_over_Z=down/Z))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(rows=rows,scope='Synthetic controls. Ratios target1 for harmonic oscillator; shifted ladder can fail narrow windows without excluding an interacting scalar.'),indent=2)+'\n');print(rows)
