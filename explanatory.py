*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
*  CLASS input parameter file  *
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*

> This example of input file, intended for CLASS beginners, lists all
> possibilities with detailed comments.  You can use a more concise version, in
> which only the arguments in which you are interested would appear.  Only
> lines containing an equal sign not preceded by a sharp sign "#" are
> considered by the code. Hence, do not write an equal sign within a comment,
> the whole line would be interpreted as relevant input. Input files must have
> an extension ".ini".

----------------------------
----> background parameters:
----------------------------

1) Hubble parameter : either 'H0' in km/s/Mpc or 'h' or '100*theta_s' where the
   latter is the peak scale parameter 100(ds_dec/da_dec) close to 1.042143
   (default: 'h' set to 0.67556)

#H0 = 67.556
h =0.67556
#100*theta_s = 1.042143

2) photon density: either 'T_cmb' in K or 'Omega_g' or 'omega_g' (default:
   'T_cmb' set to 2.7255)

T_cmb = 2.7255
#Omega_g =
#omega_g =

3) baryon density: either 'Omega_b' or 'omega_b' (default: 'omega_b' set to
   0.022032)

#Omega_b =
omega_b = 0.022032

4a) ultra-relativistic species / massless neutrino density: either 'N_ur' or
   'Omega_ur' or 'omega_ur' (default: 'N_ur' set to 3.046) (note: instead of
   'N_ur' you can pass equivalently 'N_eff', although this syntax is
   deprecated) (one more remark: if you have respectively 1,2,3 massive neutrinos, if you stick to the default value T_ncdm equal to 0.71611, designed to give m/omega of 93.14 eV, and if you want to use N_ur to get N_eff equal to 3.046 in the early universe, then you should pass here respectively 2.0328,1.0196,0.00641)

N_ur = 3.046
#Omega_ur =
#omega_ur =

4b) to simulate ultra-relativistic species with non-standard
    properties, you can pass 'ceff2_ur' and 'cvis2_ur' (effective squared
    sound speed and viscosity parameter, like in the Generalised Dark
    Matter formalism of W. Hu) (default: both set to 1/3)

#ceff2_ur =
#cvis2_ur =

5) density of cdm (cold dark matter): 'Omega_cdm' or 'omega_cdm' (default:
   'omega_cdm' set to 0.12038)

#Omega_cdm =
omega_cdm = 0.12038

5b) For models with decaying cold dark matter (dcdm) you can choose to pass either:

5b1) the current fractional density of dcdm+dr (decaying cold dark
    matter and its relativistic decay radiation): 'Omega_dcdmdr' or
    'omega_dcdmdr' (default: 'Omega_dcdmdr' set to 0)

Omega_dcdmdr = 0.0
#omega_dcdmdr = 0.0

5b2) the rescaled initial value for dcdm density (see 1407.2418 for definitions). If you specify 5b1, 5b2 will be found autamtically by a shooting method, and vice versa. (default: 'Omega_dcdmdr' set to 0, hence so is 'Omega_ini_dcdm')

#Omega_ini_dcdm =
#omega_ini_dcdm =

5c) decay constant of dcdm in km/s/Mpc, same unit as H0 above.

Gamma_dcdm = 0.0

6) all parameters describing the ncdm sector (i.e. any non-cold dark matter
   relics, including massive neutrinos, warm dark matter, etc.):

  -> 'N_ncdm' is the number of distinct species (default: set to 0)

N_ncdm = 0

  -> 'use_ncdm_psd_files' is the list of N_ncdm numbers: 0 means 'phase-space
     distribution (psd) passed analytically inside the code, in the mnodule
     background.c, inside the function background_ncdm_distribution()'; 1 means
     'psd passed as a file with at list two columns: first for q, second for
     f_0(q)', where q is p/T_ncdm (default: only zeros)

#use_ncdm_psd_files = 0

  -> if some of the previous values are equal to one, 'ncdm_psd_filenames' is
     the list of names of psd files (as many as number of ones in previous entry)

ncdm_psd_filenames = psd_FD_single.dat

  -> 'ncdm_psd_parameters' is an optional list of double parameters to describe
     the analytic distribution function or to modify a p.s.d. passed as a file.
     It is made available in the routine background_ncdm_distribution.

#ncdm_psd_parameters = Nactive, sin^2_12 ,s23 ,s13
ncdm_psd_parameters = 0.3 ,0.5, 0.05


The remaining parameters should be entered as a list of N_ncdm numbers
separated by commas:

  -> 'Omega_ncdm' or 'omega_ncdm' or 'm_ncdm' in eV (default: all set to zero);
           with only one of these inputs, CLASS computes the correct value of
           the mass; if both (Omega_ncdm, m_ncdm) or (omega_ncdm, m_ncdm) are
           passed, CLASS will renormalise the psd in order to fulfill both
           conditions.
           Passing zero in the list of m_ncdm's or Omeg_ncdm's means that for
           this component, this coefficient is not imposed, and its value is
           inferred from the other one.

