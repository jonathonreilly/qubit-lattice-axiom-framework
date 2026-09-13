"""Run bounded, mathematical fault injections against the consolidated primary."""
from pathlib import Path
import gzip,hashlib,json,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parents[4]
PACK=Path(__file__).resolve().parent
PRIMARY=ROOT/'scripts/native_common_frame_spin_connection_2026_09_13.py'
CASES=[
 ('common_frame_vertex_sign','vertices=s.Matrix([[s.sin(k[0]),s.sin(k[1]),b*s.sin(k[2])/v**2],','vertices=s.Matrix([[s.sin(k[0]),s.sin(k[1]),-b*s.sin(k[2])/v**2],'),
 ('naive_node_frame_order',"naive.jacobian(k).subs(sub),F*R)","naive.jacobian(k).subs(sub),R*F)"),
 ('Laurent_second_neighbor_sign','sincoeff(2,-1/(2*v**2),2)','sincoeff(2,1/(2*v**2),2)'),
 ('Laurent_Taylor_constant','expected=(zz+2)/(2*vv**2)','expected=(zz+1)/(2*vv**2)'),
 ('relative_bound_coefficient','np.max(error/norm)<.25','np.max(error/norm)<.01'),
 ('protected_y_edges','return (tail[0]+tail[1])%2==0','return False'),
 ('flat_spin_rotation_weight','+div(v)*f/2)+pauli(curl(v))*f/4','+div(v)*f/2)+pauli(curl(v))*f/2'),
 ('compact_connection_weight','for a,b,c,i,j in product(range(3),repeat=5))/4','for a,b,c,i,j in product(range(3),repeat=5))/2'),
 ('metric_frame_order','G=F.T*F;g=G.inv()','G=F*F.T;g=G.inv()'),
 ('density_connection_weight','A[i]-I2*sum(Gamma[k][k][i] for k in range(3))/2','A[i]-I2*sum(Gamma[k][k][i] for k in range(3))/4'),
 ('curved_spin_transport_weight','gamma[i]*gamma[j]*(dN[i]*dM[j]-dM[i]*dN[j])/4','gamma[i]*gamma[j]*(dN[i]*dM[j]-dM[i]*dN[j])/8'),
 ('curved_drift_metric','drift=G*covector','drift=g*covector'),
 ('polar_metric_power','positive_root(J@E@E@J.T)','positive_root(J@E@J.T)'),
 ('polar_rotation_variation','dOab=(Jb*Sa-Sa*Jb.T-Sa*Ab-Ab*Sa)/2','dOab=(Jb*Sa-Sa*Jb.T-Sa*Ab-Ab*Sa)/3'),
 ('Neumann_series_sign','power=-np.einsum','power=np.einsum'),
 ('numerical_orientation','EPS[a,b,c]=(a-b)*(b-c)*(c-a)/2','EPS[a,b,c]=-(a-b)*(b-c)*(c-a)/2'),
 ('central_frame_derivative','central=(field(x+aa)-field(x-aa))/(2*aa)','central=(field(x+aa)-field(x-aa))/aa'),
 ('variable_xz_vertex','sk[:,2]*sk[:,0]/v','sk[:,0]'),
 ('connection_chirality','continuum+=w*Cref[:,None,None]*psi','continuum+=Cref[:,None,None]*psi'),
 ('operator_bound_coefficient','error+etaref<bound','error+etaref<bound/1000'),
 ('native_path_phase','Ap=(1j)**(length-1)*np.eye(size)','Ap=(-1j)**(length-1)*np.eye(size)'),
 ('native_imaginary_hopping_sign','J=-Ap@(np.eye(size)-B[0]@B[length])/2','J=Ap@(np.eye(size)-B[0]@B[length])/2'),
]

def main():
    start=time.monotonic();original=PRIMARY.read_bytes();text=original.decode();rows=[]
    dest=PACK/'mutations';dest.mkdir(exist_ok=True)
    for label,old,new in CASES:
        assert text.count(old)==1,(label,text.count(old))
        changed=text.replace(old,new,1).encode()
        (dest/(label+'.source.py.gz')).write_bytes(gzip.compress(changed,mtime=0))
        with tempfile.TemporaryDirectory(prefix='probe_',dir=dest) as tmp:
            base=Path(tmp);scripts=base/'scripts';scripts.mkdir()
            probe=scripts/PRIMARY.name;probe.write_bytes(changed)
            proc=subprocess.run([sys.executable,str(probe)],cwd=base,capture_output=True,timeout=60)
            (dest/(label+'.stdout.gz')).write_bytes(gzip.compress(proc.stdout,mtime=0))
            (dest/(label+'.stderr.gz')).write_bytes(gzip.compress(proc.stderr,mtime=0))
            if (base/'outputs').exists():
                for f in (base/'outputs').iterdir():
                    (dest/(label+'.'+f.name+'.gz')).write_bytes(gzip.compress(f.read_bytes(),mtime=0))
            effective=proc.returncode!=0 and b'AssertionError' in proc.stderr
            rows.append(dict(name=label,effective=effective,returncode=proc.returncode,
                             source_sha256=hashlib.sha256(changed).hexdigest(),
                             last_error=proc.stderr.decode(errors='replace').splitlines()[-1] if proc.stderr else ''))
            print(label,'REJECTED' if effective else 'NOT_REJECTED',flush=True)
    receipt=dict(primary_sha256=hashlib.sha256(original).hexdigest(),mutations=len(rows),
                 effective=sum(r['effective'] for r in rows),rows=rows,
                 elapsed_seconds=time.monotonic()-start)
    (PACK/'MUTATIONS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    assert all(r['effective'] for r in rows),receipt
    assert PRIMARY.read_bytes()==original

if __name__=='__main__':main()
