import React, { useState, useEffect } from 'react';
import api from '../services/api';
import Loading from '../components/Loading';
import Notification from '../components/Notification';

const CapsuleGeneratorPage = () => {
  const [theme, setTheme] = useState('');
  const [items, setItems] = useState([]);
  const [outfits, setOutfits] = useState([]);
  const [loading, setLoading] = useState(false);
  const [themes, setThemes] = useState([]);
  const [notification, setNotification] = useState(null);

  useEffect(() => {
    // Fetch available themes when component mounts
    const fetchThemes = async () => {
      try {
        const themeList = await api.getCapsuleThemes();
        setThemes(themeList);
        if (themeList.length > 0) {
          setTheme(themeList[0].id);
        }
      } catch (error) {
        setNotification({
          type: 'error',
          message: 'Failed to load capsule themes'
        });
      }
    };
    
    fetchThemes();
  }, []);

  const handleGenerate = async () => {
    if (!theme) {
      setNotification({
        type: 'error',
        message: 'Please select a theme'
      });
      return;
    }
    
    setLoading(true);
    
    try {
      const response = await api.generateCapsule(theme, {});
      setItems(response.wardrobe_items);
      setOutfits(response.outfits);
      setNotification({
        type: 'success',
        message: 'Capsule wardrobe generated successfully!'
      });
    } catch (error) {
      setNotification({
        type: 'error',
        message: `Failed to generate capsule wardrobe: ${error.message}`
      });
    } finally {
      setLoading(false);
    }
  };

  const handleSaveOutfit = (outfitId) => {
    setNotification({
      type: 'success',
      message: `Outfit #${outfitId} saved successfully!`
    });
  };

  return (
    <div className="max-w-6xl mx-auto p-4">
      <h1 className="text-3xl font-bold text-center my-8">Capsule Wardrobe Generator</h1>
      
      {notification && (
        <Notification 
          type={notification.type} 
          message={notification.message}
          onClose={() => setNotification(null)}
        />
      )}
      
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div className="mb-6">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Select a Capsule Wardrobe Theme
          </label>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {themes.map((t) => (
              <div 
                key={t.id}
                className={`border rounded-lg p-4 cursor-pointer ${theme === t.id ? 'border-blue-500 bg-blue-50' : 'border-gray-200'}`}
                onClick={() => setTheme(t.id)}
              >
                <h3 className="font-bold text-lg">{t.name}</h3>
                <p className="text-gray-600 text-sm">{t.description}</p>
              </div>
            ))}
          </div>
        </div>
        
        <div className="flex items-center justify-between">
          <button
            onClick={handleGenerate}
            className="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            disabled={loading}
          >
            {loading ? 'Generating...' : 'Generate Capsule Wardrobe'}
          </button>
        </div>
      </div>
      
      {loading && <Loading message="Generating capsule wardrobe..." />}
      
      {items.length > 0 && (
        <div className="mt-8">
          <h2 className="text-2xl font-bold mb-4">Your Capsule Wardrobe Items</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            {items.map((item) => (
              <div key={item.id} className="bg-white shadow-md rounded-lg p-4 border border-gray-200">
                <h3 className="font-bold">{item.name}</h3>
                <p className="text-gray-600 text-sm">{item.category}</p>
                <p className="text-gray-600 text-sm">Color: {item.color}</p>
              </div>
            ))}
          </div>
          
          <h2 className="text-2xl font-bold mb-4">Outfit Combinations</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {outfits.map((outfit) => (
              <div key={outfit.id} className="bg-white shadow-md rounded-lg p-6">
                <h3 className="text-xl font-bold mb-2">{outfit.name}</h3>
                <p className="text-gray-600 mb-4">{outfit.description}</p>
                <div className="mb-4">
                  <h4 className="font-bold mb-2">Items:</h4>
                  <ul className="list-disc pl-5">
                    {outfit.items.map((itemId, index) => {
                      const item = items.find(i => i.id === itemId);
                      return item ? <li key={index}>{item.name}</li> : null;
                    })}
                  </ul>
                </div>
                <button 
                  className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleSaveOutfit(outfit.id)}
                >
                  Save Outfit
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
      
      <div className="mt-8 bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-bold mb-2">What is a Capsule Wardrobe?</h3>
        <p className="mb-4">
          A capsule wardrobe is a collection of essential clothing items that don't go out of fashion 
          and can be worn in multiple combinations. The idea is to have a smaller collection of 
          high-quality, versatile pieces that can be mixed and matched to create a variety of outfits.
        </p>
        <h3 className="text-xl font-bold mb-2">Benefits:</h3>
        <ul className="list-disc pl-5 space-y-2">
          <li>Saves time and money</li>
          <li>Reduces decision fatigue</li>
          <li>Encourages creativity with existing pieces</li>
          <li>Promotes sustainable fashion choices</li>
          <li>Ensures you always have something to wear</li>
        </ul>
      </div>
    </div>
  );
};

export default CapsuleGeneratorPage;