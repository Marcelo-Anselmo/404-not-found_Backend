from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def created_pdf(professor, alunos):

    data_professor = professor[0]

    def formatar_data_brasileira(data):
        if not data:
            return None

        return data.strftime("%d/%m/%Y %H:%M:%S")

    arquivo_pdf = canvas.Canvas("ata_online.pdf", pagesize=A4)

    arquivo_pdf.drawString(280, 800, "ATA Online")

    arquivo_pdf.drawString(
        60,
        760,
        "Professor:",
    )
    arquivo_pdf.drawString(120, 760, data_professor.nome)

    arquivo_pdf.drawString(280, 760, "Disciplina: ")
    arquivo_pdf.drawString(340, 760, data_professor.disciplina)

    arquivo_pdf.drawString(60, 730, "Data: ")
    arquivo_pdf.drawString(
        95, 730, str(formatar_data_brasileira(data_professor.created_at))
    )

    arquivo_pdf.drawString(280, 730, "Aula: ")
    arquivo_pdf.drawString(310, 730, str(data_professor.aula))

    arquivo_pdf.drawString(380, 730, "Turno:")
    arquivo_pdf.drawString(420, 730, data_professor.turno)

    arquivo_pdf.drawString(60, 700, "Descrição: ")
    arquivo_pdf.drawString(120, 700, data_professor.descricao)

    arquivo_pdf.drawString(
        60,
        680,
        "______________________________________________________________________",
    )

    eixo_y = 640
    eixo_x = 60

    for aluno in alunos:

        arquivo_pdf.drawString(
            eixo_x,
            eixo_y - 20,
            "_______________________________________________________________________",
        )

        arquivo_pdf.drawString(eixo_x, eixo_y, "Aluno:")
        eixo_x += 35
        arquivo_pdf.drawString(eixo_x, eixo_y, aluno.nome)
        eixo_y -= 15
        eixo_x -= 35
        arquivo_pdf.drawString(eixo_x, eixo_y, "Curso:")
        eixo_x += 40
        arquivo_pdf.drawString(eixo_x, eixo_y, aluno.curso)
        eixo_x += 160
        arquivo_pdf.drawString(eixo_x, eixo_y, "RA:")
        eixo_x += 25
        arquivo_pdf.drawString(eixo_x, eixo_y, str(aluno.RA))
        eixo_x += 95
        arquivo_pdf.drawString(eixo_x, eixo_y, "Data:")
        eixo_x += 40
        arquivo_pdf.drawString(
            eixo_x, eixo_y, str(formatar_data_brasileira(aluno.created_at))
        )

        eixo_x -= 360
        eixo_y -= 30

    arquivo_pdf.save()

    def send_email(professor):
        corpo_email = """
        <p>Obrigado por usar no sistema de Autentica Ulife!</p>
        <p>Segue em anexo a ata em pdf</p>
        """

        msg = MIMEMultipart()
        msg["Subject"] = (
            f"Lista de Presença/Disciplina: {professor.disciplina}/Data: {str(formatar_data_brasileira(professor.created_at))}"
        )
        msg["From"] = "group.404.error.not.found@gmail.com"
        msg["To"] = professor.email
        password = "wgdiquculfxyvhjw"
        msg.attach(MIMEText(corpo_email, "html"))

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        cam_arquivo = os.path.join(diretorio_atual, "ata_online.pdf")
        # cam_arquivo = "C:/Users/lucia/OneDrive/Documentos/Meus Projetos/404-not-found_Backend/ata_online.pdf"

        with open(cam_arquivo, "rb") as file:
            anexo = MIMEApplication(file.read(), _subtype="pdf")
            anexo.add_header(
                "Content-Disposition", "attachment", filename="ata_online.pdf"
            )

        msg.attach(anexo)

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))

    send_email(data_professor)
