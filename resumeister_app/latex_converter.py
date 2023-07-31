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

        \\summary{summary}

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



        \\end{{document}}  
    """

    #   \\begin{{workSection}}  {{Activities}}
    #             {activities_list}
    #         \\end{{workSection}}
    # \\end{{document}}
    education_list = """"""
    # for edu in resume_text.get("education"):
    #     mystr = """
    #         \\educationItem[
    #             university=""" + edu.get("university") + """,
    #             graduation=""" + edu.get("graduation") + """,
    #             grade=""" + edu.get("grade") + """,
    #             program=""" + edu.get("program") + """,
    #             coursework=""" + edu.get("coursework") + """
    #         ]
    #     """
    #     education_list += mystr
    experience_list = """"""
    # for exp in resume_text.get("experience"):
    #     print(exp)
    #     mystr = """
    #         \\experienceItem[
    #             company=""" + exp.get("company") + """,
    #             location=""" + exp.get("location") + """,
    #             position=""" + exp.get("position") + """,
    #             duration=""" + exp.get("duration") + """
    #         ]
    #         """
    #     flag = False
    #     points = """
    #         \\begin{{itemize}}
    #             \\itemsep -6pt {{}}"""
    #     for point in exp.get("points"):
    #         if point:
    #             points += "\\item " + point
    #             flag = True
    #     points += """
    #         \\end{{itemize}}
    #     """
    #     if flag:
    #         mystr += points
    #     experience_list += mystr
    skill_list = """"""
    for skill in resume_text.get("skills"):
        mystr = """\\skillItem[
            category=""" + skill.get("category") + """
            skills="""
        for i in skill.get("skills"):
            mystr += i + "{{,}} "
        mystr += """
        ]
        """
        skill_list += mystr

    # Fill in the template with the extracted information
    tex_content = tex_template.format(
        fullname=resume_text.get("fullname"), email=resume_text.get("email"), phone=resume_text.get("phone"),
        github=resume_text.get("github"), linkedin=resume_text.get("linkedin"), summary="",
        education_list=education_list, experience_list=experience_list, skill_list=skill_list,
        project_list=""
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
