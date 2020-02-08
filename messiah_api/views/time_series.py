def timeseries(data):
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from random import random
    import matplotlib.pyplot as plt
    alpha = 0.5
    beta = 0.5
    gamma = 0.5
    fit1 = ExponentialSmoothing(data, seasonal_periods=4, trend='add', seasonal='add').fit(smoothing_level=alpha, smoothing_slope=beta,
smoothing_seasonal=gamma)
    yhat1 = fit1.predict(len(data), len(data)+10)
    print(yhat)
    return yhat

    