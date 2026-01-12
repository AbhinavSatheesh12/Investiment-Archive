import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';

const SentimentChart = ({ data }) => {
    const chartData = [
        { name: 'Positive', value: data.Positive, color: '#22c55e' },
        { name: 'Negative', value: data.Negative, color: '#ef4444' },
        { name: 'Neutral', value: data.Neutral, color: '#94a3b8' },
    ].filter(d => d.value > 0);

    if (chartData.length === 0) return null;

    return (
        <div className="bg-card-bg p-6 rounded-xl shadow-lg border border-slate-700 w-full md:w-1/3 mb-8 md:mb-0 h-80">
            <h3 className="text-xl font-semibold mb-4 text-center text-slate-200">Sentiment Distribution</h3>
            <ResponsiveContainer width="100%" height="85%">
                <PieChart>
                    <Pie
                        data={chartData}
                        cx="50%"
                        cy="50%"
                        innerRadius={60}
                        outerRadius={80}
                        paddingAngle={5}
                        dataKey="value"
                    >
                        {chartData.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={entry.color} />
                        ))}
                    </Pie>
                    <Tooltip
                        contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '8px', color: '#fff' }}
                    />
                    <Legend />
                </PieChart>
            </ResponsiveContainer>
        </div>
    );
};

export default SentimentChart;
