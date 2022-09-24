# Fitting and Forecasting an Autoregressive processes AR(p)

## Fitting AR(p)

In this project we are working with data from the file 88.csv.

First we compute the periodogram and direct spectral estimate using the 50% cosine taper at the Fourier frequencies.

Then we fit an AR(p) model using the following methods:

1. Yule-Walker (untapered)

2. Yule-Walker (50% cosine tapered)

3. Approximate maximum likelihood

We compare the models using the AIC.

## Forecasting AR(p)

We assume that in fact we only observed values x_1, ..., x_118. We fit and select the model again using approximate maximum likelihood on just the observed values. Then we forecast X_119, ..., X_128 using the selected model and parameter estimates.

Lastly, we produce a 90% confidence interval of our predictions. We will look at a Monte Carlo simulation method of providing these.

If we simulate the innovation terms {x_119, ..., x_128} and iterate the AR model, we can obtain one possible future trajectory of X_119, ..., X_128. Then we repeat this procedure 999 times to get 999 possible trajectories for X_119, ..., X_128. Then, if at each time I take the 50th and 950th largest values of those 999, we can build 90% prediction intervals at times t = 119, ..., 128. That is, a set of intervals which have a 90% chance of containing the true, realised trajectory x119, ..., x128.
