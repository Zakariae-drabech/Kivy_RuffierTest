''' Module for calculating the results of Ruffier tests.


The sum of the three tries at pulse readings (before strain, right after strain, and after a short break)
ideally, there should be no more than 200 beats per minute.
We propose that the children measure their pulse for 15 seconds,
and find the result of beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result is from the ideal 200 beats, the worse it is.
Traditionally, tables are given by values divided by 10.


Ruffier index  
   IR = (S - 200) / 10
is evaluated corresponding to age according to the table:
---------------|-------------------------------------------------------------------------------------------------------
               |  7–8             9–10                11–12             13–14               15+ (only for adolescents!)
---------------|-------------------------------------------------------------------------------------------------------                
perfect        |  6.4 and below   4.9 and below       3.4 and below     1.9 and below       0.4 and below
good           |  6.5–11.9        5–10.4              3.5–8.9           2–7.4               0.5–5.9
satisfactory   |  12–16.9         10.5–15.4           9–13.9            7.5–12.4            6–10.9
weak           |  17–20.9         15.5–19.4           14–17.9           12.5–16.4           11–14.9
unsatisfactory | 21 and above    19.5 and above      18 and above      16.5 and above      15 and above


the result “unsatisfactory” is 4 from the result “weak” for all ages,
“weak” is separated from “satisfactory” by 5, and “good” from “satisfactory” by 5.5


so we will write a function ruffier_result(r_index, level) which will produce
the calculated Ruffier index and level “unsatisfactory” for the tested age, and produce a result

'''

# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = 'there is no data for that age'

txt_res1 = "low. See your doctor right away!"
txt_res2 = "satisfactory. See your doctor!"
txt_res3 = "average. It may be worth seeing your doctor to get checked out."
txt_res4 = "above average"
txt_res5 = "high"

def ruffier_index(P1, P2, P3):
   ''' it returns the index value according to the three pulse calculations for comparison with the table'''
   return (4 * (P1+P2+P3) - 200) / 10

def test(P1, P2, P3, age):
    ''' this function can be used from outside the module for calculating the Ruffier index.
    We return the ready texts that just need to be written in the necessary place
    We use the constants used at the beginning of this module for texts. '''

    if age < 7:
        return txt_index + "0 \n" +txt_nodata # this is a mystery beyond this test
    
    index = ruffier_index(P1,P2,P3)

    if  age == 7 or  age == 8:
        if index >= 21:
            result= txt_res1
        elif index < 21 and index >= 17:
            result= txt_res2
        elif index < 17 and index >= 12:
            result= txt_res3
        elif index < 12 and index >= 6.5:
            result= txt_res4
        else:
            result= txt_res5
    if  age == 9 or  age == 10:
        if index >= 19.5:
            result= txt_res1
        elif index < 19.5 and index >= 15.5:
            result= txt_res2
        elif index < 15.5 and index >= 10.5:
            result= txt_res3
        elif index < 10.5 and index >= 5:
            result= txt_res4
        else:
            result= txt_res5
    if  age == 11 or  age == 12:
        if index >= 18:
            result= txt_res1
        elif index < 18 and index >= 14:
            result= txt_res2
        elif index < 14 and index >= 9:
            result= txt_res3
        elif index < 9 and index >= 3.5:
            result= txt_res4
        else:
            result= txt_res5
    if  age == 13 or  age == 14:
        if index >= 16.5:
            result= txt_res1
        elif index < 16.5 and index >= 12.5:
            result= txt_res2
        elif index < 12.5 and index >= 7.5:
            result= txt_res3
        elif index < 7.5 and index >= 2:
            result= txt_res4
        else:
            result= txt_res5
    if  age >= 15:
        if index >= 15:
            result= txt_res1
        elif index < 15 and index >= 11:
            result= txt_res2
        elif index < 11 and index >= 6:
            result= txt_res3
        elif index < 6 and index >= 0.5:
            result= txt_res4
        else:
            result= txt_res5

    return txt_index + str(index) + '\n' + txt_workheart + result

