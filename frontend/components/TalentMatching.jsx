"use client";

import React, { useEffect, useState } from "react";
import { motion } from 'framer-motion';
import { GitBranch, Code2, Award, Zap } from "lucide-react";


const StudentCard = ({ student, index }) => (
  <motion.div 
    initial={{ opacity: 0, scale: 0.95 }}
    animate={{ opacity: 1, scale: 1 }}
    transition={{ delay: index * 0.1, duration: 0.4 }}
    className="liquid-glass rounded-3xl p-8 border border-white/5 flex flex-col justify-between hover:border-white/20 transition-all"
  >
    <div>
      <div className="flex justify-between items-start mb-6">
        <div>
          <h3 className="text-xl font-medium">{student.name}</h3>
          <p className="text-gray-400 text-sm">{student.role}</p>
        </div>
        <div className="bg-white/10 px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1">
          <Zap size={12} className="fill-white" /> {student.match}%
        </div>
      </div>
      
      <div className="flex flex-wrap gap-2 mb-8">
        {student.skills.map((skill) => (
          <span key={skill} className="px-3 py-1 bg-white/5 rounded-full text-[10px] uppercase tracking-wider text-gray-300 border border-white/5">
            {skill}
          </span>
        ))}
      </div>
    </div>

    <button className="w-full py-3 rounded-xl bg-white/5 hover:bg-white/10 transition-colors flex items-center justify-center gap-2 text-sm">
  <GitBranch size={16} /> View Profile
</button>
  </motion.div>

);

const TalentMatching = ({ onNext, requestId }) => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    if (!requestId) return;

    const fetchMatches = async () => {
      try {
        const res = await fetch(
          `https://project-hive-backend-iiud.onrender.com/business-requests/${requestId}/match`,
          {
            method: "POST",
          }
        );

        const data = await res.json();

        setStudents(data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchMatches();
  }, [requestId]);  return (
    <div className="min-h-screen bg-black text-white p-6 md:p-12 font-sans">
      <div className="max-w-6xl mx-auto">
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mb-12"
        >
          <h1 className="text-4xl md:text-5xl font-light mb-4">Talent Scout</h1>
          <p className="text-gray-500">Autonomous matching results based on project requirements</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          {students.map((match, i) => (
  <StudentCard
    key={match.student.id}
    student={{
      name: match.student.name,
      role: match.reason,
      skills: match.skill_match,
      match: Math.round(match.score * 20),
    }}
    index={i}
  />
))}
        </div>

        <div className="flex justify-center">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={async () => {
  try {
    await fetch("https://project-hive-backend-iiud.onrender.com/projects", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        business_request_id: requestId,
        title: "Business Website",
        description: "Generated from ProjectHive",
        assigned_students: students.map((s) => s.student.id),
        tech_stack: {
  frontend: ["React", "Next.js"],
  backend: ["FastAPI"],
  database: ["PostgreSQL"],
},
        deadline: "2026-12-31",
      }),
    });

    onNext();
  } catch (err) {
    console.error(err);
  }
}}
            className="bg-white text-black px-8 py-3 rounded-full font-medium hover:bg-gray-200"
          >
            Launch Dashboard
          </motion.button>
        </div>
      </div>
    </div>
  );
};

export default TalentMatching;