from pathlib import Path
import subprocess,json,hashlib,ast
r=Path(__file__).resolve().parent;w=r/'author-draft-slot'
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
old=git('rev-parse','HEAD');new=git('rev-parse','origin/main');landing=json.loads((r/'train68-landing.json').read_text());assert landing['landing_state']=='LANDED';subprocess.run(['git','-C',str(w),'merge-base','--is-ancestor',landing['candidate_commit'],new],check=True)
assert not git('diff','--name-only') and not git('diff','--cached','--name-only')
paths=git('ls-files','--others','--exclude-standard').splitlines();hashes={p:hashlib.sha256((w/p).read_bytes()).hexdigest() for p in paths};changed=git('diff','--name-only',old,new).splitlines();assert not set(paths)&set(changed)
subprocess.run(['git','-C',str(w),'merge','--ff-only',new],check=True,stdout=subprocess.DEVNULL)
assert all(hashlib.sha256((w/p).read_bytes()).hexdigest()==h for p,h in hashes.items())
(r/'drain8026-parent-base-advance-v1.json').write_text(json.dumps({'old':old,'new':new,'owned_addition_hashes':hashes,'intervening_paths':changed,'source_bytes_preserved':True},indent=2)+'\n')
claim='gauge_wilson_spatial_loop_area_suppression_bounded_theorem_note_2026-09-07';helper='scripts/gauge_wilson_spatial_loop_area_coefficients_check_2026_09_07.py'
for path in ['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py']:
 p=w/path;s=p.read_text();marker='EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {';assert s.count(marker)==1 and claim not in s
 before=ast.parse(s);mapping=lambda tree:next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for t in n.targets))
 prior=mapping(before);assert 'gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07' in prior
 s=s.replace(marker,marker+'\n    '+repr(claim)+': ['+repr(helper)+'],',1);after=mapping(ast.parse(s));assert after==dict(prior,**{claim:[helper]});p.write_text(s);paths.append(path)
subprocess.run(['python3','scripts/vocab_lint.py','--fix',*paths],cwd=w,check=True)
for p in paths:
 if p.endswith('.py'):compile((w/p).read_text(),p,'exec')
subprocess.run(['git','-C',str(w),'add','--',*paths],check=True)
subprocess.run(['git','-C',str(w),'diff','--cached','--check'],check=True)
print('staged',len(paths),'paths at',git('rev-parse','HEAD'))
