import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-gray-800 text-white shadow-lg">
      <div className="max-w-6xl mx-auto px-4 py-4">
        <div className="flex justify-between items-center">
          <Link to="/" className="text-2xl font-bold text-purple-400">
            StyleMate Pro
          </Link>
          <nav>
            <ul className="flex space-x-6">
              <li>
                <Link to="/" className="hover:text-purple-300 transition duration-300">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/outfit-suggestion" className="hover:text-purple-300 transition duration-300">
                  Outfit Suggestion
                </Link>
              </li>
              <li>
                <Link to="/garment-generator" className="hover:text-purple-300 transition duration-300">
                  Garment Generator
                </Link>
              </li>
              <li>
                <Link to="/capsule-generator" className="hover:text-purple-300 transition duration-300">
                  Capsule Generator
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;