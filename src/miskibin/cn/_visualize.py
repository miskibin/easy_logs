import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
from itertools import combinations
from collections.abc import Callable


def create_random_edges(nodes, number_of_neighbors: float) -> nx.Graph:
    """
    Creates edges between nodes in a graph based on the type of connection
    nodes: list of nodes
    number_of_neighbors: approx number of neighbors to connect to
    OUTDATED number_of_neighbors: is counted not correctly
    """
    while True:
        G = nx.Graph()
        G.add_nodes_from(nodes)
        k = number_of_neighbors / len(G.nodes())
        pairs = list(combinations(G.nodes(), 2))
        edges = []
        for pair in pairs:
            if np.random.random() <= k and pair[::-1] not in pairs:
                edges.append(pair)
        G.remove_edges_from(G.edges())
        G.add_edges_from(edges)
        if nx.is_connected(G):
            return G


def spread(G: nx.Graph, infected_nodes: list[int], k: float) -> list[int]:
    """
    G: networkx graph
    infected_nodes: list of nodes
    k: probability of infecting a node
    """

    new_infected_nodes = []
    for node in infected_nodes:
        neighbors = list(G.neighbors(node))
        for node in G.nodes:
            if node in neighbors and np.random.random() < k:
                new_infected_nodes.append(node)
    return list(set(infected_nodes + new_infected_nodes))


class AnimatedGraph:
    def __init__(
        self,
        G: nx.Graph,
        infected_nodes: list,
        spread_func: Callable[[nx.Graph, float], nx.Graph],
        k: float = 1,
    ) -> None:
        """
        Creates an animated plot of the spread of a disease in a network.
        Args:
            `G`: networkx graph
            `infected_nodes`: list of infected nodes
            `spread_func`: function that spreads the infection
            `k` (optional): probability of infecting a node (can be used in spread_func)
        Note:
            `spread_func`
            args:
                `nx.graph`: networkx graph
                `infected_nodes`: list of infected nodes
                `k` (optional): probability of infecting a node
            returns:
                `infected_nodes`: list of infected nodes + new infected nodes
        example:
            >>> nodes = list(range(90))
            >>> G = create_random_edges(nodes, 3)
            >>> plot = AnimatedGraph(G, [0], spread, k=0.5)
            >>> plot(frames=10, interval=1000)
        """
        self.G = G
        self.N = len(G)
        self.pos = nx.spring_layout(G)
        self.infected_nodes = infected_nodes
        self.fig, self.ax = plt.subplots(figsize=(9, 7))
        self.k = k
        self.real_iterations = 0
        self.spread_func = spread_func

    def __update(self, num: int) -> None:
        if len(self.infected_nodes) == self.N:
            self.ax.set_title(
                f"All nodes infected in {self.real_iterations + 1} iterations"
            )
            return
        self.ax.clear()

        if num > 0:
            self.infected_nodes = self.spread_func(self.G, self.infected_nodes, self.k)
        nx.draw(
            self.G,
            pos=self.pos,
            ax=self.ax,
            with_labels=True,
            node_color="blue",
            edge_color="red",
        )
        nx.draw_networkx_nodes(
            self.G,
            pos=self.pos,
            ax=self.ax,
            nodelist=self.infected_nodes,
            node_color="red",
        )
        self.real_iterations = num
        self.ax.set_title(f"Iteration {num + 1}")
        self.ax.legend(["Healthy", "", "Infected"])

    def __call__(self, frames: int = 10, interval: int = 1000) -> None:

        """
        frames: number of frames to animate
        interval: time between frames in milliseconds (default 1000)
        """
        ani = animation.FuncAnimation(
            self.fig, self.__update, frames=frames, interval=interval, repeat=False
        )
        plt.show()
