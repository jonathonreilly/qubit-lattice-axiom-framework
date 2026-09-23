"""Compare every stored H2/H4 entry using independent electric-tuple sectors."""
from pathlib import Path
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
sys.path.insert(0,str(BASE/'finite_formation_independent'))
from finite_control import model,npmat
import numpy as np
data=json.loads((BASE/'FAST_MATTER_FORMATION_RESULTS.json').read_text())
rows=[]
for source in data['coefficients']:
    name=source['model']
    if name=='star_4':m=model(5,{0},[(0,1),(0,2),(0,3),(0,4)])
    elif name=='two_A_path':m=model(4,{0,2},[(0,1),(2,1),(2,3)])
    else:m=model(4,{0,2},[(0,1),(1,2),(2,3),(3,0)],int(name[-1]))
    # Author orders by site-charge word then circulation; no author code imported.
    p=sorted([i for i,w in enumerate(m['Ws']) if w==0],key=lambda i:(m['states'][i][1],m['states'][i][0][0]))
    q1=[i for i,w in enumerate(m['Ws']) if w==1];q2=[i for i,w in enumerate(m['Ws']) if w==2]
    A=m['T'].extract(q1,p);Z=m['T'].extract(q2,q1)*A;M=A.H*A
    h2=-M;h4=M*M-Z.H*Z/2
    e2=float(np.max(abs(npmat(h2)-np.array(source['H2']))));e4=float(np.max(abs(npmat(h4)-np.array(source['H4']))))
    assert len(m['states'])==source['dimension'] and len(p)==source['P_dimension']
    assert e2<2e-13 and e4<2e-13
    rows.append({'model':name,'dimension':len(m['states']),'P_dimension':len(p),'H2_max_entry_difference':e2,'H4_max_entry_difference':e4,'coefficient_entries_compared':2*len(p)**2})
    if name.startswith('ring'):
        control=next(v for v in data['first_event_loop_controls'] if v['model']==name)
        iv=[j for j,i in enumerate(p) if m['Ns'][i]==2]
        fields=[m['states'][p[j]][0][0] for j in iv]
        assert fields==control['loop_fields']
        assert np.max(abs(npmat(h2.extract(iv,iv))-np.array(control['initial_sector_H2'])))<2e-13
        assert np.max(abs(npmat(h4.extract(iv,iv))-np.array(control['initial_sector_H4'])))<2e-13
        C=int(name[-1])*(int(name[-1])+1)
        loss=np.diag([8*.7*(1-f*f/C)**2 for f in fields])
        assert np.max(abs(loss-np.array(control['initial_sector_birth_loss'])))<2e-13
out={'method':'Independent physical-sector enumeration and exact rational/algebraic coefficients, with explicit author basis ordering; no author-builder imports.','rows':rows,'all_stored_cyclic_H2_H4_and_first_losses_match':True}
(HERE/'COEFFICIENT_EVIDENCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
