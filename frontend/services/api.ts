import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);
  return axios.post(`${API_BASE_URL}/upload`, formData);
};

export const queryAgent = async (question: string) => {
  return axios.get(`${API_BASE_URL}/query`, {
    params: { q: question }
  });
};