m_ncdm = 0.04, 0.04, 0.04
Omega_ncdm =

  -> 'T_ncdm' is the ncdm temperature in units of photon temperature
     (default: set to 0.71611, which is slightly larger than the
     instantaneous decoupling value (4/11)^(1/3); indeed, this default
     value is fudged to give a ratio m/omega equal to 93.14 eV for
     active neutrinos, as predicted by precise studies of active
     neutrino decoupling, see hep-ph/0506164)

T_ncdm =

  -> 'ksi_ncdm' is the ncdm chemical potential in units of its own temperature
     (default: set to 0)

ksi_ncdm =

  -> 'deg_ncdm' is the degeneracy parameter multiplying the psd: 1 stands for
     'one family', i.e. one particle + anti-particle (default: set to 1.0)

deg_ncdm =

  -> 'Quadrature strategy' is the method used for the momentum sampling of the
  ncdm distribution function. 0 is the automatic method, 1 is Gauss-Laguerre
  quadrature, 2 is the trapezoidal rule on [0,Infinity] using the transformation
  q->1/t-1. 3 is the trapezoidal rule on [0,q_max] where q_max is the next input.
  (default: set to 0)

Quadrature strategy =

  -> 'Maximum q' is the maximum q relevant only for Quadrature strategy 3.
  (default: set to 15)

Maximum q =

7) curvature: 'Omega_k' (default: 'Omega_k' set to 0)

Omega_k = 0.

8a) Dark energy contributions. At least one out of three conditions must be satisfied:
    i)   'Omega_Lambda' unspecified.
    ii)  'Omega_fld' unspecified.
    iii) 'Omega_scf' set to a negative value. [Will be refered to as
         unspecified in the following text.]
    The code will then use the first unspecified component to satisfy the
    closure equation (sum_i Omega_i) equals (1 + Omega_k)
    (default: 'Omega_fld' and 'Omega_scf' set to 0 and 'Omega_Lambda' inferred
    by code)

# Omega_Lambda = 0.7
Omega_fld = 0
Omega_scf = 0

8b) The flag 'use_ppf' is 'yes' by default, to use the PPF approximation
    (see 0808.3125 [astro-ph]) allowing perturbations to cross the
    phantom divide. Set to 'no' to enforce true fluid equations for
    perturbations. When the PPF approximation is used, you can choose
    the ratio 'c_gamma_over_c_fld' (eq. (16) in 0808.3125). The
    default is 0.4 as recommended by that reference, and implicitely
    assumed in other codes. (default: 'use_ppf' to yes, 'c_gamma_over_c_fld' to 0.4)

use_ppf = yes
c_gamma_over_c_fld = 0.4

8c) Choose your equation of state between different models, 'CLP' for
    p/rho = w0_fld + wa_fld (1-a/a0) (Chevalier-Linder-Polarski),
    'EDE' for early Dark Energy (default:'fluid_equation_of_state' set to 'CLP')

fluid_equation_of_state = CLP

8c1) equation of state of the fluid in 'CLP' case (p/rho = w0_fld +
    wa_fld (1-a/a0)) and squared sound speed 'cs2_fld' of the fluid
    (this is the sound speed defined in the frame comoving with the
    fluid, i.e. obeying to the most sensible physical
    definition). Generalizing w(a) to a more complicated expressions
    would be easy, for that, have a look into source/background.c at
    the function background_w_fld().  (default: 'w0_fld' set to -1,
    'wa_fld' to 0, 'cs2_fls' to 1)

w0_fld = -0.9
wa_fld = 0.
cs2_fld = 1

8c2) equation of state of the fluid in 'EDE' case and squared sound speed 'cs2_fld' of the fluid
    (this is the sound speed defined in the frame comoving with the
    fluid, i.e. obeying to the most sensible physical
    definition). Generalizing w(a) to a more complicated expressions
    would be easy, for that, have a look into source/background.c at
    the function background_w_fld().  (default: 'w0_fld' set to -1,
    'Omega_EDE' to 0, 'cs2_fls' to 1)

w0_fld = -0.9
Omega_EDE = 0.
cs2_fld = 1

8d) Scalar field (scf) initial conditions from attractor solution (assuming
    pure exponential potential). (default: yes)

attractor_ic_scf = yes

8e) Scalar field (scf) potential parameters and initial conditions.  V equals
    ((\phi-B)^\alpha + A)exp(-lambda*phi), see
    http://arxiv.org/abs/astro-ph/9908085.

#scf_parameters = [scf_lambda, scf_alpha, scf_A, scf_B, phi, phi_prime]
scf_parameters = 10.0, 0.0, 0.0, 0.0, 100.0, 0.0

