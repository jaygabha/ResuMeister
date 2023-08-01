import subprocess

def format_to_tex(resume_text):
    # Sample LaTeX template with sections for name, contact, education, and experience
    tex_template = """
        \\documentclass{{resume}} % Use the custom resume.cls style

        \\begin{{document}}

        \\introduction[
            fullname={fullname},
            email={email},
            phone={phone},
            linkedin={linkedin},
            github={github}
        ]

        \\summary{{summary}}

        \\education{{
            {education_list}
        }}

        \\skills{{
            {skill_list}
        }}

        \\begin{{workSection}}{{Experience}}
            {experience_list}


        \\end{{workSection}}

        \\begin{{workSection}}{{Academic projects}}
            {project_list} 

        \\end{{workSection}}  
        \\begin{{workSection}}  {{Certifications}}
            {certi_list}
            
        \\end{{workSection}}

        \\end{{document}}  
    """

    #
    education_list = """"""
    for edu in resume_text.get("education"):
        mystr = """
            \\educationItem[
                university=""" + str(edu.get("university")).replace(",","{,}") + """,
                graduation=""" + str(edu.get("duration")).replace(",","{,}") + """,
                grade=""" + str(edu.get("gpa")).replace(",","{,}") + """,
                program=""" + str(edu.get("degree")).replace(",","{,}") + """,
                coursework=""" + str(edu.get("coursework")[0]).replace(",","{,}") + """
            ]
        """
        education_list += mystr
    experience_list = """"""
    for exp in resume_text.get("experience"):
        mystr = """
            \\experienceItem[
                company=""" + str(exp.get("organization")).replace(",","{,}") + """,
                position=""" + str(exp.get("position")).replace(",","{,}") + """,
                duration=""" + str(exp.get("duration")).replace(",","{,}") + """
            ]
            """
        flag = False
        points = """
            \\begin{itemize}
                \\itemsep -6pt {}"""
        for point in exp.get("details"):
            if point:
                points += "\\item " + point
                flag = True
        points += """
            \\end{itemize}
        """
        if flag:
            mystr += points
        experience_list += mystr
    skill_list = """"""
    for skill in resume_text.get("skills"):
        mystr = """\\skillItem[
            category=""" + str(skill.get("category")) + """,
            skills="""
        for i in skill.get("skills"):
            if i:
                mystr += str(i) + "{,} "
        mystr = mystr[:-4]
        mystr += """
        ] \\\\
        """
        skill_list += mystr

    project_list = """"""
    for prj in resume_text.get("projects"):
        mystr = """
                \\customItem[
                    title=""" + str(prj.get("name")) + """,
                    organization=""" + str(prj.get("organization")) + """,
                    duration=""" + str(prj.get("duration")) + """
                ]
                """
        flag = False
        points = """
                \\begin{itemize}
                    \\itemsep -6pt {}"""
        for point in prj.get("details"):
            if point:
                points += "\\item " + point
                flag = True
        points += """
                \\end{itemize}
            """
        if flag:
            mystr += points
        project_list += mystr

    certi_list = """"""
    for cert in resume_text.get("certifications"):
        mystr = """
                    \\customItem[
                        title=""" + str(cert.get("name")) + """,
                        organization=""" + str(cert.get("organization")) + """,
                        duration=""" + str(cert.get("duration")) + """
                    ]
                    """
        flag = False
        points = """
                    \\begin{itemize}
                        \\itemsep -6pt {}"""
        for point in cert.get("details"):
            if point:
                points += "\\item " + point
                flag = True
        points += """
                    \\end{itemize}
                """
        if flag:
            mystr += points
        certi_list += mystr

    # Fill in the template with the extracted information
    tex_content = tex_template.format(
        fullname=resume_text.get("fullname"), email=resume_text.get("email"), phone=resume_text.get("phone"),
        github=resume_text.get("github"), linkedin=resume_text.get("linkedin"), summary=resume_text.get("summary"),
        education_list=education_list, experience_list=experience_list, skill_list=skill_list,
        project_list=project_list, certi_list=certi_list
    )

    return tex_content


def save_to_tex(tex_content, tex_file):
    with open(tex_file, 'w') as file:
        file.write(tex_content)


def convert_latex_to_pdf(tex_file):
    try:
        # Run pdflatex to compile the LaTeX file to PDF
        subprocess.check_call(['pdflatex', tex_file, "-interaction=batchmode"])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while converting: {e}")
    except FileNotFoundError:
        print("pdflatex not found. Make sure you have a LaTeX distribution installed.")
