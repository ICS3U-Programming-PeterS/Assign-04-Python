#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: December 1, 2022
# This program asks the user if they want to calculate for an angle or decimal
# It then asks if they want to use sin, cos, tan, csc, sec or cot

import math
import os

# function to calculate sin(x)
def cal_sin(x_float):
    # change variable to make it easier to code
    x = x_float

    # convert from degrees to radians
    x = x * (math.pi / 180)

    # set t and sum to equal x
    t = x
    sin = x

    # for loop to calculate the value of sin using the sine series
    for i in range(1, 11, 1):
        t = (t * (-1) * x * x) / (2 * i * (2 * i + 1))
        sin = sin + t

    # return sum aka. what sin(x) is equal to
    return sin


# function to calculate cos(x)
def cal_cosine(x_float):
    # declare variables
    cosine = 0
    t = 1

    # if statement for values 270 or 90 because the program won't calculate 0
    if x_float == 270:
        return cosine
    elif x_float == 90:
        return cosine
    else:
        # declare variables
        cosine = 1
        x = x_float

        # change from degrees to radians
        x = x * math.pi / 180

        # for loop to calculate the value of Cosine using cosine series
        for i in range(1, 11, 1):
            t = t * (-1) * x * x / (2 * i * (2 * i - 1))
            cosine = cosine + t

        return cosine


# function that calculates for tan(x)
def cal_tangent(x_float):
    # calculate tangent using return values of sin(x) and cos(x)
    # tan(x) = sin(x) / cos(x)
    tangent = cal_sin(x_float) / cal_cosine(x_float)

    # return the value of tangent
    return tangent


# function that calculates for csc(x)
def cal_cosecant(x_float):
    # calculates cosecant using return value of sin(x)
    # csc(x) = 1 / sin(x)
    cosecant = 1 / cal_sin(x_float)

    # return the value of cosecant
    return cosecant


# function that calculates sec(x)
def cal_secant(x_float):
    # calculates secant using return value of cos(x)
    # sec(x) = 1 / cos(x)
    secant = 1 / cal_cosine(x_float)

    # return the value of secant
    return secant


# function that calculates cot(x)
def cal_cotangent(x_float):
    # calculates cotangent using the return vales of sin(x) and cos(x)
    # cot(x) = cos(x) / sin(x)
    cotangent = cal_cosine(x_float) / cal_sin(x_float)

    # return the value of cotangent
    return cotangent


# function that calculates inverse of sin (arcsin(x))
def degree_to_ang_sin(x_float):
    # angle = arcsin(x) in radians
    angle = math.asin(x_float)

    # converts arcsin(x) in radians to arcsin(x) in degrees
    sin_angle = angle * (180 / math.pi)

    # returns sin_angle in degrees
    return sin_angle


# function that calculates inverse of cos (arccos(x))
def degree_to_ang_cos(x_float):
    # angle = arccos(x) in radians
    angle = math.acos(x_float)

    # converts arccos(x) in radians to arccos(x) in degrees
    cos_angle = angle * (180 / math.pi)

    # returns cos_angle in degrees
    return cos_angle


# function that calculates inverse of tan (arctan(x))
def degree_to_ang_tan(x_float):
    # angle = arctan(x) in radians
    angle = math.atan(x_float)

    # converts arctan(x) in radians to arctan(x) in degrees
    tan_angle = angle * (180 / math.pi)

    # returns tan_angle in degrees
    return tan_angle


# function that calculates inverse of csc (arccsc(x))
def degree_to_ang_csc(x_float):
    # angle = arccsc(x) in radians
    # arccsc(x) = arcsin(1 / x)
    x = 1 / x_float
    angle = math.asin(x)

    # converts arccsc(x) in radians to arccsc(x) in degrees
    csc_angle = angle * (180 / math.pi)

    # returns csc_angle in degrees
    return csc_angle


# function that calculates inverse of sec (arcsec(x))
def degree_to_ang_sec(x_float):
    # angle = arcsec(x) in radians
    # arcsec(x) = arccos(1 / x)
    x = 1 / x_float
    angle = math.acos(x)

    # converts arcsec(x) in radians to arcsec(x) in degrees
    sec_angle = angle * (180 / math.pi)

    # return sec_angle in degrees
    return sec_angle


# function that calculates inverse of cot (arccot(x))
def degree_to_ang_cot(x_float):
    # angle = arccot(x) in radians
    # arccot(x) = arctan(1 / x)
    x = 1 / x_float
    angle = math.atan(x)

    # converts arccot(x) in radians to arccot(x) in degrees
    cot_angle = angle * (180 / math.pi)

    # return cot_angle in degrees
    return cot_angle


