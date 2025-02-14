import './App.css';
import React, {useEffect, useState} from 'react'; 
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import embs from './assets/tsne_embeddings_2d.json'
import clusters from './assets/clusters.json'
import colorsJson from './assets/colors.json'

function App() {

  const allColors = Object.values(colorsJson);
  const uniqueColors = Array.from(new Set(allColors));

  const allClusters = Object.values(clusters);
  const uniqueClusters = Array.from(new Set(allClusters));

  const [soundPath, setSoundPath] = useState(); 
  const [data, setData] = useState(Object.entries(embs).map(([key, pos]) => ({ x: pos[0], y: pos[1], z: clusters[key], id: key})));

  const[serverURL, setServerURL] = useState('http://127.0.0.1:5000'); 

  const setSelectedSound = (event, params) => {
    setSoundPath(data[params.dataIndex].id)
  } 

  useEffect(() => {
    const postFile = async () => {
      try {
        const res = await fetch(serverURL+'/play', 
          {method: 'POST', 
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
              'Access-Control-Allow-Headers': 'Content-Type',

            }, 
           body: JSON.stringify(
            {'filename': soundPath, 'test': 'test_yooooo'}
           )
          }
        );
    // const result = await Response;  
                    
          }
      catch (error) {
        console.error(error);
      }
  }
  postFile()
}, [soundPath])

  return (
    <div 
      className="App"
      style={{ backgroundColor: '#0a0a0a'}}
      >
      {/* <h1>{soundPath}</h1> */}
      <ScatterChart 
        width={2000}
        height={2000}
        series={[
          {
            label: 'embeddings',
            data: data,
            valueFormatter: (v) => {
              return `${v.id}.`;
            },
          }]}
        onItemClick={setSelectedSound}
        zAxis={[{
          colorMap: {
            type: 'ordinal',
            values: uniqueClusters,
            colors: uniqueColors
          }
          
        }]}
      />
    </div>

  );
}

export default App;


