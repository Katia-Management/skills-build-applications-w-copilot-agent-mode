import React, { useEffect, useMemo, useState } from 'react';

const getUsersEndpoint = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.CODESPACE_NAME;
  if (codespaceName) {
    return `https://${codespaceName}-8000.app.github.dev/api/users/`;
  }
  return 'http://localhost:8000/api/students/';
};

function Users() {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const endpoint = useMemo(() => getUsersEndpoint(), []);

  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        console.log('[Users] endpoint:', endpoint);
        const response = await fetch(endpoint);
        const data = await response.json();
        const normalized = Array.isArray(data) ? data : (data?.results || []);
        console.log('[Users] fetched data:', data);
        setRows(normalized);
      } catch (fetchError) {
        console.error('[Users] fetch error:', fetchError);
        setError('Failed to load users');
      } finally {
        setLoading(false);
      }
    };

    load();
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Users</h2>
      {loading && <p>Loading users...</p>}
      {error && <div className="alert alert-danger">{error}</div>}
      {!loading && !error && (
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Full Name</th>
                <th>Email</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.user?.username || item.username || '-'}</td>
                  <td>{item.full_name || `${item.user?.first_name || ''} ${item.user?.last_name || ''}`.trim() || '-'}</td>
                  <td>{item.user?.email || item.email || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Users;