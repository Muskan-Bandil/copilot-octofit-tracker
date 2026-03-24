import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`
    : 'http://localhost:8000/api/workouts/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
        console.log('Endpoint:', endpoint);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-header bg-warning text-dark d-flex align-items-center">
          <h3 className="mb-0">Workouts</h3>
        </div>
        <div className="card-body">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>ID</th>
                <th>User</th>
                <th>Workout</th>
                <th>Count</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((w, i) => (
                <tr key={i}>
                  <td>{w.id || i}</td>
                  <td>{w.user}</td>
                  <td>{w.workout}</td>
                  <td>{w.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