If 'attractor_ic_scf' is set to 'no', the last two entries are assumed to be
the initial values of phi in units of the reduced planck mass m_Pl and the
conformal time derivative of phi in units of [m_Pl/Mpc]. (Note however that
CLASS determines the initial scale factor dynamically and the results might not
be as expected in some models.)

8f) Scalar field (scf) tuning parameter: If Omega_scf is negative, the
    following index (0,1,2,...) in scf_parameters will be used for tuning:

scf_tuning_index = 0

9) scale factor today 'a_today' (arbitrary and irrelevant for most purposes)
   (default: set to 1)

# a_today = 1.

--------------------------------
----> thermodynamics parameters:
--------------------------------

1) primordial Helium fraction 'YHe', e.g. 0.25; if set to 'BBN' or 'bbn', will
   be inferred from Big Bang Nucleosynthesis (default: set to 'BBN')

YHe = BBN

2) 'recombination' algorithm set to 'RECFAST' or 'HyRec'

recombination = RECFAST

2) parametrization of reionization: 'reio_parametrization' must be one
   of 'reio_none' (no reionization), 'reio_camb' (like CAMB: one
   tanh() step for hydrogen reionization one for second helium
   reionization), 'reio_bins_tanh' (binned history x_e(z) with tanh()
   interpolation between input values), 'reio_half_tanh' (like
   'reio_camb' excepted that we match the function xe(z) from
   recombination with only half a tanh(z-z_reio)), 'reio_many_tanh'
   (arbitrary number of tanh-like steps with specified ending values,
   a scheme usually more useful than 'reio_bins_tanh'), 'reio_inter'
   (linear interpolation between discrete values of xe(z))...  (default:
   set to 'reio_camb')

reio_parametrization = reio_camb

3.a.) if 'reio_parametrization' set to 'reio_camb' or 'reio_half_tanh': enter
      one of 'z_reio' or 'tau_reio' (default: 'z_reio' set to 11.357 to get tau_reio of 0.0925), plus
      'reionization_exponent', 'reionization_width',
      'helium_fullreio_redshift', 'helium_fullreio_width'
      (default: set to 1.5, 0.5, 3.5, 0.5)

z_reio = 11.357
#tau_reio = 0.0925

reionization_exponent = 1.5
reionization_width = 0.5
helium_fullreio_redshift = 3.5
helium_fullreio_width = 0.5

3.b.) if 'reio_parametrization' set to 'reio_bins_tanh': enter number of bins
      and list of z_i and xe_i defining the free electron density at the center
      of each bin. Also enter a dimensionless paramater regulating the
      sharpness of the tanh() steps, independently of the bin width;
      recommended sharpness is 0.3, smaller values will make steps too sharp,
      larger values will make the step very progressive but with discontinuity
      of x_e(z) derivative around z_i values.
      (default: set to 0, blank, blank, 0.3)

binned_reio_num = 3
binned_reio_z = 8,12,16
binned_reio_xe = 0.8,0.2,0.1
binned_reio_step_sharpness = 0.3

3.c.) if 'reio_parametrization' set to 'reio_many_tanh': enter number of jumps,
      list of jump redhsifts z_i (central value of each tanh()), list of free electron density x_i after each jump, and common width of all jumps. If you want to end up with all hydrogen reionized but neglecting helium reionization, the first value of x_i in the list should be 1. For each x_i you can also pass the flags -1 or -2. They mean: for -1, after hydrogen + first helium recombination (so the code will substitute a value bigger than one based on Y_He); for -2, after hydrogen + second helium recombination (the code will substitute an even bigger value based on Y_He). You can get results close to reio_camb by setting  these parameters to the value showed below (and adapting the second many_tanh_z to the usual z_reio). (default: not set)

many_tanh_num = 2
many_tanh_z = 3.5,11.3
many_tanh_xe = -2,-1
many_tanh_width = 0.5

3.d.) if 'reio_parametrization' set to 'reio_inter': enter the number
of points, the list of redshifts z_i, and the list of free electron
fraction values x_i. The code will do linear interpolation between
them. The first z_i should always be 0. Like above, for each x_i, you
can also pass the flags -1 or -2. They mean: for -1, after the
hydrogen and the first helium recombination (so the code will
substitute a value bigger than one based on Y_He); for -2, after the
hydrogen and the second helium recombination (the code will substitute
an even bigger value based on Y_He). The last value of x_i should
always be zero, the code will substitute it with the value that one
would get in absence of reionization, as computed by the recombination
code. (default: not set)

reio_inter_num = 8
reio_inter_z =   0,  3,  4,   8,   9,  10,  11, 12
reio_inter_xe = -2, -2, -1,  -1, 0.9, 0.5, 0.1,  0

4.a) in order to model energy injection from DM annihilation, specify a
     parameter 'annihilation' corresponding to the energy fraction absorbed by
     the gas times the DM cross section divided by the DM mass, (f <sigma*v> /
     m_cdm), see e.g. 0905.0003, expressed here in units of m^3/s/Kg
     (default: set to zero)

