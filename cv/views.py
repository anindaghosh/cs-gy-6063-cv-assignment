from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):

    template = loader.get_template("cv/index.html")

    context = {
        "skills": [
            "Python",
            "JavaScript",
            "Java",
            "Kotlin",
            "Dart",
            "Dot.Net" "React",
            "Flask",
            "Express.js",
            "Tensorflow",
            "Keras",
            "Azure Cloud",
            "Azure DevOps",
            "Azure Portal",
            "Power Automate",
            "PowerBI",
            "Microsoft SQL Server Management Studio",
            "Azure Data Studio",
            "Snyk",
            "Checkmarx",
            "SonarCloud",
            "Apiiro",
            "Imperva",
            "Netskope",
            "Azure Data Factory",
        ],
        "professional_experience": [
            {
                "position": "Solutions Architect",
                "organization": "AB InBev India",
                "duration": "Aug 2021 - Jul 2024",
                "responsibilites": [
                    "Orchestrated and designed multiple global digital solutions spanning functions like Finance, Supply Chain, Logistics, Facility Management and Employee Experience while leading dynamic tech squads adhering to Agile methodologies and Scrum.",
                    "Orchestrated the seamless establishment of robust infrastructure environments for web applications through automated utilization of Terraform on Azure, ensuring optimal scalability, security, and efficiency in deployment processes.",
                    "Collaborated closely with the global application security team, serving as the designated security champion for ensuring comprehensive compliance with application security standards. Implemented and oversaw the integration of SAST, DAST, and SCA practices using cutting-edge tools like Apiiro, Snyk, Checkmarx, and SonarCloud. Adhered rigorously to OWASP Top 10 principles, ensuring the highest standards of security in global products.",
                    "Collaborated with various tech hubs, driving initiatives to enhance development metrics championed the creation and sharing of reusable components, and facilitated the exchange of best practices, fostering a culture of continuous improvement, inner-sourcing and knowledge-sharing across the organization.",
                ],
            }
        ],
        "publications": [
            {
                "title": "LOGISWARM: A low-cost multi-robot testbed for cooperative transport research",
                "organization": "Multimedia Tools and Applications",
                "edition": "Volume 81, March 2022",
                "doi": "10.1007/s11042-022-12689-3",
            },
            {
                "title": "Content based Item-Item Recommendation System based on User Interactions in E-Commerce Applications",
                "organization": "High Technology Letters",
                "edition": "Volume 27 Issue 4, April 2021",
                "doi": "10.37896/HTL27.4/3345",
            },
        ],
    }

    return render(request=request, template_name="cv/index.html", context=context)
