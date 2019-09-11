CLASS: Cosmic Linear Anisotropy Solving System  {#oringally forked from main page}
==============================================

Authors: Julien Lesgourgues and Thomas Tram

Originally forked from https://github.com/lesgourg/class_public

Modifications:
Enable G, Newton's graviataional constant to be a function of time (scale factor a).
-------
Add variable mu_of_a, with mu defined as G_at_a/G_Newton.
mu_of_a is a smoothed step function.
Input parameters are : mu_0, mu_inf, a_T, delta_T.

mu_inf is mu at infinite z. a_T sets the transition scale factor. delta_T is the width of step in log(a).

