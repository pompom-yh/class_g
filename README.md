CLASS: Cosmic Linear Anisotropy Solving System  
==============================================

Authors: Julien Lesgourgues and Thomas Tram

Originally forked from https://github.com/lesgourg/class_public

Modifications:
Enable G, Newton's graviataional constant to be a function of time (scale factor a).
-------
Add variable mu_of_a, with mu defined as the ratio G_at_a/G_Newton.

mu_of_a is a smoothed step function.

New input parameters are : mu_0, mu_inf, a_T, delta_T.

mu_0 is the gravity ratio today; mu_inf is mu at infinit redshift or a=0. a_T sets the transition scale factor. delta_T is the width of the step in log(a).

