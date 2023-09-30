import React, { useState } from "react";
import { useEffect } from "react";
import axios from "axios";

const SmartProjectSearch = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    async function fetchProjects() {
      const response = await axios.post("/api/search-projects", { searchTerm });
      setProjects(response.data);
    }

    fetchProjects();
  }, [searchTerm]);

  return (
    <div>
      <h1>Smart Project Search</h1>

      <input
        type="text"
        id="search-term"
        placeholder="Search for projects..."
        value={searchTerm}
        onChange={(event) => setSearchTerm(event.target.value)}
      />

      <button onClick={() => fetchProjects()}>Search</button>

      <ul id="project-gallery">
        {projects.map((project) => (
          <li key={project.id}>
            <h3>{project.name}</h3>
            <p>{project.technologies}</p>
            <p>{project.availability}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SmartProjectSearch;
