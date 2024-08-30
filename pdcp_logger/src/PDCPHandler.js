import React, { useState } from 'react';

const PDCPHandler = () => {
  const [ipPacket, setIpPacket] = useState('');
  const [snLength, setSnLength] = useState('12');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);
    setIsLoading(true);

    if (!ipPacket) {
      setError('Please enter an IP packet in hexadecimal format.');
      setIsLoading(false);
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/process_packet', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ip_packet: ipPacket, sn_length: parseInt(snLength) }),
      });

      if (!response.ok) {
        throw new Error('Failed to process packet');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', padding: '20px', backgroundColor: 'white', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)' }}>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '20px', textAlign: 'center' }}>5G PDCP Protocol Packer Process</h1>
      <div style={{ marginBottom: '20px' }}>
        <h2 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '10px' }}>Input Parameters</h2>
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          <div>
            <label htmlFor="ipPacket" style={{ display: 'block', marginBottom: '5px', fontSize: '14px' }}>
              IP Packet (in hex)
            </label>
            <input
              id="ipPacket"
              type="text"
              value={ipPacket}
              onChange={(e) => setIpPacket(e.target.value)}
              placeholder="e.g., 4500001c0001000040060000c0a80001c0a80002"
              style={{ width: '100%', padding: '8px', border: '1px solid #ccc', borderRadius: '4px' }}
            />
          </div>
          <div>
            <label htmlFor="snLength" style={{ display: 'block', marginBottom: '5px', fontSize: '14px' }}>
              Sequence Number Length
            </label>
            <select
              id="snLength"
              value={snLength}
              onChange={(e) => setSnLength(e.target.value)}
              style={{ width: '100%', padding: '8px', border: '1px solid #ccc', borderRadius: '4px' }}
            >
              <option value="12">12 bits</option>
              <option value="18">18 bits</option>
            </select>
          </div>
          <button 
            type="submit" 
            disabled={isLoading}
            style={{ 
              padding: '10px', 
              backgroundColor: isLoading ? '#ccc' : '#007bff', 
              color: 'white', 
              border: 'none', 
              borderRadius: '4px', 
              cursor: isLoading ? 'not-allowed' : 'pointer' 
            }}
          >
            {isLoading ? 'Processing...' : 'Process Packet'}
          </button>
        </form>
      </div>

      {error && (
        <div style={{ backgroundColor: '#f8d7da', color: '#721c24', padding: '10px', borderRadius: '4px', marginTop: '15px' }}>
          <p>{error}</p>
        </div>
      )}

      {result && (
        <div style={{ marginTop: '20px' }}>
          <h2 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '10px' }}>Processing Result</h2>
          <pre style={{ backgroundColor: '#f5f5f5', padding: '15px', borderRadius: '4px', overflowX: 'auto', fontSize: '14px' }}>
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default PDCPHandler;
