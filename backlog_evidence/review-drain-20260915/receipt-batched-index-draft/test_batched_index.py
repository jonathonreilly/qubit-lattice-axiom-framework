from pathlib import Path
import importlib.util,tempfile,subprocess,unittest
from unittest.mock import patch
from types import SimpleNamespace
spec=importlib.util.spec_from_file_location('candidate',Path(__file__).with_name('review_receipt.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class BatchIndexTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.repo=Path(self.tmp.name).resolve();self.git('init','-q')
 def git(self,*a):return subprocess.check_output(['git','-C',str(self.repo),*a],stderr=subprocess.PIPE)
 def stage(self,p,b):
  q=self.repo/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b);self.git('add','--',p)
 def verify(self,names):return m.verify_index_bytes(self.repo,names,'mismatch')
 def test_exact_binary_and_unusual_paths(self):
  names=['space name','tab\tname','new\nline','unicode-λ','empty']
  for i,p in enumerate(names):self.stage(p,b'' if p=='empty' else bytes(range(256))*i)
  self.verify(names)
 def test_staged_and_working_byte_drift(self):
  self.stage('a',b'original');(self.repo/'a').write_bytes(b'changed')
  with self.assertRaisesRegex(ValueError,'mismatch'):self.verify(['a'])
 def test_untracked_or_deleted_index_entry(self):
  (self.repo/'a').write_bytes(b'original')
  with self.assertRaises(ValueError):self.verify(['a'])
  self.git('add','a');self.git('rm','--cached','a')
  with self.assertRaises(ValueError):self.verify(['a'])
 def test_nonblob_and_truncated_protocol_rejected(self):
  self.stage('a',b'abc')
  for raw in [b'x missing\n',b'0'*40+b' tree 3\nabc\n',b'0'*40+b' blob 3\nab',b'0'*40+b' blob 3\nabc\ntrailing',b'0'*40+b' blob 3\nabcX']:
   with self.subTest(raw=raw),patch.object(m.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout=raw,stderr=b'')):
    with self.assertRaises(ValueError):self.verify(['a'])
 def test_git_failure_rejected(self):
  self.stage('a',b'abc')
  with patch.object(m.subprocess,'run',return_value=SimpleNamespace(returncode=1,stdout=b'',stderr=b'failure')):
   with self.assertRaisesRegex(ValueError,'git cat-file failed'):self.verify(['a'])
 def test_file_count_and_byte_budget(self):
  names=[f'small{i}' for i in range(65)]+['big1','big2']
  for p in names:self.stage(p,b'x'*(5*1024*1024) if p.startswith('big') else b'x')
  original=m.subprocess.run;calls=[]
  def run(*a,**kw):calls.append(kw['input']);return original(*a,**kw)
  with patch.object(m.subprocess,'run',side_effect=run):self.verify(names)
  self.assertEqual([len(q.split(b'\0'))-1 for q in calls],[64,2,1])
 def test_single_oversize_file(self):
  self.stage('big',b'x'*(8*1024*1024+1));self.verify(['big'])
 def test_sha256_git_object_format(self):
  other=self.repo/'sha256';other.mkdir();subprocess.run(['git','init','-q','--object-format=sha256',str(other)],check=True);old=self.repo;self.repo=other
  try:self.stage('a',b'bytes');self.verify(['a'])
  finally:self.repo=old
 def test_symlink_rejected(self):
  self.stage('a',b'bytes');(self.repo/'b').symlink_to(self.repo/'a');self.git('add','b')
  with self.assertRaisesRegex(ValueError,'symbolic'):self.verify(['b'])
 def test_index_drift_between_checks(self):
  self.stage('a',b'before');self.verify(['a']);self.stage('a',b'after');(self.repo/'a').write_bytes(b'before')
  with self.assertRaisesRegex(ValueError,'mismatch'):self.verify(['a'])
if __name__=='__main__':unittest.main()
