def calcExp(dist, distgoal, calories, floor, floorgoal, step, stepgoal, active, curr_const, const_login):
    con_mult = Constitution(curr_const, const_login)
    strxp = Strength(calories, dist, distgoal) * con_mult
    agixp = Agility(floor, floorgoal, step,stepgoal, active) * con_mult
    willxp = Willpower(dist, distgoal, floor, floorgoal, step, stepgoal, con_mult) * con_mult
    return (strxp, agixp, willxp, con_mult)

def add_exp(curr_str, curr_agil, curr_will, new_str, new_agil,new_will):
    curr_str += new_str
    curr_agil += new_agil
    curr_will += new_will
    return(curr_str, curr_agil, curr_will)

def calcLvl(strxp, agixp, willxp):
    strlvl = level(strxp)
    agilvl = level(agixp)
    willLvl = level(willxp)
    return (strlvl, agilvl, willLvl)


def level(exp):
    base = 1300
    baseincr = 100
    incr = 50
    level = 0
    while(exp> base):
        exp = exp - base
        base += baseincr
        baseincr += incr
        level += 1
        print(base, baseincr, exp)
    return level

#rint(level(6000))

def calculateExtra(did, goal, norm, bonus):
   if did > goal:
        extra = did - goal
        print(extra, did, goal)
        normal = did - extra

        bexp = bonus * extra
        nexp = normal * norm
        print(bexp, nexp)
        return bexp + nexp
   else:
        nexp = norm * did
        return nexp


def Strength(calories, distance, distanceGoal):
    exp = calories
    distxp = calculateExtra(distance, distanceGoal, 300, 350)
    return exp + distxp

#print(Strength(800, 5, 5))


def Agility(floor, floorgoal, steps, stepgoal, activeSum):
    floorxp = calculateExtra(floor, floorgoal, 75, 100)
    print(floorxp)
    stepxp = calculateExtra((steps / 1000), (stepgoal / 1000), 100, 125)
    print(stepxp)
    activexp = activeSum * 15
    print(activexp)
    print(stepxp, floorxp, activexp)
    return floorxp + stepxp + activexp

#print(Agility(9, 10, 10001, 10000, 30))


def Willpower(floor, floorgoal, steps, stepgoal, distance, distancegoal, const_mult):
    sum = 0
    if const_mult > 1.0:
        sum += 500
    if floor > floorgoal:
        sum += 500
    if steps > stepgoal:
        sum += 500
    if distance > distancegoal:
        sum += 500
    if sum == 1500:
        sum += 500
    return sum

def Constitution(curr_const, login_const):
    if curr_const == 1.5:
        return 1.5
    if login_const == 0:
        return 1.0
    if (curr_const >= 1.0 and curr_const < 1.5 and login_const == 1):
        return curr_const + 0.1


#str, agil, will, con = calcExp(4, 5, 800, 11, 10, 11000, 10000, 30, 1.4, 0)

#print(calcLvl(str, agil, con))
