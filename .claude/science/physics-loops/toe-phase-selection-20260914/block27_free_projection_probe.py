#!/usr/bin/env python3
"""Independent finite checks for the private free-boundary limit argument.

Tensor sine/cosine inversion is compared with a dense incidence projection.
The exhaustion values are diagnostics, not a certified convergence rate or
an exhaustive component expansion.
"""
import itertools
import json
import math
import numpy as np
from scipy.fft import dct, idct, dst, idst


DIM=4


def empty_form(side,degree):
    return {o:np.zeros(tuple(side if j in o else side+1 for j in range(DIM)))
            for o in itertools.combinations(range(DIM),degree)}


def exterior(form,side):
    degree=len(next(iter(form)))
    out=empty_form(side,degree+1)
    for q in out:
        for pos,j in enumerate(q):
            o=tuple(k for k in q if k!=j)
            out[q]+=(-1)**pos*np.diff(form[o],axis=j)
    return out


def adjoint(form,side):
    degree=len(next(iter(form)))
    out=empty_form(side,degree-1)
    for q,values in form.items():
        for pos,j in enumerate(q):
            o=tuple(k for k in q if k!=j)
            lower=[slice(None)]*DIM
            upper=[slice(None)]*DIM
            lower[j]=slice(0,side)
            upper[j]=slice(1,side+1)
            out[o][tuple(lower)]-=(-1)**pos*values
            out[o][tuple(upper)]+=(-1)**pos*values
    return out


def inverse_hodge(form,side,wrong_vertex_boundary=False):
    out={}
    for o,values in form.items():
        transformed=values.copy()
        eigen=np.zeros(values.shape)
        for axis in range(DIM):
            is_edge=axis in o
            use_dirichlet=is_edge or wrong_vertex_boundary
            size=values.shape[axis]
            if use_dirichlet:
                transformed=dst(transformed,type=1,axis=axis,norm='ortho')
                lam=2-2*np.cos(np.pi*np.arange(1,size+1)/(size+1))
            else:
                transformed=dct(transformed,type=2,axis=axis,norm='ortho')
                lam=2-2*np.cos(np.pi*np.arange(size)/size)
            shape=[1]*DIM
            shape[axis]=size
            eigen+=lam.reshape(shape)
        assert eigen.min()>0
        transformed/=eigen
        for axis in reversed(range(DIM)):
            if axis in o or wrong_vertex_boundary:
                transformed=idst(transformed,type=1,axis=axis,norm='ortho')
            else:
                transformed=idct(transformed,type=2,axis=axis,norm='ortho')
        out[o]=transformed
    return out


def project(form,side,wrong_vertex_boundary=False):
    return exterior(inverse_hodge(adjoint(form,side),side,wrong_vertex_boundary),side)


def dot(left,right):
    return float(sum(np.vdot(left[o],right[o]).real for o in left))


def difference(left,right):
    return {o:left[o]-right[o] for o in left}


def norm(form):
    return math.sqrt(dot(form,form))


def dense_projection_check():
    side=2
    links=empty_form(side,1)
    faces=empty_form(side,2)
    columns=[]
    for o,values in links.items():
        for index in np.ndindex(values.shape):
            links[o][index]=1
            column=exterior(links,side)
            columns.append(np.concatenate([column[q].ravel() for q in faces]))
            links[o][index]=0
    incidence=np.array(columns).T
    source=empty_form(side,2)
    cursor=0
    for o,values in source.items():
        v=np.sin(.29*np.arange(cursor,cursor+values.size)+.37)
        source[o]=v.reshape(values.shape)/math.sqrt(incidence.shape[0])
        cursor+=values.size
    flat=np.concatenate([source[o].ravel() for o in faces])
    solution=np.linalg.lstsq(incidence,flat,rcond=1e-12)[0]
    independent=incidence@solution
    p=project(source,side)
    actual=np.concatenate([p[o].ravel() for o in faces])
    projection_error=float(np.max(abs(actual-independent)))
    assert projection_error<1e-12
    assert norm(exterior(p,side))<1e-12
    assert norm(adjoint(difference(p,source),side))<1e-12
    assert abs(dot(p,p)-dot(source,p))<1e-12
    wrong=project(source,side,wrong_vertex_boundary=True)
    boundary_fault=norm(adjoint(difference(wrong,source),side))
    assert boundary_fault>1e-2
    # Extending by zero is not a chain map at the free boundary. This is why
    # the proof tests closure only against eventually interior test forms.
    extended=empty_form(side+2,2)
    for o,values in p.items():
        slices=tuple(slice(1,1+n) for n in values.shape)
        extended[o][slices]=values
    extension_curl=norm(exterior(extended,side+2))
    assert extension_curl>1e-2
    return dict(incidence_shape=list(incidence.shape),
                tensor_vs_incidence_max_error=projection_error,
                wrong_dirichlet_boundary_fault=boundary_fault,
                zero_extension_global_curl=extension_curl)


def exhaustion():
    radii=[1,2,3,4,6,8,12]
    probes=[]
    records=[]
    for radius in radii:
        side=2*radius
        source=empty_form(side,2)
        source[(0,1)][(radius,)*DIM]=1
        # A second orientation and translate challenge off-diagonal entries.
        source[(1,3)][(radius-1,radius,radius,radius)]=-.4
        p=project(source,side)
        record=dict(radius=radius,projection_norm_squared=dot(p,p),
                    source_inner_product=dot(source,p),
                    closure_residual=norm(exterior(p,side)),
                    coclosure_residual=norm(adjoint(difference(p,source),side)))
        assert abs(record['projection_norm_squared']-record['source_inner_product'])<2e-12
        assert record['closure_residual']<2e-12
        assert record['coclosure_residual']<2e-12
        if probes:
            prior_radius,prior=probes[-1]
            shift=radius-prior_radius
            cross=sum(np.vdot(prior[o],p[o][tuple(slice(shift,shift+n) for n in prior[o].shape)]).real
                      for o in prior)
            norm_squared=dot(prior,prior)+dot(p,p)-2*float(cross)
            record['difference_from_previous_radius']=math.sqrt(max(0.,norm_squared))
        records.append(record)
        probes=[(radius,p)]
    assert records[-1]['difference_from_previous_radius']<records[1]['difference_from_previous_radius']/5
    return records


if __name__=='__main__':
    print(json.dumps(dict(status='finite_checks_passed',
                         independent_cochain_projection=dense_projection_check(),
                         free_box_exhaustion=exhaustion(),
                         scope='Finite tensor/incidence agreement and exhaustion diagnostics only; no certified rate or all-shape enumeration.'),indent=2))
