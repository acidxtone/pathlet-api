import React, { useState } from 'react';
import { 
  ThemeProvider, 
  createTheme, 
  CssBaseline, 
  Container, 
  Paper, 
  Typography, 
  TextField, 
  Button, 
  Grid, 
  Box,
  Tabs,
  Tab
} from '@mui/material';
import { useForm, Controller } from 'react-hook-form';
import { PathletAPI, BirthData, ApiResponse } from './services/api';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#7E57C2', // Deep Purple
    },
    background: {
      default: '#121212',
      paper: '#1E1E1E'
    }
  },
  typography: {
    fontFamily: 'Poppins, Arial, sans-serif'
  }
});

const App: React.FC = () => {
  const [results, setResults] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState(0);
  const { control, handleSubmit, reset } = useForm<BirthData>();

  const onSubmit = async (data: BirthData) => {
    setLoading(true);
    try {
      const insights = await PathletAPI.calculateAll(data);
      setResults(insights);
    } catch (error) {
      console.error('Error fetching insights:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue);
    reset(); // Reset form when changing tabs
    setResults(null);
  };

  const renderInsightSection = (title: string, data: any) => (
    <Paper variant="outlined" sx={{ p: 2, mb: 2 }}>
      <Typography variant="h6">{title}</Typography>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </Paper>
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md">
        <Paper elevation={3} sx={{ p: 4, mt: 4 }}>
          <Typography variant="h4" gutterBottom>
            Pathlet Personal Insights
          </Typography>

          <Tabs 
            value={activeTab} 
            onChange={handleTabChange} 
            variant="fullWidth"
            sx={{ mb: 3 }}
          >
            <Tab label="Ascendant" />
            <Tab label="Numerology" />
            <Tab label="Human Design" />
          </Tabs>

          <form onSubmit={handleSubmit(onSubmit)}>
            <Grid container spacing={3}>
              <Grid item xs={12}>
                <Controller
                  name="birth_date"
                  control={control}
                  rules={{ required: 'Birth date is required' }}
                  render={({ field, fieldState: { error } }) => (
                    <TextField
                      {...field}
                      type="date"
                      label="Birth Date"
                      fullWidth
                      variant="outlined"
                      InputLabelProps={{ shrink: true }}
                      error={!!error}
                      helperText={error?.message}
                    />
                  )}
                />
              </Grid>

              <Grid item xs={12} md={6}>
                <Controller
                  name="birth_time"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      {...field}
                      type="time"
                      label="Birth Time (Optional)"
                      fullWidth
                      variant="outlined"
                      InputLabelProps={{ shrink: true }}
                    />
                  )}
                />
              </Grid>

              <Grid item xs={12} md={6}>
                <Controller
                  name="birth_location"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      {...field}
                      label="Birth Location (Optional)"
                      fullWidth
                      variant="outlined"
                    />
                  )}
                />
              </Grid>

              <Grid item xs={12}>
                <Button 
                  type="submit" 
                  variant="contained" 
                  color="primary" 
                  fullWidth
                  disabled={loading}
                >
                  {loading ? 'Calculating...' : 'Get My Insights'}
                </Button>
              </Grid>
            </Grid>
          </form>

          {results && (
            <Box mt={4}>
              <Typography variant="h5" gutterBottom>
                Your Insights
              </Typography>
              
              {activeTab === 0 && renderInsightSection('Ascendant', results.ascendant)}
              {activeTab === 1 && renderInsightSection('Numerology', results.numerology)}
              {activeTab === 2 && renderInsightSection('Human Design', results.human_design)}
            </Box>
          )}
        </Paper>
      </Container>
    </ThemeProvider>
  );
};

export default App;
