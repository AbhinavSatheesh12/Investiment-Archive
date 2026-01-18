import React, { useState } from 'react';
import { ExternalLink, TrendingUp, TrendingDown, Minus, ChevronDown, ChevronUp } from 'lucide-react';

const SentimentBadge = ({ sentiment }) => {
    let color = 'bg-slate-500';
    let Icon = Minus;

    if (sentiment === 'Positive' || sentiment === 'Bullish') {
        color = 'bg-success';
        Icon = TrendingUp;
    } else if (sentiment === 'Negative' || sentiment === 'Bearish') {
        color = 'bg-error';
        Icon = TrendingDown;
    }

    return (
        <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-md text-xs font-semibold text-white ${color}`}>
            <Icon size={12} />
            {sentiment}
        </span>
    );
};

const NewsItem = ({ item }) => (
    <div className="bg-card-bg p-5 rounded-lg border border-slate-800 hover:border-slate-600 transition-all shadow-md group">
        <div className="flex justify-between items-start gap-4">
            <a href={item.link} target="_blank" rel="noopener noreferrer" className="text-slate-200 font-medium group-hover:text-primary transition-colors leading-relaxed">
                {item.title}
            </a>
            <SentimentBadge sentiment={item.sentiment} />
        </div>
        <a href={item.link} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-xs text-slate-500 mt-3 hover:text-slate-300">
            Read <ExternalLink size={10} />
        </a>
    </div>
);

const NewsList = ({ news, overallSentiment }) => {
    const [isExpanded, setIsExpanded] = useState(false);
    const initialCount = 3;
    const hasMore = news.length > initialCount;
    const displayedNews = isExpanded ? news : news.slice(0, initialCount);

    return (
        <div className="flex-1 w-full md:ml-6">
            <div className="bg-card-bg p-6 rounded-xl shadow-lg border border-slate-700 mb-6">
                <div className="flex justify-between items-center">
                    <h2 className="text-2xl font-bold">Analysis Result</h2>
                    <div className="flex items-center gap-2">
                        <span className="text-slate-400 text-sm uppercase tracking-wider">Overall:</span>
                        <SentimentBadge sentiment={overallSentiment} />
                    </div>
                </div>
            </div>

            <div className="space-y-4">
                {displayedNews.map((item, index) => (
                    <NewsItem key={index} item={item} />
                ))}
            </div>

            {hasMore && (
                <button
                    onClick={() => setIsExpanded(!isExpanded)}
                    className="w-full mt-4 py-3 flex items-center justify-center gap-2 text-slate-400 hover:text-white bg-card-bg border border-slate-700 hover:border-slate-500 rounded-lg transition-all"
                >
                    {isExpanded ? (
                        <>
                            <ChevronUp size={18} />
                            Show Less
                        </>
                    ) : (
                        <>
                            <ChevronDown size={18} />
                            Show {news.length - initialCount} More Articles
                        </>
                    )}
                </button>
            )}
        </div>
    );
};

export default NewsList;
