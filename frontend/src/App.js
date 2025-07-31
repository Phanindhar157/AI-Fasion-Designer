import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import OutfitSuggestionPage from './pages/OutfitSuggestionPage';
import GarmentGeneratorPage from './pages/GarmentGeneratorPage';
import CapsuleGeneratorPage from './pages/CapsuleGeneratorPage';

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Header />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/outfit-suggestion" element={<OutfitSuggestionPage />} />
            <Route path="/garment-generator" element={<GarmentGeneratorPage />} />
            <Route path="/capsule-generator" element={<CapsuleGeneratorPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
