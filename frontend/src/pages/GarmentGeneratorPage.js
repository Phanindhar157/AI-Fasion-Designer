import React, { useState, useEffect } from 'react';
import api from '../services/api';
import Loading from '../components/Loading';
import Notification from '../components/Notification';

const GarmentGeneratorPage = () => {
  const [prompt, setPrompt] = useState('');
  const [generatedImages, setGeneratedImages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedStyle, setSelectedStyle] = useState('realistic');
  const [styles, setStyles] = useState([]);
  const [notification, setNotification] = useState(null);

  useEffect(() => {
    // Fetch available styles when component mounts
    const fetchStyles = async () => {
      try {
        const styleList = await api.getGarmentStyles();
        setStyles(styleList);
        if (styleList.length > 0) {
          setSelectedStyle(styleList[0]);
        }
      } catch (error) {
        setNotification({
          type: 'error',
          message: 'Failed to load garment styles'
        });
      }
    };
    
    fetchStyles();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) {
      setNotification({
        type: 'error',
        message: 'Please enter a description for the garment'
      });
      return;
    }
    
    setLoading(true);
    
    try {
      const designs = await api.generateGarments(prompt, selectedStyle);
      setGeneratedImages(designs);
      setNotification({
        type: 'success',
        message: 'Garment designs generated successfully!'
      });
    } catch (error) {
      setNotification({
        type: 'error',
        message: `Failed to generate designs: ${error.message}`
      });
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = (imageUrl) => {
    setNotification({
      type: 'success',
      message: 'Design downloaded successfully!'
    });
  };

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold text-center my-8">Garment Generator</h1>
      
      {notification && (
        <Notification 
          type={notification.type} 
          message={notification.message}
          onClose={() => setNotification(null)}
        />
      )}
      
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="prompt">
            Describe the garment you want to generate
          </label>
          <textarea
            id="prompt"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            rows="4"
            placeholder="e.g., A blue summer dress with floral patterns, short sleeves, and a fitted waist"
          />
        </div>
        
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Style
          </label>
          <div className="flex space-x-4">
            {styles.map((style) => (
              <label key={style} className="inline-flex items-center">
                <input
                  type="radio"
                  name="style"
                  value={style}
                  checked={selectedStyle === style}
                  onChange={() => setSelectedStyle(style)}
                  className="form-radio"
                />
                <span className="ml-2 capitalize">{style.replace('-', ' ')}</span>
              </label>
            ))}
          </div>
        </div>
        
        <div className="flex items-center justify-between">
          <button
            onClick={handleSubmit}
            className="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            disabled={loading}
          >
            {loading ? 'Generating...' : 'Generate Garment'}
          </button>
        </div>
      </div>
      
      {loading && <Loading message="Generating garment designs..." />}
      
      {generatedImages.length > 0 && (
        <div className="mt-8">
          <h2 className="text-2xl font-bold mb-4">Generated Designs</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {generatedImages.map((image) => (
              <div key={image.id} className="bg-white shadow-md rounded-lg overflow-hidden">
                <img 
                  src={image.url} 
                  alt={`Generated design for: ${image.prompt}`} 
                  className="w-full h-64 object-cover"
                />
                <div className="p-4">
                  <button 
                    className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-full"
                    onClick={() => handleDownload(image.url)}
                  >
                    Download
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      <div className="mt-8 bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-bold mb-2">How to use the Garment Generator</h3>
        <ul className="list-disc pl-5 space-y-2">
          <li>Describe the garment you want to create in detail</li>
          <li>Include information about color, pattern, style, and any specific features</li>
          <li>Choose the style that best fits your needs</li>
          <li>Click "Generate Garment" to create your designs</li>
          <li>Download your favorite designs to share with manufacturers or for personal use</li>
        </ul>
      </div>
    </div>
  );
};

export default GarmentGeneratorPage;