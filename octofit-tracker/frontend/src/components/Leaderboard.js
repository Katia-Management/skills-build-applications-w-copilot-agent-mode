import React, { useEffect, useMemo, useState } from 'react';

const getLeaderboardEndpoint = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.CODESPACE_NAME;
  if (codespaceName) {
    return `https://${codespaceName}-8000.app.github.dev/api/leaderboard/`;
  }
  return 'http://localhost:8000/api/performance-metrics/';
};

function Leaderboard() {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const endpoint = useMemo(() => getLeaderboardEndpoint(), []);

  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        console.log('[Leaderboard] endpoint:', endpoint);
        const response = await fetch(endpoint);
        const data = await response.json();
        const normalized = Array.isArray(data) ? data : (data?.results || []);
        console.log('[Leaderboard] fetched data:', data);
        setRows(normalized);
      } catch (fetchError) {
        console.error('[Leaderboard] fetch error:', fetchError);
        setError('Failed to load leaderboard');
      } finally {
        setLoading(false);
      }
    };

    load();
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Leaderboard</h2>
      {loading && <p>Loading leaderboard...</p>}
      {error && <div className="alert alert-danger">{error}</div>}
      {!loading && !error && (
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Student</th>
                <th>Fitness Score</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((item, index) => (
                <tr key={item.id || index}>
                  <td>{index + 1}</td>
                  <td>{item.student?.full_name || item.user_name || '-'}</td>
                  <td>{item.fitness_score ?? '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;