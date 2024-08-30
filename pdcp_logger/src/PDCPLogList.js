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
            <h1>PDCP Logs</h1>
            <ul>
                {logs.map((log, index) => (
                    <li key={index}>
                        <pre>{JSON.stringify(log, null, 2)}</pre>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default PDCPLogList;
