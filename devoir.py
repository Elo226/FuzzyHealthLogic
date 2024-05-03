#les imports
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def antecedant():
    "Cette fonction est declarees pour les antecedents"
    #glycemie
    glycemie_avant_repas = ctrl.Antecedent(np.arange(75,235,2), 'glycemie_avant_repas')
    glycemie_apres_repas = ctrl.Antecedent(np.arange(90,300,2), 'glycemie_apres_repas')
    #pression
    pression_diastolique = ctrl.Antecedent(np.arange (0,300,2), 'pression_diastolique')
    pression_systolique = ctrl.Antecedent(np.arange (0,200,2), 'pression_systolique')

    return glycemie_avant_repas,glycemie_apres_repas,pression_diastolique,pression_systolique

def consequence():
    """Declaration de la consequence"""
    choix_pression = ctrl.Consequent(np.arange(0, 100, 2), 'choix_pression')
    choix_glycemie = ctrl.Consequent(np.arange(0, 100, 2), 'choix_glycemie')
    return choix_glycemie, choix_pression

def defuzzificationPression(pression):
    if pression>=0 and pression<20:
        return('Normal')
    if pression>=20 and pression<40:
        return('Elevée')
    if pression>=40 and pression<60:
        return('Moderée')
    if pression>=60 and pression<80:
        return('Grave')
    if pression>=80 and pression<100:
        return('Urgence')
    
def defuzzificationGlycemie(gl):
    if gl>=0 and gl<25:
        return('Normal')
    if gl>=25 and gl<50:
        return('Elevée')
    if gl>=50 and gl<75:
        return('Moderée')
    if gl>=75 and gl<100:
        return('Grave')

def reglePression():
    rule1 = ctrl.Rule(pression_systolique ['normal'] & pression_diastolique ['normal'], choix_pression['normal'])
    rule2 = ctrl.Rule(pression_systolique ['eleve'] & pression_diastolique ['eleve'], choix_pression['eleve'])
    rule3 = ctrl.Rule(pression_systolique ['modere'] & pression_diastolique ['modere'], choix_pression['modere'])
    rule4 = ctrl.Rule(pression_systolique ['grave'] & pression_diastolique ['grave'], choix_pression['grave'])
    rule5 = ctrl.Rule(pression_systolique ['urgence'] & pression_diastolique ['urgence'], choix_pression['urgence'])
    return [rule1,rule2,rule3,rule4,rule5]

def regleGly():
    rule1 = ctrl.Rule(glycemie_avant_repas['excellent'] & glycemie_apres_repas['excellent'], choix_glycemie['excellent'])
    rule2= ctrl.Rule(glycemie_avant_repas['bien'] & glycemie_apres_repas['bien'], choix_glycemie['bien'])
    rule3= ctrl.Rule(glycemie_avant_repas['acceptable'] & glycemie_apres_repas['acceptable'], choix_glycemie['acceptable'])
    rule4= ctrl.Rule(glycemie_avant_repas['dangereux'] & glycemie_apres_repas['dangereux'], choix_glycemie['dangereux'])
    return [rule1,rule2,rule3,rule4]

def configurationPression():
    global pression_diastolique,pression_systolique,choix_pression 
    pression_diastolique,pression_systolique = antecedant()[2],antecedant()[3]
    choix_pression= consequence()[1]

    
    pression_diastolique_normal   = fuzz.trapmf(pression_diastolique.universe, [0, 0, 80,81])
    pression_diastolique_eleve   = fuzz.trapmf(pression_diastolique.universe, [0, 0, 80,81])
    pression_diastolique_hypertension_modere   = fuzz.trapmf(pression_diastolique.universe, [78, 80, 89,91])
    pression_diastolique_hypertension_grave   = fuzz.trapmf(pression_diastolique.universe, [89, 91, 300,300])
    pression_diastolique_hypertension_urgence   = fuzz.trapmf(pression_diastolique.universe, [120, 122, 300,300])

    pression_diastolique ['normal'] = pression_diastolique_normal 
    pression_diastolique ['eleve'] = pression_diastolique_eleve 
    pression_diastolique ['modere'] = pression_diastolique_hypertension_modere
    pression_diastolique ['grave'] = pression_diastolique_hypertension_grave
    pression_diastolique ['urgence'] = pression_diastolique_hypertension_urgence


    pression_systolique_normal   = fuzz.trapmf(pression_systolique.universe, [0, 0, 120,120])
    pression_systolique_eleve   = fuzz.trapmf(pression_systolique.universe, [118, 120, 129,131])
    pression_systolique_hypertension_modere   = fuzz.trapmf(pression_systolique.universe, [128, 129, 140,141])
    pression_systolique_hypertension_grave   = fuzz.trapmf(pression_systolique.universe, [139, 140, 200,200])
    pression_systolique_hypertension_urgence   = fuzz.trapmf(pression_systolique.universe, [179, 180, 200,200])

    pression_systolique ['normal'] = pression_systolique_normal 
    pression_systolique ['eleve'] = pression_systolique_eleve 
    pression_systolique ['modere'] = pression_systolique_hypertension_modere
    pression_systolique ['grave'] = pression_systolique_hypertension_grave
    pression_systolique ['urgence'] = pression_systolique_hypertension_urgence

    choix_press_normal = fuzz.trapmf(choix_pression.universe, [0, 0, 19, 19])
    choix_press_eleve = fuzz.trapmf(choix_pression.universe, [20, 20, 39, 39])
    choix_press_modere = fuzz.trapmf(choix_pression.universe, [40, 40, 59, 59])
    choix_press_grave = fuzz.trapmf(choix_pression.universe, [60, 60, 79, 79])
    choix_press_urgence  = fuzz.trapmf(choix_pression.universe, [80, 80, 100, 100])

    choix_pression['normal'] = choix_press_normal
    choix_pression['eleve'] = choix_press_eleve
    choix_pression['modere'] = choix_press_modere
    choix_pression['grave'] = choix_press_grave
    choix_pression ['urgence'] = choix_press_urgence
    
    pression_regles = ctrl.ControlSystem(reglePression())
    choisir = ctrl.ControlSystemSimulation(pression_regles)

    return choisir


