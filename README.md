# react-audio-map
Display a 2d map of audio samples in your browser !

# Instructions
Warning : all instructions assume you are in the root directory of this repo.

First step : install the python dependencies by running : 
```bash
pip install -r requirements.txt
```

Second step : Compute the clusters from the precomputed map :
```bash
python compute_clusters.py --path_to_embeddings path/to/embeddings_2d.json --n_clusters 20
```

Third step : move the precomputed map into the ```assets``` folder :
```bash
mv /path/to/embeddings_2d.json frontend/src/assets/
```

Fourth step : run the Flask server:
```bash
python server/server.py
```

Last step : run the React app:
```bash
cd frontend
npm i 
npm start
```

If you want to use another map (for instance, using a UMAP instead of t-SNE), you will have to change the variable ```embs``` within the ```frontend/src/App.jsx``` to the correct location (note that the json file must be in the ```assets``` directory of the React app). Note that you will have to recompute the clusters, following the above steps.