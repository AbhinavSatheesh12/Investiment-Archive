import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import NewsList from './components/NewsList';
import SentimentChart from './components/SentimentChart';
import { LayoutDashboard } from 'lucide-react';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (ticker) => {
    setLoading(true);
    setError(null);
    setData(null);

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/analyze', { ticker });
      setData(response.data);
    } catch (err) {
      console.error(err);
      setError('Failed to fetch data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-dark-bg p-6 md:p-12 text-slate-200 selection:bg-primary selection:text-white">
      <div className="max-w-6xl mx-auto">

        {/* Header */}
        <div className="text-center mb-12 animate-fade-in-down">
          <div className="inline-flex items-center justify-center p-3 bg-card-bg rounded-2xl mb-4 shadow-xl border border-slate-700">
            <LayoutDashboard className="text-primary h-8 w-8" />
          </div>
          <h1 className="text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400 mb-3">
            Financial Sentiment AI
          </h1>
          <p className="text-slate-400 text-lg">Real-time news analysis powered by DistilBERT</p>
        </div>

        {/* Search */}
        <SearchBar onSearch={handleSearch} isLoading={loading} />

        {/* Error */}
        {error && (
          <div className="max-w-lg mx-auto mb-8 p-4 bg-red-500/10 border border-red-500/50 rounded-lg text-red-500 text-center">
            {error}
          </div>
        )}

        {/* Results */}
        {data && (
          <div className="flex flex-col md:flex-row items-start animate-fade-in-up">
            <SentimentChart data={data.sentiment_counts} />
            <NewsList news={data.news_results} overallSentiment={data.overall_sentiment} />
          </div>
        )}

      </div>
    </div>
  );
}

export default App;
