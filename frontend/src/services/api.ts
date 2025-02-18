import axios from 'axios';

const API_BASE_URL = 'https://pathlet-api.onrender.com';

export interface BirthData {
  birth_date: string;
  birth_time?: string;
  birth_location?: string;
}

export interface ApiResponse {
  numerology: any;
  human_design: any;
  ascendant: any;
}

export const PathletAPI = {
  calculateAll: async (data: BirthData): Promise<ApiResponse> => {
    try {
      const response = await axios.post(`${API_BASE_URL}/calculate_all`, data);
      return response.data;
    } catch (error) {
      console.error('Error calculating insights:', error);
      throw error;
    }
  },

  getAscendants: async (data: BirthData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/get_ascendants`, data);
      return response.data;
    } catch (error) {
      console.error('Error fetching ascendants:', error);
      throw error;
    }
  }
};
