# Bayesian Generalized Linear Models (GLMs)
import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm

from pymc3 import *

print(f"Running on PyMC3 v{pm.__version__}")

# Generating Data
size = 200
true_intercept = 1
true_slope = 2

x = np.linspace(0, 1, size)
# y = a + b*x
true_regression_line = true_intercept + true_slope * x
# add noise
y = true_regression_line + np.random.normal(scale=0.5, size=size)

data = dict(x=x, y=y)


# Plotting Data
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, xlabel="x", ylabel="y", title="Generated data and underlying model")
ax.plot(x, y, "x", label="sampled data")
ax.plot(x, true_regression_line, label="true regression line", lw=2.0)
plt.legend(loc=0)

#Estimating the Model
with Model() as model:
    # specify glm and pass in data. The resulting linear model, its likelihood and
    # and all its parameters are automatically added to our model.
    GLM.from_formula("y ~ x", data)
    trace = pm.sample(1000, cores=1)  # draw 3000 posterior samples using NUTS sampling


# Analyzing the model
# bayesian inference gives a whole posterior distribution of likely parameters
# thus we basically have many fitting regression lines instead of just one
az.plot_trace(trace)
plt.tight_layout()
plt.show()

# a posterior prediction [P(y|x)] plot takes multiple samples from the posterior
# and plots a regression line for each of them
plt.figure(figsize=(7, 7))
plt.plot(x, y, "x", label="data")
plot_posterior_predictive_glm(trace, samples=100, label="posterior predictive regression lines")
plt.plot(x, true_regression_line, label="true regression line", lw=3.0, c="y")

plt.title("Posterior predictive regression lines")
plt.legend(loc=0)
plt.xlabel("x")
plt.ylabel("y")
plt.show()