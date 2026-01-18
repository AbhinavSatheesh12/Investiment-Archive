import React, { useState } from 'react';
import { Search } from 'lucide-react';

const SearchBar = ({ onSearch, isLoading }) => {
    const [ticker, setTicker] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (ticker.trim()) {
            onSearch(ticker);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="mb-8 w-full max-w-lg mx-auto">
            <div className="relative">
                <input
                    type="text"
                    value={ticker}
                    onChange={(e) => setTicker(e.target.value)}
                    placeholder="Enter ticker or company name (e.g. AAPL, Apple, Nvidia)"
                    className="w-full pl-12 pr-4 py-3 rounded-full bg-card-bg border border-slate-700 text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-all shadow-lg"
                    disabled={isLoading}
                />
                <Search className="absolute left-4 top-3.5 h-5 w-5 text-slate-400" />
                <button
                    type="submit"
                    className={`absolute right-2 top-2 px-4 py-1.5 bg-primary text-white rounded-full text-sm font-medium hover:bg-blue-600 transition-colors ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
                    disabled={isLoading}
                >
                    {isLoading ? 'Scanning...' : 'Analyze'}
                </button>
            </div>
        </form>
    );
};

export default SearchBar;
