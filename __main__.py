#! /usr/bin/python

from flask import Flask, render_template, request
import math
import ui_settings

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():

    def calculate_line_angle(x1, y1, x2, y2):
        dy = y2 - y1
        dx = x2 - x1
        theta = math.atan2(dy, dx)
        theta = theta * 180 / math.pi
        if (theta < 0):
            theta = 360 + theta;
        return theta

    if request.method == 'POST':
        #TODO busca a*
        return render_template('index.html', nodes=ui_settings.nodes, edges=ui_settings.edges, routes=ui_settings.routes, graph_settings=ui_settings.graph_settings, calculate_line_angle=calculate_line_angle)
    else:
        return render_template('index.html', nodes=ui_settings.nodes, edges=ui_settings.edges, routes=ui_settings.routes, graph_settings=ui_settings.graph_settings, calculate_line_angle=calculate_line_angle)


if __name__ == "__main__":
    app.run(debug=True)