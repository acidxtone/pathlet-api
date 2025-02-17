import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_URL || 'https://pathlet-api.vercel.app/api';

export const PathletService = {
    getAscendants: async (birthDate, birthLocation) => {
        try {
            const response = await axios.post(`${BASE_URL}/get_ascendants`, {
                birth_date: birthDate,
                birth_location: birthLocation
            });
            return response.data;
        } catch (error) {
            console.error('Ascendant Calculation Error:', error);
            throw error;
        }
    },

    calculateNumerology: async (birthDate) => {
        try {
            const response = await axios.post(`${BASE_URL}/calculate_numerology`, {
                birth_date: birthDate
            });
            return response.data;
        } catch (error) {
            console.error('Numerology Calculation Error:', error);
            throw error;
        }
    },

    calculateHumanDesign: async (birthDate, birthTime, birthLocation) => {
        try {
            const response = await axios.post(`${BASE_URL}/calculate_human_design`, {
                birth_date: birthDate,
                birth_time: birthTime,
                birth_location: birthLocation
            });
            return response.data;
        } catch (error) {
            console.error('Human Design Calculation Error:', error);
            throw error;
        }
    },

    calculateCompatibility: async (person1, person2) => {
        try {
            const response = await axios.post(`${BASE_URL}/calculate_compatibility`, {
                person1, 
                person2
            });
            return response.data;
        } catch (error) {
            console.error('Compatibility Calculation Error:', error);
            throw error;
        }
    }
};
