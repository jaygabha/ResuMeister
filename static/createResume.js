// To add new form under Skill section when add button is clicked 

    // Function to add a new form
    function addskillForm() {
        skill_section++;
      // Create a new form element
      var form = document.createElement('form');
      form.className = 'skills skill_section_' + skill_section.toString();
      form.id = 'skill-form-1'

      //create a new div
      var div = document.createElement('div');
      div.className = 'skill-input-div'

      // Create input elements
      var categoryInput = document.createElement('input');
      categoryInput.type = 'text';
      categoryInput.name = 'skill_category_name';
      categoryInput.id = 'skill_category_id';
      categoryInput.className = 'skill_input_category'

      categoryInput.placeholder = "Category";
      
      var colon = document.createElement('p');
      colon.textContent=':'
      
      var skillInput = document.createElement('input');
      skillInput.type = 'text';
      skillInput.name = 'skill_skills_name';
      skillInput.id = 'skill_skills_id';
      skillInput.className = 'skill_input'

      skillInput.placeholder = "Skills";
      // Append the input elements to the div
      div.appendChild(categoryInput);
      div.appendChild(colon);
      div.appendChild(skillInput);

  
      form.appendChild(div);

      // Append the new form to the container
      var container = document.getElementById('formContainer-skills');
      container.appendChild(form);
    //   container.appendChild(lineBreak);
    }

    // Attach event listener to the "Add" button
    var addButton = document.getElementById('add-skills');
    addButton.addEventListener('click', addskillForm);
 

// To add new bulletpoint under Experience Role section when add button is clicked

// Function to add a new form
// Get the button element
var addButton = document.getElementById("add-experience-roles");

// Get the UL element
var ulExpRoles = document.getElementById("ul-exp-roles");

// Add event listener to the button
addButton.addEventListener("click", function () {
// Create a new LI element
var newLi = document.createElement("li");

// Create a new input element
var newInput = document.createElement("input");
newInput.type = "text";
newInput.name = "roles-bullet";
newInput.id = "roles-bullet";
newInput.className = "coursework-bullet";
newInput.placeholder = "write something";

// Append the input element to the LI
newLi.appendChild(newInput);

// Append the LI to the UL
ulExpRoles.appendChild(newLi);
});




// To add new form under Education section when add button is clicked 

    // Function to add a new form
    function addForm() {
      // Create a new form element
      education_section++;
      var form = document.createElement('form');
      form.className = 'education_section_'+education_section.toString();
      form.id = 'education_form'

      //create a new div
      var div = document.createElement('div');
      div.className = 'degree-duration'

      // Create input elements
      var degreeInput = document.createElement('input');
      degreeInput.type = 'text';
      degreeInput.name = 'degree';
      degreeInput.id = 'degree';
      degreeInput.placeholder = "Enter Your Program's Name";

      var durationInput = document.createElement('input');
      durationInput.type = 'text';
      durationInput.name = 'duration';
      durationInput.id = 'duration';
      durationInput.placeholder = 'Enter Duration';

      // Append the input elements to the div
      div.appendChild(degreeInput);
      div.appendChild(durationInput);

      var universityInput = document.createElement('input');
      universityInput.type = 'text';
      universityInput.name = 'university';
      universityInput.id = 'university';
      universityInput.placeholder = 'Enter Your University Name, City, Country';

      var gpaInput = document.createElement('input');
      gpaInput.type = 'text';
      gpaInput.name = 'gpa';
      gpaInput.id = 'gpa';
      gpaInput.className = 'gpa'
      gpaInput.placeholder = 'GPA';

      var courseLabel = document.createElement('label');
      courseLabel.id = 'coursework-label';
      courseLabel.className = 'coursework-label';
      courseLabel.textContent = 'Relevent Coursework:'

      var create_ul = document.createElement('ul');
      create_ul.className = 'ul-bullet-course';

      var create_li = document.createElement('li');

      var course_bullet_Input = document.createElement('input');
      course_bullet_Input.type = 'text';
      course_bullet_Input.name = 'coursework-bullet';
      course_bullet_Input.id = 'coursework-bullet';
      course_bullet_Input.className = 'coursework-bullet'
      course_bullet_Input.placeholder = 'write something';
      
      create_li.appendChild(course_bullet_Input)
      create_ul.appendChild(create_li)

    //   var educationTextArea = document.createElement('textarea');
    //   educationTextArea.name = 'education';
    //   educationTextArea.id = 'education-detail';
    //   educationTextArea.cols = '97';
    //   educationTextArea.rows = '3';
    //   educationTextArea.placeholder = 'Enter your education details in form';
      
      // Create a new line break element
      var lineBreak = document.createElement('br');

      // Append the input elements to the form
      form.appendChild(div);
      form.appendChild(universityInput);
      form.appendChild(gpaInput);
      form.appendChild(courseLabel);
      form.appendChild(create_ul);

      // Append the new form to the container
      var container = document.getElementById('formContainer');
      container.appendChild(form);
    //   container.appendChild(lineBreak);
    }

    // Attach event listener to the "Add" button
    var addButton = document.getElementById('add');
    addButton.addEventListener('click', addForm);
  

