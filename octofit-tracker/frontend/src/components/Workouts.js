import React, { useEffect, useMemo, useState } from 'react';

const getWorkoutsEndpoint = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.CODESPACE_NAME;
  if (codespaceName) {
    return `https://${codespaceName}-8000.app.github.dev/api/workouts/`;
  }
  return 'http://localhost:8000/api/workout-plans/';
};

function Workouts() {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const endpoint = useMemo(() => getWorkoutsEndpoint(), []);

  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        console.log('[Workouts] endpoint:', endpoint);
        const response = await fetch(endpoint);
        const data = await response.json();
        const normalized = Array.isArray(data) ? data : (data?.results || []);
        console.log('[Workouts] fetched data:', data);
        setRows(normalized);
      } catch (fetchError) {
        console.error('[Workouts] fetch error:', fetchError);
        setError('Failed to load workouts');
      } finally {
        setLoading(false);
      }
    };

    load();
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Workouts</h2>
      {loading && <p>Loading workouts...</p>}
      {error && <div className="alert alert-danger">{error}</div>}
      {!loading && !error && (
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Difficulty</th>
                <th>Duration (weeks)</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.title || item.name || '-'}</td>
                  <td>{item.difficulty_level || '-'}</td>
                  <td>{item.duration_weeks ?? '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Workouts;