import ChatInterface from '../components/ChatInterface';
import FileUpload from '../components/FileUpload';
import { Database, ShieldCheck, Zap } from 'lucide-react';

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 text-gray-900 p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <header className="flex justify-between items-center mb-12">
          <div>
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 mb-2 flex items-center gap-3">
              <Database className="text-blue-600" /> Agentic RAG Hub
            </h1>
            <p className="text-gray-500 font-medium italic">Production-Level Local Knowledge Intelligence</p>
          </div>
          <div className="flex gap-4">
            <div className="flex items-center gap-2 bg-green-50 text-green-700 px-4 py-2 rounded-full text-xs font-bold border border-green-100">
              <ShieldCheck size={14} /> 100% Private & Local
            </div>
            <div className="flex items-center gap-2 bg-blue-50 text-blue-700 px-4 py-2 rounded-full text-xs font-bold border border-blue-100">
              <Zap size={14} /> Powered by Ollama
            </div>
          </div>
        </header>

        {/* Dashboard Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Sidebar / Upload Area */}
          <div className="lg:col-span-1 space-y-8">
            <FileUpload />
            
            <div className="bg-white p-6 rounded-xl shadow-md border border-gray-100">
              <h4 className="text-sm font-bold text-gray-700 uppercase mb-4 tracking-wider">System Insights</h4>
              <ul className="space-y-4">
                <li className="flex gap-3">
                  <div className="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 shrink-0" />
                  <p className="text-sm text-gray-600">Uses <span className="font-bold">LangGraph</span> for stateful agentic workflows.</p>
                </li>
                <li className="flex gap-3">
                  <div className="w-1.5 h-1.5 bg-green-500 rounded-full mt-2 shrink-0" />
                  <p className="text-sm text-gray-600">Self-correcting retrieval via <span className="font-bold">CRAG</span> methodology.</p>
                </li>
                <li className="flex gap-3">
                  <div className="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 shrink-0" />
                  <p className="text-sm text-gray-600">Vector storage using local <span className="font-bold">ChromaDB</span> persistency.</p>
                </li>
              </ul>
            </div>
          </div>

          {/* Main Chat Interface */}
          <div className="lg:col-span-2">
            <ChatInterface />
          </div>
        </div>
        
        <footer className="mt-16 text-center text-gray-400 text-sm">
          &copy; 2026 Agentic RAG Hub - Built for High-Performance Resume Project
        </footer>
      </div>
    </main>
  );
}
