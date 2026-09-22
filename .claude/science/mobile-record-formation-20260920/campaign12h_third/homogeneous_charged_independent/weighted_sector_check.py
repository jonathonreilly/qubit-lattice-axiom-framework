"""Exact higher-spin controls with nontrivial partial-shift amplitudes."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json,sys
sys.dont_write_bytecode=True
from finite_sector_check import physical_sector

HERE=Path(__file__).resolve().parent
rows=[physical_sector(2,2,(1,0,-1,0)),physical_sector(2,3,(1,0,1,0))]
out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'reused_own_helper_sha256':sha256((HERE/'finite_sector_check.py').read_bytes()).hexdigest(),
     'controls':rows,'scope':'Complete physical square sectors with S=2, so the factors 1 and sqrt(2/3) both occur. Exact arithmetic, not a full torus diagonalization.'}
data=json.dumps(out,indent=2)+'\n';target=HERE/'WEIGHTED_SECTOR_RESULTS.json'
assert not target.exists();target.write_text(data);print(data,end='')
