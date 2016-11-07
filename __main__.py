#! /usr/bin/python

from flask import Flask, render_template, request
import math

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

    graph_settings = {
        "node_radius": "25",
        "node_background_color" : "#2196F3",
        "node_text_color" : "#fff",
        "node_danger_background_color" : "#c30e0e",
        "node_stroke_color": "#0D47A1",
        "node_stroke_width": "4",
        "edge_stroke_color": "#1A237E",
        "edge_stroke_width": "5",
        "user_node_background_color": "#00b159",
        "user_node_stroke_color": "#333",
        "user_node_stroke_width": "2",
        "user_node_radius" : "10"
    }

    nodes = [
        { "id":  0, "x": 129, "y": 274, "danger" : 0 },
        { "id":  1, "x": 338, "y": 274, "danger" : 0 },
        { "id":  2, "x": 132, "y": 604, "danger" : 0 },
        { "id":  3, "x": 298, "y": 591, "danger" : 0  },
        { "id":  4, "x": 338, "y": 400, "danger" : 0 },
        { "id":  5, "x": 488, "y": 505, "danger" : 1 },
        { "id":  6, "x": 673, "y": 137, "danger" : 0 },
        { "id":  7, "x": 631, "y": 342, "danger" : 1 },
        { "id":  8, "x": 647, "y": 463, "danger" : 0 },
        { "id":  9, "x": 595, "y": 595, "danger" : 0 },
        { "id": 10, "x": 767, "y": 192, "danger" : 0 },
        { "id": 11, "x": 768, "y": 325, "danger" : 0 },
        { "id": 12, "x": 795, "y": 432, "danger" : 12 },
        { "id": 13, "x": 821, "y": 593, "danger" : 0 },
        { "id": 14, "x": 950, "y": 200, "danger" : 0 },
        { "id": 15, "x": 900, "y": 450, "danger" : 0 }
    ]

    edges = [
        { "id": "edge-0-1", "source": nodes[0], "target" : nodes[1], "distance": 4 },
        { "id": "edge-0-2", "source": nodes[0], "target" : nodes[2], "distance": 12 },
        { "id": "edge-2-3", "source": nodes[2], "target" : nodes[3], "distance": 2 },
        { "id": "edge-1-4", "source": nodes[1], "target" : nodes[4], "distance": 2 },
        { "id": "edge-1-6", "source": nodes[1], "target" : nodes[6], "distance": 12 },
        { "id": "edge-1-7", "source": nodes[1], "target" : nodes[7], "distance": 8 },
        { "id": "edge-4-7", "source": nodes[4], "target" : nodes[7], "distance": 8 },
        { "id": "edge-4-5", "source": nodes[4], "target" : nodes[5], "distance": 4 },
        { "id": "edge-3-5", "source": nodes[3], "target" : nodes[5], "distance": 5 },
        { "id": "edge-5-9", "source": nodes[5], "target" : nodes[9], "distance": 2 },
        { "id": "edge-9-8", "source": nodes[9], "target" : nodes[8], "distance": 2 },
        { "id": "edge-8-13", "source": nodes[8], "target" : nodes[13], "distance": 6 },
        { "id": "edge-13-12", "source": nodes[13], "target" : nodes[12], "distance": 4 },
        { "id": "edge-12-15", "source": nodes[12], "target" : nodes[15], "distance": 0.5 },
        { "id": "edge-15-14", "source": nodes[15], "target" : nodes[14], "distance": 10 },
        { "id": "edge-14-10", "source": nodes[14], "target" : nodes[10], "distance": 1 },
        { "id": "edge-10-11", "source": nodes[10], "target" : nodes[11], "distance": 2 },
        { "id": "edge-7-11", "source": nodes[7], "target" : nodes[11], "distance": 1 },
        { "id": "edge-7-12", "source": nodes[7], "target" : nodes[12], "distance": 4 },
        { "id": "edge-6-10", "source": nodes[6], "target" : nodes[10], "distance": 2 }
    ]

    routes = [
        { "id": "route-1", "edges" : [edges[0], edges[1], edges[3], edges[7]], "color": "#ffd700" },
        { "id": "route-2", "edges" : [edges[2], edges[8], edges[9]], "color": "#ff0000" },
        { "id": "route-3", "edges" : [edges[4], edges[19]], "color": "#660066" },
        { "id": "route-4", "edges" : [edges[5], edges[18]], "color": "#008000" },
        { "id": "route-5", "edges" : [edges[6], edges[17], edges[16], edges[15]], "color": "#ffa500" },
        { "id": "route-6", "edges" : [edges[10], edges[11], edges[12], edges[13], edges[14]], "color": "#00ff00" }
    ]

    if request.method == 'POST':
        #TODO busca a*
        return render_template('index.html', nodes=nodes, edges=edges, routes=routes, graph_settings=graph_settings, calculate_line_angle=calculate_line_angle)
    else:
        return render_template('index.html', nodes=nodes, edges=edges, routes=routes, graph_settings=graph_settings, calculate_line_angle=calculate_line_angle)


if __name__ == "__main__":
    app.run()
