from statsmodels.tsa.arima_model import ARIMA

class PredictionMaker:
    def __init__(self, time_step=1, p=1, q=1, d=0):
        self.time_step = time_step
        self.p = p
        self.q = q
        self.d = d 

    def make_prediction(training_data):
        model = ARIMA(training_data, order=(self.p, self.q, self.d))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast(self.time_step)
        yhat = output[0].flatten()[0]
        return yhat
