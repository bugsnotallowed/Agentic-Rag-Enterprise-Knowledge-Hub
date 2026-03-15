"use client";
import React, { useState } from 'react';
import { uploadFile } from '../services/api';
import { Upload, FileCheck, AlertCircle } from 'lucide-react';

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<string>('');
  const [uploading, setUploading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setUploading(true);
    setStatus('Uploading and Indexing...');
    
    try {
      await uploadFile(file);
      setStatus('Success! Document indexed.');
      setFile(null);
    } catch (error) {
      console.error(error);
      setStatus('Error uploading document.');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-xl shadow-md border border-gray-100 h-full flex flex-col items-center justify-center text-center">
      <div className="w-16 h-16 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mb-4">
        <Upload size={32} />
      </div>
      <h3 className="text-lg font-semibold text-gray-800 mb-2">Knowledge Ingestion</h3>
      <p className="text-sm text-gray-500 mb-6">Upload PDFs to provide context to your Agentic RAG hub.</p>
      
      <input 
        type="file" 
        id="fileInput" 
        className="hidden" 
        accept=".pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />
      <label 
        htmlFor="fileInput" 
        className="cursor-pointer bg-blue-50 text-blue-700 px-6 py-3 rounded-lg border-2 border-dashed border-blue-200 hover:bg-blue-100 transition-all mb-4"
      >
        {file ? file.name : 'Select PDF File'}
      </label>

      {file && !uploading && (
        <button 
          onClick={handleUpload}
          className="bg-blue-600 text-white px-8 py-2 rounded-lg hover:bg-blue-700 transition-colors"
        >
          Start Indexing
        </button>
      )}

      {status && (
        <div className={`mt-4 flex items-center gap-2 text-sm ${status.includes('Error') ? 'text-red-600' : 'text-green-600'}`}>
          {status.includes('Error') ? <AlertCircle size={16} /> : <FileCheck size={16} />}
          <span>{status}</span>
        </div>
      )}
    </div>
  );
}
