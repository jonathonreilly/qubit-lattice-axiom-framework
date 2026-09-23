from pathlib import Path
import json,ast,hashlib,difflib,subprocess,sys,re
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';d=json.loads((R/'drain8159-author-canonical-draft-v1.json').read_text());plan=json.loads((R/'drain8159-author-ownership-plan-v2.json').read_text());spec={
1:('finite move rates, detailed balance and source identities','finite cube carrier and curvature fixtures','finite source directions only; no spectral limit execution'),
2:('finite cochain, signed phase, partition and derivative fixtures','finite source-support configurations only','finite matrix/operator directions; no all-order or infinite-kernel execution'),
3:('exact finite alphabet and matrix-record identities','finite partial-record and order fixtures','not executed: no spectral or Fourier calculation is claimed'),
4:('cubic cochain symbols and Gaussian derivative registers','finite support/grid fixtures','finite Fourier grids and finite register degrees; no infinite-lattice execution'),
5:('finite M2 algebra actions and support witnesses','not executed: matrix-profile fixtures are not a spatial lattice','not executed: symbolic matrix support tests, not a spectral field'),
6:('cochain, filling and positive auxiliary source identities','actual finite cube configurations','finite image sums, quadrature and planar Fourier discretizations'),
7:('native gate and signed-hop identities','explicit finite edge-bit configurations','finite spectral moment and escape diagnostics, not an infinite dispersion'),
8:('signed polarization increments and winding identities','finite native winding configurations','finite twist/curvature controls, not thermodynamic stiffness'),
9:('word/native-hop and radial identities','finite polarized words and edge configurations','finite truncated word spectra and radial moments'),
10:('shared native-hop definitions and local-source identities','finite polarized word fixtures','finite source spectral and response fixtures; support-dependent bounds remain analytical'),
11:('quartet gamma/metric and polarization identities','not executed: continuum matrix and quadrature fixtures','finite angular/matrix quadrature, not a constructed interacting phase'),
12:('charged Gauss and electric cutoff identities','finite charged loop and four-edge plaquette','finite cutoff spectra and finite-time matrix evolution'),
13:('coframe coefficients and constitutive identities','not executed: supplied continuum matrix fixtures','finite rational/angular quadrature and flow solutions'),
14:('leading kinematic and polarization fixtures','not executed: continuum phase-space fixtures','finite angular quadrature and momentum-direction samples'),
15:('native star histories, CAR signs and finite cocycle identities','finite star-support patterns and CAR matrices','diagnostic Bloch values only; no native mixed-resolvent spectrum executed'),
16:('cyclic coercivity, CAR and Gauss identities','finite four-edge charged-cycle configurations','recorded k=1 ground searches and finite thermal spectra only; no untraced three-level credit'),
17:('exact Gauss coordinates and oscillator coefficients','finite one/two-plaquette and charged-cycle fixtures','finite conserved-sector spectra with multiplicities and Fourier refinements; untraced dense ancillary run excluded'),
18:('cyclic jump rates and signed-stencil moments','finite one-link generator fixtures','finite clock-mode spectra and oscillator comparisons in the specified cone'),
19:('six-state Gauss frame and symbolic ladder identities','four-site charged ring only','finite hard-cutoff ring spectra and adverse offset fixture'),
20:('theta/Fourier identities and Hessian controls','finite free-band torus sums only','finite twist/momentum samples; no fluctuating gauge-field integration'),
21:('integer cycle/harmonic metric or local matrix identities','finite periodic cycle coordinates and two-coordinate fixture','finite sparse slow spectra and cutoff refinement, not cubic interacting phase'),
22:('curl covariance and probe identities','finite curl matrices and two-coordinate fixture','finite sparse probe spectra and matrix evolution; iterated theorem not executed'),
23:('positive-weight cone identities','finite periodic curl fixtures','finite Bloch derivatives and weighted polarization checks'),
24:('charged f-sum and Ward identities','finite charged-ring configurations','finite matrix spectral/response controls; no pole or phase inference'),
25:('same-source overlap and reducing-carrier identities','finite word fixtures only','finite truncated threshold comparisons; no generic edge exponent')}
patch=[]
for x in plan['active_evidence_programs']:
 p=W/x['canonical_runner'];old=p.read_text();s=old;a,b,c=spec[x['owner']]
 s=s.replace('per_element: only the literal finite algebraic/numerical elements in this companion were executed','per_element: '+a).replace('per_site: only the explicitly enumerated finite configurations; no additional spatial domain checked','per_site: '+b).replace('per_mode: only the finite spectral/Fourier fixtures in this companion; no uniform-mode execution claim','per_mode: '+c)
 ast.parse(s);p.write_text(s);patch.extend(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=x['canonical_runner']+' v1',tofile=x['canonical_runner']+' v2'))
