"""Independent selected-file parser and one frozen weak-model calculation."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,datetime
import numpy as np
from scipy.integrate import quad

O=Path(__file__).resolve().parent;P=O.parent
CHECKS=[]
def check(name,value,detail=None):CHECKS.append({'name':name,'passed':bool(value),'detail':detail})
def sha(b):return hashlib.sha256(b).hexdigest()
def zjson(z):return [float(np.real(z)),float(np.imag(z))]
def wc(t,a,b):
 L=b-a;s=(t-a)/L
 return (140/L*s**3*(1-s)**3,140/L**2*(3*s*s-12*s**3+15*s**4-6*s**5),140/L**3*(6*s-36*s*s+60*s**3-30*s**4))
def fit(features,train=None):
 C,D,E,U=[features[:,j] for j in range(4)];Omega=fit.Omega
 R=-D-1j*E/(2*Omega);B=C+1j*D/Omega
 cols=np.column_stack([B,1j*C,U,1j*U]);n=len(C)
 if train is None:train=n
 M=np.vstack([cols[:train].real,cols[:train].imag]);rhs=np.r_[R[:train].real,R[:train].imag]
 scale=np.linalg.norm(M,axis=0);assert np.all(scale>0)
 normalized=M/scale;coef,res,rank,sv=np.linalg.lstsq(normalized,rhs,rcond=None);coef=coef/scale
 pred=cols@coef;err=R-pred
 return {'train_windows':train,'coefficients':coef.tolist(),'rank':int(rank),'raw_singular_values':np.linalg.svd(M,compute_uv=False).tolist(),'normalized_singular_values':sv.tolist(),'column_scales':scale.tolist(),'R':list(map(zjson,R)),'predictions':list(map(zjson,pred)),'complex_residuals':list(map(zjson,err)),'train_residual_norm':float(np.linalg.norm(err[:train])),'later_residual_norm':float(np.linalg.norm(err[train:])),'all_residual_norm':float(np.linalg.norm(err))}
def quad_complex(f,a,b):
 return quad(lambda t:float(np.real(f(t))),a,b,epsabs=1e-12,epsrel=1e-12,limit=150)[0]+1j*quad(lambda t:float(np.imag(f(t))),a,b,epsabs=1e-12,epsrel=1e-12,limit=150)[0]
def synthetic():
 Omega=4.;gamma=.12;nu=.08;coupling=.8+.3j;delta=2*Omega*nu;freq2=Omega**2+delta
 roots=[-gamma/2-1j*Omega+1j*np.sqrt(freq2-gamma**2/4),-gamma/2-1j*Omega-1j*np.sqrt(freq2-gamma**2/4)]
 rates=np.array([.2,.9,1.7]);amp=np.array([1+.3j,.4-.2j,.15+.6j]);lam=1j*rates
 operator=lam**2+(gamma+2j*Omega)*lam+delta+1j*gamma*Omega
 def u(t):return np.sum(amp*operator*np.exp(lam*t))/(2j*Omega*coupling)
 truth=np.array([-gamma/2,nu,coupling.real,coupling.imag]);cases=[]
 for coefficients in [(0j,0j),(.7-.2j,-.15+.25j)]:
  def z(t):return np.sum(amp*np.exp(lam*t))+sum(c*np.exp(r*t) for c,r in zip(coefficients,roots))
  features=[]
  for a in np.arange(6)*.7:
   b=a+1.3
   C,D,E=[quad_complex(lambda t,j=j:wc(t,a,b)[j]*z(t),a,b) for j in range(3)]
   U=quad_complex(lambda t:wc(t,a,b)[0]*u(t),a,b);features.append([C,D,E,U])
  features=np.array(features);fit.Omega=Omega;result=fit(features)
  C,D,E,U=features.T;res=-D-1j*E/(2*Omega)-truth[0]*(C+1j*D/Omega)-1j*nu*C-coupling*U
  check('synthetic exact weak residual '+str(coefficients),max(abs(res))<1e-11,float(max(abs(res))))
  check('synthetic rank '+str(coefficients),result['rank']==4)
  check('synthetic coefficient recovery '+str(coefficients),max(abs(np.array(result['coefficients'])-truth))<1e-8,float(max(abs(np.array(result['coefficients'])-truth))))
  cases.append({'homogeneous_amplitudes':list(map(zjson,coefficients)),'roots':list(map(zjson,roots)),'truth':truth.tolist(),'features':[[zjson(x) for x in row] for row in features],'fit':result})
 # Same single harmonic in z,u makes all complex columns scalar multiples of one vector.
 tc=np.arange(6)*.7;mono=np.exp(.3j*tc);cols=np.column_stack([(.2+.1j)*mono,1j*mono,2*mono,2j*mono]);M=np.vstack([cols.real,cols.imag]);rank=np.linalg.matrix_rank(M)
 check('monochromatic rank loss',rank<=2,int(rank))
 return cases

def main():
 receipt=json.loads((P/'FUCHS_RAW_ACQUISITION_v1.json').read_text());access=json.loads((P/'FUCHS_RAW_ACCESS_PLAN_v1.json').read_text());plan=json.loads((P/'FUCHS_WEAK_DEVELOPMENT_PLAN_v1.json').read_text());intake=json.loads((P/'FUCHS_SCHEMA_INTAKE_v1.json').read_text())
 rawpath=Path(receipt['local_path']);data=rawpath.read_bytes()
 check('raw MD5 and SHA and byte count',hashlib.md5(data).hexdigest()==receipt['md5']==access['development_file']['checksum'].split(':')[1] and sha(data)==receipt['sha256']==plan['source_sha256']==intake['source_sha256'] and len(data)==receipt['bytes']==access['development_file']['size'])
 check('plan and derivation bindings',receipt['plan_sha256']==sha((P/'FUCHS_RAW_ACCESS_PLAN_v1.json').read_bytes()) and plan['derivation_sha256']==sha((P/'FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v1.md').read_bytes()))
 metadata_path=rawpath.parent/'fuchs2024-zenodo10300430-metadata.json';mb=metadata_path.read_bytes();metadata=json.loads(mb);selected=[v for v in metadata['files'] if v['key']==access['development_file']['key']]
 check('metadata hash and selected deposit',sha(mb)==access['metadata_sha256'] and len(metadata['files'])==8 and len(selected)==1 and selected[0]==access['development_file'])
 # Parse independently from all semicolon records, retaining header lines and resets.
 headers=[];times=[];values=[];ttokens=[];vtokens=[];row_text=[];bad=[]
 for lineno,line in enumerate(data.decode('utf-8').splitlines(),1):
  if line.startswith('%'):headers.append(line);continue
  if not line.strip():continue
  fields=line.split(';')
  if len(fields)!=2:bad.append({'line':lineno,'text':line});continue
  ts,vs=[x.strip() for x in fields];t=float(ts);v=float(vs)
  if not np.isfinite(t) or not np.isfinite(v):bad.append({'line':lineno,'text':line})
  times.append(t);values.append(v);ttokens.append(ts);vtokens.append(vs);row_text.append(ts+';'+vs+'\n')
 times=np.array(times);values=np.array(values);starts=[0]+(np.flatnonzero(np.diff(times)<0)+1).tolist();ends=starts[1:]+[len(times)]
 labels=[]
 for h in headers:
  m=re.search(r'% Demod (\d+) Sample .*?/dev\d+/demods/(\d+)/sample\.([A-Za-z]+)',h)
  if m:labels.append('demod'+m[1]+'_'+('frequency' if m[3]=='Frequency' else m[3]));check('header demod index '+str(len(labels)),int(m[1])-1==int(m[2]))
 check('all rows parsed',not bad and len(times)==678861,{'rows':len(times),'bad':bad});check('nine boundaries and headers',len(starts)==9 and len(labels)==9,{'starts':starts,'labels':labels})
 t0tokens=ttokens[starts[0]:ends[0]];streams=[];arrays=[]
 for i,(a,b) in enumerate(zip(starts,ends)):
  t=times[a:b];v=values[a:b];arrays.append((t,v));dt=np.diff(t)
  token_match=ttokens[a:b]==t0tokens
  exact_dt=[Decimal(ttokens[j+1])-Decimal(ttokens[j]) for j in range(a,b-1)]
  entry={'stream':i,'header_label':labels[i],'n':b-a,'first_row':a,'last_row_exclusive':b,'t0':float(t[0]),'t1':float(t[-1]),'duration_s':float(t[-1]-t[0]),'min_dt':float(min(dt)),'max_dt':float(max(dt)),'median_dt':float(np.median(dt)),'min_value':float(min(v)),'max_value':float(max(v)),'first_value':float(v[0]),'last_value':float(v[-1]),'all_times_identical_to_stream0':bool(np.array_equal(t,arrays[0][0])),'exact_time_tokens_identical':token_match,'exact_dt_min':str(min(exact_dt)),'exact_dt_max':str(max(exact_dt)),'numeric_tokens_sha256':sha(''.join(row_text[a:b]).encode()),'float64_big_endian_pair_sha256':sha(np.column_stack([t,v]).astype('>f8').tobytes()),'unique_value_count':len(set(vtokens[a:b]))}
  expected=intake['streams'][i];check('intake full scalar metadata stream '+str(i),all(entry[k]==val for k,val in expected.items()),{'mismatches':{k:[entry.get(k),val] for k,val in expected.items() if entry.get(k)!=val}})
  check('strict and exact time correspondence '+str(i),all(q>0 for q in exact_dt) and token_match)
  streams.append(entry)
 check('carrier2/3 correspondence',np.array_equal(arrays[7][1],arrays[8][1]) and len(set(vtokens[starts[7]:ends[7]]))==1 and streams[7]['first_value']==26.6992697817)
 check('carrier1 distinct',streams[6]['unique_value_count']==1 and streams[6]['first_value']==15.8871013411)
 header_units=[h for h in headers if h.startswith('% Time (s),')]
 check('declared units',header_units==['% Time (s), Amplitude (V)']*3+['% Time (s), Phase (deg)']*3+['% Time (s), Osc Frequency (Hz)']*3)
 synth=synthetic()
 # Only one fixed development model: 2<-3, unit source phasor, 1200 seconds.
 t=arrays[0][0];z=arrays[1][1]*np.exp(1j*np.pi*arrays[4][1]/180);u=np.exp(1j*np.pi*arrays[5][1]/180);Omega=2*np.pi*arrays[7][1][0]
 duration=1200.;nwin=int(np.floor((t[-1]-t[0])/duration));indices=[];features={'piecewise_linear_Gauss4':[],'trapezoid':[]};gx,gw=np.polynomial.legendre.leggauss(4);fraction=(gx+1)/2
 for j in range(nwin):
  aa=t[0]+j*duration;bb=aa+duration;left=np.searchsorted(t,aa,side='left');right=np.searchsorted(t,bb,side='left');tt=t[left:right];zz=z[left:right];uu=u[left:right]
  a,b=tt[0],tt[-1];dt=np.diff(tt);nodes=tt[:-1,None]+dt[:,None]*fraction;nodez=zz[:-1,None]+(zz[1:]-zz[:-1])[:,None]*fraction;nodeu=uu[:-1,None]+(uu[1:]-uu[:-1])[:,None]*fraction;wv=wc(nodes,a,b);factors=dt[:,None]*gw/2
  gl=[np.sum(factors*ww*nodez) for ww in wv]+[np.sum(factors*wv[0]*nodeu)]
  wv_record=wc(tt,a,b);integrands=[ww*zz for ww in wv_record]+[wv_record[0]*uu];trap=[np.sum(dt*(q[:-1]+q[1:])/2) for q in integrands]
  features['piecewise_linear_Gauss4'].append(gl);features['trapezoid'].append(trap);indices.append({'window':j,'first_index':int(left),'last_index_exclusive':int(right),'sample_count':len(tt),'nominal_start':float(aa),'nominal_end':float(bb),'actual_start':float(a),'actual_end':float(b),'actual_length':float(b-a)})
 fit.Omega=Omega;results={}
 for key,f in features.items():
  a=np.array(f);results[key]={'features':[[zjson(x) for x in row] for row in a],'all_windows':fit(a),'chronological':fit(a,2*nwin//3)};check(key+' full rank',results[key]['all_windows']['rank']==4)
 result={'scope':'Independent parser, exact synthetic weak-model check and one declared development case; no physical channel/force/filter identification or empirical validation','source_sha256':sha(Path(__file__).read_bytes()),'raw_file':{'path':str(rawpath),'sha256':sha(data),'md5':hashlib.md5(data).hexdigest(),'bytes':len(data)},'metadata_file':{'path':str(metadata_path),'sha256':sha(mb)},'headers':headers,'boundaries':starts,'streams':streams,'synthetics':synth,'development_case':{'receiver':2,'source':3,'input':'unit_phasor','nominal_duration':duration,'Omega':float(Omega),'windows':indices,'n_windows':nwin,'omitted_final_nominal_length':float(t[-1]-(t[0]+nwin*duration)),'results':results,'max_feature_quadrature_difference':float(np.max(np.abs(np.array(features['piecewise_linear_Gauss4'])-np.array(features['trapezoid']))))},'checks':CHECKS,'passed':sum(c['passed'] for c in CHECKS),'failed':sum(not c['passed'] for c in CHECKS),'other_raw_arrays_opened':False}
 (O/'INDEPENDENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'failed':result['failed'],'rows':len(times),'boundaries':starts,'n_windows':nwin,'development':{key:{'all':value['all_windows']['coefficients'],'chronological':value['chronological']['coefficients'],'condition':value['all_windows']['normalized_singular_values'][0]/value['all_windows']['normalized_singular_values'][-1]} for key,value in results.items()},'max_feature_quadrature_difference':result['development_case']['max_feature_quadrature_difference']},indent=2));assert result['failed']==0
if __name__=='__main__':main()
