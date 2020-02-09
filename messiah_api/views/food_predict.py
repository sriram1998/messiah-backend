def foodpredict(data):
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from random import random
    import matplotlib.pyplot as plt
    alpha = 0.3
    beta = 0.6
    gamma = 0.8
    #fit1 = ExponentialSmoothing(data, seasonal_periods=4, trend='add', seasonal='add').fit(smoothing_level=alpha, smoothing_slope=beta,
#smoothing_seasonal=gamma)
    fit1 = ExponentialSmoothing(data,seasonal_periods=2, trend='add', seasonal='add').fit()
    yhat = fit1.predict(len(data), len(data)+10) 
    for i in range(0,len(yhat)):
        yhat[i]=int(yhat[i])
    print(yhat)
    print(type(data))
    print(list(yhat))
    # dict1 = {"data": yhat}
    return list(yhat)

    