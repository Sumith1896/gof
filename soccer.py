import random
import math

global minute, goals, matchReport, fouls, yellowCards, redCards, offsides, shots, tactics

minutes = range(91)
matchReport = "The match has begun"+ "\n"

teamname_att = "Barca"  
teamname_def = "ManU"

strength_att = {"forwards": 1, "defenders": 1, "goalkeeper": 2}

strength_def = {"forwards": 2, "defenders": 2, "goalkeeper": 3}

tactics = {teamname_att:[2, 2, 2, 2, 2, 2], teamname_def:[2, 2, 2, 2, 2, 2]}

goals = {teamname_att: 0, teamname_def: 0}
fouls = {teamname_att: 0, teamname_def: 0}
yellowCards = {teamname_att: 0, teamname_def: 0}
redCards = {teamname_att: 0, teamname_def: 0}
offsides = {teamname_att: 0, teamname_def: 0}
shots = {teamname_att: 0, teamname_def: 0}


def tactics_weight(val):
    newval = val*0.1+0.8
    return newval

def strengths_weight(val):
    newval = math.log10(val+1)+0.35
    return newval

def Chance_Percent(chance, universe = 100):
    chance = abs(int(chance));
    universe = abs(int(universe));
    if random.randint(1, universe) <= chance:
        return True;  
    return False;


