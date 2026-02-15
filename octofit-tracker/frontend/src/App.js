


import logo from '../public/octofitapp-small.png';

function App() {
  return (
    <Router>
      <div className="container py-4">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 rounded">
          <div className="container-fluid">
            <NavLink className="navbar-brand fw-bold d-flex align-items-center" to="/">
              <img src={logo} alt="OctoFit Logo" className="octofit-logo me-2" />
              OctoFit Tracker
            </NavLink>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item"><NavLink className="nav-link" to="/activities">Activities</NavLink></li>
                <li className="nav-item"><NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink></li>
                <li className="nav-item"><NavLink className="nav-link" to="/teams">Teams</NavLink></li>
                <li className="nav-item"><NavLink className="nav-link" to="/users">Users</NavLink></li>
                <li className="nav-item"><NavLink className="nav-link" to="/workouts">Workouts</NavLink></li>
              </ul>
            </div>
          </div>
        </nav>
        <div className="mb-4 text-center">
          <h1 className="display-4 fw-bold">OctoFit Tracker</h1>
          <p className="lead">Track your fitness activities, teams, and progress!</p>
        </div>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<Activities />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