annihilation = 0.

4.b) you can model simple variations of the above quanity as a function of
     redhsift. If 'annihilation_variation' is non-zero, the function F(z)
     defined as (f <sigma*v> / m_cdm)(z) will be a parabola in log-log scale
     between 'annihilation_zmin' and 'annihilation_zmax', with a curvature
     given by 'annihilation_variation' (must be negative), and with a maximum
     in 'annihilation_zmax'; it will be constant outside this range. To take DM
     halos into account, specify the parameters 'annihilation_f_halo', the
     amplitude of the halo contribution, and 'annihilation_z_halo', the
     characteristic redshift of halos
     (default: no variation, 'annihilation_variation' and 'annihilation_f_halo'
     set to zero).

annihilation_variation = 0.
annihilation_z = 1000
annihilation_zmax = 2500
annihilation_zmin = 30
annihilation_f_halo= 20
annihilation_z_halo= 8

4.c) You can also state whether you want to use the on-the-spot approximation
     (default: 'on the spot' is 'yes')

on the spot = yes

5) to model DM decay, specify a parameter 'decay' which is equal to the energy
   fraction absorbed by the gas divided by the lifetime of the particle, see
   e.g.  1109.6322, expressed here in 1/s
   (default: set to zero)

decay = 0.

6) State whether you want the code to compute the simplest analytic approximation to the photon damping scale (it will be added to the thermodynamics output, and its value at recombination will be stored and displayed in the standard output) (default: 'compute damping scale' set to 'no')

# compute damping scale = yes

----------------------------------------------------
----> define which perturbations should be computed:
----------------------------------------------------

1.a) list of output spectra requested:
- 'tCl' for temperature Cls,
- 'pCl' for polarization Cls,
- 'lCl' for CMB lensing potential Cls,
- 'nCl' (or 'dCl') for density number count Cls,
- 'sCl' for galaxy lensing potential Cls,
- 'mPk' for total matter power spectrum P(k) infered from gravitational potential,
- 'dTk' (or 'mTk') for density transfer functions for each species,
- 'vTk' for velocity transfer function for each species.
Warning: both lCl and sCl compute the C_ls of the lensing potential, C_l^phi-phi.
If you are used to other codes, you may want to deal instead with the deflection
Cls or the shear/convergence Cls. The relations between them are trivial:
--> deflection d:
    Cl^dd = l(l+1) C_l^phiphi
--> convergence kappa and shear gamma: the share the same harmonic power spectrum:
    Cl^gamma-gamma = 1/4 * [(l+2)!/(l-2)!] C_l^phi-phi
By defaut, the code will try to compute the following cross-correlation Cls (if
available): temperature-polarisation, temperature-CMB lensing, polarization-CMB
lensing, CMB lensing-density, and density-lensing. Other cross-correlations are
not computed because they would slow down the code considerably.

Can be left blank if you do not want to evolve cosmological perturbations at
all. (default: set to blanck, no perturbation calculation)

output = tCl,pCl,lCl
#output = tCl,pCl,lCl,mPk
#output = mPk,mTk

1.b) if you included 'tCl' in the list, you can take into account only some of
     the terms contributing to the temperature spectrum: intrinsic temperature
     corrected by Sachs-Wolfe ('tsw' or 'TSW'), early integrated Sachs-Wolfe
     ('eisw' or 'EISW'), late integrated Sachs-Wolfe ('lisw' or 'LISW'),
     Doppler ('dop' or 'Dop'), polarisation contribution ('pol' or 'Pol'). Put
     below the list of terms to be included
     (defaut: if this field is not passed, all terms will be included)

#temperature contributions = tsw, eisw, lisw, dop, pol

1.c) if one of 'eisw' or 'lisw' is turned off, the code will read 'early/late
     isw redshift', the split value of redshift z at which the isw is
     considered as late or early (if this field is absent or left blank, by
     default, 'early/late isw redshift' is set to 50)

#early/late isw redshift =

1.d) if you included 'nCl' (or 'dCl') in the list, you can take into account
     only some of the terms contributing to the obsevable number count
     fluctuation spectrum: matter density ('density'), redshift-space and
     Doppler distortions ('rsd'), lensing ('lensing'), or gravitational
     potential terms ('gr'). Put below the list of terms to be included
     (defaut: if this field is not passed, only 'dens' will be included)

#number count contributions = density, rsd, lensing, gr

1.e) if you included 'dTk' (or 'mTk') in the list, the code will give
you by default the transfer function of the scale-invariant Bardeen
potentials (for whatever gauge you are using). If you need the
transfer function of additional metric fluctuations, specific to the
gauge you are using, set the following flag to 'yes' (default:
set to 'no')

extra metric transfer functions =

