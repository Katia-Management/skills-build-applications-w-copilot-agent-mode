import React, { useEffect, useMemo, useState } from 'react';

const getTeamsEndpoint = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.CODESPACE_NAME;
  if (codespaceName) {
    return `https://${codespaceName}-8000.app.github.dev/api/teams/`;
  }
  return 'http://localhost:8000/api/teachers/';
};

function Teams() {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const endpoint = useMemo(() => getTeamsEndpoint(), []);

  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        console.log('[Teams] endpoint:', endpoint);
        const response = await fetch(endpoint);
        const data = await response.json();
        const normalized = Array.isArray(data) ? data : (data?.results || []);
        console.log('[Teams] fetched data:', data);
        setRows(normalized);
      } catch (fetchError) {
        console.error('[Teams] fetch error:', fetchError);
        setError('Failed to load teams');
      } finally {
        setLoading(false);
      }
    };

    load();
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Teams</h2>
      {loading && <p>Loading teams...</p>}
      {error && <div className="alert alert-danger">{error}</div>}
      {!loading && !error && (
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Department</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.full_name || item.name || '-'}</td>
                  <td>{item.department || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Teams;