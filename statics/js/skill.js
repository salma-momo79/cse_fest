const skills = [
    { name: 'JavaScript', description: 'Learn the basics of JavaScript', prerequisites: [] },
    { name: 'HTML & CSS', description: 'Master the core web technologies', prerequisites: [] },
    { name: 'React', description: 'Build user interfaces with React', prerequisites: ['JavaScript'] },
    { name: 'Node.js', description: 'Backend development with Node.js', prerequisites: ['JavaScript'] },
    { name: 'Python', description: 'General-purpose programming language', prerequisites: [] },
    { name: 'Django', description: 'Build web applications with Django', prerequisites: ['Python'] },
  ];
  
  const createSkillNode = (skill) => {
    const node = document.createElement('div');
    node.classList.add('skill-node');
    
    const title = document.createElement('h3');
    title.textContent = skill.name;
  
    const description = document.createElement('p');
    description.textContent = skill.description;
  
    node.appendChild(title);
    node.appendChild(description);
    return node;
  };
  
  const skillTreeContainer = document.getElementById('skill-tree');
  
  skills.forEach(skill => {
    const skillNode = createSkillNode(skill);
    skillTreeContainer.appendChild(skillNode);
  });
  