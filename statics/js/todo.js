document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("course-form");
    const courseList = document.getElementById("course-list");
    const alertBox = document.getElementById("alert");
  

    const savedCourses = JSON.parse(localStorage.getItem("courses")) || [];
    savedCourses.forEach(course => addCourseToDOM(course));
  
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const courseName = document.getElementById("courseName").value.trim();
      const previousCGPA = parseFloat(document.getElementById("previousCGPA").value.trim());
  
      if (!courseName || isNaN(previousCGPA)) {
        showAlert("Please fill in all fields correctly!", "danger");
        return;
      }
  
      const course = { name: courseName, cgpa: previousCGPA };
      addCourseToDOM(course);
      saveCourse(course);
      form.reset();
      showAlert("Course added successfully!", "success");
    });
  
    function addCourseToDOM(course) {
      const li = document.createElement("li");
      li.className = "list-group-item d-flex justify-content-between align-items-center";
      li.innerHTML = `
        <div>
          <strong>${course.name}</strong> - Previous CGPA: ${course.cgpa.toFixed(2)}
        </div>
        <button class="btn btn-sm btn-danger delete-btn">🗑️</button>
      `;
      courseList.appendChild(li);
  
      // Delete logic
      li.querySelector(".delete-btn").addEventListener("click", () => {
        courseList.removeChild(li);
        deleteCourse(course);
        showAlert("Course removed.", "warning");
      });
    }
  
    function saveCourse(course) {
      const courses = JSON.parse(localStorage.getItem("courses")) || [];
      courses.push(course);
      localStorage.setItem("courses", JSON.stringify(courses));
    }
  
    function deleteCourse(courseToDelete) {
      let courses = JSON.parse(localStorage.getItem("courses")) || [];
      courses = courses.filter(course => course.name !== courseToDelete.name || course.cgpa !== courseToDelete.cgpa);
      localStorage.setItem("courses", JSON.stringify(courses));
    }
  
    function showAlert(message, type) {
      alertBox.textContent = message;
      alertBox.className = `alert alert-${type}`;
      alertBox.classList.remove("d-none");
      setTimeout(() => alertBox.classList.add("d-none"), 3000);
    }
  });
  