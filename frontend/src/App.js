import React, { useState } from 'react';
import styled, { ThemeProvider } from 'styled-components';
import { PathletService } from './services/pathletService';

const theme = {
    colors: {
        primary: '#6A5ACD',
        secondary: '#7B68EE',
        background: '#F4F4F8',
        text: '#333333'
    },
    fonts: {
        main: "'Inter', sans-serif"
    }
};

const AppContainer = styled.div`
    font-family: ${props => props.theme.fonts.main};
    background-color: ${props => props.theme.colors.background};
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
`;

const FormContainer = styled.div`
    background-color: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 500px;
`;

const InputGroup = styled.div`
    margin-bottom: 1rem;
    
    label {
        display: block;
        margin-bottom: 0.5rem;
        color: ${props => props.theme.colors.text};
    }
    
    input {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #E0E0E0;
        border-radius: 8px;
    }
`;

const Button = styled.button`
    background-color: ${props => props.theme.colors.primary};
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    
    &:hover {
        background-color: ${props => props.theme.colors.secondary};
    }
`;

const ResultContainer = styled.div`
    margin-top: 1rem;
    background-color: #F9F9FC;
    border-radius: 8px;
    padding: 1rem;
`;

function App() {
    const [birthDate, setBirthDate] = useState('');
    const [birthTime, setBirthTime] = useState('');
    const [birthLocation, setBirthLocation] = useState('');
    const [result, setResult] = useState(null);
    const [calculationType, setCalculationType] = useState('ascendants');

    const handleCalculate = async () => {
        try {
            let calculationResult;
            switch(calculationType) {
                case 'ascendants':
                    calculationResult = await PathletService.getAscendants(birthDate, birthLocation);
                    break;
                case 'numerology':
                    calculationResult = await PathletService.calculateNumerology(birthDate);
                    break;
                case 'humanDesign':
                    calculationResult = await PathletService.calculateHumanDesign(birthDate, birthTime, birthLocation);
                    break;
                default:
                    throw new Error('Invalid calculation type');
            }
            setResult(calculationResult);
        } catch (error) {
            console.error('Calculation Error:', error);
            setResult({ error: error.message });
        }
    };

    return (
        <ThemeProvider theme={theme}>
            <AppContainer>
                <FormContainer>
                    <h1>Pathlet Insights</h1>
                    <InputGroup>
                        <label>Calculation Type</label>
                        <select 
                            value={calculationType} 
                            onChange={(e) => setCalculationType(e.target.value)}
                        >
                            <option value="ascendants">Ascendant Signs</option>
                            <option value="numerology">Numerology</option>
                            <option value="humanDesign">Human Design</option>
                        </select>
                    </InputGroup>
                    <InputGroup>
                        <label>Birth Date</label>
                        <input 
                            type="date" 
                            value={birthDate} 
                            onChange={(e) => setBirthDate(e.target.value)} 
                        />
                    </InputGroup>
                    {calculationType === 'humanDesign' && (
                        <InputGroup>
                            <label>Birth Time</label>
                            <input 
                                type="time" 
                                value={birthTime} 
                                onChange={(e) => setBirthTime(e.target.value)} 
                            />
                        </InputGroup>
                    )}
                    <InputGroup>
                        <label>Birth Location</label>
                        <input 
                            type="text" 
                            value={birthLocation} 
                            onChange={(e) => setBirthLocation(e.target.value)} 
                            placeholder="City, Country"
                        />
                    </InputGroup>
                    <Button onClick={handleCalculate}>Calculate</Button>
                    
                    {result && (
                        <ResultContainer>
                            <pre>{JSON.stringify(result, null, 2)}</pre>
                        </ResultContainer>
                    )}
                </FormContainer>
            </AppContainer>
        </ThemeProvider>
    );
}

export default App;
