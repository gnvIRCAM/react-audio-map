import os 
from absl import app, flags

import json
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import colormaps
from matplotlib.colors import rgb2hex

cmap = colormaps['hsv']
PATH_TO_SAVE = 'frontend/src/assets'

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'path_to_embeddings', 
    None, 
    required=True, 
    help='Path to 2d embeddings (json)'
)

flags.DEFINE_integer(
    'n_clusters', 
    50, 
    required=False, 
    help='Number of clusters'
)

def main(argv):
    with open(FLAGS.path_to_embeddings, 'r') as f:
        embeddings = json.load(f)

    all_embeddings = np.concatenate([np.array(e)[None, ...] for e in embeddings.values()])
    kmeans = KMeans(n_clusters=FLAGS.n_clusters).fit(all_embeddings)
    labels = kmeans.labels_
    labels_norm = [label/(FLAGS.n_clusters-1) for label in labels]
    colors = [cmap(ln) for ln in labels_norm]
    colors = {k: rgb2hex(c, keep_alpha=True) for k, c in zip(embeddings.keys(), colors)}
    clusters = {k : ln for k, ln in zip(embeddings.keys(), labels_norm)}

    with open(os.path.join(PATH_TO_SAVE, 'clusters.json'), 'w') as f:
        json.dump(clusters, f)
        
    with open(os.path.join(PATH_TO_SAVE, 'colors.json'), 'w') as f:
        json.dump(colors, f)

if __name__=='__main__':
    app.run(main)