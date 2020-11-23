#Letter Generator

from docxtpl import DocxTemplate
import random
import datetime
import jinja2


#initialise variables

lines = []

RE_list = ["Objective study on cannabis in Namibia","Prohibition of cannabis in Namibia","Legalizing cannabis in Namibia","Drug war hysteria subsides: A Case Study","Public Health Promotion and Protection","Medical Cannabis Policies: Namibia","Medical Cannabis Legalizationin Nambibia","Public Opinion and Cannabis Legalisation","Recreational Purposes Is Acceptable","Public Support For Medical Cannabis Legalization","A Cannabis Legalization Framework","Cannabis is Expanding in Suothern Africa","Commercial Production Of Cannabis For Therapeutic Purposes","Achieving Public Health Goals in Namibia","Developmental Harms of Cannabis NOT Well Understood","National Policies On Cannabis Development","Peer Revieved Scientific Literature: Namibia and Cannabis","Boundaries of Cannabis Use in Namibia","Cannabis and Southern African Black Market Trade","World Cannabis Report On Welfare","Cannabis in Canada: A Case Study","World Health Report: Portugal and Hard Drugs","Prevalence of Cannabis Use in Namibia","Prohibition and Cannabis Prevalence: A Namibian Context","Reducing Use of Hard Drugs in Namibia","Promoting Natural Remedies in Namibia: Cannabis and relaed products","Regulating Cannabis in Namibia","Banning Prohibition of Natural Resources: A study of cannabis resources","Decriminalising and Regulating Cannabis in Namibia","Cannabis Societies in Namibia","Cannabis in the MIning Industry","Tourism and Cannabis: Namibia's Potential","Responsible Cannabis Use In Namibia","Making better decisions: Cananbis and Namibia","Health and Harm: Cannabis is Safe"]



#Compile letters

for i in range(0,100):

    p_box = random.randint(0,999)
    loc_id = random.choice(["Swakopmund", "Grootfontein","Rundu", "Otjiwarongo","Walvis Bay", "Ongwediva", "Keetmenshoop", "Mariental", "Okahandja", "Windhoek", "Katima Mulilo", "Oshakati", "Tsumeb", "Rehoboth", "Luderitz", "Gobabis"])
    today = datetime.date.today()    
    today_date = str(today.day) + " " +str(today.strftime('%B'))+" "+str(today.year)

    #Generate RE
    RE = random.choice(RE_list)
    



    #Generate content

    with open("content.txt") as content:
        lines = content.readlines()
  

    para_1 = random.choice(lines).strip()
    para_2 = random.choice(lines).strip()
    para_3 = random.choice(lines).strip()
    para_4 = random.choice(lines).strip()
    para_5 = random.choice(lines).strip()
    para_6 = random.choice(lines).strip()
    para_7 = random.choice(lines).strip()


    if para_1 == para_2 == para_3 == para_4 == para_5 == para_6 == para_7:
       
        para_1 = random.choice(lines).strip()
        para_2 = random.choice(lines).strip()
        para_3 = random.choice(lines).strip()
        para_4 = random.choice(lines).strip()
        para_5 = random.choice(lines).strip()
        para_6 = random.choice(lines).strip()
        para_7 = random.choice(lines).strip()
            


    #Generate "Namibian" names

    with open("firstnames.txt") as names:
        fnames = names.readlines()
    first_Name = random.choice(fnames)
    first_Name = first_Name.strip()

    with open("lastnames.txt") as names:
        lnames = names.readlines()
    last_Name = random.choice(lnames)
    last_Name = last_Name.strip()

    Hero = first_Name + " " + last_Name

    
    #Dictionary for modify .docx

    context = {"p_box": p_box ,
               "loc_id": loc_id,
               "today_date": today_date,
               "RE": RE,
               "para_1":para_1,
               "para_2":para_2,
               "para_3":para_3,
               "para_4":para_4,
               "para_5":para_5,
               "para_6":para_6,
               "para_7":para_7,
               "Hero":Hero}

    

    doc_Name = "Letter_Temp.docx"

    doc = DocxTemplate(doc_Name)

    doc.render(context)

    hn = random.choice([RE,Hero])
    if hn == RE:
        gn = Hero
    if hn == Hero:
        gn = RE
        
    
    doc.save("Cause Letters/" +hn+"-"+gn+ ".docx")

    

        
        
        