2) if you want an estimate of the non-linear P(k) and Cls, enter 'halofit' or
   'Halofit' or 'HALOFIT' for Halofit (non linear); otherwise leave blank
   (default: blank, linear P(k) and Cls)

non linear =

3) if you want to consider perturbed recombination, enter a word containing the
   letter 'y' or 'Y'. CLASS will then compute the perturbation in the
   ionization fraction x_e and the baryon temperature. The initial conformal
   time will be small, therefore you should use the default integrator ndf15
   (i.e. do not set 'evolver' to 0, otherwise the code will be slower).
   (default: neglect perturbed recombination)

#perturbed recombination = yes

4) list of modes ('s' for scalars, 'v' for vectors, 't' for tensors). More than
   one letter allowed, can be attached or separated by arbitrary characters;
   letters can be small or capital.
   (default: set to 's')

modes = s
#modes = s,t

5) relevant only if you ask for 'tCl, lCl' and/or 'pCl, lCl': if you want the
   spectrum of lensed Cls, enter a word containing the letter 'y' or 'Y'
   (default: no lensed Cls)

lensing = yes

6) which perturbations should be included in tensor calculations? write 'exact'
   to include photons, ultra-relativistic species 'ur' and all non-cold dark
   matter species 'ncdm'; write 'massless' to appriximate 'ncdm' as extra
   relativistic species (good approximation if ncdm is still relativistic at
   the time of recombination); write 'photons' to include only photons
   (default: 'massless')

tensor method =

7) list of initial conditions for scalars ('ad' for adiabatic, 'bi' for baryon
   isocurvature, 'cdi' for CDM isocurvature, 'nid' for neutrino density
   isocurvature, 'niv' for neutrino velocity isocurvature). More than one of
   these allowed, can be attached or separated by arbitrary characters; letters
   can be small or capital.
   (default: set to 'ad')

ic = ad
#ic = ad&bi&nid

8) gauge in which calculations are performed: 'sync' or 'synchronous' or
   'Synchronous' for synchronous, 'new' or 'newtonian' or 'Newtonian' for
   Newtonian/longitudinal gauge
   (default: set to synchronous)

gauge = synchronous

---------------------------------------------
----> define primordial perturbation spectra:
---------------------------------------------

1) primordial spectrum type ('analytic_Pk' for an analytic smooth function with amplitude, tilt, running, etc.; analytic spectra with feature can also be added as a new type;'inflation_V' for a numerical computation of the inflationary primordial spectrum, through a full integration of the perturbation equations, given a parametrization of the potential V(phi) in the observable window, like in astro-ph/0703625; 'inflation_H' for the same, but given a parametrization of the potential H(phi) in the observable window, like in astro-ph/0710.1630; 'inflation_V_end' for the same, but given a parametrization of the potential V(phi) in the whole region between the observable part and the end of inflation; there is also an option 'two scales' in order to specify two amplitudes instead of one amplitude and one tilt, like in the isocurvature mode analysis of the Planck inflation paper (works also for adiabatic mode only; see details below, item 2.c); finally 'external_Pk' allows for the primordial spectrum to be computed externally by some piece of code, or to be read from a table, see 2.d). (default: set to 'analytic_Pk')

P_k_ini type = analytic_Pk

2) parameters related to one of the primordial spectrum types (will only be
   read if they correspond to the type selected above)

2.a) for type 'analytic_Pk':

2.a.1) pivot scale in Mpc-1 (default: set to 0.05)

k_pivot = 0.05

2.a.2) scalar adiabatic perturbations: curvature power spectrum value at pivot scale ('A_s' or 'ln10^{10}A_s') OR 'sigma8' (found by iterations using a shooting method), tilt at the same scale 'n_s', and tilt running 'alpha_s' (default: set 'A_s' to 2.215e-9, 'n_s' to 0.9619, 'alpha_s' to 0)

A_s = 2.215e-9
#ln10^{10}A_s = 3.0980
# sigma8 = 0.848365
n_s = 0.9619
alpha_s = 0.

2.a.3) isocurvature/entropy perturbations: for each mode xx ('xx' being one of
       'bi', 'cdi', 'nid', 'niv', corresponding to baryon, cdm, neutrino
       density and neutrino velocity entropy perturbations), enter the
       entropy-to-curvature ratio f_xx, tilt n_xx and running alpha_xx, all
       defined at the pivot scale; e.g.  f_cdi of 0.5 means S_cdi/R equal to
       one half and (S_cdi/R)^2 to 0.25
       (default: set each 'f_xx' to 1, 'n_xx' to 1, 'alpha_xx' to 0)

f_bi = 1.
n_bi = 1.5

f_cdi=1.

f_nid=1.
n_nid=2.
alpha_nid= 0.01

etc.

