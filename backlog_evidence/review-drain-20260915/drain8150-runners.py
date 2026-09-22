from pathlib import Path
import json,re,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';paths=json.loads((R/'drain8150-author-live-paths.json').read_text());names=json.loads((R/'drain8150-new-names.json').read_text())
for i,tag in enumerate(['rate','unit','flip']):
 p=W/paths[2*i+1];s=p.read_text();s=s.replace(paths[2*i],'docs/'+names[i]).replace(Path(paths[2*i]).stem.lower(),Path(names[i]).stem.lower())
 s=re.sub(r'(?s)""".*?"""','"""Exact finite checks of the '+tag+' identities and declared witnesses.\nThe paired note defines the scope; broad negative certification is deferred.\nHistorical runner and mutation basenames remain recovery identifiers.\n"""',s,count=1)
 s=s.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 300')
 fences=[(R/f'drain8150-{tag}-fence.txt').read_text(),'No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The menu, weights and '+{'rate':'clock','unit':'formation','flip':'mixture'}[tag]+' conventions are declared mathematical inputs, not empirical or axiom-selected values.']
 s=re.sub(r'(?s)FENCES = \(.*?\n\)', 'FENCES = '+repr(tuple(fences)),s,count=1)
 s=re.sub(r'(?m)^    "lattice_wide:.*$', '    "lattice_wide: checked and not executed — written conditional identities and sufficient constructions; no infinite-lattice execution; broad negative certification deferred",',s)
 s=re.sub(r'(?m)^    print\("scope:.*$', '    print("scope: '+tag+' identities and declared finite witnesses; broad negative certification deferred; no clause adopted")',s)
 if tag=='unit':
  s=s.replace("the star's center-first, one-leaf-first and leaves-first orders in the all-+x and the mixed environment", "the star's center-first and leaves-first orders in all-+x, and center-first, one-leaf-first and leaves-first in the mixed environment")
  s=s.replace('the star (three orders, two environments)','the star (two all-+x orders and three mixed-environment orders)')
  s=s.replace('three star orders in two environments','two star orders in all-+x and three in the mixed environment')
  s=s.replace('U2 (isolated):','finite isolated comparisons:').replace('U2 (environment):','finite fixed-environment comparisons:')
 if tag=='flip':s=s.replace('X2 (only if):','X2 finite samples:')
 ast.parse(s);p.write_text(s)
