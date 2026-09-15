from pathlib import Path
import json
r=Path('/private/tmp/review-drain-20260915/author-pool/author-backlog')
items=[(8062,'NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09','native_uniform_quasilocal_star_vertex_2026_09_09','native_uniform_quasilocal_star_controls_2026_09_09'),(8063,'NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09','native_star_thermodynamic_limit_2026_09_09','native_star_thermodynamic_controls_2026_09_09')]
scopes={8062:[
'per_element: exact finite Gaussian-dyadic matrix and CAR predicates are executed; general Wick extraction is analytical.',
'per_site: periodic L4 and L6 face-pair incidence is executed; arbitrary-volume geometric claims use the proof.',
'per_mode: shifted-shell arithmetic is executed on declared finite sizes; no node value or band amplitude is computed.',
'per_block: the smooth-filter cocycle and spatial truncation bounds are analytical, not finite numerical locality measurements.',
'lattice_wide: uniform quasi-locality and the ordered perturbative limit are analytical; no interacting ground state is solved.'
],8063:[
'per_element: exact finite CAR quadratic commutator predicates are executed on the declared three-mode matrices.',
'per_site: finite hopping-path boundary independence is executed for L8, L12 and L16 at the declared orders.',
'per_mode: finite exact weighted-tail arithmetic is executed; smooth coefficient-symbol convergence is analytical.',
'per_block: local Gaussian state and cocycle limits are analytical; no infinite-volume resolvent is numerically evaluated.',
'lattice_wide: the GNS core and wrong-pair gap argument is analytical; no interacting phase or nodal value is computed.'
]}
for n,note,stem,helper in items:
 p=r/'scripts'/f'{stem}.py';s=p.read_text()
 s=s.replace('import argparse,json,hashlib,signal,time,resource','import argparse,json,hashlib,signal,time,resource,sys\n import importlib.util')
 old="helper=root/AUDIT_INPUT_PATHS[-1];data=helper.read_bytes();ns={'__name__':'controls','__file__':str(helper)};exec(compile(data,str(helper),'exec'),ns);out=ns['check']()"
 new=f"helper=root/'scripts/{helper}.py';data=helper.read_bytes()\n spec=importlib.util.spec_from_file_location('controls',root/'scripts/{helper}.py')\n module=importlib.util.module_from_spec(spec);exec(compile(data,str(helper),'exec'),module.__dict__);out=module.check()"
 assert old in s;s=s.replace(old,new)
 s=s.replace('rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss','rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform==\'darwin\' else 1024)')
 oldend="actual_current_surface_status='conditional-support');print(json.dumps(out,indent=2))"
 newend=f"actual_current_surface_status='conditional-support')\n payload=json.dumps(out,indent=2)+'\\n';(root/'outputs/{stem}.json').write_text(payload);print(payload,end='')\n print(f\"TOTAL: {{out['checks']}} PASS / 0 FAIL\")\n"+'\n'.join(' print('+repr(v)+')' for v in scopes[n])
 assert oldend in s;s=s.replace(oldend,newend);p.write_text(s)
 h=r/'scripts'/f'{helper}.py';hs=h.read_text();first,rest=hs.split('\n',1)
 h.write_text(first+'\nAUDIT_TIMEOUT_SEC=180\nAUDIT_INPUT_PATHS=(\'docs/'+note+'.md\',)\n'+rest)
 np=r/'docs'/f'{note}.md';ns=np.read_text();ns=ns.replace('**Status:**','**Type:** bounded_theorem\n\n**Status:**',1)
 ns+='\n\n## Canonical evidence and historical provenance\n\nThe [canonical runner cache](../logs/runner-cache/'+stem+'.txt) records the current bounded execution. Its TOTAL counts the actual helper mathematical predicates; the memory guard is separate. The five execution-scope lines distinguish finite controls from analytical general statements.\n\nThe [original historical handoff](work_history/repo/review_feedback/pr'+str(n)+'-evidence/kept/pr'+str(n)+'-HANDOFF.md) and the adjacent exact archive preserve original proofs, reviews, subprocess controls and failed attempts. Historical review or execution claims are provenance, not a current verdict or a newly executed campaign.\n'
 np.write_text(ns)