2.a.4) cross-correlation between different adiabatic/entropy mode: for each
       pair (xx, yy) where 'xx' and 'yy' are one of 'ad', 'bi', 'cdi', 'nid',
       'niv', enter the correlation c_xx_yy (parameter between -1 and 1,
       standing for cosDelta, the cosine of the cross-correlation angle), the
       tilt n_xx_yy of the function cosDelta(k), and its running alpha_xx_yy,
       all defined at the pivot scale. So, for a pair of fully correlated
       (resp. anti-correlated) modes, one should set (c_xx_yy, n_xx_yy,
       alpha_xx_yy) to (1,0,0) (resp. (-1,0,0)
       (default: set each 'c_xx_yy' to 0, 'n_xx_yy' to 0, 'alpha_xx_yy' to 0)

c_ad_bi = 0.5
#n_ad_bi = 0.1

c_ad_cdi = -1.

c_bi_nid = 1.
#n_bi_nid = -0.2
#alpha_bi_nid = 0.002

etc.

2.a.5) tensor mode (if any): tensor-to-scalar power spectrum ratio, tilt,
       running at the pivot scale; if 'n_t' and/or 'alpha_t' is set to 'scc' or
       'SCC' isntead of a numerical value, it will be inferred from the
       self-consistency condition of single field slow-roll inflation: for n_t,
       -r/8*(2-r/8-n_s); for alpha_t, r/8(r/8+n_s-1)
       (default: set 'r' to 1, 'n_t' to 'scc', 'alpha_t' to 'scc')

r = 1.
n_t = scc
alpha_t = scc

2.b) for type 'inflation_V'

2.b.1) type of potential: 'polynomial' for a Taylor expansion of the potential around phi_pivot. Other shapes can easily be defined in primordial module.

potential = polynomial

2.b.2) for 'inflation_V' and 'polynomial': enter either the coefficients 'V_0', 'V_1', 'V_2', 'V_3', 'V_4' of the Taylor expansion (in units of Planck mass to appropriate power), or their ratios 'R_0', 'R_1', 'R_2', 'R_3', 'R_4' corresponding to (128pi/3)*V_0^3/V_1^2, V_1^2/V_0^2, V_2/V_0, V_1*V_3/V_0, V_1^2*V_4/V_0^3, or the potential-slow-roll parameters 'PSR_0', 'PSR_1', 'PSR_2', 'PSR_3', 'PSR_4', equal respectively to R_0, epsilon_V=R_1/(16pi), eta_V=R_2/(8pi), ksi_V=R_3/(8pi)^2, omega_V=R_4/(8pi)^3 (default: 'V_0' set to 1.25e-13, 'V_1' to 1.12e-14, 'V_2' to 6.95e-14, 'V_3' and 'V_4' to zero).

V_0=1.e-13
V_1=-1.e-14
V_2=7.e-14
V_3=
V_4=

#R_0=2.18e-9
#R_1=0.1
#R_2=0.01
#R_3=
#R_4=

#PSR_0 = 2.18e-9
#PSR_1 = 0.001989
#PSR_2 = 0.0003979
#PSR_3 =
#PSR_4 =

2.c) for 'inflation_H': enter either the coefficients 'H_0', 'H_1', 'H_2', 'H_3', 'H_4' of the Taylor expansion (in units of Planck mass to appropriate power), or the Hubble-slow-roll parameters 'HSR_0', 'HSR_1', 'HSR_2', 'HSR_3', 'HSR_4'

H_0=1.e-13
H_1=-1.e-14
H_2=7.e-14
H_3=
H_4=

#HSR_0 = 2.18e-9
#HSR_1 = 0.001989
#HSR_2 = 0.0003979
#HSR_3 =
#HSR_4 =

2.d) for type 'inflation_V_end':

2.d.1) value of the field at the minimum of the potential after inflation, or at a value in which you want to impose the end of inflation, in hybrid-like models. By convention, the code expects inflation to take place for values smaller than this value, with phi increasing with time (using a reflection symmetry, it is always possible to be in that case) (default: 'phi_end' set to 0)

phi_end =

2.d.2) shape of the potential. Refers to functions pre-coded in the primordail module, so far 'polynomial' and 'higgs_inflation'. (default: 'full_potential' set to 0)

full_potential = polynomial

2.d.3) parameters of the potential. The meaning of each parameter is explained in the function primrodial_inflation_potential() in source/primordial.c

Vparam0 =
Vparam1 =
Vparam2 =
Vparam3 =
Vparam4 =

2.d.4) how much the scale factor a or the product (aH) increases between Hubble crossing for the pivot scale (during inflation) and the end of inflation. You can pass either: 'N_star' (standing for log(a_end/a_pivot)) set to a number; or 'ln_aH_ratio' (standing for log(aH_end/aH_pivot)) set to a number; (default: 'N_star' set to 60)

#ln_aH_ratio = 50
#N_star = 55

2.d.5) should the inflation module do its nomral job of numerical integration ('numerical') or use analytical slow-roll formulas to infer the primordial spectrum from the potential ('analytical') (default: 'inflation_behavior' set to 'numerical')

