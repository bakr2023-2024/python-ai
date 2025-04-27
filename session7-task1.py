import matplotlib.pyplot as plt
week = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
temperatures = [25,27,23,28,19,20,24]
plt.figure()
plt.plot(week,temperatures,marker='x')
plt.title("temperature variation over a week")
plt.xlabel("Days of the week")
plt.ylabel("Temperature / C")
plt.axis((0,6,0,40))
plt.show()