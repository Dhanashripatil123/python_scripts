distance=11


if distance < 3:
   mode="walk"
elif distance <= 15:
   mode="bike"
elif distance > 15:
   mode="car"

print(mode)      
