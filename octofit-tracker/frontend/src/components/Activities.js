import React, { useEffect, useMemo, useState } from 'react';

const getActivitiesEndpoint = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.CODESPACE_NAME;
  if (codespaceName) {
    return `https://${codespaceName}-8000.app.github.dev/api/activities/`;
  }
  return 'http://localhost:8000/api/activity-logs/';
};

function Activities() {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const endpoint = useMemo(() => getActivitiesEndpoint(), []);

  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        console.log('[Activities] endpoint:', endpoint);
        const response = await fetch(endpoint);
        const data = await response.json();
        const normalized = Array.isArray(data) ? data : (data?.results || []);
        console.log('[Activities] fetched data:', data);
        setRows(normalized);
      } catch (fetchError) {
        console.error('[Activities] fetch error:', fetchError);
        setError('Failed to load activities');
      } finally {
        setLoading(false);
      }
    };

    load();
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Activities</h2>
      {loading && <p>Loading activities...</p>}
      {error && <div className="alert alert-danger">{error}</div>}
      {!loading && !error && (
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Exercise</th>
                <th>Date</th>
                <th>Duration</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.exercise?.name || item.activity_type || '-'}</td>
                  <td>{item.date || '-'}</td>
                  <td>{item.duration_minutes || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Activities;