total_chores = 4 
original_count = total_chores
print(f"you have {original_count}chores to finish today!/n")

completed_count = 0 
chore_num = 1 

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore= "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished;{next_chore}? (yes/no): ")
    if answer =="yes":
        completed_count += 1 
        chore_num+= 1 
        print("Greate job!")
    else:
        print("ok finish it first")

    print("Chores remaining:", total_chores - completed_count)
    print()
print("ALL CHORES COMPLETED!!!!")

print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

# PART 9: Print the final chore checklist summary
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed:", completed_count)
print("Chores Remaining:", total_chores - completed_count)
print("======================================")
