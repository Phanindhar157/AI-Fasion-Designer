import React from 'react';

const Notification = ({ type = 'info', message, onClose }) => {
  const getColorClasses = () => {
    switch (type) {
      case 'success':
        return 'bg-green-100 border-green-400 text-green-700';
      case 'error':
        return 'bg-red-100 border-red-400 text-red-700';
      case 'warning':
        return 'bg-yellow-100 border-yellow-400 text-yellow-700';
      default:
        return 'bg-blue-100 border-blue-400 text-blue-700';
    }
  };

  return (
    <div className={`border px-4 py-3 rounded relative mb-4 ${getColorClasses()}`} role="alert">
      <span className="block sm:inline">{message}</span>
      <button 
        onClick={onClose}
        className="absolute top-0 bottom-0 right-0 px-4 py-3"
      >
        <svg className="fill-current h-6 w-6" role="button" viewBox="0 0 20 20">
          <title>Close</title>
          <path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.777-3.037-2.777-3.037a1.2 1.2 0 1 1 1.697-1.697L10 8.181l2.651-3.029a1.2 1.2 0 1 1 1.697 1.697l-2.777 3.037 2.777 3.037c.52.52.52 1.36 0 1.88z"/>
        </svg>
      </button>
    </div>
  );
};

export default Notification;