// To add new form under Experience section when add button is clicked 

// Function to add a new form
function addFormExperience() {
  // Create a new form element
  experience_section++;
  var form = document.createElement('form');
  form.className = 'experience_section_'+experience_section.toString();
  form.id = 'experience_form'

  //create a new div
  var div = document.createElement('div');
  div.className = 'experience-duration'

  // Create input elements
  var experienceInput = document.createElement('input');
  experienceInput.type = 'text';
  experienceInput.name = 'experience';
  experienceInput.id = 'experience';
  experienceInput.placeholder = 'Enter Your Postion';

  var durationInput = document.createElement('input');
  durationInput.type = 'text';
  durationInput.name = 'duration';
  durationInput.id = 'duration';
  durationInput.placeholder = 'Enter Duration';

  // Append the input elements to the div
  div.appendChild(experienceInput);
  div.appendChild(durationInput);

  var organisationInput = document.createElement('input');
  organisationInput.type = 'text';
  organisationInput.name = 'organisation';
  organisationInput.id = 'organisation';
  organisationInput.placeholder = 'Enter Your organisation Name, City, Country';

  var experienceTextArea = document.createElement('textarea');
  experienceTextArea.name = 'experience';
  experienceTextArea.id = 'experience-detail';
  experienceTextArea.cols = '97';
  experienceTextArea.rows = '3';
  experienceTextArea.placeholder = 'Enter your experience details in form';
  
  // Create a new line break element
  var lineBreak = document.createElement('br');

  // Append the input elements to the form
  form.appendChild(div);
  form.appendChild(organisationInput);
  form.appendChild(experienceTextArea);

  // Append the new form to the container
  var container = document.getElementById('form-container-experience');
  container.appendChild(form);
//   container.appendChild(lineBreak);
}

// Attach event listener to the "Add" button
var addButton = document.getElementById('add-experience');
addButton.addEventListener('click', addFormExperience);



// To add new form under Projects section when add button is clicked 

// Function to add a new form
function addFormProject() {
  // Create a new form element
  project_section++;
  var form = document.createElement('form');
  form.className = 'project_section_'+project_section.toString();
  form.id = 'project_form'

  //create a new div
  var div = document.createElement('div');
  div.className = 'project-duration'

  // Create input elements
  var projectInput = document.createElement('input');
  projectInput.type = 'text';
  projectInput.name = 'project';
  projectInput.id = 'project';
  projectInput.placeholder = 'Enter Your Project Name';

  var durationInput = document.createElement('input');
  durationInput.type = 'text';
  durationInput.name = 'duration';
  durationInput.id = 'duration';
  durationInput.placeholder = 'Enter Duration';

  // Append the input elements to the div
  div.appendChild(projectInput);
  div.appendChild(durationInput);

  var organisationInput = document.createElement('input');
  organisationInput.type = 'text';
  organisationInput.name = 'organisation';
  organisationInput.id = 'organisation-project';
  organisationInput.placeholder = 'Enter Your organisation Name, City, Country';

  var projectTextArea = document.createElement('textarea');
  projectTextArea.name = 'project';
  projectTextArea.id = 'project-detail';
  projectTextArea.cols = '97';
  projectTextArea.rows = '3';
  projectTextArea.placeholder = 'Enter your project details in form';
  
  // Create a new line break element
  var lineBreak = document.createElement('br');

  // Append the input elements to the form
  form.appendChild(div);
  form.appendChild(organisationInput);
  form.appendChild(projectTextArea);

  // Append the new form to the container
  var container = document.getElementById('form-container-project');
  container.appendChild(form);
//   container.appendChild(lineBreak);
}

