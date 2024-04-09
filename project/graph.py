import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import carboninputs
from reportlab.lib.styles import getSampleStyleSheet




energy = carboninputs.Inputs.energy_usage()
waste = carboninputs.Inputs.wastes()
travel = carboninputs.Inputs.business_travel()

def show_data():
    
    labels = 'energy usage', 'waste', 'business travel'
    sizes = [energy,waste, travel]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    # plt.legend([f'energy {energy} CO2', f'waste {waste} CO2', f'travel {travel} CO2'],loc="best")

    plt.savefig("carbon_emission_plot.png")
    
    plt.plot()
    plt.show()
    plt.close()
    
show_data()

    
text_high_energy = ["since overall employees use too much energy we recommend that employees should monitor and"
                    ,"analyze energy usage and reduce energy"
                     ,"use by replacing old equipment or energy inefficient equipments and to new efficient equipment "]


text_medium_energy = [f"employees use medium or less amount of energy  wich is {energy} and its less than half ",
                      "amount of the maximum which is 14 000 , the amount of energy using is at a safe zone",
                      "but still it would be better if the amount was close to zero"]

text_medium_waste = [f"the amount of waste in the corporation is at a average or medium range which is {waste} and its less",
                     "than a half of the maximum which is 682, it's adviced that the more material being recycled or "
                     ,"composed the better result you will get"]

text_medium_travel = ["the amount of CO2 that being produced by travling is at a good rate even though employees can reduce",
                      "to less than amount or close to zero, by working remote from home or takin public transportaions",
                      f"the current amount being procuced is {travel} wich is less than the maximim (23100)"]



text_high_waste = ["the material waste is high it is recommended to use less harmful material and replace "
                    ,"long lasting matterials to disposble ones, it is advised to recycle the the products and , " 
                     ,"reuse materials sometimes wastes can be useful if it was used to produce energy from it "]

text_high_travel = ["travels can be optimized by encouraging employees to use public transports or choose low emission "
                    ,"vehicles providing remote work options so that employees don not travel out of needs, reducing air travels"]

if energy<=energy/2:
    text_of_energy = text_medium_energy
else:
    text_of_energy = text_high_energy

if waste<=waste/2:
    text_of_waste = text_medium_waste
else:
    text_of_waste = text_high_energy

if travel<=travel/2:
    text_of_travel = text_medium_travel
else:
    text_of_travel = text_high_travel

advice = [text_of_energy," ", text_of_waste," ", text_of_travel]



def create_pdf():
    pdf_path = 'carbon_emission_report.pdf'
    pdf = canvas.Canvas(pdf_path, pagesize=A4)
    pdf.setTitle("Report")
    
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf')) 
    # Inserting Title
    pdf.setFont("Arial", 16)
    pdf.drawString(210, 770, "Carbon Emission Footprint")
    pdf.line(30, 740, 550, 740)

    textline = ["energey usage",
                "wastes",
                "business travel"]
    
    text = pdf.beginText(30, 680)
    text.setFont("Arial", 12)
    for line in textline:
        text.textLine(line)
    pdf.drawText(text)
    pdf.setFont("Arial", 12)
    pdf.drawString(25, 700, "the follow informations below analyze how much this company produce carbon by three diffent methonds")
    # Inserting Graph
    pdf.drawInlineImage('carbon_emission_plot.png', 50, 300, width=450, height=300)
    text1 = pdf.beginText(30, 200)
    text1.setFont("Arial", 12)
    for text in advice:
        
        for line in text:
            
            text1.textLine(line)
    pdf.drawText(text1)

    print(f"PDF generated successfully at: {pdf_path}")

     # Save the canvas to the pdf
    pdf.save()
# Execute the functions
create_pdf()

print(f"energy is {energy} waste is {waste} travel is {travel}")

