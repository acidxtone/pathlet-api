import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_URL || 'https://pathlet-api.vercel.app/api';

interface AscendantResult {
    possible_signs: string[];
    details?: Record<string, any>;
}

interface NumerologyResult {
    life_path_number: number;
    description: string;
    challenges?: string[];
    opportunities?: string[];
}

interface HumanDesignResult {
    type: string;
    strategy: string;
    authority: string;
    profile: string;
    description?: string;
}

interface CompatibilityResult {
    compatibility_score: number;
    insights?: string[];
    challenges?: string[];
}

export const PathletService = {
    getAscendants: async (birthDate: string, birthLocation: string): Promise<AscendantResult> => {
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

    calculateNumerology: async (birthDate: string): Promise<NumerologyResult> => {
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

    calculateHumanDesign: async (
        birthDate: string, 
        birthTime?: string, 
        birthLocation?: string
    ): Promise<HumanDesignResult> => {
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

    calculateCompatibility: async (
        person1: Record<string, any>, 
        person2: Record<string, any>
    ): Promise<CompatibilityResult> => {
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
