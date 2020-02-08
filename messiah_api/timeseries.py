
def timeseries():
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from random import random
    import matplotlib.pyplot as plt
    # contrived dataset
    data = [100*random() for x in range(1, 100)]
    length = [x for x in range(1, 100)]
    length1 = [x for x in range(101, 112)]
    # fit model
    alpha = 0.5
    beta = 0.5
    gamma = 0.5
    fit1 = ExponentialSmoothing(data, seasonal_periods=4, trend='add', seasonal='add').fit(smoothing_level=alpha, smoothing_slope=beta,
smoothing_seasonal=gamma)
    yhat1 = fit1.predict(len(data), len(data)+10)
    #print(yhat)
    #print(length)
    plt.plot(length, data)
    plt.plot(length1, yhat1, 'r')
    #plt.plot(length1, yhat2, 'b')
    #plt.plot(length1, yhat3, 'g')
    #plt.plot(length1, yhat4, 'y')
    plt.savefig("mygraph.png")
    #plt.plot(yhat.index, yhat, label='Test')
timeseries()
