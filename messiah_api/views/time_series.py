def timeseries(data):
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from random import random
    import matplotlib.pyplot as plt
    # contrived dataset
     #[x + random() for x in range(1, 100)]
    # fit model
    model = ExponentialSmoothing(data)
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(data), len(data)+10)
    print(yhat)
    return yhat
    