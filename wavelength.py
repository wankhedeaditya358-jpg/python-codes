wavelength = int(input("Enter a wavelength in nm : "))

if (wavelength >= 380 and wavelength <= 449):
    print("Violet")
elif (wavelength >= 450 and wavelength <= 489):
    print("Blue")
elif (wavelength >= 485 and wavelength <= 499):
    print("Cyan")
elif (wavelength >= 500 and wavelength <= 564):
    print("green")
elif (wavelength >= 565 and wavelength <= 589):
    print("yellow")
elif (wavelength >= 590 and wavelength <= 624):
    print("orange")
elif (wavelength >= 625 and wavelength <= 750):
    print("red")
else:
    print("Enter a valid wavelength")