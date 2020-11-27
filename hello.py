from flask import Flask, render_template
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import numpy as np
import pandas as pd

import mpld3
from mpld3 import plugins

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/about/')
def about():
    fig, ax = plt.subplots()

    x = np.linspace(-2, 2, 20)
    y = x[:, None]
    X = np.zeros((20, 20, 4))

    X[:, :, 0] = np.exp(- (x - 1) ** 2 - (y) ** 2)
    X[:, :, 1] = np.exp(- (x + 0.71) ** 2 - (y - 0.71) ** 2)
    X[:, :, 2] = np.exp(- (x + 0.71) ** 2 - (y + 0.71) ** 2)
    X[:, :, 3] = np.exp(-0.25 * (x ** 2 + y ** 2))

    im = ax.imshow(X, extent=(10, 20, 10, 20),
                   origin='lower', zorder=1, interpolation='nearest')
    fig.colorbar(im, ax=ax)

    ax.set_title('An Image', size=20)
    plugins.connect(fig, plugins.MousePosition(fontsize=14))

    return render_template('about.html', plot=mpld3.fig_to_html(fig))

if __name__ == '__main__':
    app.run(debug=True, port='8080')