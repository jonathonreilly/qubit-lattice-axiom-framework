"""Independent transcription of the proposed formula, not an author helper."""
import numpy as np

def phase_matrix(theta):
    theta = np.asarray(theta)
    out = np.zeros(theta.shape + (2, 2), complex)
    out[..., 0, 0] = np.exp(-0.5j * theta)
    out[..., 1, 1] = np.exp(+0.5j * theta)
    return out

def lattice_frame(m, v, a, q):
    sigma = np.sqrt(m*m/4 + v*v/(a*a))
    g, J = sigma/2 + m/4, sigma/2 - m/4
    theta = np.angle(g - J * np.exp(-1j * a * q))
    return phase_matrix(theta)

def amplitude(m, v, a, p):
    p = np.asarray(p)
    q = 2*np.arcsin(a*p/2)/a
    w = np.sqrt(1-a*a*p*p/4)
    factor = w ** -0.5
    cont = phase_matrix(np.arctan(v*p/m))
    lat = lattice_frame(m, v, a, q)
    return factor[..., None, None] * (cont.conj().swapaxes(-1, -2) @ lat)

def boost_p(m, v, a, p, psi, dpsi):
    E = np.sqrt(m*m+v*v*p*p)
    Ep = v*v*p/E
    w = np.sqrt(1-a*a*p*p/4)
    wp = -a*a*p/(4*w)
    connection = 0.5 * (Ep*w + E*wp) * psi
    origin = -0.5 * a * E * psi
    return 1j * (E*w*dpsi + connection) + origin

def alias_cell(a, q, hat):
    q = np.asarray(q)
    out = np.zeros(q.shape + (2,), complex)
    for ell in range(-8, 9):
        k = q + 2*np.pi*ell/a
        phase = np.exp(+0.5j*a*k)
        out += (phase * np.sinc(a*k/(2*np.pi)))[..., None] * hat(k)
    return out
