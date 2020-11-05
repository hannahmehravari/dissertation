# Forcecasting Models

## Autoregressive integrated moving average (ARIMA) model
### Inputs
- The number of lag observations included in the model, also called the lag order.
- The number of times that the raw observations are differenced, also called the degree of differencing.
- The size of the moving average window, also called the order of moving average.
- Differenced time series to remove trend and seasonal structures
### Python Library
- [statsmodels](https://pypi.org/project/statsmodels/).tsa.arima_model.[ARIMA](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.html)


## Autoregressive conditional heteroskedasticity (ARCH) model
### Inputs
- Prewhitened residual series that is uncorrelated and contains no trends or seasonal changes
- The number of lag squared residual errors
### Python library
- [arch](https://pypi.org/project/arch/)
## Generalized autoregressive conditional heteroskedasticity (GARCH) model
### Inputs
- The number of lag variances
- The number of lag residual errors
- Does the time series have to be prewhitened ?
### Python library
- [arch](https://pypi.org/project/arch/)


## Autoregressive (AR) model
## Autoregressive–moving-average (ARMA) model
## Moving-average (MA) model