# Freeze new receipts without changing the originals.
for e in d['files']:e['sha256']=hashlib.sha256((W/e['path']).read_bytes()).hexdigest()
d['status']='AUTHOR PREPARATION; EARLY AFFECTED REVIEW REQUESTED, NOT FINAL COLD ACCEPTANCE';d['predecessor']='drain8159-author-canonical-draft-v1.json';d['refinement']='Resolution classes tied to actual owned fixtures; no scientific arithmetic/domain/tolerance changes.'
(R/'drain8159-author-canonical-draft-v2.json').write_text(json.dumps(d,indent=2)+'\n');(R/'drain8159-author-resolution-corrections-v2.patch').write_text(''.join(patch))
# Actual API is read-only. No imports of primary sources.
sys.dont_write_bytecode=True;sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')];import runner_cache as cache,build_citation_graph as graph
api=[]
for x in plan['active_evidence_programs']:
 p=x['canonical_runner'];s=(W/p).read_text();tree=ast.parse(s);compile(tree,p,'exec');ins=list(cache.declared_input_paths(W/p));assert all((W/q).exists() for q in ins)
 assert s.index('AUDIT_INPUT_PATHS =')<s.index('_INPUT_TEXT =')
 for z in ast.walk(tree):
  if isinstance(z,ast.Assert) and isinstance(z.test,ast.Compare) and isinstance(z.test.left,ast.Constant) and isinstance(z.test.left.value,str) and isinstance(z.test.comparators[0],ast.Subscript):
   q=z.test.comparators[0]
   if isinstance(q.value,ast.Name) and q.value.id=='_INPUT_TEXT':assert z.test.left.value in (W/ast.literal_eval(q.slice)).read_text()
 api.append({'runner':p,'timeout':cache.declared_timeout_for(W/p),'declared_inputs':ins,'proposed_transitive_helpers':x['transitive_helpers'],'json_output':'logs/runner-cache/'+Path(p).stem+'.json','no_execution':True})
# Resolve full planned transitive input closure independently of not-yet-edited registries.
by={x['runner']:x for x in api}
for x in api:
 closure=set(x['declared_inputs'])
 for h in x['proposed_transitive_helpers']:closure.add(h);closure.update(by[h]['declared_inputs'])
 x['runtime_closure']=[{'path':p,'sha256':hashlib.sha256((W/p).read_bytes()).hexdigest()} for p in sorted(closure)]
notes=[]
for p in d['notes']:
 cites=[str(q.relative_to(W)) for q in graph.extract_citations((W/p).read_text(),W/p)];notes.append({'path':p,'actual_citations':cites})
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only','HEAD']);assert not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'])
(R/'drain8159-author-input-discovery-v2.json').write_text(json.dumps({'programs':api,'notes':notes,'status':'Prestage actual declarations verified; future nine additive registry entries and dual API equality still required before cold freeze'},indent=2)+'\n')
print('41 compile/input checks; no primary executions; draft v2 frozen')
