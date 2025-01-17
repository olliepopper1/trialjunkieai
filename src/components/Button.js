import React from 'react';

const Button = ({ label, onClick }) => {
  return (
    <button className="bg-blue-500 text-white font-bold py-2 px-4 rounded" onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;
