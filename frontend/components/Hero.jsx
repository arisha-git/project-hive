"use client";

import React, { useState } from "react";
import {
  Search,
  User,
  Play,
  Menu,
  X,
  Star,
  Clock,
  Calendar,
} from "lucide-react";
import { motion } from "framer-motion";

const Hero = ({ onStart }) => {
      const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <div className="relative w-full h-screen overflow-hidden text-white">

      {/* Global Styles */}
      <style>{`
        @keyframes blurFadeUp {
          from {
            opacity: 0;
            filter: blur(20px);
            transform: translateY(40px);
          }
          to {
            opacity: 1;
            filter: blur(0);
            transform: translateY(0);
          }
        }

        .animate-blur-fade-up {
          animation: blurFadeUp 1s ease-out forwards;
          opacity: 0;
        }

        .liquid-glass {
          background: rgba(255,255,255,0.01);
          backdrop-filter: blur(4px);
          -webkit-backdrop-filter: blur(4px);
          border: none;
          box-shadow: inset 0 1px 1px rgba(255,255,255,0.1);
          position: relative;
          overflow: hidden;
        }

        .liquid-glass::before {
          content: "";
          position: absolute;
          inset: 0;
          border-radius: inherit;
          padding: 1.4px;

          background: linear-gradient(
            180deg,
            rgba(255,255,255,.45) 0%,
            rgba(255,255,255,.15) 20%,
            rgba(255,255,255,0) 40%,
            rgba(255,255,255,0) 60%,
            rgba(255,255,255,.15) 80%,
            rgba(255,255,255,.45) 100%
          );

          -webkit-mask:
            linear-gradient(#fff 0 0) content-box,
            linear-gradient(#fff 0 0);

          mask:
            linear-gradient(#fff 0 0) content-box,
            linear-gradient(#fff 0 0);

          -webkit-mask-composite: xor;
          mask-composite: exclude;

          pointer-events: none;
        }
      `}</style>

      {/* Background Video */}

      <video
        autoPlay
        muted
        loop
        playsInline
        className="fixed inset-0 w-full h-full object-cover z-0"
        src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260406_094145_4a271a6c-3869-4f1c-8aa7-aeb0cb227994.mp4"
      />

      {/* Blur Overlay */}

      <div
        className="fixed inset-0 z-[1] pointer-events-none backdrop-blur-xl"
        style={{
          WebkitMaskImage:
            "linear-gradient(to top, black 0%, transparent 45%)",
          maskImage:
            "linear-gradient(to top, black 0%, transparent 45%)",
        }}
      />

      {/* Navbar */}

      <header className="fixed top-0 inset-x-0 z-50 px-4 sm:px-12 py-6 flex justify-between items-center">

        <div
          className="animate-blur-fade-up text-2xl font-bold tracking-tight"
          style={{ animationDelay: "0ms" }}
        >
          ProjectHive
        </div>

        <nav className="hidden lg:flex gap-8">
          {[
            "GitHub",
          ].map((item, i) => (
            <a
              key={item}
              href="#"
              className="text-sm hover:text-gray-300 animate-blur-fade-up"
              style={{ animationDelay: `${100 + i * 50}ms` }}
            >
              {item}
            </a>
          ))}
        </nav>

        <div className="flex gap-4">


          <button
            className="w-10 h-10 flex items-center justify-center rounded-full liquid-glass animate-blur-fade-up"
            style={{ animationDelay: "400ms" }}
          >
            <User size={18} />
          </button>

          <button
            className="lg:hidden w-10 h-10 flex items-center justify-center rounded-full liquid-glass"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X size={18} /> : <Menu size={18} />}
          </button>

        </div>

      </header>

      {/* Hero */}

      <main className="relative z-10 h-full flex flex-col justify-end px-4 sm:px-12 pb-16">

        <div className="max-w-2xl">

          <div
            className="flex gap-6 mb-8 animate-blur-fade-up"
            style={{ animationDelay: "300ms" }}
          >
            <span className="flex items-center gap-2">
               6 AI Agents
            </span>

            <span className="flex items-center gap-2">
              Real-Time Matching
            </span>

            <span className="flex items-center gap-2">
              Autonomous Workflow
            </span>
          </div>

          <h1
            className="text-5xl md:text-7xl font-normal tracking-tighter mb-6 animate-blur-fade-up"
            style={{ animationDelay: "400ms" }}
          >
            Where Business
            <br />
            Meets Young Talent
          </h1>

          <p
            className="text-xl text-gray-400 mb-10 animate-blur-fade-up"
            style={{ animationDelay: "500ms" }}
          >
            Describe your business idea, let AI generate the project roadmap, and instantly match the best student developers to bring it to life.
          </p>

          <div
            className="flex gap-4 animate-blur-fade-up"
            style={{ animationDelay: "600ms" }}
          >

            <button 
            onClick={onStart} 
            className="bg-white text-black rounded-full px-8 py-3 font-medium flex items-center gap-2 hover:bg-gray-200">
              Start Building
              <Play size={16} fill="black" />
            </button>
          </div>

        </div>

      </main>

    </div>
  );
};

export default Hero;