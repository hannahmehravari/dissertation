# Glossary

## Stationarity
In the most intuitive sense, stationarity means that the statistical properties of a process generating a time series do not change over time. It does not mean that the series does not change over time, just that the way it changes does not itself change over time. Such processes should be possible to predict, as the way they change is predictable.

A stationary time series is one whose properties do not depend on the time at which the series is observed.Thus, time series with trends, or with seasonality, are not stationary.

A stationary process has the property that the mean, variance and autocorrelation structure do not change over time.

- [Stationarity in time series analysis](https://towardsdatascience.com/stationarity-in-time-series-analysis-90c94f27322#:~:text=In%20t%20he%20most%20intuitive,not%20itself%20change%20over%20time.)
- [Stationarity and differencing](https://otexts.com/fpp2/stationarity.html)

### White Noise
A white noise series is stationary — it does not matter when you observe it, it should look much the same at any point in time.

## Autocorrelation Function / Coefficent
The Autocorrelation function is one of the widest used tools in timeseries analysis. It is used to determine stationarity and seasonality.
ACF plot is also useful for identifying non-stationary time series. For a stationary time series, the ACF will drop to zero relatively quickly, while the ACF of non-stationary data decreases slowly. Also, for non-stationary data, the value of ACF(lag=1) is often large and positive.

## Correlogram
A plot of autocorrelation at lag t (shift by index) against lag t.

## Time Series Patterns
### Trend
A trend exists when there is a long-term increase or decrease in the data. It does not have to be linear.

### Seasonal
A seasonal pattern occurs when a time series is affected by seasonal factors such as the time of the year or the day of the week. Seasonality is always of a fixed and known frequency.

#### Seasonal Stationary
A time series where the seasonal component has been removed is called seasonal stationary. A time series with a clear seasonal component is referred to as non-stationary.

#### Seasonal Adjustment / Deseasonalizing
Once seasonality is identified, it can be modeled. The model of seasonality can be removed from the time series. This process is called Seasonal Adjustment, or Deseasonalizing.

### Cyclic
A cycle occurs when the data exhibit rises and falls that are not of a fixed frequency.
A time series with cyclic behaviour (but with no trend or seasonality) is stationary. This is because the cycles are not of a fixed length, so before we observe the series we cannot be sure where the peaks and troughs of the cycles will be.

[Time series patterns](https://otexts.com/fpp2/tspatterns.html)

## Differencing
### Differenced time series
The differenced series is the change between consecutive observations in the original series. The differenced series will have only `len(original_ts) - 1` values, since it is not possible to calculate a difference for the first observation `original_ts[0]`

To distinguish seasonal differences from ordinary differences, we sometimes refer to ordinary differences as “first differences”.

### Seasonal differencing
The seasonal difference of a time series is the series of changes from one season to the next.
If there is a seasonal component at the level of one week, the seasonal difference is the observation of today minus the observation of this day last week.

[Seasonal differencing](https://faculty.fuqua.duke.edu/~rnau/Decision411_2007/Class10notes.htm)

### Random Walk Model
When the differenced series is white noise, the model for the original series can be written as
yt−yt−1=εt, where εt denotes white noise. Rearranging this leads to the “random walk” model:
yt=yt−1+εt

The forecasts from a random walk model are equal to the last observation, as future movements are unpredictable, and are equally likely to be up or down. Thus, the random walk model underpins naïve forecasts.

### Drift Model
Related to the random walk model, allows the differences to have a non-zero mean. Then
yt−yt−1=c+εt  or yt=c+yt−1+εt

The value of c is the average of the changes between consecutive observations. If c is positive, then the average change is an increase in the value of  yt. Thus,  
yt will tend to drift upwards. However, if c is negative, yt will tend to drift downwards.

### Second Order Differencing
Occasionally the differenced data will not appear to be stationary and it may be necessary to difference the data a second time to obtain a stationary series:
y′′t=y′t−y′t−1
=(yt−yt−1)−(yt−1−yt−2)
=yt−2yt−1+yt−2

In this case, y′′t will have T−2 values. Then, we would model the “change in the changes” of the original data. In practice, it is almost never necessary to go beyond second-order differences.

### Unit root tests
One way to determine more objectively whether differencing is required is to use a unit root test. These are statistical hypothesis tests of stationarity that are designed for determining whether differencing is required.

Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test is one of these. In this test, the null hypothesis is that the data are stationary, and we look for evidence that the null hypothesis is false. Consequently, small p-values (e.g., less than 0.05) suggest that differencing is required. 

This process of using a sequence of KPSS tests to determine the appropriate number of first differences is carried out by the function [ndiffs()](http://alkaline-ml.com/pmdarima/1.5.1/modules/generated/pmdarima.arima.ndiffs.html).


## Other links:

- [How to Identify and Remove Seasonality from Time Series Data with Python](https://machinelearningmastery.com/time-series-seasonality-with-python/)
