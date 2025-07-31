import React from 'react';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const navigate = useNavigate();

  const features = [
    {
      title: 'Outfit Suggestions',
      description: 'Get personalized outfit recommendations based on your style, body type, and occasion.',
      icon: '👕',
      path: '/outfit-suggestion'
    },
    {
      title: 'Garment Generator',
      description: 'Create custom clothing designs with our AI-powered garment generator.',
      icon: '👗',
      path: '/garment-generator'
    },
    {
      title: 'Capsule Wardrobe',
      description: 'Build a versatile capsule wardrobe tailored to your lifestyle.',
      icon: '🧳',
      path: '/capsule-generator'
    }
  ];

  return (
    <div className="max-w-6xl mx-auto p-4">
      {/* Hero Section */}
      <div className="text-center py-12 bg-gradient-to-r from-purple-500 to-indigo-600 rounded-2xl text-white mb-12">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">Welcome to StyleMate Pro</h1>
        <p className="text-xl mb-8 max-w-2xl mx-auto">
          Your AI-powered personal stylist that helps you look your best every day
        </p>
        <button 
          onClick={() => navigate('/outfit-suggestion')}
          className="bg-white text-purple-600 hover:bg-gray-100 font-bold py-3 px-6 rounded-full text-lg transition duration-300"
        >
          Get Started
        </button>
      </div>

      {/* Features Section */}
      <div className="mb-16">
        <h2 className="text-3xl font-bold text-center mb-12">How StyleMate Pro Works</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div 
              key={index} 
              className="bg-white shadow-lg rounded-xl p-6 hover:shadow-xl transition duration-300 cursor-pointer"
              onClick={() => navigate(feature.path)}
            >
              <div className="text-4xl mb-4">{feature.icon}</div>
              <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
              <p className="text-gray-600 mb-4">{feature.description}</p>
              <button className="text-purple-600 font-semibold hover:text-purple-800">
                Try it now →
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* How It Works Section */}
      <div className="bg-gray-50 rounded-2xl p-8 mb-16">
        <h2 className="text-3xl font-bold text-center mb-8">How It Works</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center text-2xl mx-auto mb-4">1</div>
            <h3 className="text-xl font-bold mb-2">Tell Us About Yourself</h3>
            <p className="text-gray-600">Share your style preferences, body measurements, and lifestyle needs</p>
          </div>
          <div className="text-center">
            <div className="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center text-2xl mx-auto mb-4">2</div>
            <h3 className="text-xl font-bold mb-2">Get AI-Powered Recommendations</h3>
            <p className="text-gray-600">Our advanced algorithms create personalized fashion suggestions</p>
          </div>
          <div className="text-center">
            <div className="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center text-2xl mx-auto mb-4">3</div>
            <h3 className="text-xl font-bold mb-2">Look Your Best</h3>
            <p className="text-gray-600">Implement our suggestions and boost your confidence</p>
          </div>
        </div>
      </div>

      {/* Testimonials */}
      <div className="mb-16">
        <h2 className="text-3xl font-bold text-center mb-8">What Our Users Say</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-white shadow-lg rounded-xl p-6">
            <div className="text-yellow-400 text-2xl mb-4">★★★★★</div>
            <p className="text-gray-600 mb-4">
              "StyleMate Pro completely transformed my wardrobe. I've never felt more confident in my outfits!"
            </p>
            <div className="flex items-center">
              <div className="bg-gray-200 border-2 border-dashed rounded-xl w-16 h-16" />
              <div className="ml-4">
                <h4 className="font-bold">Sarah K.</h4>
                <p className="text-gray-600">Professional, 32</p>
              </div>
            </div>
          </div>
          <div className="bg-white shadow-lg rounded-xl p-6">
            <div className="text-yellow-400 text-2xl mb-4">★★★★★</div>
            <p className="text-gray-600 mb-4">
              "The garment generator helped me create exactly what I envisioned. The designs were perfect for my brand!"
            </p>
            <div className="flex items-center">
              <div className="bg-gray-200 border-2 border-dashed rounded-xl w-16 h-16" />
              <div className="ml-4">
                <h4 className="font-bold">Michael T.</h4>
                <p className="text-gray-600">Fashion Designer, 28</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;