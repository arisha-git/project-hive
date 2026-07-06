"use client";

import React, { useState } from 'react';
import Hero from '../components/Hero';
import BusinessInput from '../components/BusinessInput';
import AgentProcessing from '../components/AgentProcessing';
import GeneratedPRD from '../components/GeneratedPRD';
import TalentMatching from '../components/TalentMatching';
import ProjectDashboard from '../components/ProjectDashboard';

const App = () => {
  const [view, setView] = useState("hero");
  const [requestId, setRequestId] = useState(null);

  // Logic to handle state transitions between screens
  const handleTransition = (nextView) => {
    setView(nextView);
  };

  return (
    <div className="bg-black min-h-screen text-white">
      {view === 'hero' && (
        <Hero onStart={() => handleTransition('input')} />
      )}
      
      {view === "input" && (
  <BusinessInput
    onNext={(id) => {
      setRequestId(id);
      handleTransition("processing");
    }}
  />
)}
      
      {view === "processing" && (
  <AgentProcessing
    requestId={requestId}
    onComplete={() => handleTransition("prd")}
  />
)}
      
      {view === "prd" && (
  <GeneratedPRD
    requestId={requestId}
    onNext={() => handleTransition("matching")}
/>
)}
      
      {view === "matching" && (
  <TalentMatching
    requestId={requestId}
    onNext={() => handleTransition("dashboard")}
  />
)}
      
      {view === "dashboard" && (
  <ProjectDashboard requestId={requestId} />
)}
    </div>
  );
};

export default App;