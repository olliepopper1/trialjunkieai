import React from 'react';
import { DefaultButton } from '@fluentui/react';
import Header from './components/Header';
import Footer from './components/Footer';

const App = () => {
  return (
    <div>
      <Header />
      <main className="p-4">
        <h1 className="text-3xl font-bold">Welcome to My App</h1>
        <DefaultButton text="Click Me" onClick={() => alert('Button clicked!')} />
      </main>
      <Footer />
    </div>
  );
};

export default App;
