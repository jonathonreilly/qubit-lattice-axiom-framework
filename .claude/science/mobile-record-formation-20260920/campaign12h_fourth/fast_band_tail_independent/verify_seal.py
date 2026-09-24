"""Read-only packet integrity check; this is not a scientific validator."""
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parent

def verify(rows):
 errors=[]
 for row in rows:
  path=ROOT/row['path']
  if not path.resolve().is_relative_to(ROOT):errors.append({'path':row['path'],'reason':'outside packet'})
  elif not path.is_file():errors.append({'path':row['path'],'reason':'missing'})
  elif path.stat().st_size!=row['bytes']:errors.append({'path':row['path'],'reason':'byte count mismatch'})
  elif hashlib.sha256(path.read_bytes()).hexdigest()!=row['sha256']:errors.append({'path':row['path'],'reason':'digest mismatch'})
 return errors

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('seal',nargs='?',default='PRE_SEAL.json');parser.add_argument('--self-test',action='store_true');args=parser.parse_args()
 if args.self_test:
  p=ROOT/'fiber_engine.py';r={'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  tests={'genuine_accepted':not verify([r]),'changed_digest_rejected':bool(verify([{**r,'sha256':'0'*64}])),'changed_size_rejected':bool(verify([{**r,'bytes':0}])),'missing_rejected':bool(verify([{**r,'path':'ABSENT_INTEGRITY_TEST'}])),'escape_rejected':bool(verify([{**r,'path':'../outside_packet'}]))}
  print(json.dumps({'scope':'integrity only','tests':tests,'passed':all(tests.values())},indent=2));sys.exit(0 if all(tests.values()) else 1)
 seal=json.loads((ROOT/args.seal).read_text());errors=verify(seal['artifacts']);print(json.dumps({'seal':args.seal,'artifacts_checked':len(seal['artifacts']),'errors':errors,'passed':not errors},indent=2));sys.exit(1 if errors else 0)
