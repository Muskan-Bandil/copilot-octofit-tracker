import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`
    : 'http://localhost:8000/api/teams/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
        console.log('Endpoint:', endpoint);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-header bg-info text-white d-flex align-items-center">
          <h3 className="mb-0">Teams</h3>
        </div>
        <div className="card-body">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              {teams.map((t, i) => (
                <tr key={i}>
                  <td>{t.id || i}</td>
                  <td>{t.name}</td>
                  <td>{t.description}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Teams;
