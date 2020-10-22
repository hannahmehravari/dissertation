# Glossary

## Stationarity
In the most intuitive sense, stationarity means that the statistical properties of a process generating a time series do not change over time. It does not mean that the series does not change over time, just that the way it changes does not itself change over time. Such processes should be possible to predict, as the way they change is predictable.

A stationary process has the property that the mean, variance and autocorrelation structure do not change over time.

- [Stationarity in time series analysis](https://towardsdatascience.com/stationarity-in-time-series-analysis-90c94f27322#:~:text=In%20t%20he%20most%20intuitive,not%20itself%20change%20over%20time.)
- [Stationarity and differencing](https://otexts.com/fpp2/stationarity.html)


## Autocorrelation Function / Coefficent
The Autocorrelation function is one of the widest used tools in timeseries analysis. It is used to determine stationarity and seasonality.

## Correlogram
A plot of autocorrelation at lag t (shift by index) against lag t.


## Time Series Patterns
### Trend
A trend exists when there is a long-term increase or decrease in the data. It does not have to be linear.

### Seasonal
A seasonal pattern occurs when a time series is affected by seasonal factors such as the time of the year or the day of the week. Seasonality is always of a fixed and known frequency.

### Cyclic
A cycle occurs when the data exhibit rises and falls that are not of a fixed frequency.

[Time series patterns](https://otexts.com/fpp2/tspatterns.html)


## Seasonal differencing
The seasonal difference of a time series is the series of changes from one season to the next.

[Seasonal differencing](https://faculty.fuqua.duke.edu/~rnau/Decision411_2007/Class10notes.htm)


## Other links:

- [How to Identify and Remove Seasonality from Time Series Data with Python](https://machinelearningmastery.com/time-series-seasonality-with-python/)
