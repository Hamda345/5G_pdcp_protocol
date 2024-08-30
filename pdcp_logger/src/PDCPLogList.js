import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PDCPLogList = () => {
    const [logs, setLogs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchLogs = async () => {
            try {
                const response = await axios.get('http://localhost:5000/log');
                setLogs(response.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        fetchLogs();
    }, []);

    if (loading) return <p>Loading logs...</p>;
    if (error) return <p>Error fetching logs: {error}</p>;

    return (
        <div>
            <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '20px', textAlign: 'center' }}>PDCP Logs</h1>
            <ul style={{ listStyle: 'none', padding: 0 }}>
                {logs.map((log, index) => (
                    <li key={index} style={{ marginBottom: '15px', backgroundColor: '#f5f5f5', padding: '10px', borderRadius: '4px' }}>
                        <pre style={{ margin: 0, whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>
                            {JSON.stringify(log, null, 2)}
                        </pre>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default PDCPLogList;
