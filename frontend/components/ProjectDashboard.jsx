"use client";

import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  CheckSquare, 
  Layers, 
  Users, 
  BarChart, 
  BrainCircuit, 
  AlertTriangle, 
  Calendar,
  RefreshCw
} from 'lucide-react';

const DashboardCard = ({ title, icon: Icon, children, className }) => (
  <div className={`liquid-glass p-6 rounded-3xl border border-white/5 ${className}`}>
    <div className="flex items-center gap-3 mb-6">
      <div className="p-2 rounded-full bg-white/5">
        <Icon size={18} className="text-gray-400" />
      </div>
      <h3 className="text-sm uppercase tracking-widest text-gray-400">{title}</h3>
    </div>
    {children}
  </div>
);

const ProjectDashboard = () => {
  const [conflictResolved, setConflictResolved] = useState(false);
  const [project, setProject] = useState(null);
  useEffect(() => {
  const fetchProject = async () => {
    try {
      const res = await fetch("https://project-hive-backend-iiud.onrender.com/projects");
      const data = await res.json();

      if (data.length > 0) {
        setProject(data[data.length - 1]);
      }
    } catch (err) {
      console.error(err);
    }
  };

  fetchProject();
}, []);

  const triggerBottleneck = () => {
    // Simulating agent workflow
    setConflictResolved('processing');
    setTimeout(() => setConflictResolved(true), 2500);
  };

  if (!project) {
  return (
    <div className="min-h-screen bg-black flex items-center justify-center text-white">
      Loading Project...
    </div>
  );
}


  return (
    <div className="min-h-screen bg-black text-white p-6 md:p-12 font-sans">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-end mb-12 gap-6">
          <div>
            <h1 className="text-4xl font-light mb-2">{project.title}</h1>
            <p className="text-gray-500">{project.business_name}</p>
          </div>
          <div className="liquid-glass px-6 py-3 rounded-full flex items-center gap-4">
            <div className="text-sm text-gray-400">Total Progress</div>
            <div className="w-32 h-1.5 bg-white/10 rounded-full overflow-hidden">
              <div
  className="h-full bg-white rounded-full"
  style={{ width: `${project.progress}%` }}
/>
            </div>
            <div className="font-bold">{project.progress}%</div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Column */}
          <div className="lg:col-span-2 space-y-6">
            <DashboardCard title="Requirements" icon={CheckSquare}>
              <ul className="space-y-3">
                {[
  [
  "Business Request Submitted",
  "AI PRD Generated",
  `Project Status: ${project.status}`,
]].map((item, i) => (
                  <li key={i} className="flex items-center gap-3 text-sm">
                    <div className="w-4 h-4 rounded border border-white/20" /> {item}
                  </li>
                ))}
              </ul>
            </DashboardCard>
            
            <div className="grid grid-cols-2 gap-6">
              <DashboardCard title="Architecture" icon={Layers}>
                <div className="text-xs text-gray-400 font-mono">
  {Object.entries(project.tech_stack).map(([key, value]) => (
  <div key={key}>
    {key}: {Array.isArray(value) ? value.join(", ") : value}
  </div>
))}
</div>
              </DashboardCard>
              <DashboardCard title="Team" icon={Users}>
                <div className="flex -space-x-2">
                  {['A','S','S','S'].map((letter, index) => <div
  key={`${letter}-${index}`}
  className="w-8 h-8 rounded-full bg-white/20 border border-black flex items-center justify-center text-xs"
>
  {letter}
</div>)}
                </div>
              </DashboardCard>
            </div>
          </div>

          {/* Sidebar Column */}
          <div className="space-y-6">
            <DashboardCard title="AI Suggestions" icon={BrainCircuit}>
              <p className="text-xs text-gray-400 italic">{`Project "${project.title}" has been created successfully.

Recommended stack:
${Object.keys(project.tech_stack).join(", ")}

Current Status:
${project.status}`}</p>
            </DashboardCard>

            <DashboardCard title="Conflict Arbitrator" icon={AlertTriangle}>
              {conflictResolved === 'processing' ? (
                <div className="flex items-center gap-3 text-sm animate-pulse">
                  <RefreshCw className="animate-spin" size={16} /> AI Agent resolving project conflict...
                </div>
              ) : conflictResolved === true ? (
                <div className="text-sm text-emerald-400">✅ Conflict Resolved Successfully</div>
              ) : (
                <button 
                  onClick={triggerBottleneck}
                  className="w-full text-left text-xs bg-white/5 p-3 rounded-xl hover:bg-white/10 transition"
                >
                  Simulate Team Conflict
                </button>
              )}
            </DashboardCard>

            <DashboardCard title="Timeline" icon={Calendar}>
              <div className="text-sm">Current Phase: <span className="text-gray-400">{project.status}</span></div>
            </DashboardCard>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProjectDashboard;