def simulate_attack(teamname_att, teamname_def, strength_att, strength_def):
    #These variables contain the match report
    global minute, goals, matchReport, fouls, yellowCards, redCards, offsides, shots, tactics
    #input values: attacker's name, defender's name, 
    #   attacker's strength array, defender's strength array

    #players' strength values vary from 0.1 to 9.9
    
    matchReport =  matchReport+" "+str(minute) + ": "+teamname_att+" attacks"+ "\n"
    offense_strength = strength_att["forwards"]/strength_def["defenders"]
    defense_strength = strength_def["defenders"]/strength_att["forwards"]
    if Chance_Percent(50*offense_strength*tactics_weight(tactics[teamname_att][1])/tactics_weight(tactics[teamname_att][2])):
        #attacking team passes 1st third of opponent's field side
        matchReport = matchReport+" "+teamname_def+" advance"+ "\n"
        
        if Chance_Percent(25*tactics_weight(tactics[teamname_def][5])):
            #the defending team fouls the attacking team
            fouls[teamname_def]+=1
            matchReport = matchReport+" "+teamname_def+' foul'+ "\n"
            
            if Chance_Percent(43):
                #yellow card for the defending team
                yellowCards[teamname_def]+=1
                matchReport = matchReport+" "+teamname_def+" yellow"+ "\n"
    
            elif Chance_Percent(3):
                #red card for the defending team
                redCards[teamname_def]+=1
                matchReport = matchReport+" "+teamname_def+" red"+ "\n"
            
            #indirect free kick
            matchReport = matchReport+" "+teamname_att+" iFreeKick"+ "\n"
            
            if Chance_Percent(25*strengths_weight(strength_att["forwards"])):
                #shot at the goal
                shots[teamname_att]+=1
                matchReport = matchReport+" "+teamname_att+" iFreeKick_shot"+ "\n"
                
                if Chance_Percent(25/strengths_weight(strength_def["goalkeeper"])):
                    #attacking team scores
                    goals[teamname_att]+=1
                    matchReport = matchReport+" "+teamname_att+" shot score:GOAL"+ "\n"
                
                else:
                    #defending goalkeeper saves
                    matchReport = matchReport+" "+teamname_def+" iFreeKick shot saved"+ "\n"
                
            else:
                #defending team cleares the ball
                matchReport = matchReport+" "+teamname_def+" iFreeKick clear"+ "\n"
            

        elif Chance_Percent(17*tactics_weight(tactics[teamname_att][2])):
            #attacking team is caught offside
            offsides[teamname_att]+=1
            matchReport = matchReport+" "+teamname_def+" offside"+ "\n"
        
        else:
            #attack isn't interrupted
            #attack passes the 2nd third of the opponent's field side - good chance
            matchReport = matchReport+" "+teamname_def+" advance further"+ "\n"
            
            if Chance_Percent(25*tactics_weight(tactics[teamname_def][5])):
                #the defending team fouls the attacking team
                fouls[teamname_def]+=1
                matchReport = matchReport+" "+teamname_def+" foul"+ "\n"
            
                if Chance_Percent(43):
                    #yellow card for the defending team
                    yellowCards[teamname_def]+=1
                    matchReport = matchReport+" "+teamname_def+" yellow"+ "\n"
                
                elif Chance_Percent(3):
                    #red card for the defending team
                    redCards[teamname_def]+=1
                    matchReport = matchReport+" "+teamname_def+" red"+ "\n"
                
                if Chance_Percent(19):
                    #penalty for the attacking team
                    shots[teamname_att]+=1
                    matchReport = matchReport+" "+teamname_att+" penalty"+ "\n"
                    
                    if Chance_Percent(77): 
                        #attacking team scores
                        goals[teamname_att]+=1
                        matchReport = matchReport+" "+teamname_att+" shot score:GOAL"+ "\n"
                    
                    elif Chance_Percent(50):
                        #shot misses the goal
                        matchReport = matchReport+" "+teamname_att+" penalty miss"+ "\n"
                    
                    else:
                        #defending goalkeeper saves
                        matchReport = matchReport+" "+teamname_def+" penalty save"+ "\n"
                    
                else:
                    #direct free kick
                    matchReport = matchReport+" "+teamname_att+" dFreeKick"+ "\n"
                    if Chance_Percent(33*strengths_weight(strength_att["forwards"])):
                        #shot at the goal
                        shots[teamname_att]+=1
                        matchReport = matchReport+" "+teamname_att+" dFreeKick shot"+ "\n"
                        
                        if Chance_Percent(33/strengths_weight(strength_def["goalkeeper"])):
                            #attacking team scores
                            goals[teamname_att]+=1
                            matchReport = matchReport+" "+teamname_att+" shot score:GOAL"+ "\n"
                        
                        else:
                            #defending goalkeeper saves
                            matchReport = matchReport+" "+teamname_def+" dFreeKick shot save"+ "\n"
                        
                    else:
                        #defending team cleares the ball
                        matchReport = matchReport+" "+teamname_def+" dFreeKick clear"+ "\n"
            
            elif Chance_Percent(62*strengths_weight(strength_att["forwards"])*tactics_weight(tactics[teamname_att][2])*tactics_weight(tactics[teamname_att][3])):
                #shot at the goal
                shots[teamname_att]+=1
                matchReport = matchReport+" "+teamname_att+" shot"+ "\n"
                
                if Chance_Percent(30/strengths_weight(strength_def["goalkeeper"])):
                    #the attacking team scores
                    goals[teamname_att]+=1
                    matchReport = matchReport+" "+teamname_att+" shot score:GOAL"+ "\n"
                
                else:
                    if Chance_Percent(50):
                        #the defending defenders block the shot
                        matchReport = matchReport+" "+teamname_def+" shot block"+ "\n"
                    
                    else:
                        #the defending goalkeeper saves
                        matchReport = matchReport+" "+teamname_def+" shot save"+ "\n"
                    
            else:
                #attack is stopped
                matchReport = matchReport+" "+teamname_def+" stopped'"+ "\n"
                if Chance_Percent(15*defense_strength*tactics_weight(tactics[teamname_att][1])*tactics_weight(tactics[teamname_att][3])*tactics_weight(tactics[teamname_def][4])):
                    #quick counter attack - playing on the break
                    strength_att["defenders"] = strength_att["defenders"]*0.8 #weaken the current attacking team's defense
                    matchReport = matchReport+" "+teamname_def+" quick Counter Attack"+ "\n"
                    matchReport = matchReport+"Goals-"+teamname_att+"-"+str(goals[teamname_att])+':'+teamname_def+"-"+str(goals[teamname_def]) + "\n"
                    return simulate_attack(teamname_def, teamname_att, strength_def, strength_att) #new attack - this one is finished
                
    #attacking team doesn't pass 1st third of opponent's field side
    elif Chance_Percent(15*defense_strength*tactics_weight(tactics[teamname_att][1])*tactics_weight(tactics[teamname_att][3])*tactics_weight(tactics[teamname_def][4])):
        #attack is stopped
        #quick counter attack - playing on the break
        matchReport = matchReport + " "+teamname_def+" stopped"+ "\n"
        strength_att["defenders"] = strength_att["defenders"]*0.8 #weaken the current attacking team's defense
        matchReport = matchReport+" "+teamname_def+" quick Counter Attack"+ "\n"
        matchReport = matchReport+"Goals-"+teamname_att+"-"+str(goals[teamname_att])+':'+teamname_def+"-"+str(goals[teamname_def]) + "\n"
        return simulate_attack(teamname_def, teamname_att, strength_def, strength_att) #new attack - this one is finished

    else:
        #ball goes into touch - out of the field
        matchReport = matchReport+" "+teamname_def+" throwIn"+ "\n"
        if Chance_Percent(33):
            #if a new chance is created
            if Chance_Percent(50):
                #throw-in for the attacking team
                matchReport = matchReport+" "+teamname_def+" throwIn att"+ "\n"
                matchReport = matchReport+"Goals-"+teamname_att+"-"+str(goals[teamname_att])+':'+teamname_def+"-"+str(goals[teamname_def]) + "\n"
                return simulate_attack(teamname_att, teamname_def, strength_att, strength_def); #new attack - this one is finished
            
            else:
                #throw-in for the defending team
                matchReport = matchReport+" "+teamname_def+" throwIn def"+ "\n"
                matchReport = matchReport+"Goals-"+teamname_att+"-"+str(goals[teamname_att])+':'+teamname_def+"-"+str(goals[teamname_def]) + "\n"
                return simulate_attack(teamname_def, teamname_att, strength_def, strength_att); #new attack - this one is finished
            
    matchReport = matchReport+"Goals-"+teamname_att+"-"+str(goals[teamname_att])+':'+teamname_def+"-"+str(goals[teamname_def]) + "\n"
    return True # finish the attack

for minute in minutes:
    simulate_attack(teamname_att, teamname_def, strength_att, strength_def)

print matchReport