// Attach event listener to the "Add" button
var addButton = document.getElementById('add-project');
addButton.addEventListener('click', addFormProject);



// To add new form under Certifications section when add button is clicked 

// Function to add a new form
function addFormCertifications() {
  // Create a new form element
  certification_section++;
  var form = document.createElement('form');
  form.className = 'certification_section_'+certification_section.toString();
  form.id = 'certification_form'

  //create a new div
  var div = document.createElement('div');
  div.className = 'project-duration'

  // Create input elements
  var certificationInput = document.createElement('input');
  certificationInput.type = 'text';
  certificationInput.name = 'certification';
  certificationInput.id = 'certification';
  certificationInput.placeholder = 'Certification Name';

  var durationInput = document.createElement('input');
  durationInput.type = 'text';
  durationInput.name = 'duration';
  durationInput.id = 'duration';
  durationInput.placeholder = 'Enter Duration';

  // Append the input elements to the div
  div.appendChild(certificationInput);
  div.appendChild(durationInput);

  var organisationInput = document.createElement('input');
  organisationInput.type = 'text';
  organisationInput.name = 'organisation';
  organisationInput.id = 'organisation';
  organisationInput.placeholder = 'Issuing organisation';

  var certificationTextArea = document.createElement('textarea');
  certificationTextArea.name = 'certification';
  certificationTextArea.id = 'certification-detail';
  certificationTextArea.cols = '97';
  certificationTextArea.rows = '3';
  certificationTextArea.placeholder = 'Enter your certificate details in form';
  
  // Create a new line break element
  var lineBreak = document.createElement('br');

  // Append the input elements to the form
  form.appendChild(div);
  form.appendChild(organisationInput);
  form.appendChild(certificationTextArea);

  // Append the new form to the container
  var container = document.getElementById('form-container-certifications');
  container.appendChild(form);
//   container.appendChild(lineBreak);
}

// Attach event listener to the "Add" button
var addButton = document.getElementById('add-certifications');
addButton.addEventListener('click', addFormCertifications);



var skill_section = 1
var education_section = 1
var experience_section = 1
var project_section = 1
var certification_section = 1



function removeFormSkill() {
    if (skill_section>1){
        var form = document.querySelector(".skill_section_" + skill_section.toString())
        form.remove();
        skill_section--;
    }
    else{
        console.log("Only one skill section")
    }
}

function removeForm() {
    if (education_section>1){
        var form = document.querySelector(".education_section_" + education_section.toString())
        form.remove();
        education_section--;
    }
    else{
        console.log("Only one skill section")
    }
//   var form = document.getElementById('education-form-1');
//   form.remove();
}

function removeFormExperience() {
    if(experience_section > 1){
        var form = document.querySelector(".experience_section_" + experience_section.toString())
        form.remove();
        experience_section--;

    }
    else{
        console.log("Only one skill section")
    }
    
    //   var form = document.getElementById('experience-form-1');
    //   form.remove();
}

function removeFormProject() {
    if(project_section > 1){
        var form = document.querySelector(".project_section_" + project_section.toString())
        form.remove();
        project_section--;

    }
    else{
        console.log("Only one skill section")
    }
//   var form = document.getElementById('project-form-1');
//   form.remove();
}

