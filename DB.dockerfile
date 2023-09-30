CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    technologies VARCHAR(255) NOT NULL,
    frontend_skills VARCHAR(255) NOT NULL,
    backend_skills VARCHAR(255) NOT NULL,
    databases_skills VARCHAR(255) NOT NULL,
    infrastructure_skills VARCHAR(255) NOT NULL,
    availability VARCHAR(255) NOT NULL
);
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    technologies VARCHAR(255) NOT NULL,
    frontend_skills VARCHAR(255) NOT NULL,
    backend_skills VARCHAR(255) NOT NULL,
    databases_skills VARCHAR(255) NOT NULL,
    infrastructure_skills VARCHAR(255) NOT NULL,
    availability VARCHAR(255) NOT NULL
);
INSERT INTO projects (name, technologies, frontend_skills, backend_skills, databases_skills, infrastructure_skills, availability)
VALUES ('Project 1', 'Python, Django, React', 'HTML, CSS, JavaScript', 'Python, Django', 'PostgreSQL', 'AWS', 'Full-time'),
       ('Project 2', 'Java, Spring Boot, Angular', 'HTML, CSS, TypeScript', 'Java, Spring Boot', 'MySQL', 'Azure', 'Part-time');
