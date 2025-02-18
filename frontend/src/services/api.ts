import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://pathlet-api.onrender.com';

export interface BirthData {
  birth_date: string;
  birth_time?: string;
  birth_location?: string;
}

export const PathletAPI = {
  getAscendants: async (data: BirthData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/get_ascendants`, data);
      return response.data;
    } catch (error) {
      console.error('Error fetching ascendants:', error);
      throw error;
    }
  },

  calculateNumerology: async (data: BirthData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/calculate_all`, data);
      return response.data.numerology;
    } catch (error) {
      console.error('Error calculating numerology:', error);
      throw error;
    }
  },

  calculateHumanDesign: async (data: BirthData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/calculate_all`, data);
      return response.data.human_design;
    } catch (error) {
      console.error('Error calculating human design:', error);
      throw error;
    }
  }
};
