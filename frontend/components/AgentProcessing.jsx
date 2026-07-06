"use client";

import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const AGENTS = [
  { id: "requirements", name: "Requirements Engineer" },
  { id: "architect", name: "Solution Architect" },
  { id: "talent", name: "Talent Scout" },
  { id: "pulse", name: "Project Pulse" },
  { id: "quality", name: "Quality Review" },
  { id: "conflict", name: "Conflict Arbitrator" },
];

const AgentProcessing = ({ onComplete }) => {
  const [activeAgents, setActiveAgents] = useState([]);

  useEffect(() => {
    // Staggered activation sequence
    const timers = AGENTS.map((agent, index) => {
      return setTimeout(() => {
        setActiveAgents((prev) => [...prev, agent.id]);
      }, 800 + (index * 700));
    });

    const finishTimer = setTimeout(() => {
      onComplete();
    }, 800 + (AGENTS.length * 700) + 1500);

    return () => {
      timers.forEach(clearTimeout);
      clearTimeout(finishTimer);
    };
  }, [onComplete]);

  return (
    <div className="relative min-h-screen w-full bg-black text-white flex flex-col items-center justify-center font-sans">
      {/* Ambient Glow */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(60,60,60,0.2)_0%,transparent_70%)]" />
      
      <div className="max-w-md w-full px-6 z-10">
        <h2 className="text-xl font-light tracking-widest text-center mb-12 uppercase text-gray-500">
          Initializing ProjectHive AI Agents...
        </h2>

        <div className="space-y-6">
          {AGENTS.map((agent) => (
            <div key={agent.id} className="relative flex items-center justify-between">
              <span className={`transition-opacity duration-500 ${activeAgents.includes(agent.id) ? 'opacity-100' : 'opacity-20'}`}>
                {agent.name}
              </span>
              
              <AnimatePresence>
                {activeAgents.includes(agent.id) && (
                  <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    exit={{ scale: 0 }}
                    className="flex items-center gap-2"
                  >
                    <div className="h-2 w-2 rounded-full bg-white animate-pulse" />
                    <span className="text-[10px] uppercase tracking-widest text-white/50">Active</span>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AgentProcessing;