function removeFormCertification() {
    if(certification_section > 1){
        var form = document.querySelector(".certification_section_" + certification_section.toString())
        form.remove();
        certification_section--;

    }
    else{
        console.log("Only one skill section")
    }
//   var form = document.getElementById('certification-form-1');
//   form.remove();
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function eraseCookie(name) {
            document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

function parse_data(){
    let parsed_string = getCookie("parse_data")
    parsed_string = parsed_string.replaceAll(/\\054/g, ',');
    parsed_string = parsed_string.slice(1,)
    parsed_string = parsed_string.slice(0,-1)
    parsed_string = parsed_string.replaceAll("\'", "\"");
    console.log(parsed_string);
    let data = JSON.parse(parsed_string);
    console.log(data);
    let header_form_1 = document.querySelector(".header-inputs1");
    let name = header_form_1.querySelector("input[id='name']");
    name.value = data["fullname"];
    let linkedin = header_form_1.querySelector("input[id='linkedIn']");
    linkedin.value = data["linkedin"];
    let header_form_2 = document.querySelector(".header-inputs2");
    let email = header_form_2.querySelector("input[id='email']");
    email.setAttribute('value', data["email"]);
    let phone = header_form_2.querySelector("input[id='phone']");
    phone.setAttribute('value', data["phone"]);
    let github = header_form_2.querySelector("input[id='github']");
    github.setAttribute('value', data["github"]);
    let summary = document.querySelector("textarea[id='summary-detail']")
    summary.setAttribute('value', data["summary"])
    var skills = []
    skills = data["skills"];
    for(let i=0;i<skills.length;i++){
        let skill_form = document.querySelector(".skill_section_" + skill_section.toString())
        let category = skill_form.querySelector("input[id='skill_category_id']");
        category.setAttribute('value', skills[i]["category"]);
        let skills_ele = skill_form.querySelector("input[id='skill_skils_id']");
        skills_string = ""
        for(let j=0;j<skills[i]["skills"].length;j++){
            skills_string += skills[i]["skills"][j];
            skills_string += ", ";
        }
        skills_ele.setAttribute('value', skills_string);
        document.querySelector("button[id='add-skills']").click();
    }
}

function extract_data(){
    eraseCookie("extract_data")
    let extract = {}
    let header_form_1 = document.querySelector(".header-inputs1");
    let fullname = header_form_1.querySelector("input[id='name']").value;
    let linkedin = header_form_1.querySelector("input[id='linkedIn']").value;
    let header_form_2 = document.querySelector(".header-inputs2");
    let email = header_form_2.querySelector("input[id='email']").getAttribute('value');
    let phone = header_form_2.querySelector("input[id='phone']").getAttribute('value');
    let github = header_form_2.querySelector("input[id='github']").getAttribute('value');
    let summary = document.querySelector("textarea[id='summary-detail']").getAttribute('value');
    extract["fullname"] = fullname
    extract["linkedin"] = linkedin
    extract["email"] = email
    extract["phone"] = phone
    extract["github"] = github
    extract["summary"] = summary
    extract["skills"] = []
    for(let i=1;i<=skill_section;i++){
        let skill = {}
        let skill_form = document.querySelector(".skill_section_" + i.toString())
        let category_ele = skill_form.querySelector("input[id='skill_category_id']") !== null
        if(category_ele ){
            skill["category"] = skill_form.querySelector("input[id='skill_category_id']").getAttribute('value');
        }
        else {
            continue
        }
        // console.log(skill_form.querySelector("input[id='skill_skils_id']"))
        let skill_ele = skill_form.querySelector("input[id='skill_skils_id']") !== null
        if (skill_ele){
            let skills_list = skill_form.querySelector("input[id='skill_skils_id']").getAttribute('value');
            if(skills_list !== null) {
                skill["skills"] = skills_list.split(", ");
            }
            else {
                skill["skills"] = []
            }
        }
        else {
            continue
        }

        extract["skills"].push(skill);
    }
    console.log(extract)
    setCookie("extract_data", JSON.stringify(extract))
    // window.location.assign("/saveResume")
}