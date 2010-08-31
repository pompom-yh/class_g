/** @file class.c 
 * Julien Lesgourgues, 18.04.2010    
 */
 
#include "class.h"

main(int argc, char **argv) {

  struct precision pr;        /* for precision parameters */
  struct background ba;       /* for cosmological background */
  struct thermo th;           /* for thermodynamics */
  struct perturbs pt;         /* for source functions */
  struct bessels bs;          /* for bessel functions */
  struct transfers tr;        /* for transfer functions */
  struct primordial pm;       /* for primordial spectra */
  struct spectra sp;          /* for output spectra */
  struct output op;          /* for output files */
 
  ErrorMsg errmsg;

  if (input_init_from_arguments(argc,argv,&pr,&ba,&th,&pt,&bs,&tr,&pm,&sp,&op,errmsg) == _FAILURE_) {
    printf("\n\nError running input_init_from_arguments \n=>%s\n",errmsg); 
    return _FAILURE_;
  }

  if (background_init(&pr,&ba) == _FAILURE_) {
    printf("\n\nError running background_init \n=>%s\n",ba.error_message);
    return _FAILURE_;
  }

  if (thermodynamics_init(&pr,&ba,&th) == _FAILURE_) {
    printf("\n\nError in thermodynamics_init \n=>%s\n",th.error_message);
    return _FAILURE_;
  }

  /********************************************/
  /***** output thermodynamics quantities *****/
  /********************************************/
  
  int i;

  printf("#1: redshift z\n");
  printf("#2: electron ionization fraction x_e\n");
  printf("#3: Thomson scattering rate kappa'\n");
  printf("#4: Thomson scattering rate derivative kappa''\n");
  printf("#5: exponential of optical depth e^-kappa\n");
  printf("#6: visibility function g=kappa' e^-kappa \n");
  printf("#7: squared baryon sound speed c_b^2 \n");
  for (i=0; i < th.tt_size; i++)
    printf("%e %e %e %e %e %e %e\n",
	   th.z_table[i],
	   th.thermodynamics_table[i*th.th_size+th.index_th_xe],
	   th.thermodynamics_table[i*th.th_size+th.index_th_dkappa],
	   th.thermodynamics_table[i*th.th_size+th.index_th_ddkappa],
	   th.thermodynamics_table[i*th.th_size+th.index_th_exp_m_kappa],
	   th.thermodynamics_table[i*th.th_size+th.index_th_g],
	   th.thermodynamics_table[i*th.th_size+th.index_th_cb2]
	   );

  /********************************************/

  if (thermodynamics_free(&th) == _FAILURE_) {
    printf("\n\nError in thermodynamics_free \n=>%s\n",th.error_message);
    return _FAILURE_;
  }

  if (background_free(&ba) == _FAILURE_) {
    printf("\n\nError in background_free \n=>%s\n",ba.error_message);
    return _FAILURE_;
  }

}
