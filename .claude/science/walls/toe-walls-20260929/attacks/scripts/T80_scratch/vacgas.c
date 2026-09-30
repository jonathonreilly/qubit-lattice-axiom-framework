// T80 test: annealed vacancy gas of records with contents on the periodic cubic lattice.
// Weight = prod_x (z if occupied) * prod_bonds B,  B = 1 if either end empty, c*exp(beta s.s') if both occupied.
// Menus: 's' sphere (unit 3-vector, uniform measure), 'i' two-valued (+-1).
// c = g * c0(beta): c0 = beta/sinh(beta) (sphere), 1/cosh(beta) (two-valued).  g=1 is the neutral scale.
// Special cmode "one": c = 1.
// Exact site heat-bath on the 7-state (sphere) or 3-state (two-valued) site variable, sequential scan.
// usage: vacgas menu L beta z cmode seed ntherm nmeas [cold]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t s0, s1;
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static inline uint64_t nextu(void) { // xoroshiro128+
    const uint64_t a = s0; uint64_t b = s1; const uint64_t r = a + b;
    b ^= a; s0 = rotl(a, 24) ^ b ^ (b << 16); s1 = rotl(b, 37); return r;
}
static inline double U01(void) { return ((nextu() >> 11) + 0.5) * (1.0 / 9007199254740992.0); }
static uint64_t splitmix(uint64_t *x) { uint64_t z = (*x += 0x9e3779b97f4a7c15ULL); z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL; z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL; return z ^ (z >> 31); }

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage\n"); return 1; }
    char menu = argv[1][0];
    int L = atoi(argv[2]);
    double beta = atof(argv[3]), z = atof(argv[4]);
    const char *cmode = argv[5];
    uint64_t seed = strtoull(argv[6], 0, 10);
    int ntherm = atoi(argv[7]), nmeas = atoi(argv[8]);
    int cold = (argc > 9 && atoi(argv[9]) == 1);
    uint64_t sm = seed * 7919 + 12345; s0 = splitmix(&sm); s1 = splitmix(&sm);
    double c0 = (menu == 's') ? (beta > 1e-9 ? beta / sinh(beta) : 1.0) : 1.0 / cosh(beta);
    double c, g;
    if (!strcmp(cmode, "one")) { c = 1.0; g = c / c0; } else { g = atof(cmode); c = g * c0; }
    int V = L * L * L;
    int (*nb)[6] = malloc(sizeof(int) * 6 * V);
    for (int x = 0; x < L; x++) for (int y = 0; y < L; y++) for (int w = 0; w < L; w++) {
        int i = (x * L + y) * L + w;
        nb[i][0] = (((x + 1) % L) * L + y) * L + w; nb[i][1] = (((x + L - 1) % L) * L + y) * L + w;
        nb[i][2] = (x * L + (y + 1) % L) * L + w;  nb[i][3] = (x * L + (y + L - 1) % L) * L + w;
        nb[i][4] = (x * L + y) * L + (w + 1) % L;  nb[i][5] = (x * L + y) * L + (w + L - 1) % L;
    }
    char *n = calloc(V, 1);
    double *sx = calloc(V, sizeof(double)), *sy = calloc(V, sizeof(double)), *sz = calloc(V, sizeof(double));
    double powc[7]; for (int k = 0; k <= 6; k++) powc[k] = pow(c, k);
    // init
    for (int i = 0; i < V; i++) {
        if (cold) { n[i] = 1; sx[i] = 0; sy[i] = 0; sz[i] = 1; if (menu == 'i') { sx[i] = 1; sz[i] = 0; } }
        else {
            n[i] = (U01() < z / (1 + z)) ? 1 : 0;
            if (menu == 's') { double u = 2 * U01() - 1, ph = 2 * M_PI * U01(), st = sqrt(1 - u * u); sx[i] = st * cos(ph); sy[i] = st * sin(ph); sz[i] = u; }
            else { sx[i] = (U01() < 0.5) ? 1 : -1; sy[i] = 0; sz[i] = 0; }
        }
    }
    int T = ntherm + nmeas;
    double *rho = malloc(sizeof(double) * nmeas), *M2 = malloc(sizeof(double) * nmeas);
    for (int t = 0; t < T; t++) {
        for (int i = 0; i < V; i++) {
            int k = 0; double hx = 0, hy = 0, hz = 0;
            for (int d = 0; d < 6; d++) { int j = nb[i][d]; if (n[j]) { k++; hx += sx[j]; hy += sy[j]; hz += sz[j]; } }
            if (menu == 's') {
                double hm = sqrt(hx * hx + hy * hy + hz * hz), kap = beta * hm;
                double f = (kap < 1e-8) ? 1.0 + kap * kap / 6.0 : sinh(kap) / kap;
                double w1 = z * powc[k] * f;
                if (U01() < w1 / (1.0 + w1)) {
                    n[i] = 1;
                    double u, ph = 2 * M_PI * U01();
                    if (kap < 1e-8) u = 2 * U01() - 1;
                    else { double r = U01(); u = 1.0 + log(r + (1 - r) * exp(-2 * kap)) / kap; if (u > 1) u = 1; if (u < -1) u = -1; }
                    double st = sqrt(fmax(0.0, 1 - u * u)), cp = cos(ph), sp = sin(ph);
                    if (kap < 1e-8) { sx[i] = st * cp; sy[i] = st * sp; sz[i] = u; }
                    else {
                        double ex = hx / hm, ey = hy / hm, ez = hz / hm;
                        // orthonormal basis (a,b) perpendicular to e
                        double ax, ay, az;
                        if (fabs(ez) < 0.9) { ax = -ey; ay = ex; az = 0; } else { ax = 0; ay = -ez; az = ey; }
                        double an = sqrt(ax * ax + ay * ay + az * az); ax /= an; ay /= an; az /= an;
                        double bx = ey * az - ez * ay, by = ez * ax - ex * az, bz = ex * ay - ey * ax;
                        sx[i] = u * ex + st * (cp * ax + sp * bx);
                        sy[i] = u * ey + st * (cp * ay + sp * by);
                        sz[i] = u * ez + st * (cp * az + sp * bz);
                    }
                } else n[i] = 0;
            } else {
                double wp = z * powc[k] * exp(beta * hx), wm = z * powc[k] * exp(-beta * hx);
                double r = U01() * (1.0 + wp + wm);
                if (r < 1.0) n[i] = 0; else if (r < 1.0 + wp) { n[i] = 1; sx[i] = 1; } else { n[i] = 1; sx[i] = -1; }
            }
        }
        if (t >= ntherm) {
            int N = 0; double Mx = 0, My = 0, Mz = 0;
            for (int i = 0; i < V; i++) if (n[i]) { N++; Mx += sx[i]; My += sy[i]; Mz += sz[i]; }
            rho[t - ntherm] = (double)N / V;
            M2[t - ntherm] = (Mx * Mx + My * My + Mz * Mz) / ((double)V * V);
        }
    }
    // statistics: means, jackknife on U over 20 blocks
    double mr = 0, m2 = 0, m4 = 0;
    for (int t = 0; t < nmeas; t++) { mr += rho[t]; m2 += M2[t]; m4 += M2[t] * M2[t]; }
    mr /= nmeas; m2 /= nmeas; m4 /= nmeas;
    double vr = 0, kr = 0;
    for (int t = 0; t < nmeas; t++) { double d = rho[t] - mr; vr += d * d; kr += d * d * d * d; }
    vr /= nmeas; kr /= nmeas; double kurt = (vr > 0) ? kr / (vr * vr) : 0;
    int NB = 20, bs = nmeas / NB;
    double Ub[20], m2b[20]; double sumM2 = 0, sumM4 = 0;
    double bm2[20], bm4[20];
    for (int b = 0; b < NB; b++) { double a = 0, a4 = 0; for (int t = b * bs; t < (b + 1) * bs; t++) { a += M2[t]; a4 += M2[t] * M2[t]; } bm2[b] = a / bs; bm4[b] = a4 / bs; sumM2 += bm2[b]; sumM4 += bm4[b]; m2b[b] = bm2[b]; }
    double Ufull = 1 - (sumM4 / NB) / (3 * (sumM2 / NB) * (sumM2 / NB));
    double jm = 0, jv = 0;
    for (int b = 0; b < NB; b++) { double a = (sumM2 - bm2[b]) / (NB - 1), a4 = (sumM4 - bm4[b]) / (NB - 1); Ub[b] = 1 - a4 / (3 * a * a); jm += Ub[b]; }
    jm /= NB; for (int b = 0; b < NB; b++) jv += (Ub[b] - jm) * (Ub[b] - jm);
    double Uerr = sqrt(jv * (NB - 1.0) / NB);
    double sm2 = 0; for (int b = 0; b < NB; b++) sm2 += (m2b[b] - m2) * (m2b[b] - m2);
    double m2err = sqrt(sm2 / (NB * (NB - 1.0)));
    // M2 here is <|M|^2>/V^2 per sweep, i.e. m^2 per site squared of order parameter density
    printf("%c %d %.4f %.4g %.4f %.4f %.5f %.3e %.3f %.5f %.5f %.5f %.5f %d\n", menu, L, beta, z, g, c, mr, vr * V, kurt, m2, m2err, Ufull, Uerr, cold);
    return 0;
}
