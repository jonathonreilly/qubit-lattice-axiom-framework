"""Reproduce exposed Hensen2015 aggregates using deposited fixed selections.
Original archive stays external. No parameter scan, fitting or new holdout claim.
"""
from pathlib import Path
import argparse,csv,hashlib,io,json,zipfile
import mpmath as mp
ap=argparse.ArgumentParser();ap.add_argument('--archive',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
archive=Path(args.archive).read_bytes();archive_sha=hashlib.sha256(archive).hexdigest()
assert archive_sha=='c28eb0f075759aef620a0b2e00a70fd675ce712bc8214d11c103f5a3d29492c0','archive identity changed'
z=zipfile.ZipFile(io.BytesIO(archive));raw=z.read('bell_open_data.txt');assert hashlib.sha256(raw).hexdigest()=='5a6b1853554ad508d35c795415d64922ed9e5bc0469f6052ad222486ad3566ff'
rows=list(csv.reader(io.StringIO(raw.decode('ascii'))));table=[[0]*4 for _ in range(4)];stage=[0]*4;selected=[];wins=0
starts={0:5426350,1:5425700};length=52450;separation=250000
for linenum,row in enumerate(rows,1):
 assert len(row)==17
 timestamp=row[0];(day,run,t1,ch1,t2,ch2,a,b,ta,tb,ra,rb,ea,eb,ia,ib)=map(int,row[1:])
 assert ch1 in (0,1) and ch2 in (0,1) and a in (0,1) and b in (0,1)
 gate=(starts[ch1]<=t1<starts[ch1]+length and starts[ch2]+separation<=t2<starts[ch2]+separation+length and ch1!=ch2)
 if not gate:continue
 stage[0]+=1
 if not ((ia==0 or ia>250) and (ib==0 or ib>250)):continue
 stage[1]+=1
 if ea!=0 or eb!=0:continue
 stage[2]+=1
 ca=10620<ra<=14320;cb=10620<rb<=14320
 xa=1 if ca else -1;xb=1 if cb else -1
 col={(1,1):0,(1,-1):1,(-1,1):2,(-1,-1):3}[xa,xb]
 table[2*a+b][col]+=1;wins+=int(((-1)**(a*b))*xa*xb==1);selected.append(linenum)
 stage[3]+=1
N=len(selected);assert N==245 and wins==196,'fixed original count reproduction failed'
mp.mp.dps=65
corr=[mp.mpf(row[0]-row[1]-row[2]+row[3])/sum(row) for row in table];S=sum(corr[:3])-corr[3]
err=mp.sqrt(mp.fsum((1-e*e)/sum(row) for row,e in zip(table,corr)))
tau=mp.mpf('1.08e-5');qs={'original_deposit_bound':mp.mpf(3)/4+3*(tau+tau*tau),'conditional_independent_bias_bound':mp.mpf(3)/4+tau-tau*tau,'ideal_fresh_uniform_bound':mp.mpf(3)/4}
tails={key:mp.fsum(mp.binomial(N,j)*q**j*(1-q)**(N-j) for j in range(wins,N+1)) for key,q in qs.items()}
result={'archive_sha256':archive_sha,'members_sha256':{n:hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist()},'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'data_role':'Exposed development reproduction; published aggregates were known before download. No independent empirical test or new theory fit.','rows_in_deposit':len(rows),'stage_counts':dict(zip(['original_herald_gate','also_invalid_marker_gate','also_no_early_excitation_click','scored_trials'],stage)),'selected_line_numbers_sha256':hashlib.sha256(json.dumps(selected,separators=(',',':')).encode()).hexdigest(),'trials':N,'wins':wins,'settings_rows':['00','01','10','11'],'outcome_columns':['++','+-','-+','--'],'table':table,'correlations':[str(v) for v in corr],'S':str(S),'S_descriptive_error_original_iid_formula':str(err),'game_score':str(8*(mp.mpf(wins)/N-mp.mpf('.5'))),'tau_from_published_input_analysis':str(tau),'conditional_win_bounds':{k:str(v) for k,v in qs.items()},'fixed_horizon_tails':{k:str(v) for k,v in tails.items()},'limitations':['Original selection/calibration values adopted from deposited example, not optimized here.','Original deposited tail and tighter conditional-product-input tail use distinct bounds; neither is a posterior model probability.','S descriptive error uses the original iid-style variance formula, separate from memory-allowing tail.','CSV and fixed selection reproduction do not independently verify space-time closure, random-source calibration or latent conditional independence.','No record-order search, stop-time optimization, memory-network fitting or holdout selection.'],'checks':{'identity_verified':True,'original_counts_reproduced':True,'all_rows_have_17_fields':True,'all_setting_and_herald_channels_binary':True,'no_selection_parameter_scan':True}}
Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
