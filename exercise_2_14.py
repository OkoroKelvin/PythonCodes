user_age = int(input("Input your age"))
maximum_heart_rate = 220 - user_age
target_heart_range_1 = maximum_heart_rate * (50 / 100)
target_heart_range_2 = maximum_heart_rate * (85 / 100)

print("Your maximum heart rate is: ", maximum_heart_rate)
print("Your target heart rate is between", str(target_heart_range_1)+" - "+str(target_heart_range_2))