def configurationGlycemie():

    global glycemie_avant_repas,glycemie_apres_repas,choix_glycemie
    glycemie_avant_repas,glycemie_apres_repas=antecedant()[0],antecedant()[1]
    choix_glycemie=consequence()[0]


    glycemie_avant_repas_excellent   = fuzz.trapmf(glycemie_avant_repas.universe, [71, 72, 108,109])
    glycemie_avant_repas_bien   = fuzz.trapmf(glycemie_avant_repas.universe, [107, 109, 145,146])
    glycemie_avant_repas_acceptable   = fuzz.trapmf(glycemie_avant_repas.universe, [144, 146, 180,182])
    glycemie_avant_repas_dangereux   = fuzz.trapmf(glycemie_avant_repas.universe, [50, 180, 235,235])

    glycemie_avant_repas['excellent'] = glycemie_avant_repas_excellent
    glycemie_avant_repas['bien'] = glycemie_avant_repas_bien
    glycemie_avant_repas['acceptable'] = glycemie_avant_repas_acceptable
    glycemie_avant_repas['dangereux'] = glycemie_avant_repas_dangereux


    glycemie_apres_repas_excellent   = fuzz.trapmf(glycemie_apres_repas.universe, [88, 90, 126,128])
    glycemie_apres_repas_bien   = fuzz.trapmf(glycemie_apres_repas.universe, [127, 128, 180,182])
    glycemie_apres_repas_acceptable   = fuzz.trapmf(glycemie_apres_repas.universe, [180, 182, 234,236])
    glycemie_apres_repas_dangereux   = fuzz.trapmf(glycemie_apres_repas.universe, [235, 236, 300,300])

  
    glycemie_apres_repas['excellent']= glycemie_apres_repas_excellent
    glycemie_apres_repas['bien']=glycemie_apres_repas_bien
    glycemie_apres_repas['acceptable']= glycemie_apres_repas_acceptable
    glycemie_apres_repas['dangereux']= glycemie_apres_repas_dangereux


    choix_glyc_excellent = fuzz.trapmf(choix_glycemie.universe, [0, 0, 24, 24])
    choix_glyc_bien = fuzz.trapmf(choix_glycemie.universe, [25, 25, 49, 49])
    choix_glyc_acceptable = fuzz.trapmf(choix_glycemie.universe, [50, 50, 74, 74])
    choix_glyc_dangereux = fuzz.trapmf(choix_glycemie.universe, [75, 75, 100, 100])

    choix_glycemie['excellent'] = choix_glyc_excellent
    choix_glycemie['bien'] = choix_glyc_bien
    choix_glycemie['acceptable'] = choix_glyc_acceptable
    choix_glycemie['dangereux'] = choix_glyc_dangereux


    diabete_regles = ctrl.ControlSystem(regleGly())
    choisir = ctrl.ControlSystemSimulation(diabete_regles)
    return choisir


def etatPression(Diastole,Systole,choix):
    try:
        choisir = configurationPression()

        choisir.input['pression_systolique'] = Systole
        choisir.input['pression_diastolique'] = Diastole

        choisir.compute()
        return defuzzificationPression(choisir.output[choix])
    except:
        return None


def etatGlycemie(avant,apres,choix):
    try:
        choisir = configurationGlycemie()
       

        choisir.input['glycemie_avant_repas'] = avant
        choisir.input['glycemie_apres_repas'] = apres

        choisir.compute()
        return defuzzificationGlycemie(choisir.output[choix])
    except:
        return None


