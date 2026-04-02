from utils import *
from graph_generation import *
from algos import *

m = load_mtx_mat("donnees/polblogs/polblogs.mtx")
S = spectral_partition_fast(m)
g = mat_to_graph(m)
renderGraph(g, "blogs_partition", S)