# main function does input and output and checks erroneous data
def main():
    # set replay to equal "y"
    replay = "y"

    # while loop to loop until user says to stop
    while replay == "y":
        # set operation check to false
        operation_check = False

        # while loop for when operation check is false
        while operation_check == False:
            os.system("clear")
            # display the options
            print("Choose from one of the following:")
            print(
                "\t [1]"
                " Solve for Sine \n \t [2] Solve for Cosine"
                " \n \t"
                + " [3] Solve for Tangent \n \t "
                + "[4] Solve for Cosecant \n \t "
                + "[5] Solve for Secant \n \t "
                + "[6] Solve for Cotangent"
            )
            operation = input("Enter your selection: ")
            # try catch to check if input is between 1 and 6
            try:
                check = int(operation)

                # set operation_check to true if it is between 1 and 6
                if check >= 1 and check <= 6:
                    operation_check = True

                # set it to false for everything else
                else:
                    operation_check = False
            # set it to false if it isn't a number
            except ValueError:
                operation_check = False

        # get ang_or_dec to determine what user is solving for
        ang_or_dec = input("Do you want to find an angle or decimal place (A/D): ")
        print()

        # if statement if ang_or_dec is A/a
        if ang_or_dec == "a" or ang_or_dec == "A":
            # get input for x_string
            x_string = input("Enter what you want to calculate: ")

            # try catch to check x is float
            try:
                x_float = float(x_string)
                if x_float != 0:
                    # solve sine for angle
                    if check == 1:
                        # make sure input is from 1 to -1
                        if x_float < 1 and x_float > -1:
                            # assign sine to the function return
                            sine = degree_to_ang_sin(x_float)
                            print(
                                "The value of sin({0:.2f}) = {1}".format(sine, x_float)
                            )

                        # erroneous data
                        else:
                            print(
                                "What you enter must be less than 1 and greater than -1."
                            )

                    # solve cosine for angle
                    if check == 2:
                        # make sure input is from 1 to -1
                        if x_float < 1 and x_float > -1:
                            # assign cosine to the function return
                            cosine = degree_to_ang_cos(x_float)
                            print(
                                "The value of cos({0:.2f}) = {1}".format(
                                    cosine, x_float
                                )
                            )

                        # erroneous data
                        else:
                            print(
                                "What you enter must be less than 1 and greater than -1."
                            )

                    # solve tangent for angle
                    if check == 3:
                        # assign tangent to the function return
                        tangent = degree_to_ang_tan(x_float)
                        print(
                            "The value of tan({0:.2f}) = {1}".format(tangent, x_float)
                        )

                    # solve cosecant for angle
                    if check == 4:
                        # assign cosecant to the function return
                        cosecant = degree_to_ang_csc(x_float)
                        print(
                            "The value of csc({0:.2f}) = {1}".format(cosecant, x_float)
                        )

                    # solve secant for angle
                    if check == 5:
                        # assign secant to the function return
                        secant = degree_to_ang_sec(x_float)
                        print("The value of sec({0:.2f}) = {1}".format(secant, x_float))

                    # solve cotangent for angle
                    if check == 6:
                        # assign cotangent to the function return
                        cotangent = degree_to_ang_cot(x_float)
                        print(
                            "The value of cot({0:.2f}) = {1}".format(cotangent, x_float)
                        )
                else:
                    print("Your number cannot be zero.")

            # erroneous data
            except:
                print("{} isn't a real number.".format(x_string))

        elif ang_or_dec == "d" or ang_or_dec == "D":
            # get x_string from the user
            x_string = input("Enter the value of x (in degrees): ")

            # try catch to check x is float
            try:
                x_float = float(x_string)
                # solve sine for decimal
                if check == 1:
                    # make sure x_float is less than 360
                    if x_float < 360:
                        # assign sin to the function return
                        sin = cal_sin(x_float)
                        print("The value of sin({0}) = {1:.4f}".format(x_float, sin))

                    # erroneous data
                    else:
                        print("The angle you enter must be less than 360.")

                # solve cosine for decimal
                elif check == 2:
                    # make sure x_float is less than 360
                    if x_float < 360:
                        # assign cosine to the function return
                        cosine = cal_cosine(x_float)
                        print("The value of cos({0}) = {1:.4f}".format(x_float, cosine))

                    # erroneous data
                    else:
                        print("The angle you enter must be less than 360.")

                # solve tangent for decimal
                elif check == 3:
                    # make sure x_float is less than 360
                    if x_float < 360:
                        # assign tangent to the function return
                        tangent = cal_tangent(x_float)
                        print(
                            "The value of tan({0}) = {1:.4f}".format(x_float, tangent)
                        )

                    # erroneous data
                    else:
                        print("The angle you enter must be less than 360.")

                # solve cosecant for decimal
                elif check == 4:
                    # make sure x_float is less than 360
                    if x_float < 360:
                        # assign cosecant to the function return
                        cosecant = cal_cosecant(x_float)
                        print(
                            "The value of csc({0}) = {1:.4f}".format(x_float, cosecant)
                        )

                    # erroneous data
                    else:
                        print("The angle you enter must be less than 360.")

                # solve secant for decimal
                elif check == 5:
                    # make sure x_float is less than 360
                    if x_float < 360:
                        # assign secant to the function return
                        secant = cal_secant(x_float)
                        print("The value of sec({0}) = {1:.4f}".format(x_float, secant))

                    # erroneous data
                    else:
                        print("The angle you enter must be less than 360.")

                # solve cotangent for decimal
                elif check == 6:
                    # make sure x_float is less than 360
                    if x_float < 360:
                        # assign cotangent to the function return
                        cotangent = cal_cotangent(x_float)
                        print(
                            "The value of cot({0}) = {1:.4f}".format(x_float, cotangent)
                        )

                    # erroneous data
                    else:
                        print("The angle you enter must be less than 360.")

            # erroneous data
            except:
                print("Enter in a real number.")

        # erroneous data
        else:
            continue

        print()
        # get replay to see if user still wants to use again
        replay = input("Do you want to play again (y/n)? ")

        # if replay still = y
        if replay == "y":
            continue
        else:
            break


if __name__ == "__main__":
    main()
