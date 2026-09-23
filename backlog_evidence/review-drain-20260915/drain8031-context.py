import subprocess,pathlib,json,hashlib
r='/private/tmp/review-drain-20260915/integration-resume';o=pathlib.Path('/private/tmp/review-drain-20260915/drain8031-context');o.mkdir(exist_ok=True); rev='631d6b36cd1e9b860763ebcad36e40a2bbe7439c'
paths=['docs/repo/'+n+'.md' for n in ['REVIEW_FEEDBACK_WORKFLOW','ACTIVE_REVIEW_QUEUE','DEFERRED_DECISIONS','CONTROLLED_VOCABULARY']]+['docs/CANONICAL_HARNESS_INDEX.md','docs/audit/README.md','docs/audit/data/premise_decision_history.json']+['docs/'+n+'_BOUNDED_THEOREM_NOTE_2026-09-07.md' for n in ['GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF','GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT','GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS']]
rows=[]
for p in paths:
 b=subprocess.check_output(['git','-C',r,'show',rev+':'+p]);f=o/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b);rows.append(dict(path=p,revision=rev,sha256=hashlib.sha256(b).hexdigest(),blob=subprocess.check_output(['git','-C',r,'rev-parse',rev+':'+p]).decode().strip()))
(o/'manifest.json').write_text(json.dumps(rows,indent=2))