#inflation_behavior = numerical

2.e) for type 'two_scales' (currently this option works only for scalar modes, and either for pure adiabatic modes or adiabatic + one type of isocurvature):

2.e.1) two wavenumbers 'k1' and 'k2' in 1/Mpc, at which primordial amplitude
       parameters will be given. The value of 'k_pivot' will not be used in
       input but quantities at k_pivot will still be calculated and stored in
       the primordial structure (no default value: compulsory input if 'P_k_ini
       type' has been set to 'two_scales')

k1=0.002
k2=0.1

2.e.2) two amplitudes 'P_{RR}^1', 'P_{RR}^2' for the adiabatic primordial
       spectrum (no default value: compulsory input if 'P_k_ini type' has been
       set to 'two_scales')

P_{RR}^1 = 2.3e-9
P_{RR}^2 = 2.3e-9

2.e.3) if one isocurvature mode has been turned on ('ic' set e.g. to 'ad,cdi'
       or 'ad,nid', etc.), enter values of the isocurvature amplitude
       'P_{II}^1', 'P_{II}^2', and cross-correlation amplitude 'P_{RI}^1',
       '|P_{RI}^2|' (see Planck paper on inflation for details on definitions)

P_{II}^1 = 1.e-11
P_{II}^2 = 1.e-11
P_{RI}^1 = -1.e-13
|P_{RI}^2| = 1.e-13

2.e.4) set 'special iso' to 'axion' or 'curvaton' for two particular cases:
       'axion' means uncorrelated, n_ad equal to n_iso, 'curvaton' means fully
       anti-correlated with f_iso<0 (in the conventions of the Planck inflation
       paper this would be called fully correlated), n_iso equal to one; in
       these two cases, the last three of the four paramneters in 2.c.3 will be
       over-written give the input for 'P_{II}^1' (defaut: 'special_iso' left
       blanck, code assumes general case described by four parameters of 2.c.3)

special_iso =

2.f) for type 'external_Pk' (see external documentation external_Pk/README.md
     for more details):

2.f.1) Command generating the table. If the table is already generated, just
       write "cat <table_file>". The table should have two columns (k, pk) if
       tensors are not requested, or three columns (k, pks, pkt) if they are.

#command = python external_Pk/generate_Pk_example.py
#command = python external_Pk/generate_Pk_example_w_tensors.py
command = cat external_Pk/Pk_example.dat
#command = cat external_Pk/Pk_example_w_tensors.dat

2.f.2) If the table is not pregenerated, parameters to be passed to the
       command, in the right order, starting from "custom1" and up to
       "custom10". They must be real numbers.

custom1 = 0.05     # In the example command: k_pivot
custom2 = 2.215e-9 # In the example command: A_s
custom3 = 0.9624   # In the example command: n_s
custom4 = 2e-10    # In the example (with tensors) command: A_t
custom5 = -0.1     # In the example (with tensors) command: n_t
#custom6 = 0
#custom7 = 0
#custom8 = 0
#custom9 = 0
#custom10 = 0

-------------------------------------
----> define format of final spectra:
-------------------------------------

1) maximum l for CLs:
- 'l_max_scalars' for CMB scalars (temperature, polarization, cmb lensing potential),
- 'l_max_tensors' for CMB tensors (temperature, polarization)
- 'l_max_lss'     for Large Scale Structure Cls (density, galaxy lensing potential)
Reducing 'l_max_lss' with respect to l_max_scalars reduces the execution time significantly
(default: set 'l_max_scalars' to 2500, 'l_max_tensors' to 500, 'l_max_lss' to 300)

l_max_scalars = 2500
l_max_tensors = 500
#l_max_lss = 600

2) maximum k in P(k), 'P_k_max_h/Mpc' in units of h/Mpc or 'P_k_max_1/Mpc' in
   units of 1/Mpc. If scalar Cls are also requested, a minimum value is
   automatically imposed (the same as in scalar Cls computation)
   (default: set to 1 1/Mpc)

P_k_max_h/Mpc = 1.
#P_k_max_1/Mpc = 0.7

3) value(s) 'z_pk' of redshift(s) for P(k,z) output file(s); can be ordered
   arbitrarily, but must be separated by comas (default: set 'z_pk' to 0)

z_pk = 0
#z_pk = 0., 1.2, 3.5

4) if the code is interfaced with routines that need to interpolate P(k,z) at
   various values of (k,z), enter 'z_max_pk', the maximum value of z at which
   such interpolations are needed. (default: set to maximum value in above
   'z_pk' input)

#z_max_pk = 10.

6) parameters for the the matter density number count (option 'nCl' (or 'dCl'))
   or galaxy lensing potential (option 'sCl') Cls:

