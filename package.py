
name = "graphviz"

version = "2.44.1"

description = "Graphviz - Graph Visualization Software"

url = "https://www.graphviz.org/"

build_command = False


def commands():
    env = globals()["env"]
    env.PATH.append("c:/Graphviz/bin")
