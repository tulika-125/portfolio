import { useEffect, useState } from "react";

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/data")
      .then(response => response.json())
      .then(info => setData(info))
      .catch(error => console.log(error));
  }, []);

  if (!data) return <h2>Loading portfolio...</h2>;

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>{data.name}</h1>
      <h2>{data.role}</h2>

      <h3>About</h3>
      <p>{data.about}</p>

      <h3>Skills</h3>
      <ul>
        {data.skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <h3>Projects</h3>
      {data.projects.map((project, index) => (
        <div key={index} style={{ marginBottom: "20px" }}>
          <h4>{project.title}</h4>
          <p>{project.tech}</p>
          <p>{project.description}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