6a) enter here a description of the selection functions W(z) of each
    redshift bin; selection can be set to 'gaussian', 'tophat' or
    'dirac', then pass a list of N mean redshifts in growing order
    separated by comas, 1 or N widths separated by comas, 1 or N bias
    separated by a comma, and 1 or N magnification bias separated by a
    comma. The width stands for one standard deviation of the gaussian
    (in z space), or for the half-width of the top-hat. Finally,
    non_diagonal sets the number of cross-correlation spectra that you
    want to calculate: 0 means only auto-correlation, 1 means only
    adjacent bins, and number of bins minus one means all correlations
    (default: set to 'gaussian',1,0.1,1.,0.,0)

selection=gaussian
selection_mean = 0.98,0.99,1.0,1.1,1.2
selection_width = 0.1
selection_bias =
selection_magnification_bias =
non_diagonal=4

    [note: for good performances, the code uses the Limber approximation for nCl. If you want high precision even with thin selection functions, increase the default value of the precision parameters l_switch_limber_for_nc_local_over_z, l_switch_limber_for_nc_los_over_z; for instance, add them to the input file with values 10000 and 2000, instead of the default 100 and 30]

6b) It is possible to multiply the window function W(z) by a selection function
    'dNdz' (number of objects per redshift interval). Type the name of the file
    containing the redshift in the first column and the number of objects in
    the second column (do not call it 'analytic*'). Set to 'analytic' to use
    instead the analytic expression from arXiv:1004.4640 (this function can be
    tuned in the module transfer.c, in the subroutine transfer_dNdz_analytic).
    Leave blank to use a uniform distribution (default).

dNdz_selection =

6c) It is possible to consider source number counts evolution. Type the name of
    the file containing the redshift on the first column and the number of
    objects on the second column (do not call it 'analytic*'). Set to
    'analytic' to use instead the analytic expression from Eq. 48 of
    arXiv:1105.5292. Leave blank to use constant comoving number densities
    (default).

dNdz_evolution =

7a) file name root 'root' for all output files (if Cl requested, written to
    '<root>cl.dat'; if P(k) requested, written to '<root>pk.dat'; plus similar
    files for scalars, tensors, pairs of initial conditions, etc.; if file with
    input parameters requested, written to '<root>parameters.ini') (default:
    the input module sets automatically 'root' to 'output/<thisfilename>N_',
    where N is the first available integer number, starting from 00, to avoid
    erasing the output of previous runs)

#root = output/test_

7b) do you want headers at the beginning of each output file (giving precisions
    on the output units/ format) ? If 'headers' set to something containing the
    letter 'y' or 'Y', headers written, otherwise not written
    (default: written)

headers = yes

7c) in all output files, do you want columns to be normalized and ordered with
    the default CLASS definitions or with the CAMB definitions (often idential
    to the CMBFAST one) ? Set 'format' to either 'class', 'CLASS', 'camb' or
    'CAMB' (default: 'class')

format = class

7d) Do you want to write a table of background quantitites in a file? This will
    include H, densities, Omegas, various cosmological distances, sound
    horizon, etc., as a function of conformal time, proper time, scale factor.
    File created if 'write background'  set to something containing the letter
    'y' or 'Y', file written, otherwise not written (default: not written)

write background = no

7e) Do you want to write a table of thermodynamics quantitites in a file? File
    is created if 'write thermodynamics' is set to something containing the
    letter 'y' or 'Y'. (default: not written)

write thermodynamics = no

7f) Do you want to write a table of perturbations to files for certain
    wavenumbers k? Dimension of k is 1/Mpc. The actual wave numbers are chosen
    such that they are as close as possible to the requested k-values.

k_output_values = #0.01, 0.1, 0.0001

7g) Do you want to write the primordial scalar(/tensor) spectrum in a file,
    with columns k [1/Mpc], P_s(k) [dimensionless], ( P_t(k) [dimensionless])?
    File created if 'write primordial'  set to something containing the letter
    'y' or 'Y', file written, otherwise not written (default: not written)

write primordial = no

7h) Do you want to have all input/precision parameters which have been read
    written in file '<root>parameters.ini', and those not written in file
    '<root>unused_parameters' ? If 'write parameters' set to something
    containing the letter 'y' or 'Y', file written, otherwise not written
    (default: not written)

write parameters = yeap

7i) Do you want a warning written in the standard output when an input
    parameter or value could not be interpreted ? If 'write warnings' set to
    something containing the letter 'y' or 'Y', warnings written, otherwise not
    written (default: not written)

write warnings =

----------------------------------------------------
----> amount of information sent to standard output:
----------------------------------------------------

Increase integer values to make each module more talkative (default: all set to 0)

input_verbose = 1
background_verbose = 1
thermodynamics_verbose = 1
perturbations_verbose = 1
transfer_verbose = 1
primordial_verbose = 1
spectra_verbose = 1
nonlinear_verbose = 1
lensing_verbose = 1
output_verbose = 1
