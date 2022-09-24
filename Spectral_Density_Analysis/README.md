# Spectral Density Analysis

First we write a function that computes the (theoretical) spectral density function for an ARMA(p, q) process. 

Then we simulate a Gaussian ARMA(2,2) process of length N. The function will use a burn in method, i.e. set X_1 = X_2 = 0, and
X_t = φ_1,2 X_t−1 + φ_2,2 X_t−2 + epsilon_t − theta_1,2 epsilon_t−1 − theta_2,2 epsilon_t−2 for t > 2. The function should then discard the first 100 values so that it reaches an (approx.) stationary state. Return X_101, ..., X_101+N as the time series of length N.

Using the Fast Fourier Transform algorithm, we compute the periodogram and the direct spectral estimate using a p100% cosine taper.

Finally, we examine the pseudo-cyclical behaviour of an ARMA process.
