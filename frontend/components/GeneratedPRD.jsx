"use client";

import React from 'react';
import { motion } from 'framer-motion';
import { Target, Server, Clock, CheckCircle, AlertTriangle, Layers } from 'lucide-react';

const Card = ({ title, icon: Icon, children, delay }) => (
  <motion.div 
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.5, delay }}
    className="liquid-glass p-6 rounded-3xl border border-white/5"
  >
    <div className="flex items-center gap-3 mb-4">
      <div className="p-2 rounded-full bg-white/5">
        <Icon size={18} className="text-gray-400" />
      </div>
      <h3 className="text-sm uppercase tracking-widest text-gray-400">{title}</h3>
    </div>
    <div className="text-gray-300 text-sm leading-relaxed">
      {children}
    </div>
  </motion.div>
);

const GeneratedPRD = ({ onNext }) => {
  return (
    <div className="min-h-screen bg-black text-white p-6 md:p-12 font-sans">
      <div className="max-w-6xl mx-auto">
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mb-12"
        >
          <h1 className="text-4xl md:text-5xl font-light mb-4">Project Blueprint</h1>
          <p className="text-gray-500">Requirements Engineer & Solution Architect output</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          <Card title="Problem" icon={AlertTriangle} delay={0.1}>
            Small businesses struggle to find affordable software developers while students struggle to gain real-world project experience.
          </Card>
          <Card title="Objectives" icon={Target} delay={0.2}>
            Automatically analyze business ideas, generate project requirements, match skilled students, and monitor project delivery.
          </Card>
          <Card title="Tech Stack" icon={Server} delay={0.3}>
            React, FastAPI, PostgreSQL, NVIDIA AI, Gemini API, ADK
          </Card>
          <Card title="Architecture" icon={Layers} delay={0.4}>
            Multi-agent AI workflow with autonomous planning, matching, monitoring, and conflict resolution.
          </Card>
          <Card title="Timeline" icon={Clock} delay={0.5}>
           Planning → Talent Matching → Development → Review → Delivery
          </Card>
          <Card title="Deliverables" icon={CheckCircle} delay={0.6}>
            Project roadmap, AI-generated PRD, matched student team, project dashboard.
          </Card>
        </div>

        <div className="flex justify-center">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={onNext}
            className="bg-white text-black px-8 py-3 rounded-full font-medium hover:bg-gray-200"
          >
            Match Talent
          </motion.button>
        </div>
      </div>
    </div>
  );
};

export default GeneratedPRD;
