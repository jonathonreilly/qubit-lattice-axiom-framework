"""Adversarial schema-3 checks against real Git/discovery/cache APIs."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
import test_review_receipt as fixtures
TOOL = fixtures.TOOL


def digest(data):
    return hashlib.sha256(data).hexdigest()


def interval(data, start=0, end=None):
    end = len(data) if end is None else end
    return {'start': start, 'end': end, 'sha256': digest(data[start:end])}


class SummaryTests(unittest.TestCase):
    write = fixtures.ReceiptTests.write
    git = fixtures.ReceiptTests.git
    hash = fixtures.ReceiptTests.hash
    bind = fixtures.ReceiptTests.bind
    check = fixtures.ReceiptTests.check

    def setUp(self):
        fixtures.ReceiptTests.setUp(self)
        self.write('scripts/primary.py', (self.repo/'scripts/primary.py').read_text() + 'print("fixture execution")\n')
        report=json.loads(Path(self.record['reviewer']['report']['path']).read_text())
        for row in report['original_dispositions']:
            row['final_sha256']=self.hash(row['final_path'])
        addendum=self.home/'fixture-dispositions.json';addendum.write_text(json.dumps(report))
        self.record['constituents'][0]['dispositions']={'path':str(addendum),
            'sha256':digest(addendum.read_bytes()),'json_pointer':'/original_dispositions'}
        self.old = '# Live summary\n\n## Scope\nOld α claim.\n\n## Untouched\nHistory.\n'.encode()
        self.new = self.old.replace(b'Old', b'Conditional')
        self.write('.gitattributes', 'logs/runner-cache/*.txt -whitespace\n')
        self.write('docs/SUMMARY.md', self.old.decode())
        self.git('add', '.')
        self.git('commit', '-qm', 'summary baseline')
        base = self.git('rev-parse', 'HEAD')
        self.write('docs/SUMMARY.md', self.new.decode())
        # Tiny fixture primary executes its own actual helper; no fabricated cache.
        code = ('import sys;sys.path.insert(0,"scripts");import runner_cache as c;'
                'p="scripts/primary.py";i=c.capture_runner_execution_identity(p);'
                'r=c.execute_runner(p,30);assert r["exit_code"]==0;'
                'c.write_cache(p,r,identity=i.content)')
        subprocess.run([sys.executable, '-c', code], cwd=self.repo, check=True,
                       capture_output=True, env={'PYTHONDONTWRITEBYTECODE': '1'})
        cache = 'logs/runner-cache/primary.txt'
        self.git('add', '.')
        self.record.update(schema_version=3, supporting_proofs=[], summary_corrections=[])
        self.record['source'] = {'base':base,'commit':base,'tree':self.git('write-tree'),
                                'paths':self.bind(['docs/SUMMARY.md',cache]),'deleted_paths':[]}
        self.record['inputs']['runtime'] += self.bind(['docs/NOTE.md','scripts/primary.py'])
        self.owner_paths = sorted(['docs/NOTE.md','scripts/primary.py','scripts/helper.py',
                                   'docs/PARENT.md','data/input.txt',cache])
        self.owner = {'decision':'confirmed','path':'docs/NOTE.md','claim_id':'note',
                      'source_sha256':self.hash('docs/NOTE.md'),
                      'scope':'Supplied conditional identity; no physical selector.',
                      'bindings':self.bind(self.owner_paths)}
        self.owner_ref = self.ref('owner.json', self.owner)
        a = self.old.index(b'Old');c=self.new.index(b'Conditional')
        self.edit = {'old':interval(self.old,a,a+3), 'new':interval(self.new,c,c+11),
                     'old_context':interval(self.old,self.old.index(b'## Scope'),self.old.index(b'## Untouched')),
                     'new_context':interval(self.new,self.new.index(b'## Scope'),self.new.index(b'## Untouched')),
                     'canonical_notes':[{'path':'docs/NOTE.md','claim_id':'note',
                                         'scope':self.owner['scope'],'review_reference':self.owner_ref}],
                     'rationale':'Changed assertion reports only the confirmed supplied identity.'}
        self.item = {'path':'docs/SUMMARY.md','base_sha256':digest(self.old),
                     'current_sha256':digest(self.new),'edits':[self.edit]}
        self.confirm()

    def ref(self, name, value):
        p=self.home/name;p.write_text(json.dumps({'confirmation':value}))
        return {'path':str(p),'sha256':digest(p.read_bytes()),'json_pointer':'/confirmation'}

    def confirm(self):
        report={**{k:v for k,v in self.item.items() if k!='review_reference'},
                'decision':'confirmed_derivative','scope_rationale':'Independent scoped entailment judgment; no whole-note approval.'}
        self.item['review_reference']=self.ref('summary.json',report)
        self.record['summary_corrections']=[self.item]

    def invalid(self, contains=None, cache=True):
        code,result=self.check(cache=cache)
        self.assertEqual(code,1,result)
        if contains:self.assertIn(contains,result['error'])

    def test_valid_scoped_output(self):
        code,result=self.check(cache=True);self.assertEqual(code,0,result)
        self.assertEqual(result['summary_corrections'][0]['role'],'scoped_summary_correction')
        self.assertNotIn('docs/SUMMARY.md',[n['path'] for n in result['notes']])
        self.assertNotIn('verdict',result)

    def test_cache_required(self):
        self.invalid('require cache',cache=False)

    def test_downgrades_even_empty(self):
        for version in (1,2):
            self.record['schema_version']=version;self.record['summary_corrections']=[]
            self.invalid('requires receipt schema version 3')

    def test_unknown_new_fields(self):
        for obj in (self.record,self.item,self.edit,self.edit['old'],self.edit['canonical_notes'][0]):
            obj['invented']=True;self.invalid('exact fields');del obj['invented']

    def test_explicit_list_required(self):
        del self.record['summary_corrections'];self.invalid('exact fields')
        self.record['summary_corrections']={};self.invalid('must be explicit')

    def test_stale_base_hash(self):
        self.item['base_sha256']='0'*64;self.confirm();self.invalid('whole-file hash')

    def test_stale_slice_anchor(self):
        self.edit['old']['sha256']='0'*64;self.confirm();self.invalid('slice hash')

    def test_omitted_edit(self):
        self.edit['new']=interval(self.new,self.edit['new']['start'],self.edit['new']['end']-1)
        self.confirm();self.invalid('uncovered trailing')

    def test_overlap_and_duplicate(self):
        self.item['edits'].append(copy.deepcopy(self.edit));self.confirm();self.invalid('overlapping')

    def test_context_must_enclose(self):
        self.edit['old_context']=interval(self.old,0,3);self.confirm();self.invalid('enclosing context')

    def test_split_utf8_zero_width(self):
        n=self.old.index('α'.encode())+1
        self.edit['old']=interval(self.old,n,n);self.confirm();self.invalid('UTF-8')

    def test_unconfirmed_or_held_owner(self):
        self.owner['decision']='held'
        self.edit['canonical_notes'][0]['review_reference']=self.ref('owner-held.json',self.owner)
        self.confirm();self.invalid('held authority')

    def test_owner_inputs_not_just_source_are_confirmed(self):
        self.owner['bindings'][0]['sha256']='0'*64
        self.edit['canonical_notes'][0]['review_reference']=self.ref('owner-stale.json',self.owner)
        self.confirm();self.invalid('confirmation mismatch')

    def test_owner_must_be_normal_not_summary(self):
        self.edit['canonical_notes'][0]['path']='docs/SUMMARY.md';self.confirm();self.invalid('normal canonical note')

    def test_report_mutation(self):
        Path(self.item['review_reference']['path']).write_text('{}');self.invalid('evidence hash changed')

    def test_contradictory_prose_not_confirmed(self):
        self.edit['rationale']='This establishes unconditional physical selection.'
        # Keep the genuinely independent old confirmation; author cannot repin it.
        self.invalid('derivative confirmation mismatch')

    def test_duplicate_role(self):
        self.record['non_science_notes']=[{'path':'docs/SUMMARY.md','rationale':'not science',
            'review_reference':self.record['reviewer']['report']}]
        self.invalid('duplicate summary role')

    def rebind(self):
        self.git('add', '.')
        self.record['source']['tree']=self.git('write-tree')
        changed=self.git('diff','--name-only',self.record['source']['base'],'--cached').splitlines()
        self.record['source']['paths']=self.bind(changed)

    def test_new_metadata_cannot_hide_in_summary(self):
        self.new=b'**Type:** open_gate\n'+self.new
        self.write('docs/SUMMARY.md',self.new.decode());self.rebind()
        self.item['current_sha256']=digest(self.new);self.confirm()
        self.invalid('metadata changed')

    def metadata_fixture(self, old, new):
        # Bind a completely reviewed byte replacement so rejection is specifically
        # the metadata contract, not missing range/report/index/cache evidence.
        self.old, self.new = old, new
        self.write('.gitattributes', 'logs/runner-cache/*.txt -whitespace\ndocs/SUMMARY.md whitespace=cr-at-eol\n')
        (self.repo/'docs/SUMMARY.md').write_bytes(old)
        self.git('add', '.'); self.git('commit', '-qm', 'metadata baseline')
        base = self.git('rev-parse', 'HEAD')
        self.record['source'].update(base=base, commit=base)
        cache = 'logs/runner-cache/primary.txt'
        if cache not in {row['path'] for row in self.record['inputs']['runtime']}:
            self.record['inputs']['runtime'] += self.bind([cache])
        (self.repo/'docs/SUMMARY.md').write_bytes(new); self.rebind()
        self.edit.update(old=interval(old), new=interval(new),
                         old_context=interval(old), new_context=interval(new))
        self.item.update(base_sha256=digest(old), current_sha256=digest(new))
        self.confirm()

    def test_embedded_delimiter_preserves_complete_frontmatter(self):
        for newline in (b'\n', b'\r\n'):
            with self.subTest(newline=newline):
                old = newline.join([b'---', b'title: "a---b"', b'authority: conditional',
                                    b'---', b'# Summary', b'Old claim.', b''])
                self.metadata_fixture(old, old.replace(b'conditional', b'retained'))
                self.invalid('metadata changed')

    def test_unchanged_embedded_delimiter_frontmatter_is_allowed(self):
        for newline in (b'\n', b'\r\n'):
            with self.subTest(newline=newline):
                old = newline.join([b'---', b'title: "a---b"', b'authority: conditional',
                                    b'---', b'# Summary', b'Old claim.', b''])
                self.metadata_fixture(old, old.replace(b'Old claim.', b'Conditional claim.'))
                status, result = self.check(cache=True)
                self.assertEqual(status, 0, result)

    def test_unclosed_frontmatter_rejected(self):
        for newline in (b'\n', b'\r\n'):
            with self.subTest(newline=newline):
                old = newline.join([b'---', b'title: "a---b"', b'authority: conditional', b''])
                self.metadata_fixture(old, old.replace(b'conditional', b'retained'))
                self.invalid('unclosed summary frontmatter')

    def test_explicit_authority_metadata_preserved(self):
        for label in (b'Authority:', b'**Authority:**', b'**Authority**:',
                      b'Status authority:', b'**Status authority:**', b'**Status:**'):
            with self.subTest(label=label):
                old = b'# Summary\n' + label + b' conditional\nOld claim.\n'
                self.metadata_fixture(old, old.replace(b'conditional', b'retained'))
                self.invalid('metadata changed')

    def baseline_reader(self, own=False):
        runner='scripts/summary_reader.py'
        self.write(runner,'AUDIT_TIMEOUT_SEC=30\nAUDIT_INPUT_PATHS=("docs/SUMMARY.md",)\n')
        if own:
            prefix=b'Runner: `scripts/summary_reader.py`\n'
            self.old=prefix+self.old;self.new=prefix+self.new
        else:
            self.write('docs/DOWNSTREAM.md','# Downstream\n**Type:** bounded_theorem\nRunner: `scripts/summary_reader.py`\n')
        self.write('docs/SUMMARY.md',self.old.decode());self.git('add','.');self.git('commit','-qm','reader baseline')
        base=self.git('rev-parse','HEAD');self.record['source']['base']=base;self.record['source']['commit']=base
        self.record['inputs']['runtime']+=self.bind(['logs/runner-cache/primary.txt'])
        self.write('docs/SUMMARY.md',self.new.decode());self.rebind()
        a=self.old.index(b'Old');c=self.new.index(b'Conditional')
        self.edit.update(old=interval(self.old,a,a+3),new=interval(self.new,c,c+11),
                         old_context=interval(self.old),new_context=interval(self.new))
        self.item.update(base_sha256=digest(self.old),current_sha256=digest(self.new));self.confirm()

    def test_unchanged_downstream_input_consumer_still_required(self):
        self.baseline_reader();self.invalid('uncovered changed/runner-affected notes: docs/DOWNSTREAM.md')

    def test_changed_summary_cannot_skip_own_input_affected_inventory(self):
        self.baseline_reader(own=True);self.invalid('runner/input-affected summary')

    def test_existing_metadata_cannot_be_deleted(self):
        self.baseline_reader(own=True)
        self.new=self.new.split(b'\n',1)[1]
        self.write('docs/SUMMARY.md',self.new.decode());self.rebind()
        self.item['current_sha256']=digest(self.new);self.confirm()
        self.invalid('metadata changed')

    def test_circular_owner_input_rejected(self):
        p='scripts/primary.py'
        self.write(p,(self.repo/p).read_text().replace('("data/input.txt",)',
                   '("data/input.txt", "docs/SUMMARY.md")'))
        code=('import sys;sys.path.insert(0,"scripts");import runner_cache as c;'
              'p="scripts/primary.py";i=c.capture_runner_execution_identity(p);'
              'r=c.execute_runner(p,30);c.write_cache(p,r,identity=i.content)')
        subprocess.run([sys.executable,'-c',code],cwd=self.repo,check=True,capture_output=True,
                       env={'PYTHONDONTWRITEBYTECODE':'1'})
        self.record['inputs']['runtime']=self.bind(['data/input.txt','docs/NOTE.md',p])
        self.rebind()
        # New immutable mapping leaves the original review file untouched.
        original=json.loads(Path(self.record['reviewer']['report']['path']).read_text())
        for row in original['original_dispositions']:row['final_sha256']=self.hash(row['final_path'])
        f=self.home/'cycle-dispositions.json';f.write_text(json.dumps(original))
        self.record['constituents'][0]['dispositions']={'path':str(f),'sha256':digest(f.read_bytes()),'json_pointer':'/original_dispositions'}
        self.owner['bindings']=self.bind(sorted(self.owner_paths+['docs/SUMMARY.md']))
        self.edit['canonical_notes'][0]['review_reference']=self.ref('cycle-owner.json',self.owner)
        self.confirm();self.invalid('circular summary authority')


class RangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec=importlib.util.spec_from_file_location('receipt_ranges',TOOL)
        cls.module=importlib.util.module_from_spec(spec);spec.loader.exec_module(cls.module)

    def test_all_edit_forms_and_uncovered_prefix(self):
        old='α abc tail'.encode();new='α xy tail!'.encode()
        edits=[]
        for a,b,c,d in [(3,6,3,5),(11,11,10,11)]:
            edits.append({'old':interval(old,a,b),'new':interval(new,c,d),
                          'old_context':interval(old),'new_context':interval(new),
                          'canonical_notes':[],'rationale':'test'})
        self.module.reconstruct_summary(old,new,edits)
        prefixed=b'Z'+new
        for edit in edits:
            n=edit['new'];edit['new']=interval(prefixed,n['start']+1,n['end']+1)
            edit['new_context']=interval(prefixed)
        with self.assertRaisesRegex(ValueError,'uncovered'):
            self.module.reconstruct_summary(old,prefixed,edits)

    def test_authority_cycles_and_shared_acyclic_parents(self):
        check=self.module.require_acyclic_summary_authority
        check({'a':{'b','c'},'b':{'c'}},'a',{'summary'})
        for graph in ({'a':{'b'},'b':{'a'}},{'a':{'a'}},{'a':{'b'},'b':{'summary'}}):
            with self.assertRaisesRegex(ValueError,'cyclic|circular'):
                check(graph,'a',{'summary'})

    def test_bounds_hash_types_and_noop(self):
        old=b'abc';new=b'axc'
        edit={'old':interval(old,1,2),'new':interval(new,1,2),
              'old_context':interval(old),'new_context':interval(new),
              'canonical_notes':[],'rationale':'test'}
        for bounds in [(-1,2),(1,4),(2,1),(True,2)]:
            bad=copy.deepcopy(edit);bad['old']['start'],bad['old']['end']=bounds
            with self.assertRaisesRegex(ValueError,'bounds'):
                self.module.reconstruct_summary(old,new,[bad])
        same=copy.deepcopy(edit);same['new']=interval(old,1,2);same['new_context']=interval(old)
        with self.assertRaisesRegex(ValueError,'no-op'):
            self.module.reconstruct_summary(old,old,[same])


if __name__=='__main__':unittest.main()
