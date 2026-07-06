"use client";

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const BusinessInput = ({ onNext }) => {
  const [inputValue, setInputValue] = useState('');

  return (
    <div className="relative min-h-screen w-full bg-black text-white flex items-center justify-center p-6 font-sans overflow-hidden">
      {/* Background Ambience */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.03)_0%,transparent_70%)]" />

      <div className="max-w-xl w-full z-10">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="text-3xl md:text-4xl font-normal tracking-tight mb-8">
            Describe your business idea
          </h2>
          
          <div className="liquid-glass rounded-3xl p-1">
            <textarea
              className="w-full h-40 bg-transparent text-lg text-white/90 p-6 focus:outline-none resize-none placeholder:text-gray-600"
              placeholder="e.g. I own a local bakery and I want to allow customers to order custom cakes online..."
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
            />
          </div>

          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={async () => {
  try {
    const response = await fetch("https://project-hive-backend-iiud.onrender.com/business-requests", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        business_name: "Demo Business",
        owner_name: "Arisha",
        email: "demo@example.com",
        description: inputValue,
      }),
    });

    const data = await response.json();

    console.log("Created Business Request:", data);

    onNext(data.id);
  } catch (err) {
    console.error(err);
  }
}}
            className="mt-6 w-full bg-white text-black py-4 rounded-full font-medium hover:bg-gray-200 transition-colors duration-300"
          >
            Generate Project Plan
          </motion.button>
        </motion.div>
      </div>
    </div>
  );
};

export default BusinessInput;
