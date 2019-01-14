                    ##Eapa Choudhury
                    ##Midterm Part II

import statistics

weight_credit_score = .45
weight_salary = .35
weight_job_history = .2


def credit(equifax, transunion, experian):
    scores = [equifax, transunion, experian]
    average = statistics.mean(scores)
    deviation_equifax = ((equifax - average)/equifax) * 100
    deviation_transunion = ((transunion - average)/transunion) * 100
    deviation_experian = ((experian - average)/experian) * 100
    if deviation_equifax >= -5:
        scores.remove(equifax)
    if deviation_transunion >= -5:
        scores.remove(transunion)
    if deviation_experian >= -5:
        scores.remove(experian)
    real_score = statistics.mean(scores)
    if real_score > 850:
        score = 100
    elif (real_score > 800) and (real_score < 850):
        score = 80
    elif (real_score > 750) and (real_score <800):
        score = 60
    elif (real_score > 700) and (real_score < 750):
        score = 40
    else:
        score = 20
    weighted_score_credit = score * weight_credit_score
    return weighted_score_credit


def salary(income):
    if income > 200000:
        score = 100
    elif (income > 150000) and (income < 200000):
        score = 80
    elif (income > 100000) and (income < 150000):
        score = 60
    elif (income > 100000) and (income < 50000):
        score = 40
    else:
        score = 20
    weighted_score_salary = score * weight_salary
    return weighted_score_salary


def job(years_at_current, career_length):
    job_ratio = float(years_at_current/career_length)
    if (years_at_current > 3) and (job_ratio > .6):
        score = 100
    elif (years_at_current > 3) and (job_ratio > .5):
        score = 80
    elif (years_at_current > 3) and (job_ratio > .4):
        score = 60
    elif (years_at_current > 3) and (job_ratio > .3):
        score = 40
    else:
        score = 20
    weighted_job_score = score * weight_job_history
    return weighted_job_score

credit_score = credit(850, 772, 853)
salary_score = salary(117000)
job_score = job(4,8)
total_weighted_score = credit_score + salary_score + job_score
if total_weighted_score >= 60:
    print("You are approved for your credit card!")
else:
    print("Sorry, we can't approve you for your credit card at this moment.")


